# print initial layout
print("Game board layout: ")
print("[ 0 1 2 ]")
print("[ 3 4 5 ]")
print("[ 6 7 8 ]")

# create all necessary lists and variables
xwin = False
owin = False
board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
boardspaces = [0, 1, 2, 3, 4, 5, 6, 7, 8]
turns = 0
q = 0
boardentry = "X"

while (xwin is False and owin is False) and turns < 9:
    # game program
    if q % 2 == 0:
        select = int(input("Player 1 (X), Enter the space you want to move to: "))
        boardentry = "X"
    else:
        select = int(input("Player 2 (O), Enter the space you want to move to: "))
        boardentry = "O"

    if select not in boardspaces:
        print("space already taken or invalid input, try again")
        continue
    else:
        boardspaces.remove(select)
        board[select] = boardentry
        turns += 1

        print("[", board[0], board[1], board[2], "]")
        print("[", board[3], board[4], board[5], "]")
        print("[", board[6], board[7], board[8], "]")
    q += 1

    # checking to see if either play has won the game before next move
    # check rows
    if (board[0] == board[1] == board[2]) and board[0] != "-":
        if board[0] == "X":
            xwin = True
        else:
            owin = True
    elif (board[3] == board[4] == board[5]) and board[3] != "-":
        if board[3] == "X":
            xwin = True
        else:
            owin = True
    elif (board[6] == board[7] == board[8]) and board[6] != "-":
        if board[6] == "X":
            xwin = True
        else:
            owin = True
    # check columns
    elif (board[0] == board[3] == board[6]) and board[0] != "-":
        if board[0] == "X":
            xwin = True
        else:
            owin = True
    elif (board[1] == board[4] == board[7]) and board[1] != "-":
        if board[1] == "X":
            xwin = True
        else:
            owin = True
    elif (board[2] == board[5] == board[8]) and board[2] != "-":
        if board[2] == "X":
            xwin = True
        else:
            owin = True
    # checking diagonals
    elif (board[0] == board[4] == board[8]) and board[0] != "-":
        if board[0] == "X":
            xwin = True
        else:
            owin = True
    elif board[6] == board[4] == board[2] and board[6] != "-":
        if board[6] == "X":
            xwin = True
        else:
            owin = True
# print out result of the game played
print("\n")
if turns == 9:
    print("Game tied")
elif xwin is True:
    print("Player 1 (X) wins")
else:
    print("Player 2 (O) wins")
