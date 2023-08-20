from tkinter import *
import random

def trun_next(row, col):
    global player
    if game_buttons[row][col]['text'] == "" and winner_checker() == False:
        if player == players[0]:
            game_buttons[row][col]['text'] = player

            if winner_checker() == False:
                player = players[1]
                label.config(text=(players[1] + " " + "turn"))
            elif winner_checker() == True:
                label.config(text=(players[0] + " " + "Win!"))
            elif winner_checker() == 'tie':
                label.config(text=("Tie!, No winner"))
        elif player == players[1]:
            game_buttons[row][col]['text'] = player

            if winner_checker() == False:
                player = players[0]
                label.config(text=(players[0] + " " + "turn"))
            elif winner_checker() == True:
                label.config(text=(players[1] + " " + "Win!"))
            elif winner_checker() == 'tie':
                label.config(text=("Tie!, No winner"))
            

def winner_checker():
    for row in range(3):
            if game_buttons[row][0]["text"] == game_buttons[row][1]["text"] == game_buttons[row][2]["text"] != "":
                game_buttons[row][0].config(bg="blue")
                game_buttons[row][1].config(bg="blue")
                game_buttons[row][2].config(bg="blue")
                return True
            
    for col in range(3):
            if game_buttons[0][col]["text"] == game_buttons[1][col]["text"] == game_buttons[2][col]["text"] != "":
                game_buttons[0][col].config(bg="blue")
                game_buttons[1][col].config(bg="blue")
                game_buttons[2][col].config(bg="blue")
                return True
            

    if game_buttons[0][0]["text"] == game_buttons[1][1]["text"] == game_buttons[2][2]["text"] != "":
        game_buttons[0][0].config(bg="blue")
        game_buttons[1][1].config(bg="blue")
        game_buttons[2][2].config(bg="blue")
        return True
    

    elif game_buttons[0][2]["text"] == game_buttons[1][1]["text"] == game_buttons[2][0]["text"] != "":
        game_buttons[0][2].config(bg="blue")
        game_buttons[1][1].config(bg="blue")
        game_buttons[2][0].config(bg="blue")
        return True
    
    if empty_space_checker() == False:
        for row in range(3):
            for col in range(3):
                game_buttons[row][col].config(bg='red')


        return 'tie'
    else:
        return False

def empty_space_checker():
    spaces = 9
    for row in range(3):
        for col in range(3):
            if game_buttons[row][col]['text'] != "":
                spaces -= 1
    
    if spaces == 0:
        return False
    else:
        return True


def new_game_start():
    global player
    player = random.choice(players)

    label.config(text=(player + " turn"))

    for row in range(3):
        for col in range(3):
            game_buttons[row][col].config(text="", bg="#F0F0F0")

window = Tk()
window.title(" Tic Tac Toe X O Game")

players = ["x", "o"]
player  = random.choice(players)

game_buttons = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]

label = Label(text=(player +" " + "trun"), font=('Calibri)',40))
label.pack(side="top")

button_restart = Button(text="restart",font=('Calibri)',30), command= new_game_start)
button_restart.pack(side="top")


frame_btns = Frame(window)
frame_btns.pack()

for row in range(3):
    for col in range(3):
        game_buttons[row][col] = Button(frame_btns, text= "", font=('Calibri)',55),width=4, height=1,command=lambda row=row , col=col: trun_next(row,col))
        game_buttons[row][col].grid(row=row, column=col)

window.mainloop()