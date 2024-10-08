"""
    #Day 54 is about difference between is keyword and double equal to in python...
        'is' vs '=='
        Is and == both are cpmparing opeators i.e they check two value are equal or not.
        However there are some key difference between them...

        The 'is' operator compares the identity of two objects, while the '==' operator compares 
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

print(a == b)  #True '==' => check if two variables have the same value
print(a is b)  #True 'is' => check if two variables point to the same object.

print(a == c)  #True  '==' => check if two variables have the same value
print(a is c)  #False 'is' => check if two variables point to the same object.