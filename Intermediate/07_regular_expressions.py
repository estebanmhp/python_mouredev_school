# Regular expressions

import re

my_string = "Lesson number 7: Regular expressions(CLASS NUMBER 7)"
another_string = "Lesson number 6: File handling"

# Methods

# Match
# Match only at the beginning

print(re.match("Lesson number 7", my_string)) # <re.Match object; span=(0, 15), match='Lesson number 7'>
print(re.match("Lesson number 7", another_string)) # None
print(re.match("Regular expressions", my_string)) # None -
print(re.match("lesson number 7", my_string, re.I)) # <re.Match object; span=(0, 15), match='Lesson number 7'> -> re.I = ignore case

# Span

match = re.match("lesson number 7", my_string, re.I)
print(match) # <re.Match object; span=(0, 15), match='Lesson number 7'>
print(match.span()) # (0, 15) = Tuple
span = match.span()
start, end = span
print(my_string[start:end]) # Lesson number 7

def match_span(text, str):
    match = re.match(text, str, re.I)
    if match is not None:
        # print(match)
        start, end = match.span()
        print(str[start:end])
    else:
        print(match)

match_span("lesson number 6", another_string)
match_span("lesson number 7", another_string)
match_span("lesson number 7", my_string)

# Search
# Return the first occurence

search = re.search("number", my_string, re.I)
print(search)
start, end = search.span() # (7, 13)
print(my_string[start:end]) # number

# Find all
# Return all ocurrences

find_all = re.findall("number", my_string, re.I)
print(find_all) # ['number', 'NUMBER']

# Split
# Return the string split by the specifed pattern

split = re.split(":", my_string)
print(split) # ['Lesson number 7', ' Regular expressions(CLASS NUMBER 7)']

# Sub
# Replace the specifed substring

import re

my_string = "Lesson number 7: Regular expressions(CLASS NUMBER 7)"

sub = re.sub("Regular expressions", "REGULAR EXPRESSIONS", my_string)
print(sub) # Lesson number 7: REGULAR EXPRESSIONS(CLASS NUMBER 7)
sub = re.sub("Regular expressions", "RegEx(Regular expressions)", my_string)
print(sub) # Lesson number 7: RegEx(Regular expressions)(CLASS NUMBER 7)
sub = re.sub("number|NUMBER", "#", my_string)
print(sub) # Lesson # 7: Regular expressions(CLASS # 7)

# Custom patterns

import re

my_string = "Lesson number 7: Regular expressions(Lesson Number 7)"

pattern = r"[nN]umberr"
print(re.findall(pattern, my_string)) # ['number', 'Number']

pattern = r"[nN]umber|Expressions"
print(re.findall(pattern, my_string, re.I)) # ['number', 'expressions', 'Number']

pattern = r"[a-e]"
print(re.findall(pattern, my_string)) # ['e', 'b', 'e', 'e', 'a', 'e', 'e', 'e', 'b', 'e']

pattern = r"[0-9]"
print(re.findall(pattern, my_string)) # ['7', '7']

pattern = r"\d"
print(re.findall(pattern, my_string)) # ['7', '7']

pattern = r"\D"
print(re.findall(pattern, my_string)) # all the characters without including any number

pattern = r"[l]."
print(re.findall(pattern, my_string, re.I)) # ['Le', 'la', 'Le']

# Example of a pattern for a validation

import re

def email_validation(email):
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9]+\.[a-zA-Z-.]+$"
    find = re.findall(pattern, email)
    if find:
        print(f"Valid email: {find}")
    else: 
        print("Invalid email")

email_validation("rucita1@gmail.com") # Valid email: $['rucita1@gmail.com']
email_validation("rucita1@gmailcom") # Invalid email
email_validation("rucita1@gmail.com.1") # Invalid email
email_validation("rucita1@gmail.com.es") # Valid email: ['rucita1@gmail.com.es']