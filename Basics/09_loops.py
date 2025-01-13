# Loops

# While

condition = 0

while condition <= 10:
    print(condition)
    condition += 2
else: # Optional 
    print("While loop reach the condition and finished it")

while condition < 20:
    condition += 1
    if condition == 15:
        print("Equal to 15")
        break # Stop when the condition is equal to 15 and finish the loop
    else:
        print(condition)

while condition < 20:
    condition += 1
    if condition == 18:
        continue  # Skip when the condition is equal to 18 and continue the loop
    else:
        print(condition)

# for

my_list = [35, 24, 62, 52, 30, 30, 17]
for element in my_list:
    print(element)

my_tuple = (35, 1.77, "Brais", "Moure")
for element in my_tuple:
    print(element)

my_set = {"Macarena", "Pet", 6}
for element in my_set:
    print(element)

my_dict = {
    "Name":"Vivian",
    "Age":29,
    "Language": ["Spanish", "English", "Italian"]
}
for element in my_dict:
    print(element) # Keys
for element in my_dict.values():
    print(element) # Values
for key, value in my_dict.items():
    print(key, value) # Keys and Values
else: # Optional
    print("All the data was printed")

for element in my_dict:
    if element == "Language":
        break
    else: 
        print(element)

for element in my_dict:
    if element == "Age":
        continue
    else: 
        print(element)