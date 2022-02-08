from tkinter import *
import calendar
from tkinter.tix import COLUMN

text=calendar.calendar(2019)

root = Tk()
root.geometry("500x600")
root.title("CALENDAR")
label1 = Label(root, text="CALENDAR",bg='dark gray',font=("times",28,'bold'))
label1.grid(row=1, column=1)