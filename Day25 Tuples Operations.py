"""
    #Day 25 is about operations on Tuples
        We can manipulate tuple as it is not allowed 
        by python but there is a way to change it...
        We can change it by convertion it to list first
        makes changes and reconvert it back to tuple
        eg.
            Tuples = (1,2,3,4,5,6)
            temp = list(Tuples)
            temp.append(7)      #add item
            temp.pop(3)         #remove item
            temp[2] = 10        #change item
            Tuples = tuple(temp)
            print(tuples)

        However we can directly concatinate two tupes as 
        we will be creating a new tuple...
        eg.
            num1 = (1,2,3)
            num2 = (4,5,6)
            numbers = num1 + num2
            print(numbers)

        • Function to count repetation of element
            tup = (1,2,3,4,5,4,3,5,6,7)
            print(tup.count(4))    

        • Function to find index first apperence on value
            tup = (85,34,56,2,65,78,12,98,4)
            print(tup.index(56))
        
        • Function to find length of tuple
            tup = (85,34,56,2,65,78,12,98,4)
            print(tup.index(56))

        NOTE: we can use every function of list once we convert tuple into list
"""
#Manipulation of Tuple
Tuples = (1,2,3,4,5,6)
temp = list(Tuples)
temp.append(7)      #add item
temp.pop(3)         #remove item
temp[2] = 10        #change item
Tuples = tuple(temp)
print(Tuples)       #(1, 2, 10, 5, 6, 7)

#Concatination
num1 = (1,2,3)
num2 = (4,5,6)
numbers = num1 + num2
print(numbers)      #(1, 2, 3, 4, 5, 6)

#count()
tup = (1,2,3,4,5,4,3,5,6,7)
print(tup.count(4)) #2

#index()
tup = (85,34,56,2,65,78,12,98,4)
print(tup.index(56))#2    

#len()
tup = (85,34,56,2,65,78,12,98,4)
print(len(tup))     #9