import json

x = '{"name": "John", "age": 30, "city": "New York"}'

y = json.loads(x)
# print(y["age"])  



x = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# convert into JSON
y = json.dumps(x)

# print(y)  # {"name": "John", "age": 30, "city": "New York"}

# print(json.dumps(x, indent=4))  # Pretty print JSON
# print(json.dumps(x, indent=4, separators=(";", "=")))  # Custom separators
# print(json.dumps(x, indent=4, sort_keys=True))  # Sort keys
# print(json.dumps(x, indent=4, ensure_ascii=False))  # Non-ASCII characters
# print(json.dumps(x, indent=4, default=str))  # Custom serialization
# print(json.dumps(x, indent=4, cls=json.JSONEncoder))  # Custom encoder


# print(json.dumps({"name": "John", "age": 30})) 
# print(json.dumps(["apple", "banana", "cherry"]))
# print(json.dumps(("apple", "cherry")))
# print(json.dumps("Hello"))
# print(json.dumps(42))
# print(json.dumps(3.14))
# print(json.dumps(True))
# print(json.dumps(None))
# print(json.dumps(False))


x = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "married": True,
    "divorced": False,
    "children": ("Anna", "Billy"),
    "pets": None,
    "cars": [
        {"model": "BMW 230", "mpg": 27.5},
        {"model": "Ford Edge", "mpg": 24.1},
        {"model": "Nissan Altima", "mpg": 25.1}
    ]
}

print(json.dumps(x, indent=4, separators=(";", "="), sort_keys=True, ensure_ascii=False)) 

