a = input()
b = input()
c = []

for i in range(len(a)):
    if b == a[i]:
        c.append(i)

if len(c) == 1:
    print(c[0])
else:
    print(str(c[0]) + " " + str(c[-1]))