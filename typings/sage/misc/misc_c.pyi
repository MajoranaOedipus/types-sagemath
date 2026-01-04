"""
Miscellaneous functions (Cython)

This file contains support for products, running totals, balanced
sums, and also a function to flush output from external library calls.

AUTHORS:

- William Stein (2005)
- Joel B. Mohler (2007-10-03): Reimplemented in Cython and optimized
- Robert Bradshaw (2007-10-26): Balanced product tree, other optimizations, (lazy) generator support
- Robert Bradshaw (2008-03-26): Balanced product tree for generators and iterators
- Stefan van Zwam (2013-06-06): Added bitset tests, some docstring cleanup
"""

from typing import Literal, overload, Self, SupportsIndex
from collections.abc import Iterable
from typings_sagemath import (
    Addable,
    AddableWith,
    AddableWithExt,
    Multiplicable,
    MultiplicableWith,
    MultiplicableWithExt,
)

# cannot be accurately expressed, I specialise some useful cases

@overload
def running_total[A: Addable](L: Iterable[A], start: A | None = None) -> list[A]: ...
@overload
def running_total[A](L: Iterable[A], start: AddableWith[A]) -> list[AddableWith[A]]: ...
@overload
def running_total[A, S](
    L: Iterable[A], start: AddableWithExt[A, S]
) -> list[AddableWithExt[A, S] | S]:
    """
    Return a list where the `i`-th entry is the sum of all entries up to (and
    including) `i`.

    INPUT:

    - ``L`` -- the list
    - ``start`` -- (optional) a default start value

    EXAMPLES::

        sage: running_total(range(5))
        [0, 1, 3, 6, 10]
        sage: running_total("abcdef")
        ['a', 'ab', 'abc', 'abcd', 'abcde', 'abcdef']
        sage: running_total("abcdef", start="%")
        ['%a', '%ab', '%abc', '%abcd', '%abcde', '%abcdef']
        sage: running_total([1..10], start=100)
        [101, 103, 106, 110, 115, 121, 128, 136, 145, 155]
        sage: running_total([])
        []
    """
    ...

@overload
def prod[M: Multiplicable](
    x: Iterable[M], z: M | None = None, recursion_cutoff: int = 5
) -> M: ...
@overload
def prod[M](
    x: Iterable[M], z: MultiplicableWith[M], recursion_cutoff: int = 5
) -> MultiplicableWith[M]: ...
@overload
def prod[M, P](
    x: Iterable[M], z: MultiplicableWithExt[M, P], recursion_cutoff: int = 5
) -> MultiplicableWithExt[M, P] | P:
    """prod(x, z=None, Py_ssize_t recursion_cutoff=5)

    File: /build/sagemath/src/sage/src/sage/misc/misc_c.pyx (starting at line 72)

    Return the product of the elements in the list x.

    If optional argument z is not given, start the product with the first
    element of the list, otherwise use z.  The empty product is the int 1 if z
    is not specified, and is z if given.

    This assumes that your multiplication is associative; we do not promise
    which end of the list we start at.

    .. SEEALSO::

        For the symbolic product function, see :func:`sage.calculus.calculus.symbolic_product`.

    EXAMPLES::

        sage: prod([1,2,34])
        68
        sage: prod([2,3], 5)
        30
        sage: prod((1,2,3), 5)
        30
        sage: F = factor(-2006); F
        -1 * 2 * 17 * 59
        sage: prod(F)
        -2006

    AUTHORS:

    - Joel B. Mohler (2007-10-03): Reimplemented in Cython and optimized
    - Robert Bradshaw (2007-10-26): Balanced product tree, other optimizations, (lazy) generator support
    - Robert Bradshaw (2008-03-26): Balanced product tree for generators and iterators
    """

