from metodos import texto_es_numero, advert,error,info,resultado
UNIDADES = ['', 'uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis', 'siete', 'ocho', 'nueve']
DECENAS = ['', 'diez', 'veinte', 'treinta', 'cuarenta', 'cincuenta', 'sesenta', 'setenta', 'ochenta', 'noventa']

def numero_a_palabras(numero):
    """Al escrbir un numero lo convierte a como se escribe."""
    if numero < 10:
        return UNIDADES[numero]
    elif numero < 20:
        return f'diez y {UNIDADES[numero - 10]}' if numero != 10 else 'diez'
    else:
        unidad = numero % 10
        decena = numero // 10
        return f'{DECENAS[decena]} y {UNIDADES[unidad]}' if unidad != 0 else DECENAS[decena]

def solicitar_numero():
    """Le pide  al usuario que ingrese un número entre 0 y 99."""
    return texto_es_numero(input(info("Ingrese un número entre 0 y 99: ")))

def mostrar_escrito():
    """Esta parte , principal que solicita un número y muestra como se escribe ."""
    numero = solicitar_numero()
    palabras = numero_a_palabras(numero)
    print(f"{numero} en palabras: {palabras}")

if __name__ == "__main__":
    mostrar_escrito()