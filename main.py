# Import the required libraries :
from tkinter import *
import random

yourScore = 0
computerScore = 0

# Computer Value
choices = ["Rock",
    "Paper",
    "Scissor"
]


def ComputerChoiceRandom():
    cv = random.choice(choices)
    return cv


def yourScoreCount():
    global yourScore
    yourScore = yourScore + 1
    return yourScore


def computerScoreCount():
    global computerScore
    computerScore = computerScore + 1
    return computerScore


def isRock():
    resultToDispaly.set("Your choice :Rock")
    ch = ComputerChoiceRandom()
    resultToDispaly.set(str(resultToDispaly.get())+"\n Computer's choice :" + str(ch))
    if ch == "Scissor":
        yourScoreCount()
    elif ch == "Paper":
        computerScoreCount()
    resultToDispaly.set(str(resultToDispaly.get()) + "\n Your Score : "+ str(yourScore))
    resultToDispaly.set(str(resultToDispaly.get()) + "\n Computer Score :"+ str(computerScore))



def isScissor():
    resultToDispaly.set("Your choice : Scissor")
    ch = ComputerChoiceRandom()
    resultToDispaly.set(str(resultToDispaly.get()) + "\n Computer's choice :" + str(ch))
    if ch == "Paper":
        yourScoreCount()
    elif ch == "Rock":
        computerScoreCount()
    resultToDispaly.set(str(resultToDispaly.get()) + "\n Your Score : " + str(yourScore))
    resultToDispaly.set(str(resultToDispaly.get()) + "\n Computer Score :" + str(computerScore))


def isPaper():
    resultToDispaly.set("Your choice :Paper")
    ch = ComputerChoiceRandom()
    resultToDispaly.set(str(resultToDispaly.get()) + "\n Computer's choice :" + str(ch))
    if ch == "Rock":
        yourScoreCount()
    elif ch == "Scissor":
        computerScoreCount()
    resultToDispaly.set(str(resultToDispaly.get()) + "\n Your Score : " + str(yourScore))
    resultToDispaly.set(str(resultToDispaly.get()) + "\n Computer Score :" + str(computerScore))


if __name__ == '__main__':
    root = Tk()
    root.title("Rock-Paper-Scissor")
    root.resizable(width=False, height=False)
    root.geometry("300x400")
    # Initialize the button variables :


    frame1 = Frame(root)
    frame1.pack()

    rockButton = Button(frame1, text="Rock", font=10, width=7, command=isRock, bg='#A1CAF1')
    paperButton = Button(frame1, text="Paper", font=10, width=7, command=isPaper, bg='#F4C2C2')
    scissorButton = Button(frame1, text="Scissor", font=10, width=7, command=isScissor, bg='#5FA777')

    resultToDispaly = StringVar()

    label = Label(root, textvariable=resultToDispaly, bg="yellow", width="100", height="10", font=10, justify='left')

    rockButton.pack()
    scissorButton.pack()
    paperButton.pack()
    label.pack()
    root.mainloop()
