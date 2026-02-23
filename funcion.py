#!/usr/bin/env python3

def calcular_total(carrito):    
    if not carrito:
        return 0

    total = 0
    for item in carrito:
        # Validar que existan las claves necesarias
        if 'precio' not in item or 'cantidad' not in item:
            raise ValueError(f"Falta clave en el item: {item}")
        
        precio = item['precio']
        cantidad = item['cantidad']

        # Validar tipos y valores
        if not isinstance(precio, (int, float)) or precio < 0:
            raise ValueError(f"Precio inválido en el item: {item}")
        if not isinstance(cantidad, int) or cantidad < 0:
            raise ValueError(f"Cantidad inválida en el item: {item}")

        total += precio * cantidad

    return total


def mostrar_carrito(carrito):
    """Imprime los productos del carrito con nombre, precio, cantidad y total."""
    if not carrito:
        print("El carrito está vacío.")
        return
    
    print("Carrito de compras:")
    for item in carrito:
        nombre = item.get("nombre", "Producto sin nombre")
        precio = item.get("precio", "N/A")
        cantidad = item.get("cantidad", "N/A")
        print(f"- {nombre}: {cantidad} x {precio}")
    
    try:
        total = calcular_total(carrito)
        print(f"TOTAL: {total}")
    except ValueError as e:
        print(f"Error al calcular total: {e}")


# Ejemplos de uso
carrito_valido = [
    {"nombre": "pan", "precio": 6000, "cantidad": 5},
    {"nombre": "leche", "precio": 8000, "cantidad": 10}
]

carrito_vacio = []

carrito_invalido = [
    {"nombre": "huevos", "precio": "abc", "cantidad": 2}  # precio inválido
]

mostrar_carrito(carrito_valido)
print("\n---\n")
mostrar_carrito(carrito_vacio)
print("\n---\n")
mostrar_carrito(carrito_invalido)

