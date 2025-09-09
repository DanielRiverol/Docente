# ejemplo 1

nombre = input("¿Cuál es tu nombre? ")
edad = int(input("¿Cuál es tu edad? "))
telefono = input("¿Cuál es tu teléfono? ")

nuevo_contacto = {"nombre": nombre, "edad": edad, "telefono": telefono}

print(
    f"""|----Contacto----|
Nombre: {nuevo_contacto["nombre"]}
Edad: {nuevo_contacto["edad"]}
Teléfono: {nuevo_contacto["telefono"]}
|----------------|
"""
)

# ejemplo 2
frutas = {"banana": 1.29, "pera": 0.45, "manzana": 1.85, "kiwi": 2.15}
