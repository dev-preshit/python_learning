"""
    #Day 60 is about Getter and Setter in Python...
        Getters:
            Getters in Python are methods that are used to access the values of an object's
            properties. They are used to return the value of a specific property, and are
            typically defined using the @property decorator.
            Basically we can use the function as variable but can't put value on it...
            class Myclass:
                def __init__(self,value):
                    self.value = value
                
                @property   #This is getter
                def ten_value(self):
                    return 10* self.value

            It is important to note that the getters do not take any parameters and we cannot
            set the value through getter method.For that we need setter method which can be
            added by decorating method with @property_name.setter.
            basically it allow to set a value for a method...
            class Myclass:
                def __init__(self,value):
                    self.value = value
                
                @property   #This is getter
                def ten_value(self):
                    return 10* self.value

                @ten_value.setter  #This is setter
                def ten_value(self,newvalue):
                    self.value = newvalue

            Well this @property can be also use for encapsulation in python
            infact we have perform encapsulation...

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