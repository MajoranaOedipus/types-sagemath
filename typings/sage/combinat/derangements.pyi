from sage.categories.finite_enumerated_sets import FiniteEnumeratedSets as FiniteEnumeratedSets
from sage.combinat.combinat import CombinatorialElement as CombinatorialElement
from sage.combinat.permutation import Permutation as Permutation, Permutations as Permutations
from sage.misc.misc_c import prod as prod
from sage.misc.prandom import random as random, randrange as randrange
from sage.rings.integer import Integer as Integer
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing as PolynomialRing
from sage.rings.rational_field import QQ as QQ
from sage.structure.parent import Parent as Parent
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

class Derangement(CombinatorialElement):
    """
    A derangement.

    A derangement on a set `S` is a permutation `\\sigma` such that `\\sigma(x)
    \\neq x` for all `x \\in S`, i.e. `\\sigma` is a permutation of `S` with no
    fixed points.

    EXAMPLES::

        sage: D = Derangements(4)
        sage: elt = D([4,3,2,1])
        sage: TestSuite(elt).run()
    """
    def to_permutation(self):
        """
        Return the permutation corresponding to ``self``.

        EXAMPLES::

            sage: D = Derangements(4)
            sage: p = D([4,3,2,1]).to_permutation(); p
            [4, 3, 2, 1]
            sage: type(p)
            <class 'sage.combinat.permutation.StandardPermutations_all_with_category.element_class'>
            sage: D = Derangements([1, 3, 3, 4])
            sage: D[0].to_permutation()
            Traceback (most recent call last):
            ...
            ValueError: can only convert to a permutation for derangements of [1, 2, ..., n]
        """

