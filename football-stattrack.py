from tkinter import *
from tkinter import messagebox, Label
import datetime

root = Tk()
root.title("Football Stat Track")
root.geometry("650x550")
root.configure(background='green')
date = datetime.datetime.now().date()

heading = Label(root, text='Football Stat Track', font='arial 15 bold', fg='#ADD8E6', bg='green')
heading.pack()


date_lbl = Label(root,text="Today's Date: " + str(date),font='arial 12 bold',fg='#ADD8E6', bg='green')
date_lbl.pack()


def func_exit():
    m_box = messagebox.askquestion("Exit", "Are you sure you want to exit?",icon='warning')
    if m_box == 'yes':
        root.destroy()


menu_bar = Menu(root)
root.config(menu=menu_bar)
file = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='File', menu=file)
file.add_command(label='Exit', compound=LEFT, command=func_exit)


class Player:

    def _init_(self, fName, lName, num, height, weight, gpa, bench, squat, vert, fDash):
        self.fName = fName
        self.lName = lName
        self.num = num
        self.height = height
        self.weight = weight
        self.gpa = gpa
        self.bench = bench
        self.squat = squat
        self.vert = vert
        self.fDash = fDash


root.mainloop()


#Adrianna Ambeau Database Code
#Note that you must create the c:\sqlite\db folder first before you execute the program.
#Or you can place the database file a folder of your choice.

import sqlite3
conn = sqlite3.connect('football.db')
