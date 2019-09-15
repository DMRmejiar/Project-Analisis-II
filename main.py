# by: David Mejía, Juan José Zapata, Felipe Correa, Andrés Quintero, Paola Posada
# !/usr/bin/python
from caracterizacionRevistas import *

class Main:
    local_controller = Controller()
    print("Bienvenido, ¿Qué desea realizar?")
    user_exit = False
    while True and (not user_exit):
        print("Opciones\n%.- Salir\n1.- Buscar revistas por nombre \n2.- Buscar resvistas por ISSN")
        var_select = input()
        search_type = ''
        var_value_print = ''
        if var_select == '%':
            break
        if var_select == '1':
            search_type = 'name'
            var_value_print = 'nombre'
        elif var_select == '2':
            search_type = 'issn'
            var_value_print = 'ISSN'
        else:
            continue
        while True and (not user_exit):
            print("Ingrese el " + var_value_print + " de la revista.\nIngrese '*' para regresar\nIngrese '%' para salir:")
            var_value = input()
            if var_value == '%':
                user_exit = True
                break
            if var_value == '*':
                break
            while not user_exit:
                usr_message = local_controller.search(var_value, search_type)
                print(usr_message[0])
                if usr_message[1]==-1 and search_type=="issn":
                    break
                if usr_message[1]==-1 and search_type=="name":
                    continue
                # print("ingrese '*' para regresar o el indice de una revista para ver su info")
                var_input = input()
                if var_input == '%':
                    user_exit = True
                    break
                if var_input == '*':
                    break
                else:
                    # print(local_controller.printInfo(var_input))
                    brt_to_print = local_controller.printInfo(var_input)
                    if brt_to_print == 'range':
                        print('Ingrese un valor en el rango adecuado')
                    elif brt_to_print == 'number':
                        print('Ingrese solo caracteres numericos')
                    else:
                        magazine_info = brt_to_print
                        volume_navigate = True
                        while volume_navigate and (not user_exit):
                            print(magazine_info)
                            print("Ingrese el volumen o presione '*' para regresar al menu\nIngrese % para salir: ")
                            var_input1 = input()
                            if var_input1 == '%':
                                user_exit = True
                                break
                            if var_input1 == '*':
                                break
                            crt_to_print = local_controller.show_article_by_Volume(var_input1)
                            if crt_to_print == None:
                                print('No hay articulos asociados a ese volumen')
                            else:
                                while volume_navigate and (not user_exit):
                                    present_volume = var_input1
                                    print('Los articulos asociados a este volumen son:\n' + crt_to_print)
                                    print("Ingrese el numero del articulo para ver la informacion o presione '*' para continuar\nPresione % para salir:")
                                    var_input2 = input()
                                    if var_input2 == '%':
                                        user_exit = True
                                        break
                                    if var_input2 == '*':
                                        break
                                    art_to_print = local_controller.show_article_info(present_volume,var_input2)
                                    if art_to_print == None:
                                        print('No hay información acerca de ese artículo')
                                    else:
                                        while not(user_exit) and volume_navigate:
                                            art_to_print = local_controller.show_article_info(present_volume, var_input2)
                                            if len(art_to_print[0])==0:
                                                break
                                            print('INFORMACION DEL ARTICULO \n' + art_to_print[0])
                                            print(" presione la tecla 'enter' para regresar al menu\nIngrese % para salir")
                                            var_input3 = str(input()).lower()
                                            if var_input3 == '%':
                                                user_exit = True
                                                break
                                            else:
                                                break
