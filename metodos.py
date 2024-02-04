def texto_color(texto: str, color: str):
    colores = "\033[39m {}\033[00m"
    if color == "negro":
        colores = "\033[30m {}\033[00m"
    elif color == "rojo_oscuro":
        colores = "\033[31m {}\033[00m"
    elif color == "verde_oscuro":
        colores = "\033[32m {}\033[00m"
    elif color == "amarillo_oscuro":
        colores = "\033[33m {}\033[00m"
    elif color == "azul_oscuro":
        colores = "\033[34m {}\033[00m"
    elif color == "magenta_oscuro":
        colores = "\033[35m {}\033[00m"
    elif color == "cyan_oscuro":
        colores = "\033[36m {}\033[00m"
    elif color == "gris":
        colores = "\033[37m {}\033[00m"
    elif color == "gris_oscuro":
        colores = "\033[90m {}\033[00m"
    elif color == "rojo":
        colores = "\033[91m {}\033[00m"
    elif color == "verde":
        colores = "\033[92m {}\033[00m"
    elif color == "amarillo":
        colores = "\033[93m {}\033[00m"
    elif color == "azul":
        colores = "\033[94m {}\033[00m"
    elif color == "magenta":
        colores = "\033[95m {}\033[00m"
    elif color == "cyan":
        colores = "\033[96m {}\033[00m"
    elif color == "blanco":
        colores = "\033[97m {}\033[00m"
    return colores.format(texto)

def texto_es_numero(valor):
    while True:
        try:
            numero=int(valor)
            return numero
        except ValueError:
            print (error("Ingrese un numero que sea valido"))
            print (error("Digite  el valor que sea valido"))
            valor = input ()

def info(texto: str):
    return texto_color(texto, color="azul_oscuro")

def advert(texto: str):
    return texto_color(texto, color="amarillo")

def error(texto: str):
    return texto_color(texto, color="rojo")

def menus (texto: str):
    return texto_color(texto, color="verde")
def resultado (texto: str):
    return texto_color(texto, color="amarillo_oscuro")

