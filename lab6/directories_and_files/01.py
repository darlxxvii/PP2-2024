#Write a Python program to list only directories, files and all directories, files in a specified path.
import os

path= r"C:\Users\nazvi\OneDrive\Документы\Инфо ент материалы"
all=list(os.listdir(path))
print(all)