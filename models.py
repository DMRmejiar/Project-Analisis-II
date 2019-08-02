#!/usr/bin/python

class Magazine:
    def __init__(self, title, issns, articles):
        self.title = title
        self.ISSNs = issns
        self.articles = articles


class Article:
    def __init__(self, lens_id, title, source_title, date, authors, publisher):
        self.lens_id = lens_id
        self.title = title
        self.source_title = source_title
        self.date = date
        self.authors = authors
        self.publisher = publisher
