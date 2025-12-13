import _cython_3_2_1
from typing import Any, ClassVar

__pyx_capi__: dict
balanced_sum: _cython_3_2_1.cython_function_or_method
cyflush: _cython_3_2_1.cython_function_or_method
iterator_prod: _cython_3_2_1.cython_function_or_method
normalize_index: _cython_3_2_1.cython_function_or_method

def prod(x, z=None, recursion_cutoff=5):
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
- Robert Bradshaw (2008-03-26): Balanced product tree for generators and iterators"""

mul = prod
running_total: _cython_3_2_1.cython_function_or_method

class NonAssociative:
    """File: /build/sagemath/src/sage/src/sage/misc/misc_c.pyx (starting at line 265)

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
    def __init__(self, left, right=...) -> Any:
        """NonAssociative.__init__(self, left, right=None)

        File: /build/sagemath/src/sage/src/sage/misc/misc_c.pyx (starting at line 284)

        EXAMPLES::

            sage: from sage.misc.misc_c import NonAssociative
            sage: NonAssociative('a')
            a
            sage: NonAssociative('a','b')
            (a*b)"""
    def __mul__(self, other) -> Any:
        """NonAssociative.__mul__(self, other)

        File: /build/sagemath/src/sage/src/sage/misc/misc_c.pyx (starting at line 312)

        EXAMPLES::

            sage: from sage.misc.misc_c import NonAssociative
            sage: a, b, c = [NonAssociative(label) for label in 'abc']
            sage: (a*b)*c
            ((a*b)*c)
            sage: a*(b*c)
            (a*(b*c))"""

class sized_iter:
    """sized_iter(iterable, length=None)

    File: /build/sagemath/src/sage/src/sage/misc/misc_c.pyx (starting at line 627)

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
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, iterable, length=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/misc/misc_c.pyx (starting at line 687)"""
    def __iter__(self) -> Any:
        """sized_iter.__iter__(self)

        File: /build/sagemath/src/sage/src/sage/misc/misc_c.pyx (starting at line 696)"""
    def __len__(self) -> Any:
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
    def __next__(self) -> Any:
        """sized_iter.__next__(self)

        File: /build/sagemath/src/sage/src/sage/misc/misc_c.pyx (starting at line 730)"""
