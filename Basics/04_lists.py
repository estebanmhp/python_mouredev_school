# Lists

my_list = list()
another_list = []

print(type(my_list))
print(type(another_list))

# Length

print(len(my_list))

# Initialization

my_list = [35, 24, 62, 52, 30, 30, 17]
another_list = [35, 1.77, "Mao", "Smith"]

print(my_list)
print(another_list)

# Accesing list items

# Positive index
# Index position starts from 0

print(another_list[0]) # First element = 35
print(another_list[3]) # Last element = Smith

# Negative index (reverse order)
# Index position starts from -1

print(another_list[-1]) # Last element = Smith
print(another_list[-4]) # Fourth last element = 35

# Unpacking List Items

age, height, name, surname = another_list
name, surname = another_list[2], another_list[3] # Not recommended

print(f"You height is {height}")
print(name)
print(surname)

# Methods

print(my_list.count(30)) # Count how many elements are equal to the specified value
print(my_list + another_list) # Concatenate lists
another_list.append("Mao Company") # Add a new element, at the end
print(another_list)
another_list.insert(1, "Red") # Add a new element, at the specified index
print(another_list)
another_list[1] = "Blue" # Add an new element or change its value, at the specified index
print(another_list)
another_list.remove("Blue") # Remove the first element that has the same value
print(another_list)
my_list.remove(30) # Just remove one 30, leave the second one
print(my_list)
my_list.pop() # Remove and return an element, at the end by default
print(my_list)
pop_element = my_list.pop(2) # Removes and returns the element at the specified index
print(pop_element) 
print(my_list)
del my_list[2] # Just remove the element at the specified index
print(my_list)
copy_list = my_list.copy() # Copy a list
print(copy_list)
my_list.clear() # Delete the list, returning an empty list
print(my_list)
copy_list.reverse() # Reverse order
print(copy_list)
copy_list.sort() # Sort the list, from smallest to largest by default
print(copy_list)
print(copy_list[1:2]) # Slices a list, first parameter (start) second (end) third (step)
print(copy_list[::-1]) # Reverse order
