import typer
from rich.console import Console
from rich.panel import Panel

from services.git_service import GitService
from services.llm_service import GoogleLLMService


#instancia de Typer, que manejará nuestra CLI
app = typer.Typer()

# 'rich' para una salida más bonita en la terminal
console = Console()


def generate_commit(git_service: GitService, llm_service: GoogleLLMService):
    """
    Función principal que orquesta la lógica de la aplicación.
    """
    console.print("[yellow]🔍 Analizando cambios en el 'staging area' de Git...[/yellow]")

    # 1. Obtener el diff del servicio de Git
    diff = git_service.get_staged_diff()

    if diff:
        console.print("[green]✅ Cambios encontrados. Generando mensaje de commit con IA...[/green]")

        # 2. Generar el mensaje de commit usando el servicio de LLM
        with console.status("[bold cyan]Pensando...", spinner="dots") as status:
            commit_message = llm_service.generate_commit_message(diff)

        # 3. Mostrar el resultado
        console.print("\n✨ [bold magenta]Mensaje de commit sugerido:[/bold magenta]")
        console.print(Panel(commit_message, border_style="green", expand=True))
    else:
        # El servicio de Git ya imprime un mensaje si no hay diff,
        console.print("[bold red]Operación cancelada.[/bold red]")


@app.command()
def main():
    """
    Herramienta CLI para generar mensajes de commit con IA.
    """
    # --- Inyección de Dependencias ---
    git_service_instance = GitService()
    llm_service_instance = GoogleLLMService()

    # Llamamos a la lógica principal pasándole las dependencias
    generate_commit(git_service_instance, llm_service_instance)


if __name__ == "__main__":
    app()