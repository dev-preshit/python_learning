"""
    #Day 58 is about Constructors in Python...
        A constructor is a function in class which is called automatically
        when a object is created.
        This function is generally use to initilise the value we want
        at the time of object creation.
        To create a constructor we have to use __init__() keyword
        eg.
            def __init__()
"""

class Person:
    def __init__(self,nm,age):
        self.name = nm
        self.age = age

    def info(self):
       print(f'{self.name} is {self.age} year old')

a = Person('ram',15) 
a.info()
# ram is 15 year old