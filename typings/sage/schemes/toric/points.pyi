from _typeshed import Incomplete
from collections.abc import Generator
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.misc_c import prod as prod
from sage.parallel.decorate import Parallel as Parallel
from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing as PolynomialRing

class InfinitePointEnumerator:
    ring: Incomplete
    fan: Incomplete
    def __init__(self, fan, ring) -> None:
        """
        Point enumerator for infinite fields.

        INPUT:

        - ``fan`` -- fan of the toric variety

        - ``ring`` -- infinite base ring over which to enumerate points

        TESTS::

            sage: from sage.schemes.toric.points import InfinitePointEnumerator
            sage: fan = toric_varieties.P2().fan()
            sage: n = InfinitePointEnumerator(fan, QQ)
            sage: ni = iter(n)
            sage: [next(ni) for k in range(10)]
            [(0, 1, 1), (1, 1, 1), (-1, 1, 1), (1/2, 1, 1), (-1/2, 1, 1),
             (2, 1, 1), (-2, 1, 1), (1/3, 1, 1), (-1/3, 1, 1), (3, 1, 1)]

            sage: X = ToricVariety(Fan([], lattice=ZZ^0))
            sage: X.point_set().cardinality()
            1
            sage: X.base_ring().is_finite()
            False
            sage: X.point_set().list()
            ([],)
        """
    def __iter__(self):
        """
        Iterate over the points.

        OUTPUT: iterator over points

        EXAMPLES::

            sage: from sage.schemes.toric.points import InfinitePointEnumerator
            sage: fan = toric_varieties.P2().fan()
            sage: n = InfinitePointEnumerator(fan, QQ)
            sage: ni = iter(n)
            sage: [next(ni) for k in range(5)]
            [(0, 1, 1), (1, 1, 1), (-1, 1, 1), (1/2, 1, 1), (-1/2, 1, 1)]
        """

