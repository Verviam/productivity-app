
print("What habits do you want to work on? \n Habits List: []")

habits = []
    
def addHabit():
    toAdd = input("Add Habits: ")
    habits.append((toAdd))
    
    for habit in habits:
        
        # add each habit in habits.txt
    # open("habits.txt", "a")
addHabit()

# open file in write mode
with open("habits.txt", "a") as x:
    for habit in habits:
        # write each item on a new line
        x.write("%s\n" % habits)
    print('Done')