# This error occurs whe you are using the wrong data type.
# len(1234)
# TypeError: object of type 'int' has no len()
# This error occurs when you try to use a method or function that is not applicable to the data type you are working with.
# For example, trying to find the length of an integer using the len() function will raise a TypeError because integers do not have a length.
# To fix this error, you need to ensure that you are using the correct data type for the operation you are trying to perform.
# In this case, you can convert the integer to a string before using the len() function.
print(len(str(1234)))
# This will return the length of the string representation of the integer, which is 4 in this case.
# Type return return which data type is returned by a function.
# For example, the type() function returns the data type of the object passed to it.
# This can be useful for debugging and understanding the data types you are working with in your code.
print(type(1234))  # Output: <class 'int'>
print(type(12.34))  # Output: <class 'float'>
print(type("Hello"))  # Output: <class 'str'>
print(type(False))  # Output: <class 'bool'>
print(type([1, 2, 3]))  # Output: <class 'list'>
print(type((1, 2, 3)))  # Output: <class 'tuple'>
print(type({1, 2, 3}))  # Output: <class 'set'>
print(type({"key": "value"}))  # Output: <class 'dict'>
# This code demonstrates the use of the type() function to check the data types of various objects in Python.
# It prints the data type of each object, such as integers, floats, strings, booleans, lists, tuples, sets, and dictionaries.
# The output shows the class of each object, which helps in understanding the data types being used in the code.
