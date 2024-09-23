"""
    #Day 13 is about String Methods/Functions in Python...
        Python has various methods to manipulate strings.
        Using these methods, you can find length, change strings into lower or upper case, and much more.
    
        • Function to count the number of times a character repeats in a string

            str = "afsaakfjdakjda"
            StringCount = str.count("a")
        This will return how many times the character 'a' is repeated.
        
        • Function to check whether a string ends with a particular character

            str = "Hello guys!!!"
            Newstring = str.endswith("!!!")
        This will return a boolean value (True/False).
        We can also provide a particular range to check if it ends with a given character or not:

            NewString = str.endswith("uy", 3, 10)

        • Function to check whether a string starts with a particular character

            str = "Hello guys!!!"
            Newstring = str.startswith("guys")
        This will return a boolean value (True/False).
        
        • Function to find the index of a particular character in a string

            str = "He's a boy, he is not a girl"
            FindString = str.find("a")
        This will return the index of the first 'a' found in the string.
        If the character is not found, it will return -1.

        • Function to find the index of a particular substring in a string

            str = "He's a boy, he is not a girl"
            FindString = str.index("a")
        This will return the index of the first 'a' found in the string.
        If the character is not found, it will raise an error: Substring not found.

        • Function to check if a string is alphanumeric (contains only A-Z, a-z, 0-9)

            str = "HellothisismetheProgrammer123"
            alphaString = str.isalnum()
        This will return True if only A-Z, a-z, or 0-9 are present; otherwise, it will return False (punctuations are not allowed).

        • Function to check if a string consists of alphabets only

            str = "HellothisismetheProgrammer123"
            alphaString = str.isalpha()
        This will return True if only A-Z or a-z are present; otherwise, it will return False (0-9 and punctuations are not allowed).
"""

#count()
str = "afsaakfjdakjda"
StringCount = str.count("a")
print(StringCount)

#endswith()
str = "Hello guys!!!"
Newstring = str.endswith("!!!")
print(Newstring)

#startswith()
Newstring = str.startswith("Hello")
print(Newstring)

#find()
str = "He's a boy, he is not a girl"
FindString = str.find("a")
print(FindString)

#index()
FindStringIndex = str.index("a")
print(FindStringIndex)

#isalnum()
str = "HellothisismetheProgrammer123"
alphaString = str.isalnum()
print(alphaString)

#isalpha()
str = "HellothisismetheProgrammer"
alphaOnlyString = str.isalpha()
print(alphaOnlyString)

"""
    OUTPUT:
        5
        True
        True
        5
        5
        True
        True
"""
