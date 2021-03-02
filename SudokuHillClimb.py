#SudokuHillClimb.py is a program that attempts to solve a 25x25 sudoku board using the Hill Climbing technique 
#Author(s): Mason Humphrey, 
#Date: 3/1/2021

from SudokuBoard import *

board = []
globalMin = 1000
bestBoard = []
conflictCollection = [1001] #a list of all of the conflict values, if the sum = 0 then we have completed the game
maxIterations = 100 #the number of times we iterate over the entire board
Iterations = 0 #current number of iterations
stopper = 0 #used to find out how many iterations since we last updated globalMin

#climbHills(inputBoard) takes in an appropriately formatted .csv which represens a sudoku board, and attempts to solve it via hill climbing
#Author: Mason Humphrey
#Date: 2/31/2021
#params: inputBoard - .csv file containing a 25x25 sudoku board
def climbHills(inputBoard): #string sb to indicate which board is being played i.e. ("sudoku1.csv")
    global board
    global conflictCollection
    global Iterations
    global maxIterations
    global globalMin
    global stopper

    sb = SudokuBoard(inputBoard)
    board = sb.board #2d array
    ls = sb.lockedSquares #locked squares
    
    while sum(conflictCollection) != 0 and stopper < 3 and Iterations < maxIterations * 100: #Just finished an iteration, and the globalMin is not 0, maxIterations*100 because there are indexes in the board

        if sum(conflictCollection) < globalMin:  #checks local min against global min
            globalMin = sum(conflictCollection)  #if local min is smaller, then we change globalMin to this
            bestBoard = sb                       #we also save this board, as it is our best solution thus far, Ask nick if this works like this
            stopper = 0
        else:
            stopper = stopper + 1

        conflictCollection.clear()  #clear conflicts for that iteration, iterate again

        for x in range(len(board)):      #begins looping through the board, switching values for more favorable ones
            for y in range(len(board)): 
                if ls[x][y] == True:     #if the square is locked, 
                    pass                 #do nothing
                else:                    #otherwise we are allowed to edit this square

                    print ("current y: " , x, "current x: ", y) #needs to be swapped because board is processed col, row and I didn't realize til now
                    print ("Current Value:", board[x][y], "\n")
                    print (sb)

                    column = SudokuBoard.getColumn(sb, y)
                    row = SudokuBoard.getRow(sb,x)
                    region = SudokuBoard.getRegion(sb, (int(y/5)), (int(x/5))) #needs to be swapped because this is processed col, row, in SudokuBoard

                    print ("Current Column: ", column)
                    print ("Current Row: ", row)
                    print ("Current Region:", region, "\n") 

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
                    bestVal = conflictList.index(min(conflictList)) + 1 #+1 because index starts at 0, and we start at 1
                    print ("\nmin # of conflicts:", minConflicts, ) #minconflicts is # of conflicts in best possible move
                    conflictCollection.append(minConflicts) 

                    print ("best value:", bestVal, "\n")
                    board = SudokuBoard.replaceSquare(sb, x, y, bestVal)
                    print("\n --------------------------------------------------------------------------\n\n")

                    Iterations = Iterations + 1 #to keep track of the # of iterations


    #If there are 0 conflicts, we have solved the puzzle
    if sum(conflictCollection) == 0:
        print("Game completed optimally in ", (Iterations/100) , " iterations\n")
        print("Complete Board:\n")
        print (sb)

    elif stopper >= 3: #if it has been 3 full board iterations and we havent reset the global min, we are at the global min
        print("Game ended due to reaching global min in", (Iterations/100) , "iterations\n")
        print("Global minimum # of conflicts: ", globalMin, "\n")
        print("Global minimum board:\n")
        print (bestBoard)

    #If we are over the number
    elif Iterations >= maxIterations * 100: #*100 because there are indexes in the board
        print("Game ended due to max iteration limit of", maxIterations, "\n")
        print("Global minimum # of conflicts: ", globalMin, "\n")
        print("Global minimum board:\n")
        print (bestBoard)
    

# To test, un-comment one of these
#climbHills("sudoku1.csv")
#climbHills("sudoku2.csv")
#climbHills("sudoku3.csv")
#climbHills("sudoku4.csv")
