# Para usar fechas y horas, importamos las "clases" específicas
# que necesitamos del módulo 'datetime'.
from datetime import datetime, date, timedelta

# -----------------------------------------------------------------
# EJEMPLO 1: datetime.now() - La fecha y hora actuales
# -----------------------------------------------------------------
# Propósito: Obtener el momento exacto en que se ejecuta esta línea.
# Devuelve un objeto 'datetime' que contiene todo.

print("--- Ejemplo 1: Fecha y Hora Actuales (datetime.now()) ---")

# Obtenemos el momento actual
ahora = datetime.now()

print(f"Objeto 'datetime' completo: {ahora}")

# Podemos acceder a cada parte individualmente
print(f"Año:    {ahora.year}")
print(f"Mes:    {ahora.month}")
print(f"Día:    {ahora.day}")
print(f"Hora:   {ahora.hour}")
print(f"Minuto: {ahora.minute}")
print(f"Segundo:{ahora.second}")

# También podemos obtener solo la fecha de "hoy" (sin la hora)
hoy = date.today()
print(f"\nObjeto 'date' de hoy: {hoy}")
print(f"El año de hoy es: {hoy.year}")


# -----------------------------------------------------------------
# EJEMPLO 2: Creando una fecha específica
# -----------------------------------------------------------------
# Propósito: Crear un objeto 'date' o 'datetime' para una fecha
# que nosotros definamos (ej. un cumpleaños, la fecha de un evento).

print("\n--- Ejemplo 2: Crear una Fecha Específica ---")

# Creamos una fecha usando: date(año, mes, día)
fecha_evento = date(2025, 12, 25)  # Navidad 2025

print(f"La fecha del evento es: {fecha_evento}")
print(f"El mes del evento es: {fecha_evento.month}")

# También podemos crear una fecha con hora específica:
# datetime(año, mes, día, hora, minuto, segundo)
inicio_evento = datetime(2026, 1, 1, 9, 30, 0)  # 1 de Enero 2026 a las 9:30 AM
print(f"El evento iniciará: {inicio_evento}")


# -----------------------------------------------------------------
# EJEMPLO 3: strftime() - Formatear una fecha a un string
# -----------------------------------------------------------------
# Propósito: Convertir un objeto 'datetime' (que Python entiende)
# a un 'string' (texto) legible para humanos.

print("\n--- Ejemplo 3: Formatear Fechas (strftime) ---")

# Usamos la variable 'ahora' del Ejemplo 1
fecha_para_mostrar = datetime.now()

# Formatos comunes:
# %Y = Año con 4 dígitos (ej. 2025)
# %m = Mes como número (ej. 11)
# %d = Día del mes (ej. 04)
# %H = Hora (formato 24h)
# %M = Minutos
# %A = Nombre del día (ej. Tuesday)
# %B = Nombre del mes (ej. November)

formato_iso = fecha_para_mostrar.strftime("%Y-%m-%d")
print(f"Formato ISO (ideal para bases de datos): {formato_iso}")

formato_latam = fecha_para_mostrar.strftime("%d/%m/%Y")
print(f"Formato LATAM: {formato_latam}")

formato_eeuu = fecha_para_mostrar.strftime("%m-%d-%Y %H:%M")
print(f"Formato EEUU (con hora): {formato_eeuu}")

formato_largo = fecha_para_mostrar.strftime("Hoy es %A, %d de %B de %Y")
print(f"Formato Largo (amigable): {formato_largo}")


# -----------------------------------------------------------------
# EJEMPLO 4: timedelta - Aritmética de Fechas
# -----------------------------------------------------------------
# Propósito: Calcular la diferencia entre dos fechas, o sumar
# y restar tiempo a una fecha.

print("\n--- Ejemplo 4: Aritmética de Fechas (timedelta) ---")

# Usemos las variables de ejemplos anteriores:
hoy = date.today()
navidad = date(hoy.year, 12, 25)  # Navidad de este año

# ¿Qué pasa si la Navidad de este año ya pasó?
if hoy > navidad:
    # Si ya pasó, calculamos la Navidad del próximo año
    navidad = date(hoy.year + 1, 12, 25)
    print("La Navidad de este año ya pasó. Calculando para el próximo año.")

# Calculamos la diferencia (resta de fechas)
# El resultado es un objeto 'timedelta'
diferencia = navidad - hoy

print(f"Fecha de hoy: {hoy}")
print(f"Fecha de Navidad: {navidad}")
print(f"Diferencia (objeto timedelta): {diferencia}")

# 'timedelta' tiene propiedades, la más útil es .days
print(f"¡Faltan {diferencia.days} días para Navidad!")

# También podemos sumar tiempo (ej. qué fecha será en 7 días)
en_una_semana = hoy + timedelta(days=7)
print(f"La fecha en una semana será: {en_una_semana}")

hace_30_dias = hoy - timedelta(days=30)
print(f"La fecha hace 30 días fue: {hace_30_dias}")
