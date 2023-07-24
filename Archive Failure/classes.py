
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
