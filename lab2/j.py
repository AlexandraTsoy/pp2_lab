a=int(input())
b=[]
def abc(c):
    low=False
    up=False
    num=False
    for i in c:
        if i>='a' and i<='z':
            low= True
        if i>='A' and i<='Z':
             num= True
        if i>='0' and i<='9':
            up=  True
    if low and up and num:
        return True
    else:
        return False
    
for i in range(a):
     passw=input()
     if abc(passw) and passw not in b:
          b.append(passw)
b.sort()
print(len(b))
for s in b:
    print(s)