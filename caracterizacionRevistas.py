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

    def printInfoOLD(self, index):
        str_to_return = ''
        d = False
        try:
            i = 0
            for journal in self.__journal_list:
                i = i + 1
                if i == int(index):
                    # print('Nombre de la revista: ' + journal.get_title())
                    str_to_return += 'Nombre de la revista' + journal.get_title()
                    str_to_return += '\n'
                    # print('Editorial: ' + str(journal.get_publisher()))
                    str_to_return += 'Editorial: ' + str(journal.get_publisher())
                    str_to_return += '\n'
                    if str(journal.get_country()) == "None":
                        # print('País: Desconocido')
                        str_to_return += 'País: Desconocido'
                        str_to_return += '\n'
                    else:
                        # print('País: ' + str(journal.get_country()))
                        str_to_return += 'País: ' + str(journal.get_country())
                        str_to_return += '\n'
                    if len(journal.get_issn_list()) > 0:
                        # print("Para la revista " + journal.get_title() + " estos son los ISSNs: ")
                        str_to_return += 'Para la revista ' + journal.get_title() + ' estos son los ISSNs: '
                        str_to_return += '\n'
                        for issn in journal.get_issn_list():
                            # print("  " + issn['value'] + " - " + issn['type'])
                            # iss = {'0': "12345", '1': "Impreso"}
                            str_to_return += '   ' + issn['value'] + ' - ' + issn['type']
                            str_to_return += '\n'
                    # print("Articulos: ")
                    str_to_return += 'Articulos: '
                    str_to_return += '\n'
                    for article in journal.get_articles():
                        str_to_return += '\n'
                        for i_for in range(0, 80):
                            str_to_return += '_'
                        str_to_return += '\n'
                        str_to_return += article.get_title()
                        str_to_return += '\n'
                        for i_for in range(0, 80):
                            str_to_return += '_'
                        str_to_return += '\n'
                        # print()
                        # print("______________________________________________________________________________________")
                        # print()
                        # print(article.get_title())
                        # print()
                        # print("______________________________________________________________________________________")
                        # print()
                    d = True
        except Exception as e:
            # print("error, solo se admiten numeros en el rango valido")
            str_to_return = 'Lo sentimos, solo se admiten numeros en el rango valido'
        else:
            if not d:
                # print("subindice fuera de rango")
                str_to_return = 'subindice fuera de rango'
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
