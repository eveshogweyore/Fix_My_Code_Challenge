#!/usr/bin/python3
""" This comment is freaking me out. """


class square():
    """A square class."""

    width = 0
    height = 0

    #def __init__(self, *args, **kwargs):
    def __init__(self, side):
        """ The constructor. """
        #if kwargs:
            #for key, value in kwargs.items():
                #setattr(self, key, value)
        #else:
            #self.width = args[0]
            #self.height = args[1]
        self.height = side
        self.width = side

    def area_of_my_square(self):
        """ Area of the square. """
        return self.width * self.height

    def PerimeterOfMySquare(self):
        """ Perimeter of a square. """
        return (2 * self.width) + (2 * self.height)

    def __str__(self):
        """ String representation of square class. """
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    #s = square(width=12, height=9)
    s = square(12)
    print(s)
    print(s.area_of_my_square())
    print(s.PerimeterOfMySquare())
