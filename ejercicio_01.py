from metodos import error,info,advert,texto_es_numero
def realizar_division(numero1, numero2):
    """
    Realiza la división de dos números y maneja la división por cero.
    Retorna el resultado de la división o None si ocurre una división por cero.
    """
    if numero2 != 0:
        return numero1 / numero2
    else:
        print(error("Error, no se puede dividir por cero"))
        return None

def solicitar_numero(mensaje):
    """
    Solicita al usuario ingresar un número, repitiendo hasta que se ingrese un valor válido.
    """
    while True:
        try:
            valor = texto_es_numero(input(info(mensaje)))
            return valor
        except ValueError:
            print(advert("Ingrese números válidos"))

def division():
    """
    Solicita dos números al usuario y realiza la división.
    Muestra el resultado o un mensaje de error en caso de división por cero.
    """
    numero1 = solicitar_numero("Ingrese el primer número: ")
    numero2 = solicitar_numero("Ingrese el segundo número: ")

    resultado = realizar_division(numero1, numero2)
    
    if resultado is not None:
        print(info("El resultado de la división es:"), resultado)
    
        
if __name__ == "__main__":
    division()