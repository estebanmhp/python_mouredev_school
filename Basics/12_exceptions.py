# Exceptions

number_one, number_two = 5, 1
print(number_one + number_two)

number_two = "1"
# Error -> print(number_one + number_two) 

# try except

try:
    print(number_one + number_two)
except:
    print("Error")

# try except else (optional)

number_two = 1

try:
    print(number_one + number_two)
except:
    print("Error")
else:
    print("No errors. Continue with the rest of the code") # No exceptions so run this code

# try except else finally (optional)

number_two = "1"

try:
    print(number_one + number_two)
except:
    print("Error")
else:
    print("No errors. Continue with the rest of the code")
finally:
    print("Always run this code, with or without errors")

# Type exceptions

try:
    print(5 + "5")
except TypeError:
    print("TypeError")
except ValueError:
    print("ValueError")

try:
    print(5 + int("x"))
except TypeError:
    print("TypeError")
except ValueError:
    print("ValueError")

# Catch the info exception

try:
    print(5 + "5")
except TypeError as error:
    print(error)

try:
    print(5 + int("x"))
except TypeError as error:
    print(error)
except Exception as error:
    print(error)