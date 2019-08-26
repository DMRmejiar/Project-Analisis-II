#by: David Mejía, Juan José Zapata, Felipe Correa, Andrés Quintero, Paola Posada
#!/usr/bin/python

class Journal:
    def __init__(self, title, publisher, issns, country, articles):
        self.__title = title
        self.__publisher = publisher
        self.__ISSNs = issns
        self.__country = country
        self.__articles = articles

    def __init__(self, title, publisher, issns, country):
        self.__title = title
        self.__publisher = publisher
        self.__ISSNs = issns
        self.__country = country
        self.__articles = []

    def get_title(self):
        return self.__title

    def get_publisher(self):
        return self.__publisher

    def get_issn_list(self):
        return self.__ISSNs

    def get_country(self):
        return self.__country

    def get_articles(self):
        return self.__articles

    def set_article(self, article):
        self.__articles.append(article)


class Article:
    def __init__(self, lens_id, title, journal, authors):
        self.__lens_id = lens_id
        self.__title = title
        self.__journal = journal
        self.__authors = authors

    def get_lens_id(self):
        return self.__lens_id

    def get_title(self):
        return self.__title

    def get_journal(self):
        return self.__journal

    def get_authors(self):
        return self.__authors
