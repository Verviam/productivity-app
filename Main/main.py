import tkinter as tk
from tkinter import ttk 
from tkinter import messagebox
from PIL import Image, ImageTk
import datetime as dt
from time import strftime
from tkcalendar import DateEntry
from tkinter import filedialog
from functools import partial
import json
import notes
import os

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
    welcomeLabel = tk.Label(displayFrame, text='Hello User298302', font=('Bold', 30), bg="#0B6E4F", fg="#00f678")
    welcomeLabel.place(x=10, y=10)
    cover = tk.Frame(displayFrame, bg='red')
    cover.configure(width=33, height=33, bg='#0B6E4F')
    cover.place(x=390, y=10)
 
    # drag and drop habits and to do into schedule 
    # only show today's schedule
    # find out why it can't be located on top left corner if the tk.Label is in (homeFrame)
    homeFrame.pack(pady=20)

def toDoPage():
    toDoFrame = tk.Frame(displayFrame)
    topLabel = tk.Label(toDoFrame, text='To Do List', font=('Bold', 30), bg="#0B6E4F", fg="#00f678")
    topLabel.pack()
    # add different to do lists for different tasks
    toDoFrame.pack(pady=20)

def schedulePage():
    scheduleFrame = tk.Frame(displayFrame, bg = '#073B3A')
    topLabel = tk.Label(scheduleFrame, text='Schedule', font=('Bold', 30), bg="#073B3A", fg="#00f678")
    topLabel.pack()
    
    def saveTask():
        if tasks:
            with open('tasks.json', 'w') as file: 
                json.dump(tasks, file)

        # Add handling for cases when the user doesn't select time

    def updateTaskLabel(timestamp): # change to be based on date too or delete
        selectedTime = timeClick.get()
        taskText = tasks.get(timestamp, "")

        for label in timeLabelsPm:
            timePm = label.cget ("text")
            if timePm.startswith(selectedTime) and timePm.endswith("pm:"):
                label.config(text=timePm.replace("pm:", "pm: " + taskText))
        for label in timeLabelsAm:
            timeAm = label.cget("text")
            if timeAm.startswith(selectedTime) and timeAm.endswith("am:"):
                label.config(text=timeAm.replace("am:", "am: " + taskText))

    def addTaskClick():
        dateInput = cal.get_date()
        taskInput = taskEntry.get()
        timeInput = timeClick.get() 
        
        if dateInput and timeInput and taskInput:
            timestamp = f"{dateInput.strftime('%Y-%m-%d')} {timeInput}" 
            tasks[timestamp] = taskInput
            saveTask()
            updateTaskLabel(timestamp)
     
    def onClose():
        saveTask()
        root.destroy()

    def loadTask():
        global tasks
        if os.path.exists('tasks.json'):
            with open('tasks.json', 'r+') as file:  # see if r+ neededd
                    tasks = json.load(file)
                    for timestamp in tasks.keys():
                        updateTaskLabel(timestamp)
        else: 
            tasks = {}
    
    # Entrybox with temporary text
    def delTempText(e):
        taskEntry.delete(0,"end") 
    
    loadTask()
    def setup_schedule_frame():
        scheduleFrame = tk.Frame(displayFrame, bg='#073B3A')
        scheduleFrame.pack(pady=20)
        Pm = "pm:"
        numsPm = ['11', '10', '9', '8', '7', '6', '5', '4', '3', '2', '1', '12']
        timeLabelsPm= []
        for numPm in numsPm: #iterates over your nums
            timePm = numPm + Pm 
            pmLabel = tk.Label(scheduleFrame,text=timePm, fg="#00f678", bg="#073B3A", font=('Bold', 12)) #set your text
            pmLabel.pack(padx=5)
            timeLabelsPm.append(pmLabel) #appends the label to the list for further use

        Am = "am:"
        numsAm = ['11', '10', '9', '8', '7', '6', '5', '4', '3', '2', '1', '12']
        timeLabelsAm=[] 
        for numAm in numsAm: #iterates over your nums
            timeAm = numAm + Am
            amLabel = tk.Label(scheduleFrame,text=timeAm, fg="#00f678", bg="#073B3A", font=('Bold', 12)) #set your text
            amLabel.pack(padx=5)
            timeLabelsAm.append(amLabel) #appends the label to the list for further use
        
        for label in range (len(timeLabelsAm)):
            timeLabelsAm[label].pack(anchor = "sw", side=tk.BOTTOM)

        for label in range (len(timeLabelsPm)):
            timeLabelsPm[label].pack(anchor = "sw", side=tk.BOTTOM)
    
        taskEntry = tk.Entry(scheduleFrame, width=40)
        taskEntry.pack(padx=100)
        taskEntry.insert(0, 'Enter Your Task Here')
        taskEntry.bind("<FocusIn>", delTempText)
        
        # Select Day Calendar
        cal = DateEntry(scheduleFrame, width=12, background="#00f678", foreground='black', borderwidth=2)
        cal.pack(side=tk.TOP)

        # Select Time
        options = [
            "12am", 
            "1am", 
            "2am", 
            "3am", 
            "4am", 
            "5am", 
            "6am", 
            "7am", 
            "8am", 
            "9am", 
            "10am", 
            "11am", 
            "12pm", 
            "1pm", 
            "2pm", 
            "3pm", 
            "4pm", 
            "5pm", 
            "6pm", 
            "7pm", 
            "8pm", 
            "9pm", 
            "10pm", 
            "11pm"
            ]
        
        timeClick = tk.StringVar()

        timeClick.set("Select a Time")
        dropDown = tk.OptionMenu(scheduleFrame, timeClick, *options)
        dropDown.pack()

        tasks = {} 

        addTaskButton = ttk.Button(scheduleFrame, text="Add Task", command=addTaskClick)
        addTaskButton.pack()

        root.protocol("WM_DELETE_WINDOW", onClose) #saves tasks when window closed
        scheduleFrame.pack(pady=20) # make it able to be called back to home page
    displayFrame.destroy()
    setup_schedule_frame()

