import random


def get_random_choice():
    choices = ['Rock', 'Paper', 'Scissors']
    return random.choice(choices)


class Game:
    def __init__(self, moves):
        self.moves = moves

