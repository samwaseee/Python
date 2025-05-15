# jhon

# name = input("Enter your name: ")
# age = input("Enter your age: ")
# print(f"Hello {name}, you are {age} years old.")

y = True

while y == True:
    x = input("Enter a number: ")
    try:
        x = float(x)  # Convert input to float
        y = False  # Exit the loop if conversion is successful
    except:
        print("Please enter a valid number.")

print(f"You entered: {x}")