#the try-except block is used to handle exception in the python program

#the try block let you test a block for error 

# the except block lets you handle the eeror 
#the else block lets you execute code when there is no error 
#the finally block lets you execute code,regardless of the resulty of the try and except block 

# try:
#     print(x)
# except:
#     print("an exception occured")

# try:
#     x=10/0
 
#     print("division by zero")
# finally:
#     print("executing finally block") 


# def safe_divide(a,b):
#     try:
#         return a/b
#     except ZeroDivisionError:
#         print("division by zero is not allowed")
#     except TypeError:
#         print("invalid input type")


# safe_divide(10,0)


# def read_file_content(filename):
#     try:
#         open.read(filename)
#     except FileNotFoundError:
#         print("file not found")
#     except IsADirectoryError:
#         print("expected file but found directory")
#     finally:
#         print("executing finally block")

# read_file_content("test.txt")


def calculate_mean(numbers):
    if len(numbers)==0:
        raise ValueError("The list is empty. Cannot calculate mean.")
    return sum(numbers)/len(numbers)

numbers=[1,2,3,4,5]

print(calculate_mean(numbers))


def name(name):
    try:
        name =input("enter your name:")
        age = str(name)
    except ValueError:
        print("invalid input")

    


    