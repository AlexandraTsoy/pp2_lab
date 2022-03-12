x1, y1 = map(int, input().split()) 
p=int(input()) 
abc=[] 
 
def str(a): 
    return a[1] 
 
for i in range(p): 
    a = input() 
    x2, y2 = a.split() 
    b= ((int(x2)-x1)**2+(int(y2)-y1)**2)**0.5
    abc.append((a, b)) 
 
abc.sort(key = str)
 
for x in abc: 
    print(x[0])