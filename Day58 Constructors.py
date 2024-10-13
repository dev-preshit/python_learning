"""
    # Day 58 is about Constructors in Python...
    A constructor is a function in a class that is called automatically
    when an object is created.
    This function is generally used to initialize the values we want
    at the time of object creation.
    To create a constructor, we have to use the __init__() method.
    e.g.,
        def __init__():

"""

class Person:
    def __init__(self, nm, age):
        self.name = nm
        self.age = age

    def info(self):
       print(f'{self.name} is {self.age} years old')  # Changed "year" to "years" for grammatical correctness

a = Person('Ram', 15) 
a.info()
# Ram is 15 years old
