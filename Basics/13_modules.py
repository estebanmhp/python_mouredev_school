# Modules

# Import all the module

import my_module 

my_module.sum_value(5, 3, 1)
my_module.print_value("Python")

# Import a specific function of module

from my_module import print_value, sum_value

sum_value(5, 7, 2)
print_value("Hello")

# Import system modules

import math

print(math.pi)

# Rename modules

from math import pi as PI_VALUE

print(PI_VALUE)