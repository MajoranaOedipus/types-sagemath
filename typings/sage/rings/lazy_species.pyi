from _typeshed import Incomplete
from collections.abc import Generator
from sage.arith.misc import divisors as divisors, multinomial as multinomial
from sage.categories.tensor import tensor as tensor
from sage.combinat.integer_vector import IntegerVectors as IntegerVectors
from sage.combinat.partition import Partitions as Partitions
from sage.combinat.permutation import CyclicPermutations as CyclicPermutations
from sage.combinat.set_partition import SetPartitions as SetPartitions
from sage.combinat.sf.sf import SymmetricFunctions as SymmetricFunctions
from sage.combinat.subset import subsets as subsets
from sage.data_structures.stream import Stream_exact as Stream_exact, Stream_function as Stream_function, Stream_truncated as Stream_truncated, Stream_zero as Stream_zero
from sage.functions.other import binomial as binomial, factorial as factorial
from sage.graphs.graph_generators import graphs as graphs
from sage.groups.perm_gps.permgroup import PermutationGroup as PermutationGroup
from sage.groups.perm_gps.permgroup_named import AlternatingGroup as AlternatingGroup, CyclicPermutationGroup as CyclicPermutationGroup, DihedralGroup as DihedralGroup, SymmetricGroup as SymmetricGroup
from sage.misc.inherit_comparison import InheritComparisonClasscallMetaclass as InheritComparisonClasscallMetaclass
from sage.misc.lazy_list import lazy_list as lazy_list
from sage.misc.misc_c import prod as prod
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.lazy_series import LazyCompletionGradedAlgebraElement as LazyCompletionGradedAlgebraElement, LazyModuleElement as LazyModuleElement
from sage.rings.lazy_series_ring import LazyCompletionGradedAlgebra as LazyCompletionGradedAlgebra, LazyPowerSeriesRing as LazyPowerSeriesRing, LazySymmetricFunctions as LazySymmetricFunctions
from sage.rings.rational_field import QQ as QQ
from sage.rings.species import PolynomialSpecies as PolynomialSpecies
from sage.structure.element import parent as parent
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

def weighted_compositions(n, d, weight_multiplicities, _w0: int = 0) -> Generator[Incomplete]:
    """
    Return all compositions of `n` of weight `d`.

    The weight of a composition `n_1, n_2, \\dots` is `\\sum_i w_i n_i`.

    INPUT:

    - ``n`` -- nonnegative integer; the sum of the parts
    - ``d`` -- nonnegative integer; the total weight
    - ``weight_multiplicities`` -- iterable;
      ``weight_multiplicities[i]`` is the number of positions with
      weight ``i+1``

    .. TODO::

        Possibly this could be merged with
        :class:`~sage.combinat.integer_vector_weighted.WeightedIntegerVectors`.
        However, that class does not support fixing the sum of the
        parts currently.

    EXAMPLES::

        sage: from sage.rings.lazy_species import weighted_compositions
        sage: list(weighted_compositions(1, 1, [2,1]))
        [[1, 0], [0, 1]]

        sage: list(weighted_compositions(2, 1, [2,1]))
        []

        sage: list(weighted_compositions(1, 2, [2,1,1]))
        [[0, 0, 1]]

        sage: list(weighted_compositions(3, 4, [2,2]))
        [[2, 0, 1, 0],
         [1, 1, 1, 0],
         [0, 2, 1, 0],
         [2, 0, 0, 1],
         [1, 1, 0, 1],
         [0, 2, 0, 1]]
    """
def weighted_vector_compositions(n_vec, d, weight_multiplicities_vec) -> Generator[Incomplete, Incomplete]:
    """
    Return all compositions of the vector `n` of weight `d`.

    INPUT:

    - ``n_vec`` -- a `k`-tuple of non-negative integers

    - ``d`` -- a non-negative integer, the total sum of the parts in
      all components

    - ``weight_multiplicities_vec`` -- `k`-tuple of iterables, where
      ``weight_multiplicities_vec[j][i]`` is the number of
      positions with weight `i+1` in the `j`-th component

    EXAMPLES::

        sage: from sage.rings.lazy_species import weighted_vector_compositions
        sage: list(weighted_vector_compositions([1,1], 2, [[2,1,1], [1,1,1]]))
        [([1, 0], [1]), ([0, 1], [1])]

        sage: list(weighted_vector_compositions([3,1], 4, [[2,1,0,0,1], [2,1,0,0,1]]))
        [([3, 0], [1, 0]),
         ([3, 0], [0, 1]),
         ([2, 1], [1, 0]),
         ([2, 1], [0, 1]),
         ([1, 2], [1, 0]),
         ([1, 2], [0, 1]),
         ([0, 3], [1, 0]),
         ([0, 3], [0, 1])]
    """

