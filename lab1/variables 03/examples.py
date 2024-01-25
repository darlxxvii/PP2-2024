#1 
x = 5
y = "John"
print(x)
print(y)

#2
x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

#3
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

#4
x = 5
y = "John"
print(type(x))
print(type(y))

#5
x = "John"
# is the same as
x = 'John'

#6
a = 4
A = "Sally"
#A will not overwrite a

#7
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

#8 (illegal variable names)
#2myvar = "John"
#my-var = "John"
#my var = "John"

#9
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

#10
x = y = z = "Orange"
print(x)
print(y)
print(z)

#11
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

#12
x = "Python is awesome"
print(x)

#13
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

#14
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

#15
x = 5
y = 10
print(x + y)

#16 (error)
#x = 5
#y = "John"
#print(x + y)

#17
x = 5
y = "John"
print(x, y)

#18
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

#19
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

#20
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

#21
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

