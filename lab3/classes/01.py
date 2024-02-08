"""Define a class which has at least two methods: getString: to get a string from 
console input printString: to print the string in upper case."""
class String:
    def getString(self):
        self.string=input("Enter your string:")
    def printString(self):
        print(self.string.upper())
#    def __str__(self):
#        return f"{self.string}"

stri=String()
stri.getString()
stri.printString()