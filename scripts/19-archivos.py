# Definimos el nombre de nuestro archivo como una constante
ARCHIVO_DE_TAREAS = "tareas.txt"


def agregar_tarea():
    """Pide una tarea al usuario y la guarda en el archivo."""

    print("\n--- 1. Agregar Tarea ---")
    tarea = input("Escribe la nueva tarea: ")

    # Validamos que la tarea no esté vacía
    if not tarea.strip():
        print("Error: La tarea no puede estar vacía.")
        return

    try:
        # Usamos 'a' (append) para AÑADIR al final del archivo.
        # 'encoding="utf-8"' es importante para tildes, ñ, etc.
        with open(ARCHIVO_DE_TAREAS, "a", encoding="utf-8") as f:

            # ¡Importante! Escribimos la tarea Y un salto de línea (\n)
            # para que la próxima tarea se escriba en la línea de abajo.
            f.write(f"{tarea}\n")

        print(f"¡Tarea '{tarea}' agregada con éxito!")

    except Exception as e:
        # Capturamos cualquier error de permisos o de disco
        print(f"Error al guardar la tarea: {e}")


def ver_tareas():
    """Lee y muestra todas las tareas del archivo."""

    print("\n--- 2. Ver Tareas Pendientes ---")

    try:
        # Usamos 'r' (read) para leer el contenido.
        # Si el archivo no existe, esto saltará al 'except'.
        with open(ARCHIVO_DE_TAREAS, "r", encoding="utf-8") as f:

            # Leemos todas las líneas del archivo en una lista
            tareas = f.readlines()

            if not tareas:
                # El archivo existe pero está vacío
                print("(No hay tareas pendientes. ¡Agrega una!)")
            else:
                print("Este es tu listado de tareas:")
                # Usamos 'enumerate' para numerar la lista desde 1
                for i, tarea in enumerate(tareas, 1):
                    # Usamos .strip() para quitar el salto de línea (\n)
                    # que guardamos al escribir, y así evitar doble
                    # espaciado al imprimir.
                    print(f"  {i}. {tarea.strip()}")

    except FileNotFoundError:
        # ¡El Plan B! Si el archivo 'tareas.txt' no existe.
        print("(No hay tareas pendientes. ¡Agrega la primera!)")
    except Exception as e:
        print(f"Error al leer las tareas: {e}")


# -----------------------------------------------------------------
# MENÚ PRINCIPAL
# -----------------------------------------------------------------
if __name__ == "__main__":
    while True:
        print("\n===============================")
        print("    LISTA DE TAREAS v1.0     ")
        print("===============================")
        print("1: Agregar nueva tarea")
        print("2: Ver tareas pendientes")
        print("3: Salir")
        print("-------------------------------")
        opcion = input("Elige una opción (1-3): ")

        if opcion == "1":
            agregar_tarea()
        elif opcion == "2":
            ver_tareas()
        elif opcion == "3":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, elige 1, 2 o 3.")
