import time
from Player import RandomComputerPlayer,HumanPlayer,SmartComputerPlayer


class TicTacToe:
    def __init__(self) :
        self.board = [" " for _ in range(9)]
        self.current_winner = None
    
    def print_board(self):
        for row in [self.board[i*3 : (i+1)*3] for i in range(3)]:
            print("| " + " | ".join(row)+" |")
    
    @staticmethod
    def show_board_nums():
        number_board=[[str(i) for i in range(j*3,(j+1)*3)] for j in range(3)]
        for row in number_board:
            print("| "+" | ".join(row)+" |")
    
    def available_moves(self):
        return [i for i in range(9) if self.board[i] == " "  ]
    
    def make_move(self,spot,player):
        if self.board[spot]==' ':
            self.board[spot]=player
            if self.winner(spot,player):
                self.current_winner=player
            return True 
        return False
    
    def winner(self,spot,player):
        #check row 
        row_ind=spot//3
        row=self.board[row_ind*3:(row_ind+1)*3]
        if all(i==player for i in row):
            return True 
        
        #check columns
        col_ind=spot%3
        col=[self.board[col_ind + i*3] for i in range(3)]
        if all(i==player for i in col):
            return True 
        
        #check diagonals
        if spot%2 == 0 : #seulement les nombres pairs peuvent se trouver en un diagonal 
            diagonal1=[self.board[i] for i in [0,4,8]]
            diagonal2=[self.board[i] for i in [2,4,6]]
            if all(i==player for i in diagonal1) or all(i==player for i in diagonal2 ):
                return True 
        
        return False 

def play(game, x_player, o_player, print_game=True):
    if print_game : 
        game.show_board_nums()
    player='X'
    while len(game.available_moves()) > 0:
        if player=='X':
            spot = x_player.get_move(game)
        else:
            spot = o_player.get_move(game)

        if game.make_move(spot,player):
            if print_game:
                print(player + f'makes a move to {spot}')
                game.print_board()
                print('*' * 15)
            if game.current_winner:
                if print_game:
                    print(f'player {player} wins !!')
                return player
            player='O' if player=='X' else 'X'
        # a small break to improve readability 
        time.sleep(1)
    if print_game:
        print('It\'s a tie!')



# The Tic Tac Toe game menu
play_again='yes'
while play_again=='yes':
    print('Welcome to Tic Tac Toe')
    print('game modes : \n1. Human vs Human \n2. Human vs Computer(easy mode) \n3.Human vs Computer(hard mode)  \n4. Computer vs Computer')
    mode=input('Choose a game mode (1-4): ')

    if mode=='1' : 
        x_player=HumanPlayer('X')
        o_player=HumanPlayer('O')
        game=TicTacToe()
        play(game,x_player,o_player,print_game=True)

    elif mode=='2' : 
        while True :
            try:
                human_letter=input('choose your letter (X or O) : ').strip().lower()
                if human_letter not in ['x','o']:
                    raise ValueError
                break
            except ValueError:
                print('invalid input , u should choose between X and O')
        if human_letter=='x':
            x_player=HumanPlayer('X')
            o_player=RandomComputerPlayer('O')

        else:
            x_player=RandomComputerPlayer('X')
            o_player=HumanPlayer('O')

        game=TicTacToe()
        play(game,x_player,o_player,print_game=True)


    elif mode=='3':
        while True :
            try:
                human_letter=input('choose ur letter (X or O) : ').strip().lower()
                if human_letter.lower() not in ['x','o']:
                    raise ValueError
                break
            except ValueError:
                print('Invalid Input, try again!!')
        if human_letter.lower()=='x':
            x_player=HumanPlayer('X')
            o_player=SmartComputerPlayer('O')
        else:
            x_player=SmartComputerPlayer('X')
            o_player=HumanPlayer('O')
        
        game = TicTacToe()
        play(game,x_player,o_player,print_game=True)


    elif mode=='4':
        x_wins=0
        o_wins=0
        ties=0
        for _ in range(100):
            x_player=SmartComputerPlayer('X')
            o_player=SmartComputerPlayer('O')
            game=TicTacToe()
            result=play(game,x_player,o_player,print_game=False)
            if result=='X':
                x_wins+=1
            elif result=='O':
                o_wins+=1
            else:
                ties+=1

        print(f'X wins = {x_wins}, O wins = {o_wins} , and ties={ties} ')
    
    else: 
        print('invalid input , choose from the available modes, Try again!!')

    while True:
        play_again=input('do u want to play again?? (yes or no) : ').strip().lower()
        if play_again in ['yes','no']:
            break
        print('invalid input , please choose yes or no')
  

