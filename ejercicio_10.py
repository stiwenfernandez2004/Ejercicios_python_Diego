from metodos import advert, info, resultado

def convertir_segundos_a_tiempo(segundos):
    horas = segundos // 3600
    minutos = (segundos % 3600) // 60
    segundos_restantes = segundos % 60
    return horas, minutos, segundos_restantes

def validar_segundos(segundos):
    return segundos >= 0

def solicitar_entero_positivo(mensaje):
    while True:
        try:
            valor = int(input(info(mensaje)))
            if validar_segundos(valor):
                return valor
            else:
                print(advert("Ingrese un número entero positivo mayor o igual a cero."))
        except ValueError:
            print(advert("Ingrese un número entero válido."))

def mostrar_tiempo():
    segundos = solicitar_entero_positivo("Ingrese la cantidad de segundos invertidos en el examen: ")

    tiempo_convertido = convertir_segundos_a_tiempo(segundos)
    
    minutos_totales = tiempo_convertido[0] * 60 + tiempo_convertido[1]
    segundos_totales = tiempo_convertido[0] * 3600 + tiempo_convertido[1] * 60 + tiempo_convertido[2]

    print(resultado(f"Tiempo invertido: {tiempo_convertido[0]} horas, {minutos_totales} minutos, {segundos_totales} segundos"))

if __name__ == "__main__":
    mostrar_tiempo()