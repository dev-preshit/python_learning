"""
    #day 11 is about string and some property of sting in python
        anything in single and double quort is concidered as string my python interpreter...
        eg.
            name = "ram"
            fruit = 'apple'

    we can also store multiple line in a single variable by using triple quort...
    eg. 
        para = '''The first approach is by using triple quotes, 
        we should add a triple quote then we can
        add separate line inside the quotes, the multi-line
        string is created.'''

    String is basically a array of text data and same like array there is concept of indexing in string...
    eg. 
        variable = para[index]
    indexing always start from 0 just like c
    we can also access it using loops in future...
"""

name = "ram"
fruit = 'apple'

print("hello, I am ",name)
print("I eat",fruit)
"""
OUTPUT:
    hello i am  ram
    i eat apple    
"""
para = '''The first approach is by using triple quotes, 
we should add a triple quote then we can
add separate line inside the quotes, the multi-line
string is created.'''

print(para)
"""
OUTPUT:
    The first approach is by using triple quotes, 
    we should add a triple quote then we can
    add separate line inside the quotes, the multi-line
    string is created.
"""

r = name[0]
a = name[1]
m = name[2]

print(r)
print(a)
print(m)
"""
OUTPUT:
    r
    a
    m
"""
