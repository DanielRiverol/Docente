# Lista principal para almacenar todos los productos.
# Cada producto será una sublista: [nombre, categoria, precio]
productos = []

# Bucle principal del programa
while True:
    print("\n" + "="*40)
    print("      SISTEMA BÁSICO DE PRODUCTOS")
    print("="*40)
    print("1. Agregar producto")
    print("2. Mostrar productos")
    print("3. Buscar producto por nombre")
    print("4. Eliminar producto por posición")
    print("5. Salir")
    print("="*40)

    # 1. VALIDACIÓN: Asegurarse de que la opción sea un número y esté en el rango 1-5.
    opcion = input("Elige una opción (1-5): ").strip()

    # Condicional para manejar la opción seleccionada
    if opcion.isdigit():
        opcion = int(opcion) 
    else:
        opcion = 0 # Opción inválida si no es un dígito
    
    
    # ---------------------------------
    # FUNCIONALIDADES DEL SISTEMA
    # ---------------------------------

    if opcion == 1:
        # 1. AGREGAR PRODUCTO
        print("\n--- AGREGAR NUEVO PRODUCTO ---")
        
        # Validación para el nombre
        nombre_valido = False
        while not nombre_valido:
            nombre = input("Ingresa el nombre del producto: ").strip()
            if nombre == "":
                print("⚠️ Error: El nombre del producto no puede estar vacío.")
            else:
                nombre_valido = True

        # Validación para la categoría
        categoria_valida = False
        while not categoria_valida:
            categoria = input("Ingresa la categoría del producto: ").strip()
            if categoria == "":
                print("⚠️ Error: La categoría del producto no puede estar vacía.")
            else:
                categoria_valida = True

        # Validación para el precio (debe ser un número entero positivo)
        precio_valido = False
        while not precio_valido:
            precio_str = input("Ingresa el precio (sin centavos): ").strip()
            if precio_str.isdigit():
                precio = int(precio_str)
                if precio > 0:
                    precio_valido = True
                else:
                    print("⚠️ Error: El precio debe ser un número positivo.")
            else:
                print("⚠️ Error: El precio debe ser un número entero válido.")

        # Añadir el producto a la lista principal
        productos.append([nombre, categoria, precio])
        print(f"\n✅ Producto '{nombre}' agregado exitosamente.")

    elif opcion == 2:
        # 2. MOSTRAR PRODUCTOS
        print("\n--- PRODUCTOS REGISTRADOS ---")
        if len(productos) == 0: # Condicional: Usamos len() para verificar si la lista está vacía
            print("▶️ No hay productos registrados para mostrar.")
        else:
            print("Nro. | Nombre                 | Categoría            | Precio")
            print("-----|------------------------|----------------------|-------")
            
            # Recorrer la lista con un bucle 'for' usando el rango de índices (SIN ENUMERATE)
            # Esto es equivalente a usar enumerate: recorremos los números 0, 1, 2, ...
            for i in range(len(productos)):
                producto = productos[i] # Obtenemos el producto usando el índice 'i'
                
                # El número de producto visible para el usuario (empieza en 1)
                numero_producto = i + 1
                nombre = producto[0]
                categoria = producto[1]
                precio = producto[2]
                
                # Presentación de la información
                print(f"{numero_producto:<4} | {nombre:<22} | {categoria:<20} | ${precio}")
            print("----------------------------------------------------------")

    elif opcion == 3:
        # 3. BUSCAR PRODUCTO
        print("\n--- BUSCAR PRODUCTO POR NOMBRE ---")
        if len(productos) == 0:
            print("▶️ No hay productos para buscar.")
        else:
            termino_busqueda = input("Ingresa el nombre o parte del nombre a buscar: ").strip().lower()
            coincidencias_encontradas = 0 # Contador para saber si encontramos algo
            
            print("\n✅ Se encontraron las siguientes coincidencias:")
            print("Nombre                 | Categoría            | Precio")
            print("-----------------------|----------------------|-------")

            # Recorrer la lista completa de productos
            for producto in productos:
                # Condicional para la búsqueda
                if termino_busqueda in producto[0].lower():
                    # Si hay coincidencia, incrementamos el contador y mostramos el producto
                    coincidencias_encontradas = coincidencias_encontradas + 1
                    
                    nombre = producto[0]
                    categoria = producto[1]
                    precio = producto[2]
                    print(f"{nombre:<22} | {categoria:<20} | ${precio}")
            
            # Condicional final para informar si no se encontró nada
            if coincidencias_encontradas == 0:
                print(f"❌ No se encontraron productos que contengan '{termino_busqueda}'.")
                print("----------------------------------------------------------")


    elif opcion == 4:
        # 4. ELIMINAR PRODUCTO
        print("\n--- ELIMINAR PRODUCTO ---")
        if len(productos) == 0:
            print("▶️ No hay productos para eliminar.")
        else:
            # Primero mostramos la lista numerada para que el usuario elija (SIN ENUMERATE)
            print("Productos actuales:")
            for i in range(len(productos)):
                producto = productos[i]
                print(f"{i + 1}. {producto[0]} (Precio: ${producto[2]})")

            # Bucle y validación para la posición
            posicion_valida = False
            while not posicion_valida:
                posicion_str = input("Ingresa el NÚMERO del producto a eliminar: ").strip()
                
                if posicion_str.isdigit():
                    posicion = int(posicion_str)
                    # La posición debe estar entre 1 y el número total de productos
                    if posicion >= 1 and posicion <= len(productos):
                        posicion_valida = True
                    else:
                        print(f"⚠️ Error: El número debe estar entre 1 y {len(productos)}.")
                else:
                    print("⚠️ Error: Ingresa un número de posición válido.")

            # Eliminación del producto
            # El índice real de la lista es 'posicion' menos 1
            indice_a_eliminar = posicion - 1
            nombre_eliminado = productos[indice_a_eliminar][0]
            
            # Usamos pop para eliminar por índice
            productos.pop(indice_a_eliminar)
            print(f"\n✅ Producto '{nombre_eliminado}' (Nro. {posicion}) eliminado exitosamente.")

    elif opcion == 5:
        # 5. SALIR
        print("\n👋 ¡Gracias por usar el Sistema de Productos! ¡Hasta luego!")
        break # Esto rompe el bucle 'while True' y finaliza el programa

    else:
        # Opción por defecto
        print("\n❌ Opción no válida. Por favor, ingresa un número del 1 al 5.")