class LazyCombinatorialSpeciesElement(LazyCompletionGradedAlgebraElement):
    '''
    EXAMPLES:

    Compute the molecular expansion of `E(-X)`::

        sage: L = LazyCombinatorialSpecies(ZZ, "X")
        sage: E = L(SymmetricGroup)
        sage: E_inv = 1 / E
        sage: E_inv
        1 + (-X) + (-E_2+X^2) + (-E_3+2*X*E_2-X^3)
          + (-E_4+2*X*E_3+E_2^2-3*X^2*E_2+X^4)
          + (-E_5+2*X*E_4+2*E_2*E_3-3*X^2*E_3-3*X*E_2^2+4*X^3*E_2-X^5)
          + (-E_6+2*X*E_5+2*E_2*E_4-3*X^2*E_4+E_3^2-6*X*E_2*E_3+4*X^3*E_3-E_2^3+6*X^2*E_2^2-5*X^4*E_2+X^6)
          + O^7

    Compare with the explicit formula::

        sage: def coefficient(m):
        ....:     return sum((-1)^len(la) * multinomial((n := la.to_exp())) * prod(E[i]^ni for i, ni in enumerate(n, 1)) for la in Partitions(m))

        sage: all(coefficient(m) == E_inv[m] for m in range(10))
        True
    '''
    def isotype_generating_series(self):
        '''
        Return the isotype generating series of ``self``.

        EXAMPLES::

            sage: L = LazyCombinatorialSpecies(QQ, "X")
            sage: E = L(SymmetricGroup)
            sage: E.isotype_generating_series()
            1 + X + X^2 + X^3 + X^4 + X^5 + X^6 + O(X^7)

            sage: C = L(CyclicPermutationGroup, valuation=1)
            sage: E(C).isotype_generating_series()
            1 + X + 2*X^2 + 3*X^3 + 5*X^4 + 7*X^5 + 11*X^6 + O(X^7)

            sage: L2.<X, Y> = LazyCombinatorialSpecies(QQ)
            sage: E(X + Y).isotype_generating_series()
            1 + (X+Y) + (X^2+X*Y+Y^2) + (X^3+X^2*Y+X*Y^2+Y^3)
            + (X^4+X^3*Y+X^2*Y^2+X*Y^3+Y^4)
            + (X^5+X^4*Y+X^3*Y^2+X^2*Y^3+X*Y^4+Y^5)
            + (X^6+X^5*Y+X^4*Y^2+X^3*Y^3+X^2*Y^4+X*Y^5+Y^6)
            + O(X,Y)^7

            sage: C(X + Y).isotype_generating_series()
            (X+Y) + (X^2+X*Y+Y^2) + (X^3+X^2*Y+X*Y^2+Y^3)
            + (X^4+X^3*Y+2*X^2*Y^2+X*Y^3+Y^4)
            + (X^5+X^4*Y+2*X^3*Y^2+2*X^2*Y^3+X*Y^4+Y^5)
            + (X^6+X^5*Y+3*X^4*Y^2+4*X^3*Y^3+3*X^2*Y^4+X*Y^5+Y^6)
            + O(X,Y)^7
        '''
    def generating_series(self):
        '''
        Return the (exponential) generating series of ``self``.

        EXAMPLES::

            sage: L = LazyCombinatorialSpecies(QQ, "X")
            sage: E = L.Sets()
            sage: E.generating_series()
            1 + X + 1/2*X^2 + 1/6*X^3 + 1/24*X^4 + 1/120*X^5 + 1/720*X^6 + O(X^7)

            sage: C = L.Cycles()
            sage: C.generating_series()
            X + 1/2*X^2 + 1/3*X^3 + 1/4*X^4 + 1/5*X^5 + 1/6*X^6 + 1/7*X^7 + O(X^8)

            sage: L2.<X, Y> = LazyCombinatorialSpecies(QQ)
            sage: E(X + Y).generating_series()
            1 + (X+Y) + (1/2*X^2+X*Y+1/2*Y^2)
            + (1/6*X^3+1/2*X^2*Y+1/2*X*Y^2+1/6*Y^3)
            + (1/24*X^4+1/6*X^3*Y+1/4*X^2*Y^2+1/6*X*Y^3+1/24*Y^4)
            + (1/120*X^5+1/24*X^4*Y+1/12*X^3*Y^2+1/12*X^2*Y^3+1/24*X*Y^4+1/120*Y^5)
            + (1/720*X^6+1/120*X^5*Y+1/48*X^4*Y^2+1/36*X^3*Y^3+1/48*X^2*Y^4+1/120*X*Y^5+1/720*Y^6)
            + O(X,Y)^7

            sage: C(X + Y).generating_series()
            (X+Y) + (1/2*X^2+X*Y+1/2*Y^2) + (1/3*X^3+X^2*Y+X*Y^2+1/3*Y^3)
            + (1/4*X^4+X^3*Y+3/2*X^2*Y^2+X*Y^3+1/4*Y^4)
            + (1/5*X^5+X^4*Y+2*X^3*Y^2+2*X^2*Y^3+X*Y^4+1/5*Y^5)
            + (1/6*X^6+X^5*Y+5/2*X^4*Y^2+10/3*X^3*Y^3+5/2*X^2*Y^4+X*Y^5+1/6*Y^6)
            + (1/7*X^7+X^6*Y+3*X^5*Y^2+5*X^4*Y^3+5*X^3*Y^4+3*X^2*Y^5+X*Y^6+1/7*Y^7)
            + O(X,Y)^8
        '''
    def cycle_index_series(self):
        '''
        Return the cycle index series for this species.

        EXAMPLES::

            sage: L = LazyCombinatorialSpecies(ZZ, "X")
            sage: E = L.Sets()
            sage: h = SymmetricFunctions(QQ).h()
            sage: LazySymmetricFunctions(h)(E.cycle_index_series())
            h[] + h[1] + h[2] + h[3] + h[4] + h[5] + h[6] + O^7

            sage: s = SymmetricFunctions(QQ).s()
            sage: C = L.Cycles()
            sage: s(C.cycle_index_series()[5])
            s[1, 1, 1, 1, 1] + s[2, 2, 1] + 2*s[3, 1, 1] + s[3, 2] + s[5]

            sage: L = LazyCombinatorialSpecies(QQ, "X")
            sage: E = L.Sets()
            sage: L2.<X, Y> = LazyCombinatorialSpecies(QQ)
            sage: E(X + Y).cycle_index_series()[3]
            1/6*p[] # p[1, 1, 1] + 1/2*p[] # p[2, 1] + 1/3*p[] # p[3]
            + 1/2*p[1] # p[1, 1] + 1/2*p[1] # p[2] + 1/2*p[1, 1] # p[1]
            + 1/6*p[1, 1, 1] # p[] + 1/2*p[2] # p[1] + 1/2*p[2, 1] # p[]
            + 1/3*p[3] # p[]
        '''
    def restrict(self, min_degree=None, max_degree=None):
        '''
        Return the series obtained by keeping only terms of
        degree between ``min_degree`` and ``max_degree``.

        INPUT:

        - ``min_degree``, ``max_degree`` -- (optional) integers
          indicating which degrees to keep

        EXAMPLES::

            sage: L = LazyCombinatorialSpecies(ZZ, "X")
            sage: G = L.Graphs()
            sage: list(G.isotypes(2))
            [Graph on 2 vertices, Graph on 2 vertices]

            sage: list(G.restrict(2, 2).isotypes(2))
            [Graph on 2 vertices, Graph on 2 vertices]
        '''
    def structures(self, *labels) -> Generator[Incomplete, Incomplete]:
        '''
        Iterate over the structures on the given set of labels.

        Generically, this yields a list of pairs consisting of a
        molecular species and a relabelled representative of the
        cosets of corresponding groups.

        The relabelling is such that the first few labels correspond
        to the first factor in the atomic decomposition, etc.

        EXAMPLES::

            sage: L = LazyCombinatorialSpecies(QQ, "X")
            sage: E = L(SymmetricGroup)
            sage: list(E.structures([1,2,3]))
            [(E_3, ((1, 2, 3),))]

            sage: C = L(CyclicPermutationGroup, valuation=1)
            sage: list(C.structures([1,2,3]))
            [(C_3, ((1, 2, 3),)), (C_3, ((1, 3, 2),))]

            sage: F = 1/(2-E)
            sage: sorted(F.structures([1,2,3]))
            [(E_3, ((1, 2, 3),)),
             (X*E_2, ((1,), (2, 3)), 0),
             (X*E_2, ((1,), (2, 3)), 1),
             (X*E_2, ((2,), (1, 3)), 0),
             (X*E_2, ((2,), (1, 3)), 1),
             (X*E_2, ((3,), (1, 2)), 0),
             (X*E_2, ((3,), (1, 2)), 1),
             (X^3, ((1,), (2,), (3,))),
             (X^3, ((1,), (3,), (2,))),
             (X^3, ((2,), (1,), (3,))),
             (X^3, ((2,), (3,), (1,))),
             (X^3, ((3,), (1,), (2,))),
             (X^3, ((3,), (2,), (1,)))]

            sage: from sage.rings.species import PolynomialSpecies
            sage: L = LazyCombinatorialSpecies(QQ, "X, Y")
            sage: P = PolynomialSpecies(QQ, "X, Y")
            sage: XY = L(P(PermutationGroup([], domain=[1, 2]), {0: [1], 1: [2]}))
            sage: list((XY).structures([1], ["a"]))
            [(X*Y, ((1,), (\'a\',)))]

            sage: sorted(E(XY).structures([1,2], [3, 4]))
            [((E_2, ((((1, \'X\'), (3, \'Y\')), ((2, \'X\'), (4, \'Y\'))),)),
              ((X*Y, ((1,), (3,))), (X*Y, ((2,), (4,))))),
             ((E_2, ((((1, \'X\'), (4, \'Y\')), ((2, \'X\'), (3, \'Y\'))),)),
              ((X*Y, ((1,), (4,))), (X*Y, ((2,), (3,)))))]

            sage: list(XY.structures([], [1, 2]))
            []
        '''
    def isotypes(self, *shape) -> Generator[Incomplete]:
        '''
        Iterate over the isotypes on the given list of sizes.

        Generically, this yields a list of tuples consisting of a
        molecular species and, if necessary, an index.

        EXAMPLES::

            sage: L = LazyCombinatorialSpecies(QQ, "X")
            sage: E = L(SymmetricGroup)
            sage: list(E.isotypes(3))
            [(E_3,)]

            sage: P = L(CyclicPermutationGroup, valuation=1)
            sage: list(P.isotypes(3))
            [(C_3,)]

            sage: F = 1/(2-E)
            sage: sorted(F.isotypes(3))
            [(E_3,), (X*E_2, 0), (X*E_2, 1), (X^3,)]

            sage: from sage.rings.species import PolynomialSpecies
            sage: L = LazyCombinatorialSpecies(QQ, "X, Y")
            sage: P = PolynomialSpecies(QQ, "X, Y")
            sage: XY = L(P(PermutationGroup([], domain=[1, 2]), {0: [1], 1: [2]}))
            sage: list((XY).isotypes(1, 1))
            [(X*Y,)]

            sage: list(E(XY).isotypes(2, 2))
            [(E_2(X*Y),)]
        '''
    def polynomial(self, degree=None, names=None):
        '''
        Return ``self`` as a polynomial if ``self`` is actually so or up to
        specified degree.

        INPUT:

        - ``degree`` -- (optional) integer
        - ``names`` -- (default: name of the variables of the series) names of the variables

        OUTPUT:

        If ``degree`` is not ``None``, the terms of the series of
        degree greater than ``degree`` are first truncated.  If
        ``degree`` is ``None`` and the series is not a polynomial
        polynomial, a ``ValueError`` is raised.

        EXAMPLES::

            sage: L = LazyCombinatorialSpecies(ZZ, "X")
            sage: E = L(SymmetricGroup)
            sage: E.polynomial(3)
            1 + X + E_2 + E_3
        '''
    def __call__(self, *args):
        '''
        Evaluate ``self`` at ``*args``.

        EXAMPLES::

            sage: L.<X> = LazyCombinatorialSpecies(QQ)
            sage: E2 = L(SymmetricGroup(2))
            sage: E2(E2)
            E_2(E_2) + O^11

            sage: E = L.Sets()
            sage: A = L.undefined(1)
            sage: A.define(X*E(A))
            sage: A[5]  # random
            X*E_4 + X^2*E_3 + 3*X^3*E_2 + X*E_2(X^2) + 3*X^5
            sage: A[5] == X*E[4] + X^2*E[3] + 3*X^3*E[2] + X*E[2](X[1]^2) + 3*X^5
            True

            sage: C = L.Cycles()
            sage: F = E(C(A))
            sage: [sum(F[n].monomial_coefficients().values()) for n in range(1, 7)]
            [1, 3, 7, 19, 47, 130]
            sage: oeis(_)  # optional -- internet
            0: A001372: Number of unlabeled mappings (or mapping patterns)
             from n points to themselves; number of unlabeled endofunctions.

            sage: R.<q> = QQ[]
            sage: L = LazyCombinatorialSpecies(R, "X")
            sage: E = L.Sets()
            sage: E1 = E.restrict(1)
            sage: E(q*E1)[4]
            (q^4+q)*E_4 + q^2*E_2(E_2) + q^2*X*E_3 + q^3*E_2^2

        TESTS::

            sage: L.<X> = LazyCombinatorialSpecies(QQ)
            sage: E2 = L(SymmetricGroup(2))
            sage: X(X + E2)
            X + E_2 + O^8
            sage: E2(X + E2)
            E_2 + X*E_2 + E_2(E_2) + O^9

            sage: from sage.rings.species import PolynomialSpecies
            sage: P = PolynomialSpecies(QQ, "X")
            sage: Gc = L(lambda n: sum(P(G.automorphism_group()) for G in graphs(n) if G.is_connected()) if n else 0)
            sage: E = L.Sets()
            sage: G = L.Graphs()
            sage: E(Gc) - G
            O^7

            sage: (1+E2)(X)
            1 + E_2 + O^7

            sage: L.<X,Y> = LazyCombinatorialSpecies(QQ)
            sage: X(Y, 0)
            Y + O^8

            sage: L1 = LazyCombinatorialSpecies(QQ, "X")
            sage: E = L1.Sets()
            sage: L.<X,Y> = LazyCombinatorialSpecies(QQ)
            sage: E(X)
            1 + X + E_2(X) + E_3(X) + E_4(X) + E_5(X) + E_6(X) + O^7

        It would be extremely nice to allow the following, but this
        poses theoretical problems::

            sage: L.<X> = LazyCombinatorialSpecies(QQ)
            sage: E1 = L.Sets().restrict(1)
            sage: Omega = L.undefined(1)
            sage: L.define_implicitly([Omega], [E1(Omega) - X])
            sage: Omega[1]  # not tested
        '''
    def revert(self):
        """
        Return the compositional inverse of ``self``.

        EXAMPLES::

            sage: L.<X> = LazyCombinatorialSpecies(QQ)
            sage: E1 = L.Sets().restrict(1)
            sage: g = E1.revert()
            sage: g[:5]
            [X, -E_2, -E_3 + X*E_2, -E_4 + E_2(E_2) + X*E_3 - X^2*E_2]

            sage: E = L.Sets()
            sage: P = E(X*E1(-X))*(1+X) - 1
            sage: P.revert()[:5]
            [X, X^2, X*E_2 + 2*X^3, X*E_3 + 2*X^2*E_2 + E_2(X^2) + 5*X^4]

        TESTS::

            sage: (3 + 2*X).revert()
            (-3/2) + 1/2*X
        """
    compositional_inverse = revert
    def combinatorial_logarithm(self):
        """
        Return the combinatorial logarithm of ``self``.

        This is the series reversion of the species of non-empty sets
        applied to ``self - 1``.

        EXAMPLES::

            sage: L.<X> = LazyCombinatorialSpecies(QQ)
            sage: L.Sets().restrict(1).revert() - (1+X).combinatorial_logarithm()
            O^7

        This method is much faster, however::

            sage: (1+X).combinatorial_logarithm().generating_series()[10]
            -1/10
        """

