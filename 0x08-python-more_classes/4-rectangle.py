#!/usr/bin/python3
"""This is a module for a Rectangle class"""


class Rectangle:
    """This class defines a rectangle"""

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle object

        Args:
            width (int): The width of the new rectangle
            height (int): The height of the new rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle

        Args:
            value (int): The new width of the rectangle

        Raises:
            TypeError: If value is not an integer
            ValueError: If value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle

        Args:
            value (int): The new height of the rectangle

        Raises:
            TypeError: If value is not an integer
            ValueError: If value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Return the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return a string representation of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join(["#" * self.__width for _ in range(self.__height)])

    def __repr__(self):
        """Return a string representation of the rectangle that
        can be used to recreate the rectangle object"""
        return "Rectangle({}, {})".format(self.__width, self.__height)
    # Import the Rectangle class from the 4-rectangle module
    Rectangle = __import__('4-rectangle').Rectangle

    # Create a new Rectangle object with width=2 and height=4
    my_rectangle = Rectangle(2, 4)

    # Print the string representation of the rectangle using
    # the __str__ method
    print(str(my_rectangle))

    # Print a separator
    print("--")

    # Print the string representation of the rectangle using
    # the print() function
    print(my_rectangle)

    # Print a separator
    print("--")

    # Print the string representation of the rectangle that can be
    # used to recreate the object using the __repr__ method
    print(repr(my_rectangle))

    # Print a separator
    print("--")

    # Print the memory address of the my_rectangle object in hexadecimal
    # format
    print(hex(id(my_rectangle)))

    # Print a separator
    print("--")

    # Create a new Rectangle object using the eval() function and
    # the string returned by the __repr__ method
    new_rectangle = eval(repr(my_rectangle))

    # Print the string representation of the new rectangle using
    # the __str__ method
    print(str(new_rectangle))

    # Print a separator
    print("--")

    # Print the string representation of the new rectangle using
    # the print() function
    print(new_rectangle)

    # Print a separator
    print("--")

    # Print the string representation of the new rectangle that can
    # be used to recreate the object using the __repr__ method
    print(repr(new_rectangle))

    # Print a separator
    print("--")

    # Print the memory address of the new_rectangle object in
    # hexadecimal format
    print(hex(id(new_rectangle)))

    # Print a separator
    print("--")

    # Check if new_rectangle and my_rectangle refer to the same
    # object in memory and print the result
    print(new_rectangle is my_rectangle)

    # Check if new_rectangle and my_rectangle are instances of the
    # same class and print the result
    print(type(new_rectangle) is type(my_rectangle))
