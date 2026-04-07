## Add your own just recipes here. This is imported by the main justfile.

# Overriding recipes from the root justfile by adding a recipe with the same
# name in this file is not possible until a known issue in just is fixed,
# https://github.com/casey/just/issues/2540

##
## linkml-validate sweep: maps each fixture class to its owning schema,
## and checks valid fixtures (pass) and invalid fixtures (fail).
##
_test-linkml-validate:
	#!{{shebang}}
	import subprocess
	from pathlib import Path

	schema_map = {
		"AssessmentPlan": "src/oscal/schema/oscal_assessment_plan.yaml",
		"AssessmentPlanDocument": "src/oscal/schema/oscal_assessment_plan.yaml",
		"AssessmentResults": "src/oscal/schema/oscal_assessment_results.yaml",
		"BackMatter": "src/oscal/schema/oscal_catalog.yaml",
		"CatalogDocument": "src/oscal/schema/oscal_catalog.yaml",
		"ComponentDefinition": "src/oscal/schema/oscal_component.yaml",
		"Control": "src/oscal/schema/oscal_catalog.yaml",
		"ControlImplementationSet": "src/oscal/schema/oscal_component.yaml",
		"DefinedComponent": "src/oscal/schema/oscal_component.yaml",
		"DocumentId": "src/oscal/schema/oscal_catalog.yaml",
		"Finding": "src/oscal/schema/oscal_assessment_plan.yaml",
		"Group": "src/oscal/schema/oscal_catalog.yaml",
		"Hash": "src/oscal/schema/oscal_catalog.yaml",
		"ImplementedRequirement": "src/oscal/schema/oscal_component.yaml",
		"Link": "src/oscal/schema/oscal_catalog.yaml",
		"Location": "src/oscal/schema/oscal_catalog.yaml",
		"Metadata": "src/oscal/schema/oscal_catalog.yaml",
		"Observation": "src/oscal/schema/oscal_assessment_plan.yaml",
		"Parameter": "src/oscal/schema/oscal_catalog.yaml",
		"Part": "src/oscal/schema/oscal_catalog.yaml",
		"Party": "src/oscal/schema/oscal_catalog.yaml",
		"Property": "src/oscal/schema/oscal_catalog.yaml",
		"Result": "src/oscal/schema/oscal_assessment_results.yaml",
		"Risk": "src/oscal/schema/oscal_assessment_plan.yaml",
		"Role": "src/oscal/schema/oscal_catalog.yaml",
		"SystemComponent": "src/oscal/schema/oscal_component.yaml",
	}

	failures = []
	for subset, expected_ok in (("valid", True), ("invalid", False)):
		for fixture in sorted((Path("tests/data") / subset).glob("*.yaml")):
			target_class = fixture.stem.split("-")[0]
			schema_path = schema_map.get(target_class)
			if schema_path is None:
				print(f"SKIP {fixture}: no standalone schema mapping")
				continue

			result = subprocess.run(
				[
					"uv",
					"run",
					"linkml-validate",
					"-s",
					schema_path,
					"-C",
					target_class,
					str(fixture),
				],
				capture_output=True,
				text=True,
			)
			ok = result.returncode == 0
			if ok != expected_ok:
				failures.append((fixture, result.stdout, result.stderr))

	if failures:
		for fixture, stdout, stderr in failures:
			print(f"VALIDATION MISMATCH: {fixture}")
			if stdout:
				print(stdout)
			if stderr:
				print(stderr)
		raise SystemExit(f"linkml-validate mismatches: {len(failures)}")

