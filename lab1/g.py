a = input()
b = 0
c = len(a)

for i in range(c):
    b += int(a[-(1 + i)]) * 2**i


print(int(b))