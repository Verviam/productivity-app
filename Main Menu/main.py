import tkinter as tk
from tkinter import ttk 
from tkinter import messagebox
from PIL import Image, ImageTk

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

    topLabel = tk.Label(homeFrame, text='Productivity App', font=('Bold', 30))
    topLabel.pack()

    homeFrame.pack(pady=20)



# Indicator functions
def indicator(label, page):
    hide_indicator()
    label.config(bg='#21D375')
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
homeButton = tk.Button(optionsMenu, image = homeImg, borderwidth=0, highlightthickness=0, command=lambda: indicator(homeIndicate, homePage))
homeButton.place(x=10, y=50)
homeIndicate = tk.Label(optionsMenu, text='', bg = '#073B3A')
homeIndicate.place(x=3, y=50, width=5, height=40)

# To Do List Button
todoListImg = ImageTk.PhotoImage(Image.open("Image/todolist_img.png"))
todoListButton = tk.Button(optionsMenu, image = todoListImg,borderwidth=0, highlightthickness=0, command=lambda: indicator(todoListIndicate))
todoListButton.place(x=10, y=105)
todoListIndicate = tk.Label(optionsMenu, text='', bg = '#073B3A')
todoListIndicate.place(x=3, y=105, width=5, height=40)

# Schedule Button
scheduleImg = ImageTk.PhotoImage(Image.open("Image/schedule_img.png"))
scheduleButton = tk.Button(optionsMenu, image = scheduleImg, borderwidth=0, highlightthickness=0, command=lambda: indicator(scheduleIndicate))
scheduleButton.place(x=10, y=160)
scheduleIndicate = tk.Label(optionsMenu, text='', bg = '#073B3A')
scheduleIndicate.place(x=3, y=160, width=5, height=40)

# Habits Button
habitsImg = ImageTk.PhotoImage(Image.open("Image/habits_img.png"))
habitsButton = tk.Button(optionsMenu, image = habitsImg, borderwidth=0, highlightthickness=0, command=lambda: indicator(habitsIndicate))
habitsButton.place(x=10, y=215)
habitsIndicate = tk.Label(optionsMenu, text='', bg = '#073B3A')
habitsIndicate.place(x=3, y=215, width=5, height=40)

# Notes Button
notesImg = ImageTk.PhotoImage(Image.open("Image/notes_img.png"))
notesButton = tk.Button(optionsMenu, image = notesImg, borderwidth=0, highlightthickness=0, command=lambda: indicator(notesIndicate))
notesButton.place(x=10, y=270)
notesIndicate = tk.Label(optionsMenu, text='', bg = '#073B3A')
notesIndicate.place(x=3, y=270, width=5, height=40)

# Timer Button
timerImg = ImageTk.PhotoImage(Image.open("Image/timer_img.png"))
timerButton = tk.Button(optionsMenu, image = timerImg, borderwidth=0, highlightthickness=0, command=lambda: indicator(timerIndicate))
timerButton.place(x=10, y=325)
timerIndicate = tk.Label(optionsMenu, text='', bg = '#073B3A')
timerIndicate.place(x=3, y=325, width=5, height=40)

# Settings Button
settingsImg = ImageTk.PhotoImage(Image.open("Image/settings_img.png"))
settingsButton = tk.Button(optionsMenu, image = settingsImg, borderwidth=0, highlightthickness=0, command=lambda: indicator(settingsIndicate))
settingsButton.place(x=12, y=700)
settingsIndicate = tk.Label(optionsMenu, text='', bg = '#073B3A')
settingsIndicate.place(x=3, y=700, width=5, height=40)
# Have user's name next to setting icon 
# change settings icon size and background

# Options Menu
optionsMenu.pack(side=tk.LEFT)
optionsMenu.pack_propagate(False)
optionsMenu.configure(width=210, height=2000) 

displayFrame = tk.Frame(root, bg='#0B6E4F')
displayFrame.pack(side=tk.LEFT)
displayFrame.pack_propagate(False)
displayFrame.configure(height = 2000, width = 2000)



    #     self.frames = {}
    #     for P in (homePage, toDoList, habits, schedule, notes):
    #         page = P(root, self)
    #         self.frames[P] = page
    #         page.grid(row = 0, column = 0, sticky="nsew")

    #     self.show_frame(homePage)

    # def show_frame(self, page):
    #     frame = self.frames[page]
    #     frame.tkraise()

root.mainloop()

