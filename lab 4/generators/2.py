def genevens(n):
    for i in range(1, n, 2): 
        yield i
n = int(input())
for x in genevens(n):
    print (x)