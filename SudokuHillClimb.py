from SudokuBoard import *

board = []
globalMin = 100 #
conflictCollection = [100] #a list of all of the conflict values, if the sum = 0 then we have completed the game
maxIterations = 50 #the number of times we iterate over the entire board
Iterations = 0 #current number of iterations


def climbHills(inputBoard): #string sb to indicate which board is being played i.e. ("sudoku1.csv")
    global board
    global conflictCollection
    global Iterations
    global maxIterations
    sb = SudokuBoard(inputBoard)
    board = sb.board #2d array
    ls = sb.lockedSquares #locked squares
    
    while sum(conflictCollection) != 0 and Iterations < maxIterations * 100: #Just finished an iteration, and the globalMin is not 0
        conflictCollection.clear()  #clear conflicts for that iteration, iterate again

        for x in range(len(board)):      #begins looping through the board, switching values for more favorable ones
            for y in range(len(board)): 
                if ls[x][y] == True:     #if the square is locked, 
                    pass                 #do nothing
                else:                    #otherwise we are allowed to edit this square

                    print ("current y: " , x, "current x: ", y) #needs to be swapped because board is processed col, row and I didn't realize til now
                    print ("Current Value: ", board[x][y])
                    print (sb)

                    column = SudokuBoard.getColumn(sb, y)
                    row = SudokuBoard.getRow(sb,x)
                    region = SudokuBoard.getRegion(sb, (int(y/5)), (int(x/5))) #needs to be swapped because this is processed col, row, in SudokuBoard

                    print ("Current Column: ", column)
                    print ("Current Row: ", row)
                    print ("Current Region: ", region) 

                    currentValue = board[x][y]
                    indexCount = 0
                    conflictList = []

                    for j in range(1,26):
                        if j == currentValue:#if we are at the current val, it is counted 3 too many times
                            conflictList.append(SudokuBoard.countConflicts(sb, j, column, row, region))
                            conflictList[-1] = conflictList[-1] - 3
                        else:
                            conflictList.append(SudokuBoard.countConflicts(sb, j, column, row, region))


                    for j in conflictList: #simply used for printing visual / understanding what is going on
                        indexCount = indexCount + 1
                        print("Trying: ", indexCount,  "    conflicts:", j)
                    
                    minConflicts = min(conflictList)
                    bestVal = conflictList.index(min(conflictList)) + 1
                    print ("min # of conflicts:", minConflicts) #minconflicts is local min
                    conflictCollection.append(minConflicts) #in order to calculate global min
                    print ("best value:", bestVal, "\n")
                    print("\n")
                    board = SudokuBoard.replaceSquare(sb, x, y, bestVal)

                    Iterations = Iterations + 1 #to keep track of the # of iterations


    if sum(conflictCollection) == 0:
        print("Game complete in ", Iterations , " iterations")
        print("Final Board:")
        print (sb)

    if Iterations >= maxIterations * 100:
        print("Game ended due to max iteration limit of ", Iterations)
        print("Global min upon failure: ", sum(conflictCollection))
        print("Final Board:")
        print (sb)



climbHills("sudoku2.csv")
