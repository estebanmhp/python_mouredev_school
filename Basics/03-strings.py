# Strings

my_text = "String" # Double quotes
another_text = 'Another string' # Single quotes

# Length

print(len(my_text))
print(len(another_text))

# Concatenate

print(my_text + " " + another_text)

# Special characters

new_line = "String with\na new line"
tab_string = "\t String with\ttab"
scpae_string = "\\t String with no \\n special characters"

print(new_line)
print(tab_string)
print(scpae_string)

# Formatting

name, surname, age = "Andre", "Sastre", 26

print("My name is %s %s. I am %d years old" %(name, surname, age))
print("My name is {} {}. I am {} years old".format(name, surname, age))
print(f"My name is {name} {surname}. I am {age} years old")

# Unpacking Characters

language = "Python"
a, b, c, d, e, f = language

print(a)
print(b)
print(f"{f}{e}{d}{c}{b}{a}")

last_letter = language[-1]
second_last = language[-2]
print(last_letter)
print(second_last)

# Slicing

slice = language[0:2]
print(slice) # Py

slice = language[2:] # thon
print(slice)

slice = language[:6:2] # Pto
print(slice)

slice = language[::2] # Pto
print(slice)

# Reverse

reverse = language[::-1]
print(reverse)

# Methods

print(language.capitalize()) # uppercase the first letter
print(language.upper()) # to uppercase
print(language.count("y")) # how many characters are the specified character
print(language.isnumeric()) # true if it is a number, otherwise false
print("2".isnumeric()) # true
print(language.lower()) # to lowercase
print(language.startswith("p")) # true if starts with the specified value (case sensitive), false otherwise

print(language.upper().isupper()) # First convert the string to uppercase and then check if all of the string is uppercase