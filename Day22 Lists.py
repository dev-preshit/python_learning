"""
    #day 22 is about the list in python
        If a programmer want to store multiple data on one name/variable
        Than the may use list...
        • Lists are ordered collection of data items.
        • They store multiple items in a single variable.
        • List items are separated by commas and enclosed within square brackets [].
        • Lists are changeable meaning we can alter them after creation.
        • Lists can contain duplicate items.
        
        eg.
            list = [1,2,3,4,5,6]
            color = ["red","blue","green"]
            print(list)
            print(color)

        List follow indexing same as string
        eg.
            a = list[2]
            print(a)

        It is not important that the data in a list should be same it can be mix
        i.e. int, float, string, boolen, etc...
        eg. 
            mix = ["one", 1, True, 1.00]
        
        • 'in' keyword
            we can use 'in' keyword while checking in condition to check whether 
            element in list is presesnt or not...
            eg.
                if 1 in mix:
                    print("TRUE")
                else:
                    print("FALSE")
            
        • slicing of list
            Just like string we can slice list...
            Syntax:
                list[start: stop: step]
            
            eg.
                mix2 = ["one", 1, 543, true, 0, "zero", 65, "mix", "Hunderd"]
                print(mix2[0:len(mix2)])

        List Comprehension
            List comprehensions are used for creating new lists from other iterables like lists,
            tuples, dictionaries, sets, and even in arrays and strings.
        Syntax:
            List [Expression(item) for item in iterable if Condition)
        where,
            Expression: It is the item which is being iterated.
            Iterable: It can be list, tuples, dictionaries. sets. and even in arrays and strings.
            Condition: Condition checks if the item should be added to the new list or not.
        eg 1.
            list = [i for i in range(50) if i%2 == 0]
            print(list)
        eg 2.
            names ["milo", "Sarah", "Bruno", "Anastasia", "Rosas"]
            namesWith_o = [item for item in names if "o" in item]
            print( namesWith_O )       
"""

#lists creation
list = [1,2,3,4,5,6]
color = ["red","blue","green"]
print(list)         # [1, 2, 3, 4, 5, 6]
print(color)        # ['red', 'blue', 'green']

#indexing of list
a = list[2]
print(a)
# 3
b = list[-2]
print(b)
# 5

#mix datatype
mix = ["one", 1, True, 1.00]
print(mix)         # ['one', 1, True, 1.0]

#in keyword
if 1 in mix :
    print("TRUE")
else :
    print("FALSE")
# TRUE

#Sliceing of list
mix2 = ["one", 1, 543, True, 0, "zero", 65, "mix", "Hunderd"]
print(mix2[0:len(mix2)])        # ['one', 1, 543, True, 0, 'zero', 65, 'mix', 'Hunderd']
print(mix2[1:-1])               # [1, 543, True, 0, 'zero', 65, 'mix']
print(mix2[0 : len(mix2) : 2])  # ['one', 543, 0, 65, 'Hunderd']

#List Comprehension
#eg 1.
#  [Expression]   [Iterable]   [Condition]
list = [i for i in range(25) if i%2 == 0]
print(list)       # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24]


#eg 2.
names = ["milo", "Sarah", "Bruno", "Anastasia", "Rosas"]
namesWith_o = [item for item in names if "o" in item]
print( namesWith_o )            # ['milo', 'Bruno', 'Rosas']