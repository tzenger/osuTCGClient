# Import necessary modules
from pack import *
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

# Create root window (Manager Window)
root = Tk()

# Set root window title and dimensions
root.title("Card Manager")
root.geometry('600x150')  # Set geometry (widthxheight)
root.configure(bg="pink")  # Set background color
root.resizable(False, False)

# Create card display
display = Toplevel(height = 480, width = 1280)
display.title("Card Display")
display.resizable(False, False)

# Import background
bg = PhotoImage(file = "assets/cardDisplayBg.png")

# Create canvas for background (highlightthickness removes white border around window)
displayCanvas = Canvas(display, height = 480, width = 1280, highlightthickness=0)
displayCanvas.pack(fill = "both", expand = True)

# Display background
displayCanvas.create_image(0, 0, image = bg, anchor = "nw")

# Loads the card image for the input cardName
# Parameters:
#   cardName (str): The name of the card image file
# Returns:
#   ImageTk.PhotoImage: The loaded card image
def LoadCardImage(cardName, sheen):
    rarity = ""
    if(sheen == 0):
        rarity = "b"
    elif(sheen == 1):
        rarity = "h"
    elif(sheen == 2):
        rarity = "p"
    image = str("cards/" + rarity + cardName)
    image = Image.open(image)
    image = image.resize((150, 208))
    image = ImageTk.PhotoImage(image)
    return image
    
# --- COUNTERS ---

# Counters on the display
counterA1 = Label(display, width = 2, height = 1, font=('Comic Sans MS', 10), padx=0, pady=0)
counterA2 = Label(display, width = 2, height = 1, font=('Comic Sans MS', 10), padx=0, pady=0)
counterA3 = Label(display, width = 2, height = 1, font=('Comic Sans MS', 10), padx=0, pady=0)
counterA4 = Label(display, width = 2, height = 1, font=('Comic Sans MS', 10), padx=0, pady=0)
counterA5 = Label(display, width = 2, height = 1, font=('Comic Sans MS', 10), padx=0, pady=0)

counterB1 = Label(display, width = 2, height = 1, font=('Comic Sans MS', 10), padx=0, pady=0)
counterB2 = Label(display, width = 2, height = 1, font=('Comic Sans MS', 10), padx=0, pady=0)
counterB3 = Label(display, width = 2, height = 1, font=('Comic Sans MS', 10), padx=0, pady=0)
counterB4 = Label(display, width = 2, height = 1, font=('Comic Sans MS', 10), padx=0, pady=0)
counterB5 = Label(display, width = 2, height = 1, font=('Comic Sans MS', 10), padx=0, pady=0)

#Spinboxes for counting
def spinbox_callback(opponent, cardNumber, value):
    match opponent:
        case 0:
            match cardNumber:
                case 0:
                    counterA1.configure(text=value)
                    counterA1.place(x=30, y=220)
                case 1:
                    counterA2.configure(text=value)
                    counterA2.place(x=210, y=220)
                case 2:
                    counterA3.configure(text=value)
                    counterA3.place(x=390, y=220)
                case 3:
                    counterA4.configure(text=value)
                    counterA4.place(x=120, y=240)
                case 4:
                    counterA5.configure(text=value)
                    counterA5.place(x=300, y=240)
        case 1:
            match cardNumber:
                case 0:
                    counterB1.configure(text=value)
                    counterB1.place(x=740, y=220)
                case 1:
                    counterB2.configure(text=value)
                    counterB2.place(x=920, y=220)
                case 2:
                    counterB3.configure(text=value)
                    counterB3.place(x=1100, y=220)
                case 3:
                    counterB4.configure(text=value)
                    counterB4.place(x=830, y=240)
                case 4:
                    counterB5.configure(text=value)
                    counterB5.place(x=1010, y=240)
    return

# Count text boxes for spinboxes
countA1 = IntVar()
countA2 = IntVar()
countA3 = IntVar()
countA4 = IntVar()
countA5 = IntVar()

countB1 = IntVar()
countB2 = IntVar()
countB3 = IntVar()
countB4 = IntVar()
countB5 = IntVar()

