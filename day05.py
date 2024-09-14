"""
#day 5 is about escape characters , comment(s) and print statement
    1)escape characters
        
        escape characters can be use by putting backslash (\) ahead of already using character by python
        it is same as escape characters in c language 
    
    2)comment(s)
        
        comment is a simple technique to document code for future self or for other programmer.
        this could be done by simply putting (#) symbol ahead of statement 
        there is a concept called multi-line comment which can be done by triple double quotes(""" """)
    
    3)print statement
        
        like any other programming language print statement is use to print any object(string or number) on terminal
        python provide some wired feature with print statement
        syntax:
             print(object(s),sep=" ",end=" ")
             where object => (string or number)
                   sep => use to separate object where it is (,) by any character by default its space( )
                   end => can print anything at the end of print statement by default its new line character

"""


# this is comment in python

print("Hey",6,7,23,342,"this is print statement",sep=" :",end=" ")

print("hey this is me \n \"preshit\" \t \'preshit kamble\'")


"""
OUTPUT:
    Hey :6 :7 :23 :342 :this is print statement hey this is me 
    "preshit"       'preshit kamble'
"""