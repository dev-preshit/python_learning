"""
    #Day 65 is about Static method in python
        Static methods in Python are methods associated with a class rather than 
        an object of the class. They are defined using the @staticmethod decorator 
        and do not have access to the object of the class (i.e., self). These methods 
        are invoked on the class itself, not on an object of the class. 

        @staticmethod
        def Fun_name(argument(s)):
            block of code

            
"""

class Math:
    def __init__(self, num: int) -> None:
        self.num = num

    @staticmethod
    def average(numbers: list) -> float:
        count = len(numbers)
        total = 0
        for item in numbers:
            total += item

        return total / count


a = Math(10)

numbers = []
for _ in range(10):
    numbers.append(float(input("Enter a number: ")))

print(f"Average is => {Math.average(numbers):.2f}")
#                      ^^^^ using class name instead of object
#   Average is => 10.00

print(f"Average is => {a.average(numbers):.2f}")
#                      ^ using object directly
#   Average is => 10.00
