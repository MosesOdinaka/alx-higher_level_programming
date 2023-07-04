#!/usr/bin/python3


class Rectangle:
    """This class defines a rectangle"""

    # Class attribute to keep track of the number of instances
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle object

        Args:
            width (int): The width of the new rectangle
            height (int): The height of the new rectangle
        """
        self.width = width
        self.height = height
        # Increment the number of instances when a new instance is created
        Rectangle.number_of_instances += 1

    # ... other methods and properties ...

    def __del__(self):
        """Print a message when an instance of Rectangle is deleted"""
        print("Bye rectangle...")
        # Decrement the number of instances when an instance is deleted
        Rectangle.number_of_instances -= 1


class Rectangle:
    """This class defines a rectangle"""

    # Class attribute to keep track of the number of instances
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle object

        Args:
            width (int): The width of the new rectangle
            height (int): The height of the new rectangle
        """
        self.width = width
        self.height = height
        # Increment the number of instances when a new instance is created
        Rectangle.number_of_instances += 1

    # ... other methods and properties ...

    def __del__(self):
        """Print a message when an instance of Rectangle is deleted"""
        print("Bye rectangle...")
        # Decrement the number of instances when an instance is deleted
        Rectangle.number_of_instances -= 1
