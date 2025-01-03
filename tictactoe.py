from tkinter import *
import random

def next_turn(row, column):
    global player
    
    # If the button is empty, make the move
    if buttons[row][column]['text'] == "":
        buttons[row][column]['text'] = player
        # Check if the current move resulted in a win
        if check_winner():
            label.config(text=player + " wins!")
            disable_buttons()
        elif empty_space():
            # Switch to the other player
            player = players[1] if player == players[0] else players[0]
            label.config(text=player + " turn")
        else:
            label.config(text="It's a draw!")
    else:
        return

def check_winner():
    # Check rows, columns, and diagonals
    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            return True

    for column in range(3):
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
            return True

    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        return True

    if buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        return True

    return False

def empty_space():
    for row in buttons:
        for button in row:
            if button['text'] == "":
                return True
    return False

def disable_buttons():
    for row in buttons:
        for button in row:
            button.config(state=DISABLED)

def new_game():
    global player
    player = random.choice(players)
    label.config(text=player + " turn")
    
    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="", state=NORMAL)

# Main window setup
window = Tk()
window.title("Tic-Tac-Toe")

players = ["x", "o"]
player = random.choice(players)
buttons = [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]]

label = Label(text=player + " turn", font=('consolas', 40))
label.pack(side="top")

reset_button = Button(text="Restart", font=('consolas', 20), command=new_game)
reset_button.pack(side="top")

frame = Frame(window)
frame.pack()

for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text="", font=('consolas', 40), width=5, height=2,
                                      command=lambda row=row, column=column: next_turn(row, column))
        buttons[row][column].grid(row=row, column=column)

window.mainloop()
