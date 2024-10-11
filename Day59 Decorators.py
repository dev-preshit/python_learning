"""
    Day 59 is about Decorators in python...
        A decorator is a function that takes another function as an argument
        and returns a new function that modifies the behavior of the original
        function. The new function is often referred to as a "decorated" function.
        Syntax:
            @decorator_function
            def my_function():
                pass
"""

def greet(fx):
    def mfx(*augs,**kwaugs):
        print("GOOD MORING")
        fx(*augs,**kwaugs)
        print("GOOD NIGHT")
    return mfx
    

@greet
def hello():
    print("Hello world")

@greet
def add(x,y):
    print(x+y)

hello()
# greet(hello)() #Can Also write like this
# GOOD MORING
# Hello world
# GOOD NIGHT

add(10,20)
# greet(add)(10,20) #Can Also write like this
# GOOD MORING
# 30
# GOOD NIGHT