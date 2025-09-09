# match
# Definimos una variable
estado = "pendiente"

# Usamos el 'match' para comprobar el valor
match estado:
    case "enviado":
        print("El producto está en camino.")
    case "entregado":
        print("El producto ha sido entregado.")
    case "pendiente":
        print("El pedido está pendiente de envío.")
    case _:
        print("Estado desconocido.")

# mas complejo
# Ejemplo de una orden que llega al sistema.
# Puedes cambiarla a ('agregar', 'libro', 15.99) o 'salir' para ver los otros casos.
# orden = ('borrar', 'libro_id_123')
orden = ("agregar", "libro", 34.99)

match orden:
    # Caso 1: La orden es 'salir'
    case "salir":
        print("Cerrando la aplicación.")

    # Caso 2: La orden es una tupla de 3 elementos
    case ("agregar", item, precio):
        print(f"Agregando {item} al carrito por ${precio}.")

    # Caso 3: La orden es una tupla de 2 elementos
    case ("borrar", item_id):
        print(f"Borrando el artículo con ID {item_id}.")

    # Caso 4: Ninguno de los casos anteriores coincide
    case _:
        print("Orden no reconocida.")

# Comando
comando = input("Ingresa un comando (ej: iniciar, detener, salir): ")

match comando:
    case "iniciar":
        print("Iniciando el sistema...")
        print("El sistema ya está funcionando.")

    case "detener":
        print("Deteniendo el sistema...")
        print("El sistema se ha detenido correctamente.")

    case "reiniciar":
        print("Reiniciando el sistema...")
        print("El sistema se ha reiniciado.")

    case "salir":
        print("Saliendo del programa. ¡Hasta pronto!")

    case _:
        print(f"Error: Comando '{comando}' no reconocido.")

# 1. Pedimos al usuario que ingrese los datos
try:
    num1 = float(input("Ingresa el primer número: "))
    operador = input("Ingresa el operador (+, -, *, /): ")
    num2 = float(input("Ingresa el segundo número: "))

    resultado = 0

    # 2. Usamos 'match' para seleccionar la operación
    match operador:
        case "+":
            resultado = num1 + num2
            print(f"Resultado: {resultado}")

        case "-":
            resultado = num1 - num2
            print(f"Resultado: {resultado}")

        case "*":
            resultado = num1 * num2
            print(f"Resultado: {resultado}")

        case "/":
            if num2 == 0:
                # Manejamos la división por cero aquí mismo
                print("Error: No se puede dividir por cero.")
            else:
                resultado = num1 / num2
                print(f"Resultado: {resultado}")

        case _:
            print("Error: Operador no válido.")

except ValueError:
    print("Error: Por favor, ingresa solo números para los operandos.")
