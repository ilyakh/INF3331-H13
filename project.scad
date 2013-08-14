

translate() {
	union() {
		translate(v = [0, 0, 0]) {
			difference() {
				difference() {
					difference() {
						union() {
							translate(v = [2.3750000000, 0, 0]) {
								difference() {
									cube(center = true, size = [30.2500000000, 35, 15]);
									rotate(a = 90, v = [0, 1, 0]) {
										cylinder($fn = 72, h = 60.5000000000, r = 3.5500000000, center = true);
									}
								}
							}
							translate(v = [0, 0, 0]) {
								difference() {
									cube(center = true, size = [4.7500000000, 35, 15]);
									rotate(a = 90, v = [0, 1, 0]) {
										cylinder($fn = 72, h = 9.5000000000, r = 2.6750000000, center = true);
									}
								}
							}
							translate(v = [-2.3750000000, 0, 0]) {
								difference() {
									cube(center = true, size = [30.2500000000, 35, 15]);
									rotate(a = 90, v = [0, 1, 0]) {
										cylinder($fn = 72, h = 60.5000000000, r = 3.5500000000, center = true);
									}
								}
							}
						}
						translate(v = [0, 0, 7.6500000000]) {
							cube(center = true, size = [47.5000000000, 35, 15]);
						}
					}
				}
				union() {
					translate(v = [-14.5000000000, 0, 0]) {
						translate(v = [0, -14.5000000000, 0]) {
							cylinder($fn = 72, h = 100, r = 1.5000000000, center = true);
						}
						translate(v = [0, 14.5000000000, 0]) {
							cylinder($fn = 72, h = 100, r = 1.5000000000, center = true);
						}
					}
					translate(v = [14.5000000000, 0, 0]) {
						translate(v = [0, -14.5000000000, 0]) {
							cylinder($fn = 72, h = 100, r = 1.5000000000, center = true);
						}
						translate(v = [0, 14.5000000000, 0]) {
							cylinder($fn = 72, h = 100, r = 1.5000000000, center = true);
						}
					}
				}
			}
		}
	}
}
/***********************************************
******      SolidPython code:      *************
************************************************
 
# -*- coding: utf-8 -*-

from core import *


class Support( Element ):

    def create_inner( self ):

        length = self.s.x - ( self.p.get('core_length') )
        radius = self.p.get('inner_radius')

        return difference() (
            cube( [ length, self.s.y, self.s.z ], center=True ),
            rotate(90, [0,1,0]) (
                cylinder(
                    h=length *2,
                    r=radius,
                    center=True,
                    segments=self.p.get("segments")
                )
            )
        )

    def create_core( self ):
        length = self.p.get('core_length')
        radius = self.p.get('core_radius')

        return difference() (
            cube( [ length, self.s.y, self.s.z ], center=True ),
            rotate(90, [0,1,0]) (
                cylinder(
                    h=length *2,
                    r=radius,
                    center=True,
                    segments=self.p.get("segments")
                )
            )
        )

    def create_outer( self ):
        length = self.s.x - ( self.p.get('core_length') )
        radius = self.p.get('outer_radius')

        return difference() (
            cube( [ length, self.s.y, self.s.z ], center=True ),
            rotate(90, [0,1,0]) (
                cylinder(
                    h=length *2,
                    r=radius,
                    center=True,
                    segments=self.p.get("segments")
                )
            )
        )

    def create_bolt_hole( self ):
        return cylinder(
            self.p.get('bolt_hole_radius'),
            100,
            center=True,
            segments=self.p.get("segments")
        )

    def create_bolt_holes( self ):



        x_offset_from_center = self.s.half('x') - \
                             (self.p.get('bolt_hole_radius') + \
                              self.p.get('bolt_hole_outer_offset'))

        y_offset_from_center = self.s.half('y') - \
                             (self.p.get('bolt_hole_radius') + \
                              self.p.get('bolt_hole_outer_offset'))

        return union() (
            left( x_offset_from_center ) (
                back( y_offset_from_center ) ( self.create_bolt_hole() ),
                forward( y_offset_from_center ) ( self.create_bolt_hole() )
            ),
            right( x_offset_from_center ) (
                back( y_offset_from_center ) ( self.create_bolt_hole() ),
                forward( y_offset_from_center ) ( self.create_bolt_hole() )
            ),
        )

    def create_first_layer( self ):

        total_length = sum([
            self.p.get('inner_length'),
            self.p.get('core_length'),
            self.p.get('outer_length'),
        ])

        half_core_length = self.p.get('core_length') / 2.0

        return difference() (
            difference() (
                union() (
                    translate(
                        [self.p.get('inner_length') / 2.0 + half_core_length , 0, 0]
                    ) ( self.create_inner() ),
                    translate([0,0,0]) ( self.create_core() ),
                    translate(
                        [-(self.p.get('outer_length') / 2.0 + half_core_length), 0, 0]
                    ) ( self.create_outer() )
                ),
                # half to subtract
                translate([ 0, 0, self.s.half('z') + self.p.get("vertical_compensation") ]) (
                    cube([total_length * 10.0, self.s.y, self.s.z], center=True )
                )
            )
        )

    def apply_bolt_holes( self, target ):
        return difference() (
            target,
            self.create_bolt_holes()
        )

    def create_second_layer( self ):
        return mirror([1, 0, 0]) (
            self.create_first_layer()
        )

    def create( self ):

        spacing = 30

        # position with a equidistant point-cloud

        return union() (
            translate( [0, 0, 0] ) (
                self.apply_bolt_holes( self.create_first_layer() )
            ),

            # translate( [ self.s.x + spacing, 0, 0] ) (
            #    self.apply_bolt_holes( self.create_second_layer() )
            # ),


            # translate( [0, self.s.y + spacing, 0] ) (
            #
            #     translate( [ 0, 0, 0 ] ) (
            #         self.apply_bolt_holes(
            #             rotate( 90, [0,0,1] ) (
            #                 self.create_first_layer()
            #             )
            #         )
            #     ),
            #
            #     translate( [ self.s.x + spacing, 0, 0 ] ) (
            #         self.apply_bolt_holes(
            #             rotate( 90, [0,0,1] ) (
            #                 self.create_second_layer()
            #             )
            #         )
            #     )
            # )
            #
        )






if __name__ == "__main__":


    e = Support(
        Size( 35, 35, 15 ),
        parameters={
            'segments': 72,
            'outer_length': 0 ,
            'outer_radius': 3.55,
            'core_length': 4.75,
            'core_radius': 5.35 / 2.0,
            'inner_length': 0,
            'inner_radius': 3.55,
            'bolt_hole_radius': 1.5,
            'bolt_hole_outer_offset': 1.5,
            'vertical_compensation': 0.15
        }
    )
    e.create()

    scad_render_to_file( e.put(), "project.scad" ) 
 
***********************************************/
                            
