"""
    #Day 66 is about Instance variables Vs Class variables in python...
        • Class variable:
            Class variables are defined at the class level and are shared
            among all instances of the class. They are defined outside of
            any method and are usually used to store information that is
            common to all instances of the class.
        • Instance variable:
            Instance variables are defined at the instance level and are
            unique to each instance of the class. They are defined inside
            the init method and are usually used to store information that
            is specific to each instance of the class.
"""
class Employee:
    company_name = "Ram_coolers"  # <= this is class variable

    def __init__(self, name):
        self.name = name          # <= this is instance variable
        self.salary = 10000       # <= this is instance variable

    def showDetails(self):
        print(f"Name of employee is {self.name}, having salary ${self.salary} and works for {self.company_name}")


emp1 = Employee("Amit")
emp1.showDetails()   # Both line 12 & 13 will give the same output
Employee.showDetails(emp1)  # Corrected typo: Employee.showDetails

emp1.salary = 10500  # <= this is an instance variable
emp1.showDetails()

emp2 = Employee("Ajay")
emp2.showDetails()

# This line creates a new instance variable `company_name` for `emp2`
emp2.company_name = "Ram_coolers Nepal"  # <= this is now an instance variable for `emp2`
emp2.salary = 8000  # <= this is an instance variable
emp2.showDetails()

# To modify the class variable for all instances, use the class name:
Employee.company_name = "Ram_coolers International"
emp1.showDetails()
emp2.showDetails()
