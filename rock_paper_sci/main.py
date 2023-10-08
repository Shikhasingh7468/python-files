from User import User
from Computer import Computer
from Game import Game

def main():
    print("Let's play Rock-Paper-Scissors!")
    moves = 0
    while(moves <3):
        User.setChoice()
        Computer.setChoice()
        Game.status(User.getChoice(),Computer.getChoice())
        number = Game.determine_winner(User.getChoice(), Computer.getChoice())
        if number == 0:
            Computer.increment_score()
        elif number == 1:
            User.increment_score()
        else:
            pass
        print(Game.getMessage())
        moves = moves + 1
    print("-------Game Over-------")
    print("User score:"+str(User.score)+ " Computer Score:"+str(Computer.score))

if __name__ == "__main__":
    main()
