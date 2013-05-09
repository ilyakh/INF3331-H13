

translate(v = [0, 0, 0]) {
	difference() {
		union() {
			cylinder(h = 10.0000000000, r = 24.0000000000);
			cylinder(h = 1, r = 50, center = true);
		}
		cylinder(h = 20.0000000000, r = 20.0000000000, center = true);
	}
}
/***********************************************
******      SolidPython code:      *************
************************************************
 
from solid import *
from solid.utils import *
import doctest

from math import sqrt

from metrics import *
from units import *
from core import *




        
class Plate( Element ):
    def create_plate( self ):
        return cube( self.size() )

    def create( self ):
        return create_plate()

class PerforatedPlate( Plate ):
    def __init__( self, size, hole_radius=None ):
        Plate.__init__( self, size )
        self.hole_radius = hole_radius if hole_radius else 1.0

    def create_hole( self, radius=None, depth=None ):
        depth = depth if depth else self.size.z
        radius = self.hole_radius
        return cylinder( radius, depth)

    def create( self, position=None ):
        return difference() (
            # the solid part
            self.create_plate(),
            # the hole through the solid part
            # translated to the center of x/y-axes
            translate( [self.size.center('x'), self.size.center('y'), 0] ) (
                self.create_hole()
            )
        )


class PerforatedRoundedPlate( PerforatedPlate ):
    def __init__( self, size, hole_radius=None ):
        PerforatedPlate.__init__( self, size, hole_radius )
    
    def create_plate( self, reverse=False ):    
        depth =  self.size.z
        radius = self.size.center('y')
        
        result = difference() (
            cube( self.size() ),
            translate( [self.size.half('x'), 0, 0] ) (
                cube( [ self.size.x, self.size.y, self.size.z ] )
            )
        )
        
        return union() (
            result,
            translate( [self.size.half('x'), self.size.half('y'), 0] ) (
                cylinder( radius, depth )
            )
        )    


class PerforatedSection( Element ):
    def __init__( self, length=10, unit=20, hole_radius=5 ):
        # the length is calculated from the center of 
        # the center of the opposite hole
        self.length = length - unit # (lenght - 2 * (unit/2))
        self.unit = unit
        self.e1 = PerforatedRoundedPlate( Size( unit, unit, 1 ), hole_radius )
        self.e2 = PerforatedRoundedPlate( Size( unit, unit, 1 ), hole_radius )
        
    def create_bridge( self ):
        return translate([-self.length,0,0]) (
            cube([self.length, self.unit, 1])
        )
    
    def create( self, position=None ):        
        bridge = self.create_bridge()
    
        ends = union() (
            translate([-self.length,0,0]) (
                mirror([-1,0,0]) (self.e1.put())
            ),
            self.e2.put(),            
        )
        
        return union() (
            ends, 
            bridge
        )

    
class Grill(Element):
    def create_grill( self ):

        holes = []

        # parameterize
        width = 2
        step = width * 2

        for i in range( -1, self.size.x * 2, step ):
            holes.append(
                translate([i,-2,0]) (
                    rotate( 45 ) (
                        cube( [width, self.size.diagonal() * 2,self.size.z] )
                    )
                )
            )

        holes = union() (
            *holes
        )

        return holes

    def create( self ):
        return difference() (
            cube( self.size() ),
            self.create_grill()
        )


class Mesh( Grill ):
    def create( self ):
        grill_a = Grill( self.size )
        grill_b = Grill( self.size )

        grill_b = mirror([-1,0,0]) (
            grill_b.put([-self.size.x, 0, 0])
        )

        return union() (
            color("Blue") ( grill_a.put() ),
            color("Red") ( grill_b )
        )


class MeshRow(Element):
    def create( self ):
        pass


    
class HoleGrill(Grill):
    
    def create_hole( self, radius=1 ):
        return cylinder( radius, self.size.z )
    
    def find_holes( self, step=5 ):
        result = []
        odd = False
    
        x = self.size.x
        y = self.size.y
        z = self.size.z
        
        v = {}
    
        v['x'] = [i for i in range( 1, x, step )]
        v['y'] = [i for i in range( 1, y, step )]
        
        for d in range( -x, x+1, 2 ):
            odd = not odd
            for x, y in zip( v['x'], v['y'] ):
                if odd:
                    result.append( [x+d, y+step, 0] )
                else:
                    result.append( [x+d, y, 0] )
        
        return result
                
                
        
        
    def create( self ):
    
        g = cube( self.size() )
    
        holes = []
        
        for h in self.find_holes():
            h = translate(h) (
                self.create_hole()
            )        
            holes.append( h )

        holes = union() ( *holes )
        
        g = difference() (
            g,
            holes
        )   
        
        return g

        
        
class LineGrill( Grill ):
    pass


class MeshBox(Element):
    def create( self ):

        c = cube( [self.size.x, self.size.y, 1] )
        holes = []

        x_points = partition( self.size.x, 21 )[1:]
        y_points = partition( self.size.y, 3 )[1:]

        x_median = x_points[len(x_points) // 2]
        y_median = y_points[len(y_points) // 2]



        x_median_delta = x_median - self.size.half('x')
        y_median_delta = y_median - self.size.half('y')

        for i in x_points:
            for k in y_points:
                holes.append(
                    translate([i-x_median_delta, k-y_median_delta, 0]) (
                        cube( [1,1,1], center=True )
                    )
                )

        holes = union() ( *holes )

        return difference() (
            c,
            holes
        )


class Roller( Element ):
    def create( self ):

        wall_thickness = self.parameters['wall_thickness']
        wall_height = self.parameters['wall_height']
        hole_diameter = self.parameters['hole_diameter']

        circle = cylinder( self.size.x, self.size.z, center=True )
        hole = cylinder( hole_diameter, wall_height * 2, center=True )

        wall = cylinder( (wall_thickness * 2) + hole_diameter, wall_height )

        result = difference() (
            union() (
                wall,
                circle
            ),
            hole
        )

        return result


        
if __name__ == "__main__":

    e = MeshBox( Size(45, 5, 1) )
    e = Roller( Size( 50, 50, 1 ), parameters={
        'hole_diameter': 20.0,
        'wall_thickness': 2.0,
        'wall_height': 10.0
    })
    e.create()

    scad_render_to_file( e.put(), "project.scad" )
 
 
***********************************************/
                            
