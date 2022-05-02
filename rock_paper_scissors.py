import random
#!/usr/bin/env python3

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']


"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def move(self):
        pass

    def learn(self, my_move, their_move):
        pass

def computer_action(moves):
    computer_action = random.choice(moves)
    if computer_action == 'rock':
        return 'rock'
    if computer_action == 'paper':
        return 'paper'
    if computer_action == 'scissors':
        return 'scissors'
    return
    
    
class RandomPlayer(Player):
    def __init__(self):
        super().__init__()
    def move(self, moves):
        return computer_action(moves)
    def point(self, one, two):
        return beats(one, two)

    
def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        move1 = self.p1.move(moves)
        move2 = self.p2.move(moves)
        print(f"Player 1: {move1}  Player 2: {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        if move1 == move2:
            print("TIE!")
        
    def keep_score(self):
        one = self.p1.move(moves)
        two = self.p2.move(moves)
        # beats(one, two)
        if beats(one, two):
            print("P1 wins!")
            p1_count = 0
            p2_count = 0
            p1_count += 1
            print(p1_count)

    def play_game(self):
        print("Game start!")
        for round in range(3):
            print(f"Round {round}:")
            self.play_round()
            self.keep_score()
        print("Game over!")


if __name__ == '__main__':
    game = Game(RandomPlayer(), RandomPlayer())
    game.play_game()



# 3. Keep score
# The starter Game class does not keep score. It doesn't even notice which player won each round. Update the Game class so that it displays the outcome of each round, and keeps score for both players. You can use the provided beats function, which tells whether one move beats another one.

# Make sure to handle ties — when both players make the same move!