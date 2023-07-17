from tkinter import *
from PIL import Image,ImageTk
from ctypes import windll, byref, sizeof, c_int
import customtkinter as ctk

# window setup
root = Tk(className='Productivity') #create window and name
root.geometry("1080x720") # set window size
root.configure(bg='white') # set window color

# icon
Image_icon = PhotoImage(file="productivity_icon.png")
root.iconphoto(False, Image_icon)

#menu bar
sideMenu = PhotoImage(file="menu_bar.png")
Label(root, image =sideMenu).place(x=0, y=0)
# change the background color of side menu and main frame of app

Label(root, text="To Do List", bg="white", font=("Arial", 15), wraplength=300).place(x=50, y=30.5) #Edit font size and wrap length and place later

tasks = Listbox(root, selectbackground='Gold', bg='Silver', font=('Helvetica', 12), height=12, width=25)
scroller = Scrollbar(root, orient=VERTICAL, command=tasks.yview)
scroller.place(x=260, y=80, height=232)

tasks.config(yscrollcommand=scroller.set)
tasks.place(x=35, y=80)

#home
homeImg = ImageTk.PhotoImage(Image.open("home.png"))
home = Label(root, image=homeImg, bg="white")
home.pack(anchor=NW)

root.mainloop()