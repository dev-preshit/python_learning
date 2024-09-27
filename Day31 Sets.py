"""
    #Day 31 is about Sets in python
        Set is a collection of well define objects...
        This doesn't allow elements to be repeted example when we have to save aadhar No.
        or Employee number which can't be repeted in a country or company resp.

        • Sets are unordered collection of data items.
        • They store multiple items in a single variable.
        • Sets items are separated by commas and enclosed within curly brackets {}.
        • Sets are unchangeable meaning we can't alter them after creation.
        • Sets do not contain duplicate items.
        eg.
            Sets = {1,2,3,4,3,5,2}
            print(Sets)
            color = {"red","blue","green"}
            print(color)

        It is not important that the data in a Set should be same it can be mix
        i.e. int, float, string, boolen, etc...
        eg. 
            mix = {"one", 1, True, 1.00}

        As order is not maintain so we cant call element using index
        So how to access it 

        We can access the set by using for loop
        eg.
            for value in mix:
                print(value)

        • 'in' keyword
            we can use 'in' keyword while checking in condition to check whether 
            element in set is presesnt or not...
            eg.
                if 1 in mix:
                    print("TRUE")
                else:
                    print("FALSE")
"""

Sets = {1,2,3,4,3,5,2}
print(Sets)     # {1, 2, 3, 4, 5}
color = {"red","blue","green"}
print(color)    # {'blue', 'red', 'green'}

mix = {"one", 1, False, 2.34}
print(mix)      # {False, 'one', 2.34, 1}

for value in mix:
    print(value, end = ",")     # False,one,2.34,1,

# Note:   Output could be different for every run