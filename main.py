#by: David Mejía, Juan José Zapata, Felipe Correa, Andrés Quintero, Paola Posada
#!/usr/bin/python
from caracterizacionRevistas import *


class Main:
    controlador = Controller()
    print("Bienvenido, ¿Qué desea realizar?")
    while True:
        print("Opciones\n1.- Buscar revistas por nombre \n2.- Buscar resvistas por ISSN")
        seleccion=input()
        if seleccion == "1":
            while True:
                print("Ingrese el nombre de la revista o '*' para regresar:")
                name = input()
                if name=='*':
                    break
                message = controlador.byName(name)
                print (message + "ingrese '*' para regresar o el indice de una revista para ver su info")
                inp = input()
                if(inp=='*'):
                    False
                else:
                    controlador.printInfo(inp)
        if seleccion == "2":
            while True:
                print("Ingrese el ISSN de la revista o '*' para regresar:")
                search = input()
                if search=='*':
                    break
                message = controlador.byISSN(search)
                print (message + "ingrese '*' para regresar o el indice de una revista para ver info")
                inp =input()
                if(inp=='*'):
                    False
                else:
                    controlador.printInfo(inp)
