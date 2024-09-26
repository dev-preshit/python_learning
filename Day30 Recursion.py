"""
    #Day 30 is about Recursion in python...
        when a function is called within itself it is know as recursion...
        This create a infinity loop as function is caled within itself
        which can be use in make different scenario...
        Syntax:
            def fn_name(n):
                ----------
                ----------
                fn_name(1)
        eg.
            factorial value using recursion  
        def facto(n):
            if n == 0 or n == 1:
                return 1
            else:
                return (n * facto(n-1))
            
"""

#Factorial using recursion 
def facto(n):
            if n == 0 or n == 1:
                return 1
            else:
                return (n * facto(n-1))
n = int(input("Enter a number: "))
print(f"factorial of {n} is {facto(n)}")

"""
Output:
    Enter a number: 5
    factorial of 5 is 120
"""


# Fibonacci series using Recursion
def fibo(n):
    if n==0:
        return 0
    elif n == 1:
        return 1
    else:
        return (fibo(n-2) + fibo(n-1))

n = int(input("Enter a number: "))
for i in range(n):    
    print(fibo(i),end = ",")

"""
Output:
    Enter a number: 5
    0,1,1,2,3,
"""