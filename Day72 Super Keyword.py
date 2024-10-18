"""
    #Day 72 is about Super Keyword in python...
        The super() keyword in Python is used to refer to the parent class.
        It is especially useful when a class inherits from multiple parent
        classes and you want to call a method from one of the parent
        classes.

"""
class parent:
    def __init__(self,name,age) -> None:
        self.name = name
        self.age = age
        
    def parent_method(self):
        print("Parent class")
    
class child(parent):
    def __init__(self, name, age,lang):
        super().__init__(name, age)
        self.lang = lang

    def parent_method(self):
        print(f"{self.name}, {self.age}, {self.lang}")

    def child_method(self):
        print("Child class")
        super().parent_method()

    
obj = child("Lalu",54,"python")
obj.parent_method()
obj.child_method()
