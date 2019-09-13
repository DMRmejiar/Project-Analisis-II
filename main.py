# by: David Mejía, Juan José Zapata, Felipe Correa, Andrés Quintero, Paola Posada
# !/usr/bin/python
from caracterizacionRevistas import *


class Main:
    local_controller = Controller()
    user_exit = False
    print("Bienvenido, ¿Qué desea realizar?")
    while True and (not user_exit):
        print("Opciones\n1.- Buscar revistas por nombre \n2.- Buscar resvistas por ISSN \n0.- Salir")
        var_select = input()
        search_type = ''
        var_value_print = ''
        if var_select == '1':
            search_type = 'name'
            var_value_print = 'nombre'
        elif var_select == '2':
            search_type = 'issn'
            var_value_print = 'ISSN'
        elif var_select == '0':
            user_exit = True
            print("Hasta luego, nos vemos pronto ")
            break
        while not user_exit:
            print("Ingrese el " + var_value_print + "de la revista o '*' para regresar al menu principal:\n"
                                                    "Presione 0 para salir")
            var_value = input()
            if var_value == '*' or var_value == '0':
                user_exit = True
                print("Hasta luego, nos vemos pronto ")
                break
            print(local_controller.search(var_value, search_type))
            #print("ingrese '*' para regresar o el indice de una revista para ver su info")
            var_input = input()
            if var_value == '*' or var_value == '0':
                user_exit = True
                print("Hasta luego, nos vemos pronto ")
                break
            else:
                print(local_controller.printInfo(var_input))
                to_print = local_controller.printInfo(var_input)
                if to_print == 'range':
                    print('Ingrese un valor en el rango adecuado')
                elif to_print == 'number':
                    print('Ingrese solo caracteres numericos')
                else:
                    print(to_print)
