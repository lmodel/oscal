#!/usr/bin/env python3
"""
Wrapper for linkml gen-java that patches one upstream bug.

Bug A — Zero files generated for modular/split schemas (oocodegen.py):
  OOCodeGenerator.create_documents() calls sv.all_classes(imports=False),
  returning only classes defined directly in the root schema file.  For
  schemas like OSCAL where the root file contains only imports and no class
  definitions, this produces an empty list and gen-java silently exits 0
  without writing any files.
  Fix: call schemaview.merge_imports() on the generator's SchemaView after
  construction so that all classes from imported modules are treated as
  part of the root schema before create_documents() is called.

Bug raised upstream.

See project.justfile gen-java-artifact for usage.
"""

import click
from linkml.generators.javagen import JavaGenerator
from linkml._version import __version__
from linkml.utils.generator import shared_arguments
from linkml.utils.deprecation import deprecation_warning
from pathlib import Path


@shared_arguments(JavaGenerator)
@click.option(
    "--output-directory",
    default="output",
    show_default=True,
    help="Output directory for individually generated class files",
)
@click.option("--package", help="Package name where relevant for generated class files")
@click.option(
    "--template-dir",
    type=click.Path(exists=True, file_okay=False, dir_okay=True, path_type=Path),
    help="Directory containing the Jinja2 templates to use",
)
@click.option("--template-variant", help="Use the specified template variant")
@click.option(
    "--template-file",
    help="Optional jinja2 template to use for class generation (takes precedence over --template-dir)",
)
@click.option(
    "--generate-records/--no-generate-records",
    default=False,
    help="Optional Java 17 record implementation (deprecated, use --template-variant=records instead)",
)
@click.option("--extra-template", multiple=True, help="Name of an additional, arbitrary template to use")
@click.option("--visitor", multiple=True, help="Generate a visitor interface for the specified class")
@click.option("--true-enums/--no-true-enums", default=False, help="Treat enums as distinct types rather than strings")
@click.option("--use-aliases/--no-use-aliases", default=False, help="Use aliases when available to name fields")
@click.version_option(__version__, "-V", "--version")
@click.command(name="java")
def cli(
    yamlfile,
    output_directory=None,
    package=None,
    template_dir=None,
    template_variant=None,
    template_file=None,
    generate_records=False,
    head=None,
    emit_metadata=None,
    genmeta=False,
    classvars=True,
    slots=True,
    true_enums=False,
    use_aliases=False,
    extra_template=[],
    visitor=[],
    **args,
):
    """Patched gen-java CLI: merges imports before generating class files."""
    if generate_records:
        template_variant = "records"
    if template_file is not None:
        if template_dir is not None or template_variant is not None:
            import logging
            logging.warning("--template-file will take precedence over --template-dir and --template-variant")

    if "metadata" not in args:
        args["metadata"] = True
    if emit_metadata is not None:
        deprecation_warning("metadata-flag")
        args["metadata"] = emit_metadata
    if head is not None:
        deprecation_warning("metadata-flag")
        args["metadata"] = head

    gen = JavaGenerator(
        yamlfile,
        package=package,
        template_dir=template_dir,
        template_file=template_file,
        genmeta=genmeta,
        gen_classvars=classvars,
        gen_slots=slots,
        true_enums=true_enums,
        use_aliases=use_aliases,
        **args,
    )

    # Bug A fix: merge imports so create_documents() sees all classes, not just
    # those defined directly in the root schema file.
    gen.schemaview.merge_imports()

    gen.serialize(
        output_directory,
        template_variant=template_variant,
        extra_templates=extra_template,
        visitors=visitor,
        **args,
    )


if __name__ == "__main__":
    cli()
