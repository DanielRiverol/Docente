tupla_colores = ("rojo", "verde", "azul", "amarillo", "blanco")

# Slicing básico en una tupla
sub_tupla = tupla_colores[1:4]
print(sub_tupla)
# Resultado: ('verde', 'azul', 'amarillo')
# Tupla original
tupla_original = (1, 2, 3)

# Paso 1: Convertir a lista
lista_temporal = list(tupla_original)

# Paso 2: Modificar la lista
lista_temporal.append(4)

# Paso 3: Convertir de vuelta a tupla
nueva_tupla = tuple(lista_temporal)

print(nueva_tupla)
# Resultado: (1, 2, 3, 4)
