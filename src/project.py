# -*- coding: utf8 -*- 

from clouds import *
from primitives import *

if __name__ == "__main__":

    # create the rounded corner
    a = Cuboid( 10, 10, 1 )
    b = Cuboid( 5, 5, 1 ).left(2.5).forward(2.5)
    d = Frustum( 1, 2.5, 2.5 ).left(1.25).forward(1.25)
    c = Frustum( 1, 5, 5 )
    a.carve( b ).join( c ).carve( d )

    # assemble the part
    a = Union(
        a.copy( [15,20,0] ).mirror('x'), # upper right
        a.copy( [15,-20,0] ).mirror('y').mirror('x'), # lower right
        a.copy( [-15,-20,0] ).mirror('y'), # lower left
        a.copy( [-15,20,0] ), # upper left

        Cuboid( 40, 30, 1 ), # plate along y
        Cuboid( 20, 50, 1 ) # plate along x
    )

    a.save( "project.scad" )