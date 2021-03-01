from SudokuBoard import *


x = 0 #current x coord
y = 0 #current y coord
board = []
globalMin = 100


def climbHills(inputBoard): #string sb to indicate which board is being played i.e. ("sudoku1.csv")
    global board
    global globalMin
    sb = SudokuBoard(inputBoard)
    board = sb.board #2d array
    ls = sb.lockedSquares #locked squares
    
    for x in range(len(board)): 
        for y in range(len(board)): 
            if ls[x][y] == True: #if the square is locked, 
                pass #do nothing
            else: #otherwise we are allowed to edit this square

                print ("current y: " , x, "current x: ", y) #needs to be swapped because board is processed col, row and I didn't realize til now
                print ("Current Value: ", board[x][y])
                print (sb)

                column = SudokuBoard.getColumn(sb, y)
                row = SudokuBoard.getRow(sb,x)
                region = SudokuBoard.getRegion(sb, (int(y/5)), (int(x/5))) #needs to be swapped because this is processed col, row, in SudokuBoard (at least i think, either way it works)

                # print("\n")
                print ("Current Column: ", column)
                print ("Current Row: ", row)
                print ("Current Region: ", region) #currently broken
                # print ("y/5:", int(x/5), "    x/5:", int(y/5))

                currentValue = board[x][y]
                indexCount = 0
                conflictList = []
                for j in range(1,26):
                    if j == currentValue:#if we are at the current val, it is counted 3 too many times
                        conflictList.append(SudokuBoard.countConflicts(sb, j, column, row, region))
                        conflictList[-1] = conflictList[-1] - 3

                    else:
                        conflictList.append(SudokuBoard.countConflicts(sb, j, column, row, region))



                for j in conflictList: #simply for printing visual / understanding what is going on
                    indexCount = indexCount + 1
                    print("Trying: ", indexCount,  "    conflicts:", j)
                
                minConflicts = min(conflictList)
                bestVal = conflictList.index(min(conflictList)) + 1
                print ("min # of conflicts:", minConflicts)
                print ("best value:", bestVal, "\n")
                print("\n")
                board = SudokuBoard.replaceSquare(sb, x, y, bestVal)

                #need some way of continuing until all mins are 0









climbHills("sudoku1.csv")

#we are at starting position, are we locked? if not:
    #replace current value, with every value 1-25
    #with each of these, look at # of conflicts using getRow, getColumn, and getRegion, update heuristic (global_min, local_min)
    #pick swap that had the least conflicts. This is best choice
    #do this until all conflicts = 0 for every [x][y] or until we get stuck at a global min