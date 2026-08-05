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
	import json
	import subprocess
	import tempfile
	from pathlib import Path

	def normalize_keys(value):
		# Native OSCAL JSON uses hyphenated keys; the schema uses underscores.
		if isinstance(value, dict):
			return {k.replace("-", "_"): normalize_keys(v) for k, v in value.items()}
		if isinstance(value, list):
			return [normalize_keys(item) for item in value]
		return value

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
				print(f"[linkml-validate] SKIP {fixture}: no standalone schema mapping")
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
			status = "PASS" if ok == expected_ok else "FAIL"
			expectation = "valid" if expected_ok else "invalid"
			print(f"[linkml-validate] {status} {fixture} ({target_class}, expect {expectation})")
			if ok != expected_ok:
				failures.append((fixture, result.stdout, result.stderr))

	# cncf-ai-benchmarks: *.json files are ComponentDefinitionDocument instances.
	# The fixtures use native OSCAL hyphenated keys, so normalize each one to
	# underscore keys in a temp copy before handing it to linkml-validate.
	# tests/data/cncf-ai-benchmarks/ must all be valid; tests/data/invalid/cncf-ai-benchmarks/
	# are copies with a single fault injected (malformed last-modified timezone) and must fail.
	cncf_schema = schema_map["ComponentDefinition"]
	cncf_dirs = (
		(Path("tests/data/cncf-ai-benchmarks"), True),
		(Path("tests/data/invalid/cncf-ai-benchmarks"), False),
	)
	with tempfile.TemporaryDirectory(prefix="cncf-normalized-") as tmpdir:
		for cncf_dir, expected_ok in cncf_dirs:
			expectation = "valid" if expected_ok else "invalid"
			for fixture in sorted(cncf_dir.glob("*.json")):
				normalized = Path(tmpdir) / fixture.name
				normalized.write_text(
					json.dumps(normalize_keys(json.loads(fixture.read_text())))
				)
				result = subprocess.run(
					[
						"uv",
						"run",
						"linkml-validate",
						"-s",
						cncf_schema,
						"-C",
						"ComponentDefinitionDocument",
						str(normalized),
					],
					capture_output=True,
					text=True,
				)
				ok = result.returncode == 0
				status = "PASS" if ok == expected_ok else "FAIL"
				print(
					f"[linkml-validate] {status} {fixture} "
					f"(ComponentDefinitionDocument, expect {expectation})"
				)
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

# ============== Supplemental generator recipes (beyond gen-project defaults) ==============
# gen-project already covers: graphql, jsonldcontext, jsonld, jsonschema, owl,
# prefixmap, proto, python, shex, shacl, sqlddl, excel, typescript.
# Explicit in main justfile: java (patched here), typescript (dup), owl (dup), pydantic (→ datamodel/).
# The recipes below cover the remaining available generators.
# Run all at once with: just gen-project-extended

# ---- Schema / metadata formats ----

# NOTE: recipe named gen-merged-schema to avoid conflict with CDM's gen-linkml recipe
# Generate a single self-contained merged LinkML YAML with all imports resolved
[group('model development - extended')]
gen-merged-schema:
  mkdir -p {{dest}}/linkml
  uv run gen-linkml --mergeimports -o {{dest}}/linkml/{{schema_name}}.merged.linkml.yaml {{source_schema_path}}

# gen-yaml CLI hits the linkml-runtime 1.11.0 RepresenterError (JsonObj missing SafeDumper representer).
# Use the same patched script as _gen-yaml until linkml-runtime > 1.11.0 lands.
# Generate resolved YAML schema (patched yamlgen)
[group('model development - extended')]
gen-yaml-artifact:
  mkdir -p {{dest}}/yaml
  uv run python scripts/issues/gen_yaml_patched.py {{source_schema_path}} > {{dest}}/yaml/{{schema_name}}.yaml

# Generate SSSOM mapping TSV from schema slot_uri / mappings
[group('model development - extended')]
gen-sssom-artifact:
  mkdir -p {{dest}}/sssom
  uv run gen-sssom --mergeimports -o {{dest}}/sssom/{{schema_name}}.sssom.tsv {{source_schema_path}}