# spinboxes
spA1 = Spinbox(root, from_= 0, to = 20, width = 3, wrap = True)
spA1.configure(command= lambda : spinbox_callback(0, 0, spA1.get()))
spA1.place(x=250, y=30)

spA2 = Spinbox(root, from_= 0, to = 20, width = 3, wrap = True)
spA2.configure(command= lambda : spinbox_callback(0, 1, spA2.get()))
spA2.place(x=250, y=50)

spA3 = Spinbox(root, from_= 0, to = 20, width = 3, wrap = True)
spA3.configure(command= lambda : spinbox_callback(0, 2, spA3.get()))
spA3.place(x=250, y=70)

spA4 = Spinbox(root, from_= 0, to = 20, width = 3, wrap = True)
spA4.configure(command= lambda : spinbox_callback(0, 3, spA4.get()))
spA4.place(x=250, y=90)

spA5 = Spinbox(root, from_= 0, to = 20, width = 3, wrap = True)
spA5.configure(command= lambda : spinbox_callback(0, 4, spA5.get()))
spA5.place(x=250, y=110)

spB1 = Spinbox(root, from_= 0, to = 20, width = 3, wrap = True)
spB1.configure(command= lambda : spinbox_callback(1, 0, spB1.get()))
spB1.place(x=540, y=30)

spB2 = Spinbox(root, from_= 0, to = 20, width = 3, wrap = True)
spB2.configure(command= lambda : spinbox_callback(1, 1, spB2.get()))
spB2.place(x=540, y=50)

spB3 = Spinbox(root, from_= 0, to = 20, width = 3, wrap = True)
spB3.configure(command= lambda : spinbox_callback(1, 2, spB3.get()))
spB3.place(x=540, y=70)

spB4 = Spinbox(root, from_= 0, to = 20, width = 3, wrap = True)
spB4.configure(command= lambda : spinbox_callback(1, 3, spB4.get()))
spB4.place(x=540, y=90)

spB5 = Spinbox(root, from_= 0, to = 20, width = 3, wrap = True)
spB5.configure(command= lambda : spinbox_callback(1, 4, spB5.get()))
spB5.place(x=540, y=110)

# --- END OF COUNTERS ---


blankB = LoadCardImage("blankBlue.png", -1)
blankR = LoadCardImage("blankRed.png", -1)


cardA1 = Label(display, image = blankB)
cardA2 = Label(display, image = blankB)
cardA3 = Label(display, image = blankB)
cardA4 = Label(display, image = blankB)
cardA5 = Label(display, image = blankB)

cardB1 = Label(display, image = blankR)
cardB2 = Label(display, image = blankR)
cardB3 = Label(display, image = blankR)
cardB4 = Label(display, image = blankR)
cardB5 = Label(display, image = blankR)

cardA1.image = blankB
cardA2.image = blankB
cardA3.image = blankB
cardA4.image = blankB
cardA5.image = blankB

cardB1.image = blankR
cardB2.image = blankR
cardB3.image = blankR
cardB4.image = blankR
cardB5.image = blankR

cardA1.place(x=30, y=10)
cardA2.place(x=210, y=10)
cardA3.place(x=390, y=10)
cardA4.place(x=120, y=260)
cardA5.place(x=300, y=260)

cardB1.place(x=740, y=10)
cardB2.place(x=920, y=10)
cardB3.place(x=1100, y=10)
cardB4.place(x=830, y=260)
cardB5.place(x=1010, y=260)



# Opponent Lables
lblA1 = Label(root, text = "Opponent 1", font = ("Comic Sans", 10))
lblA1.place(x = 10, y = 10)

lblA2 = Label(root, text = "Opponent 2", font = ("Comic Sans", 10))
lblA2.place(x = 300, y = 10)

# Dropdown Menus
cards = ["(empty)"] + list(common) + list(uncommon) + list(rare)
cards.sort()

patterns = ["Basic", "Holographic", "Polychrome"]