class NaiveFinitePointEnumerator:
    ring: Incomplete
    fan: Incomplete
    def __init__(self, fan, ring) -> None:
        """
        The naive point enumerator.

        This is very slow.

        INPUT:

        - ``fan`` -- fan of the toric variety

        - ``ring`` -- finite base ring over which to enumerate points

        EXAMPLES::

            sage: from sage.schemes.toric.points import NaiveFinitePointEnumerator
            sage: fan = toric_varieties.P2().fan()
            sage: n = NaiveFinitePointEnumerator(fan, GF(3))
            sage: next(iter(n))
            (0, 0, 1)
        """
    @cached_method
    def rays(self):
        """
        Return all rays (real and virtual).

        OUTPUT: tuple of rays of the fan

        EXAMPLES::

            sage: from sage.schemes.toric.points import NaiveFinitePointEnumerator
            sage: fan = toric_varieties.torus(2).fan()
            sage: fan.rays()
            Empty collection
            in 2-d lattice N
            sage: n = NaiveFinitePointEnumerator(fan, GF(3))
            sage: n.rays()
            N(1, 0),
            N(0, 1)
            in 2-d lattice N
        """
    @cached_method
    def units(self):
        """
        Return the units in the base field.

        EXAMPLES::

            sage: P2 = toric_varieties.P2(base_ring=GF(5))
            sage: ne = P2.point_set()._naive_enumerator()
            sage: ne.units()
            (1, 2, 3, 4)
        """
    @cached_method
    def roots(self, n):
        """
        Return the `n`-th roots in the base field.

        INPUT:

        - ``n`` -- integer

        OUTPUT:

        Tuple containing all `n`-th roots (not only the primitive
        ones). In particular, 1 is included.

        EXAMPLES::

            sage: P2 = toric_varieties.P2(base_ring=GF(5))
            sage: ne = P2.point_set()._naive_enumerator()
            sage: ne.roots(2)
            (1, 4)
            sage: ne.roots(3)
            (1,)
            sage: ne.roots(4)
            (1, 2, 3, 4)
        """
    @cached_method
    def rescalings(self):
        """
        Return the rescalings of homogeneous coordinates.

        OUTPUT:

        A tuple containing all points that are equivalent to
        `[1:1:\\dots:1]`, the distinguished point of the big torus
        orbit.

        EXAMPLES::

            sage: P2_123 = toric_varieties.P2_123(base_ring=GF(5))
            sage: ni = P2_123.point_set()._naive_enumerator()
            sage: ni.rescalings()
            ((1, 1, 1), (1, 4, 4), (4, 2, 3), (4, 3, 2))

            sage: dP8 = toric_varieties.dP8(base_ring=GF(3))
            sage: ni = dP8.point_set()._naive_enumerator()
            sage: ni.rescalings()
            ((1, 1, 1, 1), (1, 2, 2, 2), (2, 1, 2, 1), (2, 2, 1, 2))

            sage: P1xP1 = toric_varieties.P1xP1(base_ring=GF(3))
            sage: ni = P1xP1.point_set()._naive_enumerator()
            sage: ni.rescalings()
            ((1, 1, 1, 1), (1, 1, 2, 2), (2, 2, 1, 1), (2, 2, 2, 2))
        """
    def orbit(self, point):
        """
        Return the orbit of homogeneous coordinates under rescalings.

        OUTPUT: the set of all homogeneous coordinates that are equivalent to ``point``

        EXAMPLES::

            sage: P2_123 = toric_varieties.P2_123(base_ring=GF(7))
            sage: ne = P2_123.point_set()._naive_enumerator()
            sage: sorted(ne.orbit([1, 0, 0]))
            [(1, 0, 0), (2, 0, 0), (4, 0, 0)]
            sage: sorted(ne.orbit([0, 1, 0]))
            [(0, 1, 0), (0, 6, 0)]
            sage: sorted(ne.orbit([0, 0, 1]))
            [(0, 0, 1), (0, 0, 2), (0, 0, 3), (0, 0, 4), (0, 0, 5), (0, 0, 6)]
            sage: sorted(ne.orbit([1, 1, 0]))
            [(1, 1, 0), (1, 6, 0), (2, 1, 0), (2, 6, 0), (4, 1, 0), (4, 6, 0)]
        """
    def cone_iter(self) -> Generator[Incomplete, Incomplete]:
        """
        Iterate over all cones of the fan.

        OUTPUT:

        Iterator over the cones, starting with the high-dimensional
        ones.

        EXAMPLES::

            sage: dP6 = toric_varieties.dP6(base_ring=GF(11))
            sage: ne = dP6.point_set()._naive_enumerator()
            sage: for cone in ne.cone_iter():
            ....:     print(cone.ambient_ray_indices())
            (0, 1)
            (1, 2)
            (2, 3)
            (3, 4)
            (4, 5)
            (0, 5)
            (0,)
            (1,)
            (2,)
            (3,)
            (4,)
            (5,)
            ()
        """
    def coordinate_iter(self) -> Generator[Incomplete]:
        """
        Iterate over all distinct homogeneous coordinates.

        This method does NOT identify homogeneous coordinates that are
        equivalent by a homogeneous rescaling.

        OUTPUT: an iterator over the points

        EXAMPLES::

            sage: P2 = toric_varieties.P2(base_ring=GF(2))
            sage: ni = P2.point_set()._naive_enumerator()
            sage: list(ni.coordinate_iter())
            [(0, 0, 1), (1, 0, 0), (0, 1, 0), (0, 1, 1),
             (1, 0, 1), (1, 1, 0), (1, 1, 1)]

            sage: P1xP1 = toric_varieties.P1xP1(base_ring=GF(2))
            sage: ni = P1xP1.point_set()._naive_enumerator()
            sage: list(ni.coordinate_iter())
            [(0, 1, 0, 1), (1, 0, 0, 1), (1, 0, 1, 0),
             (0, 1, 1, 0), (0, 1, 1, 1), (1, 0, 1, 1),
             (1, 1, 0, 1), (1, 1, 1, 0), (1, 1, 1, 1)]

        TESTS::

            sage: V = ToricVariety(Fan([Cone([(1,1)])]), base_ring=GF(3))
            sage: ni = V.point_set()._naive_enumerator()
            sage: list(ni.coordinate_iter())
            [(0, 1), (0, 2), (1, 1), (1, 2), (2, 1), (2, 2)]
        """
    def __iter__(self):
        """
        Iterate over the distinct points of the toric variety.

        This function does identify orbits under the homogeneous
        rescalings, and returns precisely one representative per
        orbit.

        OUTPUT: an iterator over points

        EXAMPLES::

            sage: P2 = toric_varieties.P2(base_ring=GF(2))
            sage: ni = P2.point_set()._naive_enumerator()
            sage: list(ni)
            [(0, 0, 1), (1, 0, 0), (0, 1, 0), (0, 1, 1),
             (1, 0, 1), (1, 1, 0), (1, 1, 1)]

            sage: P1xP1 = toric_varieties.P1xP1(base_ring=GF(3))
            sage: ni = P1xP1.point_set()._naive_enumerator()
            sage: list(ni)
            [(0, 1, 0, 1), (1, 0, 0, 1), (1, 0, 1, 0), (0, 1, 1, 0),
             (0, 1, 1, 1), (0, 1, 1, 2), (1, 0, 1, 1), (1, 0, 1, 2),
             (1, 1, 0, 1), (1, 2, 0, 1), (1, 1, 1, 0), (1, 2, 1, 0),
             (1, 1, 1, 1), (1, 1, 1, 2), (1, 2, 1, 1), (1, 2, 1, 2)]
        """

