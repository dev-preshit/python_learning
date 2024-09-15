"""
    #Day 13 is about String Method/Function in Python...
        Python has various method to manipunate string 
        Using this methods you can find length, change string into lower and upper case and much more

        #Function length of string

            stringLen = len(str)
        this will give length of string including all symbols and spaces...

        #Function to convert to lowercase and uppercase

            upperString = str.upper()
        this will convert all string characters into uppercase...

            lowerString = str.lower()
        this will convert all string characters into lowercase...

        #Function to remove any tralling characters

            str = "!!!DEV!!!!!"
            stripString = str.rstrip("!")
        this will remove all "!" from string 
        NOTE: it will only remove ending "!" not starting...

        #Function to replace String element

            str = "silver spoon"
            newString = str.replace("sp", "M")
        this will replace all "sp" in in string with "M"...

        #Function to seprate and create a list of sting

            str = "Silver Moon"
            listString = str.split(" ")
        this will split string wherever there is a space and treate it as different element...
        ['Silver', 'Moon']

        #Function to capitalize a string

            str = "hello world"
            capString = str.capitalize()
        this will turn first character into capital and rest will be change into lowercase...

        #Function to align sting to center as pre the parameter pass my user

            str = "This is an example"
            centralString = str.center(50)
        this will make string length to 50 by adding spaces ahead and end of string
        so if str.len() is equal to 18 than center() will add 32 spaces 16 ahead and 16 at end to create new lenght to 50...

            centralString1 = str.center(50,".")
        or else we can also pass charater we want to print instead of space...
"""


#len()
str = "Hello Github"
stringLen = len(str)
print(stringLen)

#upper()
upperString = str.upper()
print(upperString)

#lower()
lowerString = str.lower()
print(lowerString)

#rstrip()
str = "!!!DEV!!!!!"
stripString = str.rstrip("!")
print(stripString)

#replace()
str = "silver spoon"
newString = str.replace("sp", "M")
print(newString)

#split()
str = "Silver Moon"
listString = str.split(" ")
print(listString)

#capitalize()
str = "hello world"
capString = str.capitalize()
print(capString)

#center()
str = "This is an example"
centralString = str.center(50)
centralString1 = str.center(50,".")

print(centralString)
print(centralString1)

"""
    OUTPUT:
        12
        HELLO GITHUB
        hello github
        !!!DEV
        silver Moon
        ['Silver', 'Moon']
        Hello world
                        This is an example
        ................This is an example................
"""