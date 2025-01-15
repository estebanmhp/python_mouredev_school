# File handling

# txt file

# Read and write

txt_file = open("Intermediate/text_file.txt", "r+") 
# print(txt_file.read()) # Read all the file
print(txt_file.read(15)) # Read just n numbers of characters
print(txt_file.readline()) # Read a line 
print(txt_file.readline()) # Read the next line
print(txt_file.readlines()) # Read and show the file like a list, each line is an element
for line in txt_file.readlines():
    print(line) # It is possible to print line by line, like an iterable object

txt_file.write("\nI am from Colombia")
print(txt_file.readline())
txt_file.close()

# Read and write (overwrite), this can crete the file if this doesnt exist

txt_file2 = open("Intermediate/text_file2.txt", "w+") 
txt_file2.write("My name is Vivi\nMy family name is Escorcia\nI am 28 years old\nI love dogs\nI am from Colombia")
txt_file2.write("\nI am an architect")
for line in txt_file2.readlines():
    print(line)
txt_file2.close()

# Delete a file

import os
os.remove("Intermediate/text_file2.txt")

# .json file

import json

json_file = open("Intermediate/json_file.json", "w+")

json_test = {
    "Name": "Maurice", 
    "Surname":"Flowers", 
    "Age":32, 
    "Languages": ["Python", "JavaScript", "C"],
    "Website": "https://flowersdevelopers.dev"
}

json.dump(json_test, json_file, indent=4) # Write to a json file from an object(dictionary)

json_file.close() # To read a file this need to be closed

with open("Intermediate/json_file.json") as other_json_file:
    for line in other_json_file.readlines():
        print(line)

json_dict = json.load(open("Intermediate/json_file.json")) # Json file to a dictonary
print(json_dict)
print(type(json_dict))
print(json_dict["Name"])

# CSV file

import csv

csv_file = open("Intermediate/csv_file.csv", "w+")

csv_writer = csv.writer(csv_file)
csv_writer.writerow(["Name", "Surname", "Age", "Language", "Website"])
csv_writer.writerow(["Maurice", "Flowers", 32, "Python", "https://flowersdevelop.dev"])

csv_file.close()

with open("Intermediate/csv_file.csv") as other_csv_file:
    for line in other_csv_file.readlines():
        print(line)