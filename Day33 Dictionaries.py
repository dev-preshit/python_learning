"""
    #Day 33 is about Dictionaries in Python
        Dictionary is key-value pairs which means 
        for every value there is a key present...

        • Dictionaries are ordered collection of data items. 
        • They store multiple items in a Singte variable. 
        • Dictionary items are key-value pairs that are separated by 
        commas and enclosed within curly brackets {}.

        eg.
            dic = {
                "name": "Ram",
                "Age" : 17,
                "Class": "11th"
            }
            print(dic)

            print(dic["name"]) ----------- 1
            print(dic.get("name"))---------2

            difference between both 1 and 2 is that
            1 will throw error if key is not present in dictionary
            but 2 will print none if key is not present...

            to get  all keys we can use keys method
            eg.
                print(dic.keys())
            or can use for loop 
            eg.
                for key in dic.keys():
                    print(into[key])
            
            same will be ture with value() function
                print(dic.value())
            or can use for loop
            eg.
                for val in dic.value():
                    print(val)

            for key value pair we can use items() function
            eg.
                print(dic.items())
            same will work with loop
            eg.
                for key,value in dic.items():
                    print(f"The value corresponding to key {key} is {value}")


"""
#dic creation
dic = {
    "name": "Ram",
    "Age" : 17,
    "Class": "11th"
    }

#print dic
print(dic)                      # {'name': 'Ram', 'Age': 17, 'Class': '11th'}

#print preticular key
print(dic["name"])              # Ram

#get()
print(dic.get("name"))          # Ram

#keys()
print(dic.keys())               # dict_keys(['name', 'Age', 'Class'])

#keys() in loop
for key in dic.keys():
    print(key,end = ",")        # name,Age,Class,
print()

#keys() as index
for key in dic.keys():
    print(dic[key],end = ",")   # Ram,17,11th,
print()

#values()
print(dic.values())             # dict_values(['Ram', 17, '11th'])

#values() in loop
for val in dic.values():
    print(val,end = ",")        # Ram,17,11th,
print()

#items()
print(dic.items())              # dict_items([('name', 'Ram'), ('Age', 17), ('Class', '11th')])

#items() in loop
for key,value in dic.items():
    print(f"The value corresponding to key {key} is {value}")# The value corresponding to key name is Ram
                                                             # The value corresponding to key Age is 17
                                                             # The value corresponding to key Class is 11th