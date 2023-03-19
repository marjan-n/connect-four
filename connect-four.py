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
            if valueDim < 4 or (valueDim in numsToAvoid):
                raise ValueError
            else:
                valid = True
                print(f'You entered {valueDim} for {dimension}.')
        except ValueError:
            print(errorLine)
    return valueDim

def userInputColor(userNum, invalidChar):
    print(f'Hello, user {userNum}. What is the 1st letter of your favourite color?')
    valid = False
    favColor = ""
    while (valid is False):
        try:
            favColor = input("Enter the 1st letter of your favourite colour. Enter 0 to quit: ")
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
        pass
    def updateBoard(self):
        pass
    def playGame(self):
        stop = False
        while stop == False:
            locationUser1 = self.getLocation()
            self.updateBoard(locationUser1)
            locationUser2 = self.getLocation()
            self.updateBoard(locationUser2)


inputLine = "Enter a number greater than or equal to 4. Enter 0 to quit:"
valueRows = getPosNumUserInput("rows", inputLine, "error", [])
valueCols = getPosNumUserInput("columns", inputLine, "error", [])
charUser1 = userInputColor(1, ['O'])
charUser2 = userInputColor(2, ['O', charUser1])
connectFourBoard = ConnectFourBoard(valueRows, valueCols, charUser1, charUser2)
print(connectFourBoard.getBoard())


# def getLocation (dimension):





