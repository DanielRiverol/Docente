lista_peliculas = [
    "Matrix",
    "Rescatando al soldado Ryan",
    "Náufrago",
    "Titanic",
    "El Conde de Montecristo",
]
print(lista_peliculas)
for pelicula in lista_peliculas:
    print(pelicula)

print(lista_peliculas[0])

# reasignacion
lista_peliculas[4] = "Otra peli"
print(lista_peliculas)


# slicing
print(lista_peliculas[:2])


# concatenar
lista_peliculas2 = ["El hobbit", "Harry Potter y la cámara de los secretos"]

if lista_peliculas != lista_peliculas2:
    lista_peliculas3 = lista_peliculas + lista_peliculas2
    print(lista_peliculas3)

# METODOS
# append
frutas = ["manzana", "banana"]
frutas.append("naranja")
print(frutas)
# Resultado: ['manzana', 'banana', 'naranja']

# insert
colores = ["rojo", "azul"]
colores.insert(1, "verde")  # Inserta "verde" en la posición 1
print(colores)
# Resultado: ['rojo', 'verde', 'azul']

# remove
numeros = [1, 2, 3, 2]
numeros.remove(2)
print(numeros)
# Resultado: [1, 3, 2]

# sort
letras = ["c", "a", "b"]
letras.sort()
print(letras)
# Resultado: ['a', 'b', 'c']
