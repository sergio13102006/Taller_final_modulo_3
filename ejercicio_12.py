import csv
from typing import Dict
from rich.console import Console
from rich.table import Table
import os

console = Console()
ARCHIVO_CSV = "estudiantes.csv"


def inicializar_archivo() -> None:
    """Crea el archivo CSV si no existe, con encabezados."""
    if not os.path.exists(ARCHIVO_CSV):
        with open(ARCHIVO_CSV, mode="w", newline="", encoding="utf-8") as archivo:
            escritor = csv.writer(archivo)
            escritor.writerow(["nombre", "edad", "calificacion"])
        console.print("[green]Archivo creado correctamente.[/green]")


def agregar_estudiante(nombre: str, edad: int, calificacion: float) -> None:
    """Agrega un nuevo estudiante al archivo CSV."""
    with open(ARCHIVO_CSV, mode="a", newline="", encoding="utf-8") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow([nombre, edad, calificacion])
    console.print(f"[green]Estudiante agregado:[/green] {nombre}, {edad} años, calificación {calificacion}")


def analizar_columna(nombre_columna: str) -> Dict[str, float]:
    """
    Lee el archivo CSV de estudiantes y calcula el promedio, máximo y mínimo
    de la columna numérica especificada.
    Devuelve un diccionario con esos tres valores.
    """
    try:
        with open(ARCHIVO_CSV, mode="r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            valores = []

            for fila in lector:
                try:
                    valor = float(fila[nombre_columna])
                    valores.append(valor)
                except (ValueError, KeyError):
                    continue

        if not valores:
            console.print(f"[red]No se encontraron datos válidos en la columna '{nombre_columna}'.[/red]")
            return {}

        promedio = sum(valores) / len(valores)
        maximo = max(valores)
        minimo = min(valores)

        resultados = {
            "promedio": round(promedio, 2),
            "maximo": maximo,
            "minimo": minimo
        }

        return resultados

    except FileNotFoundError:
        console.print(f"[red]El archivo '{ARCHIVO_CSV}' no existe.[/red]")
        return {}


def mostrar_resultados(resultados: Dict[str, float]) -> None:
    """Muestra los resultados en una tabla usando Rich."""
    if not resultados:
        console.print("[yellow]No hay resultados para mostrar.[/yellow]")
        return

    tabla = Table(title="Análisis de Datos")
    tabla.add_column("Estadística", style="cyan", justify="center")
    tabla.add_column("Valor", style="magenta", justify="center")

    for clave, valor in resultados.items():
        tabla.add_row(clave.capitalize(), str(valor))

    console.print(tabla)


def mostrar_estudiantes() -> None:
    """Muestra todos los estudiantes actuales."""
    try:
        with open(ARCHIVO_CSV, mode="r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            filas = list(lector)

            if not filas:
                console.print("[yellow]No hay estudiantes registrados aún.[/yellow]")
                return

            tabla = Table(title="Lista de Estudiantes")
            tabla.add_column("Nombre", style="cyan")
            tabla.add_column("Edad", style="magenta")
            tabla.add_column("Calificación", style="green")

            for fila in filas:
                tabla.add_row(fila["nombre"], fila["edad"], fila["calificacion"])

            console.print(tabla)

    except FileNotFoundError:
        console.print("[red]No existe el archivo CSV todavía.[/red]")


def main() -> None:
    """Menú principal del programa."""
    inicializar_archivo()

    while True:
        console.print("\n[bold cyan]--- Gestor de Estudiantes ---[/bold cyan]")
        console.print("1. Ver estudiantes")
        console.print("2. Agregar estudiante")
        console.print("3. Analizar columna (edad o calificacion)")
        console.print("4. Salir")

        opcion = input("\nSelecciona una opción: ")

        if opcion == "1":
            mostrar_estudiantes()
        elif opcion == "2":
            nombre = input("Nombre del estudiante: ").strip()
            try:
                edad = int(input("Edad: ").strip())
                calificacion = float(input("Calificación: ").strip())
            except ValueError:
                console.print("[red]Edad y calificación deben ser números.[/red]")
                continue
            agregar_estudiante(nombre, edad, calificacion)
        elif opcion == "3":
            columna = input("Ingresa el nombre de la columna para realizar el promedio (edad/calificacion): ").strip()
            resultados = analizar_columna(columna)
            mostrar_resultados(resultados)
        elif opcion == "4":
            console.print("[bold green]Hasta luego![/bold green]")
            break
        else:
            console.print("[red]Opción no válida, intenta otra vez.[/red]")


if __name__ == "__main__":
    main()
