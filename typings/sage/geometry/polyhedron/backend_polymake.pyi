from .base import Polyhedron_base as Polyhedron_base
from .base_QQ import Polyhedron_QQ as Polyhedron_QQ
from .base_ZZ import Polyhedron_ZZ as Polyhedron_ZZ
from sage.structure.element import Element as Element

class Polyhedron_polymake(Polyhedron_base):
    """
    Polyhedra with polymake.

    INPUT:

    - ``parent`` -- :class:`~sage.geometry.polyhedron.parent.Polyhedra`
      the parent

    - ``Vrep`` -- list ``[vertices, rays, lines]`` or ``None``; the
      V-representation of the polyhedron. If ``None``, the polyhedron
      is determined by the H-representation.

    - ``Hrep`` -- list ``[ieqs, eqns]`` or ``None``; the
      H-representation of the polyhedron. If ``None``, the polyhedron
      is determined by the V-representation.

    - ``polymake_polytope`` -- a polymake polytope object

    Only one of ``Vrep``, ``Hrep``, or ``polymake_polytope`` can be different
    from ``None``.

    EXAMPLES::

        sage: p = Polyhedron(vertices=[(0,0),(1,0),(0,1)], rays=[(1,1)],   # optional - jupymake
        ....:                lines=[], backend='polymake')
        sage: TestSuite(p).run()                                           # optional - jupymake

    A lower-dimensional affine cone; we test that there are no mysterious
    inequalities coming in from the homogenization::

        sage: P = Polyhedron(vertices=[(1, 1)], rays=[(0, 1)],             # optional - jupymake
        ....:                backend='polymake')
        sage: P.n_inequalities()                                           # optional - jupymake
        1
        sage: P.equations()                                                # optional - jupymake
        (An equation (1, 0) x - 1 == 0,)

    The empty polyhedron::

        sage: Polyhedron(eqns=[[1, 0, 0]], backend='polymake')             # optional - jupymake
        The empty polyhedron in QQ^2

    It can also be obtained differently::

        sage: # optional - jupymake
        sage: P=Polyhedron(ieqs=[[-2, 1, 1], [-3, -1, -1], [-4, 1, -2]],
        ....:              backend='polymake')
        sage: P
        The empty polyhedron in QQ^2
        sage: P.Vrepresentation()
        ()
        sage: P.Hrepresentation()
        (An equation -1 == 0,)

    The full polyhedron::

        sage: Polyhedron(eqns=[[0, 0, 0]], backend='polymake')             # optional - jupymake
        A 2-dimensional polyhedron in QQ^2 defined as the convex hull of 1 vertex and 2 lines
        sage: Polyhedron(ieqs=[[0, 0, 0]], backend='polymake')             # optional - jupymake
        A 2-dimensional polyhedron in QQ^2 defined as the convex hull of 1 vertex and 2 lines


    Quadratic fields work::

        sage: V = polytopes.dodecahedron().vertices_list()                              # needs sage.groups sage.rings.number_field
        sage: Polyhedron(vertices=V, backend='polymake')        # optional - jupymake, needs sage.groups sage.rings.number_field
        A 3-dimensional polyhedron
         in (Number Field in sqrt5 with defining polynomial x^2 - 5
             with sqrt5 = 2.236067977499790?)^3
         defined as the convex hull of 20 vertices

    TESTS:

    Tests copied from various methods in :mod:`sage.geometry.polyhedron.base`::

        sage: p = Polyhedron(vertices = [[1,0,0], [0,1,0], [0,0,1]],       # optional - jupymake
        ....:                backend='polymake')
        sage: p.n_equations()                                              # optional - jupymake
        1
        sage: p.n_inequalities()                                           # optional - jupymake
        3

        sage: p = Polyhedron(vertices = [[t,t^2,t^3] for t in range(6)],   # optional - jupymake
        ....:                backend='polymake')
        sage: p.n_facets()                                                 # optional - jupymake
        8

        sage: p = Polyhedron(vertices = [[1,0],[0,1],[1,1]], rays=[[1,1]], # optional - jupymake
        ....:                backend='polymake')
        sage: p.n_vertices()                                               # optional - jupymake
        2

        sage: p = Polyhedron(vertices = [[1,0],[0,1]], rays=[[1,1]],       # optional - jupymake
        ....:                backend='polymake')
        sage: p.n_rays()                                                   # optional - jupymake
        1

        sage: p = Polyhedron(vertices = [[0,0]], rays=[[0,1],[0,-1]],      # optional - jupymake
        ....:                backend='polymake')
        sage: p.n_lines()                                                  # optional - jupymake
        1
    """
    def __init__(self, parent, Vrep, Hrep, polymake_polytope=None, **kwds) -> None:
        """
        Initialize the polyhedron.

        See :class:`Polyhedron_polymake` for a description of the input
        data.

        TESTS:

            sage: # optional - jupymake
            sage: p = Polyhedron(backend='polymake')
            sage: TestSuite(p).run()
            sage: p = Polyhedron(vertices=[(1, 1)], rays=[(0, 1)],
            ....:                backend='polymake')
            sage: TestSuite(p).run()

        We skip the Lawrence test because it involves numerically unstable
        floating point arithmetic::

            sage: p = Polyhedron(vertices=[(-1,-1), (1,0), (1,1), (0,1)],  # optional - jupymake
            ....:                backend='polymake')
            sage: TestSuite(p).run(skip='_test_lawrence')            # optional - jupymake

        ::

            sage: # optional - jupymake
            sage: p = Polyhedron(rays=[[1,1]], backend='polymake')
            sage: TestSuite(p).run()
            sage: p = Polyhedron(rays=[[1]], backend='polymake')
            sage: TestSuite(p).run()
            sage: p = Polyhedron(rays=[[1,1,1]], lines=[[1,0,0]], backend='polymake')
            sage: TestSuite(p).run()
            sage: p = Polyhedron(vertices=[[]], backend='polymake')
            sage: TestSuite(p).run()
        """

class Polyhedron_QQ_polymake(Polyhedron_polymake, Polyhedron_QQ):
    """
    Polyhedra over `\\QQ` with polymake.

    INPUT:

    - ``Vrep`` -- list ``[vertices, rays, lines]`` or ``None``
    - ``Hrep`` -- list ``[ieqs, eqns]`` or ``None``

    EXAMPLES::

        sage: p = Polyhedron(vertices=[(0,0),(1,0),(0,1)],                 # optional - jupymake
        ....:                rays=[(1,1)], lines=[],
        ....:                backend='polymake', base_ring=QQ)
        sage: TestSuite(p).run()                                           # optional - jupymake
    """
class Polyhedron_ZZ_polymake(Polyhedron_polymake, Polyhedron_ZZ):
    """
    Polyhedra over `\\ZZ` with polymake.

    INPUT:

    - ``Vrep`` -- list ``[vertices, rays, lines]`` or ``None``
    - ``Hrep`` -- list ``[ieqs, eqns]`` or ``None``

    EXAMPLES::

        sage: p = Polyhedron(vertices=[(0,0),(1,0),(0,1)],                 # optional - jupymake
        ....:                rays=[(1,1)], lines=[],
        ....:                backend='polymake', base_ring=ZZ)
        sage: TestSuite(p).run()                                           # optional - jupymake
    """
