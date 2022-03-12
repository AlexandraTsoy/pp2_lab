a = [] 
 
def str(b): 
    return b[2], b[1], b[0] 
 
while True: 
    date = input().split() 
    if date[0] == '0': 
        break 
    a.append((date[0], date[1], date[2])) 
 
a = sorted(a, key = str) 
for i in a: 
    print(*i)