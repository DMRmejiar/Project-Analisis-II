#!/usr/bin/python
import models
# from models import *
import json


def create_article(article):
    article_object = models.Article(article.get('Lens ID'),
                                    article.get('Title'),
                                    article.get('Source Title'),
                                    article.get('Date Published'),
                                    article.get('Author'),
                                    article.get('Publisher'))
    return article_object


class Controller:

    def __init__(self):
        with open("university_of_antioquia.json", encoding="utf-8") as dataUdeA:
            self.articles = json.loads(dataUdeA.read())
        self.list_magazine = []

    def getMagazines(self):
        return self.list_magazine

    def add_magazine(self, article):
        article_object = create_article(article)
        list_articles = [article_object]
        magazine_object = models.Magazine(article.get('Source Title'), article.get('ISSNs'), list_articles)
        position=self.count(magazine_object)
        if position != -1:
            self.list_magazine[position].articles.append(article_object)
        else:
            self.list_magazine.append(magazine_object)

    def count(self, magazine):
        for magazines in self.list_magazine:
            if magazine.title in magazines.title:
                return self.list_magazine.index(magazines)

        return -1

    def search_name(self, value):
        i=0
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
            if nombre=='*':
                break
            self.list_magazine.clear()
            self.search_name(nombre)
            i=0
            for revista in self.getMagazines():
                i = i+1
                print(i, revista.title)
            if i == 0:
                print('No se encontró ninguna revista con el nombre "', nombre, '" intete de nuevo')
                True
            else:
                print("Para conocer la informacion de alguna de las revistas anteriores ingrese el "
                      "numero que le corresponde o '*' para regresar")
                buscar = input()
                y = 0
                try:
                    for revista in self.getMagazines():
                        y = y + 1
                        if y == int(buscar):
                            print('Abriendo:', '"', revista.title, '"')
                            False
                except:
                    print("Error, solo se aceptan valores numericos")
                    buscar == '*'
                if buscar=='*':
                    break
            break


    def byISSN(self):
        while True:
            print("Ingrese el ISSN de la revista o '*' para regresar:")
            ISSN = input()
            if ISSN=='*':
                break
            self.list_magazine.clear()
            self.search_issn(ISSN)
            i=0
            for revista in self.getMagazines():
                i = i+1
                print(i, revista.title)
            if i == 0:
                print('No se encontró ninguna revista con el Issn "', ISSN, '" intente de nuevo')
                True
            else:
                print("Para conocer la informacion de alguna de las revistas anteriores ingrese el "
                      "numero que le corresponde o '*' para regresar")
                buscar = input()
                y = 0
                try:
                    for revista in self.getMagazines():
                        y = y + 1
                        if y == int(buscar):
                            print('Abriendo:', '"', revista.title, '"')
                            False
                except:
                    print("Error, solo se aceptan valores numericos")
                    buscar == '*'
                if buscar == '*':
                    break
            break


    def exit(self):
        print("Pulse E para salir, cualquier tecla para volver al menu")
        salir = input()
        if salir == 'E' or salir == 'e':
            exit()
        else:
            True

    def search(self):
        # Aqui se filtra el tipo de busqueda a realizar, se detecta si es por issn o por nombre de revista
        # Luego se llama a search_name o search_issn dependiendo del resultado
        pass