import random

class Player : 
    def __init__(self,player):
        # player is x or o 
        self.player=player
    def get_move(self,game):
        raise NotImplementedError("Subclasses must implement get_move()")
    
class RandomComputerPlayer(Player):
    def __init__(self,player):
        super().__init__(player)

    def get_move(self,game):
        spot = random.choice(game.available_moves())
        return spot
    

class HumanPlayer(Player):
    def __init__(self,player):
        super().__init__(player)

    def get_move(self,game):
        while True:
            try:
                spot=int(input(f"{self.player}'s turn.Choose ur next move (0-8) : "))
                if spot not in game.available_moves():
                    raise ValueError
                break
            except ValueError:
                print('Invalid Input , Try Again!!')
        return spot 


class SmartComputerPlayer(Player):
    def __init__(self,player):
        super().__init__(player)
    
    def get_move(self, game):
        if len(game.available_moves())==9:
            spot=random.choice(game.available_moves())
        else:
            spot=self.minimax(game,self.player)['position']
        
        return spot 

    def minimax(self,state,player):
        max_player= self.player 
        other_player= 'O' if player=='X' else 'X'
        if state.current_winner==other_player:
            return {'position': None , 'score': len(state.available_moves())+1} if other_player==max_player else {'position': None , 'score': -len(state.available_moves())-1}
        elif len(state.available_moves())==0:
            return {'position': None , 'score': 0}
        
        if player==max_player:
            best={'position': None , 'score': float('-inf')}
        else: 
            best={'position': None , 'score': float('inf')}

        for possible_move in state.available_moves():
            state.make_move(possible_move,player)
            sim_score=self.minimax(state,other_player)
            state.board[possible_move]=' '
            state.current_winner=None
            sim_score['position']=possible_move

            if player==max_player:
                if sim_score['score']>best['score']:
                    best=sim_score
            else:
                if sim_score['score']<best['score']:
                    best=sim_score

        return best 



        

        
        




        


