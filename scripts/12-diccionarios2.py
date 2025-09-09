catalogo_entretenimiento_90s = {
    "Peliculas": {
        "Pulp Fiction": {
            "director": "Quentin Tarantino",
            "anio": 1994,
            "genero": ["Crimen", "Drama"],
        },
        "Jurassic Park": {
            "director": "Steven Spielberg",
            "anio": 1993,
            "genero": ["Ciencia Ficción", "Aventura"],
        },
        "Titanic": {
            "director": "James Cameron",
            "anio": 1997,
            "genero": ["Romance", "Drama"],
        },
        "Forrest Gump": {
            "director": "Robert Zemeckis",
            "anio": 1994,
            "genero": ["Comedia", "Drama"],
        },
        "El Silencio de los Inocentes": {
            "director": "Jonathan Demme",
            "anio": 1991,
            "genero": ["Thriller", "Terror"],
        },
        "El Club de la Pelea": {
            "director": "David Fincher",
            "anio": 1999,
            "genero": ["Drama", "Thriller"],
        },
    },
    "Series": {
        "Friends": {
            "creador": "Marta Kauffman, David Crane",
            "temporadas": 10,
            "genero": ["Comedia", "Sitcom"],
        },
        "Los Simpson": {
            "creador": "Matt Groening",
            "temporadas": 36,
            "genero": ["Animación", "Comedia"],
        },
        "Seinfeld": {
            "creador": "Jerry Seinfeld, Larry David",
            "temporadas": 9,
            "genero": ["Comedia", "Sitcom"],
        },
        "Expedientes X": {
            "creador": "Chris Carter",
            "temporadas": 11,
            "genero": ["Ciencia Ficción", "Misterio"],
        },
        "ER": {
            "creador": "Michael Crichton",
            "temporadas": 15,
            "genero": ["Drama", "Médico"],
        },
        "Dragon Ball Z": {
            "creador": "Akira Toriyama",
            "temporadas": 9,
            "genero": ["Animación", "Aventura"],
        },
    },
}

# acceso a datos
print(catalogo_entretenimiento_90s["Peliculas"]["El Club de la Pelea"]["genero"])
# Resultado: ['Drama', 'Thriller']
print(catalogo_entretenimiento_90s["Series"]["Expedientes X"]["creador"])
# Resultado: Chris Carter
# metodos
claves = catalogo_entretenimiento_90s.keys()
print(claves)
# Resultado: dict_keys(['Peliculas', 'Series'])
titulos_peliculas = catalogo_entretenimiento_90s["Peliculas"].keys()
print(titulos_peliculas)
# Resultado: dict_keys(['Pulp Fiction', 'Jurassic Park', 'Titanic', 'Forrest Gump', 'El Silencio de los Corderos', 'El Club de la Pelea'])
valores_series = catalogo_entretenimiento_90s["Series"].values()
# Esto te mostraría todos los diccionarios de las series.
# Por ejemplo, el primero sería: dict_values([{'creador': 'Marta Kauffman, David Crane', 'temporadas': 10, 'genero': ['Comedia', 'Sitcom']}, ...])
# Usando .get() para evitar un error
pelicula_no_existente = catalogo_entretenimiento_90s["Peliculas"].get(
    "Matrix", "No se encuentra en el catálogo"
)
print(pelicula_no_existente)
# Resultado: No se encuentra en el catálogo

# Usando el acceso directo, esto daría un error
# print(catalogo_entretenimiento_90s["Peliculas"]["Matrix"])
# BUscando una existete con get
pelicula_existente = catalogo_entretenimiento_90s["Peliculas"].get(
    "Titanic", "No se encuentra en el catálogo"
)
print(pelicula_existente)

# Añadimos una nueva película y actualizamos una existente
catalogo_entretenimiento_90s["Peliculas"].update(
    {
        "Hombres de Negro": {
            "director": "Barry Sonnenfeld",
            "anio": 1997,
            "genero": ["Ciencia Ficción", "Acción"],
        }
    }
)

print("Hombres de Negro" in catalogo_entretenimiento_90s["Peliculas"])
# Resultado: True
# actualizar peli existente
catalogo_entretenimiento_90s["Peliculas"].update(
    {
        "Pulp Fiction": {
            "director": "Saracatunga",
            "anio": 1997,
            "genero": ["Ciencia Ficción", "Acción"],
        }
    }
)

# lista de pelis actualizada
print(catalogo_entretenimiento_90s["Peliculas"])

# Eliminamos una película que no te gusta del diccionario
pelicula_eliminada = catalogo_entretenimiento_90s["Peliculas"].pop("Titanic")

print("Titanic" in catalogo_entretenimiento_90s["Peliculas"])
# Resultado: False

for titulo_pelicula, detalles in catalogo_entretenimiento_90s["Peliculas"].items():
    print(f"Titulo: {titulo_pelicula}")
    for item, valor in detalles.items():
        print(f"{item.title()}:{valor}")
