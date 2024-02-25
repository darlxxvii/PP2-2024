import re
with open("row.txt") as f:
    txt = f.read()
x=re.search("ab*",txt)
z=input()
x=re.search("ab{2,3}",txt)
if x:
    print("for Row.txt: Yes")
else:
    print('for Row.txt: No')
if z:
    print("for your input: Yes")
else:
    print('for your input: No')