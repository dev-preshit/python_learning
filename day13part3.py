"""
    #Day 13 is about String Methods/Functions in Python...
        Python has various methods to manipulate strings.
        Using these methods, you can check if strings contain only lowercase or uppercase characters, whether they are printable, and more.

        #Function to check if a string contains only lowercase characters

            str = "hello world"
            lowerString = str.islower()
        This will return True if all characters in the string are in lowercase, otherwise False.

        #Function to check if a string contains only uppercase characters

            str = "HELLO WORLD"
            upperString = str.isupper()
        This will return True if all characters in the string are in uppercase, otherwise False.

        #Function to check if the whole string is printable

            str = "Hello World"
            printString = str.isprintable()
        This will return True if there are no characters like (\n or \t) in the string and False if such characters are present.

        #Function to check if a string contains only whitespace

            str = "     "
            spaceString = str.isspace()
        This will return True if the string contains only whitespace characters, otherwise False.

        #Function to convert a string to title case (first letter of each word capitalized)

            str = "hello world"
            titleString = str.title()
        This will return the string with the first letter of each word capitalized.

        #Function to check if a string is in title case (first letter of each word capitalized)

            str = "Hello World"
            isCapString = str.istitle()
        This will return True if the first letter of each word is capitalized, otherwise False.

        #Function to swap uppercase to lowercase characters and vice versa

            str = "hELLO wORLD"
            swapString = str.swapcase()
        This will return the string with uppercase characters converted to lowercase and vice versa.
"""

#islower()
str = "hello world"
lowerString = str.islower()
print(lowerString)

#isupper()
str = "HELLO WORLD"
upperString = str.isupper()
print(upperString)

#isprintable()
str = "Hello World"
printString = str.isprintable()
print(printString)

#isspace()
str = "     "
spaceString = str.isspace()
print(spaceString)

#title()
str = "hello world"
titleString = str.title()
print(titleString)  

#istitle()
str = "Hello World"
isCapString = str.istitle()
print(isCapString) 

#swapcase()
str = "hELLO wORLD"
swapString = str.swapcase()
print(swapString)

"""
    OUTPUT:
        True
        True
        True
        True
        Hello World
        True
        Hello World 
"""