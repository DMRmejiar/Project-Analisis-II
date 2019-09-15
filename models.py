# by: David Mejía, Juan José Zapata, Felipe Correa, Andrés Quintero, Paola Posada
# !/usr/bin/python

class Journal:
    def __init__(self, title, publisher, issns, country, volumes):
        self.__title = title
        self.__publisher = publisher
        self.__ISSNs = issns
        self.__country = country
        self.__volumes = volumes

    def get_title(self):
        return self.__title

    def get_publisher(self):
        return self.__publisher

    def get_issn_list(self):
        return self.__ISSNs

    def get_country(self):
        return self.__country

    def get_volumes(self):
        return self.__volumes

    def get_articles(self, volume_number):
        return self.__volumes[volume_number]

    def set_article(self, volume_number, article):
        if volume_number in self.__volumes:
            self.__volumes[volume_number].append(article)
        else:
            self.__volumes[volume_number] = [article]


class Article:
    def __init__(self, lens_id, title, authors, volume):
        self.__lens_id = lens_id
        self.__title = title
        self.__authors = authors
        self.__volume = volume

    def get_lens_id(self):
        return self.__lens_id

    def get_title(self):
        return self.__title

    def get_authors(self):
        return self.__authors

    def get_volume(self):
        return self.__volume