class LazyCombinatorialSpeciesElementGeneratingSeriesMixin:
    '''
    A lazy species element whose generating series are obtained
    by specializing the cycle index series rather than the molecular
    expansion.

    TESTS:

    We check that the series are correct even if the cycle index
    series are not in the powersum basis::

        sage: from sage.rings.lazy_species import LazyCombinatorialSpeciesElement, LazyCombinatorialSpeciesElementGeneratingSeriesMixin
        sage: class F(LazyCombinatorialSpeciesElementGeneratingSeriesMixin, LazyCombinatorialSpeciesElement):
        ....:     def __init__(self, parent):
        ....:         super().__init__(parent, parent(PermutationGroup([], domain=[1,2])))
        ....:     def cycle_index_series(self):
        ....:         s = SymmetricFunctions(QQ).s()
        ....:         L = LazySymmetricFunctions(s)
        ....:         return L(s[1, 1] + s[2])

        sage: L = LazyCombinatorialSpecies(QQ, "X")
        sage: F(L).generating_series()
        X^2 + O(X^7)

        sage: F(L).isotype_generating_series()
        X^2 + O(X^7)
        sage: TestSuite(F(L)).run(skip=[\'_test_category\', \'_test_pickling\'])


        sage: class F(LazyCombinatorialSpeciesElementGeneratingSeriesMixin, LazyCombinatorialSpeciesElement):
        ....:     def __init__(self, parent):
        ....:         G = PermutationGroup([], domain=[1,2,3,4])
        ....:         pi = {0:[1,2],1:[3,4]}
        ....:         P = parent._laurent_poly_ring
        ....:         super().__init__(parent, parent(P(G, pi)))
        ....:     def cycle_index_series(self):
        ....:         s = SymmetricFunctions(QQ).s()
        ....:         L = LazySymmetricFunctions(tensor([s, s]))
        ....:         return L(self[4].support()[0].cycle_index())

        sage: L = LazyCombinatorialSpecies(QQ, "X, Y")
        sage: F(L).isotype_generating_series()
        X^2*Y^2 + O(X,Y)^7

        sage: F(L).generating_series()
        X^2*Y^2 + O(X,Y)^7

        sage: TestSuite(F(L)).run(skip=[\'_test_category\', \'_test_pickling\'])
    '''
    def isotype_generating_series(self):
        '''
        Return the isotype generating series of ``self``.

        The series is obtained by applying the principal
        specialization of order `1` to the cycle index series, that
        is, setting `x_1 = x` and `x_k = 0` for `k > 1`.

        EXAMPLES::

            sage: L = LazyCombinatorialSpecies(QQ, "X")
            sage: L.Graphs().isotype_generating_series().truncate(8)
            1 + X + 2*X^2 + 4*X^3 + 11*X^4 + 34*X^5 + 156*X^6 + 1044*X^7

        TESTS::

            sage: L.Graphs().isotype_generating_series()[20]
            645490122795799841856164638490742749440
        '''
    def generating_series(self):
        '''
        Return the (exponential) generating series of ``self``.

        The series is obtained by applying the exponential
        specialization to the cycle index series.

        EXAMPLES::

            sage: L = LazyCombinatorialSpecies(QQ, "X")
            sage: L.Graphs().generating_series().truncate(7)
            1 + X + X^2 + 4/3*X^3 + 8/3*X^4 + 128/15*X^5 + 2048/45*X^6
        '''

