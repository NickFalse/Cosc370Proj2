#SudokuAnnealing.py is a program that attempts to solve a 25x25 sudoku board using the simulated annealing technique 
#Author(s): Mason Humphrey, 
#Date: 3/1/2021

from SudokuBoard import *
import time
from random import randint

board = []
globalMin = 1000
bestBoard = []
conflictCollection = [1001] #a list of all of the conflict values, if the sum = 0 then we have completed the game
maxIterations = 150 #the number of times we iterate over the entire board
Iterations = 0 #current number of iterations
stopper = 0 #used to find out how many iterations since we last updated globalMin
temp = 5
worstVal = 5
guess = 0
guessIndex = 0

#sudokuAnnealing(inputBoard) takes in an appropriately formatted .csv which represens a sudoku board, and attempts to solve it via hill climbing
#Author: Mason Humphrey
#Date: 3/2/2021
#params: inputBoard - .csv file containing a 25x25 sudoku board
def sudokuAnnealing(inputBoard): #string sb to indicate which board is being played i.e. ("sudoku1.csv")
    start = time.time()

    global board
    global conflictCollection
    global Iterations
    global maxIterations
    global globalMin
    global stopper
    global temp
    global guess
    global guessIndex

    sb = SudokuBoard(inputBoard)
    board = sb.board #2d array
    ls = sb.lockedSquares #locked squares
    
    while sum(conflictCollection) != 0 and stopper < 5 and Iterations < maxIterations * 625: #Just finished an iteration, and the globalMin is not 0, maxIterations*100 because there are indexes in the board
        if Iterations > 0:
            temp = temp - 1 #the temp is decremented by 2 every iteration (starting at 10), we have 5 levels

        if temp == -1:  #checks temp to see if we are done
            bestBoard = sb #we need to print all the goodies
            print("Game ended with", sum(conflictCollection), "Conflicts")
            print("Global minimum board:\n")
            print (bestBoard)
            return exit()
            

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
                    conflictList = []

                    for j in range(1,26):
                        if j == currentValue:#if we are at the current val, it is counted 3 too many times
                            conflictList.append(SudokuBoard.countConflicts(sb, j, column, row, region))
                            conflictList[-1] = conflictList[-1] - 3
                        else:
                            conflictList.append(SudokuBoard.countConflicts(sb, j, column, row, region))


                    bestVal = guess_and_Check(conflictList, 0)   #returning to 'None' for some reason

                    print("Our returned guess:", bestVal, "\n")

                    board = SudokuBoard.replaceSquare(sb, x, y, bestVal)

                    conflictCollection.append(conflictList[guess - 1]) #may be appending wrong value thus getting lots of conflicts

                    #print("Total # of conflicts:", sum(conflictCollection),"\n")
                        
                    print("Conflict Collection", conflictCollection, "\n")

                    # for j in conflictList: #simply used for printing visual / understanding what is going on
                    #     indexCount = indexCount + 1
                    #     print("Trying: ", indexCount,  "    conflicts:", j) trying the number indexCount, the value at this index is the num of conflicts
                    
                    #minConflicts = min(conflictList)
            

                    print ("Guessed value:", bestVal, "\n")

                    print ("Temp:", temp,"\n")

                    print("\n --------------------------------------------------------------------------\n\n")

                    Iterations = Iterations + 1 #to keep track of the # of iterations

    end = time.time()
    #If there are 0 conflicts, we have solved the puzzle
    # if sum(conflictCollection) == 0:
    #     #print("Game completed optimally in ", round((Iterations/625),2) , " iterations\n")
    #     print("Sudoku solved! There are 0 conflicts!")
    #     print("Time taken:", round((end - start),2),"\n")
    #     print("Complete Board:\n")
    #     print (sb)

    # elif stopper >= 5: #if it has been 10 full board iterations and we havent reset the global min, we are at the global min
    #     print("Game ended due to reaching global min in", round((Iterations/625),2), "iterations\n")
    #     print("Game ending unsolved due to reaching global min conflicts\n")
    #     print("Time taken:", round((end - start),2),"\n")
    #     print("Global minimum # of conflicts:", globalMin, "\n")
    #     print("Global minimum board:\n")
    #     print (bestBoard)

    # #If we are over the number
    # elif Iterations >= maxIterations * 625: #*100 because there are indexes in the board
    #     print("Game ended due to max iteration limit of", maxIterations, "\n")
    #     print("Global minimum # of conflicts:", globalMin, "\n")
    #     print("Time taken:", round((end - start),2), "seconds\n")
    #     print("Global minimum board:\n")
    #     print (bestBoard)


def guess_and_Check(conflictList, failure):
    global conflictCollection
    global temp
    global guessIndex
    guess = randint(1,25)
    guess_failure = failure

    if guess_failure > 25: #if we have failed 25 times, return the value with the least conflicts
        print("Total # of conflicts:", sum(conflictCollection),"\n")
        return conflictList.index(min(conflictList)) + 1  
    #return the value with the least amount of conflicts

    print("Guessing:", guess, "At a temp of:", temp ,"\n")
    guessConflicts = conflictList[guess - 1] #at our guess index, how many conflicts did we have?

    print("number of conflicts with guess:", guessConflicts, "\n")

    if temp == 5 and guessConflicts <= worstVal * 1:
        print("Accepting guess of", guess, "\n")
        guessIndex = conflictList[guess - 1]
        return guess
    elif temp == 4 and guessConflicts <= worstVal * .8:
        print("Accepting guess of", guess, "\n")
        guessIndex = conflictList[guess - 1]
        return guess #need to also return the number of conflicts
    elif temp == 3 and guessConflicts <= worstVal * .6:
        print("Accepting guess of", guess, "\n")
        guessIndex = conflictList[guess - 1]
        return guess
    elif temp == 2 and guessConflicts <= worstVal * .4:
        print("Accepting guess of", guess, "\n")
        guessIndex = conflictList[guess - 1]
        return guess
    elif temp == 1 and guessConflicts <= worstVal * .2:
        print("Accepting guess of", guess, "\n")
        guessIndex = conflictList[guess - 1]
        return guess
    elif temp == 0 and guessConflicts <= worstVal * .0:
        print("Accepting guess of", guess, "\n")
        guessIndex = conflictList[guess - 1]
        print("Total # of conflicts:", sum(conflictCollection),"\n")
        return guess
    else:
        print("rejecting guess, guessing again \n")
        guess_failure = guess_failure + 1
        return guess_and_Check(conflictList, guess_failure)
    


# To test, un-comment one of these
#sudokuAnnealing("sudoku1.csv")
#sudokuAnnealing("sudoku2.csv")
#sudokuAnnealing("sudoku3.csv")
#sudokuAnnealing("sudoku4.csv")
