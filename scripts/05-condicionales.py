"""
Condicional if condicion
                codigo
            else
                codigo
"""

# edad=9
# # cambiamos >=18
# if edad >= 18:
#     print(f'Sos mayor de edad, tu edad es {edad} años')
# else:
#     print(f'No sos mayor de edad, tu edad es {edad} años')

# conduce = input('¿Sabés conducir? si/no ')
# sube = input('¿Tenés SUBE? si/no ')
# bici = input('¿Tenés Bici? si/no ')

# if conduce == 'si':
#     print('Podés ir en auto.')
# elif sube == 'si':
#     print('Podés ir en colectivo.')
# elif bici == 'si':
#     print('Podés ir en bici.')
# else:
#     print('Te toca caminar.')

# v2
# conduce = input('¿Sabés conducir? si/no ')

# if conduce == 'si':
#     print('Podés ir en auto.')
# else:
#     sube = input('¿Tenés SUBE? si/no ')
#     if sube == 'si':
#         print('Podés ir en colectivo.')
#     else:
#         bici = input('¿Tenés Bici? si/no ')
#         if bici == 'si':
#             print('Podés ir en bici.')
#         else:
#             print('Te toca caminar.')

# TALLAS
talla = int(input('Ingresa tu número de talla'))

if talla < 10:
    print("Eres talla XS")
elif talla < 14:
    print("Eres talla S")
elif talla < 18:
    print("Eres talla M")
else:
    print("Eres talla L o superior")
