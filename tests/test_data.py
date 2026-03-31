"""
Fixture-based validation tests for the OSCAL LinkML data model.

Fixture layout
--------------
tests/data/valid/
    YAML files that MUST load successfully against the OSCAL schema.  Each
    file is named after the target class (e.g. ``Observation-001.yaml``).
tests/data/invalid/
    YAML files that MUST fail validation.  Each file intentionally omits a
    required field, uses a bad value, or otherwise violates the schema.
tests/data/problem/
    Fixtures that document known model quirks.  They are not part of the
    main parametrized runs; individual tests reference them directly.

All classes are loaded from the unified ``oscal.datamodel.oscal`` module
(generated from ``src/oscal/schema/oscal.yaml`` which imports all sub-schemas).
No separate schema compilation is needed.

Alias workarounds
-----------------
The LinkML Python generator emits ``__post_init__`` code that reads
hyphenated attribute aliases from the object ``__dict__`` (e.g.
``"subject-uuid"``, ``"role-id"``, ``"param-id"``).  Because fixture keys
were migrated to underscores for JSON-schema compatibility, some classes fail
during ``yaml_loader`` instantiation unless the alias key is injected
manually afterwards.  :func:`_validate_schema` contains targeted workarounds
for each affected class.
"""
import json
import os
import glob
from functools import lru_cache
import pytest
from pathlib import Path
import yaml

import oscal.datamodel.oscal
from jsonschema import Draft7Validator
from linkml_runtime.loaders import yaml_loader

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------

DATA_DIR_VALID = Path(__file__).parent / "data" / "valid"
DATA_DIR_INVALID = Path(__file__).parent / "data" / "invalid"
SCHEMA_DIR = Path(__file__).parent.parent / "src" / "oscal" / "schema"
JSONSCHEMA_PATH = Path(__file__).parent.parent / "project" / "jsonschema" / "oscal.schema.json"

# ---------------------------------------------------------------------------
# Parametrize inputs
# ---------------------------------------------------------------------------

# All *.yaml files collected at import time so pytest can parametrize them.
VALID_EXAMPLE_FILES = glob.glob(os.path.join(DATA_DIR_VALID, '*.yaml'))
INVALID_EXAMPLE_FILES = glob.glob(os.path.join(DATA_DIR_INVALID, '*.yaml'))

# Fixture filenames (basename only) that are expected to *pass* the Python
# yaml_loader despite living in the invalid directory.  Add a fixture here
# when it is invalid for a reason the Python model cannot yet enforce (e.g.
# permissive enum semantics).  These fixtures are skipped by
# test_invalid_data_files so the test suite does not give a false failure.
NON_FAILING_INVALID_FIXTURES: set[str] = {
    "AssessmentPlan-bad-last-modified.yaml",
    "CatalogDocument-bad-uuid-only.yaml",
}

# Spot-check cases for the allow-other enum tests.
# Each tuple is (enum_class_name, a_known_valid_value).
ALLOW_OTHER_ENUM_CASES = [
    ("HashAlgorithmEnum", "SHA-256"),
    ("ObservationMethodEnum", "EXAMINE"),
    ("RiskStatusEnum", "open"),
]


# ---------------------------------------------------------------------------
# Validation helper
# ---------------------------------------------------------------------------


