from sage.categories.enumerated_sets import EnumeratedSets as EnumeratedSets
from sage.categories.fields import Fields as Fields
from sage.categories.finite_dimensional_lie_algebras_with_basis import FiniteDimensionalLieAlgebrasWithBasis as FiniteDimensionalLieAlgebrasWithBasis
from sage.categories.graded_algebras_with_basis import GradedAlgebrasWithBasis as GradedAlgebrasWithBasis
from sage.categories.kac_moody_algebras import KacMoodyAlgebras as KacMoodyAlgebras
from sage.categories.monoids import Monoids as Monoids
from sage.combinat.free_module import CombinatorialFreeModule as CombinatorialFreeModule
from sage.combinat.integer_lists.invlex import IntegerListsLex as IntegerListsLex
from sage.combinat.root_system.coxeter_group import CoxeterGroup as CoxeterGroup
from sage.data_structures.blas_dict import iaxpy as iaxpy
from sage.matrix.constructor import matrix as matrix
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.lazy_attribute import lazy_attribute as lazy_attribute
from sage.monoids.indexed_free_monoid import IndexedFreeAbelianMonoid as IndexedFreeAbelianMonoid, IndexedMonoid as IndexedMonoid
from sage.rings.integer_ring import ZZ as ZZ
from sage.sets.family import Family as Family
from sage.sets.finite_enumerated_set import FiniteEnumeratedSet as FiniteEnumeratedSet
from sage.sets.non_negative_integers import NonNegativeIntegers as NonNegativeIntegers

class CenterIndices(IndexedFreeAbelianMonoid):
    """
    Set of basis indices for the center of a universal enveloping algebra.

    This also constructs the lift from the center to the universal enveloping
    algebra as part of computing the generators and basis elements. The
    basic algorithm is to construct the centralizer of each filtered
    component in increasing order (as each is a finite dimensional vector
    space). For more precise details, see [Motsak2006]_.
    """
    @staticmethod
    def __classcall__(cls, center):
        """
        Normalize input to ensure a unique representation.

        EXAMPLES::

            sage: from sage.algebras.lie_algebras.center_uea import CenterIndices
            sage: g = lie_algebras.pwitt(GF(3), 3)
            sage: U = g.pbw_basis()
            sage: Z = U.center()
            sage: CenterIndices(Z) is CenterIndices(Z)
            True
        """
    def __init__(self, center, indices=None) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: g = lie_algebras.pwitt(GF(5), 5)
            sage: U = g.pbw_basis()
            sage: Z = U.center()
            sage: I = Z.indices()
            sage: TestSuite(I).run(max_runs=7)
        """
    def lift_on_basis(self, m):
        """
        Return the image of the basis element indexed by ``m`` in the
        universal enveloping algebra.

        EXAMPLES::

            sage: g = lie_algebras.Heisenberg(QQ, 3)
            sage: U = g.pbw_basis()
            sage: Z = U.center()
            sage: I = Z.indices()
            sage: z0 = I.monoid_generators()[0]
            sage: I._lift_map
            {0: {1: 1}}
            sage: I.lift_on_basis(z0)
            PBW['z']
            sage: I._lift_map
            {0: {1: 1}, 1: {PBW['z']: PBW['z']}}
            sage: I.lift_on_basis(z0^3)
            PBW['z']^3
            sage: I._lift_map
            {0: {1: 1}, 1: {PBW['z']: PBW['z']}}
            sage: I._construct_next_degree()
            sage: I._construct_next_degree()
            sage: I._lift_map
            {0: {1: 1},
             1: {PBW['z']: PBW['z']},
             2: {PBW['z']^2: PBW['z']^2},
             3: {PBW['z']^3: PBW['z']^3}}
            sage: I.lift_on_basis(z0^3)
            PBW['z']^3
        """
    def __iter__(self):
        """
        Iterate over ``self`` in degree increasing order.

        EXAMPLES::

            sage: g = lie_algebras.pwitt(GF(3), 6)
            sage: U = g.pbw_basis()
            sage: Z = U.center()
            sage: I = Z.indices()
            sage: it = iter(I)
            sage: [next(it) for _ in range(10)]
            [1, Z[0], Z[1], Z[2], Z[3], Z[4], Z[5], Z[6], Z[7], Z[0]^2]
        """
    def some_elements(self):
        """
        Return some elements of ``self``.

        EXAMPLES::

            sage: g = lie_algebras.pwitt(GF(3), 3)
            sage: U = g.pbw_basis()
            sage: Z = U.center()
            sage: I = Z.indices()
            sage: I.some_elements()
            [1, Z[0], Z[1], Z[2], Z[0]*Z[1]*Z[2], Z[0]*Z[2]^4, Z[0]^4*Z[1]^3]
        """
    def degree(self, m):
        """
        Return the degre of ``m`` in ``self``.

        EXAMPLES::

            sage: g = LieAlgebra(QQ, cartan_type=['E', 6])
            sage: U = g.pbw_basis()
            sage: Z = U.center()
            sage: I = Z.indices()
            sage: [I.degree(g) for g in I.monoid_generators()]
            [2, 5, 6, 8, 9, 12]
            sage: [(elt, I.degree(elt)) for elt in I.some_elements()]
            [(1, 0), (Z[0], 2), (Z[0]^2, 4), (Z[1], 5), (Z[0]^3*Z[1], 11),
             (Z[0]^10, 20), (Z[0]*Z[1]^4, 22)]
        """

class SimpleLieCenterIndices(CenterIndices):
    """
    Set of basis indices for the center of a universal enveloping algebra of
    a simple Lie algebra.

    For more information, see
    :class:`~sage.algebras.lie_algebras.center_uea.CenterIndices`.
    """
    def __init__(self, center) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: g = LieAlgebra(QQ, cartan_type=['E', 6])
            sage: U = g.pbw_basis()
            sage: Z = U.center()
            sage: I = Z.indices()
            sage: TestSuite(I).run()
        """
    def __iter__(self):
        """
        Iterate over ``self`` in degree increasing order.

        EXAMPLES::

            sage: g = LieAlgebra(QQ, cartan_type=['E', 6])
            sage: U = g.pbw_basis()
            sage: Z = U.center()
            sage: I = Z.indices()
            sage: it = iter(I)
            sage: [next(it) for _ in range(10)]
            [1, Z[0], Z[0]^2, Z[1], Z[2], Z[0]^3, Z[0]*Z[1], Z[3], Z[0]*Z[2], Z[0]^4]
        """

