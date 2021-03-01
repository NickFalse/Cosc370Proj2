from SudokuBoard import *


x = 0 #current x coord
y = 0 #current y coord
board = []


def climbHills(inputBoard): #string sb to indicate which board is being played i.e. ("sudoku1.csv")
    global board
    sb = SudokuBoard(inputBoard)
    board = sb.board #2d array
    ls = sb.lockedSquares #locked squares
    
    for x in range(0, 25): 
        for y in range(0, 25): 
            if ls[x][y] == True: #if the square is locked, 
                pass #do nothing
            else: #otherwise we are allowed to edit this square

                print ("current y: " , x, "current x: ", y) #needs to be swapped because board is processed col, row and I didn't realize til now
                print ("Current Value: ", board[x][y])
                print (sb)

                column = SudokuBoard.getColumn(sb, x)
                row = SudokuBoard.getRow(sb,y)
                region = SudokuBoard.getRegion(sb, (int(y/5)), (int(x/5))) #needs to be swapped because this is processed col, row, in SudokuBoard (at least i think, either way it works)

                # print("\n")
                # print ("Current Column: ", column)
                # print ("Current Row: ", row)
                # print ("Current Region: ", region) #currently broken
                # print ("y/5:", int(x/5), "    x/5:", int(y/5))



                currentValue = board[x][y]
                indexCount = 0
                conflictList = []
                for j in range(1,26):
                    conflictList.append(SudokuBoard.countConflicts(sb, j, column, row, region))

                for j in conflictList:
                    indexCount = indexCount + 1
                    print("Trying: ", indexCount,  "    conflicts:", j)

                









    #count # of total conflicts (instances of the current value) in row, col, and region, this is local min
    #loop through all numbers 1-25, replacing the current square w/ the number


    #board = SudokuBoard.replaceSquare(sb, 0, 0, 99)
    #print(SudokuBoard.replaceSquare(sb, 0, 0, 99))  how to replace a square








climbHills("sudoku1.csv")

#we are at starting position, are we locked? if not:
    #replace current value, with every value 1-25
    #with each of these, look at # of conflicts using getRow, getColumn, and getRegion, update heuristic (global_min, local_min)
    #pick swap that had the least conflicts. This is best choice
    #do this until all conflicts = 0 for every [x][y] or until we get stuck at a global min