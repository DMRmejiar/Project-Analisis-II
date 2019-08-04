#!/usr/bin/python
import pyth
from caracterizacionRevistas import *

class Main:

    print("Bienvenido, ¿Qué desea realizar?")
    print("Opciones\n1.- Buscar revistas por nombre \n2.- Buscar resvistas por ISSN")
    seleccion = input()
    controlador = Controller()

    while True:
        if seleccion == '1':
            print("Ingrese el nombre de la revista:")
            nombre = input()
            controlador.search_name(nombre)
            i=0
            for revista in controlador.getMagazines():
                i = i+1
                print(i, revista.title)
            if i == 0:
                print('No se encontró ninguna revista con el nombre "', nombre, '" intete de nuevo')
                True
            else:
                print("Para conocer la informacion de alguna de las revistas anteriores ingrese el "
                      "numero que le corresponde")
                buscar = input()
                break


        elif seleccion == '2':
            print("Ingrese el ISSN de la revista:")
            ISSN = input()
            pyth.searchISSN(ISSN)
            break
        else:
            print("Opción invalida, intentelo nuevamente")
            seleccion = input()
            True