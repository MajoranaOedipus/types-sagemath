from _typeshed import Incomplete
from collections.abc import Generator
from sage.misc.misc_c import prod as prod

def mrange_iter(iter_list, typ=...):
    """
    Return the multirange list derived from the given list of iterators.

    This is the list version of :func:`xmrange_iter`. Use :class:`xmrange_iter`
    for the iterator.

    More precisely, return the iterator over all objects of type ``typ`` of
    n-tuples of Python ints with entries between 0 and the integers in
    the sizes list. The iterator is empty if sizes is empty or contains
    any nonpositive integer.

    INPUT:

    - ``iter_list`` -- a finite iterable of finite iterables

    - ``typ`` -- (default: list) a type or class; more
      generally, something that can be called with a list as input

    OUTPUT: list

    EXAMPLES::

        sage: mrange_iter([range(3),[0,2]])
        [[0, 0], [0, 2], [1, 0], [1, 2], [2, 0], [2, 2]]
        sage: mrange_iter([['Monty','Flying'],['Python','Circus']], tuple)
        [('Monty', 'Python'), ('Monty', 'Circus'), ('Flying', 'Python'), ('Flying', 'Circus')]
        sage: mrange_iter([[2,3,5,7],[1,2]], sum)
        [3, 4, 4, 5, 6, 7, 8, 9]

    Examples that illustrate empty multi-ranges::

        sage: mrange_iter([range(5),range(3),range(0)])
        []
        sage: mrange_iter([range(5), range(3), range(-2)])
        []

    This example is not empty, and should not be. See :issue:`6561`.

    ::

        sage: mrange_iter([])
        [[]]

    AUTHORS:

    - Joel B. Mohler
    """

class xmrange_iter:
    """
    Return the multirange iterate derived from the given iterators and
    type.

    .. NOTE::

       This basically gives you the Cartesian product of sets.

    More precisely, return the iterator over all objects of type typ of
    n-tuples of Python ints with entries between 0 and the integers in
    the sizes list. The iterator is empty if sizes is empty or contains
    any nonpositive integer.

    Use :func:`mrange_iter` for the non-iterator form.

    INPUT:

    - ``iter_list`` -- list of objects usable as iterators (possibly
      lists)

    - ``typ`` -- (default: list) a type or class; more generally,
      something that can be called with a list as input

    OUTPUT: a generator

    EXAMPLES: We create multi-range iterators, print them and also
    iterate through a tuple version. ::

        sage: z = xmrange_iter([list(range(3)),list(range(2))], tuple);z
        xmrange_iter([[0, 1, 2], [0, 1]], <... 'tuple'>)
        sage: for a in z:
        ....:     print(a)
        (0, 0)
        (0, 1)
        (1, 0)
        (1, 1)
        (2, 0)
        (2, 1)

    We illustrate a few more iterations.

    ::

        sage: list(xmrange_iter([range(3),range(2)]))
        [[0, 0], [0, 1], [1, 0], [1, 1], [2, 0], [2, 1]]
        sage: list(xmrange_iter([range(3),range(2)], tuple))
        [(0, 0), (0, 1), (1, 0), (1, 1), (2, 0), (2, 1)]

    Here we compute the sum of each element of the multi-range
    iterator::

        sage: list(xmrange_iter([range(3),range(2)], sum))
        [0, 1, 1, 2, 2, 3]

    Next we compute the product::

        sage: list(xmrange_iter([range(3),range(2)], prod))
        [0, 0, 0, 1, 0, 2]

    Examples that illustrate empty multi-ranges.

    ::

        sage: list(xmrange_iter([range(5),range(3),range(-2)]))
        []
        sage: list(xmrange_iter([range(5),range(3),range(0)]))
        []

    This example is not empty, and should not be. See :issue:`6561`.

    ::

        sage: list(xmrange_iter([]))
        [[]]

    We use a multi-range iterator to iterate through the Cartesian
    product of sets.

    ::

        sage: X = ['red', 'apple', 389]
        sage: Y = ['orange', 'horse']
        sage: for i,j in xmrange_iter([X, Y], tuple):
        ....:     print((i, j))
        ('red', 'orange')
        ('red', 'horse')
        ('apple', 'orange')
        ('apple', 'horse')
        (389, 'orange')
        (389, 'horse')

    AUTHORS:

    - Joel B. Mohler
    """
    iter_list: Incomplete
    typ: Incomplete
    def __init__(self, iter_list, typ=...) -> None: ...
    def __iter__(self): ...
    def __len__(self) -> int:
        """
        Return the cardinality of this iterator as an int.

        This raises a :exc:`TypeError` if the cardinality does not fit
        into a Python int.

        EXAMPLES::

            sage: C = cartesian_product_iterator([range(3),range(4)])
            sage: len(C)
            12
            sage: len(cartesian_product_iterator([]))
            1
            sage: len(cartesian_product_iterator([ZZ,[]]))
            0
            sage: len(cartesian_product_iterator([ZZ,ZZ]))
            Traceback (most recent call last):
            ...
            TypeError: cardinality does not fit into a Python int
        """
    def cardinality(self):
        """
        Return the cardinality of this iterator.

        EXAMPLES::

            sage: C = cartesian_product_iterator([range(3),range(4)])
            sage: C.cardinality()
            12
            sage: C = cartesian_product_iterator([ZZ,QQ])
            sage: C.cardinality()
            +Infinity
            sage: C = cartesian_product_iterator([ZZ,[]])
            sage: C.cardinality()
            0
        """

