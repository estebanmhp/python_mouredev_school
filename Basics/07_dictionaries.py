# Dictionaries

my_dict = dict()
another_dict = {}

print(type(my_dict))
print(type(another_dict))

# Initialization

another_dict = {"Name": "Macarena", "Surname":"Smith", "Age":6, 1:"Pet"}
my_dict = {
    "Name": "Maurice", 
    "Surname":"Flowers", 
    "Age":32, 
    "Languages":{"French", "English", "Spanish"},
    "Pet":["Macarena", "Kira"]
} # A dictionary could have any data type inside, from primivite types to lists, sets, tuples, any data type 

print(another_dict)
print(my_dict)

# Length

print(len(another_dict)) # 4 keys = length 4
print(len(my_dict)) # 5 keys = length 5

# Accessing Dictionary elements

print(my_dict["Name"]) # Print the value in the key
print(my_dict["Pet"][0]) # Accesing to elements of the element
print(my_dict.get("Address")) # Instead of error, get returns none if it doesnt exists

# Adding elements

my_dict["Address"] = "Develop street" # Add a new key
my_dict["Pet"].append("Luna") # Add a new value inside of a key

print(my_dict)

# Removing a key and its value

my_dict.pop("Surname") # Remove the element with the specified key name
print(my_dict)

del my_dict["Address"] # Remove the element with the specified key name
print(my_dict)

my_dict.popitem() # Remove the last element
print(my_dict)

# Checking an element

print("Mauricie" in my_dict) # False because this looks for keys, not values
print("Name" in my_dict)

# Methods

print(my_dict.items()) # key:values
print(my_dict.keys()) # Keys
print(my_dict.values()) # Values

new_dict = dict.fromkeys(("Name", "Age")) # Create a new dictionary with empty keys
print(new_dict) 
new_dict = dict.fromkeys(my_dict) # It is like a copy just with the keys
print(new_dict)

print(list(my_dict)) # Dictionary to list, just with the keys
print(tuple(my_dict)) # Dictionary to tuple, just with the keys
print(set(my_dict)) # Dictionary to set, just with the keys

print(list(my_dict.values())) # Dictionary to list, with the values
print(tuple(my_dict.values())) # Dictionary to tuple, with the values