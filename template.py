# -*- coding: utf-8 -*-

from core import *





if __name__ == "__main__":

    e = Element(
        Size(1,1,1),
        parameters={}
    )

    e.create()

    scad_render_to_file( e.put(), "project.scad" )