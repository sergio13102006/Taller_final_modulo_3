import json
import os
from typing import List, Dict, Optional
from rich.console import Console
from rich.table import Table

console = Console()
ARCHIVO_BIBLIOTECA = "biblioteca.json"

def cargar_biblioteca() -> List[Dict[str, Optional[str]]]:
    """
    Carga la lista de libros desde el archivo JSON.
    Si no existe, crea un archivo con algunos libros de ejemplo.
    """
    if not os.path.exists(ARCHIVO_BIBLIOTECA):
        libros_iniciales = [
            {"libro_id": "001", "titulo": "Cien Años de Soledad", "prestado_a": None},
            {"libro_id": "002", "titulo": "Don Quijote de la Mancha", "prestado_a": None},
            {"libro_id": "003", "titulo": "El Principito", "prestado_a": None},
        ]
        guardar_biblioteca(libros_iniciales)
        return libros_iniciales

    with open(ARCHIVO_BIBLIOTECA, "r", encoding="utf-8") as archivo:
        return json.load(archivo)


def guardar_biblioteca(libros: List[Dict[str, Optional[str]]]) -> None:
    """Guarda la lista actualizada de libros en el archivo JSON."""
    with open(ARCHIVO_BIBLIOTECA, "w", encoding="utf-8") as archivo:
        json.dump(libros, archivo, indent=4, ensure_ascii=False)


# -------------------------------
# Funciones principales
# -------------------------------
def prestar_libro(libro_id: str, nombre_aprendiz: str) -> None:
    """Marca un libro como prestado a un aprendiz."""
    libros = cargar_biblioteca()
    for libro in libros:
        if libro["libro_id"] == libro_id:
            if libro["prestado_a"]:
                console.print(f"[red]El libro '{libro['titulo']}' ya está prestado a {libro['prestado_a']}.[/red]")
                return
            libro["prestado_a"] = nombre_aprendiz
            guardar_biblioteca(libros)
            console.print(f"[green]El libro '{libro['titulo']}' ha sido prestado a {nombre_aprendiz}.[/green]")
            return
    console.print("[red]No se encontró el libro con ese ID.[/red]")


def devolver_libro(libro_id: str) -> None:
    """Marca un libro como devuelto (disponible)."""
    libros = cargar_biblioteca()
    for libro in libros:
        if libro["libro_id"] == libro_id:
            if not libro["prestado_a"]:
                console.print(f"[yellow]El libro '{libro['titulo']}' ya estaba disponible.[/yellow]")
                return
            libro["prestado_a"] = None
            guardar_biblioteca(libros)
            console.print(f"[green]El libro '{libro['titulo']}' ha sido devuelto.[/green]")
            return
    console.print("[red]No se encontró el libro con ese ID.[/red]")


def buscar_libro(query: str) -> List[Dict[str, Optional[str]]]:
    """Busca libros por título (insensible a mayúsculas/minúsculas)."""
    libros = cargar_biblioteca()
    resultados = [libro for libro in libros if query.lower() in libro["titulo"].lower()]

    if not resultados:
        console.print("[yellow]No se encontraron libros con ese título.[/yellow]")
    else:
        mostrar_tabla(resultados, "Resultados de la búsqueda")

    return resultados


def ver_libros_prestados() -> List[Dict[str, Optional[str]]]:
    """Muestra todos los libros actualmente prestados."""
    libros = cargar_biblioteca()
    prestados = [libro for libro in libros if libro["prestado_a"]]

    if not prestados:
        console.print("[yellow]No hay libros prestados actualmente.[/yellow]")
    else:
        mostrar_tabla(prestados, "Libros Prestados")

    return prestados


def mostrar_tabla(libros: List[Dict[str, Optional[str]]], titulo: str) -> None:
    """Muestra una tabla formateada con los datos de los libros."""
    tabla = Table(title=titulo)
    tabla.add_column("ID", style="cyan", justify="center")
    tabla.add_column("Título", style="magenta")
    tabla.add_column("Prestado a", style="green")

    for libro in libros:
        prestado_a = libro["prestado_a"] if libro["prestado_a"] else "Disponible"
        tabla.add_row(libro["libro_id"], libro["titulo"], prestado_a)

    console.print(tabla)


# -------------------------------
# Menú principal
# -------------------------------
def main() -> None:
    """Menú principal de la biblioteca."""
    while True:
        console.print("\n[bold cyan]--- Sistema de Biblioteca ---[/bold cyan]")
        console.print("1. Ver todos los libros")
        console.print("2. Ver libros prestados")
        console.print("3. Buscar libro por título")
        console.print("4. Prestar libro")
        console.print("5. Devolver libro")
        console.print("6. Salir")

        opcion = input("\nSelecciona una opción: ").strip()

        if opcion == "1":
            mostrar_tabla(cargar_biblioteca(), "Inventario de Libros")
        elif opcion == "2":
            ver_libros_prestados()
        elif opcion == "3":
            query = input("Ingrese el título o parte del título del libro: ").strip()
            buscar_libro(query)
        elif opcion == "4":
            libro_id = input("ID del libro a prestar: ").strip()
            nombre = input("Nombre del aprendiz: ").strip()
            prestar_libro(libro_id, nombre)
        elif opcion == "5":
            libro_id = input("ID del libro a devolver: ").strip()
            devolver_libro(libro_id)
        elif opcion == "6":
            console.print("[bold green]Hasta luego.[/bold green]")
            break
        else:
            console.print("[red]Opción no válida.[/red]")


if __name__ == "__main__":
    main()
