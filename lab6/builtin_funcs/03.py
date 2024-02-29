#Write a Python program with builtin function that checks whether a passed string is palindrome or not.
str=input()
x=reversed(str)
reverse=''.join(x)
if reverse==str:
    print("palindrome")
else:
    print("Not palindrome")