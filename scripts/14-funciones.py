"""
def nombre_funcion():
    # instrucciones
"""


# deficición / declaración
def saludar():
    print("Hola mundo!")


# invocación
saludar()
saludar()
saludar()


"""
Funciones con parámetros
def saludadr_con_parametros(parametro):
    # instrucciones -> parámetros
"""


def evaluar_edad(edad):
    if edad >= 18:
        print("Sos mayor de edad")
    else:
        print("Sos menor de edad")

evaluar_edad(18)
evaluar_edad(12)

"""
Parámetros opcionales/defecto
def parametros_por_defecto(parametro='valor'):
    # código
"""
def saludar2(nombre='anónimo'):
    print(f"Hola {nombre}")

saludar2()
saludar2('Julian')


# return
def sumar(a, b):
    resultado = a + b
    return resultado


# Guardamos el resultado de la función en una variable
total = sumar(5, 3)
print(f"La suma es: {total}")
# Resultado: La suma es: 8


def buscar_numero_par(numeros):
    for num in numeros:
        if num % 2 == 0:
            print("¡Encontré un número par!")
            return num  # Devuelve el número y sale de la función
    return None  # Si el bucle termina sin encontrar nada, devuelve None


lista1 = [1, 3, 5, 8, 9]
par_encontrado = buscar_numero_par(lista1)
print(f"El primer par es: {par_encontrado}")
# Resultado: ¡Encontré un número par!
# El primer par es: 8

lista2 = [1, 3, 5, 7, 9]
par_encontrado = buscar_numero_par(lista2)
print(f"El primer par es: {par_encontrado}")
# Resultado: El primer par es: None
