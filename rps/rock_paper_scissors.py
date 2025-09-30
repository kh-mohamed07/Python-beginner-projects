import random 

def is_win(player_choice,opponent_choice):
    if (player_choice =='s' and opponent_choice=='p') or (player_choice =='p' and opponent_choice=='r') or (player_choice =='r' and opponent_choice=='s'):
        return True
def play(user_choice,computer_choice):
    if user_choice==computer_choice:
        return 'draw'
    elif is_win(user_choice,computer_choice):
        return 'UserWin'
    return 'UserLose'



max_points=int(input('Enter the point needed to Win :  '))
user_points=0
computer_points=0
user_rounds=0
computer_rounds=0
options_map={'r':'rock' , 'p':'paper' , 's':'scissors'}
repeat='yes'

while repeat=='yes':
    while user_points != max_points and computer_points != max_points:
        user_choice=input('Type your move ("r" for rock, "p" for paper, "s" for scissors): ').lower()
        if user_choice not in options_map:
            print('Input Error !! ')
            continue
        computer_choice=random.choice(['r','p','s'])
        result=play(user_choice,computer_choice)
        if result=='draw':
            print(f"the computer choice was {options_map[computer_choice]} so it's a  Draw") 
        elif result=='UserLose':
            print(f"the computer choice was {options_map[computer_choice]} so you lose this point")
            computer_points+=1
        elif result=='UserWin':
            print(f"the computer choice was {options_map[computer_choice]} so you win this point")
            user_points+=1
        print(f'current score : You({user_points}) - computer({computer_points})')
    print('Game over')
    if user_points>computer_points:
        print('Congrats!! you are the winner')
        user_rounds+=1
    else:
        print('You lose the Game , Hard luck')
        computer_rounds+=1
    print(f'Wins: You: {user_rounds}   ---  Computer: {computer_rounds} ')
    repeat=input('do u want to play another round?? (Yes or No) : ').lower()