class SumSpeciesElement(LazyCombinatorialSpeciesElement):
    def __init__(self, left, right) -> None:
        '''
        Initialize the sum of two species.

        EXAMPLES::

            sage: L = LazyCombinatorialSpecies(QQ, "X")
            sage: F = L.Sets() + L.SetPartitions()
            sage: TestSuite(F).run(skip=[\'_test_category\', \'_test_pickling\'])
        '''
    def structures(self, *labels) -> Generator[Incomplete, Incomplete]:
        '''
        Iterate over the structures on the given set of labels.

        EXAMPLES::

            sage: L = LazyCombinatorialSpecies(QQ, "X")
            sage: F = L.Sets() + L.SetPartitions()
            sage: list(F.structures([1,2,3]))
            [((1, 2, 3), \'left\'),
             ({{1, 2, 3}}, \'right\'),
             ({{1, 2}, {3}}, \'right\'),
             ({{1, 3}, {2}}, \'right\'),
             ({{1}, {2, 3}}, \'right\'),
             ({{1}, {2}, {3}}, \'right\')]
        '''
    def generating_series(self):
        '''
        Return the (exponential) generating series of ``self``.

        EXAMPLES::

            sage: L = LazyCombinatorialSpecies(QQ, "X")
            sage: F = L.Sets() + L.SetPartitions()
            sage: F.generating_series()
            2 + 2*X + 3/2*X^2 + X^3 + 2/3*X^4 + 53/120*X^5 + 17/60*X^6 + O(X^7)

        TESTS::

            sage: F.generating_series()[20]
            3978781402721/187146308321280000
        '''
    def isotype_generating_series(self):
        '''
        Return the isotype generating series of ``self``.

        EXAMPLES::

            sage: L = LazyCombinatorialSpecies(QQ, "X")
            sage: F = L.Sets() + L.SetPartitions()
            sage: F.isotype_generating_series()
            2 + 2*X + 3*X^2 + 4*X^3 + 6*X^4 + 8*X^5 + 12*X^6 + O(X^7)

        TESTS::

            sage: F.isotype_generating_series()[20]
            628
        '''

