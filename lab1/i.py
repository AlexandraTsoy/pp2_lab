a = int(input())
b = []

for i in range(a):
    i = input()
    b.append(i)

for i in range(a):
    if '@gmail.com' in b[i]:
        print(b[i][:-10])