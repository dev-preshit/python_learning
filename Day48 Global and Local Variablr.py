"""
    # Day 48 is about Global and Local variables in Python...
        Global variables are the variables that are accessible throughout the whole code,
        while local variables can only be accessed within a function.
        Variables that are declared inside a function are local variables, which are only accessible
        within that function. However, if we declare a variable outside of a function, we can use 
        that variable inside the function as long as it is not redeclared in the function, 
        making it a global variable...
        
        What if we want to change the value of a global variable inside a function?
        We can do so by using the global keyword.
        The global keyword is used as a prefix to a variable to indicate that the variable is 
        not declared in the function but is a global variable being used...
"""

x = 10
print(x)  # 10
print(f"Global x is {x}")  # Global x is 10

y = 5
print(f"Global y is {y}")  # Global y is 5

def hello():
    x = 20
    global y
    y = y + 2
    print(f"    Local x is {x}")  # Local x is 20
    print(f"    Global y is {y}")  # Global y is 7
    print("    I am inside the function")  # I am inside the function

hello()

print(f"Global x is {x}")  # Global x is 10
print(f"Global y is {y}")  # Global y is 7
