import tkinter as tk
from tkinter import ttk 
from tkinter import messagebox
from PIL import Image, ImageTk
import datetime as dt
from time import strftime
from tkcalendar import DateEntry

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
    topLabel = tk.Label(scheduleFrame, text='Schedule', font=('Bold', 30), bg="#0B6E4F", fg="#00f678")
    topLabel.pack()

    Pm = "pm"
    numsPm = ['11', '10', '9', '8', '7', '6', '5', '4', '3', '2', '1', '12']
    timeLabelsPm=[] 
    for numPm in numsPm: #iterates over your nums
        timePm = numPm + Pm
        pmLabel = tk.Label(scheduleFrame,text=timePm, bg='#0B6E4F', font=('Bold', 12)) #set your text
        pmLabel.pack()
        timeLabelsPm.append(pmLabel) #appends the label to the list for further use
    
    Am = "am"
    numsAm = ['11', '10', '9', '8', '7', '6', '5', '4', '3', '2', '1', '12']
    timeLabelsAm=[] 
    for numAm in numsAm: #iterates over your nums
        timeAm = numAm + Am
        amLabel = tk.Label(scheduleFrame,text=timeAm, bg='#0B6E4F', font=('Bold', 12)) #set your text
        amLabel.pack()
        timeLabelsAm.append(amLabel) #appends the label to the list for further use
    
    for label in range (0, len(timeLabelsAm)):
        timeLabelsAm[label].pack(anchor = "sw", side=tk.BOTTOM)

    for label in range (0, len(timeLabelsPm)):
        timeLabelsPm[label].pack(anchor = "sw", side=tk.BOTTOM)
     
    # separate labels with outlines 

    # Select Day Calendar
    cal = DateEntry(scheduleFrame, width=12, background='#0B6E4F', foreground='black', borderwidth=2, )
    cal.pack(side=tk.TOP)
    

    def dateSelect():
        selected_date = cal.get_date()
        print(f"Selected date: {selected_date}")
        # You can implement functionality to add events to the selected date here

    # Add an event-to-schedule button
    add_event_button = ttk.Button(scheduleFrame, text="Add Event", command=dateSelect)
    add_event_button.pack()

    # make add event button visible over frame 

    def buttonFunc():
        print(entry.get())
        label.config(text="some other text")
    entry = ttk.Entry(master=root)
    entry.pack()


    # entrybox input task
    # entrybox input time and date
    # place label on schedule based on entrybox inputs
    # make it able to be called back to home page
    # have every day's schedule be displayed here

    scheduleFrame.pack(pady=20)

    # To Do: 
    # make times on left of screen
    # add scrollbar to time selection
    # create an add event button that allows user input for event name and adds to specific time with specific day
    # drag and drop feature

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

                