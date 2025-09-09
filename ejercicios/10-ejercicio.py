# Recorremos cada número del 1 al 100
# for numero in range(1, 101):

#     # 1. Verificamos la condición más estricta: si es múltiplo de 3 Y de 5
#     if numero % 3 == 0 and numero % 5 == 0:
#         print("Tuti-Fruti")

#     # 2. Verificamos si es múltiplo de 3
#     elif numero % 3 == 0:
#         print("Tuti")

#     # 3. Verificamos si es múltiplo de 5
#     elif numero % 5 == 0:
#         print("Fruti")

#     # 4. Si no cumple ninguna de las condiciones
#     else:
#         print(numero)

# Es primo
# Bucle para revisar números del 2 al 20
# for numero in range(2, 101):
#     es_primo = True

#     # Bucle para revisar los posibles divisores
#     # (revisamos desde 2 hasta el número - 1)
#     for i in range(2, numero):
#         if numero % i == 0:
#             es_primo = False
#             break  # Encontramos un divisor, no necesitamos seguir revisando

#     # Si la variable 'es_primo' sigue siendo True, el número es primo
#     if es_primo:
#         print(f"{numero} es primo.")

# El número que vamos a revisar
numero = int(
    input(
        "Ingresa un número para conocer si es primo y si es un palíndromo en binario: "
    )
)

print(f"Analizando el número {numero}...")

if numero <= 1:
    print(f"El número {numero} no es primo, ya que no es un número natural mayor a 1.")
else:
    # --- Verificamos si es un número primo ---
    es_primo = True

    # Revisamos si es divisible por cualquier número entre 2 y el mismo número - 1
    for i in range(2, numero):
        if numero % i == 0:
            es_primo = False
            break  # Si encontramos un divisor, no necesitamos seguir revisando

    if es_primo:
        print(f"Propiedad 1: {numero} es un número primo. ✅")
    else:
        print(f"Propiedad 1: {numero} no es un número primo. ❌")

# --- Verificamos si su forma binaria es un palíndromo ---
# La forma binaria de 73 es 1001001

# Convertimos el número a su representación binaria (quitando el prefijo "0b")
binario = bin(numero)[2:]

# Invertimos la cadena de texto para verificar si es un palíndromo
binario_invertido = binario[::-1]

if binario == binario_invertido:
    print(f"Propiedad 2: Su forma binaria ({binario}) es un palíndromo. ✅")
else:
    print(f"Propiedad 2: Su forma binaria ({binario}) no es un palíndromo. ❌")
