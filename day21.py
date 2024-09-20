"""
    #day 21 is about Function Arguments in Python...
        Sometimes programmer have to pass some value to function for its operations
        This can be done using Arguments 

        Arguments are basically a list of variable which we declare at the time of 
        function defineing in brackets which can be feather use in function...
        eg. 
            def function(argunments list)

        arguments are divided into 4 types...
        • Default Arguments
        • Keyword Arguments
        • Required Arguments
        • Variable length Arguments

        1) Default arguments:
            We can provide a default value while creating a function. This
            way the function assumes a default value even if a value is not
            provided in the function call for that argument...

        2) Keyword arguments:
            We can provide arguments with key = value pair, this way the
            interpreter recognizes the arguments by the parameter name.
            Hence, the order in which the arguments are passed does
            not matter...

        3) Required arguments:
            In case we don't declare the arguments with a key = value pair syntax,
            then it is necessary to pass the arguments in the correct
            positional order and the number of arguments passed should
            match with actual function definition.

        4)Variable-length arguments:
            Sometimes we may need to pass more arguments than those
            defined in the actual function. This can be done using variable-length arguments.

            There are two ways to achieve this:
            
            i)Arbitrary Arguments:
                While creating a function, pass a * before the parameter name
                while defining the function: The function accesses the
                arguments by processing them in the form of tuple.
                eg.
                    def function(*argument)
                
            ii)Keyword Arbitrary Arguments:
                While creating a function, pass a ** before the parameter name
                while defining the function. The function accesses the
                arguments by processing them in the form of dictionary.
                eg.
                    def function(**argument)

        Return statement:
            The return statement is used to return the value of the
            expression back to the calling function.
            eg.
                def function(argument list)
                    block of code
                    return <variable/operation>

                a = function(argument list)

"""

# Default Arguments
def mean(a=10,b=20):
    print(f"The mean of {a} and {b} is",(a+b)/2)

mean()      #The mean of (10) and (20) is 15.0
mean(30,23) #The mean of 30 and 23 is 26.5
mean(a=20)  #The mean of (20) and 20 is 20.0
mean(b=20)  #The mean of 10 and (20) is 15.0

#Keyword Arguments
def avg(a=10,b=20):
    print(f"The mean of {a} and {b} is",(a+b)/2)

avg(a=87,b=12)  #The mean of 87 and 12 is 49.5
avg(b=23,a=54)  #The mean of 54 and 23 is 38.5

#Required Argments
def average(a,b):
    print(f"The mean of {a} and {b} is",(a+b)/2)

average(87,12)  #The mean of 87 and 12 is 49.5
average(23,54)  #The mean of 54 and 23 is 38.5

#Variable-length arguments
#i)Arbitrary Arguments
def allAvg(*numbers):
    sum = 0
    for i in numbers:
        print(i,end = ",")
        sum = sum + i
    print("Average is:",sum/len(numbers))

allAvg(23,42,341,23,4,23,5,12,43,4) #23,42,341,23,4,23,5,12,43,4 Average is: 52.0
#ii)Keyword Arbitrary Arguments

def car(**cars):
    print(f"Car: {cars["name"]} ,Color: {cars["color"]} ,Top Speed: {cars["Tspeed"]}")        

car(name="tata",color="red",Tspeed=250) #Car: tata ,Color: red ,Top Speed: 250

#Return statement
def adder(a,b):
    return a+b
a=123
b=456    
ans=adder(a,b)  
print(f"Sum of {a} and {b} is",ans)     #Sum of 123 and 456 is 579