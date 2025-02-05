#A program that creates an interactive tic tac toe board 

#multiple variables need value for each, shown by commas and duplicated 10's
rowSize, columnSize = 3,3

board = [['-' for i in range(rowSize)] for i in range(columnSize)]

#traverses 2D array to set each square a value
def printBoard(array):
    for i in range(rowSize):
        print(board[i])
        print("---------------")

printBoard(board)

def makeSelection(player):
    playerChoice = int(input("What is your move?"))
    
    #finding the index on the board of playersChoice 
    row = (playerChoice - 1) // 3
    col = (playerChoice - 1) % 3
    checkSpace(player)
    # if(boardSelection[row][col] == " "):
    #     if(playerOne):
    #         boardSelection[row][col] = "X"
    #     else:
    #         boardSelection[row][col] = "O"
    # else:
    #     print("Thats an occupied square! Pick another!")
    #     makeSelection(player)

def checkSpace(player):
    if(boardSelection[row][col] == " "):
        if(playerOne):
            boardSelection[row][col] = "X"
        else:
            boardSelection[row][col] = "O"
    else:
        print("Thats an occupied square! Pick another!")
        makeSelection(player)
    

#Gives each space on grid a value for user input 
def defineSpace(array):
    boardSpot = 1
    for i in range(rowSize):
        for j in range(columnSize):
            board[i][j] = boardSpot
            boardSpot = boardSpot + 1

boardSelection = defineSpace(board)

while(true):
    printBoard()

        


    

#Main function
# while(true):
#     printBoard(board)
    
    



