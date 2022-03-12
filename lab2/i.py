a=int(input())
shell=[]
hend=[]
for i in range(a):
    b=input().split()
    if int(b[0])==1:
        shell.append(b[1])
    elif int(b[0])==2:
        hend.append(shell[0])
        shell.pop(0)

for i in hend:
    print(i, end=' ')