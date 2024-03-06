#Write a Python program to delete file by specified path.
#Before deleting check for access and whether a given path exists or not.
import os
path_=r"C:\Users\nazvi\OneDrive\Рабочий стол\ppp\lab1\syntax\01.py"
print(os.access(path_, os.R_OK ))#readable
print(os.access(path_, os.X_OK ))#executeable
print(os.access(path_, os.W_OK ))#writeable
print(os.access(path_, os.F_OK ))#existable
if os.path.exists(path_):
    print("Exists")
else:
    print("Does not exist")
os.remove(path_)