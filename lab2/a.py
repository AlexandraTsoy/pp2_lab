arr =[]
a = map(int, input().split())

for i in a:
    arr.append(i)

x=len(arr)-1
y=int(arr[0])
if x%y==0 :
    print("1")
else :
    print("0")