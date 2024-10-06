"""
    #Day 48 is about Global and Local variable in Python...
        Global variables are the varibles which are acessable through out the whole code
        while Local variable can only be access in a function 
        Variable which are declared inside a function is local vaiable which are only accessable
        in that function only , but is we declare a variable outside of function than we can use 
        that variable inside function as long it is not declared in function to making 
        it a global variable...
        
        What if we want to change value on global variable inside function
        we can do so by using global keyword
        Global Keyword is use as prefix to variable which tell that the variable is 
        not declared in function but the global variable is been used...
"""
x = 10
print(x)

# 10
print(f" global x is {x}")
#  global x is 10

y = 5
print(f" global y is {y}")
#  global y is 5

def hello():
    x = 20
    global y
    y = y + 2
    print(f"    local x is {x}")
#     local x is 20
    print(f"    global y is {y}")
#     global y is 7
    print("    i am inside function")
#     i am inside function

hello()

print(f" global x is {x}")
#  global x is 10

print(f" global y is {y}")
#  global y is 7