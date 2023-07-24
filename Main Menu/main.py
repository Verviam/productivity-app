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

optionsMenu = tk.Frame(root, bg='#073B3A') 

# Home Image Button
homeImg = ImageTk.PhotoImage(Image.open("Image/home_img.png"))
homeButton = tk.Button(optionsMenu, image = homeImg, borderwidth=0, highlightthickness=0)
homeButton.place(x=10, y=50)
homeIndicate = tk.Label(optionsMenu, text='', bg = '#073B3A')
homeIndicate.place(x=3, y=50, width=5, height=40)

#  fg= '#073B3A'
# To Do List Button
todoListImg = ImageTk.PhotoImage(Image.open("Image/todolist_img.png"))
todoListButton = tk.Button(optionsMenu, image = todoListImg,borderwidth=0, highlightthickness=0)
todoListButton.place(x=10, y=105)
todoListIndicate = tk.Label(optionsMenu, text='', bg = '#21D375')
todoListIndicate.place(x=3, y=105, width=5, height=40)

# Schedule Button
scheduleImg = ImageTk.PhotoImage(Image.open("Image/schedule_img.png"))
scheduleButton = tk.Button(optionsMenu, image = scheduleImg, borderwidth=0, highlightthickness=0)
scheduleButton.place(x=10, y=160)
scheduleIndicate = tk.Label(optionsMenu, text='', bg = '#21D375')
scheduleIndicate.place(x=3, y=160, width=5, height=40)

# Habits Button
habitsImg = ImageTk.PhotoImage(Image.open("Image/habits_img.png"))
habitsButton = tk.Button(optionsMenu, image = habitsImg, borderwidth=0, highlightthickness=0)
habitsButton.place(x=10, y=215)
habitsIndicate = tk.Label(optionsMenu, text='', bg = '#21D375')
habitsIndicate.place(x=3, y=215, width=5, height=40)

# Notes Button
notesImg = ImageTk.PhotoImage(Image.open("Image/notes_img.png"))
notesButton = tk.Button(optionsMenu, image = notesImg, borderwidth=0, highlightthickness=0)
notesButton.place(x=10, y=270)
notesIndicate = tk.Label(optionsMenu, text='', bg = '#21D375')
notesIndicate.place(x=3, y=270, width=5, height=40)

# Timer Button
timerImg = ImageTk.PhotoImage(Image.open("Image/timer_img.png"))
timerButton = tk.Button(optionsMenu, image = timerImg, borderwidth=0, highlightthickness=0)
timerButton.place(x=10, y=325)
timerIndicate = tk.Label(optionsMenu, text='', bg = '#21D375')
timerIndicate.place(x=3, y=325, width=5, height=40)

# Settings Button
settingsImg = ImageTk.PhotoImage(Image.open("Image/settings_img.png"))
settingsButton = tk.Button(optionsMenu, image = settingsImg, borderwidth=0, highlightthickness=0)
settingsButton.place(x=10, y=700)
settingsIndicate = tk.Label(optionsMenu, text='', bg = '#21D375')
settingsIndicate.place(x=3, y=700, width=5, height=40)

# Options Menu
optionsMenu.pack(side=tk.LEFT)
optionsMenu.pack_propagate(False)
optionsMenu.configure(width=210, height=2000) 

homePage = tk.Frame(root, bg='#0B6E4F')
homePage.pack(side=tk.LEFT)
homePage.pack_propagate(False)
homePage.configure(height = 2000, width = 2000)



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







root = root()
root.mainloop()

