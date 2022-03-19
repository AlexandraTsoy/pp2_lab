import math
from time import sleep
a = int(input())
b = int(input())
print(f"Square root of {a} after {b} miliseconds is ", end = '', flush = True)
sleep(b * 0.001)
print(math.sqrt(a))