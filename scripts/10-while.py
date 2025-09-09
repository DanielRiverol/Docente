"""
while condicion
    instrucciones
"""

# x=0

# while x < 10:
#     x+=1
#     print(x)

# Adivina el numero
# numero_secreto = 7
# adivinanza = 0  # Inicializamos la variable con un valor incorrecto

# while adivinanza != numero_secreto:
#     adivinanza = int(input("Adivina el número secreto (entre 1 y 10): "))

# print("¡Correcto! Adivinaste el número secreto.")

# v2

# numero_secreto = 7
# adivinanza = 0
# contador_intentos = 0

# print("¡Adivina el número secreto entre 1 y 10!")

# while adivinanza != numero_secreto:
#     adivinanza = int(input("Ingresa tu número: "))
#     contador_intentos += 1

#     # Esta es la nueva línea. Si la adivinanza no es la correcta...
#     # if adivinanza != numero_secreto:
#     #     print("¡Incorrecto! Intenta de nuevo.")

# print(f"¡Correcto! Adivinaste el número secreto en {contador_intentos} intentos.")

# Inicio de sesion
contrasena_correcta = "python123"
contrasena_ingresada = ""
intentos_maximos = 3
intentos = 0

while contrasena_ingresada != contrasena_correcta and intentos < intentos_maximos:
    contrasena_ingresada = input("Ingresa la contraseña para acceder: ")
    intentos += 1

    if contrasena_ingresada != contrasena_correcta:
        print(
            f"Contraseña incorrecta. Te quedan {intentos_maximos - intentos} intentos."
        )

if contrasena_ingresada == contrasena_correcta:
    print("¡Acceso concedido! Bienvenido al sistema.")
else:
    print("Has superado el número de intentos. Acceso denegado.")
