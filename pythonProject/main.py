from PyQt5.QtWidgets import *
from PyQt5 import uic
import random

class MyGUI(QMainWindow):
    def __init__(self):
        super(MyGUI,self).__init__()
        uic.loadUi("gui.ui",self)

        self.show()

        # self.playbtn.clicked.connect(get_random_choice())
def main():
    app = QApplication([])
    window = MyGUI()
    app.exec()

    moves = 5
    score = 0
    for i in range(moves):
        moves = moves + 1
        user_choice = get_random_choice()
        computer_choice = get_random_choice()

        if user_choice == computer_choice:
            # It's a tie
            print("It's a tie!")
        elif (user_choice == 'Rock' and computer_choice == 'Scissors') or \
                (user_choice == 'Paper' and computer_choice == 'Rock') or \
                (user_choice == 'Scissors' and computer_choice == 'Paper'):
            # User wins
            score = score + 5
        else:
            print("Computer wins")
            # Computer wins



def get_random_choice():
    choices = ['Rock', 'Paper', 'Scissors']
    return random.choice(choices)

if __name__ == "__main__":
    main()
