"""
    #Day 98 is about multiProcessing in Python...
        Multiprocessing is a technique in programming that allows multiple 
        processes to run concurrently, taking advantage of multiple CPU cores. 
        In Python, we can use the multiprocessing module to implement multiprocessing. 
        In this tutorial, we will take a closer look at the multiprocessing module and 
        its various functions and how they can be used in Python.
"""

import multiprocessing
import requests

def downloadFile(url, name):
  print(f"Started Downloading {name}")
  response = requests.get(url)
  open(f"D:/git/osmodule/files/file{name}.jpg", "wb").write(response.content)
  print(f"Finished Downloading {name}")
 

if __name__ == "__main__":
  print("Starting the download process...")
  url = "https://picsum.photos/2000/3000"
  pros = []
  for i in range(50):
    # downloadFile(url, i)
    p = multiprocessing.Process(target=downloadFile, args=[url, i])
    p.start()
    pros.append(p)

  for p in pros:
    p.join()