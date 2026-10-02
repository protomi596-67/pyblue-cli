from setuptools import setup, find_packages

setup(
    name="pyblue-cli",
    version="0.1.0",
    author="Tomi",
    description="Blue Team Automation - Seguridad Defensiva con IA",
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=[
        "typer>=0.12.0",
        "rich>=13.7.0",
        "questionary>=2.0.1",
        "requests>=2.31.0",
    ],
    entry_points={
        "console_scripts": [
            "pyblue-cli=cli.main:app",
        ],
    },
)