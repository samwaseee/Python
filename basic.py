x = 2;
y = "jhon";
Y = "Jhon"

if Y is y:
    print("Y is y(case sensitive)")

print(y + Y)

if x is y:
    print("x is y")
else:
    print("x is not y")
    print("x :", x, "which is :", type(x))
    print("y :", y, "which is :", type(y))


print(str(x))
print(float(x))
print(complex(x))
print(bool(x))



o,b,c = "orange", "banana", "cherry"
print(o)
print(b)
print(c)

o1 = o2 = o3 = "orange"
print(o1)
print(o2)
print(o3)

fruits = ["apple", "banana", "cherry"]
a, b, c = fruits
print(a)
print(b)
print(c)

print(type(fruits))
