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
    while (valid is  False):
        try:
            valueDim=int(input(inputLine))
            if (valueDim < 4 or (valueDim in numsToAvoid)) and valueDim != 0 :
                raise ValueError
            else:
                valid = True
                print(f'You entered {valueDim} for {dimension}.')
        except ValueError:
            print(errorLine)
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
    def __init__(self, dimRows, dimCols, colUser1, colUser2):
        self.board = np.full((dimRows, dimCols), 'O')
        self.dimRows = dimRows
        self.dimCols = dimCols
        self.colUser1 = colUser1
        self.colUser2 = colUser2
    def getBoard(self):
        return self.board
    def printBoard(self):
        print(self.board)
    def getLocation(self):
        stop = False
        row = 0
        col = 0
        row = getPosNumUserInput("row", "what row?", "error", [])
        if row != 0:
            col = getPosNumUserInput("col", "what col?", "error", [])
        return (row, col)
    def updateBoard(self, locationUser):
        pass
    def playGame(self):
        stop = False
        while stop == False:
            print(f'\nUser 1!')
            locationUser1 = self.getLocation()
            if locationUser1 == (0, 0):
                stop = True
                continue
            self.updateBoard(locationUser1)
            print(f'\nUser 2!')
            locationUser2 = self.getLocation()
            if locationUser2 == (0, 0):
                stop = True
                continue
            self.updateBoard(locationUser2)


inputLine = "Enter a number greater than or equal to 4. Enter 0 to quit:"
valueRows = getPosNumUserInput("rows", inputLine, "error", [])
valueCols = getPosNumUserInput("columns", inputLine, "error", [])
charUser1 = getCharUserInput(1, "Enter the 1st letter of your favourite colour. Enter 0 to quit: ", "error char", ['O'])
charUser2 = getCharUserInput(2, "Enter the 1st letter of your favourite colour. Enter 0 to quit: ", "error char", ['O', charUser1])
connectFourBoard = ConnectFourBoard(valueRows, valueCols, charUser1, charUser2)
print(connectFourBoard.getBoard())
print()
connectFourBoard.playGame()


# def getLocation (dimension):





