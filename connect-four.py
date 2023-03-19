# packages
import numpy as np

# 0 to quit case 
# ascii check that it's a character
# check when to end game
# check that location is valid and empty

def userInputDimBoard(dimension, inputLine):
    """
    Function that retreives a board dimension from the user.
    """
    valueDim = 0
    valid = False
    print(f'Getting the number of {dimension}!')
    while (valid is  False):
        try:
            valueDim=int(input(inputLine))
            if valueDim < 4 and valueDim != 0:
                raise ValueError
            else:
                valid = True
                print(f'You entered {valueDim} {dimension}.')
        except ValueError:
            print("This is not a whole number greater than or equal to 4. Enter 0 to quit: ")
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
    def __init__(self, dimRows, dimCols):
        self.board = np.full((dimRows, dimCols), 'O')
    def getBoard(self):
        return self.board
    def printBoard(self):
        print(self.board)


inputLine = "Enter a number greater than or equal to 4. Enter 0 to quit:"
valueRows = userInputDimBoard("rows", inputLine)
valueCols = userInputDimBoard("columns", inputLine)
connectFourBoard = ConnectFourBoard(valueRows, valueCols)
print(connectFourBoard.getBoard())
charUser1 = userInputColor(1, ['O'])
charUser2 = userInputColor(2, ['O', charUser1])


# def getLocation (dimension):





