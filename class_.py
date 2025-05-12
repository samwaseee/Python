class MyClass:
    x = 5 # Class variable

p1 = MyClass() # Creating an instance of the class
# print(p1.x) # Accessing the class variable

# The __init__() function is called automatically every time the class is being used to create a new object.
# The __init__() function lets the class initialize the object's attributes and serves no other purpose.
# It is only used within classes.
class Person:
    def __init__(self, name, age):
        self.name = name # Instance variable
        self.age = age # Instance variable
    def myfunc(self):
        print("Hello my name is " + self.name) # Instance method
p1 = Person("John", 36) # Creating an instance of the class
# p1.myfunc() # Calling the instance method

del p1.age # Deleting the instance variable

# The __str__() function is called when you use the print() function on an object of the class.
# The __str__() function returns a string representation of the object.
class Person:
    def __init__(self, name, age):
        self.name = name # Instance variable
        self.age = age # Instance variable
    def myfunc(self):
        print("Hello my name is " + self.name) # Instance method
    def __str__(self):
        return f"Person name={self.name}, age={self.age}" # String representation of the object
p1 = Person("John", 36) # Creating an instance of the class
# print(p1) # Calling the __str__() function


p1.age = 40 # Changing the value of the instance variable
# print(p1) # Calling the __str__() function

del p1 # Deleting the instance variable

class Person:
    def __init__(abc, fname, lname):
        abc.firstname = fname
        abc.lastname = lname

    def printname(abc):
        print(abc.firstname, abc.lastname)


p1 = Person("John", "Doe")
# p1.printname() # John Doe

class Student(Person):
    pass # Inheriting the Person class

p2 = Student("Mike", "Olsen")
# p2.printname() # Mike Olsen

class Student(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname) # Calling the constructor of the parent class

x = Student("Mike", "Olsen")
# print(x.firstname) # Mike

class Student(Person):
    def __init__(abc, fname, lname):
        super().__init__(fname, lname) # Calling the constructor of the parent class
        # super() is a built-in function that returns a temporary object of the superclass  By using the super() function, you do not have to use the name of the parent element, it will automatically inherit the methods and properties from its parent.


x = Student("Mike", "Olsen")
print(x.firstname) # Mike

class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname) # Calling the constructor of the parent class
        self.graduationyear = 2023 # Instance variable

    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

x = Student("Mike", "Olsen")
x.welcome() # Welcome Mike Olsen to the class of 2023