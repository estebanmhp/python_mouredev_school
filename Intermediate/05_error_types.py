# Error types

# Syntax error
# print "Hello" -> SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
print("Hello")

# Name error
# print(language) -> NameError: name 'language' is not defined
language = "Python"
print(language)

# Index error
numbers = [1, 2, 3, 4, 5]
# print(numbers[6]) -> IndexError: list index out of range
# print(numbers[-6]) -> IndexError: list index out of range
print(numbers[4]) # 5
print(numbers[-5]) # 1

# Module not found
# import maths -> ModuleNotFoundError: No module named 'maths'
import math

# Attribute error
# print(math.PI) -> AttributeError: module 'math' has no attribute 'PI'. Did you mean: 'pi'?
print(math.pi)

# Key error
my_dict = {"Name": "Steph", "Age": 34}
# print(my_dict["Surname"]) -> KeyError: 'Surname'
# print(my_dict["age"]) -> KeyError: 'age'
print(my_dict["Age"]) # 34

# Type error
# print(numbers["3"]) -> TypeError: list indices must be integers or slices, not str
print(numbers[3]) # 4

# Importe error
# from math import PI -> ImportError: cannot import name 'PI' from 'math' (unknown location)
from math import pi
print(pi)

# Value error
# number = int("10 Años")
# print(type(number)) -> ValueError: invalid literal for int() with base 10: '10 Años'
number = int("10")
print(type(number)) # <class 'int'>

# Zero division error
# print(4 / 0) -> ZeroDivisionError: division by zero
print(4 / 2) # 2