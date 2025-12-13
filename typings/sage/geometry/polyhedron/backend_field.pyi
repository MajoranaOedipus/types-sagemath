from .base import Polyhedron_base as Polyhedron_base

class Polyhedron_field(Polyhedron_base):
    """
    Polyhedra over all fields supported by Sage.

    INPUT:

    - ``Vrep`` -- list ``[vertices, rays, lines]`` or ``None``

    - ``Hrep`` -- list ``[ieqs, eqns]`` or ``None``

    EXAMPLES::

        sage: p = Polyhedron(vertices=[(0,0),(AA(2).sqrt(),0),(0,AA(3).sqrt())],        # needs sage.rings.number_field
        ....:                rays=[(1,1)], lines=[], backend='field', base_ring=AA)
        sage: TestSuite(p).run()                                                        # needs sage.rings.number_field

    TESTS::

        sage: K.<sqrt3> = QuadraticField(3)                                             # needs sage.rings.number_field
        sage: p = Polyhedron([(0,0), (1,0), (1/2, sqrt3/2)])                            # needs sage.rings.number_field
        sage: TestSuite(p).run()                                                        # needs sage.rings.number_field

    Check that :issue:`19013` is fixed::

        sage: # needs sage.rings.number_field
        sage: x = polygen(ZZ, 'x')
        sage: K.<phi> = NumberField(x^2 - x - 1, embedding=1.618)
        sage: P1 = Polyhedron([[0,1], [1,1], [1,-phi+1]])
        sage: P2 = Polyhedron(ieqs=[[-1,-phi,0]])
        sage: P1.intersection(P2)
        The empty polyhedron
         in (Number Field in phi with defining polynomial x^2 - x - 1 with phi = 1.618033988749895?)^2

    Check that :issue:`28654` is fixed::

        sage: Polyhedron(lines=[[1]], backend='field')
        A 1-dimensional polyhedron in QQ^1 defined as the convex hull of 1 vertex and 1 line
    """
