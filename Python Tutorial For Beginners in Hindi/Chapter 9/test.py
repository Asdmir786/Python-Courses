stri = "Afeef Kela Khata Rehta hai"

f = open("kela.txt","w")
g = open("kela.txt")
f.write("Afeef Kela Khata Rehta hai")

print(g.read())
f.close()
g.close()