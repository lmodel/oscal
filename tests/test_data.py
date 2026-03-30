"""Data test."""
import os
import glob
from functools import lru_cache
import pytest
from pathlib import Path
import yaml

import oscal.datamodel.oscal
from linkml.generators.pythongen import PythonGenerator
from linkml_runtime.loaders import yaml_loader

DATA_DIR_VALID = Path(__file__).parent / "data" / "valid"
DATA_DIR_INVALID = Path(__file__).parent / "data" / "invalid"
SCHEMA_DIR = Path(__file__).parent.parent / "src" / "oscal" / "schema"

ASSESSMENT_RESULTS_SCHEMA = SCHEMA_DIR / "oscal_assessment_results.yaml"
COMPONENT_SCHEMA = SCHEMA_DIR / "oscal_component.yaml"
ASSESSMENT_RESULTS_CLASSES = {
    "AssessmentResults",
    "Result",
    "ImportAssessmentPlan",
    "AssessmentLog",
    "AssessmentLogEntry",
    "Attestation",
}
COMPONENT_CLASSES = {
    "ComponentDefinition",
    "ImportComponentDefinition",
    "DefinedComponent",
    "Capability",
    "IncorporatesComponent",
    "ControlImplementationSet",
    "ImplementedRequirement",
    "ImplementedControlStatement",
}

VALID_EXAMPLE_FILES = glob.glob(os.path.join(DATA_DIR_VALID, '*.yaml'))
INVALID_EXAMPLE_FILES = glob.glob(os.path.join(DATA_DIR_INVALID, '*.yaml'))


@lru_cache(maxsize=1)
def _assessment_results_module():
    """Compile the standalone assessment-results schema to Python on demand."""
    return PythonGenerator(
        str(ASSESSMENT_RESULTS_SCHEMA),
        mergeimports=True,
        base_dir=str(ASSESSMENT_RESULTS_SCHEMA.parent),
    ).compile_module()


@lru_cache(maxsize=1)
def _component_module():
    """Compile the standalone component schema to Python on demand."""
    return PythonGenerator(
        str(COMPONENT_SCHEMA),
        mergeimports=True,
        base_dir=str(COMPONENT_SCHEMA.parent),
    ).compile_module()


def _validate_standalone_schema(filepath: str, target_class_name: str):
    """Load fixtures for schemas not included in the default unified model."""
    if target_class_name in ASSESSMENT_RESULTS_CLASSES:
        module = _assessment_results_module()
    elif target_class_name in COMPONENT_CLASSES:
        module = _component_module()
    else:
        raise ValueError(f"Unsupported standalone class: {target_class_name}")

    target_class = getattr(module, target_class_name)

    # Work around generated-model alias mismatch for keyed nested lists in
    # component standalone classes. The generated __post_init__ expects
    # hyphenated identifier keys in object dict access.
    if target_class_name in {"ControlImplementationSet", "ImplementedRequirement"}:
        data = yaml.safe_load(Path(filepath).read_text())

        if target_class_name == "ControlImplementationSet":
            converted = []
            for item in data.get("set_parameters", []) or []:
                obj = module.SetParameter(**item)
                obj.__dict__["param-id"] = obj.param_id
                converted.append(obj)
            data["set_parameters"] = converted

        if target_class_name == "ImplementedRequirement":
            converted = []
            for item in data.get("statements", []) or []:
                obj = module.ImplementedControlStatement(**item)
                obj.__dict__["statement-id"] = obj.statement_id
                converted.append(obj)
            data["statements"] = converted

        return target_class(**data)

    return yaml_loader.load(filepath, target_class=target_class)


@pytest.mark.parametrize("filepath", VALID_EXAMPLE_FILES)
def test_valid_data_files(filepath):
    """Test loading of all valid data files."""
    target_class_name = Path(filepath).stem.split("-")[0]
    if target_class_name in ASSESSMENT_RESULTS_CLASSES or target_class_name in COMPONENT_CLASSES:
        obj = _validate_standalone_schema(filepath, target_class_name)
        assert obj
        return

    tgt_class = getattr(
        oscal.datamodel.oscal,
        target_class_name,
    )
    obj = yaml_loader.load(filepath, target_class=tgt_class)
    assert obj


@pytest.mark.parametrize("filepath", INVALID_EXAMPLE_FILES)
def test_invalid_data_files(filepath):
    """Test that invalid example data fails validation for supported schemas."""
    target_class_name = Path(filepath).stem.split("-")[0]
    if target_class_name in ASSESSMENT_RESULTS_CLASSES or target_class_name in COMPONENT_CLASSES:
        with pytest.raises(Exception):
            _validate_standalone_schema(filepath, target_class_name)
        return

    if hasattr(oscal.datamodel.oscal, target_class_name):
        tgt_class = getattr(
            oscal.datamodel.oscal,
            target_class_name,
        )
        with pytest.raises(Exception):
            yaml_loader.load(filepath, target_class=tgt_class)
        return

    pytest.skip(f"No invalid-data validator configured for {target_class_name}")
