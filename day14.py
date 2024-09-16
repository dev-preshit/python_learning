"""
    #day 14 is about if else statement
        whenever programmer have to make decision amoung 2 different statement or more than 2 statement 
        might be 2,3,4 or 100 too...
        than programmer will use if else statement

        base on cases this if else statement are fearther divided into 4 parts
        1) simple if
        2) if else
        3) if elif else
        4) nested if else

        #SIMPLE IF
            The simple if statement in python is decision-making statement use to 
            execute a block of code based on condition...
        
        Syntax:
            if condition :
                if condition is true than this statement will execute

        #IF-ELSE
            The if else statement is use to decision among two condition either the
            condition will be true or false...

        Syntax:
            if condition :
                if condition is true than this statement will execute
            else :
                if condition is false than this statement will execute

        #IF-ELSE-ELIF
            The elif statement is use when there is more than 2 condition
            to be check to execute correct block...
            elif block is basically else if in 'C'

        Syntax:
            if condition :
                if condition is true this block will executed
                else it will go to elif (next) block
            elif condition :
                if condition is true this block will executed
                else it will go to elif (next) block
            elif condition :
                if condition is true this block will executed
                else it will go to else (last) block
            else :
                if all condition is false than this statement will execute

        #NESTED IF ELSE
            The statement is considered as nested if else when there are
            if-else-elif within if...

        Syntax:
            if condition :
                if condition:
                    if condition of outer if and inner if both are true 
                    than this block will be executed
                else :
                    if condition of outer if is true and inner if is false
                    than this block will be executed
            else :
                if condition:
                    if condition of outer if is false and inner if is true
                    than this block will be executed
                else :
                    if condition of outer if and inner if both are false
                    than this block will be executed
        
        NOTE: in every above statement only one block can be execited anytime you check condition...
    
"""
# simple if
a = int(input("Enter a number: "))

if a == 0 :
    print("Entered number is zero (0)")

"""
    Output:
        Enter a number: 0
        Entered number is zero (0)

        Enter a number: 10
"""

# if-else
age = int(input("Enter your age"))
print("your age is ",age)

if age >= 18 :
    print("You can vote")
else :
    print("You cannot vote")

"""
    Output:
        Enter a number: 20
        You can vote

        Enter a number: 10
        You cannot vote
"""

a = int(input("Enter a number: "))

if a < 0:
    print("Number is -ve")
elif a == 0:
    print("Number is 0")
else :
    print("Number is +ve")

"""
    Output:
        Enter a number: -10
        Number is -ve

        Enter a number: 0
        Number is zero

        Enter a number: 10
        Number is +ve
"""

a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
c = int(input("Enter a number: "))

if a > b:
    if a > c:
        print(a," is greater")
    else :
        print(c," is greater")
else :
    if b > c:
        print(b," is greater")
    else :
        print(c," is greater")

"""
    Output:
        Enter a number: 12    
        Enter a number: 123    
        Enter a number: 1234

        1234 is greater    
"""