def mrange(sizes, typ=...):
    """
    Return the multirange list with given sizes and type.

    This is the list version of :class:`xmrange`.
    Use :class:`xmrange` for the iterator.

    More precisely, return the iterator over all objects of type typ of
    n-tuples of Python ints with entries between 0 and the integers in
    the sizes list. The iterator is empty if sizes is empty or contains
    any nonpositive integer.

    INPUT:

    - ``sizes`` -- list of nonnegative integers

    - ``typ`` -- (default: list) a type or class; more
      generally, something that can be called with a list as input

    OUTPUT: list

    EXAMPLES::

        sage: mrange([3,2])
        [[0, 0], [0, 1], [1, 0], [1, 1], [2, 0], [2, 1]]
        sage: mrange([3,2], tuple)
        [(0, 0), (0, 1), (1, 0), (1, 1), (2, 0), (2, 1)]
        sage: mrange([3,2], sum)
        [0, 1, 1, 2, 2, 3]

    Examples that illustrate empty multi-ranges::

        sage: mrange([5,3,-2])
        []
        sage: mrange([5,3,0])
        []

    This example is not empty, and should not be. See :issue:`6561`.

    ::

        sage: mrange([])
        [[]]

    AUTHORS:

    - Jon Hanke

    - William Stein
    """

class xmrange:
    """
    Return the multirange iterate with given sizes and type.

    More precisely, return the iterator over all objects of type typ of
    n-tuples of Python ints with entries between 0 and the integers in
    the sizes list. The iterator is empty if sizes is empty or contains
    any nonpositive integer.

    Use mrange for the non-iterator form.

    INPUT:

    - ``sizes`` -- list of nonnegative integers

    - ``typ`` -- (default: list) a type or class; more
      generally, something that can be called with a list as input

    OUTPUT: a generator

    EXAMPLES: We create multi-range iterators, print them and also
    iterate through a tuple version.

    ::

        sage: z = xmrange([3,2]);z
        xmrange([3, 2])
        sage: z = xmrange([3,2], tuple);z
        xmrange([3, 2], <... 'tuple'>)
        sage: for a in z:
        ....:     print(a)
        (0, 0)
        (0, 1)
        (1, 0)
        (1, 1)
        (2, 0)
        (2, 1)

    We illustrate a few more iterations.

    ::

        sage: list(xmrange([3,2]))
        [[0, 0], [0, 1], [1, 0], [1, 1], [2, 0], [2, 1]]
        sage: list(xmrange([3,2], tuple))
        [(0, 0), (0, 1), (1, 0), (1, 1), (2, 0), (2, 1)]

    Here we compute the sum of each element of the multi-range
    iterator::

        sage: list(xmrange([3,2], sum))
        [0, 1, 1, 2, 2, 3]

    Next we compute the product::

        sage: list(xmrange([3,2], prod))
        [0, 0, 0, 1, 0, 2]

    Examples that illustrate empty multi-ranges.

    ::

        sage: list(xmrange([5,3,-2]))
        []
        sage: list(xmrange([5,3,0]))
        []

    This example is not empty, and should not be. See :issue:`6561`.

    ::

        sage: list(xmrange([]))
        [[]]

    We use a multi-range iterator to iterate through the Cartesian
    product of sets.

    ::

        sage: X = ['red', 'apple', 389]
        sage: Y = ['orange', 'horse']
        sage: for i,j in xmrange([len(X), len(Y)]):
        ....:     print((X[i], Y[j]))
        ('red', 'orange')
        ('red', 'horse')
        ('apple', 'orange')
        ('apple', 'horse')
        (389, 'orange')
        (389, 'horse')

    AUTHORS:

    - Jon Hanke

    - William Stein
    """
    sizes: Incomplete
    typ: Incomplete
    def __init__(self, sizes, typ=...) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self): ...

