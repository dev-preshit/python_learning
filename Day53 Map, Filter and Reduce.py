"""
    # Day 53 is about Map, Filter, and Reduce in Python...
        In Python, the map, filter, and reduce functions are built-in functions that allow
        you to apply a function to a sequence of elements and return a new sequence.

        map():
            The map function applies a function to each element in a sequence and returns
            a new sequence containing the transformed elements.
            Syntax:
                map(function, iterable)
            Lambda functions will also work...
            It will return a map object, which will need to be typecast into a list, tuple, or set.

        filter():
            The filter function filters a sequence of elements based on a given predicate (a
            function that returns a boolean value) and returns a new sequence containing
            only the elements that meet the predicate. 
            Syntax:
                filter(predicate, iterable)
            Lambda functions will also work...
            It will return a filter object, which will need to be typecast into a list, tuple, or set.
        
        reduce():
            The reduce function is a higher-order function that applies a function to a
            sequence and returns a single value. It is part of the functools module in Python.
            Syntax:
                reduce(function, iterable)
            Lambda functions will also work...
            It will return a reduced value and will not need to be typecast into a list, tuple, or set
            as it is a single value.
"""

# MAP() FUNCTION
def cube(x):
    return x * x * x

l = [1, 2, 3, 4, 5]

# newl = []
# for i in l:
#     newl.append(cube(i))
# [1, 8, 27, 64, 125]

Mapl = list(map(cube, l))
# [1, 8, 27, 64, 125]
print(Mapl)
# Both will give the same answer, but the length of code is reduced.



# FILTER() FUNCTION
def filter_fx(x):
    return x > 0

l = [1, -7, 0, -4, 5]

# Fill = []
# for i in l:
#     if True == filter_fx(i):
#         Fill.append(i)
# [1, 5]

Fill = list(filter(filter_fx, l))
# [1, 5]
print(Fill)
# Both will give the same answer, but the length of code is reduced.



# REDUCE() FUNCTION
from functools import reduce
 
def pro(x, y):
    return x * y

l = [1, 2, 3, 4, 5]
Redl = reduce(pro, l)
print(Redl)
# 120
