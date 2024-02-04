from metodos import info , error , advert , menus,texto_es_numero
import ejercicio_01,ejercicio_02,ejercicio_03,ejercicio_04,ejercicio_05_8,ejercicio_06,ejercicio_07,ejercicio_09,ejercicio_10,ejercicio_11,ejercicio_12,ejercicio_13,ejercicio_14,ejercicio_15,ejercicio_16
def menu():
    while True:
        print(info("seleccione el ejercicio a ejecutar segun el siguiente menu:"))
        print(menus("1) Cociente de 2 números:"))
        print(menus("2) Número par o impar"))
        print(menus("3) calcular el area del circulo"))
        print(menus("4) Numero par e impar "))
        print(menus("5y8) Mostrar fecha"))
        print(menus("6) Numero mayor , menor , medio:"))
        print(menus("7) Calcular hipotenza "))
        print(menus("9)Mostrar mes segun el numero que escriba) "))
        print(menus("10)Calculadora de Tiempo de Examens"))
        print(menus("11) Mostrar Dígitos en Orden Inverso) "))
        print(menus("12) verificador de numero capicua ):"))
        print(menus("13) Contador de Ocurrencias de Carácter"))
        print(menus("14) Verificador de Palíndromos "))
        print(menus("15) Número a Palabras "))
        print(menus("16)Capitalizador de Frases "))
        print(menus("30) Salir:"))

        opcion = input(advert("Ingrese un número segun el menu : "))
        opcion = int (opcion)
        if not opcion:
            print(error("El numero de la opcion que quieras debe ser mayor a 0 ,intentalo nuevamente"))
        elif opcion == 1:
            ejercicio_01.division ()
        elif opcion == 2:
            ejercicio_02.pedir_numero()
        elif opcion == 3:
            ejercicio_03.pedir_y_mostrar_area ()
        elif opcion == 4:
            ejercicio_04.multiplo()
        elif opcion == 5:
            ejercicio_05_8.menu_validar_fecha()
        elif opcion == 6:
            ejercicio_06.pedir_numeros_y_mostrar_resultados()
        elif opcion == 7:
            ejercicio_07.pedir_catetos()
        elif opcion == 9:
            ejercicio_09.mostrar_mes()
        elif opcion == 10:
            ejercicio_10.mostrar_tiempo()
        elif opcion == 11:
            ejercicio_11.mostrar_digitos_invertidos()
        elif opcion == 12:
            ejercicio_12.verificar_si_es_capicua()
        elif opcion == 13:
            ejercicio_13.mostrar_ocurrencias()
        elif opcion == 14:
            ejercicio_14.mostrar_polindromo()
        elif opcion == 15:
            ejercicio_15.mostrar_escrito()
        elif opcion == 16:
            ejercicio_16.main()
        elif opcion == 30:
            print(info("Programa finalizado..."))
            break
        else:
            print("Opción inválida. Intente nuevamente.")
            


if __name__ == "__main__":
    print (menus("Bienvenido a el desarrrollo de el taller de logica de programacion"))
    print (menus("Realizado por: Stiwen fernandez"))
    print (menus("Ficha : 2670142"))
    menu ()
