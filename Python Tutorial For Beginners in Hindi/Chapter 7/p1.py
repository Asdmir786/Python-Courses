number_for_multiplication_till_10 = int(input("Enter any Number I will give you its multiplication table till you want becuz I am Inevetible: "))
number_for_table = int(input("GImme a number on how much till multiply, 10, 20, 30, what?: "))

for one_to_ten in range(1,(number_for_table+1)):
    print(number_for_multiplication_till_10, "x", one_to_ten, "=", number_for_multiplication_till_10*one_to_ten)