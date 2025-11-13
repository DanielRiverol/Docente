import sqlite3

# Nombre del archivo que contendrá nuestra base de datos
DB_FILE = "mi_base_de_datos.db"

# Es crucial inicializar la conexión como 'None'
# para que el bloque 'finally' funcione correctamente.
conexion = None

try:
    # --- 1. CONECTARSE ---
    # Esto crea el archivo 'mi_base_de_datos.db' si no existe
    # y se conecta a él.
    conexion = sqlite3.connect(DB_FILE)
    print(f"¡Éxito! Conexión establecida con '{DB_FILE}'")

    # --- 2. CREAR UN CURSOR ---
    # El "cursor" es el objeto que usamos para enviar comandos SQL.
    cursor = conexion.cursor()
    print("Cursor creado.")

    # --- 3. COMANDO SQL: CREATE TABLE ---
    # Vamos a crear una tabla para guardar estudiantes.
    # 'IF NOT EXISTS' es útil: evita un error si la tabla ya existe.
    print("\nEjecutando comando CREATE TABLE...")
    comando_crear_tabla = """
    CREATE TABLE IF NOT EXISTS estudiantes (
        id INTEGER PRIMARY KEY,
        nombre TEXT NOT NULL,
        promedio REAL
    );
    """
    cursor.execute(comando_crear_tabla)
    print("Tabla 'estudiantes' creada (o ya existía).")

    # --- 4. COMANDO SQL: INSERT INTO ---
    # Ahora, insertemos algunos datos.
    # Usamos '?' como marcadores de posición (placeholders)
    # para pasar los datos de forma segura.
    print("Ejecutando comando INSERT...")

    comando_insertar = "INSERT INTO estudiantes (nombre, promedio) VALUES (?, ?);"

    datos_ana = ("Ana García", 9.5)
    datos_luis = ("Luis Martínez", 8.2)

    cursor.execute(comando_insertar, datos_ana)
    cursor.execute(comando_insertar, datos_luis)
    print("Datos insertados.")

    # --- 5. GUARDAR LOS CAMBIOS (COMMIT) ---
    # ¡NADA se guarda permanentemente hasta que haces 'commit'!
    conexion.commit()
    print("Cambios guardados (commit) en la base de datos.")

    # --- 6. COMANDO SQL: SELECT (Consultar) ---
    # Ahora, leamos los datos que acabamos de guardar.
    print("\nEjecutando comando SELECT * ...")
    comando_seleccionar = "SELECT * FROM estudiantes;"

    cursor.execute(comando_seleccionar)

    # .fetchall() (buscar todos) obtiene los resultados como una lista de tuplas.
    estudiantes = cursor.fetchall()

    print("\n--- INICIO DE RESULTADOS ---")
    for estudiante in estudiantes:
        # Cada 'estudiante' es una tupla: (id, nombre, promedio)
        print(estudiante)
    print("--- FIN DE RESULTADOS ---")


except sqlite3.Error as e:
    # Si ocurre CUALQUIER error de base de datos...
    print(f"\n¡ERROR! Ocurrió un error de SQLite: {e}")

finally:
    # --- 7. CERRAR LA CONEXIÓN ---
    # Este bloque 'finally' se ejecuta SIEMPRE.
    # (Incluso si hubo un error en el 'try').
    if conexion:
        conexion.close()
        print("\nConexión cerrada de forma segura.")
