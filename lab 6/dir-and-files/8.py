import os
path='input.txt'
if os.path.exists(path):
    os.remove(path)
else:
    print("There is no such file")