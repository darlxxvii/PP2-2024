#Write a Python program to check for access to a specified path. 
#Test the existence, readability, writability and executability of the specified path
import os

filename = "3.py"

print(os.access(filename, os.F_OK)) # existence
print(os.access(filename, os.R_OK)) # readable
print(os.access(filename, os.W_OK)) # writable
print(os.access(filename, os.X_OK)) # executable