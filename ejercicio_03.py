from metodos import error,info,advert,texto_es_numero,resultado
import math
def calcular_area_circulo(radio):
    return math.pi * (radio ** 2)

def pedir_y_mostrar_area():
    print(info("Ingrese el radio del circulo:"))
    valor = input()
    
    try:
        radio = texto_es_numero(valor)
        area = calcular_area_circulo(radio)
        print(resultado (f"El area del circulo  {radio} es: {area}"))
    except ValueError:
        print(advert("Ingrese un numero valido"))

if __name__ == "__main__":
    pedir_y_mostrar_area()
        
    
    