import math
n = int(input("Input the size of the list:"))
print("Input the elements of the list")
data = input().split()
list = []
for i in range(n):
    a = int(data[i])
    list.append(a)
result = math.prod(list)
print("The product of list elements:", result)