"""
    #day 16 is about match case statement in python
        this is another decision making statement use to make decision in python
        it is similar as switch case statement in c

        Syntax:
            match x:
                case 1:
                    statement
                case 2:
                    statement
                case 3:
                    statement
                case _:
                    statement

        a match statement will compare a given vaiable's value to different shapes. 
        The main idea is to keep on comparing the variable with all the present patterns until it fits into one.

"""

a = int(input("enter a number: "))

match a:
    case 0:
        print("You press Zero")
    case 1:
        print("You press One")
    case 2:
        print("You press Two")
    case _:
        print("Not yet define")

"""
    Output:
        enter a number: 0
        You press Zero 

        enter a number: 1
        You press One 

        enter a number: 2
        You press Two 
         
        enter a number: 3
        Not yet define
"""
    