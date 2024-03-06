#Write a Python program to count the number of lines in a text file.
def count_lines(filen):
    with open(filen, 'r') as file:
        lines = file.readlines()
        return len(lines)
print(count_lines("text.txt"))