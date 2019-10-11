import pandas as pd
import numpy as np
import json


class JournalCharacterization:
    __file = None
    __original_file = None
    __article_list = []
    __journal_list = []

    def __init__(self, path_source):
        temp_var = pd.read_json(path_source)
        self.__file = pd.DataFrame(temp_var)
        self.clean_articles()
        self.init_journals()

    # Inicializa articulos
    def clean_articles(self):
        for index, row in self.__file.iterrows():
            if str(row['journal']) != 'nan':
                temp_article = {
                    'record_lens_id': row['record_lens_id'],
                    'title': row['title'],
                    'authors': row['authors'],
                    'volume': row['volume'],
                    'issue': row['issue'],
                    'journal': row['journal']
                }
                if temp_article not in self.__article_list:
                    self.__article_list.append(temp_article)

    # Inicializa journals
    def init_journals(self):
        for article in self.get_articles():
            if not article['journal'] in self.get_journals():
                self.__journal_list.append(article['journal'])

    # Metodo filtra y retorna journals segun busqueda
    def filter_journals(self, search_value, search_type):
        returned_journal_list = []
        if search_type == 'name':
            for journal in self.get_journals():
                if str(search_value).lower() in str(journal['title_full']).lower():
                    returned_journal_list.append(journal)
        elif search_type == 'issn':
            for journal in self.get_journals():
                for journal_issn in journal['issn']:
                    if str(search_value) in str(journal_issn['value']):
                        returned_journal_list.append(journal)
        return returned_journal_list

    # Metodo retorna articulos relacionados a una revista
    def get_journal_articles(self, journal):
        returned_article_list = []
        for article in self.get_articles():
            if article['journal'] == journal:
                print('yes')
                returned_article_list.append(article)
        return returned_article_list

    def get_file(self):
        return self.__original_file

    def get_articles(self):
        return self.__article_list

    def get_journals(self):
        return self.__journal_list


test = JournalCharacterization('university_of_antioquia.json')
test.clean_articles()
# print(test.get_articles()[0]['authors'])
# print(test.get_journals())
searched_list = test.filter_journals('187', 'issn')
print(searched_list)
# print(test.get_journal_articles(searched_list[0]))
for art in test.get_journal_articles(searched_list[0]):
    print(art['title'], art['volume'], art['issue'])
