from Book import *
from FileReader import *


def sortAuthor(temp):
    temp.sort(key = lambda x: x.authorLast)
    return temp

def sortGenre(temp):
    temp.sort(key = lambda x: x.genre)
    return temp

def sortTitle(temp):
    temp.sort(key = lambda x: x.title)
    return temp