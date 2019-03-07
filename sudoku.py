# File: proj3.py
# Author: Maura Choudhary
# Date: 12/4/18
# Section: 20
# E-mail: maurac1@umbc.edu
# Description: This program allows a user to play or solve a sudoku puzzle

# Constants for the board
MIN_NUM = 1
MAX_NUM = 9
EMPTY = 0
SEPARATOR = ","
BOX1 = [1, 2, 3]
BOX2 = [4, 5, 6]
BOX3 = [7, 8, 9]

# Constants for menus
PLAY = "p"
SOLVE = "s"
SAVE = "s"
UNDO = "u"
QUIT = "q"
YES = "y"
NO = "n"

# Constants for a move list
MOVE_ROW = 0
MOVE_COLUMN = 1
MOVE_NUM = 2

# prettyPrint() prints the board with row and column labels,
#               and spaces the board out so that it looks nice
# Input:        board;   the square 2d game board (of integers) to print
# Output:       None;    prints the board in a pretty way
def prettyPrint(board):
    # print column headings and top border
    print("\n    1 2 3 | 4 5 6 | 7 8 9 ") 
    print("  +-------+-------+-------+")

    for i in range(len(board)): 
        # convert "0" cells to underscores  (DEEP COPY!!!)
        boardRow = list(board[i]) 
        for j in range(len(boardRow)):
            if boardRow[j] == 0:
                boardRow[j] = "_"

        # fill in the row with the numbers from the board
        print( "{} | {} {} {} | {} {} {} | {} {} {} |".format(i + 1, 
                boardRow[0], boardRow[1], boardRow[2], 
                boardRow[3], boardRow[4], boardRow[5], 
                boardRow[6], boardRow[7], boardRow[8]) )

        # the middle and last borders of the board
        if (i + 1) % 3 == 0:
            print("  +-------+-------+-------+")


# savePuzzle() writes the contents a sudoku puzzle out
#              to a file in comma separated format
# Input:       board;    the square 2d puzzle (of integers) to write to a file
#              fileName; the name of the file to use for writing to 
def savePuzzle(board, fileName):
    ofp = open(fileName, "w")
    for i in range(len(board)):
        rowStr = ""
        for j in range(len(board[i])):
            rowStr += str(board[i][j]) + ","
        # don't write the last comma to the file
        ofp.write(rowStr[ : len(rowStr)-1] + "\n")
    ofp.close()

# checkBoardFull() checks if the board is full
#
# Input:           board; the square 2d puzzle of integers
# Output:          solution; the solved puzzle
def checkBoardFull(board):

    full = True
    
    # loop through the board looking for empty spaces
    for i in range(len(board)):
        for j in range(len(board[0])):
            
            # if there's a 0 the board isn't full
            if board[i][j] == 0:
                full = False
    return full

# getValidString() gets a valid user input
#
# Input:           options, prompt; list of valid options, prompt to display
# Output:          choice; valid user choice
def getValidString(options, prompt):

    choice = input(prompt)
    
    # while the user picks something that's not an option
    while choice not in options:
        print("That is not one of the options.")
        choice = input(prompt)
    return choice

# getValidInt()   gets a valid user integer
#
# Input:          prompt; prompt to display
# Output:         choice; valid user choice
def getValidInt(prompt):

    choice = int(input(prompt))

    # while the choice is not in the valid range
    while choice < MIN_NUM or choice > MAX_NUM:
        print("You must choose a number greater than 1 and less than 9.")
        choice = int(input(prompt))
    return choice

