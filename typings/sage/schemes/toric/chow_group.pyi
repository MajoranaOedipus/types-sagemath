from _typeshed import Incomplete
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.fast_methods import WithEqualityById as WithEqualityById
from sage.misc.flatten import flatten as flatten
from sage.modules.fg_pid.fgp_element import FGP_Element as FGP_Element
from sage.modules.fg_pid.fgp_module import FGP_Module_class as FGP_Module_class
from sage.modules.free_module import FreeModule as FreeModule
from sage.rings.infinity import Infinity as Infinity
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.rational_field import QQ as QQ
from sage.schemes.toric.divisor import ToricDivisor_generic as ToricDivisor_generic
from sage.schemes.toric.variety import ToricVariety_field as ToricVariety_field
from sage.structure.factory import UniqueFactory as UniqueFactory
from sage.structure.sage_object import SageObject as SageObject

class ChowCycle(FGP_Element):
    """
    The elements of the Chow group.

    .. WARNING::

        Do not construct :class:`ChowCycle` objects manually. Instead,
        use the parent :class:`ChowGroup<ChowGroup_class>` to obtain
        generators or Chow cycles corresponding to cones of the fan.

    EXAMPLES::

        sage: P2 = toric_varieties.P2()
        sage: A = P2.Chow_group()
        sage: A.gens()
        (( 0 | 0 | 1 ), ( 0 | 1 | 0 ), ( 1 | 0 | 0 ))
        sage: cone = P2.fan(1)[0]
        sage: A(cone)
        ( 0 | 1 | 0 )
        sage: A( Cone([(1,0)]) )
        ( 0 | 1 | 0 )
    """
    def __init__(self, parent, v, check: bool = True) -> None:
        """
        Construct a :class:`ChowCycle`.

        INPUT:

        - ``parent`` -- a :class:`ChowGroup_class`

        - ``v`` -- a vector in the covering module, that is, with one
          entry for each cone of the toric variety

        - ``check`` -- boolean (default: ``True``); verify that ``v``
          is in the covering module. Set to ``False`` if you want to
          initialize from a coordinate vector.

        TESTS::

            sage: P2 = toric_varieties.P2()
            sage: A = P2.Chow_group()
            sage: from sage.schemes.toric.chow_group import ChowCycle
            sage: ChowCycle(A, (0,1,2,3,11,12,13), check=False)
            ( 36 | 6 | 0 )
        """
    @cached_method
    def degree(self) -> int:
        """
        Return the degree of the Chow cycle.

        OUTPUT:

        Integer. The complex dimension of the subvariety representing
        the Chow cycle.

        This raises a :exc:`ValueError` if the Chow cycle is a
        sum of mixed degree cycles.

        EXAMPLES::

            sage: P2 = toric_varieties.P2()
            sage: A = P2.Chow_group()
            sage: [ a.degree() for a in A.gens() ]
            [2, 1, 0]
        """
    def project_to_degree(self, degree):
        """
        Project a (mixed-degree) Chow cycle to the given ``degree``.

        INPUT:

        - ``degree`` -- integer; the degree to project to

        OUTPUT:

        The projection of the Chow class to the given degree as a new
        :class:`ChowCycle` of the same Chow group.

        EXAMPLES::

            sage: A = toric_varieties.P2().Chow_group()
            sage: cycle = 10*A.gen(0) + 11*A.gen(1) + 12*A.gen(2); cycle
            ( 12 | 11 | 10 )
            sage: cycle.project_to_degree(2)
            ( 0 | 0 | 10 )
        """
    def count_points(self):
        """
        Return the number of points in the Chow cycle.

        OUTPUT:

        An element of ``self.base_ring()``, which is usually
        `\\ZZ`. The number of points in the Chow cycle.

        EXAMPLES::

            sage: P2 = toric_varieties.P2()
            sage: A = P2.Chow_group()
            sage: a = 5*A.gen(2) + 7*A.gen(1); a
            ( 5 | 7 | 0 )
            sage: a.count_points()
            5

        In the case of a smooth complete toric variety, the Chow
        (homology) groups are Poincaré dual to the integral cohomology
        groups. Here is such a smooth example::

            sage: D = P2.divisor(1)
            sage: a = D.Chow_cycle()
            sage: aD = a.intersection_with_divisor(D)
            sage: aD.count_points()
            1
            sage: P2.integrate(aD.cohomology_class())                                   # needs sage.libs.singular
            1

        For toric varieties with at most orbifold singularities, the
        isomorphism only holds over `\\QQ`. But the normalization of
        the integral is still chosen such that the intersection
        numbers (which are potentially rational) computed both ways
        agree::

            sage: P1xP1_Z2 = toric_varieties.P1xP1_Z2()
            sage: Dt = P1xP1_Z2.divisor(1);  Dt
            V(t)
            sage: Dy = P1xP1_Z2.divisor(3);  Dy
            V(y)
            sage: Dt.Chow_cycle(QQ).intersection_with_divisor(Dy).count_points()
            1/2
            sage: P1xP1_Z2.integrate(Dt.cohomology_class() * Dy.cohomology_class())     # needs sage.libs.singular
            1/2
        """
    def intersection_with_divisor(self, divisor):
        """
        Intersect the Chow cycle with ``divisor``.

        See Chapter 5.1 of [Ful1993]_ for a description of the toric algorithm.

        INPUT:

        - ``divisor`` -- a :class:`ToricDivisor
          <sage.schemes.toric.divisor.ToricDivisor_generic>`
          that can be moved away from the Chow cycle. For example, any
          Cartier divisor. See also :meth:`ToricDivisor.move_away_from
          <sage.schemes.toric.divisor.ToricDivisor_generic.move_away_from>`.

        OUTPUT:

        A new :class:`ChowCycle`. If the divisor is not Cartier then
        this method potentially raises a :exc:`ValueError`, indicating
        that the divisor cannot be made transversal to the Chow cycle.

        EXAMPLES::

            sage: dP6 = toric_varieties.dP6()
            sage: cone = dP6.fan().cone_containing(2); cone
            1-d cone of Rational polyhedral fan in 2-d lattice N
            sage: D = dP6.divisor(cone); D
            V(y)
            sage: A = dP6.Chow_group()
            sage: A(cone)
            ( 0 | 0, 0, 1, 0 | 0 )
            sage: intersection = A(cone).intersection_with_divisor(D); intersection
            ( -1 | 0, 0, 0, 0 | 0 )
            sage: intersection.count_points()
            -1

        You can do the same computation over the rational Chow group
        since there is no torsion in this case::

            sage: A_QQ = dP6.Chow_group(base_ring=QQ)
            sage: A_QQ(cone)
            ( 0 | 0, 0, 0, 1 | 0 )
            sage: intersection_QQ = A_QQ(cone).intersection_with_divisor(D); intersection
            ( -1 | 0, 0, 0, 0 | 0 )
            sage: intersection_QQ.count_points()
            -1
            sage: type(intersection_QQ.count_points())
            <... 'sage.rings.rational.Rational'>
            sage: type(intersection.count_points())
            <... 'sage.rings.integer.Integer'>

        TESTS:

        The relations are the Chow cycles rationally equivalent to the
        zero cycle. Their intersection with any divisor must be the zero cycle::

            sage: [ r.intersection_with_divisor(D) for r in dP6.Chow_group().relation_gens() ]
            [( 0 | 0, 0, 0, 0 | 0 ), ( 0 | 0, 0, 0, 0 | 0 ),
             ( 0 | 0, 0, 0, 0 | 0 ), ( 0 | 0, 0, 0, 0 | 0 ),
             ( 0 | 0, 0, 0, 0 | 0 ), ( 0 | 0, 0, 0, 0 | 0 ),
             ( 0 | 0, 0, 0, 0 | 0 )]
            sage: [ r.intersection_with_divisor(D).lift() for r in dP6.Chow_group().relation_gens() ]
            [(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
             (0, 0, 0, 0, 0, 0, 0, 0, 1, -1, 0, 0, 0),
             (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
             (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
             (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
             (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
             (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)]
        """
    def cohomology_class(self):
        """
        Return the (Poincaré-dual) cohomology class.

        Consider a simplicial cone of the fan, that is, a
        `d`-dimensional cone spanned by `d` rays. Take the product of
        the corresponding `d` homogeneous coordinates. This monomial
        represents a cohomology classes of the toric variety `X`, see
        :meth:`~sage.schemes.toric.variety.ToricVariety_field.cohomology_ring`.
        Its cohomological degree is `2d`, which is the same degree as
        the Poincaré-dual of the (real) `\\dim(X)-2d`-dimensional torus
        orbit associated to the simplicial cone. By linearity, we can
        associate a cohomology class to each Chow cycle of a
        simplicial toric variety.

        If the toric variety is compact and smooth, the associated
        cohomology class actually is the Poincaré dual (over the
        integers) of the Chow cycle. In particular, integrals of dual
        cohomology classes perform intersection computations.

        If the toric variety is compact and has at most orbifold
        singularities, the torsion parts in cohomology and the Chow
        group can differ. But they are still isomorphic as rings over
        the rationals. Moreover, the normalization of integration
        (:meth:`volume_class
        <sage.schemes.toric.variety.ToricVariety_field.volume_class>`)
        and :meth:`count_points` are chosen to agree.

        OUTPUT:

        The
        :class:`~sage.schemes.toric.variety.CohomologyClass`
        which is associated to the Chow cycle.

        If the toric variety is not simplicial, that is, has worse
        than orbifold singularities, there is no way to associate a
        cohomology class of the correct degree. In this case,
        :meth:`cohomology_class` raises a :exc:`ValueError`.

        EXAMPLES::

            sage: # needs sage.libs.singular
            sage: dP6 = toric_varieties.dP6()
            sage: cone = dP6.fan().cone_containing(2,3)
            sage: HH = dP6.cohomology_ring()
            sage: A = dP6.Chow_group()
            sage: HH(cone)
            [-w^2]
            sage: A(cone)
            ( 1 | 0, 0, 0, 0 | 0 )
            sage: A(cone).cohomology_class()
            [-w^2]

        Here is an example of a toric variety with orbifold
        singularities, where we can also use the isomorphism with the
        rational cohomology ring::

            sage: # needs sage.libs.singular
            sage: WP4 = toric_varieties.P4_11169()
            sage: A = WP4.Chow_group()
            sage: HH = WP4.cohomology_ring()
            sage: cone3d = Cone([(0,0,1,0), (0,0,0,1), (-9,-6,-1,-1)])
            sage: A(cone3d)
            ( 0 | -1 | 0 | 0 | 0 )
            sage: HH(cone3d)
            [3*z4^3]
            sage: D = -WP4.K()  # the anticanonical divisor
            sage: A(D)
            ( 0 | 0 | 0 | -18 | 0 )
            sage: HH(D)
            [18*z4]
            sage: WP4.integrate( A(cone3d).cohomology_class() * D.cohomology_class() )
            1
            sage: WP4.integrate( HH(cone3d) * D.cohomology_class() )
            1
            sage: A(cone3d).intersection_with_divisor(D).count_points()
            1
        """

