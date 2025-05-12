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

for key in thisdict:  # Iterating through the dictionary
#     print(f"{key} : {thisdict[key]}")  # Accessing values using keys in a loop 
        pass

for value in thisdict.values():  # Iterating through the values
#     print(value)  # Accessing values in a loop
        pass

for key, value in thisdict.items():  # Iterating through key-value pairs
#     print(key, value)  # Accessing key-value pairs in a loop
        pass

thisdict["year"] = 2020  # Updating a value
# print(thisdict)
thisdict["color"] = "red"  # Adding a new key-value pair
# print(thisdict)

# print(thisdict.items())  # Getting all key-value pairs in the dictionary

if "brand" in thisdict:  # Checking if a key exists in the dictionary
    # print("Key 'brand' exists in the dictionary.")
    pass

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
# print(mydict)  # Printing the copied dictionary

mydict = dict(thisdict)  # Creating a copy of the dictionary using dict()
# print(mydict)  # Printing the copied dictionary

x = mydict.setdefault("model", "Mustang")  # Setting a default value for a key
# print(x)  # Printing the default value

child1 = {
    "name": "John",
    "year": 2000,
}
child2 = {
    "name": "Jane",
    "year": 2002,
}
child3 = {
    "name": "Mike",
    "year": 2004,
}
myfamily = {
    "child1": child1,
    "child2": child2,
    "child3": child3,
}
# print(myfamily)  # Printing the nested dictionary
# print(myfamily["child1"]["name"])  # Accessing a value in a nested dictionary

for x,obj in myfamily.items():  # Iterating through the nested dictionary
    # print(x)  # Accessing keys in a loop
    for y in obj:  # Iterating through the inner dictionary
        # print(y +':', obj[y])  # Accessing key-value pairs in a loop
        pass

x ={'key1', 'key2', 'key3'}  # Creating a set

thisdict = dict.fromkeys(x, 0)  # Creating a dictionary with keys from a set
# print(thisdict)  # Printing the dictionary with keys from a set