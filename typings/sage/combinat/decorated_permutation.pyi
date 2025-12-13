from sage.arith.misc import factorial as factorial
from sage.categories.finite_enumerated_sets import FiniteEnumeratedSets as FiniteEnumeratedSets
from sage.combinat.colored_permutations import SignedPermutations as SignedPermutations
from sage.combinat.permutation import Permutations as Permutations
from sage.combinat.subset import Subsets as Subsets
from sage.misc.inherit_comparison import InheritComparisonClasscallMetaclass as InheritComparisonClasscallMetaclass
from sage.rings.integer import Integer as Integer
from sage.structure.list_clone import ClonableArray as ClonableArray
from sage.structure.parent import Parent as Parent
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

class DecoratedPermutation(ClonableArray, metaclass=InheritComparisonClasscallMetaclass):
    """
    A decorated permutation.

    A decorated permutation is a signed permutation where all
    non-fixed points have positive sign.
    """
    @staticmethod
    def __classcall_private__(cls, pi):
        """
        Create a decorated permutation.

        EXAMPLES::

            sage: DecoratedPermutation([2, 1, 3])
            [2, 1, 3]

            sage: DecoratedPermutation([2, 1, -3])
            [2, 1, -3]

        TESTS:

        Check that hashing and comparison works::

            sage: S = DecoratedPermutations(3)
            sage: elt1 = S([2, 1, -3])
            sage: elt2 = DecoratedPermutation([2, 1, -3])
            sage: elt1 == elt2
            True

            sage: elt1 == [2, 1, -3]
            False

            sage: elt2 = DecoratedPermutation([2, 1, 3])
            sage: elt1 != elt2
            True

            sage: hash(elt1)                                                    # random
            915443076393556996
        """
    def __init__(self, parent, pi, check: bool = True) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: S = DecoratedPermutations(3)
            sage: elt = S([2, 1, -3])
            sage: TestSuite(elt).run()
        """
    def check(self) -> None:
        """
        Check that ``self`` is a valid decorated permutation.

        EXAMPLES::

            sage: S = DecoratedPermutations(3)
            sage: elt = S([2, 1, -3])
            sage: elt.check()
            sage: elt = S([2, -1, 3])
            Traceback (most recent call last):
            ...
            ValueError: invalid decorated permutation
        """
    def size(self):
        """
        Return the size of the decorated permutation.

        EXAMPLES::

            sage: DecoratedPermutation([2, 1, -3]).size()
            3
        """
    def to_signed_permutation(self):
        """
        Return ``self`` as a signed permutation.

        EXAMPLES::

            sage: DecoratedPermutation([2, 1, -3]).to_signed_permutation()
            [2, 1, -3]
        """

class DecoratedPermutations(UniqueRepresentation, Parent):
    """
    Class of all decorated permutations of `n`.

    A decorated permutation is a signed permutation where all
    non-fixed points have positive sign.

    INPUT:

    - ``n`` -- integer; the size of the decorated permutations

    EXAMPLES:

    This will create an instance to manipulate the decorated
    permutations of size 3::

        sage: S = DecoratedPermutations(3); S
        Decorated permutations of size 3
        sage: S.cardinality()
        16
    """
    def __init__(self, n) -> None:
        """
        Initialize ``self``.

        TESTS::

            sage: S = DecoratedPermutations(4)
            sage: TestSuite(S).run()
        """
    def __contains__(self, pi) -> bool:
        """
        Check if ``pi`` is in ``self``.

        TESTS::

            sage: S = DecoratedPermutations(3)
            sage: [2, 1, -3] in S
            True
            sage: [2, -1, 3] in S
            False
        """
    Element = DecoratedPermutation
    def cardinality(self):
        """
        Return the cardinality of ``self``.

        The number of decorated permutations of size `n` is equal to

        .. MATH::

            \\sum_{k=0^n} \\frac{n!}{k!}

        EXAMPLES::

            sage: [DecoratedPermutations(n).cardinality() for n in range(11)]
            [1, 2, 5, 16, 65, 326, 1957, 13700, 109601, 986410, 9864101]
        """
    def __iter__(self):
        """
        Iterator on the decorated permutations of size `n`.

        TESTS::

            sage: S = DecoratedPermutations(2); S.list()
            [[1, 2], [-1, 2], [1, -2], [-1, -2], [2, 1]]
            sage: sum(1 for a in S)
            5
        """
