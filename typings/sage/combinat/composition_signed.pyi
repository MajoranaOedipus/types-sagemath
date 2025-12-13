from .composition import Composition as Composition, Compositions_n as Compositions_n
from sage.arith.misc import binomial as binomial
from sage.misc.persist import register_unpickle_override as register_unpickle_override
from sage.rings.integer import Integer as Integer
from sage.rings.integer_ring import ZZ as ZZ

class SignedCompositions(Compositions_n):
    """
    The class of signed compositions of `n`.

    EXAMPLES::

        sage: SC3 = SignedCompositions(3); SC3
        Signed compositions of 3
        sage: SC3.cardinality()
        18
        sage: len(SC3.list())
        18
        sage: SC3.first()
        [1, 1, 1]
        sage: SC3.last()
        [-3]
        sage: SC3.random_element() # random
        [1, -1, 1]
        sage: SC3.list()
        [[1, 1, 1],
         [1, 1, -1],
         [1, -1, 1],
         [1, -1, -1],
         [-1, 1, 1],
         [-1, 1, -1],
         [-1, -1, 1],
         [-1, -1, -1],
         [1, 2],
         [1, -2],
         [-1, 2],
         [-1, -2],
         [2, 1],
         [2, -1],
         [-2, 1],
         [-2, -1],
         [3],
         [-3]]

    TESTS::

        sage: SC = SignedCompositions(3)
        sage: TestSuite(SC).run()
    """
    def __contains__(self, x) -> bool:
        """
        TESTS::

            sage: [] in SignedCompositions(0)
            True
            sage: [0] in SignedCompositions(0)
            False
            sage: [2,1,3] in SignedCompositions(6)
            True
            sage: [-2, 1, -3] in SignedCompositions(6)
            True
        """
    def cardinality(self):
        """
        Return the number of elements in ``self``.

        The number of signed compositions of `n` is equal to

        .. MATH::

            \\sum_{i=1}^{n+1} \\binom{n-1}{i-1} 2^i

        EXAMPLES::

            sage: SC4 = SignedCompositions(4)
            sage: SC4.cardinality() == len(SC4.list())
            True
            sage: SignedCompositions(3).cardinality()
            18
        """
    def __iter__(self):
        """
        TESTS::

            sage: SignedCompositions(0).list()   #indirect doctest
            [[]]
            sage: SignedCompositions(1).list()   #indirect doctest
            [[1], [-1]]
            sage: SignedCompositions(2).list()   #indirect doctest
            [[1, 1], [1, -1], [-1, 1], [-1, -1], [2], [-2]]
        """
