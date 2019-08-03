#!/usr/bin/python
import models
# from models import *
import json


class Controller:

    def __init__(self):
        with open("university_of_antioquia.json", encoding="utf-8") as dataUdeA:
            self.articles = json.loads(dataUdeA.read())
        self.list_magazine = []

    def getMagazines(self):
        return self.list_magazine

    def create_article(self, article):
        article_object = models.Article(article.get('Lens ID'),
                                        article.get('Title'),
                                        article.get('Source Title'),
                                        article.get('Date Published'),
                                        article.get('Author'),
                                        article.get('Publisher'))
        return article_object

    def add_magazine(self, article):
        article_object = self.create_article(article)
        list_articles = [article_object]
        magazine_object = models.Magazine(article.get('Source Title'), article.get('ISSNs'), list_articles)
        self.list_magazine.append(magazine_object)
        pass

    def search_name(self, value):
        for article in self.articles:
            if value in article.get('Source Title'):
                self.add_magazine(article)

    def search_issn(self):
        # Se busca por issn y se llena una lista de revistas con las caracteristicas
        pass

    def search(self):
        # Aqui se filtra el tipo de busqueda a realizar, se detecta si es por issn o por nombre de revista
        # Luego se llama a search_name o search_issn dependiendo del resultado
        pass
