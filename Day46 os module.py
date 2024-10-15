"""
    # Day 46 is about the os module in Python...
        The os module in Python can be used to perform various 
        computer file-related tasks. The os module is a built-in Python module
        that allows programmers to perform a wide variety of tasks, such as reading
        and writing files, interacting with the file system, and running system commands.
"""

#importing os module
import os

#create directory
os.mkdir("osmodule") 

#get current directory
print(os.getcwd()) 

#change directory
os.chdir("D:\\git\\osmodule") 
print(os.getcwd())

# bulk creation of directories
for i in range(1, 21):  
    # checking for existing directories
    if os.path.exists(f"data {i}"):
        print("Directory already exists")
    else:
        os.mkdir(f"data {i}")

#listing files present in directory
print(os.listdir("D:\\git\\osmodule"))

#rename directories
for i in range(1, 21):
    os.rename(f"data {i}", f"folder {i}")
print(os.listdir("D:\\git\\osmodule"))
