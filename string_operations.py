big_str = '''lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'''

a = "hello, world"

print(a[5:])
print(a[0:5])
print(a[:-5])
print(a[0:10:2])
print(a[10::-1])

if "lorem" in a:
    print("yes")

print(a.count("lorem"))
print("expension" in a)

print(a.upper())
print(a.lower())


b = "    hello, world    "
print(b.strip())  # removes leading and trailing whitespace
print(b.lstrip())  # removes leading whitespace
print(b.rstrip())  # removes trailing whitespace

print(b.replace("hello", "hi"))  # replaces all occurrences of "hello" with "hi"
print(b.split(","))  # splits the string into a list of substrings using "," as the delimiter

print(a+" " + b)  # concatenates two strings
print(a*3)  # repeats the string 3 times

age = 25   
txt = "My name is John, and I am {} years old".format(age)  # using format method
print(txt)

price = 49.99
txt = f"My name is John, and I am {age} years old. The price is {price:.2f}"  # using f-string
print(txt)

txt = f"The price is {20 * 59} dollars"
print(txt)

txt = "We are the so-called \"Vikings\" from the north."  # using escape character to include double quotes
print(txt)