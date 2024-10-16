"""
    # Day 46 is about the os module in Python...
        The os module in Python can be used to perform various 
        computer file-related tasks. The os module is a built-in Python module
        that allows programmers to perform a wide variety of tasks, such as reading
        and writing files, interacting with the file system, and running system commands.
"""

#importing os module
import os

#create dir
os.mkdir("osmodule") 

#get current dir
print(os.getcwd()) 

#change dir
os.chdir("D:/git/osmodule") 
print(os.getcwd())

# bulk creation of dir
for i in range(1):  
    # checking existing files
    if os.path.exists(f"data {i}"):
        print("Dir allready exist")
    else:
        os.mkdir(f"data {i}")

#listing files present in dir
print(os.listdir("D:\git\osmodule"))

#rename files
for i in range(1):
        os.rename(f"data {i}",f"folder {i}")
print(os.listdir("D:\git\osmodule"))