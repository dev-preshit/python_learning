"""
    # Day 49 is about File I/O in Python...
        File handling is an important task that can be done using Python...
        It is a built-in function...

        To use a file, we have to open it first using the open function:
        Example: 
            f = open("File_name", "mode")
            where File_name is any file with its extension; it is important 
            along with its modes.
            There are 4 modes to open a file:
                1.  read (r): This mode opens the file for reading only and gives 
                    an error if the file doesn't exist. This is the default mode if 
                    no mode parameter is passed.
                
                2.  write (w): This mode opens the file for writing only and
                    creates a new file if the file doesn't exist.
                
                3.  append (a): This mode opens the file for appending only
                    and creates a new file if the file doesn't exist.
                
                4.  create (x): This mode creates a file and gives an error
                    if the file already exists.

                5.  text (t): Apart from these modes, we also need to
                    specify how the file must be handled. The t mode is used
                    to handle text files. 't' refers to text mode. There is
                    no difference between 'r' and 'rt' or 'w' and 'wt' since text
                    mode is the default. The default mode is 'rt' (open for
                    reading text, a synonym of 'rt').
                
                6.  binary (b): This mode is used to handle binary files (images, PDFs, etc).
            Example:
                f = open('myfile.txt', 'w')

            Instead of opening and closing the file multiple times, we can use the WITH keyword.
            Example:
                with open("myfile.txt", "r") as f:
                    text = f.read()
                    print(text)
"""

# File writing
f = open("Day49 myfile.txt", "w")
f.write("Hello, this is file handling.")
f.close()

# File reading
f = open("Day49 myfile.txt", "r")
text = f.read()
print(text)
f.close()

# File appending 
f = open("Day49 myfile.txt", "a")
f.write("\nHello, this is append mode.")
f.close()

# With keyword
with open("Day49 myfile.txt", "r") as f:
    text = f.read()
    print(text)
