"""
    # Day 42 is about Enumerate Function in Python...
        The enumerate function is a built-in function in Python that allows
        you to loop over a sequence (such as a list, tuple, or string) and get
        the index and value of each element in the sequence at the same
        !ime. Here's a basic example of how it works.
        eg.
            marks = [23,45,67,89,100,54,78]

            for index, mark in enumerate(marks):
                print(f"{mark} on index {index}")
        
        By default, the enumerate function starts the index at O, but you can
        specify a different starting index by passing it as an argument to the
        enumerate function:
        
            fruits = ['apple','mango','banana']

            for index, fruit in enumerate(fruits,start=1):
                print(f"{index} => {fruit}")
            
"""

marks = [23,45,67,89,100,54,78]

for index, mark in enumerate(marks):
    print(f"{mark} on index {index}")

"""
Output:
    23 on index 0
    45 on index 1
    67 on index 2
    89 on index 3
    100 on index 4
    54 on index 5
    78 on index 6
"""

fruits = ['apple','mango','banana']

for index, fruit in enumerate(fruits,start=1,):
    print(f"{index} => {fruit}")

"""
Output:
    1 => apple
    2 => mango
    3 => banana
"""