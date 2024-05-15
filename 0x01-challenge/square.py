#!/usr/bin/python3
""" This comment is freaking  me out. """


class square():
    """A square class."""
    side = 0
    # height = 0

    def __init__(self, *args, **kwargs):
        """ The constructor. """
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square. """
        return self.side * self.side

    def PerimeterOfMySquare(self):
        """ Perimeter of a square. """
        return 4 * self.side;

    def __str__(self):
        """ String representation of square class. """
        return "{}/{}".format(self.side, self.side)


if __name__ == "__main__":
    s = square(side=12)
    print(s)
    print(s.area_of_my_square())
    print(s.PerimeterOfMySquare())
