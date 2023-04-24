from tkinter import *
from tkinter.ttk import *
import os

w = Tk()

w.title('Access')
w.geometry('200x200')


Label(w, text='Admin Access:').grid(column=0, row=0)

enter_pass = Entry(w, width=15)
enter_pass.grid(column=0, row=1)

# set password
password = 'password123'

# enter password, open admin file if password is correct
access = Label(w, text=None)
def go():
    if enter_pass.get() == password:
        access.config(text='Access Granted :)')
        os.system('python GUI_client_v2.py')
    else:
        access.config(text='Access Denied :(')
Button(w, text='Enter', command=go).grid(column=0, row=2)
access.grid(column=0, row=3)


# customer access, no need for password
def customer():
    os.system('python GUI_customer.py')
Button(w, text='Customer Access', command=customer).grid(column=0, row=4)


w.mainloop()