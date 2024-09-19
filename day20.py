"""
    #day 20 is about function in python
        functions are basically a seprate block of code which is define by programmer
        We can reuse the same block of code by calling it wherever it is needed...
        this can save lot of time and memory space as we have to write code once and can use it 
        wherever and whenever we want...

        there are two types of functions:
            1)Build-in function
            2)User-define function
        
        1)Build-in funtion
            Build-in function are already define function is python we dont have 
            to write code for and can be use direclty...
            eg.
                len(),print(),range(),int(),min(),max(),etc...
        
            
        2)User-define funtion 
        User-define funtion have to be declire by programmer before using...

        How to create a function
            def funtion_name(argument list):
                block of code

            now we can call this function using function_name and passing argument
            NOTE:argument list can be empty to but you have to put "()" after function_name
"""

#lets create a funtion to add two number

def adder(a,b): #this is function defination
    print(a+b)  #this is function declaration

x=10
y=20
adder(12,43)    #this is function calling
adder(x,y)      #this is function calling
p=int(input("Enter number: "))
q=int(input("Enter number: "))
adder(p,q)

"""
    Output:
        55
        30
        Enter number: 5
        Enter number: 6
        11
"""

#lets create a large function to find greater number

def great():    #this is function defination
    a=int(input("Enter number: "))  #this all is function declaration(line 41-46)
    b=int(input("Enter number: "))  
    if a > b:
        print(f"{a} is greater than {b}")
    else:
        print(f"{b} is greater than {a}")

print("1st time")
great()     #this is function calling
print("2nd time")
great()     #this is function calling
print("3rd time")
great()     #this is function calling
"""
    Here we just write code to find greater number once but can use it multiple times

    Output:
        1st time
        Enter number: 58
        Enter number: 98
        98 is greater than 58

        2nd time
        Enter number: 54
        Enter number: 657
        657 is greater than 54

        3rd time
        Enter number: 3658
        Enter number: 48544 
        48544 is greater than 3658
"""
    
"""
    In programming programmer have freedom to declare funtion later but have to define above main code
    It could be done so by using "pass" keyword
    eg...
        def sum()
            pass
        
    we will see how to write this in feather lecture
"""
