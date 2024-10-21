#Execies 8
#pdf merger
# Write a program to manipulate pdf files using pyPDF. Your programs 
# should be able to merge multiple pdf files into a single pdf. You are 
# welcome to add more functionalities
# pypdf is a free and open-source pure-python PDF library capable of splitting, 
# merging, cropping, and transforming the pages of PDF files. It can also add 
# custom data, viewing options, and passwords to PDF files. pypdf can retrieve 
# text and metadata from PDFs as well.

"""
    Folder Check:

    Listing Files:
        The program first lists all the files in the specified folder 
        D:\git\osmodule using the os.listdir() function.
        This list includes all files in the folder, regardless of the extension.

Merging Logic:

    Initialization:
        The PdfWriter object from the pypdf library is initialized with the name merger.
        This object allows the merging of multiple PDF files into one.

    Iterating Over Files:
        The for loop iterates through all the files in the folder.
        For each file, it checks if the file has a .pdf extension using if file.endswith(".pdf").
        If the file is a PDF, it prints the file name and appends it to the merger object using 
        the append() method.

    Merging Files:
        After all PDFs are appended, the merged PDF is written to the specified output path 
        D:\git\osmodule\MergedPdf.pdf using the write() method.
        The merger.close() method is called to close the writer and release the resources.

Output:

    After merging all PDFs, the program prints "Done" to indicate completion.

Main Program:

    The program begins by reading all the files in the folder using os.listdir().
    It appends all the .pdf files into a single merged document and saves it with the 
    name MergedPdf.pdf in the same folder.

"""


import pypdf as p
import os

merger = p.PdfWriter()
files = os.listdir("D:\\git\\osmodule")
print(files)

for file in files:
    if file.endswith(".pdf"):
        print(file)
        merger.append(f"D:\\git\\osmodule\\{file}")

else:
    print("Done")

merger.write("D:\\git\\osmodule\\MergedPdf.pdf")
merger.close()