from metodos import texto_es_numero, advert, info,resultado

def calcular_Hipotenuza(cateto1, cateto2):
    return (cateto1**2 + cateto2**2)**0.5

def solicitar_cateto(mensaje):
    while True:
        try:
            valor = texto_es_numero(input(info(mensaje)))
            return valor
        except ValueError:
            print(advert("Ingrese números válidos"))

def pedir_catetos():
    cateto1 = solicitar_cateto("Digite por favor el primer cateto: ")
    cateto2 = solicitar_cateto("Digite por favor el segundo cateto: ")
    Hipotenuza = calcular_Hipotenuza(cateto1, cateto2)
    print(resultado(f"La hipotenusa es: {Hipotenuza}"))

if __name__ == "__main__":
    pedir_catetos()
    