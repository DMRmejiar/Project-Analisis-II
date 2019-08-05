#!/usr/bin/python
import pyth
from caracterizacionRevistas import *

class Main:
    controlador = Controller()
    print("Bienvenido, ¿Qué desea realizar?")
    while True:
        print("Opciones\n1.- Buscar revistas por nombre \n2.- Buscar resvistas por ISSN")
        seleccion=input()
        if seleccion == "1":
            controlador.byname()
        if seleccion == "2":
            controlador.byISSN()
