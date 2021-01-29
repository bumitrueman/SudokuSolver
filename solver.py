# Credits
# Thanks to Tech With Tim for the code tutorial.


# Display the puzzle
def displayPuzzle(puzzle):
    for r in range(len(puzzle)):
        if r % 3 == 0 and r != 0:
            print('---------------------')

        for c in range(len(puzzle[0])):
            if c % 3 == 0 and c != 0:
                print('| ', end='')
            
            if c == len(puzzle[0])-1:
                print(puzzle[r][c])
            else:
                print(puzzle[r][c], end=' ')


# Find the empty spaces in the puzzle
def findEmptySpaces(puzzle):
    for r in range(len(puzzle)):
        for c in range(len(puzzle[0])):
            if puzzle[r][c] == 0:
                return (r, c)
    return None


# validate the guess input
def checkGuess(puzzle, guess, pos):
    r, c = pos

    # check if the same number exist in the row.
    for num in range(len(puzzle)):
        if puzzle[num][c] == guess and num != r:
            return False
    
    # check if the same number exist in the column.
    for num in range(len(puzzle[0])):
        if puzzle[r][num] == guess and num != c:
            return False

    # check if the same number exist in the sub-box
    rBox = (r // 3) * 3
    cBox = (c // 3) * 3
    for r_bx in range(rBox, rBox + 3):
        for c_bx in range(cBox, cBox + 3):
            if puzzle[r_bx][c_bx] == guess:
                return False

    return True


# main function to solve the puzzle
def solvePuzzle(puzzle):
    # 1. Find the empty spaces.
    pos = findEmptySpaces(puzzle)

    if pos is None:
        return True
    else:
        # Guess Number.
        for guess in range(1, 10):
            if checkGuess(puzzle, guess, pos):
                # update the puzzle
                r, c = pos
                puzzle[r][c] = guess

                # call solver again
                if solvePuzzle(puzzle):
                    return True
                else:
                    # reset puzzle guess 
                    puzzle[r][c] = 0
                
    return False



if __name__ == '__main__':
        
    puzzle = [
        [0,0,0,0,0,0,1,8,2],
        [1,0,6,2,0,5,9,0,4],
        [0,4,2,0,0,0,5,0,7],
        [6,0,4,1,0,0,8,0,0],
        [0,2,0,6,5,3,7,0,1],
        [7,1,0,0,8,9,0,0,6],
        [0,0,9,0,0,0,0,1,0],
        [0,0,0,0,0,0,6,0,3],
        [0,0,0,0,9,1,0,0,0]
    ]

    ans = [
        [5,9,7,3,6,4,1,8,2],
        [1,8,6,2,7,5,9,3,4],
        [3,4,2,9,1,8,5,6,7],
        [6,3,4,1,2,7,8,5,9],
        [9,2,8,6,5,3,7,4,1],
        [7,1,5,4,8,9,3,2,6],
        [2,7,9,5,3,6,4,1,8],
        [8,5,1,7,4,2,6,9,3],
        [4,6,3,8,9,1,2,7,5]
    ]



    print('############# Puzzle #############')
    displayPuzzle(puzzle)
    print(''*5)

    print('############# Solver #############')
    solvePuzzle(puzzle)
    displayPuzzle(puzzle)
    print(''*5)

    print('############# Ans #############')
    displayPuzzle(ans)