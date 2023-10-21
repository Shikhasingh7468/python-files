from Game import Game

class User:
    choice = ''
    score = 0
    def __init__(self,name):
        self.name = name;

    @staticmethod
    def setChoice():
        num = int(input("Enter number (0,1,2):"))
        if num == 0:
            User.choice = Game.ROCK
        elif num == 1:
            User.choice = Game.PAPER
        elif num == 2:
            User.choice = Game.SCISSOR
        else:
            pass

    def getChoice():
        return User.choice
    
    def increment_score():
        User.score = User.score + 2