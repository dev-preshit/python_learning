"""
    #Day 84 is about time module in python...
        This module allows us to use different time function 
        This is a build-in module in python

        • time.time()
        => This returns the time in second from 1 jan 1970.
        January 1, 1970 was the beginning of the Unix epoch, a fixed date and 
        time in computing that serves as a reference point for measuring system time: 

        • time.sleep()
        => This will ad time delay in second from where it is interpritted by python

        • time.localtime()
        => This function featch the local time from computer and create a string 
        
        • time.strftime()
        =>This function formats a time value as a string, based on a specified foramt.
        This function is particularly useful for formatting
        dates and times in a human-readable format, such as for display in a GUI,
        a log file, or a report.

"""

import time as t

# • time.time()
print(t.time())

#we can use this to find the time took to execute a function
def forloop():
    for i in range(100):
        print(i)

t1 = t.time()
forloop()
print(t.time() - t1)

# • time.sleep()
for i in range(65,91):
    print(chr(i))
    t.sleep(1)
    # This will print character from A to Z on 1 second delay

#• time.localtime()
time_struct = t.localtime()
print(time_struct)

# • time.strftime()
time_in_format = t.strftime("%d-%m-%Y %I:%M:%S %p",time_struct)
print(time_in_format)


def getDate():
    while True:
        time_struct = t.localtime()
        time_in_format = t.strftime("%I:%M:%S %p",time_struct)
        print(time_in_format,end="\r")

getDate()

