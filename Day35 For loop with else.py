"""
    # Day 35 is about For loop with else in Python...
        Python allows the else keyword to be used with the for and
        while loops as well. The else block appears after the body of the
        loop. The statements in the else block will be executed after all
        iterations are completed. The program exits the loop only after
        the else block is executed.
        
        Example: 
            for i in range(5):
                print(i)
            else:
                print("Loop ended")

        But what if there is a break statement in the for loop?
        
        Example:
            for i in range(5):
                print(i)
                if i == 3:
                    break
            else:
                print("Loop ended")
"""

# For else loop
for i in range(5):
    print(i, end=",")
else:
    print("Loop ended")
# Output: 0,1,2,3,4,Loop ended

# Break statement
for i in range(5):
    print(i, end=",")
    if i == 4:
        break
else:
    print("Loop ended")
# Output: 0,1,2,3,4,

for x in range(5):
    print(f"Iteration no {x + 1} in for loop")
else:
    print("Else block in loop")
print("Out of loop")

# Output:
# Iteration no 1 in for loop
# Iteration no 2 in for loop
# Iteration no 3 in for loop
# Iteration no 4 in for loop
# Iteration no 5 in for loop
# Else block in loop
# Out of loop
