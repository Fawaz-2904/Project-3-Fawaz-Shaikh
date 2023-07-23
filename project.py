from tkinter import *
from PIL import Image, ImageTk
from self import self

self.bg = ImageTk.PhotoImage(file="D:\images\login.jpg")
bg=Label(self.root,image=self.bg).place(x=250, y=0, relwidth=1, relheight=1)


