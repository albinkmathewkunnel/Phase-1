#this is all about the args and kwargs 
#if you do not know how many arguments will passes into your function \
#*args and **kwargs allow functions to accet a unknows number of arguments 

def students(*kids):
    print("this is are my kids",kids[2])

students("albin","komal","eve")

#args means arbitary arguments 

#What is *args?
#The *args parameter allows a function to accept any number of positional arguments.

#Inside the function, args becomes a tuple containing all the passed arguments:

def my_function(*numbers):
  total = 0
  for num in numbers:
    total += num
  return total

print(my_function(1, 2, 3))
print(my_function(10, 20, 30, 40))
print(my_function(5))

#**kwargs
#If you do not know how many keyword arguments will be passed into your function, add two asterisks ** before the parameter name.

#This way, the function will receive a dictionary of arguments and can access the items accordingly:
def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")