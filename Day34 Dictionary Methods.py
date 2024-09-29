"""
    #Day 34 is about Dictionary Methods in python...
        • Function to add key-value pair in dictionary
            info1 = {"emp_id":123, "emp_nm":"Ram" , emp_ad : 1234}
            info2 = {"emp_age" : 31, "emp_dept" : "manager"}

            print(info1,info2, end = "\t")

        • Function to clear a dictionary
            info2.clear()
        
        • Function to pop from a dictionary
            info1.pop(emp_ad)

        • Function popitems removes the last key-value pair from dictionary
            info1.popoitem()
        
        • To delete a dictionary
            info2 = {"emp_age" : 31, "emp_dept" : "manager"}
            del info2
"""

info1 = {"emp_id":123, "emp_nm":"Ram" , "emp_ad" : 1234}
info2 = {"emp_age" : 31, "emp_dept" : "manager"}


print(info1,info2, sep = "\t")
#{'emp_id': 123, 'emp_nm': 'Ram', 'emp_ad': 1234}        {'emp_age': 31, 'emp_dept': 'manager'}

info2.update({"DoB" : "23/july/1993"})


print(info1,info2, sep = "\t")
# {'emp_id': 123, 'emp_nm': 'Ram', 'emp_ad': 1234}        {'emp_age': 31, 'emp_dept': 'manager', 'DoB': '23/july/1993'}


info1.update(info2)
print(info1)
# {'emp_id': 123, 'emp_nm': 'Ram', 'emp_ad': 1234, 'emp_age': 31, 'emp_dept': 'manager', 'DoB': '23/july/1993'}


info2.clear()
print(info2)
#{}


info1.pop("emp_ad")
print(info1)
#{'emp_id': 123, 'emp_nm': 'Ram', 'emp_age': 31, 'emp_dept': 'manager', 'DoB': '23/july/1993'}


info1.popitem()
print(info1)
#{'emp_id': 123, 'emp_nm': 'Ram', 'emp_age': 31, 'emp_dept': 'manager'}

del info1
#will detele dictionary