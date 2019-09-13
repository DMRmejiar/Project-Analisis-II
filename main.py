# by: David Mejía, Juan José Zapata, Felipe Correa, Andrés Quintero, Paola Posada
# !/usr/bin/python
from caracterizacionRevistas import *



class Main:
    local_controller = Controller()
    print("Bienvenido, ¿Qué desea realizar?")
    while True:
        print("Opciones\n1.- Buscar revistas por nombre \n2.- Buscar resvistas por ISSN")
        var_select = input()
        search_type = ''
        var_value_print = ''
        if var_select == '1':
            search_type = 'name'
            var_value_print = 'nombre'
        elif var_select == '2':
            search_type = 'issn'
            var_value_print = 'ISSN'
        while True:
            print("Ingrese el " + var_value_print + "de la revista o '*' para regresar:")
            var_value = input()
            if var_value == '*':
                break
            print(local_controller.search(var_value, search_type))
            # print("ingrese '*' para regresar o el indice de una revista para ver su info")
            var_input = input()
            if var_input == '*':
                break
            else:
                # print(local_controller.printInfo(var_input))
                to_print = local_controller.printInfo(var_input)
                if to_print == 'range':
                    print('Ingrese un valor en el rango adecuado')
                elif to_print == 'number':
                    print('Ingrese solo caracteres numericos')
                else:
                    print(to_print)
                    print('ingrese el volumen: ')
                    var_input = input()
                    to_print = local_controller.show_article_by_Volume(var_input)
                    if to_print == None:
                        print('no hay articulos asociados a ese volumen')
                    else:
                        print('los articulos asociados a este volumen son: '+ to_print)