# --- Dropdown for Opponent A Boxes and Holos ---
nA1 = StringVar()
dropA1 = ttk.Combobox(root, width = 20, textvariable = nA1, state = "readonly")
dropA1['values'] = cards
dropA1.grid(row = 20)
dropA1.current(0)
dropA1.place(x=10, y=30)

nhlA1 = StringVar()
dropPatternA1 = ttk.Combobox(root, width = 10, textvariable = nhlA1, state = "readonly")
dropPatternA1['values'] = patterns
dropPatternA1.grid(row = 20)
dropPatternA1.current(0)
dropPatternA1.place(x=160, y=30)


nA2 = StringVar()
dropA2 = ttk.Combobox(root, width = 20, textvariable = nA2, state = "readonly")
dropA2['values'] = cards
dropA2.grid(row = 20)
dropA2.current(0)
dropA2.place(x=10, y=50)

nhlA2 = StringVar()
dropPatternA2 = ttk.Combobox(root, width = 10, textvariable = nhlA2, state = "readonly")
dropPatternA2['values'] = patterns
dropPatternA2.grid(row = 20)
dropPatternA2.current(0)
dropPatternA2.place(x=160, y=50)


nA3 = StringVar()
dropA3 = ttk.Combobox(root, width = 20, textvariable = nA3, state = "readonly")
dropA3['values'] = cards
dropA3.grid(row = 20)
dropA3.current(0)
dropA3.place(x=10, y=70)

nhlA3 = StringVar()
dropPatternA3 = ttk.Combobox(root, width = 10, textvariable = nhlA3, state = "readonly")
dropPatternA3['values'] = patterns
dropPatternA3.grid(row = 20)
dropPatternA3.current(0)
dropPatternA3.place(x=160, y=70)


nA4 = StringVar()
dropA4 = ttk.Combobox(root, width = 20, textvariable = nA4, state = "readonly")
dropA4['values'] = cards
dropA4.grid(row = 20)
dropA4.current(0)
dropA4.place(x=10, y=90)

nhlA4 = StringVar()
dropPatternA4 = ttk.Combobox(root, width = 10, textvariable = nhlA4, state = "readonly")
dropPatternA4['values'] = patterns
dropPatternA4.grid(row = 20)
dropPatternA4.current(0)
dropPatternA4.place(x=160, y=90)


nA5 = StringVar()
dropA5 = ttk.Combobox(root, width = 20, textvariable = nA5, state = "readonly")
dropA5['values'] = cards
dropA5.grid(row = 20)
dropA5.current(0)
dropA5.place(x=10, y=110)

nhlA5 = StringVar()
dropPatternA5 = ttk.Combobox(root, width = 10, textvariable = nhlA5, state = "readonly")
dropPatternA5['values'] = patterns
dropPatternA5.grid(row = 20)
dropPatternA5.current(0)
dropPatternA5.place(x=160, y=110)


# --- Dropdown for Opponent B Boxes and Holos ---
nB1 = StringVar()
dropB1 = ttk.Combobox(root, width = 20, textvariable = nB1, state = "readonly")
dropB1['values'] = cards
dropB1.grid(row = 20)
dropB1.current(0)
dropB1.place(x=300, y=30)

nhlB1 = StringVar()
dropPatternB1 = ttk.Combobox(root, width = 10, textvariable = nhlB1, state = "readonly")
dropPatternB1['values'] = patterns
dropPatternB1.grid(row = 20)
dropPatternB1.current(0)
dropPatternB1.place(x=450, y=30)


nB2 = StringVar()
dropB2 = ttk.Combobox(root, width = 20, textvariable = nB2, state = "readonly")
dropB2['values'] = cards
dropB2.grid(row = 20)
dropB2.current(0)
dropB2.place(x=300, y=50)

nhlB2 = StringVar()
dropPatternB2 = ttk.Combobox(root, width = 10, textvariable = nhlB2, state = "readonly")
dropPatternB2['values'] = patterns
dropPatternB2.grid(row = 20)
dropPatternB2.current(0)
dropPatternB2.place(x=450, y=50)


