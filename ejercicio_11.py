from typing import List
from rich.console import Console
from rich.table import Table
console = Console()
archivo_tareas="tarea.txt"

def agregar_tarea(tarea: str) -> None:
    """Agrega una nueva tarea o archivio donde vamso a guardar la informacion"""
    with open(archivo_tareas, "a") as archivo:
        archivo.write(tarea+"\n")
        console.print(f"Archivo agregado [green]{tarea}[/green]*")
def ver_tarea()-> List[str]:
    """Podemos observar las tareas o archivo """
    try:
        with open(archivo_tareas, "r",encoding="utf-8") as archivo:
            tareas = [lineas.strip() for lineas in archivo.readlines()]
    except FileNotFoundError:
        tareas=[]
    return tareas
def mostrar_tarea() -> None:
    """Muestra las tareas en una tabla usando Rich."""
    tareas = ver_tarea()

    if not tareas:
        console.print("[yellow]No hay tareas registradas todavía.[/yellow]")
        return

    tabla = Table(title="Lista de Tareas")
    tabla.add_column("N°", justify="center", style="cyan")
    tabla.add_column("Descripción", style="magenta")

    for i, tarea in enumerate(tareas, start=1):
        tabla.add_row(str(i), tarea)

    console.print(tabla)


def main() -> None:
    """Función principal con el menú del gestor."""
    while True:
        console.print("\n[bold cyan]--- Gestor de Tareas ---[/bold cyan]")
        console.print("1. Ver tareas")
        console.print("2. Agregar tarea")
        console.print("3. Salir")

        opcion = input("\nSelecciona una opción: ")

        if opcion == "1":
            mostrar_tarea()
        elif opcion == "2":
            tarea = input("Escribe la nueva tarea: ").strip()
            if tarea:
                agregar_tarea(tarea)
            else:
                console.print("[red]No puedes agregar una tarea vacía.[/red]")
        elif opcion == "3":
            console.print("[bold green]Hasta luego![/bold green]")
            break
        else:
            console.print("[red]Opción no válida, intenta otra vez.[/red]")


if __name__ == "__main__":
    main()
