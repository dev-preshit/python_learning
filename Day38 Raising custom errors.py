"""
    # Day 38 is about Raising Custom Errors in Python...
        Sometimes we have to raise an error to stop the flow of a program,
        which will prevent further malfunction.
        This can be done using the raise keyword.
        
        Example:
            if condition:
                raise ValueError("error message")

        We can also define a Custom Exception.
        In Python, we can define custom exceptions by creating
        a new class derived from the built-in Exception class.
        
        Example:
            class CustomError(Exception):
                # code...
                pass
            
            try:
                # code...
            except CustomError:
                # code...
"""

a = int(input("Enter any value between 5 and 9: "))

if a < 5 or a > 9:
    raise ValueError("Value should be between 5 and 9")

# Output:
# Enter any value between 5 and 9: 2
# Traceback (most recent call last):
#   File "Day38 Raising custom errors.py", line 28, in <module>
#     raise ValueError("Value should be between 5 and 9")
# ValueError: Value should be between 5 and 9

a = input("Enter 'quit' to proceed: ")

if a == "quit":
    print("Alright, quitting")
else:
    raise NameError("You should enter 'quit' to proceed")

# Output:
# Enter 'quit' to proceed: dev 
# Traceback (most recent call last):
#   File "Day38 Raising custom errors.py", line 44, in <module>
#     raise NameError("You should enter 'quit' to proceed")
# NameError: You should enter 'quit' to proceed