class FiniteFieldPointEnumerator(NaiveFinitePointEnumerator):
    @cached_method
    def multiplicative_generator(self):
        """
        Return the multiplicative generator of the finite field.

        OUTPUT: a finite field element

        EXAMPLES::

            sage: point_set = toric_varieties.P2(base_ring=GF(5^2, 'a')).point_set()    # needs sage.rings.finite_rings
            sage: ffe = point_set._finite_field_enumerator()                            # needs sage.rings.finite_rings
            sage: ffe.multiplicative_generator()                                        # needs sage.rings.finite_rings
            a
        """
    @cached_method
    def multiplicative_group_order(self): ...
    @cached_method
    def root_generator(self, n):
        """
        Return a generator for :meth:`roots`.

        INPUT:

        - ``n`` -- integer

        OUTPUT: a multiplicative generator for :meth:`roots`

        EXAMPLES::

            sage: point_set = toric_varieties.P2(base_ring=GF(5)).point_set()
            sage: ffe = point_set._finite_field_enumerator()
            sage: ffe.root_generator(2)
            4
            sage: ffe.root_generator(3)
            1
            sage: ffe.root_generator(4)
            2

        TESTS::

            sage: for p in primes(10):                                                  # needs sage.rings.finite_rings
            ....:     for k in range(1, 5):
            ....:         F = GF(p^k, 'a')
            ....:         N = F.cardinality() - 1
            ....:         ffe = point_set._finite_field_enumerator(F)
            ....:         assert N == ffe.multiplicative_group_order()
            ....:         for n in N.divisors():
            ....:             x = ffe.root_generator(n)
            ....:             assert set(x**i for i in range(N)) == set(ffe.roots(n))
        """
    def log(self, z):
        """
        Return the component-wise log of ``z``.

        INPUT:

        - ``z`` -- list/tuple/iterable of nonzero finite field
          elements

        OUTPUT:

        Tuple of integers. The logarithm with base the
        :meth:`multiplicative_generator`.

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: F.<a> = GF(5^2)
            sage: point_set = toric_varieties.P2_123(base_ring=F).point_set()
            sage: ffe = point_set._finite_field_enumerator()
            sage: z = tuple(a^i for i in range(25));  z
            (1, a, a + 3, 4*a + 3, 2*a + 2, 4*a + 1, 2, 2*a, 2*a + 1, 3*a + 1,
             4*a + 4, 3*a + 2, 4, 4*a, 4*a + 2, a + 2, 3*a + 3, a + 4, 3, 3*a,
             3*a + 4, 2*a + 4, a + 1, 2*a + 3, 1)
            sage: ffe.log(z)
            (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16,
             17, 18, 19, 20, 21, 22, 23, 0)
            sage: ffe.exp(ffe.log(z)) == z
            True
            sage: ffe.log(ffe.exp(range(24))) == tuple(range(24))
            True
        """
    def exp(self, powers):
        """
        Return the component-wise exp of ``z``.

        INPUT:

        - ``powers`` -- list/tuple/iterable of integers

        OUTPUT:

        Tuple of finite field elements. The powers of the
        :meth:`multiplicative_generator`.

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: F.<a> = GF(5^2)
            sage: point_set = toric_varieties.P2_123(base_ring=F).point_set()
            sage: ffe = point_set._finite_field_enumerator()
            sage: powers = list(range(24))
            sage: ffe.exp(powers)
            (1, a, a + 3, 4*a + 3, 2*a + 2, 4*a + 1, 2, 2*a, 2*a + 1, 3*a + 1,
             4*a + 4, 3*a + 2, 4, 4*a, 4*a + 2, a + 2, 3*a + 3, a + 4, 3, 3*a,
             3*a + 4, 2*a + 4, a + 1, 2*a + 3)
            sage: ffe.log(ffe.exp(powers)) == tuple(powers)
            True
        """
    @cached_method
    def rescaling_log_generators(self):
        """
        Return the log generators of :meth:`rescalings`.

        OUTPUT:

        A tuple containing the logarithms (see :meth:`log`) of the
        generators of the multiplicative group of :meth:`rescalings`.

        EXAMPLES::

            sage: point_set = toric_varieties.P2_123(base_ring=GF(5)).point_set()
            sage: ffe = point_set._finite_field_enumerator()
            sage: ffe.rescalings()
            ((1, 1, 1), (1, 4, 4), (4, 2, 3), (4, 3, 2))
            sage: list(map(ffe.log, ffe.rescalings()))
            [(0, 0, 0), (0, 2, 2), (2, 1, 3), (2, 3, 1)]
            sage: ffe.rescaling_log_generators()
            ((2, 3, 1),)
        """
    def cone_points_iter(self) -> Generator[Incomplete]:
        """
        Iterate over the open torus orbits and yield distinct points.

        OUTPUT:

        For each open torus orbit (cone): A triple consisting of the
        cone, the nonzero homogeneous coordinates in that orbit (list
        of integers), and the nonzero log coordinates of distinct
        points as a cokernel.

        EXAMPLES::

            sage: fan = NormalFan(ReflexivePolytope(2, 0))
            sage: X = ToricVariety(fan, base_ring=GF(7))
            sage: point_set = X.point_set()
            sage: ffe = point_set._finite_field_enumerator()
            sage: cpi = ffe.cone_points_iter()
            sage: cone, nonzero_points, cokernel = list(cpi)[5]
            sage: cone
            1-d cone of Rational polyhedral fan in 2-d lattice N
            sage: cone.ambient_ray_indices()
            (2,)
            sage: nonzero_points
            [0, 1]
            sage: cokernel
            Finitely generated module V/W over Integer Ring with invariants (2)
            sage: list(cokernel)
            [(0), (1)]
            sage: [p.lift() for p in cokernel]
            [(0, 0), (0, 1)]
        """
    def __iter__(self):
        """
        Iterate over the distinct points of the toric variety.

        This function does identify orbits under the homogeneous
        rescalings, and returns precisely one representative per
        orbit.

        OUTPUT: iterator over points

        EXAMPLES::

            sage: point_set = toric_varieties.P2(base_ring=GF(2)).point_set()
            sage: ffe = point_set._finite_field_enumerator()
            sage: list(ffe)
            [(0, 0, 1), (1, 0, 0), (0, 1, 0), (0, 1, 1),
             (1, 0, 1), (1, 1, 0), (1, 1, 1)]

            sage: fan = NormalFan(ReflexivePolytope(2, 0))
            sage: X = ToricVariety(fan, base_ring=GF(7))
            sage: point_set = X.point_set()
            sage: ffe = point_set._finite_field_enumerator()
            sage: list(ffe)
            [(1, 0, 0), (0, 1, 0), (0, 0, 1), (0, 1, 1), (0, 1, 3), (1, 0, 1),
             (1, 0, 3), (1, 1, 0), (1, 3, 0), (1, 1, 1), (1, 1, 3), (1, 1, 2),
             (1, 1, 6), (1, 1, 4), (1, 1, 5), (1, 3, 2), (1, 3, 6), (1, 3, 4),
             (1, 3, 5), (1, 3, 1), (1, 3, 3)]
            sage: set(point_set._naive_enumerator()) == set(ffe)
            True
        """
    def cardinality(self):
        """
        Return the cardinality of the point set.

        OUTPUT: integer; the number of points

        EXAMPLES::

            sage: fan = NormalFan(ReflexivePolytope(2, 0))
            sage: X = ToricVariety(fan, base_ring=GF(7))
            sage: point_set = X.point_set()
            sage: ffe = point_set._finite_field_enumerator()
            sage: ffe.cardinality()
            21
        """