class Derangements(UniqueRepresentation, Parent):
    """
    The class of all derangements of a set or multiset.

    A derangement on a set `S` is a permutation `\\sigma` such that `\\sigma(x)
    \\neq x` for all `x \\in S`, i.e. `\\sigma` is a permutation of `S` with no
    fixed points.

    For an integer, or a list or string with all elements
    distinct, the derangements are obtained by a standard result described
    in [BV2004]_. For a list or string with repeated elements, the derangements
    are formed by computing all permutations of the input and discarding all
    non-derangements.

    INPUT:

    - ``x`` -- can be an integer which corresponds to derangements of
      `\\{1, 2, 3, \\ldots, x\\}`, a list, or a string

    REFERENCES:

    - [BV2004]_
    - :wikipedia:`Derangement`

    EXAMPLES::

        sage: D1 = Derangements([2,3,4,5])
        sage: D1.list()
        [[3, 4, 5, 2],
         [5, 4, 2, 3],
         [3, 5, 2, 4],
         [4, 5, 3, 2],
         [4, 2, 5, 3],
         [5, 2, 3, 4],
         [5, 4, 3, 2],
         [4, 5, 2, 3],
         [3, 2, 5, 4]]
        sage: D1.cardinality()
        9
        sage: D1.random_element() # random
        [4, 2, 5, 3]
        sage: D2 = Derangements([1,2,3,1,2,3])
        sage: D2.cardinality()
        10
        sage: D2.list()
        [[2, 1, 1, 3, 3, 2],
         [2, 1, 2, 3, 3, 1],
         [2, 3, 1, 2, 3, 1],
         [2, 3, 1, 3, 1, 2],
         [2, 3, 2, 3, 1, 1],
         [3, 1, 1, 2, 3, 2],
         [3, 1, 2, 2, 3, 1],
         [3, 1, 2, 3, 1, 2],
         [3, 3, 1, 2, 1, 2],
         [3, 3, 2, 2, 1, 1]]
        sage: D2.random_element() # random
        [2, 3, 1, 3, 1, 2]
    """
    @staticmethod
    def __classcall_private__(cls, x):
        """
        Normalize ``x`` to ensure a unique representation.

        EXAMPLES::

            sage: D = Derangements(4)
            sage: D2 = Derangements([1, 2, 3, 4])
            sage: D3 = Derangements((1, 2, 3, 4))
            sage: D is D2
            True
            sage: D is D3
            True
        """
    def __init__(self, x) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: D = Derangements(4)
            sage: TestSuite(D).run()
            sage: D = Derangements('abcd')
            sage: TestSuite(D).run()
            sage: D = Derangements([2, 2, 1, 1])
            sage: TestSuite(D).run()
        """
    Element = Derangement
    def __iter__(self):
        """
        Iterate through ``self``.

        EXAMPLES::

            sage: D = Derangements(4)
            sage: D.list() # indirect doctest
            [[2, 3, 4, 1],
             [4, 3, 1, 2],
             [2, 4, 1, 3],
             [3, 4, 2, 1],
             [3, 1, 4, 2],
             [4, 1, 2, 3],
             [4, 3, 2, 1],
             [3, 4, 1, 2],
             [2, 1, 4, 3]]
            sage: D = Derangements([1,44,918,67])
            sage: D.list()
            [[44, 918, 67, 1],
             [67, 918, 1, 44],
             [44, 67, 1, 918],
             [918, 67, 44, 1],
             [918, 1, 67, 44],
             [67, 1, 44, 918],
             [67, 918, 44, 1],
             [918, 67, 1, 44],
             [44, 1, 67, 918]]
            sage: D = Derangements(['A','AT','CAT','CATS'])
            sage: D.list()
            [['AT', 'CAT', 'CATS', 'A'],
             ['CATS', 'CAT', 'A', 'AT'],
             ['AT', 'CATS', 'A', 'CAT'],
             ['CAT', 'CATS', 'AT', 'A'],
             ['CAT', 'A', 'CATS', 'AT'],
             ['CATS', 'A', 'AT', 'CAT'],
             ['CATS', 'CAT', 'AT', 'A'],
             ['CAT', 'CATS', 'A', 'AT'],
             ['AT', 'A', 'CATS', 'CAT']]
            sage: D = Derangements('CART')
            sage: D.list()
            [['A', 'R', 'T', 'C'],
             ['T', 'R', 'C', 'A'],
             ['A', 'T', 'C', 'R'],
             ['R', 'T', 'A', 'C'],
             ['R', 'C', 'T', 'A'],
             ['T', 'C', 'A', 'R'],
             ['T', 'R', 'A', 'C'],
             ['R', 'T', 'C', 'A'],
             ['A', 'C', 'T', 'R']]
            sage: D = Derangements([1,1,2,2,3,3])
            sage: D.list()
            [[2, 2, 3, 3, 1, 1],
             [2, 3, 1, 3, 1, 2],
             [2, 3, 1, 3, 2, 1],
             [2, 3, 3, 1, 1, 2],
             [2, 3, 3, 1, 2, 1],
             [3, 2, 1, 3, 1, 2],
             [3, 2, 1, 3, 2, 1],
             [3, 2, 3, 1, 1, 2],
             [3, 2, 3, 1, 2, 1],
             [3, 3, 1, 1, 2, 2]]
            sage: D = Derangements('SATTAS')
            sage: D.list()
            [['A', 'S', 'S', 'A', 'T', 'T'],
             ['A', 'S', 'A', 'S', 'T', 'T'],
             ['A', 'T', 'S', 'S', 'T', 'A'],
             ['A', 'T', 'S', 'A', 'S', 'T'],
             ['A', 'T', 'A', 'S', 'S', 'T'],
             ['T', 'S', 'S', 'A', 'T', 'A'],
             ['T', 'S', 'A', 'S', 'T', 'A'],
             ['T', 'S', 'A', 'A', 'S', 'T'],
             ['T', 'T', 'S', 'A', 'S', 'A'],
             ['T', 'T', 'A', 'S', 'S', 'A']]
            sage: D = Derangements([1,1,2,2,2])
            sage: D.list()
            []
            sage: D = Derangements(0)
            sage: D.list()
            [[]]
        """
    def cardinality(self):
        """
        Count the number of derangements of a positive integer, a list,
        or a string.

        The list or string may contain repeated
        elements.  If an integer `n` is given, the value returned
        is the number of derangements of `[1, 2, 3, \\ldots, n]`.

        For an integer, or a list or string with all elements
        distinct, the value is obtained by the standard result
        `D_2 = 1, D_3 = 2, D_n = (n-1) (D_{n-1} + D_{n-2})`.

        For a list or string with repeated elements, the number of
        derangements is computed by Macmahon's theorem. If the numbers
        of repeated elements are `a_1, a_2, \\ldots, a_k` then the number
        of derangements is given by the coefficient of `x_1 x_2 \\cdots
        x_k` in the expansion of `\\prod_{i=0}^k (S - s_i)^{a_i}` where
        `S = x_1 + x_2 + \\cdots + x_k`.

        EXAMPLES::

            sage: D = Derangements(5)
            sage: D.cardinality()
            44
            sage: D = Derangements([1,44,918,67,254])
            sage: D.cardinality()
            44
            sage: D = Derangements(['A','AT','CAT','CATS','CARTS'])
            sage: D.cardinality()
            44
            sage: D = Derangements('UNCOPYRIGHTABLE')
            sage: D.cardinality()
            481066515734
            sage: D = Derangements([1,1,2,2,3,3])
            sage: D.cardinality()
            10
            sage: D = Derangements('SATTAS')
            sage: D.cardinality()
            10
            sage: D = Derangements([1,1,2,2,2])
            sage: D.cardinality()
            0
            sage: D = Derangements(0)
            sage: D.cardinality()
            1
        """
    def random_element(self):
        """
        Produce all derangements of a positive integer, a list, or
        a string.  The list or string may contain repeated elements.
        If an integer `n` is given, then a random
        derangements of `[1, 2, 3, \\ldots, n]` is returned

        For an integer, or a list or string with all elements
        distinct, the value is obtained by an algorithm described in
        [MPP2008]_. For a list or string with repeated elements the
        derangement is formed by choosing an element at random from the list of
        all possible derangements.

        OUTPUT:

        A single list or string containing a derangement, or an
        empty list if there are no derangements.

        EXAMPLES::

            sage: D = Derangements(4)
            sage: D.random_element() # random
            [2, 3, 4, 1]
            sage: D = Derangements(['A','AT','CAT','CATS','CARTS','CARETS'])
            sage: D.random_element() # random
            ['AT', 'CARTS', 'A', 'CAT', 'CARETS', 'CATS']
            sage: D = Derangements('UNCOPYRIGHTABLE')
            sage: D.random_element() # random
            ['C', 'U', 'I', 'H', 'O', 'G', 'N', 'B', 'E', 'L', 'A', 'R', 'P', 'Y', 'T']
            sage: D = Derangements([1,1,1,1,2,2,2,2,3,3,3,3])
            sage: D.random_element() # random
            [3, 2, 2, 3, 1, 3, 1, 3, 2, 1, 1, 2]
            sage: D = Derangements('ESSENCES')
            sage: D.random_element() # random
            ['N', 'E', 'E', 'C', 'S', 'S', 'S', 'E']
            sage: D = Derangements([1,1,2,2,2])
            sage: D.random_element()
            []

        TESTS:

        Check that index error discovered in :issue:`29974` is fixed::

            sage: D = Derangements([1,1,2,2])
            sage: _ = [D.random_element() for _ in range(20)]
        """
