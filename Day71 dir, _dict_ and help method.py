"""
    #day 71 is about dir(), __dice__ and help() methods in python...
    Whenever we import a new module in python we don't know anything about it
    except some basic function/ Variable but we can get to know about lots of
    info a module carry by using dir(), __dice__() and help() methods

    dir():   
        The dir() function returns a list of all the attributes and
        methods (including dunder methods) available for an object. It is a
        useful tool for discovering what you can do with an object.

    __dict__: 
        The __dict__ attribute returns a dictionary representation 
        of an object's attributes. It is a useful tool for introspection.

    help():
        The help() function is used to get help documentation for
        an object, including a description of its attributes and methods.
"""



class person:
    def __init__(self,Name,age,gender):
        self.name = Name
        self.age = age
        self.gender = gender

# dir()
m = person("Sahil",17,"M")
print(dir(m))

# __dict__
print(m.__dict__)

#help()
print(help(m))
print(help(person))