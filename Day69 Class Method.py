"""
    #Day 69 is about Class Methods in Python...
        Just like class variable, a class method is a method that is associated 
        with the class itself rather than any specific object of the class. This 
        means it operates on the class as a whole rather than on individual objects. 
        Class methods are defined using the @classmethod decorator, followed by the 
        method definition. The first parameter of the method is always cls, which 
        represents the class itself.
"""

class Employee:
    company_name = "Ram_coolers"

    def __init__(self, name):
        self.name = name        
        self.salary = 10000      

    def showDetails(self):
        print(f"Name of employee is {self.name}, having salary ${self.salary} and works for {self.company_name}")

    @classmethod
    def changeCompany(cls,newcompany):
        cls.company_name = newcompany
    
e1 = Employee("Dev")
e1.showDetails()
e1.changeCompany("Tesla")
e1.showDetails()

