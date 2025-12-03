# 🎓 Sistema de Gestión de Alumnos (CLI)

Una aplicación de consola (CLI) construida en **Python** para gestionar una base de datos de alumnos. Permite realizar operaciones CRUD (Crear, Leer, Eliminar) de manera sencilla, interactiva y visualmente agradable gracias al uso de colores.

## 📋 Características

* **Persistencia de Datos:** Utiliza **SQLite** para guardar la información de forma permanente en un archivo local (`instituto.db`).
* **Interfaz Colorida:** Uso de la librería `colorama` para mensajes de éxito, error e información visualmente distintos.
* **Validaciones Robustas:**
    * Verificación de campos vacíos.
    * Validación de rango de edad (5 - 120 años).
    * Validación de formato de email (debe contener '@').
    * Control de duplicados (emails únicos).
* **Funcionalidades:**
    1.  Registrar nuevos alumnos.
    2.  Consultar listado completo o buscar por nombre.
    3.  Eliminar alumnos por ID (con confirmación de seguridad).

## 🛠️ Requisitos

* Python 3.x instalado.
* Librería externa: `colorama`.

## 🚀 Instalación y Configuración

Sigue estos pasos para ejecutar el proyecto en tu computadora:

1.  **Descarga o clona el proyecto** en tu carpeta de preferencia.

2.  **Instala las dependencias.**
    Abre tu terminal en la carpeta del proyecto y ejecuta:
    ```bash
    pip install -r requirements.txt
    ```
    *(Si no tienes el archivo `requirements.txt`, simplemente ejecuta: `pip install colorama`)*

3.  **Ejecuta la aplicación.**
    Inicia el programa con el siguiente comando:
    ```bash
    python app.py
    ```

## 📖 Uso

Al iniciar la aplicación, verás un menú principal con las siguientes opciones:

1.  **Registrar nuevo alumno:** Te pedirá Nombre, Apellido, Edad, Curso y Email. Si hay algún error en los datos, el sistema te avisará en rojo.
2.  **Consultar alumnos:**
    * *Opción 1:* Ver todos los alumnos registrados.
    * *Opción 2:* Buscar un alumno específico por su nombre.
3.  **Eliminar un alumno:** Te mostrará la lista de alumnos y te pedirá el **ID** del que deseas borrar. Incluye una pregunta de confirmación (S/N) para evitar accidentes.
4.  **Salir:** Cierra la aplicación de manera segura.

## 📂 Estructura del Proyecto

```text
📁 proyecto-alumnos/
│
├── app.py              # Código fuente principal de la aplicación
├── requirements.txt    # Lista de dependencias (colorama)
├── instituto.db        # Base de datos SQLite (se crea automáticamente)
└── README.md           # Este archivo de documentación

📝 Notas Adicionales

    La base de datos instituto.db se creará automáticamente la primera vez que ejecutes el programa.

    Si deseas reiniciar los datos desde cero, simplemente borra el archivo instituto.db y vuelve a ejecutar el programa.

Desarrollado con Python 🐍 y SQLite.


***

### ¿Cómo usar esto?
1.  Crea un archivo nuevo en tu carpeta llamado `README.md`.
2.  Pega el contenido de arriba.
3.  Si subes tu código a GitHub o GitLab, este texto se mostrará automáticamente com