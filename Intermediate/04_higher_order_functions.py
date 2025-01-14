# Higher functions

def sum_one(value):
    return value + 1

def sum_add_one(first_value, second_value):
    return sum_one(first_value + second_value)

print(sum_add_one(5, 10))

# Function as parameter

def multiply_by_2(value):
    return value * 2

def sum_five(value):
    return value + 5

def sum_function(first_value, second_value, function):
    return function(first_value + second_value)

print(sum_function(5, 10, multiply_by_2))
print(sum_function(5, 10, sum_five))

# Closures

def sum_ten():
    ten = 10
    def add(number):
        return number + ten
    return add

add_closure = sum_ten()
print(add_closure(5)) # 15
print(sum_ten()(5)) # 15

def sum_ten(value):
    ten = 10
    def add(number):
        return number + ten + value
    return add

add_closure = sum_ten(5)
print(add_closure(5)) # 20
print(sum_ten(5)(5)) # 20

# Built-in Higher order functions

numbers = [2, 5, 10, 21, 3, 30]

# Map

print(list(map(multiply_by_2, numbers))) # [4, 10, 20, 42]
print(list(map(lambda number: number * 2, numbers))) # [4, 10, 20, 42]

# Filter

def greater_than_10(number):
    if number > 10:
        return True
    else: 
        return False

print(list(filter(greater_than_10, numbers))) # [21, 30]
print(list(filter(lambda number: number > 10, numbers))) # [21, 30]

# Reduce

from functools import reduce

def sum(first_value, second_value):
    return first_value + second_value

print(reduce(sum, numbers)) # 71 = [2+5 = 7+10 = 17+21 = 38+3 = 41+30 = 71]