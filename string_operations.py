big_str = '''lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'''
print(len(big_str)) 

a = "hello, world"

print(a[5:]) # prints from index 5 to the end
print(a[0:5]) # prints from index 0 to 5 (not including 5)
print(a[:-5]) # prints from the beginning to the last 5 characters
print(a[0:10:2]) # prints from index 0 to 10 with a step of 2
print(a[10::-1]) # prints from index 10 to the beginning with a step of -1 (reverses the string)

if "lorem" in a: # checks if "lorem" is in the string
    print("yes")

print(a.count("lorem")) # counts the number of occurrences of "lorem" in the string
print("expension" in a) # checks if "expension" is in the string

print(a.upper())
print(a.lower())

print("________________________________________________________")


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

txt = "Hello\rWorld!" # using carriage return to move the cursor to the beginning of the line
print(txt) 

txt = "Hello\tWorld!" # using tab to add a tab space
print(txt)

txt = "Hello\bWorld!" # using backspace to remove the last character
print(txt)

txt = "\110\145\154\154\157"
print(txt) # prints "Hello" using octal values

txt = "\x48\x65\x6c\x6c\x6f"
print(txt) # prints "Hello" using hexadecimal values

txt = "Hello\nWorld!" # using newline to move to the next line
print(txt)

txt = "Hello\vWorld!" # using vertical tab to move to the next line
print(txt)

txt = "Hello\fWorld!" # using form feed to move to the next line
print(txt)

print("________________________________________________________")

txt = "Hello Python!"

print(txt.capitalize()) # capitalizes the first character of the string
print(txt.title()) # capitalizes the first character of each word in the string
print(txt.swapcase()) # swaps the case of each character in the string
print(txt.isalnum()) # checks if the string is alphanumeric (contains only letters and numbers)
print(txt.isalpha()) # checks if the string contains only letters
print(txt.isdigit()) # checks if the string contains only digits
print(txt.islower()) # checks if the string is in lowercase
print(txt.isupper()) # checks if the string is in uppercase
print(txt.istitle()) # checks if the string is in title case (first character of each word is uppercase)
print(txt.isnumeric()) # checks if the string contains only numeric characters
print(txt.isdecimal()) # checks if the string contains only decimal characters
print(txt.isidentifier()) # checks if the string is a valid identifier (variable name)
print(txt.isprintable()) # checks if the string is printable (contains only printable characters)
print(txt.isspace()) # checks if the string contains only whitespace characters
print(txt.isascii()) # checks if the string contains only ASCII characters
print(txt.islower()) # checks if the string is in lowercase
print(txt.isupper()) # checks if the string is in uppercase
print(txt.casefold()) # returns a case-insensitive version of the string
print(txt.rjust(20)) # right-aligns the string in a field of 20 characters
print(txt.ljust(20)) # left-aligns the string in a field of 20 characters
print(txt.center(20)) # centers the string in a field of 20 characters
print(txt.zfill(20)) # pads the string with zeros on the left to make it 20 characters long
print(txt.expandtabs(4)) # replaces tabs with spaces (4 spaces per tab)
print(txt.startswith("Hello")) # checks if the string starts with "Hello"
print(txt.endswith("Python!")) # checks if the string ends with "Python!"
print(txt.count("o")) # counts the number of occurrences of "o" in the string
print(txt.encode("utf-8")) # encodes the string to bytes using UTF-8 encoding
print(txt.expandtabs(4)) # replaces tabs with spaces (4 spaces per tab)
print(txt.format_map({"name": "John", "age": 25})) # formats the string using a dictionary
print(txt.index("Python")) # returns the index of the first occurrence of "Python" in the string
print(txt.rindex("Python")) # returns the index of the last occurrence of "Python" in the string
print(txt.format_map({"name": "John", "age": 25})) # formats the string using a dictionary
print(txt.partition("Python")) # splits the string into a tuple of three parts: before, separator, and after the first occurrence of "Python"
print(txt.rpartition("Python")) # splits the string into a tuple of three parts: before, separator, and after the last occurrence of "Python"
print(txt.join(["Hello", "World"])) # joins the list of strings with the string as a separator
print(txt.splitlines()) # splits the string into a list of lines