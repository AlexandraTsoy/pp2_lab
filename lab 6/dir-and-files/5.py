arr=[x for x in input("Enter something :\n").split()]
f=open('output.txt','a')
for i in arr:
    f.write(i)
f.close()