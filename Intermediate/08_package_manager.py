# Package manager

# PIP (sudo apt install python3-pip)

# pip install numpy

import numpy
import pandas._version

print(numpy.version.version)

numbers = [1, 2, 3, 4, 5, 6]
numbers_array = numpy.array(numbers)
print(type(numbers_array)) # <class 'numpy.ndarray'>
print(numbers_array * 2) # [2 4 6 8 10 12]

# pip install pandas

import pandas

# pip list -> show all the packages that we already have
# pip unistall package_name -> pip uninstall pandas
# pip show package_name -> show the info of the package_name

# Create and import a package 
# Arithmetics Package

import mypackage # name of the folder 
from mypackage import arithmetics # importe the module 

print(arithmetics.sum_two_values(6, 7)) # 6 + 7 = 13