"""
    #Day80 is about Multilevel Inheritance in python...
        When-ever we inherite a child class into another child class
        than it is considered as multilevel inheritance.

        In Python, multilevel inheritance is achieved by using the class
        hierarchy. The syntax for multilevel inheritance is quite simple and
        follows the same syntax as single inheritance.
"""

class Vehical:
    def __init__(self,type):
        self.type = type
    
    def Show(self):
        print(f"Vehical type {self.type}")
    
class Car(Vehical):
    def __init__(self,type,model):
        self.model = model
        Vehical.__init__(self,type)
    
    def Show(self):
        Vehical.Show(self)
        print(f"Vehical type {self.model}")

class model(Car):
    def __init__(self,type,model,color):
        self.color = color
        Car.__init__(self,type,model)
    
    def Show(self):
        Car.Show(self)
        print(f"Vehical color {self.color}")

m = model("Car","Tata","Tiago")
print(m.Show())
print(model.mro())