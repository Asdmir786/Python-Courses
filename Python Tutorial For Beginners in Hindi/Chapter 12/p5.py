number = int(input("Gimme a Number and I will give you a list of it from 1 to 10\n: "))

listah = []

for i in range(1,11):
    tempvar = number*i
    listah.append(tempvar)

print(listah)
with open("Tables.txt","a") as faluda:
    faluda.write(str(listah) + "\n")
