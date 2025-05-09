thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "electric": False,
    "colors": ["red", "white", "blue"],
}
# print(thisdict)
# print(thisdict["brand"])  # Accessing a value using a key
# print(thisdict.get("model"))  # Accessing a value using the get() method
# print(thisdict.keys())  # Getting all keys in the dictionary
# print(thisdict.values())  # Getting all values in the dictionary
# print(len(thisdict))  # Getting the number of items in the dictionary

# for key in thisdict:  # Iterating through the dictionary
#     print(f"{key} : {thisdict[key]}")  # Accessing values using keys in a loop

# for value in thisdict.values():  # Iterating through the values
#     print(value)  # Accessing values in a loop

# for key, value in thisdict.items():  # Iterating through key-value pairs
#     print(key, value)  # Accessing key-value pairs in a loop

thisdict["year"] = 2020  # Updating a value
# print(thisdict)
thisdict["color"] = "red"  # Adding a new key-value pair
# print(thisdict)

# print(thisdict.items())  # Getting all key-value pairs in the dictionary

if "brand" in thisdict:  # Checking if a key exists in the dictionary
    print("Key 'brand' exists in the dictionary.")

thisdict.update({"year": 2021, "color": "blue"})  # Updating multiple values
# print(thisdict)
thisdict.pop("colors")  # Removing a key-value pair
# print(thisdict)
thisdict.popitem()  # Removing the last inserted key-value pair
# print(thisdict)
del thisdict["model"]  # Removing a key-value pair using del
# print(thisdict) 

# thisdict.clear()  # Removing all items from the dictionary

# del thisdict  # Deleting the entire dictionary

# print(thisdict)  # Printing the empty dictionary

mydict = thisdict.copy()  # Creating a copy of the dictionary
print(mydict)  # Printing the copied dictionary

mydict = dict(thisdict)  # Creating a copy of the dictionary using dict()
print(mydict)  # Printing the copied dictionary