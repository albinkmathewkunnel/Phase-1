thisdict={
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

# Dictionaries are used to store data values in key:value pairs.

# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

# IF you want to accessa specif value you can 

print(thisdict["brand"])
#When we say that dictionaries are ordered, it means that the items have a defined order, and that order will not change.

# Unordered means that the items do not have a defined order, you cannot refer to an item by using an index.

# Changeable
# Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created.

# Duplicates Not Allowed
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)