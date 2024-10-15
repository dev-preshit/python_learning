"""
    # Day 51 is about the seek() and tell() functions in Python...
        In Python, the seek() and tell() functions are used to work with file
        objects and their positions within a file. These functions are part of
        the built-in I/O module, which provides a consistent interface for
        reading and writing to various file-like objects, such as files, pipes,
        and in-memory buffers.

        seek() function:
            Points to the character position passed as an argument, in bytes in the seek function...
        
        tell() function:
            Returns the current position within the file, in bytes...

        truncate() function:
            Truncates the file to a specific size...
"""

with open("Day51 myfile.txt", "r") as f:
    # Move to the 5th byte in the file
    f.seek(5)

    # Return current position of the pointer
    pos = f.tell()
    print(pos)
    # 5

    # Read the next 5 bytes after the 5th byte
    text = f.read(5)    
    print(text)
    # 6789A

with open("Day51 myfile.txt", "a") as f:
    f.write("\nHello world!!")
    f.truncate(23)

with open("Day51 myfile.txt", "r") as f:
    print(f.read())
    # 123456789ABCDEF
    # Hello
