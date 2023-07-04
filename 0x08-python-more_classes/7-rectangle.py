#!/usr/bin/python3


class Rectangle:
    """This class defines a rectangle"""

    # Class attributes to keep track of the number of instances
    # and the print symbol
    number_of_instances = 0
    print_symbol = "#"

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

    def __str__(self):
        """Return a string representation of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ""
        # Use the print_symbol class attribute as the symbol
        # for the string representation
        return "\n".join([str(self.print_symbol) * self.__width for _
                         in range(self.__height)])

    def __del__(self):
        """Print a message when an instance of Rectangle is deleted"""
        print("Bye rectangle...")
        # Decrement the number of instances when an instance is deleted
        Rectangle.number_of_instances -= 1
