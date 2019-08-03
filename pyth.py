# Juan Luis Rojas Rincon

import json

with open("university_of_antioquia.json", encoding="utf-8") as dataUdeA:
    articles = json.loads(dataUdeA.read())


def readList():
    print("Lista de artículos")

    for article in articles:
        print(article)


def readField(field):
    print("Lista de ID de artículos")

    for article in articles:
        print(article.get(field))


def readArticle(ar):
    print("El articulito")
    print(articles[int(ar)])


def searchISSN(value):
    i = 0
    for article in articles:
        # for issn in article['ISSNs']:
        if article.get('ISSNs') == value:
            i = i + 1
            # if issn == value:
            print(article.get('Source Title'))
    if i==0:
        print('No se encontró ninguna revista asociada al ISSN ', value)


def searchName(value):
    i = 0
    for article in articles:
        if value in article.get('Source Title'):
            i = i +1
            print(i, article.get('Source Title'))
    if i == 0:
        print('No se encontró ninguna revista con el nombre ', value)


# temp = input("Ingrese el campo a buscar")
# readArticle(temp)
# temp = input("Ingrese el ISSN")
# searchISSN(temp)
#temp = input("Ingrese el nombre de la revista")
#searchName(temp)
# readList()
# readField('Lens ID')
