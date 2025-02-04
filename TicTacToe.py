#A program that creates an interactive tic tac toe board 

#multiple variables need value for each, shown by commas and duplicated 10's
rowSize, columnSize = 3,3

board = [[0 for i in range(rowSize)] for i in range(columnSize)]

#traverses 2D array to set each square a value

def setValues(array)
    for i in range(columnSize):
        for j in range(rowSize):
            array[i][j] = i
            j = j + 1
        array[]
        j = j + 1
        

def printBoard(array):
    for i in range(rowSize):
        print(board[i])

def makeSelection(player):
    playerChoice = input("Make a choice: ")
    

#Main function
while(true):
    printBoard(board)
    
    



