from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from ctypes import windll, byref, sizeof, c_int
import customtkinter as ctk
# make images scale with window size function

# window setup
root = Tk(className='Productivity') #create window and name
#root.geometry("1080x720") # set window size
root.configure(bg='#0B6E4F') # set window color
root.state("zoomed")
# icon
Image_icon = PhotoImage(file="Image/productivity_icon.png")
root.iconphoto(False, Image_icon)

#scrollbar: All Below
# Create A Main frame
main_frame = Frame(root)
main_frame.pack(fill=BOTH, expand=1)

# Create A Canvas
my_canvas = Canvas(main_frame)
my_canvas.pack(side=LEFT, fill=BOTH, expand=1)
my_canvas.configure(bg='#0B6E4F')

# Add A Scrollbars to Canvas
scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
scrollbar.pack(side=RIGHT, fill=Y)

# Configure the canvas
my_canvas.configure(yscrollcommand=scrollbar.set)
my_canvas.bind("<Configure>", lambda e: my_canvas.config(scrollregion=my_canvas.bbox("all"))) 

# Create Another Frame INSIDE the Canvas
second_frame = Frame(my_canvas)

# Add that New Frame a Window In The Canvas
my_canvas.create_window((0,0),window=second_frame, anchor="nw")
#scrollbar: All Above

#for i in range(101):
    #idk = Button(second_frame, text=f'{i}').grid(row=i, column=0, pady=10, padx=100)

#taskbar 
taskbar = Listbox(root, selectbackground='black', bg='#073B3A', fg="#073B3A", font=('Helvetica', 12), height=60, width=30) #8
taskbar.place(x=-2, y=-3)

#logo
productivityIcon = ImageTk.PhotoImage(Image.open("Image/productivity_icon.png"))
productivity = Label(root, image=productivityIcon, bg="#073B3A")
productivity.place(x=8, y=5)

#home
homeImg = ImageTk.PhotoImage(Image.open("Image/home_img.png"))
home = Label(root, image=homeImg, bg="#073B3A")
home.place(x=16, y=56)
Label(root, text="Home", bg="#073B3A", fg ="#21D375", font=("Cambria", 20), wraplength=300).place(x=76, y=56)

#todolist
todolistImg = ImageTk.PhotoImage(Image.open ("Image/todolist_img.png"))
todolist = Label(root, image=todolistImg, bg="#073B3A")
todolist.place(x=int(14.7), y=100)
Label(root, text="Todolist", bg="#073B3A", fg ="#21D375", font=("Cambria", 19), wraplength=300).place(x=int(74.7), y=103)

#schedule
scheduleImg = ImageTk.PhotoImage(Image.open("Image/schedule_img.png"))
schedule = Label(root, image=scheduleImg, bg="#073B3A")
schedule.place(x=int(14.7), y=150)
Label(root, text="Schedule", bg="#073B3A", fg ="#21D375", font=("Cambria ", 17), wraplength=300).place(x=int(74.7), y=160)

#habits
habitsImg = ImageTk.PhotoImage(Image.open("Image/habits_img.png"))
habits = Label(root, image=habitsImg, bg="#073B3A")
habits.place(x=int(14.7), y=201)
Label(root, text="Habits", bg="#073B3A", fg ="#21D375", font=("Cambria", 19), wraplength=300).place(x=int(74.7), y=205)

#notes
notesImg = ImageTk.PhotoImage(Image.open("Image/notes_img.png"))
notes = Label(root, image=notesImg, bg="#073B3A")
notes.place(x=19, y=251)
Label(root, text="Notes", bg="#073B3A", fg ="#21D375", font=("Cambria", 19), wraplength=300).place(x=79, y=253)

#timer
timerImg = ImageTk.PhotoImage(Image.open("Image/timer_img.png"))
timer = Label(root, image=timerImg, bg="#073B3A")
timer.place(x=13, y=298)
Label(root, text="Timler", bg="#073B3A", fg ="#21D375", font=("Cambria", 22), wraplength=300).place(x=73, y=298)

#arrows
# arrowsImg = ImageTk.PhotoImage(Image.open("Image/right_arrows_img.png"))
# arrows = Label(root, image=arrowsImg, bg="#073B3A")
# arrows.place(x=23, y=930)

#settings
settingsImg = ImageTk.PhotoImage(Image.open("Image/settings_img.png"))
settings = Label(root, image=settingsImg, bg="#073B3A")
settings.place(x=230, y=970)

#name
Label(root, text="Muscle Cow", bg="#073B3A", fg ="#21D375", font=("Cambria", 100), wraplength=300).place(x=15, y=969)

# change the background color of side menu and main frame of app

Label(root, text="Hello Muscle Cow", bg="#0B6E4F", fg ="#21D375", font=("Cambria", 25), wraplength=300).place(x=300, y=10) #Edit font size and wrap length and place later

tasks = Listbox(root, selectbackground='Gold', bg='Silver', font=('Cambria', 12), height=12, width=25)
tasks.place(x=300, y=80)







# scroller = Scrollbar(root, orient=VERTICAL, command=tasks.yview)
# scroller.place(x=360, y=80, height=232)

# tasks.config(yscrollcommand=scroller.set)

root.mainloop()