from tkinter import *
from tkinter import messagebox
from random import randint
from PIL import Image, ImageTk

root = Tk()

width = root.winfo_screenwidth()
height = root.winfo_screenheight()

root.geometry(f"{width}x{height}")
root.resizable(False, False)


image = Image.open('space.jpg')
image = image.resize((width, height))
image = ImageTk.PhotoImage(image)

label = Label(root, image=image)
label.place(relheight=1, relwidth=1)

def on_hover(btn):
    a, b = randint(100, width-140), randint(20, height-30)
    btn.place(x=(a-w)//2, y=(b-h)//2)


def on_click():
    messagebox.showinfo("Tabriklaymiz", "Tugmani bosganingiz bilan ")


button = Button(root, text="Click me!", command=on_click, border=0)
w, h = 140, 30
button.place(x=(width-w)//2, y=(height-h)//2)

button.bind('<Enter>', lambda e: on_hover(button))

root.mainloop()
