from metodos import info,advert,error,resultado
def contar_ocurrencias(caracter, cadena):
    
    return cadena.count(caracter)

def solicitar_caracter():
    """Solicita al usuario que ingrese un carácter."""
    while True:
        caracter = input(info("Ingrese un carácter: "))
        if len(caracter) == 1:
            return caracter
        else:
            print(error("Ingrese solo un carácter."))

def solicitar_cadena():
    """Solicita al usuario que ingrese una cadena de caracteres."""
    return input(info("Ingrese una cadena de caracteres: "))

def mostrar_ocurrencias():
    """Función principal que solicita un carácter y una cadena, y muestra el resultado."""
    caracter = solicitar_caracter()
    cadena = solicitar_cadena()
    resultado = contar_ocurrencias(caracter, cadena)
    print(f"El carácter '{caracter}' aparece {resultado} veces en la cadena.")

if __name__ == "__main__":
    mostrar_ocurrencias()