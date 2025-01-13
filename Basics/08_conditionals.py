# Conditionals

# if condition (executes the code if the condition is true)

condition = True
if condition:
    print("Executes if the condition is true")

condition = False
if not condition:
    print("Executes if the condition is false")

condition = 5 * 2
if condition == 10:
    print("The result is 10")

# if else condition

condition = 5 * 4
if condition > 10 and condition < 20:
    print("Result greater than 10 and less than 20")
else:
    print("Result less or equal to 10. Or greater or equal to 20")

# else if condition

condition = 5 * -5
if condition > 10 and condition < 20:
    print("Result greater than 10 and less than 20")
elif condition < 0:
    print("Result is negative")
else:
    print("Result less or equal to 10. Or greater or equal to 20")