# makeMove()     allows the user to place a number in a cell that
#                meets Sudoku requirements
# Input:         board, moves, correct, solution; the square 2d puzzle,
#                the list of moves, a boolean for whether correctness checking
#                is on, a square 2d list of the solution
# Output:        None; lists passed by reference are appropriately altered
def makeMove(board, moves, correct, solution):
    
    moveMade = False
    
    # get a row
    numRow = getValidInt("Enter a row number (1-9): ")

    # get a column
    numColumn = getValidInt("Enter a column number (1-9): ")

    # get a number
    prompt = "Enter a number to put in cell ("+ str(numRow) +", "+ str(numColumn) +"): "
    num = getValidInt(prompt)
    move = [numRow - 1, numColumn - 1, num]

    print()
    
    # find possible errors for a move
    errors = checkMove(board, numRow, numColumn, num)

    available = True
    if board[numRow - 1][numColumn - 1] != 0:
        print("There's already a number there. Try again.")
        available = False
        
    # if correctness checking is on
    if correct and available:

        # perform correctness checking
        if correctCheck(move, solution):

            # check if it's a valid move
            if len(errors) == 0:
                board[numRow - 1][numColumn - 1] = num
                moves.append(move)

            # if it's not, print out the errors
            else:
                for i in range(len(errors)):
                    print(errors[i])

        # if the move isn't right and correctness checking is on
        # print out an error message
        else:
            msg = "OOPS! " + str(num) + " does not belong in position (" \
                + str(numRow) + ", " + str(numColumn) + "): "
            print(msg)

    # if correctness checking is off and it's a valid move
    elif len(errors) == 0 and available:
        board[numRow - 1][numColumn - 1] = num
        moves.append(move)
    
    elif available:
        for i in range(len(errors)):
            print(errors[i])

# checkMove()    checks that a move is valid
#
# Input:         board, rowNum, columnNum, num; the square 2d puzzle, the row where
#                the user is making a move, the column, the list of moves, number
#                they wish to enter
# Output:        errors; list of errors
def checkMove(board, rowNum, columnNum, num):

    # get the row
    row = list(board[rowNum - 1])

    # get the column
    column = []
    for i in range(len(board)):
        column.append(board[i][columnNum-1])

    # get the nonette(square[])
    square = []
    rowStart = 0
    rowStop = 0
    columnStart = 0
    columnStop = 0

    # get the starting row
    if rowNum in BOX1:
        rowStart = 0
    elif rowNum in BOX2:
        rowStart = 3
    elif rowNum in BOX3:
        rowStart = 6

    # get the starting column
    if columnNum in BOX1:
        columnStart = 0
    elif columnNum in BOX2:
        columnStart = 3
    elif columnNum in BOX3:
        columnStart = 6
        
    # create a 2d list for the nonette that
    #   that the number is in
    for i in range(rowStart, rowStart + 3):
        squareRow = []
        for j in range(columnStart, columnStart + 3):
            squareRow.append(board[i][j])
        square.append(squareRow)

    # check for errors
    errors = []

    #if board[rowNum - 1][columnNum - 1] != 0:
        #errors.append("There is already a number in that cell! Try again.")
        #return errors
    # check if the number is in the nonette
    for i in range(len(square)):
        for j in range(len(square[i])):
            if square[i][j] == num:
                eMsg = "The number " + str(num) + " is already in that square."
                errors.append(eMsg)
                
    # check if the number's already in the row
    if num in row:
        eMsg = "The number " + str(num) + " is already in that row."
        errors.append(eMsg)

    # check if the number's already in the column
    if num in column:
        eMsg = "The number " + str(num) + " is already in that column."
        errors.append(eMsg)

    # return the list of errors
    return errors

# correctCheck()   performs correctness checking
#
# Input:           move, solution; a list of the info about the move, the
#                  the 2d puzzle solution
# Output:          valid; boolean for whether or not it's a valid move
def correctCheck(move, solution):

    valid = True
    row = move[MOVE_ROW]
    column = move[MOVE_COLUMN]
    solutionNum = solution[row][column]

    # if the number is not in the solution
    if solutionNum != move[MOVE_NUM]:
        valid = False
        
    return valid

# checkWin()    compares the two boards to see if it has been solved
#
# Input:        board, solution; the square 2d puzzle, the square 2d solution
# Output:       win; boolean reporting if the user has won
def checkWin(board, solution):

    win = True

    # loop through the board and compare to the solution
    for i in range(len(board)):
        for j in range(len(board[i])):

            # if there is a discrepancy it isn't a win
            if board[i][j] != solution[i][j]:
                win = False
    return win