def _validate_schema(filepath: str, target_class_name: str):
    """
    Load a YAML fixture against the unified OSCAL model (``oscal.datamodel.oscal``).

    ``yaml_loader.load`` handles the vast majority of fixtures without any
    special treatment.

    Alias fallback
    --------------
    Several generated classes have a ``__post_init__`` that reads hyphenated
    alias keys from the object's ``__dict__`` — e.g. ``"subject-uuid"`` for
    ``SubjectReference``, ``"param-id"`` for ``SetParameter``.  When
    ``yaml_loader`` constructs these objects from underscore-keyed fixture
    data it raises a ``KeyError``.  The except branch below catches that,
    re-parses the YAML manually, and injects the required hyphenated key
    before constructing the top-level object.  Only the classes known to need
    this treatment are handled; all other failures are re-raised.

    I raised upstream issues/PR to address this in Linkml project.

    Affected classes (as of current codegen)
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    * ``Observation``              — ``SubjectReference.subject_uuid``
    * ``Parameter``                — ``ParameterGuideline`` construction
    * ``Risk``                     — ``RelatedObservation.observation_uuid``
    * ``AssessmentPlan``           — ``ResponsibleParty.role_id``
    * ``CatalogDocument``          — ``ResourceLink.href`` inside ``BackMatter``
    """
    target_class = getattr(oscal.datamodel.oscal, target_class_name)

    try:
        return yaml_loader.load(filepath, target_class=target_class)
    except Exception:
        # Work around generated-model alias mismatches observed for select
        # classes in the unified model.
        if target_class_name not in {
            "Observation",
            "Parameter",
            "CatalogDocument",
            "Risk",
            "AssessmentPlan",
            "ControlImplementationSet",
            "ImplementedRequirement",
        }:
            raise

        data = yaml.safe_load(Path(filepath).read_text())

        if target_class_name == "Observation":
            converted = []
            for item in data.get("subjects", []) or []:
                obj = oscal.datamodel.oscal.SubjectReference(**item)
                obj.__dict__["subject-uuid"] = obj.subject_uuid
                converted.append(obj)
            data["subjects"] = converted

        elif target_class_name == "Parameter":
            converted = []
            for item in data.get("guidelines", []) or []:
                converted.append(oscal.datamodel.oscal.ParameterGuideline(**item))
            data["guidelines"] = converted

        elif target_class_name == "Risk":
            converted = []
            for item in data.get("related_observations", []) or []:
                obj = oscal.datamodel.oscal.RelatedObservation(**item)
                obj.__dict__["observation-uuid"] = obj.observation_uuid
                converted.append(obj)
            data["related_observations"] = converted

        elif target_class_name == "AssessmentPlan":
            metadata_data = data.get("metadata", {})
            converted = []
            for item in metadata_data.get("responsible_parties", []) or []:
                obj = oscal.datamodel.oscal.ResponsibleParty(**item)
                obj.__dict__["role-id"] = obj.role_id
                converted.append(obj)
            metadata_data["responsible_parties"] = converted
            data["metadata"] = oscal.datamodel.oscal.Metadata(**metadata_data)

        elif target_class_name == "CatalogDocument":
            catalog_data = data.get("catalog", {})
            back_matter_data = catalog_data.get("back_matter", {})
            converted_resources = []

            for item in back_matter_data.get("resources", []) or []:
                converted_rlinks = []
                for rlink in item.get("rlinks", []) or []:
                    obj = oscal.datamodel.oscal.ResourceLink(**rlink)
                    obj.__dict__["href"] = obj.href
                    converted_rlinks.append(obj)

                converted_item = dict(item)
                converted_item["rlinks"] = converted_rlinks
                converted_resources.append(oscal.datamodel.oscal.Resource(**converted_item))

            converted_catalog = dict(catalog_data)
            converted_catalog["back_matter"] = oscal.datamodel.oscal.BackMatter(
                resources=converted_resources
            )
            data["catalog"] = oscal.datamodel.oscal.Catalog(**converted_catalog)

        elif target_class_name == "ControlImplementationSet":
            converted = []
            for item in data.get("set_parameters", []) or []:
                obj = oscal.datamodel.oscal.SetParameter(**item)
                obj.__dict__["param-id"] = obj.param_id
                converted.append(obj)
            data["set_parameters"] = converted

        elif target_class_name == "ImplementedRequirement":
            converted = []
            for item in data.get("statements", []) or []:
                obj = oscal.datamodel.oscal.ImplementedControlStatement(**item)
                obj.__dict__["statement-id"] = obj.statement_id
                converted.append(obj)
            data["statements"] = converted

        return target_class(**data)


@lru_cache(maxsize=1)
def _load_generated_json_schema():
    """Load the generated unified JSON Schema used for schema-level validation tests."""
    return json.loads(JSONSCHEMA_PATH.read_text())


