from sage.categories.enumerated_sets import EnumeratedSets as EnumeratedSets
from sage.misc.cachefunc import cached_function as cached_function
from sage.misc.callable_dict import CallableDict as CallableDict
from sage.structure.parent import Parent as Parent

def from_list(l):
    """
    Return a ranker from the list l.

    INPUT:

    - ``l`` -- list

    OUTPUT: ``[rank, unrank]`` -- functions

    EXAMPLES::

        sage: import sage.combinat.ranker as ranker
        sage: l = [1,2,3]
        sage: r,u = ranker.from_list(l)
        sage: r(1)
        0
        sage: r(3)
        2
        sage: u(2)
        3
        sage: u(0)
        1
    """
def rank_from_list(l):
    """
    Return a rank function for the elements of ``l``.

    INPUT:

    - ``l`` -- a duplicate free list (or iterable) of hashable objects

    OUTPUT:

    - a function from the elements of ``l`` to ``0,...,len(l)``

    EXAMPLES::

        sage: import sage.combinat.ranker as ranker
        sage: l = ['a', 'b', 'c']
        sage: r = ranker.rank_from_list(l)
        sage: r('a')
        0
        sage: r('c')
        2

    For non elements a :exc:`ValueError` is raised, as with the usual
    ``index`` method of lists::

        sage: r('blah')
        Traceback (most recent call last):
        ...
        ValueError: 'blah' is not in dict

    Currently, the rank function is a
    :class:`~sage.misc.callable_dict.CallableDict`; but this is an
    implementation detail::

        sage: type(r)
        <class 'sage.misc.callable_dict.CallableDict'>
        sage: r
        {'a': 0, 'b': 1, 'c': 2}

    With the current implementation, no error is issued in case of
    duplicate value in ``l``. Instead, the rank function returns the
    position of some of the duplicates::

        sage: r = ranker.rank_from_list(['a', 'b', 'a', 'c'])
        sage: r('a')
        2

    Constructing the rank function itself is of complexity
    ``O(len(l))``. Then, each call to the rank function consists of an
    essentially constant time dictionary lookup.

    TESTS::

        sage: TestSuite(r).run()
    """
def unrank_from_list(l):
    """
    Return an unrank function from a list.

    EXAMPLES::

        sage: import sage.combinat.ranker as ranker
        sage: l = [1,2,3]
        sage: u = ranker.unrank_from_list(l)
        sage: u(2)
        3
        sage: u(0)
        1
    """
def on_fly():
    """
    Return a pair of enumeration functions rank / unrank.

    rank assigns on the fly an integer, starting from 0, to any object
    passed as argument. The object should be hashable. unrank is the
    inverse function; it returns None for indices that have not yet
    been assigned.

    EXAMPLES::

        sage: [rank, unrank] = sage.combinat.ranker.on_fly()
        sage: rank('a')
        0
        sage: rank('b')
        1
        sage: rank('c')
        2
        sage: rank('a')
        0
        sage: unrank(2)
        'c'
        sage: unrank(3)
        sage: rank('d')
        3
        sage: unrank(3)
        'd'

    .. TODO:: add tests as in combinat::rankers
    """
def unrank(L, i):
    """
    Return the `i`-th element of `L`.

    INPUT:

    - ``L`` -- list, tuple, finite enumerated set, etc.
    - ``i`` -- integer

    The purpose of this utility is to give a uniform idiom to recover
    the `i`-th element of an object ``L``, whether ``L`` is a list,
    tuple (or more generally a :class:`collections.abc.Sequence`), an
    enumerated set, some old parent of Sage still implementing
    unranking in the method ``__getitem__``, or an iterable (see
    :class:`collections.abc.Iterable`). See :issue:`15919`.

    EXAMPLES:

    Lists, tuples, and other :class:`sequences <collections.abc.Sequence>`::

        sage: from sage.combinat.ranker import unrank
        sage: unrank(['a','b','c'], 2)
        'c'
        sage: unrank(('a','b','c'), 1)
        'b'
        sage: unrank(range(3,13,2), 1)
        5

    Enumerated sets::

        sage: unrank(GF(7), 2)
        2
        sage: unrank(IntegerModRing(29), 10)
        10

    An iterable::

        sage: unrank(NN,4)
        4

    An iterator::

        sage: unrank(('a{}'.format(i) for i in range(20)), 0)
        'a0'
        sage: unrank(('a{}'.format(i) for i in range(20)), 2)
        'a2'

    .. WARNING::

        When unranking an iterator, it returns the ``i``-th element
        beyond where it is currently at::

            sage: from sage.combinat.ranker import unrank
            sage: it = iter(range(20))
            sage: unrank(it, 2)
            2
            sage: unrank(it, 2)
            5

    TESTS::

        sage: from sage.combinat.ranker import unrank
        sage: unrank(list(range(3)), 10)
        Traceback (most recent call last):
        ...
        IndexError: list index out of range

        sage: unrank(('a{}'.format(i) for i in range(20)), 22)
        Traceback (most recent call last):
        ...
        IndexError: index out of range
    """
