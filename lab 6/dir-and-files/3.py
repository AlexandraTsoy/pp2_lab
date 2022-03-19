import os
path="C:\\Users\\User\\Desktop\\test\\dir1"
if os.path.exists(path):
    print("The path exists")
    print(os.path.basename(path))
    print(os.path.dirname(path))
else: 
    print("There is no such path")