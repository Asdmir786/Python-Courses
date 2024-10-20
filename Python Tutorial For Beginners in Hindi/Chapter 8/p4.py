# Write a recursive function to calculate the sum of first n natural numbers.

def NaturalNumberCalculator(naturalNumber):
        if naturalNumber==1:
            return 1
        return NaturalNumberCalculator(naturalNumber-1) + naturalNumber

print (NaturalNumberCalculator(4))