# --- 1. Escribir ('w') ---
print("--- Forma Antigua: Escribiendo ('w') ---")
# Abrimos el archivo
f_antiguo = open("antiguo.txt", "w", encoding="utf-8")
f_antiguo.write("Esta es la primera línea.\n")
f_antiguo.write("Esta es la segunda línea.\n")
# ¡Cierre manual obligatorio!
f_antiguo.close()
print("Archivo 'antiguo.txt' creado.")


# --- 2. Añadir ('a') ---
print("\n--- Forma Antigua: Añadiendo ('a') ---")
# Volvemos a abrir, pero en modo 'a' (append)
f_antiguo = open("antiguo.txt", "a", encoding="utf-8")
f_antiguo.write("Esta línea se añadió después.\n")
# ¡Cierre manual obligatorio!
f_antiguo.close()
print("Archivo 'antiguo.txt' actualizado.")


# --- 3. Leer ('r') ---
print("\n--- Forma Antigua: Leyendo ('r') ---")
try:
    f_antiguo = open("antiguo.txt", "r", encoding="utf-8")
    contenido = f_antiguo.read()
    # ¡Cierre manual obligatorio!
    f_antiguo.close()

    print("Contenido leído:")
    print(contenido)
except FileNotFoundError:
    print("El archivo no se encontró.")

# --- 1. Escribir ('w') ---
print("\n\n--- Forma Moderna: Escribiendo ('w') ---")
# 'f' solo existe dentro de este bloque
# El archivo se cierra automáticamente al salir del bloque
with open("moderno.txt", "w", encoding="utf-8") as f:
    f.write("Esta es la primera línea.\n")
    f.write("Esta es la segunda línea.\n")
# ¡No se necesita f.close()!
print("Archivo 'moderno.txt' creado.")


# --- 2. Añadir ('a') ---
print("\n--- Forma Moderna: Añadiendo ('a') ---")
with open("moderno.txt", "a", encoding="utf-8") as f:
    f.write("Esta línea se añadió después.\n")
# ¡No se necesita f.close()!
print("Archivo 'moderno.txt' actualizado.")


# --- 3. Leer ('r') ---
print("\n--- Forma Moderna: Leyendo ('r') ---")
try:
    with open("moderno.txt", "r", encoding="utf-8") as f:
        contenido = f.read()
        # ¡No se necesita f.close()!

    print("Contenido leído:")
    print(contenido)
except FileNotFoundError:
    print("El archivo no se encontró.")
