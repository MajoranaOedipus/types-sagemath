import sage.structure.sage_object
from sage.cpython.string import bytes_to_str as bytes_to_str, str_to_bytes as str_to_bytes
from sage.geometry.cone import ConvexRationalPolyhedralCone as ConvexRationalPolyhedralCone
from sage.geometry.lattice_polytope import LatticePolytopeClass as LatticePolytopeClass
from sage.geometry.polyhedron.base import Polyhedron_base as Polyhedron_base
from sage.geometry.polyhedron.combinatorial_polyhedron.conversions import facets_tuple_to_bit_rep_of_Vrep as facets_tuple_to_bit_rep_of_Vrep, facets_tuple_to_bit_rep_of_facets as facets_tuple_to_bit_rep_of_facets, incidence_matrix_to_bit_rep_of_Vrep as incidence_matrix_to_bit_rep_of_Vrep, incidence_matrix_to_bit_rep_of_facets as incidence_matrix_to_bit_rep_of_facets
from sage.graphs.graph import Graph as Graph
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.misc import is_iterator as is_iterator
from sage.structure.element import Matrix as Matrix, have_same_parent as have_same_parent, parent as parent
from typing import Any, ClassVar, overload

class CombinatorialPolyhedron(sage.structure.sage_object.SageObject):
    """CombinatorialPolyhedron(data, Vrep=None, facets=None, unbounded=False, far_face=None)

    File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 114)

    The class of the Combinatorial Type of a Polyhedron, a Polytope.

    INPUT:

    - ``data`` -- an instance of
       * :class:`~sage.geometry.polyhedron.parent.Polyhedron_base`
       * or a :class:`~sage.geometry.lattice_polytope.LatticePolytopeClass`
       * or a :class:`~sage.geometry.cone.ConvexRationalPolyhedralCone`
       * or an ``incidence_matrix`` as in
         :meth:`~sage.geometry.polyhedron.base.Polyhedron_base.incidence_matrix`
         In this case you should also specify the ``Vrep`` and ``facets`` arguments
       * or list of facets, each facet given as
         a list of ``[vertices, rays, lines]`` if the polyhedron is unbounded,
         then rays and lines and the extra argument ``nr_lines`` are required
         if the polyhedron contains no lines, the rays can be thought of
         as the vertices of the facets deleted from a bounded polyhedron see
         :class:`~sage.geometry.polyhedron.parent.Polyhedron_base` on how to use
         rays and lines
       * or an integer, representing the dimension of a polyhedron equal to its
         affine hull
       * or a tuple consisting of facets and vertices as two
         :class:`~sage.geometry.polyhedron.combinatorial_polyhedron.list_of_faces.ListOfFaces`.
    - ``Vrep`` -- (optional) when ``data`` is an incidence matrix, it should
      be the list of ``[vertices, rays, lines]``, if the rows in the incidence_matrix
      should correspond to names
    - ``facets`` -- (optional) when ``data`` is an incidence matrix or a list of facets,
      it should be a list of facets that would be used instead of indices (of the columns
      of the incidence matrix).
    - ``unbounded`` -- value will be overwritten if ``data`` is a polyhedron;
      if ``unbounded`` and ``data`` is incidence matrix or a list of facets,
      need to specify ``far_face``
    - ``far_face`` -- (semi-optional); if the polyhedron is unbounded this
      needs to be set to the list of indices of the rays and line unless ``data`` is
      an instance of :class:`~sage.geometry.polyhedron.parent.Polyhedron_base`.

    EXAMPLES:

    We illustrate all possible input: a polyhedron:

        sage: P = polytopes.cube()
        sage: CombinatorialPolyhedron(P)
        A 3-dimensional combinatorial polyhedron with 6 facets

    a lattice polytope::

        sage: points = [(1,0,0), (0,1,0), (0,0,1),
        ....: (-1,0,0), (0,-1,0), (0,0,-1)]
        sage: L = LatticePolytope(points)
        sage: CombinatorialPolyhedron(L)
        A 3-dimensional combinatorial polyhedron with 8 facets

    a cone::

        sage: M = Cone([(1,0), (0,1)])
        sage: CombinatorialPolyhedron(M)
        A 2-dimensional combinatorial polyhedron with 2 facets

    an incidence matrix::

        sage: P = Polyhedron(rays=[[0,1]])
        sage: data = P.incidence_matrix()
        sage: far_face = [i for i in range(2) if not P.Vrepresentation()[i].is_vertex()]
        sage: CombinatorialPolyhedron(data, unbounded=True, far_face=far_face)
        A 1-dimensional combinatorial polyhedron with 1 facet
        sage: C = CombinatorialPolyhedron(data, Vrep=['myvertex'],
        ....: facets=['myfacet'], unbounded=True, far_face=far_face)
        sage: C.Vrepresentation()
        ('myvertex',)
        sage: C.Hrepresentation()
        ('myfacet',)

    a list of facets::

        sage: CombinatorialPolyhedron(((1,2,3),(1,2,4),(1,3,4),(2,3,4)))
        A 3-dimensional combinatorial polyhedron with 4 facets
        sage: facetnames = ['facet0', 'facet1', 'facet2', 'myfacet3']
        sage: facetinc = ((1,2,3),(1,2,4),(1,3,4),(2,3,4))
        sage: C = CombinatorialPolyhedron(facetinc, facets=facetnames)
        sage: C.Vrepresentation()
        (1, 2, 3, 4)
        sage: C.Hrepresentation()
        ('facet0', 'facet1', 'facet2', 'myfacet3')

    an integer::

        sage: CombinatorialPolyhedron(-1).f_vector()
        (1)
        sage: CombinatorialPolyhedron(0).f_vector()
        (1, 1)
        sage: CombinatorialPolyhedron(5).f_vector()
        (1, 0, 0, 0, 0, 0, 1)

    tuple of ``ListOfFaces``::

        sage: from sage.geometry.polyhedron.combinatorial_polyhedron.conversions \\\n        ....:     import facets_tuple_to_bit_rep_of_facets, \\\n        ....:            facets_tuple_to_bit_rep_of_Vrep
        sage: bi_pyr = ((0,1,4), (1,2,4), (2,3,4), (3,0,4),
        ....:           (0,1,5), (1,2,5), (2,3,5), (3,0,5))
        sage: facets = facets_tuple_to_bit_rep_of_facets(bi_pyr, 6)
        sage: Vrep = facets_tuple_to_bit_rep_of_Vrep(bi_pyr, 6)
        sage: C = CombinatorialPolyhedron((facets, Vrep)); C
        A 3-dimensional combinatorial polyhedron with 8 facets
        sage: C.f_vector()
        (1, 6, 12, 8, 1)

    Specifying that a polyhedron is unbounded is important. The following with a
    polyhedron works fine::

        sage: P = Polyhedron(ieqs=[[1,-1,0],[1,1,0]])
        sage: C = CombinatorialPolyhedron(P)  # this works fine
        sage: C
        A 2-dimensional combinatorial polyhedron with 2 facets

    The following is incorrect, as ``unbounded`` is implicitly set to ``False``::

        sage: data = P.incidence_matrix()
        sage: vert = P.Vrepresentation()
        sage: C = CombinatorialPolyhedron(data, Vrep=vert)
        sage: C
        A 2-dimensional combinatorial polyhedron with 2 facets
        sage: C.f_vector()
        Traceback (most recent call last):
        ...
        ValueError: not all vertices are intersections of facets
        sage: C.vertices()
        (A line in the direction (0, 1), A vertex at (1, 0), A vertex at (-1, 0))

    The correct usage is::

        sage: far_face = [i for i in range(3) if not P.Vrepresentation()[i].is_vertex()]
        sage: C = CombinatorialPolyhedron(data, Vrep=vert, unbounded=True, far_face=far_face)
        sage: C
        A 2-dimensional combinatorial polyhedron with 2 facets
        sage: C.f_vector()
        (1, 0, 2, 1)
        sage: C.vertices()
        ()

    TESTS:

    Checking that :issue:`27987` is fixed::

        sage: P1 = Polyhedron(vertices=[[0,1],[1,0]], rays=[[1,1]])
        sage: P2 = Polyhedron(vertices=[[0,1],[1,0],[1,1]])
        sage: P1.incidence_matrix() == P2.incidence_matrix()
        True
        sage: CombinatorialPolyhedron(P1).f_vector()
        (1, 2, 3, 1)
        sage: CombinatorialPolyhedron(P2).f_vector()
        (1, 3, 3, 1)
        sage: P1 = Polyhedron(vertices=[[0,1],[1,0]], rays=[[1,1]])
        sage: P2 = Polyhedron(vertices=[[0,1],[1,0],[1,1]])
        sage: CombinatorialPolyhedron(P1).f_vector()
        (1, 2, 3, 1)
        sage: CombinatorialPolyhedron(P2).f_vector()
        (1, 3, 3, 1)

    Some other tests regarding small polyhedra::

        sage: P = Polyhedron(rays=[[1,0],[0,1]])
        sage: C = CombinatorialPolyhedron(P)
        sage: C
        A 2-dimensional combinatorial polyhedron with 2 facets
        sage: C.f_vector()
        (1, 1, 2, 1)
        sage: C.vertices()
        (A vertex at (0, 0),)
        sage: data = P.incidence_matrix()
        sage: vert = P.Vrepresentation()
        sage: far_face = [i for i in range(3) if not P.Vrepresentation()[i].is_vertex()]
        sage: C = CombinatorialPolyhedron(data, Vrep=vert, unbounded=True, far_face=far_face)
        sage: C
        A 2-dimensional combinatorial polyhedron with 2 facets
        sage: C.f_vector()
        (1, 1, 2, 1)
        sage: C.vertices()
        (A vertex at (0, 0),)
        sage: CombinatorialPolyhedron(3r)
        A 3-dimensional combinatorial polyhedron with 0 facets

    Check that on wrong input subsequent calls of ``f_vector`` fail::

        sage: data = P.incidence_matrix()
        sage: vert = P.Vrepresentation()
        sage: C = CombinatorialPolyhedron(data, Vrep=vert)
        sage: C.f_vector()
        Traceback (most recent call last):
        ...
        ValueError: not all vertices are intersections of facets
        sage: C.f_vector()
        Traceback (most recent call last):
        ...
        ValueError: not all vertices are intersections of facets

    Check that :issue:`28678` is fixed::

        sage: CombinatorialPolyhedron([])
        A -1-dimensional combinatorial polyhedron with 0 facets
        sage: CombinatorialPolyhedron(LatticePolytope([], lattice=ToricLattice(3)))
        A -1-dimensional combinatorial polyhedron with 0 facets"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @overload
    def __init__(self, data, Vrep=..., facets=..., unbounded=..., far_face=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 348)

                Initialize :class:`CombinatorialPolyhedron`.

                See :class:`CombinatorialPolyhedron`.

                TESTS::

                    sage: C = CombinatorialPolyhedron([[0,1,2], [0,1,3],   # indirect doctest
                    ....:                              [0,2,3], [1,2,3]])

                    sage: TestSuite(sage.geometry.polyhedron.combinatorial_polyhedron.base.CombinatorialPolyhedron).run()
        """
    @overload
    def __init__(self, P) -> Any:
        """File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 348)

                Initialize :class:`CombinatorialPolyhedron`.

                See :class:`CombinatorialPolyhedron`.

                TESTS::

                    sage: C = CombinatorialPolyhedron([[0,1,2], [0,1,3],   # indirect doctest
                    ....:                              [0,2,3], [1,2,3]])

                    sage: TestSuite(sage.geometry.polyhedron.combinatorial_polyhedron.base.CombinatorialPolyhedron).run()
        """
    @overload
    def __init__(self, L) -> Any:
        """File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 348)

                Initialize :class:`CombinatorialPolyhedron`.

                See :class:`CombinatorialPolyhedron`.

                TESTS::

                    sage: C = CombinatorialPolyhedron([[0,1,2], [0,1,3],   # indirect doctest
                    ....:                              [0,2,3], [1,2,3]])

                    sage: TestSuite(sage.geometry.polyhedron.combinatorial_polyhedron.base.CombinatorialPolyhedron).run()
        """
    @overload
    def __init__(self, M) -> Any:
        """File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 348)

                Initialize :class:`CombinatorialPolyhedron`.

                See :class:`CombinatorialPolyhedron`.

                TESTS::

                    sage: C = CombinatorialPolyhedron([[0,1,2], [0,1,3],   # indirect doctest
                    ....:                              [0,2,3], [1,2,3]])

                    sage: TestSuite(sage.geometry.polyhedron.combinatorial_polyhedron.base.CombinatorialPolyhedron).run()
        """
    @overload
    def __init__(self, data, unbounded=..., far_face=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 348)

                Initialize :class:`CombinatorialPolyhedron`.

                See :class:`CombinatorialPolyhedron`.

                TESTS::

                    sage: C = CombinatorialPolyhedron([[0,1,2], [0,1,3],   # indirect doctest
                    ....:                              [0,2,3], [1,2,3]])

                    sage: TestSuite(sage.geometry.polyhedron.combinatorial_polyhedron.base.CombinatorialPolyhedron).run()
        """
    @overload
    def __init__(self, data, Vrep=..., 
....: facets = ..., unbounded=..., far_face=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 348)

                Initialize :class:`CombinatorialPolyhedron`.

                See :class:`CombinatorialPolyhedron`.

                TESTS::

                    sage: C = CombinatorialPolyhedron([[0,1,2], [0,1,3],   # indirect doctest
                    ....:                              [0,2,3], [1,2,3]])

                    sage: TestSuite(sage.geometry.polyhedron.combinatorial_polyhedron.base.CombinatorialPolyhedron).run()
        """
    @overload
    def __init__(self, facetinc, facets=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 348)

                Initialize :class:`CombinatorialPolyhedron`.

                See :class:`CombinatorialPolyhedron`.

                TESTS::

                    sage: C = CombinatorialPolyhedron([[0,1,2], [0,1,3],   # indirect doctest
                    ....:                              [0,2,3], [1,2,3]])

                    sage: TestSuite(sage.geometry.polyhedron.combinatorial_polyhedron.base.CombinatorialPolyhedron).run()
        """
    @overload
    def __init__(self, P) -> Any:
        """File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 348)

                Initialize :class:`CombinatorialPolyhedron`.

                See :class:`CombinatorialPolyhedron`.

                TESTS::

                    sage: C = CombinatorialPolyhedron([[0,1,2], [0,1,3],   # indirect doctest
                    ....:                              [0,2,3], [1,2,3]])

                    sage: TestSuite(sage.geometry.polyhedron.combinatorial_polyhedron.base.CombinatorialPolyhedron).run()
        """
    @overload
    def __init__(self, data, Vrep=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 348)

                Initialize :class:`CombinatorialPolyhedron`.

                See :class:`CombinatorialPolyhedron`.

                TESTS::

                    sage: C = CombinatorialPolyhedron([[0,1,2], [0,1,3],   # indirect doctest
                    ....:                              [0,2,3], [1,2,3]])

                    sage: TestSuite(sage.geometry.polyhedron.combinatorial_polyhedron.base.CombinatorialPolyhedron).run()
        """
    @overload
    def __init__(self, data, Vrep=..., unbounded=..., far_face=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 348)

                Initialize :class:`CombinatorialPolyhedron`.

                See :class:`CombinatorialPolyhedron`.

                TESTS::

                    sage: C = CombinatorialPolyhedron([[0,1,2], [0,1,3],   # indirect doctest
                    ....:                              [0,2,3], [1,2,3]])

                    sage: TestSuite(sage.geometry.polyhedron.combinatorial_polyhedron.base.CombinatorialPolyhedron).run()
        """
    @overload
    def __init__(self, P1) -> Any:
        """File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 348)

                Initialize :class:`CombinatorialPolyhedron`.

                See :class:`CombinatorialPolyhedron`.

                TESTS::

                    sage: C = CombinatorialPolyhedron([[0,1,2], [0,1,3],   # indirect doctest
                    ....:                              [0,2,3], [1,2,3]])

                    sage: TestSuite(sage.geometry.polyhedron.combinatorial_polyhedron.base.CombinatorialPolyhedron).run()
        """
    @overload
    def __init__(self, P2) -> Any:
        """File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 348)

                Initialize :class:`CombinatorialPolyhedron`.

                See :class:`CombinatorialPolyhedron`.

                TESTS::

                    sage: C = CombinatorialPolyhedron([[0,1,2], [0,1,3],   # indirect doctest
                    ....:                              [0,2,3], [1,2,3]])

                    sage: TestSuite(sage.geometry.polyhedron.combinatorial_polyhedron.base.CombinatorialPolyhedron).run()
        """
    @overload
    def __init__(self, P1) -> Any:
        """File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 348)

                Initialize :class:`CombinatorialPolyhedron`.

                See :class:`CombinatorialPolyhedron`.

                TESTS::

                    sage: C = CombinatorialPolyhedron([[0,1,2], [0,1,3],   # indirect doctest
                    ....:                              [0,2,3], [1,2,3]])

                    sage: TestSuite(sage.geometry.polyhedron.combinatorial_polyhedron.base.CombinatorialPolyhedron).run()
        """
    @overload
    def __init__(self, P2) -> Any:
        """File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 348)

                Initialize :class:`CombinatorialPolyhedron`.

                See :class:`CombinatorialPolyhedron`.

                TESTS::

                    sage: C = CombinatorialPolyhedron([[0,1,2], [0,1,3],   # indirect doctest
                    ....:                              [0,2,3], [1,2,3]])

                    sage: TestSuite(sage.geometry.polyhedron.combinatorial_polyhedron.base.CombinatorialPolyhedron).run()
        """
    @overload
    def __init__(self, P) -> Any:
        """File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 348)

                Initialize :class:`CombinatorialPolyhedron`.

                See :class:`CombinatorialPolyhedron`.

                TESTS::

                    sage: C = CombinatorialPolyhedron([[0,1,2], [0,1,3],   # indirect doctest
                    ....:                              [0,2,3], [1,2,3]])

                    sage: TestSuite(sage.geometry.polyhedron.combinatorial_polyhedron.base.CombinatorialPolyhedron).run()
        """
    @overload
    def __init__(self, data, Vrep=..., unbounded=..., far_face=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 348)

                Initialize :class:`CombinatorialPolyhedron`.

                See :class:`CombinatorialPolyhedron`.

                TESTS::

                    sage: C = CombinatorialPolyhedron([[0,1,2], [0,1,3],   # indirect doctest
                    ....:                              [0,2,3], [1,2,3]])

                    sage: TestSuite(sage.geometry.polyhedron.combinatorial_polyhedron.base.CombinatorialPolyhedron).run()
        """
    @overload
    def __init__(self, data, Vrep=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 348)

                Initialize :class:`CombinatorialPolyhedron`.

                See :class:`CombinatorialPolyhedron`.

                TESTS::

                    sage: C = CombinatorialPolyhedron([[0,1,2], [0,1,3],   # indirect doctest
                    ....:                              [0,2,3], [1,2,3]])

                    sage: TestSuite(sage.geometry.polyhedron.combinatorial_polyhedron.base.CombinatorialPolyhedron).run()
        """
    @overload
    def Hrepresentation(self) -> Any:
        """CombinatorialPolyhedron.Hrepresentation(self)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 743)

        Return a list of names of facets and possibly some equations.

        EXAMPLES::

            sage: P = polytopes.permutahedron(3)
            sage: C = CombinatorialPolyhedron(P)
            sage: C.Hrepresentation()
            (An inequality (1, 1, 0) x - 3 >= 0,
             An inequality (-1, -1, 0) x + 5 >= 0,
             An inequality (0, 1, 0) x - 1 >= 0,
             An inequality (-1, 0, 0) x + 3 >= 0,
             An inequality (1, 0, 0) x - 1 >= 0,
             An inequality (0, -1, 0) x + 3 >= 0,
             An equation (1, 1, 1) x - 6 == 0)

            sage: points = [(1,0,0), (0,1,0), (0,0,1),
            ....: (-1,0,0), (0,-1,0), (0,0,-1)]
            sage: L = LatticePolytope(points)
            sage: C = CombinatorialPolyhedron(L)
            sage: C.Hrepresentation()
            (N(1, -1, -1),
             N(1, 1, -1),
             N(1, 1, 1),
             N(1, -1, 1),
             N(-1, -1, 1),
             N(-1, -1, -1),
             N(-1, 1, -1),
             N(-1, 1, 1))

            sage: M = Cone([(1,0), (0,1)])
            sage: CombinatorialPolyhedron(M).Hrepresentation()
            (M(0, 1), M(1, 0))"""
    @overload
    def Hrepresentation(self) -> Any:
        """CombinatorialPolyhedron.Hrepresentation(self)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 743)

        Return a list of names of facets and possibly some equations.

        EXAMPLES::

            sage: P = polytopes.permutahedron(3)
            sage: C = CombinatorialPolyhedron(P)
            sage: C.Hrepresentation()
            (An inequality (1, 1, 0) x - 3 >= 0,
             An inequality (-1, -1, 0) x + 5 >= 0,
             An inequality (0, 1, 0) x - 1 >= 0,
             An inequality (-1, 0, 0) x + 3 >= 0,
             An inequality (1, 0, 0) x - 1 >= 0,
             An inequality (0, -1, 0) x + 3 >= 0,
             An equation (1, 1, 1) x - 6 == 0)

            sage: points = [(1,0,0), (0,1,0), (0,0,1),
            ....: (-1,0,0), (0,-1,0), (0,0,-1)]
            sage: L = LatticePolytope(points)
            sage: C = CombinatorialPolyhedron(L)
            sage: C.Hrepresentation()
            (N(1, -1, -1),
             N(1, 1, -1),
             N(1, 1, 1),
             N(1, -1, 1),
             N(-1, -1, 1),
             N(-1, -1, -1),
             N(-1, 1, -1),
             N(-1, 1, 1))

            sage: M = Cone([(1,0), (0,1)])
            sage: CombinatorialPolyhedron(M).Hrepresentation()
            (M(0, 1), M(1, 0))"""
    @overload
    def Hrepresentation(self) -> Any:
        """CombinatorialPolyhedron.Hrepresentation(self)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 743)

        Return a list of names of facets and possibly some equations.

        EXAMPLES::

            sage: P = polytopes.permutahedron(3)
            sage: C = CombinatorialPolyhedron(P)
            sage: C.Hrepresentation()
            (An inequality (1, 1, 0) x - 3 >= 0,
             An inequality (-1, -1, 0) x + 5 >= 0,
             An inequality (0, 1, 0) x - 1 >= 0,
             An inequality (-1, 0, 0) x + 3 >= 0,
             An inequality (1, 0, 0) x - 1 >= 0,
             An inequality (0, -1, 0) x + 3 >= 0,
             An equation (1, 1, 1) x - 6 == 0)

            sage: points = [(1,0,0), (0,1,0), (0,0,1),
            ....: (-1,0,0), (0,-1,0), (0,0,-1)]
            sage: L = LatticePolytope(points)
            sage: C = CombinatorialPolyhedron(L)
            sage: C.Hrepresentation()
            (N(1, -1, -1),
             N(1, 1, -1),
             N(1, 1, 1),
             N(1, -1, 1),
             N(-1, -1, 1),
             N(-1, -1, -1),
             N(-1, 1, -1),
             N(-1, 1, 1))

            sage: M = Cone([(1,0), (0,1)])
            sage: CombinatorialPolyhedron(M).Hrepresentation()
            (M(0, 1), M(1, 0))"""
    @overload
    def Hrepresentation(self) -> Any:
        """CombinatorialPolyhedron.Hrepresentation(self)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 743)

        Return a list of names of facets and possibly some equations.

        EXAMPLES::

            sage: P = polytopes.permutahedron(3)
            sage: C = CombinatorialPolyhedron(P)
            sage: C.Hrepresentation()
            (An inequality (1, 1, 0) x - 3 >= 0,
             An inequality (-1, -1, 0) x + 5 >= 0,
             An inequality (0, 1, 0) x - 1 >= 0,
             An inequality (-1, 0, 0) x + 3 >= 0,
             An inequality (1, 0, 0) x - 1 >= 0,
             An inequality (0, -1, 0) x + 3 >= 0,
             An equation (1, 1, 1) x - 6 == 0)

            sage: points = [(1,0,0), (0,1,0), (0,0,1),
            ....: (-1,0,0), (0,-1,0), (0,0,-1)]
            sage: L = LatticePolytope(points)
            sage: C = CombinatorialPolyhedron(L)
            sage: C.Hrepresentation()
            (N(1, -1, -1),
             N(1, 1, -1),
             N(1, 1, 1),
             N(1, -1, 1),
             N(-1, -1, 1),
             N(-1, -1, -1),
             N(-1, 1, -1),
             N(-1, 1, 1))

            sage: M = Cone([(1,0), (0,1)])
            sage: CombinatorialPolyhedron(M).Hrepresentation()
            (M(0, 1), M(1, 0))"""
    @overload
    def Vrepresentation(self) -> Any:
        """CombinatorialPolyhedron.Vrepresentation(self)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 712)

        Return a list of names of ``[vertices, rays, lines]``.

        EXAMPLES::

            sage: P = Polyhedron(rays=[[1,0,0], [0,1,0], \\\n            ....:                      [0,0,1],[0,0,-1]])
            sage: C = CombinatorialPolyhedron(P)
            sage: C.Vrepresentation()
            (A line in the direction (0, 0, 1),
             A ray in the direction (1, 0, 0),
             A vertex at (0, 0, 0),
             A ray in the direction (0, 1, 0))

            sage: points = [(1,0,0), (0,1,0), (0,0,1),
            ....: (-1,0,0), (0,-1,0), (0,0,-1)]
            sage: L = LatticePolytope(points)
            sage: C = CombinatorialPolyhedron(L)
            sage: C.Vrepresentation()
            (M(1, 0, 0), M(0, 1, 0), M(0, 0, 1), M(-1, 0, 0), M(0, -1, 0), M(0, 0, -1))

            sage: M = Cone([(1,0), (0,1)])
            sage: CombinatorialPolyhedron(M).Vrepresentation()
            (N(1, 0), N(0, 1), N(0, 0))"""
    @overload
    def Vrepresentation(self) -> Any:
        """CombinatorialPolyhedron.Vrepresentation(self)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 712)

        Return a list of names of ``[vertices, rays, lines]``.

        EXAMPLES::

            sage: P = Polyhedron(rays=[[1,0,0], [0,1,0], \\\n            ....:                      [0,0,1],[0,0,-1]])
            sage: C = CombinatorialPolyhedron(P)
            sage: C.Vrepresentation()
            (A line in the direction (0, 0, 1),
             A ray in the direction (1, 0, 0),
             A vertex at (0, 0, 0),
             A ray in the direction (0, 1, 0))

            sage: points = [(1,0,0), (0,1,0), (0,0,1),
            ....: (-1,0,0), (0,-1,0), (0,0,-1)]
            sage: L = LatticePolytope(points)
            sage: C = CombinatorialPolyhedron(L)
            sage: C.Vrepresentation()
            (M(1, 0, 0), M(0, 1, 0), M(0, 0, 1), M(-1, 0, 0), M(0, -1, 0), M(0, 0, -1))

            sage: M = Cone([(1,0), (0,1)])
            sage: CombinatorialPolyhedron(M).Vrepresentation()
            (N(1, 0), N(0, 1), N(0, 0))"""
    @overload
    def Vrepresentation(self) -> Any:
        """CombinatorialPolyhedron.Vrepresentation(self)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 712)

        Return a list of names of ``[vertices, rays, lines]``.

        EXAMPLES::

            sage: P = Polyhedron(rays=[[1,0,0], [0,1,0], \\\n            ....:                      [0,0,1],[0,0,-1]])
            sage: C = CombinatorialPolyhedron(P)
            sage: C.Vrepresentation()
            (A line in the direction (0, 0, 1),
             A ray in the direction (1, 0, 0),
             A vertex at (0, 0, 0),
             A ray in the direction (0, 1, 0))

            sage: points = [(1,0,0), (0,1,0), (0,0,1),
            ....: (-1,0,0), (0,-1,0), (0,0,-1)]
            sage: L = LatticePolytope(points)
            sage: C = CombinatorialPolyhedron(L)
            sage: C.Vrepresentation()
            (M(1, 0, 0), M(0, 1, 0), M(0, 0, 1), M(-1, 0, 0), M(0, -1, 0), M(0, 0, -1))

            sage: M = Cone([(1,0), (0,1)])
            sage: CombinatorialPolyhedron(M).Vrepresentation()
            (N(1, 0), N(0, 1), N(0, 0))"""
    @overload
    def Vrepresentation(self) -> Any:
        """CombinatorialPolyhedron.Vrepresentation(self)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 712)

        Return a list of names of ``[vertices, rays, lines]``.

        EXAMPLES::

            sage: P = Polyhedron(rays=[[1,0,0], [0,1,0], \\\n            ....:                      [0,0,1],[0,0,-1]])
            sage: C = CombinatorialPolyhedron(P)
            sage: C.Vrepresentation()
            (A line in the direction (0, 0, 1),
             A ray in the direction (1, 0, 0),
             A vertex at (0, 0, 0),
             A ray in the direction (0, 1, 0))

            sage: points = [(1,0,0), (0,1,0), (0,0,1),
            ....: (-1,0,0), (0,-1,0), (0,0,-1)]
            sage: L = LatticePolytope(points)
            sage: C = CombinatorialPolyhedron(L)
            sage: C.Vrepresentation()
            (M(1, 0, 0), M(0, 1, 0), M(0, 0, 1), M(-1, 0, 0), M(0, -1, 0), M(0, 0, -1))

            sage: M = Cone([(1,0), (0,1)])
            sage: CombinatorialPolyhedron(M).Vrepresentation()
            (N(1, 0), N(0, 1), N(0, 0))"""
    @overload
    def a_maximal_chain(self, Vindex=..., Hindex=...) -> Any:
        """CombinatorialPolyhedron.a_maximal_chain(self, Vindex=None, Hindex=None)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 2997)

        Return a maximal chain of the face lattice in increasing order
        without empty face and whole polyhedron/maximal face.

        INPUT:

        - ``Vindex`` -- integer (default: ``None``); prescribe the index of the vertex in the chain
        - ``Hindex`` -- integer (default: ``None``); prescribe the index of the facet in the chain

        Each face is given as
        :class:`~sage.geometry.polyhedron.combinatorial_polyhedron.combinatorial_face.CombinatorialFace`.

        EXAMPLES::

            sage: P = polytopes.cross_polytope(4)
            sage: C = P.combinatorial_polyhedron()
            sage: chain = C.a_maximal_chain(); chain
            [A 0-dimensional face of a 4-dimensional combinatorial polyhedron,
             A 1-dimensional face of a 4-dimensional combinatorial polyhedron,
             A 2-dimensional face of a 4-dimensional combinatorial polyhedron,
             A 3-dimensional face of a 4-dimensional combinatorial polyhedron]
            sage: [face.ambient_V_indices() for face in chain]
            [(7,), (6, 7), (5, 6, 7), (4, 5, 6, 7)]

            sage: P = polytopes.hypercube(4)
            sage: C = P.combinatorial_polyhedron()
            sage: chain = C.a_maximal_chain(); chain
            [A 0-dimensional face of a 4-dimensional combinatorial polyhedron,
             A 1-dimensional face of a 4-dimensional combinatorial polyhedron,
             A 2-dimensional face of a 4-dimensional combinatorial polyhedron,
             A 3-dimensional face of a 4-dimensional combinatorial polyhedron]
            sage: [face.ambient_V_indices() for face in chain]
            [(15,), (6, 15), (5, 6, 14, 15), (0, 5, 6, 7, 8, 9, 14, 15)]

            sage: # needs sage.combinat
            sage: P = polytopes.permutahedron(4)
            sage: C = P.combinatorial_polyhedron()
            sage: chain = C.a_maximal_chain(); chain
            [A 0-dimensional face of a 3-dimensional combinatorial polyhedron,
             A 1-dimensional face of a 3-dimensional combinatorial polyhedron,
             A 2-dimensional face of a 3-dimensional combinatorial polyhedron]
            sage: [face.ambient_V_indices() for face in chain]
            [(16,), (15, 16), (8, 9, 14, 15, 16, 17)]

            sage: P = Polyhedron(rays=[[1,0]], lines=[[0,1]])
            sage: C = P.combinatorial_polyhedron()
            sage: chain = C.a_maximal_chain()
            sage: [face.ambient_V_indices() for face in chain]
            [(0, 1)]

            sage: P = Polyhedron(rays=[[1,0,0],[0,0,1]], lines=[[0,1,0]])
            sage: C = P.combinatorial_polyhedron()
            sage: chain = C.a_maximal_chain()
            sage: [face.ambient_V_indices() for face in chain]
            [(0, 1), (0, 1, 3)]

            sage: P = Polyhedron(rays=[[1,0,0]], lines=[[0,1,0],[0,0,1]])
            sage: C = P.combinatorial_polyhedron()
            sage: chain = C.a_maximal_chain()
            sage: [face.ambient_V_indices() for face in chain]
            [(0, 1, 2)]

        Specify an index for the vertex of the chain::

            sage: P = polytopes.cube()
            sage: C = P.combinatorial_polyhedron()
            sage: [face.ambient_V_indices() for face in C.a_maximal_chain()]
            [(5,), (0, 5), (0, 3, 4, 5)]
            sage: [face.ambient_V_indices() for face in C.a_maximal_chain(Vindex=2)]
            [(2,), (2, 7), (2, 3, 4, 7)]

        Specify an index for the facet of the chain::

            sage: [face.ambient_H_indices() for face in C.a_maximal_chain()]
            [(3, 4, 5), (4, 5), (5,)]
            sage: [face.ambient_H_indices() for face in C.a_maximal_chain(Hindex=3)]
            [(3, 4, 5), (3, 4), (3,)]
            sage: [face.ambient_H_indices() for face in C.a_maximal_chain(Hindex=2)]
            [(2, 3, 5), (2, 3), (2,)]

        If the specified vertex is not contained in the specified facet an error is raised::

            sage: C.a_maximal_chain(Vindex=0, Hindex=3)
            Traceback (most recent call last):
            ...
            ValueError: the given Vindex is not compatible with the given Hindex

        An error is raised, if the specified index does not correspond to a facet::

            sage: C.a_maximal_chain(Hindex=40)
            Traceback (most recent call last):
            ...
            ValueError: the given Hindex does not correspond to a facet

        An error is raised, if the specified index does not correspond to a vertex::

            sage: C.a_maximal_chain(Vindex=40)
            Traceback (most recent call last):
            ...
            ValueError: the given Vindex does not correspond to a vertex

        ::

            sage: P = Polyhedron(rays=[[1,0,0],[0,0,1]], lines=[[0,1,0]])
            sage: C = P.combinatorial_polyhedron()
            sage: C.a_maximal_chain(Vindex=0)
            Traceback (most recent call last):
            ...
            ValueError: the given Vindex does not correspond to a vertex

        ::

            sage: P = Polyhedron(rays=[[1,0,0],[0,0,1]])
            sage: C = P.combinatorial_polyhedron()
            sage: C.a_maximal_chain(Vindex=0)
            [A 0-dimensional face of a 2-dimensional combinatorial polyhedron,
            A 1-dimensional face of a 2-dimensional combinatorial polyhedron]
            sage: C.a_maximal_chain(Vindex=1)
            Traceback (most recent call last):
            ...
            ValueError: the given Vindex does not correspond to a vertex"""
    @overload
    def a_maximal_chain(self) -> Any:
        """CombinatorialPolyhedron.a_maximal_chain(self, Vindex=None, Hindex=None)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 2997)

        Return a maximal chain of the face lattice in increasing order
        without empty face and whole polyhedron/maximal face.

        INPUT:

        - ``Vindex`` -- integer (default: ``None``); prescribe the index of the vertex in the chain
        - ``Hindex`` -- integer (default: ``None``); prescribe the index of the facet in the chain

        Each face is given as
        :class:`~sage.geometry.polyhedron.combinatorial_polyhedron.combinatorial_face.CombinatorialFace`.

        EXAMPLES::

            sage: P = polytopes.cross_polytope(4)
            sage: C = P.combinatorial_polyhedron()
            sage: chain = C.a_maximal_chain(); chain
            [A 0-dimensional face of a 4-dimensional combinatorial polyhedron,
             A 1-dimensional face of a 4-dimensional combinatorial polyhedron,
             A 2-dimensional face of a 4-dimensional combinatorial polyhedron,
             A 3-dimensional face of a 4-dimensional combinatorial polyhedron]
            sage: [face.ambient_V_indices() for face in chain]
            [(7,), (6, 7), (5, 6, 7), (4, 5, 6, 7)]

            sage: P = polytopes.hypercube(4)
            sage: C = P.combinatorial_polyhedron()
            sage: chain = C.a_maximal_chain(); chain
            [A 0-dimensional face of a 4-dimensional combinatorial polyhedron,
             A 1-dimensional face of a 4-dimensional combinatorial polyhedron,
             A 2-dimensional face of a 4-dimensional combinatorial polyhedron,
             A 3-dimensional face of a 4-dimensional combinatorial polyhedron]
            sage: [face.ambient_V_indices() for face in chain]
            [(15,), (6, 15), (5, 6, 14, 15), (0, 5, 6, 7, 8, 9, 14, 15)]

            sage: # needs sage.combinat
            sage: P = polytopes.permutahedron(4)
            sage: C = P.combinatorial_polyhedron()
            sage: chain = C.a_maximal_chain(); chain
            [A 0-dimensional face of a 3-dimensional combinatorial polyhedron,
             A 1-dimensional face of a 3-dimensional combinatorial polyhedron,
             A 2-dimensional face of a 3-dimensional combinatorial polyhedron]
            sage: [face.ambient_V_indices() for face in chain]
            [(16,), (15, 16), (8, 9, 14, 15, 16, 17)]

            sage: P = Polyhedron(rays=[[1,0]], lines=[[0,1]])
            sage: C = P.combinatorial_polyhedron()
            sage: chain = C.a_maximal_chain()
            sage: [face.ambient_V_indices() for face in chain]
            [(0, 1)]

            sage: P = Polyhedron(rays=[[1,0,0],[0,0,1]], lines=[[0,1,0]])
            sage: C = P.combinatorial_polyhedron()
            sage: chain = C.a_maximal_chain()
            sage: [face.ambient_V_indices() for face in chain]
            [(0, 1), (0, 1, 3)]

            sage: P = Polyhedron(rays=[[1,0,0]], lines=[[0,1,0],[0,0,1]])
            sage: C = P.combinatorial_polyhedron()
            sage: chain = C.a_maximal_chain()
            sage: [face.ambient_V_indices() for face in chain]
            [(0, 1, 2)]

        Specify an index for the vertex of the chain::

            sage: P = polytopes.cube()
            sage: C = P.combinatorial_polyhedron()
            sage: [face.ambient_V_indices() for face in C.a_maximal_chain()]
            [(5,), (0, 5), (0, 3, 4, 5)]
            sage: [face.ambient_V_indices() for face in C.a_maximal_chain(Vindex=2)]
            [(2,), (2, 7), (2, 3, 4, 7)]

        Specify an index for the facet of the chain::

            sage: [face.ambient_H_indices() for face in C.a_maximal_chain()]
            [(3, 4, 5), (4, 5), (5,)]
            sage: [face.ambient_H_indices() for face in C.a_maximal_chain(Hindex=3)]
            [(3, 4, 5), (3, 4), (3,)]
            sage: [face.ambient_H_indices() for face in C.a_maximal_chain(Hindex=2)]
            [(2, 3, 5), (2, 3), (2,)]

        If the specified vertex is not contained in the specified facet an error is raised::

            sage: C.a_maximal_chain(Vindex=0, Hindex=3)
            Traceback (most recent call last):
            ...
            ValueError: the given Vindex is not compatible with the given Hindex

        An error is raised, if the specified index does not correspond to a facet::

            sage: C.a_maximal_chain(Hindex=40)
            Traceback (most recent call last):
            ...
            ValueError: the given Hindex does not correspond to a facet

        An error is raised, if the specified index does not correspond to a vertex::

            sage: C.a_maximal_chain(Vindex=40)
            Traceback (most recent call last):
            ...
            ValueError: the given Vindex does not correspond to a vertex

        ::

            sage: P = Polyhedron(rays=[[1,0,0],[0,0,1]], lines=[[0,1,0]])
            sage: C = P.combinatorial_polyhedron()
            sage: C.a_maximal_chain(Vindex=0)
            Traceback (most recent call last):
            ...
            ValueError: the given Vindex does not correspond to a vertex

        ::

            sage: P = Polyhedron(rays=[[1,0,0],[0,0,1]])
            sage: C = P.combinatorial_polyhedron()
            sage: C.a_maximal_chain(Vindex=0)
            [A 0-dimensional face of a 2-dimensional combinatorial polyhedron,
            A 1-dimensional face of a 2-dimensional combinatorial polyhedron]
            sage: C.a_maximal_chain(Vindex=1)
            Traceback (most recent call last):
            ...
            ValueError: the given Vindex does not correspond to a vertex"""
    @overload
    def a_maximal_chain(self) -> Any:
        """CombinatorialPolyhedron.a_maximal_chain(self, Vindex=None, Hindex=None)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 2997)

        Return a maximal chain of the face lattice in increasing order
        without empty face and whole polyhedron/maximal face.

        INPUT:

        - ``Vindex`` -- integer (default: ``None``); prescribe the index of the vertex in the chain
        - ``Hindex`` -- integer (default: ``None``); prescribe the index of the facet in the chain

        Each face is given as
        :class:`~sage.geometry.polyhedron.combinatorial_polyhedron.combinatorial_face.CombinatorialFace`.

        EXAMPLES::

            sage: P = polytopes.cross_polytope(4)
            sage: C = P.combinatorial_polyhedron()
            sage: chain = C.a_maximal_chain(); chain
            [A 0-dimensional face of a 4-dimensional combinatorial polyhedron,
             A 1-dimensional face of a 4-dimensional combinatorial polyhedron,
             A 2-dimensional face of a 4-dimensional combinatorial polyhedron,
             A 3-dimensional face of a 4-dimensional combinatorial polyhedron]
            sage: [face.ambient_V_indices() for face in chain]
            [(7,), (6, 7), (5, 6, 7), (4, 5, 6, 7)]

            sage: P = polytopes.hypercube(4)
            sage: C = P.combinatorial_polyhedron()
            sage: chain = C.a_maximal_chain(); chain
            [A 0-dimensional face of a 4-dimensional combinatorial polyhedron,
             A 1-dimensional face of a 4-dimensional combinatorial polyhedron,
             A 2-dimensional face of a 4-dimensional combinatorial polyhedron,
             A 3-dimensional face of a 4-dimensional combinatorial polyhedron]
            sage: [face.ambient_V_indices() for face in chain]
            [(15,), (6, 15), (5, 6, 14, 15), (0, 5, 6, 7, 8, 9, 14, 15)]

            sage: # needs sage.combinat
            sage: P = polytopes.permutahedron(4)
            sage: C = P.combinatorial_polyhedron()
            sage: chain = C.a_maximal_chain(); chain
            [A 0-dimensional face of a 3-dimensional combinatorial polyhedron,
             A 1-dimensional face of a 3-dimensional combinatorial polyhedron,
             A 2-dimensional face of a 3-dimensional combinatorial polyhedron]
            sage: [face.ambient_V_indices() for face in chain]
            [(16,), (15, 16), (8, 9, 14, 15, 16, 17)]

            sage: P = Polyhedron(rays=[[1,0]], lines=[[0,1]])
            sage: C = P.combinatorial_polyhedron()
            sage: chain = C.a_maximal_chain()
            sage: [face.ambient_V_indices() for face in chain]
            [(0, 1)]

            sage: P = Polyhedron(rays=[[1,0,0],[0,0,1]], lines=[[0,1,0]])
            sage: C = P.combinatorial_polyhedron()
            sage: chain = C.a_maximal_chain()
            sage: [face.ambient_V_indices() for face in chain]
            [(0, 1), (0, 1, 3)]

            sage: P = Polyhedron(rays=[[1,0,0]], lines=[[0,1,0],[0,0,1]])
            sage: C = P.combinatorial_polyhedron()
            sage: chain = C.a_maximal_chain()
            sage: [face.ambient_V_indices() for face in chain]
            [(0, 1, 2)]

        Specify an index for the vertex of the chain::

            sage: P = polytopes.cube()
            sage: C = P.combinatorial_polyhedron()
            sage: [face.ambient_V_indices() for face in C.a_maximal_chain()]
            [(5,), (0, 5), (0, 3, 4, 5)]
            sage: [face.ambient_V_indices() for face in C.a_maximal_chain(Vindex=2)]
            [(2,), (2, 7), (2, 3, 4, 7)]

        Specify an index for the facet of the chain::

            sage: [face.ambient_H_indices() for face in C.a_maximal_chain()]
            [(3, 4, 5), (4, 5), (5,)]
            sage: [face.ambient_H_indices() for face in C.a_maximal_chain(Hindex=3)]
            [(3, 4, 5), (3, 4), (3,)]
            sage: [face.ambient_H_indices() for face in C.a_maximal_chain(Hindex=2)]
            [(2, 3, 5), (2, 3), (2,)]

        If the specified vertex is not contained in the specified facet an error is raised::

            sage: C.a_maximal_chain(Vindex=0, Hindex=3)
            Traceback (most recent call last):
            ...
            ValueError: the given Vindex is not compatible with the given Hindex

        An error is raised, if the specified index does not correspond to a facet::

            sage: C.a_maximal_chain(Hindex=40)
            Traceback (most recent call last):
            ...
            ValueError: the given Hindex does not correspond to a facet

        An error is raised, if the specified index does not correspond to a vertex::

            sage: C.a_maximal_chain(Vindex=40)
            Traceback (most recent call last):
            ...
            ValueError: the given Vindex does not correspond to a vertex

        ::

            sage: P = Polyhedron(rays=[[1,0,0],[0,0,1]], lines=[[0,1,0]])
            sage: C = P.combinatorial_polyhedron()
            sage: C.a_maximal_chain(Vindex=0)
            Traceback (most recent call last):
            ...
            ValueError: the given Vindex does not correspond to a vertex

        ::

            sage: P = Polyhedron(rays=[[1,0,0],[0,0,1]])
            sage: C = P.combinatorial_polyhedron()
            sage: C.a_maximal_chain(Vindex=0)
            [A 0-dimensional face of a 2-dimensional combinatorial polyhedron,
            A 1-dimensional face of a 2-dimensional combinatorial polyhedron]
            sage: C.a_maximal_chain(Vindex=1)
            Traceback (most recent call last):
            ...
            ValueError: the given Vindex does not correspond to a vertex"""
    @overload
    def a_maximal_chain(self) -> Any:
        """CombinatorialPolyhedron.a_maximal_chain(self, Vindex=None, Hindex=None)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 2997)

        Return a maximal chain of the face lattice in increasing order
        without empty face and whole polyhedron/maximal face.

        INPUT:

        - ``Vindex`` -- integer (default: ``None``); prescribe the index of the vertex in the chain
        - ``Hindex`` -- integer (default: ``None``); prescribe the index of the facet in the chain

        Each face is given as
        :class:`~sage.geometry.polyhedron.combinatorial_polyhedron.combinatorial_face.CombinatorialFace`.

        EXAMPLES::

            sage: P = polytopes.cross_polytope(4)
            sage: C = P.combinatorial_polyhedron()
            sage: chain = C.a_maximal_chain(); chain
            [A 0-dimensional face of a 4-dimensional combinatorial polyhedron,
             A 1-dimensional face of a 4-dimensional combinatorial polyhedron,
             A 2-dimensional face of a 4-dimensional combinatorial polyhedron,
             A 3-dimensional face of a 4-dimensional combinatorial polyhedron]
            sage: [face.ambient_V_indices() for face in chain]
            [(7,), (6, 7), (5, 6, 7), (4, 5, 6, 7)]

            sage: P = polytopes.hypercube(4)
            sage: C = P.combinatorial_polyhedron()
            sage: chain = C.a_maximal_chain(); chain
            [A 0-dimensional face of a 4-dimensional combinatorial polyhedron,
             A 1-dimensional face of a 4-dimensional combinatorial polyhedron,
             A 2-dimensional face of a 4-dimensional combinatorial polyhedron,
             A 3-dimensional face of a 4-dimensional combinatorial polyhedron]
            sage: [face.ambient_V_indices() for face in chain]
            [(15,), (6, 15), (5, 6, 14, 15), (0, 5, 6, 7, 8, 9, 14, 15)]

            sage: # needs sage.combinat
            sage: P = polytopes.permutahedron(4)
            sage: C = P.combinatorial_polyhedron()
            sage: chain = C.a_maximal_chain(); chain
            [A 0-dimensional face of a 3-dimensional combinatorial polyhedron,
             A 1-dimensional face of a 3-dimensional combinatorial polyhedron,
             A 2-dimensional face of a 3-dimensional combinatorial polyhedron]
            sage: [face.ambient_V_indices() for face in chain]
            [(16,), (15, 16), (8, 9, 14, 15, 16, 17)]

            sage: P = Polyhedron(rays=[[1,0]], lines=[[0,1]])
            sage: C = P.combinatorial_polyhedron()
            sage: chain = C.a_maximal_chain()
            sage: [face.ambient_V_indices() for face in chain]
            [(0, 1)]

            sage: P = Polyhedron(rays=[[1,0,0],[0,0,1]], lines=[[0,1,0]])
            sage: C = P.combinatorial_polyhedron()
            sage: chain = C.a_maximal_chain()
            sage: [face.ambient_V_indices() for face in chain]
            [(0, 1), (0, 1, 3)]

            sage: P = Polyhedron(rays=[[1,0,0]], lines=[[0,1,0],[0,0,1]])
            sage: C = P.combinatorial_polyhedron()
            sage: chain = C.a_maximal_chain()
            sage: [face.ambient_V_indices() for face in chain]
            [(0, 1, 2)]

        Specify an index for the vertex of the chain::

            sage: P = polytopes.cube()
            sage: C = P.combinatorial_polyhedron()
            sage: [face.ambient_V_indices() for face in C.a_maximal_chain()]
            [(5,), (0, 5), (0, 3, 4, 5)]
            sage: [face.ambient_V_indices() for face in C.a_maximal_chain(Vindex=2)]
            [(2,), (2, 7), (2, 3, 4, 7)]

        Specify an index for the facet of the chain::

            sage: [face.ambient_H_indices() for face in C.a_maximal_chain()]
            [(3, 4, 5), (4, 5), (5,)]
            sage: [face.ambient_H_indices() for face in C.a_maximal_chain(Hindex=3)]
            [(3, 4, 5), (3, 4), (3,)]
            sage: [face.ambient_H_indices() for face in C.a_maximal_chain(Hindex=2)]
            [(2, 3, 5), (2, 3), (2,)]

        If the specified vertex is not contained in the specified facet an error is raised::

            sage: C.a_maximal_chain(Vindex=0, Hindex=3)
            Traceback (most recent call last):
            ...
            ValueError: the given Vindex is not compatible with the given Hindex

        An error is raised, if the specified index does not correspond to a facet::

            sage: C.a_maximal_chain(Hindex=40)
            Traceback (most recent call last):
            ...
            ValueError: the given Hindex does not correspond to a facet

        An error is raised, if the specified index does not correspond to a vertex::

            sage: C.a_maximal_chain(Vindex=40)
            Traceback (most recent call last):
            ...
            ValueError: the given Vindex does not correspond to a vertex

        ::

            sage: P = Polyhedron(rays=[[1,0,0],[0,0,1]], lines=[[0,1,0]])
            sage: C = P.combinatorial_polyhedron()
            sage: C.a_maximal_chain(Vindex=0)
            Traceback (most recent call last):
            ...
            ValueError: the given Vindex does not correspond to a vertex

        ::

            sage: P = Polyhedron(rays=[[1,0,0],[0,0,1]])
            sage: C = P.combinatorial_polyhedron()
            sage: C.a_maximal_chain(Vindex=0)
            [A 0-dimensional face of a 2-dimensional combinatorial polyhedron,
            A 1-dimensional face of a 2-dimensional combinatorial polyhedron]
            sage: C.a_maximal_chain(Vindex=1)
            Traceback (most recent call last):
            ...
            ValueError: the given Vindex does not correspond to a vertex"""
    @overload
    def a_maximal_chain(self) -> Any:
        """CombinatorialPolyhedron.a_maximal_chain(self, Vindex=None, Hindex=None)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 2997)

        Return a maximal chain of the face lattice in increasing order
        without empty face and whole polyhedron/maximal face.

        INPUT:

        - ``Vindex`` -- integer (default: ``None``); prescribe the index of the vertex in the chain
        - ``Hindex`` -- integer (default: ``None``); prescribe the index of the facet in the chain

        Each face is given as
        :class:`~sage.geometry.polyhedron.combinatorial_polyhedron.combinatorial_face.CombinatorialFace`.

        EXAMPLES::

            sage: P = polytopes.cross_polytope(4)
            sage: C = P.combinatorial_polyhedron()
            sage: chain = C.a_maximal_chain(); chain
            [A 0-dimensional face of a 4-dimensional combinatorial polyhedron,
             A 1-dimensional face of a 4-dimensional combinatorial polyhedron,
             A 2-dimensional face of a 4-dimensional combinatorial polyhedron,
             A 3-dimensional face of a 4-dimensional combinatorial polyhedron]
            sage: [face.ambient_V_indices() for face in chain]
            [(7,), (6, 7), (5, 6, 7), (4, 5, 6, 7)]

            sage: P = polytopes.hypercube(4)
            sage: C = P.combinatorial_polyhedron()
            sage: chain = C.a_maximal_chain(); chain
            [A 0-dimensional face of a 4-dimensional combinatorial polyhedron,
             A 1-dimensional face of a 4-dimensional combinatorial polyhedron,
             A 2-dimensional face of a 4-dimensional combinatorial polyhedron,
             A 3-dimensional face of a 4-dimensional combinatorial polyhedron]
            sage: [face.ambient_V_indices() for face in chain]
            [(15,), (6, 15), (5, 6, 14, 15), (0, 5, 6, 7, 8, 9, 14, 15)]

            sage: # needs sage.combinat
            sage: P = polytopes.permutahedron(4)
            sage: C = P.combinatorial_polyhedron()
            sage: chain = C.a_maximal_chain(); chain
            [A 0-dimensional face of a 3-dimensional combinatorial polyhedron,
             A 1-dimensional face of a 3-dimensional combinatorial polyhedron,
             A 2-dimensional face of a 3-dimensional combinatorial polyhedron]
            sage: [face.ambient_V_indices() for face in chain]
            [(16,), (15, 16), (8, 9, 14, 15, 16, 17)]

            sage: P = Polyhedron(rays=[[1,0]], lines=[[0,1]])
            sage: C = P.combinatorial_polyhedron()
            sage: chain = C.a_maximal_chain()
            sage: [face.ambient_V_indices() for face in chain]
            [(0, 1)]

            sage: P = Polyhedron(rays=[[1,0,0],[0,0,1]], lines=[[0,1,0]])
            sage: C = P.combinatorial_polyhedron()
            sage: chain = C.a_maximal_chain()
            sage: [face.ambient_V_indices() for face in chain]
            [(0, 1), (0, 1, 3)]

            sage: P = Polyhedron(rays=[[1,0,0]], lines=[[0,1,0],[0,0,1]])
            sage: C = P.combinatorial_polyhedron()
            sage: chain = C.a_maximal_chain()
            sage: [face.ambient_V_indices() for face in chain]
            [(0, 1, 2)]

        Specify an index for the vertex of the chain::

            sage: P = polytopes.cube()
            sage: C = P.combinatorial_polyhedron()
            sage: [face.ambient_V_indices() for face in C.a_maximal_chain()]
            [(5,), (0, 5), (0, 3, 4, 5)]
            sage: [face.ambient_V_indices() for face in C.a_maximal_chain(Vindex=2)]
            [(2,), (2, 7), (2, 3, 4, 7)]

        Specify an index for the facet of the chain::

            sage: [face.ambient_H_indices() for face in C.a_maximal_chain()]
            [(3, 4, 5), (4, 5), (5,)]
            sage: [face.ambient_H_indices() for face in C.a_maximal_chain(Hindex=3)]
            [(3, 4, 5), (3, 4), (3,)]
            sage: [face.ambient_H_indices() for face in C.a_maximal_chain(Hindex=2)]
            [(2, 3, 5), (2, 3), (2,)]

        If the specified vertex is not contained in the specified facet an error is raised::

            sage: C.a_maximal_chain(Vindex=0, Hindex=3)
            Traceback (most recent call last):
            ...
            ValueError: the given Vindex is not compatible with the given Hindex

        An error is raised, if the specified index does not correspond to a facet::

            sage: C.a_maximal_chain(Hindex=40)
            Traceback (most recent call last):
            ...
            ValueError: the given Hindex does not correspond to a facet

        An error is raised, if the specified index does not correspond to a vertex::

            sage: C.a_maximal_chain(Vindex=40)
            Traceback (most recent call last):
            ...
            ValueError: the given Vindex does not correspond to a vertex

        ::

            sage: P = Polyhedron(rays=[[1,0,0],[0,0,1]], lines=[[0,1,0]])
            sage: C = P.combinatorial_polyhedron()
            sage: C.a_maximal_chain(Vindex=0)
            Traceback (most recent call last):
            ...
            ValueError: the given Vindex does not correspond to a vertex

        ::

            sage: P = Polyhedron(rays=[[1,0,0],[0,0,1]])
            sage: C = P.combinatorial_polyhedron()
            sage: C.a_maximal_chain(Vindex=0)
            [A 0-dimensional face of a 2-dimensional combinatorial polyhedron,
            A 1-dimensional face of a 2-dimensional combinatorial polyhedron]
            sage: C.a_maximal_chain(Vindex=1)
            Traceback (most recent call last):
            ...
            ValueError: the given Vindex does not correspond to a vertex"""
    @overload
    def a_maximal_chain(self) -> Any:
        """CombinatorialPolyhedron.a_maximal_chain(self, Vindex=None, Hindex=None)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 2997)

        Return a maximal chain of the face lattice in increasing order
        without empty face and whole polyhedron/maximal face.

        INPUT:

        - ``Vindex`` -- integer (default: ``None``); prescribe the index of the vertex in the chain
        - ``Hindex`` -- integer (default: ``None``); prescribe the index of the facet in the chain

        Each face is given as
        :class:`~sage.geometry.polyhedron.combinatorial_polyhedron.combinatorial_face.CombinatorialFace`.

        EXAMPLES::

            sage: P = polytopes.cross_polytope(4)
            sage: C = P.combinatorial_polyhedron()
            sage: chain = C.a_maximal_chain(); chain
            [A 0-dimensional face of a 4-dimensional combinatorial polyhedron,
             A 1-dimensional face of a 4-dimensional combinatorial polyhedron,
             A 2-dimensional face of a 4-dimensional combinatorial polyhedron,
             A 3-dimensional face of a 4-dimensional combinatorial polyhedron]
            sage: [face.ambient_V_indices() for face in chain]
            [(7,), (6, 7), (5, 6, 7), (4, 5, 6, 7)]

            sage: P = polytopes.hypercube(4)
            sage: C = P.combinatorial_polyhedron()
            sage: chain = C.a_maximal_chain(); chain
            [A 0-dimensional face of a 4-dimensional combinatorial polyhedron,
             A 1-dimensional face of a 4-dimensional combinatorial polyhedron,
             A 2-dimensional face of a 4-dimensional combinatorial polyhedron,
             A 3-dimensional face of a 4-dimensional combinatorial polyhedron]
            sage: [face.ambient_V_indices() for face in chain]
            [(15,), (6, 15), (5, 6, 14, 15), (0, 5, 6, 7, 8, 9, 14, 15)]

            sage: # needs sage.combinat
            sage: P = polytopes.permutahedron(4)
            sage: C = P.combinatorial_polyhedron()
            sage: chain = C.a_maximal_chain(); chain
            [A 0-dimensional face of a 3-dimensional combinatorial polyhedron,
             A 1-dimensional face of a 3-dimensional combinatorial polyhedron,
             A 2-dimensional face of a 3-dimensional combinatorial polyhedron]
            sage: [face.ambient_V_indices() for face in chain]
            [(16,), (15, 16), (8, 9, 14, 15, 16, 17)]

            sage: P = Polyhedron(rays=[[1,0]], lines=[[0,1]])
            sage: C = P.combinatorial_polyhedron()
            sage: chain = C.a_maximal_chain()
            sage: [face.ambient_V_indices() for face in chain]
            [(0, 1)]

            sage: P = Polyhedron(rays=[[1,0,0],[0,0,1]], lines=[[0,1,0]])
            sage: C = P.combinatorial_polyhedron()
            sage: chain = C.a_maximal_chain()
            sage: [face.ambient_V_indices() for face in chain]
            [(0, 1), (0, 1, 3)]

            sage: P = Polyhedron(rays=[[1,0,0]], lines=[[0,1,0],[0,0,1]])
            sage: C = P.combinatorial_polyhedron()
            sage: chain = C.a_maximal_chain()
            sage: [face.ambient_V_indices() for face in chain]
            [(0, 1, 2)]

        Specify an index for the vertex of the chain::

            sage: P = polytopes.cube()
            sage: C = P.combinatorial_polyhedron()
            sage: [face.ambient_V_indices() for face in C.a_maximal_chain()]
            [(5,), (0, 5), (0, 3, 4, 5)]
            sage: [face.ambient_V_indices() for face in C.a_maximal_chain(Vindex=2)]
            [(2,), (2, 7), (2, 3, 4, 7)]

        Specify an index for the facet of the chain::

            sage: [face.ambient_H_indices() for face in C.a_maximal_chain()]
            [(3, 4, 5), (4, 5), (5,)]
            sage: [face.ambient_H_indices() for face in C.a_maximal_chain(Hindex=3)]
            [(3, 4, 5), (3, 4), (3,)]
            sage: [face.ambient_H_indices() for face in C.a_maximal_chain(Hindex=2)]
            [(2, 3, 5), (2, 3), (2,)]

        If the specified vertex is not contained in the specified facet an error is raised::

            sage: C.a_maximal_chain(Vindex=0, Hindex=3)
            Traceback (most recent call last):
            ...
            ValueError: the given Vindex is not compatible with the given Hindex

        An error is raised, if the specified index does not correspond to a facet::

            sage: C.a_maximal_chain(Hindex=40)
            Traceback (most recent call last):
            ...
            ValueError: the given Hindex does not correspond to a facet

        An error is raised, if the specified index does not correspond to a vertex::

            sage: C.a_maximal_chain(Vindex=40)
            Traceback (most recent call last):
            ...
            ValueError: the given Vindex does not correspond to a vertex

        ::

            sage: P = Polyhedron(rays=[[1,0,0],[0,0,1]], lines=[[0,1,0]])
            sage: C = P.combinatorial_polyhedron()
            sage: C.a_maximal_chain(Vindex=0)
            Traceback (most recent call last):
            ...
            ValueError: the given Vindex does not correspond to a vertex

        ::

            sage: P = Polyhedron(rays=[[1,0,0],[0,0,1]])
            sage: C = P.combinatorial_polyhedron()
            sage: C.a_maximal_chain(Vindex=0)
            [A 0-dimensional face of a 2-dimensional combinatorial polyhedron,
            A 1-dimensional face of a 2-dimensional combinatorial polyhedron]
            sage: C.a_maximal_chain(Vindex=1)
            Traceback (most recent call last):
            ...
            ValueError: the given Vindex does not correspond to a vertex"""
    @overload
    def a_maximal_chain(self) -> Any:
        """CombinatorialPolyhedron.a_maximal_chain(self, Vindex=None, Hindex=None)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 2997)

        Return a maximal chain of the face lattice in increasing order
        without empty face and whole polyhedron/maximal face.

        INPUT:

        - ``Vindex`` -- integer (default: ``None``); prescribe the index of the vertex in the chain
        - ``Hindex`` -- integer (default: ``None``); prescribe the index of the facet in the chain

        Each face is given as
        :class:`~sage.geometry.polyhedron.combinatorial_polyhedron.combinatorial_face.CombinatorialFace`.

        EXAMPLES::

            sage: P = polytopes.cross_polytope(4)
            sage: C = P.combinatorial_polyhedron()
            sage: chain = C.a_maximal_chain(); chain
            [A 0-dimensional face of a 4-dimensional combinatorial polyhedron,
             A 1-dimensional face of a 4-dimensional combinatorial polyhedron,
             A 2-dimensional face of a 4-dimensional combinatorial polyhedron,
             A 3-dimensional face of a 4-dimensional combinatorial polyhedron]
            sage: [face.ambient_V_indices() for face in chain]
            [(7,), (6, 7), (5, 6, 7), (4, 5, 6, 7)]

            sage: P = polytopes.hypercube(4)
            sage: C = P.combinatorial_polyhedron()
            sage: chain = C.a_maximal_chain(); chain
            [A 0-dimensional face of a 4-dimensional combinatorial polyhedron,
             A 1-dimensional face of a 4-dimensional combinatorial polyhedron,
             A 2-dimensional face of a 4-dimensional combinatorial polyhedron,
             A 3-dimensional face of a 4-dimensional combinatorial polyhedron]
            sage: [face.ambient_V_indices() for face in chain]
            [(15,), (6, 15), (5, 6, 14, 15), (0, 5, 6, 7, 8, 9, 14, 15)]

            sage: # needs sage.combinat
            sage: P = polytopes.permutahedron(4)
            sage: C = P.combinatorial_polyhedron()
            sage: chain = C.a_maximal_chain(); chain
            [A 0-dimensional face of a 3-dimensional combinatorial polyhedron,
             A 1-dimensional face of a 3-dimensional combinatorial polyhedron,
             A 2-dimensional face of a 3-dimensional combinatorial polyhedron]
            sage: [face.ambient_V_indices() for face in chain]
            [(16,), (15, 16), (8, 9, 14, 15, 16, 17)]

            sage: P = Polyhedron(rays=[[1,0]], lines=[[0,1]])
            sage: C = P.combinatorial_polyhedron()
            sage: chain = C.a_maximal_chain()
            sage: [face.ambient_V_indices() for face in chain]
            [(0, 1)]

            sage: P = Polyhedron(rays=[[1,0,0],[0,0,1]], lines=[[0,1,0]])
            sage: C = P.combinatorial_polyhedron()
            sage: chain = C.a_maximal_chain()
            sage: [face.ambient_V_indices() for face in chain]
            [(0, 1), (0, 1, 3)]

            sage: P = Polyhedron(rays=[[1,0,0]], lines=[[0,1,0],[0,0,1]])
            sage: C = P.combinatorial_polyhedron()
            sage: chain = C.a_maximal_chain()
            sage: [face.ambient_V_indices() for face in chain]
            [(0, 1, 2)]

        Specify an index for the vertex of the chain::

            sage: P = polytopes.cube()
            sage: C = P.combinatorial_polyhedron()
            sage: [face.ambient_V_indices() for face in C.a_maximal_chain()]
            [(5,), (0, 5), (0, 3, 4, 5)]
            sage: [face.ambient_V_indices() for face in C.a_maximal_chain(Vindex=2)]
            [(2,), (2, 7), (2, 3, 4, 7)]

        Specify an index for the facet of the chain::

            sage: [face.ambient_H_indices() for face in C.a_maximal_chain()]
            [(3, 4, 5), (4, 5), (5,)]
            sage: [face.ambient_H_indices() for face in C.a_maximal_chain(Hindex=3)]
            [(3, 4, 5), (3, 4), (3,)]
            sage: [face.ambient_H_indices() for face in C.a_maximal_chain(Hindex=2)]
            [(2, 3, 5), (2, 3), (2,)]

        If the specified vertex is not contained in the specified facet an error is raised::

            sage: C.a_maximal_chain(Vindex=0, Hindex=3)
            Traceback (most recent call last):
            ...
            ValueError: the given Vindex is not compatible with the given Hindex

        An error is raised, if the specified index does not correspond to a facet::

            sage: C.a_maximal_chain(Hindex=40)
            Traceback (most recent call last):
            ...
            ValueError: the given Hindex does not correspond to a facet

        An error is raised, if the specified index does not correspond to a vertex::

            sage: C.a_maximal_chain(Vindex=40)
            Traceback (most recent call last):
            ...
            ValueError: the given Vindex does not correspond to a vertex

        ::

            sage: P = Polyhedron(rays=[[1,0,0],[0,0,1]], lines=[[0,1,0]])
            sage: C = P.combinatorial_polyhedron()
            sage: C.a_maximal_chain(Vindex=0)
            Traceback (most recent call last):
            ...
            ValueError: the given Vindex does not correspond to a vertex

        ::

            sage: P = Polyhedron(rays=[[1,0,0],[0,0,1]])
            sage: C = P.combinatorial_polyhedron()
            sage: C.a_maximal_chain(Vindex=0)
            [A 0-dimensional face of a 2-dimensional combinatorial polyhedron,
            A 1-dimensional face of a 2-dimensional combinatorial polyhedron]
            sage: C.a_maximal_chain(Vindex=1)
            Traceback (most recent call last):
            ...
            ValueError: the given Vindex does not correspond to a vertex"""
    @overload
    def a_maximal_chain(self) -> Any:
        """CombinatorialPolyhedron.a_maximal_chain(self, Vindex=None, Hindex=None)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 2997)

        Return a maximal chain of the face lattice in increasing order
        without empty face and whole polyhedron/maximal face.

        INPUT:

        - ``Vindex`` -- integer (default: ``None``); prescribe the index of the vertex in the chain
        - ``Hindex`` -- integer (default: ``None``); prescribe the index of the facet in the chain

        Each face is given as
        :class:`~sage.geometry.polyhedron.combinatorial_polyhedron.combinatorial_face.CombinatorialFace`.

        EXAMPLES::

            sage: P = polytopes.cross_polytope(4)
            sage: C = P.combinatorial_polyhedron()
            sage: chain = C.a_maximal_chain(); chain
            [A 0-dimensional face of a 4-dimensional combinatorial polyhedron,
             A 1-dimensional face of a 4-dimensional combinatorial polyhedron,
             A 2-dimensional face of a 4-dimensional combinatorial polyhedron,
             A 3-dimensional face of a 4-dimensional combinatorial polyhedron]
            sage: [face.ambient_V_indices() for face in chain]
            [(7,), (6, 7), (5, 6, 7), (4, 5, 6, 7)]

            sage: P = polytopes.hypercube(4)
            sage: C = P.combinatorial_polyhedron()
            sage: chain = C.a_maximal_chain(); chain
            [A 0-dimensional face of a 4-dimensional combinatorial polyhedron,
             A 1-dimensional face of a 4-dimensional combinatorial polyhedron,
             A 2-dimensional face of a 4-dimensional combinatorial polyhedron,
             A 3-dimensional face of a 4-dimensional combinatorial polyhedron]
            sage: [face.ambient_V_indices() for face in chain]
            [(15,), (6, 15), (5, 6, 14, 15), (0, 5, 6, 7, 8, 9, 14, 15)]

            sage: # needs sage.combinat
            sage: P = polytopes.permutahedron(4)
            sage: C = P.combinatorial_polyhedron()
            sage: chain = C.a_maximal_chain(); chain
            [A 0-dimensional face of a 3-dimensional combinatorial polyhedron,
             A 1-dimensional face of a 3-dimensional combinatorial polyhedron,
             A 2-dimensional face of a 3-dimensional combinatorial polyhedron]
            sage: [face.ambient_V_indices() for face in chain]
            [(16,), (15, 16), (8, 9, 14, 15, 16, 17)]

            sage: P = Polyhedron(rays=[[1,0]], lines=[[0,1]])
            sage: C = P.combinatorial_polyhedron()
            sage: chain = C.a_maximal_chain()
            sage: [face.ambient_V_indices() for face in chain]
            [(0, 1)]

            sage: P = Polyhedron(rays=[[1,0,0],[0,0,1]], lines=[[0,1,0]])
            sage: C = P.combinatorial_polyhedron()
            sage: chain = C.a_maximal_chain()
            sage: [face.ambient_V_indices() for face in chain]
            [(0, 1), (0, 1, 3)]

            sage: P = Polyhedron(rays=[[1,0,0]], lines=[[0,1,0],[0,0,1]])
            sage: C = P.combinatorial_polyhedron()
            sage: chain = C.a_maximal_chain()
            sage: [face.ambient_V_indices() for face in chain]
            [(0, 1, 2)]

        Specify an index for the vertex of the chain::

            sage: P = polytopes.cube()
            sage: C = P.combinatorial_polyhedron()
            sage: [face.ambient_V_indices() for face in C.a_maximal_chain()]
            [(5,), (0, 5), (0, 3, 4, 5)]
            sage: [face.ambient_V_indices() for face in C.a_maximal_chain(Vindex=2)]
            [(2,), (2, 7), (2, 3, 4, 7)]

        Specify an index for the facet of the chain::

            sage: [face.ambient_H_indices() for face in C.a_maximal_chain()]
            [(3, 4, 5), (4, 5), (5,)]
            sage: [face.ambient_H_indices() for face in C.a_maximal_chain(Hindex=3)]
            [(3, 4, 5), (3, 4), (3,)]
            sage: [face.ambient_H_indices() for face in C.a_maximal_chain(Hindex=2)]
            [(2, 3, 5), (2, 3), (2,)]

        If the specified vertex is not contained in the specified facet an error is raised::

            sage: C.a_maximal_chain(Vindex=0, Hindex=3)
            Traceback (most recent call last):
            ...
            ValueError: the given Vindex is not compatible with the given Hindex

        An error is raised, if the specified index does not correspond to a facet::

            sage: C.a_maximal_chain(Hindex=40)
            Traceback (most recent call last):
            ...
            ValueError: the given Hindex does not correspond to a facet

        An error is raised, if the specified index does not correspond to a vertex::

            sage: C.a_maximal_chain(Vindex=40)
            Traceback (most recent call last):
            ...
            ValueError: the given Vindex does not correspond to a vertex

        ::

            sage: P = Polyhedron(rays=[[1,0,0],[0,0,1]], lines=[[0,1,0]])
            sage: C = P.combinatorial_polyhedron()
            sage: C.a_maximal_chain(Vindex=0)
            Traceback (most recent call last):
            ...
            ValueError: the given Vindex does not correspond to a vertex

        ::

            sage: P = Polyhedron(rays=[[1,0,0],[0,0,1]])
            sage: C = P.combinatorial_polyhedron()
            sage: C.a_maximal_chain(Vindex=0)
            [A 0-dimensional face of a 2-dimensional combinatorial polyhedron,
            A 1-dimensional face of a 2-dimensional combinatorial polyhedron]
            sage: C.a_maximal_chain(Vindex=1)
            Traceback (most recent call last):
            ...
            ValueError: the given Vindex does not correspond to a vertex"""
    @overload
    def a_maximal_chain(self, Vindex=...) -> Any:
        """CombinatorialPolyhedron.a_maximal_chain(self, Vindex=None, Hindex=None)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 2997)

        Return a maximal chain of the face lattice in increasing order
        without empty face and whole polyhedron/maximal face.

        INPUT:

        - ``Vindex`` -- integer (default: ``None``); prescribe the index of the vertex in the chain
        - ``Hindex`` -- integer (default: ``None``); prescribe the index of the facet in the chain

        Each face is given as
        :class:`~sage.geometry.polyhedron.combinatorial_polyhedron.combinatorial_face.CombinatorialFace`.

        EXAMPLES::

            sage: P = polytopes.cross_polytope(4)
            sage: C = P.combinatorial_polyhedron()
            sage: chain = C.a_maximal_chain(); chain
            [A 0-dimensional face of a 4-dimensional combinatorial polyhedron,
             A 1-dimensional face of a 4-dimensional combinatorial polyhedron,
             A 2-dimensional face of a 4-dimensional combinatorial polyhedron,
             A 3-dimensional face of a 4-dimensional combinatorial polyhedron]
            sage: [face.ambient_V_indices() for face in chain]
            [(7,), (6, 7), (5, 6, 7), (4, 5, 6, 7)]

            sage: P = polytopes.hypercube(4)
            sage: C = P.combinatorial_polyhedron()
            sage: chain = C.a_maximal_chain(); chain
            [A 0-dimensional face of a 4-dimensional combinatorial polyhedron,
             A 1-dimensional face of a 4-dimensional combinatorial polyhedron,
             A 2-dimensional face of a 4-dimensional combinatorial polyhedron,
             A 3-dimensional face of a 4-dimensional combinatorial polyhedron]
            sage: [face.ambient_V_indices() for face in chain]
            [(15,), (6, 15), (5, 6, 14, 15), (0, 5, 6, 7, 8, 9, 14, 15)]

            sage: # needs sage.combinat
            sage: P = polytopes.permutahedron(4)
            sage: C = P.combinatorial_polyhedron()
            sage: chain = C.a_maximal_chain(); chain
            [A 0-dimensional face of a 3-dimensional combinatorial polyhedron,
             A 1-dimensional face of a 3-dimensional combinatorial polyhedron,
             A 2-dimensional face of a 3-dimensional combinatorial polyhedron]
            sage: [face.ambient_V_indices() for face in chain]
            [(16,), (15, 16), (8, 9, 14, 15, 16, 17)]

            sage: P = Polyhedron(rays=[[1,0]], lines=[[0,1]])
            sage: C = P.combinatorial_polyhedron()
            sage: chain = C.a_maximal_chain()
            sage: [face.ambient_V_indices() for face in chain]
            [(0, 1)]

            sage: P = Polyhedron(rays=[[1,0,0],[0,0,1]], lines=[[0,1,0]])
            sage: C = P.combinatorial_polyhedron()
            sage: chain = C.a_maximal_chain()
            sage: [face.ambient_V_indices() for face in chain]
            [(0, 1), (0, 1, 3)]

            sage: P = Polyhedron(rays=[[1,0,0]], lines=[[0,1,0],[0,0,1]])
            sage: C = P.combinatorial_polyhedron()
            sage: chain = C.a_maximal_chain()
            sage: [face.ambient_V_indices() for face in chain]
            [(0, 1, 2)]

        Specify an index for the vertex of the chain::

            sage: P = polytopes.cube()
            sage: C = P.combinatorial_polyhedron()
            sage: [face.ambient_V_indices() for face in C.a_maximal_chain()]
            [(5,), (0, 5), (0, 3, 4, 5)]
            sage: [face.ambient_V_indices() for face in C.a_maximal_chain(Vindex=2)]
            [(2,), (2, 7), (2, 3, 4, 7)]

        Specify an index for the facet of the chain::

            sage: [face.ambient_H_indices() for face in C.a_maximal_chain()]
            [(3, 4, 5), (4, 5), (5,)]
            sage: [face.ambient_H_indices() for face in C.a_maximal_chain(Hindex=3)]
            [(3, 4, 5), (3, 4), (3,)]
            sage: [face.ambient_H_indices() for face in C.a_maximal_chain(Hindex=2)]
            [(2, 3, 5), (2, 3), (2,)]

        If the specified vertex is not contained in the specified facet an error is raised::

            sage: C.a_maximal_chain(Vindex=0, Hindex=3)
            Traceback (most recent call last):
            ...
            ValueError: the given Vindex is not compatible with the given Hindex

        An error is raised, if the specified index does not correspond to a facet::

            sage: C.a_maximal_chain(Hindex=40)
            Traceback (most recent call last):
            ...
            ValueError: the given Hindex does not correspond to a facet

        An error is raised, if the specified index does not correspond to a vertex::

            sage: C.a_maximal_chain(Vindex=40)
            Traceback (most recent call last):
            ...
            ValueError: the given Vindex does not correspond to a vertex

        ::

            sage: P = Polyhedron(rays=[[1,0,0],[0,0,1]], lines=[[0,1,0]])
            sage: C = P.combinatorial_polyhedron()
            sage: C.a_maximal_chain(Vindex=0)
            Traceback (most recent call last):
            ...
            ValueError: the given Vindex does not correspond to a vertex

        ::

            sage: P = Polyhedron(rays=[[1,0,0],[0,0,1]])
            sage: C = P.combinatorial_polyhedron()
            sage: C.a_maximal_chain(Vindex=0)
            [A 0-dimensional face of a 2-dimensional combinatorial polyhedron,
            A 1-dimensional face of a 2-dimensional combinatorial polyhedron]
            sage: C.a_maximal_chain(Vindex=1)
            Traceback (most recent call last):
            ...
            ValueError: the given Vindex does not correspond to a vertex"""
    @overload
    def a_maximal_chain(self) -> Any:
        """CombinatorialPolyhedron.a_maximal_chain(self, Vindex=None, Hindex=None)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 2997)

        Return a maximal chain of the face lattice in increasing order
        without empty face and whole polyhedron/maximal face.

        INPUT:

        - ``Vindex`` -- integer (default: ``None``); prescribe the index of the vertex in the chain
        - ``Hindex`` -- integer (default: ``None``); prescribe the index of the facet in the chain

        Each face is given as
        :class:`~sage.geometry.polyhedron.combinatorial_polyhedron.combinatorial_face.CombinatorialFace`.

        EXAMPLES::

            sage: P = polytopes.cross_polytope(4)
            sage: C = P.combinatorial_polyhedron()
            sage: chain = C.a_maximal_chain(); chain
            [A 0-dimensional face of a 4-dimensional combinatorial polyhedron,
             A 1-dimensional face of a 4-dimensional combinatorial polyhedron,
             A 2-dimensional face of a 4-dimensional combinatorial polyhedron,
             A 3-dimensional face of a 4-dimensional combinatorial polyhedron]
            sage: [face.ambient_V_indices() for face in chain]
            [(7,), (6, 7), (5, 6, 7), (4, 5, 6, 7)]

            sage: P = polytopes.hypercube(4)
            sage: C = P.combinatorial_polyhedron()
            sage: chain = C.a_maximal_chain(); chain
            [A 0-dimensional face of a 4-dimensional combinatorial polyhedron,
             A 1-dimensional face of a 4-dimensional combinatorial polyhedron,
             A 2-dimensional face of a 4-dimensional combinatorial polyhedron,
             A 3-dimensional face of a 4-dimensional combinatorial polyhedron]
            sage: [face.ambient_V_indices() for face in chain]
            [(15,), (6, 15), (5, 6, 14, 15), (0, 5, 6, 7, 8, 9, 14, 15)]

            sage: # needs sage.combinat
            sage: P = polytopes.permutahedron(4)
            sage: C = P.combinatorial_polyhedron()
            sage: chain = C.a_maximal_chain(); chain
            [A 0-dimensional face of a 3-dimensional combinatorial polyhedron,
             A 1-dimensional face of a 3-dimensional combinatorial polyhedron,
             A 2-dimensional face of a 3-dimensional combinatorial polyhedron]
            sage: [face.ambient_V_indices() for face in chain]
            [(16,), (15, 16), (8, 9, 14, 15, 16, 17)]

            sage: P = Polyhedron(rays=[[1,0]], lines=[[0,1]])
            sage: C = P.combinatorial_polyhedron()
            sage: chain = C.a_maximal_chain()
            sage: [face.ambient_V_indices() for face in chain]
            [(0, 1)]

            sage: P = Polyhedron(rays=[[1,0,0],[0,0,1]], lines=[[0,1,0]])
            sage: C = P.combinatorial_polyhedron()
            sage: chain = C.a_maximal_chain()
            sage: [face.ambient_V_indices() for face in chain]
            [(0, 1), (0, 1, 3)]

            sage: P = Polyhedron(rays=[[1,0,0]], lines=[[0,1,0],[0,0,1]])
            sage: C = P.combinatorial_polyhedron()
            sage: chain = C.a_maximal_chain()
            sage: [face.ambient_V_indices() for face in chain]
            [(0, 1, 2)]

        Specify an index for the vertex of the chain::

            sage: P = polytopes.cube()
            sage: C = P.combinatorial_polyhedron()
            sage: [face.ambient_V_indices() for face in C.a_maximal_chain()]
            [(5,), (0, 5), (0, 3, 4, 5)]
            sage: [face.ambient_V_indices() for face in C.a_maximal_chain(Vindex=2)]
            [(2,), (2, 7), (2, 3, 4, 7)]

        Specify an index for the facet of the chain::

            sage: [face.ambient_H_indices() for face in C.a_maximal_chain()]
            [(3, 4, 5), (4, 5), (5,)]
            sage: [face.ambient_H_indices() for face in C.a_maximal_chain(Hindex=3)]
            [(3, 4, 5), (3, 4), (3,)]
            sage: [face.ambient_H_indices() for face in C.a_maximal_chain(Hindex=2)]
            [(2, 3, 5), (2, 3), (2,)]

        If the specified vertex is not contained in the specified facet an error is raised::

            sage: C.a_maximal_chain(Vindex=0, Hindex=3)
            Traceback (most recent call last):
            ...
            ValueError: the given Vindex is not compatible with the given Hindex

        An error is raised, if the specified index does not correspond to a facet::

            sage: C.a_maximal_chain(Hindex=40)
            Traceback (most recent call last):
            ...
            ValueError: the given Hindex does not correspond to a facet

        An error is raised, if the specified index does not correspond to a vertex::

            sage: C.a_maximal_chain(Vindex=40)
            Traceback (most recent call last):
            ...
            ValueError: the given Vindex does not correspond to a vertex

        ::

            sage: P = Polyhedron(rays=[[1,0,0],[0,0,1]], lines=[[0,1,0]])
            sage: C = P.combinatorial_polyhedron()
            sage: C.a_maximal_chain(Vindex=0)
            Traceback (most recent call last):
            ...
            ValueError: the given Vindex does not correspond to a vertex

        ::

            sage: P = Polyhedron(rays=[[1,0,0],[0,0,1]])
            sage: C = P.combinatorial_polyhedron()
            sage: C.a_maximal_chain(Vindex=0)
            [A 0-dimensional face of a 2-dimensional combinatorial polyhedron,
            A 1-dimensional face of a 2-dimensional combinatorial polyhedron]
            sage: C.a_maximal_chain(Vindex=1)
            Traceback (most recent call last):
            ...
            ValueError: the given Vindex does not correspond to a vertex"""
    @overload
    def a_maximal_chain(self, Hindex=...) -> Any:
        """CombinatorialPolyhedron.a_maximal_chain(self, Vindex=None, Hindex=None)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 2997)

        Return a maximal chain of the face lattice in increasing order
        without empty face and whole polyhedron/maximal face.

        INPUT:

        - ``Vindex`` -- integer (default: ``None``); prescribe the index of the vertex in the chain
        - ``Hindex`` -- integer (default: ``None``); prescribe the index of the facet in the chain

        Each face is given as
        :class:`~sage.geometry.polyhedron.combinatorial_polyhedron.combinatorial_face.CombinatorialFace`.

        EXAMPLES::

            sage: P = polytopes.cross_polytope(4)
            sage: C = P.combinatorial_polyhedron()
            sage: chain = C.a_maximal_chain(); chain
            [A 0-dimensional face of a 4-dimensional combinatorial polyhedron,
             A 1-dimensional face of a 4-dimensional combinatorial polyhedron,
             A 2-dimensional face of a 4-dimensional combinatorial polyhedron,
             A 3-dimensional face of a 4-dimensional combinatorial polyhedron]
            sage: [face.ambient_V_indices() for face in chain]
            [(7,), (6, 7), (5, 6, 7), (4, 5, 6, 7)]

            sage: P = polytopes.hypercube(4)
            sage: C = P.combinatorial_polyhedron()
            sage: chain = C.a_maximal_chain(); chain
            [A 0-dimensional face of a 4-dimensional combinatorial polyhedron,
             A 1-dimensional face of a 4-dimensional combinatorial polyhedron,
             A 2-dimensional face of a 4-dimensional combinatorial polyhedron,
             A 3-dimensional face of a 4-dimensional combinatorial polyhedron]
            sage: [face.ambient_V_indices() for face in chain]
            [(15,), (6, 15), (5, 6, 14, 15), (0, 5, 6, 7, 8, 9, 14, 15)]

            sage: # needs sage.combinat
            sage: P = polytopes.permutahedron(4)
            sage: C = P.combinatorial_polyhedron()
            sage: chain = C.a_maximal_chain(); chain
            [A 0-dimensional face of a 3-dimensional combinatorial polyhedron,
             A 1-dimensional face of a 3-dimensional combinatorial polyhedron,
             A 2-dimensional face of a 3-dimensional combinatorial polyhedron]
            sage: [face.ambient_V_indices() for face in chain]
            [(16,), (15, 16), (8, 9, 14, 15, 16, 17)]

            sage: P = Polyhedron(rays=[[1,0]], lines=[[0,1]])
            sage: C = P.combinatorial_polyhedron()
            sage: chain = C.a_maximal_chain()
            sage: [face.ambient_V_indices() for face in chain]
            [(0, 1)]

            sage: P = Polyhedron(rays=[[1,0,0],[0,0,1]], lines=[[0,1,0]])
            sage: C = P.combinatorial_polyhedron()
            sage: chain = C.a_maximal_chain()
            sage: [face.ambient_V_indices() for face in chain]
            [(0, 1), (0, 1, 3)]

            sage: P = Polyhedron(rays=[[1,0,0]], lines=[[0,1,0],[0,0,1]])
            sage: C = P.combinatorial_polyhedron()
            sage: chain = C.a_maximal_chain()
            sage: [face.ambient_V_indices() for face in chain]
            [(0, 1, 2)]

        Specify an index for the vertex of the chain::

            sage: P = polytopes.cube()
            sage: C = P.combinatorial_polyhedron()
            sage: [face.ambient_V_indices() for face in C.a_maximal_chain()]
            [(5,), (0, 5), (0, 3, 4, 5)]
            sage: [face.ambient_V_indices() for face in C.a_maximal_chain(Vindex=2)]
            [(2,), (2, 7), (2, 3, 4, 7)]

        Specify an index for the facet of the chain::

            sage: [face.ambient_H_indices() for face in C.a_maximal_chain()]
            [(3, 4, 5), (4, 5), (5,)]
            sage: [face.ambient_H_indices() for face in C.a_maximal_chain(Hindex=3)]
            [(3, 4, 5), (3, 4), (3,)]
            sage: [face.ambient_H_indices() for face in C.a_maximal_chain(Hindex=2)]
            [(2, 3, 5), (2, 3), (2,)]

        If the specified vertex is not contained in the specified facet an error is raised::

            sage: C.a_maximal_chain(Vindex=0, Hindex=3)
            Traceback (most recent call last):
            ...
            ValueError: the given Vindex is not compatible with the given Hindex

        An error is raised, if the specified index does not correspond to a facet::

            sage: C.a_maximal_chain(Hindex=40)
            Traceback (most recent call last):
            ...
            ValueError: the given Hindex does not correspond to a facet

        An error is raised, if the specified index does not correspond to a vertex::

            sage: C.a_maximal_chain(Vindex=40)
            Traceback (most recent call last):
            ...
            ValueError: the given Vindex does not correspond to a vertex

        ::

            sage: P = Polyhedron(rays=[[1,0,0],[0,0,1]], lines=[[0,1,0]])
            sage: C = P.combinatorial_polyhedron()
            sage: C.a_maximal_chain(Vindex=0)
            Traceback (most recent call last):
            ...
            ValueError: the given Vindex does not correspond to a vertex

        ::

            sage: P = Polyhedron(rays=[[1,0,0],[0,0,1]])
            sage: C = P.combinatorial_polyhedron()
            sage: C.a_maximal_chain(Vindex=0)
            [A 0-dimensional face of a 2-dimensional combinatorial polyhedron,
            A 1-dimensional face of a 2-dimensional combinatorial polyhedron]
            sage: C.a_maximal_chain(Vindex=1)
            Traceback (most recent call last):
            ...
            ValueError: the given Vindex does not correspond to a vertex"""
    @overload
    def a_maximal_chain(self, Hindex=...) -> Any:
        """CombinatorialPolyhedron.a_maximal_chain(self, Vindex=None, Hindex=None)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 2997)

        Return a maximal chain of the face lattice in increasing order
        without empty face and whole polyhedron/maximal face.

        INPUT:

        - ``Vindex`` -- integer (default: ``None``); prescribe the index of the vertex in the chain
        - ``Hindex`` -- integer (default: ``None``); prescribe the index of the facet in the chain

        Each face is given as
        :class:`~sage.geometry.polyhedron.combinatorial_polyhedron.combinatorial_face.CombinatorialFace`.

        EXAMPLES::

            sage: P = polytopes.cross_polytope(4)
            sage: C = P.combinatorial_polyhedron()
            sage: chain = C.a_maximal_chain(); chain
            [A 0-dimensional face of a 4-dimensional combinatorial polyhedron,
             A 1-dimensional face of a 4-dimensional combinatorial polyhedron,
             A 2-dimensional face of a 4-dimensional combinatorial polyhedron,
             A 3-dimensional face of a 4-dimensional combinatorial polyhedron]
            sage: [face.ambient_V_indices() for face in chain]
            [(7,), (6, 7), (5, 6, 7), (4, 5, 6, 7)]

            sage: P = polytopes.hypercube(4)
            sage: C = P.combinatorial_polyhedron()
            sage: chain = C.a_maximal_chain(); chain
            [A 0-dimensional face of a 4-dimensional combinatorial polyhedron,
             A 1-dimensional face of a 4-dimensional combinatorial polyhedron,
             A 2-dimensional face of a 4-dimensional combinatorial polyhedron,
             A 3-dimensional face of a 4-dimensional combinatorial polyhedron]
            sage: [face.ambient_V_indices() for face in chain]
            [(15,), (6, 15), (5, 6, 14, 15), (0, 5, 6, 7, 8, 9, 14, 15)]

            sage: # needs sage.combinat
            sage: P = polytopes.permutahedron(4)
            sage: C = P.combinatorial_polyhedron()
            sage: chain = C.a_maximal_chain(); chain
            [A 0-dimensional face of a 3-dimensional combinatorial polyhedron,
             A 1-dimensional face of a 3-dimensional combinatorial polyhedron,
             A 2-dimensional face of a 3-dimensional combinatorial polyhedron]
            sage: [face.ambient_V_indices() for face in chain]
            [(16,), (15, 16), (8, 9, 14, 15, 16, 17)]

            sage: P = Polyhedron(rays=[[1,0]], lines=[[0,1]])
            sage: C = P.combinatorial_polyhedron()
            sage: chain = C.a_maximal_chain()
            sage: [face.ambient_V_indices() for face in chain]
            [(0, 1)]

            sage: P = Polyhedron(rays=[[1,0,0],[0,0,1]], lines=[[0,1,0]])
            sage: C = P.combinatorial_polyhedron()
            sage: chain = C.a_maximal_chain()
            sage: [face.ambient_V_indices() for face in chain]
            [(0, 1), (0, 1, 3)]

            sage: P = Polyhedron(rays=[[1,0,0]], lines=[[0,1,0],[0,0,1]])
            sage: C = P.combinatorial_polyhedron()
            sage: chain = C.a_maximal_chain()
            sage: [face.ambient_V_indices() for face in chain]
            [(0, 1, 2)]

        Specify an index for the vertex of the chain::

            sage: P = polytopes.cube()
            sage: C = P.combinatorial_polyhedron()
            sage: [face.ambient_V_indices() for face in C.a_maximal_chain()]
            [(5,), (0, 5), (0, 3, 4, 5)]
            sage: [face.ambient_V_indices() for face in C.a_maximal_chain(Vindex=2)]
            [(2,), (2, 7), (2, 3, 4, 7)]

        Specify an index for the facet of the chain::

            sage: [face.ambient_H_indices() for face in C.a_maximal_chain()]
            [(3, 4, 5), (4, 5), (5,)]
            sage: [face.ambient_H_indices() for face in C.a_maximal_chain(Hindex=3)]
            [(3, 4, 5), (3, 4), (3,)]
            sage: [face.ambient_H_indices() for face in C.a_maximal_chain(Hindex=2)]
            [(2, 3, 5), (2, 3), (2,)]

        If the specified vertex is not contained in the specified facet an error is raised::

            sage: C.a_maximal_chain(Vindex=0, Hindex=3)
            Traceback (most recent call last):
            ...
            ValueError: the given Vindex is not compatible with the given Hindex

        An error is raised, if the specified index does not correspond to a facet::

            sage: C.a_maximal_chain(Hindex=40)
            Traceback (most recent call last):
            ...
            ValueError: the given Hindex does not correspond to a facet

        An error is raised, if the specified index does not correspond to a vertex::

            sage: C.a_maximal_chain(Vindex=40)
            Traceback (most recent call last):
            ...
            ValueError: the given Vindex does not correspond to a vertex

        ::

            sage: P = Polyhedron(rays=[[1,0,0],[0,0,1]], lines=[[0,1,0]])
            sage: C = P.combinatorial_polyhedron()
            sage: C.a_maximal_chain(Vindex=0)
            Traceback (most recent call last):
            ...
            ValueError: the given Vindex does not correspond to a vertex

        ::

            sage: P = Polyhedron(rays=[[1,0,0],[0,0,1]])
            sage: C = P.combinatorial_polyhedron()
            sage: C.a_maximal_chain(Vindex=0)
            [A 0-dimensional face of a 2-dimensional combinatorial polyhedron,
            A 1-dimensional face of a 2-dimensional combinatorial polyhedron]
            sage: C.a_maximal_chain(Vindex=1)
            Traceback (most recent call last):
            ...
            ValueError: the given Vindex does not correspond to a vertex"""
    @overload
    def a_maximal_chain(self, Vindex=..., Hindex=...) -> Any:
        """CombinatorialPolyhedron.a_maximal_chain(self, Vindex=None, Hindex=None)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 2997)

        Return a maximal chain of the face lattice in increasing order
        without empty face and whole polyhedron/maximal face.

        INPUT:

        - ``Vindex`` -- integer (default: ``None``); prescribe the index of the vertex in the chain
        - ``Hindex`` -- integer (default: ``None``); prescribe the index of the facet in the chain

        Each face is given as
        :class:`~sage.geometry.polyhedron.combinatorial_polyhedron.combinatorial_face.CombinatorialFace`.

        EXAMPLES::

            sage: P = polytopes.cross_polytope(4)
            sage: C = P.combinatorial_polyhedron()
            sage: chain = C.a_maximal_chain(); chain
            [A 0-dimensional face of a 4-dimensional combinatorial polyhedron,
             A 1-dimensional face of a 4-dimensional combinatorial polyhedron,
             A 2-dimensional face of a 4-dimensional combinatorial polyhedron,
             A 3-dimensional face of a 4-dimensional combinatorial polyhedron]
            sage: [face.ambient_V_indices() for face in chain]
            [(7,), (6, 7), (5, 6, 7), (4, 5, 6, 7)]

            sage: P = polytopes.hypercube(4)
            sage: C = P.combinatorial_polyhedron()
            sage: chain = C.a_maximal_chain(); chain
            [A 0-dimensional face of a 4-dimensional combinatorial polyhedron,
             A 1-dimensional face of a 4-dimensional combinatorial polyhedron,
             A 2-dimensional face of a 4-dimensional combinatorial polyhedron,
             A 3-dimensional face of a 4-dimensional combinatorial polyhedron]
            sage: [face.ambient_V_indices() for face in chain]
            [(15,), (6, 15), (5, 6, 14, 15), (0, 5, 6, 7, 8, 9, 14, 15)]

            sage: # needs sage.combinat
            sage: P = polytopes.permutahedron(4)
            sage: C = P.combinatorial_polyhedron()
            sage: chain = C.a_maximal_chain(); chain
            [A 0-dimensional face of a 3-dimensional combinatorial polyhedron,
             A 1-dimensional face of a 3-dimensional combinatorial polyhedron,
             A 2-dimensional face of a 3-dimensional combinatorial polyhedron]
            sage: [face.ambient_V_indices() for face in chain]
            [(16,), (15, 16), (8, 9, 14, 15, 16, 17)]

            sage: P = Polyhedron(rays=[[1,0]], lines=[[0,1]])
            sage: C = P.combinatorial_polyhedron()
            sage: chain = C.a_maximal_chain()
            sage: [face.ambient_V_indices() for face in chain]
            [(0, 1)]

            sage: P = Polyhedron(rays=[[1,0,0],[0,0,1]], lines=[[0,1,0]])
            sage: C = P.combinatorial_polyhedron()
            sage: chain = C.a_maximal_chain()
            sage: [face.ambient_V_indices() for face in chain]
            [(0, 1), (0, 1, 3)]

            sage: P = Polyhedron(rays=[[1,0,0]], lines=[[0,1,0],[0,0,1]])
            sage: C = P.combinatorial_polyhedron()
            sage: chain = C.a_maximal_chain()
            sage: [face.ambient_V_indices() for face in chain]
            [(0, 1, 2)]

        Specify an index for the vertex of the chain::

            sage: P = polytopes.cube()
            sage: C = P.combinatorial_polyhedron()
            sage: [face.ambient_V_indices() for face in C.a_maximal_chain()]
            [(5,), (0, 5), (0, 3, 4, 5)]
            sage: [face.ambient_V_indices() for face in C.a_maximal_chain(Vindex=2)]
            [(2,), (2, 7), (2, 3, 4, 7)]

        Specify an index for the facet of the chain::

            sage: [face.ambient_H_indices() for face in C.a_maximal_chain()]
            [(3, 4, 5), (4, 5), (5,)]
            sage: [face.ambient_H_indices() for face in C.a_maximal_chain(Hindex=3)]
            [(3, 4, 5), (3, 4), (3,)]
            sage: [face.ambient_H_indices() for face in C.a_maximal_chain(Hindex=2)]
            [(2, 3, 5), (2, 3), (2,)]

        If the specified vertex is not contained in the specified facet an error is raised::

            sage: C.a_maximal_chain(Vindex=0, Hindex=3)
            Traceback (most recent call last):
            ...
            ValueError: the given Vindex is not compatible with the given Hindex

        An error is raised, if the specified index does not correspond to a facet::

            sage: C.a_maximal_chain(Hindex=40)
            Traceback (most recent call last):
            ...
            ValueError: the given Hindex does not correspond to a facet

        An error is raised, if the specified index does not correspond to a vertex::

            sage: C.a_maximal_chain(Vindex=40)
            Traceback (most recent call last):
            ...
            ValueError: the given Vindex does not correspond to a vertex

        ::

            sage: P = Polyhedron(rays=[[1,0,0],[0,0,1]], lines=[[0,1,0]])
            sage: C = P.combinatorial_polyhedron()
            sage: C.a_maximal_chain(Vindex=0)
            Traceback (most recent call last):
            ...
            ValueError: the given Vindex does not correspond to a vertex

        ::

            sage: P = Polyhedron(rays=[[1,0,0],[0,0,1]])
            sage: C = P.combinatorial_polyhedron()
            sage: C.a_maximal_chain(Vindex=0)
            [A 0-dimensional face of a 2-dimensional combinatorial polyhedron,
            A 1-dimensional face of a 2-dimensional combinatorial polyhedron]
            sage: C.a_maximal_chain(Vindex=1)
            Traceback (most recent call last):
            ...
            ValueError: the given Vindex does not correspond to a vertex"""
    @overload
    def a_maximal_chain(self, Hindex=...) -> Any:
        """CombinatorialPolyhedron.a_maximal_chain(self, Vindex=None, Hindex=None)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 2997)

        Return a maximal chain of the face lattice in increasing order
        without empty face and whole polyhedron/maximal face.

        INPUT:

        - ``Vindex`` -- integer (default: ``None``); prescribe the index of the vertex in the chain
        - ``Hindex`` -- integer (default: ``None``); prescribe the index of the facet in the chain

        Each face is given as
        :class:`~sage.geometry.polyhedron.combinatorial_polyhedron.combinatorial_face.CombinatorialFace`.

        EXAMPLES::

            sage: P = polytopes.cross_polytope(4)
            sage: C = P.combinatorial_polyhedron()
            sage: chain = C.a_maximal_chain(); chain
            [A 0-dimensional face of a 4-dimensional combinatorial polyhedron,
             A 1-dimensional face of a 4-dimensional combinatorial polyhedron,
             A 2-dimensional face of a 4-dimensional combinatorial polyhedron,
             A 3-dimensional face of a 4-dimensional combinatorial polyhedron]
            sage: [face.ambient_V_indices() for face in chain]
            [(7,), (6, 7), (5, 6, 7), (4, 5, 6, 7)]

            sage: P = polytopes.hypercube(4)
            sage: C = P.combinatorial_polyhedron()
            sage: chain = C.a_maximal_chain(); chain
            [A 0-dimensional face of a 4-dimensional combinatorial polyhedron,
             A 1-dimensional face of a 4-dimensional combinatorial polyhedron,
             A 2-dimensional face of a 4-dimensional combinatorial polyhedron,
             A 3-dimensional face of a 4-dimensional combinatorial polyhedron]
            sage: [face.ambient_V_indices() for face in chain]
            [(15,), (6, 15), (5, 6, 14, 15), (0, 5, 6, 7, 8, 9, 14, 15)]

            sage: # needs sage.combinat
            sage: P = polytopes.permutahedron(4)
            sage: C = P.combinatorial_polyhedron()
            sage: chain = C.a_maximal_chain(); chain
            [A 0-dimensional face of a 3-dimensional combinatorial polyhedron,
             A 1-dimensional face of a 3-dimensional combinatorial polyhedron,
             A 2-dimensional face of a 3-dimensional combinatorial polyhedron]
            sage: [face.ambient_V_indices() for face in chain]
            [(16,), (15, 16), (8, 9, 14, 15, 16, 17)]

            sage: P = Polyhedron(rays=[[1,0]], lines=[[0,1]])
            sage: C = P.combinatorial_polyhedron()
            sage: chain = C.a_maximal_chain()
            sage: [face.ambient_V_indices() for face in chain]
            [(0, 1)]

            sage: P = Polyhedron(rays=[[1,0,0],[0,0,1]], lines=[[0,1,0]])
            sage: C = P.combinatorial_polyhedron()
            sage: chain = C.a_maximal_chain()
            sage: [face.ambient_V_indices() for face in chain]
            [(0, 1), (0, 1, 3)]

            sage: P = Polyhedron(rays=[[1,0,0]], lines=[[0,1,0],[0,0,1]])
            sage: C = P.combinatorial_polyhedron()
            sage: chain = C.a_maximal_chain()
            sage: [face.ambient_V_indices() for face in chain]
            [(0, 1, 2)]

        Specify an index for the vertex of the chain::

            sage: P = polytopes.cube()
            sage: C = P.combinatorial_polyhedron()
            sage: [face.ambient_V_indices() for face in C.a_maximal_chain()]
            [(5,), (0, 5), (0, 3, 4, 5)]
            sage: [face.ambient_V_indices() for face in C.a_maximal_chain(Vindex=2)]
            [(2,), (2, 7), (2, 3, 4, 7)]

        Specify an index for the facet of the chain::

            sage: [face.ambient_H_indices() for face in C.a_maximal_chain()]
            [(3, 4, 5), (4, 5), (5,)]
            sage: [face.ambient_H_indices() for face in C.a_maximal_chain(Hindex=3)]
            [(3, 4, 5), (3, 4), (3,)]
            sage: [face.ambient_H_indices() for face in C.a_maximal_chain(Hindex=2)]
            [(2, 3, 5), (2, 3), (2,)]

        If the specified vertex is not contained in the specified facet an error is raised::

            sage: C.a_maximal_chain(Vindex=0, Hindex=3)
            Traceback (most recent call last):
            ...
            ValueError: the given Vindex is not compatible with the given Hindex

        An error is raised, if the specified index does not correspond to a facet::

            sage: C.a_maximal_chain(Hindex=40)
            Traceback (most recent call last):
            ...
            ValueError: the given Hindex does not correspond to a facet

        An error is raised, if the specified index does not correspond to a vertex::

            sage: C.a_maximal_chain(Vindex=40)
            Traceback (most recent call last):
            ...
            ValueError: the given Vindex does not correspond to a vertex

        ::

            sage: P = Polyhedron(rays=[[1,0,0],[0,0,1]], lines=[[0,1,0]])
            sage: C = P.combinatorial_polyhedron()
            sage: C.a_maximal_chain(Vindex=0)
            Traceback (most recent call last):
            ...
            ValueError: the given Vindex does not correspond to a vertex

        ::

            sage: P = Polyhedron(rays=[[1,0,0],[0,0,1]])
            sage: C = P.combinatorial_polyhedron()
            sage: C.a_maximal_chain(Vindex=0)
            [A 0-dimensional face of a 2-dimensional combinatorial polyhedron,
            A 1-dimensional face of a 2-dimensional combinatorial polyhedron]
            sage: C.a_maximal_chain(Vindex=1)
            Traceback (most recent call last):
            ...
            ValueError: the given Vindex does not correspond to a vertex"""
    @overload
    def a_maximal_chain(self, Vindex=...) -> Any:
        """CombinatorialPolyhedron.a_maximal_chain(self, Vindex=None, Hindex=None)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 2997)

        Return a maximal chain of the face lattice in increasing order
        without empty face and whole polyhedron/maximal face.

        INPUT:

        - ``Vindex`` -- integer (default: ``None``); prescribe the index of the vertex in the chain
        - ``Hindex`` -- integer (default: ``None``); prescribe the index of the facet in the chain

        Each face is given as
        :class:`~sage.geometry.polyhedron.combinatorial_polyhedron.combinatorial_face.CombinatorialFace`.

        EXAMPLES::

            sage: P = polytopes.cross_polytope(4)
            sage: C = P.combinatorial_polyhedron()
            sage: chain = C.a_maximal_chain(); chain
            [A 0-dimensional face of a 4-dimensional combinatorial polyhedron,
             A 1-dimensional face of a 4-dimensional combinatorial polyhedron,
             A 2-dimensional face of a 4-dimensional combinatorial polyhedron,
             A 3-dimensional face of a 4-dimensional combinatorial polyhedron]
            sage: [face.ambient_V_indices() for face in chain]
            [(7,), (6, 7), (5, 6, 7), (4, 5, 6, 7)]

            sage: P = polytopes.hypercube(4)
            sage: C = P.combinatorial_polyhedron()
            sage: chain = C.a_maximal_chain(); chain
            [A 0-dimensional face of a 4-dimensional combinatorial polyhedron,
             A 1-dimensional face of a 4-dimensional combinatorial polyhedron,
             A 2-dimensional face of a 4-dimensional combinatorial polyhedron,
             A 3-dimensional face of a 4-dimensional combinatorial polyhedron]
            sage: [face.ambient_V_indices() for face in chain]
            [(15,), (6, 15), (5, 6, 14, 15), (0, 5, 6, 7, 8, 9, 14, 15)]

            sage: # needs sage.combinat
            sage: P = polytopes.permutahedron(4)
            sage: C = P.combinatorial_polyhedron()
            sage: chain = C.a_maximal_chain(); chain
            [A 0-dimensional face of a 3-dimensional combinatorial polyhedron,
             A 1-dimensional face of a 3-dimensional combinatorial polyhedron,
             A 2-dimensional face of a 3-dimensional combinatorial polyhedron]
            sage: [face.ambient_V_indices() for face in chain]
            [(16,), (15, 16), (8, 9, 14, 15, 16, 17)]

            sage: P = Polyhedron(rays=[[1,0]], lines=[[0,1]])
            sage: C = P.combinatorial_polyhedron()
            sage: chain = C.a_maximal_chain()
            sage: [face.ambient_V_indices() for face in chain]
            [(0, 1)]

            sage: P = Polyhedron(rays=[[1,0,0],[0,0,1]], lines=[[0,1,0]])
            sage: C = P.combinatorial_polyhedron()
            sage: chain = C.a_maximal_chain()
            sage: [face.ambient_V_indices() for face in chain]
            [(0, 1), (0, 1, 3)]

            sage: P = Polyhedron(rays=[[1,0,0]], lines=[[0,1,0],[0,0,1]])
            sage: C = P.combinatorial_polyhedron()
            sage: chain = C.a_maximal_chain()
            sage: [face.ambient_V_indices() for face in chain]
            [(0, 1, 2)]

        Specify an index for the vertex of the chain::

            sage: P = polytopes.cube()
            sage: C = P.combinatorial_polyhedron()
            sage: [face.ambient_V_indices() for face in C.a_maximal_chain()]
            [(5,), (0, 5), (0, 3, 4, 5)]
            sage: [face.ambient_V_indices() for face in C.a_maximal_chain(Vindex=2)]
            [(2,), (2, 7), (2, 3, 4, 7)]

        Specify an index for the facet of the chain::

            sage: [face.ambient_H_indices() for face in C.a_maximal_chain()]
            [(3, 4, 5), (4, 5), (5,)]
            sage: [face.ambient_H_indices() for face in C.a_maximal_chain(Hindex=3)]
            [(3, 4, 5), (3, 4), (3,)]
            sage: [face.ambient_H_indices() for face in C.a_maximal_chain(Hindex=2)]
            [(2, 3, 5), (2, 3), (2,)]

        If the specified vertex is not contained in the specified facet an error is raised::

            sage: C.a_maximal_chain(Vindex=0, Hindex=3)
            Traceback (most recent call last):
            ...
            ValueError: the given Vindex is not compatible with the given Hindex

        An error is raised, if the specified index does not correspond to a facet::

            sage: C.a_maximal_chain(Hindex=40)
            Traceback (most recent call last):
            ...
            ValueError: the given Hindex does not correspond to a facet

        An error is raised, if the specified index does not correspond to a vertex::

            sage: C.a_maximal_chain(Vindex=40)
            Traceback (most recent call last):
            ...
            ValueError: the given Vindex does not correspond to a vertex

        ::

            sage: P = Polyhedron(rays=[[1,0,0],[0,0,1]], lines=[[0,1,0]])
            sage: C = P.combinatorial_polyhedron()
            sage: C.a_maximal_chain(Vindex=0)
            Traceback (most recent call last):
            ...
            ValueError: the given Vindex does not correspond to a vertex

        ::

            sage: P = Polyhedron(rays=[[1,0,0],[0,0,1]])
            sage: C = P.combinatorial_polyhedron()
            sage: C.a_maximal_chain(Vindex=0)
            [A 0-dimensional face of a 2-dimensional combinatorial polyhedron,
            A 1-dimensional face of a 2-dimensional combinatorial polyhedron]
            sage: C.a_maximal_chain(Vindex=1)
            Traceback (most recent call last):
            ...
            ValueError: the given Vindex does not correspond to a vertex"""
    @overload
    def a_maximal_chain(self, Vindex=...) -> Any:
        """CombinatorialPolyhedron.a_maximal_chain(self, Vindex=None, Hindex=None)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 2997)

        Return a maximal chain of the face lattice in increasing order
        without empty face and whole polyhedron/maximal face.

        INPUT:

        - ``Vindex`` -- integer (default: ``None``); prescribe the index of the vertex in the chain
        - ``Hindex`` -- integer (default: ``None``); prescribe the index of the facet in the chain

        Each face is given as
        :class:`~sage.geometry.polyhedron.combinatorial_polyhedron.combinatorial_face.CombinatorialFace`.

        EXAMPLES::

            sage: P = polytopes.cross_polytope(4)
            sage: C = P.combinatorial_polyhedron()
            sage: chain = C.a_maximal_chain(); chain
            [A 0-dimensional face of a 4-dimensional combinatorial polyhedron,
             A 1-dimensional face of a 4-dimensional combinatorial polyhedron,
             A 2-dimensional face of a 4-dimensional combinatorial polyhedron,
             A 3-dimensional face of a 4-dimensional combinatorial polyhedron]
            sage: [face.ambient_V_indices() for face in chain]
            [(7,), (6, 7), (5, 6, 7), (4, 5, 6, 7)]

            sage: P = polytopes.hypercube(4)
            sage: C = P.combinatorial_polyhedron()
            sage: chain = C.a_maximal_chain(); chain
            [A 0-dimensional face of a 4-dimensional combinatorial polyhedron,
             A 1-dimensional face of a 4-dimensional combinatorial polyhedron,
             A 2-dimensional face of a 4-dimensional combinatorial polyhedron,
             A 3-dimensional face of a 4-dimensional combinatorial polyhedron]
            sage: [face.ambient_V_indices() for face in chain]
            [(15,), (6, 15), (5, 6, 14, 15), (0, 5, 6, 7, 8, 9, 14, 15)]

            sage: # needs sage.combinat
            sage: P = polytopes.permutahedron(4)
            sage: C = P.combinatorial_polyhedron()
            sage: chain = C.a_maximal_chain(); chain
            [A 0-dimensional face of a 3-dimensional combinatorial polyhedron,
             A 1-dimensional face of a 3-dimensional combinatorial polyhedron,
             A 2-dimensional face of a 3-dimensional combinatorial polyhedron]
            sage: [face.ambient_V_indices() for face in chain]
            [(16,), (15, 16), (8, 9, 14, 15, 16, 17)]

            sage: P = Polyhedron(rays=[[1,0]], lines=[[0,1]])
            sage: C = P.combinatorial_polyhedron()
            sage: chain = C.a_maximal_chain()
            sage: [face.ambient_V_indices() for face in chain]
            [(0, 1)]

            sage: P = Polyhedron(rays=[[1,0,0],[0,0,1]], lines=[[0,1,0]])
            sage: C = P.combinatorial_polyhedron()
            sage: chain = C.a_maximal_chain()
            sage: [face.ambient_V_indices() for face in chain]
            [(0, 1), (0, 1, 3)]

            sage: P = Polyhedron(rays=[[1,0,0]], lines=[[0,1,0],[0,0,1]])
            sage: C = P.combinatorial_polyhedron()
            sage: chain = C.a_maximal_chain()
            sage: [face.ambient_V_indices() for face in chain]
            [(0, 1, 2)]

        Specify an index for the vertex of the chain::

            sage: P = polytopes.cube()
            sage: C = P.combinatorial_polyhedron()
            sage: [face.ambient_V_indices() for face in C.a_maximal_chain()]
            [(5,), (0, 5), (0, 3, 4, 5)]
            sage: [face.ambient_V_indices() for face in C.a_maximal_chain(Vindex=2)]
            [(2,), (2, 7), (2, 3, 4, 7)]

        Specify an index for the facet of the chain::

            sage: [face.ambient_H_indices() for face in C.a_maximal_chain()]
            [(3, 4, 5), (4, 5), (5,)]
            sage: [face.ambient_H_indices() for face in C.a_maximal_chain(Hindex=3)]
            [(3, 4, 5), (3, 4), (3,)]
            sage: [face.ambient_H_indices() for face in C.a_maximal_chain(Hindex=2)]
            [(2, 3, 5), (2, 3), (2,)]

        If the specified vertex is not contained in the specified facet an error is raised::

            sage: C.a_maximal_chain(Vindex=0, Hindex=3)
            Traceback (most recent call last):
            ...
            ValueError: the given Vindex is not compatible with the given Hindex

        An error is raised, if the specified index does not correspond to a facet::

            sage: C.a_maximal_chain(Hindex=40)
            Traceback (most recent call last):
            ...
            ValueError: the given Hindex does not correspond to a facet

        An error is raised, if the specified index does not correspond to a vertex::

            sage: C.a_maximal_chain(Vindex=40)
            Traceback (most recent call last):
            ...
            ValueError: the given Vindex does not correspond to a vertex

        ::

            sage: P = Polyhedron(rays=[[1,0,0],[0,0,1]], lines=[[0,1,0]])
            sage: C = P.combinatorial_polyhedron()
            sage: C.a_maximal_chain(Vindex=0)
            Traceback (most recent call last):
            ...
            ValueError: the given Vindex does not correspond to a vertex

        ::

            sage: P = Polyhedron(rays=[[1,0,0],[0,0,1]])
            sage: C = P.combinatorial_polyhedron()
            sage: C.a_maximal_chain(Vindex=0)
            [A 0-dimensional face of a 2-dimensional combinatorial polyhedron,
            A 1-dimensional face of a 2-dimensional combinatorial polyhedron]
            sage: C.a_maximal_chain(Vindex=1)
            Traceback (most recent call last):
            ...
            ValueError: the given Vindex does not correspond to a vertex"""
    @overload
    def a_maximal_chain(self, Vindex=...) -> Any:
        """CombinatorialPolyhedron.a_maximal_chain(self, Vindex=None, Hindex=None)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 2997)

        Return a maximal chain of the face lattice in increasing order
        without empty face and whole polyhedron/maximal face.

        INPUT:

        - ``Vindex`` -- integer (default: ``None``); prescribe the index of the vertex in the chain
        - ``Hindex`` -- integer (default: ``None``); prescribe the index of the facet in the chain

        Each face is given as
        :class:`~sage.geometry.polyhedron.combinatorial_polyhedron.combinatorial_face.CombinatorialFace`.

        EXAMPLES::

            sage: P = polytopes.cross_polytope(4)
            sage: C = P.combinatorial_polyhedron()
            sage: chain = C.a_maximal_chain(); chain
            [A 0-dimensional face of a 4-dimensional combinatorial polyhedron,
             A 1-dimensional face of a 4-dimensional combinatorial polyhedron,
             A 2-dimensional face of a 4-dimensional combinatorial polyhedron,
             A 3-dimensional face of a 4-dimensional combinatorial polyhedron]
            sage: [face.ambient_V_indices() for face in chain]
            [(7,), (6, 7), (5, 6, 7), (4, 5, 6, 7)]

            sage: P = polytopes.hypercube(4)
            sage: C = P.combinatorial_polyhedron()
            sage: chain = C.a_maximal_chain(); chain
            [A 0-dimensional face of a 4-dimensional combinatorial polyhedron,
             A 1-dimensional face of a 4-dimensional combinatorial polyhedron,
             A 2-dimensional face of a 4-dimensional combinatorial polyhedron,
             A 3-dimensional face of a 4-dimensional combinatorial polyhedron]
            sage: [face.ambient_V_indices() for face in chain]
            [(15,), (6, 15), (5, 6, 14, 15), (0, 5, 6, 7, 8, 9, 14, 15)]

            sage: # needs sage.combinat
            sage: P = polytopes.permutahedron(4)
            sage: C = P.combinatorial_polyhedron()
            sage: chain = C.a_maximal_chain(); chain
            [A 0-dimensional face of a 3-dimensional combinatorial polyhedron,
             A 1-dimensional face of a 3-dimensional combinatorial polyhedron,
             A 2-dimensional face of a 3-dimensional combinatorial polyhedron]
            sage: [face.ambient_V_indices() for face in chain]
            [(16,), (15, 16), (8, 9, 14, 15, 16, 17)]

            sage: P = Polyhedron(rays=[[1,0]], lines=[[0,1]])
            sage: C = P.combinatorial_polyhedron()
            sage: chain = C.a_maximal_chain()
            sage: [face.ambient_V_indices() for face in chain]
            [(0, 1)]

            sage: P = Polyhedron(rays=[[1,0,0],[0,0,1]], lines=[[0,1,0]])
            sage: C = P.combinatorial_polyhedron()
            sage: chain = C.a_maximal_chain()
            sage: [face.ambient_V_indices() for face in chain]
            [(0, 1), (0, 1, 3)]

            sage: P = Polyhedron(rays=[[1,0,0]], lines=[[0,1,0],[0,0,1]])
            sage: C = P.combinatorial_polyhedron()
            sage: chain = C.a_maximal_chain()
            sage: [face.ambient_V_indices() for face in chain]
            [(0, 1, 2)]

        Specify an index for the vertex of the chain::

            sage: P = polytopes.cube()
            sage: C = P.combinatorial_polyhedron()
            sage: [face.ambient_V_indices() for face in C.a_maximal_chain()]
            [(5,), (0, 5), (0, 3, 4, 5)]
            sage: [face.ambient_V_indices() for face in C.a_maximal_chain(Vindex=2)]
            [(2,), (2, 7), (2, 3, 4, 7)]

        Specify an index for the facet of the chain::

            sage: [face.ambient_H_indices() for face in C.a_maximal_chain()]
            [(3, 4, 5), (4, 5), (5,)]
            sage: [face.ambient_H_indices() for face in C.a_maximal_chain(Hindex=3)]
            [(3, 4, 5), (3, 4), (3,)]
            sage: [face.ambient_H_indices() for face in C.a_maximal_chain(Hindex=2)]
            [(2, 3, 5), (2, 3), (2,)]

        If the specified vertex is not contained in the specified facet an error is raised::

            sage: C.a_maximal_chain(Vindex=0, Hindex=3)
            Traceback (most recent call last):
            ...
            ValueError: the given Vindex is not compatible with the given Hindex

        An error is raised, if the specified index does not correspond to a facet::

            sage: C.a_maximal_chain(Hindex=40)
            Traceback (most recent call last):
            ...
            ValueError: the given Hindex does not correspond to a facet

        An error is raised, if the specified index does not correspond to a vertex::

            sage: C.a_maximal_chain(Vindex=40)
            Traceback (most recent call last):
            ...
            ValueError: the given Vindex does not correspond to a vertex

        ::

            sage: P = Polyhedron(rays=[[1,0,0],[0,0,1]], lines=[[0,1,0]])
            sage: C = P.combinatorial_polyhedron()
            sage: C.a_maximal_chain(Vindex=0)
            Traceback (most recent call last):
            ...
            ValueError: the given Vindex does not correspond to a vertex

        ::

            sage: P = Polyhedron(rays=[[1,0,0],[0,0,1]])
            sage: C = P.combinatorial_polyhedron()
            sage: C.a_maximal_chain(Vindex=0)
            [A 0-dimensional face of a 2-dimensional combinatorial polyhedron,
            A 1-dimensional face of a 2-dimensional combinatorial polyhedron]
            sage: C.a_maximal_chain(Vindex=1)
            Traceback (most recent call last):
            ...
            ValueError: the given Vindex does not correspond to a vertex"""
    @overload
    def a_maximal_chain(self, Vindex=...) -> Any:
        """CombinatorialPolyhedron.a_maximal_chain(self, Vindex=None, Hindex=None)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 2997)

        Return a maximal chain of the face lattice in increasing order
        without empty face and whole polyhedron/maximal face.

        INPUT:

        - ``Vindex`` -- integer (default: ``None``); prescribe the index of the vertex in the chain
        - ``Hindex`` -- integer (default: ``None``); prescribe the index of the facet in the chain

        Each face is given as
        :class:`~sage.geometry.polyhedron.combinatorial_polyhedron.combinatorial_face.CombinatorialFace`.

        EXAMPLES::

            sage: P = polytopes.cross_polytope(4)
            sage: C = P.combinatorial_polyhedron()
            sage: chain = C.a_maximal_chain(); chain
            [A 0-dimensional face of a 4-dimensional combinatorial polyhedron,
             A 1-dimensional face of a 4-dimensional combinatorial polyhedron,
             A 2-dimensional face of a 4-dimensional combinatorial polyhedron,
             A 3-dimensional face of a 4-dimensional combinatorial polyhedron]
            sage: [face.ambient_V_indices() for face in chain]
            [(7,), (6, 7), (5, 6, 7), (4, 5, 6, 7)]

            sage: P = polytopes.hypercube(4)
            sage: C = P.combinatorial_polyhedron()
            sage: chain = C.a_maximal_chain(); chain
            [A 0-dimensional face of a 4-dimensional combinatorial polyhedron,
             A 1-dimensional face of a 4-dimensional combinatorial polyhedron,
             A 2-dimensional face of a 4-dimensional combinatorial polyhedron,
             A 3-dimensional face of a 4-dimensional combinatorial polyhedron]
            sage: [face.ambient_V_indices() for face in chain]
            [(15,), (6, 15), (5, 6, 14, 15), (0, 5, 6, 7, 8, 9, 14, 15)]

            sage: # needs sage.combinat
            sage: P = polytopes.permutahedron(4)
            sage: C = P.combinatorial_polyhedron()
            sage: chain = C.a_maximal_chain(); chain
            [A 0-dimensional face of a 3-dimensional combinatorial polyhedron,
             A 1-dimensional face of a 3-dimensional combinatorial polyhedron,
             A 2-dimensional face of a 3-dimensional combinatorial polyhedron]
            sage: [face.ambient_V_indices() for face in chain]
            [(16,), (15, 16), (8, 9, 14, 15, 16, 17)]

            sage: P = Polyhedron(rays=[[1,0]], lines=[[0,1]])
            sage: C = P.combinatorial_polyhedron()
            sage: chain = C.a_maximal_chain()
            sage: [face.ambient_V_indices() for face in chain]
            [(0, 1)]

            sage: P = Polyhedron(rays=[[1,0,0],[0,0,1]], lines=[[0,1,0]])
            sage: C = P.combinatorial_polyhedron()
            sage: chain = C.a_maximal_chain()
            sage: [face.ambient_V_indices() for face in chain]
            [(0, 1), (0, 1, 3)]

            sage: P = Polyhedron(rays=[[1,0,0]], lines=[[0,1,0],[0,0,1]])
            sage: C = P.combinatorial_polyhedron()
            sage: chain = C.a_maximal_chain()
            sage: [face.ambient_V_indices() for face in chain]
            [(0, 1, 2)]

        Specify an index for the vertex of the chain::

            sage: P = polytopes.cube()
            sage: C = P.combinatorial_polyhedron()
            sage: [face.ambient_V_indices() for face in C.a_maximal_chain()]
            [(5,), (0, 5), (0, 3, 4, 5)]
            sage: [face.ambient_V_indices() for face in C.a_maximal_chain(Vindex=2)]
            [(2,), (2, 7), (2, 3, 4, 7)]

        Specify an index for the facet of the chain::

            sage: [face.ambient_H_indices() for face in C.a_maximal_chain()]
            [(3, 4, 5), (4, 5), (5,)]
            sage: [face.ambient_H_indices() for face in C.a_maximal_chain(Hindex=3)]
            [(3, 4, 5), (3, 4), (3,)]
            sage: [face.ambient_H_indices() for face in C.a_maximal_chain(Hindex=2)]
            [(2, 3, 5), (2, 3), (2,)]

        If the specified vertex is not contained in the specified facet an error is raised::

            sage: C.a_maximal_chain(Vindex=0, Hindex=3)
            Traceback (most recent call last):
            ...
            ValueError: the given Vindex is not compatible with the given Hindex

        An error is raised, if the specified index does not correspond to a facet::

            sage: C.a_maximal_chain(Hindex=40)
            Traceback (most recent call last):
            ...
            ValueError: the given Hindex does not correspond to a facet

        An error is raised, if the specified index does not correspond to a vertex::

            sage: C.a_maximal_chain(Vindex=40)
            Traceback (most recent call last):
            ...
            ValueError: the given Vindex does not correspond to a vertex

        ::

            sage: P = Polyhedron(rays=[[1,0,0],[0,0,1]], lines=[[0,1,0]])
            sage: C = P.combinatorial_polyhedron()
            sage: C.a_maximal_chain(Vindex=0)
            Traceback (most recent call last):
            ...
            ValueError: the given Vindex does not correspond to a vertex

        ::

            sage: P = Polyhedron(rays=[[1,0,0],[0,0,1]])
            sage: C = P.combinatorial_polyhedron()
            sage: C.a_maximal_chain(Vindex=0)
            [A 0-dimensional face of a 2-dimensional combinatorial polyhedron,
            A 1-dimensional face of a 2-dimensional combinatorial polyhedron]
            sage: C.a_maximal_chain(Vindex=1)
            Traceback (most recent call last):
            ...
            ValueError: the given Vindex does not correspond to a vertex"""
    def choose_algorithm_to_compute_edges_or_ridges(self, edges_or_ridges) -> Any:
        '''CombinatorialPolyhedron.choose_algorithm_to_compute_edges_or_ridges(self, edges_or_ridges)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 3575)

        Use some heuristics to pick primal or dual algorithm for
        computation of edges resp. ridges.

        We estimate how long it takes to compute a face using the primal
        and the dual algorithm. This may differ significantly, so that e.g.
        visiting all faces with the primal algorithm is faster than using
        the dual algorithm to just visit vertices and edges.

        We guess the number of edges and ridges and do a wild estimate on
        the total number of faces.

        INPUT:

        - ``edges_or_ridges`` -- string; one of:
          * ``\'edges\'``
          * ``\'ridges\'``

        OUTPUT: either ``\'primal\'`` or ``\'dual\'``

        EXAMPLES::

            sage: C = polytopes.permutahedron(5).combinatorial_polyhedron()
            sage: C.choose_algorithm_to_compute_edges_or_ridges("edges")
            \'primal\'
            sage: C.choose_algorithm_to_compute_edges_or_ridges("ridges")
            \'primal\'

        ::

            sage: C = polytopes.cross_polytope(5).combinatorial_polyhedron()
            sage: C.choose_algorithm_to_compute_edges_or_ridges("edges")
            \'dual\'
            sage: C.choose_algorithm_to_compute_edges_or_ridges("ridges")
            \'dual\'


        ::

            sage: C = polytopes.Birkhoff_polytope(5).combinatorial_polyhedron()
            sage: C.choose_algorithm_to_compute_edges_or_ridges("edges")
            \'dual\'
            sage: C.choose_algorithm_to_compute_edges_or_ridges("ridges")
            \'primal\'
            sage: C.choose_algorithm_to_compute_edges_or_ridges("something_else")
            Traceback (most recent call last):
            ...
            ValueError: unknown computation goal something_else'''
    def dim(self) -> Any:
        """CombinatorialPolyhedron.dimension(self)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 783)

        Return the dimension of the polyhedron.

        EXAMPLES::

            sage: C = CombinatorialPolyhedron([(1,2,3), (1,2,4),
            ....:                              (1,3,4), (2,3,4)])
            sage: C.dimension()
            3

            sage: P = Polyhedron(rays=[[1,0,0],[0,1,0],[0,0,1],[0,0,-1]])
            sage: CombinatorialPolyhedron(P).dimension()
            3

        ``dim`` is an alias::

            sage: CombinatorialPolyhedron(P).dim()
            3"""
    @overload
    def dimension(self) -> Any:
        """CombinatorialPolyhedron.dimension(self)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 783)

        Return the dimension of the polyhedron.

        EXAMPLES::

            sage: C = CombinatorialPolyhedron([(1,2,3), (1,2,4),
            ....:                              (1,3,4), (2,3,4)])
            sage: C.dimension()
            3

            sage: P = Polyhedron(rays=[[1,0,0],[0,1,0],[0,0,1],[0,0,-1]])
            sage: CombinatorialPolyhedron(P).dimension()
            3

        ``dim`` is an alias::

            sage: CombinatorialPolyhedron(P).dim()
            3"""
    @overload
    def dimension(self) -> Any:
        """CombinatorialPolyhedron.dimension(self)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 783)

        Return the dimension of the polyhedron.

        EXAMPLES::

            sage: C = CombinatorialPolyhedron([(1,2,3), (1,2,4),
            ....:                              (1,3,4), (2,3,4)])
            sage: C.dimension()
            3

            sage: P = Polyhedron(rays=[[1,0,0],[0,1,0],[0,0,1],[0,0,-1]])
            sage: CombinatorialPolyhedron(P).dimension()
            3

        ``dim`` is an alias::

            sage: CombinatorialPolyhedron(P).dim()
            3"""
    @overload
    def dimension(self) -> Any:
        """CombinatorialPolyhedron.dimension(self)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 783)

        Return the dimension of the polyhedron.

        EXAMPLES::

            sage: C = CombinatorialPolyhedron([(1,2,3), (1,2,4),
            ....:                              (1,3,4), (2,3,4)])
            sage: C.dimension()
            3

            sage: P = Polyhedron(rays=[[1,0,0],[0,1,0],[0,0,1],[0,0,-1]])
            sage: CombinatorialPolyhedron(P).dimension()
            3

        ``dim`` is an alias::

            sage: CombinatorialPolyhedron(P).dim()
            3"""
    @overload
    def dual(self) -> CombinatorialPolyhedron:
        """CombinatorialPolyhedron.dual(self) -> CombinatorialPolyhedron

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 3311)

        Return the dual/polar of ``self``.

        Only defined for bounded polyhedra.

        .. SEEALSO::

            :meth:`~sage.geometry.polyhedron.base.Polyhedron_base.polar`.

        EXAMPLES::

            sage: P = polytopes.cube()
            sage: C = P.combinatorial_polyhedron()
            sage: D = C.dual()
            sage: D.f_vector()
            (1, 6, 12, 8, 1)
            sage: D1 = P.polar().combinatorial_polyhedron()
            sage: D1.face_lattice().is_isomorphic(D.face_lattice())                     # needs sage.combinat
            True

        Polar is an alias to be consistent with :class:`~sage.geometry.polyhedron.base.Polyhedron_base`::

            sage: C.polar().f_vector()
            (1, 6, 12, 8, 1)

        For unbounded polyhedra, an error is raised::

            sage: C = CombinatorialPolyhedron([[0,1], [0,2]], far_face=[1,2], unbounded=True)
            sage: C.dual()
            Traceback (most recent call last):
            ...
            ValueError: self must be bounded"""
    @overload
    def dual(self) -> Any:
        """CombinatorialPolyhedron.dual(self) -> CombinatorialPolyhedron

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 3311)

        Return the dual/polar of ``self``.

        Only defined for bounded polyhedra.

        .. SEEALSO::

            :meth:`~sage.geometry.polyhedron.base.Polyhedron_base.polar`.

        EXAMPLES::

            sage: P = polytopes.cube()
            sage: C = P.combinatorial_polyhedron()
            sage: D = C.dual()
            sage: D.f_vector()
            (1, 6, 12, 8, 1)
            sage: D1 = P.polar().combinatorial_polyhedron()
            sage: D1.face_lattice().is_isomorphic(D.face_lattice())                     # needs sage.combinat
            True

        Polar is an alias to be consistent with :class:`~sage.geometry.polyhedron.base.Polyhedron_base`::

            sage: C.polar().f_vector()
            (1, 6, 12, 8, 1)

        For unbounded polyhedra, an error is raised::

            sage: C = CombinatorialPolyhedron([[0,1], [0,2]], far_face=[1,2], unbounded=True)
            sage: C.dual()
            Traceback (most recent call last):
            ...
            ValueError: self must be bounded"""
    @overload
    def dual(self) -> Any:
        """CombinatorialPolyhedron.dual(self) -> CombinatorialPolyhedron

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 3311)

        Return the dual/polar of ``self``.

        Only defined for bounded polyhedra.

        .. SEEALSO::

            :meth:`~sage.geometry.polyhedron.base.Polyhedron_base.polar`.

        EXAMPLES::

            sage: P = polytopes.cube()
            sage: C = P.combinatorial_polyhedron()
            sage: D = C.dual()
            sage: D.f_vector()
            (1, 6, 12, 8, 1)
            sage: D1 = P.polar().combinatorial_polyhedron()
            sage: D1.face_lattice().is_isomorphic(D.face_lattice())                     # needs sage.combinat
            True

        Polar is an alias to be consistent with :class:`~sage.geometry.polyhedron.base.Polyhedron_base`::

            sage: C.polar().f_vector()
            (1, 6, 12, 8, 1)

        For unbounded polyhedra, an error is raised::

            sage: C = CombinatorialPolyhedron([[0,1], [0,2]], far_face=[1,2], unbounded=True)
            sage: C.dual()
            Traceback (most recent call last):
            ...
            ValueError: self must be bounded"""
    @overload
    def edges(self, names=..., algorithm=...) -> Any:
        """CombinatorialPolyhedron.edges(self, names=True, algorithm=None)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 1187)

        Return the edges of the polyhedron, i.e. the rank 1 faces.

        INPUT:

        - ``names`` -- boolean (default: ``True``); if ``False``,
          then the Vrepresentatives in the edges are given by
          their indices in the Vrepresentation

        - ``algorithm`` -- string (optional);
          specify whether the face generator starts with facets or vertices:
          * ``'primal'`` -- start with the facets
          * ``'dual'`` -- start with the vertices
          * ``None`` -- choose automatically

        .. NOTE::

            To compute edges and f_vector, first compute the edges.
            This might be faster.

        EXAMPLES::

            sage: P = polytopes.cyclic_polytope(3,5)
            sage: C = CombinatorialPolyhedron(P)
            sage: C.edges()
            ((A vertex at (3, 9, 27), A vertex at (4, 16, 64)),
             (A vertex at (2, 4, 8), A vertex at (4, 16, 64)),
             (A vertex at (1, 1, 1), A vertex at (4, 16, 64)),
             (A vertex at (0, 0, 0), A vertex at (4, 16, 64)),
             (A vertex at (2, 4, 8), A vertex at (3, 9, 27)),
             (A vertex at (0, 0, 0), A vertex at (3, 9, 27)),
             (A vertex at (1, 1, 1), A vertex at (2, 4, 8)),
             (A vertex at (0, 0, 0), A vertex at (2, 4, 8)),
             (A vertex at (0, 0, 0), A vertex at (1, 1, 1)))

            sage: C.edges(names=False)
            ((3, 4), (2, 4), (1, 4), (0, 4), (2, 3), (0, 3), (1, 2), (0, 2), (0, 1))

            sage: P = Polyhedron(rays=[[-1,0],[1,0]])
            sage: C = CombinatorialPolyhedron(P)
            sage: C.edges()
            ((A line in the direction (1, 0), A vertex at (0, 0)),)

            sage: P = Polyhedron(vertices=[[0,0],[1,0]])
            sage: C = CombinatorialPolyhedron(P)
            sage: C.edges()
            ((A vertex at (0, 0), A vertex at (1, 0)),)

            sage: from itertools import combinations
            sage: N = combinations(['a','b','c','d','e'], 4)
            sage: C = CombinatorialPolyhedron(N)
            sage: C.edges()
            (('d', 'e'),
             ('c', 'e'),
             ('b', 'e'),
             ('a', 'e'),
             ('c', 'd'),
             ('b', 'd'),
             ('a', 'd'),
             ('b', 'c'),
             ('a', 'c'),
             ('a', 'b'))"""
    @overload
    def edges(self) -> Any:
        """CombinatorialPolyhedron.edges(self, names=True, algorithm=None)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 1187)

        Return the edges of the polyhedron, i.e. the rank 1 faces.

        INPUT:

        - ``names`` -- boolean (default: ``True``); if ``False``,
          then the Vrepresentatives in the edges are given by
          their indices in the Vrepresentation

        - ``algorithm`` -- string (optional);
          specify whether the face generator starts with facets or vertices:
          * ``'primal'`` -- start with the facets
          * ``'dual'`` -- start with the vertices
          * ``None`` -- choose automatically

        .. NOTE::

            To compute edges and f_vector, first compute the edges.
            This might be faster.

        EXAMPLES::

            sage: P = polytopes.cyclic_polytope(3,5)
            sage: C = CombinatorialPolyhedron(P)
            sage: C.edges()
            ((A vertex at (3, 9, 27), A vertex at (4, 16, 64)),
             (A vertex at (2, 4, 8), A vertex at (4, 16, 64)),
             (A vertex at (1, 1, 1), A vertex at (4, 16, 64)),
             (A vertex at (0, 0, 0), A vertex at (4, 16, 64)),
             (A vertex at (2, 4, 8), A vertex at (3, 9, 27)),
             (A vertex at (0, 0, 0), A vertex at (3, 9, 27)),
             (A vertex at (1, 1, 1), A vertex at (2, 4, 8)),
             (A vertex at (0, 0, 0), A vertex at (2, 4, 8)),
             (A vertex at (0, 0, 0), A vertex at (1, 1, 1)))

            sage: C.edges(names=False)
            ((3, 4), (2, 4), (1, 4), (0, 4), (2, 3), (0, 3), (1, 2), (0, 2), (0, 1))

            sage: P = Polyhedron(rays=[[-1,0],[1,0]])
            sage: C = CombinatorialPolyhedron(P)
            sage: C.edges()
            ((A line in the direction (1, 0), A vertex at (0, 0)),)

            sage: P = Polyhedron(vertices=[[0,0],[1,0]])
            sage: C = CombinatorialPolyhedron(P)
            sage: C.edges()
            ((A vertex at (0, 0), A vertex at (1, 0)),)

            sage: from itertools import combinations
            sage: N = combinations(['a','b','c','d','e'], 4)
            sage: C = CombinatorialPolyhedron(N)
            sage: C.edges()
            (('d', 'e'),
             ('c', 'e'),
             ('b', 'e'),
             ('a', 'e'),
             ('c', 'd'),
             ('b', 'd'),
             ('a', 'd'),
             ('b', 'c'),
             ('a', 'c'),
             ('a', 'b'))"""
    @overload
    def edges(self, names=...) -> Any:
        """CombinatorialPolyhedron.edges(self, names=True, algorithm=None)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 1187)

        Return the edges of the polyhedron, i.e. the rank 1 faces.

        INPUT:

        - ``names`` -- boolean (default: ``True``); if ``False``,
          then the Vrepresentatives in the edges are given by
          their indices in the Vrepresentation

        - ``algorithm`` -- string (optional);
          specify whether the face generator starts with facets or vertices:
          * ``'primal'`` -- start with the facets
          * ``'dual'`` -- start with the vertices
          * ``None`` -- choose automatically

        .. NOTE::

            To compute edges and f_vector, first compute the edges.
            This might be faster.

        EXAMPLES::

            sage: P = polytopes.cyclic_polytope(3,5)
            sage: C = CombinatorialPolyhedron(P)
            sage: C.edges()
            ((A vertex at (3, 9, 27), A vertex at (4, 16, 64)),
             (A vertex at (2, 4, 8), A vertex at (4, 16, 64)),
             (A vertex at (1, 1, 1), A vertex at (4, 16, 64)),
             (A vertex at (0, 0, 0), A vertex at (4, 16, 64)),
             (A vertex at (2, 4, 8), A vertex at (3, 9, 27)),
             (A vertex at (0, 0, 0), A vertex at (3, 9, 27)),
             (A vertex at (1, 1, 1), A vertex at (2, 4, 8)),
             (A vertex at (0, 0, 0), A vertex at (2, 4, 8)),
             (A vertex at (0, 0, 0), A vertex at (1, 1, 1)))

            sage: C.edges(names=False)
            ((3, 4), (2, 4), (1, 4), (0, 4), (2, 3), (0, 3), (1, 2), (0, 2), (0, 1))

            sage: P = Polyhedron(rays=[[-1,0],[1,0]])
            sage: C = CombinatorialPolyhedron(P)
            sage: C.edges()
            ((A line in the direction (1, 0), A vertex at (0, 0)),)

            sage: P = Polyhedron(vertices=[[0,0],[1,0]])
            sage: C = CombinatorialPolyhedron(P)
            sage: C.edges()
            ((A vertex at (0, 0), A vertex at (1, 0)),)

            sage: from itertools import combinations
            sage: N = combinations(['a','b','c','d','e'], 4)
            sage: C = CombinatorialPolyhedron(N)
            sage: C.edges()
            (('d', 'e'),
             ('c', 'e'),
             ('b', 'e'),
             ('a', 'e'),
             ('c', 'd'),
             ('b', 'd'),
             ('a', 'd'),
             ('b', 'c'),
             ('a', 'c'),
             ('a', 'b'))"""
    @overload
    def edges(self) -> Any:
        """CombinatorialPolyhedron.edges(self, names=True, algorithm=None)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 1187)

        Return the edges of the polyhedron, i.e. the rank 1 faces.

        INPUT:

        - ``names`` -- boolean (default: ``True``); if ``False``,
          then the Vrepresentatives in the edges are given by
          their indices in the Vrepresentation

        - ``algorithm`` -- string (optional);
          specify whether the face generator starts with facets or vertices:
          * ``'primal'`` -- start with the facets
          * ``'dual'`` -- start with the vertices
          * ``None`` -- choose automatically

        .. NOTE::

            To compute edges and f_vector, first compute the edges.
            This might be faster.

        EXAMPLES::

            sage: P = polytopes.cyclic_polytope(3,5)
            sage: C = CombinatorialPolyhedron(P)
            sage: C.edges()
            ((A vertex at (3, 9, 27), A vertex at (4, 16, 64)),
             (A vertex at (2, 4, 8), A vertex at (4, 16, 64)),
             (A vertex at (1, 1, 1), A vertex at (4, 16, 64)),
             (A vertex at (0, 0, 0), A vertex at (4, 16, 64)),
             (A vertex at (2, 4, 8), A vertex at (3, 9, 27)),
             (A vertex at (0, 0, 0), A vertex at (3, 9, 27)),
             (A vertex at (1, 1, 1), A vertex at (2, 4, 8)),
             (A vertex at (0, 0, 0), A vertex at (2, 4, 8)),
             (A vertex at (0, 0, 0), A vertex at (1, 1, 1)))

            sage: C.edges(names=False)
            ((3, 4), (2, 4), (1, 4), (0, 4), (2, 3), (0, 3), (1, 2), (0, 2), (0, 1))

            sage: P = Polyhedron(rays=[[-1,0],[1,0]])
            sage: C = CombinatorialPolyhedron(P)
            sage: C.edges()
            ((A line in the direction (1, 0), A vertex at (0, 0)),)

            sage: P = Polyhedron(vertices=[[0,0],[1,0]])
            sage: C = CombinatorialPolyhedron(P)
            sage: C.edges()
            ((A vertex at (0, 0), A vertex at (1, 0)),)

            sage: from itertools import combinations
            sage: N = combinations(['a','b','c','d','e'], 4)
            sage: C = CombinatorialPolyhedron(N)
            sage: C.edges()
            (('d', 'e'),
             ('c', 'e'),
             ('b', 'e'),
             ('a', 'e'),
             ('c', 'd'),
             ('b', 'd'),
             ('a', 'd'),
             ('b', 'c'),
             ('a', 'c'),
             ('a', 'b'))"""
    @overload
    def edges(self) -> Any:
        """CombinatorialPolyhedron.edges(self, names=True, algorithm=None)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 1187)

        Return the edges of the polyhedron, i.e. the rank 1 faces.

        INPUT:

        - ``names`` -- boolean (default: ``True``); if ``False``,
          then the Vrepresentatives in the edges are given by
          their indices in the Vrepresentation

        - ``algorithm`` -- string (optional);
          specify whether the face generator starts with facets or vertices:
          * ``'primal'`` -- start with the facets
          * ``'dual'`` -- start with the vertices
          * ``None`` -- choose automatically

        .. NOTE::

            To compute edges and f_vector, first compute the edges.
            This might be faster.

        EXAMPLES::

            sage: P = polytopes.cyclic_polytope(3,5)
            sage: C = CombinatorialPolyhedron(P)
            sage: C.edges()
            ((A vertex at (3, 9, 27), A vertex at (4, 16, 64)),
             (A vertex at (2, 4, 8), A vertex at (4, 16, 64)),
             (A vertex at (1, 1, 1), A vertex at (4, 16, 64)),
             (A vertex at (0, 0, 0), A vertex at (4, 16, 64)),
             (A vertex at (2, 4, 8), A vertex at (3, 9, 27)),
             (A vertex at (0, 0, 0), A vertex at (3, 9, 27)),
             (A vertex at (1, 1, 1), A vertex at (2, 4, 8)),
             (A vertex at (0, 0, 0), A vertex at (2, 4, 8)),
             (A vertex at (0, 0, 0), A vertex at (1, 1, 1)))

            sage: C.edges(names=False)
            ((3, 4), (2, 4), (1, 4), (0, 4), (2, 3), (0, 3), (1, 2), (0, 2), (0, 1))

            sage: P = Polyhedron(rays=[[-1,0],[1,0]])
            sage: C = CombinatorialPolyhedron(P)
            sage: C.edges()
            ((A line in the direction (1, 0), A vertex at (0, 0)),)

            sage: P = Polyhedron(vertices=[[0,0],[1,0]])
            sage: C = CombinatorialPolyhedron(P)
            sage: C.edges()
            ((A vertex at (0, 0), A vertex at (1, 0)),)

            sage: from itertools import combinations
            sage: N = combinations(['a','b','c','d','e'], 4)
            sage: C = CombinatorialPolyhedron(N)
            sage: C.edges()
            (('d', 'e'),
             ('c', 'e'),
             ('b', 'e'),
             ('a', 'e'),
             ('c', 'd'),
             ('b', 'd'),
             ('a', 'd'),
             ('b', 'c'),
             ('a', 'c'),
             ('a', 'b'))"""
    @overload
    def edges(self) -> Any:
        """CombinatorialPolyhedron.edges(self, names=True, algorithm=None)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 1187)

        Return the edges of the polyhedron, i.e. the rank 1 faces.

        INPUT:

        - ``names`` -- boolean (default: ``True``); if ``False``,
          then the Vrepresentatives in the edges are given by
          their indices in the Vrepresentation

        - ``algorithm`` -- string (optional);
          specify whether the face generator starts with facets or vertices:
          * ``'primal'`` -- start with the facets
          * ``'dual'`` -- start with the vertices
          * ``None`` -- choose automatically

        .. NOTE::

            To compute edges and f_vector, first compute the edges.
            This might be faster.

        EXAMPLES::

            sage: P = polytopes.cyclic_polytope(3,5)
            sage: C = CombinatorialPolyhedron(P)
            sage: C.edges()
            ((A vertex at (3, 9, 27), A vertex at (4, 16, 64)),
             (A vertex at (2, 4, 8), A vertex at (4, 16, 64)),
             (A vertex at (1, 1, 1), A vertex at (4, 16, 64)),
             (A vertex at (0, 0, 0), A vertex at (4, 16, 64)),
             (A vertex at (2, 4, 8), A vertex at (3, 9, 27)),
             (A vertex at (0, 0, 0), A vertex at (3, 9, 27)),
             (A vertex at (1, 1, 1), A vertex at (2, 4, 8)),
             (A vertex at (0, 0, 0), A vertex at (2, 4, 8)),
             (A vertex at (0, 0, 0), A vertex at (1, 1, 1)))

            sage: C.edges(names=False)
            ((3, 4), (2, 4), (1, 4), (0, 4), (2, 3), (0, 3), (1, 2), (0, 2), (0, 1))

            sage: P = Polyhedron(rays=[[-1,0],[1,0]])
            sage: C = CombinatorialPolyhedron(P)
            sage: C.edges()
            ((A line in the direction (1, 0), A vertex at (0, 0)),)

            sage: P = Polyhedron(vertices=[[0,0],[1,0]])
            sage: C = CombinatorialPolyhedron(P)
            sage: C.edges()
            ((A vertex at (0, 0), A vertex at (1, 0)),)

            sage: from itertools import combinations
            sage: N = combinations(['a','b','c','d','e'], 4)
            sage: C = CombinatorialPolyhedron(N)
            sage: C.edges()
            (('d', 'e'),
             ('c', 'e'),
             ('b', 'e'),
             ('a', 'e'),
             ('c', 'd'),
             ('b', 'd'),
             ('a', 'd'),
             ('b', 'c'),
             ('a', 'c'),
             ('a', 'b'))"""
    @overload
    def f_vector(self, num_threads=..., parallelization_depth=..., algorithm=...) -> Any:
        """CombinatorialPolyhedron.f_vector(self, num_threads=None, parallelization_depth=None, algorithm=None)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 1697)

        Compute the ``f_vector`` of the polyhedron.

        The ``f_vector`` contains the number of faces of dimension `k`
        for each `k` in ``range(-1, self.dimension() + 1)``.

        INPUT:

        - ``num_threads`` -- integer (optional); specify the number of threads

        - ``parallelization_depth`` -- integer (optional); specify
          how deep in the lattice the parallelization is done

        - ``algorithm`` -- string (optional);
          specify whether the face generator starts with facets or vertices:

          * ``'primal'`` -- start with the facets
          * ``'dual'`` -- start with the vertices
          * ``None`` -- choose automatically

        .. NOTE::

            To obtain edges and/or ridges as well, first do so. This might
            already compute the ``f_vector``.

        EXAMPLES::

            sage: P = polytopes.permutahedron(5)
            sage: C = CombinatorialPolyhedron(P)
            sage: C.f_vector()
            (1, 120, 240, 150, 30, 1)

            sage: P = polytopes.cyclic_polytope(6,10)
            sage: C = CombinatorialPolyhedron(P)
            sage: C.f_vector()
            (1, 10, 45, 120, 185, 150, 50, 1)

        Using two threads::

            sage: P = polytopes.permutahedron(5)
            sage: C = CombinatorialPolyhedron(P)
            sage: C.f_vector(num_threads=2)
            (1, 120, 240, 150, 30, 1)

        TESTS::

            sage: type(C.f_vector())
            <class 'sage.modules.vector_integer_dense.Vector_integer_dense'>"""
    @overload
    def f_vector(self) -> Any:
        """CombinatorialPolyhedron.f_vector(self, num_threads=None, parallelization_depth=None, algorithm=None)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 1697)

        Compute the ``f_vector`` of the polyhedron.

        The ``f_vector`` contains the number of faces of dimension `k`
        for each `k` in ``range(-1, self.dimension() + 1)``.

        INPUT:

        - ``num_threads`` -- integer (optional); specify the number of threads

        - ``parallelization_depth`` -- integer (optional); specify
          how deep in the lattice the parallelization is done

        - ``algorithm`` -- string (optional);
          specify whether the face generator starts with facets or vertices:

          * ``'primal'`` -- start with the facets
          * ``'dual'`` -- start with the vertices
          * ``None`` -- choose automatically

        .. NOTE::

            To obtain edges and/or ridges as well, first do so. This might
            already compute the ``f_vector``.

        EXAMPLES::

            sage: P = polytopes.permutahedron(5)
            sage: C = CombinatorialPolyhedron(P)
            sage: C.f_vector()
            (1, 120, 240, 150, 30, 1)

            sage: P = polytopes.cyclic_polytope(6,10)
            sage: C = CombinatorialPolyhedron(P)
            sage: C.f_vector()
            (1, 10, 45, 120, 185, 150, 50, 1)

        Using two threads::

            sage: P = polytopes.permutahedron(5)
            sage: C = CombinatorialPolyhedron(P)
            sage: C.f_vector(num_threads=2)
            (1, 120, 240, 150, 30, 1)

        TESTS::

            sage: type(C.f_vector())
            <class 'sage.modules.vector_integer_dense.Vector_integer_dense'>"""
    @overload
    def f_vector(self) -> Any:
        """CombinatorialPolyhedron.f_vector(self, num_threads=None, parallelization_depth=None, algorithm=None)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 1697)

        Compute the ``f_vector`` of the polyhedron.

        The ``f_vector`` contains the number of faces of dimension `k`
        for each `k` in ``range(-1, self.dimension() + 1)``.

        INPUT:

        - ``num_threads`` -- integer (optional); specify the number of threads

        - ``parallelization_depth`` -- integer (optional); specify
          how deep in the lattice the parallelization is done

        - ``algorithm`` -- string (optional);
          specify whether the face generator starts with facets or vertices:

          * ``'primal'`` -- start with the facets
          * ``'dual'`` -- start with the vertices
          * ``None`` -- choose automatically

        .. NOTE::

            To obtain edges and/or ridges as well, first do so. This might
            already compute the ``f_vector``.

        EXAMPLES::

            sage: P = polytopes.permutahedron(5)
            sage: C = CombinatorialPolyhedron(P)
            sage: C.f_vector()
            (1, 120, 240, 150, 30, 1)

            sage: P = polytopes.cyclic_polytope(6,10)
            sage: C = CombinatorialPolyhedron(P)
            sage: C.f_vector()
            (1, 10, 45, 120, 185, 150, 50, 1)

        Using two threads::

            sage: P = polytopes.permutahedron(5)
            sage: C = CombinatorialPolyhedron(P)
            sage: C.f_vector(num_threads=2)
            (1, 120, 240, 150, 30, 1)

        TESTS::

            sage: type(C.f_vector())
            <class 'sage.modules.vector_integer_dense.Vector_integer_dense'>"""
    @overload
    def f_vector(self, num_threads=...) -> Any:
        """CombinatorialPolyhedron.f_vector(self, num_threads=None, parallelization_depth=None, algorithm=None)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 1697)

        Compute the ``f_vector`` of the polyhedron.

        The ``f_vector`` contains the number of faces of dimension `k`
        for each `k` in ``range(-1, self.dimension() + 1)``.

        INPUT:

        - ``num_threads`` -- integer (optional); specify the number of threads

        - ``parallelization_depth`` -- integer (optional); specify
          how deep in the lattice the parallelization is done

        - ``algorithm`` -- string (optional);
          specify whether the face generator starts with facets or vertices:

          * ``'primal'`` -- start with the facets
          * ``'dual'`` -- start with the vertices
          * ``None`` -- choose automatically

        .. NOTE::

            To obtain edges and/or ridges as well, first do so. This might
            already compute the ``f_vector``.

        EXAMPLES::

            sage: P = polytopes.permutahedron(5)
            sage: C = CombinatorialPolyhedron(P)
            sage: C.f_vector()
            (1, 120, 240, 150, 30, 1)

            sage: P = polytopes.cyclic_polytope(6,10)
            sage: C = CombinatorialPolyhedron(P)
            sage: C.f_vector()
            (1, 10, 45, 120, 185, 150, 50, 1)

        Using two threads::

            sage: P = polytopes.permutahedron(5)
            sage: C = CombinatorialPolyhedron(P)
            sage: C.f_vector(num_threads=2)
            (1, 120, 240, 150, 30, 1)

        TESTS::

            sage: type(C.f_vector())
            <class 'sage.modules.vector_integer_dense.Vector_integer_dense'>"""
    @overload
    def f_vector(self) -> Any:
        """CombinatorialPolyhedron.f_vector(self, num_threads=None, parallelization_depth=None, algorithm=None)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 1697)

        Compute the ``f_vector`` of the polyhedron.

        The ``f_vector`` contains the number of faces of dimension `k`
        for each `k` in ``range(-1, self.dimension() + 1)``.

        INPUT:

        - ``num_threads`` -- integer (optional); specify the number of threads

        - ``parallelization_depth`` -- integer (optional); specify
          how deep in the lattice the parallelization is done

        - ``algorithm`` -- string (optional);
          specify whether the face generator starts with facets or vertices:

          * ``'primal'`` -- start with the facets
          * ``'dual'`` -- start with the vertices
          * ``None`` -- choose automatically

        .. NOTE::

            To obtain edges and/or ridges as well, first do so. This might
            already compute the ``f_vector``.

        EXAMPLES::

            sage: P = polytopes.permutahedron(5)
            sage: C = CombinatorialPolyhedron(P)
            sage: C.f_vector()
            (1, 120, 240, 150, 30, 1)

            sage: P = polytopes.cyclic_polytope(6,10)
            sage: C = CombinatorialPolyhedron(P)
            sage: C.f_vector()
            (1, 10, 45, 120, 185, 150, 50, 1)

        Using two threads::

            sage: P = polytopes.permutahedron(5)
            sage: C = CombinatorialPolyhedron(P)
            sage: C.f_vector(num_threads=2)
            (1, 120, 240, 150, 30, 1)

        TESTS::

            sage: type(C.f_vector())
            <class 'sage.modules.vector_integer_dense.Vector_integer_dense'>"""
    @overload
    def face_by_face_lattice_index(self, index) -> Any:
        """CombinatorialPolyhedron.face_by_face_lattice_index(self, index)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 2948)

        Return the element of :meth:`CombinatorialPolyhedron.face_lattice` with corresponding index.

        The element will be returned as
        :class:`~sage.geometry.polyhedron.combinatorial_polyhedron.combinatorial_face.CombinatorialFace`.

        EXAMPLES::

            sage: # needs sage.combinat
            sage: P = polytopes.cube()
            sage: C = CombinatorialPolyhedron(P)
            sage: F = C.face_lattice()
            sage: F
            Finite lattice containing 28 elements
            sage: G = F.relabel(C.face_by_face_lattice_index)
            sage: G.level_sets()[0]
            [A -1-dimensional face of a 3-dimensional combinatorial polyhedron]
            sage: G.level_sets()[3]
            [A 2-dimensional face of a 3-dimensional combinatorial polyhedron,
             A 2-dimensional face of a 3-dimensional combinatorial polyhedron,
             A 2-dimensional face of a 3-dimensional combinatorial polyhedron,
             A 2-dimensional face of a 3-dimensional combinatorial polyhedron,
             A 2-dimensional face of a 3-dimensional combinatorial polyhedron,
             A 2-dimensional face of a 3-dimensional combinatorial polyhedron]

            sage: P = Polyhedron(rays=[[0,1], [1,0]])
            sage: C = CombinatorialPolyhedron(P)
            sage: F = C.face_lattice()                                                  # needs sage.combinat
            sage: G = F.relabel(C.face_by_face_lattice_index)                           # needs sage.combinat
            sage: G._elements                                                           # needs sage.combinat
            (A -1-dimensional face of a 2-dimensional combinatorial polyhedron,
              A 0-dimensional face of a 2-dimensional combinatorial polyhedron,
              A 1-dimensional face of a 2-dimensional combinatorial polyhedron,
              A 1-dimensional face of a 2-dimensional combinatorial polyhedron,
              A 2-dimensional face of a 2-dimensional combinatorial polyhedron)

            sage: def f(i): return C.face_by_face_lattice_index(i).ambient_V_indices()
            sage: G = F.relabel(f)                                                      # needs sage.combinat
            sage: G._elements                                                           # needs sage.combinat
            ((), (0,), (0, 1), (0, 2), (0, 1, 2))"""
    @overload
    def face_by_face_lattice_index(self, i) -> Any:
        """CombinatorialPolyhedron.face_by_face_lattice_index(self, index)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 2948)

        Return the element of :meth:`CombinatorialPolyhedron.face_lattice` with corresponding index.

        The element will be returned as
        :class:`~sage.geometry.polyhedron.combinatorial_polyhedron.combinatorial_face.CombinatorialFace`.

        EXAMPLES::

            sage: # needs sage.combinat
            sage: P = polytopes.cube()
            sage: C = CombinatorialPolyhedron(P)
            sage: F = C.face_lattice()
            sage: F
            Finite lattice containing 28 elements
            sage: G = F.relabel(C.face_by_face_lattice_index)
            sage: G.level_sets()[0]
            [A -1-dimensional face of a 3-dimensional combinatorial polyhedron]
            sage: G.level_sets()[3]
            [A 2-dimensional face of a 3-dimensional combinatorial polyhedron,
             A 2-dimensional face of a 3-dimensional combinatorial polyhedron,
             A 2-dimensional face of a 3-dimensional combinatorial polyhedron,
             A 2-dimensional face of a 3-dimensional combinatorial polyhedron,
             A 2-dimensional face of a 3-dimensional combinatorial polyhedron,
             A 2-dimensional face of a 3-dimensional combinatorial polyhedron]

            sage: P = Polyhedron(rays=[[0,1], [1,0]])
            sage: C = CombinatorialPolyhedron(P)
            sage: F = C.face_lattice()                                                  # needs sage.combinat
            sage: G = F.relabel(C.face_by_face_lattice_index)                           # needs sage.combinat
            sage: G._elements                                                           # needs sage.combinat
            (A -1-dimensional face of a 2-dimensional combinatorial polyhedron,
              A 0-dimensional face of a 2-dimensional combinatorial polyhedron,
              A 1-dimensional face of a 2-dimensional combinatorial polyhedron,
              A 1-dimensional face of a 2-dimensional combinatorial polyhedron,
              A 2-dimensional face of a 2-dimensional combinatorial polyhedron)

            sage: def f(i): return C.face_by_face_lattice_index(i).ambient_V_indices()
            sage: G = F.relabel(f)                                                      # needs sage.combinat
            sage: G._elements                                                           # needs sage.combinat
            ((), (0,), (0, 1), (0, 2), (0, 1, 2))"""
    @overload
    def face_generator(self, dimension=..., algorithm=...) -> Any:
        """CombinatorialPolyhedron.face_generator(self, dimension=None, algorithm=None)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 2662)

        Iterator over all proper faces of specified dimension.

        INPUT:

        - ``dimension`` -- if specified, then iterate over only this dimension

        - ``algorithm`` -- string (optional);
          specify whether the face generator starts with facets or vertices:

          * ``'primal'`` -- start with the facets
          * ``'dual'`` -- start with the vertices
          * ``None`` -- choose automatically

        OUTPUT: :class:`~sage.geometry.polyhedron.combinatorial_polyhedron.face_iterator.FaceIterator`

        .. NOTE::

            :class:`~sage.geometry.polyhedron.combinatorial_polyhedron.face_iterator.FaceIterator`
            can ignore subfaces or supfaces of the current face.

        EXAMPLES::

            sage: # needs sage.combinat
            sage: P = polytopes.permutahedron(5)
            sage: C = CombinatorialPolyhedron(P)
            sage: it = C.face_generator(dimension=2)
            sage: face = next(it); face
            A 2-dimensional face of a 4-dimensional combinatorial polyhedron
            sage: face.ambient_Vrepresentation()
            (A vertex at (1, 3, 2, 5, 4),
             A vertex at (2, 3, 1, 5, 4),
             A vertex at (3, 1, 2, 5, 4),
             A vertex at (3, 2, 1, 5, 4),
             A vertex at (2, 1, 3, 5, 4),
             A vertex at (1, 2, 3, 5, 4))
            sage: face = next(it); face
            A 2-dimensional face of a 4-dimensional combinatorial polyhedron
            sage: face.ambient_Vrepresentation()
            (A vertex at (2, 1, 4, 5, 3),
             A vertex at (3, 2, 4, 5, 1),
             A vertex at (3, 1, 4, 5, 2),
             A vertex at (1, 3, 4, 5, 2),
             A vertex at (1, 2, 4, 5, 3),
             A vertex at (2, 3, 4, 5, 1))
            sage: face.ambient_Hrepresentation()
            (An inequality (0, 0, -1, -1, 0) x + 9 >= 0,
             An inequality (0, 0, 0, -1, 0) x + 5 >= 0,
             An equation (1, 1, 1, 1, 1) x - 15 == 0)
            sage: face.ambient_H_indices()
            (25, 29, 30)
            sage: face = next(it); face
            A 2-dimensional face of a 4-dimensional combinatorial polyhedron
            sage: face.ambient_H_indices()
            (24, 29, 30)
            sage: face.ambient_V_indices()
            (32, 89, 90, 94)

            sage: C = CombinatorialPolyhedron([[0,1,2],[0,1,3],[0,2,3],[1,2,3]])
            sage: it = C.face_generator()
            sage: for face in it: face.ambient_Vrepresentation()
            (1, 2, 3)
            (0, 2, 3)
            (0, 1, 3)
            (0, 1, 2)
            (2, 3)
            (1, 3)
            (1, 2)
            (3,)
            (2,)
            (1,)
            (0, 3)
            (0, 2)
            (0,)
            (0, 1)

            sage: P = Polyhedron(rays=[[1,0],[0,1]], vertices=[[1,0],[0,1]])
            sage: C = CombinatorialPolyhedron(P)
            sage: it = C.face_generator(1)
            sage: for face in it: face.ambient_Vrepresentation()
            (A vertex at (0, 1), A vertex at (1, 0))
            (A ray in the direction (1, 0), A vertex at (1, 0))
            (A ray in the direction (0, 1), A vertex at (0, 1))

        .. SEEALSO::

            :class:`~sage.geometry.polyhedron.combinatorial_polyhedron.face_iterator.FaceIterator`,
            :class:`~sage.geometry.polyhedron.combinatorial_polyhedron.combinatorial_face.CombinatorialFace`."""
    @overload
    def face_generator(self, dimension=...) -> Any:
        """CombinatorialPolyhedron.face_generator(self, dimension=None, algorithm=None)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 2662)

        Iterator over all proper faces of specified dimension.

        INPUT:

        - ``dimension`` -- if specified, then iterate over only this dimension

        - ``algorithm`` -- string (optional);
          specify whether the face generator starts with facets or vertices:

          * ``'primal'`` -- start with the facets
          * ``'dual'`` -- start with the vertices
          * ``None`` -- choose automatically

        OUTPUT: :class:`~sage.geometry.polyhedron.combinatorial_polyhedron.face_iterator.FaceIterator`

        .. NOTE::

            :class:`~sage.geometry.polyhedron.combinatorial_polyhedron.face_iterator.FaceIterator`
            can ignore subfaces or supfaces of the current face.

        EXAMPLES::

            sage: # needs sage.combinat
            sage: P = polytopes.permutahedron(5)
            sage: C = CombinatorialPolyhedron(P)
            sage: it = C.face_generator(dimension=2)
            sage: face = next(it); face
            A 2-dimensional face of a 4-dimensional combinatorial polyhedron
            sage: face.ambient_Vrepresentation()
            (A vertex at (1, 3, 2, 5, 4),
             A vertex at (2, 3, 1, 5, 4),
             A vertex at (3, 1, 2, 5, 4),
             A vertex at (3, 2, 1, 5, 4),
             A vertex at (2, 1, 3, 5, 4),
             A vertex at (1, 2, 3, 5, 4))
            sage: face = next(it); face
            A 2-dimensional face of a 4-dimensional combinatorial polyhedron
            sage: face.ambient_Vrepresentation()
            (A vertex at (2, 1, 4, 5, 3),
             A vertex at (3, 2, 4, 5, 1),
             A vertex at (3, 1, 4, 5, 2),
             A vertex at (1, 3, 4, 5, 2),
             A vertex at (1, 2, 4, 5, 3),
             A vertex at (2, 3, 4, 5, 1))
            sage: face.ambient_Hrepresentation()
            (An inequality (0, 0, -1, -1, 0) x + 9 >= 0,
             An inequality (0, 0, 0, -1, 0) x + 5 >= 0,
             An equation (1, 1, 1, 1, 1) x - 15 == 0)
            sage: face.ambient_H_indices()
            (25, 29, 30)
            sage: face = next(it); face
            A 2-dimensional face of a 4-dimensional combinatorial polyhedron
            sage: face.ambient_H_indices()
            (24, 29, 30)
            sage: face.ambient_V_indices()
            (32, 89, 90, 94)

            sage: C = CombinatorialPolyhedron([[0,1,2],[0,1,3],[0,2,3],[1,2,3]])
            sage: it = C.face_generator()
            sage: for face in it: face.ambient_Vrepresentation()
            (1, 2, 3)
            (0, 2, 3)
            (0, 1, 3)
            (0, 1, 2)
            (2, 3)
            (1, 3)
            (1, 2)
            (3,)
            (2,)
            (1,)
            (0, 3)
            (0, 2)
            (0,)
            (0, 1)

            sage: P = Polyhedron(rays=[[1,0],[0,1]], vertices=[[1,0],[0,1]])
            sage: C = CombinatorialPolyhedron(P)
            sage: it = C.face_generator(1)
            sage: for face in it: face.ambient_Vrepresentation()
            (A vertex at (0, 1), A vertex at (1, 0))
            (A ray in the direction (1, 0), A vertex at (1, 0))
            (A ray in the direction (0, 1), A vertex at (0, 1))

        .. SEEALSO::

            :class:`~sage.geometry.polyhedron.combinatorial_polyhedron.face_iterator.FaceIterator`,
            :class:`~sage.geometry.polyhedron.combinatorial_polyhedron.combinatorial_face.CombinatorialFace`."""
    @overload
    def face_generator(self) -> Any:
        """CombinatorialPolyhedron.face_generator(self, dimension=None, algorithm=None)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 2662)

        Iterator over all proper faces of specified dimension.

        INPUT:

        - ``dimension`` -- if specified, then iterate over only this dimension

        - ``algorithm`` -- string (optional);
          specify whether the face generator starts with facets or vertices:

          * ``'primal'`` -- start with the facets
          * ``'dual'`` -- start with the vertices
          * ``None`` -- choose automatically

        OUTPUT: :class:`~sage.geometry.polyhedron.combinatorial_polyhedron.face_iterator.FaceIterator`

        .. NOTE::

            :class:`~sage.geometry.polyhedron.combinatorial_polyhedron.face_iterator.FaceIterator`
            can ignore subfaces or supfaces of the current face.

        EXAMPLES::

            sage: # needs sage.combinat
            sage: P = polytopes.permutahedron(5)
            sage: C = CombinatorialPolyhedron(P)
            sage: it = C.face_generator(dimension=2)
            sage: face = next(it); face
            A 2-dimensional face of a 4-dimensional combinatorial polyhedron
            sage: face.ambient_Vrepresentation()
            (A vertex at (1, 3, 2, 5, 4),
             A vertex at (2, 3, 1, 5, 4),
             A vertex at (3, 1, 2, 5, 4),
             A vertex at (3, 2, 1, 5, 4),
             A vertex at (2, 1, 3, 5, 4),
             A vertex at (1, 2, 3, 5, 4))
            sage: face = next(it); face
            A 2-dimensional face of a 4-dimensional combinatorial polyhedron
            sage: face.ambient_Vrepresentation()
            (A vertex at (2, 1, 4, 5, 3),
             A vertex at (3, 2, 4, 5, 1),
             A vertex at (3, 1, 4, 5, 2),
             A vertex at (1, 3, 4, 5, 2),
             A vertex at (1, 2, 4, 5, 3),
             A vertex at (2, 3, 4, 5, 1))
            sage: face.ambient_Hrepresentation()
            (An inequality (0, 0, -1, -1, 0) x + 9 >= 0,
             An inequality (0, 0, 0, -1, 0) x + 5 >= 0,
             An equation (1, 1, 1, 1, 1) x - 15 == 0)
            sage: face.ambient_H_indices()
            (25, 29, 30)
            sage: face = next(it); face
            A 2-dimensional face of a 4-dimensional combinatorial polyhedron
            sage: face.ambient_H_indices()
            (24, 29, 30)
            sage: face.ambient_V_indices()
            (32, 89, 90, 94)

            sage: C = CombinatorialPolyhedron([[0,1,2],[0,1,3],[0,2,3],[1,2,3]])
            sage: it = C.face_generator()
            sage: for face in it: face.ambient_Vrepresentation()
            (1, 2, 3)
            (0, 2, 3)
            (0, 1, 3)
            (0, 1, 2)
            (2, 3)
            (1, 3)
            (1, 2)
            (3,)
            (2,)
            (1,)
            (0, 3)
            (0, 2)
            (0,)
            (0, 1)

            sage: P = Polyhedron(rays=[[1,0],[0,1]], vertices=[[1,0],[0,1]])
            sage: C = CombinatorialPolyhedron(P)
            sage: it = C.face_generator(1)
            sage: for face in it: face.ambient_Vrepresentation()
            (A vertex at (0, 1), A vertex at (1, 0))
            (A ray in the direction (1, 0), A vertex at (1, 0))
            (A ray in the direction (0, 1), A vertex at (0, 1))

        .. SEEALSO::

            :class:`~sage.geometry.polyhedron.combinatorial_polyhedron.face_iterator.FaceIterator`,
            :class:`~sage.geometry.polyhedron.combinatorial_polyhedron.combinatorial_face.CombinatorialFace`."""
    def face_iter(self, *args, **kwargs):
        """CombinatorialPolyhedron.face_generator(self, dimension=None, algorithm=None)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 2662)

        Iterator over all proper faces of specified dimension.

        INPUT:

        - ``dimension`` -- if specified, then iterate over only this dimension

        - ``algorithm`` -- string (optional);
          specify whether the face generator starts with facets or vertices:

          * ``'primal'`` -- start with the facets
          * ``'dual'`` -- start with the vertices
          * ``None`` -- choose automatically

        OUTPUT: :class:`~sage.geometry.polyhedron.combinatorial_polyhedron.face_iterator.FaceIterator`

        .. NOTE::

            :class:`~sage.geometry.polyhedron.combinatorial_polyhedron.face_iterator.FaceIterator`
            can ignore subfaces or supfaces of the current face.

        EXAMPLES::

            sage: # needs sage.combinat
            sage: P = polytopes.permutahedron(5)
            sage: C = CombinatorialPolyhedron(P)
            sage: it = C.face_generator(dimension=2)
            sage: face = next(it); face
            A 2-dimensional face of a 4-dimensional combinatorial polyhedron
            sage: face.ambient_Vrepresentation()
            (A vertex at (1, 3, 2, 5, 4),
             A vertex at (2, 3, 1, 5, 4),
             A vertex at (3, 1, 2, 5, 4),
             A vertex at (3, 2, 1, 5, 4),
             A vertex at (2, 1, 3, 5, 4),
             A vertex at (1, 2, 3, 5, 4))
            sage: face = next(it); face
            A 2-dimensional face of a 4-dimensional combinatorial polyhedron
            sage: face.ambient_Vrepresentation()
            (A vertex at (2, 1, 4, 5, 3),
             A vertex at (3, 2, 4, 5, 1),
             A vertex at (3, 1, 4, 5, 2),
             A vertex at (1, 3, 4, 5, 2),
             A vertex at (1, 2, 4, 5, 3),
             A vertex at (2, 3, 4, 5, 1))
            sage: face.ambient_Hrepresentation()
            (An inequality (0, 0, -1, -1, 0) x + 9 >= 0,
             An inequality (0, 0, 0, -1, 0) x + 5 >= 0,
             An equation (1, 1, 1, 1, 1) x - 15 == 0)
            sage: face.ambient_H_indices()
            (25, 29, 30)
            sage: face = next(it); face
            A 2-dimensional face of a 4-dimensional combinatorial polyhedron
            sage: face.ambient_H_indices()
            (24, 29, 30)
            sage: face.ambient_V_indices()
            (32, 89, 90, 94)

            sage: C = CombinatorialPolyhedron([[0,1,2],[0,1,3],[0,2,3],[1,2,3]])
            sage: it = C.face_generator()
            sage: for face in it: face.ambient_Vrepresentation()
            (1, 2, 3)
            (0, 2, 3)
            (0, 1, 3)
            (0, 1, 2)
            (2, 3)
            (1, 3)
            (1, 2)
            (3,)
            (2,)
            (1,)
            (0, 3)
            (0, 2)
            (0,)
            (0, 1)

            sage: P = Polyhedron(rays=[[1,0],[0,1]], vertices=[[1,0],[0,1]])
            sage: C = CombinatorialPolyhedron(P)
            sage: it = C.face_generator(1)
            sage: for face in it: face.ambient_Vrepresentation()
            (A vertex at (0, 1), A vertex at (1, 0))
            (A ray in the direction (1, 0), A vertex at (1, 0))
            (A ray in the direction (0, 1), A vertex at (0, 1))

        .. SEEALSO::

            :class:`~sage.geometry.polyhedron.combinatorial_polyhedron.face_iterator.FaceIterator`,
            :class:`~sage.geometry.polyhedron.combinatorial_polyhedron.combinatorial_face.CombinatorialFace`."""
    @overload
    def face_lattice(self) -> Any:
        """CombinatorialPolyhedron.face_lattice(self)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 2784)

        Generate the face-lattice.

        OUTPUT: :class:`~sage.combinat.posets.lattices.FiniteLatticePoset`

        .. NOTE::

            Use :meth:`CombinatorialPolyhedron.face_by_face_lattice_index` to get
            the face for each index.

        .. WARNING::

            The labeling of the face lattice might depend on architecture
            and implementation. Relabeling the face lattice with
            :meth:`CombinatorialPolyhedron.face_by_face_lattice_index` or
            the properties obtained from this face will be platform independent.

        EXAMPLES::

            sage: P = Polyhedron(rays=[[1,0],[0,1]])
            sage: C = CombinatorialPolyhedron(P)
            sage: C.face_lattice()                                                      # needs sage.combinat
            Finite lattice containing 5 elements

            sage: P = Polyhedron(rays=[[1,0,0], [-1,0,0], [0,-1,0], [0,1,0]])
            sage: C = CombinatorialPolyhedron(P)
            sage: P1 = Polyhedron(rays=[[1,0], [-1,0]])
            sage: C1 = CombinatorialPolyhedron(P1)
            sage: C.face_lattice().is_isomorphic(C1.face_lattice())                     # needs sage.combinat
            True

            sage: P = polytopes.permutahedron(5)
            sage: C = CombinatorialPolyhedron(P)
            sage: C.face_lattice()                                                      # needs sage.combinat
            Finite lattice containing 542 elements

        TESTS::

            sage: P = polytopes.cyclic_polytope(4,10)
            sage: C = CombinatorialPolyhedron(P)
            sage: C.face_lattice().is_isomorphic(P.face_lattice())                      # needs sage.combinat
            True

            sage: P = polytopes.permutahedron(4)
            sage: C = CombinatorialPolyhedron(P)
            sage: C.face_lattice().is_isomorphic(P.face_lattice())                      # needs sage.combinat
            True"""
    @overload
    def face_lattice(self) -> Any:
        """CombinatorialPolyhedron.face_lattice(self)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 2784)

        Generate the face-lattice.

        OUTPUT: :class:`~sage.combinat.posets.lattices.FiniteLatticePoset`

        .. NOTE::

            Use :meth:`CombinatorialPolyhedron.face_by_face_lattice_index` to get
            the face for each index.

        .. WARNING::

            The labeling of the face lattice might depend on architecture
            and implementation. Relabeling the face lattice with
            :meth:`CombinatorialPolyhedron.face_by_face_lattice_index` or
            the properties obtained from this face will be platform independent.

        EXAMPLES::

            sage: P = Polyhedron(rays=[[1,0],[0,1]])
            sage: C = CombinatorialPolyhedron(P)
            sage: C.face_lattice()                                                      # needs sage.combinat
            Finite lattice containing 5 elements

            sage: P = Polyhedron(rays=[[1,0,0], [-1,0,0], [0,-1,0], [0,1,0]])
            sage: C = CombinatorialPolyhedron(P)
            sage: P1 = Polyhedron(rays=[[1,0], [-1,0]])
            sage: C1 = CombinatorialPolyhedron(P1)
            sage: C.face_lattice().is_isomorphic(C1.face_lattice())                     # needs sage.combinat
            True

            sage: P = polytopes.permutahedron(5)
            sage: C = CombinatorialPolyhedron(P)
            sage: C.face_lattice()                                                      # needs sage.combinat
            Finite lattice containing 542 elements

        TESTS::

            sage: P = polytopes.cyclic_polytope(4,10)
            sage: C = CombinatorialPolyhedron(P)
            sage: C.face_lattice().is_isomorphic(P.face_lattice())                      # needs sage.combinat
            True

            sage: P = polytopes.permutahedron(4)
            sage: C = CombinatorialPolyhedron(P)
            sage: C.face_lattice().is_isomorphic(P.face_lattice())                      # needs sage.combinat
            True"""
    @overload
    def face_lattice(self) -> Any:
        """CombinatorialPolyhedron.face_lattice(self)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 2784)

        Generate the face-lattice.

        OUTPUT: :class:`~sage.combinat.posets.lattices.FiniteLatticePoset`

        .. NOTE::

            Use :meth:`CombinatorialPolyhedron.face_by_face_lattice_index` to get
            the face for each index.

        .. WARNING::

            The labeling of the face lattice might depend on architecture
            and implementation. Relabeling the face lattice with
            :meth:`CombinatorialPolyhedron.face_by_face_lattice_index` or
            the properties obtained from this face will be platform independent.

        EXAMPLES::

            sage: P = Polyhedron(rays=[[1,0],[0,1]])
            sage: C = CombinatorialPolyhedron(P)
            sage: C.face_lattice()                                                      # needs sage.combinat
            Finite lattice containing 5 elements

            sage: P = Polyhedron(rays=[[1,0,0], [-1,0,0], [0,-1,0], [0,1,0]])
            sage: C = CombinatorialPolyhedron(P)
            sage: P1 = Polyhedron(rays=[[1,0], [-1,0]])
            sage: C1 = CombinatorialPolyhedron(P1)
            sage: C.face_lattice().is_isomorphic(C1.face_lattice())                     # needs sage.combinat
            True

            sage: P = polytopes.permutahedron(5)
            sage: C = CombinatorialPolyhedron(P)
            sage: C.face_lattice()                                                      # needs sage.combinat
            Finite lattice containing 542 elements

        TESTS::

            sage: P = polytopes.cyclic_polytope(4,10)
            sage: C = CombinatorialPolyhedron(P)
            sage: C.face_lattice().is_isomorphic(P.face_lattice())                      # needs sage.combinat
            True

            sage: P = polytopes.permutahedron(4)
            sage: C = CombinatorialPolyhedron(P)
            sage: C.face_lattice().is_isomorphic(P.face_lattice())                      # needs sage.combinat
            True"""
    @overload
    def face_lattice(self) -> Any:
        """CombinatorialPolyhedron.face_lattice(self)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 2784)

        Generate the face-lattice.

        OUTPUT: :class:`~sage.combinat.posets.lattices.FiniteLatticePoset`

        .. NOTE::

            Use :meth:`CombinatorialPolyhedron.face_by_face_lattice_index` to get
            the face for each index.

        .. WARNING::

            The labeling of the face lattice might depend on architecture
            and implementation. Relabeling the face lattice with
            :meth:`CombinatorialPolyhedron.face_by_face_lattice_index` or
            the properties obtained from this face will be platform independent.

        EXAMPLES::

            sage: P = Polyhedron(rays=[[1,0],[0,1]])
            sage: C = CombinatorialPolyhedron(P)
            sage: C.face_lattice()                                                      # needs sage.combinat
            Finite lattice containing 5 elements

            sage: P = Polyhedron(rays=[[1,0,0], [-1,0,0], [0,-1,0], [0,1,0]])
            sage: C = CombinatorialPolyhedron(P)
            sage: P1 = Polyhedron(rays=[[1,0], [-1,0]])
            sage: C1 = CombinatorialPolyhedron(P1)
            sage: C.face_lattice().is_isomorphic(C1.face_lattice())                     # needs sage.combinat
            True

            sage: P = polytopes.permutahedron(5)
            sage: C = CombinatorialPolyhedron(P)
            sage: C.face_lattice()                                                      # needs sage.combinat
            Finite lattice containing 542 elements

        TESTS::

            sage: P = polytopes.cyclic_polytope(4,10)
            sage: C = CombinatorialPolyhedron(P)
            sage: C.face_lattice().is_isomorphic(P.face_lattice())                      # needs sage.combinat
            True

            sage: P = polytopes.permutahedron(4)
            sage: C = CombinatorialPolyhedron(P)
            sage: C.face_lattice().is_isomorphic(P.face_lattice())                      # needs sage.combinat
            True"""
    @overload
    def face_lattice(self) -> Any:
        """CombinatorialPolyhedron.face_lattice(self)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 2784)

        Generate the face-lattice.

        OUTPUT: :class:`~sage.combinat.posets.lattices.FiniteLatticePoset`

        .. NOTE::

            Use :meth:`CombinatorialPolyhedron.face_by_face_lattice_index` to get
            the face for each index.

        .. WARNING::

            The labeling of the face lattice might depend on architecture
            and implementation. Relabeling the face lattice with
            :meth:`CombinatorialPolyhedron.face_by_face_lattice_index` or
            the properties obtained from this face will be platform independent.

        EXAMPLES::

            sage: P = Polyhedron(rays=[[1,0],[0,1]])
            sage: C = CombinatorialPolyhedron(P)
            sage: C.face_lattice()                                                      # needs sage.combinat
            Finite lattice containing 5 elements

            sage: P = Polyhedron(rays=[[1,0,0], [-1,0,0], [0,-1,0], [0,1,0]])
            sage: C = CombinatorialPolyhedron(P)
            sage: P1 = Polyhedron(rays=[[1,0], [-1,0]])
            sage: C1 = CombinatorialPolyhedron(P1)
            sage: C.face_lattice().is_isomorphic(C1.face_lattice())                     # needs sage.combinat
            True

            sage: P = polytopes.permutahedron(5)
            sage: C = CombinatorialPolyhedron(P)
            sage: C.face_lattice()                                                      # needs sage.combinat
            Finite lattice containing 542 elements

        TESTS::

            sage: P = polytopes.cyclic_polytope(4,10)
            sage: C = CombinatorialPolyhedron(P)
            sage: C.face_lattice().is_isomorphic(P.face_lattice())                      # needs sage.combinat
            True

            sage: P = polytopes.permutahedron(4)
            sage: C = CombinatorialPolyhedron(P)
            sage: C.face_lattice().is_isomorphic(P.face_lattice())                      # needs sage.combinat
            True"""
    @overload
    def face_lattice(self) -> Any:
        """CombinatorialPolyhedron.face_lattice(self)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 2784)

        Generate the face-lattice.

        OUTPUT: :class:`~sage.combinat.posets.lattices.FiniteLatticePoset`

        .. NOTE::

            Use :meth:`CombinatorialPolyhedron.face_by_face_lattice_index` to get
            the face for each index.

        .. WARNING::

            The labeling of the face lattice might depend on architecture
            and implementation. Relabeling the face lattice with
            :meth:`CombinatorialPolyhedron.face_by_face_lattice_index` or
            the properties obtained from this face will be platform independent.

        EXAMPLES::

            sage: P = Polyhedron(rays=[[1,0],[0,1]])
            sage: C = CombinatorialPolyhedron(P)
            sage: C.face_lattice()                                                      # needs sage.combinat
            Finite lattice containing 5 elements

            sage: P = Polyhedron(rays=[[1,0,0], [-1,0,0], [0,-1,0], [0,1,0]])
            sage: C = CombinatorialPolyhedron(P)
            sage: P1 = Polyhedron(rays=[[1,0], [-1,0]])
            sage: C1 = CombinatorialPolyhedron(P1)
            sage: C.face_lattice().is_isomorphic(C1.face_lattice())                     # needs sage.combinat
            True

            sage: P = polytopes.permutahedron(5)
            sage: C = CombinatorialPolyhedron(P)
            sage: C.face_lattice()                                                      # needs sage.combinat
            Finite lattice containing 542 elements

        TESTS::

            sage: P = polytopes.cyclic_polytope(4,10)
            sage: C = CombinatorialPolyhedron(P)
            sage: C.face_lattice().is_isomorphic(P.face_lattice())                      # needs sage.combinat
            True

            sage: P = polytopes.permutahedron(4)
            sage: C = CombinatorialPolyhedron(P)
            sage: C.face_lattice().is_isomorphic(P.face_lattice())                      # needs sage.combinat
            True"""
    @overload
    def facet_adjacency_matrix(self, algorithm=...) -> Any:
        """CombinatorialPolyhedron.facet_adjacency_matrix(self, algorithm=None)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 1479)

        Return the binary matrix of facet adjacencies.

        INPUT:

        - ``algorithm`` -- string (optional);
          specify whether the face generator starts with facets or vertices:
          * ``'primal'`` -- start with the facets
          * ``'dual'`` -- start with the vertices
          * ``None`` -- choose automatically

        .. SEEALSO::

            :meth:`~sage.geometry.polyhedron.base.Polyhedron_base.vertex_adjacency_matrix`.

        EXAMPLES::

            sage: P = polytopes.cube()
            sage: C = P.combinatorial_polyhedron()
            sage: C.facet_adjacency_matrix()
            [0 1 1 0 1 1]
            [1 0 1 1 1 0]
            [1 1 0 1 0 1]
            [0 1 1 0 1 1]
            [1 1 0 1 0 1]
            [1 0 1 1 1 0]

        TESTS::

            sage: CombinatorialPolyhedron(-1).facet_adjacency_matrix()
            []
            sage: CombinatorialPolyhedron(0).facet_adjacency_matrix()
            []
            sage: polytopes.cube().facet_adjacency_matrix().is_immutable()
            True"""
    @overload
    def facet_adjacency_matrix(self) -> Any:
        """CombinatorialPolyhedron.facet_adjacency_matrix(self, algorithm=None)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 1479)

        Return the binary matrix of facet adjacencies.

        INPUT:

        - ``algorithm`` -- string (optional);
          specify whether the face generator starts with facets or vertices:
          * ``'primal'`` -- start with the facets
          * ``'dual'`` -- start with the vertices
          * ``None`` -- choose automatically

        .. SEEALSO::

            :meth:`~sage.geometry.polyhedron.base.Polyhedron_base.vertex_adjacency_matrix`.

        EXAMPLES::

            sage: P = polytopes.cube()
            sage: C = P.combinatorial_polyhedron()
            sage: C.facet_adjacency_matrix()
            [0 1 1 0 1 1]
            [1 0 1 1 1 0]
            [1 1 0 1 0 1]
            [0 1 1 0 1 1]
            [1 1 0 1 0 1]
            [1 0 1 1 1 0]

        TESTS::

            sage: CombinatorialPolyhedron(-1).facet_adjacency_matrix()
            []
            sage: CombinatorialPolyhedron(0).facet_adjacency_matrix()
            []
            sage: polytopes.cube().facet_adjacency_matrix().is_immutable()
            True"""
    @overload
    def facet_adjacency_matrix(self) -> Any:
        """CombinatorialPolyhedron.facet_adjacency_matrix(self, algorithm=None)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 1479)

        Return the binary matrix of facet adjacencies.

        INPUT:

        - ``algorithm`` -- string (optional);
          specify whether the face generator starts with facets or vertices:
          * ``'primal'`` -- start with the facets
          * ``'dual'`` -- start with the vertices
          * ``None`` -- choose automatically

        .. SEEALSO::

            :meth:`~sage.geometry.polyhedron.base.Polyhedron_base.vertex_adjacency_matrix`.

        EXAMPLES::

            sage: P = polytopes.cube()
            sage: C = P.combinatorial_polyhedron()
            sage: C.facet_adjacency_matrix()
            [0 1 1 0 1 1]
            [1 0 1 1 1 0]
            [1 1 0 1 0 1]
            [0 1 1 0 1 1]
            [1 1 0 1 0 1]
            [1 0 1 1 1 0]

        TESTS::

            sage: CombinatorialPolyhedron(-1).facet_adjacency_matrix()
            []
            sage: CombinatorialPolyhedron(0).facet_adjacency_matrix()
            []
            sage: polytopes.cube().facet_adjacency_matrix().is_immutable()
            True"""
    @overload
    def facet_adjacency_matrix(self) -> Any:
        """CombinatorialPolyhedron.facet_adjacency_matrix(self, algorithm=None)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 1479)

        Return the binary matrix of facet adjacencies.

        INPUT:

        - ``algorithm`` -- string (optional);
          specify whether the face generator starts with facets or vertices:
          * ``'primal'`` -- start with the facets
          * ``'dual'`` -- start with the vertices
          * ``None`` -- choose automatically

        .. SEEALSO::

            :meth:`~sage.geometry.polyhedron.base.Polyhedron_base.vertex_adjacency_matrix`.

        EXAMPLES::

            sage: P = polytopes.cube()
            sage: C = P.combinatorial_polyhedron()
            sage: C.facet_adjacency_matrix()
            [0 1 1 0 1 1]
            [1 0 1 1 1 0]
            [1 1 0 1 0 1]
            [0 1 1 0 1 1]
            [1 1 0 1 0 1]
            [1 0 1 1 1 0]

        TESTS::

            sage: CombinatorialPolyhedron(-1).facet_adjacency_matrix()
            []
            sage: CombinatorialPolyhedron(0).facet_adjacency_matrix()
            []
            sage: polytopes.cube().facet_adjacency_matrix().is_immutable()
            True"""
    @overload
    def facet_adjacency_matrix(self) -> Any:
        """CombinatorialPolyhedron.facet_adjacency_matrix(self, algorithm=None)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 1479)

        Return the binary matrix of facet adjacencies.

        INPUT:

        - ``algorithm`` -- string (optional);
          specify whether the face generator starts with facets or vertices:
          * ``'primal'`` -- start with the facets
          * ``'dual'`` -- start with the vertices
          * ``None`` -- choose automatically

        .. SEEALSO::

            :meth:`~sage.geometry.polyhedron.base.Polyhedron_base.vertex_adjacency_matrix`.

        EXAMPLES::

            sage: P = polytopes.cube()
            sage: C = P.combinatorial_polyhedron()
            sage: C.facet_adjacency_matrix()
            [0 1 1 0 1 1]
            [1 0 1 1 1 0]
            [1 1 0 1 0 1]
            [0 1 1 0 1 1]
            [1 1 0 1 0 1]
            [1 0 1 1 1 0]

        TESTS::

            sage: CombinatorialPolyhedron(-1).facet_adjacency_matrix()
            []
            sage: CombinatorialPolyhedron(0).facet_adjacency_matrix()
            []
            sage: polytopes.cube().facet_adjacency_matrix().is_immutable()
            True"""
    @overload
    def facet_graph(self, names=..., algorithm=...) -> Any:
        """CombinatorialPolyhedron.facet_graph(self, names=True, algorithm=None)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 1532)

        Return the facet graph.

        The facet graph of a polyhedron consists of
        ridges as edges and facets as vertices.

        INPUT:

        - ``algorithm`` -- string (optional);
          specify whether the face generator starts with facets or vertices:

          * ``'primal'`` -- start with the facets
          * ``'dual'`` -- start with the vertices
          * ``None`` -- choose automatically

        If ``names`` is ``False``, the ``vertices`` of the graph will
        be the indices of the facets in the Hrepresentation.

        EXAMPLES::

            sage: P = polytopes.cyclic_polytope(4,6)
            sage: C = CombinatorialPolyhedron(P)
            sage: C.facet_graph()                                                       # needs sage.graphs
            Graph on 9 vertices

        TESTS::

            sage: P = Polyhedron(ieqs=[[1,-1,0],[1,1,0]])
            sage: CombinatorialPolyhedron(P).facet_graph()                              # needs sage.graphs
            Graph on 2 vertices

        Checking that :issue:`28604` is fixed::

            sage: C = CombinatorialPolyhedron(polytopes.cube()); C
            A 3-dimensional combinatorial polyhedron with 6 facets
            sage: C.facet_graph(names=False)                                            # needs sage.graphs
            Graph on 6 vertices

            sage: C = CombinatorialPolyhedron(polytopes.hypersimplex(5,2)); C
            A 4-dimensional combinatorial polyhedron with 10 facets
            sage: C.facet_graph()                                                       # needs sage.combinat sage.graphs
            Graph on 10 vertices"""
    @overload
    def facet_graph(self) -> Any:
        """CombinatorialPolyhedron.facet_graph(self, names=True, algorithm=None)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 1532)

        Return the facet graph.

        The facet graph of a polyhedron consists of
        ridges as edges and facets as vertices.

        INPUT:

        - ``algorithm`` -- string (optional);
          specify whether the face generator starts with facets or vertices:

          * ``'primal'`` -- start with the facets
          * ``'dual'`` -- start with the vertices
          * ``None`` -- choose automatically

        If ``names`` is ``False``, the ``vertices`` of the graph will
        be the indices of the facets in the Hrepresentation.

        EXAMPLES::

            sage: P = polytopes.cyclic_polytope(4,6)
            sage: C = CombinatorialPolyhedron(P)
            sage: C.facet_graph()                                                       # needs sage.graphs
            Graph on 9 vertices

        TESTS::

            sage: P = Polyhedron(ieqs=[[1,-1,0],[1,1,0]])
            sage: CombinatorialPolyhedron(P).facet_graph()                              # needs sage.graphs
            Graph on 2 vertices

        Checking that :issue:`28604` is fixed::

            sage: C = CombinatorialPolyhedron(polytopes.cube()); C
            A 3-dimensional combinatorial polyhedron with 6 facets
            sage: C.facet_graph(names=False)                                            # needs sage.graphs
            Graph on 6 vertices

            sage: C = CombinatorialPolyhedron(polytopes.hypersimplex(5,2)); C
            A 4-dimensional combinatorial polyhedron with 10 facets
            sage: C.facet_graph()                                                       # needs sage.combinat sage.graphs
            Graph on 10 vertices"""
    @overload
    def facet_graph(self) -> Any:
        """CombinatorialPolyhedron.facet_graph(self, names=True, algorithm=None)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 1532)

        Return the facet graph.

        The facet graph of a polyhedron consists of
        ridges as edges and facets as vertices.

        INPUT:

        - ``algorithm`` -- string (optional);
          specify whether the face generator starts with facets or vertices:

          * ``'primal'`` -- start with the facets
          * ``'dual'`` -- start with the vertices
          * ``None`` -- choose automatically

        If ``names`` is ``False``, the ``vertices`` of the graph will
        be the indices of the facets in the Hrepresentation.

        EXAMPLES::

            sage: P = polytopes.cyclic_polytope(4,6)
            sage: C = CombinatorialPolyhedron(P)
            sage: C.facet_graph()                                                       # needs sage.graphs
            Graph on 9 vertices

        TESTS::

            sage: P = Polyhedron(ieqs=[[1,-1,0],[1,1,0]])
            sage: CombinatorialPolyhedron(P).facet_graph()                              # needs sage.graphs
            Graph on 2 vertices

        Checking that :issue:`28604` is fixed::

            sage: C = CombinatorialPolyhedron(polytopes.cube()); C
            A 3-dimensional combinatorial polyhedron with 6 facets
            sage: C.facet_graph(names=False)                                            # needs sage.graphs
            Graph on 6 vertices

            sage: C = CombinatorialPolyhedron(polytopes.hypersimplex(5,2)); C
            A 4-dimensional combinatorial polyhedron with 10 facets
            sage: C.facet_graph()                                                       # needs sage.combinat sage.graphs
            Graph on 10 vertices"""
    @overload
    def facet_graph(self, names=...) -> Any:
        """CombinatorialPolyhedron.facet_graph(self, names=True, algorithm=None)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 1532)

        Return the facet graph.

        The facet graph of a polyhedron consists of
        ridges as edges and facets as vertices.

        INPUT:

        - ``algorithm`` -- string (optional);
          specify whether the face generator starts with facets or vertices:

          * ``'primal'`` -- start with the facets
          * ``'dual'`` -- start with the vertices
          * ``None`` -- choose automatically

        If ``names`` is ``False``, the ``vertices`` of the graph will
        be the indices of the facets in the Hrepresentation.

        EXAMPLES::

            sage: P = polytopes.cyclic_polytope(4,6)
            sage: C = CombinatorialPolyhedron(P)
            sage: C.facet_graph()                                                       # needs sage.graphs
            Graph on 9 vertices

        TESTS::

            sage: P = Polyhedron(ieqs=[[1,-1,0],[1,1,0]])
            sage: CombinatorialPolyhedron(P).facet_graph()                              # needs sage.graphs
            Graph on 2 vertices

        Checking that :issue:`28604` is fixed::

            sage: C = CombinatorialPolyhedron(polytopes.cube()); C
            A 3-dimensional combinatorial polyhedron with 6 facets
            sage: C.facet_graph(names=False)                                            # needs sage.graphs
            Graph on 6 vertices

            sage: C = CombinatorialPolyhedron(polytopes.hypersimplex(5,2)); C
            A 4-dimensional combinatorial polyhedron with 10 facets
            sage: C.facet_graph()                                                       # needs sage.combinat sage.graphs
            Graph on 10 vertices"""
    @overload
    def facet_graph(self) -> Any:
        """CombinatorialPolyhedron.facet_graph(self, names=True, algorithm=None)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 1532)

        Return the facet graph.

        The facet graph of a polyhedron consists of
        ridges as edges and facets as vertices.

        INPUT:

        - ``algorithm`` -- string (optional);
          specify whether the face generator starts with facets or vertices:

          * ``'primal'`` -- start with the facets
          * ``'dual'`` -- start with the vertices
          * ``None`` -- choose automatically

        If ``names`` is ``False``, the ``vertices`` of the graph will
        be the indices of the facets in the Hrepresentation.

        EXAMPLES::

            sage: P = polytopes.cyclic_polytope(4,6)
            sage: C = CombinatorialPolyhedron(P)
            sage: C.facet_graph()                                                       # needs sage.graphs
            Graph on 9 vertices

        TESTS::

            sage: P = Polyhedron(ieqs=[[1,-1,0],[1,1,0]])
            sage: CombinatorialPolyhedron(P).facet_graph()                              # needs sage.graphs
            Graph on 2 vertices

        Checking that :issue:`28604` is fixed::

            sage: C = CombinatorialPolyhedron(polytopes.cube()); C
            A 3-dimensional combinatorial polyhedron with 6 facets
            sage: C.facet_graph(names=False)                                            # needs sage.graphs
            Graph on 6 vertices

            sage: C = CombinatorialPolyhedron(polytopes.hypersimplex(5,2)); C
            A 4-dimensional combinatorial polyhedron with 10 facets
            sage: C.facet_graph()                                                       # needs sage.combinat sage.graphs
            Graph on 10 vertices"""
    @overload
    def facets(self, names=...) -> Any:
        """CombinatorialPolyhedron.facets(self, names=True)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 990)

        Return the facets as lists of ``[vertices, rays, lines]``.

        If ``names`` is ``False``, then the Vrepresentatives in the facets
        are given by their indices in the Vrepresentation.

        The facets are the maximal nontrivial faces.

        EXAMPLES::

            sage: P = polytopes.cube()
            sage: C = CombinatorialPolyhedron(P)
            sage: C.facets()
            ((A vertex at (1, -1, -1),
              A vertex at (1, 1, -1),
              A vertex at (1, 1, 1),
              A vertex at (1, -1, 1)),
             (A vertex at (1, 1, -1),
              A vertex at (1, 1, 1),
              A vertex at (-1, 1, -1),
              A vertex at (-1, 1, 1)),
             (A vertex at (1, 1, 1),
              A vertex at (1, -1, 1),
              A vertex at (-1, -1, 1),
              A vertex at (-1, 1, 1)),
             (A vertex at (-1, -1, 1),
              A vertex at (-1, -1, -1),
              A vertex at (-1, 1, -1),
              A vertex at (-1, 1, 1)),
             (A vertex at (1, -1, -1),
              A vertex at (1, 1, -1),
              A vertex at (-1, -1, -1),
              A vertex at (-1, 1, -1)),
             (A vertex at (1, -1, -1),
              A vertex at (1, -1, 1),
              A vertex at (-1, -1, 1),
              A vertex at (-1, -1, -1)))
            sage: C.facets(names=False)
            ((0, 1, 2, 3),
             (1, 2, 6, 7),
             (2, 3, 4, 7),
             (4, 5, 6, 7),
             (0, 1, 5, 6),
             (0, 3, 4, 5))

        The empty face is trivial and hence the ``0``-dimensional
        polyhedron does not have facets::

            sage: C = CombinatorialPolyhedron(0)
            sage: C.facets()
            ()"""
    @overload
    def facets(self) -> Any:
        """CombinatorialPolyhedron.facets(self, names=True)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 990)

        Return the facets as lists of ``[vertices, rays, lines]``.

        If ``names`` is ``False``, then the Vrepresentatives in the facets
        are given by their indices in the Vrepresentation.

        The facets are the maximal nontrivial faces.

        EXAMPLES::

            sage: P = polytopes.cube()
            sage: C = CombinatorialPolyhedron(P)
            sage: C.facets()
            ((A vertex at (1, -1, -1),
              A vertex at (1, 1, -1),
              A vertex at (1, 1, 1),
              A vertex at (1, -1, 1)),
             (A vertex at (1, 1, -1),
              A vertex at (1, 1, 1),
              A vertex at (-1, 1, -1),
              A vertex at (-1, 1, 1)),
             (A vertex at (1, 1, 1),
              A vertex at (1, -1, 1),
              A vertex at (-1, -1, 1),
              A vertex at (-1, 1, 1)),
             (A vertex at (-1, -1, 1),
              A vertex at (-1, -1, -1),
              A vertex at (-1, 1, -1),
              A vertex at (-1, 1, 1)),
             (A vertex at (1, -1, -1),
              A vertex at (1, 1, -1),
              A vertex at (-1, -1, -1),
              A vertex at (-1, 1, -1)),
             (A vertex at (1, -1, -1),
              A vertex at (1, -1, 1),
              A vertex at (-1, -1, 1),
              A vertex at (-1, -1, -1)))
            sage: C.facets(names=False)
            ((0, 1, 2, 3),
             (1, 2, 6, 7),
             (2, 3, 4, 7),
             (4, 5, 6, 7),
             (0, 1, 5, 6),
             (0, 3, 4, 5))

        The empty face is trivial and hence the ``0``-dimensional
        polyhedron does not have facets::

            sage: C = CombinatorialPolyhedron(0)
            sage: C.facets()
            ()"""
    @overload
    def facets(self, names=...) -> Any:
        """CombinatorialPolyhedron.facets(self, names=True)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 990)

        Return the facets as lists of ``[vertices, rays, lines]``.

        If ``names`` is ``False``, then the Vrepresentatives in the facets
        are given by their indices in the Vrepresentation.

        The facets are the maximal nontrivial faces.

        EXAMPLES::

            sage: P = polytopes.cube()
            sage: C = CombinatorialPolyhedron(P)
            sage: C.facets()
            ((A vertex at (1, -1, -1),
              A vertex at (1, 1, -1),
              A vertex at (1, 1, 1),
              A vertex at (1, -1, 1)),
             (A vertex at (1, 1, -1),
              A vertex at (1, 1, 1),
              A vertex at (-1, 1, -1),
              A vertex at (-1, 1, 1)),
             (A vertex at (1, 1, 1),
              A vertex at (1, -1, 1),
              A vertex at (-1, -1, 1),
              A vertex at (-1, 1, 1)),
             (A vertex at (-1, -1, 1),
              A vertex at (-1, -1, -1),
              A vertex at (-1, 1, -1),
              A vertex at (-1, 1, 1)),
             (A vertex at (1, -1, -1),
              A vertex at (1, 1, -1),
              A vertex at (-1, -1, -1),
              A vertex at (-1, 1, -1)),
             (A vertex at (1, -1, -1),
              A vertex at (1, -1, 1),
              A vertex at (-1, -1, 1),
              A vertex at (-1, -1, -1)))
            sage: C.facets(names=False)
            ((0, 1, 2, 3),
             (1, 2, 6, 7),
             (2, 3, 4, 7),
             (4, 5, 6, 7),
             (0, 1, 5, 6),
             (0, 3, 4, 5))

        The empty face is trivial and hence the ``0``-dimensional
        polyhedron does not have facets::

            sage: C = CombinatorialPolyhedron(0)
            sage: C.facets()
            ()"""
    @overload
    def facets(self) -> Any:
        """CombinatorialPolyhedron.facets(self, names=True)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 990)

        Return the facets as lists of ``[vertices, rays, lines]``.

        If ``names`` is ``False``, then the Vrepresentatives in the facets
        are given by their indices in the Vrepresentation.

        The facets are the maximal nontrivial faces.

        EXAMPLES::

            sage: P = polytopes.cube()
            sage: C = CombinatorialPolyhedron(P)
            sage: C.facets()
            ((A vertex at (1, -1, -1),
              A vertex at (1, 1, -1),
              A vertex at (1, 1, 1),
              A vertex at (1, -1, 1)),
             (A vertex at (1, 1, -1),
              A vertex at (1, 1, 1),
              A vertex at (-1, 1, -1),
              A vertex at (-1, 1, 1)),
             (A vertex at (1, 1, 1),
              A vertex at (1, -1, 1),
              A vertex at (-1, -1, 1),
              A vertex at (-1, 1, 1)),
             (A vertex at (-1, -1, 1),
              A vertex at (-1, -1, -1),
              A vertex at (-1, 1, -1),
              A vertex at (-1, 1, 1)),
             (A vertex at (1, -1, -1),
              A vertex at (1, 1, -1),
              A vertex at (-1, -1, -1),
              A vertex at (-1, 1, -1)),
             (A vertex at (1, -1, -1),
              A vertex at (1, -1, 1),
              A vertex at (-1, -1, 1),
              A vertex at (-1, -1, -1)))
            sage: C.facets(names=False)
            ((0, 1, 2, 3),
             (1, 2, 6, 7),
             (2, 3, 4, 7),
             (4, 5, 6, 7),
             (0, 1, 5, 6),
             (0, 3, 4, 5))

        The empty face is trivial and hence the ``0``-dimensional
        polyhedron does not have facets::

            sage: C = CombinatorialPolyhedron(0)
            sage: C.facets()
            ()"""
    def flag_f_vector(self, *args) -> Any:
        """CombinatorialPolyhedron.flag_f_vector(self, *args)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 1773)

        Return the flag f-vector.

        For each `-1 < i_0 < \\dots < i_n < d` the flag f-vector
        counts the number of flags `F_0 \\subset \\dots \\subset F_n`
        with `F_j` of dimension `i_j` for each `0 \\leq j \\leq n`,
        where `d` is the dimension of the polyhedron.

        INPUT:

        - ``args`` -- integer (optional); specify an entry of the
          flag-f-vector (must be an increasing sequence of integers)

        OUTPUT:

        - a dictionary, if no arguments were given

        - an integer, if arguments were given

        EXAMPLES:

        Obtain the entire flag-f-vector::

            sage: C = polytopes.hypercube(4).combinatorial_polyhedron()
            sage: C.flag_f_vector()                                                     # needs sage.combinat
                {(-1,): 1,
                 (0,): 16,
                 (0, 1): 64,
                 (0, 1, 2): 192,
                 (0, 1, 2, 3): 384,
                 (0, 1, 3): 192,
                 (0, 2): 96,
                 (0, 2, 3): 192,
                 (0, 3): 64,
                 (1,): 32,
                 (1, 2): 96,
                 (1, 2, 3): 192,
                 (1, 3): 96,
                 (2,): 24,
                 (2, 3): 48,
                 (3,): 8,
                 (4,): 1}

        Specify an entry::

            sage: C.flag_f_vector(0,3)                                                  # needs sage.combinat
            64
            sage: C.flag_f_vector(2)                                                    # needs sage.combinat
            24

        Leading ``-1`` and trailing entry of dimension are allowed::

            sage: C.flag_f_vector(-1,0,3)                                               # needs sage.combinat
            64
            sage: C.flag_f_vector(-1,0,3,4)                                             # needs sage.combinat
            64

        One can get the number of trivial faces::

            sage: C.flag_f_vector(-1)                                                   # needs sage.combinat
            1
            sage: C.flag_f_vector(4)                                                    # needs sage.combinat
            1

        Polyhedra with lines, have ``0`` entries accordingly::

            sage: C = (Polyhedron(lines=[[1]]) * polytopes.hypercube(2)).combinatorial_polyhedron()
            sage: C.flag_f_vector()                                                     # needs sage.combinat
            {(-1,): 1, (0, 1): 0, (0, 2): 0, (0,): 0, (1, 2): 8, (1,): 4, (2,): 4, 3: 1}

        If the arguments are not strictly increasing or out of range,
        a key error is raised::

            sage: C.flag_f_vector(-1,0,3,5)                                             # needs sage.combinat
            Traceback (most recent call last):
            ...
            KeyError: (0, 3, 5)
            sage: C.flag_f_vector(-1,3,0)                                               # needs sage.combinat
            Traceback (most recent call last):
            ...
            KeyError: (3, 0)"""
    def graph(self) -> Any:
        """CombinatorialPolyhedron.vertex_graph(self, names=True, algorithm=None)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 1266)

        Return a graph in which the vertices correspond to vertices
        of the polyhedron, and edges to bounded rank 1 faces.

        INPUT:

        - ``names`` -- boolean (default: ``True``); if ``False``,
          then the nodes of the graph are labeld by the
          indices of the Vrepresentation

        - ``algorithm`` -- string (optional);
          specify whether the face generator starts with facets or vertices:
          * ``'primal'`` -- start with the facets
          * ``'dual'`` -- start with the vertices
          * ``None`` -- choose automatically

        EXAMPLES::

            sage: P = polytopes.cyclic_polytope(3,5)
            sage: C = CombinatorialPolyhedron(P)
            sage: G = C.vertex_graph(); G                                               # needs sage.graphs
            Graph on 5 vertices
            sage: sorted(G.degree())                                                    # needs sage.graphs
            [3, 3, 4, 4, 4]

            sage: P = Polyhedron(rays=[[1]])
            sage: C = CombinatorialPolyhedron(P)
            sage: C.graph()                                                             # needs sage.graphs
            Graph on 1 vertex"""
    @overload
    def hasse_diagram(self) -> Any:
        """CombinatorialPolyhedron.hasse_diagram(self)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 2836)

        Return the Hasse diagram of ``self``.

        This is the Hasse diagram of the poset of the faces of ``self``:
        A directed graph consisting of a vertex for each face
        and an edge for each minimal inclusion of faces.

        .. NOTE::

            The vertices of the Hasse diagram are given by indices.
            Use :meth:`CombinatorialPolyhedron.face_by_face_lattice_index`
            to relabel.

        .. WARNING::

            The indices of the Hasse diagram might depend on architecture
            and implementation. Relabeling the face lattice with
            :meth:`CombinatorialPolyhedron.face_by_face_lattice_index` or
            the properties obtained from this face will be platform independent

        EXAMPLES::

            sage: # needs sage.graphs sage.rings.number_field
            sage: P = polytopes.regular_polygon(4).pyramid()
            sage: C = CombinatorialPolyhedron(P)
            sage: D = C.hasse_diagram(); D
            Digraph on 20 vertices
            sage: D.average_degree()
            21/5
            sage: D.relabel(C.face_by_face_lattice_index)
            sage: dim_0_vert = D.vertices(sort=True)[1:6]; dim_0_vert
            [A 0-dimensional face of a 3-dimensional combinatorial polyhedron,
             A 0-dimensional face of a 3-dimensional combinatorial polyhedron,
             A 0-dimensional face of a 3-dimensional combinatorial polyhedron,
             A 0-dimensional face of a 3-dimensional combinatorial polyhedron,
             A 0-dimensional face of a 3-dimensional combinatorial polyhedron]
            sage: sorted(D.out_degree(vertices=dim_0_vert))
            [3, 3, 3, 3, 4]"""
    @overload
    def hasse_diagram(self) -> Any:
        """CombinatorialPolyhedron.hasse_diagram(self)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 2836)

        Return the Hasse diagram of ``self``.

        This is the Hasse diagram of the poset of the faces of ``self``:
        A directed graph consisting of a vertex for each face
        and an edge for each minimal inclusion of faces.

        .. NOTE::

            The vertices of the Hasse diagram are given by indices.
            Use :meth:`CombinatorialPolyhedron.face_by_face_lattice_index`
            to relabel.

        .. WARNING::

            The indices of the Hasse diagram might depend on architecture
            and implementation. Relabeling the face lattice with
            :meth:`CombinatorialPolyhedron.face_by_face_lattice_index` or
            the properties obtained from this face will be platform independent

        EXAMPLES::

            sage: # needs sage.graphs sage.rings.number_field
            sage: P = polytopes.regular_polygon(4).pyramid()
            sage: C = CombinatorialPolyhedron(P)
            sage: D = C.hasse_diagram(); D
            Digraph on 20 vertices
            sage: D.average_degree()
            21/5
            sage: D.relabel(C.face_by_face_lattice_index)
            sage: dim_0_vert = D.vertices(sort=True)[1:6]; dim_0_vert
            [A 0-dimensional face of a 3-dimensional combinatorial polyhedron,
             A 0-dimensional face of a 3-dimensional combinatorial polyhedron,
             A 0-dimensional face of a 3-dimensional combinatorial polyhedron,
             A 0-dimensional face of a 3-dimensional combinatorial polyhedron,
             A 0-dimensional face of a 3-dimensional combinatorial polyhedron]
            sage: sorted(D.out_degree(vertices=dim_0_vert))
            [3, 3, 3, 3, 4]"""
    @overload
    def incidence_matrix(self) -> Any:
        """CombinatorialPolyhedron.incidence_matrix(self)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 1064)

        Return the incidence matrix.

        .. NOTE::

            The columns correspond to inequalities/equations in the
            order :meth:`Hrepresentation`, the rows correspond to
            vertices/rays/lines in the order
            :meth:`Vrepresentation`.

        .. SEEALSO::

            :meth:`~sage.geometry.polyhedron.base.Polyhedron_base.incidence_matrix`.

        EXAMPLES::

            sage: P = polytopes.cube()
            sage: C = P.combinatorial_polyhedron()
            sage: C.incidence_matrix()
            [1 0 0 0 1 1]
            [1 1 0 0 1 0]
            [1 1 1 0 0 0]
            [1 0 1 0 0 1]
            [0 0 1 1 0 1]
            [0 0 0 1 1 1]
            [0 1 0 1 1 0]
            [0 1 1 1 0 0]

        In this case the incidence matrix is only computed once::

            sage: P.incidence_matrix() is C.incidence_matrix()
            True
            sage: C.incidence_matrix.clear_cache()
            sage: C.incidence_matrix() is P.incidence_matrix()
            False
            sage: C.incidence_matrix() == P.incidence_matrix()
            True

        ::

            sage: # needs sage.combinat
            sage: P = polytopes.permutahedron(5, backend='field')
            sage: C = P.combinatorial_polyhedron()
            sage: C.incidence_matrix.clear_cache()
            sage: C.incidence_matrix() == P.incidence_matrix()
            True

        The incidence matrix is consistent with
        :meth:`~sage.geometry.polyhedron.base.Polyhedron_base.incidence_matrix`::

            sage: P = Polyhedron([[0,0]])
            sage: P.incidence_matrix()
            [1 1]
            sage: C = P.combinatorial_polyhedron()
            sage: C.incidence_matrix.clear_cache()
            sage: P.combinatorial_polyhedron().incidence_matrix()
            [1 1]

        TESTS:

        Check that :issue:`29455` is fixed::

            sage: C = Polyhedron([[0]]).combinatorial_polyhedron()
            sage: C.incidence_matrix.clear_cache()
            sage: C.incidence_matrix()
            [1]
            sage: C = CombinatorialPolyhedron(-1)
            sage: C.incidence_matrix.clear_cache()
            sage: C.incidence_matrix()
            []

        Check that the base ring is ``ZZ``, see :issue:`29840`::

            sage: C = CombinatorialPolyhedron([[0,1,2], [0,1,3], [0,2,3], [1,2,3]])
            sage: C.incidence_matrix().base_ring()
            Integer Ring"""
    @overload
    def incidence_matrix(self) -> Any:
        """CombinatorialPolyhedron.incidence_matrix(self)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 1064)

        Return the incidence matrix.

        .. NOTE::

            The columns correspond to inequalities/equations in the
            order :meth:`Hrepresentation`, the rows correspond to
            vertices/rays/lines in the order
            :meth:`Vrepresentation`.

        .. SEEALSO::

            :meth:`~sage.geometry.polyhedron.base.Polyhedron_base.incidence_matrix`.

        EXAMPLES::

            sage: P = polytopes.cube()
            sage: C = P.combinatorial_polyhedron()
            sage: C.incidence_matrix()
            [1 0 0 0 1 1]
            [1 1 0 0 1 0]
            [1 1 1 0 0 0]
            [1 0 1 0 0 1]
            [0 0 1 1 0 1]
            [0 0 0 1 1 1]
            [0 1 0 1 1 0]
            [0 1 1 1 0 0]

        In this case the incidence matrix is only computed once::

            sage: P.incidence_matrix() is C.incidence_matrix()
            True
            sage: C.incidence_matrix.clear_cache()
            sage: C.incidence_matrix() is P.incidence_matrix()
            False
            sage: C.incidence_matrix() == P.incidence_matrix()
            True

        ::

            sage: # needs sage.combinat
            sage: P = polytopes.permutahedron(5, backend='field')
            sage: C = P.combinatorial_polyhedron()
            sage: C.incidence_matrix.clear_cache()
            sage: C.incidence_matrix() == P.incidence_matrix()
            True

        The incidence matrix is consistent with
        :meth:`~sage.geometry.polyhedron.base.Polyhedron_base.incidence_matrix`::

            sage: P = Polyhedron([[0,0]])
            sage: P.incidence_matrix()
            [1 1]
            sage: C = P.combinatorial_polyhedron()
            sage: C.incidence_matrix.clear_cache()
            sage: P.combinatorial_polyhedron().incidence_matrix()
            [1 1]

        TESTS:

        Check that :issue:`29455` is fixed::

            sage: C = Polyhedron([[0]]).combinatorial_polyhedron()
            sage: C.incidence_matrix.clear_cache()
            sage: C.incidence_matrix()
            [1]
            sage: C = CombinatorialPolyhedron(-1)
            sage: C.incidence_matrix.clear_cache()
            sage: C.incidence_matrix()
            []

        Check that the base ring is ``ZZ``, see :issue:`29840`::

            sage: C = CombinatorialPolyhedron([[0,1,2], [0,1,3], [0,2,3], [1,2,3]])
            sage: C.incidence_matrix().base_ring()
            Integer Ring"""
    @overload
    def incidence_matrix(self) -> Any:
        """CombinatorialPolyhedron.incidence_matrix(self)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 1064)

        Return the incidence matrix.

        .. NOTE::

            The columns correspond to inequalities/equations in the
            order :meth:`Hrepresentation`, the rows correspond to
            vertices/rays/lines in the order
            :meth:`Vrepresentation`.

        .. SEEALSO::

            :meth:`~sage.geometry.polyhedron.base.Polyhedron_base.incidence_matrix`.

        EXAMPLES::

            sage: P = polytopes.cube()
            sage: C = P.combinatorial_polyhedron()
            sage: C.incidence_matrix()
            [1 0 0 0 1 1]
            [1 1 0 0 1 0]
            [1 1 1 0 0 0]
            [1 0 1 0 0 1]
            [0 0 1 1 0 1]
            [0 0 0 1 1 1]
            [0 1 0 1 1 0]
            [0 1 1 1 0 0]

        In this case the incidence matrix is only computed once::

            sage: P.incidence_matrix() is C.incidence_matrix()
            True
            sage: C.incidence_matrix.clear_cache()
            sage: C.incidence_matrix() is P.incidence_matrix()
            False
            sage: C.incidence_matrix() == P.incidence_matrix()
            True

        ::

            sage: # needs sage.combinat
            sage: P = polytopes.permutahedron(5, backend='field')
            sage: C = P.combinatorial_polyhedron()
            sage: C.incidence_matrix.clear_cache()
            sage: C.incidence_matrix() == P.incidence_matrix()
            True

        The incidence matrix is consistent with
        :meth:`~sage.geometry.polyhedron.base.Polyhedron_base.incidence_matrix`::

            sage: P = Polyhedron([[0,0]])
            sage: P.incidence_matrix()
            [1 1]
            sage: C = P.combinatorial_polyhedron()
            sage: C.incidence_matrix.clear_cache()
            sage: P.combinatorial_polyhedron().incidence_matrix()
            [1 1]

        TESTS:

        Check that :issue:`29455` is fixed::

            sage: C = Polyhedron([[0]]).combinatorial_polyhedron()
            sage: C.incidence_matrix.clear_cache()
            sage: C.incidence_matrix()
            [1]
            sage: C = CombinatorialPolyhedron(-1)
            sage: C.incidence_matrix.clear_cache()
            sage: C.incidence_matrix()
            []

        Check that the base ring is ``ZZ``, see :issue:`29840`::

            sage: C = CombinatorialPolyhedron([[0,1,2], [0,1,3], [0,2,3], [1,2,3]])
            sage: C.incidence_matrix().base_ring()
            Integer Ring"""
    @overload
    def incidence_matrix(self) -> Any:
        """CombinatorialPolyhedron.incidence_matrix(self)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 1064)

        Return the incidence matrix.

        .. NOTE::

            The columns correspond to inequalities/equations in the
            order :meth:`Hrepresentation`, the rows correspond to
            vertices/rays/lines in the order
            :meth:`Vrepresentation`.

        .. SEEALSO::

            :meth:`~sage.geometry.polyhedron.base.Polyhedron_base.incidence_matrix`.

        EXAMPLES::

            sage: P = polytopes.cube()
            sage: C = P.combinatorial_polyhedron()
            sage: C.incidence_matrix()
            [1 0 0 0 1 1]
            [1 1 0 0 1 0]
            [1 1 1 0 0 0]
            [1 0 1 0 0 1]
            [0 0 1 1 0 1]
            [0 0 0 1 1 1]
            [0 1 0 1 1 0]
            [0 1 1 1 0 0]

        In this case the incidence matrix is only computed once::

            sage: P.incidence_matrix() is C.incidence_matrix()
            True
            sage: C.incidence_matrix.clear_cache()
            sage: C.incidence_matrix() is P.incidence_matrix()
            False
            sage: C.incidence_matrix() == P.incidence_matrix()
            True

        ::

            sage: # needs sage.combinat
            sage: P = polytopes.permutahedron(5, backend='field')
            sage: C = P.combinatorial_polyhedron()
            sage: C.incidence_matrix.clear_cache()
            sage: C.incidence_matrix() == P.incidence_matrix()
            True

        The incidence matrix is consistent with
        :meth:`~sage.geometry.polyhedron.base.Polyhedron_base.incidence_matrix`::

            sage: P = Polyhedron([[0,0]])
            sage: P.incidence_matrix()
            [1 1]
            sage: C = P.combinatorial_polyhedron()
            sage: C.incidence_matrix.clear_cache()
            sage: P.combinatorial_polyhedron().incidence_matrix()
            [1 1]

        TESTS:

        Check that :issue:`29455` is fixed::

            sage: C = Polyhedron([[0]]).combinatorial_polyhedron()
            sage: C.incidence_matrix.clear_cache()
            sage: C.incidence_matrix()
            [1]
            sage: C = CombinatorialPolyhedron(-1)
            sage: C.incidence_matrix.clear_cache()
            sage: C.incidence_matrix()
            []

        Check that the base ring is ``ZZ``, see :issue:`29840`::

            sage: C = CombinatorialPolyhedron([[0,1,2], [0,1,3], [0,2,3], [1,2,3]])
            sage: C.incidence_matrix().base_ring()
            Integer Ring"""
    @overload
    def incidence_matrix(self) -> Any:
        """CombinatorialPolyhedron.incidence_matrix(self)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 1064)

        Return the incidence matrix.

        .. NOTE::

            The columns correspond to inequalities/equations in the
            order :meth:`Hrepresentation`, the rows correspond to
            vertices/rays/lines in the order
            :meth:`Vrepresentation`.

        .. SEEALSO::

            :meth:`~sage.geometry.polyhedron.base.Polyhedron_base.incidence_matrix`.

        EXAMPLES::

            sage: P = polytopes.cube()
            sage: C = P.combinatorial_polyhedron()
            sage: C.incidence_matrix()
            [1 0 0 0 1 1]
            [1 1 0 0 1 0]
            [1 1 1 0 0 0]
            [1 0 1 0 0 1]
            [0 0 1 1 0 1]
            [0 0 0 1 1 1]
            [0 1 0 1 1 0]
            [0 1 1 1 0 0]

        In this case the incidence matrix is only computed once::

            sage: P.incidence_matrix() is C.incidence_matrix()
            True
            sage: C.incidence_matrix.clear_cache()
            sage: C.incidence_matrix() is P.incidence_matrix()
            False
            sage: C.incidence_matrix() == P.incidence_matrix()
            True

        ::

            sage: # needs sage.combinat
            sage: P = polytopes.permutahedron(5, backend='field')
            sage: C = P.combinatorial_polyhedron()
            sage: C.incidence_matrix.clear_cache()
            sage: C.incidence_matrix() == P.incidence_matrix()
            True

        The incidence matrix is consistent with
        :meth:`~sage.geometry.polyhedron.base.Polyhedron_base.incidence_matrix`::

            sage: P = Polyhedron([[0,0]])
            sage: P.incidence_matrix()
            [1 1]
            sage: C = P.combinatorial_polyhedron()
            sage: C.incidence_matrix.clear_cache()
            sage: P.combinatorial_polyhedron().incidence_matrix()
            [1 1]

        TESTS:

        Check that :issue:`29455` is fixed::

            sage: C = Polyhedron([[0]]).combinatorial_polyhedron()
            sage: C.incidence_matrix.clear_cache()
            sage: C.incidence_matrix()
            [1]
            sage: C = CombinatorialPolyhedron(-1)
            sage: C.incidence_matrix.clear_cache()
            sage: C.incidence_matrix()
            []

        Check that the base ring is ``ZZ``, see :issue:`29840`::

            sage: C = CombinatorialPolyhedron([[0,1,2], [0,1,3], [0,2,3], [1,2,3]])
            sage: C.incidence_matrix().base_ring()
            Integer Ring"""
    @overload
    def incidence_matrix(self) -> Any:
        """CombinatorialPolyhedron.incidence_matrix(self)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 1064)

        Return the incidence matrix.

        .. NOTE::

            The columns correspond to inequalities/equations in the
            order :meth:`Hrepresentation`, the rows correspond to
            vertices/rays/lines in the order
            :meth:`Vrepresentation`.

        .. SEEALSO::

            :meth:`~sage.geometry.polyhedron.base.Polyhedron_base.incidence_matrix`.

        EXAMPLES::

            sage: P = polytopes.cube()
            sage: C = P.combinatorial_polyhedron()
            sage: C.incidence_matrix()
            [1 0 0 0 1 1]
            [1 1 0 0 1 0]
            [1 1 1 0 0 0]
            [1 0 1 0 0 1]
            [0 0 1 1 0 1]
            [0 0 0 1 1 1]
            [0 1 0 1 1 0]
            [0 1 1 1 0 0]

        In this case the incidence matrix is only computed once::

            sage: P.incidence_matrix() is C.incidence_matrix()
            True
            sage: C.incidence_matrix.clear_cache()
            sage: C.incidence_matrix() is P.incidence_matrix()
            False
            sage: C.incidence_matrix() == P.incidence_matrix()
            True

        ::

            sage: # needs sage.combinat
            sage: P = polytopes.permutahedron(5, backend='field')
            sage: C = P.combinatorial_polyhedron()
            sage: C.incidence_matrix.clear_cache()
            sage: C.incidence_matrix() == P.incidence_matrix()
            True

        The incidence matrix is consistent with
        :meth:`~sage.geometry.polyhedron.base.Polyhedron_base.incidence_matrix`::

            sage: P = Polyhedron([[0,0]])
            sage: P.incidence_matrix()
            [1 1]
            sage: C = P.combinatorial_polyhedron()
            sage: C.incidence_matrix.clear_cache()
            sage: P.combinatorial_polyhedron().incidence_matrix()
            [1 1]

        TESTS:

        Check that :issue:`29455` is fixed::

            sage: C = Polyhedron([[0]]).combinatorial_polyhedron()
            sage: C.incidence_matrix.clear_cache()
            sage: C.incidence_matrix()
            [1]
            sage: C = CombinatorialPolyhedron(-1)
            sage: C.incidence_matrix.clear_cache()
            sage: C.incidence_matrix()
            []

        Check that the base ring is ``ZZ``, see :issue:`29840`::

            sage: C = CombinatorialPolyhedron([[0,1,2], [0,1,3], [0,2,3], [1,2,3]])
            sage: C.incidence_matrix().base_ring()
            Integer Ring"""
    @overload
    def incidence_matrix(self) -> Any:
        """CombinatorialPolyhedron.incidence_matrix(self)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 1064)

        Return the incidence matrix.

        .. NOTE::

            The columns correspond to inequalities/equations in the
            order :meth:`Hrepresentation`, the rows correspond to
            vertices/rays/lines in the order
            :meth:`Vrepresentation`.

        .. SEEALSO::

            :meth:`~sage.geometry.polyhedron.base.Polyhedron_base.incidence_matrix`.

        EXAMPLES::

            sage: P = polytopes.cube()
            sage: C = P.combinatorial_polyhedron()
            sage: C.incidence_matrix()
            [1 0 0 0 1 1]
            [1 1 0 0 1 0]
            [1 1 1 0 0 0]
            [1 0 1 0 0 1]
            [0 0 1 1 0 1]
            [0 0 0 1 1 1]
            [0 1 0 1 1 0]
            [0 1 1 1 0 0]

        In this case the incidence matrix is only computed once::

            sage: P.incidence_matrix() is C.incidence_matrix()
            True
            sage: C.incidence_matrix.clear_cache()
            sage: C.incidence_matrix() is P.incidence_matrix()
            False
            sage: C.incidence_matrix() == P.incidence_matrix()
            True

        ::

            sage: # needs sage.combinat
            sage: P = polytopes.permutahedron(5, backend='field')
            sage: C = P.combinatorial_polyhedron()
            sage: C.incidence_matrix.clear_cache()
            sage: C.incidence_matrix() == P.incidence_matrix()
            True

        The incidence matrix is consistent with
        :meth:`~sage.geometry.polyhedron.base.Polyhedron_base.incidence_matrix`::

            sage: P = Polyhedron([[0,0]])
            sage: P.incidence_matrix()
            [1 1]
            sage: C = P.combinatorial_polyhedron()
            sage: C.incidence_matrix.clear_cache()
            sage: P.combinatorial_polyhedron().incidence_matrix()
            [1 1]

        TESTS:

        Check that :issue:`29455` is fixed::

            sage: C = Polyhedron([[0]]).combinatorial_polyhedron()
            sage: C.incidence_matrix.clear_cache()
            sage: C.incidence_matrix()
            [1]
            sage: C = CombinatorialPolyhedron(-1)
            sage: C.incidence_matrix.clear_cache()
            sage: C.incidence_matrix()
            []

        Check that the base ring is ``ZZ``, see :issue:`29840`::

            sage: C = CombinatorialPolyhedron([[0,1,2], [0,1,3], [0,2,3], [1,2,3]])
            sage: C.incidence_matrix().base_ring()
            Integer Ring"""
    @overload
    def incidence_matrix(self) -> Any:
        """CombinatorialPolyhedron.incidence_matrix(self)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 1064)

        Return the incidence matrix.

        .. NOTE::

            The columns correspond to inequalities/equations in the
            order :meth:`Hrepresentation`, the rows correspond to
            vertices/rays/lines in the order
            :meth:`Vrepresentation`.

        .. SEEALSO::

            :meth:`~sage.geometry.polyhedron.base.Polyhedron_base.incidence_matrix`.

        EXAMPLES::

            sage: P = polytopes.cube()
            sage: C = P.combinatorial_polyhedron()
            sage: C.incidence_matrix()
            [1 0 0 0 1 1]
            [1 1 0 0 1 0]
            [1 1 1 0 0 0]
            [1 0 1 0 0 1]
            [0 0 1 1 0 1]
            [0 0 0 1 1 1]
            [0 1 0 1 1 0]
            [0 1 1 1 0 0]

        In this case the incidence matrix is only computed once::

            sage: P.incidence_matrix() is C.incidence_matrix()
            True
            sage: C.incidence_matrix.clear_cache()
            sage: C.incidence_matrix() is P.incidence_matrix()
            False
            sage: C.incidence_matrix() == P.incidence_matrix()
            True

        ::

            sage: # needs sage.combinat
            sage: P = polytopes.permutahedron(5, backend='field')
            sage: C = P.combinatorial_polyhedron()
            sage: C.incidence_matrix.clear_cache()
            sage: C.incidence_matrix() == P.incidence_matrix()
            True

        The incidence matrix is consistent with
        :meth:`~sage.geometry.polyhedron.base.Polyhedron_base.incidence_matrix`::

            sage: P = Polyhedron([[0,0]])
            sage: P.incidence_matrix()
            [1 1]
            sage: C = P.combinatorial_polyhedron()
            sage: C.incidence_matrix.clear_cache()
            sage: P.combinatorial_polyhedron().incidence_matrix()
            [1 1]

        TESTS:

        Check that :issue:`29455` is fixed::

            sage: C = Polyhedron([[0]]).combinatorial_polyhedron()
            sage: C.incidence_matrix.clear_cache()
            sage: C.incidence_matrix()
            [1]
            sage: C = CombinatorialPolyhedron(-1)
            sage: C.incidence_matrix.clear_cache()
            sage: C.incidence_matrix()
            []

        Check that the base ring is ``ZZ``, see :issue:`29840`::

            sage: C = CombinatorialPolyhedron([[0,1,2], [0,1,3], [0,2,3], [1,2,3]])
            sage: C.incidence_matrix().base_ring()
            Integer Ring"""
    @overload
    def incidence_matrix(self) -> Any:
        """CombinatorialPolyhedron.incidence_matrix(self)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 1064)

        Return the incidence matrix.

        .. NOTE::

            The columns correspond to inequalities/equations in the
            order :meth:`Hrepresentation`, the rows correspond to
            vertices/rays/lines in the order
            :meth:`Vrepresentation`.

        .. SEEALSO::

            :meth:`~sage.geometry.polyhedron.base.Polyhedron_base.incidence_matrix`.

        EXAMPLES::

            sage: P = polytopes.cube()
            sage: C = P.combinatorial_polyhedron()
            sage: C.incidence_matrix()
            [1 0 0 0 1 1]
            [1 1 0 0 1 0]
            [1 1 1 0 0 0]
            [1 0 1 0 0 1]
            [0 0 1 1 0 1]
            [0 0 0 1 1 1]
            [0 1 0 1 1 0]
            [0 1 1 1 0 0]

        In this case the incidence matrix is only computed once::

            sage: P.incidence_matrix() is C.incidence_matrix()
            True
            sage: C.incidence_matrix.clear_cache()
            sage: C.incidence_matrix() is P.incidence_matrix()
            False
            sage: C.incidence_matrix() == P.incidence_matrix()
            True

        ::

            sage: # needs sage.combinat
            sage: P = polytopes.permutahedron(5, backend='field')
            sage: C = P.combinatorial_polyhedron()
            sage: C.incidence_matrix.clear_cache()
            sage: C.incidence_matrix() == P.incidence_matrix()
            True

        The incidence matrix is consistent with
        :meth:`~sage.geometry.polyhedron.base.Polyhedron_base.incidence_matrix`::

            sage: P = Polyhedron([[0,0]])
            sage: P.incidence_matrix()
            [1 1]
            sage: C = P.combinatorial_polyhedron()
            sage: C.incidence_matrix.clear_cache()
            sage: P.combinatorial_polyhedron().incidence_matrix()
            [1 1]

        TESTS:

        Check that :issue:`29455` is fixed::

            sage: C = Polyhedron([[0]]).combinatorial_polyhedron()
            sage: C.incidence_matrix.clear_cache()
            sage: C.incidence_matrix()
            [1]
            sage: C = CombinatorialPolyhedron(-1)
            sage: C.incidence_matrix.clear_cache()
            sage: C.incidence_matrix()
            []

        Check that the base ring is ``ZZ``, see :issue:`29840`::

            sage: C = CombinatorialPolyhedron([[0,1,2], [0,1,3], [0,2,3], [1,2,3]])
            sage: C.incidence_matrix().base_ring()
            Integer Ring"""
    @overload
    def incidence_matrix(self) -> Any:
        """CombinatorialPolyhedron.incidence_matrix(self)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 1064)

        Return the incidence matrix.

        .. NOTE::

            The columns correspond to inequalities/equations in the
            order :meth:`Hrepresentation`, the rows correspond to
            vertices/rays/lines in the order
            :meth:`Vrepresentation`.

        .. SEEALSO::

            :meth:`~sage.geometry.polyhedron.base.Polyhedron_base.incidence_matrix`.

        EXAMPLES::

            sage: P = polytopes.cube()
            sage: C = P.combinatorial_polyhedron()
            sage: C.incidence_matrix()
            [1 0 0 0 1 1]
            [1 1 0 0 1 0]
            [1 1 1 0 0 0]
            [1 0 1 0 0 1]
            [0 0 1 1 0 1]
            [0 0 0 1 1 1]
            [0 1 0 1 1 0]
            [0 1 1 1 0 0]

        In this case the incidence matrix is only computed once::

            sage: P.incidence_matrix() is C.incidence_matrix()
            True
            sage: C.incidence_matrix.clear_cache()
            sage: C.incidence_matrix() is P.incidence_matrix()
            False
            sage: C.incidence_matrix() == P.incidence_matrix()
            True

        ::

            sage: # needs sage.combinat
            sage: P = polytopes.permutahedron(5, backend='field')
            sage: C = P.combinatorial_polyhedron()
            sage: C.incidence_matrix.clear_cache()
            sage: C.incidence_matrix() == P.incidence_matrix()
            True

        The incidence matrix is consistent with
        :meth:`~sage.geometry.polyhedron.base.Polyhedron_base.incidence_matrix`::

            sage: P = Polyhedron([[0,0]])
            sage: P.incidence_matrix()
            [1 1]
            sage: C = P.combinatorial_polyhedron()
            sage: C.incidence_matrix.clear_cache()
            sage: P.combinatorial_polyhedron().incidence_matrix()
            [1 1]

        TESTS:

        Check that :issue:`29455` is fixed::

            sage: C = Polyhedron([[0]]).combinatorial_polyhedron()
            sage: C.incidence_matrix.clear_cache()
            sage: C.incidence_matrix()
            [1]
            sage: C = CombinatorialPolyhedron(-1)
            sage: C.incidence_matrix.clear_cache()
            sage: C.incidence_matrix()
            []

        Check that the base ring is ``ZZ``, see :issue:`29840`::

            sage: C = CombinatorialPolyhedron([[0,1,2], [0,1,3], [0,2,3], [1,2,3]])
            sage: C.incidence_matrix().base_ring()
            Integer Ring"""
    @overload
    def incidence_matrix(self) -> Any:
        """CombinatorialPolyhedron.incidence_matrix(self)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 1064)

        Return the incidence matrix.

        .. NOTE::

            The columns correspond to inequalities/equations in the
            order :meth:`Hrepresentation`, the rows correspond to
            vertices/rays/lines in the order
            :meth:`Vrepresentation`.

        .. SEEALSO::

            :meth:`~sage.geometry.polyhedron.base.Polyhedron_base.incidence_matrix`.

        EXAMPLES::

            sage: P = polytopes.cube()
            sage: C = P.combinatorial_polyhedron()
            sage: C.incidence_matrix()
            [1 0 0 0 1 1]
            [1 1 0 0 1 0]
            [1 1 1 0 0 0]
            [1 0 1 0 0 1]
            [0 0 1 1 0 1]
            [0 0 0 1 1 1]
            [0 1 0 1 1 0]
            [0 1 1 1 0 0]

        In this case the incidence matrix is only computed once::

            sage: P.incidence_matrix() is C.incidence_matrix()
            True
            sage: C.incidence_matrix.clear_cache()
            sage: C.incidence_matrix() is P.incidence_matrix()
            False
            sage: C.incidence_matrix() == P.incidence_matrix()
            True

        ::

            sage: # needs sage.combinat
            sage: P = polytopes.permutahedron(5, backend='field')
            sage: C = P.combinatorial_polyhedron()
            sage: C.incidence_matrix.clear_cache()
            sage: C.incidence_matrix() == P.incidence_matrix()
            True

        The incidence matrix is consistent with
        :meth:`~sage.geometry.polyhedron.base.Polyhedron_base.incidence_matrix`::

            sage: P = Polyhedron([[0,0]])
            sage: P.incidence_matrix()
            [1 1]
            sage: C = P.combinatorial_polyhedron()
            sage: C.incidence_matrix.clear_cache()
            sage: P.combinatorial_polyhedron().incidence_matrix()
            [1 1]

        TESTS:

        Check that :issue:`29455` is fixed::

            sage: C = Polyhedron([[0]]).combinatorial_polyhedron()
            sage: C.incidence_matrix.clear_cache()
            sage: C.incidence_matrix()
            [1]
            sage: C = CombinatorialPolyhedron(-1)
            sage: C.incidence_matrix.clear_cache()
            sage: C.incidence_matrix()
            []

        Check that the base ring is ``ZZ``, see :issue:`29840`::

            sage: C = CombinatorialPolyhedron([[0,1,2], [0,1,3], [0,2,3], [1,2,3]])
            sage: C.incidence_matrix().base_ring()
            Integer Ring"""
    @overload
    def is_bipyramid(self, certificate=...) -> Any:
        """CombinatorialPolyhedron.is_bipyramid(self, certificate=False)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 2431)

        Test whether the polytope is a bipyramid over some other polytope.

        INPUT:

        - ``certificate`` -- boolean (default: ``False``); specifies whether
          to return a vertex of the polytope which is the apex of a pyramid,
          if found

        INPUT:

        - ``certificate`` -- boolean (default: ``False``); specifies whether
          to return two vertices of the polytope which are the apices of a
          bipyramid, if found

        OUTPUT:

        If ``certificate`` is ``True``, returns a tuple containing:

        1. Boolean.
        2. ``None`` or a tuple containing:
            a. The first apex.
            b. The second apex.

        If ``certificate`` is ``False`` returns a boolean.

        EXAMPLES::

            sage: C = polytopes.hypercube(4).combinatorial_polyhedron()
            sage: C.is_bipyramid()
            False
            sage: C.is_bipyramid(certificate=True)
            (False, None)
            sage: C = polytopes.cross_polytope(4).combinatorial_polyhedron()
            sage: C.is_bipyramid()
            True
            sage: C.is_bipyramid(certificate=True)
            (True, [A vertex at (1, 0, 0, 0), A vertex at (-1, 0, 0, 0)])

        For unbounded polyhedra, an error is raised::

            sage: C = CombinatorialPolyhedron([[0,1], [0,2]], far_face=[1,2], unbounded=True)
            sage: C.is_pyramid()
            Traceback (most recent call last):
            ...
            ValueError: polyhedron has to be compact

        TESTS::

            sage: CombinatorialPolyhedron(-1).is_bipyramid()
            False
            sage: CombinatorialPolyhedron(-1).is_bipyramid(True)
            (False, None)
            sage: C = polytopes.cross_polytope(1)
            sage: C.is_bipyramid()
            True
            sage: C.is_bipyramid(True)
            (True, [A vertex at (1), A vertex at (-1)])

        Check that bug analog to :issue:`30292` is avoided::

            sage: Polyhedron([[0, 1, 0], [0, 0, 1], [0, -1, -1], [1, 0, 0], [-1, 0, 0]]).is_bipyramid(certificate=True)
            (True, [A vertex at (1, 0, 0), A vertex at (-1, 0, 0)])

        ALGORITHM:

        Assume all faces of a polyhedron to be given as lists of vertices.

        A polytope is a bipyramid with apexes `v`, `w` if and only if for each
        proper face `v \\in F` there exists a face `G` with
        `G \\setminus \\{w\\} = F \\setminus \\{v\\}`
        and vice versa (for each proper face
        `w \\in F` there exists ...).

        To check this property it suffices to check for all facets of the polyhedron."""
    @overload
    def is_bipyramid(self) -> Any:
        """CombinatorialPolyhedron.is_bipyramid(self, certificate=False)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 2431)

        Test whether the polytope is a bipyramid over some other polytope.

        INPUT:

        - ``certificate`` -- boolean (default: ``False``); specifies whether
          to return a vertex of the polytope which is the apex of a pyramid,
          if found

        INPUT:

        - ``certificate`` -- boolean (default: ``False``); specifies whether
          to return two vertices of the polytope which are the apices of a
          bipyramid, if found

        OUTPUT:

        If ``certificate`` is ``True``, returns a tuple containing:

        1. Boolean.
        2. ``None`` or a tuple containing:
            a. The first apex.
            b. The second apex.

        If ``certificate`` is ``False`` returns a boolean.

        EXAMPLES::

            sage: C = polytopes.hypercube(4).combinatorial_polyhedron()
            sage: C.is_bipyramid()
            False
            sage: C.is_bipyramid(certificate=True)
            (False, None)
            sage: C = polytopes.cross_polytope(4).combinatorial_polyhedron()
            sage: C.is_bipyramid()
            True
            sage: C.is_bipyramid(certificate=True)
            (True, [A vertex at (1, 0, 0, 0), A vertex at (-1, 0, 0, 0)])

        For unbounded polyhedra, an error is raised::

            sage: C = CombinatorialPolyhedron([[0,1], [0,2]], far_face=[1,2], unbounded=True)
            sage: C.is_pyramid()
            Traceback (most recent call last):
            ...
            ValueError: polyhedron has to be compact

        TESTS::

            sage: CombinatorialPolyhedron(-1).is_bipyramid()
            False
            sage: CombinatorialPolyhedron(-1).is_bipyramid(True)
            (False, None)
            sage: C = polytopes.cross_polytope(1)
            sage: C.is_bipyramid()
            True
            sage: C.is_bipyramid(True)
            (True, [A vertex at (1), A vertex at (-1)])

        Check that bug analog to :issue:`30292` is avoided::

            sage: Polyhedron([[0, 1, 0], [0, 0, 1], [0, -1, -1], [1, 0, 0], [-1, 0, 0]]).is_bipyramid(certificate=True)
            (True, [A vertex at (1, 0, 0), A vertex at (-1, 0, 0)])

        ALGORITHM:

        Assume all faces of a polyhedron to be given as lists of vertices.

        A polytope is a bipyramid with apexes `v`, `w` if and only if for each
        proper face `v \\in F` there exists a face `G` with
        `G \\setminus \\{w\\} = F \\setminus \\{v\\}`
        and vice versa (for each proper face
        `w \\in F` there exists ...).

        To check this property it suffices to check for all facets of the polyhedron."""
    @overload
    def is_bipyramid(self, certificate=...) -> Any:
        """CombinatorialPolyhedron.is_bipyramid(self, certificate=False)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 2431)

        Test whether the polytope is a bipyramid over some other polytope.

        INPUT:

        - ``certificate`` -- boolean (default: ``False``); specifies whether
          to return a vertex of the polytope which is the apex of a pyramid,
          if found

        INPUT:

        - ``certificate`` -- boolean (default: ``False``); specifies whether
          to return two vertices of the polytope which are the apices of a
          bipyramid, if found

        OUTPUT:

        If ``certificate`` is ``True``, returns a tuple containing:

        1. Boolean.
        2. ``None`` or a tuple containing:
            a. The first apex.
            b. The second apex.

        If ``certificate`` is ``False`` returns a boolean.

        EXAMPLES::

            sage: C = polytopes.hypercube(4).combinatorial_polyhedron()
            sage: C.is_bipyramid()
            False
            sage: C.is_bipyramid(certificate=True)
            (False, None)
            sage: C = polytopes.cross_polytope(4).combinatorial_polyhedron()
            sage: C.is_bipyramid()
            True
            sage: C.is_bipyramid(certificate=True)
            (True, [A vertex at (1, 0, 0, 0), A vertex at (-1, 0, 0, 0)])

        For unbounded polyhedra, an error is raised::

            sage: C = CombinatorialPolyhedron([[0,1], [0,2]], far_face=[1,2], unbounded=True)
            sage: C.is_pyramid()
            Traceback (most recent call last):
            ...
            ValueError: polyhedron has to be compact

        TESTS::

            sage: CombinatorialPolyhedron(-1).is_bipyramid()
            False
            sage: CombinatorialPolyhedron(-1).is_bipyramid(True)
            (False, None)
            sage: C = polytopes.cross_polytope(1)
            sage: C.is_bipyramid()
            True
            sage: C.is_bipyramid(True)
            (True, [A vertex at (1), A vertex at (-1)])

        Check that bug analog to :issue:`30292` is avoided::

            sage: Polyhedron([[0, 1, 0], [0, 0, 1], [0, -1, -1], [1, 0, 0], [-1, 0, 0]]).is_bipyramid(certificate=True)
            (True, [A vertex at (1, 0, 0), A vertex at (-1, 0, 0)])

        ALGORITHM:

        Assume all faces of a polyhedron to be given as lists of vertices.

        A polytope is a bipyramid with apexes `v`, `w` if and only if for each
        proper face `v \\in F` there exists a face `G` with
        `G \\setminus \\{w\\} = F \\setminus \\{v\\}`
        and vice versa (for each proper face
        `w \\in F` there exists ...).

        To check this property it suffices to check for all facets of the polyhedron."""
    @overload
    def is_bipyramid(self) -> Any:
        """CombinatorialPolyhedron.is_bipyramid(self, certificate=False)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 2431)

        Test whether the polytope is a bipyramid over some other polytope.

        INPUT:

        - ``certificate`` -- boolean (default: ``False``); specifies whether
          to return a vertex of the polytope which is the apex of a pyramid,
          if found

        INPUT:

        - ``certificate`` -- boolean (default: ``False``); specifies whether
          to return two vertices of the polytope which are the apices of a
          bipyramid, if found

        OUTPUT:

        If ``certificate`` is ``True``, returns a tuple containing:

        1. Boolean.
        2. ``None`` or a tuple containing:
            a. The first apex.
            b. The second apex.

        If ``certificate`` is ``False`` returns a boolean.

        EXAMPLES::

            sage: C = polytopes.hypercube(4).combinatorial_polyhedron()
            sage: C.is_bipyramid()
            False
            sage: C.is_bipyramid(certificate=True)
            (False, None)
            sage: C = polytopes.cross_polytope(4).combinatorial_polyhedron()
            sage: C.is_bipyramid()
            True
            sage: C.is_bipyramid(certificate=True)
            (True, [A vertex at (1, 0, 0, 0), A vertex at (-1, 0, 0, 0)])

        For unbounded polyhedra, an error is raised::

            sage: C = CombinatorialPolyhedron([[0,1], [0,2]], far_face=[1,2], unbounded=True)
            sage: C.is_pyramid()
            Traceback (most recent call last):
            ...
            ValueError: polyhedron has to be compact

        TESTS::

            sage: CombinatorialPolyhedron(-1).is_bipyramid()
            False
            sage: CombinatorialPolyhedron(-1).is_bipyramid(True)
            (False, None)
            sage: C = polytopes.cross_polytope(1)
            sage: C.is_bipyramid()
            True
            sage: C.is_bipyramid(True)
            (True, [A vertex at (1), A vertex at (-1)])

        Check that bug analog to :issue:`30292` is avoided::

            sage: Polyhedron([[0, 1, 0], [0, 0, 1], [0, -1, -1], [1, 0, 0], [-1, 0, 0]]).is_bipyramid(certificate=True)
            (True, [A vertex at (1, 0, 0), A vertex at (-1, 0, 0)])

        ALGORITHM:

        Assume all faces of a polyhedron to be given as lists of vertices.

        A polytope is a bipyramid with apexes `v`, `w` if and only if for each
        proper face `v \\in F` there exists a face `G` with
        `G \\setminus \\{w\\} = F \\setminus \\{v\\}`
        and vice versa (for each proper face
        `w \\in F` there exists ...).

        To check this property it suffices to check for all facets of the polyhedron."""
    @overload
    def is_bipyramid(self, certificate=...) -> Any:
        """CombinatorialPolyhedron.is_bipyramid(self, certificate=False)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 2431)

        Test whether the polytope is a bipyramid over some other polytope.

        INPUT:

        - ``certificate`` -- boolean (default: ``False``); specifies whether
          to return a vertex of the polytope which is the apex of a pyramid,
          if found

        INPUT:

        - ``certificate`` -- boolean (default: ``False``); specifies whether
          to return two vertices of the polytope which are the apices of a
          bipyramid, if found

        OUTPUT:

        If ``certificate`` is ``True``, returns a tuple containing:

        1. Boolean.
        2. ``None`` or a tuple containing:
            a. The first apex.
            b. The second apex.

        If ``certificate`` is ``False`` returns a boolean.

        EXAMPLES::

            sage: C = polytopes.hypercube(4).combinatorial_polyhedron()
            sage: C.is_bipyramid()
            False
            sage: C.is_bipyramid(certificate=True)
            (False, None)
            sage: C = polytopes.cross_polytope(4).combinatorial_polyhedron()
            sage: C.is_bipyramid()
            True
            sage: C.is_bipyramid(certificate=True)
            (True, [A vertex at (1, 0, 0, 0), A vertex at (-1, 0, 0, 0)])

        For unbounded polyhedra, an error is raised::

            sage: C = CombinatorialPolyhedron([[0,1], [0,2]], far_face=[1,2], unbounded=True)
            sage: C.is_pyramid()
            Traceback (most recent call last):
            ...
            ValueError: polyhedron has to be compact

        TESTS::

            sage: CombinatorialPolyhedron(-1).is_bipyramid()
            False
            sage: CombinatorialPolyhedron(-1).is_bipyramid(True)
            (False, None)
            sage: C = polytopes.cross_polytope(1)
            sage: C.is_bipyramid()
            True
            sage: C.is_bipyramid(True)
            (True, [A vertex at (1), A vertex at (-1)])

        Check that bug analog to :issue:`30292` is avoided::

            sage: Polyhedron([[0, 1, 0], [0, 0, 1], [0, -1, -1], [1, 0, 0], [-1, 0, 0]]).is_bipyramid(certificate=True)
            (True, [A vertex at (1, 0, 0), A vertex at (-1, 0, 0)])

        ALGORITHM:

        Assume all faces of a polyhedron to be given as lists of vertices.

        A polytope is a bipyramid with apexes `v`, `w` if and only if for each
        proper face `v \\in F` there exists a face `G` with
        `G \\setminus \\{w\\} = F \\setminus \\{v\\}`
        and vice versa (for each proper face
        `w \\in F` there exists ...).

        To check this property it suffices to check for all facets of the polyhedron."""
    @overload
    def is_bipyramid(self) -> Any:
        """CombinatorialPolyhedron.is_bipyramid(self, certificate=False)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 2431)

        Test whether the polytope is a bipyramid over some other polytope.

        INPUT:

        - ``certificate`` -- boolean (default: ``False``); specifies whether
          to return a vertex of the polytope which is the apex of a pyramid,
          if found

        INPUT:

        - ``certificate`` -- boolean (default: ``False``); specifies whether
          to return two vertices of the polytope which are the apices of a
          bipyramid, if found

        OUTPUT:

        If ``certificate`` is ``True``, returns a tuple containing:

        1. Boolean.
        2. ``None`` or a tuple containing:
            a. The first apex.
            b. The second apex.

        If ``certificate`` is ``False`` returns a boolean.

        EXAMPLES::

            sage: C = polytopes.hypercube(4).combinatorial_polyhedron()
            sage: C.is_bipyramid()
            False
            sage: C.is_bipyramid(certificate=True)
            (False, None)
            sage: C = polytopes.cross_polytope(4).combinatorial_polyhedron()
            sage: C.is_bipyramid()
            True
            sage: C.is_bipyramid(certificate=True)
            (True, [A vertex at (1, 0, 0, 0), A vertex at (-1, 0, 0, 0)])

        For unbounded polyhedra, an error is raised::

            sage: C = CombinatorialPolyhedron([[0,1], [0,2]], far_face=[1,2], unbounded=True)
            sage: C.is_pyramid()
            Traceback (most recent call last):
            ...
            ValueError: polyhedron has to be compact

        TESTS::

            sage: CombinatorialPolyhedron(-1).is_bipyramid()
            False
            sage: CombinatorialPolyhedron(-1).is_bipyramid(True)
            (False, None)
            sage: C = polytopes.cross_polytope(1)
            sage: C.is_bipyramid()
            True
            sage: C.is_bipyramid(True)
            (True, [A vertex at (1), A vertex at (-1)])

        Check that bug analog to :issue:`30292` is avoided::

            sage: Polyhedron([[0, 1, 0], [0, 0, 1], [0, -1, -1], [1, 0, 0], [-1, 0, 0]]).is_bipyramid(certificate=True)
            (True, [A vertex at (1, 0, 0), A vertex at (-1, 0, 0)])

        ALGORITHM:

        Assume all faces of a polyhedron to be given as lists of vertices.

        A polytope is a bipyramid with apexes `v`, `w` if and only if for each
        proper face `v \\in F` there exists a face `G` with
        `G \\setminus \\{w\\} = F \\setminus \\{v\\}`
        and vice versa (for each proper face
        `w \\in F` there exists ...).

        To check this property it suffices to check for all facets of the polyhedron."""
    @overload
    def is_bipyramid(self, _True) -> Any:
        """CombinatorialPolyhedron.is_bipyramid(self, certificate=False)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 2431)

        Test whether the polytope is a bipyramid over some other polytope.

        INPUT:

        - ``certificate`` -- boolean (default: ``False``); specifies whether
          to return a vertex of the polytope which is the apex of a pyramid,
          if found

        INPUT:

        - ``certificate`` -- boolean (default: ``False``); specifies whether
          to return two vertices of the polytope which are the apices of a
          bipyramid, if found

        OUTPUT:

        If ``certificate`` is ``True``, returns a tuple containing:

        1. Boolean.
        2. ``None`` or a tuple containing:
            a. The first apex.
            b. The second apex.

        If ``certificate`` is ``False`` returns a boolean.

        EXAMPLES::

            sage: C = polytopes.hypercube(4).combinatorial_polyhedron()
            sage: C.is_bipyramid()
            False
            sage: C.is_bipyramid(certificate=True)
            (False, None)
            sage: C = polytopes.cross_polytope(4).combinatorial_polyhedron()
            sage: C.is_bipyramid()
            True
            sage: C.is_bipyramid(certificate=True)
            (True, [A vertex at (1, 0, 0, 0), A vertex at (-1, 0, 0, 0)])

        For unbounded polyhedra, an error is raised::

            sage: C = CombinatorialPolyhedron([[0,1], [0,2]], far_face=[1,2], unbounded=True)
            sage: C.is_pyramid()
            Traceback (most recent call last):
            ...
            ValueError: polyhedron has to be compact

        TESTS::

            sage: CombinatorialPolyhedron(-1).is_bipyramid()
            False
            sage: CombinatorialPolyhedron(-1).is_bipyramid(True)
            (False, None)
            sage: C = polytopes.cross_polytope(1)
            sage: C.is_bipyramid()
            True
            sage: C.is_bipyramid(True)
            (True, [A vertex at (1), A vertex at (-1)])

        Check that bug analog to :issue:`30292` is avoided::

            sage: Polyhedron([[0, 1, 0], [0, 0, 1], [0, -1, -1], [1, 0, 0], [-1, 0, 0]]).is_bipyramid(certificate=True)
            (True, [A vertex at (1, 0, 0), A vertex at (-1, 0, 0)])

        ALGORITHM:

        Assume all faces of a polyhedron to be given as lists of vertices.

        A polytope is a bipyramid with apexes `v`, `w` if and only if for each
        proper face `v \\in F` there exists a face `G` with
        `G \\setminus \\{w\\} = F \\setminus \\{v\\}`
        and vice versa (for each proper face
        `w \\in F` there exists ...).

        To check this property it suffices to check for all facets of the polyhedron."""
    @overload
    def is_bipyramid(self) -> Any:
        """CombinatorialPolyhedron.is_bipyramid(self, certificate=False)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 2431)

        Test whether the polytope is a bipyramid over some other polytope.

        INPUT:

        - ``certificate`` -- boolean (default: ``False``); specifies whether
          to return a vertex of the polytope which is the apex of a pyramid,
          if found

        INPUT:

        - ``certificate`` -- boolean (default: ``False``); specifies whether
          to return two vertices of the polytope which are the apices of a
          bipyramid, if found

        OUTPUT:

        If ``certificate`` is ``True``, returns a tuple containing:

        1. Boolean.
        2. ``None`` or a tuple containing:
            a. The first apex.
            b. The second apex.

        If ``certificate`` is ``False`` returns a boolean.

        EXAMPLES::

            sage: C = polytopes.hypercube(4).combinatorial_polyhedron()
            sage: C.is_bipyramid()
            False
            sage: C.is_bipyramid(certificate=True)
            (False, None)
            sage: C = polytopes.cross_polytope(4).combinatorial_polyhedron()
            sage: C.is_bipyramid()
            True
            sage: C.is_bipyramid(certificate=True)
            (True, [A vertex at (1, 0, 0, 0), A vertex at (-1, 0, 0, 0)])

        For unbounded polyhedra, an error is raised::

            sage: C = CombinatorialPolyhedron([[0,1], [0,2]], far_face=[1,2], unbounded=True)
            sage: C.is_pyramid()
            Traceback (most recent call last):
            ...
            ValueError: polyhedron has to be compact

        TESTS::

            sage: CombinatorialPolyhedron(-1).is_bipyramid()
            False
            sage: CombinatorialPolyhedron(-1).is_bipyramid(True)
            (False, None)
            sage: C = polytopes.cross_polytope(1)
            sage: C.is_bipyramid()
            True
            sage: C.is_bipyramid(True)
            (True, [A vertex at (1), A vertex at (-1)])

        Check that bug analog to :issue:`30292` is avoided::

            sage: Polyhedron([[0, 1, 0], [0, 0, 1], [0, -1, -1], [1, 0, 0], [-1, 0, 0]]).is_bipyramid(certificate=True)
            (True, [A vertex at (1, 0, 0), A vertex at (-1, 0, 0)])

        ALGORITHM:

        Assume all faces of a polyhedron to be given as lists of vertices.

        A polytope is a bipyramid with apexes `v`, `w` if and only if for each
        proper face `v \\in F` there exists a face `G` with
        `G \\setminus \\{w\\} = F \\setminus \\{v\\}`
        and vice versa (for each proper face
        `w \\in F` there exists ...).

        To check this property it suffices to check for all facets of the polyhedron."""
    @overload
    def is_bipyramid(self, _True) -> Any:
        """CombinatorialPolyhedron.is_bipyramid(self, certificate=False)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 2431)

        Test whether the polytope is a bipyramid over some other polytope.

        INPUT:

        - ``certificate`` -- boolean (default: ``False``); specifies whether
          to return a vertex of the polytope which is the apex of a pyramid,
          if found

        INPUT:

        - ``certificate`` -- boolean (default: ``False``); specifies whether
          to return two vertices of the polytope which are the apices of a
          bipyramid, if found

        OUTPUT:

        If ``certificate`` is ``True``, returns a tuple containing:

        1. Boolean.
        2. ``None`` or a tuple containing:
            a. The first apex.
            b. The second apex.

        If ``certificate`` is ``False`` returns a boolean.

        EXAMPLES::

            sage: C = polytopes.hypercube(4).combinatorial_polyhedron()
            sage: C.is_bipyramid()
            False
            sage: C.is_bipyramid(certificate=True)
            (False, None)
            sage: C = polytopes.cross_polytope(4).combinatorial_polyhedron()
            sage: C.is_bipyramid()
            True
            sage: C.is_bipyramid(certificate=True)
            (True, [A vertex at (1, 0, 0, 0), A vertex at (-1, 0, 0, 0)])

        For unbounded polyhedra, an error is raised::

            sage: C = CombinatorialPolyhedron([[0,1], [0,2]], far_face=[1,2], unbounded=True)
            sage: C.is_pyramid()
            Traceback (most recent call last):
            ...
            ValueError: polyhedron has to be compact

        TESTS::

            sage: CombinatorialPolyhedron(-1).is_bipyramid()
            False
            sage: CombinatorialPolyhedron(-1).is_bipyramid(True)
            (False, None)
            sage: C = polytopes.cross_polytope(1)
            sage: C.is_bipyramid()
            True
            sage: C.is_bipyramid(True)
            (True, [A vertex at (1), A vertex at (-1)])

        Check that bug analog to :issue:`30292` is avoided::

            sage: Polyhedron([[0, 1, 0], [0, 0, 1], [0, -1, -1], [1, 0, 0], [-1, 0, 0]]).is_bipyramid(certificate=True)
            (True, [A vertex at (1, 0, 0), A vertex at (-1, 0, 0)])

        ALGORITHM:

        Assume all faces of a polyhedron to be given as lists of vertices.

        A polytope is a bipyramid with apexes `v`, `w` if and only if for each
        proper face `v \\in F` there exists a face `G` with
        `G \\setminus \\{w\\} = F \\setminus \\{v\\}`
        and vice versa (for each proper face
        `w \\in F` there exists ...).

        To check this property it suffices to check for all facets of the polyhedron."""
    @overload
    def is_bipyramid(self, certificate=...) -> Any:
        """CombinatorialPolyhedron.is_bipyramid(self, certificate=False)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 2431)

        Test whether the polytope is a bipyramid over some other polytope.

        INPUT:

        - ``certificate`` -- boolean (default: ``False``); specifies whether
          to return a vertex of the polytope which is the apex of a pyramid,
          if found

        INPUT:

        - ``certificate`` -- boolean (default: ``False``); specifies whether
          to return two vertices of the polytope which are the apices of a
          bipyramid, if found

        OUTPUT:

        If ``certificate`` is ``True``, returns a tuple containing:

        1. Boolean.
        2. ``None`` or a tuple containing:
            a. The first apex.
            b. The second apex.

        If ``certificate`` is ``False`` returns a boolean.

        EXAMPLES::

            sage: C = polytopes.hypercube(4).combinatorial_polyhedron()
            sage: C.is_bipyramid()
            False
            sage: C.is_bipyramid(certificate=True)
            (False, None)
            sage: C = polytopes.cross_polytope(4).combinatorial_polyhedron()
            sage: C.is_bipyramid()
            True
            sage: C.is_bipyramid(certificate=True)
            (True, [A vertex at (1, 0, 0, 0), A vertex at (-1, 0, 0, 0)])

        For unbounded polyhedra, an error is raised::

            sage: C = CombinatorialPolyhedron([[0,1], [0,2]], far_face=[1,2], unbounded=True)
            sage: C.is_pyramid()
            Traceback (most recent call last):
            ...
            ValueError: polyhedron has to be compact

        TESTS::

            sage: CombinatorialPolyhedron(-1).is_bipyramid()
            False
            sage: CombinatorialPolyhedron(-1).is_bipyramid(True)
            (False, None)
            sage: C = polytopes.cross_polytope(1)
            sage: C.is_bipyramid()
            True
            sage: C.is_bipyramid(True)
            (True, [A vertex at (1), A vertex at (-1)])

        Check that bug analog to :issue:`30292` is avoided::

            sage: Polyhedron([[0, 1, 0], [0, 0, 1], [0, -1, -1], [1, 0, 0], [-1, 0, 0]]).is_bipyramid(certificate=True)
            (True, [A vertex at (1, 0, 0), A vertex at (-1, 0, 0)])

        ALGORITHM:

        Assume all faces of a polyhedron to be given as lists of vertices.

        A polytope is a bipyramid with apexes `v`, `w` if and only if for each
        proper face `v \\in F` there exists a face `G` with
        `G \\setminus \\{w\\} = F \\setminus \\{v\\}`
        and vice versa (for each proper face
        `w \\in F` there exists ...).

        To check this property it suffices to check for all facets of the polyhedron."""
    @overload
    def is_compact(self) -> Any:
        """CombinatorialPolyhedron.is_compact(self)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 3249)

        Return whether the polyhedron is compact.

        EXAMPLES::

            sage: C = CombinatorialPolyhedron([[0,1], [0,2]], far_face=[1,2], unbounded=True)
            sage: C.is_compact()
            False
            sage: C = CombinatorialPolyhedron([[0,1], [0,2], [1,2]])
            sage: C.is_compact()
            True
            sage: P = polytopes.simplex()
            sage: P.combinatorial_polyhedron().is_compact()
            True
            sage: P = Polyhedron(rays=P.vertices())
            sage: P.combinatorial_polyhedron().is_compact()
            False"""
    @overload
    def is_compact(self) -> Any:
        """CombinatorialPolyhedron.is_compact(self)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 3249)

        Return whether the polyhedron is compact.

        EXAMPLES::

            sage: C = CombinatorialPolyhedron([[0,1], [0,2]], far_face=[1,2], unbounded=True)
            sage: C.is_compact()
            False
            sage: C = CombinatorialPolyhedron([[0,1], [0,2], [1,2]])
            sage: C.is_compact()
            True
            sage: P = polytopes.simplex()
            sage: P.combinatorial_polyhedron().is_compact()
            True
            sage: P = Polyhedron(rays=P.vertices())
            sage: P.combinatorial_polyhedron().is_compact()
            False"""
    @overload
    def is_compact(self) -> Any:
        """CombinatorialPolyhedron.is_compact(self)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 3249)

        Return whether the polyhedron is compact.

        EXAMPLES::

            sage: C = CombinatorialPolyhedron([[0,1], [0,2]], far_face=[1,2], unbounded=True)
            sage: C.is_compact()
            False
            sage: C = CombinatorialPolyhedron([[0,1], [0,2], [1,2]])
            sage: C.is_compact()
            True
            sage: P = polytopes.simplex()
            sage: P.combinatorial_polyhedron().is_compact()
            True
            sage: P = Polyhedron(rays=P.vertices())
            sage: P.combinatorial_polyhedron().is_compact()
            False"""
    @overload
    def is_compact(self) -> Any:
        """CombinatorialPolyhedron.is_compact(self)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 3249)

        Return whether the polyhedron is compact.

        EXAMPLES::

            sage: C = CombinatorialPolyhedron([[0,1], [0,2]], far_face=[1,2], unbounded=True)
            sage: C.is_compact()
            False
            sage: C = CombinatorialPolyhedron([[0,1], [0,2], [1,2]])
            sage: C.is_compact()
            True
            sage: P = polytopes.simplex()
            sage: P.combinatorial_polyhedron().is_compact()
            True
            sage: P = Polyhedron(rays=P.vertices())
            sage: P.combinatorial_polyhedron().is_compact()
            False"""
    @overload
    def is_compact(self) -> Any:
        """CombinatorialPolyhedron.is_compact(self)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 3249)

        Return whether the polyhedron is compact.

        EXAMPLES::

            sage: C = CombinatorialPolyhedron([[0,1], [0,2]], far_face=[1,2], unbounded=True)
            sage: C.is_compact()
            False
            sage: C = CombinatorialPolyhedron([[0,1], [0,2], [1,2]])
            sage: C.is_compact()
            True
            sage: P = polytopes.simplex()
            sage: P.combinatorial_polyhedron().is_compact()
            True
            sage: P = Polyhedron(rays=P.vertices())
            sage: P.combinatorial_polyhedron().is_compact()
            False"""
    def is_lawrence_polytope(self) -> Any:
        """CombinatorialPolyhedron.is_lawrence_polytope(self)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 2241)

        Return ``True`` if ``self`` is a Lawrence polytope.

        A polytope is called a Lawrence polytope if it has a centrally
        symmetric (normalized) Gale diagram.

        Equivalently, there exists a partition `P_1,\\dots,P_k`
        of the vertices `V` such that each part
        `P_i` has size `2` or `1` and for each part there exists
        a facet with vertices exactly `V \\setminus P_i`.

        EXAMPLES::

            sage: C = polytopes.simplex(5).combinatorial_polyhedron()
            sage: C.is_lawrence_polytope()
            True
            sage: P = polytopes.hypercube(4).lawrence_polytope()
            sage: C = P.combinatorial_polyhedron()
            sage: C.is_lawrence_polytope()
            True
            sage: P = polytopes.hypercube(4)
            sage: C = P.combinatorial_polyhedron()
            sage: C.is_lawrence_polytope()
            False

        For unbounded polyhedra, an error is raised::

            sage: C = CombinatorialPolyhedron([[0,1], [0,2]], far_face=[1,2], unbounded=True)
            sage: C.is_lawrence_polytope()
            Traceback (most recent call last):
            ...
            NotImplementedError: this function is implemented for polytopes only

        AUTHORS:

        - Laith Rastanawi
        - Jonathan Kliem

        REFERENCES:

            For more information, see [BaSt1990]_."""
    @overload
    def is_neighborly(self, k=...) -> bool:
        """CombinatorialPolyhedron.is_neighborly(self, k=None) -> bool

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 1953)

        Return whether the polyhedron is neighborly.

        If the input `k` is provided, then return whether the polyhedron is `k`-neighborly.

        A polyhedron is neighborly if every set of `n` vertices forms a face
        for `n` up to floor of half the dimension of the polyhedron.
        It is `k`-neighborly if this is true for `n` up to `k`.

        INPUT:

        - ``k`` -- the dimension up to which to check if every set of ``k``
          vertices forms a face. If no ``k`` is provided, check up to floor
          of half the dimension of the polyhedron.

        OUTPUT:

        - ``True`` if the every set of up to ``k`` vertices forms a face,
        - ``False`` otherwise

        .. SEEALSO::

            :meth:`neighborliness`

        EXAMPLES::

            sage: P = polytopes.cyclic_polytope(8,12)
            sage: C = P.combinatorial_polyhedron()
            sage: C.is_neighborly()
            True
            sage: P = polytopes.simplex(6)
            sage: C = P.combinatorial_polyhedron()
            sage: C.is_neighborly()
            True
            sage: P = polytopes.cyclic_polytope(4,10)
            sage: P = P.join(P)
            sage: C = P.combinatorial_polyhedron()
            sage: C.is_neighborly()
            False
            sage: C.is_neighborly(k=2)
            True"""
    @overload
    def is_neighborly(self) -> Any:
        """CombinatorialPolyhedron.is_neighborly(self, k=None) -> bool

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 1953)

        Return whether the polyhedron is neighborly.

        If the input `k` is provided, then return whether the polyhedron is `k`-neighborly.

        A polyhedron is neighborly if every set of `n` vertices forms a face
        for `n` up to floor of half the dimension of the polyhedron.
        It is `k`-neighborly if this is true for `n` up to `k`.

        INPUT:

        - ``k`` -- the dimension up to which to check if every set of ``k``
          vertices forms a face. If no ``k`` is provided, check up to floor
          of half the dimension of the polyhedron.

        OUTPUT:

        - ``True`` if the every set of up to ``k`` vertices forms a face,
        - ``False`` otherwise

        .. SEEALSO::

            :meth:`neighborliness`

        EXAMPLES::

            sage: P = polytopes.cyclic_polytope(8,12)
            sage: C = P.combinatorial_polyhedron()
            sage: C.is_neighborly()
            True
            sage: P = polytopes.simplex(6)
            sage: C = P.combinatorial_polyhedron()
            sage: C.is_neighborly()
            True
            sage: P = polytopes.cyclic_polytope(4,10)
            sage: P = P.join(P)
            sage: C = P.combinatorial_polyhedron()
            sage: C.is_neighborly()
            False
            sage: C.is_neighborly(k=2)
            True"""
    @overload
    def is_neighborly(self) -> Any:
        """CombinatorialPolyhedron.is_neighborly(self, k=None) -> bool

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 1953)

        Return whether the polyhedron is neighborly.

        If the input `k` is provided, then return whether the polyhedron is `k`-neighborly.

        A polyhedron is neighborly if every set of `n` vertices forms a face
        for `n` up to floor of half the dimension of the polyhedron.
        It is `k`-neighborly if this is true for `n` up to `k`.

        INPUT:

        - ``k`` -- the dimension up to which to check if every set of ``k``
          vertices forms a face. If no ``k`` is provided, check up to floor
          of half the dimension of the polyhedron.

        OUTPUT:

        - ``True`` if the every set of up to ``k`` vertices forms a face,
        - ``False`` otherwise

        .. SEEALSO::

            :meth:`neighborliness`

        EXAMPLES::

            sage: P = polytopes.cyclic_polytope(8,12)
            sage: C = P.combinatorial_polyhedron()
            sage: C.is_neighborly()
            True
            sage: P = polytopes.simplex(6)
            sage: C = P.combinatorial_polyhedron()
            sage: C.is_neighborly()
            True
            sage: P = polytopes.cyclic_polytope(4,10)
            sage: P = P.join(P)
            sage: C = P.combinatorial_polyhedron()
            sage: C.is_neighborly()
            False
            sage: C.is_neighborly(k=2)
            True"""
    @overload
    def is_neighborly(self) -> Any:
        """CombinatorialPolyhedron.is_neighborly(self, k=None) -> bool

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 1953)

        Return whether the polyhedron is neighborly.

        If the input `k` is provided, then return whether the polyhedron is `k`-neighborly.

        A polyhedron is neighborly if every set of `n` vertices forms a face
        for `n` up to floor of half the dimension of the polyhedron.
        It is `k`-neighborly if this is true for `n` up to `k`.

        INPUT:

        - ``k`` -- the dimension up to which to check if every set of ``k``
          vertices forms a face. If no ``k`` is provided, check up to floor
          of half the dimension of the polyhedron.

        OUTPUT:

        - ``True`` if the every set of up to ``k`` vertices forms a face,
        - ``False`` otherwise

        .. SEEALSO::

            :meth:`neighborliness`

        EXAMPLES::

            sage: P = polytopes.cyclic_polytope(8,12)
            sage: C = P.combinatorial_polyhedron()
            sage: C.is_neighborly()
            True
            sage: P = polytopes.simplex(6)
            sage: C = P.combinatorial_polyhedron()
            sage: C.is_neighborly()
            True
            sage: P = polytopes.cyclic_polytope(4,10)
            sage: P = P.join(P)
            sage: C = P.combinatorial_polyhedron()
            sage: C.is_neighborly()
            False
            sage: C.is_neighborly(k=2)
            True"""
    @overload
    def is_neighborly(self, k=...) -> Any:
        """CombinatorialPolyhedron.is_neighborly(self, k=None) -> bool

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 1953)

        Return whether the polyhedron is neighborly.

        If the input `k` is provided, then return whether the polyhedron is `k`-neighborly.

        A polyhedron is neighborly if every set of `n` vertices forms a face
        for `n` up to floor of half the dimension of the polyhedron.
        It is `k`-neighborly if this is true for `n` up to `k`.

        INPUT:

        - ``k`` -- the dimension up to which to check if every set of ``k``
          vertices forms a face. If no ``k`` is provided, check up to floor
          of half the dimension of the polyhedron.

        OUTPUT:

        - ``True`` if the every set of up to ``k`` vertices forms a face,
        - ``False`` otherwise

        .. SEEALSO::

            :meth:`neighborliness`

        EXAMPLES::

            sage: P = polytopes.cyclic_polytope(8,12)
            sage: C = P.combinatorial_polyhedron()
            sage: C.is_neighborly()
            True
            sage: P = polytopes.simplex(6)
            sage: C = P.combinatorial_polyhedron()
            sage: C.is_neighborly()
            True
            sage: P = polytopes.cyclic_polytope(4,10)
            sage: P = P.join(P)
            sage: C = P.combinatorial_polyhedron()
            sage: C.is_neighborly()
            False
            sage: C.is_neighborly(k=2)
            True"""
    @overload
    def is_prism(self, certificate=...) -> Any:
        """CombinatorialPolyhedron.is_prism(self, certificate=False)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 2551)

        Test whether the polytope is a prism of some polytope.

        INPUT:

        - ``certificate`` -- boolean (default: ``False``); specifies whether
          to return two facets of the polytope which are the bases of a prism,
          if found

        OUTPUT:

        If ``certificate`` is ``True``, returns a tuple containing:

        1. Boolean.
        2. ``None`` or a tuple containing:
            a. List of the vertices of the first base facet.
            b. List of the vertices of the second base facet.

        If ``certificate`` is ``False`` returns a boolean.

        TESTS::

            sage: CombinatorialPolyhedron(-1).is_prism()
            False
            sage: CombinatorialPolyhedron(1).is_prism()
            False
            sage: C = polytopes.cross_polytope(3).prism().combinatorial_polyhedron()
            sage: C.is_prism(certificate=True)
            (True,
            [(A vertex at (0, 0, 1, 0),
            A vertex at (0, 1, 0, 0),
            A vertex at (0, 0, 0, -1),
            A vertex at (0, 0, -1, 0),
            A vertex at (0, -1, 0, 0),
            A vertex at (0, 0, 0, 1)),
            (A vertex at (1, 1, 0, 0),
            A vertex at (1, 0, 0, -1),
            A vertex at (1, 0, -1, 0),
            A vertex at (1, -1, 0, 0),
            A vertex at (1, 0, 0, 1),
            A vertex at (1, 0, 1, 0))])
            sage: C = CombinatorialPolyhedron([[0,1], [0,2]], far_face=[1,2], unbounded=True)
            sage: C.is_prism()
            Traceback (most recent call last):
            ...
            ValueError: self must be bounded"""
    @overload
    def is_prism(self) -> Any:
        """CombinatorialPolyhedron.is_prism(self, certificate=False)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 2551)

        Test whether the polytope is a prism of some polytope.

        INPUT:

        - ``certificate`` -- boolean (default: ``False``); specifies whether
          to return two facets of the polytope which are the bases of a prism,
          if found

        OUTPUT:

        If ``certificate`` is ``True``, returns a tuple containing:

        1. Boolean.
        2. ``None`` or a tuple containing:
            a. List of the vertices of the first base facet.
            b. List of the vertices of the second base facet.

        If ``certificate`` is ``False`` returns a boolean.

        TESTS::

            sage: CombinatorialPolyhedron(-1).is_prism()
            False
            sage: CombinatorialPolyhedron(1).is_prism()
            False
            sage: C = polytopes.cross_polytope(3).prism().combinatorial_polyhedron()
            sage: C.is_prism(certificate=True)
            (True,
            [(A vertex at (0, 0, 1, 0),
            A vertex at (0, 1, 0, 0),
            A vertex at (0, 0, 0, -1),
            A vertex at (0, 0, -1, 0),
            A vertex at (0, -1, 0, 0),
            A vertex at (0, 0, 0, 1)),
            (A vertex at (1, 1, 0, 0),
            A vertex at (1, 0, 0, -1),
            A vertex at (1, 0, -1, 0),
            A vertex at (1, -1, 0, 0),
            A vertex at (1, 0, 0, 1),
            A vertex at (1, 0, 1, 0))])
            sage: C = CombinatorialPolyhedron([[0,1], [0,2]], far_face=[1,2], unbounded=True)
            sage: C.is_prism()
            Traceback (most recent call last):
            ...
            ValueError: self must be bounded"""
    @overload
    def is_prism(self) -> Any:
        """CombinatorialPolyhedron.is_prism(self, certificate=False)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 2551)

        Test whether the polytope is a prism of some polytope.

        INPUT:

        - ``certificate`` -- boolean (default: ``False``); specifies whether
          to return two facets of the polytope which are the bases of a prism,
          if found

        OUTPUT:

        If ``certificate`` is ``True``, returns a tuple containing:

        1. Boolean.
        2. ``None`` or a tuple containing:
            a. List of the vertices of the first base facet.
            b. List of the vertices of the second base facet.

        If ``certificate`` is ``False`` returns a boolean.

        TESTS::

            sage: CombinatorialPolyhedron(-1).is_prism()
            False
            sage: CombinatorialPolyhedron(1).is_prism()
            False
            sage: C = polytopes.cross_polytope(3).prism().combinatorial_polyhedron()
            sage: C.is_prism(certificate=True)
            (True,
            [(A vertex at (0, 0, 1, 0),
            A vertex at (0, 1, 0, 0),
            A vertex at (0, 0, 0, -1),
            A vertex at (0, 0, -1, 0),
            A vertex at (0, -1, 0, 0),
            A vertex at (0, 0, 0, 1)),
            (A vertex at (1, 1, 0, 0),
            A vertex at (1, 0, 0, -1),
            A vertex at (1, 0, -1, 0),
            A vertex at (1, -1, 0, 0),
            A vertex at (1, 0, 0, 1),
            A vertex at (1, 0, 1, 0))])
            sage: C = CombinatorialPolyhedron([[0,1], [0,2]], far_face=[1,2], unbounded=True)
            sage: C.is_prism()
            Traceback (most recent call last):
            ...
            ValueError: self must be bounded"""
    @overload
    def is_prism(self, certificate=...) -> Any:
        """CombinatorialPolyhedron.is_prism(self, certificate=False)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 2551)

        Test whether the polytope is a prism of some polytope.

        INPUT:

        - ``certificate`` -- boolean (default: ``False``); specifies whether
          to return two facets of the polytope which are the bases of a prism,
          if found

        OUTPUT:

        If ``certificate`` is ``True``, returns a tuple containing:

        1. Boolean.
        2. ``None`` or a tuple containing:
            a. List of the vertices of the first base facet.
            b. List of the vertices of the second base facet.

        If ``certificate`` is ``False`` returns a boolean.

        TESTS::

            sage: CombinatorialPolyhedron(-1).is_prism()
            False
            sage: CombinatorialPolyhedron(1).is_prism()
            False
            sage: C = polytopes.cross_polytope(3).prism().combinatorial_polyhedron()
            sage: C.is_prism(certificate=True)
            (True,
            [(A vertex at (0, 0, 1, 0),
            A vertex at (0, 1, 0, 0),
            A vertex at (0, 0, 0, -1),
            A vertex at (0, 0, -1, 0),
            A vertex at (0, -1, 0, 0),
            A vertex at (0, 0, 0, 1)),
            (A vertex at (1, 1, 0, 0),
            A vertex at (1, 0, 0, -1),
            A vertex at (1, 0, -1, 0),
            A vertex at (1, -1, 0, 0),
            A vertex at (1, 0, 0, 1),
            A vertex at (1, 0, 1, 0))])
            sage: C = CombinatorialPolyhedron([[0,1], [0,2]], far_face=[1,2], unbounded=True)
            sage: C.is_prism()
            Traceback (most recent call last):
            ...
            ValueError: self must be bounded"""
    @overload
    def is_prism(self) -> Any:
        """CombinatorialPolyhedron.is_prism(self, certificate=False)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 2551)

        Test whether the polytope is a prism of some polytope.

        INPUT:

        - ``certificate`` -- boolean (default: ``False``); specifies whether
          to return two facets of the polytope which are the bases of a prism,
          if found

        OUTPUT:

        If ``certificate`` is ``True``, returns a tuple containing:

        1. Boolean.
        2. ``None`` or a tuple containing:
            a. List of the vertices of the first base facet.
            b. List of the vertices of the second base facet.

        If ``certificate`` is ``False`` returns a boolean.

        TESTS::

            sage: CombinatorialPolyhedron(-1).is_prism()
            False
            sage: CombinatorialPolyhedron(1).is_prism()
            False
            sage: C = polytopes.cross_polytope(3).prism().combinatorial_polyhedron()
            sage: C.is_prism(certificate=True)
            (True,
            [(A vertex at (0, 0, 1, 0),
            A vertex at (0, 1, 0, 0),
            A vertex at (0, 0, 0, -1),
            A vertex at (0, 0, -1, 0),
            A vertex at (0, -1, 0, 0),
            A vertex at (0, 0, 0, 1)),
            (A vertex at (1, 1, 0, 0),
            A vertex at (1, 0, 0, -1),
            A vertex at (1, 0, -1, 0),
            A vertex at (1, -1, 0, 0),
            A vertex at (1, 0, 0, 1),
            A vertex at (1, 0, 1, 0))])
            sage: C = CombinatorialPolyhedron([[0,1], [0,2]], far_face=[1,2], unbounded=True)
            sage: C.is_prism()
            Traceback (most recent call last):
            ...
            ValueError: self must be bounded"""
    @overload
    def is_pyramid(self, certificate=...) -> Any:
        """CombinatorialPolyhedron.is_pyramid(self, certificate=False)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 2340)

        Test whether the polytope is a pyramid over one of its facets.

        INPUT:

        - ``certificate`` -- boolean (default: ``False``); specifies whether
          to return a vertex of the polytope which is the apex of a pyramid,
          if found

        OUTPUT:

        If ``certificate`` is ``True``, returns a tuple containing:

        1. Boolean.
        2. The apex of the pyramid or ``None``.

        If ``certificate`` is ``False`` returns a boolean.

        AUTHORS:

        - Laith Rastanawi
        - Jonathan Kliem

        EXAMPLES::

            sage: C = polytopes.cross_polytope(4).combinatorial_polyhedron()
            sage: C.is_pyramid()
            False
            sage: C.is_pyramid(certificate=True)
            (False, None)
            sage: C = polytopes.cross_polytope(4).pyramid().combinatorial_polyhedron()
            sage: C.is_pyramid()
            True
            sage: C.is_pyramid(certificate=True)
            (True, A vertex at (1, 0, 0, 0, 0))
            sage: C = polytopes.simplex(5).combinatorial_polyhedron()
            sage: C.is_pyramid(certificate=True)
            (True, A vertex at (1, 0, 0, 0, 0, 0))

        For unbounded polyhedra, an error is raised::

            sage: C = CombinatorialPolyhedron([[0,1], [0,2]], far_face=[1,2], unbounded=True)
            sage: C.is_pyramid()
            Traceback (most recent call last):
            ...
            ValueError: polyhedron has to be compact

        TESTS::

            sage: CombinatorialPolyhedron(-1).is_pyramid()
            False
            sage: CombinatorialPolyhedron(-1).is_pyramid(True)
            (False, None)
            sage: CombinatorialPolyhedron(0).is_pyramid()
            True
            sage: CombinatorialPolyhedron(0).is_pyramid(True)
            (True, 0)

        Check that :issue:`30292` is fixed::

            sage: Polyhedron([[0, -1, -1], [0, -1, 1], [0, 1, -1], [0, 1, 1], [1, 0, 0]]).is_pyramid(certificate=True)
            (True, A vertex at (1, 0, 0))"""
    @overload
    def is_pyramid(self) -> Any:
        """CombinatorialPolyhedron.is_pyramid(self, certificate=False)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 2340)

        Test whether the polytope is a pyramid over one of its facets.

        INPUT:

        - ``certificate`` -- boolean (default: ``False``); specifies whether
          to return a vertex of the polytope which is the apex of a pyramid,
          if found

        OUTPUT:

        If ``certificate`` is ``True``, returns a tuple containing:

        1. Boolean.
        2. The apex of the pyramid or ``None``.

        If ``certificate`` is ``False`` returns a boolean.

        AUTHORS:

        - Laith Rastanawi
        - Jonathan Kliem

        EXAMPLES::

            sage: C = polytopes.cross_polytope(4).combinatorial_polyhedron()
            sage: C.is_pyramid()
            False
            sage: C.is_pyramid(certificate=True)
            (False, None)
            sage: C = polytopes.cross_polytope(4).pyramid().combinatorial_polyhedron()
            sage: C.is_pyramid()
            True
            sage: C.is_pyramid(certificate=True)
            (True, A vertex at (1, 0, 0, 0, 0))
            sage: C = polytopes.simplex(5).combinatorial_polyhedron()
            sage: C.is_pyramid(certificate=True)
            (True, A vertex at (1, 0, 0, 0, 0, 0))

        For unbounded polyhedra, an error is raised::

            sage: C = CombinatorialPolyhedron([[0,1], [0,2]], far_face=[1,2], unbounded=True)
            sage: C.is_pyramid()
            Traceback (most recent call last):
            ...
            ValueError: polyhedron has to be compact

        TESTS::

            sage: CombinatorialPolyhedron(-1).is_pyramid()
            False
            sage: CombinatorialPolyhedron(-1).is_pyramid(True)
            (False, None)
            sage: CombinatorialPolyhedron(0).is_pyramid()
            True
            sage: CombinatorialPolyhedron(0).is_pyramid(True)
            (True, 0)

        Check that :issue:`30292` is fixed::

            sage: Polyhedron([[0, -1, -1], [0, -1, 1], [0, 1, -1], [0, 1, 1], [1, 0, 0]]).is_pyramid(certificate=True)
            (True, A vertex at (1, 0, 0))"""
    @overload
    def is_pyramid(self, certificate=...) -> Any:
        """CombinatorialPolyhedron.is_pyramid(self, certificate=False)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 2340)

        Test whether the polytope is a pyramid over one of its facets.

        INPUT:

        - ``certificate`` -- boolean (default: ``False``); specifies whether
          to return a vertex of the polytope which is the apex of a pyramid,
          if found

        OUTPUT:

        If ``certificate`` is ``True``, returns a tuple containing:

        1. Boolean.
        2. The apex of the pyramid or ``None``.

        If ``certificate`` is ``False`` returns a boolean.

        AUTHORS:

        - Laith Rastanawi
        - Jonathan Kliem

        EXAMPLES::

            sage: C = polytopes.cross_polytope(4).combinatorial_polyhedron()
            sage: C.is_pyramid()
            False
            sage: C.is_pyramid(certificate=True)
            (False, None)
            sage: C = polytopes.cross_polytope(4).pyramid().combinatorial_polyhedron()
            sage: C.is_pyramid()
            True
            sage: C.is_pyramid(certificate=True)
            (True, A vertex at (1, 0, 0, 0, 0))
            sage: C = polytopes.simplex(5).combinatorial_polyhedron()
            sage: C.is_pyramid(certificate=True)
            (True, A vertex at (1, 0, 0, 0, 0, 0))

        For unbounded polyhedra, an error is raised::

            sage: C = CombinatorialPolyhedron([[0,1], [0,2]], far_face=[1,2], unbounded=True)
            sage: C.is_pyramid()
            Traceback (most recent call last):
            ...
            ValueError: polyhedron has to be compact

        TESTS::

            sage: CombinatorialPolyhedron(-1).is_pyramid()
            False
            sage: CombinatorialPolyhedron(-1).is_pyramid(True)
            (False, None)
            sage: CombinatorialPolyhedron(0).is_pyramid()
            True
            sage: CombinatorialPolyhedron(0).is_pyramid(True)
            (True, 0)

        Check that :issue:`30292` is fixed::

            sage: Polyhedron([[0, -1, -1], [0, -1, 1], [0, 1, -1], [0, 1, 1], [1, 0, 0]]).is_pyramid(certificate=True)
            (True, A vertex at (1, 0, 0))"""
    @overload
    def is_pyramid(self) -> Any:
        """CombinatorialPolyhedron.is_pyramid(self, certificate=False)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 2340)

        Test whether the polytope is a pyramid over one of its facets.

        INPUT:

        - ``certificate`` -- boolean (default: ``False``); specifies whether
          to return a vertex of the polytope which is the apex of a pyramid,
          if found

        OUTPUT:

        If ``certificate`` is ``True``, returns a tuple containing:

        1. Boolean.
        2. The apex of the pyramid or ``None``.

        If ``certificate`` is ``False`` returns a boolean.

        AUTHORS:

        - Laith Rastanawi
        - Jonathan Kliem

        EXAMPLES::

            sage: C = polytopes.cross_polytope(4).combinatorial_polyhedron()
            sage: C.is_pyramid()
            False
            sage: C.is_pyramid(certificate=True)
            (False, None)
            sage: C = polytopes.cross_polytope(4).pyramid().combinatorial_polyhedron()
            sage: C.is_pyramid()
            True
            sage: C.is_pyramid(certificate=True)
            (True, A vertex at (1, 0, 0, 0, 0))
            sage: C = polytopes.simplex(5).combinatorial_polyhedron()
            sage: C.is_pyramid(certificate=True)
            (True, A vertex at (1, 0, 0, 0, 0, 0))

        For unbounded polyhedra, an error is raised::

            sage: C = CombinatorialPolyhedron([[0,1], [0,2]], far_face=[1,2], unbounded=True)
            sage: C.is_pyramid()
            Traceback (most recent call last):
            ...
            ValueError: polyhedron has to be compact

        TESTS::

            sage: CombinatorialPolyhedron(-1).is_pyramid()
            False
            sage: CombinatorialPolyhedron(-1).is_pyramid(True)
            (False, None)
            sage: CombinatorialPolyhedron(0).is_pyramid()
            True
            sage: CombinatorialPolyhedron(0).is_pyramid(True)
            (True, 0)

        Check that :issue:`30292` is fixed::

            sage: Polyhedron([[0, -1, -1], [0, -1, 1], [0, 1, -1], [0, 1, 1], [1, 0, 0]]).is_pyramid(certificate=True)
            (True, A vertex at (1, 0, 0))"""
    @overload
    def is_pyramid(self, certificate=...) -> Any:
        """CombinatorialPolyhedron.is_pyramid(self, certificate=False)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 2340)

        Test whether the polytope is a pyramid over one of its facets.

        INPUT:

        - ``certificate`` -- boolean (default: ``False``); specifies whether
          to return a vertex of the polytope which is the apex of a pyramid,
          if found

        OUTPUT:

        If ``certificate`` is ``True``, returns a tuple containing:

        1. Boolean.
        2. The apex of the pyramid or ``None``.

        If ``certificate`` is ``False`` returns a boolean.

        AUTHORS:

        - Laith Rastanawi
        - Jonathan Kliem

        EXAMPLES::

            sage: C = polytopes.cross_polytope(4).combinatorial_polyhedron()
            sage: C.is_pyramid()
            False
            sage: C.is_pyramid(certificate=True)
            (False, None)
            sage: C = polytopes.cross_polytope(4).pyramid().combinatorial_polyhedron()
            sage: C.is_pyramid()
            True
            sage: C.is_pyramid(certificate=True)
            (True, A vertex at (1, 0, 0, 0, 0))
            sage: C = polytopes.simplex(5).combinatorial_polyhedron()
            sage: C.is_pyramid(certificate=True)
            (True, A vertex at (1, 0, 0, 0, 0, 0))

        For unbounded polyhedra, an error is raised::

            sage: C = CombinatorialPolyhedron([[0,1], [0,2]], far_face=[1,2], unbounded=True)
            sage: C.is_pyramid()
            Traceback (most recent call last):
            ...
            ValueError: polyhedron has to be compact

        TESTS::

            sage: CombinatorialPolyhedron(-1).is_pyramid()
            False
            sage: CombinatorialPolyhedron(-1).is_pyramid(True)
            (False, None)
            sage: CombinatorialPolyhedron(0).is_pyramid()
            True
            sage: CombinatorialPolyhedron(0).is_pyramid(True)
            (True, 0)

        Check that :issue:`30292` is fixed::

            sage: Polyhedron([[0, -1, -1], [0, -1, 1], [0, 1, -1], [0, 1, 1], [1, 0, 0]]).is_pyramid(certificate=True)
            (True, A vertex at (1, 0, 0))"""
    @overload
    def is_pyramid(self, certificate=...) -> Any:
        """CombinatorialPolyhedron.is_pyramid(self, certificate=False)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 2340)

        Test whether the polytope is a pyramid over one of its facets.

        INPUT:

        - ``certificate`` -- boolean (default: ``False``); specifies whether
          to return a vertex of the polytope which is the apex of a pyramid,
          if found

        OUTPUT:

        If ``certificate`` is ``True``, returns a tuple containing:

        1. Boolean.
        2. The apex of the pyramid or ``None``.

        If ``certificate`` is ``False`` returns a boolean.

        AUTHORS:

        - Laith Rastanawi
        - Jonathan Kliem

        EXAMPLES::

            sage: C = polytopes.cross_polytope(4).combinatorial_polyhedron()
            sage: C.is_pyramid()
            False
            sage: C.is_pyramid(certificate=True)
            (False, None)
            sage: C = polytopes.cross_polytope(4).pyramid().combinatorial_polyhedron()
            sage: C.is_pyramid()
            True
            sage: C.is_pyramid(certificate=True)
            (True, A vertex at (1, 0, 0, 0, 0))
            sage: C = polytopes.simplex(5).combinatorial_polyhedron()
            sage: C.is_pyramid(certificate=True)
            (True, A vertex at (1, 0, 0, 0, 0, 0))

        For unbounded polyhedra, an error is raised::

            sage: C = CombinatorialPolyhedron([[0,1], [0,2]], far_face=[1,2], unbounded=True)
            sage: C.is_pyramid()
            Traceback (most recent call last):
            ...
            ValueError: polyhedron has to be compact

        TESTS::

            sage: CombinatorialPolyhedron(-1).is_pyramid()
            False
            sage: CombinatorialPolyhedron(-1).is_pyramid(True)
            (False, None)
            sage: CombinatorialPolyhedron(0).is_pyramid()
            True
            sage: CombinatorialPolyhedron(0).is_pyramid(True)
            (True, 0)

        Check that :issue:`30292` is fixed::

            sage: Polyhedron([[0, -1, -1], [0, -1, 1], [0, 1, -1], [0, 1, 1], [1, 0, 0]]).is_pyramid(certificate=True)
            (True, A vertex at (1, 0, 0))"""
    @overload
    def is_pyramid(self) -> Any:
        """CombinatorialPolyhedron.is_pyramid(self, certificate=False)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 2340)

        Test whether the polytope is a pyramid over one of its facets.

        INPUT:

        - ``certificate`` -- boolean (default: ``False``); specifies whether
          to return a vertex of the polytope which is the apex of a pyramid,
          if found

        OUTPUT:

        If ``certificate`` is ``True``, returns a tuple containing:

        1. Boolean.
        2. The apex of the pyramid or ``None``.

        If ``certificate`` is ``False`` returns a boolean.

        AUTHORS:

        - Laith Rastanawi
        - Jonathan Kliem

        EXAMPLES::

            sage: C = polytopes.cross_polytope(4).combinatorial_polyhedron()
            sage: C.is_pyramid()
            False
            sage: C.is_pyramid(certificate=True)
            (False, None)
            sage: C = polytopes.cross_polytope(4).pyramid().combinatorial_polyhedron()
            sage: C.is_pyramid()
            True
            sage: C.is_pyramid(certificate=True)
            (True, A vertex at (1, 0, 0, 0, 0))
            sage: C = polytopes.simplex(5).combinatorial_polyhedron()
            sage: C.is_pyramid(certificate=True)
            (True, A vertex at (1, 0, 0, 0, 0, 0))

        For unbounded polyhedra, an error is raised::

            sage: C = CombinatorialPolyhedron([[0,1], [0,2]], far_face=[1,2], unbounded=True)
            sage: C.is_pyramid()
            Traceback (most recent call last):
            ...
            ValueError: polyhedron has to be compact

        TESTS::

            sage: CombinatorialPolyhedron(-1).is_pyramid()
            False
            sage: CombinatorialPolyhedron(-1).is_pyramid(True)
            (False, None)
            sage: CombinatorialPolyhedron(0).is_pyramid()
            True
            sage: CombinatorialPolyhedron(0).is_pyramid(True)
            (True, 0)

        Check that :issue:`30292` is fixed::

            sage: Polyhedron([[0, -1, -1], [0, -1, 1], [0, 1, -1], [0, 1, 1], [1, 0, 0]]).is_pyramid(certificate=True)
            (True, A vertex at (1, 0, 0))"""
    @overload
    def is_pyramid(self) -> Any:
        """CombinatorialPolyhedron.is_pyramid(self, certificate=False)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 2340)

        Test whether the polytope is a pyramid over one of its facets.

        INPUT:

        - ``certificate`` -- boolean (default: ``False``); specifies whether
          to return a vertex of the polytope which is the apex of a pyramid,
          if found

        OUTPUT:

        If ``certificate`` is ``True``, returns a tuple containing:

        1. Boolean.
        2. The apex of the pyramid or ``None``.

        If ``certificate`` is ``False`` returns a boolean.

        AUTHORS:

        - Laith Rastanawi
        - Jonathan Kliem

        EXAMPLES::

            sage: C = polytopes.cross_polytope(4).combinatorial_polyhedron()
            sage: C.is_pyramid()
            False
            sage: C.is_pyramid(certificate=True)
            (False, None)
            sage: C = polytopes.cross_polytope(4).pyramid().combinatorial_polyhedron()
            sage: C.is_pyramid()
            True
            sage: C.is_pyramid(certificate=True)
            (True, A vertex at (1, 0, 0, 0, 0))
            sage: C = polytopes.simplex(5).combinatorial_polyhedron()
            sage: C.is_pyramid(certificate=True)
            (True, A vertex at (1, 0, 0, 0, 0, 0))

        For unbounded polyhedra, an error is raised::

            sage: C = CombinatorialPolyhedron([[0,1], [0,2]], far_face=[1,2], unbounded=True)
            sage: C.is_pyramid()
            Traceback (most recent call last):
            ...
            ValueError: polyhedron has to be compact

        TESTS::

            sage: CombinatorialPolyhedron(-1).is_pyramid()
            False
            sage: CombinatorialPolyhedron(-1).is_pyramid(True)
            (False, None)
            sage: CombinatorialPolyhedron(0).is_pyramid()
            True
            sage: CombinatorialPolyhedron(0).is_pyramid(True)
            (True, 0)

        Check that :issue:`30292` is fixed::

            sage: Polyhedron([[0, -1, -1], [0, -1, 1], [0, 1, -1], [0, 1, 1], [1, 0, 0]]).is_pyramid(certificate=True)
            (True, A vertex at (1, 0, 0))"""
    @overload
    def is_pyramid(self, _True) -> Any:
        """CombinatorialPolyhedron.is_pyramid(self, certificate=False)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 2340)

        Test whether the polytope is a pyramid over one of its facets.

        INPUT:

        - ``certificate`` -- boolean (default: ``False``); specifies whether
          to return a vertex of the polytope which is the apex of a pyramid,
          if found

        OUTPUT:

        If ``certificate`` is ``True``, returns a tuple containing:

        1. Boolean.
        2. The apex of the pyramid or ``None``.

        If ``certificate`` is ``False`` returns a boolean.

        AUTHORS:

        - Laith Rastanawi
        - Jonathan Kliem

        EXAMPLES::

            sage: C = polytopes.cross_polytope(4).combinatorial_polyhedron()
            sage: C.is_pyramid()
            False
            sage: C.is_pyramid(certificate=True)
            (False, None)
            sage: C = polytopes.cross_polytope(4).pyramid().combinatorial_polyhedron()
            sage: C.is_pyramid()
            True
            sage: C.is_pyramid(certificate=True)
            (True, A vertex at (1, 0, 0, 0, 0))
            sage: C = polytopes.simplex(5).combinatorial_polyhedron()
            sage: C.is_pyramid(certificate=True)
            (True, A vertex at (1, 0, 0, 0, 0, 0))

        For unbounded polyhedra, an error is raised::

            sage: C = CombinatorialPolyhedron([[0,1], [0,2]], far_face=[1,2], unbounded=True)
            sage: C.is_pyramid()
            Traceback (most recent call last):
            ...
            ValueError: polyhedron has to be compact

        TESTS::

            sage: CombinatorialPolyhedron(-1).is_pyramid()
            False
            sage: CombinatorialPolyhedron(-1).is_pyramid(True)
            (False, None)
            sage: CombinatorialPolyhedron(0).is_pyramid()
            True
            sage: CombinatorialPolyhedron(0).is_pyramid(True)
            (True, 0)

        Check that :issue:`30292` is fixed::

            sage: Polyhedron([[0, -1, -1], [0, -1, 1], [0, 1, -1], [0, 1, 1], [1, 0, 0]]).is_pyramid(certificate=True)
            (True, A vertex at (1, 0, 0))"""
    @overload
    def is_pyramid(self) -> Any:
        """CombinatorialPolyhedron.is_pyramid(self, certificate=False)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 2340)

        Test whether the polytope is a pyramid over one of its facets.

        INPUT:

        - ``certificate`` -- boolean (default: ``False``); specifies whether
          to return a vertex of the polytope which is the apex of a pyramid,
          if found

        OUTPUT:

        If ``certificate`` is ``True``, returns a tuple containing:

        1. Boolean.
        2. The apex of the pyramid or ``None``.

        If ``certificate`` is ``False`` returns a boolean.

        AUTHORS:

        - Laith Rastanawi
        - Jonathan Kliem

        EXAMPLES::

            sage: C = polytopes.cross_polytope(4).combinatorial_polyhedron()
            sage: C.is_pyramid()
            False
            sage: C.is_pyramid(certificate=True)
            (False, None)
            sage: C = polytopes.cross_polytope(4).pyramid().combinatorial_polyhedron()
            sage: C.is_pyramid()
            True
            sage: C.is_pyramid(certificate=True)
            (True, A vertex at (1, 0, 0, 0, 0))
            sage: C = polytopes.simplex(5).combinatorial_polyhedron()
            sage: C.is_pyramid(certificate=True)
            (True, A vertex at (1, 0, 0, 0, 0, 0))

        For unbounded polyhedra, an error is raised::

            sage: C = CombinatorialPolyhedron([[0,1], [0,2]], far_face=[1,2], unbounded=True)
            sage: C.is_pyramid()
            Traceback (most recent call last):
            ...
            ValueError: polyhedron has to be compact

        TESTS::

            sage: CombinatorialPolyhedron(-1).is_pyramid()
            False
            sage: CombinatorialPolyhedron(-1).is_pyramid(True)
            (False, None)
            sage: CombinatorialPolyhedron(0).is_pyramid()
            True
            sage: CombinatorialPolyhedron(0).is_pyramid(True)
            (True, 0)

        Check that :issue:`30292` is fixed::

            sage: Polyhedron([[0, -1, -1], [0, -1, 1], [0, 1, -1], [0, 1, 1], [1, 0, 0]]).is_pyramid(certificate=True)
            (True, A vertex at (1, 0, 0))"""
    @overload
    def is_pyramid(self, _True) -> Any:
        """CombinatorialPolyhedron.is_pyramid(self, certificate=False)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 2340)

        Test whether the polytope is a pyramid over one of its facets.

        INPUT:

        - ``certificate`` -- boolean (default: ``False``); specifies whether
          to return a vertex of the polytope which is the apex of a pyramid,
          if found

        OUTPUT:

        If ``certificate`` is ``True``, returns a tuple containing:

        1. Boolean.
        2. The apex of the pyramid or ``None``.

        If ``certificate`` is ``False`` returns a boolean.

        AUTHORS:

        - Laith Rastanawi
        - Jonathan Kliem

        EXAMPLES::

            sage: C = polytopes.cross_polytope(4).combinatorial_polyhedron()
            sage: C.is_pyramid()
            False
            sage: C.is_pyramid(certificate=True)
            (False, None)
            sage: C = polytopes.cross_polytope(4).pyramid().combinatorial_polyhedron()
            sage: C.is_pyramid()
            True
            sage: C.is_pyramid(certificate=True)
            (True, A vertex at (1, 0, 0, 0, 0))
            sage: C = polytopes.simplex(5).combinatorial_polyhedron()
            sage: C.is_pyramid(certificate=True)
            (True, A vertex at (1, 0, 0, 0, 0, 0))

        For unbounded polyhedra, an error is raised::

            sage: C = CombinatorialPolyhedron([[0,1], [0,2]], far_face=[1,2], unbounded=True)
            sage: C.is_pyramid()
            Traceback (most recent call last):
            ...
            ValueError: polyhedron has to be compact

        TESTS::

            sage: CombinatorialPolyhedron(-1).is_pyramid()
            False
            sage: CombinatorialPolyhedron(-1).is_pyramid(True)
            (False, None)
            sage: CombinatorialPolyhedron(0).is_pyramid()
            True
            sage: CombinatorialPolyhedron(0).is_pyramid(True)
            (True, 0)

        Check that :issue:`30292` is fixed::

            sage: Polyhedron([[0, -1, -1], [0, -1, 1], [0, 1, -1], [0, 1, 1], [1, 0, 0]]).is_pyramid(certificate=True)
            (True, A vertex at (1, 0, 0))"""
    @overload
    def is_pyramid(self, certificate=...) -> Any:
        """CombinatorialPolyhedron.is_pyramid(self, certificate=False)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 2340)

        Test whether the polytope is a pyramid over one of its facets.

        INPUT:

        - ``certificate`` -- boolean (default: ``False``); specifies whether
          to return a vertex of the polytope which is the apex of a pyramid,
          if found

        OUTPUT:

        If ``certificate`` is ``True``, returns a tuple containing:

        1. Boolean.
        2. The apex of the pyramid or ``None``.

        If ``certificate`` is ``False`` returns a boolean.

        AUTHORS:

        - Laith Rastanawi
        - Jonathan Kliem

        EXAMPLES::

            sage: C = polytopes.cross_polytope(4).combinatorial_polyhedron()
            sage: C.is_pyramid()
            False
            sage: C.is_pyramid(certificate=True)
            (False, None)
            sage: C = polytopes.cross_polytope(4).pyramid().combinatorial_polyhedron()
            sage: C.is_pyramid()
            True
            sage: C.is_pyramid(certificate=True)
            (True, A vertex at (1, 0, 0, 0, 0))
            sage: C = polytopes.simplex(5).combinatorial_polyhedron()
            sage: C.is_pyramid(certificate=True)
            (True, A vertex at (1, 0, 0, 0, 0, 0))

        For unbounded polyhedra, an error is raised::

            sage: C = CombinatorialPolyhedron([[0,1], [0,2]], far_face=[1,2], unbounded=True)
            sage: C.is_pyramid()
            Traceback (most recent call last):
            ...
            ValueError: polyhedron has to be compact

        TESTS::

            sage: CombinatorialPolyhedron(-1).is_pyramid()
            False
            sage: CombinatorialPolyhedron(-1).is_pyramid(True)
            (False, None)
            sage: CombinatorialPolyhedron(0).is_pyramid()
            True
            sage: CombinatorialPolyhedron(0).is_pyramid(True)
            (True, 0)

        Check that :issue:`30292` is fixed::

            sage: Polyhedron([[0, -1, -1], [0, -1, 1], [0, 1, -1], [0, 1, 1], [1, 0, 0]]).is_pyramid(certificate=True)
            (True, A vertex at (1, 0, 0))"""
    @overload
    def is_simple(self) -> Any:
        """CombinatorialPolyhedron.is_simple(self)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 2130)

        Test whether the polytope is simple.

        If the polyhedron is unbounded, return ``False``.

        A polytope is simple, if each vertex is contained in exactly `d` facets,
        where `d` is the dimension of the polytope.

        EXAMPLES::

            sage: P = polytopes.cyclic_polytope(4,10)
            sage: C = P.combinatorial_polyhedron()
            sage: C.is_simple()
            False
            sage: P = polytopes.hypercube(4)
            sage: C = P.combinatorial_polyhedron()
            sage: C.is_simple()
            True

        Return ``False`` for unbounded polyhedra::

            sage: C = CombinatorialPolyhedron([[0,1], [0,2]], far_face=[1,2], unbounded=True)
            sage: C.is_simple()
            False"""
    @overload
    def is_simple(self) -> Any:
        """CombinatorialPolyhedron.is_simple(self)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 2130)

        Test whether the polytope is simple.

        If the polyhedron is unbounded, return ``False``.

        A polytope is simple, if each vertex is contained in exactly `d` facets,
        where `d` is the dimension of the polytope.

        EXAMPLES::

            sage: P = polytopes.cyclic_polytope(4,10)
            sage: C = P.combinatorial_polyhedron()
            sage: C.is_simple()
            False
            sage: P = polytopes.hypercube(4)
            sage: C = P.combinatorial_polyhedron()
            sage: C.is_simple()
            True

        Return ``False`` for unbounded polyhedra::

            sage: C = CombinatorialPolyhedron([[0,1], [0,2]], far_face=[1,2], unbounded=True)
            sage: C.is_simple()
            False"""
    @overload
    def is_simple(self) -> Any:
        """CombinatorialPolyhedron.is_simple(self)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 2130)

        Test whether the polytope is simple.

        If the polyhedron is unbounded, return ``False``.

        A polytope is simple, if each vertex is contained in exactly `d` facets,
        where `d` is the dimension of the polytope.

        EXAMPLES::

            sage: P = polytopes.cyclic_polytope(4,10)
            sage: C = P.combinatorial_polyhedron()
            sage: C.is_simple()
            False
            sage: P = polytopes.hypercube(4)
            sage: C = P.combinatorial_polyhedron()
            sage: C.is_simple()
            True

        Return ``False`` for unbounded polyhedra::

            sage: C = CombinatorialPolyhedron([[0,1], [0,2]], far_face=[1,2], unbounded=True)
            sage: C.is_simple()
            False"""
    @overload
    def is_simple(self) -> Any:
        """CombinatorialPolyhedron.is_simple(self)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 2130)

        Test whether the polytope is simple.

        If the polyhedron is unbounded, return ``False``.

        A polytope is simple, if each vertex is contained in exactly `d` facets,
        where `d` is the dimension of the polytope.

        EXAMPLES::

            sage: P = polytopes.cyclic_polytope(4,10)
            sage: C = P.combinatorial_polyhedron()
            sage: C.is_simple()
            False
            sage: P = polytopes.hypercube(4)
            sage: C = P.combinatorial_polyhedron()
            sage: C.is_simple()
            True

        Return ``False`` for unbounded polyhedra::

            sage: C = CombinatorialPolyhedron([[0,1], [0,2]], far_face=[1,2], unbounded=True)
            sage: C.is_simple()
            False"""
    @overload
    def is_simplex(self) -> bool:
        """CombinatorialPolyhedron.is_simplex(self) -> bool

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 2003)

        Return whether the polyhedron is a simplex.

        A simplex is a bounded polyhedron with `d+1` vertices, where
        `d` is the dimension.

        EXAMPLES::

            sage: CombinatorialPolyhedron(2).is_simplex()
            False
            sage: CombinatorialPolyhedron([[0,1],[0,2],[1,2]]).is_simplex()
            True"""
    @overload
    def is_simplex(self) -> Any:
        """CombinatorialPolyhedron.is_simplex(self) -> bool

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 2003)

        Return whether the polyhedron is a simplex.

        A simplex is a bounded polyhedron with `d+1` vertices, where
        `d` is the dimension.

        EXAMPLES::

            sage: CombinatorialPolyhedron(2).is_simplex()
            False
            sage: CombinatorialPolyhedron([[0,1],[0,2],[1,2]]).is_simplex()
            True"""
    @overload
    def is_simplex(self) -> Any:
        """CombinatorialPolyhedron.is_simplex(self) -> bool

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 2003)

        Return whether the polyhedron is a simplex.

        A simplex is a bounded polyhedron with `d+1` vertices, where
        `d` is the dimension.

        EXAMPLES::

            sage: CombinatorialPolyhedron(2).is_simplex()
            False
            sage: CombinatorialPolyhedron([[0,1],[0,2],[1,2]]).is_simplex()
            True"""
    @overload
    def is_simplicial(self) -> bool:
        """CombinatorialPolyhedron.is_simplicial(self) -> bool

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 2019)

        Test whether the polytope is simplicial.

        This method is not implemented for unbounded polyhedra.

        A polytope is simplicial, if each facet contains exactly `d` vertices,
        where `d` is the dimension of the polytope.

        EXAMPLES::

            sage: P = polytopes.cyclic_polytope(4,10)
            sage: C = P.combinatorial_polyhedron()
            sage: C.is_simplicial()
            True
            sage: P = polytopes.hypercube(4)
            sage: C = P.combinatorial_polyhedron()
            sage: C.is_simplicial()
            False

        For unbounded polyhedra, an error is raised::

            sage: C = CombinatorialPolyhedron([[0,1], [0,2]], far_face=[1,2], unbounded=True)
            sage: C.is_simplicial()
            Traceback (most recent call last):
            ...
            NotImplementedError: this function is implemented for polytopes only"""
    @overload
    def is_simplicial(self) -> Any:
        """CombinatorialPolyhedron.is_simplicial(self) -> bool

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 2019)

        Test whether the polytope is simplicial.

        This method is not implemented for unbounded polyhedra.

        A polytope is simplicial, if each facet contains exactly `d` vertices,
        where `d` is the dimension of the polytope.

        EXAMPLES::

            sage: P = polytopes.cyclic_polytope(4,10)
            sage: C = P.combinatorial_polyhedron()
            sage: C.is_simplicial()
            True
            sage: P = polytopes.hypercube(4)
            sage: C = P.combinatorial_polyhedron()
            sage: C.is_simplicial()
            False

        For unbounded polyhedra, an error is raised::

            sage: C = CombinatorialPolyhedron([[0,1], [0,2]], far_face=[1,2], unbounded=True)
            sage: C.is_simplicial()
            Traceback (most recent call last):
            ...
            NotImplementedError: this function is implemented for polytopes only"""
    @overload
    def is_simplicial(self) -> Any:
        """CombinatorialPolyhedron.is_simplicial(self) -> bool

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 2019)

        Test whether the polytope is simplicial.

        This method is not implemented for unbounded polyhedra.

        A polytope is simplicial, if each facet contains exactly `d` vertices,
        where `d` is the dimension of the polytope.

        EXAMPLES::

            sage: P = polytopes.cyclic_polytope(4,10)
            sage: C = P.combinatorial_polyhedron()
            sage: C.is_simplicial()
            True
            sage: P = polytopes.hypercube(4)
            sage: C = P.combinatorial_polyhedron()
            sage: C.is_simplicial()
            False

        For unbounded polyhedra, an error is raised::

            sage: C = CombinatorialPolyhedron([[0,1], [0,2]], far_face=[1,2], unbounded=True)
            sage: C.is_simplicial()
            Traceback (most recent call last):
            ...
            NotImplementedError: this function is implemented for polytopes only"""
    @overload
    def is_simplicial(self) -> Any:
        """CombinatorialPolyhedron.is_simplicial(self) -> bool

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 2019)

        Test whether the polytope is simplicial.

        This method is not implemented for unbounded polyhedra.

        A polytope is simplicial, if each facet contains exactly `d` vertices,
        where `d` is the dimension of the polytope.

        EXAMPLES::

            sage: P = polytopes.cyclic_polytope(4,10)
            sage: C = P.combinatorial_polyhedron()
            sage: C.is_simplicial()
            True
            sage: P = polytopes.hypercube(4)
            sage: C = P.combinatorial_polyhedron()
            sage: C.is_simplicial()
            False

        For unbounded polyhedra, an error is raised::

            sage: C = CombinatorialPolyhedron([[0,1], [0,2]], far_face=[1,2], unbounded=True)
            sage: C.is_simplicial()
            Traceback (most recent call last):
            ...
            NotImplementedError: this function is implemented for polytopes only"""
    @overload
    def join_of_Vrep(self, *indices) -> Any:
        """CombinatorialPolyhedron.join_of_Vrep(self, *indices)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 2610)

        Return the smallest face containing all Vrepresentatives indicated by the indices.

        .. SEEALSO::

            :meth:`~sage.geometry.polyhedron.combinatorial_polyhedron.face_iterator_base.join_of_Vrep`.

        EXAMPLES::

            sage: # needs sage.combinat
            sage: P = polytopes.permutahedron(4)
            sage: C = CombinatorialPolyhedron(P)
            sage: C.join_of_Vrep(0,1)
            A 1-dimensional face of a 3-dimensional combinatorial polyhedron
            sage: C.join_of_Vrep(0,11).ambient_V_indices()
            (0, 1, 10, 11, 12, 13)
            sage: C.join_of_Vrep(8).ambient_V_indices()
            (8,)
            sage: C.join_of_Vrep().ambient_V_indices()
            ()"""
    @overload
    def join_of_Vrep(self) -> Any:
        """CombinatorialPolyhedron.join_of_Vrep(self, *indices)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 2610)

        Return the smallest face containing all Vrepresentatives indicated by the indices.

        .. SEEALSO::

            :meth:`~sage.geometry.polyhedron.combinatorial_polyhedron.face_iterator_base.join_of_Vrep`.

        EXAMPLES::

            sage: # needs sage.combinat
            sage: P = polytopes.permutahedron(4)
            sage: C = CombinatorialPolyhedron(P)
            sage: C.join_of_Vrep(0,1)
            A 1-dimensional face of a 3-dimensional combinatorial polyhedron
            sage: C.join_of_Vrep(0,11).ambient_V_indices()
            (0, 1, 10, 11, 12, 13)
            sage: C.join_of_Vrep(8).ambient_V_indices()
            (8,)
            sage: C.join_of_Vrep().ambient_V_indices()
            ()"""
    @overload
    def meet_of_Hrep(self, *indices) -> Any:
        """CombinatorialPolyhedron.meet_of_Hrep(self, *indices)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 2634)

        Return the largest face contained in all facets indicated by the indices.

        .. SEEALSO::

            :meth:`~sage.geometry.polyhedron.combinatorial_polyhedron.face_iterator_base.meet_of_Hrep`.

        EXAMPLES::

            sage: # needs sage.rings.number_field
            sage: P = polytopes.dodecahedron()
            sage: C = CombinatorialPolyhedron(P)
            sage: C.meet_of_Hrep(0)
            A 2-dimensional face of a 3-dimensional combinatorial polyhedron
            sage: C.meet_of_Hrep(0).ambient_H_indices()
            (0,)
            sage: C.meet_of_Hrep(0,1).ambient_H_indices()
            (0, 1)
            sage: C.meet_of_Hrep(0,2).ambient_H_indices()
            (0, 2)
            sage: C.meet_of_Hrep(0,2,3).ambient_H_indices()
            (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11)
            sage: C.meet_of_Hrep().ambient_H_indices()
            ()"""
    @overload
    def meet_of_Hrep(self) -> Any:
        """CombinatorialPolyhedron.meet_of_Hrep(self, *indices)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 2634)

        Return the largest face contained in all facets indicated by the indices.

        .. SEEALSO::

            :meth:`~sage.geometry.polyhedron.combinatorial_polyhedron.face_iterator_base.meet_of_Hrep`.

        EXAMPLES::

            sage: # needs sage.rings.number_field
            sage: P = polytopes.dodecahedron()
            sage: C = CombinatorialPolyhedron(P)
            sage: C.meet_of_Hrep(0)
            A 2-dimensional face of a 3-dimensional combinatorial polyhedron
            sage: C.meet_of_Hrep(0).ambient_H_indices()
            (0,)
            sage: C.meet_of_Hrep(0,1).ambient_H_indices()
            (0, 1)
            sage: C.meet_of_Hrep(0,2).ambient_H_indices()
            (0, 2)
            sage: C.meet_of_Hrep(0,2,3).ambient_H_indices()
            (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11)
            sage: C.meet_of_Hrep().ambient_H_indices()
            ()"""
    @overload
    def n_facets(self) -> Any:
        """CombinatorialPolyhedron.n_facets(self)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 942)

        Return the number of facets.

        Is equivalent to ``len(self.facets())``.

        EXAMPLES::

            sage: P = polytopes.cube()
            sage: C = CombinatorialPolyhedron(P)
            sage: C.n_facets()
            6

            sage: P = polytopes.cyclic_polytope(4,20)
            sage: C = CombinatorialPolyhedron(P)
            sage: C.n_facets()
            170

            sage: P = Polyhedron(lines=[[0,1]], vertices=[[1,0], [-1,0]])
            sage: C = CombinatorialPolyhedron(P)
            sage: C.n_facets()
            2

            sage: P = Polyhedron(rays=[[1,0], [-1,0], [0,1]])
            sage: C = CombinatorialPolyhedron(P)
            sage: C.n_facets()
            1

            sage: C = CombinatorialPolyhedron(-1)
            sage: C.f_vector()
            (1)
            sage: C.n_facets()
            0

        Facets are defined to be the maximal nontrivial faces.
        The ``0``-dimensional polyhedron does not have nontrivial faces::

            sage: C = CombinatorialPolyhedron(0)
            sage: C.f_vector()
            (1, 1)
            sage: C.n_facets()
            0"""
    @overload
    def n_facets(self) -> Any:
        """CombinatorialPolyhedron.n_facets(self)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 942)

        Return the number of facets.

        Is equivalent to ``len(self.facets())``.

        EXAMPLES::

            sage: P = polytopes.cube()
            sage: C = CombinatorialPolyhedron(P)
            sage: C.n_facets()
            6

            sage: P = polytopes.cyclic_polytope(4,20)
            sage: C = CombinatorialPolyhedron(P)
            sage: C.n_facets()
            170

            sage: P = Polyhedron(lines=[[0,1]], vertices=[[1,0], [-1,0]])
            sage: C = CombinatorialPolyhedron(P)
            sage: C.n_facets()
            2

            sage: P = Polyhedron(rays=[[1,0], [-1,0], [0,1]])
            sage: C = CombinatorialPolyhedron(P)
            sage: C.n_facets()
            1

            sage: C = CombinatorialPolyhedron(-1)
            sage: C.f_vector()
            (1)
            sage: C.n_facets()
            0

        Facets are defined to be the maximal nontrivial faces.
        The ``0``-dimensional polyhedron does not have nontrivial faces::

            sage: C = CombinatorialPolyhedron(0)
            sage: C.f_vector()
            (1, 1)
            sage: C.n_facets()
            0"""
    @overload
    def n_facets(self) -> Any:
        """CombinatorialPolyhedron.n_facets(self)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 942)

        Return the number of facets.

        Is equivalent to ``len(self.facets())``.

        EXAMPLES::

            sage: P = polytopes.cube()
            sage: C = CombinatorialPolyhedron(P)
            sage: C.n_facets()
            6

            sage: P = polytopes.cyclic_polytope(4,20)
            sage: C = CombinatorialPolyhedron(P)
            sage: C.n_facets()
            170

            sage: P = Polyhedron(lines=[[0,1]], vertices=[[1,0], [-1,0]])
            sage: C = CombinatorialPolyhedron(P)
            sage: C.n_facets()
            2

            sage: P = Polyhedron(rays=[[1,0], [-1,0], [0,1]])
            sage: C = CombinatorialPolyhedron(P)
            sage: C.n_facets()
            1

            sage: C = CombinatorialPolyhedron(-1)
            sage: C.f_vector()
            (1)
            sage: C.n_facets()
            0

        Facets are defined to be the maximal nontrivial faces.
        The ``0``-dimensional polyhedron does not have nontrivial faces::

            sage: C = CombinatorialPolyhedron(0)
            sage: C.f_vector()
            (1, 1)
            sage: C.n_facets()
            0"""
    @overload
    def n_facets(self) -> Any:
        """CombinatorialPolyhedron.n_facets(self)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 942)

        Return the number of facets.

        Is equivalent to ``len(self.facets())``.

        EXAMPLES::

            sage: P = polytopes.cube()
            sage: C = CombinatorialPolyhedron(P)
            sage: C.n_facets()
            6

            sage: P = polytopes.cyclic_polytope(4,20)
            sage: C = CombinatorialPolyhedron(P)
            sage: C.n_facets()
            170

            sage: P = Polyhedron(lines=[[0,1]], vertices=[[1,0], [-1,0]])
            sage: C = CombinatorialPolyhedron(P)
            sage: C.n_facets()
            2

            sage: P = Polyhedron(rays=[[1,0], [-1,0], [0,1]])
            sage: C = CombinatorialPolyhedron(P)
            sage: C.n_facets()
            1

            sage: C = CombinatorialPolyhedron(-1)
            sage: C.f_vector()
            (1)
            sage: C.n_facets()
            0

        Facets are defined to be the maximal nontrivial faces.
        The ``0``-dimensional polyhedron does not have nontrivial faces::

            sage: C = CombinatorialPolyhedron(0)
            sage: C.f_vector()
            (1, 1)
            sage: C.n_facets()
            0"""
    @overload
    def n_facets(self) -> Any:
        """CombinatorialPolyhedron.n_facets(self)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 942)

        Return the number of facets.

        Is equivalent to ``len(self.facets())``.

        EXAMPLES::

            sage: P = polytopes.cube()
            sage: C = CombinatorialPolyhedron(P)
            sage: C.n_facets()
            6

            sage: P = polytopes.cyclic_polytope(4,20)
            sage: C = CombinatorialPolyhedron(P)
            sage: C.n_facets()
            170

            sage: P = Polyhedron(lines=[[0,1]], vertices=[[1,0], [-1,0]])
            sage: C = CombinatorialPolyhedron(P)
            sage: C.n_facets()
            2

            sage: P = Polyhedron(rays=[[1,0], [-1,0], [0,1]])
            sage: C = CombinatorialPolyhedron(P)
            sage: C.n_facets()
            1

            sage: C = CombinatorialPolyhedron(-1)
            sage: C.f_vector()
            (1)
            sage: C.n_facets()
            0

        Facets are defined to be the maximal nontrivial faces.
        The ``0``-dimensional polyhedron does not have nontrivial faces::

            sage: C = CombinatorialPolyhedron(0)
            sage: C.f_vector()
            (1, 1)
            sage: C.n_facets()
            0"""
    @overload
    def n_facets(self) -> Any:
        """CombinatorialPolyhedron.n_facets(self)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 942)

        Return the number of facets.

        Is equivalent to ``len(self.facets())``.

        EXAMPLES::

            sage: P = polytopes.cube()
            sage: C = CombinatorialPolyhedron(P)
            sage: C.n_facets()
            6

            sage: P = polytopes.cyclic_polytope(4,20)
            sage: C = CombinatorialPolyhedron(P)
            sage: C.n_facets()
            170

            sage: P = Polyhedron(lines=[[0,1]], vertices=[[1,0], [-1,0]])
            sage: C = CombinatorialPolyhedron(P)
            sage: C.n_facets()
            2

            sage: P = Polyhedron(rays=[[1,0], [-1,0], [0,1]])
            sage: C = CombinatorialPolyhedron(P)
            sage: C.n_facets()
            1

            sage: C = CombinatorialPolyhedron(-1)
            sage: C.f_vector()
            (1)
            sage: C.n_facets()
            0

        Facets are defined to be the maximal nontrivial faces.
        The ``0``-dimensional polyhedron does not have nontrivial faces::

            sage: C = CombinatorialPolyhedron(0)
            sage: C.f_vector()
            (1, 1)
            sage: C.n_facets()
            0"""
    @overload
    def n_facets(self) -> Any:
        """CombinatorialPolyhedron.n_facets(self)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 942)

        Return the number of facets.

        Is equivalent to ``len(self.facets())``.

        EXAMPLES::

            sage: P = polytopes.cube()
            sage: C = CombinatorialPolyhedron(P)
            sage: C.n_facets()
            6

            sage: P = polytopes.cyclic_polytope(4,20)
            sage: C = CombinatorialPolyhedron(P)
            sage: C.n_facets()
            170

            sage: P = Polyhedron(lines=[[0,1]], vertices=[[1,0], [-1,0]])
            sage: C = CombinatorialPolyhedron(P)
            sage: C.n_facets()
            2

            sage: P = Polyhedron(rays=[[1,0], [-1,0], [0,1]])
            sage: C = CombinatorialPolyhedron(P)
            sage: C.n_facets()
            1

            sage: C = CombinatorialPolyhedron(-1)
            sage: C.f_vector()
            (1)
            sage: C.n_facets()
            0

        Facets are defined to be the maximal nontrivial faces.
        The ``0``-dimensional polyhedron does not have nontrivial faces::

            sage: C = CombinatorialPolyhedron(0)
            sage: C.f_vector()
            (1, 1)
            sage: C.n_facets()
            0"""
    @overload
    def n_vertices(self) -> Any:
        """CombinatorialPolyhedron.n_vertices(self)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 823)

        Return the number of vertices.

        Is equivalent to ``len(self.vertices())``.

        EXAMPLES::

            sage: P = polytopes.cube()
            sage: C = CombinatorialPolyhedron(P)
            sage: C.n_vertices()
            8

            sage: P = polytopes.cyclic_polytope(4,20)
            sage: C = CombinatorialPolyhedron(P)
            sage: C.n_vertices()
            20

            sage: P = Polyhedron(lines=[[0,1]], vertices=[[1,0], [-1,0]])
            sage: C = CombinatorialPolyhedron(P)
            sage: C.n_vertices()
            0

            sage: P = Polyhedron(rays=[[1,0,0], [0,1,0]], lines=[[0,0,1]])
            sage: C = CombinatorialPolyhedron(P)
            sage: C.n_vertices()
            0

            sage: C = CombinatorialPolyhedron(4)
            sage: C.f_vector()
            (1, 0, 0, 0, 0, 1)
            sage: C.n_vertices()
            0

            sage: C = CombinatorialPolyhedron(0)
            sage: C.f_vector()
            (1, 1)
            sage: C.n_vertices()
            1"""
    @overload
    def n_vertices(self) -> Any:
        """CombinatorialPolyhedron.n_vertices(self)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 823)

        Return the number of vertices.

        Is equivalent to ``len(self.vertices())``.

        EXAMPLES::

            sage: P = polytopes.cube()
            sage: C = CombinatorialPolyhedron(P)
            sage: C.n_vertices()
            8

            sage: P = polytopes.cyclic_polytope(4,20)
            sage: C = CombinatorialPolyhedron(P)
            sage: C.n_vertices()
            20

            sage: P = Polyhedron(lines=[[0,1]], vertices=[[1,0], [-1,0]])
            sage: C = CombinatorialPolyhedron(P)
            sage: C.n_vertices()
            0

            sage: P = Polyhedron(rays=[[1,0,0], [0,1,0]], lines=[[0,0,1]])
            sage: C = CombinatorialPolyhedron(P)
            sage: C.n_vertices()
            0

            sage: C = CombinatorialPolyhedron(4)
            sage: C.f_vector()
            (1, 0, 0, 0, 0, 1)
            sage: C.n_vertices()
            0

            sage: C = CombinatorialPolyhedron(0)
            sage: C.f_vector()
            (1, 1)
            sage: C.n_vertices()
            1"""
    @overload
    def n_vertices(self) -> Any:
        """CombinatorialPolyhedron.n_vertices(self)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 823)

        Return the number of vertices.

        Is equivalent to ``len(self.vertices())``.

        EXAMPLES::

            sage: P = polytopes.cube()
            sage: C = CombinatorialPolyhedron(P)
            sage: C.n_vertices()
            8

            sage: P = polytopes.cyclic_polytope(4,20)
            sage: C = CombinatorialPolyhedron(P)
            sage: C.n_vertices()
            20

            sage: P = Polyhedron(lines=[[0,1]], vertices=[[1,0], [-1,0]])
            sage: C = CombinatorialPolyhedron(P)
            sage: C.n_vertices()
            0

            sage: P = Polyhedron(rays=[[1,0,0], [0,1,0]], lines=[[0,0,1]])
            sage: C = CombinatorialPolyhedron(P)
            sage: C.n_vertices()
            0

            sage: C = CombinatorialPolyhedron(4)
            sage: C.f_vector()
            (1, 0, 0, 0, 0, 1)
            sage: C.n_vertices()
            0

            sage: C = CombinatorialPolyhedron(0)
            sage: C.f_vector()
            (1, 1)
            sage: C.n_vertices()
            1"""
    @overload
    def n_vertices(self) -> Any:
        """CombinatorialPolyhedron.n_vertices(self)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 823)

        Return the number of vertices.

        Is equivalent to ``len(self.vertices())``.

        EXAMPLES::

            sage: P = polytopes.cube()
            sage: C = CombinatorialPolyhedron(P)
            sage: C.n_vertices()
            8

            sage: P = polytopes.cyclic_polytope(4,20)
            sage: C = CombinatorialPolyhedron(P)
            sage: C.n_vertices()
            20

            sage: P = Polyhedron(lines=[[0,1]], vertices=[[1,0], [-1,0]])
            sage: C = CombinatorialPolyhedron(P)
            sage: C.n_vertices()
            0

            sage: P = Polyhedron(rays=[[1,0,0], [0,1,0]], lines=[[0,0,1]])
            sage: C = CombinatorialPolyhedron(P)
            sage: C.n_vertices()
            0

            sage: C = CombinatorialPolyhedron(4)
            sage: C.f_vector()
            (1, 0, 0, 0, 0, 1)
            sage: C.n_vertices()
            0

            sage: C = CombinatorialPolyhedron(0)
            sage: C.f_vector()
            (1, 1)
            sage: C.n_vertices()
            1"""
    @overload
    def n_vertices(self) -> Any:
        """CombinatorialPolyhedron.n_vertices(self)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 823)

        Return the number of vertices.

        Is equivalent to ``len(self.vertices())``.

        EXAMPLES::

            sage: P = polytopes.cube()
            sage: C = CombinatorialPolyhedron(P)
            sage: C.n_vertices()
            8

            sage: P = polytopes.cyclic_polytope(4,20)
            sage: C = CombinatorialPolyhedron(P)
            sage: C.n_vertices()
            20

            sage: P = Polyhedron(lines=[[0,1]], vertices=[[1,0], [-1,0]])
            sage: C = CombinatorialPolyhedron(P)
            sage: C.n_vertices()
            0

            sage: P = Polyhedron(rays=[[1,0,0], [0,1,0]], lines=[[0,0,1]])
            sage: C = CombinatorialPolyhedron(P)
            sage: C.n_vertices()
            0

            sage: C = CombinatorialPolyhedron(4)
            sage: C.f_vector()
            (1, 0, 0, 0, 0, 1)
            sage: C.n_vertices()
            0

            sage: C = CombinatorialPolyhedron(0)
            sage: C.f_vector()
            (1, 1)
            sage: C.n_vertices()
            1"""
    @overload
    def n_vertices(self) -> Any:
        """CombinatorialPolyhedron.n_vertices(self)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 823)

        Return the number of vertices.

        Is equivalent to ``len(self.vertices())``.

        EXAMPLES::

            sage: P = polytopes.cube()
            sage: C = CombinatorialPolyhedron(P)
            sage: C.n_vertices()
            8

            sage: P = polytopes.cyclic_polytope(4,20)
            sage: C = CombinatorialPolyhedron(P)
            sage: C.n_vertices()
            20

            sage: P = Polyhedron(lines=[[0,1]], vertices=[[1,0], [-1,0]])
            sage: C = CombinatorialPolyhedron(P)
            sage: C.n_vertices()
            0

            sage: P = Polyhedron(rays=[[1,0,0], [0,1,0]], lines=[[0,0,1]])
            sage: C = CombinatorialPolyhedron(P)
            sage: C.n_vertices()
            0

            sage: C = CombinatorialPolyhedron(4)
            sage: C.f_vector()
            (1, 0, 0, 0, 0, 1)
            sage: C.n_vertices()
            0

            sage: C = CombinatorialPolyhedron(0)
            sage: C.f_vector()
            (1, 1)
            sage: C.n_vertices()
            1"""
    @overload
    def n_vertices(self) -> Any:
        """CombinatorialPolyhedron.n_vertices(self)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 823)

        Return the number of vertices.

        Is equivalent to ``len(self.vertices())``.

        EXAMPLES::

            sage: P = polytopes.cube()
            sage: C = CombinatorialPolyhedron(P)
            sage: C.n_vertices()
            8

            sage: P = polytopes.cyclic_polytope(4,20)
            sage: C = CombinatorialPolyhedron(P)
            sage: C.n_vertices()
            20

            sage: P = Polyhedron(lines=[[0,1]], vertices=[[1,0], [-1,0]])
            sage: C = CombinatorialPolyhedron(P)
            sage: C.n_vertices()
            0

            sage: P = Polyhedron(rays=[[1,0,0], [0,1,0]], lines=[[0,0,1]])
            sage: C = CombinatorialPolyhedron(P)
            sage: C.n_vertices()
            0

            sage: C = CombinatorialPolyhedron(4)
            sage: C.f_vector()
            (1, 0, 0, 0, 0, 1)
            sage: C.n_vertices()
            0

            sage: C = CombinatorialPolyhedron(0)
            sage: C.f_vector()
            (1, 1)
            sage: C.n_vertices()
            1"""
    @overload
    def neighborliness(self) -> Any:
        """CombinatorialPolyhedron.neighborliness(self)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 1915)

        Return the largest ``k``, such that the polyhedron is ``k``-neighborly.

        A polyhedron is `k`-neighborly if every set of `n` vertices forms a face
        for `n` up to `k`.

        In case of the `d`-dimensional simplex, it returns `d + 1`.

        .. SEEALSO::

            :meth:`is_neighborly`

        EXAMPLES::

            sage: P = polytopes.cyclic_polytope(8,12)
            sage: C = P.combinatorial_polyhedron()
            sage: C.neighborliness()
            4
            sage: P = polytopes.simplex(6)
            sage: C = P.combinatorial_polyhedron()
            sage: C.neighborliness()
            7
            sage: P = polytopes.cyclic_polytope(4,10)
            sage: P = P.join(P)
            sage: C = P.combinatorial_polyhedron()
            sage: C.neighborliness()
            2"""
    @overload
    def neighborliness(self) -> Any:
        """CombinatorialPolyhedron.neighborliness(self)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 1915)

        Return the largest ``k``, such that the polyhedron is ``k``-neighborly.

        A polyhedron is `k`-neighborly if every set of `n` vertices forms a face
        for `n` up to `k`.

        In case of the `d`-dimensional simplex, it returns `d + 1`.

        .. SEEALSO::

            :meth:`is_neighborly`

        EXAMPLES::

            sage: P = polytopes.cyclic_polytope(8,12)
            sage: C = P.combinatorial_polyhedron()
            sage: C.neighborliness()
            4
            sage: P = polytopes.simplex(6)
            sage: C = P.combinatorial_polyhedron()
            sage: C.neighborliness()
            7
            sage: P = polytopes.cyclic_polytope(4,10)
            sage: P = P.join(P)
            sage: C = P.combinatorial_polyhedron()
            sage: C.neighborliness()
            2"""
    @overload
    def neighborliness(self) -> Any:
        """CombinatorialPolyhedron.neighborliness(self)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 1915)

        Return the largest ``k``, such that the polyhedron is ``k``-neighborly.

        A polyhedron is `k`-neighborly if every set of `n` vertices forms a face
        for `n` up to `k`.

        In case of the `d`-dimensional simplex, it returns `d + 1`.

        .. SEEALSO::

            :meth:`is_neighborly`

        EXAMPLES::

            sage: P = polytopes.cyclic_polytope(8,12)
            sage: C = P.combinatorial_polyhedron()
            sage: C.neighborliness()
            4
            sage: P = polytopes.simplex(6)
            sage: C = P.combinatorial_polyhedron()
            sage: C.neighborliness()
            7
            sage: P = polytopes.cyclic_polytope(4,10)
            sage: P = P.join(P)
            sage: C = P.combinatorial_polyhedron()
            sage: C.neighborliness()
            2"""
    @overload
    def neighborliness(self) -> Any:
        """CombinatorialPolyhedron.neighborliness(self)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 1915)

        Return the largest ``k``, such that the polyhedron is ``k``-neighborly.

        A polyhedron is `k`-neighborly if every set of `n` vertices forms a face
        for `n` up to `k`.

        In case of the `d`-dimensional simplex, it returns `d + 1`.

        .. SEEALSO::

            :meth:`is_neighborly`

        EXAMPLES::

            sage: P = polytopes.cyclic_polytope(8,12)
            sage: C = P.combinatorial_polyhedron()
            sage: C.neighborliness()
            4
            sage: P = polytopes.simplex(6)
            sage: C = P.combinatorial_polyhedron()
            sage: C.neighborliness()
            7
            sage: P = polytopes.cyclic_polytope(4,10)
            sage: P = P.join(P)
            sage: C = P.combinatorial_polyhedron()
            sage: C.neighborliness()
            2"""
    @overload
    def polar(self) -> Any:
        """CombinatorialPolyhedron.dual(self) -> CombinatorialPolyhedron

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 3311)

        Return the dual/polar of ``self``.

        Only defined for bounded polyhedra.

        .. SEEALSO::

            :meth:`~sage.geometry.polyhedron.base.Polyhedron_base.polar`.

        EXAMPLES::

            sage: P = polytopes.cube()
            sage: C = P.combinatorial_polyhedron()
            sage: D = C.dual()
            sage: D.f_vector()
            (1, 6, 12, 8, 1)
            sage: D1 = P.polar().combinatorial_polyhedron()
            sage: D1.face_lattice().is_isomorphic(D.face_lattice())                     # needs sage.combinat
            True

        Polar is an alias to be consistent with :class:`~sage.geometry.polyhedron.base.Polyhedron_base`::

            sage: C.polar().f_vector()
            (1, 6, 12, 8, 1)

        For unbounded polyhedra, an error is raised::

            sage: C = CombinatorialPolyhedron([[0,1], [0,2]], far_face=[1,2], unbounded=True)
            sage: C.dual()
            Traceback (most recent call last):
            ...
            ValueError: self must be bounded"""
    @overload
    def polar(self) -> Any:
        """CombinatorialPolyhedron.dual(self) -> CombinatorialPolyhedron

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 3311)

        Return the dual/polar of ``self``.

        Only defined for bounded polyhedra.

        .. SEEALSO::

            :meth:`~sage.geometry.polyhedron.base.Polyhedron_base.polar`.

        EXAMPLES::

            sage: P = polytopes.cube()
            sage: C = P.combinatorial_polyhedron()
            sage: D = C.dual()
            sage: D.f_vector()
            (1, 6, 12, 8, 1)
            sage: D1 = P.polar().combinatorial_polyhedron()
            sage: D1.face_lattice().is_isomorphic(D.face_lattice())                     # needs sage.combinat
            True

        Polar is an alias to be consistent with :class:`~sage.geometry.polyhedron.base.Polyhedron_base`::

            sage: C.polar().f_vector()
            (1, 6, 12, 8, 1)

        For unbounded polyhedra, an error is raised::

            sage: C = CombinatorialPolyhedron([[0,1], [0,2]], far_face=[1,2], unbounded=True)
            sage: C.dual()
            Traceback (most recent call last):
            ...
            ValueError: self must be bounded"""
    @overload
    def pyramid(self, new_vertex=..., new_facet=...) -> CombinatorialPolyhedron:
        """CombinatorialPolyhedron.pyramid(self, new_vertex=None, new_facet=None) -> CombinatorialPolyhedron

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 3354)

        Return the pyramid of ``self``.

        INPUT:

        - ``new_vertex`` -- (optional); specify a new vertex name to set up
          the pyramid with vertex names
        - ``new_facet`` -- (optional); specify a new facet name to set up
          the pyramid with facet names

        EXAMPLES::

            sage: C = CombinatorialPolyhedron(((1,2,3),(1,2,4),(1,3,4),(2,3,4)))
            sage: C1 = C.pyramid()
            sage: C1.facets()
            ((0, 1, 2, 4), (0, 1, 3, 4), (0, 2, 3, 4), (1, 2, 3, 4), (0, 1, 2, 3))

        ::

            sage: P = polytopes.cube()
            sage: C = CombinatorialPolyhedron(P)
            sage: C1 = C.pyramid()
            sage: P1 = P.pyramid()
            sage: C2 = P1.combinatorial_polyhedron()
            sage: C2.vertex_facet_graph().is_isomorphic(C1.vertex_facet_graph())        # needs sage.combinat
            True

        One can specify a name for the new vertex::

            sage: P = polytopes.cyclic_polytope(4,10)
            sage: C = P.combinatorial_polyhedron()
            sage: C1 = C.pyramid(new_vertex='apex')
            sage: C1.is_pyramid(certificate=True)
            (True, 'apex')
            sage: C1.facets()[0]
            (A vertex at (0, 0, 0, 0),
             A vertex at (1, 1, 1, 1),
             A vertex at (2, 4, 8, 16),
             A vertex at (3, 9, 27, 81),
             'apex')

        One can specify a name for the new facets::

            sage: # needs sage.rings.number_field
            sage: P = polytopes.regular_polygon(4)
            sage: C = P.combinatorial_polyhedron()
            sage: C1 = C.pyramid(new_facet='base')
            sage: C1.Hrepresentation()
            (An inequality (-1/2, 1/2) x + 1/2 >= 0,
             An inequality (-1/2, -1/2) x + 1/2 >= 0,
             An inequality (1/2, 0.50000000000000000?) x + 1/2 >= 0,
             An inequality (1/2, -1/2) x + 1/2 >= 0,
             'base')

        For unbounded polyhedra, an error is raised::

            sage: C = CombinatorialPolyhedron([[0,1], [0,2]], far_face=[1,2], unbounded=True)
            sage: C.pyramid()
            Traceback (most recent call last):
            ...
            ValueError: self must be bounded"""
    @overload
    def pyramid(self) -> Any:
        """CombinatorialPolyhedron.pyramid(self, new_vertex=None, new_facet=None) -> CombinatorialPolyhedron

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 3354)

        Return the pyramid of ``self``.

        INPUT:

        - ``new_vertex`` -- (optional); specify a new vertex name to set up
          the pyramid with vertex names
        - ``new_facet`` -- (optional); specify a new facet name to set up
          the pyramid with facet names

        EXAMPLES::

            sage: C = CombinatorialPolyhedron(((1,2,3),(1,2,4),(1,3,4),(2,3,4)))
            sage: C1 = C.pyramid()
            sage: C1.facets()
            ((0, 1, 2, 4), (0, 1, 3, 4), (0, 2, 3, 4), (1, 2, 3, 4), (0, 1, 2, 3))

        ::

            sage: P = polytopes.cube()
            sage: C = CombinatorialPolyhedron(P)
            sage: C1 = C.pyramid()
            sage: P1 = P.pyramid()
            sage: C2 = P1.combinatorial_polyhedron()
            sage: C2.vertex_facet_graph().is_isomorphic(C1.vertex_facet_graph())        # needs sage.combinat
            True

        One can specify a name for the new vertex::

            sage: P = polytopes.cyclic_polytope(4,10)
            sage: C = P.combinatorial_polyhedron()
            sage: C1 = C.pyramid(new_vertex='apex')
            sage: C1.is_pyramid(certificate=True)
            (True, 'apex')
            sage: C1.facets()[0]
            (A vertex at (0, 0, 0, 0),
             A vertex at (1, 1, 1, 1),
             A vertex at (2, 4, 8, 16),
             A vertex at (3, 9, 27, 81),
             'apex')

        One can specify a name for the new facets::

            sage: # needs sage.rings.number_field
            sage: P = polytopes.regular_polygon(4)
            sage: C = P.combinatorial_polyhedron()
            sage: C1 = C.pyramid(new_facet='base')
            sage: C1.Hrepresentation()
            (An inequality (-1/2, 1/2) x + 1/2 >= 0,
             An inequality (-1/2, -1/2) x + 1/2 >= 0,
             An inequality (1/2, 0.50000000000000000?) x + 1/2 >= 0,
             An inequality (1/2, -1/2) x + 1/2 >= 0,
             'base')

        For unbounded polyhedra, an error is raised::

            sage: C = CombinatorialPolyhedron([[0,1], [0,2]], far_face=[1,2], unbounded=True)
            sage: C.pyramid()
            Traceback (most recent call last):
            ...
            ValueError: self must be bounded"""
    @overload
    def pyramid(self) -> Any:
        """CombinatorialPolyhedron.pyramid(self, new_vertex=None, new_facet=None) -> CombinatorialPolyhedron

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 3354)

        Return the pyramid of ``self``.

        INPUT:

        - ``new_vertex`` -- (optional); specify a new vertex name to set up
          the pyramid with vertex names
        - ``new_facet`` -- (optional); specify a new facet name to set up
          the pyramid with facet names

        EXAMPLES::

            sage: C = CombinatorialPolyhedron(((1,2,3),(1,2,4),(1,3,4),(2,3,4)))
            sage: C1 = C.pyramid()
            sage: C1.facets()
            ((0, 1, 2, 4), (0, 1, 3, 4), (0, 2, 3, 4), (1, 2, 3, 4), (0, 1, 2, 3))

        ::

            sage: P = polytopes.cube()
            sage: C = CombinatorialPolyhedron(P)
            sage: C1 = C.pyramid()
            sage: P1 = P.pyramid()
            sage: C2 = P1.combinatorial_polyhedron()
            sage: C2.vertex_facet_graph().is_isomorphic(C1.vertex_facet_graph())        # needs sage.combinat
            True

        One can specify a name for the new vertex::

            sage: P = polytopes.cyclic_polytope(4,10)
            sage: C = P.combinatorial_polyhedron()
            sage: C1 = C.pyramid(new_vertex='apex')
            sage: C1.is_pyramid(certificate=True)
            (True, 'apex')
            sage: C1.facets()[0]
            (A vertex at (0, 0, 0, 0),
             A vertex at (1, 1, 1, 1),
             A vertex at (2, 4, 8, 16),
             A vertex at (3, 9, 27, 81),
             'apex')

        One can specify a name for the new facets::

            sage: # needs sage.rings.number_field
            sage: P = polytopes.regular_polygon(4)
            sage: C = P.combinatorial_polyhedron()
            sage: C1 = C.pyramid(new_facet='base')
            sage: C1.Hrepresentation()
            (An inequality (-1/2, 1/2) x + 1/2 >= 0,
             An inequality (-1/2, -1/2) x + 1/2 >= 0,
             An inequality (1/2, 0.50000000000000000?) x + 1/2 >= 0,
             An inequality (1/2, -1/2) x + 1/2 >= 0,
             'base')

        For unbounded polyhedra, an error is raised::

            sage: C = CombinatorialPolyhedron([[0,1], [0,2]], far_face=[1,2], unbounded=True)
            sage: C.pyramid()
            Traceback (most recent call last):
            ...
            ValueError: self must be bounded"""
    @overload
    def pyramid(self) -> Any:
        """CombinatorialPolyhedron.pyramid(self, new_vertex=None, new_facet=None) -> CombinatorialPolyhedron

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 3354)

        Return the pyramid of ``self``.

        INPUT:

        - ``new_vertex`` -- (optional); specify a new vertex name to set up
          the pyramid with vertex names
        - ``new_facet`` -- (optional); specify a new facet name to set up
          the pyramid with facet names

        EXAMPLES::

            sage: C = CombinatorialPolyhedron(((1,2,3),(1,2,4),(1,3,4),(2,3,4)))
            sage: C1 = C.pyramid()
            sage: C1.facets()
            ((0, 1, 2, 4), (0, 1, 3, 4), (0, 2, 3, 4), (1, 2, 3, 4), (0, 1, 2, 3))

        ::

            sage: P = polytopes.cube()
            sage: C = CombinatorialPolyhedron(P)
            sage: C1 = C.pyramid()
            sage: P1 = P.pyramid()
            sage: C2 = P1.combinatorial_polyhedron()
            sage: C2.vertex_facet_graph().is_isomorphic(C1.vertex_facet_graph())        # needs sage.combinat
            True

        One can specify a name for the new vertex::

            sage: P = polytopes.cyclic_polytope(4,10)
            sage: C = P.combinatorial_polyhedron()
            sage: C1 = C.pyramid(new_vertex='apex')
            sage: C1.is_pyramid(certificate=True)
            (True, 'apex')
            sage: C1.facets()[0]
            (A vertex at (0, 0, 0, 0),
             A vertex at (1, 1, 1, 1),
             A vertex at (2, 4, 8, 16),
             A vertex at (3, 9, 27, 81),
             'apex')

        One can specify a name for the new facets::

            sage: # needs sage.rings.number_field
            sage: P = polytopes.regular_polygon(4)
            sage: C = P.combinatorial_polyhedron()
            sage: C1 = C.pyramid(new_facet='base')
            sage: C1.Hrepresentation()
            (An inequality (-1/2, 1/2) x + 1/2 >= 0,
             An inequality (-1/2, -1/2) x + 1/2 >= 0,
             An inequality (1/2, 0.50000000000000000?) x + 1/2 >= 0,
             An inequality (1/2, -1/2) x + 1/2 >= 0,
             'base')

        For unbounded polyhedra, an error is raised::

            sage: C = CombinatorialPolyhedron([[0,1], [0,2]], far_face=[1,2], unbounded=True)
            sage: C.pyramid()
            Traceback (most recent call last):
            ...
            ValueError: self must be bounded"""
    @overload
    def pyramid(self, new_vertex=...) -> Any:
        """CombinatorialPolyhedron.pyramid(self, new_vertex=None, new_facet=None) -> CombinatorialPolyhedron

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 3354)

        Return the pyramid of ``self``.

        INPUT:

        - ``new_vertex`` -- (optional); specify a new vertex name to set up
          the pyramid with vertex names
        - ``new_facet`` -- (optional); specify a new facet name to set up
          the pyramid with facet names

        EXAMPLES::

            sage: C = CombinatorialPolyhedron(((1,2,3),(1,2,4),(1,3,4),(2,3,4)))
            sage: C1 = C.pyramid()
            sage: C1.facets()
            ((0, 1, 2, 4), (0, 1, 3, 4), (0, 2, 3, 4), (1, 2, 3, 4), (0, 1, 2, 3))

        ::

            sage: P = polytopes.cube()
            sage: C = CombinatorialPolyhedron(P)
            sage: C1 = C.pyramid()
            sage: P1 = P.pyramid()
            sage: C2 = P1.combinatorial_polyhedron()
            sage: C2.vertex_facet_graph().is_isomorphic(C1.vertex_facet_graph())        # needs sage.combinat
            True

        One can specify a name for the new vertex::

            sage: P = polytopes.cyclic_polytope(4,10)
            sage: C = P.combinatorial_polyhedron()
            sage: C1 = C.pyramid(new_vertex='apex')
            sage: C1.is_pyramid(certificate=True)
            (True, 'apex')
            sage: C1.facets()[0]
            (A vertex at (0, 0, 0, 0),
             A vertex at (1, 1, 1, 1),
             A vertex at (2, 4, 8, 16),
             A vertex at (3, 9, 27, 81),
             'apex')

        One can specify a name for the new facets::

            sage: # needs sage.rings.number_field
            sage: P = polytopes.regular_polygon(4)
            sage: C = P.combinatorial_polyhedron()
            sage: C1 = C.pyramid(new_facet='base')
            sage: C1.Hrepresentation()
            (An inequality (-1/2, 1/2) x + 1/2 >= 0,
             An inequality (-1/2, -1/2) x + 1/2 >= 0,
             An inequality (1/2, 0.50000000000000000?) x + 1/2 >= 0,
             An inequality (1/2, -1/2) x + 1/2 >= 0,
             'base')

        For unbounded polyhedra, an error is raised::

            sage: C = CombinatorialPolyhedron([[0,1], [0,2]], far_face=[1,2], unbounded=True)
            sage: C.pyramid()
            Traceback (most recent call last):
            ...
            ValueError: self must be bounded"""
    @overload
    def pyramid(self, new_facet=...) -> Any:
        """CombinatorialPolyhedron.pyramid(self, new_vertex=None, new_facet=None) -> CombinatorialPolyhedron

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 3354)

        Return the pyramid of ``self``.

        INPUT:

        - ``new_vertex`` -- (optional); specify a new vertex name to set up
          the pyramid with vertex names
        - ``new_facet`` -- (optional); specify a new facet name to set up
          the pyramid with facet names

        EXAMPLES::

            sage: C = CombinatorialPolyhedron(((1,2,3),(1,2,4),(1,3,4),(2,3,4)))
            sage: C1 = C.pyramid()
            sage: C1.facets()
            ((0, 1, 2, 4), (0, 1, 3, 4), (0, 2, 3, 4), (1, 2, 3, 4), (0, 1, 2, 3))

        ::

            sage: P = polytopes.cube()
            sage: C = CombinatorialPolyhedron(P)
            sage: C1 = C.pyramid()
            sage: P1 = P.pyramid()
            sage: C2 = P1.combinatorial_polyhedron()
            sage: C2.vertex_facet_graph().is_isomorphic(C1.vertex_facet_graph())        # needs sage.combinat
            True

        One can specify a name for the new vertex::

            sage: P = polytopes.cyclic_polytope(4,10)
            sage: C = P.combinatorial_polyhedron()
            sage: C1 = C.pyramid(new_vertex='apex')
            sage: C1.is_pyramid(certificate=True)
            (True, 'apex')
            sage: C1.facets()[0]
            (A vertex at (0, 0, 0, 0),
             A vertex at (1, 1, 1, 1),
             A vertex at (2, 4, 8, 16),
             A vertex at (3, 9, 27, 81),
             'apex')

        One can specify a name for the new facets::

            sage: # needs sage.rings.number_field
            sage: P = polytopes.regular_polygon(4)
            sage: C = P.combinatorial_polyhedron()
            sage: C1 = C.pyramid(new_facet='base')
            sage: C1.Hrepresentation()
            (An inequality (-1/2, 1/2) x + 1/2 >= 0,
             An inequality (-1/2, -1/2) x + 1/2 >= 0,
             An inequality (1/2, 0.50000000000000000?) x + 1/2 >= 0,
             An inequality (1/2, -1/2) x + 1/2 >= 0,
             'base')

        For unbounded polyhedra, an error is raised::

            sage: C = CombinatorialPolyhedron([[0,1], [0,2]], far_face=[1,2], unbounded=True)
            sage: C.pyramid()
            Traceback (most recent call last):
            ...
            ValueError: self must be bounded"""
    @overload
    def pyramid(self) -> Any:
        """CombinatorialPolyhedron.pyramid(self, new_vertex=None, new_facet=None) -> CombinatorialPolyhedron

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 3354)

        Return the pyramid of ``self``.

        INPUT:

        - ``new_vertex`` -- (optional); specify a new vertex name to set up
          the pyramid with vertex names
        - ``new_facet`` -- (optional); specify a new facet name to set up
          the pyramid with facet names

        EXAMPLES::

            sage: C = CombinatorialPolyhedron(((1,2,3),(1,2,4),(1,3,4),(2,3,4)))
            sage: C1 = C.pyramid()
            sage: C1.facets()
            ((0, 1, 2, 4), (0, 1, 3, 4), (0, 2, 3, 4), (1, 2, 3, 4), (0, 1, 2, 3))

        ::

            sage: P = polytopes.cube()
            sage: C = CombinatorialPolyhedron(P)
            sage: C1 = C.pyramid()
            sage: P1 = P.pyramid()
            sage: C2 = P1.combinatorial_polyhedron()
            sage: C2.vertex_facet_graph().is_isomorphic(C1.vertex_facet_graph())        # needs sage.combinat
            True

        One can specify a name for the new vertex::

            sage: P = polytopes.cyclic_polytope(4,10)
            sage: C = P.combinatorial_polyhedron()
            sage: C1 = C.pyramid(new_vertex='apex')
            sage: C1.is_pyramid(certificate=True)
            (True, 'apex')
            sage: C1.facets()[0]
            (A vertex at (0, 0, 0, 0),
             A vertex at (1, 1, 1, 1),
             A vertex at (2, 4, 8, 16),
             A vertex at (3, 9, 27, 81),
             'apex')

        One can specify a name for the new facets::

            sage: # needs sage.rings.number_field
            sage: P = polytopes.regular_polygon(4)
            sage: C = P.combinatorial_polyhedron()
            sage: C1 = C.pyramid(new_facet='base')
            sage: C1.Hrepresentation()
            (An inequality (-1/2, 1/2) x + 1/2 >= 0,
             An inequality (-1/2, -1/2) x + 1/2 >= 0,
             An inequality (1/2, 0.50000000000000000?) x + 1/2 >= 0,
             An inequality (1/2, -1/2) x + 1/2 >= 0,
             'base')

        For unbounded polyhedra, an error is raised::

            sage: C = CombinatorialPolyhedron([[0,1], [0,2]], far_face=[1,2], unbounded=True)
            sage: C.pyramid()
            Traceback (most recent call last):
            ...
            ValueError: self must be bounded"""
    @overload
    def ridges(self, add_equations=..., names=..., algorithm=...) -> Any:
        """CombinatorialPolyhedron.ridges(self, add_equations=False, names=True, algorithm=None)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 1362)

        Return the ridges.

        The ridges of a polyhedron are the faces
        contained in exactly two facets.

        To obtain all faces of codimension 1 use
        :meth:`CombinatorialPolyhedron.face_generator` instead.

        The ridges will be given by the facets, they are contained in.

        INPUT:

        - ``add_equations`` -- if ``True``, then equations of the polyhedron
          will be added (only applicable when ``names`` is ``True``)

        - ``names`` -- boolean (default: ``True``);
          if ``False``, then the facets are given by their indices

        - ``algorithm`` -- string (optional);
          specify whether the face generator starts with facets or vertices:
          * ``'primal'`` -- start with the facets
          * ``'dual'`` -- start with the vertices
          * ``None`` -- choose automatically

        .. NOTE::

            To compute ridges and f_vector, compute the ridges first.
            This might be faster.

        EXAMPLES::

            sage: # needs sage.combinat
            sage: P = polytopes.permutahedron(2)
            sage: C = CombinatorialPolyhedron(P)
            sage: C.ridges()
            ((An inequality (1, 0) x - 1 >= 0, An inequality (-1, 0) x + 2 >= 0),)
            sage: C.ridges(add_equations=True)
            (((An inequality (1, 0) x - 1 >= 0, An equation (1, 1) x - 3 == 0),
              (An inequality (-1, 0) x + 2 >= 0, An equation (1, 1) x - 3 == 0)),)

            sage: P = polytopes.cyclic_polytope(4,5)
            sage: C = CombinatorialPolyhedron(P)
            sage: C.ridges()
            ((An inequality (24, -26, 9, -1) x + 0 >= 0,
              An inequality (-50, 35, -10, 1) x + 24 >= 0),
             (An inequality (-12, 19, -8, 1) x + 0 >= 0,
              An inequality (-50, 35, -10, 1) x + 24 >= 0),
             (An inequality (8, -14, 7, -1) x + 0 >= 0,
              An inequality (-50, 35, -10, 1) x + 24 >= 0),
             (An inequality (-6, 11, -6, 1) x + 0 >= 0,
              An inequality (-50, 35, -10, 1) x + 24 >= 0),
             (An inequality (-12, 19, -8, 1) x + 0 >= 0,
              An inequality (24, -26, 9, -1) x + 0 >= 0),
             (An inequality (8, -14, 7, -1) x + 0 >= 0,
              An inequality (24, -26, 9, -1) x + 0 >= 0),
             (An inequality (-6, 11, -6, 1) x + 0 >= 0,
              An inequality (24, -26, 9, -1) x + 0 >= 0),
             (An inequality (8, -14, 7, -1) x + 0 >= 0,
              An inequality (-12, 19, -8, 1) x + 0 >= 0),
             (An inequality (-6, 11, -6, 1) x + 0 >= 0,
              An inequality (-12, 19, -8, 1) x + 0 >= 0),
             (An inequality (-6, 11, -6, 1) x + 0 >= 0,
              An inequality (8, -14, 7, -1) x + 0 >= 0))
            sage: C.ridges(names=False)
            ((3, 4),
             (2, 4),
             (1, 4),
             (0, 4),
             (2, 3),
             (1, 3),
             (0, 3),
             (1, 2),
             (0, 2),
             (0, 1))

            sage: P = Polyhedron(rays=[[1,0]])
            sage: C = CombinatorialPolyhedron(P)
            sage: C
            A 1-dimensional combinatorial polyhedron with 1 facet
            sage: C.ridges()
            ()
            sage: it = C.face_generator(0)
            sage: for face in it: face.ambient_Hrepresentation()
            (An inequality (1, 0) x + 0 >= 0, An equation (0, 1) x + 0 == 0)

        TESTS:

        Testing that ``add_equations`` is ignored if ``names`` is ``False``::

            sage: C = CombinatorialPolyhedron(polytopes.simplex())
            sage: C.ridges(names=False, add_equations=True)
            ((2, 3), (1, 3), (0, 3), (1, 2), (0, 2), (0, 1))"""
    @overload
    def ridges(self) -> Any:
        """CombinatorialPolyhedron.ridges(self, add_equations=False, names=True, algorithm=None)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 1362)

        Return the ridges.

        The ridges of a polyhedron are the faces
        contained in exactly two facets.

        To obtain all faces of codimension 1 use
        :meth:`CombinatorialPolyhedron.face_generator` instead.

        The ridges will be given by the facets, they are contained in.

        INPUT:

        - ``add_equations`` -- if ``True``, then equations of the polyhedron
          will be added (only applicable when ``names`` is ``True``)

        - ``names`` -- boolean (default: ``True``);
          if ``False``, then the facets are given by their indices

        - ``algorithm`` -- string (optional);
          specify whether the face generator starts with facets or vertices:
          * ``'primal'`` -- start with the facets
          * ``'dual'`` -- start with the vertices
          * ``None`` -- choose automatically

        .. NOTE::

            To compute ridges and f_vector, compute the ridges first.
            This might be faster.

        EXAMPLES::

            sage: # needs sage.combinat
            sage: P = polytopes.permutahedron(2)
            sage: C = CombinatorialPolyhedron(P)
            sage: C.ridges()
            ((An inequality (1, 0) x - 1 >= 0, An inequality (-1, 0) x + 2 >= 0),)
            sage: C.ridges(add_equations=True)
            (((An inequality (1, 0) x - 1 >= 0, An equation (1, 1) x - 3 == 0),
              (An inequality (-1, 0) x + 2 >= 0, An equation (1, 1) x - 3 == 0)),)

            sage: P = polytopes.cyclic_polytope(4,5)
            sage: C = CombinatorialPolyhedron(P)
            sage: C.ridges()
            ((An inequality (24, -26, 9, -1) x + 0 >= 0,
              An inequality (-50, 35, -10, 1) x + 24 >= 0),
             (An inequality (-12, 19, -8, 1) x + 0 >= 0,
              An inequality (-50, 35, -10, 1) x + 24 >= 0),
             (An inequality (8, -14, 7, -1) x + 0 >= 0,
              An inequality (-50, 35, -10, 1) x + 24 >= 0),
             (An inequality (-6, 11, -6, 1) x + 0 >= 0,
              An inequality (-50, 35, -10, 1) x + 24 >= 0),
             (An inequality (-12, 19, -8, 1) x + 0 >= 0,
              An inequality (24, -26, 9, -1) x + 0 >= 0),
             (An inequality (8, -14, 7, -1) x + 0 >= 0,
              An inequality (24, -26, 9, -1) x + 0 >= 0),
             (An inequality (-6, 11, -6, 1) x + 0 >= 0,
              An inequality (24, -26, 9, -1) x + 0 >= 0),
             (An inequality (8, -14, 7, -1) x + 0 >= 0,
              An inequality (-12, 19, -8, 1) x + 0 >= 0),
             (An inequality (-6, 11, -6, 1) x + 0 >= 0,
              An inequality (-12, 19, -8, 1) x + 0 >= 0),
             (An inequality (-6, 11, -6, 1) x + 0 >= 0,
              An inequality (8, -14, 7, -1) x + 0 >= 0))
            sage: C.ridges(names=False)
            ((3, 4),
             (2, 4),
             (1, 4),
             (0, 4),
             (2, 3),
             (1, 3),
             (0, 3),
             (1, 2),
             (0, 2),
             (0, 1))

            sage: P = Polyhedron(rays=[[1,0]])
            sage: C = CombinatorialPolyhedron(P)
            sage: C
            A 1-dimensional combinatorial polyhedron with 1 facet
            sage: C.ridges()
            ()
            sage: it = C.face_generator(0)
            sage: for face in it: face.ambient_Hrepresentation()
            (An inequality (1, 0) x + 0 >= 0, An equation (0, 1) x + 0 == 0)

        TESTS:

        Testing that ``add_equations`` is ignored if ``names`` is ``False``::

            sage: C = CombinatorialPolyhedron(polytopes.simplex())
            sage: C.ridges(names=False, add_equations=True)
            ((2, 3), (1, 3), (0, 3), (1, 2), (0, 2), (0, 1))"""
    @overload
    def ridges(self, add_equations=...) -> Any:
        """CombinatorialPolyhedron.ridges(self, add_equations=False, names=True, algorithm=None)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 1362)

        Return the ridges.

        The ridges of a polyhedron are the faces
        contained in exactly two facets.

        To obtain all faces of codimension 1 use
        :meth:`CombinatorialPolyhedron.face_generator` instead.

        The ridges will be given by the facets, they are contained in.

        INPUT:

        - ``add_equations`` -- if ``True``, then equations of the polyhedron
          will be added (only applicable when ``names`` is ``True``)

        - ``names`` -- boolean (default: ``True``);
          if ``False``, then the facets are given by their indices

        - ``algorithm`` -- string (optional);
          specify whether the face generator starts with facets or vertices:
          * ``'primal'`` -- start with the facets
          * ``'dual'`` -- start with the vertices
          * ``None`` -- choose automatically

        .. NOTE::

            To compute ridges and f_vector, compute the ridges first.
            This might be faster.

        EXAMPLES::

            sage: # needs sage.combinat
            sage: P = polytopes.permutahedron(2)
            sage: C = CombinatorialPolyhedron(P)
            sage: C.ridges()
            ((An inequality (1, 0) x - 1 >= 0, An inequality (-1, 0) x + 2 >= 0),)
            sage: C.ridges(add_equations=True)
            (((An inequality (1, 0) x - 1 >= 0, An equation (1, 1) x - 3 == 0),
              (An inequality (-1, 0) x + 2 >= 0, An equation (1, 1) x - 3 == 0)),)

            sage: P = polytopes.cyclic_polytope(4,5)
            sage: C = CombinatorialPolyhedron(P)
            sage: C.ridges()
            ((An inequality (24, -26, 9, -1) x + 0 >= 0,
              An inequality (-50, 35, -10, 1) x + 24 >= 0),
             (An inequality (-12, 19, -8, 1) x + 0 >= 0,
              An inequality (-50, 35, -10, 1) x + 24 >= 0),
             (An inequality (8, -14, 7, -1) x + 0 >= 0,
              An inequality (-50, 35, -10, 1) x + 24 >= 0),
             (An inequality (-6, 11, -6, 1) x + 0 >= 0,
              An inequality (-50, 35, -10, 1) x + 24 >= 0),
             (An inequality (-12, 19, -8, 1) x + 0 >= 0,
              An inequality (24, -26, 9, -1) x + 0 >= 0),
             (An inequality (8, -14, 7, -1) x + 0 >= 0,
              An inequality (24, -26, 9, -1) x + 0 >= 0),
             (An inequality (-6, 11, -6, 1) x + 0 >= 0,
              An inequality (24, -26, 9, -1) x + 0 >= 0),
             (An inequality (8, -14, 7, -1) x + 0 >= 0,
              An inequality (-12, 19, -8, 1) x + 0 >= 0),
             (An inequality (-6, 11, -6, 1) x + 0 >= 0,
              An inequality (-12, 19, -8, 1) x + 0 >= 0),
             (An inequality (-6, 11, -6, 1) x + 0 >= 0,
              An inequality (8, -14, 7, -1) x + 0 >= 0))
            sage: C.ridges(names=False)
            ((3, 4),
             (2, 4),
             (1, 4),
             (0, 4),
             (2, 3),
             (1, 3),
             (0, 3),
             (1, 2),
             (0, 2),
             (0, 1))

            sage: P = Polyhedron(rays=[[1,0]])
            sage: C = CombinatorialPolyhedron(P)
            sage: C
            A 1-dimensional combinatorial polyhedron with 1 facet
            sage: C.ridges()
            ()
            sage: it = C.face_generator(0)
            sage: for face in it: face.ambient_Hrepresentation()
            (An inequality (1, 0) x + 0 >= 0, An equation (0, 1) x + 0 == 0)

        TESTS:

        Testing that ``add_equations`` is ignored if ``names`` is ``False``::

            sage: C = CombinatorialPolyhedron(polytopes.simplex())
            sage: C.ridges(names=False, add_equations=True)
            ((2, 3), (1, 3), (0, 3), (1, 2), (0, 2), (0, 1))"""
    @overload
    def ridges(self) -> Any:
        """CombinatorialPolyhedron.ridges(self, add_equations=False, names=True, algorithm=None)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 1362)

        Return the ridges.

        The ridges of a polyhedron are the faces
        contained in exactly two facets.

        To obtain all faces of codimension 1 use
        :meth:`CombinatorialPolyhedron.face_generator` instead.

        The ridges will be given by the facets, they are contained in.

        INPUT:

        - ``add_equations`` -- if ``True``, then equations of the polyhedron
          will be added (only applicable when ``names`` is ``True``)

        - ``names`` -- boolean (default: ``True``);
          if ``False``, then the facets are given by their indices

        - ``algorithm`` -- string (optional);
          specify whether the face generator starts with facets or vertices:
          * ``'primal'`` -- start with the facets
          * ``'dual'`` -- start with the vertices
          * ``None`` -- choose automatically

        .. NOTE::

            To compute ridges and f_vector, compute the ridges first.
            This might be faster.

        EXAMPLES::

            sage: # needs sage.combinat
            sage: P = polytopes.permutahedron(2)
            sage: C = CombinatorialPolyhedron(P)
            sage: C.ridges()
            ((An inequality (1, 0) x - 1 >= 0, An inequality (-1, 0) x + 2 >= 0),)
            sage: C.ridges(add_equations=True)
            (((An inequality (1, 0) x - 1 >= 0, An equation (1, 1) x - 3 == 0),
              (An inequality (-1, 0) x + 2 >= 0, An equation (1, 1) x - 3 == 0)),)

            sage: P = polytopes.cyclic_polytope(4,5)
            sage: C = CombinatorialPolyhedron(P)
            sage: C.ridges()
            ((An inequality (24, -26, 9, -1) x + 0 >= 0,
              An inequality (-50, 35, -10, 1) x + 24 >= 0),
             (An inequality (-12, 19, -8, 1) x + 0 >= 0,
              An inequality (-50, 35, -10, 1) x + 24 >= 0),
             (An inequality (8, -14, 7, -1) x + 0 >= 0,
              An inequality (-50, 35, -10, 1) x + 24 >= 0),
             (An inequality (-6, 11, -6, 1) x + 0 >= 0,
              An inequality (-50, 35, -10, 1) x + 24 >= 0),
             (An inequality (-12, 19, -8, 1) x + 0 >= 0,
              An inequality (24, -26, 9, -1) x + 0 >= 0),
             (An inequality (8, -14, 7, -1) x + 0 >= 0,
              An inequality (24, -26, 9, -1) x + 0 >= 0),
             (An inequality (-6, 11, -6, 1) x + 0 >= 0,
              An inequality (24, -26, 9, -1) x + 0 >= 0),
             (An inequality (8, -14, 7, -1) x + 0 >= 0,
              An inequality (-12, 19, -8, 1) x + 0 >= 0),
             (An inequality (-6, 11, -6, 1) x + 0 >= 0,
              An inequality (-12, 19, -8, 1) x + 0 >= 0),
             (An inequality (-6, 11, -6, 1) x + 0 >= 0,
              An inequality (8, -14, 7, -1) x + 0 >= 0))
            sage: C.ridges(names=False)
            ((3, 4),
             (2, 4),
             (1, 4),
             (0, 4),
             (2, 3),
             (1, 3),
             (0, 3),
             (1, 2),
             (0, 2),
             (0, 1))

            sage: P = Polyhedron(rays=[[1,0]])
            sage: C = CombinatorialPolyhedron(P)
            sage: C
            A 1-dimensional combinatorial polyhedron with 1 facet
            sage: C.ridges()
            ()
            sage: it = C.face_generator(0)
            sage: for face in it: face.ambient_Hrepresentation()
            (An inequality (1, 0) x + 0 >= 0, An equation (0, 1) x + 0 == 0)

        TESTS:

        Testing that ``add_equations`` is ignored if ``names`` is ``False``::

            sage: C = CombinatorialPolyhedron(polytopes.simplex())
            sage: C.ridges(names=False, add_equations=True)
            ((2, 3), (1, 3), (0, 3), (1, 2), (0, 2), (0, 1))"""
    @overload
    def ridges(self, names=...) -> Any:
        """CombinatorialPolyhedron.ridges(self, add_equations=False, names=True, algorithm=None)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 1362)

        Return the ridges.

        The ridges of a polyhedron are the faces
        contained in exactly two facets.

        To obtain all faces of codimension 1 use
        :meth:`CombinatorialPolyhedron.face_generator` instead.

        The ridges will be given by the facets, they are contained in.

        INPUT:

        - ``add_equations`` -- if ``True``, then equations of the polyhedron
          will be added (only applicable when ``names`` is ``True``)

        - ``names`` -- boolean (default: ``True``);
          if ``False``, then the facets are given by their indices

        - ``algorithm`` -- string (optional);
          specify whether the face generator starts with facets or vertices:
          * ``'primal'`` -- start with the facets
          * ``'dual'`` -- start with the vertices
          * ``None`` -- choose automatically

        .. NOTE::

            To compute ridges and f_vector, compute the ridges first.
            This might be faster.

        EXAMPLES::

            sage: # needs sage.combinat
            sage: P = polytopes.permutahedron(2)
            sage: C = CombinatorialPolyhedron(P)
            sage: C.ridges()
            ((An inequality (1, 0) x - 1 >= 0, An inequality (-1, 0) x + 2 >= 0),)
            sage: C.ridges(add_equations=True)
            (((An inequality (1, 0) x - 1 >= 0, An equation (1, 1) x - 3 == 0),
              (An inequality (-1, 0) x + 2 >= 0, An equation (1, 1) x - 3 == 0)),)

            sage: P = polytopes.cyclic_polytope(4,5)
            sage: C = CombinatorialPolyhedron(P)
            sage: C.ridges()
            ((An inequality (24, -26, 9, -1) x + 0 >= 0,
              An inequality (-50, 35, -10, 1) x + 24 >= 0),
             (An inequality (-12, 19, -8, 1) x + 0 >= 0,
              An inequality (-50, 35, -10, 1) x + 24 >= 0),
             (An inequality (8, -14, 7, -1) x + 0 >= 0,
              An inequality (-50, 35, -10, 1) x + 24 >= 0),
             (An inequality (-6, 11, -6, 1) x + 0 >= 0,
              An inequality (-50, 35, -10, 1) x + 24 >= 0),
             (An inequality (-12, 19, -8, 1) x + 0 >= 0,
              An inequality (24, -26, 9, -1) x + 0 >= 0),
             (An inequality (8, -14, 7, -1) x + 0 >= 0,
              An inequality (24, -26, 9, -1) x + 0 >= 0),
             (An inequality (-6, 11, -6, 1) x + 0 >= 0,
              An inequality (24, -26, 9, -1) x + 0 >= 0),
             (An inequality (8, -14, 7, -1) x + 0 >= 0,
              An inequality (-12, 19, -8, 1) x + 0 >= 0),
             (An inequality (-6, 11, -6, 1) x + 0 >= 0,
              An inequality (-12, 19, -8, 1) x + 0 >= 0),
             (An inequality (-6, 11, -6, 1) x + 0 >= 0,
              An inequality (8, -14, 7, -1) x + 0 >= 0))
            sage: C.ridges(names=False)
            ((3, 4),
             (2, 4),
             (1, 4),
             (0, 4),
             (2, 3),
             (1, 3),
             (0, 3),
             (1, 2),
             (0, 2),
             (0, 1))

            sage: P = Polyhedron(rays=[[1,0]])
            sage: C = CombinatorialPolyhedron(P)
            sage: C
            A 1-dimensional combinatorial polyhedron with 1 facet
            sage: C.ridges()
            ()
            sage: it = C.face_generator(0)
            sage: for face in it: face.ambient_Hrepresentation()
            (An inequality (1, 0) x + 0 >= 0, An equation (0, 1) x + 0 == 0)

        TESTS:

        Testing that ``add_equations`` is ignored if ``names`` is ``False``::

            sage: C = CombinatorialPolyhedron(polytopes.simplex())
            sage: C.ridges(names=False, add_equations=True)
            ((2, 3), (1, 3), (0, 3), (1, 2), (0, 2), (0, 1))"""
    @overload
    def ridges(self) -> Any:
        """CombinatorialPolyhedron.ridges(self, add_equations=False, names=True, algorithm=None)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 1362)

        Return the ridges.

        The ridges of a polyhedron are the faces
        contained in exactly two facets.

        To obtain all faces of codimension 1 use
        :meth:`CombinatorialPolyhedron.face_generator` instead.

        The ridges will be given by the facets, they are contained in.

        INPUT:

        - ``add_equations`` -- if ``True``, then equations of the polyhedron
          will be added (only applicable when ``names`` is ``True``)

        - ``names`` -- boolean (default: ``True``);
          if ``False``, then the facets are given by their indices

        - ``algorithm`` -- string (optional);
          specify whether the face generator starts with facets or vertices:
          * ``'primal'`` -- start with the facets
          * ``'dual'`` -- start with the vertices
          * ``None`` -- choose automatically

        .. NOTE::

            To compute ridges and f_vector, compute the ridges first.
            This might be faster.

        EXAMPLES::

            sage: # needs sage.combinat
            sage: P = polytopes.permutahedron(2)
            sage: C = CombinatorialPolyhedron(P)
            sage: C.ridges()
            ((An inequality (1, 0) x - 1 >= 0, An inequality (-1, 0) x + 2 >= 0),)
            sage: C.ridges(add_equations=True)
            (((An inequality (1, 0) x - 1 >= 0, An equation (1, 1) x - 3 == 0),
              (An inequality (-1, 0) x + 2 >= 0, An equation (1, 1) x - 3 == 0)),)

            sage: P = polytopes.cyclic_polytope(4,5)
            sage: C = CombinatorialPolyhedron(P)
            sage: C.ridges()
            ((An inequality (24, -26, 9, -1) x + 0 >= 0,
              An inequality (-50, 35, -10, 1) x + 24 >= 0),
             (An inequality (-12, 19, -8, 1) x + 0 >= 0,
              An inequality (-50, 35, -10, 1) x + 24 >= 0),
             (An inequality (8, -14, 7, -1) x + 0 >= 0,
              An inequality (-50, 35, -10, 1) x + 24 >= 0),
             (An inequality (-6, 11, -6, 1) x + 0 >= 0,
              An inequality (-50, 35, -10, 1) x + 24 >= 0),
             (An inequality (-12, 19, -8, 1) x + 0 >= 0,
              An inequality (24, -26, 9, -1) x + 0 >= 0),
             (An inequality (8, -14, 7, -1) x + 0 >= 0,
              An inequality (24, -26, 9, -1) x + 0 >= 0),
             (An inequality (-6, 11, -6, 1) x + 0 >= 0,
              An inequality (24, -26, 9, -1) x + 0 >= 0),
             (An inequality (8, -14, 7, -1) x + 0 >= 0,
              An inequality (-12, 19, -8, 1) x + 0 >= 0),
             (An inequality (-6, 11, -6, 1) x + 0 >= 0,
              An inequality (-12, 19, -8, 1) x + 0 >= 0),
             (An inequality (-6, 11, -6, 1) x + 0 >= 0,
              An inequality (8, -14, 7, -1) x + 0 >= 0))
            sage: C.ridges(names=False)
            ((3, 4),
             (2, 4),
             (1, 4),
             (0, 4),
             (2, 3),
             (1, 3),
             (0, 3),
             (1, 2),
             (0, 2),
             (0, 1))

            sage: P = Polyhedron(rays=[[1,0]])
            sage: C = CombinatorialPolyhedron(P)
            sage: C
            A 1-dimensional combinatorial polyhedron with 1 facet
            sage: C.ridges()
            ()
            sage: it = C.face_generator(0)
            sage: for face in it: face.ambient_Hrepresentation()
            (An inequality (1, 0) x + 0 >= 0, An equation (0, 1) x + 0 == 0)

        TESTS:

        Testing that ``add_equations`` is ignored if ``names`` is ``False``::

            sage: C = CombinatorialPolyhedron(polytopes.simplex())
            sage: C.ridges(names=False, add_equations=True)
            ((2, 3), (1, 3), (0, 3), (1, 2), (0, 2), (0, 1))"""
    @overload
    def ridges(self, names=..., add_equations=...) -> Any:
        """CombinatorialPolyhedron.ridges(self, add_equations=False, names=True, algorithm=None)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 1362)

        Return the ridges.

        The ridges of a polyhedron are the faces
        contained in exactly two facets.

        To obtain all faces of codimension 1 use
        :meth:`CombinatorialPolyhedron.face_generator` instead.

        The ridges will be given by the facets, they are contained in.

        INPUT:

        - ``add_equations`` -- if ``True``, then equations of the polyhedron
          will be added (only applicable when ``names`` is ``True``)

        - ``names`` -- boolean (default: ``True``);
          if ``False``, then the facets are given by their indices

        - ``algorithm`` -- string (optional);
          specify whether the face generator starts with facets or vertices:
          * ``'primal'`` -- start with the facets
          * ``'dual'`` -- start with the vertices
          * ``None`` -- choose automatically

        .. NOTE::

            To compute ridges and f_vector, compute the ridges first.
            This might be faster.

        EXAMPLES::

            sage: # needs sage.combinat
            sage: P = polytopes.permutahedron(2)
            sage: C = CombinatorialPolyhedron(P)
            sage: C.ridges()
            ((An inequality (1, 0) x - 1 >= 0, An inequality (-1, 0) x + 2 >= 0),)
            sage: C.ridges(add_equations=True)
            (((An inequality (1, 0) x - 1 >= 0, An equation (1, 1) x - 3 == 0),
              (An inequality (-1, 0) x + 2 >= 0, An equation (1, 1) x - 3 == 0)),)

            sage: P = polytopes.cyclic_polytope(4,5)
            sage: C = CombinatorialPolyhedron(P)
            sage: C.ridges()
            ((An inequality (24, -26, 9, -1) x + 0 >= 0,
              An inequality (-50, 35, -10, 1) x + 24 >= 0),
             (An inequality (-12, 19, -8, 1) x + 0 >= 0,
              An inequality (-50, 35, -10, 1) x + 24 >= 0),
             (An inequality (8, -14, 7, -1) x + 0 >= 0,
              An inequality (-50, 35, -10, 1) x + 24 >= 0),
             (An inequality (-6, 11, -6, 1) x + 0 >= 0,
              An inequality (-50, 35, -10, 1) x + 24 >= 0),
             (An inequality (-12, 19, -8, 1) x + 0 >= 0,
              An inequality (24, -26, 9, -1) x + 0 >= 0),
             (An inequality (8, -14, 7, -1) x + 0 >= 0,
              An inequality (24, -26, 9, -1) x + 0 >= 0),
             (An inequality (-6, 11, -6, 1) x + 0 >= 0,
              An inequality (24, -26, 9, -1) x + 0 >= 0),
             (An inequality (8, -14, 7, -1) x + 0 >= 0,
              An inequality (-12, 19, -8, 1) x + 0 >= 0),
             (An inequality (-6, 11, -6, 1) x + 0 >= 0,
              An inequality (-12, 19, -8, 1) x + 0 >= 0),
             (An inequality (-6, 11, -6, 1) x + 0 >= 0,
              An inequality (8, -14, 7, -1) x + 0 >= 0))
            sage: C.ridges(names=False)
            ((3, 4),
             (2, 4),
             (1, 4),
             (0, 4),
             (2, 3),
             (1, 3),
             (0, 3),
             (1, 2),
             (0, 2),
             (0, 1))

            sage: P = Polyhedron(rays=[[1,0]])
            sage: C = CombinatorialPolyhedron(P)
            sage: C
            A 1-dimensional combinatorial polyhedron with 1 facet
            sage: C.ridges()
            ()
            sage: it = C.face_generator(0)
            sage: for face in it: face.ambient_Hrepresentation()
            (An inequality (1, 0) x + 0 >= 0, An equation (0, 1) x + 0 == 0)

        TESTS:

        Testing that ``add_equations`` is ignored if ``names`` is ``False``::

            sage: C = CombinatorialPolyhedron(polytopes.simplex())
            sage: C.ridges(names=False, add_equations=True)
            ((2, 3), (1, 3), (0, 3), (1, 2), (0, 2), (0, 1))"""
    @overload
    def simpliciality(self) -> Any:
        """CombinatorialPolyhedron.simpliciality(self)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 2061)

        Return the largest `k` such that the polytope is `k`-simplicial.

        Return the dimension in case of a simplex.

        A polytope is `k`-simplicial, if every `k`-face is a simplex.

        EXAMPLES::

            sage: cyclic = polytopes.cyclic_polytope(10,4)
            sage: CombinatorialPolyhedron(cyclic).simpliciality()
            3

            sage: hypersimplex = polytopes.hypersimplex(5,2)
            sage: CombinatorialPolyhedron(hypersimplex).simpliciality()
            2

            sage: cross = polytopes.cross_polytope(4)
            sage: P = cross.join(cross)
            sage: CombinatorialPolyhedron(P).simpliciality()
            3

            sage: P = polytopes.simplex(3)
            sage: CombinatorialPolyhedron(P).simpliciality()
            3

            sage: P = polytopes.simplex(1)
            sage: CombinatorialPolyhedron(P).simpliciality()
            1

        TESTS::

            sage: P = polytopes.cube()
            sage: C = CombinatorialPolyhedron(P)
            sage: C.simpliciality is C.simpliciality
            True"""
    @overload
    def simpliciality(self) -> Any:
        """CombinatorialPolyhedron.simpliciality(self)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 2061)

        Return the largest `k` such that the polytope is `k`-simplicial.

        Return the dimension in case of a simplex.

        A polytope is `k`-simplicial, if every `k`-face is a simplex.

        EXAMPLES::

            sage: cyclic = polytopes.cyclic_polytope(10,4)
            sage: CombinatorialPolyhedron(cyclic).simpliciality()
            3

            sage: hypersimplex = polytopes.hypersimplex(5,2)
            sage: CombinatorialPolyhedron(hypersimplex).simpliciality()
            2

            sage: cross = polytopes.cross_polytope(4)
            sage: P = cross.join(cross)
            sage: CombinatorialPolyhedron(P).simpliciality()
            3

            sage: P = polytopes.simplex(3)
            sage: CombinatorialPolyhedron(P).simpliciality()
            3

            sage: P = polytopes.simplex(1)
            sage: CombinatorialPolyhedron(P).simpliciality()
            1

        TESTS::

            sage: P = polytopes.cube()
            sage: C = CombinatorialPolyhedron(P)
            sage: C.simpliciality is C.simpliciality
            True"""
    @overload
    def simpliciality(self) -> Any:
        """CombinatorialPolyhedron.simpliciality(self)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 2061)

        Return the largest `k` such that the polytope is `k`-simplicial.

        Return the dimension in case of a simplex.

        A polytope is `k`-simplicial, if every `k`-face is a simplex.

        EXAMPLES::

            sage: cyclic = polytopes.cyclic_polytope(10,4)
            sage: CombinatorialPolyhedron(cyclic).simpliciality()
            3

            sage: hypersimplex = polytopes.hypersimplex(5,2)
            sage: CombinatorialPolyhedron(hypersimplex).simpliciality()
            2

            sage: cross = polytopes.cross_polytope(4)
            sage: P = cross.join(cross)
            sage: CombinatorialPolyhedron(P).simpliciality()
            3

            sage: P = polytopes.simplex(3)
            sage: CombinatorialPolyhedron(P).simpliciality()
            3

            sage: P = polytopes.simplex(1)
            sage: CombinatorialPolyhedron(P).simpliciality()
            1

        TESTS::

            sage: P = polytopes.cube()
            sage: C = CombinatorialPolyhedron(P)
            sage: C.simpliciality is C.simpliciality
            True"""
    @overload
    def simpliciality(self) -> Any:
        """CombinatorialPolyhedron.simpliciality(self)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 2061)

        Return the largest `k` such that the polytope is `k`-simplicial.

        Return the dimension in case of a simplex.

        A polytope is `k`-simplicial, if every `k`-face is a simplex.

        EXAMPLES::

            sage: cyclic = polytopes.cyclic_polytope(10,4)
            sage: CombinatorialPolyhedron(cyclic).simpliciality()
            3

            sage: hypersimplex = polytopes.hypersimplex(5,2)
            sage: CombinatorialPolyhedron(hypersimplex).simpliciality()
            2

            sage: cross = polytopes.cross_polytope(4)
            sage: P = cross.join(cross)
            sage: CombinatorialPolyhedron(P).simpliciality()
            3

            sage: P = polytopes.simplex(3)
            sage: CombinatorialPolyhedron(P).simpliciality()
            3

            sage: P = polytopes.simplex(1)
            sage: CombinatorialPolyhedron(P).simpliciality()
            1

        TESTS::

            sage: P = polytopes.cube()
            sage: C = CombinatorialPolyhedron(P)
            sage: C.simpliciality is C.simpliciality
            True"""
    @overload
    def simpliciality(self) -> Any:
        """CombinatorialPolyhedron.simpliciality(self)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 2061)

        Return the largest `k` such that the polytope is `k`-simplicial.

        Return the dimension in case of a simplex.

        A polytope is `k`-simplicial, if every `k`-face is a simplex.

        EXAMPLES::

            sage: cyclic = polytopes.cyclic_polytope(10,4)
            sage: CombinatorialPolyhedron(cyclic).simpliciality()
            3

            sage: hypersimplex = polytopes.hypersimplex(5,2)
            sage: CombinatorialPolyhedron(hypersimplex).simpliciality()
            2

            sage: cross = polytopes.cross_polytope(4)
            sage: P = cross.join(cross)
            sage: CombinatorialPolyhedron(P).simpliciality()
            3

            sage: P = polytopes.simplex(3)
            sage: CombinatorialPolyhedron(P).simpliciality()
            3

            sage: P = polytopes.simplex(1)
            sage: CombinatorialPolyhedron(P).simpliciality()
            1

        TESTS::

            sage: P = polytopes.cube()
            sage: C = CombinatorialPolyhedron(P)
            sage: C.simpliciality is C.simpliciality
            True"""
    @overload
    def simpliciality(self) -> Any:
        """CombinatorialPolyhedron.simpliciality(self)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 2061)

        Return the largest `k` such that the polytope is `k`-simplicial.

        Return the dimension in case of a simplex.

        A polytope is `k`-simplicial, if every `k`-face is a simplex.

        EXAMPLES::

            sage: cyclic = polytopes.cyclic_polytope(10,4)
            sage: CombinatorialPolyhedron(cyclic).simpliciality()
            3

            sage: hypersimplex = polytopes.hypersimplex(5,2)
            sage: CombinatorialPolyhedron(hypersimplex).simpliciality()
            2

            sage: cross = polytopes.cross_polytope(4)
            sage: P = cross.join(cross)
            sage: CombinatorialPolyhedron(P).simpliciality()
            3

            sage: P = polytopes.simplex(3)
            sage: CombinatorialPolyhedron(P).simpliciality()
            3

            sage: P = polytopes.simplex(1)
            sage: CombinatorialPolyhedron(P).simpliciality()
            1

        TESTS::

            sage: P = polytopes.cube()
            sage: C = CombinatorialPolyhedron(P)
            sage: C.simpliciality is C.simpliciality
            True"""
    def simplicity(self) -> Any:
        """CombinatorialPolyhedron.simplicity(self)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 2170)

        Return the largest `k` such that the polytope is `k`-simple.

        Return the dimension in case of a simplex.

        A polytope `P` is `k`-simple, if every `(d-1-k)`-face
        is contained in exactly `k+1` facets of `P` for `1 \\leq k \\leq d-1`.

        Equivalently it is `k`-simple if the polar/dual polytope is `k`-simplicial.

        EXAMPLES::

            sage: hyper4 = polytopes.hypersimplex(4,2)
            sage: CombinatorialPolyhedron(hyper4).simplicity()
            1

            sage: hyper5 = polytopes.hypersimplex(5,2)
            sage: CombinatorialPolyhedron(hyper5).simplicity()
            2

            sage: hyper6 = polytopes.hypersimplex(6,2)
            sage: CombinatorialPolyhedron(hyper6).simplicity()
            3

            sage: P = polytopes.simplex(3)
            sage: CombinatorialPolyhedron(P).simplicity()
            3

            sage: P = polytopes.simplex(1)
            sage: CombinatorialPolyhedron(P).simplicity()
            1

        TESTS::

            sage: P = polytopes.cube()
            sage: C = CombinatorialPolyhedron(P)
            sage: C.simplicity is C.simplicity
            True"""
    @overload
    def vertex_adjacency_matrix(self, algorithm=...) -> Any:
        """CombinatorialPolyhedron.vertex_adjacency_matrix(self, algorithm=None)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 1307)

        Return the binary matrix of vertex adjacencies.

        INPUT:

        - ``algorithm`` -- string (optional);
          specify whether the face generator starts with facets or vertices:
          * ``'primal'`` -- start with the facets
          * ``'dual'`` -- start with the vertices
          * ``None`` -- choose automatically

        .. SEEALSO::

            :meth:`~sage.geometry.polyhedron.base.Polyhedron_base.vertex_adjacency_matrix`.

        EXAMPLES::

            sage: P = polytopes.cube()
            sage: C = P.combinatorial_polyhedron()
            sage: C.vertex_adjacency_matrix()
            [0 1 0 1 0 1 0 0]
            [1 0 1 0 0 0 1 0]
            [0 1 0 1 0 0 0 1]
            [1 0 1 0 1 0 0 0]
            [0 0 0 1 0 1 0 1]
            [1 0 0 0 1 0 1 0]
            [0 1 0 0 0 1 0 1]
            [0 0 1 0 1 0 1 0]

        TESTS::

            sage: CombinatorialPolyhedron(-1).vertex_adjacency_matrix()
            []
            sage: CombinatorialPolyhedron(0).vertex_adjacency_matrix()
            [0]
            sage: polytopes.cube().vertex_adjacency_matrix().is_immutable()
            True"""
    @overload
    def vertex_adjacency_matrix(self) -> Any:
        """CombinatorialPolyhedron.vertex_adjacency_matrix(self, algorithm=None)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 1307)

        Return the binary matrix of vertex adjacencies.

        INPUT:

        - ``algorithm`` -- string (optional);
          specify whether the face generator starts with facets or vertices:
          * ``'primal'`` -- start with the facets
          * ``'dual'`` -- start with the vertices
          * ``None`` -- choose automatically

        .. SEEALSO::

            :meth:`~sage.geometry.polyhedron.base.Polyhedron_base.vertex_adjacency_matrix`.

        EXAMPLES::

            sage: P = polytopes.cube()
            sage: C = P.combinatorial_polyhedron()
            sage: C.vertex_adjacency_matrix()
            [0 1 0 1 0 1 0 0]
            [1 0 1 0 0 0 1 0]
            [0 1 0 1 0 0 0 1]
            [1 0 1 0 1 0 0 0]
            [0 0 0 1 0 1 0 1]
            [1 0 0 0 1 0 1 0]
            [0 1 0 0 0 1 0 1]
            [0 0 1 0 1 0 1 0]

        TESTS::

            sage: CombinatorialPolyhedron(-1).vertex_adjacency_matrix()
            []
            sage: CombinatorialPolyhedron(0).vertex_adjacency_matrix()
            [0]
            sage: polytopes.cube().vertex_adjacency_matrix().is_immutable()
            True"""
    @overload
    def vertex_adjacency_matrix(self) -> Any:
        """CombinatorialPolyhedron.vertex_adjacency_matrix(self, algorithm=None)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 1307)

        Return the binary matrix of vertex adjacencies.

        INPUT:

        - ``algorithm`` -- string (optional);
          specify whether the face generator starts with facets or vertices:
          * ``'primal'`` -- start with the facets
          * ``'dual'`` -- start with the vertices
          * ``None`` -- choose automatically

        .. SEEALSO::

            :meth:`~sage.geometry.polyhedron.base.Polyhedron_base.vertex_adjacency_matrix`.

        EXAMPLES::

            sage: P = polytopes.cube()
            sage: C = P.combinatorial_polyhedron()
            sage: C.vertex_adjacency_matrix()
            [0 1 0 1 0 1 0 0]
            [1 0 1 0 0 0 1 0]
            [0 1 0 1 0 0 0 1]
            [1 0 1 0 1 0 0 0]
            [0 0 0 1 0 1 0 1]
            [1 0 0 0 1 0 1 0]
            [0 1 0 0 0 1 0 1]
            [0 0 1 0 1 0 1 0]

        TESTS::

            sage: CombinatorialPolyhedron(-1).vertex_adjacency_matrix()
            []
            sage: CombinatorialPolyhedron(0).vertex_adjacency_matrix()
            [0]
            sage: polytopes.cube().vertex_adjacency_matrix().is_immutable()
            True"""
    @overload
    def vertex_adjacency_matrix(self) -> Any:
        """CombinatorialPolyhedron.vertex_adjacency_matrix(self, algorithm=None)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 1307)

        Return the binary matrix of vertex adjacencies.

        INPUT:

        - ``algorithm`` -- string (optional);
          specify whether the face generator starts with facets or vertices:
          * ``'primal'`` -- start with the facets
          * ``'dual'`` -- start with the vertices
          * ``None`` -- choose automatically

        .. SEEALSO::

            :meth:`~sage.geometry.polyhedron.base.Polyhedron_base.vertex_adjacency_matrix`.

        EXAMPLES::

            sage: P = polytopes.cube()
            sage: C = P.combinatorial_polyhedron()
            sage: C.vertex_adjacency_matrix()
            [0 1 0 1 0 1 0 0]
            [1 0 1 0 0 0 1 0]
            [0 1 0 1 0 0 0 1]
            [1 0 1 0 1 0 0 0]
            [0 0 0 1 0 1 0 1]
            [1 0 0 0 1 0 1 0]
            [0 1 0 0 0 1 0 1]
            [0 0 1 0 1 0 1 0]

        TESTS::

            sage: CombinatorialPolyhedron(-1).vertex_adjacency_matrix()
            []
            sage: CombinatorialPolyhedron(0).vertex_adjacency_matrix()
            [0]
            sage: polytopes.cube().vertex_adjacency_matrix().is_immutable()
            True"""
    @overload
    def vertex_adjacency_matrix(self) -> Any:
        """CombinatorialPolyhedron.vertex_adjacency_matrix(self, algorithm=None)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 1307)

        Return the binary matrix of vertex adjacencies.

        INPUT:

        - ``algorithm`` -- string (optional);
          specify whether the face generator starts with facets or vertices:
          * ``'primal'`` -- start with the facets
          * ``'dual'`` -- start with the vertices
          * ``None`` -- choose automatically

        .. SEEALSO::

            :meth:`~sage.geometry.polyhedron.base.Polyhedron_base.vertex_adjacency_matrix`.

        EXAMPLES::

            sage: P = polytopes.cube()
            sage: C = P.combinatorial_polyhedron()
            sage: C.vertex_adjacency_matrix()
            [0 1 0 1 0 1 0 0]
            [1 0 1 0 0 0 1 0]
            [0 1 0 1 0 0 0 1]
            [1 0 1 0 1 0 0 0]
            [0 0 0 1 0 1 0 1]
            [1 0 0 0 1 0 1 0]
            [0 1 0 0 0 1 0 1]
            [0 0 1 0 1 0 1 0]

        TESTS::

            sage: CombinatorialPolyhedron(-1).vertex_adjacency_matrix()
            []
            sage: CombinatorialPolyhedron(0).vertex_adjacency_matrix()
            [0]
            sage: polytopes.cube().vertex_adjacency_matrix().is_immutable()
            True"""
    @overload
    def vertex_facet_graph(self, names=...) -> Any:
        """CombinatorialPolyhedron.vertex_facet_graph(self, names=True)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 1588)

        Return the vertex-facet graph.

        This method constructs a directed bipartite graph.
        The nodes of the graph correspond to elements of the Vrepresentation
        and facets. There is a directed edge from Vrepresentation to facets
        for each incidence.

        If ``names`` is set to ``False``, then the vertices (of the graph) are given by
        integers.

        INPUT:

        - ``names`` -- boolean (default: ``True``); if ``True`` label the vertices of the
          graph by the corresponding names of the Vrepresentation resp. Hrepresentation;
          if ``False`` label the vertices of the graph by integers

        EXAMPLES::

            sage: P = polytopes.hypercube(2).pyramid()
            sage: C = CombinatorialPolyhedron(P)
            sage: G = C.vertex_facet_graph(); G                                         # needs sage.graphs
            Digraph on 10 vertices
            sage: C.Vrepresentation()
            (A vertex at (0, -1, -1),
             A vertex at (0, -1, 1),
             A vertex at (0, 1, -1),
             A vertex at (0, 1, 1),
             A vertex at (1, 0, 0))
            sage: sorted(G.neighbors_out(C.Vrepresentation()[4]))                       # needs sage.graphs
            [An inequality (-1, -1, 0) x + 1 >= 0,
             An inequality (-1, 0, -1) x + 1 >= 0,
             An inequality (-1, 0, 1) x + 1 >= 0,
             An inequality (-1, 1, 0) x + 1 >= 0]

        If ``names`` is ``True`` (the default) but the combinatorial polyhedron
        has been initialized without specifying names to
        ``Vrepresentation`` and ``Hrepresentation``,
        then indices of the Vrepresentation and the facets will be used along
        with a string 'H' or 'V'::

            sage: C = CombinatorialPolyhedron(P.incidence_matrix())
            sage: C.vertex_facet_graph().vertices(sort=True)                            # needs sage.graphs
            [('H', 0),
             ('H', 1),
             ('H', 2),
             ('H', 3),
             ('H', 4),
             ('V', 0),
             ('V', 1),
             ('V', 2),
             ('V', 3),
             ('V', 4)]

        If ``names`` is ``False`` then the vertices of the graph are given by integers::

            sage: C.vertex_facet_graph(names=False).vertices(sort=True)                 # needs sage.graphs
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

        TESTS:

        Test that :issue:`29898` is fixed::

            sage: Polyhedron().vertex_facet_graph()                                     # needs sage.graphs
            Digraph on 0 vertices
            sage: Polyhedron([[0]]).vertex_facet_graph()                                # needs sage.graphs
            Digraph on 1 vertex
            sage: Polyhedron([[0]]).vertex_facet_graph(False)                           # needs sage.graphs
            Digraph on 1 vertex"""
    @overload
    def vertex_facet_graph(self) -> Any:
        """CombinatorialPolyhedron.vertex_facet_graph(self, names=True)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 1588)

        Return the vertex-facet graph.

        This method constructs a directed bipartite graph.
        The nodes of the graph correspond to elements of the Vrepresentation
        and facets. There is a directed edge from Vrepresentation to facets
        for each incidence.

        If ``names`` is set to ``False``, then the vertices (of the graph) are given by
        integers.

        INPUT:

        - ``names`` -- boolean (default: ``True``); if ``True`` label the vertices of the
          graph by the corresponding names of the Vrepresentation resp. Hrepresentation;
          if ``False`` label the vertices of the graph by integers

        EXAMPLES::

            sage: P = polytopes.hypercube(2).pyramid()
            sage: C = CombinatorialPolyhedron(P)
            sage: G = C.vertex_facet_graph(); G                                         # needs sage.graphs
            Digraph on 10 vertices
            sage: C.Vrepresentation()
            (A vertex at (0, -1, -1),
             A vertex at (0, -1, 1),
             A vertex at (0, 1, -1),
             A vertex at (0, 1, 1),
             A vertex at (1, 0, 0))
            sage: sorted(G.neighbors_out(C.Vrepresentation()[4]))                       # needs sage.graphs
            [An inequality (-1, -1, 0) x + 1 >= 0,
             An inequality (-1, 0, -1) x + 1 >= 0,
             An inequality (-1, 0, 1) x + 1 >= 0,
             An inequality (-1, 1, 0) x + 1 >= 0]

        If ``names`` is ``True`` (the default) but the combinatorial polyhedron
        has been initialized without specifying names to
        ``Vrepresentation`` and ``Hrepresentation``,
        then indices of the Vrepresentation and the facets will be used along
        with a string 'H' or 'V'::

            sage: C = CombinatorialPolyhedron(P.incidence_matrix())
            sage: C.vertex_facet_graph().vertices(sort=True)                            # needs sage.graphs
            [('H', 0),
             ('H', 1),
             ('H', 2),
             ('H', 3),
             ('H', 4),
             ('V', 0),
             ('V', 1),
             ('V', 2),
             ('V', 3),
             ('V', 4)]

        If ``names`` is ``False`` then the vertices of the graph are given by integers::

            sage: C.vertex_facet_graph(names=False).vertices(sort=True)                 # needs sage.graphs
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

        TESTS:

        Test that :issue:`29898` is fixed::

            sage: Polyhedron().vertex_facet_graph()                                     # needs sage.graphs
            Digraph on 0 vertices
            sage: Polyhedron([[0]]).vertex_facet_graph()                                # needs sage.graphs
            Digraph on 1 vertex
            sage: Polyhedron([[0]]).vertex_facet_graph(False)                           # needs sage.graphs
            Digraph on 1 vertex"""
    @overload
    def vertex_facet_graph(self) -> Any:
        """CombinatorialPolyhedron.vertex_facet_graph(self, names=True)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 1588)

        Return the vertex-facet graph.

        This method constructs a directed bipartite graph.
        The nodes of the graph correspond to elements of the Vrepresentation
        and facets. There is a directed edge from Vrepresentation to facets
        for each incidence.

        If ``names`` is set to ``False``, then the vertices (of the graph) are given by
        integers.

        INPUT:

        - ``names`` -- boolean (default: ``True``); if ``True`` label the vertices of the
          graph by the corresponding names of the Vrepresentation resp. Hrepresentation;
          if ``False`` label the vertices of the graph by integers

        EXAMPLES::

            sage: P = polytopes.hypercube(2).pyramid()
            sage: C = CombinatorialPolyhedron(P)
            sage: G = C.vertex_facet_graph(); G                                         # needs sage.graphs
            Digraph on 10 vertices
            sage: C.Vrepresentation()
            (A vertex at (0, -1, -1),
             A vertex at (0, -1, 1),
             A vertex at (0, 1, -1),
             A vertex at (0, 1, 1),
             A vertex at (1, 0, 0))
            sage: sorted(G.neighbors_out(C.Vrepresentation()[4]))                       # needs sage.graphs
            [An inequality (-1, -1, 0) x + 1 >= 0,
             An inequality (-1, 0, -1) x + 1 >= 0,
             An inequality (-1, 0, 1) x + 1 >= 0,
             An inequality (-1, 1, 0) x + 1 >= 0]

        If ``names`` is ``True`` (the default) but the combinatorial polyhedron
        has been initialized without specifying names to
        ``Vrepresentation`` and ``Hrepresentation``,
        then indices of the Vrepresentation and the facets will be used along
        with a string 'H' or 'V'::

            sage: C = CombinatorialPolyhedron(P.incidence_matrix())
            sage: C.vertex_facet_graph().vertices(sort=True)                            # needs sage.graphs
            [('H', 0),
             ('H', 1),
             ('H', 2),
             ('H', 3),
             ('H', 4),
             ('V', 0),
             ('V', 1),
             ('V', 2),
             ('V', 3),
             ('V', 4)]

        If ``names`` is ``False`` then the vertices of the graph are given by integers::

            sage: C.vertex_facet_graph(names=False).vertices(sort=True)                 # needs sage.graphs
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

        TESTS:

        Test that :issue:`29898` is fixed::

            sage: Polyhedron().vertex_facet_graph()                                     # needs sage.graphs
            Digraph on 0 vertices
            sage: Polyhedron([[0]]).vertex_facet_graph()                                # needs sage.graphs
            Digraph on 1 vertex
            sage: Polyhedron([[0]]).vertex_facet_graph(False)                           # needs sage.graphs
            Digraph on 1 vertex"""
    @overload
    def vertex_facet_graph(self, names=...) -> Any:
        """CombinatorialPolyhedron.vertex_facet_graph(self, names=True)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 1588)

        Return the vertex-facet graph.

        This method constructs a directed bipartite graph.
        The nodes of the graph correspond to elements of the Vrepresentation
        and facets. There is a directed edge from Vrepresentation to facets
        for each incidence.

        If ``names`` is set to ``False``, then the vertices (of the graph) are given by
        integers.

        INPUT:

        - ``names`` -- boolean (default: ``True``); if ``True`` label the vertices of the
          graph by the corresponding names of the Vrepresentation resp. Hrepresentation;
          if ``False`` label the vertices of the graph by integers

        EXAMPLES::

            sage: P = polytopes.hypercube(2).pyramid()
            sage: C = CombinatorialPolyhedron(P)
            sage: G = C.vertex_facet_graph(); G                                         # needs sage.graphs
            Digraph on 10 vertices
            sage: C.Vrepresentation()
            (A vertex at (0, -1, -1),
             A vertex at (0, -1, 1),
             A vertex at (0, 1, -1),
             A vertex at (0, 1, 1),
             A vertex at (1, 0, 0))
            sage: sorted(G.neighbors_out(C.Vrepresentation()[4]))                       # needs sage.graphs
            [An inequality (-1, -1, 0) x + 1 >= 0,
             An inequality (-1, 0, -1) x + 1 >= 0,
             An inequality (-1, 0, 1) x + 1 >= 0,
             An inequality (-1, 1, 0) x + 1 >= 0]

        If ``names`` is ``True`` (the default) but the combinatorial polyhedron
        has been initialized without specifying names to
        ``Vrepresentation`` and ``Hrepresentation``,
        then indices of the Vrepresentation and the facets will be used along
        with a string 'H' or 'V'::

            sage: C = CombinatorialPolyhedron(P.incidence_matrix())
            sage: C.vertex_facet_graph().vertices(sort=True)                            # needs sage.graphs
            [('H', 0),
             ('H', 1),
             ('H', 2),
             ('H', 3),
             ('H', 4),
             ('V', 0),
             ('V', 1),
             ('V', 2),
             ('V', 3),
             ('V', 4)]

        If ``names`` is ``False`` then the vertices of the graph are given by integers::

            sage: C.vertex_facet_graph(names=False).vertices(sort=True)                 # needs sage.graphs
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

        TESTS:

        Test that :issue:`29898` is fixed::

            sage: Polyhedron().vertex_facet_graph()                                     # needs sage.graphs
            Digraph on 0 vertices
            sage: Polyhedron([[0]]).vertex_facet_graph()                                # needs sage.graphs
            Digraph on 1 vertex
            sage: Polyhedron([[0]]).vertex_facet_graph(False)                           # needs sage.graphs
            Digraph on 1 vertex"""
    @overload
    def vertex_facet_graph(self) -> Any:
        """CombinatorialPolyhedron.vertex_facet_graph(self, names=True)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 1588)

        Return the vertex-facet graph.

        This method constructs a directed bipartite graph.
        The nodes of the graph correspond to elements of the Vrepresentation
        and facets. There is a directed edge from Vrepresentation to facets
        for each incidence.

        If ``names`` is set to ``False``, then the vertices (of the graph) are given by
        integers.

        INPUT:

        - ``names`` -- boolean (default: ``True``); if ``True`` label the vertices of the
          graph by the corresponding names of the Vrepresentation resp. Hrepresentation;
          if ``False`` label the vertices of the graph by integers

        EXAMPLES::

            sage: P = polytopes.hypercube(2).pyramid()
            sage: C = CombinatorialPolyhedron(P)
            sage: G = C.vertex_facet_graph(); G                                         # needs sage.graphs
            Digraph on 10 vertices
            sage: C.Vrepresentation()
            (A vertex at (0, -1, -1),
             A vertex at (0, -1, 1),
             A vertex at (0, 1, -1),
             A vertex at (0, 1, 1),
             A vertex at (1, 0, 0))
            sage: sorted(G.neighbors_out(C.Vrepresentation()[4]))                       # needs sage.graphs
            [An inequality (-1, -1, 0) x + 1 >= 0,
             An inequality (-1, 0, -1) x + 1 >= 0,
             An inequality (-1, 0, 1) x + 1 >= 0,
             An inequality (-1, 1, 0) x + 1 >= 0]

        If ``names`` is ``True`` (the default) but the combinatorial polyhedron
        has been initialized without specifying names to
        ``Vrepresentation`` and ``Hrepresentation``,
        then indices of the Vrepresentation and the facets will be used along
        with a string 'H' or 'V'::

            sage: C = CombinatorialPolyhedron(P.incidence_matrix())
            sage: C.vertex_facet_graph().vertices(sort=True)                            # needs sage.graphs
            [('H', 0),
             ('H', 1),
             ('H', 2),
             ('H', 3),
             ('H', 4),
             ('V', 0),
             ('V', 1),
             ('V', 2),
             ('V', 3),
             ('V', 4)]

        If ``names`` is ``False`` then the vertices of the graph are given by integers::

            sage: C.vertex_facet_graph(names=False).vertices(sort=True)                 # needs sage.graphs
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

        TESTS:

        Test that :issue:`29898` is fixed::

            sage: Polyhedron().vertex_facet_graph()                                     # needs sage.graphs
            Digraph on 0 vertices
            sage: Polyhedron([[0]]).vertex_facet_graph()                                # needs sage.graphs
            Digraph on 1 vertex
            sage: Polyhedron([[0]]).vertex_facet_graph(False)                           # needs sage.graphs
            Digraph on 1 vertex"""
    @overload
    def vertex_facet_graph(self) -> Any:
        """CombinatorialPolyhedron.vertex_facet_graph(self, names=True)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 1588)

        Return the vertex-facet graph.

        This method constructs a directed bipartite graph.
        The nodes of the graph correspond to elements of the Vrepresentation
        and facets. There is a directed edge from Vrepresentation to facets
        for each incidence.

        If ``names`` is set to ``False``, then the vertices (of the graph) are given by
        integers.

        INPUT:

        - ``names`` -- boolean (default: ``True``); if ``True`` label the vertices of the
          graph by the corresponding names of the Vrepresentation resp. Hrepresentation;
          if ``False`` label the vertices of the graph by integers

        EXAMPLES::

            sage: P = polytopes.hypercube(2).pyramid()
            sage: C = CombinatorialPolyhedron(P)
            sage: G = C.vertex_facet_graph(); G                                         # needs sage.graphs
            Digraph on 10 vertices
            sage: C.Vrepresentation()
            (A vertex at (0, -1, -1),
             A vertex at (0, -1, 1),
             A vertex at (0, 1, -1),
             A vertex at (0, 1, 1),
             A vertex at (1, 0, 0))
            sage: sorted(G.neighbors_out(C.Vrepresentation()[4]))                       # needs sage.graphs
            [An inequality (-1, -1, 0) x + 1 >= 0,
             An inequality (-1, 0, -1) x + 1 >= 0,
             An inequality (-1, 0, 1) x + 1 >= 0,
             An inequality (-1, 1, 0) x + 1 >= 0]

        If ``names`` is ``True`` (the default) but the combinatorial polyhedron
        has been initialized without specifying names to
        ``Vrepresentation`` and ``Hrepresentation``,
        then indices of the Vrepresentation and the facets will be used along
        with a string 'H' or 'V'::

            sage: C = CombinatorialPolyhedron(P.incidence_matrix())
            sage: C.vertex_facet_graph().vertices(sort=True)                            # needs sage.graphs
            [('H', 0),
             ('H', 1),
             ('H', 2),
             ('H', 3),
             ('H', 4),
             ('V', 0),
             ('V', 1),
             ('V', 2),
             ('V', 3),
             ('V', 4)]

        If ``names`` is ``False`` then the vertices of the graph are given by integers::

            sage: C.vertex_facet_graph(names=False).vertices(sort=True)                 # needs sage.graphs
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

        TESTS:

        Test that :issue:`29898` is fixed::

            sage: Polyhedron().vertex_facet_graph()                                     # needs sage.graphs
            Digraph on 0 vertices
            sage: Polyhedron([[0]]).vertex_facet_graph()                                # needs sage.graphs
            Digraph on 1 vertex
            sage: Polyhedron([[0]]).vertex_facet_graph(False)                           # needs sage.graphs
            Digraph on 1 vertex"""
    @overload
    def vertex_facet_graph(self, _False) -> Any:
        """CombinatorialPolyhedron.vertex_facet_graph(self, names=True)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 1588)

        Return the vertex-facet graph.

        This method constructs a directed bipartite graph.
        The nodes of the graph correspond to elements of the Vrepresentation
        and facets. There is a directed edge from Vrepresentation to facets
        for each incidence.

        If ``names`` is set to ``False``, then the vertices (of the graph) are given by
        integers.

        INPUT:

        - ``names`` -- boolean (default: ``True``); if ``True`` label the vertices of the
          graph by the corresponding names of the Vrepresentation resp. Hrepresentation;
          if ``False`` label the vertices of the graph by integers

        EXAMPLES::

            sage: P = polytopes.hypercube(2).pyramid()
            sage: C = CombinatorialPolyhedron(P)
            sage: G = C.vertex_facet_graph(); G                                         # needs sage.graphs
            Digraph on 10 vertices
            sage: C.Vrepresentation()
            (A vertex at (0, -1, -1),
             A vertex at (0, -1, 1),
             A vertex at (0, 1, -1),
             A vertex at (0, 1, 1),
             A vertex at (1, 0, 0))
            sage: sorted(G.neighbors_out(C.Vrepresentation()[4]))                       # needs sage.graphs
            [An inequality (-1, -1, 0) x + 1 >= 0,
             An inequality (-1, 0, -1) x + 1 >= 0,
             An inequality (-1, 0, 1) x + 1 >= 0,
             An inequality (-1, 1, 0) x + 1 >= 0]

        If ``names`` is ``True`` (the default) but the combinatorial polyhedron
        has been initialized without specifying names to
        ``Vrepresentation`` and ``Hrepresentation``,
        then indices of the Vrepresentation and the facets will be used along
        with a string 'H' or 'V'::

            sage: C = CombinatorialPolyhedron(P.incidence_matrix())
            sage: C.vertex_facet_graph().vertices(sort=True)                            # needs sage.graphs
            [('H', 0),
             ('H', 1),
             ('H', 2),
             ('H', 3),
             ('H', 4),
             ('V', 0),
             ('V', 1),
             ('V', 2),
             ('V', 3),
             ('V', 4)]

        If ``names`` is ``False`` then the vertices of the graph are given by integers::

            sage: C.vertex_facet_graph(names=False).vertices(sort=True)                 # needs sage.graphs
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

        TESTS:

        Test that :issue:`29898` is fixed::

            sage: Polyhedron().vertex_facet_graph()                                     # needs sage.graphs
            Digraph on 0 vertices
            sage: Polyhedron([[0]]).vertex_facet_graph()                                # needs sage.graphs
            Digraph on 1 vertex
            sage: Polyhedron([[0]]).vertex_facet_graph(False)                           # needs sage.graphs
            Digraph on 1 vertex"""
    @overload
    def vertex_graph(self, names=..., algorithm=...) -> Any:
        """CombinatorialPolyhedron.vertex_graph(self, names=True, algorithm=None)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 1266)

        Return a graph in which the vertices correspond to vertices
        of the polyhedron, and edges to bounded rank 1 faces.

        INPUT:

        - ``names`` -- boolean (default: ``True``); if ``False``,
          then the nodes of the graph are labeld by the
          indices of the Vrepresentation

        - ``algorithm`` -- string (optional);
          specify whether the face generator starts with facets or vertices:
          * ``'primal'`` -- start with the facets
          * ``'dual'`` -- start with the vertices
          * ``None`` -- choose automatically

        EXAMPLES::

            sage: P = polytopes.cyclic_polytope(3,5)
            sage: C = CombinatorialPolyhedron(P)
            sage: G = C.vertex_graph(); G                                               # needs sage.graphs
            Graph on 5 vertices
            sage: sorted(G.degree())                                                    # needs sage.graphs
            [3, 3, 4, 4, 4]

            sage: P = Polyhedron(rays=[[1]])
            sage: C = CombinatorialPolyhedron(P)
            sage: C.graph()                                                             # needs sage.graphs
            Graph on 1 vertex"""
    @overload
    def vertex_graph(self) -> Any:
        """CombinatorialPolyhedron.vertex_graph(self, names=True, algorithm=None)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 1266)

        Return a graph in which the vertices correspond to vertices
        of the polyhedron, and edges to bounded rank 1 faces.

        INPUT:

        - ``names`` -- boolean (default: ``True``); if ``False``,
          then the nodes of the graph are labeld by the
          indices of the Vrepresentation

        - ``algorithm`` -- string (optional);
          specify whether the face generator starts with facets or vertices:
          * ``'primal'`` -- start with the facets
          * ``'dual'`` -- start with the vertices
          * ``None`` -- choose automatically

        EXAMPLES::

            sage: P = polytopes.cyclic_polytope(3,5)
            sage: C = CombinatorialPolyhedron(P)
            sage: G = C.vertex_graph(); G                                               # needs sage.graphs
            Graph on 5 vertices
            sage: sorted(G.degree())                                                    # needs sage.graphs
            [3, 3, 4, 4, 4]

            sage: P = Polyhedron(rays=[[1]])
            sage: C = CombinatorialPolyhedron(P)
            sage: C.graph()                                                             # needs sage.graphs
            Graph on 1 vertex"""
    @overload
    def vertices(self, names=...) -> Any:
        """CombinatorialPolyhedron.vertices(self, names=True)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 873)

        Return the elements in the Vrepresentation that are vertices.

        In case of an unbounded polyhedron, there might be lines and
        rays in the Vrepresentation.

        If ``names`` is set to ``False``, then the vertices are given by
        their indices in the Vrepresentation.

        EXAMPLES::

            sage: P = Polyhedron(rays=[[1,0,0],[0,1,0],[0,0,1]])
            sage: C = CombinatorialPolyhedron(P)
            sage: C.vertices()
            (A vertex at (0, 0, 0),)
            sage: C.Vrepresentation()
            (A vertex at (0, 0, 0),
             A ray in the direction (0, 0, 1),
             A ray in the direction (0, 1, 0),
             A ray in the direction (1, 0, 0))
            sage: P = polytopes.cross_polytope(3)
            sage: C = CombinatorialPolyhedron(P)
            sage: C.vertices()
            (A vertex at (-1, 0, 0),
             A vertex at (0, -1, 0),
             A vertex at (0, 0, -1),
             A vertex at (0, 0, 1),
             A vertex at (0, 1, 0),
             A vertex at (1, 0, 0))
            sage: C.vertices(names=False)
            (0, 1, 2, 3, 4, 5)

            sage: points = [(1,0,0), (0,1,0), (0,0,1),
            ....:           (-1,0,0), (0,-1,0), (0,0,-1)]
            sage: L = LatticePolytope(points)
            sage: C = CombinatorialPolyhedron(L)
            sage: C.vertices()
            (M(1, 0, 0), M(0, 1, 0), M(0, 0, 1), M(-1, 0, 0), M(0, -1, 0), M(0, 0, -1))
            sage: C.vertices(names=False)
            (0, 1, 2, 3, 4, 5)

            sage: P = Polyhedron(vertices=[[0,0]])
            sage: C = CombinatorialPolyhedron(P)
            sage: C.vertices()
            (A vertex at (0, 0),)"""
    @overload
    def vertices(self) -> Any:
        """CombinatorialPolyhedron.vertices(self, names=True)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 873)

        Return the elements in the Vrepresentation that are vertices.

        In case of an unbounded polyhedron, there might be lines and
        rays in the Vrepresentation.

        If ``names`` is set to ``False``, then the vertices are given by
        their indices in the Vrepresentation.

        EXAMPLES::

            sage: P = Polyhedron(rays=[[1,0,0],[0,1,0],[0,0,1]])
            sage: C = CombinatorialPolyhedron(P)
            sage: C.vertices()
            (A vertex at (0, 0, 0),)
            sage: C.Vrepresentation()
            (A vertex at (0, 0, 0),
             A ray in the direction (0, 0, 1),
             A ray in the direction (0, 1, 0),
             A ray in the direction (1, 0, 0))
            sage: P = polytopes.cross_polytope(3)
            sage: C = CombinatorialPolyhedron(P)
            sage: C.vertices()
            (A vertex at (-1, 0, 0),
             A vertex at (0, -1, 0),
             A vertex at (0, 0, -1),
             A vertex at (0, 0, 1),
             A vertex at (0, 1, 0),
             A vertex at (1, 0, 0))
            sage: C.vertices(names=False)
            (0, 1, 2, 3, 4, 5)

            sage: points = [(1,0,0), (0,1,0), (0,0,1),
            ....:           (-1,0,0), (0,-1,0), (0,0,-1)]
            sage: L = LatticePolytope(points)
            sage: C = CombinatorialPolyhedron(L)
            sage: C.vertices()
            (M(1, 0, 0), M(0, 1, 0), M(0, 0, 1), M(-1, 0, 0), M(0, -1, 0), M(0, 0, -1))
            sage: C.vertices(names=False)
            (0, 1, 2, 3, 4, 5)

            sage: P = Polyhedron(vertices=[[0,0]])
            sage: C = CombinatorialPolyhedron(P)
            sage: C.vertices()
            (A vertex at (0, 0),)"""
    @overload
    def vertices(self) -> Any:
        """CombinatorialPolyhedron.vertices(self, names=True)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 873)

        Return the elements in the Vrepresentation that are vertices.

        In case of an unbounded polyhedron, there might be lines and
        rays in the Vrepresentation.

        If ``names`` is set to ``False``, then the vertices are given by
        their indices in the Vrepresentation.

        EXAMPLES::

            sage: P = Polyhedron(rays=[[1,0,0],[0,1,0],[0,0,1]])
            sage: C = CombinatorialPolyhedron(P)
            sage: C.vertices()
            (A vertex at (0, 0, 0),)
            sage: C.Vrepresentation()
            (A vertex at (0, 0, 0),
             A ray in the direction (0, 0, 1),
             A ray in the direction (0, 1, 0),
             A ray in the direction (1, 0, 0))
            sage: P = polytopes.cross_polytope(3)
            sage: C = CombinatorialPolyhedron(P)
            sage: C.vertices()
            (A vertex at (-1, 0, 0),
             A vertex at (0, -1, 0),
             A vertex at (0, 0, -1),
             A vertex at (0, 0, 1),
             A vertex at (0, 1, 0),
             A vertex at (1, 0, 0))
            sage: C.vertices(names=False)
            (0, 1, 2, 3, 4, 5)

            sage: points = [(1,0,0), (0,1,0), (0,0,1),
            ....:           (-1,0,0), (0,-1,0), (0,0,-1)]
            sage: L = LatticePolytope(points)
            sage: C = CombinatorialPolyhedron(L)
            sage: C.vertices()
            (M(1, 0, 0), M(0, 1, 0), M(0, 0, 1), M(-1, 0, 0), M(0, -1, 0), M(0, 0, -1))
            sage: C.vertices(names=False)
            (0, 1, 2, 3, 4, 5)

            sage: P = Polyhedron(vertices=[[0,0]])
            sage: C = CombinatorialPolyhedron(P)
            sage: C.vertices()
            (A vertex at (0, 0),)"""
    @overload
    def vertices(self, names=...) -> Any:
        """CombinatorialPolyhedron.vertices(self, names=True)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 873)

        Return the elements in the Vrepresentation that are vertices.

        In case of an unbounded polyhedron, there might be lines and
        rays in the Vrepresentation.

        If ``names`` is set to ``False``, then the vertices are given by
        their indices in the Vrepresentation.

        EXAMPLES::

            sage: P = Polyhedron(rays=[[1,0,0],[0,1,0],[0,0,1]])
            sage: C = CombinatorialPolyhedron(P)
            sage: C.vertices()
            (A vertex at (0, 0, 0),)
            sage: C.Vrepresentation()
            (A vertex at (0, 0, 0),
             A ray in the direction (0, 0, 1),
             A ray in the direction (0, 1, 0),
             A ray in the direction (1, 0, 0))
            sage: P = polytopes.cross_polytope(3)
            sage: C = CombinatorialPolyhedron(P)
            sage: C.vertices()
            (A vertex at (-1, 0, 0),
             A vertex at (0, -1, 0),
             A vertex at (0, 0, -1),
             A vertex at (0, 0, 1),
             A vertex at (0, 1, 0),
             A vertex at (1, 0, 0))
            sage: C.vertices(names=False)
            (0, 1, 2, 3, 4, 5)

            sage: points = [(1,0,0), (0,1,0), (0,0,1),
            ....:           (-1,0,0), (0,-1,0), (0,0,-1)]
            sage: L = LatticePolytope(points)
            sage: C = CombinatorialPolyhedron(L)
            sage: C.vertices()
            (M(1, 0, 0), M(0, 1, 0), M(0, 0, 1), M(-1, 0, 0), M(0, -1, 0), M(0, 0, -1))
            sage: C.vertices(names=False)
            (0, 1, 2, 3, 4, 5)

            sage: P = Polyhedron(vertices=[[0,0]])
            sage: C = CombinatorialPolyhedron(P)
            sage: C.vertices()
            (A vertex at (0, 0),)"""
    @overload
    def vertices(self) -> Any:
        """CombinatorialPolyhedron.vertices(self, names=True)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 873)

        Return the elements in the Vrepresentation that are vertices.

        In case of an unbounded polyhedron, there might be lines and
        rays in the Vrepresentation.

        If ``names`` is set to ``False``, then the vertices are given by
        their indices in the Vrepresentation.

        EXAMPLES::

            sage: P = Polyhedron(rays=[[1,0,0],[0,1,0],[0,0,1]])
            sage: C = CombinatorialPolyhedron(P)
            sage: C.vertices()
            (A vertex at (0, 0, 0),)
            sage: C.Vrepresentation()
            (A vertex at (0, 0, 0),
             A ray in the direction (0, 0, 1),
             A ray in the direction (0, 1, 0),
             A ray in the direction (1, 0, 0))
            sage: P = polytopes.cross_polytope(3)
            sage: C = CombinatorialPolyhedron(P)
            sage: C.vertices()
            (A vertex at (-1, 0, 0),
             A vertex at (0, -1, 0),
             A vertex at (0, 0, -1),
             A vertex at (0, 0, 1),
             A vertex at (0, 1, 0),
             A vertex at (1, 0, 0))
            sage: C.vertices(names=False)
            (0, 1, 2, 3, 4, 5)

            sage: points = [(1,0,0), (0,1,0), (0,0,1),
            ....:           (-1,0,0), (0,-1,0), (0,0,-1)]
            sage: L = LatticePolytope(points)
            sage: C = CombinatorialPolyhedron(L)
            sage: C.vertices()
            (M(1, 0, 0), M(0, 1, 0), M(0, 0, 1), M(-1, 0, 0), M(0, -1, 0), M(0, 0, -1))
            sage: C.vertices(names=False)
            (0, 1, 2, 3, 4, 5)

            sage: P = Polyhedron(vertices=[[0,0]])
            sage: C = CombinatorialPolyhedron(P)
            sage: C.vertices()
            (A vertex at (0, 0),)"""
    @overload
    def vertices(self, names=...) -> Any:
        """CombinatorialPolyhedron.vertices(self, names=True)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 873)

        Return the elements in the Vrepresentation that are vertices.

        In case of an unbounded polyhedron, there might be lines and
        rays in the Vrepresentation.

        If ``names`` is set to ``False``, then the vertices are given by
        their indices in the Vrepresentation.

        EXAMPLES::

            sage: P = Polyhedron(rays=[[1,0,0],[0,1,0],[0,0,1]])
            sage: C = CombinatorialPolyhedron(P)
            sage: C.vertices()
            (A vertex at (0, 0, 0),)
            sage: C.Vrepresentation()
            (A vertex at (0, 0, 0),
             A ray in the direction (0, 0, 1),
             A ray in the direction (0, 1, 0),
             A ray in the direction (1, 0, 0))
            sage: P = polytopes.cross_polytope(3)
            sage: C = CombinatorialPolyhedron(P)
            sage: C.vertices()
            (A vertex at (-1, 0, 0),
             A vertex at (0, -1, 0),
             A vertex at (0, 0, -1),
             A vertex at (0, 0, 1),
             A vertex at (0, 1, 0),
             A vertex at (1, 0, 0))
            sage: C.vertices(names=False)
            (0, 1, 2, 3, 4, 5)

            sage: points = [(1,0,0), (0,1,0), (0,0,1),
            ....:           (-1,0,0), (0,-1,0), (0,0,-1)]
            sage: L = LatticePolytope(points)
            sage: C = CombinatorialPolyhedron(L)
            sage: C.vertices()
            (M(1, 0, 0), M(0, 1, 0), M(0, 0, 1), M(-1, 0, 0), M(0, -1, 0), M(0, 0, -1))
            sage: C.vertices(names=False)
            (0, 1, 2, 3, 4, 5)

            sage: P = Polyhedron(vertices=[[0,0]])
            sage: C = CombinatorialPolyhedron(P)
            sage: C.vertices()
            (A vertex at (0, 0),)"""
    @overload
    def vertices(self) -> Any:
        """CombinatorialPolyhedron.vertices(self, names=True)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 873)

        Return the elements in the Vrepresentation that are vertices.

        In case of an unbounded polyhedron, there might be lines and
        rays in the Vrepresentation.

        If ``names`` is set to ``False``, then the vertices are given by
        their indices in the Vrepresentation.

        EXAMPLES::

            sage: P = Polyhedron(rays=[[1,0,0],[0,1,0],[0,0,1]])
            sage: C = CombinatorialPolyhedron(P)
            sage: C.vertices()
            (A vertex at (0, 0, 0),)
            sage: C.Vrepresentation()
            (A vertex at (0, 0, 0),
             A ray in the direction (0, 0, 1),
             A ray in the direction (0, 1, 0),
             A ray in the direction (1, 0, 0))
            sage: P = polytopes.cross_polytope(3)
            sage: C = CombinatorialPolyhedron(P)
            sage: C.vertices()
            (A vertex at (-1, 0, 0),
             A vertex at (0, -1, 0),
             A vertex at (0, 0, -1),
             A vertex at (0, 0, 1),
             A vertex at (0, 1, 0),
             A vertex at (1, 0, 0))
            sage: C.vertices(names=False)
            (0, 1, 2, 3, 4, 5)

            sage: points = [(1,0,0), (0,1,0), (0,0,1),
            ....:           (-1,0,0), (0,-1,0), (0,0,-1)]
            sage: L = LatticePolytope(points)
            sage: C = CombinatorialPolyhedron(L)
            sage: C.vertices()
            (M(1, 0, 0), M(0, 1, 0), M(0, 0, 1), M(-1, 0, 0), M(0, -1, 0), M(0, 0, -1))
            sage: C.vertices(names=False)
            (0, 1, 2, 3, 4, 5)

            sage: P = Polyhedron(vertices=[[0,0]])
            sage: C = CombinatorialPolyhedron(P)
            sage: C.vertices()
            (A vertex at (0, 0),)"""
    def __eq__(self, other) -> Any:
        """CombinatorialPolyhedron.__eq__(self, other)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 3294)

        Return whether ``self`` and ``other`` are equal."""
    def __ge__(self, other: object) -> bool:
        """Return self>=value."""
    def __gt__(self, other: object) -> bool:
        """Return self>value."""
    def __le__(self, other: object) -> bool:
        """Return self<=value."""
    def __lt__(self, other: object) -> bool:
        """Return self<value."""
    def __ne__(self, other: object) -> bool:
        """Return self!=value."""
    def __reduce__(self) -> Any:
        """CombinatorialPolyhedron.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/geometry/polyhedron/combinatorial_polyhedron/base.pyx (starting at line 635)

        Override __reduce__ to correctly pickle/unpickle.

        TESTS::

            sage: # needs sage.combinat
            sage: P = polytopes.permutahedron(4)
            sage: C = CombinatorialPolyhedron(P)
            sage: C1 = loads(C.dumps())
            sage: it = C.face_generator()
            sage: it1 = C1.face_generator()
            sage: tup = tuple((face.ambient_Vrepresentation(),
            ....:              face.ambient_Hrepresentation()) for face in it)
            sage: tup1 = tuple((face.ambient_Vrepresentation(),
            ....:               face.ambient_Hrepresentation()) for face in it1)
            sage: tup == tup1
            True

            sage: P = polytopes.cyclic_polytope(4,10)
            sage: C = CombinatorialPolyhedron(P)
            sage: C1 = loads(C.dumps())
            sage: it = C.face_generator()
            sage: it1 = C1.face_generator()
            sage: tup = tuple((face.ambient_Vrepresentation(), face.ambient_Hrepresentation()) for face in it)
            sage: tup1 = tuple((face.ambient_Vrepresentation(), face.ambient_Hrepresentation()) for face in it1)
            sage: tup == tup1
            True

            sage: P = Polyhedron(rays=[[1,0,0], [-1,0,0], [0,-1,0]])
            sage: C = CombinatorialPolyhedron(P)
            sage: C1 = loads(C.dumps())
            sage: it = C.face_generator()
            sage: it1 = C1.face_generator()
            sage: tup = tuple((face.ambient_Vrepresentation(), face.ambient_Hrepresentation()) for face in it)
            sage: tup1 = tuple((face.ambient_Vrepresentation(), face.ambient_Hrepresentation()) for face in it1)
            sage: tup == tup1
            True

            sage: P = Polyhedron(rays=[[1,0,0], [-1,0,0],
            ....:                      [0,-1,0], [0,1,0]])
            sage: C = CombinatorialPolyhedron(P)
            sage: C1 = loads(C.dumps())
            sage: it = C.face_generator()
            sage: it1 = C1.face_generator()
            sage: tup = tuple((face.ambient_Vrepresentation(), face.ambient_Hrepresentation()) for face in it)
            sage: tup1 = tuple((face.ambient_Vrepresentation(), face.ambient_Hrepresentation()) for face in it1)
            sage: tup == tup1
            True"""
