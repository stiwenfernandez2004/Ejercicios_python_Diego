from metodos import advert, info, resultado

def obtener_nombre_mes(numero_mes):
    """
    Muestra  el nombre del mes correspondiente al número que digite el usuario.
    Si el número no está en el rango de 1 a 12, es none.
    """
    meses = ["", "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
    return meses[numero_mes] if 1 <= numero_mes <= 12 else None

def validar_numero_mes(numero_mes):
    """
    Verifica si el número de mes está en el rango válido (1 a 12).
    si no, pide de nuevo el numero
    """
    return 1 <= numero_mes <= 12

def solicitar_entero(mensaje):
    """
    Solicita al usuario ingresar un número entero, repitiendo hasta que se ingrese un valor válido.
    """
    while True:
        try:
            valor = int(input(info(mensaje)))
            return valor
        except ValueError:
            print(advert("Ingrese un número entero válido."))

def mostrar_mes():
    """
    Muestra el nombre del mes correspondiente al número ingresado por el usuario,
    solicitando el número hasta que se ingrese un valor válido.
    """
    while True:
        numero_mes = solicitar_entero("Ingrese un número de mes (entre 1 y 12): ")

        if validar_numero_mes(numero_mes):
            break
        else:
            print(advert("Ingrese un número válido entre 1 y 12."))

    nombre_mes = obtener_nombre_mes(numero_mes)
    print(resultado(f"El mes correspondiente al número {numero_mes} es: {nombre_mes}"))

if __name__ == "__main__":
    mostrar_mes()
