from tkinter import *
from PIL import Image,ImageTk
from ctypes import windll, byref, sizeof, c_int
import customtkinter as ctk

root = Tk(className='Productivity') #create window and name
root.geometry("1080x720") # set window size
root.configure(bg='white') # set window color

#custom title bar functions
def start_drag(e):
        e.widget.offset = (e.x, e.y) # save the offset from the top-left corner of window
def move_app(e):
        root.geometry(f'+{e.x_root-e.widget.offset[0]}+{e.y_root-e.widget.offset[1]}') # calculate top-left corner of window based on the saved offset7
def quitter(e):
        root.quit()
        #root.destroy()
def hide_screen(e):
        root.overrideredirect(0)
        root.iconify

# custom title bar characteristics
root.overrideredirect(True)
title_bar = Frame(root, bg="#073B3A", relief="raised", bd=1)
title_bar.pack(expand=1, fill=X)
title_bar.place(x=-1, y=-1)
title_bar.bind("<Button-1>", start_drag)
title_bar.bind("<B1-Motion>", move_app)

# custom title bar label
title_label = Label(title_bar, text="Productivity", bg="#073B3A", fg="#21D375", font="Ebrima")
title_label.pack(side=LEFT, pady=4, padx=468.5) #

# adds icon to top left
Image_icon = PhotoImage(file = "productivity_icon.png")
root.iconphoto(False, Image_icon)

#close button
close_button = Label(title_bar, text=" X ", bg="#073B3A", fg="#21D375", font="Ebrima")
close_button.pack(side=RIGHT, pady=4)
close_button.bind("<Button-1>", quitter)

#minimize button
minimize_button = Label(title_bar, text=" _ ", bg="#073B3A", fg="#21D375", font="Ebrima")
minimize_button.pack(side=RIGHT, pady=4)
minimize_button.bind("<Button-1>", hide_screen)


# HWND = windll.user32.GetParent(root.winfo_id())
# title_bar_color = 0x00FF0000
# title_text_color = 0x0000FF99

# windll.dwmapi.DwmSetWindowAttribute(
#     HWND,
#     35,
#     byref(c_int(title_bar_color)),
#     sizeof(c_int))

# windll.dwmapi.DwmSetWindowAttribute(
#     HWND,
#     36,
#     byref(c_int(title_text_color)),
#     sizeof(c_int))

Label(root, text="To Do List", bg="white", font=("Comic Sans MS", 15), wraplength=300).place(x=50, y=30.5
                                                                                             ) #Edit font size and wrap length and place later

tasks = Listbox(root, selectbackground='Gold', bg='Silver', font=('Helvetica', 12), height=12, width=25)
scroller = Scrollbar(root, orient=VERTICAL, command=tasks.yview)
scroller.place(x=260, y=80, height=232)

tasks.config(yscrollcommand=scroller.set)
tasks.place(x=35, y=80)

#taskbar
taskbar_border_color = Frame(root, background="black")
taskbar = Listbox(root, selectbackground='black', bg='azure3', font=('Helvetica', 12), height=50, width=5)
taskbar.place(x=0, y=30.5, height=800)

#home
homeImg = ImageTk.PhotoImage(Image.open("home.png"))
home = Label(root, image=homeImg, bg="white")
home.pack(side='top',pady=100)

root.mainloop()


# Frame(height = 20,width = 640,bg = 'grey').pack()

# clickMe = Button(root, text="Click here for Monkey").pack() # creates button

# canvas = Canvas(root).pack()
# scrollbar = Scrollbar(root)
# scrollbar.pack(side=RIGHT, fill= Y)



# window = tk.Tk()



# label = tk.Label(text="Muscle Gao", font = "10")
# label.pack()

# frame1 = tk.Frame()
# frame1.pack()

# window.mainloop()

# scroller = Scrollbar(root, orient=VERTICAL, command=tasks.yview)
# scroller.place(x=260, y=50, height=232)

# tasks.config(yscrollcommand=scroller.set)

# tasks.place(x=35, y=50)

# # Adding items to the Listbox
# with open('tasks.txt', 'r+') as tasks_list:
#     for task in tasks_list:
#         tasks.insert(END, task)
#     tasks_list.close()

# # Creating the Entry widget where the user can enter a new item
# new_item_entry = Entry(root, width=37)
# new_item_entry.place(x=35, y=310)

# # Creating the Buttons
# add_btn = Button(root, text='Add Item', bg='Azure', width=10, font=('Helvetica', 12),
#                  command=lambda: add_item(new_item_entry, tasks))
# add_btn.place(x=45, y=350)

# delete_btn = Button(root, text='Delete Item', bg='Azure', width=10, font=('Helvetica', 12),
#                  command=lambda: delete_item(tasks))
# delete_btn.place(x=150, y=350)

