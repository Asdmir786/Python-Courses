def MultiplicationTableOfAnyNumber(NumberToMultiply, NumberToHowManyTimesToMultiply):
    for i in range(1, NumberToHowManyTimesToMultiply+1):
        print(f"{NumberToMultiply} x {i} =", NumberToMultiply*i)

a = int(input("Gimme a number to multiply: "))
b = int(input("How many Times: "))

MultiplicationTableOfAnyNumber(a,b)