@lru_cache(maxsize=None)
def _jsonschema_validator(target_class_name: str):
    """Build a class-specific validator from the generated unified JSON Schema defs."""
    schema = _load_generated_json_schema()
    subschema = dict(schema["$defs"][target_class_name])
    subschema["$schema"] = schema["$schema"]
    subschema["$defs"] = schema["$defs"]
    return Draft7Validator(subschema)


def _validate_generated_json_schema(filepath: str, target_class_name: str):
    """Validate one fixture against the generated JSON Schema definition for its target class."""
    instance = yaml.safe_load(Path(filepath).read_text())
    return sorted(
        _jsonschema_validator(target_class_name).iter_errors(instance),
        key=lambda error: tuple(error.path),
    )


# ---------------------------------------------------------------------------
# Enum helpers
# ---------------------------------------------------------------------------

@lru_cache(maxsize=1)
def _load_schema_enum_index():
    """
    Build an index of all enum definitions found across the OSCAL schema files.

    Returns a ``{enum_name: enum_definition_dict}`` mapping.  The definition
    dict is the raw YAML structure from the relevant schema file, containing
    keys such as ``permissible_values`` and ``annotations``.

    The result is cached because it reads and parses every schema file in
    :data:`SCHEMA_DIR`.
    """
    enum_index = {}
    for schema_file in SCHEMA_DIR.glob("*.yaml"):
        schema_data = yaml.safe_load(schema_file.read_text()) or {}
        for enum_name, enum_def in (schema_data.get("enums") or {}).items():
            enum_index[enum_name] = enum_def
    return enum_index


@lru_cache(maxsize=1)
def _allow_other_enum_names():
    """
    Return the names of every enum that is annotated ``allow_any: true``.

    OSCAL uses a custom LinkML annotation (``allow_any``) to mark enums that
    should accept values outside the declared permissible set (the
    "allow-other" pattern).  This function discovers them dynamically so that
    new allow-other enums added to the schema are automatically picked up by
    the coverage tests without requiring manual edits here.

    See https://github.com/linkml/linkml/issues/127#issuecomment-4145672661

    Only enums that are also present as a class in ``oscal.datamodel.oscal``
    are included — schema enums without a corresponding Python class cannot be
    exercised in unit tests.
    """
    allow_other_names = []
    for enum_name, enum_def in _load_schema_enum_index().items():
        annotation_value = (enum_def.get("annotations") or {}).get("allow_any")
        if isinstance(annotation_value, dict):
            allow_any = annotation_value.get("value")
        else:
            allow_any = annotation_value

        if allow_any is True and hasattr(oscal.datamodel.oscal, enum_name):
            allow_other_names.append(enum_name)

    return tuple(sorted(allow_other_names))


# ---------------------------------------------------------------------------
# Parametrized fixture tests
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("filepath", VALID_EXAMPLE_FILES)
def test_valid_data_files(filepath):
    """
    Each file in ``tests/data/valid/`` must load without error.

    The target class is inferred from the filename stem before the first
    hyphen (e.g. ``Observation-001.yaml`` → ``Observation``) and loaded
    from the unified ``oscal.datamodel.oscal`` module via
    :func:`_validate_schema`.
    """
    target_class_name = Path(filepath).stem.split("-")[0]
    obj = _validate_schema(filepath, target_class_name)
    assert obj


@pytest.mark.parametrize("filepath", VALID_EXAMPLE_FILES)
def test_valid_data_files_match_generated_json_schema(filepath):
    """
    Valid fixtures should also satisfy the generated JSON Schema.

    This covers pattern- and enum-level constraints that the Python dataclass
    loader may not enforce directly.
    """
    target_class_name = Path(filepath).stem.split("-")[0]
    errors = _validate_generated_json_schema(filepath, target_class_name)
    assert not errors, [error.message for error in errors]


