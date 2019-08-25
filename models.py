#by: David Mejía, Juan José Zapata, Felipe Correa, Andrés Quintero, Paola Posada
#!/usr/bin/python

class Journal:
    def __init__(self, title, publisher, issns, country, articles):
        self.__title = title
        self.__publisher = publisher
        self.__ISSNs = issns
        self.__country = country
        self.__articles = articles


class Article:
    def __init__(self, lens_id, title, journal, authors):
        self.__lens_id = lens_id
        self.__title = title
        self.__journal = journal
        self.__authors = authors
