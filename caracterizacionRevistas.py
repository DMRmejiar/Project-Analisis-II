# by: David Mejía, Juan José Zapata, Felipe Correa, Andrés Quintero, Paola Posada
# !/usr/bin/python
from pandasHelper import JournalPandasHelper
import json


class Controller:

    def __init__(self):
        self.__pandas_manager = JournalPandasHelper('university_of_antioquia.json')
        self.__journals = self.__pandas_manager.get_journal_list()
        self.__journal_list = []

    def search(self, var, search_type):
        var.strip()
        if (var == '*') or (var == ''):
            return " "
        self.update_journal_list(var, search_type)
        return self.print_journal_list()

# Actualizar lista de revistas
    def update_journal_list(self, var, search_type):
        self.__journal_list.clear()
        if search_type == 'name':
            for var_journal in self.__journals:
                if not str(var_journal.get_title()).lower().find(str(var).lower()) == -1:
                    self.__journal_list.append(var_journal)
        elif search_type == 'issn':
            for var_journal in self.__journals:
                if not str(var_journal.get_issn_list()).lower().find(str(var)) == -1:
                    self.__journal_list.append(var_journal)

# Buscar y mostrar el listado de revistas
    def print_journal_list(self):
        journal_counter = 0
        str_to_return = ''
        code = 1
        for var_journal in self.__journal_list:
            journal_counter += 1
            str_to_return += str(journal_counter) + ' ' + str(var_journal.get_title()) + '\n'
        if journal_counter == 0:
            str_to_return += 'No se encontró ninguna revista, intente de nuevo'
            code = -1
        else:
            str_to_return += "Para conocer la informacion de alguna de las revistas anteriores" + \
                             " \nIngrese el numero que le corresponde o '*' para regresar" + \
                             "\nIngrese % Para salir"
        return [str_to_return, code]

# Mostrar el listado de articulos asociados a un volumen
    def show_article_by_Volume(self, var):
        articles_counter = 0
        str_to_return = ''
        vol = str(var)
        for temp_journal in self.__journal_list:
            if len(temp_journal.get_volumes()) > 0:
                for temp_volume in temp_journal.get_volumes():
                    if temp_volume == vol:
                        for article in temp_journal.get_articles(var):
                            articles_counter += 1
                            str_to_return += str(articles_counter) + ' ' + article.get_title() + '\n'
        if articles_counter == 0:
            return None
        return str_to_return

# Mostrar la informacion de un articulo
    def show_article_info(self, volume, articl):
        articles_counter = 0
        str_to_return = ''
        vol = str(volume)
        art = str(articl)
        code = 1
        for temp_journal in self.__journal_list:
            if len(temp_journal.get_volumes()) > 0:
                for temp_volume in temp_journal.get_volumes():
                    if temp_volume == vol:
                        for article in temp_journal.get_articles(vol):
                            articles_counter += 1
                            if str(articles_counter) == str(art):
                                str_to_return += 'Articulo N°: ' + str(articles_counter) + '\n'
                                str_to_return += 'Titulo del Articulo: ' + str(article.get_title()) + '\n'
                                # str_to_return += 'Autores: ' + str(article.get_authors()) + '\n'
                                str_to_return += 'Volumen: ' + str(article.get_volume()) + '\n'
                                str_to_return += 'Autores: \n'
                                for authors in article.get_authors():
                                    str_to_return += '• ' + (authors['first_name'] + ' ' + authors['last_name'] + '\n')

        if articles_counter == 0:
            code = -1
        return [str_to_return, code]

    def printInfo(self, index):
        try:
            index = int(index) - 1
        except Exception as e:
            return 'number'
        try:
            temp_journal = self.__journal_list[index]
        except Exception as e:
            return 'range'
        str_to_return = 'Nombre de la revista: ' + temp_journal.get_title() + '\n' + 'Pais: '
        if str(temp_journal.get_country()) == 'None':
            str_to_return += 'Desconocido \n'
        else:
            str_to_return += str(temp_journal.get_country())+ '\n'
        str_to_return += 'Editorial: '
        if str(temp_journal.get_publisher()) == 'None':
            str_to_return += 'Desconocida \n'
        else:
            str_to_return += str(temp_journal.get_publisher())+ '\n'
        str_to_return += 'ISSNs asociados a la revista "' + temp_journal.get_title() + '" :' + '\n'
        if len(temp_journal.get_issn_list()) > 0:
            for temp_issn in temp_journal.get_issn_list():
                str_to_return += '   ' + temp_issn['value'] + ' ' + temp_issn['type'] + '\n'
        else:
            str_to_return += '   No se encontraron ISSNs asociados' + '\n'

        str_to_return += 'Volumenes de la revista: ' + '\n'
        if len(temp_journal.get_volumes()) > 0:
            for temp_volume in temp_journal.get_volumes():
                if temp_volume != 'null' and temp_volume != '-1':
                    str_to_return += '• ' + str(temp_volume) + '\n'
                else:
                    str_to_return += 'Revista sin volumenes disponibles' + '\n'
        else:
            str_to_return += 'No se encontraron volumenes asociados a la revista' + '\n'
        return str_to_return

    def test(self):
        return json.dumps()
