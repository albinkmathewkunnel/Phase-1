# information which we are sharing into functions as arguments
#function with argument 

def myfunction(fname):
    print(fname + ""+"this is my first function with argument")

myfunction("albin")
myfunction("Komal")
myfunction("eve")

#parameter and arguments --parameter is the variable listed nside the parenthesis in the function defieniton,
# argment- is the actual vaue is that sent to the fucntion when its called 

def sum(a,b):
    print(a+b)

sum(10,11)

#number of arguments we can add 2 ,or more 
#you can assign value inside in the function paramter 

def sum(a,b=10):
    print(a+b)

sum(10)

#you can send arguments with the key value syntax 

def my_functions(animal,name):
    print("hello my "+animal+" name is"+name )

my_functions(animal='dog',name="binny")

#passing diffreent data types as arguments 
#string ,number,list,dictionary,etc

def diff(fruits):
    for i in fruits:
        print(i)

fruits=["apple","orange"]
diff(fruits)