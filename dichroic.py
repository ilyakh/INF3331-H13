# -*- coding: utf-8 -*- 

# -*- coding: utf-8 -*-

from core import *



class Attachment( Element ):
    def create_arc( self ):
        frame_area_radius = self.p.get('arc_radius') + self.p.get('arc_frame_thickness')

        return difference() (
            cylinder(
                h=self.p.get('sled_thickness'),
                r=frame_area_radius,
                center=True
            ),
            cylinder(
                h=self.p.get('sled_thickness') + 10.0,
                r=self.p.get('arc_radius'),
                center=True
            ),
            translate( [0, -frame_area_radius / 2.0, 0] ) (
                cube([
                    frame_area_radius * 2.0,
                    frame_area_radius,
                    self.p.get('sled_thickness') + 10.0
                ], center=True )
            )
        )


    def create_arm( self ):
        frame_area_radius = self.p.get('arc_radius') + self.p.get('arc_frame_thickness')

        return cube([
            self.p.get('arc_frame_thickness'),
            self.p.get('arm_length'),
            self.p.get('sled_thickness')
        ], center=True)

    def create_back( self ):
        length = self.p.get('arc_radius') + (self.p.get('arc_frame_thickness'))
        length *= 2

        end_of_arms = self.p.get('arm_length') + ( self.p.get('arc_frame_thickness') / 2.0 )

        result = cube([
            length,
            self.p.get('arc_frame_thickness'),
            self.p.get('sled_thickness')

        ], center=True)

        result = back( end_of_arms + 5.0 ) ( result )

        return result


    def create( self ):

        arm_offset = self.p.get('arc_radius') + (self.p.get('arc_frame_thickness') / 2.0)
        arm_length = self.p.get('arm_length')

        return union() (
            # arc itself
            scale([1.0, 0.8, 1.0]) (
                self.create_arc()
            ),

            # the left arm
            translate([ arm_offset, -arm_length / 2.0, 0 ]) (
                self.create_arm()
            ),

            # the right arm
            translate([ -arm_offset, -arm_length / 2.0, 0 ]) (
                self.create_arm()
            ),

            self.create_back()
        )



class Sled( Attachment ):

    def create(self):
        arm_offset = self.p.get('arc_radius') + (self.p.get('arc_frame_thickness') / 2.0)
        arm_length = self.p.get('arm_length')

        result = scale([1.3, 1.3, 1.0]) (
            union() (
                # arc itself
                scale([1.0, 0.8, 1.0]) (
                    self.create_arc()
                ),

                # the left arm
                translate([ arm_offset, -arm_length / 2.0, 0 ]) (
                    self.create_arm()
                ),

                # the right arm
                translate([ -arm_offset, -arm_length / 2.0, 0 ]) (
                    self.create_arm()
                ),

                # self.create_back() # not available for the sled
            )
        )

        result = color('red') ( result )

        return result




class Dichroic( Element ):
    def create_hole( self ):
        result = cylinder(
            h=self.p.get('length'),
            r=self.p.get('radius') + self.p.get( 'inner_padding' ),
            center=True
        )

        result = rotate( 90, [1, 0, 0] ) ( result )
        result = color('red') ( result )

        result = right( self.p.get('right_offset') ) ( result )
        result = forward( 30.0 ) ( result )

        return result

    def create_rod(self):
        result = cylinder(
            h=self.p.get('length'),
            r=self.p.get('radius'),
            center=True
        )

        result = rotate( 90, [1, 0, 0] ) ( result )
        result = color('red') ( result )

        result = right( self.p.get('right_offset') ) ( result )
        result = forward( 15.5 ) ( result )

        return result

    def create( self ):
        return self.create_rod()


class Handle( Element ):
    def create_handle(self):

        result = union() (

            cube([
                self.p.get('width'),
                self.p.get('offset'),
            ], center=True),

            forward( self.p.get('offset') ) (
                rotate(90, [0, 1, 0]) (
                    cylinder(
                        h=self.p.get('width'),
                        r=self.p.get('radius'),
                        center=True
                    )
                )
            )

        )

        return result


if __name__ == "__main__":

    a = Attachment(
        None,
        parameters={
            'arc_radius': 50.0,
            'arc_frame_thickness': 10.0,
            'arm_length': 100.0,
            'sled_thickness': 20.0
        }
    )

    b = Sled(
        None,

        parameters={
            'arc_radius': 50.0,
            'arc_frame_thickness': 10.0,
            'arm_length': 100.0,
            'sled_thickness': 20.0,

        }
    )

    c = Dichroic(
        None,

        parameters={
            'radius': 3.5,
            'length': 80.0,
            'inner_padding': 1.0,
            'right_offset': 30.0
        }
    )

    d = Handle(
        None,

        parameters={
            'radius': 5.0,
            'width': 16.0,
            'offset': 1.0
        }
    )

    a.create()
    b.create()
    c_hole = c.create_hole()
    c.create()


    e = a.put() - c_hole + b.put() + c.put()

    scad_render_to_file( e, "project.scad" )


