from .base_QQ import Polyhedron_QQ as Polyhedron_QQ
from _typeshed import Incomplete
from collections.abc import Generator
from sage.arith.misc import gcd as gcd
from sage.misc.cachefunc import cached_method as cached_method
from sage.modules.free_module_element import vector as vector
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.rational_field import QQ as QQ

class Polyhedron_ZZ(Polyhedron_QQ):
    """
    Base class for Polyhedra over `\\ZZ`.

    TESTS::

        sage: p = Polyhedron([(0,0)], base_ring=ZZ);  p
        A 0-dimensional polyhedron in ZZ^2 defined as the convex hull of 1 vertex
        sage: TestSuite(p).run()
    """
    def __getattribute__(self, name):
        """
        TESTS:

        A lattice polytope does not have a Ehrhart quasipolynomial because it
        is always a polynomial::

            sage: P = polytopes.cube()
            sage: P.__getattribute__(name='ehrhart_quasipolynomial')
            Traceback (most recent call last):
            ...
            AttributeError: ehrhart_quasipolynomial
        """
    def __dir__(self):
        """
        TESTS:

        Removes the Ehrhart quasipolynomial from the list of methods for the
        lattice polyhedron::

            sage: P = polytopes.cube()
            sage: 'ehrhart_polynomial' in P.__dir__()
            True
            sage: 'ehrhart_quasipolynomial' in P.__dir__()
            False
        """
    def is_lattice_polytope(self):
        """
        Return whether the polyhedron is a lattice polytope.

        OUTPUT:

        ``True`` if the polyhedron is compact and has only integral
        vertices, ``False`` otherwise.

        EXAMPLES::

            sage: polytopes.cross_polytope(3).is_lattice_polytope()
            True
            sage: polytopes.regular_polygon(5).is_lattice_polytope()                    # needs sage.rings.number_field
            False

        TESTS:

        Check :issue:`22622`::

            sage: P1 = Polyhedron(vertices = [[1, 0], [0, 1]], rays = [[1, 1]])
            sage: P1.is_lattice_polytope()
            False
        """
    def ehrhart_polynomial(self, engine=None, variable: str = 't', verbose: bool = False, dual=None, irrational_primal=None, irrational_all_primal=None, maxdet=None, no_decomposition=None, compute_vertex_cones=None, smith_form=None, dualization=None, triangulation=None, triangulation_max_height=None, **kwds):
        """
        Return the Ehrhart polynomial of this polyhedron.

        Let `P` be a lattice polytope in `\\RR^d` and define `L(P,t) = \\# (tP
        \\cap \\ZZ^d)`. Then E. Ehrhart proved in 1962 that `L` coincides with a
        rational polynomial of degree `d` for integer `t`. `L` is called the
        *Ehrhart polynomial* of `P`. For more information see the
        :wikipedia:`Ehrhart_polynomial`.

        The Ehrhart polynomial may be computed using either  LattE Integrale
        or Normaliz by setting ``engine``  to 'latte' or 'normaliz' respectively.

        INPUT:

        - ``engine`` -- string; the backend to use. Allowed values are:

          * ``None`` (default); When no input is given the Ehrhart polynomial
            is computed using LattE Integrale (optional)
          * ``'latte'``; use LattE integrale program (optional)
          * ``'normaliz'``; use Normaliz program (optional). The backend of
            ``self`` must be set to 'normaliz'.

        - ``variable`` -- string (default: ``'t'``); the variable in which the
          Ehrhart polynomial should be expressed

        - When the ``engine`` is 'latte' or None, the additional input values are:

          * ``verbose`` -- boolean (default: ``False``); if ``True``, print the
            whole output of the LattE command.

          The following options are passed to the LattE command, for details
          consult `the LattE documentation
          <https://www.math.ucdavis.edu/~latte/software/packages/latte_current/>`__:

          * ``dual`` -- boolean; triangulate and signed-decompose in the dual
            space
          * ``irrational_primal`` -- boolean; triangulate in the dual space,
            signed-decompose in the primal space using irrationalization.
          * ``irrational_all_primal`` -- boolean; triangulate and signed-decompose
            in the primal space using irrationalization.
          * ``maxdet`` -- integer; decompose down to an index (determinant) of
            ``maxdet`` instead of index 1 (unimodular cones).
          * ``no_decomposition`` -- boolean; do not signed-decompose
            simplicial cones.
          * ``compute_vertex_cones`` -- string; either 'cdd' or 'lrs' or '4ti2'
          * ``smith_form`` -- string; either 'ilio' or 'lidia'
          * ``dualization`` -- string; either 'cdd' or '4ti2'
          * ``triangulation`` -- string; 'cddlib', '4ti2' or 'topcom'
          * ``triangulation_max_height`` -- integer; use a uniform distribution of
            height from 1 to this number

        OUTPUT:

        The Ehrhart polynomial as a univariate polynomial in ``variable``
        over a rational field.

        .. SEEALSO::

            :mod:`~sage.interfaces.latte` the interface to LattE Integrale
            `PyNormaliz <https://pypi.org/project/PyNormaliz>`_

        EXAMPLES:

        To start, we find the Ehrhart polynomial of a three-dimensional
        ``simplex``, first using ``engine='latte'``. Leaving the engine
        unspecified sets the ``engine`` to 'latte' by default::

            sage: simplex = Polyhedron(vertices=[(0,0,0),(3,3,3),(-3,2,1),(1,-1,-2)])
            sage: poly = simplex.ehrhart_polynomial(engine = 'latte')  # optional - latte_int
            sage: poly                                                 # optional - latte_int
            7/2*t^3 + 2*t^2 - 1/2*t + 1
            sage: poly(1)                                              # optional - latte_int
            6
            sage: len(simplex.integral_points())
            6
            sage: poly(2)                                              # optional - latte_int
            36
            sage: len((2*simplex).integral_points())
            36

        Now we find the same Ehrhart polynomial, this time using
        ``engine='normaliz'``. To use the Normaliz engine, the ``simplex`` must
        be defined with ``backend='normaliz'``::

            sage: simplex = Polyhedron(vertices=[(0,0,0),(3,3,3),(-3,2,1),(1,-1,-2)], backend='normaliz') # optional - pynormaliz
            sage: poly = simplex.ehrhart_polynomial(engine='normaliz') # optional - pynormaliz
            sage: poly                                                 # optional - pynormaliz
            7/2*t^3 + 2*t^2 - 1/2*t + 1

        If the ``engine='normaliz'``, the backend should be ``'normaliz'``, otherwise
        it returns an error::

            sage: simplex = Polyhedron(vertices=[(0,0,0),(3,3,3),(-3,2,1),(1,-1,-2)])
            sage: simplex.ehrhart_polynomial(engine='normaliz')
            Traceback (most recent call last):
            ...
            TypeError: The polyhedron's backend should be 'normaliz'

        Now we find the Ehrhart polynomials of the unit hypercubes of
        dimensions three through six. They are computed first with
        ``engine='latte'`` and then with ``engine='normaliz'``.
        The degree of the Ehrhart polynomial matches the dimension of the
        hypercube, and the coefficient of the leading monomial equals the
        volume of the unit hypercube::

            sage: # optional - latte_int
            sage: from itertools import product
            sage: def hypercube(d):
            ....:     return Polyhedron(vertices=list(product([0,1],repeat=d)))
            sage: hypercube(3).ehrhart_polynomial()
            t^3 + 3*t^2 + 3*t + 1
            sage: hypercube(4).ehrhart_polynomial()
            t^4 + 4*t^3 + 6*t^2 + 4*t + 1
            sage: hypercube(5).ehrhart_polynomial()
            t^5 + 5*t^4 + 10*t^3 + 10*t^2 + 5*t + 1
            sage: hypercube(6).ehrhart_polynomial()
            t^6 + 6*t^5 + 15*t^4 + 20*t^3 + 15*t^2 + 6*t + 1

            sage: # optional - pynormaliz
            sage: from itertools import product
            sage: def hypercube(d):
            ....:     return Polyhedron(vertices=list(product([0,1],repeat=d)),backend='normaliz')
            sage: hypercube(3).ehrhart_polynomial(engine='normaliz')
            t^3 + 3*t^2 + 3*t + 1
            sage: hypercube(4).ehrhart_polynomial(engine='normaliz')
            t^4 + 4*t^3 + 6*t^2 + 4*t + 1
            sage: hypercube(5).ehrhart_polynomial(engine='normaliz')
            t^5 + 5*t^4 + 10*t^3 + 10*t^2 + 5*t + 1
            sage: hypercube(6).ehrhart_polynomial(engine='normaliz')
            t^6 + 6*t^5 + 15*t^4 + 20*t^3 + 15*t^2 + 6*t + 1

        An empty polyhedron::

            sage: p = Polyhedron(ambient_dim=3, vertices=[])
            sage: p.ehrhart_polynomial()
            0
            sage: parent(_)
            Univariate Polynomial Ring in t over Rational Field

        The polyhedron should be compact::

            sage: C = Polyhedron(rays=[[1,2],[2,1]])
            sage: C.ehrhart_polynomial()
            Traceback (most recent call last):
            ...
            ValueError: Ehrhart polynomial only defined for compact polyhedra

        TESTS:

        The cache of the Ehrhart polynomial is being pickled::

            sage: P = polytopes.cube()
            sage: P.ehrhart_polynomial()  # optional - latte_int
            8*t^3 + 12*t^2 + 6*t + 1
            sage: Q = loads(dumps(P))
            sage: Q.ehrhart_polynomial.is_in_cache()  # optional - latte_int
            True
        """
    @cached_method
    def polar(self):
        """
        Return the polar (dual) polytope.

        The polytope must have the IP-property (see
        :meth:`has_IP_property`), that is, the origin must be an
        interior point. In particular, it must be full-dimensional.

        OUTPUT:

        The polytope whose vertices are the coefficient vectors of the
        inequalities of ``self`` with inhomogeneous term normalized to
        unity.

        EXAMPLES::

            sage: p = Polyhedron(vertices=[(1,0,0),(0,1,0),(0,0,1),(-1,-1,-1)], base_ring=ZZ)
            sage: p.polar()
            A 3-dimensional polyhedron in ZZ^3 defined as the convex hull of 4 vertices
            sage: type(_)
            <class 'sage.geometry.polyhedron.parent.Polyhedra_ZZ_ppl_with_category.element_class'>
            sage: p.polar().base_ring()
            Integer Ring

        TESTS:

        Test that :issue:`28551` is fixed::

            sage: polytopes.cube(backend='normaliz').polar().backend()  # optional - pynormaliz
            'normaliz'
        """
    @cached_method
    def is_reflexive(self):
        """
        A lattice polytope is reflexive if it contains the origin in its interior
        and its polar with respect to the origin is a lattice polytope.

        Equivalently, it is reflexive if it is of the form `\\{x \\in \\mathbb{R}^d: Ax \\leq 1\\}`
        for some integer matrix `A` and `d` the ambient dimension.

        EXAMPLES::

            sage: p = Polyhedron(vertices=[(1,0,0),(0,1,0),(0,0,1),(-1,-1,-1)], base_ring=ZZ)
            sage: p.is_reflexive()
            True
            sage: polytopes.hypercube(4).is_reflexive()
            True
            sage: p = Polyhedron(vertices=[(1,0), (0,2), (-1,0), (0,-1)], base_ring=ZZ)
            sage: p.is_reflexive()
            False
            sage: p = Polyhedron(vertices=[(1,0), (0,2), (-1,0)], base_ring=ZZ)
            sage: p.is_reflexive()
            False

        An error is raised, if the polyhedron is not compact::

            sage: p = Polyhedron(rays=[(1,)], base_ring=ZZ)
            sage: p.is_reflexive()
            Traceback (most recent call last):
            ...
            ValueError: the polyhedron is not compact
        """
    @cached_method
    def has_IP_property(self) -> bool:
        """
        Test whether the polyhedron has the IP property.

        The IP (interior point) property means that

        * ``self`` is compact (a polytope).

        * ``self`` contains the origin as an interior point.

        This implies that

        * ``self`` is full-dimensional.

        * The dual polyhedron is again a polytope (that is, a compact
          polyhedron), though not necessarily a lattice polytope.

        EXAMPLES::

            sage: Polyhedron([(1,1),(1,0),(0,1)], base_ring=ZZ).has_IP_property()
            False
            sage: Polyhedron([(0,0),(1,0),(0,1)], base_ring=ZZ).has_IP_property()
            False
            sage: Polyhedron([(-1,-1),(1,0),(0,1)], base_ring=ZZ).has_IP_property()
            True

        REFERENCES:

        - [PALP]_
        """
    def fibration_generator(self, dim) -> Generator[Incomplete]:
        """
        Generate the lattice polytope fibrations.

        For the purposes of this function, a lattice polytope fiber is
        a sub-lattice polytope. Projecting the plane spanned by the
        subpolytope to a point yields another lattice polytope, the
        base of the fibration.

        INPUT:

        - ``dim`` -- integer; the dimension of the lattice polytope
          fiber

        OUTPUT:

        A generator yielding the distinct lattice polytope fibers of
        given dimension.

        EXAMPLES::

            sage: P = Polyhedron(toric_varieties.P4_11169().fan().rays(), base_ring=ZZ)             # needs palp sage.graphs
            sage: list(P.fibration_generator(2))                                        # needs palp sage.graphs
            [A 2-dimensional polyhedron in ZZ^4 defined as the convex hull of 3 vertices]
        """
    def find_translation(self, translated_polyhedron):
        """
        Return the translation vector to ``translated_polyhedron``.

        INPUT:

        - ``translated_polyhedron`` -- a polyhedron

        OUTPUT:

        A `\\ZZ`-vector that translates ``self`` to
        ``translated_polyhedron``. A :exc:`ValueError` is raised if
        ``translated_polyhedron`` is not a translation of ``self``,
        this can be used to check that two polyhedra are not
        translates of each other.

        EXAMPLES::

            sage: X = polytopes.cube()
            sage: X.find_translation(X + vector([2,3,5]))
            (2, 3, 5)
            sage: X.find_translation(2*X)
            Traceback (most recent call last):
            ...
            ValueError: polyhedron is not a translation of self
        """
    @cached_method
    def minkowski_decompositions(self):
        """
        Return all Minkowski sums that add up to the polyhedron.

        OUTPUT:

        A tuple consisting of pairs `(X,Y)` of `\\ZZ`-polyhedra that
        add up to ``self``. All pairs up to exchange of the summands
        are returned, that is, `(Y,X)` is not included if `(X,Y)`
        already is.

        EXAMPLES::

            sage: square = Polyhedron(vertices=[(0,0),(1,0),(0,1),(1,1)])
            sage: square.minkowski_decompositions()
            ((A 0-dimensional polyhedron in ZZ^2 defined as the convex hull of 1 vertex,
              A 2-dimensional polyhedron in ZZ^2 defined as the convex hull of 4 vertices),
             (A 1-dimensional polyhedron in ZZ^2 defined as the convex hull of 2 vertices,
              A 1-dimensional polyhedron in ZZ^2 defined as the convex hull of 2 vertices))

        Example from http://cgi.di.uoa.gr/~amantzaf/geo/ ::

            sage: Q = Polyhedron(vertices=[(4,0), (6,0), (0,3), (4,3)])
            sage: R = Polyhedron(vertices=[(0,0), (5,0), (8,4), (3,2)])
            sage: (Q+R).minkowski_decompositions()
            ((A 0-dimensional polyhedron in ZZ^2 defined as the convex hull of 1 vertex,
              A 2-dimensional polyhedron in ZZ^2 defined as the convex hull of 7 vertices),
             (A 2-dimensional polyhedron in ZZ^2 defined as the convex hull of 4 vertices,
              A 2-dimensional polyhedron in ZZ^2 defined as the convex hull of 4 vertices),
             (A 1-dimensional polyhedron in ZZ^2 defined as the convex hull of 2 vertices,
              A 2-dimensional polyhedron in ZZ^2 defined as the convex hull of 7 vertices),
             (A 2-dimensional polyhedron in ZZ^2 defined as the convex hull of 5 vertices,
              A 2-dimensional polyhedron in ZZ^2 defined as the convex hull of 4 vertices),
             (A 1-dimensional polyhedron in ZZ^2 defined as the convex hull of 2 vertices,
              A 2-dimensional polyhedron in ZZ^2 defined as the convex hull of 7 vertices),
             (A 2-dimensional polyhedron in ZZ^2 defined as the convex hull of 5 vertices,
              A 2-dimensional polyhedron in ZZ^2 defined as the convex hull of 3 vertices),
             (A 1-dimensional polyhedron in ZZ^2 defined as the convex hull of 2 vertices,
              A 2-dimensional polyhedron in ZZ^2 defined as the convex hull of 7 vertices),
             (A 1-dimensional polyhedron in ZZ^2 defined as the convex hull of 2 vertices,
              A 2-dimensional polyhedron in ZZ^2 defined as the convex hull of 6 vertices))

           sage: [ len(square.dilation(i).minkowski_decompositions())
           ....:   for i in range(6) ]
           [1, 2, 5, 8, 13, 18]
           sage: [ integer_ceil((i^2 + 2*i - 1) / 2) + 1 for i in range(10) ]
           [1, 2, 5, 8, 13, 18, 25, 32, 41, 50]
        """
    def normal_form(self, algorithm: str = 'palp_native', permutation: bool = False):
        '''
        Return the normal form of vertices of the lattice polytope ``self``.

        INPUT:

        - ``algorithm`` -- must be ``\'palp_native\'``, the default

        - ``permutation`` -- boolean (default: ``False``); if ``True``, the permutation
          applied to vertices to obtain the normal form is returned as well

        For more more detail,
        see :meth:`~sage.geometry.lattice_polytope.LatticePolytopeClass.normal_form`.

        EXAMPLES:

        We compute the normal form of the "diamond"::

            sage: d = Polyhedron([(1,0), (0,1), (-1,0), (0,-1)])
            sage: d.vertices()
            (A vertex at (-1, 0),
             A vertex at (0, -1),
             A vertex at (0, 1),
             A vertex at (1, 0))
            sage: d.normal_form()                                                       # needs sage.groups
            [(1, 0), (0, 1), (0, -1), (-1, 0)]
            sage: d.lattice_polytope().normal_form("palp_native")                       # needs sage.groups
            M( 1,  0),
            M( 0,  1),
            M( 0, -1),
            M(-1,  0)
            in 2-d lattice M

        Using ``permutation=True``::

            sage: d.normal_form(permutation=True)                                       # needs sage.groups
            ([(1, 0), (0, 1), (0, -1), (-1, 0)], ())

        It is not possible to compute normal forms for polytopes which do not
        span the space::

            sage: p = Polyhedron([(1,0,0), (0,1,0), (-1,0,0), (0,-1,0)])
            sage: p.normal_form()
            Traceback (most recent call last):
            ...
            ValueError: normal form is not defined for lower-dimensional polyhedra, got
            A 2-dimensional polyhedron in ZZ^3 defined as the convex hull of 4 vertices

        The normal form is also not defined for unbounded polyhedra::

            sage: p = Polyhedron(vertices=[[1, 1]], rays=[[1, 0], [0, 1]], base_ring=ZZ)
            sage: p.normal_form()
            Traceback (most recent call last):
            ...
            ValueError: normal form is not defined for unbounded polyhedra, got
            A 2-dimensional polyhedron in ZZ^2 defined as the convex hull of 1 vertex and 2 rays

        See :issue:`15280` for proposed extensions to these cases.

        TESTS::

            sage: d.normal_form(algorithm=\'palp_fiction\')
            Traceback (most recent call last):
            ...
            ValueError: algorithm must be \'palp_native\'
        '''
