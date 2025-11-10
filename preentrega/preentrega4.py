# Lista principal para almacenar los productos: [nombre, categoria, precio]
productos = []

# Bucle principal del programa
while True:
    print("\n" + "=" * 40)
    print("      SISTEMA BÁSICO DE PRODUCTOS")
    print("=" * 40)
    print("1. Agregar producto")
    print("2. Mostrar productos")
    print("3. Buscar producto por nombre")
    print("4. Eliminar producto por posición")
    print("5. Salir")
    print("=" * 40)

    # Lectura de la Opción de Menú
    opcion_str = input("Elige una opción (1-5): ").strip()

    opcion = 0
    # Intentamos convertir a entero para manejar la opción
    if opcion_str.isdigit():
        opcion = int(opcion_str)

    # ---------------------------------
    # 1. AGREGAR PRODUCTO
    # ---------------------------------
    if opcion == 1:
        print("\n--- AGREGAR NUEVO PRODUCTO ---")

        # Validar Nombre (no vacío)
        while True:
            nombre = input("Ingresa el nombre del producto: ").strip()
            if nombre:  # Evalúa como True si la cadena no está vacía
                break
            print("⚠️ Error: El nombre no puede estar vacío.")

        # Validar Categoría (no vacío)
        while True:
            categoria = input("Ingresa la categoría del producto: ").strip()
            if categoria:  # Evalúa como True si la cadena no está vacía
                break
            print("⚠️ Error: La categoría no puede estar vacía.")

        # Validar Precio (Asumimos que es número y validamos solo positivo)
        while True:
            precio_str = input("Ingresa el precio (sin centavos): ").strip()

            # Asumimos que la entrada es un número para simplificar la validación
            if precio_str.isdigit():
                precio = int(precio_str)
                if precio > 0:
                    break
                else:
                    print("⚠️ Error: El precio debe ser un número positivo.")
            else:
                print("⚠️ Error: El precio debe ser un número entero válido.")

        # Añadir producto
        productos.append([nombre, categoria, precio])
        print(f"\n✅ Producto '{nombre}' agregado exitosamente.")

    # ---------------------------------
    # 2. MOSTRAR PRODUCTOS
    # ---------------------------------
    elif opcion == 2:
        print("\n--- PRODUCTOS REGISTRADOS ---")
        if len(productos) == 0:
            print("▶️ No hay productos registrados para mostrar.")
        else:
            print("Nro. | Nombre                 | Categoría            | Precio")
            print("-----|------------------------|----------------------|-------")

            # Bucle for para recorrer la lista por índice
            for i in range(len(productos)):
                p = productos[i]  # p es el producto actual
                # Mostramos la posición como índice + 1
                print(f"{i + 1:<4} | {p[0]:<22} | {p[1]:<20} | ${p[2]}")
            print("----------------------------------------------------------")

    # ---------------------------------
    # 3. BUSCAR PRODUCTO
    # ---------------------------------
    elif opcion == 3:
        print("\n--- BUSCAR PRODUCTO POR NOMBRE ---")
        if len(productos) == 0:
            print("▶️ No hay productos para buscar.")
        else:
            termino = (
                input("Ingresa el nombre o parte del nombre a buscar: ").strip().lower()
            )
            encontrados = 0

            print("\n✅ Coincidencias encontradas:")
            print("Nombre                 | Categoría            | Precio")
            print("-----------------------|----------------------|-------")

            # Bucle for para buscar coincidencias
            for p in productos:
                # Condicional para buscar el término en el nombre del producto (minúsculas)
                if termino in p[0].lower():
                    encontrados = encontrados + 1
                    print(f"{p[0]:<22} | {p[1]:<20} | ${p[2]}")

            if encontrados == 0:
                print(f"❌ No se encontraron productos que contengan '{termino}'.")
                print("----------------------------------------------------------")

    # ---------------------------------
    # 4. ELIMINAR PRODUCTO
    # ---------------------------------
    elif opcion == 4:
        print("\n--- ELIMINAR PRODUCTO ---")
        if len(productos) == 0:
            print("▶️ No hay productos para eliminar.")
        else:
            # Mostrar lista numerada
            print("Productos actuales:")
            for i in range(len(productos)):
                print(f"{i + 1}. {productos[i][0]} (Precio: ${productos[i][2]})")

            # Validar Posición (while True + break)
            while True:
                posicion_str = input(
                    "Ingresa el NÚMERO del producto a eliminar: "
                ).strip()

                # Asumimos que es un dígito y convertimos
                if posicion_str.isdigit():
                    posicion = int(posicion_str)

                    # Verificación de Rango
                    if posicion >= 1 and posicion <= len(productos):
                        break  # ¡ÉXITO!
                    else:
                        print(
                            f"⚠️ Error: El número debe estar entre 1 y {len(productos)}."
                        )
                else:
                    print("⚠️ Error: Ingresa un número de posición válido.")

            # Eliminar usando .pop() basado en el índice (posicion - 1)
            indice_a_eliminar = posicion - 1
            nombre_eliminado = productos[indice_a_eliminar][0]

            productos.pop(indice_a_eliminar)
            print(
                f"\n✅ Producto '{nombre_eliminado}' (Nro. {posicion}) eliminado exitosamente."
            )

    # ---------------------------------
    # 5. SALIR
    # ---------------------------------
    elif opcion == 5:
        print("\n👋 ¡Gracias por usar el Sistema de Productos! ¡Hasta luego!")
        break

    # ---------------------------------
    # Opción Inválida
    # ---------------------------------
    else:
        print("\n❌ Opción no válida. Por favor, ingresa un número del 1 al 5.")
