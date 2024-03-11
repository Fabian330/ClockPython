import tkinter as tk
from tkinter import *
from time import strftime

root = tk.Tk()
root.title("Clock")
w = 500
h = 320
x_window = root.winfo_screenwidth() // 2 - w // 2
y_window = root.winfo_screenheight() // 3 - h // 4
position = str(w) + "x" + str(h) + "+" + str(x_window) + "+" + str(y_window)
root.geometry(position)
root.maxsize(500, 320)
root.minsize(500, 320)
root.configure(background="#161917")

def get_date():
    actual_date = strftime("%a, %d %b %Y")
    date.config(text = actual_date)
    date.after(1000, get_date)

def get_hour():
    actual_hour = strftime("%H:%M:%S")
    hour.config(text = actual_hour)
    hour.after(1000, get_hour)

sc = tk.Canvas(root, width = 500, height =90, bg = "#161917", highlightthickness = 0)
sc.pack()
date = Label(root, bg = "#161917", fg = "#FFFFFF", font = ("Sans Serif", 16))
date.pack()
hour = Label(root, bg = "#161917", fg = "#FFFFFF", font = ("Sans Serif", 64, "bold"))
hour.pack()
get_date()
get_hour()

root.mainloop()