"""
    #day 23 is about Function of list in python...
        • Function to add element at end of list
            l = [1,4,9]
            l.append(16)
            print(l)

        • Function to sort a list
            l = [85,34,56,2,65,78,12,98,4]
            l.sort()
            print(l)    #assending order
            l.sort(reverse = True)
            print(l)    #desending order

        • Function to reverse orignal list
            l = [85,34,56,2,65,78,12,98,4]
            l.reverse()
            print(l)
        
        • Function to find index first apperence on value
            l = [85,34,56,2,65,78,12,98,4]
            print(l.index(56))
        
        • Function to count repetation of element
            l = [1,2,3,4,5,4,3,5,6,7]
            print(l.count(4))

        • Function to create copy of list
            Note:
                if you assign a list 'l' to another variable 
                and than make change in new variable that it will affect 'l'
                eg.
                    m = l
                    m[0] = 0
                    print(l)

                #for that reason we use copy()
                    m = l.copy()
                    m[0] = 0
                    print(l)
                    print(m)
        
        • Function to insert value at given index
            l.insert( 1  ,  234 )
                   #index  #value
            print(l)

        • Function to add an entire list to the exising list
            k = [100, 200, 300]
            l.extend(k)
            print(l)
            But if we want that list shouldn't be change that we 
            can simply concatinate two list to a new created one
            eg. 
                list = l + k
        

"""
#append()
l = [1,4,9]
l.append(16)
print(l)    #[1, 4, 9, 16]

#sort()
l = [85,34,56,2,65,78,12,98,4]
l.sort()    
print(l)    #assending order    #[2, 4, 12, 34, 56, 65, 78, 85, 98]
l.sort(reverse = True)
print(l)    #desending order    #[98, 85, 78, 65, 56, 34, 12, 4, 2]

#reverse()
l = [85,34,56,2,65,78,12,98,4]
l.reverse()
print(l)    #[4, 98, 12, 78, 65, 2, 56, 34, 85]

#index()
l = [85,34,56,2,65,78,12,98,4]
print(l.index(56))  #2

#count()
p = [1,2,3,4,5,4,3,5,6,7]
print(p.count(4))   #2

#copy()
n = [1,2,3,4,5,4,3,5,6,7]
m = n
m[0] = 0
print(n)    #[0, 2, 3, 4, 5, 4, 3, 5, 6, 7]

#for this reason we use copy()
m = l.copy()
m[0] = 0
print(l)    #[85, 34, 56, 2, 65, 78, 12, 98, 4]
print(m)    #[0, 34, 56, 2, 65, 78, 12, 98, 4]

#insert()
l.insert( 1  ,  234 )
        #index  #value
print(l)    #[85, 234, 34, 56, 2, 65, 78, 12, 98, 4]

#extend()
k = [100, 200, 300]

list = l + k

l.extend(k)
print(l)    #[85, 234, 34, 56, 2, 65, 78, 12, 98, 4, 100, 200, 300]
print(list) #[85, 234, 34, 56, 2, 65, 78, 12, 98, 4, 100, 200, 300]