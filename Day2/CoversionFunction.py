# How to convert a string to an integer in Python
def string_to_int(s):
    try:
        return int(s)
    except ValueError:
        print(f"Error: '{s}' is not a valid integer.")
        return None
# How to convert a string to a float in Python


def string_to_float(s):
    try:
        return float(s)
    except ValueError:
        print(f"Error: '{s}' is not a valid float.")
        return None
# How to convert an integer to a string in Python


def int_to_string(i):
    return str(i)
# How to convert a float to a string in Python


def float_to_string(f):
    return str(f)
# How to convert a string to a boolean in Python


def string_to_bool(s):
    if s.lower() in ['true', '1', 'yes']:
        return True
    elif s.lower() in ['false', '0', 'no']:
        return False
    else:
        print(f"Error: '{s}' is not a valid boolean string.")
        return None
# How to convert a boolean to a string in Python


def bool_to_string(b):
    return str(b).lower()  # Convert boolean to lowercase string representation
# How to convert a string to a list in Python


def string_to_list(s, delimiter=','):
    # Split the string by the specified delimiter (default is comma)
    return s.split(delimiter)
# How to convert a list to a string in Python


def list_to_string(lst, delimiter=','):
    # Join the list elements into a string with the specified delimiter (default is comma)
    return delimiter.join(lst)
# How to convert a string to a tuple in Python


def string_to_tuple(s, delimiter=','):
    # Split the string by the specified delimiter and convert to a tuple
    return tuple(s.split(delimiter))
# How to convert a tuple to a string in Python


def tuple_to_string(tup, delimiter=','):
    # Join the tuple elements into a string with the specified delimiter (default is comma)
    return delimiter.join(tup)
# How to convert a string to a set in Python


def string_to_set(s, delimiter=','):
    # Split the string by the specified delimiter and convert to a set
    return set(s.split(delimiter))
# How to convert a set to a string in Python


def set_to_string(s, delimiter=','):
    # Join the set elements into a string with the specified delimiter (default is comma)
    return delimiter.join(s)
# How to convert a string to a dictionary in Python


def string_to_dict(s, item_delimiter=',', key_value_delimiter=':'):
    try:
        return dict(item.split(key_value_delimiter) for item in s.split(item_delimiter))
    except ValueError:
        print(f"Error: '{s}' is not a valid dictionary string.")
        return None
# How to convert a dictionary to a string in Python


def dict_to_string(d, item_delimiter=',', key_value_delimiter=':'):
    return item_delimiter.join(f"{key}{key_value_delimiter}{value}" for key, value in d.items())


# Example usage of the conversion functions
if __name__ == "__main__":
    # String to Integer
    print(string_to_int("123"))  # Output: 123
    print(string_to_int("abc"))  # Output: Error message

    # String to Float
    print(string_to_float("123.45"))  # Output: 123.45
    print(string_to_float("abc"))  # Output: Error message

    # Integer to String
    print(int_to_string(123))  # Output: "123"

    # Float to String
    print(float_to_string(123.45))  # Output: "123.45"

    # String to Boolean
    print(string_to_bool("True"))  # Output: True
    print(string_to_bool("false"))  # Output: False
    print(string_to_bool("maybe"))  # Output: Error message

    # Boolean to String
    print(bool_to_string(True))  # Output: "true"

    # String to List
    # Output: ['apple', 'banana', 'cherry']
    print(string_to_list("apple,banana,cherry"))

    # List to String
    # Output: "apple,banana,cherry"
    print(list_to_string(['apple', 'banana', 'cherry']))

    # String to Tuple
    # Output: ('apple', 'banana', 'cherry')
    print(string_to_tuple("apple,banana,cherry"))

    # Tuple to String
    # Output: "apple,banana,cherry"
    print(tuple_to_string(('apple', 'banana', 'cherry')))

    # String to Set
    # Output: {'apple', 'banana', 'cherry'}
    print(string_to_set("apple,banana,cherry"))

    # Set to String
    # Output: "apple,banana,cherry"
    print(set_to_string({'apple', 'banana', 'cherry'}))

    # String to Dictionary
    # Output: {'name': 'John', 'age': '30', 'city': 'New York'}
    print(string_to_dict("name:John,age:30,city:New York"))

    # Dictionary to String
    # Output: "name:John,age:30,city:New York"
    print(dict_to_string({'name': 'John', 'age': '30', 'city': 'New York'}))
