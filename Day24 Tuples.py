"""
    #day 24 is about tuples in python
        tuple is similar to list use to store data on one variable
        but unlike list we can't change it...
        • Tuples are ordered collection of data items.
        • They store multiple items in a single variable.
        • Tuples items are separated by commas and enclosed within round brackets ().
        • Tuples are unchangeable meaning we can't alter them after creation.
        • Tuples do not contain duplicate items.
        
        eg.
            tup = (1,2,3,4,5,6)
            colortup = ("red","blue","green")
            print(tup)
            print(colortup)
        
        Tuple follow indexing same as list
            a = tup[2]
            print(a)
        It is not important that the data in a Tuple should be same it can be mix
        i.e. int, float, string, boolen, etc...
        eg. 
            mixTup = ("one", 1, True, 1.00)
        
        • 'in' keyword
            we can use 'in' keyword while checking in condition to check whether 
            element in tuple is presesnt or not...
            eg.
                if 1 in mixtup:
                    print("TRUE")
                else:
                    print("FALSE")

        • slicing of tuple
            We can slice tuple but unlike list it won't update the same 
            list but will create a new tuple...
            Syntax:
                tuple[start: stop: step]
            
            eg.
                mixTup2 = ("one", 1, 543, true, 0, "zero", 65, "mix", "Hunderd")
                newMixTup = mixTup2[0 : len(mixTup2)]
                print(newMixTup)
"""

#tuple creation
tup = (1,2,3,4,5,6)
colortup = ("red","blue","green")
print(tup)      #(1, 2, 3, 4, 5, 6)
print(colortup) #('red', 'blue', 'green')

#indexing of tuple
a = tup[2]
print(a)        #3
b = tup[-2]
print(b)        #5

#mix datatype
mixTup = ("one", 1, True, 1.00)
print(mixTup)   #('one', 1, True, 1.0)

#in keyword
if 1 in mixTup :
    print("TRUE")
else :
    print("FALSE")
# TRUE

#Sliceing of tuple
mixTup = ("one", 1, 543, True, 0, "zero", 65, "mix", "Hunderd")
newtup1 = mixTup[0:len(mixTup)] 
print(newtup1)          # ('one', 1, 543, True, 0, 'zero', 65, 'mix', 'Hunderd')
newtup2 = mixTup[1:-1]
print(newtup2)          #(1, 543, True, 0, 'zero', 65, 'mix')
newtup3 = mixTup[0 : len(mixTup) : 2]
print(newtup3)          #('one', 543, 0, 65, 'Hunderd') 
