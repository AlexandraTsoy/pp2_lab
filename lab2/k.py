a=input()
a=a.replace('!','').replace('?','').replace('.','').replace(',','').split()

unique=[]
for i in a:
    if i not in unique:
        unique.append(i)
unique.sort()
print(len(unique))
print(*unique, sep='\n')