class CenterUEA(CombinatorialFreeModule):
    """
    The center of a universal enveloping algebra.

    .. TODO::

        Generalize this to be the centralizer of any set of the UEA.

    .. TODO::

        For characteristic `p > 0`, implement the `p`-center of a simple
        Lie algebra. See, e.g.,

        - Theorem 5.12 of [Motsak2006]_
        - http://www.math.kobe-u.ac.jp/icms2006/icms2006-video/slides/059.pdf

    EXAMPLES::

        sage: g = LieAlgebra(QQ, cartan_type=['A', 2])
        sage: U = g.pbw_basis()
        sage: Z = U.center()
        sage: B = Z.basis()
        sage: it = iter(B)
        sage: center_elts = [next(it) for _ in range(6)]; center_elts
        [1, Z[0], Z[1], Z[0]^2, Z[0]*Z[1], Z[1]^2]
        sage: elts = [U(v) for v in center_elts]  # long time
        sage: all(v * g == g * v for g in U.algebra_generators() for v in elts)  # long time
        True

    The Heisenberg Lie algebra `H_4` over a finite field; note the basis
    elements `b^p \\in Z(U(H_4))` for the basis elements `b \\in H_4`::

        sage: g = lie_algebras.Heisenberg(GF(3), 4)
        sage: U = g.pbw_basis()
        sage: Z = U.center()
        sage: B = Z.basis()
        sage: it = iter(B)
        sage: center_elts = [next(it) for _ in range(12)]; center_elts
        [1, Z[0], Z[0]^2, Z[0]^3, Z[1], Z[2], Z[3], Z[4], Z[5], Z[6], Z[7], Z[8]]
        sage: elts = [U(v) for v in center_elts]; elts
        [1, PBW['z'], PBW['z']^2, PBW['z']^3, PBW['p1']^3, PBW['p2']^3, PBW['p3']^3,
         PBW['p4']^3, PBW['q1']^3, PBW['q2']^3, PBW['q3']^3, PBW['q4']^3]
        sage: all(v * g == g * v for g in U.algebra_generators() for v in elts)
        True

    An example with a free 4-step nilpotent Lie algebras on 2 generators::

        sage: L = LieAlgebra(QQ, 2, step=4); L
        Free Nilpotent Lie algebra on 8 generators
         (X_1, X_2, X_12, X_112, X_122, X_1112, X_1122, X_1222) over Rational Field
        sage: U = L.pbw_basis()
        sage: Z = U.center()
        sage: it = iter(Z.basis())
        sage: center_elts = [next(it) for _ in range(10)]; center_elts
        [1, Z[0], Z[1], Z[2], Z[0]^2, Z[0]*Z[1], Z[0]*Z[2], Z[1]^2, Z[1]*Z[2], Z[2]^2]
        sage: elts = [U(v) for v in center_elts]; elts
        [1, PBW[(1, 1, 1, 2)], PBW[(1, 1, 2, 2)], PBW[(1, 2, 2, 2)], PBW[(1, 1, 1, 2)]^2,
         PBW[(1, 1, 1, 2)]*PBW[(1, 1, 2, 2)], PBW[(1, 1, 1, 2)]*PBW[(1, 2, 2, 2)],
         PBW[(1, 1, 2, 2)]^2, PBW[(1, 1, 2, 2)]*PBW[(1, 2, 2, 2)], PBW[(1, 2, 2, 2)]^2]
        sage: all(v * g == g * v for g in U.algebra_generators() for v in elts)
        True

    Using the Engel Lie algebra::

        sage: L.<X,Y,Z> = LieAlgebra(QQ, {('X','Y'): {'Z': 1}}, nilpotent=True)
        sage: U = L.pbw_basis()
        sage: Z = U.center()
        sage: it = iter(Z.basis())
        sage: center_elts = [next(it) for _ in range(6)]; center_elts
        [1, Z[0], Z[0]^2, Z[0]^3, Z[0]^4, Z[0]^5]
        sage: elts = [U(v) for v in center_elts]; elts
        [1, PBW['Z'], PBW['Z']^2, PBW['Z']^3, PBW['Z']^4, PBW['Z']^5]
        sage: all(v * g == g * v for g in U.algebra_generators() for v in elts)
        True
    """
    def __init__(self, g, UEA) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: g = LieAlgebra(ZZ['t'].fraction_field(), cartan_type=['D', 4])
            sage: U = g.pbw_basis()
            sage: Z = U.center()
            sage: TestSuite(Z).run()

            sage: g = lie_algebras.Heisenberg(GF(3), 4)
            sage: U = g.pbw_basis()
            sage: Z = U.center()
            sage: TestSuite(Z).run()
        """
    @cached_method
    def algebra_generators(self):
        """
        Return the algebra generators of ``self``.

        .. WARNING::

            When the universal enveloping algebra is not known to have
            a finite generating set, the generating set will be the basis
            of ``self`` in a degree (weakly) increasing order indexed by
            `\\ZZ_{\\geq 0}`. In particular, the `0`-th generator will be
            the multiplicative identity `1`.

        EXAMPLES::

            sage: g = lie_algebras.Heisenberg(QQ, 3)
            sage: U = g.pbw_basis()
            sage: Z = U.center()
            sage: Z.algebra_generators()[0]
            1
            sage: Z.algebra_generators()[1]
            Z[0]

            sage: g = LieAlgebra(QQ, cartan_type=['G', 2])
            sage: U = g.pbw_basis()
            sage: Z = U.center()
            sage: Z.algebra_generators()
            Finite family {0: Z[0], 1: Z[1]}
        """
    @cached_method
    def one_basis(self):
        """
        Return the basis index of `1` in ``self``.

        EXAMPLES::

            sage: g = LieAlgebra(QQ['t'].fraction_field(), cartan_type=['B', 5])
            sage: U = g.pbw_basis()
            sage: Z = U.center()
            sage: ob = Z.one_basis(); ob
            1
            sage: ob.parent() is Z.indices()
            True
        """
    def ambient(self):
        """
        Return the ambient algebra of ``self``.

        EXAMPLES::

            sage: g = LieAlgebra(GF(5), cartan_type=['A', 2])
            sage: U = g.pbw_basis()
            sage: Z = U.center()
            sage: Z.ambient() is U
            True
        """
    def product_on_basis(self, left, right):
        """
        Return the product of basis elements indexed by ``left`` and ``right``.

        EXAMPLES::

            sage: g = LieAlgebra(QQ, cartan_type=['E', 6])
            sage: U = g.pbw_basis()
            sage: Z = U.center()
            sage: mg = Z.indices().monoid_generators()
            sage: Z.product_on_basis(mg[1]*mg[2], mg[0]*mg[1]^3*mg[2]*mg[3]^3)
            Z[0]*Z[1]^4*Z[2]^2*Z[3]^3
        """
    def degree_on_basis(self, m):
        """
        Return the degree of the basis element indexed by ``m`` in ``self``.

        EXAMPLES::

            sage: g = LieAlgebra(QQ, cartan_type=['E', 6])
            sage: U = g.pbw_basis()
            sage: Z = U.center()
            sage: I = Z.indices()
            sage: it = iter(I)
            sage: supports = [next(it) for _ in range(10)]; supports
            [1, Z[0], Z[0]^2, Z[1], Z[2], Z[0]^3, Z[0]*Z[1], Z[3], Z[0]*Z[2], Z[0]^4]
            sage: [Z.degree_on_basis(m) for m in supports]
            [0, 2, 4, 5, 6, 6, 7, 8, 8, 8]
        """
    @lazy_attribute
    def lift(self):
        """
        The lift map from ``self`` to the universal enveloping algebra.

        EXAMPLES::

            sage: g = LieAlgebra(QQ, cartan_type=['A', 1])
            sage: U = g.pbw_basis()
            sage: Z = U.center()
            sage: gens = Z.algebra_generators()
            sage: U(gens[0]^2 + gens[0])
            4*PBW[alpha[1]]^2*PBW[-alpha[1]]^2
             + 2*PBW[alpha[1]]*PBW[alphacheck[1]]^2*PBW[-alpha[1]]
             + 1/4*PBW[alphacheck[1]]^4 - PBW[alphacheck[1]]^3
             - 2*PBW[alpha[1]]*PBW[-alpha[1]] + 1/2*PBW[alphacheck[1]]^2
             + PBW[alphacheck[1]]
            sage: U(-1/4*gens[0]) == U.casimir_element()
            True
        """
    def retract(self, elt):
        """
        The retraction map to ``self`` from the universal enveloping algebra.

        .. TODO::

            Implement a version of this that checks if the leading term of
            ``elt`` is divisible by a product of all of the currently known
            generators in order to avoid constructing the full centralizer
            of larger degrees than needed.

        EXAMPLES::

            sage: g = lie_algebras.Heisenberg(QQ, 3)
            sage: U = g.pbw_basis()
            sage: Z = U.center()
            sage: z0 = Z.algebra_generators()[1]; z0
            Z[0]
            sage: Z.retract(U(z0^2) - U(3*z0))
            Z[0]^2 - 3*Z[0]

            sage: g = LieAlgebra(QQ, cartan_type=['A', 2])
            sage: U = g.pbw_basis()
            sage: Z = U.center()
            sage: z0, z1 = Z.algebra_generators()
            sage: Z.retract(U(z0*z0) - U(z1))  # long time
            Z[0]^2 - Z[1]
            sage: zc = Z.retract(U.casimir_element()); zc
            -1/3*Z[0]
            sage: U(zc) == U.casimir_element()
            True
        """
