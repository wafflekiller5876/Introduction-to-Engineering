import Book
import FileReader

#searches by title
#returns a list with books with the title 
def SearchTitle(list, title):
    tempList = []

    if (title == ""):
        return list
    
    for i in list:
        if i.title == title:
            tempList.append(i)
    return tempList

#searches by firstName
#returns a list with books with the firstName 
def SearchFirstName(list, fName):
    tempList = []

    if (fName == ""):
        return list

    for i in list:
        if i.authorFirst == fName:
            tempList.append(i)
    return tempList

#searches by lastName
#returns a list with books with the lastName 
def SearchLastName(list, lName):
    tempList = []

    if (lName == ""):
        return list

    for i in list:
        if i.authorLast == lName:
            tempList.append(i)

    return tempList

#searches by genre
#returns a list with books with the genre 
def SearchGenre(list, genre):
    tempList = []

    if (genre == ""):
        return list

    for i in list:
        if i.genre == genre:
            tempList.append(i)

    return tempList

#searches for specified parameters
#if a parameter == "" then it is considered empty
#returns a list of book objects
def Search(title, fName, lName, genre):
    list = Book.listA
    
    tempList = SearchTitle(list, title)
    tempList = SearchFirstName(tempList, fName)
    tempList = SearchLastName(tempList, lName)
    tempList = SearchGenre(tempList, genre)

    return tempList

#checks if a book has been purchased. If it is not in the database, it is out of stock
#returns a bool
def CheckInStock(title, fName, lName, genre):
    tempList = Search(title, fName, lName, genre)
    if not tempList:
        return False
    else:
        return True

# #Commented out test cases
# Book.listA = FileReader.fileReader("test_file.txt", Book.listA)
# test = Search("Harry Potter", "Calvin", "Hirschler", "Fiction")
# print(CheckInStock("Harry Potter", "Calvin", "Hirschler", "Fiction"))

# #if empty
# if not test:
#     print("Book not found")
# else:
#     for i in test:
#         print(i.title + " " + i.authorFirst)