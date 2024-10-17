"""
    # Day 70 is about using Class Methods as Alternative Constructors in Python.

    When using a class, we often need to initialize some parameters, but due to the input style, 
    we can't do so directly. Therefore, we first need to decode the format of the input 
    and then pass it to the constructor, which can make the main file messy.

    To avoid this, we use class methods to decode the input format and pass the returned value 
    from these methods to the constructor.
"""
class Student:
    def __init__(self,name,age) -> None:
        self.name = name
        self.age = age

    @classmethod
    def fromspaceStr(cls,String):
        return cls(String.split(" ")[0],int(String.split(" ")[1])) # will split string from space and return
    
    @classmethod
    def fromUnderStr(cls,String):
        return cls(String.split("_")[0],int(String.split("_")[1])) # will split string from Under scroll and return
    
    @classmethod
    def fromcommaStr(cls,String):
        return cls(String.split(",")[0],int(String.split(",")[1])) # will split string from comma and return
    

str1 = "Rani 30"
s1 = Student.fromspaceStr(str1)
print(s1.name,s1.age)

str2 = "Rani_30"
s2 = Student.fromUnderStr(str2)
print(s2.name,s2.age)

str3 = "Rani,30"
s3 = Student.fromcommaStr(str3)
print(s3.name,s3.age)