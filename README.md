

    c = a.copy([-10, 8,  0 ])
    d = a.copy([10, -8,  0 ])
    e = a.copy([-10, -8, 0 ])
    f = a.copy([10, 8, 0])


        # create the rounded corner
        a = Cuboid( 10, 10, 1 )
        b = Cuboid( 5, 5, 1 ).left(2.5).forward(2.5)
        c = Cylinder( 1, 5, 5 )
        a.carve( b )
        a.join( c )

        # create two corners side-by-side
        a = Union(
            a.copy([15,20,0]),
            a.rotate(90, 'z').copy([-15,20,0]),
            a.rotate(90, 'z').copy([-15,-20,0]),
            a.rotate(90, 'z').copy([15,-20,0])
        )



    # create the rounded corner
    a = Cuboid( 10, 10, 1 )
    b = Cuboid( 5, 5, 1 ).left(2.5).forward(2.5)
    d = Cylinder( 1, 2.5, 2.5 ).left(1.25).forward(1.25)
    c = Cylinder( 1, 5, 5 )
    a.carve( b )
    a.join( c )
    # create a hole
    a.carve( d )


    a = Union(
        a.copy([15,20,0]),
        a.copy([15,-20,0]).rotate( 270, 'z'),
        a.copy([-15,20,0]).rotate( 90, 'z'),
        a.copy([-15,-20,0]).rotate( -180, 'z'),

        Cuboid( 40, 30, 1 ),
        Cuboid( 20, 50, 1 )
    )

    m = a.copy().up( 10 )

    a.join( m )

    a.carve(
        Cuboid( 1, 30, 15 ).left( 15 ),
        Cuboid( 1, 30, 15 ).right( 15 ),
        Cuboid( 20, 1, 15 ).forward( 20 ),
        Cuboid( 20, 1, 15 ).back( 20 ),
    )