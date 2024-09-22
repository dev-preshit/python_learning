"""
    #day 10 is about input in python
        In python we can take direct input in file by using "INPUT FUNCTION"( input() )...  
        By default it take input in "string" format but we can change it using typecasting feature (DAY 9)
        Syntax:
            variable = input() ==> < datatype = str >

            variable2 = int(input()) ==> < datatype = int >
            variable3 = float(input()) ==> < datatype = float >

        We can pass string/instruction in input function as argument which will be print on treminal itself
        Syntax:
            variable4 = input("Enter your name: ")
        Output:
            Enter your name:|
        
        
"""

#String input

variable = input("Enter your name: ")
print("Hello my name is",variable)

"""
    OUTPUT: 
        Enter your name: Dev-Preshit
        Hello my name is Dev-Preshit
"""

# Int input

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("ADD:",a+b)

# NOTE: We can do same with float

"""
    OUTPUT: 
        Enter first number: 10
        Enter second number: 20
        ADD: 30
"""