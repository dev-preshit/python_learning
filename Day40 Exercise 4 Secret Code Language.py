# EXERCISE 4
# Secret Code Language
# Create a coder and decoder for a string secret language...

import random

def coder(string):
    n = len(string)
    if n == 1 or n == 2:
        return string[::-1]
    else:
        fchar = string[0]
        string = string[1:] + fchar
        for _ in range(3):
            string += chr(random.randint(97, 122))
        for _ in range(3):
            string = chr(random.randint(97, 122)) + string
        return string

def decoder(Dstring):
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
    print("Coded message:", Strreply)
    return Strreply

def Dinput():
    Dstrinput = input("Enter message to decode: ")
    stringlist = Dstrinput.split(" ")
    replylist = []

    for i in stringlist:
        dcode = decoder(i)
        replylist.append(dcode)

    Strreply = " ".join(replylist)
    print("Decoded message:", Strreply)
    return Strreply

print("Welcome to the Coder and Decoder of messages")
Cinput()
Dinput()
