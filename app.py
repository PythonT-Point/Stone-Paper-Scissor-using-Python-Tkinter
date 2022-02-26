
# Import Required Library
from tkinter import *
import random as rand
 
# Create Object
wd = Tk()
 
# Set geometry
wd.geometry("500x300")
 
# Set title
wd.title("Pythontpoint")
 
# Computer Value
computervalue = {
    "0":"Stone",
    "1":"Paper",
    "2":"Scissor"
}
 
# Reset The Game
def reset_game():
    button1["state"] = "active"
    button2["state"] = "active"
    button3["state"] = "active"
    label1.config(text = "Player              ")
    label3.config(text = "Computer")
    label4.config(text = "")
 
# Disable the Button
def button_disable():
    button1["state"] = "disable"
    button2["state"] = "disable"
    button3["state"] = "disable"
 
# If player selected Stone
def isStone():
    cv = computervalue[str(rand.randint(0,2))]
    if cv == "Stone":
        matchresult = "Match Draw"
    elif cv=="Scissor":
        matchresult = "Player Win"
    else:
        matchresult = "Computer Win"
    label4.config(text = matchresult)
    label1.config(text = "Stone            ")
    label3.config(text = cv)
    button_disable()
 
# If player selected paper
def ispaper():
    cv = computervalue[str(rand.randint(0, 2))]
    if cv == "Paper":
        matchresult = "Match Draw"
    elif cv=="Scissor":
        matchresult = "Computer Win"
    else:
        matchresult = "Player Win"
    label4.config(text = matchresult)
    label1.config(text = "Paper           ")
    label3.config(text = cv)
    button_disable()
 
# If player selected scissor
def isscissor():
    cv = computervalue[str(rand.randint(0,2))]
    if cv == "Stone":
        matchresult = "Computer Win"
    elif cv == "Scissor":
        matchresult = "Match Draw"
    else:
        matchresult = "Player Win"
    label4.config(text = matchresult)
    label1.config(text = "Scissor         ")
    label3.config(text = cv)
    button_disable()
 
# Add Labels, Frames and Button
Label(wd,
      text = "Stone Paper Scissor",
      font = "normal 22 bold",
      fg = "blue").pack(pady = 20)
 
frame = Frame(wd)
frame.pack()
 
label1 = Label(frame,
           text = "Player              ",
           font = 12)
 
label2 = Label(frame,
           text = "VS             ",
           font = "normal 12 bold")
 
label3 = Label(frame, text = "Computer", font = 12)
 
label1.pack(side = LEFT)
label2.pack(side = LEFT)
label3.pack()
 
label4 = Label(wd,
           text = "",
           font = "normal 25 bold",
           bg = "white",
           width = 15 ,
           borderwidth = 2,
           relief = "solid")
label4.pack(pady = 20)
 
frame1 = Frame(wd)
frame1.pack()
 
button1 = Button(frame1, text = "Stone",
            font = 10, width = 7,
            command = isStone)
 
button2 = Button(frame1, text = "Paper ",
            font = 10, width = 7,
            command = ispaper)
 
button3 = Button(frame1, text = "Scissor",
            font = 10, width = 7,
            command = isscissor)
 
button1.pack(side = LEFT, padx = 10)
button2.pack(side = LEFT,padx = 10)
button3.pack(padx = 10)
 
Button(wd, text = "Reset Game",
       font = 10, fg = "red",
       bg = "black", command = reset_game).pack(pady = 20)
 
# Execute Tkinter
wd.mainloop()