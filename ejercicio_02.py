from metodos import error,info,advert,texto_es_numero

def numero_par_impar(numero):
    """Verifica si un número es par o impar y muestra el resultado."""
    if numero % 2 == 0:
        print(numero,info( "es un número par"))
    else:
        print(numero,info("es un número impar"))

def pedir_numero():
    """Solicita al usuario ingresar un valor numérico y verifica si es par o impar."""
    print("")
    print(info("Ingrese el valor numérico en donde se le dirá si es el número es par o impar"))
    
    while True:
        try:
            valor = texto_es_numero(input())
            numero = int(valor)
            numero_par_impar(numero)
            break
        except ValueError:
            print(advert("Ingrese un número válido"))

if __name__ == "__main__":
    pedir_numero()