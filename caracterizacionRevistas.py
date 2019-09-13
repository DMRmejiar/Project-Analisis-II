# by: David Mejía, Juan José Zapata, Felipe Correa, Andrés Quintero, Paola Posada
# !/usr/bin/python
from pandasHelper import JournalPandasHelper


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

    def update_journal_list(self, var, search_type):
        self.__journal_list.clear()
        if search_type == 'name':
            for var_journal in self.__journals:
                if not str(var_journal.get_title()).lower().find(str(var).lower()) == -1:
                    self.__journal_list.append(var_journal)
        elif search_type == 'issn':
            for var_journal in self.__journals:
                for var_issn in var_journal.get_issn_list():
                    if var in var_issn['value']:
                        self.__journal_list.append(var_journal)

    def print_journal_list(self):
        journal_counter = 0
        str_to_return = ''
        for var_journal in self.__journal_list:
            journal_counter += 1
            str_to_return += str(journal_counter) + ' ' + str(var_journal.get_title()) + '\n'
        if journal_counter == 0:
            str_to_return += 'No se encontró ninguna revista, intente de nuevo'
        else:
            str_to_return += "Para conocer la informacion de alguna de las revistas anteriores" + \
                            " ingrese el numero que le corresponde o '*' para regresar"
        return str_to_return

    def show_article_by_Volume(self, var):
        str_to_return = ' '
        vol = str(var)
        for temp_journal in self.__journal_list:
            if len(temp_journal.get_volumes()) > 0:
                for temp_volume in temp_journal.get_volumes():
                    if temp_volume == vol:
                        for article in temp_journal.get_articles(var):
                            str_to_return += '   ' + article.get_title() + '\n'
        return str_to_return

    def printInfo(self, index):
        try:
            index = int(index) - 1
        except Exception as e:
            return 'number'
        try:
            temp_journal = self.__journal_list[index]
        except Exception as e:
            return 'range'
        str_to_return = 'Nombre de la revista ' + temp_journal.get_title() + '\n' + \
            'Editorial: ' + str(temp_journal.get_publisher()) + '\n' + 'Pais: '
        if str(temp_journal.get_country()) == 'None':
            str_to_return += 'Desconocido'
        else:
            str_to_return += str(temp_journal.get_country())
        str_to_return += '\n' + 'ISSNs asociados a la revista ' + temp_journal.get_title() + ':' + '\n'
        if len(temp_journal.get_issn_list()) > 0:
            for temp_issn in temp_journal.get_issn_list():
                str_to_return += '   ' + temp_issn['value'] + ' ' + temp_issn['type'] + '\n'
        else:
            str_to_return += '   No se encontraron ISSNs asociados' + '\n'
        str_to_return += 'Volumenes de la revista' + '\n'
        if len(temp_journal.get_volumes()) > 0:
            for temp_volume in temp_journal.get_volumes():
                if temp_volume != 'null':
                    str_to_return += '   ' + str(temp_volume) + '\n'
                else:
                    str_to_return += '   Sin volumen' + '\n'
        else:
            str_to_return += '   No se encontraron Volumenes asociados' + '\n'

        return str_to_return
