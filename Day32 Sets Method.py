"""
    #Day 32 is about Set Method in Python...
        • Function to union two set
            s1 = {1, 3, 4, 6, 7}
            s2 = {5, 6, 7, 8, 9}
            print(s1.union(s2))

        This will merge s1 with s2 but won't change set s1 or s2.

        • Function to update set after union
            s1 = {1, 3, 4, 6, 7}
            s2 = {5, 6, 7, 8, 9}
            print(s1.update(s2))
            print(s1,s2)
        This will update s1 and store union in it.
        
        • Function to find intersection
            s1 = {1, 3, 4, 6, 7}
            s2 = {5, 6, 7, 8, 9}
            print(s1.intersection(s2))
            print(s1,s2)
        This will give elements which are common in both sets.

        • Function to have updated intersection
            s1 = {1, 3, 4, 6, 7}
            s2 = {5, 6, 7, 8, 9}
            print(s1.intersection_update(s2))
            print(s1,s2)
        This will give elements which are common in 
        both sets and store it in s1.

        • Function to find symmetric_difference
            s1 = {1, 3, 4, 6, 7}
            s2 = {5, 6, 7, 8, 9}
            print(s1.symmetric_difference(s2))
            print(s1,s2)
        This will give elements which is not common in both set.

        • Function to have symmetric_difference_update
            s1 = {1, 3, 4, 6, 7}
            s2 = {5, 6, 7, 8, 9}
            print(s1.symmetric_difference_update(s2))
            print(s1,s2)
        This will give elements which is not common in 
        both set and store it in s1.

        • Function to find difference in set1 and set2
            s1 = {1, 3, 4, 6, 7}
            s2 = {5, 6, 7, 8, 9}
            print(s1.difference(s2))
            print(s1,s2)
        This will give elements present in firse set and absent in second set
        e.i present in s1 but not in s2.
            
        • Function to find difference in set1 and set2
            s1 = {1, 3, 4, 6, 7}
            s2 = {5, 6, 7, 8, 9}
            print(s1.difference_update(s2))
            print(s1,s2)
        This will have elements present in firse set and absent in second set
        e.i present in s1 but not in s2 and store it in s1.

        • Function to find does set are disjoint or not
            s1 = {1, 3, 4, 6, 7}
            s2 = {5, 6, 7, 8, 9}
            print(s1.isdisjoint(s2))
        This will give TRUE if there is no element common in two sets
        else FALSE

        • Function to find does set A is superset for B or not
            s1 = {1, 3, 4, 6, 7}
            s2 = {6, 7}
            print(s1.issuperset(s2))
        This will give TRUE if s1 is superset for s2

        • Function to find does set A is subset for B or not
            s1 = {6, 7}
            s2 = {5, 6, 7, 8, 9}
            print(s1.issuperset(s2))
        This will give TRUE if s1 is subset for s2

        • Function to add element in set
            s1 = {1, 3, 4, 6, 7}
            s2 = s1.add(10) 
            print(s2)
        This will add element in set
        
        • Function to remove element
            s3 = s2.remove(1) / s3 = s2.discard(1)
            print(s3)
        This will remove element from set
        
        • Function to discard element
            s3 = s2.discard(1)
            print(s3)
        This will remove element from set too

        NOTE: if we use remove and if elemnent is not present in set it will rise an error
        while in discard it will not rise error and program will work as it is...

        • Function to pop last element form set
            s1 = {1, 3, 4, 6, 7}
            s2 = s1.pop(10)
            print(s1) 
            print(s2)

        • del keyword
            del s1

"""

#union()
s1 = {1, 3, 4, 6, 7}
s2 = {2, 5, 6, 7, 8, 9}
print(s1.union(s2)) #{1, 2, 3, 4, 5, 6, 7, 8, 9}

#update()
print(s1.update(s2))
print(s1,s2)    #{1, 2, 3, 4, 5, 6, 7, 8, 9} {2, 5, 6, 7, 8, 9}

#intersection()
s1 = {1, 3, 4, 6, 7}
s2 = {5, 6, 7, 8, 9}
print(s1.intersection(s2))  #{6, 7}
print(s1,s2)    #{1, 3, 4, 6, 7} {5, 6, 7, 8, 9}

#intersection_update()
print(s1.intersection_update(s2))   # None
print(s1,s2)                        # {6, 7} {5, 6, 7, 8, 9}

#symmetric_difference()
s1 = {1, 3, 4, 6, 7}
s2 = {5, 6, 7, 8, 9}
print(s1.symmetric_difference(s2))  # {1, 3, 4, 5, 8, 9}
print(s1,s2)                        # {1, 3, 4, 6, 7} {5, 6, 7, 8, 9}

#symmetric_difference_update()
print(s1.symmetric_difference_update(s2))   # None
print(s1,s2)                                # {1, 3, 4, 5, 8, 9} {5, 6, 7, 8, 9}

# difference()
s1 = {1, 3, 4, 6, 7}
s2 = {5, 6, 7, 8, 9}
print(s1.difference(s2))     #{1, 3, 4}
print(s1,s2)                 #{1, 3, 4, 6, 7} {5, 6, 7, 8, 9}

# difference_update()
print(s1.difference_update(s2))     #None
print(s1,s2)                        #{1, 3, 4} {5, 6, 7, 8, 9}

#isdisjiont()
s1 = {1, 3, 4, 6, 7}
s2 = {5, 6, 7, 8, 9}
print(s1.isdisjoint(s2))
# False

#issuperset()
s1 = {1, 3, 4, 6, 7}
s2 = {6, 7}
print(s1.issuperset(s2))
# True

#issubset()
s1 = {6, 7}
s2 = {5, 6, 7, 8, 9}
print(s1.issubset(s2))
# True  

#add()
s1 = {1, 3, 4, 6, 7}
s1.add(10) 
print(s1)   # {1, 3, 4, 6, 7, 10}

#remove()
s1.remove(1)
print(s1)   # {3, 4, 6, 7, 10}

#discard()
s2.discard(1)
print(s2)   # {5, 6, 7, 8, 9}

#pop()
s1 = {1, 3, 4, 6, 7}
s2 = s1.pop()
print(s1)   # {3, 4, 6, 7}
print(s2)   # 1

#clear()
s1.clear()
print(s1)   #set()

#del
del s1 #set will be deleted
