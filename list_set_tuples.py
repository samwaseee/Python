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

print(f"List membership: {test_membership(list_collection):.6f} seconds")
print(f"Set membership: {test_membership(set_collection):.6f} seconds")
print(f"Tuple membership: {test_membership(tuple_collection):.6f} seconds")

tasks = ["Write report", "Email client", "Prepare presentation"]
tasks.append("Call team meeting")
tasks.remove("Email client")
tasks.insert(0,"Check emails")
print(tasks)

python_user = {'Alice', 'Bob', 'Charlie'}
java_user = {'David', 'Eve', 'Bob'}
user_who_use_both = python_user & java_user
print(user_who_use_both)


# Set operations
def set_operations(set1, set2):
    union = set1 | set2
    intersection = set1 & set2
    difference = set1 - set2
    symmetric_difference = set1 ^ set2
    return union, intersection, difference, symmetric_difference

set_operations_result = set_operations(python_user, java_user)
print(f"Union: {set_operations_result[0]}")
print(f"Intersection: {set_operations_result[1]}")
print(f"Difference: {set_operations_result[2]}")
print(f"Symmetric Difference: {set_operations_result[3]}")


# tuple
def tuple_operations(tup1, tup2):
    concatenated = tup1 + tup2
    repeated = tup1 * 2
    return concatenated, repeated

fruits = ('apple', 'banana', 'cherry')
vegetables = ('carrot', 'broccoli', 'spinach')
tuple_operations_result = tuple_operations(fruits, vegetables)
print(f"Concatenated: {tuple_operations_result[0]}")
print(f"Repeated: {tuple_operations_result[1]}")