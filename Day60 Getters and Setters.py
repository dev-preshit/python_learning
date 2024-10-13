"""
       # Day 60 is about Getters and Setters in Python...
        Getters:
            Getters in Python are methods used to access the values of an object's
            properties. They are used to return the value of a specific property and are
            typically defined using the @property decorator.
            Essentially, we can use the function as a variable but cannot assign a value to it directly.
            
            class Myclass:
                def __init__(self, value):
                    self.value = value
                
                @property  # This is the getter
                def ten_value(self):
                    return 10 * self.value

        Setters:
            It is important to note that getters do not take any parameters, and we cannot
            set the value through the getter method. For that, we need a setter method, which can be
            added by decorating the method with @property_name.setter.
            Essentially, it allows setting a value for a method.
            
            class Myclass:
                def __init__(self, value):
                    self.value = value
                
                @property  # This is the getter
                def ten_value(self):
                    return 10 * self.value

                @ten_value.setter  # This is the setter
                def ten_value(self, newvalue):
                    self.value = newvalue

            In fact, @property can also be used for encapsulation in Python,
            meaning we are effectively performing encapsulation...

"""

class Myclass:
    def __init__(self,value):
        self.value = value
    
    def show(self):
        print(f'value is {self.value}')

    @property   #This is getter
    def ten_value(self):
        return 10* self.value
    
    @ten_value.setter  #This is setter
    def ten_value(self,newvalue):
            self.value = newvalue

obj = Myclass(10)
obj.show()
print(obj.ten_value) #using getter
obj.ten_value = 20 #using setter
print(obj.ten_value) #using getter
obj.show()

# value is 10
# 100
# 200
# value is 20