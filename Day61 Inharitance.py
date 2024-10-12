"""
    #Day 61 is about Inharitance in Python...
        Using one class variable and method into another class is
        a general idea of Inharitance 
        The class from which the variable and methon is been inharite 
        is called Parent class or Base class and The class which is using this properties
        is called Child class or Dericed class resp.
        
        class BaseClass:
            pass
        class DerivedClass(BaseClass):
            pass 

        Derived class inherits features from the base class where new features can
        be added to it. This results in re-usability of code.
"""

class Employee:
    def __init__(self,name,id):
        self.name = name
        self.id = id
    
    def show(self):
        print(f"The name of Employee {self.id} is {self.name}")
class Programmer(Employee):
    def add(self,x,y):
        return x+y
    
e = Employee("Narendra",420)
e.show()
p2 = Programmer("Ramcharan",123)
print(p2.add(10,20))
p2.show()
# show is method of Employee Class but we are able to use it using object of Programmer Class