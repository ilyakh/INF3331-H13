

<<<<<<< HEAD
translate(v = [0, 0, 0]) {
	cube(size = [101.6000000000, 53.3000000000, 1.0000000000]);
=======
union() {
	union() {
		union() {
			difference() {
				translate() {
					union() {
						scale(v = [1.0000000000, 0.8000000000, 1.0000000000]) {
							difference() {
								cylinder(h = 20.0000000000, r = 60.0000000000, center = true);
								cylinder(h = 30.0000000000, r = 50.0000000000, center = true);
								translate(v = [0, -30.0000000000, 0]) {
									cube(center = true, size = [120.0000000000, 60.0000000000, 30.0000000000]);
								}
							}
						}
						translate(v = [55.0000000000, -50.0000000000, 0]) {
							cube(center = true, size = [10.0000000000, 100.0000000000, 20.0000000000]);
						}
						translate(v = [-55.0000000000, -50.0000000000, 0]) {
							cube(center = true, size = [10.0000000000, 100.0000000000, 20.0000000000]);
						}
						translate(v = [0, -110.0000000000, 0]) {
							cube(center = true, size = [120.0000000000, 10.0000000000, 20.0000000000]);
						}
					}
				}
				translate(v = [0, 30.0000000000, 0]) {
					translate(v = [30.0000000000, 0, 0]) {
						color(c = "red") {
							rotate(a = 90, v = [1, 0, 0]) {
								cylinder(h = 80.0000000000, r = 4.5000000000, center = true);
							}
						}
					}
				}
			}
			translate() {
				color(c = "red") {
					scale(v = [1.3000000000, 1.3000000000, 1.0000000000]) {
						union() {
							scale(v = [1.0000000000, 0.8000000000, 1.0000000000]) {
								difference() {
									cylinder(h = 20.0000000000, r = 60.0000000000, center = true);
									cylinder(h = 30.0000000000, r = 50.0000000000, center = true);
									translate(v = [0, -30.0000000000, 0]) {
										cube(center = true, size = [120.0000000000, 60.0000000000, 30.0000000000]);
									}
								}
							}
							translate(v = [55.0000000000, -50.0000000000, 0]) {
								cube(center = true, size = [10.0000000000, 100.0000000000, 20.0000000000]);
							}
							translate(v = [-55.0000000000, -50.0000000000, 0]) {
								cube(center = true, size = [10.0000000000, 100.0000000000, 20.0000000000]);
							}
						}
					}
				}
			}
		}
		translate() {
			translate(v = [0, 15.5000000000, 0]) {
				translate(v = [30.0000000000, 0, 0]) {
					color(c = "red") {
						rotate(a = 90, v = [1, 0, 0]) {
							cylinder(h = 80.0000000000, r = 3.5000000000, center = true);
						}
					}
				}
			}
		}
	}
	translate() {
		translate(v = [0, 60.0000000000, 0]) {
			union() {
				cube(center = true, size = [50.0000000000, 15.0000000000, 5.0000000000]);
				translate(v = [0, 10.0000000000, 0]) {
					union() {
						rotate(a = 90, v = [0, 1, 0]) {
							cylinder(h = 60.0000000000, r = 5.0000000000, center = true);
						}
						translate(v = [-30.0000000000, 0, 0]) {
							sphere(r = 5.0000000000);
						}
						translate(v = [30.0000000000, 0, 0]) {
							sphere(r = 5.0000000000);
						}
					}
				}
			}
		}
	}
>>>>>>> 033f840d387372271d32b1334b5135ebd9e3fe87
}
/***********************************************
******      SolidPython code:      *************
************************************************
 
<<<<<<< HEAD
# -*- coding: utf8 -*-
=======
# -*- coding: utf-8 -*- 

# -*- coding: utf-8 -*-
>>>>>>> 033f840d387372271d32b1334b5135ebd9e3fe87

from core import *


<<<<<<< HEAD
=======

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
>>>>>>> 033f840d387372271d32b1334b5135ebd9e3fe87

class Enclosure( Element ):
    def create( self ):
        return cube( [ self.s.x, self.s.y, self.s.z ] )

class Handle( Element ):
    def create(self):

        sphere_offset = self.p.get('width') / 2.0 + self.p.get('radius')

        result = union() (

<<<<<<< HEAD
    e = Enclosure(
        Size( 101.6, 53.3, 1.0 ),
        parameters={
            "": 1.0
        }
    )

    e.create()
=======
            cube([
                self.p.get('width'),
                self.p.get('offset') * 1.5,
                self.p.get('offset') / 2.0,
            ], center=True),

            forward( self.p.get('offset') ) (
                union() (
                    rotate(90, [0, 1, 0]) (
                        cylinder(
                            h=self.p.get('width') * 1.2,
                            r=self.p.get('radius'),
                            center=True
                        )
                    ),

                    left( sphere_offset ) (
                        sphere( self.p.get('radius'))
                    ),

                    right( sphere_offset ) (
                        sphere( self.p.get('radius'))
                    )

                )
            ),


        )

        result = forward( 50 * 0.8 + self.p.get('offset') * 2 ) ( result )

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
            'width': 50.0,
            'offset': 10.0
        }
    )

    a.create()
    b.create()
    c_hole = c.create_hole()
    c.create()
    d.create()

    e = a.put() - c_hole + b.put() + c.put() + d.put()
>>>>>>> 033f840d387372271d32b1334b5135ebd9e3fe87

    scad_render_to_file( e, "project.scad" )


 
 
***********************************************/
                            
