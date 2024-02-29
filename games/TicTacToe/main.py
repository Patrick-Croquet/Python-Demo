import tkinter

def check_nul():
    print("Match nul")
def print_winner():
    global win

    if win is False:
        win = True
        print("Le joueur", current_player, "a gagné le jeu")

def switch_player():
    global current_player
    if current_player == 'X':
        current_player = 'O'
    else:
        current_player = 'X'
def check_win(clicked_row, clicked_col):
    # détecter la victoire horizontale
    count = 0
    for i in range(3):
        current_button = buttons[i][clicked_row]
        # current_button.config(text="CHECK")
        if current_button['text'] == current_player:
            count += 1
    if count == 3:
        #print("gagné horizontalement")
        print_winner()

    # détecter la victoire verticale
    count = 0
    for i in range(3):
        current_button = buttons[clicked_col][i]
        # current_button.config(text="CHECK")
        if current_button['text'] == current_player:
            count += 1
    if count == 3:
        #print("gagné verticalement")
        print_winner()

    # détecter la victoire diagonale
    count = 0
    for i in range(3):
        current_button = buttons[i][i]
        # current_button.config(text="CHECK")
        if current_button['text'] == current_player:
            count += 1
    if count == 3:
        #print("gagné diagonalement")
        print_winner()

    # détecter la victoire diagonale inversee
    count = 0
    for i in range(3):
        current_button = buttons[2-i][i]
        # current_button.config(text="CHECK")
        if current_button['text'] == current_player:
            count += 1
    if count == 3:
        #print("gagné diagonalement inversee")
        print_winner()

    if win is False:
        #print("Détecter le match nul")
        count = 0
        for col in range(3):
            for row in range(3):
                current_button = buttons[col][row]
                if current_button['text'] == 'X' or current_button['text'] == 'O':
                    count += 1
        #print(count)
        if count == 9:
            print("Match nul")
def place_symbol(row, column):
    #print("click", row, column)

    clicked_button = buttons[column][row]
    if clicked_button['text'] == "":
        clicked_button.config(text=current_player)

        check_win(row, column)
        switch_player()
def draw_grid():
    for column in range(3):
        buttons_in_cols = []
        for row in range(3):
            button = tkinter.Button(
                root, font=("Arial", 50),
                width=5, height=2,
                command=lambda r=row, c=column: place_symbol(r, c)
            )
            button.grid(row=row, column=column)
            buttons_in_cols.append(button)
        buttons.append(buttons_in_cols)
# stockage
buttons = []
current_player = "X"
win = False

# créer la fenetre de jeu
root = tkinter.Tk()

# personalisation de la fenetre
root.title("TicTactoe")
root.wm_minsize(500, 500)

draw_grid()
root.mainloop()