# -*- coding: utf8 -*- 

import numpy
from solid import *
from solid.utils import *

class Movable:
    """
    An element that has this mixin can be moved. It stores an internal book
    keeping instance 'position', so it can be tracked and anchored to a
    certain location of the three dimensional space. The anchored position
    will affect he vector around which the element will be rotated.
    """


    def right( self, distance=1 ):
        """
        Moves the Movable distance points to the right (positive-x axis)

        @param distance:    the distance to move the element for
        @type  distance:    float
        """
        self.translate( [distance, 0, 0] )
        return self

    def left( self, distance=1 ):
        """
        Moves the Movable distance points to the left (negative x-axis)

        @param distance:    the distance to move the element for
        @type  distance:    float
        """
        self.translate( [-distance, 0, 0] )
        return self

    def forward( self, distance=1 ):
        """
        Moves the Movable distance points forward (positive y-axis)

        @param distance:    the distance to move the element for
        @type  distance:    float
        """
        self.translate( [0, distance, 0] )
        return self

    def back( self, distance=1 ):
        """
        Moves the Movable distance points back (negative y-axis)

        @param distance:    the distance to move the element for
        @type  distance:    float
        """
        self.translate( [0, -distance, 0] )
        return self

    def up( self, distance=1 ):
        """
        Moves the Movable distance points to the left (positive z-axis)

        @param distance:    the distance to move the element for
        @type  distance:    float
        """
        self.translate( [0, 0, distance] )
        return self

    def down( self, distance=1 ):
        """
        Moves the Movable distance points to the left (negative z-axis)

        @param distance:    the distance to move the element for
        @type  distance:    float
        """
        self.translate( [0, 0, -distance] )
        return self

    def anchor( self ):
        """
        Mark this position as the origin of this L{Element}.
        """
        self.position.set([0, 0, 0])
        return self

    def drop( self ):
        """
        Assign current position as the z-axis 0 reference.
        """
        self.body = translate( [0, 0, self['height'] / 2.0] ) ( self.body )
        return self

    def translate( self, vector ):
        """
        Perform movement described by the vector.

        @param vector:      movement to perform
        @type  vector:      3-list
        """
        vector = numpy.array( vector )
        self.position + vector
        self.body = translate( vector.tolist() ) ( self.body )
        return self


class Scalable:

    def scale( self, vector ):
        print vector
        if not isinstance( vector, list ):
            vector = [ vector ] * 3
        self.body = scale( vector ) ( self.body )

        return self

if __name__ == "__main__":
    import doctest
    doctest.testmod()