import sqlite3
from tkinter import *
from tkinter import Label, Button
import my_players
import add_player
import datetime

conn = sqlite3.connect('football.db')

date = datetime.datetime.now().date()


class Application(object):
    def __init__(self,master):
        self.master = master

        # Frames
        self.top=Frame(master,height=150,bg='green')
        self.top.pack(fill=X)
        self.bottom=Frame(master,height=500,bg='#adff2f')
        self.bottom.pack(fill=X)

        # Today's Date
        self.heading = Label(self.top, text='Football Stat Track', font='arial 15 bold', fg='#9AFEFF', bg='green')
        self.heading.place(x=260, y=60)
        self.date_lbl = Label(self.top, text="Today's Date: " + str(date), font='arial 12 bold', fg='#9AFEFF', bg='green')
        self.date_lbl.place(x=450, y=5)

        # My Players Button
        self.players_btn = Button(self.bottom, text='    My Players   ', font='arial 12 bold',
                                  command=self.open_my_players)
        self.players_btn.place(x=250, y=10)

        # Add A Player Button
        self.btn_add_player = Button(self.bottom, text='  Add A Player   ', font='arial 12 bold',
                                     command=self.open_add_players)
        self.btn_add_player.place(x=250, y=70)

    def open_my_players(self):
        players = my_players.my_players()

    def open_add_players(self):
        add_players_window = add_player.add_player()


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


def main():
    root = Tk()
    app = Application(root)
    root.title("Football Stattrack")
    root.geometry("650x550+350+200")
    root.resizable(False,False)
    root.mainloop()


if __name__ == '__main__':
    main()

