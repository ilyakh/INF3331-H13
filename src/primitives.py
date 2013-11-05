# -*- coding: utf8 -*- 

import random, sys
import preferences

from element import *


class PrimitiveFactory( object ):
    """
    A factory that creates either Cuboid, Frustum, Sphere or any other
    user-defined primitive.
    """
    pass

class CuboidFactory( PrimitiveFactory ):
    """
    Creates a Cuboid:

    U{http://en.wikipedia.org/wiki/Cuboid}
    """

    def __init__( self ):
        pass

    def __call__( self, width=None, length=None, height=None ):
        """
        @param      width:   the size of the cuboid across the x-axis
        @type       width:   float

        @param      length:  the size of the cuboid across the y-axis
        @type       length:  float

        @param      height:  the size of the cuboid across the z-axis
        @type       height:  float

        @return     Element with a Cuboid body
        """
        if width and not length:
            length = width
        if not height:
            height = 1.0

        element = Element()

        element['width'] = width
        element['length'] = length
        element['height'] = height

        element.body = cube(
            [ width, length, height ],
            center=True
        )

        element.drop()
        element.color() # applies a random color

        return element


class FrustumFactory( PrimitiveFactory ):
    """
    Creates a Frustum.

    U{http://en.wikipedia.org/wiki/Frustum}
    """


    def __init__( self ):
        pass

    def __call__( self, height=None, bottom_radius=None, top_radius=None ):
        """
        @param      height:   the size of the cuboid across the x-axis
        @type       height:   float

        @param      bottom_radius:      the radius of the lower ring of the
                                        frustum
        @type       bottom_radius:      float

        @param      top_radius:         the radius of the upper ring of frustum
        @type       top_radius:         float

        @return     Element with a Frustum body
        """

        if not height:
            height = 1.0

        if bottom_radius == 0:
            bottom_radius = 1.0 / sys.maxint

        if top_radius == 0:
            top_radius = 1.0 / sys.maxint

        if bottom_radius is None:
            bottom_radius = 1.0
            top_radius = bottom_radius

        if top_radius is None:
            top_radius = bottom_radius

        element = Element()

        element['height'] = height
        element['length'] = max( top_radius, bottom_radius ) * 2.0
        element['width'] = max( top_radius, bottom_radius ) * 2.0
        element['top_radius'] = top_radius
        element['bottom_radius'] = bottom_radius

        element.body = cylinder(
            h=height,
            r=top_radius,
            r1=bottom_radius,
            center=True,
            segments=preferences.SEGMENTS
        )

        element.drop()
        element.color() # applies a random color

        return element


class SphereFactory( PrimitiveFactory ):
    """
    Creates a sphere.

    U{http://en.wikipedia.org/wiki/Sphere}
    """

    def __init__( self ):
        pass

    def __call__( self, radius=None ):
        """
        @param      radius:     the radius of the Sphere
        @type       radius:     float

        @return     Element with a spherical body
        """
        if not radius:
            radius = 1.0

        element = Element()

        element['height'] = radius * 2.0
        element['length'] = radius * 2.0
        element['width'] = radius * 2.0
        element['radius'] = radius

        element.body = sphere(
            r=radius,
            segments=preferences.SEGMENTS
        )

        element.drop()
        element.color() # applies a random color

        return element

class PolyhedronFactory( PrimitiveFactory ):
    pass


class UnionFunctor( object ):
    """
    Creates a union of multiple Elements.

    Can be modified to apply a special operation to each Element that comes
    through.
    """
    def __init__( self ):
        pass

    def __call__( self, *args ):
        """
        @param      args:      elements to join, the first element keeps the
                               properties, while others are joined onto it

        @return:    union of elements provided in args
        @rtype:     Element
        """
        result = args[0]
        for element in args[1:]:
            result.join( element )
        return result


# uses factory methods to allow more flexible functionality
Cuboid   = CuboidFactory()
Frustum = FrustumFactory()
Sphere   = SphereFactory()
Union    = UnionFunctor()
