from tkinter import *
import sqlite3

conn = sqlite3.connect('football.db')

class add_player(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("650x650")
        self.title("Add A Player")
        self.resizable(False,False)

        self.heading = Label(self.top, text='Add A Player', font='arial 15 bold')
        self.heading.place(x=260, y=60)