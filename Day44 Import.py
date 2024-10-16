"""
    # Day 44 is about how import works in Python...
        Importing in Python is the process of loading code from a Python module into the current script.
        This allows you to use the functions and variables defined in the module in your current script, as
        well as any additional modules that the imported module may depend on.

        To import a module in Python, you use the import statement followed by the name of the module.
        For example, to import the math module, which contains a variety of mathematical functions, you
        would use the following statement:
        eg.
            import math

        Once a module is imported, you can use any of the functions and variables defined in the module
        by using dot notation.
        eg.
            result = math.sqrt(9)
            print(result)

        If we want a specific function from a module, such as sqrt or cbrt, 
        we can import only those, which removes the need to write "math." and makes it easier to use.
        eg.
            from math import sqrt, cbrt

        It's also possible to import all the functions and variables using * 
        which stands for "all."
        eg. 
            from math import *
        However, it is not recommended to do so as it increases confusion.

        'as' keyword:
        We can create an alias by using 'as' while importing.
        eg.
            import math as m
        
        Now we can use 'm.' in place of 'math.'

        By using dir, we can see all functions and variables present in the module.
        eg.
            dir(module_name)
"""

# Importing math module
import math

# With math.
result = math.sqrt(9)
print(result)

# Import function sqrt and cbrt from math
from math import sqrt, cbrt

# Without math.
result = cbrt(64)
print(result)

# Import all functions and variables from math
from math import *

# Import module using as
import math as m

result = m.pow(m.pi, 2)
print(result)

# Display all functions and variables in the math module
print(dir(math))