class ChowGroupFactory(UniqueFactory):
    """
    Factory for :class:`ChowGroup_class`.
    """
    def create_key_and_extra_args(self, toric_variety, base_ring=..., check: bool = True):
        """
        Create a key that uniquely determines the :class:`ChowGroup_class`.

        INPUT:

        - ``toric_variety`` -- a toric variety

        - ``base_ring`` -- either `\\ZZ` (default) or `\\QQ`; the
          coefficient ring of the Chow group

        - ``check`` -- boolean (default: ``True``)

        EXAMPLES::

            sage: from sage.schemes.toric.chow_group import *
            sage: P2 = toric_varieties.P2()
            sage: ChowGroup(P2, ZZ, check=True) == ChowGroup(P2, ZZ, check=False)   # indirect doctest
            True
        """
    def create_object(self, version, key, **extra_args):
        """
        Create a :class:`ChowGroup_class`.

        INPUT:

        - ``version`` -- object version; currently not used

        - ``key`` -- a key created by :meth:`create_key_and_extra_args`

        - ``**extra_args`` -- currently not used

        EXAMPLES::

            sage: from sage.schemes.toric.chow_group import *
            sage: P2 = toric_varieties.P2()
            sage: ChowGroup(P2)    # indirect doctest
            Chow group of 2-d CPR-Fano toric variety covered by 3 affine patches
        """

