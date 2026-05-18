board= [1,2,3,4,5,6,7,8,9]

def grid():
    print (f" {board[0]} | {board[1]} | {board[2]} ")
    print ("----------")
    print (f" {board[3]} | {board[4]} | {board[5]} ")
    print ("----------")
    print (f" {board[6]} | {board[7]} | {board[8]} ")

choice= input("Please choose your move between 'O' and 'X': ").upper()
choice2= "x"
print("Player_1 chose: ",choice)
print ("The game has been begun!!😊")

grid()

for turn in range(9):
    if turn % 2 == 0:
        move = int(input("Player 1, choose your move (1-9): "))
        if move < 1 or move > 9 or board[move-1] in ["X","O"]:
            print("Invalid move! Try again.")
            move = int(input("Player 1, choose your move (1-9): "))
        board[move-1] = choice
        grid()
    else:
        move2 = int(input("Player 2, choose your move (1-9): "))
        if move2 < 1 or move2 > 9 or board[move2-1] in ["X","O"]:
            print("Invalid move! Try again.")
            move2 = int(input("Player 2, choose your move (1-9): "))
        board[move2-1] = choice2
        grid()