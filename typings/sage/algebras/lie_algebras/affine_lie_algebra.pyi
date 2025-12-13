from sage.algebras.lie_algebras.lie_algebra import FinitelyGeneratedLieAlgebra as FinitelyGeneratedLieAlgebra, LieAlgebra as LieAlgebra
from sage.algebras.lie_algebras.lie_algebra_element import UntwistedAffineLieAlgebraElement as UntwistedAffineLieAlgebraElement
from sage.categories.cartesian_product import cartesian_product as cartesian_product
from sage.categories.kac_moody_algebras import KacMoodyAlgebras as KacMoodyAlgebras
from sage.combinat.root_system.cartan_type import CartanType as CartanType
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.lazy_attribute import lazy_attribute as lazy_attribute
from sage.rings.integer_ring import ZZ as ZZ
from sage.sets.disjoint_union_enumerated_sets import DisjointUnionEnumeratedSets as DisjointUnionEnumeratedSets
from sage.sets.family import Family as Family
from sage.structure.element import parent as parent
from sage.structure.parent import Set_generic as Set_generic
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

class AffineLieAlgebra(FinitelyGeneratedLieAlgebra):
    """
    An (untwisted) affine Lie algebra.

    Note that the derived subalgebra of the Kac-Moody algebra is the
    affine Lie algebra.

    INPUT:

    Can be one of the following:

    - a base ring and an affine Cartan type: constructs the affine
      (Kac-Moody) Lie algebra of the classical Lie algebra in the
      bracket representation over the base ring

    - a classical Lie algebra: constructs the corresponding affine
      (Kac-Moody) Lie algebra

    There is the optional argument ``kac_moody``, which can be set
    to ``False`` to obtain the affine Lie algebra instead of the affine
    Kac-Moody algebra.

    .. SEEALSO::

        - :class:`UntwistedAffineLieAlgebra`
        - :class:`TwistedAffineLieAlgebra`

    REFERENCES:

    - [Ka1990]_
    """
    @staticmethod
    def __classcall_private__(cls, arg0, cartan_type=None, kac_moody: bool = True):
        """
        Parse input to ensure a unique representation.

        INPUT:

        - ``arg0`` -- a simple Lie algebra or a base ring
        - ``cartan_type`` -- a Cartan type

        EXAMPLES::

            sage: L1 = lie_algebras.Affine(QQ, ['A', 4, 1])
            sage: cl = lie_algebras.sl(QQ, 5)
            sage: L2 = lie_algebras.Affine(cl)
            sage: L1 is L2
            True
            sage: cl.affine() is L1
            True

            sage: L1 = LieAlgebra(QQ, cartan_type=['A', 5, 2])
            sage: L2 = lie_algebras.Affine(QQ, ['A', 5, 2])
            sage: L1 is L2
            True
        """
    def __init__(self, g, cartan_type, names, kac_moody) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: asl = lie_algebras.Affine(QQ, ['D', 4, 1])
            sage: TestSuite(asl).run()
        """
    @cached_method
    def basis(self):
        """
        Return the basis of ``self``.

        EXAMPLES::

            sage: g = LieAlgebra(QQ, cartan_type=['D', 4, 1])
            sage: B = g.basis()
            sage: al = RootSystem(['D',4]).root_lattice().simple_roots()
            sage: B[al[1]+al[2]+al[4],4]
            (E[alpha[1] + alpha[2] + alpha[4]])#t^4
            sage: B[-al[1]-2*al[2]-al[3]-al[4],2]
            (E[-alpha[1] - 2*alpha[2] - alpha[3] - alpha[4]])#t^2
            sage: B[al[4],-2]
            (E[alpha[4]])#t^-2
            sage: B['c']
            c
            sage: B['d']
            d

            sage: g = LieAlgebra(QQ, cartan_type=['D', 4, 2], kac_moody=False)
            sage: B = g.basis()
            sage: it = iter(B)
            sage: [next(it) for _ in range(3)]
            [c, (E[alpha[1]])#t^0, (E[alpha[2]])#t^0]
            sage: B['c']
            c
            sage: B['d']
            0
        """
    def derived_series(self):
        """
        Return the derived series of ``self``.

        EXAMPLES::

            sage: g = LieAlgebra(QQ, cartan_type=['B',3,1])
            sage: g.derived_series()
            [Affine Kac-Moody algebra of ['B', 3] in the Chevalley basis,
             Affine Lie algebra of ['B', 3] in the Chevalley basis]
            sage: g.lower_central_series()
            [Affine Kac-Moody algebra of ['B', 3] in the Chevalley basis,
             Affine Lie algebra of ['B', 3] in the Chevalley basis]

            sage: D = g.derived_subalgebra()
            sage: D.derived_series()
            [Affine Lie algebra of ['B', 3] in the Chevalley basis]
        """
    lower_central_series = derived_series
    def is_nilpotent(self):
        """
        Return ``False`` as ``self`` is semisimple.

        EXAMPLES::

            sage: g = LieAlgebra(QQ, cartan_type=['B',3,1])
            sage: g.is_nilpotent()
            False
            sage: g.is_solvable()
            False
        """
    is_solvable = is_nilpotent
    def cartan_type(self):
        """
        Return the Cartan type of ``self``.

        EXAMPLES::

            sage: g = LieAlgebra(QQ, cartan_type=['C',3,1])
            sage: g.cartan_type()
            ['C', 3, 1]
        """
    def classical(self):
        """
        Return the classical Lie algebra of ``self``.

        EXAMPLES::

            sage: g = LieAlgebra(QQ, cartan_type=['F',4,1])
            sage: g.classical()
            Lie algebra of ['F', 4] in the Chevalley basis

            sage: so5 = lie_algebras.so(QQ, 5, 'matrix')
            sage: A = so5.affine()
            sage: A.classical() == so5
            True
        """
    @cached_method
    def zero(self):
        """
        Return the element `0`.

        EXAMPLES::

            sage: g = LieAlgebra(QQ, cartan_type=['F',4,1])
            sage: g.zero()
            0
        """
    @cached_method
    def c(self):
        """
        Return the canonical central element `c` of ``self``.

        EXAMPLES::

            sage: g = LieAlgebra(QQ, cartan_type=['A',3,1])
            sage: g.c()
            c
        """
    @cached_method
    def d(self):
        """
        Return the canonical derivation `d` of ``self``.

        If ``self`` is the affine Lie algebra, then this returns `0`.

        EXAMPLES::

            sage: g = LieAlgebra(QQ, cartan_type=['A',3,1])
            sage: g.d()
            d
            sage: D = g.derived_subalgebra()
            sage: D.d()
            0
        """
    @cached_method
    def lie_algebra_generators(self):
        """
        Return the Lie algebra generators of ``self``.

        EXAMPLES::

            sage: g = LieAlgebra(QQ, cartan_type=['A',1,1])
            sage: list(g.lie_algebra_generators())
            [(E[alpha[1]])#t^0,
             (E[-alpha[1]])#t^0,
             (h1)#t^0,
             (E[-alpha[1]])#t^1,
             (E[alpha[1]])#t^-1,
             c,
             d]

            sage: L = LieAlgebra(QQ, cartan_type=['A',5,2])
            sage: list(L.lie_algebra_generators())
            [(E[alpha[1]])#t^0,
             (E[alpha[2]])#t^0,
             (E[alpha[3]])#t^0,
             (E[-alpha[1]])#t^0,
             (E[-alpha[2]])#t^0,
             (E[-alpha[3]])#t^0,
             (h1)#t^0,
             (h2)#t^0,
             (h3)#t^0,
             (E[-alpha[1] - 2*alpha[2] - alpha[3]])#t^1,
             (E[alpha[1] + 2*alpha[2] + alpha[3]])#t^-1,
             c,
             d]
        """
    def e(self, i=None):
        """
        Return the generators `e` of ``self``.

        INPUT:

        - ``i`` -- (optional) if specified, return just the
          generator `e_i`

        EXAMPLES::

            sage: g = LieAlgebra(QQ, cartan_type=['B', 3, 1])
            sage: list(g.e())
            [(E[-alpha[1] - 2*alpha[2] - 2*alpha[3]])#t^1,
             (E[alpha[1]])#t^0, (E[alpha[2]])#t^0, (E[alpha[3]])#t^0]
            sage: g.e(2)
            (E[alpha[2]])#t^0
        """
    def f(self, i=None):
        """
        Return the generators `f` of ``self``.

        INPUT:

        - ``i`` -- (optional) if specified, return just the
          generator `f_i`

        EXAMPLES::

            sage: g = LieAlgebra(QQ, cartan_type=['A', 5, 2])
            sage: list(g.f())
            [(E[alpha[1] + 2*alpha[2] + alpha[3]])#t^-1,
             (E[-alpha[1]])#t^0, (E[-alpha[2]])#t^0, (E[-alpha[3]])#t^0]
            sage: g.f(2)
            (E[-alpha[2]])#t^0
        """
    def monomial(self, m):
        """
        Construct the monomial indexed by ``m``.

        EXAMPLES::

            sage: g = LieAlgebra(QQ, cartan_type=['B',4,1])
            sage: al = RootSystem(['B',4]).root_lattice().simple_roots()
            sage: g.monomial((al[1]+al[2]+al[3],4))
            (E[alpha[1] + alpha[2] + alpha[3]])#t^4
            sage: g.monomial((-al[1]-al[2]-2*al[3]-2*al[4],2))
            (E[-alpha[1] - alpha[2] - 2*alpha[3] - 2*alpha[4]])#t^2
            sage: g.monomial((al[4],-2))
            (E[alpha[4]])#t^-2
            sage: g.monomial('c')
            c
            sage: g.monomial('d')
            d
        """

class UntwistedAffineLieAlgebra(AffineLieAlgebra):
    """
    An untwisted affine Lie algebra.

    Let `R` be a ring.  Given a finite-dimensional simple Lie algebra
    `\\mathfrak{g}` over `R`, the affine Lie algebra
    `\\widehat{\\mathfrak{g}}^{\\prime}` associated to `\\mathfrak{g}` is
    defined as

    .. MATH::

        \\widehat{\\mathfrak{g}}' = \\bigl( \\mathfrak{g} \\otimes
        R[t, t^{-1}] \\bigr) \\oplus R c,

    where `c` is the canonical central element and `R[t, t^{-1}]` is the
    Laurent polynomial ring over `R`. The Lie bracket is defined as

    .. MATH::

        [x \\otimes t^m + \\lambda c, y \\otimes t^n + \\mu c] =
        [x, y] \\otimes t^{m+n} + m \\delta_{m,-n} ( x | y ) c,

    where `( x | y )` is the Killing form on `\\mathfrak{g}`.

    There is a canonical derivation `d` on `\\widehat{\\mathfrak{g}}'`
    that is defined by

    .. MATH::

        d(x \\otimes t^m + \\lambda c) = a \\otimes m t^m,

    or equivalently by `d = t \\frac{d}{dt}`.

    The affine Kac-Moody algebra `\\widehat{\\mathfrak{g}}` is formed by
    adjoining the derivation `d` such that

    .. MATH::

        \\widehat{\\mathfrak{g}} = \\bigl( \\mathfrak{g} \\otimes R[t,t^{-1}]
        \\bigr) \\oplus R c \\oplus R d.

    Specifically, the bracket on `\\widehat{\\mathfrak{g}}` is defined as

    .. MATH::

        [t^m \\otimes x \\oplus \\lambda c \\oplus \\mu d, t^n \\otimes y \\oplus
        \\lambda_1 c \\oplus \\mu_1 d] = \\bigl( t^{m+n} [x,y] + \\mu n t^n \\otimes
        y - \\mu_1 m t^m \\otimes x\\bigr) \\oplus m \\delta_{m,-n} (x|y) c .

    EXAMPLES:

    We begin by constructing an affine Kac-Moody algebra of type `G_2^{(1)}`
    from the classical Lie algebra of type `G_2`::

        sage: g = LieAlgebra(QQ, cartan_type=['G',2])
        sage: A = g.affine()
        sage: A
        Affine Kac-Moody algebra of ['G', 2] in the Chevalley basis

    Next, we construct the generators and perform some computations::

        sage: A.inject_variables()
        Defining e1, e2, f1, f2, h1, h2, e0, f0, c, d
        sage: e1.bracket(f1)
        (h1)#t^0
        sage: e0.bracket(f0)
        (-h1 - 2*h2)#t^0 + 8*c
        sage: e0.bracket(f1)
        0
        sage: A[d, f0]
        (-E[3*alpha[1] + 2*alpha[2]])#t^-1
        sage: A([[e0, e2], [[[e1, e2], [e0, [e1, e2]]], e1]])
        (-6*E[-3*alpha[1] - alpha[2]])#t^2
        sage: f0.bracket(f1)
        0
        sage: f0.bracket(f2)
        (E[3*alpha[1] + alpha[2]])#t^-1
        sage: A[h1+3*h2, A[[[f0, f2], f1], [f1,f2]] + f1] - f1
        (2*E[alpha[1]])#t^-1

    We can construct its derived subalgebra, the affine Lie algebra
    of type `G_2^{(1)}`. In this case, there is no canonical derivation,
    so the generator `d` is `0`::

        sage: D = A.derived_subalgebra()
        sage: D.d()
        0
    """
    def __init__(self, g, kac_moody) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: asl = lie_algebras.Affine(QQ, ['A',4,1])
            sage: TestSuite(asl).run()
        """
    def derived_subalgebra(self):
        """
        Return the derived subalgebra of ``self``.

        EXAMPLES::

            sage: g = LieAlgebra(QQ, cartan_type=['B',3,1])
            sage: g
            Affine Kac-Moody algebra of ['B', 3] in the Chevalley basis
            sage: D = g.derived_subalgebra(); D
            Affine Lie algebra of ['B', 3] in the Chevalley basis
            sage: D.derived_subalgebra() == D
            True
        """
    Element = UntwistedAffineLieAlgebraElement

class TwistedAffineLieAlgebra(AffineLieAlgebra):
    """
    A twisted affine Lie algebra.

    A twisted affine Lie algebra is an affine Lie algebra for
    type `X_N^{(r)}` with `r > 1`. We realize this inside an
    untwisted affine Kac--Moody Lie algebra following Chapter 8
    of [Ka1990]_.

    Let `\\overline{\\mathfrak{g}}` be the classical Lie algebra by
    taking the index set `I \\setminus \\{\\epsilon\\}`, where
    `\\epsilon = 0` unless `\\epsilon = n` for `X_N^{(r)} = A_{2n}^{(2)}`,
    for the twisted affine Lie algebra `\\widetilde{\\mathfrak{g}}`.
    Let `\\mathfrak{g}` be the basic Lie algebra of type `X_N`.
    We realize `\\overline{\\mathfrak{g}}` as the fixed-point subalgebra
    `\\mathfrak{g}^{(0)}` of `\\mathfrak{g}` under the order `r` diagram
    automorphism `\\mu`. This naturally acts on the `\\zeta_r` (a primitive
    `r`-th root of unity) eigenspace `\\mathfrak{g}^{(1)}` of `\\mu`,
    which is the highest weight representation corresponding to
    the small adjoint (where the weight spaces are the short roots
    of `\\overline{\\mathfrak{g}}`). The *twisted affine (Kac-Moody)
    Lie algebra* `\\widehat{\\mathfrak{g}}` is constructed as the
    subalgebra of `X_N^{(1)}` given by

    .. MATH::

        \\sum_{i \\in \\ZZ} \\mathfrak{g}^{(i \\mod 2)} \\otimes t^i
        \\oplus R c \\oplus R d,

    where `R` is the base ring.

    We encode our basis by using the classical Lie algebra except
    for type `A_{2n}^{(2)}`. For type `A_{2n}^{(2)}`, the fixed-point
    algebra `\\mathfrak{g}^{(0)}` is of type `B_n` using the index set
    `\\{0, \\ldots, n-1\\}`. For `\\mathfrak{g}^{(1)}`, we identify the
    weights in this representation with the roots of type `B_n` and
    the double all of its short roots.
    """
    def __init__(self, R, cartan_type, kac_moody) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: g = lie_algebras.Affine(QQ, ['A', 5, 2])
            sage: TestSuite(g).run()

            sage: g = lie_algebras.Affine(QQ, ['D', 4, 2])
            sage: TestSuite(g).run()

            sage: g = lie_algebras.Affine(QQ, ['D', 5, 2])
            sage: TestSuite(g).run()

            sage: g = lie_algebras.Affine(QQ, ['A', 6, 2])
            sage: TestSuite(g).run(skip=['_test_elements'])  # _test_monomial_coefficients fails

            sage: g = lie_algebras.Affine(QQ, ['A', 2, 2])
            sage: TestSuite(g).run(skip=['_test_elements'])  # _test_monomial_coefficients fails

            sage: g = lie_algebras.Affine(QQ, ['E', 6, 2])
            sage: TestSuite(g).run()  # long time

            sage: g = lie_algebras.Affine(QQ, ['D', 4, 3])
            sage: TestSuite(g).run()  # long time
        """
    def derived_subalgebra(self):
        """
        Return the derived subalgebra of ``self``.

        EXAMPLES::

            sage: g = LieAlgebra(QQ, cartan_type=['A', 5, 2])
            sage: g
            Twisted affine Kac-Moody algebra of type ['B', 3, 1]^* over Rational Field
            sage: D = g.derived_subalgebra(); D
            Twisted affine Lie algebra of type ['B', 3, 1]^* over Rational Field
            sage: D.derived_subalgebra() == D
            True
        """
    def ambient(self):
        """
        Return the ambient untwisted affine Lie algebra of ``self``.

        EXAMPLES::

            sage: g = LieAlgebra(QQ, cartan_type=['A', 5, 2])
            sage: g.ambient()
            Affine Kac-Moody algebra of ['A', 5] in the Chevalley basis
        """
    def retract(self, x):
        """
        Retract the element ``x`` from the ambient untwisted affine Lie
        algebra into ``self``.

        EXAMPLES::

            sage: g = LieAlgebra(QQ, cartan_type=['A', 5, 2])
            sage: it = iter(g.basis())
            sage: elts = [next(it) for _ in range(20)]
            sage: elts
            [c,
             d,
             (E[alpha[1]])#t^0,
             (E[alpha[2]])#t^0,
             (E[alpha[3]])#t^0,
             (E[alpha[1] + alpha[2]])#t^0,
             (E[alpha[2] + alpha[3]])#t^0,
             (E[2*alpha[2] + alpha[3]])#t^0,
             (E[alpha[1] + alpha[2] + alpha[3]])#t^0,
             (E[2*alpha[1] + 2*alpha[2] + alpha[3]])#t^0,
             (E[alpha[1] + 2*alpha[2] + alpha[3]])#t^0,
             (E[-alpha[1]])#t^0,
             (E[-alpha[2]])#t^0,
             (E[-alpha[3]])#t^0,
             (E[-alpha[1] - alpha[2]])#t^0,
             (E[-alpha[2] - alpha[3]])#t^0,
             (E[-2*alpha[2] - alpha[3]])#t^0,
             (E[-alpha[1] - alpha[2] - alpha[3]])#t^0,
             (E[-2*alpha[1] - 2*alpha[2] - alpha[3]])#t^0,
             (E[-alpha[1] - 2*alpha[2] - alpha[3]])#t^0]
            sage: all(g.retract(g.to_ambient(x)) == x for x in elts)
            True
        """
    @lazy_attribute
    def to_ambient(self):
        """
        Lift the element ``x`` from the ambient untwisted affine Lie
        algebra into ``self``.

        EXAMPLES::

            sage: g = LieAlgebra(QQ, cartan_type=['A', 5, 2])
            sage: g.to_ambient
            Generic morphism:
              From: Twisted affine Kac-Moody algebra of type ['B', 3, 1]^* over Rational Field
              To:   Affine Kac-Moody algebra of ['A', 5] in the Chevalley basis
        """
    class Element(UntwistedAffineLieAlgebraElement): ...

class TwistedAffineIndices(UniqueRepresentation, Set_generic):
    """
    The indices for the basis of a twisted affine Lie algebra.

    INPUT:

    - ``cartan_type`` -- the Cartan type of twisted affine type Lie algebra

    EXAMPLES::

        sage: from sage.algebras.lie_algebras.affine_lie_algebra import TwistedAffineIndices
        sage: I = TwistedAffineIndices(['A', 3, 2])
        sage: it = iter(I)
        sage: [next(it) for _ in range(20)]
        [(alpha[1], 0), (alpha[2], 0), (alpha[1] + alpha[2], 0),
         (2*alpha[1] + alpha[2], 0), (-alpha[1], 0), (-alpha[2], 0),
         (-alpha[1] - alpha[2], 0), (-2*alpha[1] - alpha[2], 0),
         (alphacheck[1], 0), (alphacheck[2], 0), (alpha[1], 1),
         (alpha[1] + alpha[2], 1), (-alpha[1], 1), (-alpha[1] - alpha[2], 1),
         (alphacheck[1], 1), (alpha[1], -1), (alpha[1] + alpha[2], -1),
         (-alpha[1], -1), (-alpha[1] - alpha[2], -1), (alphacheck[1], -1)]

        sage: I = TwistedAffineIndices(['A', 4, 2])
        sage: it = iter(I)
        sage: [next(it) for _ in range(20)]
        [(alpha[0], 0), (alpha[1], 0), (alpha[0] + alpha[1], 0),
         (2*alpha[0] + alpha[1], 0), (-alpha[0], 0), (-alpha[1], 0),
         (-alpha[0] - alpha[1], 0), (-2*alpha[0] - alpha[1], 0),
         (alphacheck[0], 0), (alphacheck[1], 0), (alpha[0], 1), (alpha[1], 1),
         (alpha[0] + alpha[1], 1), (2*alpha[0] + alpha[1], 1), (-alpha[0], 1),
         (-alpha[1], 1), (-alpha[0] - alpha[1], 1), (-2*alpha[0] - alpha[1], 1),
         (2*alpha[0], 1), (2*alpha[0] + 2*alpha[1], 1)]

        sage: I = TwistedAffineIndices(['A', 2, 2])
        sage: it = iter(I)
        sage: [next(it) for _ in range(10)]
        [(alpha[0], 0), (-alpha[0], 0), (alphacheck[0], 0), (alpha[0], 1),
         (-alpha[0], 1), (2*alpha[0], 1), (-2*alpha[0], 1),
         (alphacheck[0], 1), (alpha[0], -1), (-alpha[0], -1)]
    """
    @staticmethod
    def __classcall_private__(cls, cartan_type):
        """
        Normalize input to ensure a unique representation.

            sage: from sage.algebras.lie_algebras.affine_lie_algebra import TwistedAffineIndices
            sage: I1 = TwistedAffineIndices(CartanType(['C', 4, 1]).dual())
            sage: I2 = TwistedAffineIndices(['D', 5, 2])
            sage: I1 is I2
            True
            sage: I = TwistedAffineIndices(['C', 4, 1])
            Traceback (most recent call last):
            ...
            ValueError: the Cartan type must be a twisted affine type
        """
    def __init__(self, cartan_type) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: from sage.algebras.lie_algebras.affine_lie_algebra import TwistedAffineIndices
            sage: I = TwistedAffineIndices(['D', 4, 2])
            sage: TestSuite(I).run()
        """
    def __contains__(self, x) -> bool:
        """
        Return if ``x`` is contained in ``self``.

        EXAMPLES::

            sage: from sage.algebras.lie_algebras.affine_lie_algebra import TwistedAffineIndices
            sage: I = TwistedAffineIndices(['D', 4, 2])
            sage: Q = RootSystem(['B', 3]).root_lattice()
            sage: all((r, 4) in I for r in Q.roots())
            True
            sage: all((r, 3) in I for r in Q.short_roots())
            True
            sage: all((r, 3) not in I for r in Q.long_roots())
            True
            sage: list(I.an_element()) in I  # lists are not included
            False
            sage: (5, Q) in I
            False
            sage: (5, 5) in I
            False
            sage: (Q.simple_root(1), Q.simple_root(1)) in I
            False
            sage: (Q.simple_coroot(2), 1) in I
            False
            sage: (Q.simple_coroot(3), 1) in I
            True
        """
    def __iter__(self):
        """
        Iterate over ``self``.

        EXAMPLES::

            sage: from sage.algebras.lie_algebras.affine_lie_algebra import TwistedAffineIndices
            sage: I = TwistedAffineIndices(['D', 3, 2])
            sage: it = iter(I)
            sage: [next(it) for _ in range(22)]
            [(alpha[1], 0), (alpha[2], 0), (alpha[1] + 2*alpha[2], 0), (alpha[1] + alpha[2], 0),
             (-alpha[1], 0), (-alpha[2], 0), (-alpha[1] - 2*alpha[2], 0), (-alpha[1] - alpha[2], 0),
             (alphacheck[1], 0), (alphacheck[2], 0), (alpha[2], 1), (alpha[1] + alpha[2], 1),
             (-alpha[2], 1), (-alpha[1] - alpha[2], 1), (alphacheck[2], 1), (alpha[2], -1),
             (alpha[1] + alpha[2], -1), (-alpha[2], -1), (-alpha[1] - alpha[2], -1),
             (alphacheck[2], -1), (alpha[1], 2), (alpha[2], 2)]
        """
