from .base_QQ import Polyhedron_QQ as Polyhedron_QQ
from .base_ZZ import Polyhedron_ZZ as Polyhedron_ZZ
from .base_number_field import Polyhedron_base_number_field as Polyhedron_base_number_field
from sage.arith.functions import LCM_list as LCM_list
from sage.matrix.constructor import vector as vector
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.functional import denominator as denominator
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.misc.misc_c import prod as prod
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.rational_field import QQ as QQ
from sage.structure.element import Element as Element

class Polyhedron_normaliz(Polyhedron_base_number_field):
    """
    Polyhedra with normaliz.

    INPUT:

    - ``parent`` -- :class:`~sage.geometry.polyhedron.parent.Polyhedra`
      the parent

    - ``Vrep`` -- list ``[vertices, rays, lines]`` or ``None``; the
      V-representation of the polyhedron; if ``None``, the polyhedron
      is determined by the H-representation

    - ``Hrep`` -- list ``[ieqs, eqns]`` or ``None``; the
      H-representation of the polyhedron; if ``None``, the polyhedron
      is determined by the V-representation

    - ``normaliz_cone`` -- a PyNormaliz wrapper of a normaliz cone

    Only one of ``Vrep``, ``Hrep``, or ``normaliz_cone`` can be different
    from ``None``.

    EXAMPLES::

        sage: p = Polyhedron(vertices=[(0,0), (1,0), (0,1)],
        ....:                rays=[(1,1)], lines=[],
        ....:                backend='normaliz')
        sage: TestSuite(p).run()

    Two ways to get the full space::

        sage: Polyhedron(eqns=[[0, 0, 0]], backend='normaliz')
        A 2-dimensional polyhedron in QQ^2 defined as the convex hull of 1 vertex and 2 lines
        sage: Polyhedron(ieqs=[[0, 0, 0]], backend='normaliz')
        A 2-dimensional polyhedron in QQ^2 defined as the convex hull of 1 vertex and 2 lines

    A lower-dimensional affine cone; we test that there are no mysterious
    inequalities coming in from the homogenization::

        sage: P = Polyhedron(vertices=[(1, 1)], rays=[(0, 1)],
        ....:                backend='normaliz')
        sage: P.n_inequalities()
        1
        sage: P.equations()
        (An equation (1, 0) x - 1 == 0,)

    The empty polyhedron::

        sage: P = Polyhedron(ieqs=[[-2, 1, 1], [-3, -1, -1], [-4, 1, -2]],
        ....:                backend='normaliz')
        sage: P
        The empty polyhedron in QQ^2
        sage: P.Vrepresentation()
        ()
        sage: P.Hrepresentation()
        (An equation -1 == 0,)

    TESTS:

    Tests copied from various methods in :mod:`sage.geometry.polyhedron.base`::

        sage: p = Polyhedron(vertices=[[1,0,0], [0,1,0], [0,0,1]],
        ....:                backend='normaliz')
        sage: p.n_equations()
        1
        sage: p.n_inequalities()
        3

        sage: p = Polyhedron(vertices=[[t,t^2,t^3] for t in range(6)],
        ....:                backend='normaliz')
        sage: p.n_facets()
        8

        sage: p = Polyhedron(vertices=[[1,0], [0,1], [1,1]], rays=[[1,1]],
        ....:                backend='normaliz')
        sage: p.n_vertices()
        2

        sage: p = Polyhedron(vertices=[[1,0], [0,1]], rays=[[1,1]],
        ....:                backend='normaliz')
        sage: p.n_rays()
        1

        sage: p = Polyhedron(vertices=[[0,0]], rays=[[0,1], [0,-1]],
        ....:                backend='normaliz')
        sage: p.n_lines()
        1

    Algebraic polyhedra::

        sage: P = Polyhedron(vertices=[[1], [sqrt(2)]],                                 # needs sage.rings.number_field sage.symbolic
        ....:                backend='normaliz', verbose=True)
        # ----8<---- Equivalent Normaliz input file ----8<----
        amb_space 1
        number_field min_poly (a^2 - 2) embedding [1.414213562373095 +/- 2.99e-16]
        cone 0
        subspace 0
        vertices 2
         1 1
         (a) 1
        # ----8<-------------------8<-------------------8<----
        # Calling PyNormaliz.NmzCone(cone=[], number_field=['a^2 - 2', 'a', '[1.414213562373095 +/- 2.99e-16]'], subspace=[], vertices=[[1, 1], [[[0, 1], [1, 1]], 1]])
        sage: P                                                                         # needs sage.rings.number_field sage.symbolic
        A 1-dimensional polyhedron in (Symbolic Ring)^1 defined as
         the convex hull of 2 vertices
        sage: P.vertices()                                                              # needs sage.rings.number_field sage.symbolic
        (A vertex at (1), A vertex at (sqrt(2)))

        sage: P = polytopes.icosahedron(exact=True,                                     # needs sage.rings.number_field
        ....:                           backend='normaliz'); P
        A 3-dimensional polyhedron in
         (Number Field in sqrt5 with defining polynomial x^2 - 5
          with sqrt5 = 2.236067977499790?)^3
         defined as the convex hull of 12 vertices

        sage: x = polygen(ZZ)
        sage: P = Polyhedron(vertices=[[sqrt(2)],                                       # needs sage.rings.number_field sage.symbolic
        ....:                          [AA.polynomial_root(x^3 - 2, RIF(0,3))]],
        ....:                backend='normaliz', verbose=True)
        # ----8<---- Equivalent Normaliz input file ----8<----
        amb_space 1
        number_field min_poly (a^6 - 2) embedding [1.122462048309373 +/- 5.38e-16]
        cone 0
        subspace 0
        vertices 2
         (a^3) 1
         (a^2) 1
        # ----8<-------------------8<-------------------8<----
        # Calling PyNormaliz.NmzCone(cone=[], number_field=['a^6 - 2', 'a', '[1.122462048309373 +/- 5.38e-16]'], subspace=[], vertices=[[[[0, 1], [0, 1], [0, 1], [1, 1], [0, 1], [0, 1]], 1], [[[0, 1], [0, 1], [1, 1], [0, 1], [0, 1], [0, 1]], 1]])
        sage: P                                                                         # needs sage.rings.number_field sage.symbolic
        A 1-dimensional polyhedron in (Symbolic Ring)^1 defined as
         the convex hull of 2 vertices
        sage: P.vertices()                                                              # needs sage.rings.number_field sage.symbolic
        (A vertex at (2^(1/3)), A vertex at (sqrt(2)))
    """
    def __init__(self, parent, Vrep, Hrep, normaliz_cone=None, normaliz_data=None, internal_base_ring=None, **kwds) -> None:
        """
        Initialize the polyhedron.

        See :class:`Polyhedron_normaliz` for a description of the input
        data.

        TESTS::

            sage: p = Polyhedron(backend='normaliz')
            sage: TestSuite(p).run()
            sage: p = Polyhedron(vertices=[(1, 1)], rays=[(0, 1)],
            ....:                backend='normaliz')
            sage: TestSuite(p).run()
            sage: p = Polyhedron(vertices=[(-1,-1), (1,0), (1,1), (0,1)],
            ....:                backend='normaliz')
            sage: TestSuite(p).run()
        """
    def __copy__(self):
        """
        Return a copy of ``self``.

        TESTS::

            sage: P = polytopes.cube(backend='normaliz')
            sage: Q = copy(P)
            sage: P._normaliz_cone is Q._normaliz_cone
            False
        """
    def integral_hull(self):
        '''
        Return the integral hull in the polyhedron.

        This is a new polyhedron that is the convex hull of all integral
        points.

        EXAMPLES:

        Unbounded example from Normaliz manual, "a dull polyhedron"::

            sage: P = Polyhedron(ieqs=[[1, 0, 2], [3, 0, -2], [3, 2, -2]],
            ....:                backend=\'normaliz\')
            sage: PI = P.integral_hull()
            sage: P.plot(color=\'yellow\') + PI.plot(color=\'green\')                       # needs sage.plot
            Graphics object consisting of 10 graphics primitives
            sage: PI.Vrepresentation()
            (A vertex at (-1, 0),
             A vertex at (0, 1),
             A ray in the direction (1, 0))

        Nonpointed case::

            sage: P = Polyhedron(vertices=[[1/2, 1/3]], rays=[[1, 1]],
            ....:                lines=[[-1, 1]], backend=\'normaliz\')
            sage: PI = P.integral_hull()
            sage: PI.Vrepresentation()
            (A vertex at (1, 0),
             A ray in the direction (1, 0),
             A line in the direction (1, -1))

        Empty polyhedron::

            sage: P = Polyhedron(backend=\'normaliz\')
            sage: PI = P.integral_hull()
            sage: PI.Vrepresentation()
            ()
        '''

