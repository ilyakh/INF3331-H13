# -*- coding: utf8 -*- 

from solid import *
from solid.utils import *

from element import Element
from primitives import Union

def chunks( l, n ):
    for i in xrange(0, len(l), n):
        yield l[i:i+n]



class RadialCloud:
    def __init__( self, element, n ):
        self.step = 360.0 / n

    def get( self ):
        first = self.element.copy( self.points[0] )
        for x,y,z in self.points[1:]:
            first.join( self.element.rotate(90, 'z').copy( [x,y,z] ) )
        return first

class CornerCloud:
    def __init__( self, element, x, y ):
        self.element = element
        self.points = self.distribute( x, y )

    def get( self ):
        elements = []
        for x,y,z in self.points:
            elements.append( self.element.rotate(90, 'z').copy( [x,y,z] ) )
        return Union( *elements )

    def distribute( self, x, y, z=0 ):
        return [
            [-x,y,z],
            [-x,-y,z],
            [x,-y,z],
            [x,y,z]
        ]



class Cloud:
    def __init__( self, x, y, function=None ):
        result = []

        if not function:
            function = lambda x,y: sin( x * 0.5 ) + cos( y * 0.5 )

        for each_x in x:
            for each_y in y:
                z = function( each_x, each_y )
                result.append(
                    [each_x, each_y, z]
                )

        self.points = result



    def __mul__( self, element ):
        elements = []

        for x, y, z in self.points:
            elements.append(
                translate([x, y, z]) (
                    element.body.copy()
                )
            )

        max_x = max( self.points, key=lambda p: p[0] )[0]
        max_y = max( self.points, key=lambda p: p[1] )[1]

        element = Element()
        element.body = translate( [
            -(max_x / 2.0),
            -(max_y / 2.0)
        ] ) (
            union() ( *elements )
        )

        return element
