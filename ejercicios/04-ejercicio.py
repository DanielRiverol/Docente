# Variables de entrada
es_premium = True
total_compra = 85

# Condición: El usuario debe ser premium O su compra debe superar los $100
if es_premium or total_compra > 100:
    print("¡Tienes acceso a un 10% de descuento!")
else:
    print("No tienes descuentos disponibles.")

"""
Casos Posibles del Sistema de Descuentos 📈

    El mayor descuento: Fin de Semana 🏖️

        Entrada: es_finde_semana = 'si'

        Resultado: Se aplica el descuento del 15%. Total a pagar: $85.

        Motivo: Es la primera condición que se revisa y la de mayor valor, por lo que las demás no se evalúan.

    Usuario VIP (no es fin de semana) 👑

        Entrada: es_finde_semana = 'no', tipo_usuario = 'vip'

        Resultado: Se aplica el descuento del 10%. Total a pagar: $90.

        Motivo: La condición de fin de semana no se cumple, pero la de usuario VIP sí, y es la siguiente más alta.

    Usuario Socio o Pago por App 🤝

        Entrada: es_finde_semana = 'no', tipo_usuario = 'socio', metodo_pago = 'tarjeta'

        Resultado: Se aplica el descuento del 5%. Total a pagar: $95.

        Motivo: La condición elif tipo_usuario == 'socio' or metodo_pago == 'app_propia' se cumple. Si en este caso el tipo_usuario fuera regular pero el metodo_pago fuera app_propia, el resultado sería el mismo.

    Nafta Premium (Usuario Regular) ⛽️

        Entrada: es_finde_semana = 'no', tipo_usuario = 'regular', tipo_combustible = 'nafta_premium'

        Resultado: Se aplica el descuento del 3%. Total a pagar: $97.

        Motivo: Ninguna de las condiciones anteriores se cumplió, por lo que el programa pasa a evaluar el tipo de combustible para un usuario regular.

    Gasoil (Usuario Regular) 🚜

        Entrada: es_finde_semana = 'no', tipo_usuario = 'regular', tipo_combustible = 'gasoil'

        Resultado: Se aplica el descuento del 2%. Total a pagar: $98.

        Motivo: La lógica del programa continúa hasta encontrar la primera condición que coincide.

    Sin Descuento 😞

        Entrada: es_finde_semana = 'no', tipo_usuario = 'regular', tipo_combustible = 'gnc'

        Resultado: Se aplica el descuento del 0%. Total a pagar: $100.

        Motivo: Ninguna de las condiciones anteriores se cumplió, por lo que la variable descuento_porcentaje se queda en su valor inicial de 0.0.
"""
# Pedimos los datos al usuario
try:
    total_compra = float(input("Ingresa el total de la compra: "))
    tipo_combustible = input(
        "Ingresa el combustible (nafta_super, nafta_premium, gasoil, gnc): "
    )
    tipo_usuario = input("Ingresa tu tipo de usuario (regular, socio, vip): ")
    es_finde_semana = input("¿Es fin de semana? (si/no): ")
    metodo_pago = input("Ingresa el método de pago (tarjeta, efectivo, app_propia): ")

    descuento_porcentaje = 0.0  # Inicializamos el descuento en 0

    # 1. Comprobamos las condiciones del descuento en orden de prioridad (de mayor a menor)
    if es_finde_semana == "si":
        descuento_porcentaje = 0.15  # 15% es el descuento más alto
    elif tipo_usuario == "vip":
        descuento_porcentaje = 0.10
    elif tipo_usuario == "socio" or metodo_pago == "app_propia":
        descuento_porcentaje = 0.05
    elif tipo_combustible == "nafta_premium":
        descuento_porcentaje = 0.03
    elif tipo_combustible == "gasoil":
        descuento_porcentaje = 0.02

    # 2. Calculamos el total con el descuento final
    monto_descuento = total_compra * descuento_porcentaje
    total_con_descuento = total_compra - monto_descuento

    # 3. Mostramos los resultados
    print("\n--- Resumen de la compra ---")
    print(f"Total sin descuento: ${total_compra:.2f}")
    print(f"Descuento aplicado: {descuento_porcentaje * 100:.0f}%")
    print(f"Monto de descuento: ${monto_descuento:.2f}")
    print(f"Total a pagar: ${total_con_descuento:.2f}")

except ValueError:
    print(
        "Error: Por favor, ingresa un valor numérico válido para el total de la compra."
    )
