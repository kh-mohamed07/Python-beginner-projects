def print_board(board):
    for row in [board[i*3:(i+1)*3] for i in range(3)]:
        print("| " + " | ".join(row) + " |")

def check_winner(board,player):
    #check rows
    for i in range(0,9,3):
        if board[i]==board[i+1]==board[i+2]==player:
            return True

    #check columns
    for i in range(3):
        if board[i]==board[i+3]==board[i+6]==player:
            return True
        
    #check diagonals
    if board[0]==board[4]==board[8]==player or board[2]==board[4]==board[6]==player :
        return True
    
    return False
    
def game():
    board=[" " for _ in range(9)]
    current_player='X'
    while " " in board:
        print_board(board)
        while True:
            try:
                move=int(input(f'Player {current_player}, choose a spot (0-8)'))
                if move not in range(9):
                    print('Please enter a number between 0 and 8')
                    continue
                if board[move] != " ":
                    print('this spot is already taken, Try again!!')
                    continue
                break
            except ValueError:
                 print("Invalid input! Please enter a number from 0 to 8.")

        board[move]=current_player

        if check_winner(board,current_player):
            print_board(board)
            print(f'The Winner is : {current_player}')
            return
        current_player='O' if current_player=='X' else 'X'
    
    print_board(board)
    print("It's a tie!!")

game()
