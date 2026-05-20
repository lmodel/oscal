#!/usr/bin/env python3
"""
Wrapper for linkml gen-pandera that patches three upstream bugs.

Bug A — No --mergeimports support (panderagen.py):
  gen-pandera does not expose --mergeimports; its DataframeGenerator base class
  (OOCodeGenerator) calls SchemaView without merging imports, so the generated
  code only reflects the root schema's classes and misses all classes defined in
  imported modules.  There is no CLI flag to work around this.
  Fix: programmatically call schemaview.merge_imports() on the generator's
  SchemaView after construction so that all classes from imported modules are
  visible during code generation.

Bug B — ValueError on cyclic class dependencies (dependency_sorter.py):
  DependencySorter._visit raises ValueError when a cycle is detected in the
  class dependency graph:
      raise ValueError(f"Cyclic dependency detected: {cycle_path}")
  CDM has legitimate circular references between classes (e.g.
  BusinessCenters -> BusinessDayAdjustments -> AdjustableDate -> BusinessCenters).
  A topological sort of a cyclic graph is impossible; the generator should break
  the cycle gracefully and continue rather than failing entirely.
  Fix: return instead of raising when a cycle node is encountered, allowing the
  dependency sort to produce a valid (if imperfect) ordering for all classes.

Bug C — AttributeError in map_type when typeof chain leads to None
  (dataframe_generator.py):
  When a TypeDefinition has a URI not present in TYPE_MAP and no typeof fallback
  (e.g. xsd:base64Binary, xsd:nonNegativeInteger, xsd:positiveInteger,
  linkml:DateOrDatetime, shex:iri, shex:nonLiteral), map_type calls
  get_type(t.typeof) with t.typeof=None which returns None, then recursively
  calls map_type(None) which crashes on NoneType.uri.
  Fix: (1) extend TYPE_MAP with common XSD/shex/linkml URIs that appear in
  OSCAL-derived schemas; (2) patch map_type to guard against a None result
  from get_type so it falls back to 'str' rather than crashing.

Bugs raised upstream.

See project.justfile gen-pandera-artifact for usage.
"""

import sys

import click
from linkml.generators.panderagen.dataframe_generator import DataframeGenerator
from linkml.generators.panderagen.dependency_sorter import DependencySorter
from linkml.generators.panderagen.pandera.pandera_dataframe_generator import (
    PanderaDataframeGenerator,
)
from linkml.generators.panderagen.panderagen import DataframeGeneratorCli
from linkml_runtime.linkml_model.meta import TypeDefinition

# ---------------------------------------------------------------------------
# Bug B fix: patch DependencySorter._visit to skip cycles instead of raising
# ---------------------------------------------------------------------------
_orig_visit = DependencySorter._visit


def _patched_visit(self, node, visited, in_progress, result):
    if node in in_progress:
        return  # cycle edge — skip rather than raise ValueError
    return _orig_visit(self, node, visited, in_progress, result)


DependencySorter._visit = _patched_visit

# ---------------------------------------------------------------------------
# Bug C fix: extend TYPE_MAP with missing URI mappings and patch map_type to
# guard against None from get_type() when the typeof chain is exhausted.
# ---------------------------------------------------------------------------
_EXTRA_TYPE_MAP: dict[str, str] = {
    "xsd:base64Binary": "str",
    "xsd:nonNegativeInteger": "int",
    "xsd:positiveInteger": "int",
    "xsd:long": "int",
    "xsd:short": "int",
    "xsd:byte": "int",
    "xsd:unsignedInt": "int",
    "xsd:unsignedLong": "int",
    "xsd:unsignedShort": "int",
    "xsd:unsignedByte": "int",
    "xsd:normalizedString": "str",
    "xsd:token": "str",
    "xsd:language": "str",
    "xsd:Name": "str",
    "xsd:NCName": "str",
    "xsd:ID": "str",
    "xsd:IDREF": "str",
    "xsd:IDREFS": "str",
    "xsd:ENTITIES": "str",
    "xsd:NMTOKEN": "str",
    "xsd:hexBinary": "str",
    "linkml:DateOrDatetime": "str",
    "linkml:Uriorcurie": "str",
    "linkml:Uri": "str",
    "linkml:Curie": "str",
    "shex:iri": "str",
    "shex:nonLiteral": "str",
    "shex:IRI": "str",
    "shex:bnode": "str",
}

_orig_map_type = DataframeGenerator.map_type


def _patched_map_type(self, t: TypeDefinition, required: bool = False) -> str:
    if t is None:
        return "str"
    # Merge extra entries into the instance TYPE_MAP on first call
    for k, v in _EXTRA_TYPE_MAP.items():
        self.TYPE_MAP.setdefault(k, v)
    return _orig_map_type(self, t, required)


DataframeGenerator.map_type = _patched_map_type


@click.command()
@click.argument("yamlfile", type=click.Path(exists=True))
@click.option(
    "--output",
    "-o",
    required=False,
    type=click.Path(dir_okay=False, writable=True),
    help="Output file (default: stdout)",
)
def cli(yamlfile: str, output: str | None) -> None:
    """Patched gen-pandera CLI: merges imports and handles cyclic dependencies."""
    # Bug A fix: create the generator and then merge imports into its SchemaView
    gen = PanderaDataframeGenerator(yamlfile)
    gen.schemaview.merge_imports()

    cli_wrapper = DataframeGeneratorCli(generator=gen)
    code = cli_wrapper.serialize()

    if output:
        with open(output, "w", encoding="utf-8") as f:
            f.write(code)
    else:
        print(code)


if __name__ == "__main__":
    cli()
