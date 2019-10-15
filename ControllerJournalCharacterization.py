from JournalCharacterization import JournalCharacterization


class ControllerJournalCharacterization:
    __journal_characterization = None
    __journal_list = []
    __article_list = []
    __volume_list = []

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
        self.__volume_list = []
        self.__article_list = self.__journal_characterization.get_journal_articles(self.__journal_list[journal_index])
        temp_volumes = []
        for article in self.__article_list:
            if article['volume'] not in temp_volumes:
                temp_volumes.append(article['volume'])
        for temp_value in temp_volumes:
            temp_volume = {'volume': str(temp_value), 'issues': []}
            self.__volume_list.append(temp_volume)
        for article in self.__article_list:
            for temp_volume in self.__volume_list:
                if temp_volume['volume'] == str(article['volume']):
                    temp_volume['issues'].append(str(article['issue']))
        for temp_volume in self.__volume_list:
            temp_issues = temp_volume['issues']
            temp_volume['issues'] = []
            for temp_issue in temp_issues:
                temp_volume['issues'].append({'issue': str(temp_issue), 'articles': []})
        for article in self.__article_list:
            for temp_volume in self.__volume_list:
                if temp_volume['volume'] == str(article['volume']):
                    for temp_issue in temp_volume['issues']:
                        # print(temp_issue['issue'])
                        if temp_issue['issue'] == str(article['issue']):
                            temp_issue['articles'].append(article)
        return self.get_volumes()

    def get_volumes(self):
        return self.__volume_list

    def get_journals(self):
        return self.__journal_list
