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
