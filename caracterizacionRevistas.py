#!/usr/bin/python
from models import *
import json

class Controller:

    def __init__(self):
        with open("university_of_antioquia.json", encoding="utf-8") as dataUdeA:
            self.articles = json.loads(dataUdeA.read())
        self.list_magazine = []

    def search_name(self, value):
        for article in self.articles:
            if value in article.get('Source Title'):

        pass

    def add_magazine(self, title, issn, articles):

        pass

    def search_issn(self):
        # Se busca por issn y se llena una lista de revistas con las caracteristicas
        pass

    def search(self):
        # Aqui se filtra el tipo de busqueda a realizar, se detecta si es por issn o por nombre de revista
        # Luego se llama a search_name o search_issn dependiendo del resultado
        pass
