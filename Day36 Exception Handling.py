"""
    # Day 36 is about Exception Handling in Python...
        Whenever Python catches an error in a program, it stops
        the further flow of execution. To solve this, we use Exception Handling.

        Exception Handling is used to catch an error without affecting the
        flow of the program, even if an unexpected error occurs.
        
        We use the try-except keywords for doing so.
        
        Example:
            try:
                Code where there is a possibility of an error occurring
            
            except Exception as e:
                print(e)
    
        We can also handle specific types of errors like:
            IndexError
            ValueError
            etc.
"""

n = input("Enter a number: ")
print("Table of", n)
try:
    for i in range(1, 11):
        print(f"{int(n)} X {i} = {int(n) * i}")
        print("End of loop")

except ValueError as e:
    print("Unexpected error:", e)

print("End of code")

# Output:
# Enter a number: dev
# Table of dev
# Unexpected error: invalid literal for int() with base 10: 'dev'
# End of code
