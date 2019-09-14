# by: David Mejía, Juan José Zapata, Felipe Correa, Andrés Quintero, Paola Posada
# !/usr/bin/python
from caracterizacionRevistas import *

class Main:
    local_controller = Controller()
    print("Bienvenido, ¿Qué desea realizar?")
    user_exit = False
    while True and (not user_exit):
        print("Opciones\n0.- Salir\n1.- Buscar revistas por nombre \n2.- Buscar resvistas por ISSN")
        var_select = input()
        search_type = ''
        var_value_print = ''
        if var_select == '0':
            break
        if var_select == '1':
            search_type = 'name'
            var_value_print = 'nombre'
        elif var_select == '2':
            search_type = 'issn'
            var_value_print = 'ISSN'
        while True and (not user_exit):
            print("Ingrese el " + var_value_print + " de la revista.\nIngrese '*' para regresar\nIngrese '0' para salir:")
            var_value = input()
            if var_value == '0':
                user_exit = True
                break
            if var_value == '*':
                break
            print(local_controller.search(var_value, search_type))
            # print("ingrese '*' para regresar o el indice de una revista para ver su info")
            var_input = input()
            if var_input == '0':
                user_exit = True
                break
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
                    magazine_info = to_print
                    volume_navigate = True
                    while volume_navigate and (not user_exit):
                        print(magazine_info)
                        print("Ingrese el volumen o presione '*' para regresar al menu\nIngrese 0 para salir: ")
                        var_input = input()
                        if var_input == '0':
                            user_exit = True
                            break
                        if var_input == '*':
                            break
                        to_print = local_controller.show_article_by_Volume(var_input)
                        if to_print == None:
                            print('No hay articulos asociados a ese volumen')
                        else:
                            present_volume = var_input
                            print('Los articulos asociados a este volumen son:\n' + to_print)
                            print("Ingrese el numero del articulo para ver la informacion o presione '*' para continuar\nPresione 0 para salir:")
                            var_input = input()
                            if var_input == '0':
                                user_exit = True
                                break
                            if var_input == '*':
                                print('Presione Y  si desea volver a la revista; de lo contrario presione N')
                                var_input = input().lower()
                                if var_input == 'y':
                                    volume_navigate = True
                                elif var_input == 'n':
                                    volume_navigate = False
                                else:
                                    break
                            to_print = local_controller.show_article_info(present_volume,var_input)
                            if to_print == None:
                                print('No hay información acerca de ese artículo')
                            else:
                                to_print = local_controller.show_article_info(present_volume, var_input)
                                print('INFORMACION DEL ARTICULO \n' + to_print)
                                print('Presione Y  si desea volver a la revista; de lo contrario presione N\nPresione 0 para salir')
                                var_input = str(input()).lower()
                                if var_input == '0':
                                    user_exit = True
                                    break
                                if var_input == 'y':
                                    volume_navigate = True
                                elif var_input == 'n':
                                    volume_navigate = False
                                else:
                                    break
