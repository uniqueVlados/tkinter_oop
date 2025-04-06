import tkinter
from tkinter import ttk
from PIL import Image, ImageTk


class BaseScreen:

    def __init__(self, win):
        self.win = win
        self.buttons = []
        self.texts = {}
        self.photos = {}

    def add_button(self, text_, command_=None):
        self.buttons.append(ttk.Button(self.win, text=text_, command=command_))

    def render_buttons(self, padx_, pady_, anchor_=None):
        pass

    def add_text(self, w, bg_, fg_, title, text_, font_=("Arial", 15, "bold")):
        self.texts[title] = tkinter.Message(self.win, width=w, font=font_, bg=bg_, fg=fg_, text=text_)

    def render_text_by_name(self, padx_, pady_, title):
        self.texts[title].pack(padx=padx_, pady=pady_)

    def add_image(self, name, path):
        pil_image = Image.open(path)
        self.photos[name] = ImageTk.PhotoImage(pil_image)

    def render_image_by_name(self, name, padx_, pady_):
        tkinter.Label(self.win, image=self.photos[name]).pack(padx=padx_, pady=pady_)

    def clear_screen(self):
        for el in self.buttons:
            el.destroy()



