import Modules.mymodule as m

a = m.person1["name"]

# print(a)

import platform

x = platform.system()
print(x)

x = platform.version()
print(x)

x = platform.machine()
print(x)

x = platform.platform()
print(x)

x = platform.processor()
print(x)

x = dir(platform)
print(x)

from Modules.mymodule import person1  #You can choose to import only parts from a module, by using the from keyword.

print(person1["name"])