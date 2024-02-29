#Write a Python program with builtin function that accepts a string 
#and calculate the number of upper case letters and lower case letters
str=input("Enter here:")
def low(str):
    lower=0
    upper=0
    for i in str:
        if i.islower():
            lower+=1
        elif i.isupper():
            upper+=1
    return upper, lower
print(low(str))
