import random
def game():
    # Variables
    gameOver = False
    lot = ["rock", "paper", "scissor"]
    userwin = False
    compwin = False
   
    # Logic

    while gameOver != True: #
        comp = random.choice(lot)
        print("Lets play a game.")
        print("Rock Paper Scissor: ")
        a = input().lower()
        # User win  logic
        if a == lot[0] and comp == lot[2]:
            print(f"You win because {a} beats {comp}. ")
            gameOver = True
        elif a == lot[1] and comp == lot[0]:
            print(f"You win because {a} beats {comp}. ")
            gameOver = True
        elif a == lot[2] and comp == lot[1]:
            print(f"You win because {a} beats {comp}. ")
            gameOver = True
        # User Lose Logic
        elif a == lot[0] and comp == lot[1]:
            print(f"You lose because {a} beats {comp}. ")
            gameOver = True
        elif a == lot[1] and comp == lot[2]:
            print(f"You lose because {a} beats {comp}. ")
            gameOver = True
        elif a == lot[2] and comp == lot[0]:
            print(f"You lose because {a} beats {comp}. ")
            gameOver = True
        # Draw Logic
        if a == comp:
            print(f"Since both, {a} and {comp} are same, it's a draw.")
            gameOver = True
game()