# Generate Python namespace manager for all prefixes in the schema
[group('model development - extended')]
gen-namespaces-artifact:
  mkdir -p {{dest}}/namespaces
  uv run gen-namespaces --mergeimports {{source_schema_path}} > {{dest}}/namespaces/{{schema_name}}.namespaces.py

# Generate TSV summary (classes, slots, counts — useful in spreadsheets)
[group('model development - extended')]
gen-summary-artifact:
  mkdir -p {{dest}}/summary
  uv run gen-summary --mergeimports {{source_schema_path}} > {{dest}}/summary/{{schema_name}}.summary.tsv

# ---- Visualization / diagram formats ----

# Generate a single combined Graphviz DOT graph of the schema
[group('model development - extended')]
gen-graphviz-artifact:
  mkdir -p {{dest}}/graphviz
  uv run gen-graphviz --mergeimports -f dot -o {{dest}}/graphviz/{{schema_name}}.dot {{source_schema_path}}

# Generate per-class Mermaid class diagram Markdown files (one .md per class)
[group('model development - extended')]
gen-mermaid-artifact:
  mkdir -p {{dest}}/mermaid
  uv run gen-mermaid-class-diagram --mergeimports -d {{dest}}/mermaid {{source_schema_path}}

# Generate Mermaid ER diagram (single file, mermaid format)
[group('model development - extended')]
gen-erdiagram-artifact:
  mkdir -p {{dest}}/erdiagram
  uv run gen-erdiagram --mergeimports -f mermaid {{source_schema_path}} > {{dest}}/erdiagram/{{schema_name}}.er.md

# Generate PlantUML diagram (stdout → single file)
[group('model development - extended')]
gen-plantuml-artifact:
  mkdir -p {{dest}}/plantuml
  uv run gen-plantuml --mergeimports {{source_schema_path}} > {{dest}}/plantuml/{{schema_name}}.plantuml

# ---- Data / query formats ----

# gen-rdf embeds ./cdm_*.context.jsonld refs that rdflib resolves against the
# schema @base URL (https://w3id.org/lmodel/…), returning HTTP 404. Patched
# script strips those refs; all prefix bindings are in the merged context.
# Generate RDF/Turtle representation of the schema
[group('model development - extended')]
gen-rdf-artifact:
  mkdir -p {{dest}}/rdf
  uv run python scripts/issues/gen_rdf_patched.py --mergeimports -o {{dest}}/rdf/{{schema_name}}.ttl {{source_schema_path}}

# Generate a directory of SPARQL validation queries (one query per constraint)
[group('model development - extended')]
gen-sparql-artifact:
  mkdir -p {{dest}}/sparql
  uv run gen-sparql --mergeimports -d {{dest}}/sparql {{source_schema_path}}

# Generate CSV data dictionary of classes and slots
[group('model development - extended')]
gen-csv-artifact:
  mkdir -p {{dest}}/csv
  uv run gen-csv --mergeimports {{source_schema_path}} > {{dest}}/csv/{{schema_name}}.csv

# ---- Database formats ----

# Generate DBML (Database Markup Language) for schema visualization tools (DBDiagram etc.)
[group('model development - extended')]
gen-dbml-artifact:
  mkdir -p {{dest}}/dbml
  uv run python3 scripts/issues/gen_dbml_patched.py -s {{source_schema_path}} -o {{dest}}/dbml/{{schema_name}}.dbml

# Generate SQLAlchemy ORM models
[group('model development - extended')]
gen-sqla-artifact:
  mkdir -p {{dest}}/sqla
  uv run gen-sqla --mergeimports {{source_schema_path}} > {{dest}}/sqla/{{schema_name}}_sqlalchemy.py

# Generate SQL validation queries
[group('model development - extended')]
gen-sqlvalidation-artifact:
  mkdir -p {{dest}}/sqlvalidation
  uv run gen-sqlvalidation --mergeimports {{source_schema_path}} > {{dest}}/sqlvalidation/{{schema_name}}.sql

