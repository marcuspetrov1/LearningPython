#A program that creates an interactive tic tac toe board 

#multiple variables need value for each, shown by commas and duplicated 10's
rowSize, columnSize = 3,3

board = [['-' for i in range(rowSize)] for i in range(columnSize)]

#traverses 2D array to set each square a value
def printBoard(array):
    for i in range(rowSize):
        print(board[i])
        print("---------------")


def makeSelection(player):
    playerChoice = int(input(player + ", What is your move?"))
    
    #finding the index on the board of playersChoice 
    row = (playerChoice - 1) // 3
    col = (playerChoice - 1) % 3
    #checkSpace(player)
    if(board[row][col] == "-"):
        if(player == playerOne):
            board[row][col] = "X"
        elif(player == playerTwo):
            board[row][col] = "O"
    else:
        print("Thats an occupied square! Pick another!")
        makeSelection(player)

# def checkSpace(player):
#     if(board[row][col] == "-"):
#         if(player == playerOne):
#             board[row][col] = "X"
#         elif(player == playerTwo):
#             board[row][col] = "O"
#     else:
#         print("Thats an occupied square! Pick another!")
#         makeSelection(player)
    

#Gives each space on grid a value for user input 
def defineSpace(array):
    boardSpot = 1
    for i in range(rowSize):
        for j in range(columnSize):
            board[i][j] = boardSpot
            boardSpot = boardSpot + 1

#boardSelection = defineSpace(board)

def checkWinner(board):
    if((board[i][0] and board[i][1] and board [i][2]) == 'X' or 'O'):
        print("Player wins!")


while(True):
    playerOne = "Bill"
    playerTwo = "Bob"
    
    makeSelection(playerOne)
    printBoard(board)
    makeSelection(playerTwo)
    printBoard(board)
    checkWinner(board)



#printBoard(defineSpace(board))
    

        
    



