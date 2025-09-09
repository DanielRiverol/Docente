"""
Ahorro
"""

objetivo = float(input("¿Cuánto dinero querés ahorrar?:"))
ahorrado = 0

while ahorrado < objetivo:
    cantidad_ahorro = float(input("Ingresa el monto que vas a ahorrar"))
    ahorrado += cantidad_ahorro
    if ahorrado < objetivo:
        print("No llegaste a tu objetivo")

print(f"Felicitaciones!!! LLegaste al objetivo. Ahorraste ${ahorrado}")

# con else
numeros = [1, 5, 8, 12, 3]
# buscando = 99
buscando = 8
indice = 0

while indice < len(numeros):
    if numeros[indice] == buscando:
        print(f"El número {buscando} se encontró en la posición {indice}.")
        break
    indice += 1
else:
    print(f"El número {buscando} no se encontró en la lista.")

# Si cambias buscando = 10, se ejecutará el 'else'
