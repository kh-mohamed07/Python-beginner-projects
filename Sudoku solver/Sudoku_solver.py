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
        puzzle[row][col]=-1
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
print(board)
    

            

 

