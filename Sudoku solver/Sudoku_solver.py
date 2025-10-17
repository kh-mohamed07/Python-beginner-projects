def find_next_emty(puzzle):
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1 :
                return r,c
    return None,None


def is_valid(puzzle,guess,row,col):
    for r in range(9):
        if puzzle[r][col]==guess:
            return False
    for c in range(9):
        if puzzle[row][c]==guess:
            return False 
    
    row_start=(row//3)*3
    col_start=(col//3)*3

    for r in range(row_start,row_start+3):
        for c in range(col_start,col_start+3):
            if puzzle[r][c]==guess:
                return False
    
    return True



def solve_sudoku(puzzle):
    row,col = find_next_emty(puzzle)
    if row == None :  # we need only to check col or row , because if one of them is None --> the other also 
        return True 
    
    for guess in range(1,10):
        if is_valid(puzzle,guess,row,col):
            puzzle[row][col]=guess
            if solve_sudoku(puzzle):
                return True


    

            

 

