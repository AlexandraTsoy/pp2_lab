n=int(input())
t=str(input())

if t=="k":
    r=int(input())
    n=n/1024
    print(round(n,r))
if t=="b":
    n=n*1024
    print(n)