ChowGroup: Incomplete

class ChowGroup_class(FGP_Module_class, WithEqualityById):
    """
    The Chow group of a toric variety.

    EXAMPLES::

        sage: P2 = toric_varieties.P2()
        sage: from sage.schemes.toric.chow_group import ChowGroup_class
        sage: A = ChowGroup_class(P2,ZZ,True);  A
        Chow group of 2-d CPR-Fano toric variety covered by 3 affine patches
        sage: A.an_element()
        ( 0 | 0 | 1 )
    """
    Element = ChowCycle
    def __init__(self, toric_variety, base_ring, check) -> None:
        """
        EXAMPLES::

            sage: from sage.schemes.toric.chow_group import *
            sage: P2 = toric_varieties.P2()
            sage: A = ChowGroup_class(P2,ZZ,True); A
            Chow group of 2-d CPR-Fano toric variety covered by 3 affine patches
            sage: isinstance(A, ChowGroup_class)
            True
            sage: isinstance(A.an_element(), ChowCycle)
            True

        TESTS::

            sage: A_ZZ = P2.Chow_group()
            sage: 2 * A_ZZ.an_element() * 3
            ( 0 | 0 | 6 )
            sage: 1/2 * A_ZZ.an_element() * 1/3
            Traceback (most recent call last):
            ...
            TypeError: unsupported operand parent(s) for *: 'Rational Field'
            and 'Chow group of 2-d CPR-Fano toric variety covered by 3 affine patches'
            sage: coercion_model.get_action(A_ZZ, ZZ)
            Right scalar multiplication by Integer Ring on Chow group of 2-d
            CPR-Fano toric variety covered by 3 affine patches
            sage: print(coercion_model.get_action(A_ZZ, QQ))
            None

        You cannot multiply integer classes with fractional
        numbers. For that you need to go to the rational Chow group::

            sage: A_QQ = P2.Chow_group(QQ)
            sage: 2 * A_QQ.an_element() * 3
            ( 0 | 0 | 6 )
            sage: 1/2 * A_QQ.an_element() * 1/3
            ( 0 | 0 | 1/6 )
            sage: coercion_model.get_action(A_QQ, ZZ)
            Right scalar multiplication by Integer Ring on QQ-Chow group of 2-d
            CPR-Fano toric variety covered by 3 affine patches
            sage: coercion_model.get_action(A_QQ, QQ)
            Right scalar multiplication by Rational Field on QQ-Chow group of 2-d
            CPR-Fano toric variety covered by 3 affine patches
        """
    def scheme(self):
        """
        Return the underlying toric variety.

        OUTPUT: a :class:`ToricVariety
        <sage.schemes.toric.variety.ToricVariety_field>`.

        EXAMPLES::

            sage: P2 = toric_varieties.P2()
            sage: A = P2.Chow_group()
            sage: A.scheme()
            2-d CPR-Fano toric variety covered by 3 affine patches
            sage: A.scheme() is P2
            True
        """
    def __truediv__(self, other) -> None:
        """
        Return the quotient of the Chow group by a subgroup.

        OUTPUT: currently not implemented

        EXAMPLES::

            sage: A = toric_varieties.dP6().Chow_group()
            sage: Asub = A.submodule([ A.gen(0), A.gen(3) ])
            sage: A/Asub
            Traceback (most recent call last):
            ...
            NotImplementedError: quotients of the Chow group are not implemented
        """
    @cached_method
    def degree(self, k=None):
        '''
        Return the degree-`k` Chow group.

        INPUT:

        - ``k`` -- integer or ``None`` (default); the degree of the
          Chow group

        OUTPUT:

        - if `k` was specified, the Chow group `A_k` as an Abelian
          group.

        - if `k` was not specified, a tuple containing the Chow groups
          in all degrees.

        .. NOTE::

            * For a smooth toric variety, this is the same as the
              Poincaré-dual cohomology group
              `H^{d-2k}(X,\\ZZ)`.

            * For a simplicial toric variety ("orbifold"),
              `A_k(X)\\otimes \\QQ = H^{d-2k}(X,\\QQ)`.

        EXAMPLES:

        Four exercises from page 65 of [Ful1993]_. First, an example
        with `A_1(X)=\\ZZ\\oplus\\ZZ/3\\ZZ`::

            sage: X = ToricVariety(Fan(cones=[[0,1], [1,2], [2,0]],
            ....:                      rays=[[2,-1], [-1,2], [-1,-1]]))
            sage: A = X.Chow_group()
            sage: A.degree(1)
            C3 x Z

        Second, an example with `A_2(X)=\\ZZ^2`::

            sage: points = [[1,0,0], [0,1,0], [0,0,1], [1,-1,1], [-1,0,-1]]
            sage: l = LatticePolytope(points)
            sage: l.show3d()                                                            # needs sage.plot
            sage: X = ToricVariety(FaceFan(l))
            sage: A = X.Chow_group()
            sage: A.degree(2)
            Z^2

        Third, an example with `A_2(X)=\\ZZ^5`::

            sage: cube = [[ 1,0,0], [0, 1,0], [0,0, 1], [-1, 1, 1],
            ....:         [-1,0,0], [0,-1,0], [0,0,-1], [ 1,-1,-1]]
            sage: lat_cube = LatticePolytope(cube)
            sage: X = ToricVariety(FaceFan((LatticePolytope(lat_cube))))
            sage: X.Chow_group().degree(2)
            Z^5

        Fourth, a fan that is not the fan over a
        polytope. Combinatorially, the fan is the same in the third
        example, only the coordinates of the first point are
        different. But the resulting fan is not the face fan of a
        cube, so the variety is "more singular". Its Chow group has
        torsion, `A_2(X)=\\ZZ^5 \\oplus \\ZZ/2`::

            sage: rays = [[ 1, 2, 3], [ 1,-1, 1], [-1, 1, 1], [-1,-1, 1],
            ....:         [-1,-1,-1], [-1, 1,-1], [ 1,-1,-1], [ 1, 1,-1]]
            sage: cones = [[0,1,2,3], [4,5,6,7], [0,1,7,6],
            ....:          [4,5,3,2], [0,2,5,7], [4,6,1,3]]
            sage: X = ToricVariety(Fan(cones, rays))
            sage: X.Chow_group().degree(2)  # long time (2s on sage.math, 2011)
            C2 x Z^5

        Finally, Example 1.3 of [FS1994]_::

            sage: def points_mod(k):
            ....:     return matrix([[ 1, 1, 2*k+1], [ 1,-1, 1],
            ....:                    [-1, 1, 1], [-1,-1, 1], [-1,-1,-1],
            ....:                    [-1, 1,-1], [ 1,-1,-1], [ 1, 1,-1]])
            sage: def rays(k):
            ....:     return matrix([[ 1,  1,  1],
            ....:                    [ 1, -1,  1],
            ....:                    [-1,  1,  1]]).solve_left(points_mod(k)).rows()
            sage: cones = [[0,1,2,3], [4,5,6,7], [0,1,7,6], [4,5,3,2], [0,2,5,7], [4,6,1,3]]
            sage: X_Delta = lambda k: ToricVariety(Fan(cones=cones, rays=rays(k)))
            sage: X_Delta(0).Chow_group().degree()  # long time (3s on sage.math, 2011)
            (Z, Z, Z^5, Z)
            sage: X_Delta(1).Chow_group().degree()  # long time (3s on sage.math, 2011)
            (Z, 0, Z^5, Z)
            sage: X_Delta(2).Chow_group().degree()  # long time (3s on sage.math, 2011)
            (Z, C2, Z^5, Z)
            sage: X_Delta(2).Chow_group(base_ring=QQ).degree()  # long time (4s on sage.math, 2011)
            (Q, 0, Q^5, Q)
        '''
    def coordinate_vector(self, chow_cycle, degree=None, reduce: bool = True):
        """
        Return the coordinate vector of the ``chow_cycle``.

        INPUT:

        - ``chow_cycle`` -- a :class:`ChowCycle`

        - ``degree`` -- ``None`` (default) or integer

        - ``reduce`` -- boolean (default: ``True``); whether to reduce
          modulo the invariants

        OUTPUT:

        * If ``degree is None`` (default), the coordinate vector
          relative to the basis ``self.gens()`` is returned.

        * If some integer ``degree=d`` is specified, the chow cycle is
          projected to the given degree and the coordinate vector
          relative to the basis ``self.gens(degree=d)`` is returned.

        EXAMPLES::

            sage: A = toric_varieties.P2().Chow_group()
            sage: a = A.gen(0) + 2*A.gen(1) + 3*A.gen(2)
            sage: A.coordinate_vector(a)
            (1, 2, 3)
            sage: A.coordinate_vector(a, degree=1)
            (2)
        """
    def gens(self, degree=None) -> tuple:
        """
        Return the generators of the Chow group.

        INPUT:

        - ``degree`` -- integer (optional); the degree of the Chow
          group

        OUTPUT:

        - if no degree is specified, the generators of the whole Chow
          group. The chosen generators may be of mixed degree.

        - if ``degree=`` `k` was specified, the generators of the
          degree-`k` part `A_k` of the Chow group.

        EXAMPLES::

            sage: A = toric_varieties.P2().Chow_group()
            sage: A.gens()
            (( 0 | 0 | 1 ), ( 0 | 1 | 0 ), ( 1 | 0 | 0 ))
            sage: A.gens(degree=1)
            (( 0 | 1 | 0 ),)
        """
    def relation_gens(self):
        """
        Return the Chow cycles equivalent to zero.

        For each `d-k-1`-dimensional cone `\\rho \\in \\Sigma^{(d-k-1)}`,
        the relations in `A_k(X)`, that is the cycles equivalent to
        zero, are generated by

        .. MATH::

            0 \\stackrel{!}{=}
            \\mathop{\\mathrm{div}}(u) =
            \\sum_{\\rho < \\sigma \\in \\Sigma^{(n-p)} }
            \\big< u, n_{\\rho,\\sigma} \\big> V(\\sigma)
            ,\\qquad
            u \\in M(\\rho)

        where `n_{\\rho,\\sigma}` is a (randomly chosen) lift of the
        generator of `N_\\sigma/N_\\rho \\simeq \\ZZ`. See also Exercise
        12.5.7 of [CLS2011]_.

        See also :meth:`relations` to obtain the relations as
        submodule of the free module generated by the cones.  Or use
        ``self.relations().gens()`` to list the relations in the free
        module.

        OUTPUT:

        A tuple of Chow cycles, each rationally equivalent to zero,
        that generates the rational equivalence.

        EXAMPLES::

            sage: P2 = toric_varieties.P2()
            sage: A = P2.Chow_group()
            sage: first = A.relation_gens()[0]; first
            ( 0 | 0 | 0 )
            sage: first.is_zero()
            True
            sage: first.lift()
            (0, 1, 0, -1, 0, 0, 0)
        """

