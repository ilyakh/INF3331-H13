# -*- coding: utf8 -*- 

import numpy


AXES = {
    "x":  [1,0,0],
    "y":  [0,1,0],
    "z":  [0,0,1],
    "-x": [-1,0,0],
    "-y": [0,-1,0],
    "-z": [0,0,-1]
}


class Position:
    """
    Test object is instantiated with a predefined position:
    >>> p = Position([3,5,2])

    The components of the numpy array can be extracted by providing a character
    corresponding to the axis as the first argument:
    >>> p.get('x')
    3.0
    >>> p.get('y')
    5.0
    >>> p.get('z')
    2.0

    Now, let's test the representation
    >>> p.get()
    [3.0, 5.0, 2.0]

    Test the operations:
    >>> p - [1,1,1]
    >>> p.get()
    [2.0, 4.0, 1.0]
    >>> p + [1,1,1]
    >>> p.get()
    [3.0, 5.0, 2.0]


    """

    def __init__( self, *args ):
        self.position = numpy.zeros(3)
        if args:
            self.position += numpy.array( *args )

        self.keywords = {
            0: ['x'],
            1: ['y'],
            2: ['z']
        }

    def __add__( self, vector ):
        self.position += vector

    def __sub__( self, vector ):
        self.position -= vector

    def get( self, axis=None ):
        if not axis:
            return self.to_list()

        for index,keywords in self.keywords.iteritems():
            if axis in keywords:
                return self.position[index]

    def set( self, axis, value=None ):
        if value is None:
            self.position = numpy.array(axis)
        else:
            for index,keywords in self.keywords.iteritems():
                if axis in keywords:
                    self.position[index] = value

    def get_keywords( self ):
        result = []
        for keywords in self.keywords.itervalues():
            result += keywords
        return result

    def get_x( self ):
        return self.position[0]

    def get_y( self ):
        return self.position[1]

    def get_z( self ):
        return self.position[2]

    def to_list( self ):
        return self.position.tolist()



if __name__ == "__main__":
    import doctest
    doctest.testmod()