@overload
def iterator_prod[M: Multiplicable](
    L: Iterable[M], z: M | None = None, multiply: Literal[True] = True
) -> M: ...
@overload
def iterator_prod[M](
    L: Iterable[M], z: MultiplicableWith[M], multiply: Literal[True] = True
): ...
@overload
def iterator_prod[M, P](
    L: Iterable[M], z: MultiplicableWithExt[M, P], multiply: Literal[True] = True
) -> MultiplicableWithExt[M, P] | P: ...
@overload
def iterator_prod[A: Addable](
    L: Iterable[A], z: A | None = None, multiply: Literal[False] = False
) -> A: ...
@overload
def iterator_prod[A](
    L: Iterable[A], z: AddableWith[A], multiply: Literal[False]
) -> AddableWith[A]: ...
@overload
def iterator_prod[A, S](
    L: Iterable[A], z: AddableWithExt[A, S], multiply: Literal[False]
) -> AddableWithExt[A, S] | S:
    """
    Attempt to do a balanced product of an arbitrary and unknown length
    sequence (such as a generator). Intermediate multiplications are always
    done with subproducts of the same size (measured by the number of original
    factors) up until the iterator terminates. This is optimal when and only
    when there are exactly a power of two number of terms.

    A StopIteration is raised if the iterator is empty and z is not given.

    EXAMPLES::

        sage: from sage.misc.misc_c import iterator_prod
        sage: iterator_prod(1..5)
        120
        sage: iterator_prod([], z='anything')
        'anything'

        sage: from sage.misc.misc_c import NonAssociative
        sage: L = [NonAssociative(label) for label in 'abcdef']
        sage: iterator_prod(L)
        (((a*b)*(c*d))*(e*f))

    When ``multiply=False``, the items are added up instead (however this
    interface should not be used directly, use :func:`balanced_sum` instead)::

        sage: iterator_prod((1..5), multiply=False)
        15
    """

class NonAssociative[L, R]:
    """
    This class is to test the balance nature of prod.

    EXAMPLES::

        sage: from sage.misc.misc_c import NonAssociative
        sage: L = [NonAssociative(label) for label in 'abcdef']
        sage: prod(L)
        (((a*b)*c)*((d*e)*f))
        sage: L = [NonAssociative(label) for label in range(20)]
        sage: prod(L, recursion_cutoff=5)
        ((((((0*1)*2)*3)*4)*((((5*6)*7)*8)*9))*(((((10*11)*12)*13)*14)*((((15*16)*17)*18)*19)))
        sage: prod(L, recursion_cutoff=1)
        (((((0*1)*2)*(3*4))*(((5*6)*7)*(8*9)))*((((10*11)*12)*(13*14))*(((15*16)*17)*(18*19))))
        sage: L = [NonAssociative(label) for label in range(14)]
        sage: prod(L, recursion_cutoff=1)
        ((((0*1)*(2*3))*((4*5)*6))*(((7*8)*(9*10))*((11*12)*13)))
    """

    left: L
    right: R
    def __init__(self, left: L, right: R = None):
        """
        EXAMPLES::

            sage: from sage.misc.misc_c import NonAssociative
            sage: NonAssociative('a')
            a
            sage: NonAssociative('a','b')
            (a*b)"""

    def __mul__[R_](self, other: R_) -> NonAssociative[Self, R_]:
        """
        EXAMPLES::

            sage: from sage.misc.misc_c import NonAssociative
            sage: a, b, c = [NonAssociative(label) for label in 'abc']
            sage: (a*b)*c
            ((a*b)*c)
            sage: a*(b*c)
            (a*(b*c))"""

@overload
def balanced_sum[A: Addable](
    x: Iterable[A], z: A | None = None, recursion_cutoff: int = 5
) -> A: ...
@overload
def balanced_sum[A](
    x: Iterable[A], z: AddableWith[A], recursion_cutoff: int = 5
) -> AddableWith[A]: ...
@overload
def balanced_sum[A, S](
    x: Iterable[A], z: AddableWithExt[A, S], recursion_cutoff: int = 5
) -> AddableWithExt[A, S] | S:
    """
    Return the sum of the elements in the list x.  If optional
    argument z is not given, start the sum with the first element of
    the list, otherwise use z.  The empty product is the int 0 if z is
    not specified, and is z if given.  The sum is computed
    recursively, where the sum is split up if the list is greater than
    recursion_cutoff.  recursion_cutoff must be at least 3.

    This assumes that your addition is associative; we do not promise
    which end of the list we start at.

    EXAMPLES::

        sage: balanced_sum([1,2,34])
        37
        sage: balanced_sum([2,3], 5)
        10
        sage: balanced_sum((1,2,3), 5)
        11

    Order should be preserved::

        sage: balanced_sum([[i] for i in range(10)], [], recursion_cutoff=3)
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    We make copies when appropriate so that we do not accidentally
    modify the arguments::

        sage: list(range(10^5))==balanced_sum([[i] for i in range(10^5)], [])
        True
        sage: list(range(10^5))==balanced_sum([[i] for i in range(10^5)], [])
        True

    TESTS::

        sage: balanced_sum((1..3)) # nonempty, z=None
        6
        sage: balanced_sum((1..-1)) # empty, z=None
        0
        sage: balanced_sum((1..3), 5) # nonempty, z is not None
        11
        sage: balanced_sum((1..-1), 5) # empty, z is not None
        5
        sage: balanced_sum([1])
        1

    AUTHORS:

    - Joel B. Mohler (2007-10-03): Reimplemented in Cython and optimized
    - Robert Bradshaw (2007-10-26): Balanced product tree, other optimizations, (lazy) generator support
    """

