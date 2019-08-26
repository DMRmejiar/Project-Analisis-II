#by: David Mejía, Juan José Zapata, Felipe Correa, Andrés Quintero, Paola Posada
#!/usr/bin/python
import models
from pandasHelper import UFileInPandas
# from models import *
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
        # End of pandas helper
        #with open("university_of_antioquia.json", encoding="utf-8") as dataUdeA:
         #   self.articles = json.loads(dataUdeA.read())
        self.__list_Journal = []

    def getJournals(self):
        return self.__list_Journal

    def add_Journal(self, article):
        article_object = create_article(article)
        list_articles = [article_object]
        journal_object = models.Journal(article.get('Source Title'), article.get('ISSNs'), list_articles)
        position = self.count(journal_object)
        if position != -1:
            self.__list_Journal[position].articles.append(article_object)
        else:
            self.__list_Journal.append(journal_object)

    def count(self, Journal):
        for Journals in self.__list_Journal:
            if Journal.title in Journals.title:
                return self.__list_Journal.index(Journals)

        return -1

    def search_name(self, value):
        i = 0
        value = value.lower()
        for article in self.articles:
            if value in str(article.get('Source Title')).lower():
                i = i + 1
                self.add_Journal(article)

    def search_issn(self,issn):

        for article in self.articles:
            articleIssn = article.get("ISSNs")
            listissns = articleIssn.split("; ")
            for issns in listissns:
                if issn in issns:
                    self.add_Journal(article)

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
            # self.__list_Journal.clear()
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
                        print(issn['value'])
                    print("Articulos: ")
                    for article in Journal.getArticles():
                        print("__________________________________________________________________________________________")
                        print(article.getTitle())
                         print("__________________________________________________________________________________________")
                    d = True
        except:
            print("error, solo se admiten numeros en el rango valido")
        else:
            if not d:
                print("subindice fuera de rango")
    def search(self):
        # Aqui se filtra el tipo de busqueda a realizar, se detecta si es por issn o por nombre de revista
        # Luego se llama a search_name o search_issn dependiendo del resultado
        pass

    def updateJournalListISSN(self, issn):
        self.__list_Journal = []
        for journal in self.__journals:
            for temp_issn in journal.getISSNs():
                if issn in temp_issn['value']:
                    self.__list_Journal.append(journal)
