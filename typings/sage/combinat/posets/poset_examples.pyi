from _typeshed import Incomplete
from sage.categories.finite_lattice_posets import FiniteLatticePosets as FiniteLatticePosets
from sage.categories.finite_posets import FinitePosets as FinitePosets
from sage.combinat.permutation import Permutation as Permutation, Permutations as Permutations, to_standard as to_standard
from sage.combinat.posets import bubble_shuffle as bubble_shuffle, hochschild_lattice as hochschild_lattice
from sage.combinat.posets.d_complete import DCompletePoset as DCompletePoset
from sage.combinat.posets.lattices import FiniteLatticePoset as FiniteLatticePoset, JoinSemilattice as JoinSemilattice, LatticePoset as LatticePoset, MeetSemilattice as MeetSemilattice
from sage.combinat.posets.posets import FinitePoset as FinitePoset, FinitePosets_n as FinitePosets_n, Poset as Poset
from sage.graphs.digraph import DiGraph as DiGraph
from sage.misc.classcall_metaclass import ClasscallMetaclass as ClasscallMetaclass
from sage.rings.integer import Integer as Integer
from sage.sets.non_negative_integers import NonNegativeIntegers as NonNegativeIntegers

def check_int(n, minimum: int = 0):
    """
    Check that ``n`` is an integer at least equal to ``minimum``.

    This is a boilerplate function ensuring input safety.

    INPUT:

    - ``n`` -- anything

    - ``minimum`` -- an optional integer (default: 0)

    EXAMPLES::

        sage: from sage.combinat.posets.poset_examples import check_int
        sage: check_int(6, 3)
        6
        sage: check_int(6)
        6

        sage: check_int(-1)
        Traceback (most recent call last):
        ...
        ValueError: number of elements must be a nonnegative integer, not -1

        sage: check_int(1, 3)
        Traceback (most recent call last):
        ...
        ValueError: number of elements must be an integer at least 3, not 1

        sage: check_int('junk')
        Traceback (most recent call last):
        ...
        ValueError: number of elements must be a nonnegative integer, not junk
    """

