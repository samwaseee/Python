mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))  # apple
print(next(myit))  # banana
print(next(myit))  # cherry

mystring = "banana"
myit = iter(mystring)

for x in myit:
    print(x)  # b a n a n a


'''
🔍 What’s the Difference:
1. Explicit vs. Implicit Iterator
for x in mystr:
→ Python implicitly calls iter(mystr) behind the scenes.

myit = iter(mystr); for x in myit:
→ You're explicitly creating the iterator and passing it to the loop.

2. Reusability
mystr can be iterated over multiple times because it’s an iterable.

myit (the iterator) can be iterated only once. Once exhausted, it can’t be reused unless you call iter(mystr) again.
'''

class Mynumbers:
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        x = self.a
        self.a += 1 
        return x
    
myclass = Mynumbers()
myiter = iter(myclass)

print(next(myiter))  # 1
print(next(myiter))  # 2    
print(next(myiter))  # 3
print(next(myiter))  # 4
print(next(myiter))  # 5
print(next(myiter))  # 6


class vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Move!")

class car(vehicle):
   pass

class Boat(vehicle):
    def move(self):
        print("Sail!")

class Plane(vehicle):
    def move(self):
        print("Fly!")

car1 = car("Toyota", "Corolla")
boat1 = Boat("Yamaha", "242X")
plane1 = Plane("Boeing", "747")

for vehicle in (car1, boat1, plane1):
    print(vehicle.brand, vehicle.model)
    vehicle.move()