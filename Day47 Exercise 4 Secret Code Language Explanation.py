# EXERCISE 4
# Secret Code Language Explanation
"""
    I have created two functions named coder and decoder, which work 
    to code and decode strings.

    The coder function first checks if the string length is 1 or 2. If yes, 
    it simply reverses the string and returns it. Otherwise, it takes the 
    first character of the word, adds it to the end, generates 6 random 
    numbers, converts them to characters, and adds them to the front and back 
    of the string.

    This coder function is called by the Cinput function, where the string 
    gets split by the split function and is stored in a list. Then the list 
    is iterated, calling the coder function for each word. After each word 
    is coded, it is returned to Cinput, where it is stored in a list and 
    converted back into a string.

    The decoder function does the reverse: it removes random characters 
    from the start and end, then adds the last character to the first place 
    if the word has more than 3 characters; otherwise, it simply reverses it.

    This decoder function gets its input from Dinput, where the input string 
    is sliced and sent to the decoder function, which returns the decoded word, 
    later added to a list, creating a string using the join method...
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
