from .generating_series import CycleIndexSeriesRing as CycleIndexSeriesRing, ExponentialGeneratingSeriesRing as ExponentialGeneratingSeriesRing, OrdinaryGeneratingSeriesRing as OrdinaryGeneratingSeriesRing
from sage.combinat.species.misc import accept_size as accept_size
from sage.combinat.species.structure import IsotypesWrapper as IsotypesWrapper, StructuresWrapper as StructuresWrapper
from sage.misc.cachefunc import cached_method as cached_method
from sage.rings.rational_field import QQ as QQ
from sage.structure.sage_object import SageObject as SageObject

class GenericCombinatorialSpecies(SageObject):
    def __init__(self, min=None, max=None, weight=None) -> None:
        """
        TESTS::

            sage: P = species.PermutationSpecies(size=3)
            sage: P._weight
            1
            sage: P._min
            3
            sage: P._max
            4
        """
    def __hash__(self):
        """
        Return a hash of the unique info tuple.

        EXAMPLES::

            sage: hash(species.SetSpecies()) #random
            -152204909943771174
        """
    def __eq__(self, x):
        """
        Test equality between two species.

        EXAMPLES::

            sage: X = species.SingletonSpecies()
            sage: X + X == X + X
            True
            sage: X == X
            True
            sage: X == species.EmptySetSpecies()
            False
            sage: X == X*X
            False

        ::

            sage: X = species.SingletonSpecies()
            sage: E = species.EmptySetSpecies()
            sage: L = CombinatorialSpecies()
            doctest:warning...
            DeprecationWarning: combinat.species is superseded by LazyCombinatorialSpecies
            See https://github.com/sagemath/sage/issues/38544 for details.
            sage: L.define(E+X*L)
            sage: K = CombinatorialSpecies()
            sage: K.define(E+X*L)
            sage: L == K
            True
        """
    def __ne__(self, other):
        """
        Check whether ``self`` and ``other`` are not equal.

        EXAMPLES::

            sage: X = species.SingletonSpecies()
            sage: X + X == X + X
            True
            sage: X != X
            False
            sage: X != species.EmptySetSpecies()
            True
            sage: X != X*X
            True

            sage: X = species.SingletonSpecies()
            sage: E = species.EmptySetSpecies()
            sage: L = CombinatorialSpecies()
            sage: L.define(E+X*L)
            sage: K = CombinatorialSpecies()
            sage: K.define(E+X*L)
            sage: L != K
            False
        """
    def weighted(self, weight):
        """
        Return a version of this species with the specified weight.

        EXAMPLES::

            sage: t = ZZ['t'].gen()
            sage: C = species.CycleSpecies(); C
            Cyclic permutation species
            sage: C.weighted(t)
            Cyclic permutation species with weight=t
        """
    def __add__(self, g):
        """
        Return the sum of ``self`` and ``g``.

        EXAMPLES::

            sage: P = species.PermutationSpecies()
            sage: F = P + P; F
            Sum of (Permutation species) and (Permutation species)
            sage: F.structures([1,2]).list()
            [[1, 2], [2, 1], [1, 2], [2, 1]]
        """
    sum = __add__
    def __mul__(self, g):
        """
        Return the product of ``self`` and ``g``.

        EXAMPLES::

            sage: P = species.PermutationSpecies()
            sage: F = P * P; F
            Product of (Permutation species) and (Permutation species)
        """
    product = __mul__
    def __call__(self, g):
        """
        EXAMPLES::

            sage: S = species.SetSpecies()
            sage: S(S)
            Composition of (Set species) and (Set species)
        """
    composition = __call__
    def functorial_composition(self, g):
        """
        Return the functorial composition of ``self`` with ``g``.

        EXAMPLES::

            sage: E = species.SetSpecies()
            sage: E2 = E.restricted(min=2, max=3)
            sage: WP = species.SubsetSpecies()
            sage: P2 = E2*E
            sage: G = WP.functorial_composition(P2)
            sage: G.isotype_generating_series()[0:5]                                    # needs sage.modules
            [1, 1, 2, 4, 11]
        """
    @accept_size
    def restricted(self, min=None, max=None):
        """
        Return the restriction of the species.

        INPUT:

        - ``min`` -- (optional) integer

        - ``max`` -- (optional) integer

        EXAMPLES::

            sage: S = species.SetSpecies().restricted(min=3); S
            Set species with min=3
            sage: S.structures([1,2]).list()
            []
            sage: S.generating_series()[0:5]
            [0, 0, 0, 1/6, 1/24]
        """
    def structures(self, labels, structure_class=None):
        """
        EXAMPLES::

            sage: F = CombinatorialSpecies()
            sage: F.structures([1,2,3]).list()
            Traceback (most recent call last):
            ...
            ValueError: Stream is not yet defined
        """
    def isotypes(self, labels, structure_class=None):
        """
        EXAMPLES::

            sage: F = CombinatorialSpecies()
            sage: F.isotypes([1,2,3]).list()
            Traceback (most recent call last):
            ...
            ValueError: Stream is not yet defined
        """
    def __pow__(self, n):
        """
        Return this species to the power `n`.

        This uses a binary exponentiation algorithm to perform the
        powering.

        EXAMPLES::

            sage: One = species.EmptySetSpecies()
            sage: X = species.SingletonSpecies()
            sage: X^2
            Product of (Singleton species) and (Singleton species)
            sage: X^5
            Product of (Singleton species) and (Product of (Product of
            (Singleton species) and (Singleton species)) and (Product
            of (Singleton species) and (Singleton species)))

            sage: (X^2).generating_series()[0:4]
            [0, 0, 1, 0]
            sage: (X^3).generating_series()[0:4]
            [0, 0, 0, 1]
            sage: ((One+X)^3).generating_series()[0:4]
            [1, 3, 3, 1]
            sage: ((One+X)^7).generating_series()[0:8]
            [1, 7, 21, 35, 35, 21, 7, 1]

            sage: x = QQ[['x']].gen()
            sage: coeffs = ((1+x+x+x**2)**25+O(x**10)).padded_list()
            sage: T = ((One+X+X+X^2)^25)
            sage: T.generating_series()[0:10] == coeffs
            True
            sage: X^1 is X
            True
            sage: A = X^32
            sage: A.digraph()                                                           # needs sage.graphs
            Multi-digraph on 6 vertices

        TESTS::

            sage: X**(-1)
            Traceback (most recent call last):
            ...
            ValueError: only positive exponents are currently supported
        """
    @cached_method
    def generating_series(self, base_ring=None):
        """
        Return the generating series for this species.

        This is an exponential generating series so the `n`-th
        coefficient of the series corresponds to the number of labeled
        structures with `n` labels divided by `n!`.

        EXAMPLES::

            sage: P = species.PermutationSpecies()
            sage: g = P.generating_series()
            sage: g[:4]
            [1, 1, 1, 1]
            sage: g.counts(4)
            [1, 1, 2, 6]
            sage: P.structures([1,2,3]).list()
            [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
            sage: len(_)
            6
        """
    @cached_method
    def isotype_generating_series(self, base_ring=None):
        """
        Return the isotype generating series for this species.

        The `n`-th coefficient of this series corresponds to the number
        of isomorphism types for the structures on `n` labels.

        EXAMPLES::

            sage: P = species.PermutationSpecies()
            sage: g = P.isotype_generating_series()
            sage: g[0:4]                                                                # needs sage.libs.flint
            [1, 1, 2, 3]
            sage: g.counts(4)                                                           # needs sage.libs.flint
            [1, 1, 2, 3]
            sage: P.isotypes([1,2,3]).list()                                            # needs sage.libs.flint
            [[2, 3, 1], [2, 1, 3], [1, 2, 3]]
            sage: len(_)                                                                # needs sage.libs.flint
            3
        """
    @cached_method
    def cycle_index_series(self, base_ring=None):
        """
        Return the cycle index series for this species.

        The cycle index series is a sequence of symmetric functions.

        EXAMPLES::

            sage: P = species.PermutationSpecies()
            sage: g = P.cycle_index_series()                                            # needs sage.modules
            sage: g[0:4]                                                                # needs sage.modules
            [p[], p[1], p[1, 1] + p[2], p[1, 1, 1] + p[2, 1] + p[3]]
        """
    def is_weighted(self):
        """
        Return ``True`` if this species has a nontrivial weighting associated
        with it.

        EXAMPLES::

            sage: C = species.CycleSpecies()
            sage: C.is_weighted()
            False
        """
    def weight_ring(self):
        """
        Return the ring in which the weights of this species occur.

        By default, this is just the field of rational numbers.

        EXAMPLES::

            sage: species.SetSpecies().weight_ring()
            Rational Field
        """
    def digraph(self):
        """
        Return a directed graph where the vertices are the individual
        species that make up this one.

        EXAMPLES::

            sage: X = species.SingletonSpecies()
            sage: B = species.CombinatorialSpecies()
            sage: B.define(X+B*B)
            sage: g = B.digraph(); g                                                    # needs sage.graphs
            Multi-digraph on 4 vertices

            sage: sorted(g, key=str)                                                    # needs sage.graphs
            [Combinatorial species,
             Product of (Combinatorial species) and (Combinatorial species),
             Singleton species,
             Sum of (Singleton species) and
              (Product of (Combinatorial species) and (Combinatorial species))]

            sage: d = {sp: i for i, sp in enumerate(g)}                                 # needs sage.graphs
            sage: g.relabel(d)                                                          # needs sage.graphs
            sage: g.canonical_label().edges(sort=True)                                  # needs sage.graphs
            [(0, 3, None), (2, 0, None), (2, 0, None), (3, 1, None), (3, 2, None)]
        """
    def algebraic_equation_system(self):
        """
        Return a system of algebraic equations satisfied by this species.

        The nodes are numbered in the order that they appear as vertices of
        the associated digraph.

        EXAMPLES::

            sage: B = species.BinaryTreeSpecies()
            sage: B.algebraic_equation_system()                                         # needs sage.graphs
            [-node3^2 + node1, -node1 + node3 + (-z)]

        ::

            sage: sorted(B.digraph().vertex_iterator(), key=str)                        # needs sage.graphs
            [Combinatorial species with min=1,
             Product of (Combinatorial species with min=1)
                    and (Combinatorial species with min=1),
             Singleton species,
             Sum of (Singleton species)
                and (Product of (Combinatorial species with min=1)
                and (Combinatorial species with min=1))]

        ::

            sage: B.algebraic_equation_system()[0].parent()                             # needs sage.graphs
            Multivariate Polynomial Ring in node0, node1, node2, node3 over
             Fraction Field of Univariate Polynomial Ring in z over Rational Field
        """
