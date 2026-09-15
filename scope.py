# a variable is only available from inside the region it is created. This is called scope.
#local scope a variable created inside a function belongs to the local scope of that function, and can only be used inside that function.

def myfunction():
    x="albin"
    print(x)
myfunction()

# as explained above the variable x is not available outside the function, so this will cause an error:
def myfunction():
    x="albin"
    def anotherfunction():
        print(x)
    anotherfunction()

myfunction()

# global scope --available within any scope and local 

x ="albin"

def globalscope():
    print(x)

globalscope()

#NON LOCAL KEYWORD 

def nonlocalfunction():
    x="albin"
    print("outer function",x)

    def myfunction2():
        nonlocal x
        x="komal"
    myfunction2()
    return x

nonlocalfunction()