def habitsPage():
    habitsFrame = tk.Frame(displayFrame)
    topLabel = tk.Label(habitsFrame, text='Habits', font=('Bold', 30), bg="#0B6E4F", fg="#00f678")
    topLabel.pack()
    
    habitsFrame.pack(pady=20)

def notesPage():

    displayFrame.destroy()

    mainnotesFrame = tk.Frame(root, bg='#0B6E4F')
    mainnotesFrame.pack(side=tk.LEFT)
    mainnotesFrame.pack_propagate(False)
    mainnotesFrame.configure(height = 2000, width = 2000)

    def add_notes():
        new_note = tk.Button(mainnotesFrame, text="Untitled", font=('Bold', 20), bg="#073B3A", fg="#00f678", 
                            activebackground="#073B3A", activeforeground="#00f678", borderwidth=0, highlightthickness=0)
        new_note.pack(padx=50, pady=5, ipadx=900, before=add_note)
        mainnotesFrame.destroy()

    filler = tk.Button(mainnotesFrame, text="", font=('Bold', 12), bg="#0B6E4F", fg="#00f678", activebackground="#0B6E4F", 
                            activeforeground="#00f678", borderwidth=0, highlightthickness=0)
    filler.pack(padx=50, pady=5, ipadx=900)

    file_path = 'D:/Python/productivity-app/productivity-app/Main/notes/Note Example.txt'
    file_name = os.path.basename(file_path)
    title = os.path.splitext(file_name)[0]

    note_example = tk.Button(mainnotesFrame, text=title, font=('Bold', 20), bg="#073B3A", fg="#00f678", 
                                activebackground="#073B3A", activeforeground="#00f678", borderwidth=0, highlightthickness=0)
    note_example.pack(padx=50, pady=5, ipadx=900)

    add_note = tk.Button(mainnotesFrame, text="+", font=('Bold', 20), bg="#073B3A", fg="#00f678", 
                            activebackground="#073B3A", activeforeground="#00f678", borderwidth=0, highlightthickness=0,
                            command=add_notes)
    add_note.pack(padx=50, pady=5, ipadx=900)
                
    

    notesFrame = tk.Frame(root, bg='#0B6E4F')
    notesFrame.pack(side=tk.LEFT)
    notesFrame.pack_propagate(False)
    notesFrame.configure(height = 2000, width = 2000)
    
    def goback():
        notesFrame.destroy()
        notesPage()

    def del_temp_text(e):
        title.delete(0, "end")
    
    def on_enter():
        text = note_entry.get("1.0", tk.END).strip()
        # Handle the text entered when the Return key is pressed
                
    def save():
        title_to_save = title.get()
        file_path = f"D:/Python/productivity-app/Main/notes/{title_to_save}.txt"
        
        with open(file_path, "w") as file:
            text_to_save = note_entry.get("1.0", tk.END)  # Get the text from the note_entry widget
            file.write(text_to_save)
        
        save_button.config(text="Saved!")
        save_button.after(2000, lambda: save_button.config(text="Save"))

    # Create widgets
    entry_button_frame = tk.Frame(notesFrame, bg="#0B6E4F")
    entry_button_frame.pack(side="top", padx=10, pady=10, fill="x")

    go_back_button = tk.Button(entry_button_frame, text="<", font=('Bold', 20), bg="#073B3A", fg="#00f678",
                                activebackground="#073B3A", activeforeground="#00f678",
                                borderwidth=0, highlightthickness=0, command=goback)
    go_back_button.pack(side="left", padx=10, pady=10)
            
    title = tk.Entry(entry_button_frame, font=('Bold', 30), bg="#073B3A", fg="#00f678", 
                        borderwidth=0, highlightthickness=0, justify='center')
    title.pack(side="left", padx=10, pady=10, fill="x", expand=True)
    title.insert(0, 'Untitled')
    title.bind("<FocusIn>", del_temp_text)
            
    save_button = tk.Button(entry_button_frame, text="Save", font=('Bold', 20), bg="#073B3A", fg="#00f678",
                            activebackground="#073B3A", activeforeground="#00f678", 
                            borderwidth=0, highlightthickness=0, command=save)
    save_button.pack(side="left", padx=10, pady=10)
            
    note_entry = tk.Text(notesFrame, font=('Bold', 20), bg="#073B3A", fg="#00f678", borderwidth=0, highlightthickness=0, wrap='word')
    note_entry.pack(padx=10, pady=10, ipadx=200, ipady=200, fill="both", expand=True)
    note_entry.bind("<Return>", on_enter)


def timerPage():
    timerFrame = tk.Frame(displayFrame)
    topLabel = tk.Label(timerFrame, text='Timer', font=('Bold', 30), bg="#0B6E4F", fg="#00f678")
    topLabel.pack()

    #time
    def time():
        time_string = strftime('%H:%M:%S %p') #time
        l1.config(text=time_string)
        l1.after(1000,time) # time delay of 1000 milliseconds 

    l1 = tk.Label(displayFrame, font="Bold, 20", bg='#0B6E4F', fg='#00f678')
    l1.place(x=10, y=653)
    time()

    #day
    def day():
        time_string = strftime('%A') #day
        l2.config(text=time_string)

    l2 = tk.Label(displayFrame, font="Bold, 20", bg='#0B6E4F', fg='#00f678')
    l2.place(x=30, y=691)
    day()
    
    #date
    def date():
        time_string = strftime('%x') #date
        l3.config(text=time_string)

    l3 = tk.Label(displayFrame, font="Bold, 20", bg='#0B6E4F', fg='#00f678')
    l3.place(x=33, y=729)
    date()

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
                