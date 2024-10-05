#EXECRISE 34
# Secret Code language explanation
#create a coder and de-coder for string secret language...
"""
    So I have created two function named as coder and decoder doing 
    work to code and decode string.

    It first check if the string length is 1 or 2 if yes than it  
    simply reverse the string and return it, or else it take first 
    character for words and adding it to last than generating 6 random 
    number converting it to character and adding it at front and back.

    This coder function is been called by Cinput function where the string 
    get split by split function and get stored in list. than the list in 
    intrated and call coder funtion for each word after each word is coded it return
    it back to Cinput where this again get store in list and get converted back in string

    Same with decoder function as it remove random words from start and end
    and than add last character at first place if word have more than 3 character
    or else ir simply reverse it.

    This decoder funtion get its input from Dinput where the input string get slice
    and been sent to decoder function which return encoded word which leter been add to 
    a list and been created a string using jion method...
"""


import random

def coder(string):
    n = len(string)
    if n == 1 or n == 2:
            return string[::-1]
    else:
            fchar = string[0]
            string = string[1:] + fchar
            for _ in range(3):
                string += chr(random.randint(97,122))
            for _ in range(3):
                string = chr(random.randint(97,122)) + string
            return string


def Decoder(Dstring):
    n = len(Dstring)
    if n == 1 or n == 2:
        return Dstring[::-1]
    else:
        Dstring = Dstring[3:-3]
        lchar = Dstring[-1]
        Dstring = lchar + Dstring[:-1]
        return Dstring

def Cinput():

    Strinput = input("Enter Message: ")
    stringlist = Strinput.split(" ")
    replylist = []

    for i in stringlist:
        code = coder(i)
        replylist.append(code)
    
    Strreply = " ".join(replylist)
    print("coded message:", Strreply)
    return Strreply

def Dinput():
    Dstrinput = input("Enter message to encode: ")
    stringlist = Dstrinput.split(" ")
    replylist = []
    for i in stringlist:
        dcode = Decoder(i)
        replylist.append(dcode)

    Strreply = " ".join(replylist)
    print("Decoded message:", Strreply)
    return Strreply

     
print("Welcome to Coder and De-coder of message")
# print("Do you want to code or de-code")

Cinput()
Dinput()