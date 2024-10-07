"""
    #Day52 is about lambda function in python...
        In Python, a lambda function is a small anonymous function without a name.
        It is defined using the lambda keyword 
        syntax:
            lambda arguments: expression

        We can also pass function into function as arguments
        
"""
# function using def 
def double(x):
    return x*2

print(double(5))
# 10

#function using lambda
twice = lambda x: x*2
print(twice(10))
# 20

avg = lambda x,y,z: (x+y+z)/3
print(avg(10, 20, 30))
# 20

#Function passed in function
def apply(fx , value):
    return fx(value) * fx(value-1)

print(apply(double, 5))
# 80

#we can also pass lambda function instead proper function
print(apply(lambda x:x*2, 5))
# 80 