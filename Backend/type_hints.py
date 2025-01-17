# Type hints

my_string = "My String variable"
print(my_string)
print(type(my_string))

my_string = 5
print(my_string)
print(type(my_string))

# Python is a dynamically typed language
# Whenever we want we can change the type of a variable or of any data without problems
# However we should follow the standards of API for backend

type_hint_variable: str = "Type hint variable"
print(type_hint_variable)
print(type(type_hint_variable))

type_hint_variable: int = 5
print(type_hint_variable)
print(type(type_hint_variable))