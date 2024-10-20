n1 = input("Enter Number 1: ")
n2 = input("Enter Number 2: ")
n3 = input("Enter Number 3: ")
n4 = input("Enter Number 4: ")

if n1 > n2 and n1 > n3 and n1 > n4:
    print(f"{n1} is the greatest number")

if n2 > n1 and n2 > n3 and n2 > n4:
    print(f"{n2} is the greatest number")

if n3 > n1 and n3 > n2 and n3 > n4:
    print(f"{n3} is the greatest number")

if n4 > n1 and n4 > n2 and n4 > n3:
    print(f"{n4} is the greatest number")