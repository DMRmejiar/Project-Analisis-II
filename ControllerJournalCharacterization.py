from JournalCharacterization import JournalCharacterization


class ControllerJournalCharacterization:
    __journal_characterization = None
    __journal_list = []
    __article_list = []
    __volume_list = {}

    def __init__(self, path_source):
        self.__journal_characterization = JournalCharacterization(path_source)

    def update_journals(self, search_value, search_type):
        self.__journal_list = []
        search_value = str(search_value)
        search_type = str(search_type)
        self.__journal_list = self.__journal_characterization.filter_journals(search_value, search_type)
        for index, journal in enumerate(self.__journal_list):
            journal['volumes'] = self.__update_articles_and_volumes(index)
        return self.get_journals()

    def __update_articles_and_volumes(self, journal_index):
        temp_volumes = []
        self.__volume_list = {}
        self.__article_list = self.__journal_characterization.get_journal_articles(self.__journal_list[journal_index])
        for article in self.__article_list:
            if article['volume'] not in temp_volumes:
                temp_volumes.append(article['volume'])
                self.__volume_list[article['volume']] = []
        for article in self.__article_list:
            if article['issue'] not in self.__volume_list[article['volume']]:
                self.__volume_list[article['volume']] = {article['issue']: [article]}
            else:
                self.__volume_list[article['volume']][article['issue']].append(article)
        return self.get_volumes()

    def get_volumes(self):
        return self.__volume_list

    def get_journals(self):
        return self.__journal_list