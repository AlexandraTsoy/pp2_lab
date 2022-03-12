


x=int(input())
mx1 = 0
mx2 = 0
l = []
a = map(int, input().split())
for i in a:
    l.append(i)
l.sort(reverse = True)
print(l[0] * l[1])


