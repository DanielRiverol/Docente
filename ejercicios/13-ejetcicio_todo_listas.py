tareas = []
while True:
    print("\n--- Gestor de Tareas ---")
    print("1. Añadir tarea")
    print("2. Eliminar tarea")
    print("3. Ver tareas")
    print("4. Salir")

    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        nueva_tarea = input("Ingresa la nueva tarea: ")
        tareas.append(nueva_tarea)
        print("Tarea añadida.")

    elif opcion == "2":
        tarea_a_eliminar = input("Ingresa la tarea que deseas eliminar: ")
        if tarea_a_eliminar in tareas:
            tareas.remove(tarea_a_eliminar)
            print("Tarea eliminada.")
        else:
            print("Esa tarea no existe.")

    elif opcion == "3":
        print("\n--- Tus Tareas ---")
        if not tareas:
            print("No tienes tareas pendientes.")
        else:
            for tarea in tareas:
                print(f"- {tarea}")

    elif opcion == "4":
        print("Saliendo del gestor de tareas. ¡Adiós!")
        break

    else:
        print("Opción no válida. Por favor, elige una opción del menú.")
