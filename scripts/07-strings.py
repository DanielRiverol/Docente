frase = "Hola Mundo"
print(frase.lower())  # hola mundo
print(frase.upper())  # HOLA MUNDO

nombre = "lUis perez"
print(nombre.capitalize())  # Luis perez

# strip / lstrip / rstrip
espacios = "   Python es genial   "
print(espacios.strip())  # Python es genial

# endswith / startswith
archivo = "reporte.xlsx"
print(archivo.endswith(".xlsx"))  # True

# find
cadena = "El sol brilla"
print(cadena.find("brilla"))  # 7
print(cadena.find("luna"))  # -1

# replace
mensaje = "Hola a todos"
nuevo_mensaje = mensaje.replace("todos", "amigos")
print(nuevo_mensaje)  # Hola a amigos

# split
productos = "manzana,banana,pera,naranja"
lista_productos = productos.split(",")
print(lista_productos)  # ['manzana', 'banana', 'pera', 'naranja']

# join
nombres = ["Ana", "Luis", "Sofía"]
cadena_unida = " - ".join(nombres)
print(cadena_unida)  # Ana - Luis - Sofía


# buccles
# Contar la cantidad de vocales en una frase
frase = "Programar en Python es divertido"
contador_vocales = 0
for caracter in frase:
    if caracter.lower() in "aeiou":
        contador_vocales += 1

print(f"La frase tiene {contador_vocales} vocales.")
# Resultado: La frase tiene 10 vocales.


titulo = "El Quijote de la Mancha"
longitud = len(titulo)

print(f"El título '{titulo}' tiene {longitud} caracteres.")
# Resultado: El título 'El Quijote de la Mancha' tiene 23 caracteres.

"""
Slicing (El equivalente a slice o splice)

El slicing te permite obtener una porción de una cadena de texto. Se utiliza la notación de corchetes [] con dos puntos : para indicar el inicio y el fin del segmento que deseas extraer.

La sintaxis es: [inicio:fin:paso]

    [inicio:fin]: Extrae los caracteres desde el índice inicio hasta el fin (sin incluirlo).

    [:fin]: Extrae desde el principio hasta el fin.

    [inicio:]: Extrae desde el inicio hasta el final.

    [:]: Crea una copia de la cadena completa.

    [::paso]: Omite caracteres según el valor de paso.

    [::-1]: Invierte la cadena.

Ejemplos de Slicing
"""

palabra = "ejemplo"

# Extraer los primeros 3 caracteres
subcadena_1 = palabra[0:3]
print(subcadena_1) # Resultado: eje

# Extraer desde el 4to caracter hasta el final
subcadena_2 = palabra[3:]
print(subcadena_2) # Resultado: mplo

# Invertir el string
palabra_invertida = palabra[::-1]
print(palabra_invertida) # Resultado: olpmeje

palabra = "ejemplo"

# [inicio:fin]
# Extrae los caracteres desde el índice 1 hasta el 4 (sin incluirlo)
subcadena_1 = palabra[1:4]
print(f"palabra[1:4] -> '{subcadena_1}'")
# Resultado: 'jem'

# [:fin]
# Extrae desde el principio (índice 0) hasta el 5 (sin incluirlo)
subcadena_2 = palabra[:5]
print(f"palabra[:5] -> '{subcadena_2}'")
# Resultado: 'ejemp'

# [inicio:]
# Extrae desde el índice 2 hasta el final
subcadena_3 = palabra[2:]
print(f"palabra[2:] -> '{subcadena_3}'")
# Resultado: 'emplo'

# [:]
# Crea una copia de la cadena completa
copia_cadena = palabra[:]
print(f"palabra[:] -> '{copia_cadena}'")
# Resultado: 'ejemplo'

# [::paso]
# Extrae los caracteres desde el principio hasta el final, saltando de 2 en 2
con_pasos = palabra[::2]
print(f"palabra[::2] -> '{con_pasos}'")
# Resultado: 'ejmlo'

# [::-1]
# Extrae la cadena de forma invertida, desde el final hacia el principio
invertida = palabra[::-1]
print(f"palabra[::-1] -> '{invertida}'")
# Resultado: 'olpmeje'
