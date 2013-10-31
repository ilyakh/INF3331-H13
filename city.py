# -*- coding: utf-8 -*-

from core import *
from random import randint



class House( Element ):


    def create_base( self ):
        base = cube([
            self.p.get('width'),
            self.p.get('length'),
            self.p.get('base_height')
        ], center=True )

        base = up( self.p.get('base_height') / 2.0 ) ( base )

        return base

    def create_roof( self ):
        diagonal = sqrt(
            pow( self.p.get('width'), 2 ) + pow( self.p.get('length'), 2 )
        )

        x = self.p.get('width') / 2.0
        y = self.p.get('length') / 2.0
        z = self.p.get('roof_height')

        roof = polyhedron(
            points=[
                [-x, -y, 0],      # 1
                [-x, y, 0],     # 2
                [x, y, 0],    # 3
                [x, -y, 0],     # 4
                [0, 0, z]        # 5 (top point)
            ],
            triangles=[ [0,1,4],[1,2,4],[2,3,4],[3,0,4],[1,0,3],[2,1,3] ]
        )

        roof = up(
            ( self.p.get('base_height') )
        ) ( roof )

        return roof


    def create( self ):
        return union() (
            self.create_base(),
            self.create_roof()
        )


class City( Element ):
    def create( self ):
        houses = []

        for i in range(self.s.x):
            for k in range(self.s.y):

                width = randint( 15, 25 )
                length = randint( 15, 30 )

                candidate = House( None, parameters={
                    'width': width,
                    'length': length,
                    'base_height': randint( 10, 20 ),
                    'roof_height': max( width, length ) / randint( 2, 4 )
                })
                candidate = candidate.put()


                candidate = rotate( randint(1,3) * 10, [0, 0, 1]) (
                    candidate
                )

                offset_x = randint( 5, 7 ) + width
                offset_y = randint( 5, 7 ) + length

                candidate = translate([
                     offset_x * i,
                     offset_y * k,
                     0
                ]) ( candidate )
                houses.append( candidate )

        return union() (
            *houses
        )


if __name__ == "__main__":

    e = House(
        None,
        parameters={
            'width': 10.0,
            'base_height': 10.0,
            'length': 15.0,
            'roof_height': 5.0
        }
    )

    e = City(
        Size( 10, 10, 0 ),
    )

    e.create()

    scad_render_to_file( e.put(), "project.scad" )