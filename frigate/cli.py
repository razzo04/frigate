import click
import frigate.gen
import frigate.pre_commit_hook
from frigate.utils import list_templates


@click.group()
def cli():
    pass


@cli.command()
@click.argument("filename")
@click.option(
    "-o",
    "--output-format",
    "output_format",
    default="markdown",
    help="Output format for the documentation",
    type=click.Choice(list_templates()),
)
@click.option(
    "--no-credits", is_flag=True, default=True, help="Disable the Frigate credits",
)
@click.option(
    "--no-deps", is_flag=True, default=True, help="Do not render dependency values",
)
@click.option(
    "--values-file",
    "values_file",
    default="values.yaml",
    help="Path to values file (default 'values.yaml')",
)
def gen(filename, output_format, no_credits, no_deps, values_file):
    click.echo(
        frigate.gen.gen(filename, output_format, credits=no_credits, deps=no_deps, values_file=values_file)
    )


@cli.command(context_settings=dict(
    ignore_unknown_options=True,
    allow_extra_args=True,
))
@click.option(
    "--artifact",
    default="README.md",
    help="What file to save the documentation as",
)
@click.option(
    "-o",
    "--output-format",
    "output_format",
    default="markdown",
    help="Output format for the documentation",
    type=click.Choice(list_templates()),
)
@click.option(
    "--no-credits",
    is_flag=True,
    default=True,
    help="Disable the Frigate credits",
)
@click.option(
    "--no-deps",
    is_flag=True,
    default=True,
    help="Do not render dependency values",
)
@click.option(
    "--values-file",
    "values_file",
    default="values.yaml",
    help="Path to values file (default 'values.yaml')",
)
def hook(artifact, output_format, no_credits, no_deps, values_file):
    frigate.pre_commit_hook.main(artifact, output_format, credits=no_credits, deps=no_deps, values_file=values_file)
