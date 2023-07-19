from tkinter import *
from PIL import Image,ImageTk
from ctypes import windll, byref, sizeof, c_int
import customtkinter as ctk

# window setup
root = Tk(className='Productivity') #create window and name
root.geometry("1080x720") # set window size
root.configure(bg='#0B6E4F') # set window color
# icon
Image_icon = PhotoImage(file="Image/productivity_icon.png")
root.iconphoto(False, Image_icon)


#taskbar 
taskbar = Listbox(root, selectbackground='black', bg='#073B3A', fg="#073B3A", font=('Helvetica', 12), height=60, width=8)
taskbar.place(x=-2, y=-3)

#logo
productivityIcon = ImageTk.PhotoImage(Image.open("Image/productivity_icon.png"))
productivity = Label(root, image=productivityIcon, bg="#073B3A")
productivity.place(x=8, y=5)

#home
homeImg = ImageTk.PhotoImage(Image.open("Image/home_img.png"))
home = Label(root, image=homeImg, bg="#073B3A")
home.place(x=16, y=56)

#todolist
todolistImg = ImageTk.PhotoImage(Image.open("Image/todolist_img.png"))
todolist = Label(root, image=todolistImg, bg="#073B3A")
todolist.place(x=int(14.7), y=100)

#schedule
scheduleImg = ImageTk.PhotoImage(Image.open("Image/schedule_img.png"))
schedule = Label(root, image=scheduleImg, bg="#073B3A")
schedule.place(x=int(14.7), y=150)

#habits
habitsImg = ImageTk.PhotoImage(Image.open("Image/habits_img.png"))
habits = Label(root, image=habitsImg, bg="#073B3A")
habits.place(x=int(14.7), y=201)

#notes
notesImg = ImageTk.PhotoImage(Image.open("Image/notes_img.png"))
notes = Label(root, image=notesImg, bg="#073B3A")
notes.place(x=19, y=251)

#arrows
arrowsImg = ImageTk.PhotoImage(Image.open("Image/right_arrows_img.png"))
arrows = Label(root, image=arrowsImg, bg="#073B3A")
arrows.place(x=23, y=930)

#settings
settingsImg = ImageTk.PhotoImage(Image.open("Image/settings_img.png"))
settings = Label(root, image=settingsImg, bg="#073B3A")
settings.place(x=19, y=970)



#timer
timerImg = ImageTk.PhotoImage(Image.open("Image/timer_img.png"))
timer = Label(root, image=timerImg, bg="#073B3A")
timer.place(x=13, y=298)

# change the background color of side menu and main frame of app

Label(root, text="Hello Muscle Cow", bg="#0B6E4F", font=("Helvetica", 25), wraplength=300).place(x=150, y=30.5) #Edit font size and wrap length and place later

tasks = Listbox(root, selectbackground='Gold', bg='Silver', font=('Helvetica', 12), height=12, width=25)
scroller = Scrollbar(root, orient=VERTICAL, command=tasks.yview)
scroller.place(x=360, y=80, height=232)

tasks.config(yscrollcommand=scroller.set)
tasks.place(x=135, y=80)

root.mainloop()