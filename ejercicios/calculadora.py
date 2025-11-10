# Este es el módulo 'calculadora'


def sumar(a, b):
    """Devuelve la suma de a y b."""
    return a + b


def restar(a, b):
    """Devuelve la resta de a y b."""
    return a - b


def multiplicar(a, b):
    """Devuelve la multiplicación de a y b."""
    return a * b


def dividir(a, b):
    """
    Devuelve la división de a y b.
    Maneja el error de división por cero.
    """
    if b == 0:
        return "Error: No se puede dividir por cero"
    else:
        return a / b
