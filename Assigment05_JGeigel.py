# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# JGeigel, 5.12.2023, Added code to complete assignment 5
# JGeigel, 5.15.2023, Added options to add more tasks and save data before exiting
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"   # An object that represents a file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strChoice = "" # A Capture the user option selection

# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
objFile = open(objFile, 'r')                #Open file object in read mode
for row in objFile:                         #Iterate through lines in the text file
    lstRow = row.split(",")                 #Create a list of "tasks" and "priorities" by splitting
                                            # each line at the comma separator.
    dicRow = {"Task": lstRow[0], "Priority": lstRow[1].strip()}     #Create a dictionary of tasks and priorities.
    lstTable.append(dicRow)                 #Append dictionary key-value pairs to a list (table).
objFile.close()                             #Close file object.

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""                               
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)

    strChoice = str(input("Which option would you like to perform? [1 to 5] - ")) #Obtain option selection from user
    print()  # adding a new line for looks

    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        print("Your current data is: \n")
        for row in lstTable:              #Iterate through list of tasks and priorities and print keys and values.
            print (row["Task"] + ' | ' + row["Priority"])
        input("\n" +"Press enter to continue.")
        continue

    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        while(True):
            print("Type in a task and assign a priority level: ")    #Obtain new task name and priority level from user.
            strTask = input("Task: ")
            strPriority = input("Priority: ")
            lstTable.append({"Task":strTask,"Priority":strPriority})    #Append new input to the list of tasks.
            for row in lstTable:
                print (row["Task"] + ' | ' + row["Priority"])           #Print current data in list of tasks and priorities.
            print()
            strChoice = input("Add more tasks? ('y/n'): ")           #Let the user choose to add more tasks if needed.
            if strChoice.lower()== 'y':
                continue
            elif strChoice.lower()=='n':
                break

    # Step 5 - Remove an item from the list/Table
    elif (strChoice.strip() == '3'):
        strTask = input("Task to Remove: ")         #Obtain from the user a task to remove.
        for row in lstTable:
            if row["Task"].lower()==strTask.lower():    #Iterate through list to find the task to be removed.
                lstTable.remove(row)
                print("Task removed.")
            else:
                print("Task not found.")
        continue

    # Step 6 - Save tasks to the ToDoList.txt file
    elif (strChoice.strip() == '4'):
        objFile =  open("ToDoList.txt","w")     #Open file object in write mode.
        for row in lstTable:                    #Iterate through list of tasks and priorities.
            objFile.write(str(row["Task"])+','+str(row["Priority"]+'\n'))   #Write tasks and priorities to file.
        objFile.close()                         #Close file object.
        print("Data added to file!")
        continue

    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        print("Would you like to save your data?")      #Prompt the user to choose between saving or not saving data.
        sav = input("Enter 'y' or 'n': ")   #User chooses to save or not to save the data
        if sav == "y":
            objFile = open("ToDoList.txt", "w")         #Open file object in write mode.
            for row in lstTable:                        #Iterate through list of tasks and priorities.
                objFile.write(str(row["Task"])+','+str(row["Priority"]+'\n')) #Write tasks and priorities to file.
            objFile.close()                             #Close file object.
            print("Data saved!")
            break
        elif sav == "n":                #Exit program if user chooses not to save data.
            break
        else:
            print("Please enter 'y' or 'n'")
            continue
        break  # and Exit the program