class ProductSpeciesElement(LazyCombinatorialSpeciesElement):
    def __init__(self, left, right) -> None:
        '''
        Initialize the product of two species.

        EXAMPLES::

            sage: L = LazyCombinatorialSpecies(QQ, "X")
            sage: F = L.Sets() * L.SetPartitions()
            sage: TestSuite(F).run(skip=[\'_test_category\', \'_test_pickling\'])
        '''
    def structures(self, *labels) -> Generator[Incomplete, Incomplete]:
        '''
        Iterate over the structures on the given set of labels.

        EXAMPLES::

            sage: L = LazyCombinatorialSpecies(ZZ, "X")
            sage: E = L.Sets()
            sage: C = L.Cycles()
            sage: P = E * C
            sage: list(P.structures([1,2]))
            [((), (1, 2)), ((1,), (2,)), ((2,), (1,))]

            sage: P = E * E
            sage: list(P.structures([1,2]))
            [((), (1, 2)), ((1,), (2,)), ((2,), (1,)), ((1, 2), ())]

            sage: L.<X, Y> = LazyCombinatorialSpecies(QQ)
            sage: list((X*Y).structures([1], [2]))
            [((X, ((1,),)), (Y, ((2,),)))]
        '''
    def generating_series(self):
        '''
        Return the (exponential) generating series of ``self``.

        EXAMPLES::

            sage: L = LazyCombinatorialSpecies(QQ, "X")
            sage: E = L.Sets()
            sage: F = E*E
            sage: F.generating_series()
            1 + 2*X + 2*X^2 + 4/3*X^3 + 2/3*X^4 + 4/15*X^5 + 4/45*X^6 + O(X^7)
        '''
    def isotype_generating_series(self):
        '''
        Return the isotype generating series of ``self``.

        EXAMPLES::

            sage: L = LazyCombinatorialSpecies(QQ, "X")
            sage: E = L.Sets()
            sage: F = E*E
            sage: F.isotype_generating_series()
            1 + 2*X + 3*X^2 + 4*X^3 + 5*X^4 + 6*X^5 + 7*X^6 + O(X^7)
        '''

class CompositionSpeciesElement(LazyCombinatorialSpeciesElementGeneratingSeriesMixin, LazyCombinatorialSpeciesElement):
    def __init__(self, left, *args) -> None:
        """
        Initialize the composition of species.

        TESTS::

            sage: L.<X> = LazyCombinatorialSpecies(QQ)
            sage: L.zero()(X)
            0
            sage: X(L.zero())
            0
            sage: (1+X)(L.zero())
            1

            sage: L2.<X,Y> = LazyCombinatorialSpecies(QQ)
            sage: F = L.Sets()(X + 2*Y)
            sage: TestSuite(F).run(skip=['_test_category', '_test_pickling'])
        """
    def structures(self, *labels) -> Generator[Incomplete, Incomplete, Incomplete]:
        '''
        Iterate over the structures on the given set of labels.

        EXAMPLES::

            sage: L = LazyCombinatorialSpecies(QQ, "X")
            sage: E = L.Sets()
            sage: E1 = L.Sets().restrict(1)
            sage: sorted(E(E1).structures([1,2,3]))
            [((((1, \'X\'),), ((2, \'X\'),), ((3, \'X\'),)), ((1,), (2,), (3,))),
             ((((1, \'X\'),), ((2, \'X\'), (3, \'X\'))), ((1,), (2, 3))),
             ((((1, \'X\'), (2, \'X\')), ((3, \'X\'),)), ((1, 2), (3,))),
             ((((1, \'X\'), (2, \'X\'), (3, \'X\')),), ((1, 2, 3),)),
             ((((1, \'X\'), (3, \'X\')), ((2, \'X\'),)), ((1, 3), (2,)))]

            sage: C = L.Cycles()
            sage: L.<X, Y> = LazyCombinatorialSpecies(QQ)
            sage: sum(1 for s in C(X*Y).structures([1,2,3], [1,2,3]))
            12

            sage: C(X*Y).generating_series()[6]
            1/3*X^3*Y^3

            sage: sum(1 for s in E(X*Y).structures([1,2,3], ["a", "b", "c"]))
            6
        '''
    def generating_series(self):
        '''
        Return the (exponential) generating series of ``self``.

        EXAMPLES::

            sage: L = LazyCombinatorialSpecies(QQ, "X")
            sage: E = L.Sets()
            sage: F = E(E.restrict(1))
            sage: F.generating_series()
            1 + X + X^2 + 5/6*X^3 + 5/8*X^4 + 13/30*X^5 + 203/720*X^6 + O(X^7)
        '''
    def cycle_index_series(self):
        '''
        Return the cycle index series for this species.

        EXAMPLES::

            sage: L = LazyCombinatorialSpecies(QQ, "X")
            sage: E = L.Sets()
            sage: F = E(E.restrict(1))
            sage: F.cycle_index_series()[5]
            h[2, 2, 1] - h[3, 1, 1] + 3*h[3, 2] + 2*h[4, 1] + 2*h[5]
        '''

