from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Football Stat Track")
root.geometry("650x550")


def func_exit():
    m_box = messagebox.askquestion("Exit", "Are you sure you want to exit?")
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
