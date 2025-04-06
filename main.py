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

#TODO:
# 1) Сделать отдельным классом входное меню (наследоваться от BaseScreen)
# 2) esc_btn переопределить в BaseScreen и разделить логику(можно проверять по self, от какого объекта был вызван)
# 3) Вынести esc_btn в нужные классы экранов и вызывать
# 4) Дооформить все экраны, кроме опыта (2ух последних)
# 4) Сделать классы для самолёта, пули и мишени (наследоваться от базового класса предмета - этот класс тоже сделать)