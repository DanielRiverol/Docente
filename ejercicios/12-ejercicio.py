# Crea una lista vacía
lista_compras = []

# Pídele al usuario 3 productos
for i in range(3):
    producto = input(f"Ingresa el producto {i + 1}: ")
    # Añade el producto a la lista
    lista_compras.append(producto)

print("\nTu lista de compras es:")
print(lista_compras)

