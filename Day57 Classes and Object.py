"""
    #Day 57 is about Classes and Object in Python...
        Class can be defined as follow
        Syntax.
            class class_name:
                <instance variable>
                <Class member funcition>
        eg.
            class Person:
                name = None
                age = 0
                def work(x):
                    # code
                

        Object can be created as follow
        Syntax.
            obj_name1 = Class()
            obj_name2 = Class()
        eg.
            vikas = Person()
            Abbaj = Person()

        Accessing class variable
        Syntax.
            obj_name.<instance variable>
            obj_name.<Class member funcition>
        eg.
            vikas.name = 'Vikas'
            vikas.age = 37
            vikas.work(x)

            Abbaj.name = 'Abbaj'
            Abbaj.age = 43
            Abbaj.work(x)
"""

class Details:
    name = 'Ram'
    age = 21
    def display(self):
        print(f"{self.name} is {self.age} year old")

person1 = Details()
person2 = Details()

person1.name = 'Charan'
person1.age = 20

person2.name = 'Ganesh'
person2.age = 21

person1.display()   # Charan is 20 year old
person2.display()   # Ganesh is 21 year old