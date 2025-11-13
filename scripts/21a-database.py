import sqlite3

# Usamos el nombre del archivo de base de datos que ya conocemos.
DB_FILE = "mi_base.db"
conexion = None

print("--- Demo de Marcadores Posicional (Tupla) vs. Nombrado (Diccionario) ---")

try:
    # --- 1. Configuración Inicial ---
    # Nos conectamos al archivo físico
    conexion = sqlite3.connect(DB_FILE)
    cursor = conexion.cursor()
    print(f"Conexión al archivo '{DB_FILE}' establecida.")

    # Creamos la tabla (IF NOT EXISTS es seguro de ejecutar múltiples veces)
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
    print("Tabla 'usuarios' asegurada (creada si no existía).")

    # --- 2. MÉTODO 1: Posicional (?) con TUPLA ---
    # El orden importa.

    print("\n--- MÉTODO 1: Insertando con Marcador Posicional (?) y Tupla ---")

    sql_posicional = "INSERT INTO usuarios (nombre, email, edad) VALUES (?, ?, ?);"

    # Los datos en una tupla, en el orden correcto
    datos_ana = ("Ana García", "ana@correo.com", 28)

    print(f"SQL: {sql_posicional}")
    print(f"Datos: {datos_ana}")

    cursor.execute(sql_posicional, datos_ana)
    print("-> Usuario 'Ana' insertado.")

    # --- 3. MÉTODO 2: Nombrado (:) con DICCIONARIO ---
    # El orden NO importa, solo los nombres de las llaves.

    print("\n--- MÉTODO 2: Insertando con Marcador Nombrado (:) y Diccionario ---")

    sql_nombrado = "INSERT INTO usuarios (nombre, email, edad) VALUES (:el_nombre, :el_email, :la_edad);"

    # Los datos en un diccionario.
    datos_luis = {
        "la_edad": 35,
        "el_nombre": "Luis Pérez",
        "el_email": "luis@correo.com",
    }

    print(f"SQL: {sql_nombrado}")
    print(f"Datos: {datos_luis}")

    cursor.execute(sql_nombrado, datos_luis)
    print("-> Usuario 'Luis' insertado.")

    # --- 4. Guardar y Verificar ---
    print("\nGuardando cambios (commit)...")
    conexion.commit()

    print("\n--- Verificando todos los datos en la BD ---")
    cursor.execute("SELECT * FROM usuarios;")

    resultados = cursor.fetchall()

    for usuario in resultados:
        # usuario es una tupla: (id, nombre, email, edad)
        print(
            f"  ID: {usuario[0]}, Nombre: {usuario[1]}, Email: {usuario[2]}, Edad: {usuario[3]}"
        )

    print("---------------------------------------------")

except sqlite3.Error as e:
    print(f"¡Error de SQLite! {e}")
finally:
    if conexion:
        conexion.close()
        print("Conexión cerrada.")
