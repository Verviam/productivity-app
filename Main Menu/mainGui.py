from tkinter import *
from PIL import Image,ImageTk
from ctypes import windll, byref, sizeof, c_int
import customtkinter as ctk

root = Tk(className='Productivity') #create window and name
root.geometry("1080x720") # set window size
root.configure(bg='white') # set window color

Label(root, text="To Do List", bg="white", font=("Comic Sans MS", 15), wraplength=300).place(x=50, y=30.5) #Edit font size and wrap length and place later

tasks = Listbox(root, selectbackground='Gold', bg='Silver', font=('Helvetica', 12), height=12, width=25)
scroller = Scrollbar(root, orient=VERTICAL, command=tasks.yview)
scroller.place(x=260, y=80, height=232)

tasks.config(yscrollcommand=scroller.set)
tasks.place(x=35, y=80)

#taskbar
taskbar_border_color = Frame(root, background="black")
taskbar = Listbox(root, selectbackground='black', bg='azure3', font=('Helvetica', 12), height=50, width=5)
taskbar.place(x=0, y=500, height=800)

#home
homeImg = ImageTk.PhotoImage(Image.open("home.png"))
home = Label(root, image=homeImg, bg="white")
home.pack(side=BOTTOM)

root.mainloop()