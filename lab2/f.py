n = int(input())
students = {}

for i in range(n):
    faml, money = input().split()
    if faml in students:
        students[faml] = int(students[faml]) + int(money)
    else:
        students[faml] = int(money)

names = sorted(students.keys())
maximum = max(students.values())

for j in names:
    if students[j] == maximum:
        print(j, " is lucky!")
    else:
        print(j, " has to receive ", maximum - int(students[j]), " tenge")