# -*- coding: utf-8 -*- 

from core import *


class Inlay( Element ):

    def get_base_height(self):
        return self.p.get( 'bottom-height' ) / 2.0

    def create_top(self):
        height = self.p.get( 'bottom-height' ) + self.p.get( 'separator-height' )


        return up( height ) (
                difference() (
                cube(
                    [ self.p.get('top-width'),
                      self.p.get('top-length'),
                      self.p.get('top-height') ], center=True ),
                self.create_bottom()
            )
        )

    def create_separator( self ):
        height =  self.p.get('bottom-height')

        return up( height ) (
            cube(
                [ self.p.get('top-width'),
                  self.p.get('top-length'),
                  self.p.get('serparator-height') ], center=True )
        )

    def create_bottom( self ):
        height = self.get_base_height()

        return up( height ) ( cube(
                [ self.p.get('bottom-width'), self.p.get('bottom-length'), self.p.get('bottom-height') ],
                center=True
            )
        )

    def create( self ):
        top = self.create_top()
        bottom = self.create_bottom()
        separator = self.create_separator()

        return union() (
            top,
            separator,
            bottom
        )




if __name__ == "__main__":

    e = Inlay(
        Size(1,1,1),
        parameters = {
            'top-height': 5.0,
            'top-width': 30.0,
            'top-length': 20.0,
            'separator-height': 1.0,
            'bottom-height': 5.0,
            'bottom-width': 26.0,
            'bottom-length': 14.0
        }
    )

    scad_render_to_file( e.put(), "project.scad" )