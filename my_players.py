from tkinter import *
import sqlite3
import add_player

conn = sqlite3.connect('football.db')


class my_players(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("650x650+620+200")
        self.title("My Players")
        self.resizable(False, False)

        # Frames
        self.top = Frame(self, height=150, bg='white')
        self.top.pack(fill=X)
        self.bottomFrame = Frame(self, height=500, bg='#fcc324')
        self.bottomFrame.pack(fill=X)

        # Heading, image and date
        self.heading = Label(self.top, text='My Players', font='arial 15 bold',
                             fg='#003f8a', bg='white')
        self.heading.place(x=260, y=60)
        # Scroll bar
        self.sb=Scrollbar(self.bottomFrame,orient=VERTICAL)
        # Listbox
        self.listBox=Listbox(self.bottomFrame,width=60,height=31)
        self.listBox.grid(row=0, column=0,padx=(40,0))
        self.sb.config(command=self.listBox.yview)
        self.listBox.config(yscrollcommand=self.sb.set)
        self.sb.grid(row=0, column=1, sticky=N+S)

        # Buttons
        btn_add = Button(self.bottomFrame, text='Add', width=12, font='Sans 12 bold')
        btn_add.grid(row=0, column=2, sticky=N, padx=10, pady=10)

    def open_add_players(self):
        add_players_window = add_player.add_player()
        self.destroy()
