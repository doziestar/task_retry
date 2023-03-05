"""Console script for task_retry."""
import sys
import click


@click.command()
def main(args=None):
    """Console script for task_retry."""
    click.echo("Replace this message by putting your code into "
               "task_retry.cli.main")
    click.echo("See click documentation at https://click.palletsprojects.com/")
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
