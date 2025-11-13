import sqlite3
from sqlite3 import Error

# Nombre del archivo de la base de datos
DB_FILE = "empresa.db"


def crear_conexion():
    """Crea una conexión a la base de datos SQLite."""
    conexion = None
    try:
        conexion = sqlite3.connect(DB_FILE)
    except Error as e:
        print(f"Error al conectar a la base de datos: {e}")
    return conexion


def crear_tabla(conexion):
    """Crea la tabla 'empleados' si no existe."""
    # UNIQUE(email) previene que se inserten emails duplicados
    sql_crear_tabla = """
    CREATE TABLE IF NOT EXISTS empleados (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        salario REAL
    );
    """
    try:
        cursor = conexion.cursor()
        cursor.execute(sql_crear_tabla)
    except Error as e:
        print(f"Error al crear la tabla: {e}")


# --- 1. CREATE (Crear) ---
def crear_empleado(conexion, empleado_tupla):
    """
    Inserta un nuevo empleado en la tabla.
    'empleado_tupla' debe ser: (nombre, email, salario)
    """
    sql = "INSERT INTO empleados(nombre, email, salario) VALUES(?, ?, ?)"
    try:
        cursor = conexion.cursor()
        cursor.execute(sql, empleado_tupla)
        conexion.commit()  # ¡Commit es obligatorio para guardar cambios!
        print(f"Empleado '{empleado_tupla[0]}' creado con ID: {cursor.lastrowid}")
        return cursor.lastrowid
    except sqlite3.IntegrityError:
        print(f"Error: El email '{empleado_tupla[1]}' ya existe.")
        return None
    except Error as e:
        print(f"Error al crear empleado: {e}")
        return None


# --- 2. READ (Leer) ---
def leer_empleado_por_id(conexion, id_empleado):
    """
    Busca y devuelve un empleado específico por su ID.
    """
    sql = "SELECT * FROM empleados WHERE id = ?"
    try:
        cursor = conexion.cursor()
        # ¡Importante! (id_empleado,) es una tupla de un solo elemento.
        # La coma es necesaria.
        cursor.execute(sql, (id_empleado,))

        # .fetchone() obtiene la primera (y única) fila del resultado
        empleado = cursor.fetchone()

        if empleado:
            print(f"Empleado encontrado (ID {id_empleado}): {empleado}")
            return empleado
        else:
            print(f"No se encontró ningún empleado con ID {id_empleado}.")
            return None
    except Error as e:
        print(f"Error al leer por ID: {e}")


def leer_todos_los_empleados(conexion):
    """Lee y muestra todos los empleados de la tabla."""
    sql = "SELECT * FROM empleados"
    try:
        cursor = conexion.cursor()
        cursor.execute(sql)

        # .fetchall() obtiene TODAS las filas del resultado
        empleados = cursor.fetchall()

        print(f"\n--- Lista de Todos los Empleados ({len(empleados)}) ---")
        if not empleados:
            print("No hay empleados registrados.")
        else:
            for emp in empleados:
                print(emp)
        print("---------------------------------------")
        return empleados
    except Error as e:
        print(f"Error al leer todos: {e}")


# --- 3. UPDATE (Actualizar) ---
def actualizar_salario(conexion, id_empleado, nuevo_salario):
    """
    Actualiza el salario de un empleado específico.
    """
    sql = "UPDATE empleados SET salario = ? WHERE id = ?"
    try:
        cursor = conexion.cursor()
        # La tupla debe coincidir con los '?': (nuevo_salario, id_empleado)
        cursor.execute(sql, (nuevo_salario, id_empleado))
        conexion.commit()  # ¡Commit es obligatorio!

        # .rowcount nos dice cuántas filas fueron afectadas
        if cursor.rowcount > 0:
            print(
                f"¡Éxito! Salario del ID {id_empleado} actualizado a {nuevo_salario}."
            )
        else:
            print(
                f"No se encontró (o no se actualizó) ningún empleado con ID {id_empleado}."
            )
    except Error as e:
        print(f"Error al actualizar: {e}")


# --- 4. DELETE (Eliminar) ---
def eliminar_empleado(conexion, id_empleado):
    """
    Elimina un empleado específico por su ID.
    """
    sql = "DELETE FROM empleados WHERE id = ?"
    try:
        cursor = conexion.cursor()
        cursor.execute(sql, (id_empleado,))
        conexion.commit()  # ¡Commit es obligatorio!

        if cursor.rowcount > 0:
            print(f"¡Éxito! Empleado ID {id_empleado} eliminado.")
        else:
            print(
                f"No se encontró (o no se eliminó) ningún empleado con ID {id_empleado}."
            )
    except Error as e:
        print(f"Error al eliminar: {e}")


# --- Flujo principal del programa ---
if __name__ == "__main__":

    conn = crear_conexion()

    if conn:  # Solo continuamos si la conexión fue exitosa

        # Preparamos la tabla
        crear_tabla(conn)

        # --- CREATE ---
        print("\n--- (CREATE) Insertando empleados ---")
        # Creamos los datos dinámicamente (como si vinieran de un input)
        datos_carlos = ("Carlos López", "carlos@empresa.com", 50000)
        datos_laura = ("Laura Martín", "laura@empresa.com", 55000)

        id_carlos = crear_empleado(conn, datos_carlos)
        id_laura = crear_empleado(conn, datos_laura)

        # --- READ (Todos) ---
        leer_todos_los_empleados(conn)

        # --- READ (Por ID) ---
        print("\n--- (READ) Buscando a Carlos por ID ---")
        if id_carlos:
            leer_empleado_por_id(conn, id_carlos)

        # --- UPDATE ---
        print(f"\n--- (UPDATE) Aumentando el salario de Carlos (ID {id_carlos}) ---")
        if id_carlos:
            actualizar_salario(conn, id_carlos, 52000)

        # Verificamos el cambio
        if id_carlos:
            leer_empleado_por_id(conn, id_carlos)

        # --- DELETE ---
        print(f"\n--- (DELETE) Eliminando a Laura (ID {id_laura}) ---")
        if id_laura:
            eliminar_empleado(conn, id_laura)

        # --- READ (Final) ---
        print("\n--- (READ) Estado final de la base de datos ---")
        leer_todos_los_empleados(conn)

        # Cerramos la conexión
        conn.close()
        print("\nConexión cerrada.")
