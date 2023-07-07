#!/usr/bin/python3
def say_my_name(first_name, last_name=""):
    """
    Prints a name in the format "My name is <first name> <last name>".

    Args:
        first_name (str): The first name to print.
        last_name (str): The last name to print. Defaults to an empty string.

    Raises:
        TypeError: If first_name or last_name are not strings.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")
