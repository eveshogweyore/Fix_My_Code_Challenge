#!/usr/bin/python3
""" This comment is freaking  me out. """


class square():
    """A square class."""
    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """ The constructor. """
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square. """
        return self.width * self.height

    def PermiterOfMySquare(self):
        """ Perimeter of a rectangles. """
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """ String representaion of square class. """
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    s = square(width=12, height=12)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