@pytest.mark.parametrize("filepath", INVALID_EXAMPLE_FILES)
def test_invalid_data_files(filepath):
    """
    Each file in ``tests/data/invalid/`` must raise an exception during loading.

    Fixtures listed in :data:`NON_FAILING_INVALID_FIXTURES` are skipped when the
    Python model cannot enforce their particular constraint (e.g. permissive enum
    semantics).  Fixtures whose class is not known to the unified model are
    also skipped with an explanatory message.
    """
    target_class_name = Path(filepath).stem.split("-")[0]

    if hasattr(oscal.datamodel.oscal, target_class_name):
        if Path(filepath).name in NON_FAILING_INVALID_FIXTURES:
            pytest.skip("Fixture is not invalid under current permissive enum semantics")

        tgt_class = getattr(oscal.datamodel.oscal, target_class_name)
        with pytest.raises(Exception):
            yaml_loader.load(filepath, target_class=tgt_class)
        return

    pytest.skip(f"No invalid-data validator configured for {target_class_name}")


@pytest.mark.parametrize("filepath", INVALID_EXAMPLE_FILES)
def test_invalid_data_files_fail_generated_json_schema(filepath):
    """
    Invalid fixtures should fail class-specific generated JSON Schema validation.

    This is the schema-level backstop for pattern, strict-enum, and other
    constraints that are more permissive when loaded through the Python model.
    """
    target_class_name = Path(filepath).stem.split("-")[0]
    errors = _validate_generated_json_schema(filepath, target_class_name)
    assert errors, f"Expected generated JSON Schema errors for {filepath}"


# ---------------------------------------------------------------------------
# Unit tests for the validation helper
# ---------------------------------------------------------------------------


def test_control_implementation_set_alias_conversion(tmp_path):
    """
    Verify that ControlImplementationSet loads correctly from underscore-keyed
    fixture YAML and that ``set_parameters`` items expose ``param_id``.

    The generated ``__post_init__`` previously read ``self.__dict__["param-id"]``
    which required a workaround in :func:`_validate_schema`.  The codegen was
    fixed upstream; ``yaml_loader.load`` now succeeds directly.
    """
    fixture = tmp_path / "ControlImplementationSet-test.yaml"
    fixture.write_text(
        "uuid: 88888888-8888-4888-8888-888888888888\n"
        "source: https://example.com/catalogs/test\n"
        "description: Test control implementation set.\n"
        "set_parameters:\n"
        "  - param_id: p-1\n"
        "    values:\n"
        "      - test-value\n"
        "implemented_requirements:\n"
        "  - uuid: 99999999-9999-4999-8999-999999999999\n"
        "    control_id: ac-1\n"
        "    description: Test requirement.\n"
    )

    obj = _validate_schema(str(fixture), "ControlImplementationSet")

    assert len(obj.set_parameters) == 1
    assert obj.set_parameters[0].param_id == "p-1"


def test_implemented_requirement_alias_conversion(tmp_path):
    """
    Verify that ImplementedRequirement loads correctly from underscore-keyed
    fixture YAML and that ``statements`` items expose ``statement_id``.

    The generated ``__post_init__`` previously read ``self.__dict__["statement-id"]``
    which required a workaround in :func:`_validate_schema`.  The codegen was
    fixed upstream; ``yaml_loader.load`` now succeeds directly.
    """
    fixture = tmp_path / "ImplementedRequirement-test.yaml"
    fixture.write_text(
        "uuid: 66666666-6666-4666-8666-666666666666\n"
        "control_id: ac-1\n"
        "description: Test implemented requirement.\n"
        "statements:\n"
        "  - statement_id: s-1\n"
        "    uuid: 77777777-7777-4777-8777-777777777777\n"
        "    description: Test statement.\n"
    )

    obj = _validate_schema(str(fixture), "ImplementedRequirement")

    assert len(obj.statements) == 1
    assert obj.statements[0].statement_id == "s-1"


# ---------------------------------------------------------------------------
# Allow-other enum tests
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("enum_name,_known_value", ALLOW_OTHER_ENUM_CASES)
def test_allow_other_enum_annotation_present_in_schema(enum_name, _known_value):
    """
    Guard that the ``allow_any: true`` annotation is present in the schema for
    each enum in :data:`ALLOW_OTHER_ENUM_CASES`.

    If this test fails it means the annotation was removed from the source
    schema, a breaking change for any consumer relying on open enum.
    """
    enum_def = _load_schema_enum_index()[enum_name]
    annotation_value = (enum_def.get("annotations") or {}).get("allow_any")
    if isinstance(annotation_value, dict):
        allow_any = annotation_value.get("value")
    else:
        allow_any = annotation_value
    assert allow_any is True


