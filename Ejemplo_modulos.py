# -----------------------------------------------------------------
# PASO 1: DEFINICIÓN DE LAS FUNCIONES SEGURAS
# -----------------------------------------------------------------


def suma(a, b):
    """Suma dos números, maneja errores de tipo."""
    try:
        return a + b
    except TypeError:
        return "Error: No se puede sumar. Verifique los tipos de datos."


def resta(a, b):
    """Resta dos números, maneja errores de tipo."""
    try:
        return a - b
    except TypeError:
        return "Error: No se puede restar. Verifique los tipos de datos."


def multiplicacion(a, b):
    """Multiplica dos números, maneja errores de tipo."""
    try:
        return a * b
    except TypeError:
        return "Error: No se puede multiplicar. Verifique los tipos de datos."


def division(a, b):
    """Divide dos números, maneja múltiples errores."""
    try:
        # Código "arriesgado"
        return a / b
    except TypeError:
        # Plan B para TypeError
        return "Error: No se puede dividir. Verifique los tipos de datos."
    except ZeroDivisionError:
        # Plan C para ZeroDivisionError
        return "Error: No se puede dividir por cero."


# -----------------------------------------------------------------
# PASO 2: EJECUCIÓN PRINCIPAL CON MENÚ
# -----------------------------------------------------------------
# Este bloque solo se ejecuta si corremos este archivo directamente.
if __name__ == "__main__":

    while True:  # Bucle infinito para que el menú siga apareciendo

        # --- El Menú ---
        print("\n==============================")
        print("   CALCULADORA SEGURA v1.0    ")
        print("==============================")
        print("1: Sumar")
        print("2: Restar")
        print("3: Multiplicar")
        print("4: Dividir")
        print("5: Salir")
        print("------------------------------")

        opcion = input("Elige una opción (1-5): ")

        # --- Lógica de Salida ---
        if opcion == "5":
            print("¡Gracias por usar la calculadora! Adiós.")
            break  # Rompe el bule 'while True'

        # --- Validación de opción (si no es 1-4) ---
        if opcion not in ("1", "2", "3", "4"):
            print("Opción no válida. Por favor, elige un número del 1 al 5.")
            continue  # Salta esta iteración, vuelve al inicio del 'while'

        # --- Entrada de Números (con su propio try...except) ---
        try:
            # Usamos float() para permitir números decimales
            num1_str = input("Ingresa el primer número: ")
            num1 = float(num1_str)

            num2_str = input("Ingresa el segundo número: ")
            num2 = float(num2_str)

        except ValueError:
            # Esto se activa si float() falla (ej. si escriben 'hola')
            print("\n¡Error de Entrada! Debes ingresar solo números.")
            print(f"Ingresaste '{num1_str}' y '{num2_str}'. Inténtalo de nuevo.")
            continue  # Vuelve al inicio del menú

        # --- Procesamiento y Salida ---
        resultado = None  # Variable para guardar el resultado

        if opcion == "1":
            resultado = suma(num1, num2)
        elif opcion == "2":
            resultado = resta(num1, num2)
        elif opcion == "3":
            resultado = multiplicacion(num1, num2)
        elif opcion == "4":
            resultado = division(num1, num2)

        # Imprimimos el resultado (que puede ser el número o el mensaje de error)
        print(f"\n--- Resultado de la operación: {resultado} ---")
