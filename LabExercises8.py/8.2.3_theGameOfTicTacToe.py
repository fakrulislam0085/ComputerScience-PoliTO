def isBoardFull(Board) :
    result = all(cell != "-" for row in Board for cell in row)
    return result

# Check for win or tie 
def isWinner(Board, row, col, curr_move) : 
    # Check row 
    if all(Board[row][j] == curr_move for j in range(3)) :
        return True 

    # Check col 
    if all(Board[i][col] == curr_move for i in range(3)) : 
        return True 

    # Check primary diagonal 
    if row == col : 
        if all(Board[i][i] == curr_move for i in range(3)) :
            return True 

    # Check secondary diagonal 
    if row + col == 2 : 
        if all(Board[i][2-i] == curr_move for i in range(3)) :
            return True 

    return False       

# Display the Board 
def displayTheBoard(gameBoard): 
    for row in gameBoard :
        print(" | ".join(row)) 
        print()

# Take player input 
def playerMove(Board, row, col, move) : 
    if Board[row][col] == "-" : 
        Board[row][col] = move 
        return True 
    else :
        print("Cell is already taken! Try again 🤷‍♀️")
        return False

# Printing the game board 
def print_game_board(gameBoard) : 
    print("Game Board: ") 
    for i in range(3) : 
        for j in range(3) : 
            print(gameBoard[i][j], end=" ")
        print()


def main() : 
    print("🎮 Welcome To Tic-Tac-Toe Game! 🎉\n")

    # Create the game board
    gameBoard = [["-" for _ in range(3)] for _ in range(3)]
    displayTheBoard(gameBoard) 

    player1 = True

    while True : 
        try : 
            row, col = map(int, input("Enter the row(0~2) and column(0~2) of the cell: ").split()) 
        except ValueError : 
            print("Enter two valid integers separed by a space.\n")
            continue 

        if row not in range(3) or col not in range(3) : 
            print("Invalid Position! Choose between 0 and 2.")
            continue 

        if player1 : 
            move = "X"      # Fixed move for player 1
            if playerMove(gameBoard, row, col, move) :
                displayTheBoard(gameBoard)
                if isWinner(gameBoard, row, col, move) : 
                    print(f"Congratulations! Player1 Wins!🏆")
                    break
                # Switch the player 
                player1 = False             

        else:
            oppositeMove = "O"  # Fixed move for player 2 
            if playerMove(gameBoard,row, col, oppositeMove) :
                displayTheBoard(gameBoard) 
                if isWinner(gameBoard, row, col, oppositeMove) :
                    print(f"Congratulations! Player2 Wins!🏆")
                    break
                # Switch the player 
                player1 = True

        if isBoardFull(gameBoard) : 
            print("It's a Tie!")
            break


if __name__ == "__main__" : 
    main() 