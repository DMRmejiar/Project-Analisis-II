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

    def printInfo(self, index):
        d = False

        try:
            i = 0
            for journal in self.__journal_list:
                i = i + 1
                if i == int(index):
                    print('Nombre de la revista: ' + journal.get_title())
                    print('Editorial: ' + str(journal.get_publisher()))
                    if str(journal.get_country()) == "None":
                        print('País: Desconocido')
                    else:
                        print('País: ' + str(journal.get_country()))
                    if len(journal.get_issn_list()) > 0:
                        print("Para la revista " + journal.get_title() + " estos son los ISSNs: ")
                        for issn in journal.get_issn_list():
                            print("  " + issn['value'] + " - " + issn['type'])
                    print("Articulos: ")
                    for article in journal.get_articles():
                        print()
                        print("______________________________________________________________________________________")
                        print()
                        print(article.get_title())
                        print()
                        print("______________________________________________________________________________________")
                        print()
                    d = True
        except Exception as e:
            print("error, solo se admiten numeros en el rango valido")
        else:
            if not d:
                print("subindice fuera de rango")
