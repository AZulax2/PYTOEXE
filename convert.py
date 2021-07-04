import os
import PyInstaller.__main__
import tkinter
from tkinter import Tk
from tkinter import *
from tkinter import simpledialog
os.system('cls')

tk = Tk()
tk.geometry()
global filename
filename = simpledialog.askstring("fichier", "Choisissez un fichier a convertir", parent=tk)

def start():
    os.system("pyinstaller --onefile --log-level ERROR --distpath output --clean --noconfirm "+ filename + " -i \"NONE\"")
    os.remove(filename+".spec")
    os.system("rmdir /s /q build")
    os.system("rmdir /s /q __pycache__")

button = Button(tk, text='Convert', command=start).place(x=30,y=30)

tk.mainloop()