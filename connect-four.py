# packages
import numpy as np

# 0 to quit case 
# ascii check that it's a character
# check when to end game
# check that location is valid and empty
# this is not connect-four

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
    
    def checkIfWinnerVertically(self, colUser):
        # check vertically
        for col in range(self.dimCols):
            sum = 0
            unique, counts = np.unique(self.board[:, col], return_counts=True)
            dictTemp = dict(zip(unique, counts))
            if colUser in dictTemp.keys():
                sum = dictTemp[colUser]
                print(dictTemp[colUser])
                if sum == 4:
                    return True
        return False
    
    def checkIfWinnerHorizontally(self, colUser):
        # check horizontally
        for row in range(self.dimRows):
            sum = 0
            unique, counts = np.unique(self.board[row, :], return_counts=True)
            dictTemp = dict(zip(unique, counts))
            if colUser in dictTemp.keys():
                sum = dictTemp[colUser]
                print(dictTemp[colUser])
                if sum == 4:
                    return True
        return False     
    
    def checkIfWinner(self, colUser):
        win1 = self.checkIfWinnerVertically(colUser)
        if win1:
            return True
        win2 = self.checkIfWinnerHorizontally(colUser)
        if win2:
            return True
        return False
    
    def updateBoard(self, locationUser, colUser):
        row = locationUser[0]
        col = locationUser[1]
        win = False
        # check if user wants to end game
        if row != 0 and col != 0:
            self.board[row-1][col-1] = colUser
            win = self.checkIfWinner(colUser)
            self.printBoard()
        # check if game was won
        if win:
            return True
        return False
    
    def playGame(self, colUser1, colUser2):
        endGame = False
        while endGame == False:
            print(f'\nUser 1!')
            locationUser1 = self.getLocation()
            endGame = self.updateBoard(locationUser1, colUser1)
            if endGame:
                continue
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





