list_before_sort = []

mark1 = int(input("Enter the marks of Student No# 1: "))
mark2 = int(input("Enter the marks of Student No# 2: "))
mark3 = int(input("Enter the marks of Student No# 3: "))
mark4 = int(input("Enter the marks of Student No# 4: "))
mark5 = int(input("Enter the marks of Student No# 5: "))
mark6 = int(input("Enter the marks of Student No# 6: "))

list_before_sort = [mark1,mark2,mark3,mark4,mark5,mark6]

print("list before sorting the marks: ", list_before_sort)

list_before_sort.sort()

print("list after sorting the marks: ", list_before_sort)
