# random
import random

# random.randint(a,b)incluye extremos a y b
print(random.randint(1,20))
# random.randrange(start, stop[, step])
# (start=0, stop=101 para incluir el 100, step=2)
numero_par = random.randrange(0, 101, 2)
print(f"Número par aleatorio: {numero_par}")
# random.random()
if random.random() < 0.30:
    print("¡Evento especial ocurrió! (30% prob.)")
else:
    print("Evento normal. (70% prob.)")
# random.uniform(a,b)
temperatura = random.uniform(15.5, 25.5)
# .2f formatea el número para mostrar solo 2 decimales
print(f"Temperatura actual: {temperatura:.2f}°C")

# random.choice(lista)
colores = ["rojo", "verde", "azul", "amarillo"]
color_elegido = random.choice(colores)
print(f"Color elegido: {color_elegido}")

# random.shuffle(lista)
cartas = ["As", "Rey", "Reina", "Jota", "10"]
print(f"Cartas sin barajar: {cartas}")
random.shuffle(cartas)
print(f"Cartas barajadas:  {cartas}")

# random.sample(a, k) nueva lista con elementos

numeros_posibles = range(1, 37)  # Del 1 al 36
numeros_ganadores = random.sample(numeros_posibles, 6)
print(f"Números de QUINI (únicos): {numeros_ganadores}")


