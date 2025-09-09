# Pedimos al usuario que ingrese la magnitud
try:
    magnitud = float(input("Ingresa la magnitud del terremoto: "))
    mensaje = ""

    # Usamos if/elif/else para determinar el nivel de daño
    if magnitud < 2.0:
        mensaje = "Micro-terremoto: No se detecta. Generalmente no se siente."
    elif magnitud < 4.0:
        mensaje = "Terremoto menor: A menudo se siente, pero rara vez causa daños."
    elif magnitud < 5.0:
        mensaje = "Terremoto ligero: Puede causar daños menores a edificios y otras estructuras."
    elif magnitud < 6.0:
        mensaje = (
            "Terremoto moderado: Puede causar daños importantes en áreas pobladas."
        )
    elif magnitud < 7.0:
        mensaje = "Terremoto fuerte: Causa daños serios en una gran área."
    elif magnitud < 8.0:
        mensaje = (
            "Terremoto mayor: Causa daños masivos y pérdidas de vida en un área amplia."
        )
    else:
        mensaje = "Terremoto cataclísmico: Daños catastróficos. Destrucción total de comunidades."

    print(mensaje)

except ValueError:
    print("Error: Por favor, ingresa un número válido para la magnitud.")
