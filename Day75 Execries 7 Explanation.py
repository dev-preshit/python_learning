#Execries 7 
# Clear Clutter
# Clear Clutter
# Write a program to clear the clutter inside a folder on your computer.
# You should use os module to rename all the png images from l.png all
# the way till n.png where n is the number of png files in that folder. Do
# the same for other file formats
"""
Folder Check:
    We check if the folder exists using the os.path.exists() function. 
    If the folder does not exist, the program informs the user and exits.

Renaming Logic:
    The main logic resides in the changer() function:

        • Input Parameters: It takes two arguments:
            file: The current file name in the folder.
            n: A counter to rename files in a sequential order (e.g., image1, image2, etc.).
        • Extension Check: It checks if the file ends with the .png extension using the string slicing.
        • Renaming Files: If the file is a .png, it renames the file using os.rename() and prints a 
          confirmation message.
        • Error Handling: If the file is not found or another error occurs during renaming, 
          a custom error message is printed using a try-except block.

Main Program:
    We first verify if the folder exists. If it doesn’t, an error message is shown and the program exits.
    If the folder exists, we list all files in the folder using os.listdir().
    A loop is used to go through each file. If a file is a .png, the changer() 
    function renames it, and a counter keeps track of the number of renamed files.
"""

import os

def changer(file, n):
    if file[-4:len(file)] == ".png":
        name = file[0:-4]
        try:
            os.rename(f"D:\git\osmodule\{file}",f"D:\git\osmodule\image {n}")
            print(f"{file} changed to image {n}")
        except FileNotFoundError:
            print(f"Error: file {file} not present in folder")
        except OSError as e:
            print("Error renaming file:",e)
        

if not os.path.exists("D:\git\osmodule"):
    print("File not exist")

n = 0
for file in os.listdir("D:\git\osmodule"):
    n += 1
    changer(file,n)