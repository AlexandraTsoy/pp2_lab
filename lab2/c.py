n = int(input())
m=[]
for i in range(n):
    a = []
    for j in range(n):
        if i == 0:
            a.append(j)
        elif j==0 :
            a.append(i)
        elif i==j:
            a.append(i*j)
        else:
            a.append(0)
    m.append(a)
for i in range(n):
    for j in range(n):
        print(m[i][j],end =' ')
    print()