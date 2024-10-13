"""
        # Day 61 is about Inheritance in Python...
        Using one class's variables and methods in another class is
        the general idea of Inheritance.
        The class from which the variables and methods are inherited 
        is called the Parent class or Base class, and the class which is using these properties
        is called the Child class or Derived class, respectively.
        
        class BaseClass:
            pass
        class DerivedClass(BaseClass):
            pass 

        The Derived class inherits features from the Base class, where new features can
        be added to it. This results in code reusability.

"""

class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id
    
    def show(self):
        print(f"The name of Employee {self.id} is {self.name}")

class Programmer(Employee):
    def add(self, x, y):
        return x + y
    
e = Employee("Narendra", 420)
e.show()
p2 = Programmer("Ramcharan", 123)
print(p2.add(10, 20))
p2.show()  
# 'show' is a method of the Employee class, but we are able to use it with an object of the Programmer class.
