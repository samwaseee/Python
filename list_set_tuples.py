import time

# Setup
list_collection = list(range(10000))
set_collection = set(range(10000))
tuple_collection = tuple(range(10000))

# Membership testing
def test_membership(collection, iterations=1000):
    start = time.time()
    for i in range(iterations):
        _ = 9999 in collection
    return time.time() - start

# print(f"List membership: {test_membership(list_collection):.6f} seconds")
# print(f"Set membership: {test_membership(set_collection):.6f} seconds")
# print(f"Tuple membership: {test_membership(tuple_collection):.6f} seconds")

tasks = ["Write report", "Email client", "Prepare presentation"]
tasks.append("Call team meeting")
tasks.remove("Email client")
tasks.insert(0,"Check emails")
del tasks[2] # Deleting an element by index
tasks.pop(1) # Removing an element by index and returning it
# print(tasks)
tasks[1:3] = ["Update report", "Send invoice"] # Replacing elements in a slice
this_tuple = ("apple", "banana", "cherry")
tasks.append(this_tuple) # Appending a tuple to the list
# print(tasks)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]  # List comprehension to filter fruits containing 'a'
# print(newlist)

fruits.sort()  # Sorting the list in ascending order
# fruits.sort(reverse=True)  # Sorting the list in descending order
# print(fruits)

new_fruits = fruits.copy()  # Creating a shallow copy of the list
# print(new_fruits)

this_list = ["abc", 34, True, 40, "male", 3.14, "abc"] # List with mixed data types and duplicates
# print(this_list)
# print(this_list[0])  # Accessing first element
# print(this_list[2:5])  # Slicing the list
# print(this_list[-1])  # Accessing last element
# print(this_list[1:])  # Slicing from index 1 to end
# print(this_list[:3])  # Slicing from start to index 3
# print(this_list[-4:-1])  # Slicing from index -4 to -1
# print(this_list[::2])  # Slicing with step 2

python_user = {'Alice', 'Bob', 'Charlie'}
java_user = {'David', 'Eve', 'Bob'}
user_who_use_both = python_user & java_user
# print(user_who_use_both)
# print(list(python_user))  # Convert set to list


# Set operations
def set_operations(set1, set2):
    union = set1 | set2
    intersection = set1 & set2
    difference = set1 - set2
    symmetric_difference = set1 ^ set2
    return union, intersection, difference, symmetric_difference

set_operations_result = set_operations(python_user, java_user)
# print(f"Union: {set_operations_result[0]}")
# print(f"Intersection: {set_operations_result[1]}")
# print(f"Difference: {set_operations_result[2]}")
# print(f"Symmetric Difference: {set_operations_result[3]}")

thisset1 = {"apple", "banana", "cherry", "apple"} # Set with duplicates(will be removed)
# print(thisset1)

thisset = {"apple", "banana", "cherry", True, 1, False, 0, 3.14} # Set with mixed data types(True, 1 and False, 0 are considered equal)
# print(thisset)
thisset.add("orange")  # Adding an element to the set
# print(thisset)
thisset.remove("banana")  # Removing an element from the set
# print(thisset)
# thisset.discard("banana")  # Discarding an element from the set (no error if not found)
# print(thisset)
# print(thisset.pop())  # Removing and returning an arbitrary element from the set
# print(thisset)

# thisset.clear()  # Clearing the set
# del thisset  # Deleting the set

# print("banana" in thisset)  # Membership test

# print(thisset.issuperset(thisset1))  # Checking if thisset is a superset of thisset1

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

# print(thisset) 



# tuple
def tuple_operations(tup1, tup2):
    concatenated = tup1 + tup2
    repeated = tup1 * 2
    return concatenated, repeated

fruits = ('apple', 'banana', 'cherry', 'kiwi', 'mango', 'apple', 'orange')
vegetables = ('carrot', 'broccoli', 'spinach')
tuple_operations_result = tuple_operations(fruits, vegetables)
# print(f"Concatenated: {tuple_operations_result[0]}")
# print(f"Repeated: {tuple_operations_result[1]}")

y = list(fruits)  # Convert tuple to list
y[1] = 'blueberry'  # Modify the list
fruits = tuple(y)  # Convert list back to tuple
# print(fruits)

(a, b, c) = vegetables  # Unpacking tuple
# print(a,b,c)

(a, b, *c) = fruits  # Unpacking with star operator
# print(a, b, c)  # c will be a list of the remaining elements

# print(fruits.index('kiwi'))  # Find index of 'kiwi' in the tuple
# print(fruits.count('apple'))  # Count occurrences of 'apple' in the tuple