class LazyCombinatorialSpecies(LazyCompletionGradedAlgebra):
    Element = LazyCombinatorialSpeciesElement
    @staticmethod
    def __classcall_private__(cls, base_ring, names, sparse: bool = True):
        '''
        Normalize input to ensure a unique representation.

        TESTS::

            sage: LazyCombinatorialSpecies(QQ, "X") is LazyCombinatorialSpecies(QQ, "X")
            True
        '''
    def __init__(self, base_ring, names, sparse) -> None:
        '''
        The ring of lazy species.

        EXAMPLES:

        We provide univariate and multivariate (mostly known as
        multisort) species::

            sage: LazyCombinatorialSpecies(QQ, "X")
            Lazy completion of Polynomial species in X over Rational Field

            sage: LazyCombinatorialSpecies(QQ, "X, Y")
            Lazy completion of Polynomial species in X, Y over Rational Field

        In the univariate case, several basic species are provided as
        methods::

            sage: L = LazyCombinatorialSpecies(QQ, "X")
            sage: L.Sets()
            Set species
            sage: L.Cycles()
            Cycle species
            sage: L.OrientedSets()
            Oriented Set species
            sage: L.Polygons()
            Polygon species
            sage: L.Graphs()
            Graph species
            sage: L.SetPartitions()
            Set Partition species

        TESTS::

            sage: LazyCombinatorialSpecies(QQ, "X, Y, Z")._arity
            3
        '''

class LazyCombinatorialSpeciesUnivariate(LazyCombinatorialSpecies):
    def Sets(self):
        '''
        Return the species of sets.

        This species corresponds to the sequence of trivial group
        actions.  Put differently, the stabilizers are the full
        symmetric groups.

        EXAMPLES::

            sage: L = LazyCombinatorialSpecies(QQ, "X")
            sage: G = L.Sets()
            sage: set(G.isotypes(4))
            {(E_4,)}
            sage: set(G.structures(["a", 1, x]))
            {(1, \'a\', x)}
        '''
    def Cycles(self):
        '''
        Return the species of (oriented) cycles.

        This species corresponds to the sequence of group actions
        having the cyclic groups as stabilizers.

        EXAMPLES::

            sage: L = LazyCombinatorialSpecies(QQ, "X")
            sage: G = L.Cycles()
            sage: set(G.isotypes(4))
            {(C_4,)}
            sage: set(G.structures(["a", "b", "c"]))
            {(\'a\', \'b\', \'c\'), (\'a\', \'c\', \'b\')}
        '''
    def Polygons(self):
        '''
        Return the species of polygons.

        Polygons are cycles up to orientation.

        This species corresponds to the sequence of group actions
        having the dihedral groups as stabilizers.

        EXAMPLES::

            sage: L = LazyCombinatorialSpecies(QQ, "X")
            sage: G = L.Polygons()
            sage: set(G.isotypes(5))
            {(P_5,)}
            sage: set(G.structures(["a", 1, "b", 2]))
            {(E_2(E_2), ((1, \'a\', 2, \'b\'),)),
             (E_2(E_2), ((1, \'b\', 2, \'a\'),)),
             (E_2(E_2), ((1, 2, \'a\', \'b\'),))}
        '''
    def OrientedSets(self):
        '''
        Return the species of oriented sets.

        Oriented sets are total orders up to an even orientation.

        This species corresponds to the sequence of group actions
        having the alternating groups as stabilizers.

        EXAMPLES::

            sage: L = LazyCombinatorialSpecies(QQ, "X")
            sage: G = L.OrientedSets()
            sage: set(G.isotypes(5))
            {(Eo_5,)}
            sage: set(G.structures(["a", 1, "b", 2]))
            {(Eo_4, ((1, 2, \'a\', \'b\'),)), (Eo_4, ((1, 2, \'b\', \'a\'),))}
        '''
    def Chains(self):
        '''
        Return the species of chains.

        Chains are linear orders up to reversal.

        EXAMPLES::

            sage: L = LazyCombinatorialSpecies(QQ, "X")
            sage: Ch = L.Chains()
            sage: set(Ch.isotypes(4))
            {(E_2(X^2),)}
            sage: list(Ch.structures(["a", "b", "c"]))
            [(\'a\', \'c\', \'b\'), (\'a\', \'b\', \'c\'), (\'b\', \'a\', \'c\')]
        '''
    def Graphs(self):
        '''
        Return the species of vertex labelled simple graphs.

        EXAMPLES::

            sage: L = LazyCombinatorialSpecies(QQ, "X")
            sage: G = L.Graphs()
            sage: set(G.isotypes(2))
            {Graph on 2 vertices, Graph on 2 vertices}

            sage: G.isotype_generating_series()[20]
            645490122795799841856164638490742749440
        '''
    def SetPartitions(self):
        '''
        Return the species of set partitions.

        EXAMPLES::

            sage: L = LazyCombinatorialSpecies(QQ, "X")
            sage: G = L.SetPartitions()
            sage: set(G.isotypes(4))
            {[1, 1, 1, 1], [2, 1, 1], [2, 2], [3, 1], [4]}
            sage: list(G.structures(["a", "b", "c"]))
            [{{\'a\', \'b\', \'c\'}},
             {{\'a\', \'b\'}, {\'c\'}},
             {{\'a\', \'c\'}, {\'b\'}},
             {{\'a\'}, {\'b\', \'c\'}},
             {{\'a\'}, {\'b\'}, {\'c\'}}]
        '''

class LazyCombinatorialSpeciesMultivariate(LazyCombinatorialSpecies): ...

