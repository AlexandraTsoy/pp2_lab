a = input()
b = ( a.split())
c = []

for i in b:
    if len(i) >= 3:
        c.append(i)

print(*c)