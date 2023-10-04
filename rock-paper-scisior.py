import random

options = ("rock", "paper", "scissor")
wining_time = 0

while True:
    opponent = random.choice(options) 
    your_turn = input("Rock, Paper, Scissors (q to quit): ").lower()

    if your_turn == "q":
        break

    if your_turn in options:
        print(f"Opponent chooses {opponent}")

        if opponent == your_turn:
            print("It's a tie")
        elif (opponent == "rock" and your_turn == "scissor") or \
             (opponent == "scissor" and your_turn == "paper") or \
             (opponent == "paper" and your_turn == "rock"):
            print("You lose")
        else:
            print("You win")
            wining_time += 1
    else:
        print("This is not a valid option")

print(f"You win {wining_time} times.")
