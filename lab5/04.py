import re
with open("row.txt") as f:
    txt = f.read()
x = re.findall('[A-Z][a-z]+', txt)
z=input("Enter your text:")
print(x)
y = re.findall('[A-Z][a-z]+', z)
print(y)