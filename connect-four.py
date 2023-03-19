# packages
import numpy as np

# 0 to quit case 
# ascii check that it's a character
# check when to end game
# check that location is valid and empty

def getPosNumUserInput(dimension, inputLine, errorLine, numsToAvoid):
    """
    Function that retreives a positive number input from the user greater than or equal to 4.
    """
    valueDim = 0
    valid = False
    print(f'Getting the number of {dimension}!')
    valueDim=int(input(inputLine))        
    print(f'You entered {valueDim} for {dimension}.')
    return valueDim

def getCharUserInput(userNum, inputLine, errorLine, invalidChar):
    print(f'Hello, user {userNum}. What is the 1st letter of your favourite color?')
    valid = False
    favColor = ""
    while (valid is False):
        try:
            favColor = input(inputLine)
            if len(favColor) > 1 or (favColor in invalidChar):
                raise ValueError
            else:
                valid = True
                print(f'You entered {favColor}.')
        except ValueError:
            print(f'{favColor} is an invalid input. Please try again.')
    return favColor

class ConnectFourBoard:
    def __init__(self, dimRows, dimCols):
        self.board = np.full((dimRows, dimCols), 'O')
        self.dimRows = dimRows
        self.dimCols = dimCols
    def getBoard(self):
        return self.board
    def printBoard(self):
        print(self.board)
    def getLocation(self):
        stop = False
        row, col = 0, 0
        row = getPosNumUserInput("row", "what row?", "error", [])
        if row != 0:
            col = getPosNumUserInput("col", "what col?", "error", [])
        return (row, col)
    def updateBoard(self, locationUser, colUser):
        row = locationUser[0]
        col = locationUser[1]
        endGame = False
        if row != 0 and col != 0:
            self.board[row-1][col-1] = colUser
        else:
            endGame = True
        self.printBoard()
        return endGame
    def playGame(self, colUser1, colUser2):
        endGame = False
        while endGame == False:
            print(f'\nUser 1!')
            locationUser1 = self.getLocation()
            endGame = self.updateBoard(locationUser1, colUser1)
            print(f'\nUser 2!')
            locationUser2 = self.getLocation()
            endGame = self.updateBoard(locationUser2, colUser2)

inputLine = "Enter a number greater than or equal to 4. Enter 0 to quit:"
valueRows = getPosNumUserInput("rows", inputLine, "error", [])
valueCols = getPosNumUserInput("columns", inputLine, "error", [])
colUser1 = getCharUserInput(1, "Enter the 1st letter of your favourite colour. Enter 0 to quit: ", "error char", ['O'])
colUser2 = getCharUserInput(2, "Enter the 1st letter of your favourite colour. Enter 0 to quit: ", "error char", ['O', colUser1])
connectFourBoard = ConnectFourBoard(valueRows, valueCols)
print(connectFourBoard.getBoard())
print()
connectFourBoard.playGame(colUser1, colUser2)


# def getLocation (dimension):





