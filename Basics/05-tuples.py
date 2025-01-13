# Tuples

my_tuple = tuple()
another_tuple = ()

print(type(my_tuple))
print(type(another_tuple))

# Initialization 

my_tuple = (35, 1.77, "Hector", "Lozano")
another_tuple = (1, 2, 3, 4)
print(my_tuple)

# Length

print(len(my_tuple))

# Accesing list items

# Positive index
# Index position starts from 0

print(my_tuple[0]) # First element = 35
print(my_tuple[3]) # Last element = Lozano

# Negative index (reverse order)
# Index position starts from -1

print(my_tuple[-1]) # Last element = Lozano
print(my_tuple[-4]) # Fourth last element = 35

# Methods

print(my_tuple.count(35)) # Count how many elements are equal to the specified value
print(my_tuple.index("Hector")) # Find and return the index of the specified value
print(my_tuple + another_tuple) # Concatenation of tuples
print(my_tuple[1:3]) # Slice a list
print(my_tuple[::-1]) # Reverse order
my_tuple = list(my_tuple) # Convert to a list
print(type(my_tuple))
del another_tuple # Delete a tuple without return an empty tuple