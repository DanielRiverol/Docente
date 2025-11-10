# Lista principal para almacenar todos los productos.
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

    # Validación de la Opción de Menú (Más concisa)
    opcion_str = input("Elige una opción (1-5): ").strip()

    if opcion_str.isdigit():
        opcion = int(opcion_str)
        if 1 <= opcion <= 5:
            # La opción es válida, continuamos con el bloque de lógica
            pass
        else:
            opcion = 0  # Marcar como inválida si no está en el rango
    else:
        opcion = 0  # Marcar como inválida si no es un dígito

    # ---------------------------------
    # FUNCIONALIDADES DEL SISTEMA
    # ---------------------------------

    if opcion == 1:
        # 1. AGREGAR PRODUCTO
        print("\n--- AGREGAR NUEVO PRODUCTO ---")

        # Validación Simplificada para Nombre (no vacío)
        nombre = ""
        while nombre == "":
            nombre = input("Ingresa el nombre del producto: ").strip()
            if nombre == "":
                print("⚠️ Error: El nombre no puede estar vacío.")

        # Validación Simplificada para Categoría (no vacío)
        categoria = ""
        while categoria == "":
            categoria = input("Ingresa la categoría del producto: ").strip()
            if categoria == "":
                print("⚠️ Error: La categoría no puede estar vacía.")

        # Validación Simplificada para Precio (entero y positivo)
        precio = 0
        while precio <= 0:
            precio_str = input("Ingresa el precio (sin centavos): ").strip()

            if precio_str.isdigit():
                precio_temporal = int(precio_str)
                if precio_temporal > 0:
                    precio = precio_temporal  # Si es válido, se asigna y sale del while
                else:
                    print(
                        "⚠️ Error: El precio debe ser un número positivo mayor a cero."
                    )
            else:
                print("⚠️ Error: El precio debe ser un número entero válido.")

        # Añadir el producto
        productos.append([nombre, categoria, precio])
        print(f"\n✅ Producto '{nombre}' agregado exitosamente.")

    elif opcion == 2:
        # 2. MOSTRAR PRODUCTOS
        print("\n--- PRODUCTOS REGISTRADOS ---")
        if len(productos) == 0:
            print("▶️ No hay productos registrados para mostrar.")
        else:
            print("Nro. | Nombre                 | Categoría            | Precio")
            print("-----|------------------------|----------------------|-------")

            for i in range(len(productos)):
                producto = productos[i]
                numero_producto = i + 1
                nombre = producto[0]
                categoria = producto[1]
                precio = producto[2]

                print(
                    f"{numero_producto:<4} | {nombre:<22} | {categoria:<20} | ${precio}"
                )
            print("----------------------------------------------------------")

    elif opcion == 3:
        # 3. BUSCAR PRODUCTO
        print("\n--- BUSCAR PRODUCTO POR NOMBRE ---")
        if len(productos) == 0:
            print("▶️ No hay productos para buscar.")
        else:
            termino_busqueda = (
                input("Ingresa el nombre o parte del nombre a buscar: ").strip().lower()
            )
            coincidencias_encontradas = 0

            print("\n✅ Se encontraron las siguientes coincidencias:")
            print("Nombre                 | Categoría            | Precio")
            print("-----------------------|----------------------|-------")

            for producto in productos:
                if termino_busqueda in producto[0].lower():
                    coincidencias_encontradas = coincidencias_encontradas + 1

                    nombre = producto[0]
                    categoria = producto[1]
                    precio = producto[2]
                    print(f"{nombre:<22} | {categoria:<20} | ${precio}")

            if coincidencias_encontradas == 0:
                print(
                    f"❌ No se encontraron productos que contengan '{termino_busqueda}'."
                )
                print("----------------------------------------------------------")

    elif opcion == 4:
        # 4. ELIMINAR PRODUCTO
        print("\n--- ELIMINAR PRODUCTO ---")
        if len(productos) == 0:
            print("▶️ No hay productos para eliminar.")
        else:
            # Mostrar productos numerados
            print("Productos actuales:")
            for i in range(len(productos)):
                producto = productos[i]
                print(f"{i + 1}. {producto[0]} (Precio: ${producto[2]})")

            # Validación Simplificada para la Posición
            posicion = 0
            # El bucle while se mantiene mientras la posición no sea válida (<= 0 o fuera de rango)
            while not (1 <= posicion <= len(productos)):
                posicion_str = input(
                    "Ingresa el NÚMERO del producto a eliminar: "
                ).strip()

                if posicion_str.isdigit():
                    posicion_temporal = int(posicion_str)

                    if 1 <= posicion_temporal <= len(productos):
                        posicion = posicion_temporal  # Válido: sale del while
                    else:
                        print(
                            f"⚠️ Error: El número debe estar entre 1 y {len(productos)}."
                        )
                else:
                    print("⚠️ Error: Ingresa un número de posición válido.")

            # Eliminación del producto
            indice_a_eliminar = posicion - 1
            nombre_eliminado = productos[indice_a_eliminar][0]

            productos.pop(indice_a_eliminar)
            print(
                f"\n✅ Producto '{nombre_eliminado}' (Nro. {posicion}) eliminado exitosamente."
            )

    elif opcion == 5:
        # 5. SALIR
        print("\n👋 ¡Gracias por usar el Sistema de Productos! ¡Hasta luego!")
        break

    else:
        # Opción por defecto
        print("\n❌ Opción no válida. Por favor, ingresa un número del 1 al 5.")
