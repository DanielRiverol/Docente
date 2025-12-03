import sqlite3
from colorama import Fore, Style, init

# Inicializar colorama
init(autoreset=True)


# Conectar o crear la base de datos e inicializar la tabla
def inicializar_db():
    conexion = sqlite3.connect("instituto.db")
    cursor = conexion.cursor()
    # Crear la tabla de alumnos
    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS alumnos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        apellido TEXT NOT NULL,
        edad INTEGER CHECK (edad >= 5 AND edad <= 120),
        curso TEXT NOT NULL,
        email TEXT UNIQUE CHECK (email LIKE '%@%')
    )
    """
    )
    conexion.commit()
    conexion.close()
    print("Base de datos y tabla de alumnos verificadas.")


def agregar_alumno():
    """
    Solicita los datos del alumno y los guarda en la base de datos,
    validando la entrada.
    """
    try:
        print(Fore.CYAN + "\n=== Registrar Nuevo Alumno ===")
        # Solicitar datos con validaciones básicas
        nombre = input("Ingresá el nombre del alumno: ").strip().capitalize()
        apellido = input("Ingresá el apellido del alumno: ").strip().capitalize()
        edad = input("Ingresá la edad del alumno: ").strip()
        curso = input("Ingresá el curso del alumno: ").strip().upper()
        email = input("Ingresá el email del alumno: ").strip().lower()

        # Validaciones
        if not nombre or not apellido or not curso:
            print(
                Fore.RED + "[ERROR] El nombre, apellido y curso no pueden estar vacíos."
            )
            return

        if not edad.isdigit() or not (5 <= int(edad) <= 120):
            print(Fore.RED + "[ERROR] La edad debe ser un número entre 5 y 120.")
            return

        if "@" not in email or " " in email:
            print(
                Fore.RED
                + "[ERROR] El email debe tener un formato válido (ejemplo@correo.com)."
            )
            return

        # Conectar e insertar
        conexion = sqlite3.connect("instituto.db")
        cursor = conexion.cursor()

        cursor.execute(
            """
            INSERT INTO alumnos (nombre, apellido, edad, curso, email)
            VALUES (?, ?, ?, ?, ?)
        """,
            (nombre, apellido, int(edad), curso, email),
        )

        conexion.commit()
        print(
            Fore.GREEN + f"[ÉXITO] Alumno {nombre} {apellido} registrado correctamente."
        )

    except sqlite3.IntegrityError:
        print(Fore.RED + "[ERROR] El email ingresado ya está registrado.")
    except sqlite3.Error as e:
        print(Fore.RED + f"[ERROR] Error en la base de datos: {e}")
    finally:
        if "conexion" in locals():
            conexion.close()


def consultar_alumnos():
    """
    Permite consultar la lista de alumnos registrados o buscar por nombre.
    """
    try:
        print(Fore.CYAN + "\n=== Consultar Alumnos ===")
        print("1. Mostrar todos los alumnos")
        print("2. Buscar alumno por nombre")
        opcion = input("Seleccioná una opción: ").strip()

        conexion = sqlite3.connect("instituto.db")
        cursor = conexion.cursor()

        if opcion == "1":
            cursor.execute(
                "SELECT id, nombre, apellido, edad, curso, email FROM alumnos"
            )
            alumnos = cursor.fetchall()

            if not alumnos:
                print(
                    Fore.YELLOW
                    + "[INFO] No hay alumnos registrados en la base de datos."
                )
            else:
                print(Fore.GREEN + "\n=== Lista de Alumnos ===")
                for alumno in alumnos:
                    print(
                        Fore.WHITE
                        + f"ID: {alumno[0]}, Nombre: {alumno[1]} {alumno[2]}, Edad: {alumno[3]}, Curso: {alumno[4]}, Email: {alumno[5]}"
                    )

        elif opcion == "2":
            nombre_busqueda = (
                input("Ingresá el nombre del alumno a buscar: ").strip().capitalize()
            )
            if not nombre_busqueda:
                print(Fore.RED + "[ERROR] El nombre no puede estar vacío.")
                return

            cursor.execute(
                "SELECT id, nombre, apellido, edad, curso, email FROM alumnos WHERE nombre = ?",
                (nombre_busqueda,),
            )
            alumnos = cursor.fetchall()

            if not alumnos:
                print(Fore.YELLOW + "[INFO] No se encontraron alumnos con ese nombre.")
            else:
                print(
                    Fore.GREEN + f"\n=== Alumnos con el nombre '{nombre_busqueda}' ==="
                )
                for alumno in alumnos:
                    print(
                        Fore.WHITE
                        + f"ID: {alumno[0]}, Nombre: {alumno[1]} {alumno[2]}, Edad: {alumno[3]}, Curso: {alumno[4]}, Email: {alumno[5]}"
                    )
        else:
            print(Fore.RED + "[ERROR] Opción no válida.")

    except sqlite3.Error as e:
        print(
            Fore.RED + f"[ERROR] Ocurrió un problema al consultar la base de datos: {e}"
        )
    finally:
        if "conexion" in locals():
            conexion.close()


def eliminar_alumno():
    """
    Permite eliminar un alumno por ID.
    """
    try:
        print(Fore.CYAN + "\n=== Eliminar Alumno ===")

        conexion = sqlite3.connect("instituto.db")
        cursor = conexion.cursor()

        # Mostrar lista breve para ayudar a elegir
        cursor.execute("SELECT id, nombre, apellido, curso FROM alumnos")
        alumnos = cursor.fetchall()

        if not alumnos:
            print(Fore.YELLOW + "[INFO] No hay alumnos registrados para eliminar.")
            return

        print(Fore.GREEN + "\n=== Lista de Alumnos ===")
        for alumno in alumnos:
            print(
                Fore.WHITE
                + f"ID: {alumno[0]}, Nombre: {alumno[1]} {alumno[2]}, Curso: {alumno[3]}"
            )

        id_alumno = input("\nIngresá el ID del alumno que querés eliminar: ").strip()

        if not id_alumno.isdigit():
            print(Fore.RED + "[ERROR] El ID ingresado no es válido.")
            return

        id_alumno = int(id_alumno)

        # Verificar existencia
        cursor.execute(
            "SELECT nombre, apellido FROM alumnos WHERE id = ?", (id_alumno,)
        )
        alumno = cursor.fetchone()

        if not alumno:
            print(Fore.YELLOW + "[INFO] No se encontró un alumno con ese ID.")
            return

        confirmacion = (
            input(
                Fore.YELLOW
                + f"¿Estás seguro de que querés eliminar a {alumno[0]} {alumno[1]}? (S/N): "
            )
            .strip()
            .lower()
        )

        if confirmacion == "s":
            cursor.execute("DELETE FROM alumnos WHERE id = ?", (id_alumno,))
            conexion.commit()
            print(
                Fore.GREEN
                + f"[ÉXITO] Alumno {alumno[0]} {alumno[1]} eliminado correctamente."
            )
        else:
            print(Fore.GREEN + "[CANCELADO] La eliminación ha sido cancelada.")

    except sqlite3.Error as e:
        print(Fore.RED + f"[ERROR] Ocurrió un problema al eliminar el alumno: {e}")
    finally:
        if "conexion" in locals():
            conexion.close()


def menu():
    """
    Menú principal del sistema.
    """
    inicializar_db()  # Aseguramos que la tabla exista al iniciar
    while True:
        print(Fore.BLUE + "\n=== Menú de Gestión de Alumnos ===")
        print(Fore.WHITE + "1. Registrar nuevo alumno")
        print(Fore.WHITE + "2. Consultar alumnos")
        print(Fore.WHITE + "3. Eliminar un alumno")
        print(Fore.WHITE + "4. Salir")

        opcion = input(Fore.CYAN + "Seleccioná una opción: ").strip()

        if opcion == "1":
            agregar_alumno()
        elif opcion == "2":
            consultar_alumnos()
        elif opcion == "3":
            eliminar_alumno()
        elif opcion == "4":
            print(Fore.GREEN + "\nGracias por usar el sistema. ¡Hasta luego!")
            break
        else:
            print(Fore.RED + "[ERROR] Opción no válida. Intentá nuevamente.")


if __name__ == "__main__":
    menu()
