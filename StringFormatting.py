price = 49

txt = f"The price is {price} dollars"

print(txt)

# The f-string (formatted string literal) is a way to format strings in Python. It allows you to embed expressions inside string literals, using curly braces {}.

txt = f"The price is {95:.2f} dollars"
print(txt)

txt = f"The price is very {'expensive' if price > 50 else 'cheap'}"
print(txt)

fruit = "baNaNa"
txt = f"I love {fruit.upper()} and {fruit.lower()}"
print(txt)

def myconvert(value):
    return value * 0.45359237

txt = f"10 pounds is {myconvert(10):.3f} kilograms"
print(txt)

price = 490000
txt = f"The price is {price:,} dollars"
print(txt)

# The :, format specifier is used to include commas as thousands separators in the formatted string.

txt = f"The price is {price:_} dollars"
print(txt)

txt = f"We have {49:<8} chickens."
print(txt)

txt = f"We have {49:>8} chickens."
print(txt)

txt = f"We have {49:^8} chickens."
print(txt)

txt = f"The temperature is {-5:=8} degrees celsius."
print(txt)

txt = f"The temperature is between {-3:+} and {7:+} degrees celsius."
print(txt)

txt = f"The temperature is between {-3:} and {7:} degrees celsius."
print(txt)

txt = f"The binary version of 50 is {50:b}"
print(txt)

txt = f"The hexadecimal version of 50 is {50:x}"
print(txt)

txt = f"The octal version of 50 is {50:o}"
print(txt)

txt = f"You scored {0.25:.0%}"
print(txt)

x = float('inf')

txt = f"The price is {x:F} dollars."
print(txt)

txt = f"We have {50000000000000:.2e} chickens."
print(txt)



price = 49
txt = "The price is {} dollars"
print(txt.format(price))

quantity = 3
itemno = 567
price = 49

txt = "I want {} pieces of item {} for {:.2f} dollars."
print(txt.format(quantity, itemno, price))

txt = "I want {2} pieces of item {0} for {1:.2f} dollars."
print(txt.format(quantity, price, itemno))

age = 36
name = "John"

txt = "His name is {0}, {1} is {2} years old."
print(txt.format(name, name, age))

myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname = "Ford", model = "Mustang"))