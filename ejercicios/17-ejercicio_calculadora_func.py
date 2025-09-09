# operaciones
def sumar(a, b):
    return a + b


def restar(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        return "Error: División por cero"
    return a / b


# calculadora
def calculadora(operacion):
    """
    Devuelve la función de operación matemática correspondiente.

    Args:
        operacion (str): El nombre de la operación ('sumar', 'restar', etc.).

    Returns:
        function: La función que realiza la operación.
        str: Un mensaje de error si la operación no es válida.
    """
    if operacion == "sumar":
        return sumar
    elif operacion == "restar":
        return restar
    elif operacion == "multiplicar":
        return multiplicar
    elif operacion == "dividir":
        return dividir
    else:
        return "Operación no válida."

# Paso 1: Obtenemos la función para la operación "multiplicar"
# La variable 'mi_funcion' ahora almacena la función multiplicar
mi_funcion = calculadora("multiplicar")

# Paso 2: Usamos la función que obtuvimos para realizar el cálculo
resultado = mi_funcion(10, 5)
print(f"El resultado de la multiplicación es: {resultado}")
# Resultado: El resultado de la multiplicación es: 50

# Ejemplo con otra operación
mi_otra_funcion = calculadora("dividir")
resultado2 = mi_otra_funcion(10, 2)
print(f"El resultado de la división es: {resultado2}")
# Resultado: El resultado de la división es: 5

# Ejemplo con una operación no válida
funcion_invalida = calculadora("potencia")
print(f"Resultado para operación inválida: {funcion_invalida}")
# Resultado: Resultado para operación inválida: Operación no válida.
