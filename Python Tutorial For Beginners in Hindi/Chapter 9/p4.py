listOfWordstoBeCensoredFromAList = []

def askForTheListStr():
    EnterofStrings = ""

    if EnterofStrings != "done":
        list_name = input()
        listOfWordstoBeCensoredFromAList.append(list_name)
    elif EnterofStrings == "done":
        return 



with open("randompara.txt",encoding='utf-8') as Rfile:
    f = Rfile.read()
    askForTheListStr()
    if "Donkey" in f:
        fnew = f.replace(listOfWordstoBeCensoredFromAList,"******")

with open("randompara.txt","w",encoding='utf-8') as Rfile1:
    Rfile1.write(fnew)