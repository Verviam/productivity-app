import tkinter as tk
from tkinter import ttk 
from tkinter import messagebox
from PIL import Image, ImageTk
import datetime as dt

root = tk.Tk()
root.geometry('1024x768')
root.resizable(False, False)
root.title('Productivity')

# icon
Image_icon = tk.PhotoImage(file="Image/productivity_icon.png")
root.iconphoto(False, Image_icon)

# Switch frame functions
def homePage():
    homeFrame = tk.Frame(displayFrame)
    topLabel = tk.Label(homeFrame, text='Productivity App', font=('Bold', 30), bg="#0B6E4F", fg="#00f678")
    topLabel.pack()

    homeFrame.pack(pady=20)

def toDoPage():
    toDoFrame = tk.Frame(displayFrame)
    topLabel = tk.Label(toDoFrame, text='To Do List', font=('Bold', 30), bg="#0B6E4F", fg="#00f678")
    topLabel.pack()
    
    toDoFrame.pack(pady=20)

def schedulePage():
    scheduleFrame = tk.Frame(displayFrame)
    topLabel = tk.Label(scheduleFrame, text='Schedule', font=('Bold', 30), bg="#0B6E4F", fg="#00f678")
    topLabel.pack()
    
    scheduleFrame.pack(pady=20)

def habitsPage():
    habitsFrame = tk.Frame(displayFrame)
    topLabel = tk.Label(habitsFrame, text='Habits', font=('Bold', 30), bg="#0B6E4F", fg="#00f678")
    topLabel.pack()
    
    habitsFrame.pack(pady=20)

def notesPage():
    notesFrame = tk.Frame(displayFrame)
    topLabel = tk.Label(notesFrame, text='Your Notes', font=('Bold', 30), bg="#0B6E4F", fg="#00f678")
    topLabel.pack()
    
    notesFrame.pack(pady=20)

def timerPage():
    timerFrame = tk.Frame(displayFrame)
    topLabel = tk.Label(timerFrame, text='Timer', font=('Bold', 30), bg="#0B6E4F", fg="#00f678")
    topLabel.pack()
    
    date = dt.datetime.now()
    
    timeLabel = tk.Label(displayFrame, text=f"{date:%A, %B %d, %Y}") # Create Label to display the Date
    time = f"{date:%A, %B %d, %Y}"
    date = tk.Label(displayFrame, text="Current Time: " + str(time), font="Bold, 20", bg="#0B6E4F", fg="#00f678")
    date.place(x=190, y=725)

    timerFrame.pack(pady=20)

def settingsPage():
    settingsFrame = tk.Frame(displayFrame)
    topLabel = tk.Label(settingsFrame, text='Settings', font=('Bold', 30))
    topLabel.pack()
    
    settingsFrame.pack(pady=20)

# Deletes Pages to switch to new frames
def deletePages():
    for frame in displayFrame.winfo_children():
        frame.destroy()

# Indicator functions
def indicator(label, page):
    hide_indicator()
    label.config(bg='#21D375')
    deletePages()
    page()


def hide_indicator():
    homeIndicate.config(bg='#073B3A')
    todoListIndicate.config(bg='#073B3A')
    scheduleIndicate.config(bg='#073B3A')
    habitsIndicate.config(bg='#073B3A')
    notesIndicate.config(bg='#073B3A')
    timerIndicate.config(bg='#073B3A')
    settingsIndicate.config(bg='#073B3A')

optionsMenu = tk.Frame(root, bg='#073B3A') 

# Home Image Button
homeImg = ImageTk.PhotoImage(Image.open("Image/home_img.png"))
homeButton = tk.Button(optionsMenu, image = homeImg, borderwidth=0, highlightthickness=0, command=lambda: indicator(homeIndicate, homePage), activebackground="#073B3A")
homeButton.place(x=10, y=50)
homeIndicate = tk.Label(optionsMenu, text='', bg = '#073B3A')
homeIndicate.place(x=3, y=50, width=5, height=40)

# To Do List Button
todoListImg = ImageTk.PhotoImage(Image.open("Image/todolist_img.png"))
todoListButton = tk.Button(optionsMenu, image = todoListImg,borderwidth=0, highlightthickness=0, command=lambda: indicator(todoListIndicate, toDoPage), activebackground="#073B3A")
todoListButton.place(x=10, y=105)
todoListIndicate = tk.Label(optionsMenu, text='', bg = '#073B3A')
todoListIndicate.place(x=3, y=105, width=5, height=40)

# Schedule Button
scheduleImg = ImageTk.PhotoImage(Image.open("Image/schedule_img.png"))
scheduleButton = tk.Button(optionsMenu, image = scheduleImg, borderwidth=0, highlightthickness=0, command=lambda: indicator(scheduleIndicate, schedulePage), activebackground="#073B3A")
scheduleButton.place(x=10, y=160)
scheduleIndicate = tk.Label(optionsMenu, text='', bg = '#073B3A')
scheduleIndicate.place(x=3, y=160, width=5, height=40)

# Habits Button
habitsImg = ImageTk.PhotoImage(Image.open("Image/habits_img.png"))
habitsButton = tk.Button(optionsMenu, image = habitsImg, borderwidth=0, highlightthickness=0, command=lambda: indicator(habitsIndicate, habitsPage), activebackground="#073B3A")
habitsButton.place(x=10, y=215)
habitsIndicate = tk.Label(optionsMenu, text='', bg = '#073B3A')
habitsIndicate.place(x=3, y=215, width=5, height=40)

# Notes Button
notesImg = ImageTk.PhotoImage(Image.open("Image/notes_img.png"))
notesButton = tk.Button(optionsMenu, image = notesImg, borderwidth=0, highlightthickness=0, command=lambda: indicator(notesIndicate, notesPage), activebackground="#073B3A")
notesButton.place(x=10, y=270)
notesIndicate = tk.Label(optionsMenu, text='', bg = '#073B3A')
notesIndicate.place(x=3, y=270, width=5, height=40)

# Timer Button
timerImg = ImageTk.PhotoImage(Image.open("Image/timer_img.png"))
timerButton = tk.Button(optionsMenu, image = timerImg, borderwidth=0, highlightthickness=0, command=lambda: indicator(timerIndicate, timerPage), activebackground="#073B3A")
timerButton.place(x=10, y=325)
timerIndicate = tk.Label(optionsMenu, text='', bg = '#073B3A')
timerIndicate.place(x=3, y=325, width=5, height=40)

# Settings Button
settingsImg = ImageTk.PhotoImage(Image.open("Image/settings_img.png"))
settingsButton = tk.Button(optionsMenu, image = settingsImg, borderwidth=0, highlightthickness=0, bg = "#073B3A", command=lambda: indicator(settingsIndicate, settingsPage), activebackground="#073B3A")
settingsButton.place(x=12, y=720)
settingsIndicate = tk.Label(optionsMenu, text='', bg = '#073B3A')
settingsIndicate.place(x=3, y=720, width=5, height=40) 


# Options Menu
optionsMenu.pack(side=tk.LEFT)
optionsMenu.pack_propagate(False)
optionsMenu.configure(width=210, height=2000) 

displayFrame = tk.Frame(root, bg='#0B6E4F')
displayFrame.pack(side=tk.LEFT)
displayFrame.pack_propagate(False)
displayFrame.configure(height = 2000, width = 2000)

# open home page as main page
homePage()
root.mainloop()

