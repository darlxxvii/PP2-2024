"""Read in a Fahrenheit temperature. Calculate and display the equivalent centigrade 
temperature. The following formula is used for the conversion: C = (5 / 9) * (F – 32)
"""
t=float(input())
def toCelcius(F):
    return (5/9)*(F-32)
print(toCelcius(t))