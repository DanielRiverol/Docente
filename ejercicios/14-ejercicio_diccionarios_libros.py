# Nuestro diccionario de la biblioteca, con 10 libros clásicos
biblioteca = {
    "Drácula": {
        "autor": "Bram Stoker",
        "anio": 1897,
        "genero": ["Gótico", "Terror"],
        "isbn": "978-0486411091",
    },
    "Frankenstein": {
        "autor": "Mary Shelley",
        "anio": 1818,
        "genero": ["Gótico", "Ciencia Ficción"],
        "isbn": "978-0486282110",
    },
    "El Conde de Montecristo": {
        "autor": "Alexandre Dumas",
        "anio": 1844,
        "genero": ["Aventura", "Clásico"],
        "isbn": "978-0486438099",
    },
    "Los Tres Mosqueteros": {
        "autor": "Alexandre Dumas",
        "anio": 1844,
        "genero": ["Aventura", "Histórico"],
        "isbn": "978-0486411329",
    },
    "Moby Dick": {
        "autor": "Herman Melville",
        "anio": 1851,
        "genero": ["Aventura", "Filosófico"],
        "isbn": "978-0553213119",
    },
    "El Retrato de Dorian Gray": {
        "autor": "Oscar Wilde",
        "anio": 1890,
        "genero": ["Filosófico", "Fantasía"],
        "isbn": "978-0486273767",
    },
    "Las Aventuras de Sherlock Holmes": {
        "autor": "Arthur Conan Doyle",
        "anio": 1892,
        "genero": ["Misterio", "Policial"],
        "isbn": "978-0486262440",
    },
    "Cumbres Borrascosas": {
        "autor": "Emily Brontë",
        "anio": 1847,
        "genero": ["Gótico", "Romance"],
        "isbn": "978-0486270520",
    },
    "Grandes Esperanzas": {
        "autor": "Charles Dickens",
        "anio": 1861,
        "genero": ["Drama", "Clásico"],
        "isbn": "978-0486424350",
    },
    "Alicia en el país de las maravillas": {
        "autor": "Lewis Carroll",
        "anio": 1865,
        "genero": ["Fantasía", "Aventura"],
        "isbn": "978-0486273736",
    },
}

# Bucle principal para el menú interactivo
while True:
    print("\n--- Sistema de Gestión de Biblioteca (Clásicos) ---")
    print("1. Ver todos los libros")
    print("2. Buscar un libro")
    print("3. Añadir un libro")
    print("4. Actualizar un libro")
    print("5. Eliminar un libro")
    print("6. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        print("\n--- Catálogo Completo ---")
        if not biblioteca:
            print("La biblioteca está vacía.")
            continue
        for titulo, info in biblioteca.items():
            print(f"Título: {titulo}")
            print(f"  Autor: {info.get('autor', 'No disponible')}")
            print(f"  Año: {info.get('anio', 'No disponible')}")
            print(f"  Géneros: {', '.join(info.get('genero', ['No disponible']))}")
            print(f"  ISBN: {info.get('isbn', 'No disponible')}\n")

    elif opcion == "2":
        titulo_busqueda = input("Ingresa el título del libro que buscas: ")
        libro = biblioteca.get(titulo_busqueda)
        if libro:
            print(f"\n--- Libro Encontrado ---")
            print(f"Título: {titulo_busqueda}")
            print(f"  Autor: {libro['autor']}")
            print(f"  Año: {libro['anio']}")
            print(f"  Géneros: {', '.join(libro['genero'])}")
            print(f"  ISBN: {libro['isbn']}")
        else:
            print(f"Lo siento, '{titulo_busqueda}' no se encuentra en el catálogo.")

    elif opcion == "3":
        print("\n--- Añadir un nuevo libro ---")
        nuevo_titulo = input("Título: ")
        if nuevo_titulo in biblioteca:
            print("Ese libro ya existe en la biblioteca.")
            continue

        nuevo_autor = input("Autor: ")
        nuevo_anio = int(input("Año: "))
        nuevo_genero = input("Géneros (separados por coma): ").split(",")
        nuevo_isbn = input("ISBN: ")

        biblioteca[nuevo_titulo] = {
            "autor": nuevo_autor,
            "anio": nuevo_anio,
            "genero": [g.strip() for g in nuevo_genero],
            "isbn": nuevo_isbn,
        }
        print(f"'{nuevo_titulo}' ha sido añadido correctamente.")

    elif opcion == "4":
        print("\n--- Actualizar un libro ---")
        titulo_actualizar = input("Ingresa el título del libro a actualizar: ")
        if titulo_actualizar in biblioteca:
            print("Deja el campo vacío si no quieres actualizarlo.")
            nuevo_autor = input(
                f"Autor actual: {biblioteca[titulo_actualizar]['autor']}. Nuevo autor: "
            )
            nuevo_anio_str = input(
                f"Año actual: {biblioteca[titulo_actualizar]['anio']}. Nuevo año: "
            )
            nuevo_isbn = input(
                f"ISBN actual: {biblioteca[titulo_actualizar]['isbn']}. Nuevo ISBN: "
            )

            if nuevo_autor:
                biblioteca[titulo_actualizar].update({"autor": nuevo_autor})
            if nuevo_anio_str:
                biblioteca[titulo_actualizar].update({"anio": int(nuevo_anio_str)})
            if nuevo_isbn:
                biblioteca[titulo_actualizar].update({"isbn": nuevo_isbn})

            print("El libro ha sido actualizado.")
        else:
            print("Ese libro no se encuentra en el catálogo.")

    elif opcion == "5":
        print("\n--- Eliminar un libro ---")
        titulo_eliminar = input("Ingresa el título del libro a eliminar: ")

        if titulo_eliminar in biblioteca:
            biblioteca.pop(titulo_eliminar)
            print(f"'{titulo_eliminar}' ha sido eliminado correctamente.")
        else:
            print("Ese libro no se encuentra en el catálogo.")

    elif opcion == "6":
        print("Saliendo del programa. ¡Hasta pronto!")
        break

    else:
        print("Opción no válida. Por favor, elige un número del 1 al 6.")
