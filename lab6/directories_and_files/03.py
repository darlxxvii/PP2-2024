#Write a Python program to test whether a given path exists or not. 
#If the path exist find the filename and directory portion of the given path.
import os
path_=r"C:\Users\nazvi\OneDrive\Рабочий стол\ppp\lab1\syntax\01.py"
if os.path.exists(path_):
    print(os.path.basename(path_))
    print(os.path.dirname(path_))
else:
    print("No such path")
