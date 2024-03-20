# Import necessary modules
from pack import *
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from random import shuffle
from sfx import *

# Create root window (Manager Window)
root = Tk()

root.title("Powerball Roller")
root.geometry('1280x480')  # Set geometry (widthxheight)
root.configure(bg="hot pink")  # Set background color
root.resizable(False, False)

# Import background
bg = PhotoImage(file = "assets/powerballRollerBg.png")

# Create canvas for background (highlightthickness removes white border around window)
root = Canvas(root, height = 480, width = 1280, highlightthickness=0)
root.pack(fill = "both", expand = True)

# Display background
root.create_image(0, 0, image = bg, anchor = "nw")


inputtxt = Text(root, height = 1, width = 7, relief = "sunken")
inputtxt.pack()

score = Label(root, text = "", font = ("Comic Sans MS", 128))
counter = 0

originalScore = 0

def Powerball(): 
    inp = inputtxt.get(1.0, "end-1c")
    inp = list(inp)
    shuffle(inp)
    inp = ''.join(inp)
    score.config(text = inp, bg= "white")
    score.place(relx=.5, rely=.5, anchor="c")

def display():
    t = inputtxt.get(1.0, "end-1c")
    score.config(text = t, bg= "white")
    score.place(relx=.5, rely=.5, anchor="c")
    loop()

def loop():
    global counter
    global originalScore
    if counter == 0:
        originalScore = int(inputtxt.get(1.0, "end-1c"))
        randomizeSound()
        root.after(1596)
    counter += 1
    Powerball()
    if counter > 383:
        counter = 0
        if(int(score.cget('text')) > originalScore):
            winningSound()
        else:
            losingSound()
        return
    # once 'loop()' is called from root, it will get called again here
    root.after(10, loop)


printButton = Button(root, text = "POWERBALL!",  command = display) 
printButton.pack()

# Run the GUI
root.mainloop()