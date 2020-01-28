import sqlite3
conn = sqlite3.connect('football.db')

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

    def __init__(self, fName, lName, num, height, weight, gpa, bench, squat, vert, fDash):
        self.__fName = fName
        self.__lName = lName
        self.__num = num
        self.__height = height
        self.__weight = weight
        self.__gpa = gpa
        self.__bench = bench
        self.__squat = squat
        self.__vert = vert
        self.__fDash = fDash

    def getfName(self):
        return self.__fName

    def getlName(self):
        return self.__lName

    def getNum(self):
        return self.__num

    def getHeight(self):
        return self.__height

    def setHeight(self, hgt):
        self.__height = hgt

    def getWeight(self):
        return self.__weight

    def setWeight(self, wgt):
        self.__weight = wgt

    def getGPA(self):
        return self.__gpa

    def setGPA(self, gpa):
        self.__gpa = gpa

    def getBench(self):
        return self.__bench

    def setBench(self, bench):
        self.__bench = bench

    def getSquat(self):
        return self.__squat

    def setSquat(self, squat):
        self.__squat = squat

    def getVert(self):
        return self.__vert

    def setVert(self, vert):
        self.__vert = vert

    def getfDash(self):
        return self.__fDash

    def setfDash(self, dash):
        self.__fDash = dash

root.mainloop()



