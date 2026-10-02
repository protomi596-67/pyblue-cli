from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt

console = Console()

def main_menu():
    while True:
        console.clear()
        console.print(Panel.fit(
            "[bold cyan]PYBLUE-CLI[/bold cyan]\n[white]Blue Team Automation[/white]",
            border_style="cyan"
        ))
        console.print("\n[1] Registrarse")
        console.print("[2] Login")
        console.print("[3] Ver planes")
        console.print("[4] Salir\n")
        
        choice = Prompt.ask("Selecciona una opción", choices=["1", "2", "3", "4"])
        
        if choice == "1":
            console.print("\n[yellow]Registrarse - Próximamente[/yellow]")
            Prompt.ask("\nPresiona Enter para continuar")
        elif choice == "2":
            console.print("\n[yellow]Login - Próximamente[/yellow]")
            Prompt.ask("\nPresiona Enter para continuar")
        elif choice == "3":
            console.print("\n[yellow]Ver planes - Próximamente[/yellow]")
            Prompt.ask("\nPresiona Enter para continuar")
        elif choice == "4":
            console.print("\n[green]¡Hasta luego![/green]")
            break