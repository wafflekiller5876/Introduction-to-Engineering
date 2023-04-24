import os


class Book:
    def __init__(self):
        self.authorFirst = ''
        self.authorLast = ''
        self.title = ''
        self.pages = ''
        self.genre = ''
        self.price = ''
        self.status = False
        


def bookMaker(title, first, last, pages, genre, price):
    temp = Book()
    temp.title = title
    temp.authorFirst = first
    temp.authorLast = last
    temp.pages = pages
    temp.genre = genre
    temp.price = price
    temp.status = True
    return temp




def dataBaseReader(name, listA):
    myFile = open(name)
    tempList = myFile.readlines()
    if len(tempList)>0:
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
    return listA


def dataBaseReset(listA):
    if os.path.exists("BookDataBase.txt"):
        os.remove("BookDataBase.txt")
    data = open("BookDataBase.txt", 'w')
    for i in listA:
        data.write(i.title)
        data.write(', ')
        data.write(i.authorFirst)
        data.write(', ')
        data.write(i.authorLast)
        data.write(', ')
        data.write(i.pages)
        data.write(', ')
        data.write(i.genre)
        data.write(', ')
        data.write(i.price)
        data.write(', ')
        if i.status == True:
            data.write('T')
            data.write('\n')
        else:
            data.write('F')
            data.write('\n')
    data.close()

listA = []
if os.path.exists("BookDataBase.txt"):
    listA = dataBaseReader("BookDataBase.txt", listA)
