"""
    # Day 62 is about Access Modifiers in Python...
        Access specifiers or access modifiers in python programming are used to
        limit the access of class variables and class methods outside of class while
        implementing the concepts of inheritance.

        Types of access modifiers
            1. Public access modifier
            2. Private access modifier
            3. Protected access modifier

        #NOTE: python do not support access modifiers 
        1. Public access modifier
            All the variables and methods (member functions) in python are by default
            public. Any instance variable in a class followed by the 'self' keyword ie.
            self.var_name are public accessed.

        2. Private access modifier
            By definition, Private members of a class (variables or methods) are those members which 
            are only accessible inside the class. We cannot use private members outside of class.
            
            In Python, there is no strict concept of privaten access modifiers like in some 
            other programming languages. However, a convention has been established to indicate 
            that a variable or method should be considered private by prefixing its name with a
            double underscore (__). This is known as a "weak internal use indicator" and it is a 
            convention only, not a strict rule. Code outside the class can still access these 
            "private" variables and methods, but it is generally understood that they should 
            not be accessed or modified.
        
            Name Mangling
            Name mangling in Python is a technique used to protect class-private and
            superclass-private attributes from being accidentally overwritten by
            subclasses. Names of class-private and superclass-private attributes are
            transformed by the addition of a single leading underscore and a double
            leading underscore respectively.
        
        3. Protected access modifier
            In object-oriented programming (OOP), the term "protected" is used to describe a 
            member (i.e., a method or attribute) of a class that is intended to be accessed 
            only by the class itself and its subclasses. In Python, the convention for indicating 
            that a member is protected is to prefix its name with a singleunderscore (_). 
            For example, if a class has a method called _my_method, it is indicating that the 
            method should only be accessed by the class itself and its subclasses.

            It's important to note that the single underscore is just a naming convention, 
            and does not actually provide any protection or restrict access to the member. 
            The syntax we follow to make any variable protected is to write variable name followed 
            by a single underscore (_) ie. _varName.

"""

# Public access modifier
class employee1:
    def __init__(self):
        self.name = 'Ram'
    
a = employee1()
print(a.__dir__()) #you can find the variable we declare as name
print(a.name) # variable name is access normally


#Private access modifier
class employee2:
    def __init__(self):
        self.__name = 'Sham'

b = employee2()
print(b.__dir__())  #you can find mangled variable we declare as _employee2__name
# print(b.__name) #this cannot be access directly
print(b._employee2__name) #this can be access indirectly

#Protected access modifier
class employee3:
    def __init__(self):
        self._name = 'Dham'
c = employee3()
print(c.__dir__())  #you can find the variable we declare as _name
print(c._name)

# NOTE: There is no things like access modifier in python we are just using some convention 
#       and techinque of python to perform it