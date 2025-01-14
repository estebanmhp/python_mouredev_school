# Lambda function

sum = lambda first_vale, second_value: first_vale + second_value
print(sum(5, 10))

multiply = lambda first_value, second_value: first_value * second_value - 3
print(multiply(5, 10))

def sum_values(value):
    return lambda first, second: first + second + value
print(sum_values(2)(5, 10))

