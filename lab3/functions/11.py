"""Write a Python function that checks whether a word or phrase is palindrome 
or not. Note: A palindrome is word, phrase, or sequence that reads the same
backward as forward, e.g., madam"""
def func(text):
    for i in range(l):
        if text[i]==" ":
            text[i]==""
    x=len(text)
    for i in range(x//2):
        if text[i]!=text[x-i-1]:
            return False
    return True
text=input("Enter here: ")
l=len(text)
print(func(text))