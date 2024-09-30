"""
    #Day 36 is about Exception Handling in python...
        Whenever python catch an error in program it stop 
        feather flow of execution for solving it we use Exception Handling

        Exception Handling is use to catch an error and not effect the
        flow of program ever if the unexpected error occur...
        
        We use try except keyword for doing so
        eg.
            try:
                Code where there is possablity of error occurring
            
            execpt Exception as e:
                print(e)
    
        We can also handle any specific type of error like
            IndexError
            ValueError
            Etc..
"""
#following code will have exception so i will comment it 
"""
n = input("Enter a number: ")
print("Table of ",n)

for i in range(1,11):
    print(f"{int(n)} X {i} = {int(n)*i}")
    print("End of loop")
print("End of code")
"""
"""
Output:
    Enter a number: dev
    Table of  dev
    Traceback (most recent call last):
      File "d:\git\python_learning\Day36 Exception Handling.py", line 22, in <module>
        print(f"{int(n)} X {i} = {int(n)*i}")
                 ^^^^^^
    ValueError: invalid literal for int() with base 10: 'dev'
"""

n = input("Enter a number: ")
print("Table of ",n)
try:
    for i in range(1,11):
        print(f"{int(n)} X {i} = {int(n)*i}")
        print("End of loop")

except Exception as e:
        print("Unexpected error:",e)

except ValueError:
    print("SORRY")

print("End of code")

"""
    Output:
        Enter a number: dev
        Table of  dev
        Unexpected error: invalid literal for int() with base 10: 'dev'
        End of code
"""