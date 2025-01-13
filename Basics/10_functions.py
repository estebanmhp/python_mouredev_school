# Functions

def my_function ():
    print("This is a function")

my_function()

def sum_two_values (first_value, second_value):
        print(f"Result = {first_value + second_value}")

sum_two_values(5, 7)
sum_two_values(5469, 23092)
sum_two_values("5", "7") # Concatenation of strings
sum_two_values(1.5, 4.6)

def sum_two_values (first_value, second_value):
    if type(first_value) is int and type(second_value) is int:
        print(f"Result = {first_value + second_value}")
    elif type(first_value) is float and type(second_value) is float:
        print(f"\"{first_value}\" and \"{second_value}\" are float numbers") 
    else:
        print(f"\"{first_value}\" and \"{second_value}\" are not numbers")

sum_two_values(5, 7)
sum_two_values(5469, 23092)
sum_two_values("5", "7") # Not numbers
sum_two_values(1.5, 4.6) # Float numbers

def sum_two_values (first_value, second_value):
    if isinstance(first_value, (int, float)) and isinstance(second_value, (int,float)):
        print(f"Result = {first_value + second_value}")
    else:
        print(f"\"{first_value}\" and \"{second_value}\" are not numbers")

sum_two_values(5, 7)
sum_two_values(5469, 23092)
sum_two_values("5", "7") # Not numbers
sum_two_values(1.5, 4.6) 

# Function Returning a Value

def sum_with_return (first_value, second_value):
    return first_value + second_value

result_returned = sum_with_return(10, 5) # Return the result of the function
print(result_returned)

# Passing Arguments with Key and Value

def print_name(name, surname):
    print(f"{name} {surname}")

print_name("Escorcia", "Juli")
print_name(surname = "Escorcia", name = "Juli")

# Function with Default Parameters

def print_name_default (name, surname, alias = "No nickname"):
    print(f"{name} {surname}. Nickname: {alias}")

print_name_default("Juli", "Escorcia")
print_name_default("Juli", "Escorcia", "J")

# Arbitrary Number of Arguments

def print_texts (*text):
    print(text)

print_texts("Hello", "Python", "More texts", "More and more")

def print_upper_texts (*texts):
    for text in texts:
        print(text.upper())

print_upper_texts("apple", "banana", "cherry", "date", "elderberry")