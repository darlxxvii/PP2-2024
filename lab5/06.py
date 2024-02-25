#Write a Python program to replace all occurrences of space, comma, or dot with a colon.
import re
with open('row.txt','r') as f:
    txt = f.read()
x = re.sub(r'[\s,.]', ':', txt)
print(x)
y=input()
z=re.sub(r'[\s,.,,]', ':', y)
print(z)