class SetSpecies(LazyCombinatorialSpeciesElement, UniqueRepresentation, metaclass=InheritComparisonClasscallMetaclass):
    def __init__(self, parent) -> None:
        '''
        Initialize the species of sets.

        TESTS::

            sage: L = LazyCombinatorialSpecies(QQ, "X")
            sage: E = L.Sets()
            sage: TestSuite(E).run(skip=[\'_test_category\', \'_test_pickling\'])

            sage: E is L.Sets()
            True
        '''
    def structures(self, labels) -> Generator[Incomplete]:
        '''
        Iterate over the structures on the given set of labels.

        EXAMPLES::

            sage: L = LazyCombinatorialSpecies(ZZ, "X")
            sage: E = L.Sets()
            sage: list(E.structures([1,2,3]))
            [(1, 2, 3)]
        '''
    def generating_series(self):
        """
        Return the (exponential) generating series of the
        species of sets.

        This is the exponential.

        EXAMPLES::

            sage: L.<X> = LazyCombinatorialSpecies(QQ)
            sage: L.Sets().generating_series()
            1 + X + 1/2*X^2 + 1/6*X^3 + 1/24*X^4 + 1/120*X^5 + 1/720*X^6 + O(X^7)
        """
    def isotype_generating_series(self):
        '''
        Return the isotype generating series of the species of
        sets.

        This is the geometric series.

        EXAMPLES::

            sage: L = LazyCombinatorialSpecies(QQ, "X")
            sage: L.Sets().isotype_generating_series()
            1 + X + X^2 + O(X^3)
        '''
    def cycle_index_series(self):
        """
        Return the cycle index series of the species of sets.

        EXAMPLES::

            sage: L.<X> = LazyCombinatorialSpecies(QQ)
            sage: L.Sets().cycle_index_series()
            h[] + h[1] + h[2] + h[3] + h[4] + h[5] + h[6] + O^7
        """

class CycleSpecies(LazyCombinatorialSpeciesElement, UniqueRepresentation, metaclass=InheritComparisonClasscallMetaclass):
    def __init__(self, parent) -> None:
        '''
        Initialize the species of cycles.

        TESTS::

            sage: L = LazyCombinatorialSpecies(QQ, "X")
            sage: C = L.Cycles()
            sage: TestSuite(C).run(skip=[\'_test_category\', \'_test_pickling\'])

            sage: C is L.Cycles()
            True
        '''
    def structures(self, labels) -> Generator[Incomplete, Incomplete]:
        '''
        Iterate over the structures on the given set of labels.

        EXAMPLES::

            sage: L = LazyCombinatorialSpecies(ZZ, "X")
            sage: C = L.Cycles()
            sage: list(C.structures([]))
            []
            sage: list(C.structures([1]))
            [(1,)]
            sage: list(C.structures([1,2]))
            [(1, 2)]
            sage: list(C.structures([1,2,3]))
            [(1, 2, 3), (1, 3, 2)]
        '''
    def generating_series(self):
        """
        Return the (exponential) generating series of the
        species of cycles.

        This is `-log(1-x)`.

        EXAMPLES::

            sage: L.<X> = LazyCombinatorialSpecies(QQ)
            sage: L.Cycles().generating_series()
            X + 1/2*X^2 + 1/3*X^3 + 1/4*X^4 + 1/5*X^5 + 1/6*X^6 + 1/7*X^7 + O(X^8)
        """
    def isotype_generating_series(self):
        '''
        Return the isotype generating series of the species of
        cycles.

        This is `x/(1-x)`.

        EXAMPLES::

            sage: L = LazyCombinatorialSpecies(QQ, "X")
            sage: L.Cycles().isotype_generating_series()
            X + X^2 + X^3 + O(X^4)
        '''

class PolygonSpecies(LazyCombinatorialSpeciesElement, UniqueRepresentation, metaclass=InheritComparisonClasscallMetaclass):
    def __init__(self, parent) -> None:
        '''
        Initialize the species of polygons.

        TESTS::

            sage: L = LazyCombinatorialSpecies(QQ, "X")
            sage: P = L.Polygons()
            sage: TestSuite(P).run(skip=[\'_test_category\', \'_test_pickling\'])

            sage: P is L.Polygons()
            True
        '''

class OrientedSetSpecies(LazyCombinatorialSpeciesElement, UniqueRepresentation, metaclass=InheritComparisonClasscallMetaclass):
    def __init__(self, parent) -> None:
        '''
        Initialize the species of polygons.

        TESTS::

            sage: L = LazyCombinatorialSpecies(QQ, "X")
            sage: Eo = L.OrientedSets()
            sage: TestSuite(Eo).run(skip=[\'_test_category\', \'_test_pickling\'])

            sage: Eo is L.OrientedSets()
            True
        '''

class ChainSpecies(LazyCombinatorialSpeciesElement, UniqueRepresentation, metaclass=InheritComparisonClasscallMetaclass):
    def __init__(self, parent) -> None:
        '''
        Initialize the species of chains.

        TESTS::

            sage: L = LazyCombinatorialSpecies(QQ, "X")
            sage: Ch = L.Chains()
            sage: TestSuite(Ch).run(skip=[\'_test_category\', \'_test_pickling\'])

            sage: Ch is L.Chains()
            True
        '''
    def structures(self, labels) -> Generator[Incomplete]:
        '''
        Iterate over the structures on the given set of labels.

        EXAMPLES::

            sage: L = LazyCombinatorialSpecies(ZZ, "X")
            sage: Ch = L.Chains()
            sage: list(Ch.structures([1,2,3]))
            [(1, 3, 2), (1, 2, 3), (2, 1, 3)]
        '''

class GraphSpecies(LazyCombinatorialSpeciesElementGeneratingSeriesMixin, LazyCombinatorialSpeciesElement, UniqueRepresentation, metaclass=InheritComparisonClasscallMetaclass):
    def __init__(self, parent) -> None:
        '''
        Initialize the species of simple graphs.

        TESTS::

            sage: L = LazyCombinatorialSpecies(QQ, "X")
            sage: G = L.Graphs()
            sage: TestSuite(G).run(skip=[\'_test_category\', \'_test_pickling\'])

            sage: G is L.Graphs()
            True
        '''
    def isotypes(self, labels) -> Generator[Incomplete, Incomplete]:
        '''
        Iterate over the isotypes on the given list of sizes.

        EXAMPLES::

            sage: L = LazyCombinatorialSpecies(QQ, "X")
            sage: G = L.Graphs()
            sage: list(G.isotypes(2))
            [Graph on 2 vertices, Graph on 2 vertices]
        '''
    def generating_series(self):
        '''
        Return the (exponential) generating series of the
        species of simple graphs.

        EXAMPLES::

            sage: L = LazyCombinatorialSpecies(QQ, "X")
            sage: L.Graphs().generating_series().truncate(7)
            1 + X + X^2 + 4/3*X^3 + 8/3*X^4 + 128/15*X^5 + 2048/45*X^6
        '''
    def cycle_index_series(self):
        '''
        Return the cycle index series of the species of simple graphs.

        The cycle index series is computed using Proposition 2.2.7 in
        [BLL1998]_.

        EXAMPLES::

            sage: L = LazyCombinatorialSpecies(QQ, "X")
            sage: L.Graphs().cycle_index_series().truncate(4)
            p[] + p[1] + (p[1,1]+p[2]) + (4/3*p[1,1,1]+2*p[2,1]+2/3*p[3])

        Check that the number of isomorphism types is computed quickly::

            sage: L.Graphs().isotype_generating_series()[20]
            645490122795799841856164638490742749440
        '''

