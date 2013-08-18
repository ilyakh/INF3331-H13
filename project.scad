

translate() {
	union() {
		union() {
			union() {
				union() {
					cube(center = false, size = [15.0000000000, 40.0000000000, 1.0000000000]);
					translate(v = [-15.0000000000, 0, 0]) {
						rotate(a = 90, v = [0, 0, 1]) {
							difference() {
								cube(size = [40.0000000000, 2.0000000000, 1.0000000000]);
								translate(v = [1.0000000000, 0, 0]) {
									cube(size = [36.0000000000, 1.1000000000, 1.0000000000]);
								}
							}
						}
					}
					translate(v = [0, 40.0000000000, 0]) {
						difference() {
							cube(size = [15.0000000000, 2.0000000000, 1.0000000000]);
							translate(v = [1.0000000000, 0, 0]) {
								cube(size = [11.0000000000, 1.1000000000, 1.0000000000]);
							}
						}
					}
					translate(v = [15.0000000000, 40.0000000000, 0]) {
						intersection() {
							cube(size = [2.0000000000, 2.0000000000, 1.0000000000]);
							cylinder($fn = 32, h = 2.0000000000, r = 2.0000000000);
						}
					}
				}
				mirror(v = [1, 0, 0]) {
					union() {
						cube(center = false, size = [15.0000000000, 40.0000000000, 1.0000000000]);
						translate(v = [-15.0000000000, 0, 0]) {
							rotate(a = 90, v = [0, 0, 1]) {
								difference() {
									cube(size = [40.0000000000, 2.0000000000, 1.0000000000]);
									translate(v = [1.0000000000, 0, 0]) {
										cube(size = [36.0000000000, 1.1000000000, 1.0000000000]);
									}
								}
							}
						}
						translate(v = [0, 40.0000000000, 0]) {
							difference() {
								cube(size = [15.0000000000, 2.0000000000, 1.0000000000]);
								translate(v = [1.0000000000, 0, 0]) {
									cube(size = [11.0000000000, 1.1000000000, 1.0000000000]);
								}
							}
						}
						translate(v = [15.0000000000, 40.0000000000, 0]) {
							intersection() {
								cube(size = [2.0000000000, 2.0000000000, 1.0000000000]);
								cylinder($fn = 32, h = 2.0000000000, r = 2.0000000000);
							}
						}
					}
				}
			}
			mirror(v = [0, 1, 0]) {
				union() {
					union() {
						cube(center = false, size = [15.0000000000, 40.0000000000, 1.0000000000]);
						translate(v = [-15.0000000000, 0, 0]) {
							rotate(a = 90, v = [0, 0, 1]) {
								difference() {
									cube(size = [40.0000000000, 2.0000000000, 1.0000000000]);
									translate(v = [1.0000000000, 0, 0]) {
										cube(size = [36.0000000000, 1.1000000000, 1.0000000000]);
									}
								}
							}
						}
						translate(v = [0, 40.0000000000, 0]) {
							difference() {
								cube(size = [15.0000000000, 2.0000000000, 1.0000000000]);
								translate(v = [1.0000000000, 0, 0]) {
									cube(size = [11.0000000000, 1.1000000000, 1.0000000000]);
								}
							}
						}
						translate(v = [15.0000000000, 40.0000000000, 0]) {
							intersection() {
								cube(size = [2.0000000000, 2.0000000000, 1.0000000000]);
								cylinder($fn = 32, h = 2.0000000000, r = 2.0000000000);
							}
						}
					}
					mirror(v = [1, 0, 0]) {
						union() {
							cube(center = false, size = [15.0000000000, 40.0000000000, 1.0000000000]);
							translate(v = [-15.0000000000, 0, 0]) {
								rotate(a = 90, v = [0, 0, 1]) {
									difference() {
										cube(size = [40.0000000000, 2.0000000000, 1.0000000000]);
										translate(v = [1.0000000000, 0, 0]) {
											cube(size = [36.0000000000, 1.1000000000, 1.0000000000]);
										}
									}
								}
							}
							translate(v = [0, 40.0000000000, 0]) {
								difference() {
									cube(size = [15.0000000000, 2.0000000000, 1.0000000000]);
									translate(v = [1.0000000000, 0, 0]) {
										cube(size = [11.0000000000, 1.1000000000, 1.0000000000]);
									}
								}
							}
							translate(v = [15.0000000000, 40.0000000000, 0]) {
								intersection() {
									cube(size = [2.0000000000, 2.0000000000, 1.0000000000]);
									cylinder($fn = 32, h = 2.0000000000, r = 2.0000000000);
								}
							}
						}
					}
				}
			}
		}
		translate(v = [-25.0000000000, 0, 0]) {
			color(c = "red") {
				union() {
					translate(v = [-5.0000000000, 0, 0]) {
						union() {
							union() {
								cube(size = [2.5000000000, 40.0000000000, 1.0000000000]);
								rotate(a = 90, v = [0, 0, 1]) {
									translate(v = [1.0000000000, 0, 0]) {
										union() {
											cube(size = [36.0000000000, 1.0000000000, 1.0000000000]);
											translate(v = [18.0000000000, 1.0000000000, 0.5000000000]) {
												rotate(a = 90, v = [0, 1, 0]) {
													cylinder($fn = 32, h = 36.0000000000, r = 0.5000000000, center = true);
												}
											}
										}
									}
								}
							}
							mirror(v = [0, 1, 0]) {
								union() {
									cube(size = [2.5000000000, 40.0000000000, 1.0000000000]);
									rotate(a = 90, v = [0, 0, 1]) {
										translate(v = [1.0000000000, 0, 0]) {
											union() {
												cube(size = [36.0000000000, 1.0000000000, 1.0000000000]);
												translate(v = [18.0000000000, 1.0000000000, 0.5000000000]) {
													rotate(a = 90, v = [0, 1, 0]) {
														cylinder($fn = 32, h = 36.0000000000, r = 0.5000000000, center = true);
													}
												}
											}
										}
									}
								}
							}
						}
					}
					mirror(v = [-1, 0, 0]) {
						union() {
							union() {
								cube(size = [2.5000000000, 40.0000000000, 1.0000000000]);
								rotate(a = 90, v = [0, 0, 1]) {
									translate(v = [1.0000000000, 0, 0]) {
										union() {
											cube(size = [36.0000000000, 1.0000000000, 1.0000000000]);
											translate(v = [18.0000000000, 1.0000000000, 0.5000000000]) {
												rotate(a = 90, v = [0, 1, 0]) {
													cylinder($fn = 32, h = 36.0000000000, r = 0.5000000000, center = true);
												}
											}
										}
									}
								}
							}
							mirror(v = [0, 1, 0]) {
								union() {
									cube(size = [2.5000000000, 40.0000000000, 1.0000000000]);
									rotate(a = 90, v = [0, 0, 1]) {
										translate(v = [1.0000000000, 0, 0]) {
											union() {
												cube(size = [36.0000000000, 1.0000000000, 1.0000000000]);
												translate(v = [18.0000000000, 1.0000000000, 0.5000000000]) {
													rotate(a = 90, v = [0, 1, 0]) {
														cylinder($fn = 32, h = 36.0000000000, r = 0.5000000000, center = true);
													}
												}
											}
										}
									}
								}
							}
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

class Quarter(Element):

    def create_quarter_of_usable_area( self ):

        long_attachment_area = difference() (
            cube([
                self['usable_area_length'] / 2.0,
                self['height'] * 2.0,
                self['height']
            ]),
            # subtract the attachment hole
            right( self['attachment_hole_padding'] / 2.0 ) (
                cube([
                    ( (self['usable_area_length'] / 2.0) - ( self['attachment_hole_padding'] * 2)),
                    self['height'] + self['hole_markup'],
                    self['height']
                ])
            )
        )

        narrow_attachment_area = difference() (
            cube([
                self['usable_area_width'] / 2.0,
                self['height'] * 2.0,
                self['height']
            ]),
            # subtract the attachment hole
            right( self['attachment_hole_padding'] / 2.0 ) (
                cube([
                    ( (self['usable_area_width'] / 2.0) - (self['attachment_hole_padding'] * 2)),
                    self['height'] + self['hole_markup'],
                    self['height']
                ])
            )
        )

        # rotate the long side
        long_attachment_area = rotate(90, [0, 0, 1]) (
            long_attachment_area
        )

        # move the areas
        long_attachment_area = left( self['usable_area_width'] / 2.0 ) (
            long_attachment_area
        )

        narrow_attachment_area = forward( self['usable_area_length'] / 2.0 ) (
            narrow_attachment_area
        )

        # add holes to the areas




        # create rounded corner
        corner = cube([
                self['height'] * 2.0,
                self['height'] * 2.0,
                self['height'],
            ],
        )

        corner = intersection() (
            corner,
            cylinder(
                self['height'] * 2,
                self['height'] * 2,
                segments=32,
            )
        )

        corner_position = [
            self['usable_area_width'] / 2.0,
            self['usable_area_length'] / 2.0,
            0,
        ]

        corner = translate(corner_position) (
            corner
        )

        features = [
            long_attachment_area,
            narrow_attachment_area,
            corner
        ]





        quarter_dimensions = [
            self['usable_area_width'] / 2.0,
            self['usable_area_length'] / 2.0,
            self['height']
        ]

        plate = cube(
            quarter_dimensions,
            center=False
        )

        return union() (
            plate,
            *features
        )

    def create_half_of_usable_area( self ):
        return union() (
            self.create_quarter_of_usable_area(),
            mirror([1,0,0]) (
                self.create_quarter_of_usable_area()
            )
        )

    def create_usable_area( self ):
        return union() (
            self.create_half_of_usable_area(),
            mirror([0,1,0]) (
                self.create_half_of_usable_area()
            )
        )

    def create_wide_wall( self ):


        wing_length = ( (self['usable_area_length'] / 2.0) - ( self['attachment_hole_padding'] * 2))

        wing = union() (
            cube([
                wing_length,
                self['height'],
                self['height']
            ]),
            translate([ wing_length / 2.0, self['height'], self['height'] / 2.0]) (
                rotate( 90, [0, 1, 0] ) (
                    cylinder( self['height'] / 2.0, wing_length, segments=32, center=True )
                )
            )
        )


        wing = translate( [ self['attachment_hole_padding'] * 0.5, 0, 0] ) (
            wing
        )

        wing = rotate(90, [0,0,1]) (
            wing
        )


        quarter_wall = union() (
            # the wall itself
            cube( [
                self['wall_height'] / 2.0,
                self['usable_area_length'] / 2.0,
                self['height']
            ]),
            # the wing
            wing

        )


        half_wall = union() (
            quarter_wall,
            mirror( [0, 1, 0] ) (
                quarter_wall
            )
        )

        wall = union() (

            left( self['wall_height']) (half_wall),

            mirror( [-1, 0, 0] ) (
                half_wall
            ),
        )

        return color('red') ( wall )

    def create(self):
        return union() (
            self.create_usable_area(),
            left( self['usable_area_width'] / 2.0 + 10.0 ) (
                self.create_wide_wall()
            )
        )

if __name__ == "__main__":
    t = Quarter(
        None,
        parameters={
            'height': 1.0,
            'usable_area_width': 30.0,
            'usable_area_length': 80.0,
            'attachment_area_width': 2.0,
            'attachment_hole_padding': 2.0,
            'wall_height': 5.0,
            'wing_markup': 0.5,
            'hole_markup': 0.1
        }
    )

    t.create()

    scad_render_to_file( t.put(), "project.scad" ) 
 
***********************************************/
                            
