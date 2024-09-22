"""
    #day 17 is about for loop in python...
        sometimes you have to repeat certain task repetadely
        which is known as looping.
        This repeting is know as loop in python
        eg. you have to print natural number untill a certain range 
        or to print a string 10 time or 100 times this can be done using loops
        This helps to reduce size of code...

        On day 17 we are learning about for loop
        Syntax:
            for <variable> in range:
                statement
        Eg. 
            name = "Dev-preshit"

            for i in name:
                print(i,end=",")

        In this example we iterate every alphabate on variable 'name' one-by-one
        where 'i' is an looping variable 
        in every loop one alphabate of "Dev-preshit" is getting 
        stored in i sequencially and than been printed by print statement 
        => print(i) 

"""
name = "Dev-preshit"

for i in name:
    print(i,end=",")

"""
    Output:
        D,e,v,-,p,r,e,s,h,i,t
"""
print()
"""

    with that it can also iterate in a list as-well
    eg. 
        colors = ["Red","Green","Blue","Orange"] 
        for color in colors :
            print(color)  

    You can also iterate into a certain range too
    by using range function 
    eg. 
        range(start,end,step)
    Note:End will always be n-1 number i.e. 
    if end = 10 than the range is upto 9 itself

    The start field can also be blank as 
    python will start loop from 0 uptill the 'end' number

    The range() function defaults to increment by one, 
    however it is possible to specify the increment value by 
    adding a third parameter
"""

colors = ["Red","Green","Blue","Orange"] 
for color in colors :
   print(color)
"""
    Output:
        Red
        Green
        Blue
        Orange 
"""
#let print number between 1-10 using for loop
for i in range(1,10+1) : #we use 10+1 as it will only go upto 9
    print(i,end=",")

"""
    Output:
        1,2,3,4,5,6,7,8,9,10,
"""
for i in range(10) :
    print(i,end=",")
    print()

for i in range(0,20,2) :
    print(i,end=",")
"""
    Output:
        0,2,4,6,8,10,12,14,16,18,
"""