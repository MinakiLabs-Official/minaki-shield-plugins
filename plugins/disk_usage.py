import click
import psutil

@click.command()
def cli():
    """Display disk usage information."""
    usage = psutil.disk_usage('/')
    click.echo(f"🔍 Checking disk usage...")
    click.echo(f"Disk usage: {usage.percent}%")
