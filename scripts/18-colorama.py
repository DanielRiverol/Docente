# Importamos las herramientas específicas que queremos de colorama
from colorama import Fore, Back, Style, init


# -----------------------------------------------------------------
# ¡MUY IMPORTANTE! Debes inicializar colorama
# -----------------------------------------------------------------
# Con autoreset=True, Python vuelve al color normal
# automáticamente después de cada 'print'. ¡Es muy útil!
init(autoreset=True)

print("Este es texto normal, como siempre.")

# -----------------------------------------------------------------
# Fore (Foreground) = Cambia el color del texto
# -----------------------------------------------------------------
print(Fore.RED + "¡Este texto es ROJO!")
print(Fore.GREEN + "Este texto es VERDE.")
print(Fore.CYAN + "Este texto es CYAN.")

# -----------------------------------------------------------------
# Back (Background) = Cambia el color del fondo
# -----------------------------------------------------------------
print(Back.YELLOW + "Este texto tiene fondo AMARILLO.")
print(Back.MAGENTA + "Este texto tiene fondo MAGENTA.")

# -----------------------------------------------------------------
# Style = Cambia el estilo (brillo)
# -----------------------------------------------------------------
print(Style.BRIGHT + Fore.GREEN + "¡Este texto es VERDE y BRILLANTE!")
print(Style.DIM + Fore.WHITE + "Este texto es blanco y atenuado (dim).")

# Como usamos init(autoreset=True), este print vuelve a ser normal
print("Este texto es normal otra vez.")


