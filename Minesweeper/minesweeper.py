import random
import re 

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

    def __str__(self):
        visible_board=[]
        for r in range(self.dim_size):
            visible_row=[]
            for c in range(self.dim_size):
                if (r,c) in self.dug : 
                    visible_row.append(str(self.board[r][c]))
                else:
                    visible_row.append('_')

            visible_board.append(visible_row)
        
        str_rep = '    ' + ' | '.join([str(c) for c in range(self.dim_size)]) + '\n'
        str_rep+='-'*self.dim_size*4 + '\n'

        for i,row in enumerate(visible_board):
            str_rep += str(i) + ' | ' + ' | '.join(row) + '\n'

        return str_rep


def play(dim_size=10 , num_bombs=10):
    board = Board(dim_size , num_bombs)
    while len(board.dug) < dim_size**2 - num_bombs :
        print(board)
        user_input=re.split(r'[,\s]+',input('where would u like to dig? (row,col): '))
        try:
            if len(user_input) != 2 :
                raise ValueError
            row,col=int(user_input[0]),int(user_input[-1])
            if row >= dim_size or row<0 or  col>=dim_size or col<0 :
                raise ValueError
        except ValueError:
            print('please enter valid numbers')
            continue
        
        safe=board.dig(row,col)
        if not safe: 
            break 

    if safe:
        print('CONGRATULATIONS!! YOU WON ')
    else:
        print('GAME OVER !! you lost :( ')
        board.dug={(r,c) for r in range(dim_size) for c in range(dim_size)}
        print(board)

if __name__=='__main__':
    print('there are 10 bombs , be careful :) ')
    play_again='yes'
    while play_again=='yes':
        play()
        while True:
            play_again=input('do u want to play again?? (yes or no)').strip().lower()
            if play_again in ['yes','no']:
                break
            else:
                print('please enter yes or no ')








    
    