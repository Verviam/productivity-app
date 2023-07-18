from tkinter import *
from PIL import Image,ImageTk
from ctypes import windll, byref, sizeof, c_int
import customtkinter as ctk

# window setup
root = Tk(className='Productivity') #create window and name
root.geometry("1080x720") # set window size
root.configure(bg='white') # set window color
# icon
Image_icon = PhotoImage(file="Image/productivity_icon.png")
root.iconphoto(False, Image_icon)


#taskbar
taskbar_border_color = Frame(root, background="black")
taskbar = Listbox(root, selectbackground='black', bg='#073B3A', fg="#073B3A", font=('Helvetica', 12), height=50, width=7)
taskbar.place(x=-2, y=0)

#home
homeImg = ImageTk.PhotoImage(Image.open("Image/home.png"))
home = Label(root, image=homeImg, bg="#073B3A")
home.place(x=-1, y=0)

#home
todolistImg = ImageTk.PhotoImage(Image.open("Image/todolist_img.png"))
todolist = Label(root, image=todolistImg, bg="#073B3A")
todolist.place(x=-1, y=55)

# change the background color of side menu and main frame of app

Label(root, text="To Do List", bg="white", font=("Arial", 15), wraplength=300).place(x=150, y=30.5) #Edit font size and wrap length and place later

tasks = Listbox(root, selectbackground='Gold', bg='Silver', font=('Helvetica', 12), height=12, width=25)
scroller = Scrollbar(root, orient=VERTICAL, command=tasks.yview)
scroller.place(x=360, y=80, height=232)

tasks.config(yscrollcommand=scroller.set)
tasks.place(x=135, y=80)

root.mainloop()