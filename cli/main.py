#!/usr/bin/env python3
import typer
from cli.menus.main_menu import main_menu

app = typer.Typer()

@app.command()
def run():
    """PyBlue-CLI - Blue Team Automation"""
    main_menu()

if __name__ == "__main__":
    app()