import random
#!/usr/bin/env python3

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']
scores = 0

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def move(self):
        pass

    def learn(self, my_move, their_move):
        pass
    
def valid_input(prompt, options):
    while True:
        option = input(prompt).lower()
        if option in options:
            return option
        print(f'Sorry, the option "{option}" is invalid. Try again!')

        
def computer_action(moves):
    computer_action = random.choice(moves)
    if computer_action == 'rock':
        return 'rock'
    if computer_action == 'paper':
        return 'paper'
    if computer_action == 'scissors':
        return 'scissors'
    return
    
    
def human_action(moves):
    choice = valid_input("Please choose from the following options: rock, paper, or scissors\n", ['rock', 'paper', 'scissors'])
    if choice == 'rock':
        return 'rock'
    if choice == 'paper':
        return 'paper'
    elif choice == 'scissors':
        return 'scissors'
    return
    
    
class RandomPlayer(Player):
    def __init__(self):
        super().__init__()
    def move(self, moves):
        return computer_action(moves)
    
    
class HumanPlayer(Player):
    def __init__(self):
        super().__init__()
    def move(self, moves):
        return human_action(moves)
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
        score1 = self.p1.score(scores)
        score2 = self.p2.score(scores)
        move1 = self.p1.move(moves)
        move2 = self.p2.move(moves)
        print(f"Player 1: {move1}  Player 2: {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        if beats(move1, move2):
            print("Player 1 wins!")
            score1 = score1 + 1
        if beats(move2, move1):
            print("Player 2 wins!")
            score2 = score2 +1
        elif move1 == move2:
            print("TIE!")
        print(f"Player 1 score: {score1}  Player 2 score: {score2}")


    def play_game(self):
        print("Game start!")
        for round in range(3):
            print(f"Round {round}:")
            self.play_round()
        # if score1 > score2:
        #     print("Player 1 wins the game!")
        # if score2 > score1:
        #     print("Player 2 wins the game!")
        # elif score1 == score2:
        #     print("Game is TIE!")
        print("Game over!")


if __name__ == '__main__':
    game = Game(HumanPlayer(), RandomPlayer())
    game.play_game()

