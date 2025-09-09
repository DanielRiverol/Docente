"""
Calculadora de liquidación
Crea un programa que calcule el salario total de un empleado
basándose en dos datos predefinidos: el número de horas trabajadas y la tarifa por hora.
El programa debe realizar la multiplicación y mostrar el resultado final.
"""

# 1. Definimos las variables con los datos de entrada
horas_trabajadas = 40
tarifa_por_hora = 25.50

# 2. Calculamos el salario total
salario_total = horas_trabajadas * tarifa_por_hora

# 3. Mostramos el resultado
print(
    f"El salario total por {horas_trabajadas} horas trabajadas a una tarifa de ${tarifa_por_hora} por hora es: ${salario_total:.2f}"
)
