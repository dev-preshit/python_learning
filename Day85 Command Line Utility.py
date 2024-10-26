"""
    #Day 85 is about Command line utility in python
        Command line utilities are programs that can be run
        from the terminal or command line interface, and they
        are an essential part of many development workflows.
        In Python, you can create your own command line
        utilities using the built-in argparse module.

        Creating command line utilities in Python is a straightforward 
        and flexible process thanks to the argparse module. With a few 
        lines of code, you can create powerful and customizable command 
        line tools that can make your development workflow easier and 
        more efficient. Whether you're working on small scripts or large 
        applications, the argparse module is a must-have tool for any 
        Python developer.
"""
import argparse
import requests

def download_file(url, local_filename): 
  if local_filename is None:
    local_filename = url.split('/')[-1]
    # NOTE the stream=True parameter below
  with requests.get(url, stream=True) as r:
      r.raise_for_status()
      with open(local_filename, 'wb') as f:
          for chunk in r.iter_content(chunk_size=8192): 
              # If you have chunk encoded response uncomment if
              # and set chunk_size parameter to None.
              #if chunk: 
              f.write(chunk)
  return local_filename
  
parser = argparse.ArgumentParser()

# Add command line arguments
parser.add_argument("url", help="Url of the file to download")
# parser.add_argument("output", help="by which name do you want to save your file")
parser.add_argument("-o", "--output", type=str, help="Name of the file", default=None)

# Parse the arguments
args = parser.parse_args()

# Use the arguments in your code
print(args.url)
print(args.output, type(args.output))
download_file(args.url, args.output)