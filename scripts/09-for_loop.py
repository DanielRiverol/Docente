"""FOR item in rango:
bloque de instrucciones
"""

# nombre= 'PENSAR'

# for letra in nombre:
#     print(letra)
# tradicional
# for numero in range(0,11):
#     print(numero)
# steps
# for numero in range(0,100,10):
#     print(numero)

# for tabla de multiplicar
# rango=range(0,11)

# numero= int(input('¿Qué número querés multiplicar? '))

# for num in rango:
#     print(f"{numero} x {num} = {numero*num}")

# for i in range(1, 11):
#     for j in range(1, 11):
#         resultado = i * j
#         print(f"{i} x {j} = {resultado}")


# stoppers
# break
# nombre= "Python"
# for letra in nombre:
#     if(letra == 'h'):
#         break
#     print(letra)

# Definimos las frutas a buscar en una cadena de texto
frutas = "naranja,pera,kiwi,manzana,uva"

# Bucle para recorrer cada fruta en la cadena
for fruta in frutas.split(","):
    print(f"Buscando: {fruta}")

    # Condición para detener el bucle
    if fruta == "manzana":
        print("¡Encontré la manzana!")
        break

total = 0
print("Ingresa 5 números, sumaré solo los positivos.")

# Bucle para pedir 5 números
for i in range(5):
    numero_str = input(f"Ingresa el número {i + 1}: ")

    # Convertimos el string a un número
    numero = int(numero_str)

    # Si el número es negativo, saltamos
    if numero < 0:
        print("Número negativo. Saltando...")
        continue

    total += numero

print(f"La suma de los números positivos es: {total}")
