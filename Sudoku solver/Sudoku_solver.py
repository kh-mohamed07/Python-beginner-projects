def find_next_emty(puzzle):
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1 : # empty cells are marked as -1
                return r,c
    return None,None  # if there is no remaining emty cells


def is_valid(puzzle,guess,row,col):
    for r in range(9):
        if puzzle[r][col]==guess: # if the guessed number already exist in the same column 
            return False
    for c in range(9):
        if puzzle[row][c]==guess: # if the guessed number already exist in the same row 
            return False 
    
    # determine 3x3 box
    row_start=(row//3)*3
    col_start=(col//3)*3

    # Check if the guess is valid in the 3x3 box
    for r in range(row_start,row_start+3): 
        for c in range(col_start,col_start+3): 
            if puzzle[r][c]==guess: # if the guessed number already exist in the same 3x3 box
                return False
    
    return True # the guess is valid 



def solve_sudoku(puzzle):
    row,col = find_next_emty(puzzle)
    if row == None :  # if puzzle is complete & we need only to check col or row , because if one of them is None --> the other also 
        return True 
    # try all possible guesses (from 0 to 9)
    for guess in range(1,10): 
        if is_valid(puzzle,guess,row,col):
            puzzle[row][col]=guess
            if solve_sudoku(puzzle): # recursively solve the rest
                return True
        puzzle[row][col]=-1 # backtrack if the guess is not valid 

    return False 


board= [[5,3,-1,-1,7,-1,-1,-1,-1],
    [6,-1,-1,1,9,5,-1,-1,-1],
    [-1,9,8,-1,-1,-1,-1,6,-1],
    [8,-1,-1,-1,6,-1,-1,-1,3],
    [4,-1,-1,8,-1,3,-1,-1,1],
    [7,-1,-1,-1,2,-1,-1,-1,6],
    [-1,6,-1,-1,-1,-1,2,8,-1],
    [-1,-1,-1,4,1,9,-1,-1,5],
    [-1,-1,-1,-1,8,-1,-1,7,9]]

solve_sudoku(board)
for row in board:
    print(row)    

            

 

