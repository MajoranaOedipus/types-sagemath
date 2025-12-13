from _typeshed import Incomplete
from sage.arith.misc import binomial as binomial
from sage.categories.finite_enumerated_sets import FiniteEnumeratedSets as FiniteEnumeratedSets
from sage.rings.integer_ring import ZZ as ZZ
from sage.structure.parent import Parent as Parent
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

class Tuples(Parent, UniqueRepresentation):
    '''
    Return the enumerated set of ordered tuples of S of length k.

    An ordered tuple of length k of set is an ordered selection with
    repetition and is represented by a list of length k containing
    elements of set.

    EXAMPLES::

        sage: S = [1,2]
        sage: Tuples(S,3).list()
        [(1, 1, 1), (2, 1, 1), (1, 2, 1), (2, 2, 1), (1, 1, 2),
         (2, 1, 2), (1, 2, 2), (2, 2, 2)]
        sage: mset = ["s","t","e","i","n"]
        sage: Tuples(mset,2).list()
        [(\'s\', \'s\'), (\'t\', \'s\'), (\'e\', \'s\'), (\'i\', \'s\'), (\'n\', \'s\'),
         (\'s\', \'t\'), (\'t\', \'t\'), (\'e\', \'t\'), (\'i\', \'t\'), (\'n\', \'t\'),
         (\'s\', \'e\'), (\'t\', \'e\'), (\'e\', \'e\'), (\'i\', \'e\'), (\'n\', \'e\'),
         (\'s\', \'i\'), (\'t\', \'i\'), (\'e\', \'i\'), (\'i\', \'i\'), (\'n\', \'i\'),
         (\'s\', \'n\'), (\'t\', \'n\'), (\'e\', \'n\'), (\'i\', \'n\'), (\'n\', \'n\')]

    ::

        sage: K.<a> = GF(4, \'a\')                                                        # needs sage.rings.finite_rings
        sage: mset = sorted((x for x in K if x != 0), key=str)                          # needs sage.rings.finite_rings
        sage: Tuples(mset, 2).list()                                                    # needs sage.rings.finite_rings
        [(1, 1),     (a, 1),     (a + 1, 1),
         (1, a),     (a, a),     (a + 1, a),
         (1, a + 1), (a, a + 1), (a + 1, a + 1)]
    '''
    @staticmethod
    def __classcall_private__(cls, S, k):
        """
        Normalize input to ensure a unique representation.

        EXAMPLES::

            sage: T = Tuples(['l','i','t'],2); T
            Tuples of ('l', 'i', 't') of length 2
        """
    S: Incomplete
    k: Incomplete
    def __init__(self, S, k) -> None:
        """
        TESTS::

            sage: T = Tuples([1,2,3],2)
            sage: T == loads(dumps(T))
            True
        """
    def unrank(self, i):
        """
        Return the `i`-th element of the set of Tuples.

        INPUT:

        - ``i`` -- integer between `0` and `n-1`, where `n` is the cardinality
          of this set

        EXAMPLES::

            sage: T = Tuples(range(7), 6)
            sage: T[73451]
            (0, 0, 1, 4, 2, 4)

        TESTS:

        Verify that :meth:`unrank` is giving the correct result::

            sage: T = Tuples(range(4), 5)
            sage: all(T[i] == x for i,x in enumerate(T))
            True

        Verify that :meth:`unrank` is fast for large inputs::

            sage: Tuples(range(3), 30)[10^12]
            (1, 0, 0, 1, 1, 1, 2, 0, 1, 2, 0, 1, 1, 0, 2, 1, 1, 0, 1, 2, 1, 2,
            1, 1, 0, 1, 0, 0, 0, 0)

        Verify that :meth:`unrank` normalizes ``i``::

            sage: T = Tuples(range(3), 2)
            sage: T[QQ(4/2)]
            (2, 0)
            sage: T[QQ(1/2)]
            Traceback (most recent call last):
            ...
            TypeError: no conversion of this rational to integer

        Verify that :meth:`unrank` throws an error when ``i`` is out of bounds::

            sage: T = Tuples(range(3), 3)
            sage: T[27]
            Traceback (most recent call last):
            ...
            IndexError: index i (=27) is greater than or equal to the cardinality
            sage: T[-28]
            Traceback (most recent call last):
            ...
            IndexError: index out of range

        Verify that :meth:`unrank` works correctly for Tuples where `k = 1`::

            sage: T = Tuples(range(6), 1)
            sage: T[5]
            (5,)

        Verify that :meth:`unrank` works when called directly::

            sage: T = Tuples(range(4), 3)
            sage: T.unrank(19)
            (3, 0, 1)
            sage: T.unrank(-1)
            Traceback (most recent call last):
            ...
            IndexError: index out of range

        Verify that :meth:`unrank` works with non-integer sets::

            sage: T = Tuples(['a', 'b', 'c'], 3)
            sage: T[15]
            ('a', 'c', 'b')
            sage: T = Tuples([None, 1, ZZ, GF(2)], 5)
            sage: T[30]
            (Integer Ring, Finite Field of size 2, 1, None, None)

        Verify that :meth:`unrank` gives the correct answer when `|S| < 1`::

            sage: T = Tuples([],5)
            sage: T[0]
            Traceback (most recent call last):
            ...
            IndexError: index i (=0) is greater than or equal to the cardinality
            sage: list(T)
            []

        Verify that :meth:`unrank` gives the correct answer when `|S| = 1`::

            sage: T = Tuples([1],5)
            sage: T[0]
            (1, 1, 1, 1, 1)

        Verify that :meth:`unrank` gives the correct answer when `k = 0`::

            sage: T = Tuples(range(6), 0)
            sage: list(T)
            [()]
            sage: T[0]
            ()
            sage: T[1]
            Traceback (most recent call last):
            ...
            IndexError: index i (=1) is greater than or equal to the cardinality

        Verify that :meth:`unrank` gives the correct answer when `|S| < 1` and
        `k = 0`::

            sage: T = Tuples(range(0), 0)
            sage: T[0]
            ()
            sage: T[-1]
            ()
            sage: T[1]
            Traceback (most recent call last):
            ...
            IndexError: index i (=1) is greater than or equal to the cardinality

        Verify that :issue:`39534` has been fixed::

            sage: T = Tuples(range(3), 30).random_element()
            sage: all(v in range(3) for v in T)
            True
            sage: len(T)
            30
        """
    def __iter__(self):
        '''
        EXAMPLES::

            sage: S = [1,2]
            sage: Tuples(S,3).list()
            [(1, 1, 1), (2, 1, 1), (1, 2, 1), (2, 2, 1), (1, 1, 2),
             (2, 1, 2), (1, 2, 2), (2, 2, 2)]
            sage: mset = ["s","t","e","i","n"]
            sage: Tuples(mset,2).list()
            [(\'s\', \'s\'), (\'t\', \'s\'), (\'e\', \'s\'), (\'i\', \'s\'), (\'n\', \'s\'),
             (\'s\', \'t\'), (\'t\', \'t\'), (\'e\', \'t\'), (\'i\', \'t\'), (\'n\', \'t\'),
             (\'s\', \'e\'), (\'t\', \'e\'), (\'e\', \'e\'), (\'i\', \'e\'), (\'n\', \'e\'),
             (\'s\', \'i\'), (\'t\', \'i\'), (\'e\', \'i\'), (\'i\', \'i\'), (\'n\', \'i\'),
             (\'s\', \'n\'), (\'t\', \'n\'), (\'e\', \'n\'), (\'i\', \'n\'), (\'n\', \'n\')]
            sage: Tuples((1,1,2),3).list()
            [(1, 1, 1), (2, 1, 1), (1, 2, 1), (2, 2, 1), (1, 1, 2),
             (2, 1, 2), (1, 2, 2), (2, 2, 2)]
        '''
    def cardinality(self):
        """
        EXAMPLES::

            sage: S = [1,2,3,4,5]
            sage: Tuples(S,2).cardinality()
            25
            sage: S = [1,1,2,3,4,5]
            sage: Tuples(S,2).cardinality()
            25
        """
