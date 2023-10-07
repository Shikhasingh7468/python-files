import random
from Game import Game


class Computer:
    choice = ""
    score = 0

    @staticmethod
    def setChoice():
        num = random.randint(0, 2)
        if num == 0:
            Computer.choice = Game.ROCK
        elif num == 1:
            Computer.choice = Game.PAPER
        else:
            Computer.choice = Game.SCISSOR

    def getChoice():
        return Computer.choice

    def increment_score():
        Computer.score = Computer.score + 2