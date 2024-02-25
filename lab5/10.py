#Write a Python program to convert a given camel case string to snake case.
import re
txt=input("Enter:")
x=re.sub(r'([a-z])([A-Z])', r'\1_\2',txt).lower()
print(x)