"""
Sistema de votación
"""

edad = int(input("Ingresa tu edad: "))

if edad >= 18 and edad <= 69:
    print("Es obligatorio votar")
elif edad >= 16:
    print("Podés votar si querés")
else:
    print("No podés votar")


# mejorado
edad = int(input("Ingresa tu edad: "))
mensaje = ""  # Creamos una variable para guardar el mensaje

if edad >= 18 and edad <= 69:
    mensaje = "Es obligatorio votar"
elif edad >= 16:
    mensaje = "Podés votar si querés"
else:
    mensaje = "No podés votar"

print(mensaje)

# LOGIN
# Credenciales guardadas en el sistema
usuario_valido = "admin"
contrasena_valida = "pass123"

# Pedimos al usuario que ingrese sus credenciales
usuario_ingresado = input("Ingresa tu nombre de usuario: ")
contrasena_ingresada = input("Ingresa tu contraseña: ")

# Verificamos si las credenciales coinciden usando 'and'
if usuario_ingresado == usuario_valido and contrasena_ingresada == contrasena_valida:
    print("¡Acceso concedido! Bienvenido.")
else:
    print("Error: Usuario o contraseña incorrectos.")

# Solicitamos los datos para el cálculo
try:
    total_compra = float(input("Ingresa el total de la compra: "))
    tipo_combustible = input("Ingresa el tipo de combustible (nafta, gasoil, gnc): ")
    tipo_usuario = input("Ingresa tu tipo de usuario (regular, socio, vip): ")

    descuento = 0

    # Lógica para aplicar el descuento
    if tipo_usuario == "vip":
        # Los usuarios VIP siempre tienen un 10% de descuento
        descuento = 0.10
    elif tipo_usuario == "socio":
        # Los socios siempre tienen un 5% de descuento
        descuento = 0.05
    elif tipo_usuario == "regular":
        # Los usuarios regulares solo tienen descuento si compran nafta
        if tipo_combustible == "nafta":
            descuento = 0.02
        else:
            descuento = 0  # No hay descuento para otros combustibles

    # Calculamos el total final
    monto_descuento = total_compra * descuento
    total_con_descuento = total_compra - monto_descuento

    # Mostramos el resultado
    print(f"\nResumen de la compra:")
    print(f"Total sin descuento: ${total_compra:.2f}")
    print(f"Descuento aplicado: ${monto_descuento:.2f}")
    print(f"Total a pagar: ${total_con_descuento:.2f}")

except ValueError:
    print("Error: Por favor, ingresa un valor numérico válido para la compra.")
