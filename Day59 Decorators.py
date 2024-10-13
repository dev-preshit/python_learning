"""
    Day 59 is about Decorators in Python...
        A decorator is a function that takes another function as an argument
        and returns a new function that modifies the behavior of the original
        function. The new function is often referred to as a "decorated" function.
        Syntax:
            @decorator_function
            def my_function():
                pass

"""

def greet(fx):
    def mfx(*args, **kwargs):  # Corrected variable names for clarity
        print("GOOD MORNING")  # Corrected spelling
        fx(*args, **kwargs)
        print("GOOD NIGHT")
    return mfx
    

@greet
def hello():
    print("Hello, world")

@greet
def add(x, y):
    print(x + y)

hello()
# greet(hello)() # Can also write like this
# GOOD MORNING
# Hello, world
# GOOD NIGHT

add(10, 20)
# greet(add)(10,20) # Can also write like this
# GOOD MORNING
# 30
# GOOD NIGHT
