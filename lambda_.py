x = lambda a: a + 10 # Lambda function
print(x(5)) # Calling the lambda function

# Lambda functions can take any number of arguments but can only have one expression.
# The expression is evaluated and returned.

# You can use a lambda function wherever you would use a normal function.

x = lambda a, b: a * b # Lambda function with two arguments
print(x(5, 6)) # Calling the lambda function

x = lambda a, b, c: a + b + c # Lambda function with three arguments
print(x(5, 6, 2)) # Calling the lambda function

# Lambda functions can also be used as arguments to higher-order functions, such as map(), filter(), and reduce().
# For example, you can use a lambda function to square each element in a list:  
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers)) # Using map() with a lambda function
print(squared_numbers) # Output: [1, 4, 9, 16, 25]

# You can also use a lambda function to filter elements in a list:
filtered_numbers = list(filter(lambda x: x % 2 == 0, numbers)) # Using filter() with a lambda function
print(filtered_numbers) # Output: [2, 4]'

# You can also use a lambda function to reduce a list to a single value:
from functools import reduce
reduced_value = reduce(lambda x, y: x + y, numbers) # Using reduce() with a lambda function
print(reduced_value) # Output: 15

"""
Lambda functions are often used for short, throwaway functions that are not reused elsewhere in the code.
They are a convenient way to create small functions without the need for a full function definition.
However, for more complex functions or functions that are reused multiple times, it is generally better to use a regular function definition.
This makes the code more readable and maintainable.
In summary, lambda functions are a powerful feature of Python that allow you to create small, anonymous functions on the fly.
They are often used in functional programming and can be used as arguments to higher-order functions.
However, they should be used judiciously and not as a replacement for regular function definitions in all cases.
Lambda functions are a powerful feature of Python that allow you to create small, anonymous functions on the fly.
"""