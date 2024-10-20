import random

ListOfTheThings = ["snake","water","gun"]

UserInput = input("Enter your word: ").lower()

Computer = random.choice(ListOfTheThings)

if Computer == UserInput:
    print(f"You({UserInput}) and the Computer({Computer}) choose the same answer, it's a draw. ")

elif UserInput == ListOfTheThings[0] and Computer == ListOfTheThings[1]:
    print(f"{ListOfTheThings[0]} beats {ListOfTheThings[1]}, you won!")
elif UserInput == ListOfTheThings[1] and Computer == ListOfTheThings[2]:
    print(f"{ListOfTheThings[1]} beats {ListOfTheThings[2]}, you won!")
elif UserInput == ListOfTheThings[2] and Computer == ListOfTheThings[0]:
    print(f"{ListOfTheThings[2]} beats {ListOfTheThings[0]}, you won!")

elif UserInput == ListOfTheThings[0] and Computer == ListOfTheThings[2]:
    print(f"{ListOfTheThings[2]} beats {ListOfTheThings[0]}, you lost!")
elif UserInput == ListOfTheThings[1] and Computer == ListOfTheThings[0]:
    print(f"{ListOfTheThings[0]} beats {ListOfTheThings[1]}, you lost!")
elif UserInput == ListOfTheThings[2] and Computer == ListOfTheThings[1]:
    print(f"{ListOfTheThings[1]} beats {ListOfTheThings[2]}, you lost!")
else:
    print("Either write snake,water, or gun. OR CRY ME A RIVER. ")

print("If you want to play again rerun the program because once a wise man said: 'Program to wrr gia'.")