class NaiveSubschemePointEnumerator:
    ambient: Incomplete
    polynomials: Incomplete
    def __init__(self, polynomials, ambient) -> None:
        """
        Point enumerator for algebraic subschemes of toric varieties.

        INPUT:

        - ``polynomials`` -- list/tuple/iterable of polynomials; the
          defining polynomials

        - ``ambient`` -- enumerator for ambient space points

        TESTS::

            sage: P2.<x,y,z> = toric_varieties.P2()
            sage: from sage.schemes.toric.points import NaiveSubschemePointEnumerator
            sage: ne = NaiveSubschemePointEnumerator(
            ....:    [x^2 + y^2 - 2*z^2], P2.point_set()._enumerator())
            sage: next(iter(ne))
            (1, 1, 1)
        """
    def __iter__(self):
        """
        Iterate over the distinct points of the toric variety.

        This function does identify orbits under the homogeneous
        rescalings, and returns precisely one representative per
        orbit.

        OUTPUT:

        Iterator over points. Each point is represented by a tuple of
        homogeneous coordinates.

        EXAMPLES::

            sage: P2.<x,y,z> = toric_varieties.P2()
            sage: from sage.schemes.toric.points import NaiveSubschemePointEnumerator
            sage: ne = NaiveSubschemePointEnumerator(
            ....:    [x^2 + y^2 - 2*z^2], P2.point_set()._enumerator())
            sage: next(iter(ne))
            (1, 1, 1)
        """

