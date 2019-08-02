#!/usr/bin/python
from models import *
import json

with open("university_of_antioquia.json", encoding="utf-8") as dataUdeA:
    articles = json.loads(dataUdeA.read())

def controller():
    pass