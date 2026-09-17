def maxofthree(a,b,c):
    if a>b and a>c:
        return ("a",a) 
    elif b>a and b>c:
        return b
    else:
        return c

print(maxofthree(10,20,30))