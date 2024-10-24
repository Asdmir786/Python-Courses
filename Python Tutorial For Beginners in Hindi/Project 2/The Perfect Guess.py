import random

class GuessTheNumber:
    random_Number = 0
    user_input = 0
    lives = 3
    def RandomMaker(self):
        self.random_Number = random.randint(1, 100)
    def __init__(self):
        print("Welcome to Guess the Numbah")
        print('''A Number will be given from 1 to 100, try to guess, 
              if your guess is lower then the program will tell, if
              higher then same thing.Remember only 3 lives.''')
        print("Generating a random Number...")
        self.RandomMaker()
        print("Random Number has been generated. ")
        while self.lives != 0:
            # self.user_input = int(input(f"Enter a Number to guess.\n:({self.random_Number})"))
            self.user_input = int(input("Enter a Number to guess.\n:"))
            if self.user_input == self.random_Number:
                print(f"You have guessed the number, it was {self.random_Number} and you guessed with {self.lives} live(s) left.")
                break
            elif self.user_input > self.random_Number:
                self.lives -= 1
                print(f"The number was too high try again. ({self.lives} left)")
            elif self.user_input < self.random_Number:
                self.lives -= 1
                print(f"The number was too low try again. ({self.lives} left)")
            
            if self.lives == 0:
                print(f"Ah Shucks, You lost, No lives are left and the number was {self.random_Number}.")

o = GuessTheNumber()

