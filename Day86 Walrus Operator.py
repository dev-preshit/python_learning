"""
    #Day 86 is about Walrus Operator in Python...
        The Walrus Operator is a new addition to Python 3.8 
        and allows you to assign a value to a variable within 
        an expression. This can be useful when you need to 
        use a value multiple times in a loop, but don't want 
        to repeat the calculation.

        The Walrus Operator is represented by the := syntax 
        and can be used in a variety of contexts including 
        while loops and if statements.
"""

a = True
print(a)
print(a:=False)

numbers = [2,3,-5,7,-9]

while (n := len(numbers)) > 0:
    print(numbers.pop())

foods = []
while (food := input("What food do you like?: ")) != "quit":
    foods.append(food)

# print(foods)

for food in foods:
    print(f"you like {food}")
