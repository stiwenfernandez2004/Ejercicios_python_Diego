def invertir_digitos(numero):
    """Invierte los dígitos de un número.
    
    Convierte el número a cadena, luego a lista de dígitos, invierte la lista y
    convierte cada elemento de nuevo a entero.
    """
    digitos_invertidos = [int(digito) for digito in str(numero)][::-1]
    return digitos_invertidos

def pedir_numero():
    """Solicita al usuario que ingrese un número entero, 
    y repite hasta que se cumpla esa condicion
    ."""
    while True:
        try:
            valor = int(input("Digite por favor un número entero: "))
            return valor
        except ValueError:
            print("Ingrese un número entero válido")

def mostrar_digitos_invertidos():
    """Solicita un número, invierte sus dígitos y muestra el resultado."""
    numero = pedir_numero()
    digitos_invertidos = invertir_digitos(numero)
    print(f"Los dígitos invertidos son: {', '.join(map(str, digitos_invertidos))}")

if __name__ == "__main__":
    mostrar_digitos_invertidos()