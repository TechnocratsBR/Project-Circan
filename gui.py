from tkinter import *
from functions import *

def store_values():
    """" 
    This function stores the values inputed by the user to the variables.

    Argument:
            None

    Returns: 
           None

    """
    global day
    global sleep
    global wake
    global naps
    global steps
    global mood
    day = E1.get()
    sleep = E2.get()
    wake = E3.get()
    naps = E4.get()
    steps = E5.get()
    mood = E6.get()

    label = Label(top, text = "Data successfully updated!", font = 'heveltica 12', fg = "Red")
    label.place(x = 290, y = 440)

def update():
    """
    This function displays the elements to be entered for the sleep analysis data to the user when prompted."

    Argument:
            None
    
    Return:
        None

    """
    # calling the global variables
    global E1
    global E2
    global E3
    global E4
    global E5
    global E6

    # Crearting Labels and entry fields for the user to input data.
    L1 = Label(top, text = "Please input today's date (MM/DD/YYYY): ", font = "heveltica 12")
    L1.place(x = 10,y = 140)
    E1 = Entry(top, bd = 3, fg = "Blue", font = "Heveltica 12")
    E1.place(x = 320,y = 140)
    L2 = Label(top,text = "At what time did you exactly sleep? (MM/DD/YYYY HH:MM): ", font = "heveltica 12")
    L2.place(x = 10,y = 180)
    E2 = Entry(top, bd = 3,  fg = "Blue", font = "Heveltica 12")
    E2.place(x = 440,y = 180)
    L3 = Label(top,text = "What time did you wake up? (MM/DD/YYYY HH:MM): ", font = "heveltica 12")
    L3.place(x = 10,y = 220)
    E3 = Entry(top, bd = 3,  fg = "Blue", font = "Heveltica 12")
    E3.place(x = 390,y = 220)
    L4 = Label(top, text = "Did you take a nap? If so, how long? (Number of hours): ", font = "heveltica 12")
    L4.place(x = 10, y = 260)
    E4 = Entry(top, bd = 3, fg = "Blue", font = "Heveltica 12")
    E4.place(x = 420, y = 260)
    L5 = Label(top, text = "How many steps did you take today? ", font = "heveltica 12")
    L5.place(x = 10, y = 300)
    E5 = Entry(top, bd = 3, fg = "Blue", font = "Heveltica 12")
    E5.place(x = 280, y = 300)
    L6 = Label(top, text = "How was your mood? ", font = "heveltica 12")
    L6.place(x = 10, y = 340)
    E6 = Scale(top, from_=-5, to=5, orient = HORIZONTAL, fg = "Blue", width = 20)
    E6.pack()
    E6.place(x = 180, y = 320)
    # Creting submit button which saves the data in the form of variables
    B = Button(top, text = "Submit", command = store_values, fg = "Black", bg = "Light blue", font = "heveltica 11", width = 25, height = 2)
    B.place(x = 265, y = 375 )



def detailed_analysis():
    """
    This functions provides the detailed analysis of the person's data by opening it up in a new window.

    Argument:
            None
    
    Returns:
            None

    """
    # opening up a new window
    detail = Tk()

    # Providing the title to the window
    detail.title("Detailed Analysis")

    # Printing out the analysis
    analysis1 = Label(detail, text = "Average sleep on weekends: " + str(avgweekends), font = "Heveltica 12")
    analysis1.place(x = 10, y = 10)

    analysis2 = Label(detail, text = "Average sleep on weekdays: " + str(avgweekdays), font = "Heveltica 12")
    analysis2.place(x = 10, y = 40)  

    analysis3 = Label(detail, text = "Average mood on weekends: " + str(moodweekends), font = "Heveltica 12")
    analysis3.place(x = 10, y = 70)

    analysis4 = Label(detail, text = "Average mood on weekdays: " + str(moodweekdays), font = "Heveltica 12")
    analysis4.place(x = 10, y = 100)

    analysis5 = Label(detail, text = "Net Average Mood: " + str(avgmood), font = "Heveltica 12")
    analysis5.place(x = 10, y = 130)

    analysis5 = Label(detail, text = "Net average sleep: " + str(avgsleep), font = "Heveltica 12")
    analysis5.place(x = 10, y = 160)

    analysis6 = Label(detail, text = "Net Mood Deviation: " + str(devmood), font = "Heveltica 12")
    analysis6.place(x = 10, y = 190)

    analysis7 = Label(detail, text = "Net Sleep Deviation: " + str(devsleep), font = "Heveltica 12")
    analysis7.place(x = 10, y = 220) 

    if devsleep > (1.5) or avgsleep < (7.50):
        conclusion1 = Label(detail, text = "You do not have a healthy sleep schedule.", font = "Heveltica 12", fg = "Red")
        conclusion2 = Label(detail, text = "Focus on mantaining consistent number of hours of sleep!", font = "Heveltica 12", fg = "Red")
        conclusion1.place(x = 10, y = 250)
        conclusion2.place(x = 10, y = 280)
    elif devsleep < (1.5) or avgsleep > (7.50):
        conclusion1 = Label(detail, text = "Congratulations! You have a healthy sleep routine. Keep going!", font = "heveltica 12", fg = "Red")
        conclusion1.place(x = 10, y = 250)

    # Setting the size of the window
    detail.geometry("500x400+10+10")

    detail.mainloop()


#---------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------#
#                                           MAIN WINDOW                                             #
#---------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------#
top = Tk()
top.title("CIRCAN")

title = Label(top, text = "PROJECT CIRCAN", fg = "White", bg = "Blue", font = "Heveltica 18 bold")
title.pack()

description = Label(top, text = "This project analysis the sleep schedule. Start building your data today!", font = "Heveltica 12")
description.place(x = 10, y = 40)
    
Update_data = Button(top, text = "Update your Data", command = update, width = 30, height = 2, fg = "Black", bg = "Light Blue")
Update_data.place(x = 30, y = 80)
top.geometry("760x700+10+10")

Graph_button = Button(top, text = "Graph Analysis", command = plot, width = 30, height = 2, fg = "black", bg = "Light Blue")
Graph_button.place(x = 265, y = 80)

Details = Button(top, text = "Detailed Analysis", command = detailed_analysis, width = 30, height = 2, fg = "Black", bg = "Light Blue")
Details.place(x = 500, y = 80)

top.mainloop()
