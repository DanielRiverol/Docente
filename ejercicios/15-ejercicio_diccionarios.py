divisas = {
    "euro": {"nombre": "Euro", "simbolo": "€", "codigo": "EUR"},
    "dolar": {"nombre": "Dólar estadounidense", "simbolo": "$", "codigo": "USD"},
    "yen": {"nombre": "Yen japonés", "simbolo": "¥", "codigo": "JPY"},
    "libra esterlina": {"nombre": "Libra esterlina", "simbolo": "£", "codigo": "GBP"},
    "franco suizo": {"nombre": "Franco suizo", "simbolo": "CHF", "codigo": "CHF"},
    "dolar canadiense": {
        "nombre": "Dólar canadiense",
        "simbolo": "C$",
        "codigo": "CAD",
    },
    "peso mexicano": {"nombre": "Peso mexicano", "simbolo": "MX$", "codigo": "MXN"},
}

# busqueda= input('Ingresa el nombre de la divisa para conocer su símbolo: ')
# for divisa, simbolo in divisas.items():
#     if divisa == busqueda:
#         print(f"{divisa.title()}: {simbolo['simbolo']}")
#         break
# # el else es sobre el for si no se interrumpe el bucle con un break
# else:
#     print('No se encuentra la divisa')
# v2
# Pedimos la búsqueda al usuario
# busqueda = input('Ingresa el nombre o código de la divisa: ').lower()

# # Recorremos cada elemento del diccionario
# for clave, info in divisas.items():
#     # Buscamos si la entrada del usuario está en la clave, el nombre o el código
#     if busqueda in clave or busqueda in info['nombre'].lower() or busqueda in info['codigo'].lower():
#         print("\n--- Divisa Encontrada ---")
#         print(f"Nombre: {info['nombre']}")
#         print(f"Símbolo: {info['simbolo']}")
#         print(f"Código: {info['codigo']}")
#         break  # Si encontramos una coincidencia, salimos del bucle
# else:
#     # Este else solo se ejecuta si el bucle terminó sin encontrar un break
#     print(f"\nLo siento, no se encontró ninguna divisa que coincida con '{busqueda}'.")

# v3

# print("\n--- Buscar una divisa ---")
# busqueda = input('Ingresa el nombre o código de la divisa: ').lower()

# encontrado = False
# for clave, info in divisas.items():
#         # Creamos una lista con todos los valores que queremos buscar
#     valores_a_buscar = [clave, info['nombre'].lower(), info['codigo'].lower()]

#         # Verificamos si la búsqueda del usuario está en alguno de esos valores
#     for valor in valores_a_buscar:
#         if busqueda in valor:
#             print("\n--- Divisa Encontrada ---")
#             print(f"Nombre: {info['nombre']}")
#             print(f"Símbolo: {info['simbolo']}")
#             print(f"Código: {info['codigo']}")
#             encontrado = True
#             break # Salimos del bucle interno

#     if encontrado:
#         break # Salimos del bucle externo

# if not encontrado:
#         print(f"\nLo siento, no se encontró ninguna divisa que coincida con '{busqueda}'.")
# v4
print("\n--- Buscar una divisa ---")
busqueda = input("Ingresa el nombre o código de la divisa: ").lower()

encontrado = False
for clave, info in divisas.items():
    # Comprobamos si la búsqueda está en alguno de los 3 valores
    if any(busqueda in s.lower() for s in [clave, info["nombre"], info["codigo"]]):
        print("\n--- Divisa Encontrada ---")
        print(f"Nombre: {info['nombre']}")
        print(f"Símbolo: {info['simbolo']}")
        print(f"Código: {info['codigo']}")
        encontrado = True
        break

if not encontrado:
    print(f"\nLo siento, no se encontró ninguna divisa que coincida con '{busqueda}'.")
