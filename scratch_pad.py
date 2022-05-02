import random

import random


moves = ['rock', 'paper', 'scissors']


def computer_action(moves):
    computer_action = random.choice(moves)
    if computer_action == 'rock':
        print ('rock')
    if computer_action == 'paper':
        print ('paper')
    if computer_action == 'scissors':
        print ('scissors')

# computer_action(moves)


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))

beats(one, two)