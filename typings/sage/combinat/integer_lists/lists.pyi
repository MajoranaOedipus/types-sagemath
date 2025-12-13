from _typeshed import Incomplete
from sage.categories.enumerated_sets import EnumeratedSets as EnumeratedSets
from sage.combinat.integer_lists.base import IntegerListsBackend as IntegerListsBackend
from sage.structure.list_clone import ClonableArray as ClonableArray
from sage.structure.parent import Parent as Parent

class IntegerList(ClonableArray):
    """
    Element class for :class:`IntegerLists`.
    """
    def check(self):
        """
        Check to make sure this is a valid element in its
        :class:`IntegerLists` parent.

        EXAMPLES::

            sage: C = IntegerListsLex(4)
            sage: C([4]).check()
            True
            sage: C([5]).check()
            False
        """

class IntegerLists(Parent):
    '''
    Enumerated set of lists of integers with constraints.

    Currently, this is simply an abstract base class which should not
    be used by itself. See :class:`IntegerListsLex` for a class which
    can be used by end users.

    ``IntegerLists`` is just a Python front-end, acting as a
    :class:`Parent`, supporting element classes and so on.
    The attribute ``.backend`` which is an instance of
    :class:`sage.combinat.integer_lists.base.IntegerListsBackend` is the
    Cython back-end which implements all operations such as iteration.

    The front-end (i.e. this class) and the back-end are supposed to be
    orthogonal: there is no imposed correspondence between front-ends
    and back-ends.

    For example, the set of partitions of 5 and the set of weakly
    decreasing sequences which sum to 5 might be implemented by the
    same back-end, but they will be presented to the user by a
    different front-end.

    EXAMPLES::

        sage: from sage.combinat.integer_lists import IntegerLists
        sage: L = IntegerLists(5)
        sage: L
        Integer lists of sum 5 satisfying certain constraints

        sage: IntegerListsLex(2, length=3, name="A given name")
        A given name
    '''
    backend: Incomplete
    backend_class = IntegerListsBackend
    Element = IntegerList
    def __init__(self, *args, **kwds) -> None:
        """
        Initialize ``self``.

        TESTS::

            sage: from sage.combinat.integer_lists import IntegerLists
            sage: C = IntegerLists(2, length=3)
            sage: C == loads(dumps(C))
            True
        """
    def __eq__(self, other):
        """
        Return whether ``self == other``.

        EXAMPLES::

            sage: C = IntegerListsLex(2, length=3)
            sage: D = IntegerListsLex(2, length=3); L = D.list()
            sage: E = IntegerListsLex(2, min_length=3)
            sage: F = IntegerListsLex(2, length=3, element_constructor=list)
            sage: G = IntegerListsLex(4, length=3)
            sage: C == C
            True
            sage: C == D
            True
            sage: C == E
            False
            sage: C == F
            False
            sage: C == None
            False
            sage: C == G
            False

        This is a minimal implementation enabling pickling tests. It
        is safe, but one would want the two following objects to be
        detected as equal::

            sage: C = IntegerListsLex(2, ceiling=[1,1,1])
            sage: D = IntegerListsLex(2, ceiling=[1,1,1])
            sage: C == D
            False

        TESTS:

        This used to fail due to poor equality testing. See
        :issue:`17979`, comment 433::

            sage: DisjointUnionEnumeratedSets(Family([2,2],
            ....:     lambda n: IntegerListsLex(n, length=2))).list()
            [[2, 0], [1, 1], [0, 2], [2, 0], [1, 1], [0, 2]]
            sage: DisjointUnionEnumeratedSets(Family([2,2],
            ....:     lambda n: IntegerListsLex(n, length=1))).list()
            [[2], [2]]
        """
    def __ne__(self, other):
        """
        Return whether ``self != other``.

        EXAMPLES::

            sage: C = IntegerListsLex(2, length=3)
            sage: D = IntegerListsLex(2, length=3); L = D.list()
            sage: E = IntegerListsLex(2, max_length=3)
            sage: C != D
            False
            sage: C != E
            True
        """
    def __hash__(self):
        """
        Return the hash of ``self``.

        EXAMPLES::

            sage: C = IntegerListsLex(2, length=3)
            sage: D = IntegerListsLex(2, max_length=3)
            sage: hash(C) == hash(C)
            True
        """
    def __iter__(self):
        """
        Return an iterator for the elements of ``self``.

        EXAMPLES::

            sage: C = IntegerListsLex(2, length=3)
            sage: list(C)     # indirect doctest
            [[2, 0, 0], [1, 1, 0], [1, 0, 1], [0, 2, 0], [0, 1, 1], [0, 0, 2]]
        """
    def __getattr__(self, name):
        """
        Get an attribute of the implementation backend.

        Ideally, this would be done using multiple inheritance, but
        Python doesn't support that for built-in types.

        EXAMPLES::

            sage: C = IntegerListsLex(2, length=3)
            sage: C.min_length
            3

        TESTS:

        Check that uninitialized instances do not lead to infinite
        recursion because there is no ``backend`` attribute::

            sage: from sage.combinat.integer_lists import IntegerLists
            sage: L = IntegerLists.__new__(IntegerLists)
            sage: L.foo
            Traceback (most recent call last):
            ...
            AttributeError: 'NoneType' object has no attribute 'foo'...
        """
    def __contains__(self, item) -> bool:
        """
        Return ``True`` if ``item`` meets the constraints imposed by
        the arguments.

        EXAMPLES::

            sage: C = IntegerListsLex(n=2, max_length=3, min_slope=0)
            sage: all(l in C for l in C)
            True
        """
