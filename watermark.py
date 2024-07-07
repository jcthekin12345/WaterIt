from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk
from tkinter import filedialog
from ttkbootstrap import Style
import pyautogui
import sys
import time

def position(func):
    def wrapper(*args, **kwargs):
        while True:
            x, y = pyautogui.position()
            print(x, y)
        return func(*args, **kwargs)
    return wrapper

def gui(root):
    root.title('WaterIt')
    root.geometry('1024x640')
    root.configure(background='#0E2954')
    root.resizable(width=True, height=True)

    #style section
    style = Style(theme='superhero')

    watermark_btn = ttk.Button(root, text='Add watermark', command=watermark_image).place(x=0, y=70)
    rm_watermark_btn = ttk.Button(root, text='Remove watermark').place(x=0, y=35)

    menubar = Menu(root)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="New", command=open_img)
    filemenu.add_command(label="Open")
    filemenu.add_command(label="Save")
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=root.quit)
    menubar.add_cascade(label="File", menu=filemenu)

    root.config(menu=menubar)

    root.mainloop()

def openfn():
    filename = filedialog.askopenfilename(title='open')
    return filename

def open_img():
    x = openfn()
    img = Image.open(x)
    width, height = img.size
    new_width = int(width * 0.40)
    new_height = int(height * 0.40)
    img = img.resize((new_width, new_height))
    img = ImageTk.PhotoImage(img)
    panel = Label(root, image=img)
    panel.image = img
    panel.place(x=300, y=0)


def watermark_image(image_path, output_path=None):
    with Image.open(image_path, "r") as img:
        img2 = img.copy()
        img2.show()


if __name__ == '__main__':
    root = Tk()
    pic_path = './imageFiles/watermark.jpg'
    output_path = './output'
    gui(root)




