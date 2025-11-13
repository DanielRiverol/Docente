# 1. Importar la biblioteca
import sqlite3
from sqlite3 import Error  # Importar la clase de Error para mejor manejo

# --- CONSTANTE PARA EL NOMBRE DEL ARCHIVO ---
DATABASE_FILE = "mi_primera_base.db"


def crear_conexion():
    """
    Crea una conexión a la base de datos SQLite
    especificada por DATABASE_FILE
    """
    conexion = None
    try:
        # 2. Conectar. Esto crea el archivo .db si no existe
        conexion = sqlite3.connect(DATABASE_FILE)
    except Error as e:
        print(f"Error al conectar a la base de datos: {e}")

    return conexion


def ejecutar_sql(conexion, sql_comando):
    """
    Función genérica para ejecutar comandos SQL (como CREATE TABLE)
    """
    try:
        # 3. Crear un Cursor
        cursor = conexion.cursor()

        # 4. Ejecutar el comando
        cursor.execute(sql_comando)

    except Error as e:
        print(f"Error al ejecutar el comando: {e}")


def insertar_usuario(conexion, usuario_tupla):
    """
    Inserta un nuevo usuario en la tabla 'usuarios'
    """
    sql_insert = """
    INSERT INTO usuarios(nombre, email, edad) 
    VALUES(?, ?, ?)
    """

    try:
        cursor = conexion.cursor()
        cursor.execute(sql_insert, usuario_tupla)

        # 4b. Guardar (commit) los cambios
        conexion.commit()
        return cursor.lastrowid  # Devolvemos el ID del usuario insertado

    except Error as e:
        print(f"Error al insertar datos: {e}")
        return None


def consultar_usuarios(conexion):
    """
    Consulta todos los usuarios de la tabla 'usuarios'
    """
    sql_select = "SELECT * FROM usuarios"

    try:
        cursor = conexion.cursor()
        cursor.execute(sql_select)
        filas = cursor.fetchall()

        print("\n--- 📋 Consulta de Usuarios Actuales ---")
        if not filas:
            print("No hay usuarios en la tabla.")
        else:
            # Recorremos las filas (que son listas de tuplas)
            for fila in filas:
                # fila es una tupla: (id, nombre, email, edad)
                print(
                    f"ID: {fila[0]}, Nombre: {fila[1]}, Email: {fila[2]}, Edad: {fila[3]}"
                )
        print("---------------------------------------")

    except Error as e:
        print(f"Error al consultar datos: {e}")


# --- ¡NUEVA FUNCIÓN! ---
def actualizar_edad_usuario(conexion, id_usuario, nueva_edad):
    """
    Actualiza la edad de un usuario específico usando su ID.
    Usa el comando UPDATE.
    """
    # Usamos '?' para protegernos de inyección SQL
    sql_update = """
    UPDATE usuarios
    SET edad = ? 
    WHERE id = ?
    """

    try:
        cursor = conexion.cursor()
        # ¡El orden en la tupla (nueva_edad, id_usuario) debe
        # coincidir con los '?' en el comando SQL!
        cursor.execute(sql_update, (nueva_edad, id_usuario))
        conexion.commit()

        # .rowcount nos dice cuántas filas fueron afectadas
        if cursor.rowcount > 0:
            print(
                f"¡Éxito! Edad del usuario ID {id_usuario} actualizada a {nueva_edad}."
            )
        else:
            print(f"No se encontró ningún usuario con ID {id_usuario}.")

    except Error as e:
        print(f"Error al actualizar datos: {e}")


# --- ¡NUEVA FUNCIÓN! ---
def eliminar_usuario(conexion, id_usuario):
    """
    Elimina un usuario específico usando su ID.
    Usa el comando DELETE.
    """
    sql_delete = "DELETE FROM usuarios WHERE id = ?"

    try:
        cursor = conexion.cursor()
        # (id_usuario,) -> La coma es importante para que sea una tupla
        cursor.execute(sql_delete, (id_usuario,))
        conexion.commit()

        if cursor.rowcount > 0:
            print(f"¡Éxito! Usuario ID {id_usuario} eliminado.")
        else:
            print(f"No se encontró ningún usuario con ID {id_usuario}.")

    except Error as e:
        print(f"Error al eliminar datos: {e}")


# --- ¡NUEVA FUNCIÓN! ---
def consultar_estadisticas(conexion):
    """
    Realiza varias consultas COUNT para obtener estadísticas.
    """
    print("\n--- 📊 Estadísticas de Usuarios ---")
    try:
        cursor = conexion.cursor()

        # 1. Conteo total
        sql_total = "SELECT COUNT(*) FROM usuarios"
        cursor.execute(sql_total)
        # .fetchone() obtiene el primer (y único) resultado
        # El resultado es una tupla, ej: (5,). Accedemos al primer
        # elemento [0] para obtener el número.
        total = cursor.fetchone()[0]
        print(f"Total de usuarios: {total}")

        # 2. Conteo de menores (asumiendo < 18)
        sql_menores = "SELECT COUNT(*) FROM usuarios WHERE edad < 18"
        cursor.execute(sql_menores)
        menores = cursor.fetchone()[0]
        print(f"Usuarios menores de edad (< 18): {menores}")

        # 3. Conteo de mayores (asumiendo >= 18)
        sql_mayores = "SELECT COUNT(*) FROM usuarios WHERE edad >= 18"
        cursor.execute(sql_mayores)
        mayores = cursor.fetchone()[0]
        print(f"Usuarios mayores de edad (>= 18): {mayores}")

        print("---------------------------------")

    except Error as e:
        print(f"Error al consultar estadísticas: {e}")


# --- Punto de entrada principal del programa ---
if __name__ == "__main__":

    sql_crear_tabla_usuarios = """
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        edad INTEGER
    );
    """

    # Conectamos
    conn = crear_conexion()

    if conn:
        print(f"Conexión establecida a {DATABASE_FILE}.")

        # 1. Crear la tabla (no falla si ya existe)
        ejecutar_sql(conn, sql_crear_tabla_usuarios)

        # 2. Insertar datos (solo si no existen, para evitar errores UNIQUE)
        # Vamos a insertar 3 usuarios para que las estadísticas sean interesantes
        print("\nInsertando usuarios (solo si no existen)...")
        id_ana = insertar_usuario(conn, ("Ana García", "ana@ejemplo.com", 28))
        id_luis = insertar_usuario(conn, ("Luis Pérez", "luis@ejemplo.com", 35))
        id_carlos = insertar_usuario(
            conn, ("Carlos Solis", "carlos@ejemplo.com", 16)
        )  # Un menor de edad

        # 3. Consultar estado inicial
        consultar_usuarios(conn)

        # 4. Actualizar un dato (UPDATE)
        # Vamos a actualizar la edad de Ana (asumiendo que su ID es 1)
        if id_ana:  # Solo si se insertó correctamente
            print(f"\nActualizando edad de Ana (ID: {id_ana})...")
            actualizar_edad_usuario(conn, id_ana, 29)

        # 5. Eliminar un dato (DELETE)
        # Vamos a eliminar a Luis (asumiendo que su ID es 2)
        if id_luis:  # Solo si se insertó correctamente
            print(f"\nEliminando a Luis (ID: {id_luis})...")
            eliminar_usuario(conn, id_luis)

        # 6. Consultar estado final
        print("\nConsultando estado final de la base de datos...")
        consultar_usuarios(conn)

        # 7. Consultar estadísticas (COUNT)
        consultar_estadisticas(conn)

        # 8. Cerrar la conexión
        conn.close()
        print("\nConexión cerrada.")
