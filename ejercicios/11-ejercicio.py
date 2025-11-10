# repetir password

# while True:
#     password = input("Ingrese su contraseña: ")
#     repeat_password = input("Repita su contraseña: ")

#     if password == repeat_password:
#         print('Contraseña confirmada.')
#         break
#     else:
#         print('Las contraseñas no coinciden.')


# numeros pares e impares
cantidad_num = int(input("Ingresa la cantidad de números que querés evaluar: "))
contador = 0
pares = 0
impares = 0
while contador < cantidad_num:
    numero = int(input("Ingresa un número: "))
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
    contador += 1

print(
    f"""Cantidad de números ingresados: {cantidad_num}.
Números pares: {pares}.
Números impares: {impares}"""
)
