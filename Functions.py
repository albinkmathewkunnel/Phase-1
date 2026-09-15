# creating functions 

def my_functions():
    print("albin k mathew ")

my_functions()

# why using functions 

def fahrenheit_to_celcius(value):
    return (value - 32)* 5/9

print(fahrenheit_to_celcius(10))
print(fahrenheit_to_celcius(95))

# WHY WE ARE USING THE RETURN STATEMENT CAUSE AFTER COMPLETING THE EXECUTION WE ARE SENDING THE RESULT BACK TO THE CODE 
# SO IT WILL STOP EXECUTION AND SEND THE RESULT BACK 

def greeting ():
    return "heloo from a function"

message=greeting()

print(message)

# the funcions cannot be empty if you need to use a function for a placeholder or for anything you need to add a 'PASS' keyword 

def myfun():
    pass
