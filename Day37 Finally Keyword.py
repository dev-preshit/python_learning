"""
    # Day 37 is about the Finally Keyword in Python...
        The finally keyword is used alongside try..except...
        The specialty of the finally block is that regardless of whether
        an error occurs or not, the content inside this block will execute.
        
        Example:
            n = input("Enter a number: ")
            print("Table of", n)
            try:
                for i in range(1, 11):
                    print(f"{int(n)} X {i} = {int(n) * i}")

            except Exception as e:
                print("Unexpected error:", e)
            
            finally:
                print("This is the finally block:")
                
            print("End of code")
        
        It is generally useful while using functions.
        
        Example:
            def func1():
                try:
                    l = [1, 2, 4, 6]
                    i = int(input("Enter the index"))
                    print(l[i])
                    return 1
                except:
                    print("Some error occurred")
                    return 0
                finally:
                    print("I am always executed")
            
            x = func1()
            print(x)
"""

n = input("Enter a number: ")
print("Table of", n)
try:
    for i in range(1, 11):
        print(f"{int(n)} X {i} = {int(n) * i}")

except Exception as e:
    print("Unexpected error:", e)
            
finally:
    print("This is the finally block:")
                
print("End of code")

# Output: 
# Enter a number: 10
# Table of 10
# 10 X 1 = 10
# 10 X 2 = 20
# 10 X 3 = 30
# 10 X 4 = 40
# 10 X 5 = 50
# 10 X 6 = 60
# 10 X 7 = 70
# 10 X 8 = 80
# 10 X 9 = 90
# 10 X 10 = 100
# This is the finally block:
# End of code