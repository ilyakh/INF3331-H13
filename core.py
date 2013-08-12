# -*- coding: utf8 -*- 

from solid import *
from solid.utils import *


from metrics import *

def partition( m, n ):

    result = []
    p = m / float(n)

    for i in range(n+1):
        result.append( p*i )
    return result



class Scalable:
    """
    Implies that if you reduced all sizes, and all positions towads the origin,
    you will have a scaled version of your element.

    Have to watch out for rounding errors.
    """
    pass


class Movable:
    def move( self, position ):
        self.position.x += position.x
        self.position.y += position.y
        self.position.z += position.z

    def __gt__( self, axis, distance ):
        pass

    def __lt__( self, axis, distance ):
        pass

    def left( self, distance ):
        pass

    def right( self, distance ):
        pass

    def up( self, distance ):
        pass

    def down( self, distance ):
        pass

    def forward( self, distance ):
        pass

    def back( self, distance ):
        pass






class Element( Movable, Scalable ):
    def __init__( self, size, position=None, parameters=None, *args, **kwargs ):
        """
        The constructor accepts the parameters common
        to all element children. It can also accept
        a dictionary of keyword-parameters (like
        hole_radius for hole element).
        """
        self.size = size
        self.position = position
        self.parameters = parameters

        self.s = self.size
        self.p = self.parameters


        self.sz = self.size
        self.prmtrs = self.parameters

    def create( self ):
        pass

    def put( self, position=None ):
        position = position if position else self.position
        return translate(position) (
            self.create()
        )









class Position:
    def __init__( self, x, y, z ):
        self.coordinates = {
            'x': x,
            'y': y,
            'z': z
        }

    def __getitem__( self, axis ):
        return self.coordinates[self.axis]

    def x( self ):
        return self.coordinates['x']

    def y( self ):
        return self.coordinates['y']

    def z( self ):
        return self.coordinates['z']









class Parameters:
    def __init__( self, elements, default=0.0 ):
        self.elements = elements
        self.default = default

    def __getitem__( self, name ):
        if self.elements.get('name'):
            return self.elements['name']
        else:
            print "Warning, the '{0}' property was not found, defaults to {1}.".format(
                name, self.default )
            return self.default
