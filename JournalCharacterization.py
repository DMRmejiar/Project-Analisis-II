import pandas as pd


# noinspection SpellCheckingInspection
class JournalCharacterization:
    __file = None
    __article_list = []
    __journal_list = []

    def __init__(self, path_source):
        temp_var = pd.read_json(path_source)
        self.__file = pd.DataFrame(temp_var)
        self.__init_articles()
        self.__init_journals()

    # Init __article_list with the Json in __file
    def __init_articles(self):
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

    # Init __journal_list with the articles in __article_list
    def __init_journals(self):
        for article in self.get_articles():
            if not article['journal'] in self.get_journals():
                self.__journal_list.append(article['journal'])

    # Search journals with the correct search parameter and return a list with these journals
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

    # Search articles with the correct journal and return a list with these articles
    def get_journal_articles(self, journal):
        returned_article_list = []
        for article in self.get_articles():
            if article['journal'] == journal:
                returned_article_list.append(article)
        return returned_article_list

    # Return __file var
    def get_file(self):
        return self.__file

    # Return __article_list var
    def get_articles(self):
        return self.__article_list

    # Return __journal_list var
    def get_journals(self):
        return self.__journal_list


""" ZONE for TESTING and DEBUG 
print("holi")
test = JournalCharacterization('university_of_antioquia.json')
# print(test.get_articles()[0]['authors'])
# print(test.get_journals())
searched_list = test.filter_journals('187', 'issn')
print(searched_list)
# print(test.get_journal_articles(searched_list[0]))
for art in test.get_journal_articles(searched_list[0]):
    print(art['title'], art['volume'], art['issue'])
 ZONE for TESTING and DEBUG """
