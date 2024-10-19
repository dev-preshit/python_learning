"""
    #Day 74 is about method overriding in python...
        Where ever we create same method in child class 
        which is already present in parent class that it is considered as 
        method overriding...

         
"""
class Animal:
    def walk(self):
        print("animal walks")
    
class Dog(Animal):
    def walk(self):
        super().walk()
        print("Dog walks")
        
class Cat(Animal):
    def walk(self):
        super().walk()
        print("Cat walks")


d = Dog()
c = Cat()

d.walk()
print()
c.walk()