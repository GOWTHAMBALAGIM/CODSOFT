from tkinter import *
from tkinter.ttk import Combobox
import random

screen = Tk()
screen.title("Password Generator")
screen.geometry('600x400')


def gen():
    if c1.get() != "":
        global sc1
        sc1.set("")
        passw = ""
        length = int(c1.get())
        lowercase = 'abcdefghijklmnopqrstuvwxyz'
        uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' + lowercase
        mixs = '0123456789' + lowercase + uppercase + '@#$%&*'

        if c2.get() == 'Low Strength':
            for i in range(0, length):
                passw = passw + random.choice(lowercase)
            sc1.set(passw)
        elif c2.get() == 'Medium Strength':
            for i in range(0, length):
                passw = passw + random.choice(uppercase)
            sc1.set(passw)
        elif c2.get() == 'High Strength':
            for i in range(0, length):
                passw = passw + random.choice(mixs)
            sc1.set(passw)


sc1 = StringVar()
t1 = Label(screen, text='Custom Password Generator', font=('Arial', 25), fg='red')
t1.place(x=60, y=0)
t2 = Label(screen, text='password:', font=('Arial', 14))
t2.place(x=145, y=250)

il = Entry(screen, font=('Arial', 14), textvariable=sc1, borderwidth=0, bg="SystemButtonFace")
il.place(x=270, y=250)
t3 = Label(screen, text='Length: ', font=('Arial', 14))
t3.place(x=145, y=120)

t4 = Label(screen, text='Strength:', font=('Arial', 14))
t4.place(x=145, y=155)

c1 = Entry(screen, font=('Arial', 14), width=10)
c1.place(x=230, y=120)

c2 = Combobox(screen, font=('Arial', 14), width=15)
c2['values'] = ('Low Strength', 'Medium Strength', 'High Strength')
c2.current(1)
c2.place(x=237, y=155)

b = Button(screen, text='Generate', font=('Arial', 14), fg='red', background="white", command=gen)
b.place(x=230, y=195)

screen.mainloop()