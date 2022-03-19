import os
with open('first.txt','r') as first,open('second.txt','w') as second:
    for line in first:
        second.write(line)
        