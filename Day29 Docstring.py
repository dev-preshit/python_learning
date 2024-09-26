"""
    #Day29 is about DocSting in python...
        • Docstrings in python
            Python docstrings are the string literals that appear
            right after the definition of a function, method, class,
            or module.
            eg.
                def value(n):
                    '''This is Docstring which is not comment and 
                    python interpreter store this string in doc attribute'''
                    print(n)
                value(5)
                print(value.__doc__)
"""

def value(n):
    '''This is Docstring which is not comment and 
python interpreter store this string in doc attribute'''
    print(n)

value(5)
print(value.__doc__)

"""
    Output:
        5
        This is Docstring which is not comment and 
        python interpreter store this string in doc attribute
"""