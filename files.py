#we are going to learn about the files handling 

# R for read 
#  a for append 
# w for write 
# x for create 
#  t text test mode 
#  b binary

f = open("demofile.txt")

f = open("demofile.txt","rt")
print(f.read())

# Using the with statement
# You can also use the with statement when opening a file:

with open("demofile.txt") as f:
    print(f.read())

# if you are not using the with statement, you must write a close statement in order to close the file:

f =open("demofile.txt")
print(f.read())

f.close()

# Read Only Parts of the File
# By default the read() method returns the whole text, but you can also specify how many characters you want to return:

with open("demofile.txt") as f:
    print(f.read(5))


# you can loop thrtough the lines 

with open("demofile.txt") as f:
    for x in f:
        print(x)


with open("demofile.txt","a") as f :
    f.write("now the file has more content  ")


# if you want to create a new file then 

f =open("myfile.txt","x")

f.write("hello world")