class Posets(metaclass=ClasscallMetaclass):
    """
    A collection of posets and lattices.

    EXAMPLES::

        sage: posets.BooleanLattice(3)
        Finite lattice containing 8 elements
        sage: posets.ChainPoset(3)
        Finite lattice containing 3 elements
        sage: posets.RandomPoset(17,.15)
        Finite poset containing 17 elements

    The category of all posets::

        sage: Posets()
        Category of posets

    The enumerated set of all posets on `3` elements, up to an
    isomorphism::

        sage: Posets(3)
        Posets containing 3 elements

    .. SEEALSO:: :class:`~sage.categories.posets.Posets`, :class:`FinitePosets`, :func:`Poset`

    TESTS::

        sage: P = Posets
        sage: TestSuite(P).run()
    """
    @staticmethod
    def __classcall__(cls, n=None):
        """
        Return either the category of all posets, or the finite
        enumerated set of all finite posets on ``n`` elements up to an
        isomorphism.

        EXAMPLES::

            sage: Posets()
            Category of posets
            sage: Posets(4)
            Posets containing 4 elements
        """
    @staticmethod
    def BooleanLattice(n, facade=None, use_subsets: bool = False):
        """
        Return the Boolean lattice containing `2^n` elements.

        - ``n`` -- integer; number of elements will be `2^n`
        - ``facade`` -- boolean; whether to make the returned poset a
          facade poset (see :mod:`sage.categories.facade_sets`); the
          default behaviour is the same as the default behaviour of
          the :func:`~sage.combinat.posets.posets.Poset` constructor
        - ``use_subsets`` -- boolean (default: ``False``); if ``True``,
          then label the elements by subsets of `\\{1, 2, \\ldots, n\\}`;
          otherwise label the elements by `0, 1, 2, \\ldots, 2^n-1`

        EXAMPLES::

            sage: posets.BooleanLattice(5)
            Finite lattice containing 32 elements

            sage: sorted(posets.BooleanLattice(2))
            [0, 1, 2, 3]
            sage: sorted(posets.BooleanLattice(2, use_subsets=True), key=list)
            [{}, {1}, {1, 2}, {2}]

        TESTS:

        Check isomorphism::

            sage: B5 = posets.BooleanLattice(5)
            sage: B5S = posets.BooleanLattice(5, use_subsets=True)
            sage: B5.is_isomorphic(B5S)
            True

        Check the corner cases::

            sage: list(posets.BooleanLattice(0, use_subsets=True))
            [{}]
            sage: list(posets.BooleanLattice(1, use_subsets=True))
            [{}, {1}]
        """
    BubblePoset: Incomplete
    ShufflePoset: Incomplete
    HochschildLattice: Incomplete
    @staticmethod
    def ChainPoset(n, facade=None):
        '''
        Return a chain (a totally ordered poset) containing `n` elements.

        - ``n`` -- integer; number of elements
        - ``facade`` -- boolean; whether to make the returned poset a
          facade poset (see :mod:`sage.categories.facade_sets`); the
          default behaviour is the same as the default behaviour of
          the :func:`~sage.combinat.posets.posets.Poset` constructor

        EXAMPLES::

            sage: C = posets.ChainPoset(6); C
            Finite lattice containing 6 elements
            sage: C.linear_extension()
            [0, 1, 2, 3, 4, 5]

        TESTS::

            sage: for i in range(5):
            ....:     for j in range(5):
            ....:         if C.covers(C(i),C(j)) and j != i+1:
            ....:             print("TEST FAILED")

        Check that :issue:`8422` is solved::

            sage: posets.ChainPoset(0)
            Finite lattice containing 0 elements
            sage: C = posets.ChainPoset(1); C
            Finite lattice containing 1 elements
            sage: C.cover_relations()
            []
            sage: C = posets.ChainPoset(2); C
            Finite lattice containing 2 elements
            sage: C.cover_relations()
            [[0, 1]]
        '''
    @staticmethod
    def AntichainPoset(n, facade=None):
        '''
        Return an antichain (a poset with no comparable elements)
        containing `n` elements.

        INPUT:

        - ``n`` -- integer; number of elements
        - ``facade`` -- boolean; whether to make the returned poset a
          facade poset (see :mod:`sage.categories.facade_sets`); the
          default behaviour is the same as the default behaviour of
          the :func:`~sage.combinat.posets.posets.Poset` constructor

        EXAMPLES::

            sage: A = posets.AntichainPoset(6); A
            Finite poset containing 6 elements

        TESTS::

            sage: for i in range(5):
            ....:     for j in range(5):
            ....:         if A.covers(A(i),A(j)):
            ....:             print("TEST FAILED")

        TESTS:

        Check that :issue:`8422` is solved::

            sage: posets.AntichainPoset(0)
            Finite poset containing 0 elements
            sage: C = posets.AntichainPoset(1); C
            Finite poset containing 1 elements
            sage: C.cover_relations()
            []
            sage: C = posets.AntichainPoset(2); C
            Finite poset containing 2 elements
            sage: C.cover_relations()
            []
        '''
    @staticmethod
    def PentagonPoset(facade=None):
        """
        Return the Pentagon poset.

        INPUT:

        - ``facade`` -- boolean; whether to make the returned poset a
          facade poset (see :mod:`sage.categories.facade_sets`); the
          default behaviour is the same as the default behaviour of
          the :func:`~sage.combinat.posets.posets.Poset` constructor

        EXAMPLES::

            sage: P = posets.PentagonPoset(); P
            Finite lattice containing 5 elements
            sage: P.cover_relations()
            [[0, 1], [0, 2], [1, 4], [2, 3], [3, 4]]

        TESTS:

        This is smallest lattice that is not modular::

            sage: P.is_modular()
            False

        This poset and the :meth:`DiamondPoset` are the two smallest
        lattices which are not distributive::

            sage: P.is_distributive()
            False
            sage: posets.DiamondPoset(5).is_distributive()
            False
        """
    @staticmethod
    def DiamondPoset(n, facade=None):
        """
        Return the lattice of rank two containing ``n`` elements.

        INPUT:

        - ``n`` -- number of elements, an integer at least 3

        - ``facade`` -- boolean; whether to make the returned poset a
          facade poset (see :mod:`sage.categories.facade_sets`); the
          default behaviour is the same as the default behaviour of
          the :func:`~sage.combinat.posets.posets.Poset` constructor

        EXAMPLES::

            sage: posets.DiamondPoset(7)
            Finite lattice containing 7 elements
        """
    @staticmethod
    def Crown(n, facade=None):
        """
        Return the crown poset of `2n` elements.

        In this poset every element `i` for `0 \\leq i \\leq n-1`
        is covered by elements `i+n` and `i+n+1`, except that
        `n-1` is covered by `n` and `n+1`.

        INPUT:

        - ``n`` -- number of elements, an integer at least 2

        - ``facade`` -- boolean; whether to make the returned poset a
          facade poset (see :mod:`sage.categories.facade_sets`); the
          default behaviour is the same as the default behaviour of
          the :func:`~sage.combinat.posets.posets.Poset` constructor

        EXAMPLES::

            sage: posets.Crown(3)
            Finite poset containing 6 elements
        """
    @staticmethod
    def DivisorLattice(n, facade=None):
        """
        Return the divisor lattice of an integer.

        Elements of the lattice are divisors of `n`, and we have
        `x \\leq y` in the lattice if `x` divides `y`.

        INPUT:

        - ``n`` -- integer
        - ``facade`` -- boolean; whether to make the returned poset a
          facade poset (see :mod:`sage.categories.facade_sets`); the
          default behaviour is the same as the default behaviour of
          the :func:`~sage.combinat.posets.posets.Poset` constructor

        EXAMPLES::

            sage: P = posets.DivisorLattice(12)
            sage: sorted(P.cover_relations())
            [[1, 2], [1, 3], [2, 4], [2, 6], [3, 6], [4, 12], [6, 12]]

            sage: P = posets.DivisorLattice(10, facade=False)
            sage: P(2) < P(5)
            False

        TESTS::

            sage: posets.DivisorLattice(1)
            Finite lattice containing 1 elements with distinguished linear extension
        """
    @staticmethod
    def HessenbergPoset(H):
        """
        Return the poset associated to a Hessenberg function ``H``.

        A *Hessenberg function* (of length `n`) is a function `H: \\{1,\\ldots,n\\}
        \\to \\{1,\\ldots,n\\}` such that `\\max(i, H(i-1)) \\leq H(i) \\leq n` for all
        `i` (where `H(0) = 0` by convention). The corresponding poset is given
        by `i < j` (in the poset) if and only if `H(i) < j` (as integers).
        These posets correspond to the natural unit interval order posets.

        INPUT:

        - ``H`` -- list of the Hessenberg function values
          (without `H(0)`)

        EXAMPLES::

            sage: P = posets.HessenbergPoset([2, 3, 5, 5, 5]); P
            Finite poset containing 5 elements
            sage: P.cover_relations()
            [[2, 4], [2, 5], [1, 3], [1, 4], [1, 5]]

        TESTS::

            sage: P = posets.HessenbergPoset([2, 2, 6, 4, 5, 6])
            Traceback (most recent call last):
            ...
            ValueError: [2, 2, 6, 4, 5, 6] is not a Hessenberg function
            sage: P = posets.HessenbergPoset([]); P
            Finite poset containing 0 elements
        """
    @staticmethod
    def IntegerCompositions(n):
        """
        Return the poset of integer compositions of the integer ``n``.

        A composition of a positive integer `n` is a list of positive
        integers that sum to `n`. The order is reverse refinement:
        `p = [p_1,p_2,...,p_l] \\leq q = [q_1,q_2,...,q_m]` if `q`
        consists of an integer composition of `p_1`, followed by an
        integer composition of `p_2`, and so on.

        EXAMPLES::

            sage: P = posets.IntegerCompositions(7); P
            Finite poset containing 64 elements
            sage: len(P.cover_relations())
            192
        """
    @staticmethod
    def IntegerPartitions(n):
        """
        Return the poset of integer partitions of the integer ``n``.

        A partition of a positive integer `n` is a non-increasing list
        of positive integers that sum to `n`. If `p` and `q` are
        integer partitions of `n`, then `p` covers `q` if and only
        if `q` is obtained from `p` by joining two parts of `p`
        (and sorting, if necessary).

        EXAMPLES::

            sage: P = posets.IntegerPartitions(7); P
            Finite poset containing 15 elements
            sage: len(P.cover_relations())
            28
        """
    @staticmethod
    def RestrictedIntegerPartitions(n):
        """
        Return the poset of integer partitions of the integer `n`
        ordered by restricted refinement.

        That is, if `p` and `q` are integer partitions of `n`, then
        `p` covers `q` if and only if `q` is obtained from `p` by
        joining two distinct parts of `p` (and sorting, if necessary).

        EXAMPLES::

            sage: P = posets.RestrictedIntegerPartitions(7); P
            Finite poset containing 15 elements
            sage: len(P.cover_relations())
            17
        """
    @staticmethod
    def IntegerPartitionsDominanceOrder(n):
        """
        Return the lattice of integer partitions of the integer `n`
        ordered by dominance.

        That is, if `p=(p_1,\\ldots,p_i)` and `q=(q_1,\\ldots,q_j)` are
        integer partitions of `n`, then `p \\geq q` if and
        only if `p_1+\\cdots+p_k \\geq q_1+\\cdots+q_k` for all `k`.

        INPUT:

        - ``n`` -- positive integer

        EXAMPLES::

            sage: P = posets.IntegerPartitionsDominanceOrder(6); P
            Finite lattice containing 11 elements
            sage: P.cover_relations()
            [[[1, 1, 1, 1, 1, 1], [2, 1, 1, 1, 1]],
             [[2, 1, 1, 1, 1], [2, 2, 1, 1]],
             [[2, 2, 1, 1], [2, 2, 2]],
             [[2, 2, 1, 1], [3, 1, 1, 1]],
             [[2, 2, 2], [3, 2, 1]],
             [[3, 1, 1, 1], [3, 2, 1]],
             [[3, 2, 1], [3, 3]],
             [[3, 2, 1], [4, 1, 1]],
             [[3, 3], [4, 2]],
             [[4, 1, 1], [4, 2]],
             [[4, 2], [5, 1]],
             [[5, 1], [6]]]
        """
    @staticmethod
    def PowerPoset(n):
        """
        Return the power poset on `n` element posets.

        Elements of the power poset are all posets on
        the set `\\{0, 1, \\ldots, n-1\\}` ordered by extension.
        That is, the antichain of `n` elements is the bottom and
        `P_a \\le P_b` in the power poset if `P_b` is an extension
        of `P_a`.

        These were studied in [Bru1994]_.

        EXAMPLES::

            sage: P3 = posets.PowerPoset(3); P3
            Finite meet-semilattice containing 19 elements
            sage: all(P.is_chain() for P in P3.maximal_elements())
            True

        TESTS::

            sage: P0 = posets.PowerPoset(0); P0
            Finite meet-semilattice containing 1 elements
            sage: P0[0]
            Finite poset containing 0 elements
            sage: P1 = posets.PowerPoset(1); P1
            Finite meet-semilattice containing 1 elements
            sage: P1[0]
            Finite poset containing 1 elements
            sage: P1[0][0]
            0
        """
    @staticmethod
    def ProductOfChains(chain_lengths, facade=None):
        """
        Return a product of chains.

        - ``chain_lengths`` -- list of nonnegative integers; number of
          elements in each chain

        - ``facade`` -- boolean; whether to make the returned poset a
          facade poset (see :mod:`sage.categories.facade_sets`); the
          default behaviour is the same as the default behaviour of
          the :func:`~sage.combinat.posets.posets.Poset` constructor

        EXAMPLES::

            sage: P = posets.ProductOfChains([2, 2]); P
            Finite lattice containing 4 elements
            sage: P.linear_extension()
            [(0, 0), (0, 1), (1, 0), (1, 1)]
            sage: P.upper_covers((0,0))
            [(0, 1), (1, 0)]
            sage: P.lower_covers((1,1))
            [(0, 1), (1, 0)]

        TESTS::

            sage: P = posets.ProductOfChains([]); P
            Finite lattice containing 0 elements
            sage: P = posets.ProductOfChains([3, 0, 1]); P
            Finite lattice containing 0 elements
            sage: P = posets.ProductOfChains([1,1,1,1]); P
            Finite lattice containing 1 elements
        """
    @staticmethod
    def RandomPoset(n, p):
        """
        Generate a random poset on ``n`` elements according to a
        probability ``p``.

        INPUT:

        - ``n`` -- number of elements, a nonnegative integer

        - ``p`` -- a probability, a real number between 0 and 1 (inclusive)

        OUTPUT:

        A poset on `n` elements. The probability `p` roughly measures
        width/height of the output: `p=0` always generates an antichain,
        `p=1` will return a chain. To create interesting examples,
        keep the probability small, perhaps on the order of `1/n`.

        EXAMPLES::

            sage: set_random_seed(0)  # Results are reproducible
            sage: P = posets.RandomPoset(5, 0.3)
            sage: P.cover_relations()
            [[5, 4], [4, 2], [1, 2]]

        .. SEEALSO:: :meth:`RandomLattice`

        TESTS::

            sage: posets.RandomPoset(6, 'garbage')
            Traceback (most recent call last):
            ...
            TypeError: probability must be a real number, not garbage

            sage: posets.RandomPoset(6, -0.5)
            Traceback (most recent call last):
            ...
            ValueError: probability must be between 0 and 1, not -0.5

            sage: posets.RandomPoset(0, 0.5)
            Finite poset containing 0 elements
        """
    @staticmethod
    def RandomLattice(n, p, properties=None):
        """
        Return a random lattice on ``n`` elements.

        INPUT:

        - ``n`` -- number of elements, a nonnegative integer

        - ``p`` -- a probability, a positive real number less than one

        - ``properties`` -- list of properties for the lattice. Currently
          implemented:

          * ``None``, no restrictions for lattices to create
          * ``'planar'``, the lattice has an upward planar drawing
          * ``'dismantlable'`` (implicated by ``'planar'``)
          * ``'distributive'`` (implicated by ``'stone'``)
          * ``'stone'``

        OUTPUT:

        A lattice on `n` elements. When ``properties`` is ``None``,
        the probability `p` roughly measures number of covering
        relations of the lattice. To create interesting examples, make
        the probability a little below one, for example `0.9`.

        Currently parameter ``p`` has no effect only when ``properties``
        is not ``None``.

        .. NOTE::

            Results are reproducible in same Sage version only. Underlying
            algorithm may change in future versions.

        EXAMPLES::

            sage: set_random_seed(0)  # Results are reproducible
            sage: L = posets.RandomLattice(8, 0.995); L
            Finite lattice containing 8 elements
            sage: L.cover_relations()
            [[7, 6], [7, 3], [7, 1], ..., [5, 4], [2, 4], [1, 4], [0, 4]]
            sage: L = posets.RandomLattice(10, 0, properties=['dismantlable'])
            sage: L.is_dismantlable()
            True

        .. SEEALSO:: :meth:`RandomPoset`

        TESTS::

            sage: posets.RandomLattice(6, 'garbage')
            Traceback (most recent call last):
            ...
            TypeError: probability must be a real number, not garbage

            sage: posets.RandomLattice(6, -0.5)
            Traceback (most recent call last):
            ...
            ValueError: probability must be a positive real number and below 1, not -0.5

            sage: posets.RandomLattice(10, 0.5, properties=['junk'])
            Traceback (most recent call last):
            ...
            ValueError: unknown value junk for 'properties'

            sage: posets.RandomLattice(0, 0.5)
            Finite lattice containing 0 elements
        """
    @staticmethod
    def SetPartitions(n):
        """
        Return the lattice of set partitions of the set `\\{1,\\ldots,n\\}`
        ordered by refinement.

        INPUT:

        - ``n`` -- positive integer

        EXAMPLES::

            sage: posets.SetPartitions(4)
            Finite lattice containing 15 elements
        """
    @staticmethod
    def SSTPoset(s, f=None):
        """
        The lattice poset on semistandard tableaux of shape ``s`` and largest
        entry ``f`` that is ordered by componentwise comparison of the
        entries.

        INPUT:

        - ``s`` -- shape of the tableaux

        - ``f`` -- integer (default: ``None``); the maximum fill number.
          By default (``None``), the method uses the number of cells in the shape.

        .. NOTE::

            This is a basic implementation and most certainly
            not the most efficient.

        EXAMPLES::

            sage: posets.SSTPoset([2,1])
            Finite lattice containing 8 elements

            sage: posets.SSTPoset([2,1],4)
            Finite lattice containing 20 elements

            sage: posets.SSTPoset([2,1],2).cover_relations()
            [[[[1, 1], [2]], [[1, 2], [2]]]]

            sage: posets.SSTPoset([3,2]).bottom()       # long time (6s on sage.math, 2012)
            [[1, 1, 1], [2, 2]]

            sage: posets.SSTPoset([3,2],4).maximal_elements()
            [[[3, 3, 4], [4, 4]]]
        """
    @staticmethod
    def StandardExample(n, facade=None):
        """
        Return the partially ordered set on `2n` elements with
        dimension `n`.

        Let `P` be the poset on `\\{0, 1, 2, \\ldots, 2n-1\\}` whose defining
        relations are that `i < j` for every `0 \\leq i < n \\leq j < 2n`
        except when `i + n = j`. The poset `P` is the so-called
        *standard example* of a poset with dimension `n`.

        INPUT:

        - ``n`` -- integer `\\ge 2`; dimension of the constructed poset

        - ``facade`` -- boolean; whether to make the returned poset a
          facade poset (see :mod:`sage.categories.facade_sets`); the
          default behaviour is the same as the default behaviour of
          the :func:`~sage.combinat.posets.posets.Poset` constructor

        OUTPUT: the standard example of a poset of dimension `n`

        EXAMPLES::

            sage: A = posets.StandardExample(3); A
            Finite poset containing 6 elements
            sage: A.dimension()                                                         # needs networkx
            3

        REFERENCES:

        - [Gar2015]_
        - [Ros1999]_

        TESTS::

            sage: A = posets.StandardExample(10); A
            Finite poset containing 20 elements
            sage: len(A.cover_relations())
            90

            sage: P = posets.StandardExample(5, facade=False)
            sage: P(4) < P(3), P(4) > P(3)
            (False, False)
        """
    @staticmethod
    def SymmetricGroupBruhatOrderPoset(n):
        """
        The poset of permutations with respect to Bruhat order.

        EXAMPLES::

            sage: posets.SymmetricGroupBruhatOrderPoset(4)
            Finite poset containing 24 elements
        """
    @staticmethod
    def SymmetricGroupBruhatIntervalPoset(start, end):
        """
        The poset of permutations with respect to Bruhat order.

        INPUT:

        - ``start`` -- list permutation

        - ``end`` -- list permutation (same n, of course)

        .. NOTE::

           Must have ``start`` <= ``end``.

        EXAMPLES:

        Any interval is rank symmetric if and only if it avoids these
        permutations::

            sage: P1 = posets.SymmetricGroupBruhatIntervalPoset([1,2,3,4], [3,4,1,2])
            sage: P2 = posets.SymmetricGroupBruhatIntervalPoset([1,2,3,4], [4,2,3,1])
            sage: ranks1 = [P1.rank(v) for v in P1]
            sage: ranks2 = [P2.rank(v) for v in P2]
            sage: [ranks1.count(i) for i in sorted(set(ranks1))]
            [1, 3, 5, 4, 1]
            sage: [ranks2.count(i) for i in sorted(set(ranks2))]
            [1, 3, 5, 6, 4, 1]
        """
    @staticmethod
    def SymmetricGroupWeakOrderPoset(n, labels: str = 'permutations', side: str = 'right'):
        """
        The poset of permutations of `\\{ 1, 2, \\ldots, n \\}` with respect
        to the weak order (also known as the permutohedron order, cf.
        :meth:`~sage.combinat.permutation.Permutation.permutohedron_lequal`).

        The optional variable ``labels`` (default: ``'permutations'``)
        determines the labelling of the elements if `n < 10`. The optional
        variable ``side`` (default: ``'right'``) determines whether the
        right or the left permutohedron order is to be used.

        EXAMPLES::

            sage: posets.SymmetricGroupWeakOrderPoset(4)
            Finite poset containing 24 elements
        """
    @staticmethod
    def TetrahedralPoset(n, *colors, **labels):
        """
        Return the tetrahedral poset based on the input colors.

        This method will return the tetrahedral poset with `n-1` layers and
        covering relations based on the input colors of 'green', 'red',
        'orange', 'silver', 'yellow' and 'blue' as defined in [Striker2011]_.
        For particular color choices, the order ideals of the resulting
        tetrahedral poset will be isomorphic to known combinatorial objects.

        For example, for the colors 'blue', 'yellow', 'orange', and 'green',
        the order ideals will be in bijection with alternating sign matrices.
        For the colors 'yellow', 'orange', and 'green', the order ideals will
        be in bijection with semistandard Young tableaux of staircase shape.
        For the colors 'red', 'orange', 'green', and optionally 'yellow', the
        order ideals will be in bijection with totally symmetric
        self-complementary plane partitions in a `2n \\times 2n \\times 2n` box.

        INPUT:

        - ``n`` -- defines the number (n-1) of layers in the poset

        - ``colors`` -- the colors that define the covering relations of the
          poset; colors used are 'green', 'red', 'yellow', 'orange', 'silver',
          and 'blue'

        - ``labels`` -- keyword variable used to determine whether the poset
          is labeled with integers or tuples.  To label with integers, the
          method should be called with ``labels='integers'``.  Otherwise, the
          labeling will default to tuples.

        EXAMPLES::

            sage: posets.TetrahedralPoset(4,'green','red','yellow','silver','blue','orange')
            Finite poset containing 10 elements

            sage: posets.TetrahedralPoset(4,'green','red','yellow','silver','blue','orange',
            ....:                         labels='integers')
            Finite poset containing 10 elements

            sage: A = AlternatingSignMatrices(3)
            sage: p = A.lattice()
            sage: ji = p.join_irreducibles_poset()
            sage: tet = posets.TetrahedralPoset(3, 'green','yellow','blue','orange')
            sage: ji.is_isomorphic(tet)
            True

        TESTS::

            sage: posets.TetrahedralPoset(4,'scarlet')
            Traceback (most recent call last):
            ...
            ValueError: color input must be among: 'green', 'red', 'yellow',
            'orange', 'silver', and 'blue'
        """
    ShardPoset: Incomplete
    TamariLattice: Incomplete
    DexterSemilattice: Incomplete
    @staticmethod
    def CoxeterGroupAbsoluteOrderPoset(W, use_reduced_words: bool = True):
        """
        Return the poset of elements of a Coxeter group with respect
        to absolute order.

        INPUT:

        - ``W`` -- a Coxeter group
        - ``use_reduced_words`` -- boolean (default: ``True``); if
          ``True``, then the elements are labeled by their lexicographically
          minimal reduced word

        EXAMPLES::

            sage: W = CoxeterGroup(['B', 3])                                            # needs sage.groups
            sage: posets.CoxeterGroupAbsoluteOrderPoset(W)                              # needs sage.groups
            Finite poset containing 48 elements

            sage: W = WeylGroup(['B', 2], prefix='s')                                   # needs sage.groups
            sage: posets.CoxeterGroupAbsoluteOrderPoset(W, False)                       # needs sage.groups
            Finite poset containing 8 elements
        """
    @staticmethod
    def NoncrossingPartitions(W):
        """
        Return the lattice of noncrossing partitions.

        INPUT:

        - ``W`` -- a finite Coxeter group or a Weyl group

        EXAMPLES::

            sage: W = CoxeterGroup(['A', 3])                                            # needs sage.groups
            sage: posets.NoncrossingPartitions(W)                                       # needs sage.groups
            Finite lattice containing 14 elements

            sage: W = WeylGroup(['B', 2], prefix='s')                                   # needs sage.groups
            sage: posets.NoncrossingPartitions(W)                                       # needs sage.groups
            Finite lattice containing 6 elements
        """
    @staticmethod
    def SymmetricGroupAbsoluteOrderPoset(n, labels: str = 'permutations'):
        """
        Return the poset of permutations with respect to absolute order.

        INPUT:

        - ``n`` -- a positive integer

        - ``label`` -- (default: ``'permutations'``) a label for the elements
          of the poset returned by the function; the options are

          * ``'permutations'`` -- labels the elements by their
            one-line notation
          * ``'reduced_words'`` -- labels the elements by the
            lexicographically minimal reduced word
          * ``'cycles'`` -- labels the elements by their expression
            as a product of cycles

        EXAMPLES::

            sage: posets.SymmetricGroupAbsoluteOrderPoset(4)                            # needs sage.groups
            Finite poset containing 24 elements
            sage: posets.SymmetricGroupAbsoluteOrderPoset(3, labels='cycles')           # needs sage.groups
            Finite poset containing 6 elements
            sage: posets.SymmetricGroupAbsoluteOrderPoset(3, labels='reduced_words')    # needs sage.groups
            Finite poset containing 6 elements
        """
    @staticmethod
    def UpDownPoset(n, m: int = 1):
        """
        Return the up-down poset on `n` elements where every `(m+1)`
        step is down and the rest are up.

        The case where `m=1` is sometimes referred to as the zig-zag poset
        or the fence.

        INPUT:

        - ``n`` -- nonnegative integer; number of elements in the poset
        - ``m`` -- nonnegative integer (default: 1); how frequently down
          steps occur

        OUTPUT:

        The partially ordered set on `\\{ 0, 1, \\ldots, n-1 \\}`
        where `i` covers `i+1` if `m` divides `i+1`, and `i+1` covers `i`
        otherwise.

        EXAMPLES::

            sage: P = posets.UpDownPoset(7, 2); P
            Finite poset containing 7 elements
            sage: sorted(P.cover_relations())
            [[0, 1], [1, 2], [3, 2], [3, 4], [4, 5], [6, 5]]

        Fibonacci numbers as the number of antichains of a poset::

            sage: [len(posets.UpDownPoset(n).antichains().list()) for n in range(6)]
            [1, 2, 3, 5, 8, 13]

        TESTS::

            sage: P = posets.UpDownPoset(0); P
            Finite poset containing 0 elements
        """
    @staticmethod
    def YoungDiagramPoset(lam, dual: bool = False):
        """
        Return the poset of cells in the Young diagram of a partition.

        INPUT:

        - ``lam`` -- a partition
        - ``dual`` -- boolean (default: ``False``); determines the orientation
          of the poset. If ``True``, then it is a join semilattice,
          otherwise it is a meet semilattice.

        EXAMPLES::

            sage: P = posets.YoungDiagramPoset(Partition([2, 2])); P
            Finite meet-semilattice containing 4 elements

            sage: sorted(P.cover_relations())
            [[(0, 0), (0, 1)], [(0, 0), (1, 0)], [(0, 1), (1, 1)], [(1, 0), (1, 1)]]

            sage: posets.YoungDiagramPoset([3, 2], dual=True)
            Finite join-semilattice containing 5 elements
        """
    @staticmethod
    def YoungsLattice(n):
        """
        Return Young's Lattice up to rank `n`.

        In other words, the poset of partitions
        of size less than or equal to `n` ordered by inclusion.

        INPUT:

        - ``n`` -- positive integer

        EXAMPLES::

            sage: P = posets.YoungsLattice(3); P
            Finite meet-semilattice containing 7 elements
            sage: P.cover_relations()
            [[[], [1]],
             [[1], [1, 1]],
             [[1], [2]],
             [[1, 1], [1, 1, 1]],
             [[1, 1], [2, 1]],
             [[2], [2, 1]],
             [[2], [3]]]
        """
    @staticmethod
    def YoungsLatticePrincipalOrderIdeal(lam):
        """
        Return the principal order ideal of the
        partition `lam` in Young's Lattice.

        INPUT:

        - ``lam`` -- a partition

        EXAMPLES::

            sage: P = posets.YoungsLatticePrincipalOrderIdeal(Partition([2,2]))
            sage: P
            Finite lattice containing 6 elements
            sage: P.cover_relations()
            [[[], [1]],
             [[1], [1, 1]],
             [[1], [2]],
             [[1, 1], [2, 1]],
             [[2], [2, 1]],
             [[2, 1], [2, 2]]]
        """
    @staticmethod
    def YoungFibonacci(n):
        """
        Return the Young-Fibonacci lattice up to rank `n`.

        Elements of the (infinite) lattice are words with letters '1'
        and '2'.  The covers of a word are the words with another '1'
        added somewhere not after the first occurrence of an existing
        '1' and, additionally, the words where the first '1' is replaced by a
        '2'. The lattice is truncated to have rank `n`.

        See :wikipedia:`Young-Fibonacci lattice`.

        EXAMPLES::

            sage: Y5 = posets.YoungFibonacci(5); Y5
            Finite meet-semilattice containing 20 elements
            sage: sorted(Y5.upper_covers(Word('211')))
            [word: 1211, word: 2111, word: 221]

        TESTS::

            sage: posets.YoungFibonacci(0)
            Finite meet-semilattice containing 1 elements
            sage: posets.YoungFibonacci(1)
            Finite meet-semilattice containing 2 elements
        """
    @staticmethod
    def DoubleTailedDiamond(n):
        """
        Return a double-tailed diamond of `2n + 2` elements.

        INPUT:

        - ``n`` -- positive integer

        EXAMPLES::

            sage: P = posets.DoubleTailedDiamond(2); P
            Finite d-complete poset containing 6 elements
            sage: P.cover_relations()
            [[1, 2], [2, 3], [2, 4], [3, 5], [4, 5], [5, 6]]
        """
    @staticmethod
    def PermutationPattern(n):
        """
        Return the poset of permutations under pattern containment
        up to rank `n`.

        INPUT:

        - ``n`` -- positive integer

        A permutation `u = u_1 \\cdots u_n` contains the pattern
        `v = v_1 \\cdots v_m` if there is a (not necessarily consecutive)
        subsequence of `u`  of length `m` whose entries have the same
        relative order as `v`.

        See :wikipedia:`Permutation_pattern`.

        EXAMPLES::

            sage: P4 = posets.PermutationPattern(4); P4
            Finite poset containing 33 elements
            sage: sorted(P4.lower_covers(Permutation([2,4,1,3])))
            [[1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2]]

        .. SEEALSO::

            :meth:`~sage.combinat.permutation.Permutation.has_pattern`

        TESTS::

            sage: posets.PermutationPattern(1)
            Finite poset containing 1 elements
            sage: posets.PermutationPattern(2)
            Finite poset containing 3 elements
        """
    @staticmethod
    def PermutationPatternInterval(bottom, top):
        """
        Return the poset consisting of an interval in the poset of permutations
        under pattern containment between ``bottom`` and ``top``.

        INPUT:

        - ``bottom``, ``top`` -- permutations where ``top`` contains
          ``bottom`` as a pattern

        A permutation `u = u_1 \\cdots u_n` contains the pattern
        `v = v_1 \\cdots v_m` if there is a (not necessarily consecutive)
        subsequence of `u`  of length `m` whose entries have the same
        relative order as `v`.

        See :wikipedia:`Permutation_pattern`.

        EXAMPLES::

            sage: t = Permutation([2,3,1])
            sage: b = Permutation([4,6,2,3,5,1])
            sage: R = posets.PermutationPatternInterval(t, b); R
            Finite poset containing 14 elements
            sage: R.moebius_function(R.bottom(),R.top())
            -4

        .. SEEALSO::

            :meth:`~sage.combinat.permutation.Permutation.has_pattern`,
            :meth:`PermutationPattern`

        TESTS::

            sage: p = Permutation([1])
            sage: posets.PermutationPatternInterval(p, p)
            Finite poset containing 1 elements
        """
    @staticmethod
    def PermutationPatternOccurrenceInterval(bottom, top, pos):
        """
        Return the poset consisting of an interval in the poset of
        permutations under pattern containment between ``bottom`` and
        ``top``, where a specified instance of ``bottom`` in ``top``
        must be maintained.

        INPUT:

        - ``bottom``, ``top`` -- permutations where ``top`` contains
           ``bottom`` as a pattern
        - ``pos`` -- list of indices indicating a distinguished copy of
           ``bottom`` inside ``top`` (indexed starting at 0)

        For further information (and picture illustrating included example),
        see [ST2010]_ .

        See :wikipedia:`Permutation_pattern`.

        EXAMPLES::

            sage: t = Permutation([3,2,1])
            sage: b = Permutation([6,3,4,5,2,1])
            sage: A = posets.PermutationPatternOccurrenceInterval(t, b, (0,2,4)); A
            Finite poset containing 8 elements

        .. SEEALSO::

            :meth:`~sage.combinat.permutation.Permutation.has_pattern`,
            :meth:`PermutationPattern`, :meth:`PermutationPatternInterval`
        """
    @staticmethod
    def RibbonPoset(n, descents):
        """
        Return a ribbon poset on ``n`` vertices with descents at ``descents``.

        INPUT:

        - ``n`` -- the number of vertices
        - ``descents`` -- an iterable; the indices on the ribbon where `y > x`

        EXAMPLES::

            sage: R = Posets.RibbonPoset(5, [1,2])
            sage: sorted(R.cover_relations())
            [[0, 1], [2, 1], [3, 2], [3, 4]]
        """
    @staticmethod
    def MobilePoset(ribbon, hangers, anchor=None):
        """
        Return a mobile poset with the ribbon ``ribbon`` and
        with hanging d-complete posets specified in ``hangers``
        and a d-complete poset attached above, specified in ``anchor``.

        INPUT:

        - ``ribbon`` -- a finite poset that is a ribbon
        - ``hangers`` -- dictionary mapping an element on the ribbon
          to a list of d-complete posets that it covers
        - ``anchor`` -- (optional) a ``tuple`` (``ribbon_elmt``,
          ``anchor_elmt``, ``anchor_poset``), where ``anchor_elmt`` covers
          ``ribbon_elmt``, and ``anchor_elmt`` is an acyclic element of
          ``anchor_poset``

        EXAMPLES::

            sage: R = Posets.RibbonPoset(5, [1,2])
            sage: H = Poset([[5, 6, 7], [(5, 6), (6,7)]])
            sage: M = Posets.MobilePoset(R, {3: [H]})
            sage: len(M.cover_relations())
            7

            sage: P = posets.MobilePoset(posets.RibbonPoset(7, [1,3]),
            ....:         {1: [posets.YoungDiagramPoset([3, 2], dual=True)],
            ....:          3: [posets.DoubleTailedDiamond(6)]},
            ....:         anchor=(4, 2, posets.ChainPoset(6)))
            sage: len(P.cover_relations())
            33
        """
posets = Posets
