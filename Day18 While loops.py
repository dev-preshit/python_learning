"""
    #day 18 is about while loop in python
        On day 17 we saw what is "for" loop and it use in different situation
        Why we have two types of loop doing same thing..?
        It make programming convinient for programmer as sometimes it is optimal to use 'for loop'
        whereas sometimes it is convenient to use 'while loop'...

        just like most of the programming language while loop expect condition and loops untill its true.
        Syntax:
            initilazation
            while <condition> :
                statement
                updation

        where   initilazation: means giving initial value to looping variable
                condition: is checked and based on its value it is decided weather the loop will execute or not
                updation: means updating looping variable by a certain value...
        eg.
            i = 0
            while i<10:
                print(i)
                i = i + 1

        We can even use the else statement with the while loop. Essentially what
        the else statement does is that as soon as the while loop condition
        becomes False, the interpreter comes out of the while loop and the else
        statement is executed.

        eg.
            i = 0
            while i<10:
                print(i)
                i = i + 1
            else:
                print("End")
"""


# while programe
i = 0
while i<10:
    print(i,end=" ")
    i = i + 1

"""
    Output:
        0 1 2 3 4 5 6 7 8 9
"""
print()



#while can also be executed in reverse
i = 10
while i>0:
    print(i,end=" ")
    i = i - 1

"""
    Output:
       10 9 8 7 6 5 4 3 2 1
"""
print()



#else with while
i = 0
while i<10:
    print(i,end=" ")
    i = i + 1
else:
    print("End")

"""
    Output:
        0 1 2 3 4 5 6 7 8 9 End
"""