class ChowGroup_degree_class(SageObject):
    """
    A fixed-degree subgroup of the Chow group of a toric variety.

    .. WARNING::

        Use
        :meth:`~sage.schemes.toric.chow_group.ChowGroup_class.degree`
        to construct :class:`ChowGroup_degree_class` instances.

    EXAMPLES::

        sage: P2 = toric_varieties.P2()
        sage: A = P2.Chow_group(); A
        Chow group of 2-d CPR-Fano toric variety covered by 3 affine patches
        sage: A.degree()
        (Z, Z, Z)
        sage: A.degree(2)
        Z
        sage: type(_)
        <class 'sage.schemes.toric.chow_group.ChowGroup_degree_class'>
    """
    def __init__(self, A, d) -> None:
        """
        Construct a :class:`ChowGroup_degree_class`.

        INPUT:

        - ``A`` -- a :class:`ChowGroup_class`

        - ``d`` -- integer; the degree of the Chow group

        EXAMPLES::

            sage: P2 = toric_varieties.P2()
            sage: A = P2.Chow_group()
            sage: from sage.schemes.toric.chow_group import ChowGroup_degree_class
            sage: A2 = ChowGroup_degree_class(A,2)
            sage: A2
            Z
        """
    def module(self):
        """
        Return the submodule of the toric Chow group generated.

        OUTPUT: a :class:`sage.modules.fg_pid.fgp_module.FGP_Module_class`

        EXAMPLES::

            sage: projective_plane = toric_varieties.P2()
            sage: A2 = projective_plane.Chow_group().degree(2)
            sage: A2.module()
            Finitely generated module V/W over Integer Ring with invariants (0)
        """
    def ngens(self) -> int:
        """
        Return the number of generators.

        OUTPUT: integer

        EXAMPLES::

            sage: projective_plane = toric_varieties.P2()
            sage: A2 = projective_plane.Chow_group().degree(2)
            sage: A2.ngens()
            1
        """
    def gen(self, i):
        """
        Return the ``i``-th generator of the Chow group of fixed degree.

        INPUT:

        - ``i`` -- integer; the index of the generator to be returned

        OUTPUT: a Chow cycle

        EXAMPLES::

            sage: projective_plane = toric_varieties.P2()
            sage: A2 = projective_plane.Chow_group().degree(2)
            sage: A2.gen(0)
            ( 0 | 0 | 1 )
        """
    def gens(self) -> tuple:
        """
        Return the generators of the Chow group of fixed degree.

        OUTPUT: a tuple of Chow cycles of fixed degree generating
        :meth:`module`.

        EXAMPLES::

            sage: projective_plane = toric_varieties.P2()
            sage: A2 = projective_plane.Chow_group().degree(2)
            sage: A2.gens()
            (( 0 | 0 | 1 ),)
        """