class SetPartitionSpecies(CompositionSpeciesElement, UniqueRepresentation, metaclass=InheritComparisonClasscallMetaclass):
    def __init__(self, parent) -> None:
        '''
        Initialize the species of set partitions.

        TESTS::

            sage: L = LazyCombinatorialSpecies(QQ, "X")
            sage: p = L.SetPartitions()
            sage: TestSuite(p).run(skip=[\'_test_category\', \'_test_pickling\'])

            sage: p is L.SetPartitions()
            True

            sage: p.generating_series()[20]
            263898766507/12412765347840000

            sage: SetPartitions(20).cardinality() / factorial(20)
            263898766507/12412765347840000

            sage: p.isotype_generating_series()[20]
            627

            sage: Partitions(20).cardinality()
            627
        '''
    def isotypes(self, labels) -> Generator[Incomplete, Incomplete]:
        '''
        Iterate over the isotypes on the given list of sizes.

        EXAMPLES::

            sage: L = LazyCombinatorialSpecies(QQ, "X")
            sage: p = L.SetPartitions()
            sage: list(p.isotypes(3))
            [[3], [2, 1], [1, 1, 1]]
        '''
    def structures(self, labels) -> Generator[Incomplete, Incomplete]:
        '''
        Iterate over the structures on the given set of labels.

        EXAMPLES::

            sage: L = LazyCombinatorialSpecies(ZZ, "X")
            sage: P = L.SetPartitions()
            sage: list(P.structures([]))
            [{}]
            sage: list(P.structures([1]))
            [{{1}}]
            sage: list(P.structures([1,2]))
            [{{1, 2}}, {{1}, {2}}]
            sage: list(P.structures([1,2,3]))
            [{{1, 2, 3}}, {{1, 2}, {3}}, {{1, 3}, {2}}, {{1}, {2, 3}}, {{1}, {2}, {3}}]
        '''
    def generating_series(self):
        '''
        Return the (exponential) generating series of ``self``.

        EXAMPLES::

            sage: L = LazyCombinatorialSpecies(ZZ, "X")
            sage: P = L.SetPartitions()
            sage: P.generating_series()
            1 + X + X^2 + 5/6*X^3 + 5/8*X^4 + 13/30*X^5 + 203/720*X^6 + O(X^7)
        '''
    def isotype_generating_series(self):
        '''
        Return the isotype generating series of ``self``.

        EXAMPLES::

            sage: L = LazyCombinatorialSpecies(ZZ, "X")
            sage: P = L.SetPartitions()
            sage: P.isotype_generating_series()
            1 + X + 2*X^2 + 3*X^3 + 5*X^4 + 7*X^5 + 11*X^6 + O(X^7)
        '''

class RestrictedSpeciesElement(LazyCombinatorialSpeciesElement):
    def __init__(self, F, min_degree, max_degree) -> None:
        '''
        Initialize the restriction of a species to the given degrees.

        TESTS::

            sage: L = LazyCombinatorialSpecies(QQ, "X")
            sage: G3 = L.Graphs().restrict(3, 3)
            sage: TestSuite(G3).run(skip=[\'_test_category\', \'_test_pickling\'])
        '''
    def isotypes(self, *shape) -> Generator[Incomplete, Incomplete]:
        '''
        Iterate over the isotypes on the given list of sizes.

        EXAMPLES::

            sage: L = LazyCombinatorialSpecies(QQ, "X")
            sage: p = L.SetPartitions().restrict(2, 2)
            sage: list(p.isotypes(3))
            []
        '''
    def structures(self, *labels) -> Generator[Incomplete, Incomplete]:
        '''
        Iterate over the structures on the given set of labels.

        EXAMPLES::

            sage: L = LazyCombinatorialSpecies(ZZ, "X")
            sage: F = L.SetPartitions().restrict(3)
            sage: list(F.structures([1]))
            []
            sage: list(F.structures([1,2,3]))
            [{{1, 2, 3}}, {{1, 2}, {3}}, {{1, 3}, {2}}, {{1}, {2, 3}}, {{1}, {2}, {3}}]
        '''
    def generating_series(self):
        '''
        Return the (exponential) generating series of ``self``.

        EXAMPLES::

            sage: L = LazyCombinatorialSpecies(QQ, "X")
            sage: E = L.Sets()
            sage: E.restrict(1, 5).generating_series()
            X + 1/2*X^2 + 1/6*X^3 + 1/24*X^4 + 1/120*X^5
            sage: E.restrict(1).generating_series()
            X + 1/2*X^2 + 1/6*X^3 + 1/24*X^4 + 1/120*X^5 + 1/720*X^6 + 1/5040*X^7 + O(X^8)
        '''
    def isotype_generating_series(self):
        '''
        Return the isotype generating series of ``self``.

        EXAMPLES::

            sage: L = LazyCombinatorialSpecies(QQ, "X")
            sage: E = L.Sets()
            sage: E.restrict(1, 5).isotype_generating_series()
            X + X^2 + X^3 + X^4 + X^5

            sage: E.restrict(1).isotype_generating_series()
            X + X^2 + X^3 + O(X^4)
        '''
    def cycle_index_series(self):
        '''
        Return the cycle index series for this species.

        EXAMPLES::

            sage: L = LazyCombinatorialSpecies(QQ, "X")
            sage: E = L.Sets()
            sage: E.restrict(1, 5).cycle_index_series()
            h[1] + h[2] + h[3] + h[4] + h[5]

            sage: E.restrict(1).cycle_index_series()
            h[1] + h[2] + h[3] + h[4] + h[5] + h[6] + h[7] + O^8
        '''
