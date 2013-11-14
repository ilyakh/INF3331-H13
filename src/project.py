# -*- coding: utf8 -*-

from clouds import *
from primitives import *
from util.coord_transform import cartesian_to_spherical

def connect( self, other ):

    thickness = 1.0

    arr = lambda x: numpy.array(x)
    mag = lambda x: numpy.linalg.norm(x)

    a = self.position.get()
    b = other.position.get()

    r, theta, phi = cartesian_to_spherical( arr(b) - arr(a) )

    print r, theta, phi, arr(b) - arr(a)


    from primitives import Frustum
    bridge = Frustum( r, 1.0, 1.0 ).color("yellow")
    bridge.global_rotate( -theta * 2 * pi, 'y' )
    bridge.global_rotate( -phi * 2 * pi, 'z' )


    self.join( bridge, other )

    return self

def spherical_pipe_connector():

    r = 5

    c = Cuboid( r*4, r*4, r*4 )

    c.carve(
        Frustum( r*10, r, r ).rotate( 90, 'y').up(r*2).left(r*4),
    )

    c.carve(
        Frustum( r*10, r, r )
    )

    c.intersect( Sphere( r*2 ) ).drop()


    c.save( "project.scad" )



def arduino_template( power_hole=True, usb_hole = True ):
    h = 20.0

    base = Cuboid( 68.6 + 10, 53.3 + 10, 1 ).\
        forward( 53.3 / 2 - 7.5 ).\
        left( 68.6 / 2 - 5 )

    hole = Frustum( h, 1.3 )

    power_side_near   = hole.copy().back( 5.1 ).left( 50.8 )
    power_side_far    = hole.copy()
    usb_side_far      = hole.copy().forward( 27.9 )
    usb_side_near     = usb_side_far.copy().forward( 15.2 ).left( 50.8 )

    return Union(
        power_side_far,
        power_side_near,
        usb_side_far,
        usb_side_near
    )

def arduino_standoffs():
    h = 5.0

    base = Cuboid( 68.6 + 10, 53.3 + 10, 1 ).\
        forward( 53.3 / 2 - 7.5 ).\
        left( 68.6 / 2 - 5 )


    hole = Frustum( h, 1.3 + (1.0 * 2) )

    power_side_near   = hole.copy().back( 5.1 ).left( 50.8 )
    power_side_far    = hole.copy()
    usb_side_far      = hole.copy().forward( 27.9 )
    usb_side_near     = usb_side_far.copy().forward( 15.2 ).left( 50.8 )

    return Union(
        power_side_far,
        power_side_near,
        usb_side_far,
        usb_side_near
    )


if __name__ == "__main__":

    h = 30

    bottom_spacing = 5

    hull_area = Cuboid( 100, 75, h )
    bottom = Cuboid( 100, 75, 3.0 ).up( bottom_spacing )

    enclosure = Cuboid(
        hull_area['width'],
        hull_area['length'] + 5 * 2.0,
        hull_area['height'] + 3 * 2.0,
    )

    enclosure.carve( hull_area.scale([1,1,1.5])).join( bottom )

    front_panel = Cuboid(
        3.0,
        hull_area['length'] + 5 * 2.0 + 20.0 * 2.0,
        hull_area['height'] + 3 * 2.0
    )

    front_panel_hole = Frustum( 100.0, 3.0 ).rotate( 90, 'y' ).\
        up( hull_area['height'] / 2.0 + 3 ).left( 10 )

    front_panel_holes = Union(
        front_panel_hole.copy().forward( hull_area['length'] / 2.0 + 15.0 ),
        front_panel_hole.copy().back( hull_area['length'] / 2.0 + 15.0 ),
        Frustum( 50.0, 7 ).rotate( 90, 'y' )
            .translate( [-10, 20, hull_area['height'] / 2.0 + 2.5 ] ),
        Cuboid( 14, 22, 50.0 ).rotate( 90, 'y' )
            .translate( [-10, -10, hull_area['height'] / 2.0 + 2.5 ] ),
    )


    front_panel.carve(
        front_panel_holes
    )


    back_panel_holes = Cuboid( hull_area['width'] / 3.0, 40.0, 2.0 )

    back_panel = Cuboid(
        3.0,
        hull_area['length'] + 5 * 2.0,
        hull_area['height'] + 3 * 2.0
    ).carve(
        back_panel_holes.up( hull_area['height'] / 3.0 )
    )


    # holes
    enclosure.join(
        arduino_standoffs().
            rotate( 180, 'z' ).
            translate([-20, 20, bottom_spacing])
    ).carve(
        arduino_template().
            rotate( 180, 'z' ).
            translate([-20, 20, 0])
    )


    enclosure.join(
        front_panel.right( hull_area['width'] / 2.0 ),
        back_panel.left( hull_area['width'] / 2.0 )
    )


    enclosure.save( "project.scad" )