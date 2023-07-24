import tkinter as tk
from tkinter import ttk 
from tkinter import messagebox
from PIL import Image, ImageTk

root = tk.Tk()
root.geometry('700x600')
root.title('Productivity')

optionsMenu = tk.Frame(root, bg='#073B3A') 

optionsMenu.pack(side=tk.LEFT)
optionsMenu.pack_propagate(False)
optionsMenu.configure(width=150, height=2000) 

homePage = tk.Frame(root, bg='#0B6E4F')
homePage.pack(side=tk.LEFT)
homePage.pack_propagate(False)
homePage.configure(height = 2000, width = 2000)

# place label inside of frame
# scale frame size based on window size

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

class root(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        root = tk.Frame(self)
        root.pack()
        
        root.grid_rowconfigure(0, minsize = 2000)
        root.grid_columnconfigure(0, minsize = 2000)
        
        # # window setup
        # root = tk.Tk(className='Productivity') #create window and name
        # root.geometry("1080x720") # set window size
        # root.configure(bg='#0B6E4F') # set window color


        self.frames = {}
        for P in (homePage, toDoList, habits, schedule, notes):
            page = P(root, self)
            self.frames[P] = page
            page.grid(row = 0, column = 0, sticky="nsew")

        self.show_frame(homePage)

    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()



# # icon
# Image_icon = tk.PhotoImage(file="Image/productivity_icon.png")
# root.iconphoto(False, Image_icon)


# #taskbar 
# taskbar = tk.Listbox(root, selectbackground='black', bg='#073B3A', fg="#073B3A", font=('Helvetica', 12), height=60, width=8)
# taskbar.place(x=-2, y=-3)

# #logo
# productivityIcon = ImageTk.PhotoImage(Image.open("Image/productivity_icon.png"))
# productivity = tk.Label(root, image=productivityIcon, bg="#073B3A")
# productivity.place(x=8, y=5)

# #home
# homeImg = ImageTk.PhotoImage(Image.open("Image/home_img.png"))
# home = tk.Label(root, image=homeImg, bg="#073B3A")
# home.place(x=16, y=56)

# #todolist
# todolistImg = ImageTk.PhotoImage(Image.open("Image/todolist_img.png"))
# todolist = tk.Label(root, image=todolistImg, bg="#073B3A")
# todolist.place(x=int(14.7), y=100)

# #schedule
# scheduleImg = ImageTk.PhotoImage(Image.open("Image/schedule_img.png"))
# schedule = tk.Label(root, image=scheduleImg, bg="#073B3A")
# schedule.place(x=int(14.7), y=150)

# #habits
# habitsImg = ImageTk.PhotoImage(Image.open("Image/habits_img.png"))
# habits = tk.Label(root, image=habitsImg, bg="#073B3A")
# habits.place(x=int(14.7), y=201)

# #notes
# notesImg = ImageTk.PhotoImage(Image.open("Image/notes_img.png"))
# notes = tk.Label(root, image=notesImg, bg="#073B3A")
# notes.place(x=19, y=251)

# #arrows
# arrowsImg = ImageTk.PhotoImage(Image.open("Image/right_arrows_img.png"))
# arrows = tk.Label(root, image=arrowsImg, bg="#073B3A")
# arrows.place(x=23, y=930)

# #settings
# settingsImg = ImageTk.PhotoImage(Image.open("Image/settings_img.png"))
# settings = tk.Label(root, image=settingsImg, bg="#073B3A")
# settings.place(x=19, y=970)

# #timer
# timerImg = ImageTk.PhotoImage(Image.open("Image/timer_img.png"))
# timer = tk.Label(root, image=timerImg, bg="#073B3A")
# timer.place(x=13, y=298)

# # change the background color of side menu and root frame of app

# tk.Label(root, text="Hello Muscle Cow", bg="#0B6E4F", fg ="#21D375", font=("Helvetica", 25), wraplength=300).place(x=85, y=10) #Edit font size and wrap length and place later

# tasks = tk.Listbox(root, selectbackground='Gold', bg='Silver', font=('Helvetica', 12), height=12, width=25)
# tasks.place(x=135, y=80)


root = root()
root.mainloop()

