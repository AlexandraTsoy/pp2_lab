def gendivs(n):
    for i in range(0, n): 
        if(i % 3 == 0 and i % 4 == 0):
            yield i
n = int(input())
for x in gendivs(n):
    print (x)