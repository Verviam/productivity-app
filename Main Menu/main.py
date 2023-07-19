import tkinter as tk
from tkinter import ttk 
from tkinter import messagebox
from PIL import Image, ImageTk

#One of the best ways to get things done is by creating habits and systems. Productivity helps you get things done by using scientifically proven ways to help you create habits to manage your schedule and todo lists and enjoy doing work
#print("Productivity: Get Stuff Done \n Menu: To-Do List, Habit Tracker, My Schedule, ")

# press button and switch to new file
# def toDoPress():

#Classes
class homePage(tk.Frame): 
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        topLabel = tk.Label(self, text="Welcome ____! Here are the tasks you have for today.", font=("Playfair Display", 30))
        topLabel.place(x=500, y=600)

        habitsButton = tk.Button(self, text="Habits", font=("Arial", 15), command=lambda: controller.show_frame(habits))
        habitsButton.place(x=400, y=320)
        # make text in each button adjustable based on user inputs in specific frame 

        toDoListButton = tk.Button(self, text="To Do List", font=("Arial", 15), command=lambda: controller.show_frame(toDoList))
        toDoListButton.place(x=700, y=320)
        # add commands for taskbar image click button

        scheduleButton = tk.Button(self, text="Schedule", font=("Arial", 15), command=lambda: controller.show_frame(schedule))
        scheduleButton.place(x=700, y=720)

        notesButton = tk.Button(self, text="Notes", font=("Arial", 15), command=lambda: controller.show_frame(notes))
        notesButton.place(x=500, y=0)


class toDoList(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        topLabel = tk.Label(self, text="Here is your To Do List", font=("Playfair Display", 30))
        topLabel.place(x=500, y=600)

        backButton = tk.Button(self, text="Back Arrow Key", font=("Arial, 15"), command=lambda: controller.show_frame(homePage))
        backButton.place(x=1000, y=0)
        
class habits(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        topLabel = tk.Label(self, text="Here are your habits", font=("Playfair Display", 30))
        topLabel.place(x=500, y=600)

        backButton = tk.Button(self, text="Back Arrow Key", font=("Arial, 15"), command=lambda: controller.show_frame(homePage))
        backButton.place(x=1000, y=0)

class schedule(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        topLabel = tk.Label(self, text="Schedule", font=("Playfair Display", 40))
        topLabel.place(x=500, y=600)

        backButton = tk.Button(self, text="Back Arrow Key", font=("Arial, 15"), command=lambda: controller.show_frame(homePage))
        backButton.place(x=1000, y=0)

class notes(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        topLabel = tk.Label(self, text="Notes", font=("Playfair Display", 30))
        topLabel.place(x=500, y=600)

        backButton = tk.Button(self, text="Back Arrow Key", font=("Arial, 15"), command=lambda: controller.show_frame(homePage))
        backButton.place(x=1000, y=0)

class main(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        root = tk.Frame(self)
        root.pack()

        # window setup
        root = tk.Tk(className='Productivity') #create window and name
        root.geometry("1080x720") # set window size
        root.configure(bg='#0B6E4F') # set window color
        # icon
        imageIcon = ImageTk.PhotoImage(Image.open("Image/productivity_icon.png"))
        root.iconphoto(False, imageIcon)

        #taskbar 
        taskbar = tk.Listbox(root, selectbackground='black', bg='#073B3A', fg="#073B3A", font=('Helvetica', 12), height=60, width=8)
        taskbar.place(x=-2, y=-3)

        #logo
        productivityIcon = ImageTk.PhotoImage(Image.open("Image/productivity_icon.png"))
        productivity = tk.Label(root, image=productivityIcon, bg="#073B3A")
        productivity.place(x=8, y=5)

        #home
        homeImg = ImageTk.PhotoImage(Image.open("Image/home_img.png"))
        home = tk.Label(root, image=homeImg, bg="#073B3A")
        home.place(x=16, y=56)

        #todolist
        todolistImg = ImageTk.PhotoImage(Image.open("Image/todolist_img.png"))
        todolist = tk.Label(root, image=todolistImg, bg="#073B3A")
        todolist.place(x=int(14.7), y=100)

        #schedule
        scheduleImg = ImageTk.PhotoImage(Image.open("Image/schedule_img.png"))
        schedule = tk.Label(root, image=scheduleImg, bg="#073B3A")
        schedule.place(x=int(14.7), y=150)

        #habits
        habitsImg = ImageTk.PhotoImage(Image.open("Image/habits_img.png"))
        habits = tk.Label(root, image=habitsImg, bg="#073B3A")
        habits.place(x=int(14.7), y=201)

        #notes
        notesImg = ImageTk.PhotoImage(Image.open("Image/notes_img.png"))
        notes = tk.Label(root, image=notesImg, bg="#073B3A")
        notes.place(x=19, y=251)


        #timer
        timerImg = ImageTk.PhotoImage(Image.open("Image/timer_img.png"))
        timer = tk.Label(root, image=timerImg, bg="#073B3A")
        timer.place(x=13, y=298)

        # change the background color of side menu and main frame of app

        tk.Label(root, text="Hello Muscle Cow", bg="#0B6E4F", font=("Helvetica", 25), wraplength=300).place(x=150, y=30.5) #Edit font size and wrap length and place later

        tasks = tk.Listbox(root, selectbackground='Gold', bg='Silver', font=('Helvetica', 12), height=12, width=25)
        scroller = tk.Scrollbar(root, orient=tk.VERTICAL, command=tasks.yview)
        scroller.place(x=360, y=80, height=232)

        tasks.config(yscrollcommand=scroller.set)
        tasks.place(x=135, y=80)


        self.frames = {}
        for P in (homePage, toDoList, habits, schedule, notes):
            page = P(root, self)
            self.frames[P] = page
            page.grid(row = 0, column = 0, sticky="nsew")

        self.show_frame(homePage)

        def show_frame(self, page):
            frame = self.frames[page]
            frame.tkraise()

main = main()
main.mainloop()
