"""
        # Day 57 is about Classes and Objects in Python...
        A class can be defined as follows:
        Syntax:
            class class_name:
                <instance variable>
                <class member function>
        e.g.:
            class Person:
                name = None
                age = 0
                def work(self):  # Added 'self' as the first parameter
                    # code
                

        Objects can be created as follows:
        Syntax:
            obj_name1 = Class()
            obj_name2 = Class()
        e.g.:
            vikas = Person()
            abbaj = Person()  # Capitalized name for consistency

        Accessing class variables:
        Syntax:
            obj_name.<instance variable>
            obj_name.<class member function>
        e.g.:
            vikas.name = 'Vikas'
            vikas.age = 37
            vikas.work()  # Removed 'x' since it's not defined

            abbaj.name = 'Abbaj'
            abbaj.age = 43
            abbaj.work()  # Removed 'x' since it's not defined

"""

class Details:
    name = 'Ram'
    age = 21

    def display(self):
        print(f"{self.name} is {self.age} years old")  # Changed "year" to "years" for grammatical correctness

person1 = Details()
person2 = Details()

person1.name = 'Charan'
person1.age = 20

person2.name = 'Ganesh'
person2.age = 21

person1.display()   # Charan is 20 years old
person2.display()   # Ganesh is 21 years old
