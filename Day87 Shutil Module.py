"""
    Day 87 is about Shutil Module in python...
         shutil is use for high level file programming
        .copy(scr,dst):
            This function copies the file located at src to 
            a new location specified by dst. If the destination 
            location already exists, the original file will 
            be overwritten.

        .copy2(src, dst):
             This function is similar to shutil.copy, but it 
             also preserves more metadata about the original 
             file, such as the timestamp.
            
        .copytree(src, dst): 
            This function recursively copies 
            the directory located at src to a new location specified 
            by dst. If the destination location already exists, 
            the original directory will be merged with it.
        
        .move(src, dst): This function moves the file located at 
        src to a new location specified by dst. This function is 
        equivalent to renaming a file in most cases.

        .rmtree(path): This function recursively deletes the 
        directory located at path, along with all of its contents. 
        This function is similar to using the rm -rf command in 
        a shell.

    
"""
import shutil as shu

shu.copy("osmodule\\MergedPdf.pdf","firstImg.pdf")
shu.copy2("osmodule\\MergedPdf.pdf","Metadata.pdf")
shu.copytree("osmodule","newmodule")
shu.move("python_learning\\test.py","osmodule")
shu.rmtree("newmodule")

# Note: do not run it without any knowledge as it may 
# led to creation and delection of certain files...