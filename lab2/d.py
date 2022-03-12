n=int(input())
list=[['.' for i in range(n)]for i in range(n)]
for i in range(n):
 for j in range(n):
       if n%2==0:
         if i+j<=i*2:
          list[i][j]="#"
       if n%2!=0:
         if i+j>=n-1:
           list[i][j]="#"


for i in range(n):
    for j in range(n):
        print(list[i][j], end='')
    print()