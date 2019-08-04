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
            for revista in controlador.getMagazines():
                print(revista.title)
            # print(controlador.getMagazines())
            # pyth.searchName(nombre)
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