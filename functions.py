def my_function():
    return "Hello from my_function!" # Function without arguments

# print(my_function())

def my_function_with_args(arg1, arg2):
    return f"Hello from my_function_with_args! Arguments: {arg1}, {arg2}" # Function with arguments

# print(my_function_with_args("arg1", "arg2"))

def my_function_with_default_args(*arg):
    return f"Hello from my_function_with_default_args! Arguments: {arg}" # Function with default arguments

# print(my_function_with_default_args("arg1", "arg2", "arg3"))

def my_function_with_keyword_args(child3, child2, child1):
    return f"The youngest child is {child3}" # Function with keyword arguments

# print(my_function_with_keyword_args(child1="John", child2="Jane", child3="Jim"))

def my_function(**kid):
  print("His last name is " + kid["lname"]) # Function with arbitrary keyword arguments

# my_function(fname = "Tobias", lname = "Refsnes") 

def my_function(x,/):
    return x * 2 # Function with positional-only argument

# print(my_function(5)) # Calling the function with a positional argument

def my_function(*,x):
    return x * 2 # Function with keyword-only argument

# print(my_function(x=5)) # Calling the function with a keyword argument

def my_function(a,b,/,*,c,d):
    return a + b + c + d # Function with positional-only and keyword-only arguments
                         # Any argument before the / , are positional-only, and any argument after the *, are keyword-only.

# print(my_function(1, 2, c=3, d=4)) # Calling the function with positional and keyword arguments

def tri_recursion(k):
    if k > 0:
        result = k + tri_recursion(k - 1) # Recursive function
        return result
    else:
        return 0
    return result

print(tri_recursion(6)) # Calling the recursive function