def is_ChowGroup(x) -> bool:
    """
    Return whether ``x`` is a :class:`ChowGroup_class`.

    INPUT:

    - ``x`` -- anything

    OUTPUT: boolean

    EXAMPLES::

        sage: P2 = toric_varieties.P2()
        sage: A = P2.Chow_group()
        sage: from sage.schemes.toric.chow_group import is_ChowGroup
        sage: is_ChowGroup(A)
        doctest:warning...
        DeprecationWarning: The function is_ChowGroup is deprecated; use 'isinstance(..., ChowGroup_class)' instead.
        See https://github.com/sagemath/sage/issues/38022 for details.
        True
        sage: is_ChowGroup('Victoria')
        False
    """
def is_ChowCycle(x) -> bool:
    """
    Return whether ``x`` is a :class:`ChowCycle`.

    INPUT:

    - ``x`` -- anything

    OUTPUT: boolean

    EXAMPLES::

        sage: P2 = toric_varieties.P2()
        sage: A = P2.Chow_group()
        sage: from sage.schemes.toric.chow_group import *
        sage: is_ChowCycle(A)
        doctest:warning...
        DeprecationWarning: The function is_ChowCycle is deprecated;
        use 'isinstance(..., ChowCycle)' instead.
        See https://github.com/sagemath/sage/issues/38277 for details.
        False
        sage: is_ChowCycle(A.an_element())
        True
        sage: is_ChowCycle('Victoria')
        False
    """
