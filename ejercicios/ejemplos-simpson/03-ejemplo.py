# Un script de Los Simpson: "¿Ya llegamos a la India?"

# Definimos el número de veces que Homer preguntará
veces_a_preguntar = 5

# Inicializamos la respuesta de Apu fuera del bucle
respuesta_apu = "Apu: No"

print("Simulación de un viaje en avión con Homero y Apu:")

for i in range(veces_a_preguntar):
    # La pregunta de Homero
    print(f"Homero: ¿Ya llegamos a la India?")

    # La respuesta de Apu, que es la misma en cada iteración del bucle
    print(respuesta_apu)

    # Agregamos una línea en blanco para separar los diálogos
    print()

# Al final del bucle, cambiamos el valor de la variable de Apu
respuesta_apu = "Apu: ¡No... a ver? ¡YA!"

# Mostramos la respuesta final de Apu
print(respuesta_apu)
print("¡Llegamos!")