class Polyhedron_QQ_normaliz(Polyhedron_normaliz, Polyhedron_QQ):
    """
    Polyhedra over `\\QQ` with normaliz.

    INPUT:

    - ``Vrep`` -- list ``[vertices, rays, lines]`` or ``None``
    - ``Hrep`` -- list ``[ieqs, eqns]`` or ``None``

    EXAMPLES::

        sage: p = Polyhedron(vertices=[(0,0), (1,0), (0,1)],
        ....:                rays=[(1,1)], lines=[],
        ....:                backend='normaliz', base_ring=QQ)
        sage: TestSuite(p).run()
    """
    def ehrhart_series(self, variable: str = 't'):
        """
        Return the Ehrhart series of a compact rational polyhedron.

        The Ehrhart series is the generating function where the coefficient of
        `t^k` is number of integer lattice points inside the `k`-th dilation of
        the polytope.

        INPUT:

        - ``variable`` -- string (default: ``'t'``)

        OUTPUT: a rational function

        EXAMPLES::

            sage: S = Polyhedron(vertices=[[0,1], [1,0]], backend='normaliz')
            sage: ES = S.ehrhart_series()
            sage: ES.numerator()
            1
            sage: ES.denominator().factor()
            (t - 1)^2

            sage: C = Polyhedron(vertices=[[0,0,0], [0,0,1], [0,1,0], [0,1,1],
            ....:                          [1,0,0], [1,0,1], [1,1,0], [1,1,1]],
            ....:                backend='normaliz')
            sage: ES = C.ehrhart_series()
            sage: ES.numerator()
            t^2 + 4*t + 1
            sage: ES.denominator().factor()
            (t - 1)^4

        The following example is from the Normaliz manual contained in the file
        ``rational.in``::

            sage: rat_poly = Polyhedron(vertices=[[1/2,1/2], [-1/3,-1/3], [1/4,-1/2]],
            ....:                       backend='normaliz')
            sage: ES = rat_poly.ehrhart_series()
            sage: ES.numerator()
            2*t^6 + 3*t^5 + 4*t^4 + 3*t^3 + t^2 + t + 1
            sage: ES.denominator().factor()
            (-1) * (t + 1)^2 * (t - 1)^3 * (t^2 + 1) * (t^2 + t + 1)

        The polyhedron should be compact::

            sage: C = Polyhedron(rays=[[1,2], [2,1]], backend='normaliz')
            sage: C.ehrhart_series()
            Traceback (most recent call last):
            ...
            NotImplementedError: Ehrhart series can only be computed for compact polyhedron

        .. SEEALSO::

            :meth:`~sage.geometry.polyhedron.backend_normaliz.hilbert_series`

        TESTS:

        Check that the Ehrhart series is pickled::

            sage: new_poly = loads(dumps(rat_poly))
            sage: new_poly.ehrhart_series.is_in_cache()
            True
        """
    def hilbert_series(self, grading, variable: str = 't'):
        """
        Return the Hilbert series of the polyhedron with respect to ``grading``.

        INPUT:

        - ``grading`` -- vector. The grading to use to form the Hilbert series

        - ``variable`` -- string (default: ``'t'``)

        OUTPUT: a rational function

        EXAMPLES::

            sage: C = Polyhedron(backend='normaliz',
            ....:                rays=[[0,0,1], [0,1,1], [1,0,1], [1,1,1]])
            sage: HS = C.hilbert_series([1,1,1])
            sage: HS.numerator()
            t^2 + 1
            sage: HS.denominator().factor()
            (-1) * (t + 1) * (t - 1)^3 * (t^2 + t + 1)

        By changing the grading, you can get the Ehrhart series of the square
        lifted at height 1::

            sage: C.hilbert_series([0,0,1])
            (t + 1)/(-t^3 + 3*t^2 - 3*t + 1)

        Here is an example ``2cone.in`` from the Normaliz manual::

            sage: C = Polyhedron(backend='normaliz', rays=[[1,3], [2,1]])
            sage: HS = C.hilbert_series([1,1])
            sage: HS.numerator()
            t^5 + t^4 + t^3 + t^2 + 1
            sage: HS.denominator().factor()
            (t + 1) * (t - 1)^2 * (t^2 + 1) * (t^2 + t + 1)

            sage: HS = C.hilbert_series([1,2])
            sage: HS.numerator()
            t^8 + t^6 + t^5 + t^3 + 1
            sage: HS.denominator().factor()
            (t + 1) * (t - 1)^2 * (t^2 + 1) * (t^6 + t^5 + t^4 + t^3 + t^2 + t + 1)

        Here is the magic square example form the Normaliz manual::

            sage: eq = [[0,1,1,1,-1,-1,-1, 0, 0, 0],
            ....:       [0,1,1,1, 0, 0, 0,-1,-1,-1],
            ....:       [0,0,1,1,-1, 0, 0,-1, 0, 0],
            ....:       [0,1,0,1, 0,-1, 0, 0,-1, 0],
            ....:       [0,1,1,0, 0, 0,-1, 0, 0,-1],
            ....:       [0,0,1,1, 0,-1, 0, 0, 0,-1],
            ....:       [0,1,1,0, 0,-1, 0,-1, 0, 0]]
            sage: magic_square = (Polyhedron(eqns=eq, backend='normaliz')
            ....:                 & Polyhedron(rays=identity_matrix(9).rows()))
            sage: grading = [1,1,1,0,0,0,0,0,0]
            sage: magic_square.hilbert_series(grading)
            (t^6 + 2*t^3 + 1)/(-t^9 + 3*t^6 - 3*t^3 + 1)

        .. SEEALSO::

            :meth:`~sage.geometry.polyhedron.backend_normaliz.ehrhart_series`

        TESTS:

        Check that the Hilbert series is pickled::

            sage: new_magic = loads(dumps(magic_square))
            sage: new_magic.hilbert_series.is_in_cache(grading)
            True
        """
    def integral_points(self, threshold: int = 10000) -> tuple:
        """
        Return the integral points in the polyhedron.

        Uses either the naive algorithm (iterate over a rectangular
        bounding box) or triangulation + Smith form.

        INPUT:

        - ``threshold`` -- integer (default: 10000); use the naïve
          algorithm as long as the bounding box is smaller than this

        OUTPUT:

        The list of integral points in the polyhedron. If the
        polyhedron is not compact, a :exc:`ValueError` is raised.

        EXAMPLES::

            sage: Polyhedron(vertices=[(-1,-1), (1,0), (1,1), (0,1)],
            ....:            backend='normaliz').integral_points()
            ((-1, -1), (0, 0), (0, 1), (1, 0), (1, 1))

            sage: simplex = Polyhedron([(1,2,3), (2,3,7), (-2,-3,-11)],
            ....:                      backend='normaliz')
            sage: simplex.integral_points()
            ((-2, -3, -11), (0, 0, -2), (1, 2, 3), (2, 3, 7))

        The polyhedron need not be full-dimensional::

            sage: simplex = Polyhedron([(1,2,3,5), (2,3,7,5), (-2,-3,-11,5)],
            ....:                      backend='normaliz')
            sage: simplex.integral_points()
            ((-2, -3, -11, 5), (0, 0, -2, 5), (1, 2, 3, 5), (2, 3, 7, 5))

            sage: point = Polyhedron([(2,3,7)],
            ....:                    backend='normaliz')
            sage: point.integral_points()
            ((2, 3, 7),)

            sage: empty = Polyhedron(backend='normaliz')
            sage: empty.integral_points()
            ()

        Here is a simplex where the naive algorithm of running over
        all points in a rectangular bounding box no longer works fast
        enough::

            sage: v = [(1,0,7,-1), (-2,-2,4,-3), (-1,-1,-1,4), (2,9,0,-5), (-2,-1,5,1)]
            sage: simplex = Polyhedron(v, backend='normaliz'); simplex
            A 4-dimensional polyhedron in ZZ^4 defined as the convex hull of 5 vertices
            sage: len(simplex.integral_points())
            49

        A rather thin polytope for which the bounding box method would
        be a very bad idea (note this is a rational (non-lattice)
        polytope, so the other backends use the bounding box method)::

            sage: P = Polyhedron(vertices=((0, 0), (178933,37121))) + 1/1000*polytopes.hypercube(2)
            sage: P = Polyhedron(vertices=P.vertices_list(),
            ....:                backend='normaliz')
            sage: len(P.integral_points())
            434

        Finally, the 3-d reflexive polytope number 4078::

            sage: v = [(1,0,0), (0,1,0), (0,0,1), (0,0,-1), (0,-2,1),
            ....:      (-1,2,-1), (-1,2,-2), (-1,1,-2), (-1,-1,2), (-1,-3,2)]
            sage: P = Polyhedron(v, backend='normaliz')
            sage: pts1 = P.integral_points()
            sage: all(P.contains(p) for p in pts1)
            True
            sage: pts2 = LatticePolytope(v).points()                                    # needs palp
            sage: for p in pts1: p.set_immutable()
            sage: set(pts1) == set(pts2)                                                # needs palp
            True

            sage: timeit('Polyhedron(v, backend='normaliz').integral_points()')  # not tested - random
            625 loops, best of 3: 1.41 ms per loop
            sage: timeit('LatticePolytope(v).points()')                          # not tested - random
            25 loops, best of 3: 17.2 ms per loop

        TESTS:

        Test some trivial cases (see :issue:`17937`):

        Empty polyhedron in 1 dimension::

            sage: P = Polyhedron(ambient_dim=1, backend='normaliz')
            sage: P.integral_points()
            ()

        Empty polyhedron in 0 dimensions::

            sage: P = Polyhedron(ambient_dim=0, backend='normaliz')
            sage: P.integral_points()
            ()

        Single point in 1 dimension::

            sage: P = Polyhedron([[3]], backend='normaliz')
            sage: P.integral_points()
            ((3),)

        Single non-integral point in 1 dimension::

            sage: P = Polyhedron([[1/2]], backend='normaliz')
            sage: P.integral_points()
            ()

        Single point in 0 dimensions::

            sage: P = Polyhedron([[]], backend='normaliz')
            sage: P.integral_points()
            ((),)

        A polytope with no integral points (:issue:`22938`)::

            sage: ieqs = [[1, 2, -1, 0], [0, -1, 2, -1], [0, 0, -1, 2],
            ....:         [0, -1, 0, 0], [0, 0, -1, 0],  [0, 0, 0, -1],
            ....:         [-1, -1, -1, -1], [1, 1, 0, 0], [1, 0, 1, 0],
            ....:         [1, 0, 0, 1]]
            sage: P = Polyhedron(ieqs=ieqs, backend='normaliz')
            sage: P.bounding_box()
            ((-3/4, -1/2, -1/4), (-1/2, -1/4, 0))
            sage: P.bounding_box(integral_hull=True)
            (None, None)
            sage: P.integral_points()
            ()

        Check the polytopes from :issue:`22984`::

            sage: base = [[0, 2, 0, -1, 0, 0, 0, 0, 0],
            ....:         [0, 0, 2, 0, -1, 0, 0, 0, 0],
            ....:         [1, -1, 0, 2, -1, 0, 0, 0, 0],
            ....:         [0, 0, -1, -1, 2, -1, 0, 0, 0],
            ....:         [0, 0, 0, 0, -1, 2, -1, 0, 0],
            ....:         [0, 0, 0, 0, 0, -1, 2, -1, 0],
            ....:         [1, 0, 0, 0, 0, 0, -1, 2, -1],
            ....:         [0, 0, 0, 0, 0, 0, 0, -1, 2],
            ....:         [0, -1, 0, 0, 0, 0, 0, 0, 0],
            ....:         [0, 0, -1, 0, 0, 0, 0, 0, 0],
            ....:         [0, 0, 0, -1, 0, 0, 0, 0, 0],
            ....:         [0, 0, 0, 0, -1, 0, 0, 0, 0],
            ....:         [0, 0, 0, 0, 0, -1, 0, 0, 0],
            ....:         [0, 0, 0, 0, 0, 0, -1, 0, 0],
            ....:         [0, 0, 0, 0, 0, 0, 0, -1, 0],
            ....:         [0, 0, 0, 0, 0, 0, 0, 0, -1],
            ....:         [-1, -1, -1, -1, -1, -1, -1, -1, -1]]

            sage: ieqs = base + [
            ....:         [2, 1, 0, 0, 0, 0, 0, 0, 0],
            ....:         [4, 0, 1, 0, 0, 0, 0, 0, 0],
            ....:         [4, 0, 0, 1, 0, 0, 0, 0, 0],
            ....:         [7, 0, 0, 0, 1, 0, 0, 0, 0],
            ....:         [6, 0, 0, 0, 0, 1, 0, 0, 0],
            ....:         [4, 0, 0, 0, 0, 0, 1, 0, 0],
            ....:         [2, 0, 0, 0, 0, 0, 0, 1, 0],
            ....:         [1, 0, 0, 0, 0, 0, 0, 0, 1]]
            sage: P = Polyhedron(ieqs=ieqs, backend='normaliz')
            sage: P.integral_points()
            ((-2, -2, -4, -5, -4, -3, -2, -1),
             (-2, -2, -4, -5, -4, -3, -2, 0),
             (-1, -2, -3, -4, -3, -2, -2, -1),
             (-1, -2, -3, -4, -3, -2, -1, 0),
             (-1, -1, -2, -2, -2, -2, -2, -1),
             (-1, -1, -2, -2, -1, -1, -1, 0),
             (-1, -1, -2, -2, -1, 0, 0, 0),
             (-1, 0, -2, -2, -2, -2, -2, -1),
             (0, -1, -1, -2, -2, -2, -2, -1),
             (0, 0, -1, -1, -1, -1, -1, 0))

            sage: ieqs = base + [
            ....:         [3, 1, 0, 0, 0, 0, 0, 0, 0],
            ....:         [4, 0, 1, 0, 0, 0, 0, 0, 0],
            ....:         [6, 0, 0, 1, 0, 0, 0, 0, 0],
            ....:         [8, 0, 0, 0, 1, 0, 0, 0, 0],
            ....:         [6, 0, 0, 0, 0, 1, 0, 0, 0],
            ....:         [4, 0, 0, 0, 0, 0, 1, 0, 0],
            ....:         [2, 0, 0, 0, 0, 0, 0, 1, 0],
            ....:         [1, 0, 0, 0, 0, 0, 0, 0, 1]]
            sage: P = Polyhedron(ieqs=ieqs, backend='normaliz')
            sage: P.integral_points()
            ((-3, -4, -6, -8, -6, -4, -2, -1),
             (-3, -4, -6, -8, -6, -4, -2, 0),
             (-2, -2, -4, -5, -4, -3, -2, -1),
             (-2, -2, -4, -5, -4, -3, -2, 0),
             (-1, -2, -3, -4, -3, -2, -2, -1),
             (-1, -2, -3, -4, -3, -2, -1, 0),
             (-1, -1, -2, -2, -2, -2, -2, -1),
             (-1, -1, -2, -2, -1, -1, -1, 0),
             (-1, -1, -2, -2, -1, 0, 0, 0),
             (-1, 0, -2, -2, -2, -2, -2, -1),
             (0, -1, -1, -2, -2, -2, -2, -1),
             (0, 0, -1, -1, -1, -1, -1, 0))
        """
    def integral_points_generators(self):
        """
        Return the integral points generators of the polyhedron.

        Every integral point in the polyhedron can be written as a (unique)
        nonnegative linear combination of integral points contained in the three
        defining parts of the polyhedron: the integral points (the compact
        part), the recession cone, and the lineality space.

        OUTPUT:

        A tuple consisting of the integral points, the Hilbert basis of the
        recession cone, and an integral basis for the lineality space.

        EXAMPLES:

        Normaliz gives a nonnegative integer basis of the lineality space::

            sage: P = Polyhedron(backend='normaliz', lines=[[2,2]])
            sage: P.integral_points_generators()
            (((0, 0),), (), ((1, 1),))

        A recession cone generated by two rays::

            sage: C = Polyhedron(backend='normaliz', rays=[[1,2], [2,1]])
            sage: C.integral_points_generators()
            (((0, 0),), ((1, 1), (1, 2), (2, 1)), ())

        Empty polyhedron::

            sage: P = Polyhedron(backend='normaliz')
            sage: P.integral_points_generators()
            ((), (), ())
        """

class Polyhedron_ZZ_normaliz(Polyhedron_QQ_normaliz, Polyhedron_ZZ):
    """
    Polyhedra over `\\ZZ` with normaliz.

    INPUT:

    - ``Vrep`` -- list ``[vertices, rays, lines]`` or ``None``
    - ``Hrep`` -- list ``[ieqs, eqns]`` or ``None``

    EXAMPLES::

        sage: p = Polyhedron(vertices=[(0,0), (1,0), (0,1)],
        ....:                rays=[(1,1)], lines=[],
        ....:                backend='normaliz', base_ring=ZZ)
        sage: TestSuite(p).run()
    """
