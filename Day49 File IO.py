"""
    #Day 49 is about File IO in Python...
        File handling is an important task that can be done using pyhton...
        It is a build in function...

        To use file we have to ope file first using open function
        eg. 
            f = open("File_name","mode")
            where File_name is any file  with there extension is importnat 
            with there modes
            there are 3 modes to open a file 
                1.  read(r):This mode open the file to read only and give 
                    error is file dosent exist. This is a default mode if 
                    no mode parameter is pass.
                
                2.  write(w):This mode open the file for writing only and
                    create ne file if file dosent exist.
                
                3.  append(a):This mode ope the file for appending only
                    and creates a new file if the file doesnt exist.
                
                4.  create (x): This mode creates a file and gives an error
                    if the file already exists.

                5.  text (t): Apart from these modes we also need to
                    specify how the file must be handled. t mode is used
                    to handle text files. t refers to the text mode. There is
                    no difference between r and rt or w and wt since text
                    mode is the default. The default mode is iri (open for
                    reading text, synonym of 'rt' ).
                
                6. binary (b): used to handle binary files (images, pdfs, etc).
            eg.
                f = open('myfile.txt','w')

            instated of opening and closing the file multiply we can use WITH keyword.
            eg.
                with open("myfile.txt","r") as f:
                    text = f.read()
                    print(text)
                
"""

#file writing
f = open("Day49 myfile.txt","w")
f.write("Hello this is file handling")
f.close()

#File reading
f = open("Day49 myfile.txt","r")
text = f.read()
print(text)
f.close()

#File appending 
f = open("Day49 myfile.txt","a")
f.write("\nHello this is append mode")
f.close()

#With keyword
with open("Day49 myfile.txt","r") as f:
    text = f.read()
    print(text)
                