# Generate TerminusDB JSON-LD schema
[group('model development - extended')]
gen-terminusdb-artifact:
  mkdir -p {{dest}}/terminusdb
  uv run gen-terminusdb --mergeimports {{source_schema_path}} > {{dest}}/terminusdb/{{schema_name}}.json

# Generate TypeDB TypeQL schema definitions
[group('model development - extended')]
gen-typedb-artifact:
  mkdir -p {{dest}}/typedb
  uv run gen-typedb --mergeimports {{source_schema_path}} > {{dest}}/typedb/{{schema_name}}.tql

# ---- Language bindings ----

# gen-java in the main justfile calls gen-java without mergeimports, so the root
# schema's classes (all defined in imported subschemas) are invisible and zero
# files are generated.  The patched script calls merge_imports() first.
# Generate Java classes (one .java file per class)
[group('model development - extended')]
gen-java-artifact:
  mkdir -p {{dest}}/java
  uv run python3 scripts/issues/gen_java_patched.py --output-directory {{dest}}/java {{source_schema_path}}

# Generate Go structs (stdout → single file)
[group('model development - extended')]
gen-golang-artifact:
  mkdir -p {{dest}}/golang
  uv run gen-golang --mergeimports {{source_schema_path}} > {{dest}}/golang/{{schema_name}}.go

# Generate Rust crate (directory with Cargo.toml + src/)
[group('model development - extended')]
gen-rust-artifact:
  mkdir -p {{dest}}/rust
  uv run gen-rust --mergeimports --force -o {{dest}}/rust {{source_schema_path}}

# Generate C++17 header file
[group('model development - extended')]
gen-cpp-artifact:
  mkdir -p {{dest}}/cpp
  uv run gen-cpp-header --mergeimports {{source_schema_path}} > {{dest}}/cpp/{{schema_name}}.h

# Generate Pandera dataframe validation schemas
[group('model development - extended')]
gen-pandera-artifact:
  mkdir -p {{dest}}/pandera
  uv run python3 scripts/issues/gen_pandera_patched.py {{source_schema_path}} > {{dest}}/pandera/{{schema_name}}_pandera.py

# Generate Markdown data dictionary (single combined file)
# NOTE Bug 12: gen-markdown-datadict creates a new ERDiagramGenerator (and
# therefore re-loads the full CDM schema) for every one of the 2500+ CDM
# classes, hanging indefinitely.  scripts/issues/gen_markdown_datadict_patched.py
# overrides _generate_class_diagram to cache one ERDiagramGenerator instance.
[group('model development - extended')]
gen-markdown-datadict-artifact:
  mkdir -p {{dest}}/markdown-datadict
  uv run python3 scripts/issues/gen_markdown_datadict_patched.py --mergeimports {{source_schema_path}} > {{dest}}/markdown-datadict/{{schema_name}}.md

# Generate GOLR (SOLR) view configurations (one JSON per class)
[group('model development - extended')]
gen-golr-artifact:
  mkdir -p {{dest}}/golr
  uv run gen-golr-views --mergeimports -d {{dest}}/golr {{source_schema_path}}

# ---- Aggregate ----

# Usage: just gen-project && just gen-project-extended
# Run all supplemental generators (those not already covered by gen-project)
[group('model development - extended')]
gen-project-extended: \
  gen-merged-schema \
  gen-yaml-artifact \
  gen-sssom-artifact \
  gen-namespaces-artifact \
  gen-summary-artifact \
  gen-graphviz-artifact \
  gen-mermaid-artifact \
  gen-erdiagram-artifact \
  gen-plantuml-artifact \
  gen-rdf-artifact \
  gen-sparql-artifact \
  gen-csv-artifact \
  gen-dbml-artifact \
  gen-sqla-artifact \
  gen-sqlvalidation-artifact \
  gen-terminusdb-artifact \
  gen-typedb-artifact \
  gen-java-artifact \
  gen-golang-artifact \
  gen-rust-artifact \
  gen-cpp-artifact \
  gen-pandera-artifact \
  gen-markdown-datadict-artifact \
  gen-golr-artifact
