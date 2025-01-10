# Variables 
# Use lowercase and snake_case

string_variable = "My string variable" 
print(string_variable)

integer_variable = 5
print(integer_variable)

integer_to_string = str(integer_variable) # Cast
print(integer_to_string)
print(type(integer_to_string))

boolean_variable = False
print(boolean_variable)

# Variable concatenation
# Print with parameters, combianes all parameters into a new string

print(string_variable, integer_variable) 
print("Value of the bool variable:", boolean_variable)

# len() -> length

print(len(integer_to_string))
print(len(string_variable))

# One single line for more than one variable

name, surname, alias, age = "Vivian", "Escorcia", "Wiwis", 28
print("My name is:", name, surname, "\nI am", age, "years old\nMy friend call me", alias)

# Input

# name = input("What is your name?")
# age = input("How old are you?")

# print("Your name is:", name, "\nYou are", age, "years old")

# Change the data type of a variable

name = 34
age = "Andre"

print("Your name is:", name, "\nYou are", age, "years old")

# Force the data type (it doesnt matter, the data type can change it at any moment)

address: str = "P. Sherman, 42 Wallaby Way, Sydney"
print(type(address)) # str

address = True
print(type(address)) # bool

address = 5
print(type(address)) # int

address = 1.2
print(type(address)) # float