from SudokuBoard import *

def climbHills(inputBoard): #string sb to indicate which board is being played i.e. ("sudoku1.csv")
    sb = SudokuBoard(inputBoard)
    print (sb)
    b = sb.board #2d array


def main():
    climbHills("sudoku1.csv")