nB3 = StringVar()
dropB3 = ttk.Combobox(root, width = 20, textvariable = nB3, state = "readonly")
dropB3['values'] = cards
dropB3.grid(row = 20)
dropB3.current(0)
dropB3.place(x=300, y=70)

nhlB3 = StringVar()
dropPatternB3 = ttk.Combobox(root, width = 10, textvariable = nhlB3, state = "readonly")
dropPatternB3['values'] = patterns
dropPatternB3.grid(row = 20)
dropPatternB3.current(0)
dropPatternB3.place(x=450, y=70)


nB4 = StringVar()
dropB4 = ttk.Combobox(root, width = 20, textvariable = nB4, state = "readonly")
dropB4['values'] = cards
dropB4.grid(row = 20)
dropB4.current(0)
dropB4.place(x=300, y=90)

nhlB4 = StringVar()
dropPatternB4 = ttk.Combobox(root, width = 10, textvariable = nhlB4, state = "readonly")
dropPatternB4['values'] = patterns
dropPatternB4.grid(row = 20)
dropPatternB4.current(0)
dropPatternB4.place(x=450, y=90)


nB5 = StringVar()
dropB5 = ttk.Combobox(root, width = 20, textvariable = nB5, state = "readonly")
dropB5['values'] = cards
dropB5.grid(row = 20)
dropB5.current(0)
dropB5.place(x=300, y=110)

nhlB5 = StringVar()
dropPatternB5 = ttk.Combobox(root, width = 10, textvariable = nhlB5, state = "readonly")
dropPatternB5['values'] = patterns
dropPatternB5.grid(row = 20)
dropPatternB5.current(0)
dropPatternB5.place(x=450, y=110)


lbl = Label(root, text="", font=('Comic Sans MS', 12))
lbl.place(x=50, y=500)

def cardPlace(event, opponent, cardNumber, cardPattern):
    match opponent:
        case 0:
            match cardNumber:
                case 0:
                    name = dropA1.get()
                case 1:
                    name = dropA2.get()
                case 2:
                    name = dropA3.get()
                case 3:
                    name = dropA4.get()
                case 4:
                    name = dropA5.get()
        case 1:
            match cardNumber:
                case 0:
                    name = dropB1.get()
                case 1:
                    name = dropB2.get()
                case 2:
                    name = dropB3.get()
                case 3:
                    name = dropB4.get()
                case 4:
                    name = dropB5.get()
                    
    if name == "(empty)":
        if opponent == 0:
            card = LoadCardImage("blankBlue.png", -1)
        else:
            card = LoadCardImage("blankRed.png", -1)
    else:
        # print(processCardPattern(cardPattern))
        card = LoadCardImage(name + ".png", processCardPattern(cardPattern))
    
    match opponent:
        case 0:
            match cardNumber:
                case 0:
                    cardA1 = Label(display, image=card)
                    cardA1.image = card
                    cardA1.place(x=30, y=10)
                case 1:
                    cardA2 = Label(display, image=card)
                    cardA2.image = card
                    cardA2.place(x=210, y=10)
                case 2:
                    cardA3 = Label(display, image=card)
                    cardA3.image = card
                    cardA3.place(x=390, y=10)
                case 3:
                    cardA4 = Label(display, image=card)
                    cardA4.image = card
                    cardA4.place(x=120, y=260)
                case 4:
                    cardA5 = Label(display, image=card)
                    cardA5.image = card
                    cardA5.place(x=300, y=260)
        case 1:
            match cardNumber:
                case 0:
                    cardB1 = Label(display, image=card)
                    cardB1.image = card
                    cardB1.place(x=740, y=10)
                case 1:
                    cardB2 = Label(display, image=card)
                    cardB2.image = card
                    cardB2.place(x=920, y=10)
                case 2:
                    cardB3 = Label(display, image=card)
                    cardB3.image = card
                    cardB3.place(x=1100, y=10)
                case 3:
                    cardB4 = Label(display, image=card)
                    cardB4.image = card
                    cardB4.place(x=830, y=260)
                case 4:
                    cardB5 = Label(display, image=card)
                    cardB5.image = card
                    cardB5.place(x=1010, y=260)
    # cardA1 = Label(display, image=card)
    # cardA1.image = card
    # cardA1.place(x=30, y=20)
    lbl.configure(text=name)
    lbl.place(x=50, y=500)

