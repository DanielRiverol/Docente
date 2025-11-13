import sqlite3

# Usamos el nombre del archivo de base de datos que ya conocemos.
DB_FILE = "mi_base.db"
conexion = None

try:
    # --- 1. Configuración ---
    conexion = sqlite3.connect(DB_FILE)
    cursor = conexion.cursor()

    # Nos aseguramos de que la tabla exista
    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY,
        nombre TEXT,
        email TEXT,
        edad INTEGER
    );
    """
    )
    print("Base de datos y tabla 'usuarios' listas.")

    # --- 2. OBTENER DATOS DINÁMICOS DEL USUARIO ---
    # Esto es código Python normal. Las variables son dinámicas.
    print("\n--- Ingrese los datos del nuevo usuario ---")

    nombre_in = input("Nombre del usuario: ")
    email_in = input("Email del usuario: ")
    edad_in = int(input("Edad del usuario: "))  # (Manejaremos el error con try)

    # --- 3. MÉTODO 1: Creando la TUPLA dinámicamente ---
    # Este es el método que te generaba dudas

    print("\n--- Insertando con el método de TUPLA (?) ---")

    sql_tupla = "INSERT INTO usuarios (nombre, email, edad) VALUES (?, ?, ?);"

    # --- ¡AQUÍ ESTÁ LA CLAVE! ---
    # No "convertimos" nada.
    # Simplemente "creamos" una tupla nueva usando las variables que ya tenemos.
    # Python lo hace al instante.
    datos_en_tupla = (nombre_in, email_in, edad_in)
    # --------------------------------

    print(f"SQL: {sql_tupla}")
    print(f"Datos empaquetados: {datos_en_tupla}")

    cursor.execute(sql_tupla, datos_en_tupla)
    conexion.commit()
    print(f"¡Éxito! Usuario '{nombre_in}' insertado con una tupla.")

    # --- 4. MÉTODO 2: Creando el DICCIONARIO dinámicamente ---
    # Para demostrar que el proceso es idéntico,
    # pidamos datos para otro usuario.

    print("\n--- Ingrese los datos de OTRO usuario ---")
    nombre_in_2 = input("Nombre del usuario: ")
    email_in_2 = input("Email del usuario: ")
    edad_in_2 = int(input("Edad del usuario: "))

    print("\n--- Insertando con el método de DICCIONARIO (:) ---")

    sql_dict = "INSERT INTO usuarios (nombre, email, edad) VALUES (:nom, :mail, :age);"

    # --- ¡EL PROCESO ES EL MISMO! ---
    # "Creamos" un diccionario nuevo usando las variables.
    datos_en_dict = {"nom": nombre_in_2, "mail": email_in_2, "age": edad_in_2}
    # ---------------------------------

    print(f"SQL: {sql_dict}")
    print(f"Datos empaquetados: {datos_en_dict}")

    cursor.execute(sql_dict, datos_en_dict)
    conexion.commit()
    print(f"¡Éxito! Usuario '{nombre_in_2}' insertado con un diccionario.")


except ValueError:
    print("\n¡ERROR! La edad debe ser un número.")
except sqlite3.Error as e:
    print(f"\n¡ERROR de SQLite! {e}")
finally:
    if conexion:
        # Mostramos los resultados finales
        print("\n--- Contenido final de la base de datos ---")
        for fila in cursor.execute("SELECT * FROM usuarios"):
            print(f"  {fila}")

        conexion.close()
        print("-----------------------------------------")
        print("Conexión cerrada.")
