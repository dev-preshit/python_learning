"""
    Day 81 is about Hybrid and Hierarchical Inheritance in python...
    Hybrid Inheritance
        When ever we use more than one inheritance concept ,
        i.e. combination of single and multiple Inheritance
        than it is known as Hybrid Inheritance
        In Python, hybrid inheritance can be implemented by creating a
        class hierarchy, in which a base class is inherited by multiple
        derived classes, and one Of the derived classes is further
        inherited by a sub-derived class.

    Hierarchical Inheritance
        When ever a tree like structure is formed it is reffer to 
        Hierarchical Inheritance.

"""
# Hybrid Inheritance
class base:
    pass
                            #              base
class derived1(base):       #               |
    pass                    #          -----------
                            #          |         |
class derived2(base):       #          D1        D2  
    pass                    #                    |       EC
                            #               -----------  /
class derived3(derived2):   #               |         | /
    pass                    #               D3        D4

class externalclass:
    pass                            
class derived4(derived2,externalclass):   
    pass


# Hierarchical Inheritance
class base:                 
    pass                    
                            #              base
class derived1(base):       #               |
    pass                    #          ---------------
                            #          |             |
class derived2(base):       #          D1            D2 
    pass                    #          |             |
                            #     -----------   -----------
class derived3(derived1):   #     |         |   |         |
    pass                    #     D3        D4  D5        D6

class derived4(derived1):
    pass

class derived5(derived2):
    pass

class derived6(derived2):
    pass