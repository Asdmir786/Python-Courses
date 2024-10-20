def Converter(Number_In_Celsius):
    result = Number_In_Celsius*(9/5)+32
    print(f"You answer is {result} Degree Fahrenheit")

a = int(input("Gimme a temp in Celsius: "))

Converter(a)