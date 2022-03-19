def rev(n):
    for i in range(n,0,-1): 
        yield i
n = int(input())
for x in rev(n):
    print (x)