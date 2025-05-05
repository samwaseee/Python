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

