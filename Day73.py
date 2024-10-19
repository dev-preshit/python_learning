class Employee:

    def __len__(self):
        i = 0
        for _ in self.name:
            i +=1
        return i
    
    def __init__(self,name):
        self.name = name

    def __str__(self):
        return f"The name of the employee is {self.name}"
    
    def __repr__(self):
        return f"this will be called if str method is not present"
    
    def __call__(self):
        print("this can be called is we call object as function i.e. e()")
