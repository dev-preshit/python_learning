"""
    #day 12 is about string Strings Slicing and Operations on Strings in Python
    slicing in python is basically access element of sting in perticular range
    Syntax:
        fruit = "apple"
        var = fruit[from:upto]
    One this you should know that the string in given range will be print uptill n-1 i.e. is element is 4 
    than it will print uptill 3 index only

    eg.
        fruit = "apple"
        var = fruit[0:4]
        so if we print it will only print "appl"
        that is uptill n-1 index

    Python has a one of the many function of sting called string length
    or function len()
    this give length of string pass into it including every charter and space...
    eg. 
        str = "ram is a boy"
        print(len(str)) => 12
        
    Python also support negative indexing i.e. if we put -ve number it will still work 
    eg.
        fruit = "apple"
        var = fruit[0:-3]
        now if we print it will only print only "ap"
        python interprit it as fruit[0:len(fruit)-3] => fruit[0:5-3] => fruit[0:2] => ap 
        this also work for from element too i.e. 
        is var = fruit[-3:-1] => fruit[len(fruit)-3:len(fruit)-1] => fruit[2:4] => pl  
"""

fruit = "apple"
var = fruit[0:4] #from index 0 to 3
print(var)

var = fruit[:4] # if not written anything tham python will concider 0 index
print(var)      # from index 0 to 3

var = fruit[3:] # if not written anything tham python will concider length of string
print(var)      #from index 3 to 5

var = fruit[:]  #if not written anything than 0 to length of string
print(var)      #from index 0 to 5


fruitlen = len(fruit) # gives the length of string
print(fruitlen)

var = fruit[0:-2]#from index 0 to lenght - 2
print(var)       #from index 0 to 3

var = fruit[:-2] # if not written anything tham python will concider 0 index
print(var)       #from index 0 to lenght - 2

var = fruit[-4:-2]#from index length - 4 to lenght - 2
print(var)        #from index 1 to 3

"""
OUTPUT:
    appl    #from index 0 to 3
    appl    #from index 0 to 3
    le      #from index 3 to 5
    apple   #from index 0 to 5
    5       #length of apple
    app     #from index 0 to 3
    app     #from index 0 to 3
    pp      #from index 1 to 3
"""
