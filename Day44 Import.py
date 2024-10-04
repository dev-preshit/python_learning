"""
    #Day 44 is about how import works in Python...
        Importing in Python is the process of loading code from a Python module into the current script.
        his allows you to use the functions and variables defined in the module in your current script, as
        well as any additional modules that the imported module may depend on.

        To import a module in Python, you use the import statement followed by the name of the module.
        For example, to import the math module, which contains a variety of mathematical functions, you
        would use the following statement:
        eg.
            import math

        Once a module is imported, you can use any of the functions and variables defined in the module
        by using the dot notation.
        eg.
            result = math.sqrt(9)
            print(result)

        If we want a specific function from a module suppose sqrt ot curt 
        which will remove the need to write math. and make it ez to use...
        eg.
            from math import sqrt, cbrt

        It's also possable to import all the function and variable using *
        which stand for all...
        eg. 
            from math import *
        however it is not recommended to do so as it increase confusion...

        as keyword
        we can create a alias by using \'as\' while importing
        eg.
            import math as m
        
        now we can use m. at the place of math.

        by using dir we can see all function and variable present in module
        eg.
            dir(module_name)
"""
#inporting math module
import math

#With math.
result = math.sqrt(9)
print(result)

#import function sqrt and cbrt from math
from math import sqrt, cbrt

#Without math.
result = cbrt(64)
print(result)

#import all function and variable from math
from math import *

#import module using as
import math as m

result = m.pow(m.pi,2)
print(result)

print(dir(math))
