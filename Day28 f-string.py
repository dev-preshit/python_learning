"""
    #Day 28 is about f-string in python...
        Python provides a function for string known as 'format' in 
        which we can set some value whereever {} is present in string...
        eg. 
            para = "Hello this is {} and I am studing {}"
            name = "Dev-Preshit"
            lang = "Python"
            NewPara = para.format(name,lang)
            print(NewPara)

        We have to use Format function which is little bit dificult to understand
        Instated we can use f-string which is much easer than using format...
        eg.
            print(f"Hello this is {name} and I am studing {lang}")

        • f-strings
        When we prefix the string with the letter if', the string becomes the 
        f-string itself. The f-string can be formatted in much same as the
        str.format() method. The f-string offers a convenient way to embed
        Python expression inside string literals for formatting...

        If we want to print a float value uptill a certain number 
        after decimal we can use format specifier to do so...
        eg.
            amount = 10
            price = 200.099999
            print(f"For {amount} amount of apple you have to pay {price:.2f} Rs")

        We can also perform mathmatical operation using f-string but the 
        answer type will be string...
        eg.
            A = '65'
            B = '32'
            print(f"Product of A and B is {A*B}")
"""

#Format function
para = "Hello this is {} and I am studing {}"
name = "Dev-Preshit"
lang = "Python"
NewPara = para.format(name,lang)
print(NewPara)
# Hello this is Dev-Preshit and I am studing Python


#f-string
print(f"Hello this is {name} and I am studing {lang}")
# Hello this is Dev-Preshit and I am studing Python


#Format specifier
amount = 10
price = 200.099999
print(f"For {amount} amount of apple you have to pay {price:.2f} Rs")
# For 10 amount of apple you have to pay 200.10 Rs


#mathmatical operation
A = 67
B = 32
print(f"Product of A and B is {A*B}")
# Product of A and B is 2144
