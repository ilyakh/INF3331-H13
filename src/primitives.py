# -*- coding: utf8 -*- 

import random
import preferences

from element import *



class CuboidFactory:
    def __init__( self ):
        pass

    def __call__( self, width=None, length=None, height=None ):
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


class FrustumFactory:
    def __init__( self ):
        pass

    def __call__( self, height=None, bottom_radius=None, top_radius=None ):
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


class SphereFactory:
    def __init__( self ):
        pass

    def __call__( self, radius=None ):
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

class PolyhedronFactory:
    pass


class UnionFunctor:
    def __init__( self ):
        pass

    def __call__( self, *args ):
        result = args[0]
        for element in args[1:]:
            result.join(element)
        return result

# uses factory methods to allow more flexible functionality
Cuboid   = CuboidFactory()
Frustum = FrustumFactory()
Sphere   = SphereFactory()
Union    = UnionFunctor()
