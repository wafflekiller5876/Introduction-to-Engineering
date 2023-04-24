from tkinter import *
from tkinter.ttk import *

from PIL import ImageTk

from Book import *
from Search import *
from CheckOut import *

window = Tk()

window.title('Library Terminal')

# background image
bg_img = ImageTk.PhotoImage(file='bookshelf.jpg')
w = bg_img.width()
h = bg_img.height()

# window size
window.geometry('%dx%d+0+0' % (w,h))

# creating a canvas to put everything on
canvas = Canvas(window, width=w, height=h)
canvas.pack(fill='both', expand=True)

# function to place things on canvas
def canv_place(x, y, thing):
    id = canvas.create_window(x, y, anchor='c', window=thing)
    return id

# pixel rows + columns
nums = [30]
n = 30
for i in range(30):
    n += 35
    nums.append(n)

r1, r2, r3, r4, r5 = nums[0], nums[1], nums[2], nums[3], nums[4]
r6, r7, r8, r9, r10 = nums[5], nums[6], nums[7], nums[8], nums[9]
r11, r12, r13, r14, r15 = nums[10], nums[11], nums[12], nums[13], nums[14]
r16, r17, r18, r19, r20 = nums[15], nums[16], nums[17], nums[18], nums[19]
r21, r22, r23, r24, r25 = nums[20], nums[21], nums[22], nums[23], nums[24]
r26, r27, r28, r29, r30 = nums[25], nums[26], nums[27], nums[28], nums[29]

mid = w/2
midA = w/2 - 80
midB = w/2 + 80

c1A, c2A= w/3, 2 * w/3
c1B, c2B, c3B, c4B = (c1A - 80), (c1A + 80), (c2A - 80), (c2A + 80)


# making background image
canvas.create_image(0, 0, image=bg_img, anchor='nw')

# title creation
title = Label(window, text='Welcome to the Library Terminal!', font=('Times New Roman', 20, 'bold'))
canv_place(mid, r1, title)

# client options, buttons

def label(x, y, text):
    temp = Label(window, text=text)
    canv_place(x, y, temp)

def entry():
    temp = Entry(window, width=20)
    return temp

# find books
def find_books():
    
    label(c1B, r3, 'Title:')
    entry1 = entry()
    canv_place(c2B, r3, entry1)

    label(c1B, r4, 'Author First:')
    entry2 = entry()
    canv_place(c2B, r4, entry2)

    label(c1B, r5, 'Author Last:')
    entry3 = entry()
    canv_place(c2B, r5, entry3)

    label(c1B, r6, 'Genre:')
    entry4 = entry()
    canv_place(c2B, r6, entry4)


    def go_search():

        title = f'{entry1.get()}'
        author_first = f'{entry2.get()}'
        author_last = f'{entry3.get()}'
        genre = f'{entry4.get()}'

        result = Search(title, author_first, author_last, genre)


        result_window = Tk()
        result_window.title('Search Results')

        Label(result_window, text='Title', font=('Times', 12, 'bold')).grid(column=0, row=0)
        Label(result_window, text='Author', font=('Times', 12, 'bold')).grid(column=1, row=0)
        Label(result_window, text='Pages', font=('Times', 12, 'bold')).grid(column=2, row=0)
        Label(result_window, text='Genre', font=('Times', 12, 'bold')).grid(column=3, row=0)
        Label(result_window, text='Price', font=('Times', 12, 'bold')).grid(column=4, row=0)
        Label(result_window, text='Status', font=('Times', 12, 'bold')).grid(column=5, row=0)

        class display_line_results:
            
            def __init__(self, book):
                
                self.book = book

                self.title = Label(result_window, text=f'{book.title}')
                self.title.grid(column=0, row=result.index(book)+1)

                self.author_name = Label(result_window, text=f'{book.authorFirst} {book.authorLast}')
                self.author_name.grid(column=1, row=result.index(book)+1)

                self.pages = Label(result_window, text=f'{book.pages}')
                self.pages.grid(column=2, row=result.index(book)+1)

                self.genre = Label(result_window, text=f'{book.genre}')
                self.genre.grid(column=3, row=result.index(book)+1)

                self.price = Label(result_window, text=f'{book.price}')
                self.price.grid(column=4, row=result.index(book)+1)

                if book.status == True:
                    self.status = 'In Stock'
                else:
                    self.status = 'Out of Stock'

                self.status_lbl = Label(result_window, text=self.status)
                self.status_lbl.grid(column=5, row=result.index(book)+1)
                
                self.chk_text = Label(result_window, text='')
                self.chk_text.grid(column=8, row=result.index(book)+1)

                def check_in(title):
                    checkIn(listA, title)
                    self.chk_text.config(text='Checked In!')
                
                def check_out(title):
                    checkOut(listA, title)
                    self.chk_text.config(text='Checked Out!')

                self.checkin = Button(result_window, text='Check In', command=lambda: check_in(book.title))
                self.checkin.grid(column=6, row=result.index(book)+1)

                self.checkout = Button(result_window, text='Check Out', command=lambda: check_out(book.title))
                self.checkout.grid(column=7, row=result.index(book)+1)

        for book in result:
            display_line_results(book)

        result_window.mainloop()

    go = Button(window, text='Go', command=go_search)
    canv_place(c1A, r7, go)

