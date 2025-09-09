print("Hola Mundo")
print("Bienvenidos al curso")

# Comentario de una sola línea -> el programa no ejecuta esta linea... sirven para hacer aclaraciones, dividir secciones

"""Esto es un
comentario multilinea
"""
print("HOLA MUNDO")
print("Bienvenidos al Curso 'Introducción a Python'")
# Variable -> nombre descriptivo
mensaje = "Hola soy una mensaje"
print(mensaje)
# type(tipo de dato)
print(type(mensaje))


# entrada y salida de datos
# entrqada input("mensaje")
ingreso = input("Ingresas tu nombre: ")
# salida
print("hola" + ingreso)  # Ponemos + para concatenar no deja espacio
print("hola", ingreso)  # Ponemos , para concatenar
print(f"hola {ingreso}")  # formateamos con f para interpolar
