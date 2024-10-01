"""
    #Day 38 is about Raising Custom Errors in Python...
        Sometimes we have to rise error to stop flow of program 
        which will stop fearther malfunction...
        This can be done using raise keyword.
        eg.
            if condition:
                raise ValueError("error-note")

        We can also define a Custom Exception
            In Python, we can define custom exceptions by creating
            a new class that is derived from the built-in Exception
            class...
            eg.
                class CustomError(Exception):
                    #code...
                    pass
                try:
                    #code...

                except CustomError:
                    #code...
"""

a = int (input("Enter any value between 5 to 9: "))

if a<5 or a>9:
    raise ValueError("Value should be between 5 to 9")

"""
    Output:
        Enter any value between 5 to 9: 2
        Traceback (most recent call last):
          File "d:\git\python_learning\Day38 Raising custom errors.py", line 28, in <module>
            raise ValueError("Value should be between 5 to 9")
        ValueError: Value should be between 5 to 9
"""

a = input("Enter quit to proceed: ")

if a == "quit":
    print("Alright quiting")
else:
    raise NameError("You should enter quit to proceed")
"""
    Output:
        Enter quit to proceed: dev 
        Traceback (most recent call last):
          File "d:\git\python_learning\Day38 Raising custom errors.py", line 44, in <module>
            raise NameError("You should enter quit to proceed")
        NameError: You should enter quit to proceed
"""

