"""A recipe you are reading states how many grams you need for the ingredient. 
Unfortunately, your store only sells items in ounces. Create a function 
to convert grams to ounces. ounces = 28.3495231 * grams"""
x=float(input("Enter the value: "))
def gr_to_ounces(x):
    return 28.3495231 * x

print(gr_to_ounces(x), "ounces")