"""
    #Day 46 is about os module in Python...
        The os module in python can be use to do various 
        rcomputer's file related work. os module is a build-in python module
        It allows programmer to presform wide varity of task, such as reading
        and writing a file, intering with the file system, and running system commands.
"""
#importing os module
import os

#create dir
os.mkdir("osmodule") 

#get current dir
print(os.getcwd()) 

#change dir
os.chdir("D:\git\osmodule") 
print(os.getcwd())

# bulk creation of dir
for i in range(1,21):  
    # checking existing files
    if os.path.exists(f"data {i}"):
        print("Dir allready exist")
    else:
        os.mkdir(f"data {i}")

#listing files present in dir
print(os.listdir("D:\git\osmodule"))

#rename files
for i in range(1,21):
        os.rename(f"data {i}",f"folder {i}")
print(os.listdir("D:\git\osmodule"))