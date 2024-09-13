"""
    #day 9 is about Typecasting in python
        Typecasting is process in programming luanguage to change datatype of data or variable to another datatype
        eg. 1 is simple number but when we write "1" in double quort it act as a string/char 
        which is not good for operation in python 
        To avoid this error we can do Typecasting 

        NOTE: the Typecasting should be valid and possable for python to conver otherwise it will throw an error
            eg. we cant change any "STRING" to number...
        
        in python there are two type of Typecasting 
            i) Explicit Typecasting
            ii)Implicit Typecasting

        1)Explicit Typecasting
            when a programmer change one datatype to another manually as per the requirement 
            than it is concidered as Explicit Typecasting...  
            programmer can do this using function 
                int(),float(),hex(),oct(),str(),ect...
        
        2)Implicit Typecasting 
            when ptyhon interpreter change datatype from lower order to higher order to prevent data lose by it self 
            than it is concidered as Implicit Typecasting...
            no need to use any function to do so...

"""

#Explicit typecasting
a = "1"
b = "2"

print("without typecasting: ",a+b)

a = int(a)
b = int(b)

print("with typecasting: ",a+b)
print(type(a),type(b),end="\n\n")

"""
    OUTPUT:
        without typecasting:  12
        with typecasting:  3
        <class 'int'> <class 'int'>
"""


#Inplicit Typecasting
a = 1.23
b = 4

print(type(a),type(b))
c = a+b
print("with typecasting: ",c)
print(type(c))

"""
    OUTPUT:
        <class 'float'> <class 'int'>
        with typecasting:  5.23
        <class 'float'> 
"""