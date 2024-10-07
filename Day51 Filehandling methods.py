"""
    #Day 51 is about seek() and tell() function in python...
        In Python, the seek() and tell() functions are used to work with file
        objects and their positions within a file. These functions are part of
        the built-in IO module, which provides a consistent interface for
        reading and writing to various file-like objects, such as files, pipes,
        and in-memory buffers.

        seek() function:
            Point the character position passed as argument, in byte in seek function...
        
        tell() function:
            Return the current position within the file, in byte...

        truncate() function:
            truncate the file to a specific size...
"""

with open("Day51 myfile.txt","r") as f:
    #move to the 15th byte in the file
    f.seek(5)

    #return current position of pointer
    pos = f.tell()
    print(pos)
    # 5

    #read the next 5 byte after 5th byte
    text = f.read(5)    
    print(text)
    # 6789A

with open("Day51 myfile.txt","a") as f:
    f.write("\nHello world!!")
    f.truncate(23)

with open("Day51 myfile.txt","r") as f:
    print(f.read())
    # 123456789ABCDEF
    # Hello

