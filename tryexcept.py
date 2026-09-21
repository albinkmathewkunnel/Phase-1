#the try-except block is used to handle exception in the python program

#the try block let you test a block for error 

# the except block lets you handle the eeror 
#the else block lets you execute code when there is no error 
#the finally block lets you execute code,regardless of the resulty of the try and except block 

# try:
#     print(x)
# except:
#     print("an exception occured")

try:
    x=10/0
 
    print("division by zero")
finally:
    print("executing finally block") 


def safe_divide(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        print("division by zero is not allowed")
    except TypeError:
        print("invalid input type")


safe_divide(10,0)
        