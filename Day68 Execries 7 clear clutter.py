# EXECRIES 7
# Clear Clutter
# Write a program to clear the clutter inside a folder on your computer.
# You should use os module to rename all the png images from l.png all
# the way till n.png where n is the number of png files in that folder. Do
# the same for other file formats

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