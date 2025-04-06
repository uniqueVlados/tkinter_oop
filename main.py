import tkinter
from tkinter import ttk, Tk
from time import *
from PIL import ImageTk, Image

from main_screen import MainScreen
from condition_screen import ConditionScreen

win = Tk()
win.geometry("1920x1080")

cond = ConditionScreen(win)
menu = MainScreen(win, cond)


win.mainloop()