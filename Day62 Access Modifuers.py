"""
    # Day 62 is about Access Modifiers in Python...
        Access specifiers or access modifiers in Python programming are used to
        limit the access of class variables and class methods outside of the class while
        implementing the concepts of inheritance.

        Types of access modifiers:
            1. Public access modifier
            2. Private access modifier
            3. Protected access modifier

        #NOTE: Python does not support strict access modifiers.
        1. Public access modifier:
            All the variables and methods (member functions) in Python are by default
            public. Any instance variable in a class followed by the 'self' keyword, i.e.,
            self.var_name, is publicly accessible.

        2. Private access modifier:
            By definition, private members of a class (variables or methods) are those members that 
            are only accessible inside the class. We cannot use private members outside the class.
            
            In Python, there is no strict concept of private access modifiers like in some 
            other programming languages. However, a convention has been established to indicate 
            that a variable or method should be considered private by prefixing its name with a
            double underscore (__). This is known as a "weak internal use indicator," and it is a 
            convention only, not a strict rule. Code outside the class can still access these 
            "private" variables and methods, but it is generally understood that they should 
            not be accessed or modified.
        
            Name Mangling:
            Name mangling in Python is a technique used to protect class-private and
            superclass-private attributes from being accidentally overwritten by
            subclasses. Names of class-private and superclass-private attributes are
            transformed by the addition of a single leading underscore and a double
            leading underscore, respectively.
        
        3. Protected access modifier:
            In object-oriented programming (OOP), the term "protected" is used to describe a 
            member (i.e., a method or attribute) of a class that is intended to be accessed 
            only by the class itself and its subclasses. In Python, the convention for indicating 
            that a member is protected is to prefix its name with a single underscore (_). 
            For example, if a class has a method called _my_method, it indicates that the 
            method should only be accessed by the class itself and its subclasses.

            It's important to note that the single underscore is just a naming convention 
            and does not actually provide any protection or restrict access to the member. 
            The syntax we follow to make any variable protected is to write the variable name followed 
            by a single underscore (_), i.e., _varName.

"""
# Public access modifier
class employee1:
    def __init__(self):
        self.name = 'Ram'
    
a = employee1()

print(a.__dir__())  # You can find the variable we declared as 'name'
print(a.name)       # The variable 'name' is accessed normally


# Private access modifier
class employee2:
    def __init__(self):
        self.__name = 'Sham'

b = employee2()
print(b.__dir__())  # You can find the mangled variable we declared as '_employee2__name'
# print(b.__name)   # This cannot be accessed directly
print(b._employee2__name)  # This can be accessed indirectly


# Protected access modifier
class employee3:
    def __init__(self):
        self._name = 'Dham'

c = employee3()
print(c.__dir__())  # You can find the variable we declared as '_name'
print(c._name)

# NOTE: There are no true access modifiers in Python; we are just using some conventions
#       and techniques of Python to achieve similar behavior.
