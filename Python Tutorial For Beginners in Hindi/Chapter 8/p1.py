def bignombah(n1, n2, n3):
    if n1 > n2 and n1 > 3:
        print(f"{n1} is the bigest number.")
    elif n2 > n1 and n2 > n3:
        print(f"{n2} is the bigest number.")
    elif n3 > n1 and n3 > n2:
        print(f"{n3} is the bigest number.")

n1 = int(input("Gimme a numbah1: "))
n2 = int(input("Gimme a numbah2: "))
n3 = int(input("Gimme a numbah3: "))

bignombah(n1,n2,n3)