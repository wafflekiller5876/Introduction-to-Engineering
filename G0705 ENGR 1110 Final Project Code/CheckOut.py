from Book import *
from FileReader import *

def checkOut(listA, title):
    for i in listA:
        if i.title == title and i.status == True:
            i.status = False
            break
    dataBaseReset(listA)
    return listA

def checkIn(listA, title):
    for i in listA:
        if i.title == title and i.status == False:
            i.status = True
            break
    dataBaseReset(listA)
    return listA