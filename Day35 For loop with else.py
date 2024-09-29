"""
    # Day 35 is about For loop with else in python...
        Python allows the else keyword to be used with the for and
        while loops too. The else block appears after the body Of the
        loop. The statements in the else block will be executed after all
        iterations are completed. The program exits the loop only after
        the else block is executed.
        eg. 
            for i in range(5):
                print(i)
            else:
                print("Loop ended")

        But what if there is a break statement in for loop...
        eg. 
            for i in range(5):
                print(i)
                if i == 3:
                    break
            else:
                print("Loop ended")
"""
#For else loop
for i in range(5):
    print(i,end=",")
else:
    print("Loop ended")
# 0,1,2,3,4,Loop ended

# break statement
for i in range(5):
    print(i,end=",")
    if i == 4:
        break
else:
    print("Loop ended")
# 0,1,2,3,4,

for x in range(5):
    print ("iteration no {} in for loop".format(x+1) )
else:
    print ("else block in loop")
print ("Out of loop")

# iteration no 1 in for loop
# iteration no 2 in for loop
# iteration no 3 in for loop
# iteration no 4 in for loop
# iteration no 5 in for loop
# else block in loop
# Out of loop