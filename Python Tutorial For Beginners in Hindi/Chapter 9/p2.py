import random

# Global variable for score
Score = 0

def game():
    global Score  # Declare Score as global to modify it
    gameOver = False
    lot = ["rock", "paper", "scissor"]
    
    while not gameOver:  # Game loop
        comp = random.choice(lot)
        print("Let's play a game.")
        print("Rock Paper Scissor: ")
        a = input().lower()
        
        # User win logic
        if a == lot[0] and comp == lot[2]:
            print(f"You win because {a} beats {comp}.")
            Score += 1
        elif a == lot[1] and comp == lot[0]:
            print(f"You win because {a} beats {comp}.")
            Score += 1
        elif a == lot[2] and comp == lot[1]:
            print(f"You win because {a} beats {comp}.")
            Score += 1
        # User lose logic
        elif a == lot[0] and comp == lot[1]:
            print(f"You lose because {a} loses to {comp}.")
            Score -= 1
        elif a == lot[1] and comp == lot[2]:
            print(f"You lose because {a} loses to {comp}.")
            Score -= 1
        elif a == lot[2] and comp == lot[0]:
            print(f"You lose because {a} loses to {comp}.")
            Score -= 1
        # Draw logic
        elif a == comp:
            print(f"Since both, {a} and {comp} are the same, it's a draw.")
        
        # End the game after one round; you can change this to allow for more rounds.
        gameOver = True

# Start the game
game()

# Write score to a file
with open("score points.txt", "w") as file:
    file.write(f"Your Score is {Score}\n")  # Write the score as a string
