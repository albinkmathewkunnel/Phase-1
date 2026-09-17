# def maxofthree(a,b,c):
#     if a>b and a>c:
#         return ("a",a) 
#     elif b>a and b>c:
#         return b
#     else:
#         return c

# print(maxofthree(10,20,30))

list1 =[10,20,50]

def findsum(list1):
    sum=0
    for i in list1:
        sum+=i
    return sum

print(findsum(list1))