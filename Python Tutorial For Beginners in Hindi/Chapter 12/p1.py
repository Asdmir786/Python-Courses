
try:
    with (
        open("1.txt") as f1,
        open("2.txt") as f2,
        open("3.txt") as f3,
    ):
        f1.read()
except FileNotFoundError:
    print("There ain't no files.")
except:
    print(" mh")
else: 
    print("There are the files that you gave")