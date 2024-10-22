"""
    #Day 77 is about Operator Overloding in python... 
    Operator Overloading is a feature in Python that allows
    developers to redefine the behavior of mathematical and
    comparison operators for custom data types. This means
    that you can use the standard mathematical operators (+, -,
    *, /, etc.) and comparison operators (>, <, ==, etc.) in your
    own classes, just as you would for built-in data types like int,
    float, and Str.
"""

class Vector:
    def __init__(self,i,j,k) -> None:
        self.i = i
        self.j = j
        self.k = k
    
    def __str__(self) -> str:
        return f"{self.i}i + {self.j}j + {self.k}k"
    
    def __add__(self1,self2):
        return Vector(self1.i+self2.i,self1.j+self2.j,self1.k+self2.k)
    
v1 = Vector(1,9,3)
print(v1)

v2 = Vector(5,2,7)
print(v2)

print(v1 + v2)