find_book_btn = Button(window, text='Find Book', command=find_books)
canv_place(c1A, r2, find_book_btn)



# display database
class param_btns:

    def __init__(self, param, row):
        
        self.text = param

        self.chkvar = BooleanVar()
        self.chkvar.set(True)

        self.chkbtn = Checkbutton(window, text=self.text, var=self.chkvar)
        canv_place(c2A, row, self.chkbtn)

def make_chk(param, row):
    new_btn = param_btns(param, row)
    return new_btn

title_chk = make_chk('Title', r3)
name_chk = make_chk('Author', r4)
pages_chk = make_chk('Pages', r5)
genre_chk = make_chk('Genre', r6)
price_chk = make_chk('Price', r7)
status_chk = make_chk('Status', r8)

params = [title_chk, name_chk, pages_chk, genre_chk, price_chk, status_chk]

def display_books():
    
    dbase_window = Tk()
    dbase_window.title('Database')

    for param in params:
        if param.chkvar.get() == True:
            Label(dbase_window, text=param.text, font=('Times', 12, 'bold')).grid(column=params.index(param), row=0)

    class display_line_dbase:

        def __init__(self, book):
            
            self.title = Label(dbase_window, text=f'{book.title}')
            if title_chk.chkvar.get() == True:
                self.title.grid(column=0, row=listA.index(book)+1)

            self.author_name = Label(dbase_window, text=f'{book.authorFirst} {book.authorLast}')
            if name_chk.chkvar.get() == True:
                self.author_name.grid(column=1, row=listA.index(book)+1)

            self.pages = Label(dbase_window, text=f'{book.pages}')
            if pages_chk.chkvar.get() == True:
                self.pages.grid(column=2, row=listA.index(book)+1)
            
            self.genre = Label(dbase_window, text=f'{book.genre}')
            if genre_chk.chkvar.get() == True:
                self.genre.grid(column=3, row=listA.index(book)+1)

            self.price = Label(dbase_window, text=f'{book.price}')
            if price_chk.chkvar.get() == True:
                self.price.grid(column=4, row=listA.index(book)+1)

            if book.status == True:
                self.status = 'In Stock'
            else:
                self.status = 'Out of Stock'

            self.status_lbl = Label(dbase_window, text=self.status)
            if status_chk.chkvar.get() == True:
                self.status_lbl.grid(column=5, row=listA.index(book)+1)

    for book in listA:
        display_line_dbase(book)


    dbase_window.mainloop()

display_btn = Button(window, text='Display Full Database', command=display_books)
canv_place(c2A, r2, display_btn)


window.mainloop()