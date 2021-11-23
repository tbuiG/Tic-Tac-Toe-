from tkinter import *
import random

def next_turn(row,column):

    global player
    if squares[row][column]['text'] == "" and check_winner() is False:

        if player == players[0]:

            squares[row][column]['text'] = player

            if check_winner() is False:
                player = players[1]
                label.config(text=(players[1] + " turn"))

            elif check_winner() is True:
                label.config(text=players[0]+" Wins")

            elif check_winner() == "Tie":
                label.config(text="Tie!")

        else:
            squares[row][column]['text'] = player

            if check_winner() is False:
                player = players[0]
                label.config(text=(players[0] + " turn"))

            elif check_winner() is True:
                label.config(text=players[1] + " Wins")

            elif check_winner() == "Tie":
                label.config(text="Tie!")



def check_winner():
    #Check all rows
    for row in range(3):
        if squares[row][0]['text'] == squares[row][1]['text'] == squares[row][2]['text'] != "":
            return True
    #Check all columns
    for column in range(3):
        if squares[0][column]['text'] == squares[1][column]['text'] == squares[2][column]['text'] != "":
            return True

    #Check diagonals
    if squares[0][0]['text'] == squares[1][1]['text'] == squares[2][2]['text'] != "":
        return True

    elif squares[0][2]['text'] == squares[1][1]['text'] == squares[2][0]['text'] != "":
        return True

    elif empty_space() is False:
        return "Tie"

    else:
        return False


def empty_space():

    spaces = 9

    for row in range(3):
        for column in range(3):
            if squares[row][column]['text'] != "":
                spaces -= 1

        if spaces == 0:
            return False
        else:
            return True

def new_game():

    global player

    player = random.choice(players)
    label.config(text=player + " turn")

    for row in range(3):
        for column in range(3):
            squares[row][column].config(text="", bg="#F0F0F0")


window = Tk()
#Window with label
window.title("Tic Tac Toe Game")
#create players
players = ["X","O"]
player = random.choice(players)
#create squares
squares = [[0,0,0],
           [0,0,0],
           [0,0,0]]

#Create Label
label = Label(text = player + " turn", font=('consolas',40))
label.pack(side="top")
#Create reset button
reset_button = Button(text="Restart", font=('consolas',20), command = new_game)
reset_button.pack(side="top")

frame = Frame(window)
frame.pack()

for row in range(3):
    for column in range(3):
        squares[row][column] = Button(frame, text="", font=('consolas', 40), width=5, height=2,
                                      command= lambda row=row, column=column: next_turn(row,column))
        squares[row][column].grid(row=row,column=column)

window.mainloop()