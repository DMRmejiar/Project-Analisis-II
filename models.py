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

    def getTitle(self):
        return self.__title

    def getPublisher(self):
        return self.__publisher

    def getISSNs(self):
        return self.__ISSNs

    def getCountry(self):
        return self.__country

    def getArticles(self):
        return self.__articles

    def setArticle(self, article):
        self.__articles.append(article)


class Article:
    def __init__(self, lens_id, title, journal, authors):
        self.__lens_id = lens_id
        self.__title = title
        self.__journal = journal
        self.__authors = authors

    def getLensId(self):
        return self.__lens_id

    def getTitle(self):
        return self.__title

    def getJournal(self):
        return self.__journal

    def getAuthors(self):
        return self.__authors
