from metodos import advert,error,resultado,info
def texto_es_numero(texto):
    """Convierte una cadena de texto a un número entero."""
    return int(texto)

def es_capicua(numero):
    """Verifica si un número es capicúa o no ."""
    return str(numero) == str(numero)[::-1]

def verificar_si_es_capicua():
    """Le dice  al usuario que ingrese un número entero y verifica si es capicúa."""
    while True:
        try:
            numero = texto_es_numero(input(info("Ingrese un número entero: ")))
            
            if es_capicua(numero):
                print(resultado("El número es capicúa."))
            else:
                print(info("El número no es capicúa."))
            break

        except ValueError:
            print(error("Ingrese un número entero válido"))

if __name__ == "__main__":
    verificar_si_es_capicua()