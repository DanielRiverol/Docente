import sqlite3

DB_FILE = "mi_base.db"


# --- CONFIGURACIÓN INICIAL ---
def iniciar_base():
    """Crea la tabla si no existe. Abre y cierra conexión manualmente."""
    conexion = sqlite3.connect(DB_FILE)
    cursor = conexion.cursor()

    sql = """
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT,
        email TEXT,
        edad INTEGER
    );
    """
    cursor.execute(sql)
    conexion.commit()  # Guardamos cambios
    conexion.close()  # ¡Cerramos manual!


# --- FUNCIONES DEL SISTEMA ---


def agregar_usuario():
    print("\n--- AGREGAR USUARIO ---")

    # 1. Inputs dinámicos
    nombre = input("Dime el nombre: ")
    email = input("Dime el email: ")
    edad_str = input("Dime la edad: ")  # Lo leemos como texto primero

    # Validación simple para que no falle si no es numero
    if not edad_str.isdigit():
        print("Error: La edad debe ser un número.")
        return

    edad = int(edad_str)

    # 2. Diccionario
    mis_datos = {"x_nombre": nombre, "x_email": email, "x_edad": edad}

    # 3. Base de Datos (Manual)
    try:
        conexion = sqlite3.connect(DB_FILE)
        cursor = conexion.cursor()

        sql = "INSERT INTO usuarios (nombre, email, edad) VALUES (:x_nombre, :x_email, :x_edad);"
        cursor.execute(sql, mis_datos)

        conexion.commit()  # Importante guardar
        print("-> Usuario guardado.")

    except sqlite3.Error as e:
        print(f"Error de BD: {e}")
    finally:
        # Esto asegura que se cierre aunque haya error
        if conexion:
            conexion.close()


def listar_usuarios():
    print("\n--- VER USUARIOS ---")

    try:
        conexion = sqlite3.connect(DB_FILE)
        cursor = conexion.cursor()

        cursor.execute("SELECT * FROM usuarios;")
        resultados = cursor.fetchall()

        if not resultados:
            print("La base de datos está vacía.")
        else:
            for usuario in resultados:
                # usuario es (id, nombre, email, edad)
                print(f"ID: {usuario[0]} | Nombre: {usuario[1]} | Email: {usuario[2]}")

    except sqlite3.Error as e:
        print(f"Error: {e}")
    finally:
        if conexion:
            conexion.close()


def modificar_usuario():
    print("\n--- MODIFICAR EMAIL ---")
    listar_usuarios()  # Mostramos la lista para ver el ID

    id_str = input("Introduce el ID del usuario a modificar: ")
    if not id_str.isdigit():
        print("El ID debe ser número.")
        return

    nuevo_email = input("Introduce el nuevo email: ")

    # Diccionario
    mis_datos = {"filtro_id": int(id_str), "dato_email": nuevo_email}

    try:
        conexion = sqlite3.connect(DB_FILE)
        cursor = conexion.cursor()

        sql = "UPDATE usuarios SET email = :dato_email WHERE id = :filtro_id;"
        cursor.execute(sql, mis_datos)
        conexion.commit()

        if cursor.rowcount > 0:
            print("-> Usuario actualizado.")
        else:
            print("-> No encontré ese ID.")

    except sqlite3.Error as e:
        print(f"Error: {e}")
    finally:
        if conexion:
            conexion.close()


def borrar_usuario():
    print("\n--- BORRAR USUARIO ---")
    listar_usuarios()

    id_str = input("Introduce el ID del usuario a eliminar: ")
    if not id_str.isdigit():
        print("El ID debe ser número.")
        return

    # Diccionario
    mis_datos = {"id_a_borrar": int(id_str)}

    try:
        conexion = sqlite3.connect(DB_FILE)
        cursor = conexion.cursor()

        sql = "DELETE FROM usuarios WHERE id = :id_a_borrar;"
        cursor.execute(sql, mis_datos)
        conexion.commit()

        if cursor.rowcount > 0:
            print("-> Usuario eliminado.")
        else:
            print("-> No encontré ese ID.")

    except sqlite3.Error as e:
        print(f"Error: {e}")
    finally:
        if conexion:
            conexion.close()


# --- MENÚ PRINCIPAL ---


def menu_principal():
    iniciar_base()  # Aseguramos que la tabla exista al arrancar

    while True:
        print("\n=== MENU SIN WITH ===")
        print("1. Insertar")
        print("2. Ver Lista")
        print("3. Modificar")
        print("4. Borrar")
        print("5. Salir")

        opcion = input("Elige opción: ")

        if opcion == "1":
            agregar_usuario()
        elif opcion == "2":
            listar_usuarios()
        elif opcion == "3":
            modificar_usuario()
        elif opcion == "4":
            borrar_usuario()
        elif opcion == "5":
            print("Adiós.")
            break
        else:
            print("Opción incorrecta.")


if __name__ == "__main__":
    menu_principal()