# makeNewBoard()   makes a deep copy of the board
#
# Input:           board; the square 2d puzzle (of integers)
# Output:          copyBoard; the copy of the board
def makeNewBoard(board):

    copyBoard = []
    for i in range(len(board)):
        row = []
        for j in range(len(board[i])):
            row.append(board[i][j])
        copyBoard.append(row)

    return copyBoard

# solvePuzzle()    solves the puzzle
#
# Input:           board, solution; the square 2d puzzle (of integers)
# Output:          solution; the solved puzzle
def solvePuzzle(solution, row, column):
    
    solution = makeNewBoard(solution)

    # BASE CASE: If the board is full
    if checkBoardFull(solution):
        return solution

    # RECURSIVE CASE
    else:

        # Find the first open spot
        row = 0
        column = 0
        while solution[row][column] != 0:

            # if at the end of the row
            if column == len(solution[0]) - 1:
                row += 1
                column = 0
                
            # otherwise in the middle of the row
            else:
                column += 1

        # loop through and try numbers 1-9
        for i in range(1, MAX_NUM + 1):
            
            # check if i is a valid move
            errors = checkMove(solution, (row + 1), (column + 1), i)
            if len(errors) == 0:

                # update board
                solution[row][column] = i

                # recursive call
                               
                result = solvePuzzle(solution, row, column)

                if checkBoardFull(result) and len(result) != 0:
                    return result

        result = []
        return result
        
def main():

    # Create a 2d list of the puzzle
    fileName = input("Enter the file name of the puzzle you'd like to try: ")
    puzzleFile = open(fileName, "r")
    puzzleFileStrings = puzzleFile.readlines()
    puzzle = []
    for i in range(len(puzzleFileStrings)):
        row = []
        row = puzzleFileStrings[i].strip().split(SEPARATOR)
        for j in range(len(row)):
            row[j] = int(row[j])
        puzzle.append(row)
    puzzleFile.close()

    # display the board
    prettyPrint(puzzle)

    # solve the puzzle
    puzzle2 = makeNewBoard(puzzle)
    solution = solvePuzzle(puzzle2, 0, 0)

    
    # ask the user if they want to play or just solve
    answer = input("Do you want to play the game (p) or just solve the puzzle (s): ")
    if answer == SOLVE:

        # display the solution
        prettyPrint(solution)

    elif answer == PLAY:

        # create a list to track the moves the user makes
        moves = []
        
        # ask if they want correctness checking
        correctCheck = False
        correct = input("Would you like correctness checking (y/n): ")
        if correct == YES:
            correctCheck = True

        end = False
        full = checkBoardFull(puzzle)
        
        # while the board is not full and the user doesn't quit:
        while not full and not end:

            # display the current board
            prettyPrint(puzzle)

            # Present the user with three choices
            options = [PLAY, SAVE, UNDO, QUIT]
            choice = getValidString(options, "play number (p), save (s), undo (u), quit (q): ")
            print()

            if choice == PLAY:

                # if correctness checking is on, send True,
                #    otherwise send False
                if correctCheck:
                    makeMove(puzzle, moves, True, solution)
                else:
                    makeMove(puzzle, moves, False, solution)
                    
            elif choice == SAVE:
                
                fileName = input("Enter the file name you'd like to save to: ")
                savePuzzle(puzzle, fileName)
                
            elif choice == UNDO:

                if len(moves) == 0:
                    print("There are no moves to undo!")

                else:

                    # find the location of the last move
                    row = moves[len(moves) - 1][MOVE_ROW]
                    column = moves[len(moves) - 1][MOVE_COLUMN]

                    # change the place back to empty
                    puzzle[row][column] = 0

                    # remove the move from the list
                    num = moves[len(moves) - 1][MOVE_NUM]
                    msg = "Removed " + str(num) + " you played at position (" \
                        + str(row + 1) + ", " + str(column + 1) + ")."
                    print(msg)
                    moves.remove(moves[len(moves) - 1])
        
            elif choice == QUIT:
                end = True
                print("Good bye! Here is the final board: ")
                
            full = checkBoardFull(puzzle)

        prettyPrint(puzzle)
        if full:

            # check win
            if checkWin(puzzle, solution):
                print("You win!")
            else:
                print("Sorry, you didn't solve it correctly.")
   
main()
