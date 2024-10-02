#EXECRISE 34
# Secret Code language
#create a coder and de-coder for string secret language...

import random

def coder(string):
    n = len(string)
    if n == 1 or n == 2:
            return string[::-1]
    else:
            i = 0
            string += string[0]
            string = string.replace(string[0],"",1)
            while i < 3:
                no = chr(random.randint(97,122))
                string = string + no
                i = i+1 
            while i < 6:
                no = chr(random.randint(97,122))
                string =  no + string
                i = i+1 
            return string

Strinput = input("Enter Message: ")
stringlist = Strinput.split(" ")
for i in stringlist:
    print(coder(i), end = " ")