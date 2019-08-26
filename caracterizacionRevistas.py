#by: David Mejía, Juan José Zapata, Felipe Correa, Andrés Quintero, Paola Posada
#!/usr/bin/python
from models import *
from pandasHelper import UFileInPandas
import json
import pandas as pd


def create_article(article):
    article_object = models.Article(article.get('Lens ID'),
                                    article.get('Title'),
                                    article.get('Journal'),
                                    article.get('Authors'))
    return article_object


class Controller:

    def __init__(self):
        # Here the pandas helper
        self.__pandasManager = UFileInPandas('university_of_antioquia.json')
        self.__journals = self.__pandasManager.getJournalList()
        self.__list_Journal = []

    def getJournals(self):
        return self.__list_Journal

    def byname(self):
        while True:
            print("Ingrese el nombre de la revista o '*' para regresar:")
            nombre = input()
            if nombre == '*':
                break

            self.__list_Journal.clear()
            for revista in self.__journals:
                if str(revista.getTitle()).find(str(nombre)) != -1:
                    self.__list_Journal.append(revista)
            i = 0
            for revista in self.__list_Journal:
                i = i + 1
                print(i, revista.getTitle())
            if i == 0:
                print('No se encontró ninguna revista con el nombre "', nombre, '" intente de nuevo')
                True
            else:
                print("Para conocer la informacion de alguna de las revistas anteriores ingrese el "
                      "numero que le corresponde o '*' para regresar")
                buscar = input()
                if buscar == '*':
                    break
                self.printInfo(buscar)

            break

    def byISSN(self):
        while True:
            print("Ingrese el ISSN de la revista o '*' para regresar:")
            temp_ISSN = input()
            if temp_ISSN == '*':
                break
            self.updateJournalListISSN(temp_ISSN)
            i = 0
            for revista in self.__list_Journal:
                i = i + 1
                print(i, revista.getTitle())
            if i == 0:
                print('No se encontró ninguna revista con el Issn "', temp_ISSN, '" intente de nuevo')
                True
            else:
                print("Para conocer la informacion de alguna de las revistas anteriores ingrese el "
                      "numero que le corresponde o '*' para regresar")
                buscar = input()
                if buscar == '*':
                    break

                self.printInfo(buscar)
            break

    def printInfo(self, index):
        d = False

        try:
            i = 0
            for Journal in self.__list_Journal:
                i = i + 1
                if i == int(index):
                    print('Nombre de la revista: ' + Journal.getTitle())
                    print('Editorial: ' + str(Journal.getPublisher()))
                    if str(Journal.getCountry()) == "None":
                        print('País: Desconocido')
                    else:
                        print('País: ' + str(Journal.getCountry()))
                    print("Para la revista " + Journal.getTitle() + " estos son los ISSNs: ")
                    for issn in Journal.getISSNs():
                        print("  " + issn['value'] + " - " + issn['type'])
                    print("Articulos: ")
                    for article in Journal.getArticles():
                        print("______________________________________________________________________________________")
                        print(article.getTitle())
                        print("______________________________________________________________________________________")
                    d = True
        except:
            print("error, solo se admiten numeros en el rango valido")
        else:
            if not d:
                print("subindice fuera de rango")

    def updateJournalListISSN(self, issn):
        self.__list_Journal = []
        for journal in self.__journals:
            for temp_issn in journal.getISSNs():
                if issn in temp_issn['value']:
                    self.__list_Journal.append(journal)
