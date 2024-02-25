import re
with open("row.txt") as f:
    txt = f.read()
x=re.search("ab*",txt)
if x:
    print("Yes")
else:
    print('No')