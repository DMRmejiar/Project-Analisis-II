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
        with open("university_of_antioquia.json", encoding="utf-8") as dataUdeA:
            self.articles = json.loads(dataUdeA.read())
        self.__list_magazine = []

    def getMagazines(self):
        return self.__list_magazine

    def add_magazine(self, article):
        article_object = create_article(article)
        list_articles = [article_object]
        magazine_object = models.Magazine(article.get('Source Title'), article.get('ISSNs'), list_articles)
        position = self.count(magazine_object)
        if position != -1:
            self.__list_magazine[position].articles.append(article_object)
        else:
            self.__list_magazine.append(magazine_object)

    def count(self, magazine):
        for magazines in self.__list_magazine:
            if magazine.title in magazines.title:
                return self.__list_magazine.index(magazines)

        return -1

    def search_name(self, value):
        i = 0
        value = value.lower()
        for article in self.articles:
            if value in str(article.get('Source Title')).lower():
                i = i + 1
                self.add_magazine(article)

    def search_issn(self,issn):

        for article in self.articles:
            articleIssn = article.get("ISSNs")
            listissns = articleIssn.split("; ")
            for issns in listissns:
                if issn in issns:
                    self.add_magazine(article)

    def byname(self):
        while True:
            print("Ingrese el nombre de la revista o '*' para regresar:")
            nombre = input()
            if nombre == '*':
                break
            self.__list_magazine.clear()
            self.search_name(nombre) #play metod search_name
            i = 0
            for revista in self.getMagazines():
                i = i + 1
                print(i, revista.title)
            if i == 0:
                print('No se encontró ninguna revista con el nombre "', nombre,'" intete de nuevo')
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
            ISSN = input()
            if ISSN == '*':
                break
            self.__list_magazine.clear()
            self.search_issn(ISSN)
            i = 0
            for revista in self.getMagazines():
                i = i + 1
                print(i, revista.title)
            if i == 0:
                print('No se encontró ninguna revista con el Issn "', ISSN, '" intente de nuevo')
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
            for magazine in self.getMagazines():
                i += 1
                if i == int(index):
                    print('Nombre de la revista: '+magazine.title)
                    print('ISSNs: '+magazine.ISSNs)
                    print("Articulos: ")
                    for article in magazine.articles:
                        print("___---___---___---___---______---___---___---___---______---___---___---___")
                        print(article.title)
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

class pandasManager:
    """docstring for pandasManager."""

    def __init__(self, json_source):
        self.__json_source = json_source
        self.__file = pd.read_json(json_source)
