mylist = ["apple","banana","cherry"]

print(mylist)

#list is changable 
# allow duplicates 
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

#list length 
thislist = ["apple", "banana", "cherry"]
print(len(thislist))

#List items  can be any data type

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

list1 = ["abc", 34, True, 40, "male"]

#also can be create using constructor 

thislist =list(("apple", "banana", "cherry"))
print(thislist)

# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.