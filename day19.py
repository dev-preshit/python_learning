"""
    #day 19 is about break and continue statement in python
        sometimes we want a loop to stop if certain condition get true or 
        sometimes we want a loop to skip centain statement for a certain condition
        in this situation we use break and co0ntinue statement respectivitely...

    break statement:
        whenever interpriter see a break in code it passes control directly to the end of the loop
        i.e. it leaves all the feather checking of condition and will end the execution of loop...
    
    continue statement:
        Whenever interpriter see a continue in code it passes control directly to the start of loop 
        i.e. it leaves all the feather execution of the intration and go to start to check the loop condition...

"""

for i in range (11):
    if i == 5:
        break
    print(i)
#At the time of break it leave the loop execution when i get equal to 5 and after no number is printed..
"""
    Output:
        0
        1
        2
        3
        4   <=
"""

for i in range (11):
    if i == 5:
        continue
    print(i)
#At the time of continue it do not print when i get equal to 5 and direaclty go to check the feather condition
"""
    Output:
        0
        1
        2
        3
        4 <=
        6
        7
        8
        9
        10
"""