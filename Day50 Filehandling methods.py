"""
    # Day 50 is about read() and readlines() in Python...
        
        readline(): Read a single line from a file at a time.
        Example:
            f = open("Day50 myfile.txt", "r")
            line = f.readline()
            print(line)
            f.close()

        writelines(): Write a list of strings to a file.
        Example:
            f = open("Day50 myfile.txt", "w")
            items = ['1\n', '2\n', '3\n', '4\n', '5\n', '6\n', '7\n', '8\n', '9\n']
            f.writelines(items)
            f.close()
"""

#writelines()
f = open("Day50 myfile.txt", "w")
items = ['1\n', '2\n', '3\n', '4\n', '5\n']
f.writelines(items)
f.close()

f = open("Day50 myfile.txt", 'a')
fruits = ['apple', 'mango', 'banana', 'grapes', 'orange']
i = 0
for fruit in fruits:
    i += 1
    f.write(f"{i}. {fruit}\n")
f.close()
    
# readline()
f = open("Day50 myfile.txt", "r")
while True:
    line = f.readline()
    if not line:
        break
    print(line)
f.close()
