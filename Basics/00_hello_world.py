# Hello world
# This is a single line comment

print("Hello Python")
print('Hello Python')

""" 
This is a 
multiline coment
""" 

'''
This is another
multiline coment
'''

# How to know the data type

print(type("Hello")) # Type 'str'
print(type(5)) # Type 'int'
print(type(1.5)) # Type 'float'
print(type(True)) # Type 'bool'
print(type(3 + 2j)) # Type 'complex'
print(type(print("String"))) # Type 'NoneType', because print is just a standard output, so its return value is None

result = print("x")
print(result) # Prints none because the value assigned to value is the return value of print("x") which is None
print(type(result)) # Prints 'NoneType