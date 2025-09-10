# Un script de Los Simpson: "¿Nos llevas a Monte Splash?"
# Se detiene solo cuando Homero cede.

# Definimos la respuesta inicial de Homero para que el bucle comience
respuesta_homero = "no"

print("¡Vamos a ver si Bart y Lisa logran convencer a Homero de ir a Monte Splash!")

# El bucle se ejecutará mientras la respuesta de Homero sea "no"
while respuesta_homero.lower() == "no":
    # Bart y Lisa hacen la pregunta
    print("\nBart y Lisa: ¿Nos llevas a Monte Splash?")

    # Pedimos al usuario que responda como Homero
    respuesta_homero = input(
        "Homero: (Responde, escribe 'no' para negarte o 'si' para ceder): "
    )

    # # Si Homero se niega, los niños insisten con la siguiente línea de diálogo
    # if respuesta_homero.lower() == "no":
    #     print("Bart y Lisa: Si dices que sí, dejaremos de fastidiarte.")

# Cuando el bucle termina, Homero cede y los niños agradecen
print("\nHomero: Ay, bueno, está bien.")
print("Bart y Lisa: ¡Gracias, papá!")
