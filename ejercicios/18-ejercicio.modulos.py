import random


# -----------------------------------------------------------------
# JUEGO 1: ADIVINA EL NÚMERO
# -----------------------------------------------------------------
def jugar_adivina_numero():
    """
    Juego donde el usuario debe adivinar un número secreto
    elegido por la computadora (entre 1 y 100).
    """
    print("\n--- 🎲 Juego: ¡Adivina el Número! ---")
    print("He pensado un número entre 1 y 10. ¿Puedes adivinarlo?")

    # Usamos randint(a, b) para obtener un número entero (incluyendo 1 y 100)
    numero_secreto = random.randint(1, 10)
    intentos = 0
    print(numero_secreto)
    while True:
        intentos += 1
        try:
            # Pedimos el número al usuario
            intento_usuario = int(input(f"Intento #{intentos}: Ingresa tu número: "))

            # Comparamos el intento con el número secreto
            if intentos == 2:
                print("Lo sentimos no adivinaste. El numero era: ", numero_secreto)
                break
            if intento_usuario < numero_secreto:
                print("¡Muy bajo! Intenta con un número más alto.")
            elif intento_usuario > numero_secreto:
                print("¡Muy alto! Intenta con un número más bajo.")
            else:
                # Si acierta, felicitamos y rompemos el bucle
                print(
                    f"\n¡Felicidades! ¡Adivinaste el número {numero_secreto} en {intentos} intentos!"
                )
                break

        except ValueError:
            # Manejo de error si el usuario no escribe un número
            print("Error: Debes ingresar un número entero válido.")


# -----------------------------------------------------------------
# JUEGO 2: SORTEO DE RIFA
# -----------------------------------------------------------------
def sorteo_rifa():
    """
    Simulador de un sorteo de rifa.
    Elige 'k' ganadores únicos de una lista de participantes.
    """
    print("\n--- 🎟️ Script: Sorteo de Rifa ---")

    # ¡Puedes modificar esta lista con los nombres reales!
    participantes = [
        "Ana García",
        "Luis Martínez",
        "Carla Sánchez",
        "David Gómez",
        "Sofía Fernández",
        "Miguel Pérez",
        "Elena Ruiz",
        "Juan Díaz",
        "Laura Jiménez",
        "Pedro Moreno",
    ]

    print(f"Lista de participantes ({len(participantes)} en total):")
    for p in participantes:
        print(f"- {p}")

    try:
        # Preguntar cuántos ganadores
        k = int(input("\n¿Cuántos ganadores deseas sortear? "))

        # Validar que no pidan más ganadores que participantes
        if k > len(participantes):
            print(
                f"Error: No puedes sortear {k} ganadores, solo hay {len(participantes)} participantes."
            )
        elif k <= 0:
            print("Error: Debes sortear al menos 1 ganador.")
        else:
            # Usamos random.sample() para obtener k ganadores ÚNICOS.
            # 'sample' es perfecto para esto porque no repite elementos.
            ganadores = random.sample(participantes, k)

            print("\n¡Sorteando...!")
            print("...")

            if k == 1:
                print(f"¡El ganador es: {ganadores[0]}!")
            else:
                print(f"Los {k} ganadores son:")
                for i, ganador in enumerate(ganadores, 1):
                    print(f"  {i}. {ganador}")

    except ValueError:
        print("Error: Debes ingresar un número válido.")


# -----------------------------------------------------------------
# JUEGO 3: PIEDRA, PAPEL O TIJERA
# -----------------------------------------------------------------
def jugar_piedra_papel_tijera():
    """
    Juego clásico de Piedra, Papel o Tijera contra la computadora.
    """
    print("\n--- ✂️ Juego: Piedra, Papel o Tijera ---")

    # Usamos una lista para que la computadora elija
    opciones = ["piedra", "papel", "tijera"]

    while True:
        # 1. Elección del Usuario
        eleccion_usuario = input(
            "\nElige piedra, papel, o tijera (o 'salir' para terminar): "
        ).lower()

        if eleccion_usuario == "salir":
            print("¡Gracias por jugar! Adiós.")
            break  # Salir del bucle principal

        # 2. Validar la entrada del usuario
        if eleccion_usuario not in opciones:
            print(
                "¡Opción no válida! Por favor, elige solo 'piedra', 'papel' o 'tijera'."
            )
            continue  # Vuelve al inicio del bucle

        # 3. Elección de la Computadora
        # Usamos random.choice() para elegir un elemento al azar de la lista
        eleccion_cpu = random.choice(opciones)

        print(f"\nTú elegiste: {eleccion_usuario}")
        print(f"La computadora eligió: {eleccion_cpu}")

        # 4. Determinar el ganador
        if eleccion_usuario == eleccion_cpu:
            print("¡Es un EMPATE!")
        elif (
            (eleccion_usuario == "piedra" and eleccion_cpu == "tijera")
            or (eleccion_usuario == "papel" and eleccion_cpu == "piedra")
            or (eleccion_usuario == "tijera" and eleccion_cpu == "papel")
        ):
            print("¡Tú GANAS!")
        else:
            print("¡La computadora GANA!")


# -----------------------------------------------------------------
# MENÚ PRINCIPAL PARA EJECUTAR LOS PROGRAMAS
# -----------------------------------------------------------------
# Esta construcción (if __name__ == "__main__":) significa:
# "Ejecuta este código solo si el archivo se está corriendo directamente"
# Es la forma estándar en Python de crear un script ejecutable.

if __name__ == "__main__":
    while True:
        print("\n===============================")
        print("  MENÚ PRINCIPAL DE PROGRAMAS  ")
        print("===============================")
        print("1: Jugar a 'Adivina el Número'")
        print("2: Realizar 'Sorteo de Rifa'")
        print("3: Jugar a 'Piedra, Papel o Tijera'")
        print("4: Salir de la aplicación")
        print("-------------------------------")
        opcion = input("Elige un programa para ejecutar (1-4): ")

        if opcion == "1":
            jugar_adivina_numero()
        elif opcion == "2":
            sorteo_rifa()
        elif opcion == "3":
            jugar_piedra_papel_tijera()
        elif opcion == "4":
            print("¡Gracias por usar los programas! Adiós.")
            break
        else:
            print("Opción no válida. Por favor, elige un número del 1 al 4.")
