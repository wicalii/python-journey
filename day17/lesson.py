# Day 17 - Functions Practice


# Basic function
def hello(name):
    return f"Hello {name}"


print(hello("Ali"))


# Function with multiple parameters
def add(a, b):
    return a + b


print(add(10, 20))


# Default parameter
def power(number, exponent=2):
    return number ** exponent


print(power(5))
print(power(3, 3))


# Boolean function
def is_even(number):
    return number % 2 == 0


print(is_even(10))
print(is_even(7))


# Function combination
def add_five(number):
    return number + 5


def multiply_two(number):
    return number * 2


result = multiply_two(add_five(10))

print(result)


# Returning multiple values
def user_info():
    name = "Ali"
    age = 19

    return name, age


name, age = user_info()

print(name)
print(age)