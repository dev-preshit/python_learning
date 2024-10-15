"""
    #Day 54 is about the difference between the 'is' keyword and '==' in Python...
        'is' vs '=='
        'is' and '==' are both comparing operators, i.e., they check whether two values are equal.
        However, there are some key differences between them...

        The 'is' operator compares the identity of two objects, while '==' compares 
        the values of the objects. This means that 'is' will only return True if the objects 
        being compared are the exact same object in memory, while '==' will return True if the 
        objects have the same value.

        is operator:
            • Checks if two variables refer to the same object in memory.
            • It compares the identity of the objects. 

        == operator:
            • Checks if two variables have the same value.
            • It compares the contents of the objects.
"""
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a == b)  # True '==' => checks if two variables have the same value
print(a is b)  # True 'is' => checks if two variables point to the same object.

print(a == c)  # True  '==' => checks if two variables have the same value
print(a is c)  # False 'is' => checks if two variables point to the same object.
