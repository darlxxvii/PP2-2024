import re
with open("row.txt") as f:
    txt = f.read()
x = re.findall('[a-z]+_[a-z]', txt)
z=input("Enter your text:")
print(x)
y = re.findall("[a-z]+_[a-z]", z)
print(y)
