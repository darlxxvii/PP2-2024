#Write a Python program to copy the contents of a file to another file
# Write to the first file
with open('file1.txt', 'w+') as f:
    f.write("Let me get some rest")
    f.seek(0) 
    x = f.read()
with open('file2.txt', 'w') as y:
    y.write(x)
