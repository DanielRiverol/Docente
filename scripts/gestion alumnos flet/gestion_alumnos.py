import flet as ft
import sqlite3
import os

# --- 1. CONFIGURACIÓN DE BASE DE DATOS ---
ruta_documentos = os.path.expanduser("~/Documents")
DB_FILE = os.path.join(ruta_documentos, "instituto_flet.db")


def obtener_conexion():
    return sqlite3.connect(DB_FILE)


def inicializar_bd():
    try:
        with obtener_conexion() as conn:
            cursor = conn.cursor()
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
    except sqlite3.Error as e:
        print(f"Error inicializando BD: {e}")


# --- 2. LÓGICA CRUD (BACKEND) ---


def db_insertar(datos):
    try:
        with obtener_conexion() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                INSERT INTO alumnos (nombre, apellido, edad, curso, email)
                VALUES (:nombre, :apellido, :edad, :curso, :email)
            """,
                datos,
            )
            return True, "Alumno registrado correctamente."
    except sqlite3.IntegrityError:
        return False, "Error: El email ya está registrado."
    except sqlite3.Error as e:
        return False, f"Error de base de datos: {e}"


def db_obtener_todos():
    try:
        with obtener_conexion() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM alumnos")
            return cursor.fetchall()
    except sqlite3.Error:
        return []


def db_buscar_alumno(texto):
    """Busca por nombre O apellido que contenga el texto."""
    try:
        with obtener_conexion() as conn:
            cursor = conn.cursor()
            sql = "SELECT * FROM alumnos WHERE nombre LIKE ? OR apellido LIKE ?"
            parametro = f"%{texto}%"
            cursor.execute(sql, (parametro, parametro))
            return cursor.fetchall()
    except sqlite3.Error:
        return []


def db_eliminar(id_alumno):
    try:
        with obtener_conexion() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM alumnos WHERE id = ?", (id_alumno,))
            if cursor.rowcount > 0:
                return True, "Alumno eliminado."
            else:
                return False, "No se encontró ese ID."
    except sqlite3.Error as e:
        return False, f"Error al eliminar: {e}"


# --- 3. INTERFAZ GRÁFICA (FRONTEND FLET) ---


def main(page: ft.Page):
    page.title = "Gestión Instituto"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window_width = 950
    page.window_height = 750
    page.scroll = "adaptive"

    inicializar_bd()

    def mostrar_mensaje(texto, color=ft.Colors.GREEN):
        page.snack_bar = ft.SnackBar(ft.Text(texto), bgcolor=color)
        page.snack_bar.open = True
        page.update()

    # --- Funciones de Eventos (Definidas antes de usarlas) ---

    def cargar_tabla(datos_filtrados=None):
        tabla.rows.clear()
        if datos_filtrados is not None:
            datos = datos_filtrados
        else:
            datos = db_obtener_todos()

        for row in datos:
            tabla.rows.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(str(row[0]))),
                        ft.DataCell(ft.Text(row[1])),
                        ft.DataCell(ft.Text(row[2])),
                        ft.DataCell(ft.Text(str(row[3]))),
                        ft.DataCell(ft.Text(row[4])),
                        ft.DataCell(ft.Text(row[5])),
                    ]
                )
            )
        page.update()

    def click_buscar(e):
        texto = txt_buscar.value.strip()
        if not texto:
            mostrar_mensaje("Escribe algo para buscar", ft.Colors.ORANGE)
            cargar_tabla()
            return

        resultados = db_buscar_alumno(texto)
        if resultados:
            cargar_tabla(resultados)
            mostrar_mensaje(
                f"Se encontraron {len(resultados)} coincidencias", ft.Colors.BLUE
            )
        else:
            cargar_tabla([])
            mostrar_mensaje("No se encontraron coincidencias", ft.Colors.RED)

    def click_ver_todos(e):
        txt_buscar.value = ""
        cargar_tabla()
        page.update()

    def click_registrar(e):
        if not txt_nombre.value or not txt_apellido.value or not txt_curso.value:
            mostrar_mensaje("Faltan datos obligatorios", ft.Colors.RED)
            return

        try:
            edad_num = int(txt_edad.value)
            if not (5 <= edad_num <= 120):
                mostrar_mensaje("Edad inválida", ft.Colors.RED)
                return
        except ValueError:
            mostrar_mensaje("La edad debe ser número", ft.Colors.RED)
            return

        if "@" not in txt_email.value:
            mostrar_mensaje("Email inválido", ft.Colors.RED)
            return

        datos = {
            "nombre": txt_nombre.value.strip().capitalize(),
            "apellido": txt_apellido.value.strip().capitalize(),
            "edad": edad_num,
            "curso": txt_curso.value.strip().upper(),
            "email": txt_email.value.strip().lower(),
        }

        exito, mensaje = db_insertar(datos)

        if exito:
            mostrar_mensaje(mensaje, ft.Colors.GREEN)
            txt_nombre.value = ""
            txt_apellido.value = ""
            txt_edad.value = ""
            txt_curso.value = ""
            txt_email.value = ""
            cargar_tabla()
        else:
            mostrar_mensaje(mensaje, ft.Colors.RED)

    def click_eliminar(e):
        if not txt_id_eliminar.value:
            return
        try:
            id_borrar = int(txt_id_eliminar.value)
            exito, mensaje = db_eliminar(id_borrar)
            if exito:
                mostrar_mensaje(mensaje, ft.Colors.ORANGE)
                txt_id_eliminar.value = ""
                cargar_tabla()
            else:
                mostrar_mensaje(mensaje, ft.Colors.RED)
        except ValueError:
            mostrar_mensaje("El ID debe ser número", ft.Colors.RED)

    # --- Definición de Campos ---

    txt_nombre = ft.TextField(label="Nombre", expand=1)
    txt_apellido = ft.TextField(label="Apellido", expand=1)
    txt_edad = ft.TextField(
        label="Edad", width=100, keyboard_type=ft.KeyboardType.NUMBER
    )
    txt_curso = ft.TextField(label="Curso", width=250)
    txt_email = ft.TextField(label="Email", width=400)
    txt_id_eliminar = ft.TextField(
        label="ID a Eliminar", width=120, keyboard_type=ft.KeyboardType.NUMBER
    )

    # --- CAMBIO AQUÍ: Campo de búsqueda limpio ---
    # 1. Quitamos suffix_icon=ft.Icons.SEARCH
    # 2. Agregamos on_submit=click_buscar (Para buscar al dar Enter)
    txt_buscar = ft.TextField(
        label="Buscar por Nombre o Apellido", expand=True, on_submit=click_buscar
    )

    tabla = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("ID")),
            ft.DataColumn(ft.Text("Nombre")),
            ft.DataColumn(ft.Text("Apellido")),
            ft.DataColumn(ft.Text("Edad"), numeric=True),
            ft.DataColumn(ft.Text("Curso")),
            ft.DataColumn(ft.Text("Email")),
        ],
        rows=[],
    )

    # --- Diseño de la Pantalla (Layout) ---

    page.add(
        ft.Text(
            "Sistema de Gestión Escolar", size=30, weight="bold", color=ft.Colors.BLUE
        ),
        # Panel de Registro
        ft.Container(
            content=ft.Column(
                [
                    ft.Text("Registrar Nuevo Alumno", weight="bold"),
                    ft.Row([txt_nombre, txt_apellido, txt_edad]),
                    ft.Row([txt_curso, txt_email]),
                    ft.ElevatedButton(
                        "Guardar Alumno",
                        on_click=click_registrar,
                        bgcolor=ft.Colors.BLUE,
                        color=ft.Colors.WHITE,
                    ),
                ]
            ),
            padding=10,
            border=ft.border.all(1, ft.Colors.GREY_300),
            border_radius=10,
        ),
        ft.Divider(),
        # Panel Búsqueda y Eliminar
        ft.Row(
            [
                # Búsqueda
                ft.Column(
                    [
                        ft.Text("Buscar Alumno", weight="bold"),
                        ft.Row(
                            [
                                txt_buscar,
                                # El botón se mantiene aquí, pero la caja de texto ya no tiene icono repetido
                                ft.IconButton(
                                    icon=ft.Icons.SEARCH,
                                    on_click=click_buscar,
                                    tooltip="Buscar",
                                ),
                                ft.IconButton(
                                    icon=ft.Icons.REFRESH,
                                    on_click=click_ver_todos,
                                    tooltip="Ver Todos",
                                ),
                            ],
                            width=400,
                        ),
                    ]
                ),
                ft.VerticalDivider(),
                # Eliminar
                ft.Column(
                    [
                        ft.Text("Eliminar", weight="bold"),
                        ft.Row(
                            [
                                txt_id_eliminar,
                                ft.ElevatedButton(
                                    "Borrar",
                                    on_click=click_eliminar,
                                    bgcolor=ft.Colors.RED,
                                    color=ft.Colors.WHITE,
                                ),
                            ]
                        ),
                    ]
                ),
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        ),
        ft.Divider(),
        ft.Text("Resultados:", size=20, weight="bold"),
        tabla,
    )

    cargar_tabla()


if __name__ == "__main__":
    ft.app(target=main)
