#!/usr/bin/python
import caracterizacionRevistas
import pyth
from caracterizacionRevistas import *

class Main:

    print("Bienvenido, ¿Qué desea realizar?")
    print("Opciones\n1.- Buscar revistas por nombre \n2.- Buscar resvistas por ISSN")
    seleccion = input()

    while True:
        if seleccion == '1':
            print("Ingrese el nombre de la revista:")
            nombre = input()
            pyth.searchName(nombre)
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