from sage.arith.misc import divisors as divisors, euler_phi as euler_phi, factorial as factorial, gcd as gcd
from sage.categories.finite_enumerated_sets import FiniteEnumeratedSets as FiniteEnumeratedSets
from sage.combinat.composition import Composition as Composition
from sage.combinat.misc import DoublyLinkedList as DoublyLinkedList
from sage.misc.misc_c import prod as prod
from sage.rings.integer import Integer as Integer
from sage.rings.integer_ring import ZZ as ZZ
from sage.structure.parent import Parent as Parent
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

def Necklaces(content):
    """
    Return the set of necklaces with evaluation ``content``.

    A necklace is a list of integers that such that the list is
    the smallest lexicographic representative of all the cyclic shifts
    of the list.

    .. SEEALSO::

        :class:`LyndonWords`

    INPUT:

    - ``content`` -- list or tuple of nonnegative integers

    EXAMPLES::

        sage: Necklaces([2,1,1])
        Necklaces with evaluation [2, 1, 1]
        sage: Necklaces([2,1,1]).cardinality()
        3
        sage: Necklaces([2,1,1]).first()
        [1, 1, 2, 3]
        sage: Necklaces([2,1,1]).last()
        [1, 2, 1, 3]
        sage: Necklaces([2,1,1]).list()
        [[1, 1, 2, 3], [1, 1, 3, 2], [1, 2, 1, 3]]
        sage: Necklaces([0,2,1,1]).list()
        [[2, 2, 3, 4], [2, 2, 4, 3], [2, 3, 2, 4]]
        sage: Necklaces([2,0,1,1]).list()
        [[1, 1, 3, 4], [1, 1, 4, 3], [1, 3, 1, 4]]
    """

class Necklaces_evaluation(UniqueRepresentation, Parent):
    """
    Necklaces with a fixed evaluation (content).

    INPUT:

    - ``content`` -- list or tuple of nonnegative integers
    """
    @staticmethod
    def __classcall_private__(cls, content):
        """
        Return the correct parent object, with standardized parameters.

        EXAMPLES::

            sage: Necklaces([2,1,1]) is Necklaces(Composition([2,1,1]))
            True
        """
    def __init__(self, content) -> None:
        """
        Initialize ``self``.

        TESTS::

            sage: N = Necklaces([2,2,2])
            sage: N == loads(dumps(N))
            True
            sage: T = Necklaces([2,1])
            sage: TestSuite(T).run()
        """
    def content(self):
        """
        Return the content (or evaluation) of the necklaces.

        EXAMPLES::

            sage: N = Necklaces([2,2,2])
            sage: N.content()
            [2, 2, 2]
        """
    def __contains__(self, x) -> bool:
        """
        Return ``True`` if ``x`` is the smallest word of all its cyclic shifts
        and the content vector of ``x`` is equal to ``content``.

        INPUT:

        - ``x`` -- list of integers

        EXAMPLES::

            sage: [2,1,2,1] in Necklaces([2,2])
            False
            sage: [1,2,1,2] in Necklaces([2,2])
            True
            sage: [1,1,2,2] in Necklaces([2,2])
            True
            sage: [1,2,2,2] in Necklaces([2,2])
            False
            sage: all(n in Necklaces([2,1,3,1]) for n in Necklaces([2,1,3,1]))
            True
            sage: all(n in Necklaces([0,1,2,3]) for n in Necklaces([0,1,2,3]))
            True
        """
    def cardinality(self) -> Integer:
        """
        Return the number of integer necklaces with the evaluation ``content``.

        The formula for the number of necklaces of content `\\alpha`
        a composition of `n` is:

        .. MATH::

            \\sum_{d|gcd(\\alpha)} \\phi(d)
            \\binom{n/d}{\\alpha_1/d, \\ldots, \\alpha_\\ell/d},

        where `\\phi(d)` is the Euler `\\phi` function.

        EXAMPLES::

            sage: Necklaces([]).cardinality()
            0
            sage: Necklaces([2,2]).cardinality()
            2
            sage: Necklaces([2,3,2]).cardinality()
            30
            sage: Necklaces([0,3,2]).cardinality()
            2

        Check to make sure that the count matches up with the number of
        necklace words generated.

        ::

            sage: comps = [[],[2,2],[3,2,7],[4,2],[0,4,2],[2,0,4]] + Compositions(4).list()
            sage: ns = [Necklaces(comp) for comp in comps]
            sage: all(n.cardinality() == len(n.list()) for n in ns)                     # needs sage.libs.pari
            True
        """
    def __iter__(self):
        """
        An iterator for the integer necklaces with evaluation ``content``.

        EXAMPLES::

            sage: Necklaces([]).list()    #indirect test
            []
            sage: Necklaces([1]).list()   #indirect test
            [[1]]
            sage: Necklaces([2]).list()   #indirect test
            [[1, 1]]
            sage: Necklaces([3]).list()   #indirect test
            [[1, 1, 1]]
            sage: Necklaces([3,3]).list() #indirect test
            [[1, 1, 1, 2, 2, 2],
             [1, 1, 2, 1, 2, 2],
             [1, 1, 2, 2, 1, 2],
             [1, 2, 1, 2, 1, 2]]
            sage: Necklaces([2,1,3]).list() #indirect test
            [[1, 1, 2, 3, 3, 3],
             [1, 1, 3, 2, 3, 3],
             [1, 1, 3, 3, 2, 3],
             [1, 1, 3, 3, 3, 2],
             [1, 2, 1, 3, 3, 3],
             [1, 2, 3, 1, 3, 3],
             [1, 2, 3, 3, 1, 3],
             [1, 3, 1, 3, 2, 3],
             [1, 3, 1, 3, 3, 2],
             [1, 3, 2, 1, 3, 3]]
        """