dropA1.bind('<<ComboboxSelected>>', lambda i : cardPlace(event = i, opponent=0, cardNumber=0, cardPattern=dropPatternA1.get()))
dropPatternA1.bind('<<ComboboxSelected>>', lambda i : cardPlace(event = i, opponent=0, cardNumber=0, cardPattern=dropPatternA1.get()))

dropA2.bind('<<ComboboxSelected>>', lambda i : cardPlace(event = i, opponent=0, cardNumber=1, cardPattern=dropPatternA2.get()))
dropPatternA2.bind('<<ComboboxSelected>>', lambda i : cardPlace(event = i, opponent=0, cardNumber=1, cardPattern=dropPatternA2.get()))

dropA3.bind('<<ComboboxSelected>>', lambda i : cardPlace(event = i, opponent=0, cardNumber=2, cardPattern=dropPatternA3.get()))
dropPatternA3.bind('<<ComboboxSelected>>', lambda i : cardPlace(event = i, opponent=0, cardNumber=2, cardPattern=dropPatternA3.get()))

dropA4.bind('<<ComboboxSelected>>', lambda i : cardPlace(event = i, opponent=0, cardNumber=3, cardPattern=dropPatternA4.get()))
dropPatternA4.bind('<<ComboboxSelected>>', lambda i : cardPlace(event = i, opponent=0, cardNumber=3, cardPattern=dropPatternA4.get()))

dropA5.bind('<<ComboboxSelected>>', lambda i : cardPlace(event = i, opponent=0, cardNumber=4, cardPattern=dropPatternA5.get()))
dropPatternA5.bind('<<ComboboxSelected>>', lambda i : cardPlace(event = i, opponent=0, cardNumber=4, cardPattern=dropPatternA5.get()))


dropB1.bind('<<ComboboxSelected>>', lambda i : cardPlace(event = i, opponent=1, cardNumber=0, cardPattern=dropPatternB1.get()))
dropPatternB1.bind('<<ComboboxSelected>>', lambda i : cardPlace(event = i, opponent=1, cardNumber=0, cardPattern=dropPatternB1.get()))

dropB2.bind('<<ComboboxSelected>>', lambda i : cardPlace(event = i, opponent=1, cardNumber=1, cardPattern=dropPatternB2.get()))
dropPatternB2.bind('<<ComboboxSelected>>', lambda i : cardPlace(event = i, opponent=1, cardNumber=1, cardPattern=dropPatternB2.get()))

dropB3.bind('<<ComboboxSelected>>', lambda i : cardPlace(event = i, opponent=1, cardNumber=2, cardPattern=dropPatternB3.get()))
dropPatternB3.bind('<<ComboboxSelected>>', lambda i : cardPlace(event = i, opponent=1, cardNumber=2, cardPattern=dropPatternB3.get()))

dropB4.bind('<<ComboboxSelected>>', lambda i : cardPlace(event = i, opponent=1, cardNumber=3, cardPattern=dropPatternB4.get()))
dropPatternB4.bind('<<ComboboxSelected>>', lambda i : cardPlace(event = i, opponent=1, cardNumber=3, cardPattern=dropPatternB4.get()))

dropB5.bind('<<ComboboxSelected>>', lambda i : cardPlace(event = i, opponent=1, cardNumber=4, cardPattern=dropPatternB5.get()))
dropPatternB5.bind('<<ComboboxSelected>>', lambda i : cardPlace(event = i, opponent=1, cardNumber=4, cardPattern=dropPatternB5.get()))


def processCardPattern(string):
    match string:
        case "Basic": return 0
        case "Holographic": return 1
        case "Polychrome": return 2



























# Display credits
creditLabel = Label(root, text="Created By: Paka, WontonSauce, idiot stick, Soulice", font=('Comic Sans MS', 12))
creditLabel.place(x=880, y=690)

# Run the GUI
root.mainloop()

# input("Continue...")