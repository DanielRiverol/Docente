# # Importamos el módulo completo que creamos
# import calculadora

# # Ahora podemos usar sus funciones usando el "prefijo" calculadora.
# num1 = 10
# num2 = 5

# print(f"--- Resultados (Método 1) ---")

# # Usamos calculadora.sumar()
# suma = calculadora.sumar(num1, num2)
# print(f"Suma: {suma}")

# # Usamos calculadora.restar()
# resta = calculadora.restar(num1, num2)
# print(f"Resta: {resta}")

# # Usamos calculadora.multiplicar()
# producto = calculadora.multiplicar(num1, num2)
# print(f"Multiplicación: {producto}")

# # Usamos calculadora.dividir()
# division = calculadora.dividir(num1, num2)
# print(f"División: {division}")

# # Probamos el error de división
# division_cero = calculadora.dividir(num1, 0)
# print(f"División por cero: {division_cero}")
# Importamos solo las funciones que queremos usar
from calculadora import sumar, restar, multiplicar, dividir

# Ahora podemos llamarlas directamente por su nombre
num1 = 10
num2 = 5

print(f"--- Resultados (Método 2) ---")

# Ya no necesitamos el prefijo 'calculadora.'
suma = sumar(num1, num2)
print(f"Suma: {suma}")

resta = restar(num1, num2)
print(f"Resta: {resta}")

producto = multiplicar(num1, num2)
print(f"Multiplicación: {producto}")

division = dividir(num1, num2)
print(f"División: {division}")

# Probamos el error de división
division_cero = dividir(num1, 0)
print(f"División por cero: {division_cero}")
