import random

class Board :
    def __init__(self,dim_size,num_bombs):
        self.dim_size=dim_size
        self.num_bombs=num_bombs
        self.board=self.make_board()
        self.assign_values_to_board()
        self.dug=set()
    
    def make_board(self):
        board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        bombs_planted=0
        while bombs_planted<self.num_bombs:
            row = random.randint(0 , self.dim_size - 1)
            col = random.randint(0 , self.dim_size - 1)
            if board[row][col] == '*':
                continue

            board[row][col] = '*'
            bombs_planted += 1
            
        return board 
    
    def assign_values_to_board(self):
        for r in range(self.dim_size):
            for c in range(self.dim_size):
                if self.board[r][c] == '*':
                    continue 
                self.board[r][c] = self.get_num_neighboring_bombs(r,c)
    
    def get_num_neighboring_bombs(self,row,col):
        num=0
        for r in range(row-1,row+2):
            for c in range(col-1,col+2):
                if r<0 or r>=self.dim_size or c<0 or c>=self.dim_size:
                    continue
                if self.board[r][c]=='*':
                    num+=1
        return num 

    def dig(self,row,col):
        self.dug.add((row,col))
        if self.board[row][col]=='*':
            return False
        elif self.board[row][col] > 0:
            return True 
        # the only left case is self.board[row][col] == 0
        for r in range(row-1,row+2):
            for c in range(col-1,col+2):
                if r<0 or r>=self.dim_size or c<0 or c>=self.dim_size:
                    continue
                if (r,c) in self.dug:
                    continue 
                self.dig(r,c)
        return True

        


def play(dim_size=10 , num_bombs=10):
    board = Board(dim_size , num_bombs)

    
    