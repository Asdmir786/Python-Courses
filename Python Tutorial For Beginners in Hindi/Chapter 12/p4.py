def DividerOfTwoNumbers(a,b):
    try:
        print(a/b)
    except ZeroDivisionError:
        print("You can't divide with zero")
    except:
        print("awdeawed")

a = int(input("Number1: "))
b = int(input("Number2: "))

DividerOfTwoNumbers(a,b)
    
    