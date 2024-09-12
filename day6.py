"""
# on day 6 we learned about variable

variable is like a box on memory where we can store data
    like c variable can be of any type
        i)int
        ii)float
        iii)char/string
        iv)boolean

    but unlike 'c' you don't have to / programmer don't have to determine it at the time of declaration
    programmer can directly store data on it & it will change its type according to data.

    syntax:
        number
            a=1
        float
            b=2.23
        #complex
            c = complex(1,3)
        char/string
            d="Hello"
        boolean
            e=true/false
        none
            f=none

    print(a,b,c,d)

like 'c' typeof function there is also type function in python
    print("type of variable ",type(c))

"""

# number
a = 1
# float
b = 2.23
#complex
c = complex(a,b)
# char / string
d = "Hello"
# boolean
e = True
# none
f = None

print(a, b, c, d, e, f,sep="\t")
print("type of variable ",type(a),type(b),type(c),type(d),type(e),type(f),sep="\n")