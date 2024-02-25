#Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.
import re
with open("row.txt") as f:
    txt = f.read()
x=re.search("a.*b$",txt)
y=input("Enter your text:")
z=re.search("a.*b$",y)
if x:
    print("for Row.txt: Yes")
else:
    print('for Row.txt: No')
if z:
    print("for your input: Yes")
else:
    print('for your input: No')