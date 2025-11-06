import csv
import json
from typing import Dict, List
from rich.console import Console
from rich.panel import Panel
import os

console = Console()

ARCHIVO_ESTUDIANTES = "estudiantes.csv"
ARCHIVO_CURSOS = "cursos.json"
ARCHIVO_REPORTE = "reporte.txt"


def inicializar_archivos() -> None:
    """Crea los archivos necesarios si no existen."""
    # CSV con encabezados
    if not os.path.exists(ARCHIVO_ESTUDIANTES):
        with open(ARCHIVO_ESTUDIANTES, mode="w", newline="", encoding="utf-8") as archivo:
            escritor = csv.writer(archivo)
            escritor.writerow(["id", "nombre"])
        console.print(f"[yellow]Archivo creado:[/yellow] {ARCHIVO_ESTUDIANTES}")

    # JSON vacío
    if not os.path.exists(ARCHIVO_CURSOS):
        with open(ARCHIVO_CURSOS, mode="w", encoding="utf-8") as archivo:
            json.dump([], archivo, indent=4)
        console.print(f"[yellow]Archivo creado:[/yellow] {ARCHIVO_CURSOS}")



def leer_csv(ruta: str) -> Dict[int, str]:
    """Lee un archivo CSV de estudiantes y devuelve un diccionario {id: nombre}."""
    estudiantes = {}
    with open(ruta, mode="r", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            try:
                estudiantes[int(fila["id"])] = fila["nombre"]
            except (ValueError, KeyError):
                continue
    return estudiantes


def leer_json(ruta: str) -> List[Dict]:
    """Lee un archivo JSON con cursos y devuelve una lista de diccionarios."""
    try:
        with open(ruta, mode="r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except json.JSONDecodeError:
        return []


def agregar_estudiante() -> None:
    """Permite agregar un nuevo estudiante al archivo CSV."""
    estudiantes = leer_csv(ARCHIVO_ESTUDIANTES)
    nuevo_id = max(estudiantes.keys(), default=0) + 1
    nombre = input("Nombre del estudiante: ").strip()

    if not nombre:
        console.print("[red]No se puede agregar un nombre vacío.[/red]")
        return

    with open(ARCHIVO_ESTUDIANTES, mode="a", newline="", encoding="utf-8") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow([nuevo_id, nombre])
    console.print(f"[green]Estudiante agregado:[/green] {nombre} (ID: {nuevo_id})")


def agregar_curso() -> None:
    """Permite registrar un curso asociado a un estudiante existente."""
    estudiantes = leer_csv(ARCHIVO_ESTUDIANTES)
    if not estudiantes:
        console.print("[red]No hay estudiantes registrados todavía.[/red]")
        return

    console.print("[bold cyan]Lista de estudiantes:[/bold cyan]")
    for id_, nombre in estudiantes.items():
        console.print(f"  {id_}. {nombre}")

    try:
        id_estudiante = int(input("Ingrese el ID del estudiante: "))
    except ValueError:
        console.print("[red]El ID debe ser un número.[/red]")
        return

    if id_estudiante not in estudiantes:
        console.print("[red]ID no encontrado.[/red]")
        return

    curso = input("Nombre del curso: ").strip()
    if not curso:
        console.print("[red]No se puede agregar un curso vacío.[/red]")
        return

    cursos = leer_json(ARCHIVO_CURSOS)
    cursos.append({"id_estudiante": id_estudiante, "curso": curso})

    with open(ARCHIVO_CURSOS, mode="w", encoding="utf-8") as archivo:
        json.dump(cursos, archivo, indent=4, ensure_ascii=False)

    console.print(f"[green]Curso '{curso}' agregado a {estudiantes[id_estudiante]}.[/green]")



def generar_reporte(estudiantes: Dict[int, str], cursos: List[Dict]) -> str:
    """Combina los datos de estudiantes y cursos para generar un reporte de texto."""
    reporte = ["Reporte de Cursos por Estudiante", "--------------------------------"]

    cursos_por_estudiante = {id_: [] for id_ in estudiantes}
    for registro in cursos:
        id_est = registro.get("id_estudiante")
        curso = registro.get("curso")
        if id_est in cursos_por_estudiante and curso:
            cursos_por_estudiante[id_est].append(curso)

    for id_est, nombre in estudiantes.items():
        reporte.append(f"{nombre}:")
        if cursos_por_estudiante[id_est]:
            for curso in cursos_por_estudiante[id_est]:
                reporte.append(f"  - {curso}")
        else:
            reporte.append("  (Sin cursos registrados)")
        reporte.append("")

    return "\n".join(reporte)


def mostrar_reporte_con_rich(contenido: str) -> None:
    """Muestra el reporte en la consola con estilo usando Rich."""
    console.print(Panel(contenido, title="[bold cyan] Reporte Generado[/bold cyan]", expand=False))


def guardar_reporte(ruta: str, contenido: str) -> None:
    """Guarda el reporte en un archivo de texto."""
    with open(ruta, mode="w", encoding="utf-8") as archivo:
        archivo.write(contenido)
    console.print(f"[green]Reporte guardado en {ruta}[/green]")


def main()-> None:
    inicializar_archivos()

    while True:
        console.print("\n[bold cyan]--- Sistema de Gestión de Cursos ---[/bold cyan]")
        console.print("1. Agregar estudiante")
        console.print("2. Agregar curso")
        console.print("3. Generar reporte")
        console.print("4. Salir")

        opcion = input("\nSelecciona una opción: ")

        if opcion == "1":
            agregar_estudiante()
        elif opcion == "2":
            agregar_curso()
        elif opcion == "3":
            estudiantes = leer_csv(ARCHIVO_ESTUDIANTES)
            cursos = leer_json(ARCHIVO_CURSOS)
            if not estudiantes:
                console.print("[red]No hay estudiantes registrados.[/red]")
                continue
            reporte_texto = generar_reporte(estudiantes, cursos)
            mostrar_reporte_con_rich(reporte_texto)
            guardar_reporte(ARCHIVO_REPORTE, reporte_texto)
        elif opcion == "4":
            console.print("[bold green]¡Hasta luego![/bold green]")
            break
        else:
            console.print("[red]Opción no válida, intenta otra vez.[/red]")


if __name__ == "__main__":
    main()
