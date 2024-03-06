#Write a Python program to write a list to a file.
n=input()
thislist=list(n)
with open("list.txt",'w') as f:
    for i in thislist:
        f.write(str(i)+" ")