# Validate Luigi Carpio's component-definition fixture with structural and
# domain-specific checks derived from the schema and fixture README.
test-luigi-carpio:
	#!/usr/bin/env -S uv run python
	import json
	import os
	import re
	from pathlib import Path
	import oscal.datamodel.oscal as model
	
	def normalize_keys(value):
		if isinstance(value, dict):
			return {
				k.replace("-", "_"): normalize_keys(v)
				for k, v in value.items()
			}
		if isinstance(value, list):
			return [normalize_keys(item) for item in value]
		return value

	fixture = Path("tests/data/luigi_carpio/component-definition.json")

	if not fixture.exists():
		raise SystemExit(f"Missing fixture: {fixture}")

	print(f"[test-luigi-carpio] validating {fixture}")
	strict_uuid = os.getenv("OSCAL_STRICT_UUID", "0").lower() in {"1", "true", "yes", "on"}
	print(f"[test-luigi-carpio] uuid-strict-mode={strict_uuid}")

	raw_instance = json.loads(fixture.read_text())
	instance = normalize_keys(raw_instance)
	obj = model.ComponentDefinitionDocument(**instance)

	def check(name, predicate, detail):
		if not predicate:
			raise SystemExit(f"[test-luigi-carpio] FAIL {name}: {detail}")
		print(f"[test-luigi-carpio] PASS {name}: {detail}")

	def iter_uuid_fields(value, path="<root>"):
		if isinstance(value, dict):
			for key, item in value.items():
				item_path = f"{path}/{key}"
				if key.endswith("uuid") and isinstance(item, str):
					yield item_path, item
				yield from iter_uuid_fields(item, item_path)
		elif isinstance(value, list):
			for i, item in enumerate(value):
				yield from iter_uuid_fields(item, f"{path}/{i}")

	component_definition = instance["component_definition"]
	components = component_definition.get("components") or []
	implemented_requirements = [
		req
		for component in components
		for ci in (component.get("control_implementations") or [])
		for req in (ci.get("implemented_requirements") or [])
	]

	metadata = component_definition.get("metadata") or {}
	last_modified = metadata.get("last_modified", "")
	check(
		"metadata.last_modified",
		bool(re.fullmatch(r"^[0-9]{4}-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9](\\.[0-9]+)?(Z|[+-]([01][0-9]|2[0-3]):[0-5][0-9])$", last_modified)),
		last_modified or "missing",
	)

	check(
		"oscal-key-style",
		"component-definition" in raw_instance,
		"top-level uses hyphenated key",
	)

	fedramp_high_ok = all(
		any(
			prop.get("name") == "fedramp-high" and str(prop.get("value", "")).lower() == "true"
			for prop in (req.get("props") or [])
		)
		for req in implemented_requirements
	)
	check(
		"fedramp-high-prop",
		fedramp_high_ok,
		f"implemented_requirements={len(implemented_requirements)}",
	)

	cjis_delta_count = sum(
		1
		for req in implemented_requirements
		if any(prop.get("name") == "cjis-delta" for prop in (req.get("props") or []))
	)
	check("cjis-delta-present", cjis_delta_count > 0, f"count={cjis_delta_count}")

	check("component-count", len(components) > 0, f"count={len(components)}")

	uuid_pattern = re.compile(r"^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[45][0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$")
	uuid_fields = list(iter_uuid_fields(instance))
	invalid_uuid_fields = [
		(path, value)
		for path, value in uuid_fields
		if not uuid_pattern.fullmatch(value)
	]

	if invalid_uuid_fields:
		sample = ", ".join(
			f"{path}={value}"
			for path, value in invalid_uuid_fields[:3]
		)
		message = (
			"[test-luigi-carpio] WARN uuid-conformance: "
			f"invalid={len(invalid_uuid_fields)}/{len(uuid_fields)} sample=[{sample}]"
		)
		print(message)
		if strict_uuid:
			raise SystemExit(message.replace("WARN", "FAIL"))
	else:
		print(f"[test-luigi-carpio] PASS uuid-conformance: invalid=0/{len(uuid_fields)}")

# Strict variant that fails on UUID quality drift.
test-luigi-carpio-strict:
	OSCAL_STRICT_UUID=1 just test-luigi-carpio
