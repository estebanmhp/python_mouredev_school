# Operators

# Arithmetic operators

print(3 + 4) # Addition
print(3 - 4) # Substraction
print(3 * 4) # Multiplication
print(3 / 4) # Division
print(10 % 4) # Modulus
print(2 ** 5) # Exponentiation
print(10 // 3) # Floor division (always return an integer)

print("Hello " + "Python") # Concatanation of strings 
print("World" + str(1)) # Cast, PY doesnt allow to mix data types -> ("World" + 5)
print("Python " * 3) # String multiplication, just with integers
print("Python " * int(2.5 * 2))

# Comparision operators

print(3 > 4) # Greather than
print(3 < 4) # Less than
print(3 >= 4) # Equal to or grether than
print(3 <= 4) # Equal to or less than
print(3 == 4) # Equal to
print(3 != 4) # Not equal to

# Compare strings / characters
# PY compares based on ASCII, character by character, left to right

print("Hello" > "Python") # False 
print("Hello" < "Python") # True
print("Hello" >= "Python") # False
print("Hello" <= "Python") # True
print("Hello" == "Python") # False
print("Hello" == "hello") # False
print("Hello" != "Python") #True

# Logic operators

print(3 > 4 and "Hello" > "Python") # && = and -> true if both are true, otherwise false
print(3 < 4 and "Hello" < "Python") # true
print(3 > 4 or "Hello" > "Python") # || = or -> true if at least one of them is true
print(3 >= 4 or "Hello" <= "Hello") # true
print(not(3 > 4) and not("Hello" > "Python")) # not -> true if false, false if true