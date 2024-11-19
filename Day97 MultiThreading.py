"""
    #Day 97 is about multiThereading in Python...
        Multithreading is a technique in programming that allows multiple 
        threads of execution to run concurrently within a single process. 
        In Python, we can use the threading module to implement multithreading. 
        In this tutorial, we will take a closer look at the threading module and 
        its various functions and how they can be used in Python.
"""

import threading as th
import time

def func1():
    for i in range(65,91):
        print(chr(i))
        time.sleep(1)
    
def func2():
    for i in range(65,91):
        print(i)
        time.sleep(1)

t1 = th.Thread(target=func1)
t2 = th.Thread(target=func2)

t1.start()
t2.start()

