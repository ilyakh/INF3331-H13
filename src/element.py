# -*- coding: utf8 -*- 

from solid import *
from solid.utils import *

import colors, random, copy

from mixins import *
from metrics import *




class Element( object, Movable ):

    def __init__( self, *args, **kwargs ):
        """
        @param  kwargs      keyword arguments are the parameters of element
                            they are maintained in a special instance called
                            Spec (specification)
        """
        self.parameters = {}
        for k, v in kwargs.iteritems():
            self[k] = v

        self.body = None
        self.position = Position()
        self.__extend__()

    def __len__( self ):
        return len( self.parameters )

    def __getitem__( self, keyword ):

        if keyword == "position":
            return self.position.to_list()
        elif keyword in self.position.get_keywords():
            return self.position.get( keyword )

        if self.parameters.get( keyword ):
            return self.parameters.__getitem__( keyword )
        else:
            return None

    def __setitem__ ( self, keyword, value ):

        if keyword in self.position.get_keywords():
            return self.position.set( keyword, value )

        if value is int:
            value = float(value)

        self.parameters.__setitem__( keyword, value )

    def __mul__( self, other ):
        if isinstance( other, float ):
            self.scale( [other, other, other] )

        return self

    def join( self, *args ):
        if len(args):
            for other in args:
                self.body = union() ( self.body, other.body )

        return self

    def carve( self, *args ):
        if len(args):
            for other in args:
                self.body = difference() ( self.body, other.body )

        return self

    def intersect( self, other ):
        self.body = intersection() ( self.body, other.body )
        return self

    def color( self, color_name=None ):
        if not color_name:
            color_name = random.choice( colors.NAMES )

        self.body = color( color_name ) ( self.body )
        return self

    def copy( self, vector=None ):
        element = copy.deepcopy( self )
        if vector:
            element.translate( vector )
        element.color()
        return element

    def spawn( self, vector ):
        if not isinstance( vector, list ):
            modifier = [1, 1, 1]
            if vector in ['x', '-x']:
                modifier = [ self['width'], 0, 0]
            elif vector in ['y', '-y']:
                modifier = [ 0, self['length'], 0]
            elif vector in ['z', '-z']:
                modifier = [ 0, 0, self['height'] ]

            axis_vector = AXES.get( vector )
            vector = [ i*j for i,j in zip( axis_vector, modifier ) ]


        self.body = union() (
            self.body,
            translate( vector ) (
                mirror( vector ) ( self.body.copy() )
            )
        )

        return self


    def roll( self, degrees ):
        self.rotate( degrees, 'x' )
        return self

    def pitch( self, degrees ):
        self.rotate( degrees, 'y' )
        return self

    def yaw( self, degrees ):
        self.rotate( degrees, 'z' )
        return self


    def mirror( self, vector ):
        if not isinstance( vector, list ):
            vector = AXES.get( vector )

        current_position = self.position.get()
        origin = [ -1*i for i in self.position.get() ]

        self.body = translate( origin ) ( self.body )
        self.body = mirror( vector ) ( self.body )
        self.body = translate( current_position ) ( self.body )

        return self

    def rotate( self, degrees, vector ):
        if not isinstance( vector, list ):
            vector = AXES.get( vector )

        current_position = self.position.get()
        # reverse the position vector to get the movement vector
        # towards the origin
        origin = [ -1*i for i in self.position.get() ]

        self.body = translate( origin ) ( self.body )
        self.body = rotate( degrees, vector ) ( self.body )
        self.body = translate( current_position ) ( self.body )

        return self

    def global_rotate( self, degrees, vector ):
        if not isinstance( vector, list ):
            vector = AXES.get( vector )

        self.body = rotate( degrees, vector ) ( self.body )

        return self

    def __extend__( self ):
        pass


    def save( self, path=None ):
        if not path:
            import datetime
            now = datetime.datetime.now()

            name = "{0}-{1}-{2}-{3}-{4}-{5}".format( *now.timetuple() )

            path = ".".join( [name, 'scad'] )

        scad_render_to_file( self.body, path, include_orig_code=False )
        return self






if __name__ == "__main__":
    import doctest
    doctest.testmod()