import math
class Calculator:
    number = 0
    OP = ""
    def sq(self, number):
        print(f"The Square of {number} is {number*number}") 
    def sqrt(self,number):
        print(f"The Square Root of {number} is {math.sqrt(number)}") 
    def cb(self, number):
        print(f"The Cube of {number} is {number * number * number}") 
    def cbrt(self, number):
        print(f"The Cube Root of {number} is {math.cbrt(number)}")
    def CheckingAnswer(self,koiSaString,number):
        if koiSaString == "sq":
            self.sq(number)
        elif koiSaString == "sqrt":
            self.sqrt(number)
        elif koiSaString == "cb":
            self.cb(number)
        elif koiSaString == "cbrt":
            self.cbrt(number)
    def __init__(self):
        print("Enter a number.")
        self.number = int(input(": "))
        print("What Do you want to do?")
        print("1. Square (sq)")
        print("1. Square Root (sqrt)")
        print("1. Cube (cb)")
        print("1. Cube Root (cbrt)")
        self.OP = input(": ")
        self.CheckingAnswer(self.OP,self.number)



Calculator()