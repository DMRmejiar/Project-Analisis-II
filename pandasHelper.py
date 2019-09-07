import pandas as pd
import models

class JournalPandasHelper:

    """docstring for JournalPandasHelper."""

    def __init__(self, source):
        self.__source = source
        self.__file_university = pd.read_json(source)

    def create_article(self, index):
        article_text = self.__file_university.iloc[index]
        temp_article = models.Article(
            article_text['record_lens_id'],
            article_text['title'],
            article_text['journal']['title_full'],
            article_text['authors'])
        return temp_article

    def get_journal_list(self):
        journal_list = self.__file_university['journal']
        journal_list_to_return = []
        index = 0
        for line in journal_list:
            try:
                temp_journal = models.Journal(
                                line['title_full'],
                                line['publisher'],
                                line['issn'],
                                line['country'],
                                [])
            except Exception as e:
                index += 1
                continue
            temp_var = False
            for compare_journal in journal_list_to_return:
                if compare_journal.get_title() == temp_journal.get_title():
                    temp_article = self.create_article(index)
                    compare_journal.set_article(temp_article)
                    temp_var = True
                    break
            if not temp_var:
                temp_article = self.create_article(index)
                temp_journal.set_article(temp_article)
                journal_list_to_return.append(temp_journal)
            index += 1
        return journal_list_to_return


