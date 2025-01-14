# List comprehension

my_original_list = [35, 24, 62, 52, 30, 30, 17]
my_list = [i for i in my_original_list]

print(my_list) # Just a copy of the list

my_original_list = [0, 1, 2, 3, 4, 5, 6, 7]
my_list = [i for i in range(8)]

print(my_list) # New list with numbers between 0 to 7 -> [0, 1, 2, 3, 4, 5, 6, 7]

my_range = range(0, 9, 2) # First parameter = start, second = end, third = steps
list_my_range = list(my_range)

print(list_my_range) # [0, 2, 4, 6, 8]

my_list = [i + 2 for i in range(8)]
print(my_list) # [2, 3, 4, 5, 6, 7, 8, 9] = [0+2, 1+2, 2+2, 3+2, 4+2, 5+2, 6+2, 7+2]

my_list = [i * i for i in range(8)]
print(my_list) # [0, 1, 4, 9, 16, 25, 36, 49] = [0*0, 1*1, 2*2, 3*3, 4*4, 5*5, 6*6, 7*7]

def sum_five(number):
    return number + 5

my_list = [sum_five(i) for i in range(8)]
print(my_list) # [5, 6, 7, 8, 9, 10, 11, 12] = [0+5, 1+5, 2+5, 3+5, 4+5, 5+5, 6+5, 7+5]

