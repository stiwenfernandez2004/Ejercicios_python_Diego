from metodos import error, info, advert, texto_es_numero, resultado

def encontrar_mayor(num1, num2, num3):
    return max(num1, num2, num3)

def encontrar_menor(num1, num2, num3):
    return min(num1, num2, num3)

def encontrar_medio(num1, num2, num3):
    suma = num1 + num2 + num3
    return suma - max(num1, num2, num3) - min(num1, num2, num3)

def pedir_numeros_y_mostrar_resultados():
    try:
        print(info("Ingrese el primer número:"))
        num1 = texto_es_numero(input())
        print(info("Ingrese el segundo número:"))
        num2 = texto_es_numero(input())
        print(info("Ingrese el tercer número:"))
        num3 = texto_es_numero(input())

        mayor = encontrar_mayor(num1, num2, num3)
        menor = encontrar_menor(num1, num2, num3)
        medio = encontrar_medio(num1, num2, num3)

        print(resultado(f"El mayor es: {mayor}"))
        print(resultado(f"El del medio es: {medio}"))
        print(resultado(f"El menor es: {menor}"))

    except ValueError:
        print(advert("Ingrese números válidos."))

if __name__ == "__main__":
    pedir_numeros_y_mostrar_resultados()
    