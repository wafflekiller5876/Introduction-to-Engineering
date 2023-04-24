from Book import *
from FileReader import *

def remove(listA, title):
    for i in listA:
        if i.title == title:
            listA.remove(i)
            break
    dataBaseReset(listA)
    return listA