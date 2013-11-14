# -*- coding: utf8 -*- 

from solid import *
from solid.utils import *

import colors, random, copy, numpy

from mixins import *
from metrics import *




class Element( object, Movable, Scalable ):
    """
    The overloaded representation of a solidpython node or a subtree.colors

    @param  body:           the solidpython node or a subtree

    @param  position:       the position of the element
    @type   position:       Position

    @param  parameters:     a dictionary of parameters that define the shape/
                            size and other properties of the Element
    @type   parameters:     dict

    """

    def __init__( self, *args, **kwargs ):
        """
        Creates an element. The kwargs variable contains the parameters.

        @param  kwargs:     keyword arguments are the parameters of element
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
        """
        @rtype:     int
        @return:    number of parameters this Element has.
        """
        return len( self.parameters )

    def __getitem__( self, keyword ):
        """
        @type       keyword: string
        @param      keyword: the name of the parameter to find

        @return:    the value of the parameter indexed by 'keyword'
        """

        if keyword == "position":
            return self.position.to_list()
        elif keyword in self.position.get_keywords():
            return self.position.get( keyword )

        if self.parameters.get( keyword ):
            return self.parameters.__getitem__( keyword )
        else:
            return None

    def __setitem__ ( self, keyword, value ):
        """
        Changes the value of a parameter marked by keyword.

        @type       keyword:    string
        @param      keyword:    index of the parameter

        @param      value:      value of the parameter marked by keyword

        """

        if keyword in self.position.get_keywords():
            return self.position.set( keyword, value )

        if value is int:
            value = float(value)

        self.parameters.__setitem__( keyword, value )

    def __mul__( self, factor ):
        """
        Scales the element, either up or down.
        
        @type   factor:     int or float
        @param  factor:     a number > 1.0 to scale up, or number < 1.0 to scale
                            down.

        @rtype:     Element
        @return:    self
        """
        if isinstance( factor, float ) or isinstance( factor, int ):
            self.scale( [factor, factor, factor] )

        return self


    def join( self, *args ):
        """
        Union operation. Makes the element or elements in the 'args' a part of
        this Element's body.

        @type   args:      Element
        @param  args:      another element, or multiple elements to include into
                           the body.

        @rtype:     Element
        @return:    self, including solid volume of the other
        """
        if len(args):
            for other in args:
                self.body = union() ( self.body, other.body )

        return self

    def carve( self, *args ):
        """
        Difference operation. Removes a part of self, corresponding to all
        elements in args.colors


        @param      args:     another element, or multiple elements to exclude
                              from the volume of the body.
        @type       args:     Element

        @return:    self
        @rtype:     ELement
        """
        if len(args):
            for other in args:
                self.body = difference() ( self.body, other.body )

        return self

    def intersect( self, other ):
        """
        Intersection operation. Removes all solid volume that is not part of
        either body of self, or the body of other (keeps only the common volume
        present in both self and other).

        @type       other:    Element
        @param      args:     another element, or multiple elements to find
                              common are with.
        """

        self.body = intersection() ( self.body, other.body )
        return self

    def color( self, color_name=None ):
        """
        Uses an SVG compatible color name to paint the element.
        For possible color names see: U{SVG color name list<>}.
        Selects a random color if no color_name is provided.

        @param      color_name:     either a color name from SVG color namespace
                                    or empty;
        @type       color_name:     string

        @return:    self
        @rtype:     Element
        """

        if not color_name:
            color_name = random.choice( colors.NAMES )

        self.body = color( color_name ) ( self.body )
        return self

    def copy( self, new_position=None ):
        """
        Creates a deep copy of this element. The parameters of the new element
        can be changed without affecting the original element.

        @param      vector:     the coordinates that specify the location to
                                which the copy of the element will be moved.
        @type       vector:     3-list

        @return:        copy of self
        @rtype:         Element
        """

        element = copy.deepcopy( self )
        if new_position:
            element.translate( new_position )
        element.color()
        return element

    def spawn( self, vector ):
        """
        This method duplicates this Element, by creating an exact copy side by
        side.

        @param      vector:     the vector perpendicular to the direction of
                                replication
        @type       vector:     3-list


        @return:    duplicated element
        @rtype:     Element
        """
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
        """
        Revolves itself around x-axis.

        @param      degrees: the number of degrees to rotate
        @type:      int or float

        @return:    rotated self
        @rtype:     Element
        """
        self.rotate( degrees, 'x' )
        return self

    def pitch( self, degrees ):
        """
        Revolves itself around y-axis.

        @param      degrees: the number of degrees to rotate
        @type:      float

        @return:    rotated self
        @rtype:     Element
        """
        self.rotate( degrees, 'y' )
        return self

    def yaw( self, degrees ):
        """
        Revolves itself around z-axis.

        @param      degrees: the number of degrees to rotate
        @type:      float

        @return:    rotated self
        @rtype:     Element
        """
        self.rotate( degrees, 'z' )
        return self


    def mirror( self, vector ):
        """
        Mirrors around a specified vector.

        @param      vector:     the vector of rotation
        @type       vector:     3-list or axis (x, y or z)

        @return:    rotated self
        @rtype:     Element

        """

        if not isinstance( vector, list ):
            vector = AXES.get( vector )

        current_position = self.position.get()
        origin = [ -1*i for i in self.position.get() ]

        self.body = translate( origin ) ( self.body )
        self.body = mirror( vector ) ( self.body )
        self.body = translate( current_position ) ( self.body )

        return self

    def rotate( self, degrees, vector ):
        """
        Rotates the element around a vector.
        @attention: The vector is computed from the original position of
        this element.

        @param  vector:     the vector to rotate around,
        @type   vector:     3-list or character

        @return:    rotated self
        @rtype:     Element

        """
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
        """
        Rotates the element around a vector starting from a global origin.

        @attention: The vector origin is the global origin. This method
        corresponds to the original behavior

        @param  vector:     the vector to rotate around, or an axis
        @type   vector:     3-list or character

        @return:    rotated self
        @rtype:     Element
        """

        if not isinstance( vector, list ):
            vector = AXES.get( vector )

        self.body = rotate( degrees, vector ) ( self.body )

        return self

    def __extend__( self ):
        pass


    def save( self, path=None ):
        """
        Compiles the body of this Element into a .scad file.
        If the path is omitted, the path will default to a string containing
        the current timestamp in format:

        YEAR-MONTH-DAY-HOUR-MINUTE-SECOND.scad

        The default timestamps are of second resolution, so two saves made
        during the same second of time will only yield the most recent one.

        @param  path:       path incl. filename to compile the .scad code to.
                            must be a valid and writable location in the
                            filesystem.
        @type   path:       string
        """

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