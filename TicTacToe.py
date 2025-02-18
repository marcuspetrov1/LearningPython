#A program that creates an interactive tic tac toe board 

#multiple variables need value for each, shown by commas and duplicated 10's
class TicTacToe:

    #initializes the instances variables of the class
    def __init__(self, gameSize, playerOne, playerTwo):    
        self.rowSize, self.columnSize = gameSize, gameSize
        #self.columnSize = gameSize
        self.board = [['-' for i in range(self.rowSize)] for i in range(self.columnSize)]
        self.playerOne = playerOne
        self.playerTwo = playerTwo

    #traverses 2D array to set each square a value
    def printBoard(self):
        for i in range(self.rowSize):
            print(self.board[i])
            print("---------------")

    def checkSpace(self, row, col, player):    
            if(self.board[row][col] == "-"):
                if(player == self.playerOne):
                    self.board[row][col] = "X"
                elif(player == self.playerTwo):
                    self.board[row][col] = "O"
            else:
                print("Thats an occupied square! Pick another!")
                self.makeSelection(player)

    def makeSelection(self, player):
        playerChoice = int(input(player + ", What is your move?" ))
        
        #finding the index on the board of playersChoice 
        row = (playerChoice - 1) // 3
        col = (playerChoice - 1) % 3
    
        self.checkSpace(row, col, player)

    #Gives each space on grid a value for user input 
    def defineSpace(self):
        boardSpot = 1
        for i in range(self.rowSize):
            for j in range(self.columnSize):
                self.board[i][j] = boardSpot
                boardSpot = boardSpot + 1

    #boardSelection = defineSpace(board)

    def checkWinner(self, player):
        #checks each row for a matching each 3 pair 
        for i in range(self.rowSize):
            #checks each row for a matching each 3 pair HORIZONTAL
            #cannot use "and" operatior because it is looking for specific value, not truthly value
            if((self.board[i][0] == self.board[i][1] == self.board[i][2] == "X") or (self.board[i][0] == self.board[i][1] == self.board[i][2] == "O")):
                print(player + " wins!")
                return True
            #checks each row for a matching each 3 pair VERTICAL
            elif((self.board[0][i] == self.board[1][i] == self.board[2][i] == "X") or (self.board[0][i] == self.board[1][i] == self.board[2][i] == "O")):
                print(player + " wins!")
                return True
            #checks each row for a matching each 3 pair TRIANGLULAR(left -> right)
            elif((self.board[0][0] == self.board[1][1] == self.board[2][2] == 'X') or (self.board[0][0] == self.board[1][1] == self.board[2][2] == 'O')):
                print(player + " wins!")
                return True
            #checks each row for a matching each 3 pair TRIANGLULAR(right -> left)
            elif((self.board[0][2] == self.board[1][1] == self.board[2][0] == 'X') or (self.board[0][2] == self.board[1][1] == self.board[2][0] == 'O')):
                print(player + " wins!")
                return True
        else: 
            return False

#---MAIN----------------------------------------------------------------------------------

game = TicTacToe(3, "Bill", "Bob")

while(True):
    game.makeSelection(game.playerOne)
    game.printBoard()
    if(game.checkWinner(game.playerOne)):
        print("Game Over! Thanks for playing!")
        break
    game.makeSelection(game.playerTwo)
    game.printBoard()
    if(game.checkWinner(game.playerTwo)):
        print("Game Over! Thanks for playing!")
        break




        
    



