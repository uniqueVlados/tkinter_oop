import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Отображение картинки через Pillow")

# Загрузка изображения через Pillow (поддерживает PNG, JPG и др.)
pil_image = Image.open("44i.png")  # Укажите путь к вашему изображению
tk_image = ImageTk.PhotoImage(pil_image)

# Создание Label с изображением
label = tk.Label(root, image=tk_image)
label.pack()

root.mainloop()