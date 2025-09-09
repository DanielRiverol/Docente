# dicconario
mi_diccionario = {"nombre": "Dani", "apellido": "Riv", "edad": 42}
mi_diccionario["hobbies"] = ["jugar", "programar"]
print(mi_diccionario["nombre"])
print(mi_diccionario["apellido"])
print(mi_diccionario["edad"])
mi_diccionario["edad"] += 1
print(mi_diccionario["edad"])

for clave in mi_diccionario:
    print(f"{clave.upper()}: {mi_diccionario[clave]}")

# metodos
# devuelve claves
print(mi_diccionario.keys())
# eliminar claves
del mi_diccionario["hobbies"]
print(mi_diccionario.keys())
# devuelve items
print(mi_diccionario.items())
# devuelve values
print(mi_diccionario.values())
