class Game:
    ROCK = "Rock"
    PAPER = "Paper"
    SCISSOR = "Scissors"
    MESSAGE = ""

    @staticmethod
    def determine_winner(user_choice, computer_choice):
        if user_choice == computer_choice:
            Game.MESSAGE = "It's a tie!"
            return -1
        elif (
            (user_choice == Game.ROCK and computer_choice == Game.SCISSOR)
            or (user_choice == Game.PAPER and computer_choice == Game.ROCK)
            or (user_choice == Game.SCISSOR and computer_choice == Game.PAPER)
        ):
            Game.MESSAGE = "You win!"
            return 1
        else:
            Game.MESSAGE = "Computer wins!"
            return 0

    @staticmethod
    def getMessage():
        return Game.MESSAGE

    @staticmethod
    def status(userChoice, computerChoice):
        print("User choice: " + userChoice + " Computer Choice: " + computerChoice)

