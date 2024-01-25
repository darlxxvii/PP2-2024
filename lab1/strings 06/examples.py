#1
x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3

#2
x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2

#3
x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'


#string
#1
print("Hello")
print('Hello')

#2
a = "Hello"
print(a)

#3
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

#4
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

#5
a = "Hello, World!"
print(a[1])

#6
for x in "banana":
  print(x)

#7
a = "Hello, World!"
print(len(a))

#8
txt = "The best things in life are free!"
print("free" in txt)

#9
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

#10
txt = "The best things in life are free!"
print("expensive" not in txt)

#11
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")

#12
b = "Hello, World!"
print(b[2:5])

#13
b = "Hello, World!"
print(b[:5])

#14
b = "Hello, World!"
print(b[2:])

#15
b = "Hello, World!"
print(b[-5:-2])

#16
a = "Hello, World!"
print(a.upper())

#17
a = "Hello, World!"
print(a.lower())

#18
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

#19
a = "Hello, World!"
print(a.replace("H", "J"))

#20
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

#21
a = "Hello"
b = "World"
c = a + b
print(c)

#22
a = "Hello"
b = "World"
c = a + " " + b
print(c)

#23 (error)
#age = 36
#txt = "My name is John, I am " + age
#print(txt)

#24
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

#25
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

#26
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

#27 (error)
#txt = "We are the so-called "Vikings" from the north."

#28
txt = "We are the so-called \"Vikings\" from the north."

#29
# \'	Single Quote
# \\	Backslash
# \n	New Line
# \r	Carriage Return
# \t	Tab
# \b	Backspace
# \f	Form Feed
# \ooo	Octal value
#\xhh	Hex value

#30
# capitalize()	Converts the first character to upper case
# casefold()	Converts string into lower case
# center()	Returns a centered string
# count()	Returns the number of times a specified value occurs in a string
# encode()	Returns an encoded version of the string
# endswith()	Returns true if the string ends with the specified value
# expandtabs()	Sets the tab size of the string
# find()	Searches the string for a specified value and returns the position of where it was found
# format()	Formats specified values in a string
# format_map()	Formats specified values in a string
# index()	Searches the string for a specified value and returns the position of where it was found
# isalnum()	Returns True if all characters in the string are alphanumeric
# isalpha()	Returns True if all characters in the string are in the alphabet
# isascii()	Returns True if all characters in the string are ascii characters
# isdecimal()	Returns True if all characters in the string are decimals
# isdigit()	Returns True if all characters in the string are digits
# isidentifier()	Returns True if the string is an identifier
# islower()	Returns True if all characters in the string are lower case
# isnumeric()	Returns True if all characters in the string are numeric
# isprintable()	Returns True if all characters in the string are printable
# isspace()	Returns True if all characters in the string are whitespaces
# istitle()	Returns True if the string follows the rules of a title
# isupper()	Returns True if all characters in the string are upper case
# join()	Joins the elements of an iterable to the end of the string
# ljust()	Returns a left justified version of the string
# lower()	Converts a string into lower case
# lstrip()	Returns a left trim version of the string
# maketrans()	Returns a translation table to be used in translations
# partition()	Returns a tuple where the string is parted into three parts
# replace()	Returns a string where a specified value is replaced with a specified value
# rfind()	Searches the string for a specified value and returns the last position of where it was found
# rindex()	Searches the string for a specified value and returns the last position of where it was found
# rjust()	Returns a right justified version of the string
# rpartition()	Returns a tuple where the string is parted into three parts
# rsplit()	Splits the string at the specified separator, and returns a list
# rstrip()	Returns a right trim version of the string
# split()	Splits the string at the specified separator, and returns a list
# splitlines()	Splits the string at line breaks and returns a list
# startswith()	Returns true if the string starts with the specified value
# strip()	Returns a trimmed version of the string
# swapcase()	Swaps cases, lower case becomes upper case and vice versa
# title()	Converts the first character of each word to upper case
# translate()	Returns a translated string
# upper()	Converts a string into upper case
# zfill()	Fills the string with a specified number of 0 values at the beginning


