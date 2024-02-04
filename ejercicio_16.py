from metodos import error,info,resultado,advert
def capitalizar_frase(frase):
    """Capitaliza la primera letra de cada palabra en una frase."""
    return frase.title()

def solicitar_frase():
    """Solicita al usuario que ingrese una frase de al menos 5 palabras."""
    while True:
        frase = input(info("Ingrese una frase de al menos 5 palabras: "))
        if len(frase.split()) >= 5:
            return frase
        else:
            print("La frase debe tener al menos 5 palabras. Intente nuevamente.")

def main():
    """Función principal que solicita una frase y muestra la versión capitalizada."""
    frase = solicitar_frase()
    frase_capitalizada = capitalizar_frase(frase)
    print(f"escribio: {frase}")
    print(f"Frase capitalizada: {frase_capitalizada}")

if __name__ == "__main__":
    main()