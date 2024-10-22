"""
    #Day 78 is Single Inheritance in python...
        We have allready seen it at the time of Inheritance(Day 61)
        
        Single inheritance is a type of inheritance where a class inherits
        properties and behaviors from a single parent class. This is the simplest
        and most common form of inheritance.
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