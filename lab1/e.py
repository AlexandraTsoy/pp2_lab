a,b=map(int,input().split())

k=0
for i in range(2, a-1):
    if (a % i == 0):
        k = k+1

if a<500 and b%2==0 and (k <= 0) :
    print("Good job!")
else:
    print("Try next time!")