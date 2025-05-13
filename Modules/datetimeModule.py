import datetime

x = datetime.datetime.now()
print(x)  

print(x.year)
print(x.strftime(f"%A"+" %B "+ "%d %Y"))  
print(x.strftime("%x"))  # 10/05/23
print(x.strftime("%X"))  # 12:00:00
print(x.strftime("%c"))  # 10/05/23 12:00:00
print(x.strftime("%I:%M:%S %p"))  # 12:00:00 PM
print(x.strftime("%H:%M:%S"))  # 12:00:00
print(x.strftime("%Y-%m-%d %H:%M:%S"))  # 2023-10-05 12:00:00
print(x.strftime("%Y-%m-%d %I:%M:%S %p"))  # 2023-10-05 12:00:00 PM
print(x.strftime("%Y-%m-%d %H:%M:%S.%f"))  # 2023-10-05 12:00:00.000000

X = datetime.datetime(2023, 10, 5)
print(X)  # 2023-10-05 00:00:00
print(X.strftime("%A"))  # Thursday
print(X.strftime("%B"))  # October