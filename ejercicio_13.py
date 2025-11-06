import json
from typing import List, Dict
from rich.console import Console
from rich.table import Table
import os

console = Console()
ARCHIVO_JSON = "inventario.json"



def cargar_inventario() -> List[Dict]:
    """Carga el inventario desde un archivo JSON."""
    if not os.path.exists(ARCHIVO_JSON):
        with open(ARCHIVO_JSON, "w", encoding="utf-8") as archivo:
            json.dump([], archivo)
        return []

    try:
        with open(ARCHIVO_JSON, "r", encoding="utf-8") as archivo:
            inventario = json.load(archivo)
            if not isinstance(inventario, list):
                console.print("[red]Formato inválido en el archivo JSON.[/red]")
                return []
            return inventario
    except (json.JSONDecodeError, FileNotFoundError):
        console.print("[red]Error al leer el archivo JSON.[/red]")
        return []


def guardar_inventario(inventario: List[Dict]) -> None:
    """Guarda el inventario actualizado en el archivo JSON."""
    with open(ARCHIVO_JSON, "w", encoding="utf-8") as archivo:
        json.dump(inventario, archivo, indent=4, ensure_ascii=False)
    console.print("[green]Inventario guardado correctamente.[/green]")


# -----------------------------------
# 📦 Funciones de gestión de inventario
# -----------------------------------
def agregar_producto(inventario: List[Dict], nombre: str, cantidad: int, precio: float) -> None:
    """Agrega un nuevo producto al inventario."""
    for item in inventario:
        if item["nombre"].lower() == nombre.lower():
            item["cantidad"] += cantidad
            item["precio"] = precio  # actualiza precio si cambió
            console.print(f"[yellow]Producto existente. Se actualizó cantidad y precio.[/yellow]")
            guardar_inventario(inventario)
            return

    inventario.append({"nombre": nombre, "cantidad": cantidad, "precio": precio})
    guardar_inventario(inventario)
    console.print(f"[green]Producto agregado:[/green] {nombre} (x{cantidad}) - ${precio}")


def vender_producto(inventario: List[Dict], nombre: str, cantidad: int) -> None:
    """Resta cantidad de un producto al realizar una venta."""
    for item in inventario:
        if item["nombre"].lower() == nombre.lower():
            if item["cantidad"] < cantidad:
                console.print(f"[red]No hay suficiente stock de {nombre}.[/red]")
                return
            item["cantidad"] -= cantidad
            guardar_inventario(inventario)
            console.print(f"[green]Venta realizada:[/green] {cantidad} unidades de {nombre}")
            return

    console.print(f"[red]El producto '{nombre}' no existe en el inventario.[/red]")


def mostrar_inventario(inventario: List[Dict]) -> None:
    """Muestra el inventario actual en una tabla con Rich."""
    if not inventario:
        console.print("[yellow]El inventario está vacío.[/yellow]")
        return

    tabla = Table(title="Inventario Actual")
    tabla.add_column("Nombre", style="cyan", justify="center")
    tabla.add_column("Cantidad", style="magenta", justify="center")
    tabla.add_column("Precio", style="green", justify="center")
    tabla.add_column("Valor total", style="bold yellow", justify="center")

    valor_total = 0
    for item in inventario:
        subtotal = item["cantidad"] * item["precio"]
        valor_total += subtotal
        tabla.add_row(
            item["nombre"],
            str(item["cantidad"]),
            f"${item['precio']:.2f}",
            f"${subtotal:.2f}"
        )

    console.print(tabla)
    console.print(f"[bold cyan]Valor total del inventario:[/bold cyan] ${valor_total:.2f}")


def main() -> None:
    inventario = cargar_inventario()

    while True:
        console.print("\n[bold cyan]--- Gestor de Inventario ---[/bold cyan]")
        console.print("1. Ver inventario")
        console.print("2. Agregar producto")
        console.print("3. Vender producto")
        console.print("4. Salir")

        opcion = input("\nSelecciona una opción: ")

        if opcion == "1":
            mostrar_inventario(inventario)
        elif opcion == "2":
            nombre = input("Nombre del producto: ").strip()
            try:
                cantidad = int(input("Cantidad: "))
                precio = float(input("Precio: "))
            except ValueError:
                console.print("[red]Error: cantidad y precio deben ser números.[/red]")
                continue
            agregar_producto(inventario, nombre, cantidad, precio)
        elif opcion == "3":
            nombre = input("Producto a vender: ").strip()
            try:
                cantidad = int(input("Cantidad a vender: "))
            except ValueError:
                console.print("[red]Error: la cantidad debe ser un número entero.[/red]")
                continue
            vender_producto(inventario, nombre, cantidad)
        elif opcion == "4":
            console.print("[bold green]¡Hasta luego![/bold green]")
            break
        else:
            console.print("[red]Opción no válida, intenta de nuevo.[/red]")


if __name__ == "__main__":
    main()
