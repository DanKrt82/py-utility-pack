''' Command-line entry point '''

import typer
from securify import _warning_, __version__
from rich.console import Console
from rich.markdown import Markdown

console = Console()

app = typer.Typer()


@app.command()
def main():
    console.print(f'securify {__version__} \n\n')
    console.print(Markdown(_warning_), markup=True)
    console.print('\n\n')