class FiniteFieldSubschemePointEnumerator(NaiveSubschemePointEnumerator):
    def inhomogeneous_equations(self, ring, nonzero_coordinates, cokernel):
        """
        Inhomogenize the defining polynomials.

        INPUT:

        - ``ring`` -- the polynomial ring for inhomogeneous
          coordinates

        - ``nonzero_coordinates`` -- list of integers. The indices of
          the nonzero homogeneous coordinates in the patch

        - ``cokernel`` -- the logs of the nonzero coordinates of
          all distinct points as a cokernel. See
          :meth:`FiniteFieldPointEnumerator.cone_points_iter`.

        EXAMPLES::

            sage: R.<s> = QQ[]
            sage: P2.<x,y,z> = toric_varieties.P2(base_ring=GF(7))
            sage: X = P2.subscheme([x^3 + 2*y^3 + 3*z^3, x*y*z + x*y^2])
            sage: point_set = X.point_set()
            sage: ffe = point_set._enumerator()
            sage: cone, nonzero_coordinates, cokernel = list(ffe.ambient.cone_points_iter())[5]
            sage: cone.ambient_ray_indices(), nonzero_coordinates
            ((2,), [0, 1])
            sage: ffe.inhomogeneous_equations(R, nonzero_coordinates, cokernel)
            [2*s^3 + 1, s^2]
        """
    def solutions_serial(self, inhomogeneous_equations, log_range) -> Generator[Incomplete]:
        """
        Iterate over solutions in a range.

        INPUT:

        - ``inhomogeneous_equations`` -- list/tuple/iterable of
          inhomogeneous equations (i.e. output from
          :meth:`inhomogeneous_equations`).

        - ``log_range`` -- list/tuple/iterable of integer ranges. One
          for each inhomogeneous coordinate. The logarithms of the
          homogeneous coordinates.

        OUTPUT:

        All solutions (as tuple of log inhomogeneous coordinates) in
        the Cartesian product of the ranges.

        EXAMPLES::

            sage: R.<s> = GF(7)[]
            sage: P2.<x,y,z> = toric_varieties.P2(base_ring=GF(7))
            sage: X = P2.subscheme(1)
            sage: point_set = X.point_set()
            sage: ffe = point_set._enumerator()
            sage: ffe.solutions_serial([s^2 - 1, s^6 - s^2], [range(6)])
            <generator object ...solutions_serial at 0x...>
            sage: list(_)
            [(0,), (3,)]
        """
    def solutions(self, inhomogeneous_equations, log_range) -> Generator[Incomplete, None, Incomplete]:
        """
        Parallel version of :meth:`solutions_serial`.

        INPUT/OUTPUT:

        Same as :meth:`solutions_serial`, except that the output
        points are in random order. Order depends on the number of
        processors and relative speed of separate processes.

        EXAMPLES::

            sage: R.<s> = GF(7)[]
            sage: P2.<x,y,z> = toric_varieties.P2(base_ring=GF(7))
            sage: X = P2.subscheme(1)
            sage: point_set = X.point_set()
            sage: ffe = point_set._enumerator()
            sage: ffe.solutions([s^2 - 1, s^6 - s^2], [range(6)])
            <generator object ...solutions at 0x...>
            sage: sorted(_)
            [(0,), (3,)]
        """
    def homogeneous_coordinates(self, log_t, nonzero_coordinates, cokernel):
        """
        Convert the log of inhomogeneous coordinates back to homogeneous coordinates.

        INPUT:

        - ``log_t`` -- log of inhomogeneous coordinates of a point

        - ``nonzero_coordinates`` -- the nonzero homogeneous
          coordinates in the patch

        - ``cokernel`` -- the logs of the nonzero coordinates of
          all distinct points as a cokernel. See
          :meth:`FiniteFieldPointEnumerator.cone_points_iter`.

        OUTPUT: the same point, but as a tuple of homogeneous coordinates

        EXAMPLES::

            sage: P2.<x,y,z> = toric_varieties.P2(base_ring=GF(7))
            sage: X = P2.subscheme([x^3 + 2*y^3 + 3*z^3, x*y*z + x*y^2])
            sage: point_set = X.point_set()
            sage: ffe = point_set._enumerator()
            sage: cone, nonzero_coordinates, cokernel = list(ffe.ambient.cone_points_iter())[5]
            sage: cone.ambient_ray_indices(), nonzero_coordinates
            ((2,), [0, 1])
            sage: ffe.homogeneous_coordinates([0], nonzero_coordinates, cokernel)
            (1, 1, 0)
            sage: ffe.homogeneous_coordinates([1], nonzero_coordinates, cokernel)
            (1, 3, 0)
            sage: ffe.homogeneous_coordinates([2], nonzero_coordinates, cokernel)
            (1, 2, 0)
        """
    def __iter__(self):
        """
        Iterate over the distinct points of the toric variety.

        This function does identify orbits under the homogeneous
        rescalings, and returns precisely one representative per
        orbit.

        OUTPUT:

        Iterator over points. Each point is represented by a tuple of
        homogeneous coordinates.

        EXAMPLES::

            sage: P2.<x,y,z> = toric_varieties.P2(base_ring=GF(7))
            sage: X = P2.subscheme([x^3 + 2*y^3 + 3*z^3, x*y*z + x*y^2])
            sage: point_set = X.point_set()
            sage: ffe = point_set._enumerator()
            sage: list(ffe)   # indirect doctest
            [(1, 1, 6), (1, 2, 5), (1, 4, 3)]
        """
    def cardinality(self):
        """
        Return the cardinality of the point set.

        OUTPUT: integer; the number of points

        EXAMPLES::

            sage: fan = NormalFan(ReflexivePolytope(2, 0))
            sage: X.<u,v,w> = ToricVariety(fan, base_ring=GF(7))
            sage: Y = X.subscheme(u^3 + v^3 + w^3 + u*v*w)
            sage: point_set = Y.point_set()
            sage: list(point_set)                                                       # needs fpylll
            [[0 : 1 : 3],
             [1 : 0 : 3],
             [1 : 3 : 0],
             [1 : 1 : 6],
             [1 : 1 : 4],
             [1 : 3 : 2],
             [1 : 3 : 5]]
            sage: ffe = point_set._enumerator()                                         # needs fpylll
            sage: ffe.cardinality()                                                     # needs fpylll
            7
        """
