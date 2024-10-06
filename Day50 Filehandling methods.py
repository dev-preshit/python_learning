"""
    #Day 50 is about read(), readlines() in Python...
        
        readline():Read a single line from a file at a time
        eg.
            f = open("Day50 myfile.txt","r")
            line = readline()
            print(line)
            f.close()

        writeline():Write a single line on file
            f = open("Day50 myfile","w")
            list = [1,2,3,4,5,6,7,8,9]
            f.writelines(list)
            f.close()

"""
#writeline()
f = open("Day50 myfile.txt","w")
list = ['1\n','2\n','3\n','4\n','5\n']
f.writelines(list)
f.close()

f = open("Day50 myfile.txt",'a')
fruits = ['apple','mango','banana','grapes','orange']
i = 0
for fruit in fruits:
    i+=1
    f.write(f"{i}. {fruit}\n")
f.close()
    

#readline()
f = open("Day50 myfile.txt","r")
while True:
    line = f.readline()
    if not line:
        break
    print(line)
f.close()

