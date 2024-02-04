from metodos import advert,error,resultado, info
def es_palindromo(cadena):
    """Verifica si una cadena de caracteres es un palíndromo."""
    return cadena == cadena[::-1]

def solicitar_cadena():
    """Solicita al usuario que ingrese una cadena de caracteres."""
    return input(info("Ingrese una cadena de caracteres: "))

def mostrar_polindromo():
    """Función principal que solicita una cadena y muestra si es un palíndromo o no."""
    cadena = solicitar_cadena()
    
    if es_palindromo(cadena):
        print(resultado("La cadena es un palíndromo."))
    else:
        print(resultado("La cadena no es un palíndromo."))

if __name__ == "__main__":
    mostrar_polindromo()