Tuples_sk = Tuples

class UnorderedTuples(Parent, UniqueRepresentation):
    '''
    Return the enumerated set of unordered tuples of S of length k.

    An unordered tuple of length k of set is a unordered selection with
    repetitions of set and is represented by a sorted list of length k
    containing elements from set.

    EXAMPLES::

        sage: S = [1,2]
        sage: UnorderedTuples(S,3).list()
        [(1, 1, 1), (1, 1, 2), (1, 2, 2), (2, 2, 2)]
        sage: UnorderedTuples(["a","b","c"],2).list()
        [(\'a\', \'a\'), (\'a\', \'b\'), (\'a\', \'c\'), (\'b\', \'b\'), (\'b\', \'c\'),
         (\'c\', \'c\')]
    '''
    @staticmethod
    def __classcall_private__(cls, S, k):
        """
        Normalize input to ensure a unique representation.

        EXAMPLES::

            sage: T = UnorderedTuples(['l','i','t'],2); T
            Unordered tuples of ('l', 'i', 't') of length 2
        """
    S: Incomplete
    k: Incomplete
    def __init__(self, S, k) -> None:
        """
        TESTS::

            sage: T = Tuples([1,2,3],2)
            sage: T == loads(dumps(T))
            True
        """
    def __iter__(self):
        '''
        EXAMPLES::

            sage: S = [1,2]
            sage: UnorderedTuples(S,3).list()
            [(1, 1, 1), (1, 1, 2), (1, 2, 2), (2, 2, 2)]
            sage: UnorderedTuples(["a","b","c"],2).list()
            [(\'a\', \'a\'), (\'a\', \'b\'), (\'a\', \'c\'), (\'b\', \'b\'), (\'b\', \'c\'),
             (\'c\', \'c\')]
            sage: UnorderedTuples([1,1,2],3).list()
            [(1, 1, 1), (1, 1, 2), (1, 2, 2), (2, 2, 2)]
        '''
    def cardinality(self):
        """
        EXAMPLES::

            sage: S = [1,2,3,4,5]
            sage: UnorderedTuples(S,2).cardinality()
            15
        """
UnorderedTuples_sk = UnorderedTuples
