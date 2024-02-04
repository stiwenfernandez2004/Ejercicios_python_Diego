from metodos import error,texto_es_numero,info,advert
def calcular_multiplo(numero:int):
    if numero <0:
        print(advert("no se puede calcular la operación"))
        return (texto_es_numero)
    else:
        return numero % 2 == 0 and numero % 3 == 0

def multiplo():
    print("")
    print(info("Ingrese el valor numerico en donde se le dira si es el número es multiplo de 2 y 3"))
    valor = texto_es_numero(info(input("Ingrese el numero a validar\n")))
    
    
    resultado = calcular_multiplo(valor)
    print("El numero es multiplo de 2 y 3" if resultado else "El número no es multiplo de 2 y 3")

if __name__ == "__main__":
    multiplo()