import re
def snake_to_camel(snake_str):
    camel_str = re.sub('_([a-z])', lambda match: match.group(1).upper(), snake_str)
    return camel_str

snake = input("Enter snake string: ")
print("Camel case:", snake_to_camel(snake))
