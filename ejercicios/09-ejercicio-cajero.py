# # Variables y configuración inicial
# pin_correcto = 1234
# saldo = 1000
# intentos = 0
# pin_ingresado = 0 # Inicializamos con un valor incorrecto

# # --- Lógica de Ingreso (con 3 intentos) ---
# print("¡Bienvenido al cajero automático!")

# # El bucle se ejecutará mientras el PIN sea incorrecto Y los intentos sean menores a 3
# while pin_ingresado != pin_correcto and intentos < 3:
#     pin_ingresado = int(input("Ingresa tu PIN: "))

#     if pin_ingresado != pin_correcto:
#         intentos += 1
#         print(f"PIN incorrecto. Te quedan {3 - intentos} intentos.")

# # --- Lógica de Operaciones ---
# # Solo continuamos si el PIN fue correcto
# if pin_ingresado == pin_correcto:
#     opcion = ''
#     while opcion != '4': # El bucle se repetirá hasta que la opción sea '4'
#         print("\n--- Menú Principal ---")
#         print("1. Consultar saldo")
#         print("2. Extracción")
#         print("3. Depósito")
#         print("4. Salir")

#         opcion = input("Selecciona una opción del 1 al 4: ")

#         if opcion == '1':
#             print(f"Tu saldo actual es: ${saldo:.2f}")

#         elif opcion == '2':
#             monto_extraccion = float(input("Ingresa el monto a extraer: $"))
#             if monto_extraccion > saldo:
#                 print("Saldo insuficiente.")
#             elif monto_extraccion <= 0:
#                 print("El monto a extraer debe ser mayor a cero.")
#             else:
#                 saldo -= monto_extraccion
#                 print(f"Has extraído ${monto_extraccion:.2f}. Tu nuevo saldo es: ${saldo:.2f}")

#         elif opcion == '3':
#             monto_deposito = float(input("Ingresa el monto a depositar: $"))
#             if monto_deposito <= 0:
#                  print("El monto a depositar debe ser mayor a cero.")
#             else:
#                 saldo += monto_deposito
#                 print(f"Has depositado ${monto_deposito:.2f}. Tu nuevo saldo es: ${saldo:.2f}")

#         elif opcion == '4':
#             print("Gracias por usar nuestro cajero. ¡Hasta la próxima!")

#         else:
#             print("Opción no válida. Por favor, selecciona una opción del 1 al 4.")

# else:
#     print("Has superado el número de intentos. Comunícate con tu banco.")

# V2
'''
Consigna: Simulación de Cajero Automático 🏦

Requisitos de Acceso (PIN)

Validación de PIN: El programa debe solicitar un PIN al usuario para acceder.

Límite de Intentos: Se permiten un máximo de tres (3) intentos.

Bloqueo: Si se exceden los 3 intentos, mostrar: "Comunícate con tu banco." y finalizar.

Requisitos del Menú de Operaciones

Si el acceso es exitoso, el programa debe mostrar y ejecutar las siguientes opciones:
Opción	Descripción
1-Consultar Saldo
2-Extracción
3-Depósito
4-Salir

Flujo: Después de cualquier operación (1, 2 o 3), el programa debe preguntar al usuario si desea realizar otra operación.

Finalización: El programa termina si el usuario selecciona Salir (Opción 4) o si responde negativamente a la pregunta de continuar operando.

Nota: Las operaciones 2 y 3 deben actualizar el saldo y validar las condiciones necesarias (ej. saldo insuficiente).'''

# # Variables y configuración inicial
pin_correcto = 1234
saldo = 1000
intentos = 0
pin_ingresado = 0

# --- Lógica de Ingreso (con 3 intentos) ---
print("¡Bienvenido al cajero automático!")

while pin_ingresado != pin_correcto and intentos < 3:
    pin_ingresado = int(input("Ingresa tu PIN: "))

    if pin_ingresado != pin_correcto:
        intentos += 1
        print(f"PIN incorrecto. Te quedan {3 - intentos} intentos.")

# --- Lógica de Operaciones ---
if pin_ingresado == pin_correcto:
    continuar_operando = True
    while continuar_operando:
        print("\n--- Menú Principal ---")
        print("1. Consultar saldo")
        print("2. Extracción")
        print("3. Depósito")
        print("4. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            print(f"Tu saldo actual es: ${saldo:.2f}")

        elif opcion == "2":
            monto_extraccion = float(input("Ingresa el monto a extraer: $"))
            if monto_extraccion > saldo:
                print("Saldo insuficiente.")
            elif monto_extraccion <= 0:
                print("El monto a extraer debe ser mayor a cero.")
            else:
                saldo -= monto_extraccion
                print(
                    f"Has extraído ${monto_extraccion:.2f}. Tu nuevo saldo es: ${saldo:.2f}"
                )

        elif opcion == "3":
            monto_deposito = float(input("Ingresa el monto a depositar: $"))
            if monto_deposito <= 0:
                print("El monto a depositar debe ser mayor a cero.")
            else:
                saldo += monto_deposito
                print(
                    f"Has depositado ${monto_deposito:.2f}. Tu nuevo saldo es: ${saldo:.2f}"
                )

        elif opcion == "4":
            print("Gracias por usar nuestro cajero. ¡Hasta la próxima!")
            continuar_operando = False  # Cambiamos la variable para salir del bucle

        else:
            print("Opción no válida. Por favor, selecciona una opción del 1 al 4.")

        # Preguntamos si desea continuar, solo si la operación no fue 'Salir'
        if continuar_operando:
            respuesta = input("\n¿Deseas realizar otra operación? (1. Sí / 2. No): ")
            if respuesta == "2":
                print("Gracias por usar nuestro cajero. ¡Hasta la próxima!")
                continuar_operando = False  # Se sale del bucle si la respuesta es '2'
else:
    print("Has superado el número de intentos. Comunícate con tu banco.")
