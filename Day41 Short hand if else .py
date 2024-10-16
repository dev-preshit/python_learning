"""
    #Day 41 is about Short-hand If-Else Statement in Python...
        There is also a shorthand syntax for the if-else statement that can be used
        when the condition being tested is simple, and the code blocks to be executed are short.
        
        Syntax: 
            exp1 if cond1 else exp2 if cond2 else exp3
        
        Example:
            a = 10
            b = 20
            print("A") if a < b else print("equal") if a == b else print("B")  
"""

check = 0
print("Zero") if check == 0 else print("Non-Zero")
# Zero

a = 10
b = 20
c = 1 if a > b else 0
print(c)
# 0

print("A") if a > b else print("equal") if a == b else print("B")
# B
