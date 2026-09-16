#decorators let you add some extra behavious to a funnction without changing the functions code 

def decorator(func):
    def inner():
        return func().upper()
    return inner

@decorator 
def greet():
    return "hello albin"

print(greet())