"""
    #Day 13 is about String Method/Function in Python...
        Python has various method to manipunate string 
        Using this methods you can find length, change string into lower and upper case and much more

        • Function length of string

            stringLen = str.len()
        this will give length of string including all symbols and spaces...

        • Function to convert to lowercase and uppercase

            upperString = str.upper()
        this will convert all string characters into uppercase...

            lowerString = str.lower()
        this will convert all string characters into lowercase...

        • Function to remove any tralling characters

            str = "!!!DEV!!!!!"
            stripString = str.rstrip("!")
        this will remove all "!" from string 
        NOTE: it will only remove ending "!" not starting...

        • Function to replace String element

            str = "silver spoon"
            newString = str.replace("sp", "M")
        this will replace all "sp" in in string with "M"...

        • Function to seprate and create a list of sting

            str = "Silver Moon"
            listString = str.split(" ")
        this will split string wherever there is a space and treate it as different element...
        ['Silver', 'Moon']

        • Function to capitalize a string

            str = "hello world"
            capString = str.capitalize()
        this will turn first character into capital and rest will be change into lowercase...

        • Function to align sting to center as pre the parameter pass my user

            str = "This is an example"
            centralString = str.center(50)
        this will make string length to 50 by adding spaces ahead and end of string
        so if str.len() is equal to 18 than center() will add 32 spaces 16 ahead and 16 at end to create new lenght to 50...

            centralString1 = str.center(50,".")
        or else we can also pass charater we want to print instead of space...

        • Function to count the number of time a character is repeting in string

            str = "afsaakfjdakjda"
            StringCount = str.count("a")
        this will return how many times the character a is repeted...
        
        • Function to check whether string ends with preticalar character

            str = "Hello guys!!!"
            Newstring = str.endswith("!!!")
        this will return boolen value (TRUE/FALSE)
        we can also provide a perticular range to find whether it end with given character or not

            NewString = str.endswith("uy",3,10)...

        • Function to check whether string start with preticalar character

            str = "Hello guys!!!"
            Newstring = str.startswith("guys")
        this will return boolen value (TRUE/FALSE)...

        
        • Function to find any perticular character index in string

            str = "He's a boy , he is not a girl"
            FindString = str.find("a")
        this will return the index of first "a" it will find in string
        if character do not found it will return -1...

        • Function to find index on perticular character in sting

            str = "He's a boy , he is not a girl"
            FindString = str.index("a")
        this will return the index of first "a" it will find in string
        if character do not found it will return error: Substring not found...

        • Function to find if string is alphanumaric i.e. it consist A-Z,a-z,0-9 or not

            str = "HellothisismetheProgrammer123"
            alphaString = str.isalnum()
        this will return True is only A-Z,a-z,0-9 is persent else False (punctuations only)...

        • Function to find if string is coinsisting alphabets only

            str = "HellothisismetheProgrammer123"
            alphaString = str.isalpha()
        this will return True is only A-Z,a-z is persent else False(0-9 and punctuations)...

        • Function to find does string contain only lowercase character

            str = "hello world"
            lowerString = str.islower()
        this will provide true if all character in string is in lowercase else false...

        • Function to find does string contain only uppercase character

            str = "HELLO WORLD"
            upperString = str.isupper()
        this will provide true if all character in string is in uppercase else false...

        • Function to find does whole string is printable or not

            str = "Hello World"
            printString = str.isprnitable()
        this will return true is there is no character like (\n or \t) and is present will return false...

        Function to check is wide-space is present in string or not

            str = "     "
            spaceString = str.isspace()
        this will return true if there is  wide-space in string else false

        • Function to convert a string into title(If first letter ao all word is capitalized)

            str = "hello world"
            titleString = str.title()
        this will provide string converted into title...

        • Function to find that string is title or not (If first letter ao all word is capitalized)

            str = "Hello World"
            isCapString = str.istitle()
        this will return true if all first letter of word is capital else false

        • Function to swap Upper to Lower case characters and visa verse

            str = "hELLO wORLD"
            swapString = str.swapcase()
        this will return "Hello World"...
"""


#len()
str = "Hello Github"
stringLen = len(str)
print(stringLen)
        # 12

#upper()
upperString = str.upper()
print(upperString)
        # HELLO GITHUB

#lower()
lowerString = str.lower()
print(lowerString)
        # hello github

#rstrip()
str = "!!!DEV!!!!!"
stripString = str.rstrip("!")
        # !!!DEV
print(stripString)

#replace()
str = "silver spoon"
newString = str.replace("sp", "M")
print(newString)
        # silver Moon

#split()
str = "Silver Moon"
listString = str.split(" ")
print(listString)
        # ['Silver', 'Moon']

#capitalize()
str = "hello world"
capString = str.capitalize()
print(capString)
        # Hello world

#center()
str = "This is an example"
centralString = str.center(50)
centralString1 = str.center(50,".")

print(centralString)
print(centralString1)
        #                 This is an example
        # ................This is an example................

#count()
str = "afsaakfjdakjda"
StringCount = str.count("a")
print(StringCount)
        # 5

#endswith()
str = "Hello guys!!!"
Newstring = str.endswith("!!!")
print(Newstring)
        # True

#startswith()
Newstring = str.startswith("Hello")
print(Newstring)
        # True

#find()
str = "He's a boy, he is not a girl"
FindString = str.find("a")
print(FindString)
        # 5

#index()
FindStringIndex = str.index("a")
print(FindStringIndex)
        # 5

#isalnum()
str = "HellothisismetheProgrammer123"
alphaString = str.isalnum()
print(alphaString)
        # True

#isalpha()
str = "HellothisismetheProgrammer"
alphaOnlyString = str.isalpha()
print(alphaOnlyString)
        # True

#islower()
str = "hello world"
lowerString = str.islower()
print(lowerString)
        # True

#isupper()
str = "HELLO WORLD"
upperString = str.isupper()
print(upperString)
        # True

#isprintable()
str = "Hello World"
printString = str.isprintable()
print(printString)
        # True

#isspace()
str = "     "
spaceString = str.isspace()
print(spaceString)
        # True

#title()
str = "hello world"
titleString = str.title()
print(titleString)  
        # Hello World

#istitle()
str = "Hello World"
isCapString = str.istitle()
print(isCapString) 
        # True

#swapcase()
str = "hELLO wORLD"
swapString = str.swapcase()
print(swapString)
        # Hello World 
