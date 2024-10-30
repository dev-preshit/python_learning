"""
    Day 91 is about Generators in python...
        Generators in Python are special type of functions that 
        allow you to create an iterable sequence of values. 
        A generator function returns a generator object, which 
        can be used to generate the values one-by-one as you 
        iterate over it. Generators are a powerful tool for 
        working with large or complex data sets, as they allow 
        you to generate the values on-the-fly, rather than 
        having to create and store the entire sequence in memory.

    Creating a Generator
        In Python, you can create a generator by using the yield statement in a function. 
        The yield statement returns a value from the generator and suspends the execution 
        of the function until the next value is requested.
    
    Using a Generator
        Once you have created a generator, you can use it in a variety of ways, 
        such as in a for loop, a list comprehension, or a generator expression. 
"""
import random as r
def my_generator():
    for i in range(0,30,2):
        yield i

gen = my_generator()
print(next(gen),end=" ")
print(next(gen),end=" ")
print(next(gen),end=" ")
print(next(gen),end=" ")
print(next(gen),end=" ")
print(next(gen),end=" ")
print(next(gen))

gen1 = my_generator()
for i in gen1:
    print(i,end=" ")