def cartesian_product_iterator(X):
    """
    Iterate over the Cartesian product.

    INPUT:

    - ``X`` -- list or tuple of lists

    OUTPUT: iterator over the Cartesian product of the elements of X

    EXAMPLES::

        sage: list(cartesian_product_iterator([[1,2], ['a','b']]))
        [(1, 'a'), (1, 'b'), (2, 'a'), (2, 'b')]
        sage: list(cartesian_product_iterator([]))
        [()]

    TESTS:

    Check that :issue:`28521` is fixed::

        sage: list(cartesian_product_iterator([[], [1]]))
        []
        sage: list(cartesian_product_iterator([[1], []]))
        []
        sage: list(cartesian_product_iterator([[1], [], [2]]))
        []
    """
def cantor_product(*args, **kwds) -> Generator[Incomplete]:
    """
    Return an iterator over the product of the inputs along the diagonals a la
    :wikipedia:`Cantor pairing <Pairing_function#Cantor_pairing_function>`.

    INPUT:

    - a certain number of iterables

    - ``repeat`` -- an optional integer. If it is provided, the input is
      repeated ``repeat`` times

    Other keyword arguments are passed to
    :class:`sage.combinat.integer_lists.invlex.IntegerListsLex`.

    EXAMPLES::

        sage: from sage.misc.mrange import cantor_product
        sage: list(cantor_product([0, 1], repeat=3))
        [(0, 0, 0),
         (1, 0, 0),
         (0, 1, 0),
         (0, 0, 1),
         (1, 1, 0),
         (1, 0, 1),
         (0, 1, 1),
         (1, 1, 1)]
        sage: list(cantor_product([0, 1], [0, 1, 2, 3]))
        [(0, 0), (1, 0), (0, 1), (1, 1), (0, 2), (1, 2), (0, 3), (1, 3)]

    Infinite iterators are valid input as well::

       sage: from itertools import islice
       sage: list(islice(cantor_product(ZZ, QQ), 14r))
        [(0, 0),
         (1, 0),
         (0, 1),
         (-1, 0),
         (1, 1),
         (0, -1),
         (2, 0),
         (-1, 1),
         (1, -1),
         (0, 1/2),
         (-2, 0),
         (2, 1),
         (-1, -1),
         (1, 1/2)]

    TESTS::

        sage: C = cantor_product([0, 1], [0, 1, 2, 3], [0, 1, 2])
        sage: sum(1 for _ in C) == 2*4*3
        True

        sage: from itertools import count
        sage: list(cantor_product([], count()))
        []
        sage: list(cantor_product(count(), [], count()))
        []

        sage: list(cantor_product(count(), repeat=0))
        [()]

        sage: next(cantor_product(count(), repeat=-1))
        Traceback (most recent call last):
        ...
        ValueError: repeat argument cannot be negative
        sage: next(cantor_product(count(), toto='hey'))
        Traceback (most recent call last):
        ...
        TypeError: ...__init__() got an unexpected keyword argument 'toto'

    ::

        sage: list(cantor_product(srange(5), repeat=2, min_slope=1))
        [(0, 1), (0, 2), (1, 2), (0, 3), (1, 3),
         (0, 4), (2, 3), (1, 4), (2, 4), (3, 4)]

    Check that :issue:`24897` is fixed::

        sage: from sage.misc.mrange import cantor_product
        sage: list(cantor_product([1]))
        [(1,)]
        sage: list(cantor_product([1], repeat=2))
        [(1, 1)]
        sage: list(cantor_product([1], [1,2]))
        [(1, 1), (1, 2)]
        sage: list(cantor_product([1,2], [1]))
        [(1, 1), (2, 1)]
    """
