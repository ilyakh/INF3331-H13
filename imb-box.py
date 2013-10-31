# -*- coding: utf-8 -*-

from core import *


class Box( Element ):

    def create(self):
        return union() (
            self.create_bottom(),
            self.create_walls()
        )

    def create_bottom(self):
        result = cube([
            self.p.get('bottom_width'),
            self.p.get('bottom_length'),
            self.p.get('bottom_thickness')
        ], center = True)



        n = 30

        for i in range( n ):

            hole = cube([
                self.p.get( 'bottom_thickness' ),
                self.p.get( 'bottom_length' ),
                self.p.get( 'bottom_thickness' ),
            ], center= True)

            translate([x_pos, 0, 0]) (
                hole
            )

            result = union() (
                result,
                hole
            )


        result = translate([
            0,
            0,
            (self.p.get('height') / 2.0) - (self.p.get('bottom_thickness') / 2.0)
        ]) ( result )

        return result


    def create_walls(self):

        wall_thickness = self.p.get('wall_thickness')

        return difference() (

            cube([
                self.p.get('bottom_width') + wall_thickness,
                self.p.get('bottom_length') + wall_thickness,
                self.p.get('height'),
            ], center = True),

            cube([
                self.p.get('bottom_width'),
                self.p.get('bottom_length'),
                self.p.get('height'),
            ], center = True)

        )




if __name__ == "__main__":

    e = Box(
        None,
        parameters={
            'bottom_width': 54.00,
            'bottom_length': 75.50 + 13.50,
            'bottom_thickness': 1.00,
            'height': 5.00,
            'wall_thickness': 2.00,
        }
    )

    e.create()

    scad_render_to_file( e.put(), "project.scad" )