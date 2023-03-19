# packages
import numpy as np

def userInputDimBoard(dimension):
    """
    Function that retreives a board dimension from the user.
    """
    valueDim = 0
    valid = False
    print(f'Getting the number of {dimension}!')
    while (valid is  False):
        try:
            valueDim=int(input("Enter a number greater than or equal to 4. Enter 0 to quit.: "))
            if valueDim < 4 and valueDim != 0:
                raise ValueError
            else:
                valid = True
                print(f'You entered {valueDim} {dimension}.')
        except ValueError:
            print("This is not a whole number greater than or equal to 4. Enter 0 to quit.")
    return valueDim

class ConnectFourBoard:
    def __init__(self, dimRows, dimCols):
        self.board = np.full((dimRows, dimCols), 'O')
    def getBoard(self):
        return self.board


valueRows = userInputDimBoard("rows")
valueCols = userInputDimBoard("columns")
connectFourBoard = ConnectFourBoard(valueRows, valueCols)
print(connectFourBoard.getBoard())



