from metodos import error,info,texto_es_numero,resultado
from datetime import datetime

def validar_fecha(cadena: str, formato: str ="%Y%m%d") -> bool:
    try:
        fecha = datetime.strptime(cadena, formato)
        return True
    except ValueError as msg_error:
        return False
    


def extraer_fecha(fecha: int) -> ():
    str_fecha = str(fecha)
    if len(str_fecha) == 8:
        if validar_fecha(str_fecha):
            return str_fecha[:4], str_fecha[4:6], str_fecha[6:]
        else:
            print(error(f"La cadena {str_fecha} no es una fecha válida."))
    
            
# if 10000000 <= fecha <= 9999999:
#     if validar_fecha(str(fecha)):
#           anio = fecha_numerica // 10000
#           mes = (fecha_numerica % 10000) // 100
#           dia = fecha_numerica % 100
#           return anio, mes,dia
    return False
    
    
def menu_validar_fecha():
    """
    metodo para validar si la fecha que escribes es valida en el formato aaaammdd
    :return:
    """
    
    print(info("--validar fecha (aaaammdd)"))
    
    numero = input(info("Digite una fecha en el formato aaaammdd: "))
    if texto_es_numero(numero):
        numero = int(numero)
        result = extraer_fecha(numero)
        if result:
            anio, mes, dia = result  # Desempaquetar la tupla
            print(resultado (f"El número {numero} representa la fecha {dia}/{mes}/{anio} que es válida."))
    else:
        print(error("Por favor, ingrese un número válido."))
        
if __name__ == "__main__":
    
    menu_validar_fecha()
    print(extraer_fecha(20240229))