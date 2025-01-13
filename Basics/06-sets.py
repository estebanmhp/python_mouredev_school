# Sets

my_set = set()
another_set = {}
another_set2 = {"banana", "orange", "mango", "lemon"} # A set cannot be declared empty, if it is empty, it would be a dictionary

print(type(my_set)) # Set
print(type(another_set)) # Dictionary
print(type(another_set2)) # Set

# Initialization

another_set = {35, 1.77, "Brais", "Moure"} # It is not an ordered data structure
print(type(another_set)) # Now it is a set

# Length

print(len(another_set))

# Adding elements

another_set.add("MoureDev")
print(another_set)
another_set.add("MoureDev") # It is not possible to have a duplicated value
print(another_set)

# Cheking an element

print("Moure" in another_set) # Checks if an element exists in a set
print("moure" in another_set) # True if it exists, otherwise false (case sensitive)

# Removing an element

another_set.remove("MoureDev")
print(another_set)

# Clear

another_set2.clear() # Remove all the elements in a set, returning an empty set
print(len(another_set2))

del another_set2 # Delete the set without returning anything

# Converting List to Set

my_set = {60, "White", "Remus", 35}
set_list = list(my_set) # Not recommended because the order of the set is unknown

print(type(set_list))
print(set_list)

# Join sets

combine_set = my_set.union(another_set) # Just add/join the unique elements
print(combine_set)
combine_set = combine_set.union({"Mac", "Blue"}) # Another way to add elements
print(combine_set)

# Differences between sets

print(combine_set.difference(my_set)) 