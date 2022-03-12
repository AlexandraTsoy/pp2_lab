a = input().split() 
 
if len(a) == 1 : 
    a = int(a[0]) 
    x = int(input()) 
else : 
    a, x = int(a[0]), int(a[1]) 
y = x 
for i in range(1, a): 
    y = y ^ (x + (2 * i)) 
print(y)