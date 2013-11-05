# -*- coding: utf8 -*- 

import numpy
from solid import *
from solid.utils import *

class Movable:

    def right( self, distance=1 ):
        self.translate( [distance, 0, 0] )
        return self

    def left( self, distance=1 ):
        self.translate( [-distance, 0, 0] )
        return self

    def forward( self, distance=1 ):
        self.translate( [0, distance, 0] )
        return self

    def back( self, distance=1 ):
        self.translate( [0, -distance, 0] )
        return self

    def up( self, distance=1 ):
        self.translate( [0, 0, distance] )
        return self

    def down( self, distance=1 ):
        self.translate( [0, 0, -distance] )
        return self

    def anchor( self ):
        self.position.set([0, 0, 0])
        return self

    def drop( self ):
        self.body = translate( [0, 0, self['height'] / 2.0] ) ( self.body )
        return self

    def translate( self, vector ):
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