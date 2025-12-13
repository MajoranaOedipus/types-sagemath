from .backend_field import Polyhedron_field as Polyhedron_field
from .base_number_field import Polyhedron_base_number_field as Polyhedron_base_number_field

class Polyhedron_number_field(Polyhedron_field, Polyhedron_base_number_field):
    """
    Polyhedra whose data can be converted to number field elements.

    All computations are done internally using a fixed real embedded number field,
    which is determined automatically.

    INPUT:

    - ``Vrep`` -- list ``[vertices, rays, lines]`` or ``None``

    - ``Hrep`` -- list ``[ieqs, eqns]`` or ``None``

    EXAMPLES::

        sage: P = Polyhedron(vertices=[[1], [sqrt(2)]], backend='number_field'); P      # needs sage.rings.number_field sage.symbolic
        A 1-dimensional polyhedron
         in (Symbolic Ring)^1 defined as the convex hull of 2 vertices
        sage: P.vertices()                                                              # needs sage.rings.number_field sage.symbolic
        (A vertex at (1), A vertex at (sqrt(2)))

        sage: P = polytopes.icosahedron(exact=True, backend='number_field')             # needs sage.rings.number_field
        sage: P                                                                         # needs sage.rings.number_field
        A 3-dimensional polyhedron
         in (Number Field in sqrt5 with defining polynomial x^2 - 5
             with sqrt5 = 2.236067977499790?)^3
         defined as the convex hull of 12 vertices

        sage: x = polygen(ZZ); P = Polyhedron(                                          # needs sage.rings.number_field sage.symbolic
        ....:     vertices=[[sqrt(2)], [AA.polynomial_root(x^3-2, RIF(0,3))]],
        ....:     backend='number_field')
        sage: P                                                                         # needs sage.rings.number_field sage.symbolic
        A 1-dimensional polyhedron
         in (Symbolic Ring)^1 defined as the convex hull of 2 vertices
        sage: P.vertices()                                                              # needs sage.rings.number_field sage.symbolic
        (A vertex at (sqrt(2)), A vertex at (2^(1/3)))

    TESTS:

    Tests from :class:`~sage.geometry.polyhedron.backend_field.Polyhedron_field` --
    here the data are already either in a number field or in ``AA``::

        sage: p = Polyhedron(vertices=[(0,0),(AA(2).sqrt(),0),(0,AA(3).sqrt())],        # needs sage.rings.number_field
        ....:                rays=[(1,1)], lines=[], backend='number_field',
        ....:                base_ring=AA)
        sage: TestSuite(p).run()                                                        # needs sage.rings.number_field

        sage: K.<sqrt3> = QuadraticField(3)                                             # needs sage.rings.number_field
        sage: p = Polyhedron([(0,0), (1,0), (1/2, sqrt3/2)], backend='number_field')    # needs sage.rings.number_field
        sage: TestSuite(p).run()                                                        # needs sage.rings.number_field

        sage: # needs sage.rings.number_field
        sage: x = polygen(ZZ, 'x')
        sage: K.<phi> = NumberField(x^2 - x - 1, embedding=1.618)
        sage: P1 = Polyhedron([[0,1], [1,1], [1,-phi+1]], backend='number_field')
        sage: P2 = Polyhedron(ieqs=[[-1,-phi,0]], backend='number_field')
        sage: P1.intersection(P2)
        The empty polyhedron
         in (Number Field in phi with defining polynomial x^2 - x - 1
             with phi = 1.618033988749895?)^2

        sage: Polyhedron(lines=[[1]], backend='number_field')
        A 1-dimensional polyhedron in QQ^1 defined as the convex hull of 1 vertex and 1 line
    """
