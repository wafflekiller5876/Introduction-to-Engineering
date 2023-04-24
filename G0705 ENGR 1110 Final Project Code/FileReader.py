from Book import *

def fileReader(name, listA):
    myFile = open(name)
    tempList = myFile.readlines()
    for index in tempList:
        info = index.split(", ")
        title = info[0]
        first = info[1]
        last = info[2]
        pages = info[3]
        genre = info[4]
        price = info[5]
        status = info[6]
        temp = Book()
        temp.title = title
        temp.authorFirst = first
        temp.authorLast = last
        temp.pages = pages
        temp.genre = genre
        temp.price = price
        if status.strip() == "T":
            temp.status = True
        else:
            temp.status = False
        listA.append(temp)
    myFile.close()
    dataBaseReset(listA)
    return listA
