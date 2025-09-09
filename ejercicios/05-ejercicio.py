# nota = int(input('Ingresa la nota (1-10): '))
# mensaje = "Tu nota es: "

# if nota >= 9:
#     mensaje += "A"
# elif nota >= 8:
#     mensaje += "B"
# elif nota >= 7:
#     mensaje += "C"
# elif nota >= 6:
#     mensaje += "D"
# else:
#     mensaje += "F"

# print(mensaje)

# mejorado
try:
    nota = int(input("Ingresa la nota (1-10): "))
    mensaje = ""

    if nota >= 1 and nota <= 10:
        if nota >= 9:
            mensaje = "A"
        elif nota >= 8:
            mensaje = "B"
        elif nota >= 7:
            mensaje = "C"
        elif nota >= 6:
            mensaje = "D"
        else:
            mensaje = "F"

        print(mensaje)
    else:
        print("Error: La nota debe ser un número entre 1 y 10.")

except ValueError:
    print("Error: Por favor, ingresa un número válido.")