def normalize_index(
    key: (
        SupportsIndex
        | slice
        | tuple[SupportsIndex | slice, ...]
        | list[SupportsIndex | slice]
        | range
    ),
    size: int,
) -> list[int]:
    """
    Normalize an index key and return a valid index or list of indices
    within the range(0, size).

    INPUT:

    - ``key`` -- the index key, which can be either an integer, a tuple/list of
      integers, or a slice
    - ``size`` -- the size of the collection

    OUTPUT:

    A tuple (SINGLE, VALUE), where SINGLE is True (i.e., 1) if VALUE
    is an integer and False (i.e., 0) if VALUE is a list.

    EXAMPLES::

        sage: from sage.misc.misc_c import normalize_index
        sage: normalize_index(-6,5)
        Traceback (most recent call last):
        ...
        IndexError: index out of range
        sage: normalize_index(-5,5)
        [0]
        sage: normalize_index(-4,5)
        [1]
        sage: normalize_index(-3,5)
        [2]
        sage: normalize_index(-2,5)
        [3]
        sage: normalize_index(-1,5)
        [4]
        sage: normalize_index(0,5)
        [0]
        sage: normalize_index(1,5)
        [1]
        sage: normalize_index(2,5)
        [2]
        sage: normalize_index(3,5)
        [3]
        sage: normalize_index(4,5)
        [4]
        sage: normalize_index(5,5)
        Traceback (most recent call last):
        ...
        IndexError: index out of range
        sage: normalize_index(6,5)
        Traceback (most recent call last):
        ...
        IndexError: index out of range
        sage: normalize_index((4,-6),5)
        Traceback (most recent call last):
        ...
        IndexError: index out of range
        sage: normalize_index((-2,3),5)
        [3, 3]
        sage: normalize_index((5,0),5)
        Traceback (most recent call last):
        ...
        IndexError: index out of range
        sage: normalize_index((-5,2),5)
        [0, 2]
        sage: normalize_index((0,-2),5)
        [0, 3]
        sage: normalize_index((2,-3),5)
        [2, 2]
        sage: normalize_index((3,3),5)
        [3, 3]
        sage: normalize_index((-2,-5),5)
        [3, 0]
        sage: normalize_index((-2,-4),5)
        [3, 1]
        sage: normalize_index([-2,-1,3],5)
        [3, 4, 3]
        sage: normalize_index([4,2,1],5)
        [4, 2, 1]
        sage: normalize_index([-2,-3,-4],5)
        [3, 2, 1]
        sage: normalize_index([3,-2,-3],5)
        [3, 3, 2]
        sage: normalize_index([-5,2,-3],5)
        [0, 2, 2]
        sage: normalize_index([4,4,-5],5)
        [4, 4, 0]
        sage: s=slice(None,None,None); normalize_index(s,5)==list(range(5))[s]
        True
        sage: s=slice(None,None,-2); normalize_index(s,5)==list(range(5))[s]
        True
        sage: s=slice(None,None,4); normalize_index(s,5)==list(range(5))[s]
        True
        sage: s=slice(None,-2,None); normalize_index(s,5)==list(range(5))[s]
        True
        sage: s=slice(None,-2,-2); normalize_index(s,5)==list(range(5))[s]
        True
        sage: s=slice(None,-2,4); normalize_index(s,5)==list(range(5))[s]
        True
        sage: s=slice(None,4,None); normalize_index(s,5)==list(range(5))[s]
        True
        sage: s=slice(None,4,-2); normalize_index(s,5)==list(range(5))[s]
        True
        sage: s=slice(None,4,4); normalize_index(s,5)==list(range(5))[s]
        True
        sage: s=slice(-2,None,None); normalize_index(s,5)==list(range(5))[s]
        True
        sage: s=slice(-2,None,-2); normalize_index(s,5)==list(range(5))[s]
        True
        sage: s=slice(-2,None,4); normalize_index(s,5)==list(range(5))[s]
        True
        sage: s=slice(-2,-2,None); normalize_index(s,5)==list(range(5))[s]
        True
        sage: s=slice(-2,-2,-2); normalize_index(s,5)==list(range(5))[s]
        True
        sage: s=slice(-2,-2,4); normalize_index(s,5)==list(range(5))[s]
        True
        sage: s=slice(-2,4,None); normalize_index(s,5)==list(range(5))[s]
        True
        sage: s=slice(-2,4,-2); normalize_index(s,5)==list(range(5))[s]
        True
        sage: s=slice(-2,4,4); normalize_index(s,5)==list(range(5))[s]
        True
        sage: s=slice(4,None,None); normalize_index(s,5)==list(range(5))[s]
        True
        sage: s=slice(4,None,-2); normalize_index(s,5)==list(range(5))[s]
        True
        sage: s=slice(4,None,4); normalize_index(s,5)==list(range(5))[s]
        True
        sage: s=slice(4,-2,None); normalize_index(s,5)==list(range(5))[s]
        True
        sage: s=slice(4,-2,-2); normalize_index(s,5)==list(range(5))[s]
        True
        sage: s=slice(4,-2,4); normalize_index(s,5)==list(range(5))[s]
        True
        sage: s=slice(4,4,None); normalize_index(s,5)==list(range(5))[s]
        True
        sage: s=slice(4,4,-2); normalize_index(s,5)==list(range(5))[s]
        True
        sage: s=slice(4,4,4); normalize_index(s,5)==list(range(5))[s]
        True
    """

