# Import necessary modules
from pack import *
from tkinter import *
from PIL import Image, ImageTk

# Create root window
root = Tk()

# Set root window title and dimensions
root.title("Pack Roller")
root.geometry('1280x720')  # Set geometry (widthxheight)
root.configure(bg="hot pink")  # Set background color
root.resizable(False, False) # keeps sizing correct

# Loads the card image for the input cardName
# Parameters:
#   cardName (str): The name of the card image file
#   sheen (int): The sheen of the card (-1 - misc, 0 - basic, 1 - holo, 2 - poly)
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
    image = image.resize((200, 277))
    image = ImageTk.PhotoImage(image)
    return image


# Create labels for card images
lbl = Label(root, text="", font=('Comic Sans MS', 12))
lbl.place(x=50, y=500)

blank = LoadCardImage("blank.png", -1)

card1 = Label(image = blank)
card2 = Label(image = blank)
card3 = Label(image = blank)
card4 = Label(image = blank)
card5 = Label(image = blank)

card1.image = blank
card2.image = blank
card3.image = blank
card4.image = blank
card5.image = blank

card1.place(x=120, y=100)
card2.place(x=330, y=100)
card3.place(x=540, y=100)
card4.place(x=750, y=100)
card5.place(x=960, y=100)

# Rolls a Mini Pack and displays the result
def Mini(wins):
    x = rollMiniPack(wins)
    y = "Number of times you have rolled Mini Pack: Too Many"
    lbl.configure(text=y)

    one = LoadCardImage("blank.png", -1)
    two = LoadCardImage(x[0][0], x[0][2])
    three = LoadCardImage(x[1][0], x[1][2])
    four = LoadCardImage(x[2][0], x[2][2])
    five = LoadCardImage("blank.png", -1)

    card1 = Label(image=one)
    card1.image = one

    card2 = Label(image=two)
    card2.image = two

    card3 = Label(image=three)
    card3.image = three

    card4 = Label(image=four)
    card4.image = four

    card5 = Label(image=five)
    card5.image = five

    card1.place(x=120, y=100)
    card2.place(x=330, y=100)
    card3.place(x=540, y=100)
    card4.place(x=750, y=100)
    card5.place(x=960, y=100)

# Rolls a Jumbo Pack and displays the result
def Jumbo(wins):
    x = rollJumboPack(wins)
    y = "Number of times you have rolled Jumbo Pack: Too Many"
    
    one = LoadCardImage(x[0][0], x[0][2])
    two = LoadCardImage(x[1][0], x[1][2])
    three = LoadCardImage(x[2][0], x[2][2])
    four = LoadCardImage(x[3][0], x[3][2])
    five = LoadCardImage(x[4][0], x[4][2])

    lbl.configure(text=y)
    
    card1 = Label(image=one)
    card1.image = one
    
    card2 = Label(image=two)
    card2.image = two

    card3 = Label(image=three)
    card3.image = three

    card4 = Label(image=four)
    card4.image = four

    card5 = Label(image=five)
    card5.image = five

    card1.place(x=120, y=100)
    card2.place(x=330, y=100)
    card3.place(x=540, y=100)
    card4.place(x=750, y=100)
    card5.place(x=960, y=100)

# Rolls a Mega Pack and displays the result
def Mega():
    x = rollMegaPack()
    y = "Number of times you have rolled Mega Pack: Too Many"

    one = LoadCardImage(x[0][0], x[0][2])
    two = LoadCardImage(x[1][0], x[1][2])
    three = LoadCardImage(x[2][0], x[2][2])
    four = LoadCardImage(x[3][0], x[3][2])
    five = LoadCardImage(x[4][0], x[4][2])

    lbl.configure(text=y)
    
    card1 = Label(image=one)
    card1.image = one
    
    card2 = Label(image=two)
    card2.image = two

    card3 = Label(image=three)
    card3.image = three

    card4 = Label(image=four)
    card4.image = four

    card5 = Label(image=five)
    card5.image = five

    card1.place(x=120, y=100)
    card2.place(x=330, y=100)
    card3.place(x=540, y=100)
    card4.place(x=750, y=100)
    card5.place(x=960, y=100)


# Rolls a Mini Pack and displays the result
def Single():
    x = rollJumboPack(0)
    y = "Number of times you have rolled Mini Pack: Too Many"
    lbl.configure(text=y)

    one = LoadCardImage("blank.png", -1)
    two = LoadCardImage("blank.png", -1)
    three = LoadCardImage(x[0][0], x[0][2])
    four = LoadCardImage("blank.png", -1)
    five = LoadCardImage("blank.png", -1)

    card1 = Label(image=one)
    card1.image = one

    card2 = Label(image=two)
    card2.image = two

    card3 = Label(image=three)
    card3.image = three

    card4 = Label(image=four)
    card4.image = four

    card5 = Label(image=five)
    card5.image = five

    card1.place(x=120, y=100)
    card2.place(x=330, y=100)
    card3.place(x=540, y=100)
    card4.place(x=750, y=100)
    card5.place(x=960, y=100)


# Create buttons for each pack type
btn1 = Button(root, text="Mini Pack", fg="green", command=lambda: Mini(0), height=2, width=25)
btn2 = Button(root, text="Jumbo Pack", fg="blue", command=lambda: Jumbo(0), height=2, width=25)
btn3 = Button(root, text="Mega Pack", fg="red", command=Mega, height=2, width=25)
btn1A = Button(root, text="Mini Pack (1 Win)", fg="green", command=lambda: Mini(1), height=2, width=25)
btn2A = Button(root, text="Jumbo Pack (1 Win)", fg="blue", command=lambda: Jumbo(1), height=2, width=25)
btn1B = Button(root, text="Mini Pack (2 Wins)", fg="green", command=lambda: Mini(2), height=2, width=25)
btn2B = Button(root, text="Jumbo Pack (2 Wins)", fg="blue", command=lambda: Jumbo(2), height=2, width=25)
btn4 = Button(root, text="Single Card", fg="black", command=Single, height=2, width=25)

# Arranges Buttons at the bottom of the window
btn1.place(x=50, y=550)
btn2.place(x=250, y=550)
btn3.place(x=450, y=550)
btn1A.place(x=50, y=600)
btn2A.place(x=250, y=600)
btn4.place(x=450, y=600)
btn1B.place(x=50, y=650)
btn2B.place(x=250, y=650)

# Display credits
creditLabel = Label(root, text="Created By: Paka, WontonSauce, idiot stick, Soulice", font=('Comic Sans MS', 12))
creditLabel.place(x=880, y=690)

# Run the GUI
root.mainloop()

# EXE STUFF (commented out for testing)
# input("Continue...")