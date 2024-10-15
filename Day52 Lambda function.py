"""
    # Day 52 is about lambda functions in Python...
        In Python, a lambda function is a small anonymous function without a name.
        It is defined using the lambda keyword.
        Syntax:
            lambda arguments: expression

        We can also pass functions into other functions as arguments.
"""

# Function using def 
def double(x):
    return x * 2

print(double(5))
# 10

# Function using lambda
twice = lambda x: x * 2
print(twice(10))
# 20

avg = lambda x, y, z: (x + y + z) / 3
print(avg(10, 20, 30))
# 20

# Function passed into a function
def apply(fx, value):
    return fx(value) * fx(value - 1)

print(apply(double, 5))
# 80

# We can also pass a lambda function instead of a proper function
print(apply(lambda x: x * 2, 5))
# 80