@pytest.mark.parametrize("enum_name,known_value", ALLOW_OTHER_ENUM_CASES)
def test_allow_other_enum_accepts_known_values(enum_name, known_value):
    """
    Sanity-check that well-known declared values still round-trip through the
    generated enum class correctly (``EnumClass(value)`` → ``str`` equals the
    original value string).
    """
    enum_class = getattr(oscal.datamodel.oscal, enum_name)
    enum_value = enum_class(known_value)
    assert str(enum_value) == known_value


@pytest.mark.xfail(reason="Generated EnumDefinitionImpl currently does not honor allow-other for unknown values")
@pytest.mark.parametrize("enum_name,_known_value", ALLOW_OTHER_ENUM_CASES)
def test_allow_other_enum_accepts_unknown_values(enum_name, _known_value):
    """
    Allow-other enums should accept values outside the declared set.

    Marked ``xfail`` because ``EnumDefinitionImpl`` in the current LinkML
    codegen does not yet pass unknown values through; it raises instead.  This
    test documents the *desired* behaviour so that a future LinkML fix can be
    detected and the xfail marker removed.
    """
    enum_class = getattr(oscal.datamodel.oscal, enum_name)
    unknown_value = "custom-nonstandard-enum-value"
    enum_value = enum_class(unknown_value)
    assert str(enum_value) == unknown_value


def test_allow_other_enum_discovery_finds_multiple_enums():
    """
    At least as many allow-other enums exist in the schema as there are entries
    in :data:`ALLOW_OTHER_ENUM_CASES`, confirming that dynamic discovery via
    :func:`_allow_other_enum_names` covers more than the hard-coded spot checks.
    """
    assert len(_allow_other_enum_names()) >= len(ALLOW_OTHER_ENUM_CASES)


@pytest.mark.xfail(
    reason="Generated EnumDefinitionImpl currently does not honor allow-other for unknown values"
)
@pytest.mark.parametrize("enum_name", _allow_other_enum_names())
def test_allow_other_all_discovered_enums_accept_unknown_values(enum_name):
    """
    Broader version of :func:`test_allow_other_enum_accepts_unknown_values`
    that covers every dynamically discovered allow-other enum, not just the
    hard-coded spot-check cases.

    Marked ``xfail`` for the same reason as the spot-check variant.
    """
    enum_class = getattr(oscal.datamodel.oscal, enum_name)
    unknown_value = f"custom-nonstandard-{enum_name.lower()}"
    enum_value = enum_class(unknown_value)
    assert str(enum_value) == unknown_value


# ---------------------------------------------------------------------------
# Documented quirks / known-behaviour tests
# ---------------------------------------------------------------------------

def test_observation_bad_enum_fixture_loads_with_string_typed_methods():
    """
    The Python model accepts any string for ``Observation.methods``.

    ``ObservationMethodEnum`` is annotated ``allow_any: true``, but the
    current ``EnumDefinitionImpl`` codegen does not enforce enum membership at
    all — it stores the raw string instead of raising.  This means an
    Observation with ``methods: [INVALID_METHOD]`` passes ``yaml_loader`` even
    though ``INVALID_METHOD`` is not a declared permissible value.

    See https://github.com/linkml/linkml/issues/127#issuecomment-4145672661

    This test lives in ``tests/data/problem/invalid/`` (not in
    ``tests/data/invalid/``) because it documents a *known limitation* rather
    than a correctly enforced schema constraint.  It will need to be updated
    once LinkML honours the allow-other annotation properly.
    """
    filepath = DATA_DIR_INVALID.parent / "problem" / "invalid" / "Observation-bad-enum.yaml"

    obj = _validate_schema(str(filepath), "Observation")

    assert obj
    assert obj.methods == ["INVALID_METHOD"]
    assert all(isinstance(method, str) for method in obj.methods)