class sized_iter[T]:
    """
    Wrapper for an iterator to verify that it has a specified length.

    INPUT:

    - ``iterable`` -- object to be iterated over

    - ``length`` -- (optional) the required length; if this is not
      given, then ``len(iterable)`` will be used

    If the iterable does not have the given length, a :exc:`ValueError` is
    raised during iteration.

    EXAMPLES::

        sage: from sage.misc.misc_c import sized_iter
        sage: list(sized_iter(range(4)))
        [0, 1, 2, 3]
        sage: list(sized_iter(range(4), 4))
        [0, 1, 2, 3]
        sage: list(sized_iter(range(5), 4))
        Traceback (most recent call last):
        ...
        ValueError: sequence too long (expected length 4, got more)
        sage: list(sized_iter(range(3), 4))
        Traceback (most recent call last):
        ...
        ValueError: sequence too short (expected length 4, got 3)

    If the iterable is too long, we get the error on the last entry::

        sage: it = sized_iter(range(5), 2)
        sage: next(it)
        0
        sage: next(it)
        Traceback (most recent call last):
        ...
        ValueError: sequence too long (expected length 2, got more)

    When the expected length is zero, the iterator is checked on
    construction::

        sage: list(sized_iter([], 0))
        []
        sage: sized_iter([1], 0)
        Traceback (most recent call last):
        ...
        ValueError: sequence too long (expected length 0, got more)

    If no ``length`` is given, the iterable must implement ``__len__``::

        sage: sized_iter(x for x in range(4))
        Traceback (most recent call last):
        ...
        TypeError: object of type 'generator' has no len()"""

    def __init__(self, iterable: Iterable[T], length: int | None = None): ...
    def __iter__(self) -> Self: ...
    def __len__(self) -> int:
        """sized_iter.__len__(self)

        File: /build/sagemath/src/sage/src/sage/misc/misc_c.pyx (starting at line 699)

        Number of entries remaining, assuming that the expected length
        is the actual length.

        EXAMPLES::

            sage: from sage.misc.misc_c import sized_iter
            sage: it = sized_iter(range(4), 4)
            sage: len(it)
            4
            sage: next(it)
            0
            sage: len(it)
            3"""

    def __next__(self) -> T:
        """sized_iter.__next__(self)

        File: /build/sagemath/src/sage/src/sage/misc/misc_c.pyx (starting at line 730)
        """

def cyflush() -> None:
    """
    Flush any output left over from external library calls.

    Starting with Python 3, some output from external libraries (like
    FLINT) is not flushed, and so if a doctest produces such output,
    the output may not appear until a later doctest. See
    :issue:`28649`.

    Use this function after a doctest which produces potentially
    unflushed output to force it to be flushed.

    EXAMPLES::

        sage: R.<t> = QQ[]
        sage: t^(sys.maxsize//2)                                                        # needs sage.libs.flint
        Traceback (most recent call last):
        ...
        RuntimeError: FLINT exception
        sage: from sage.misc.misc_c import cyflush
        sage: cyflush()
        ...
    """
