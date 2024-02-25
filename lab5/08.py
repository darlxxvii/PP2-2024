#Write a Python program to split a string at uppercase letters.
import re
txt=input("Enter: ")
x=re.sub('[A-Z]', ' ', txt)
print(x)