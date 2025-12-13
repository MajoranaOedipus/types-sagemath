import sage.structure.sage_object
from sage.structure.richcmp import revop as revop, rich_to_bool as rich_to_bool, rich_to_bool_sgn as rich_to_bool_sgn, richcmp as richcmp, richcmp_not_equal as richcmp_not_equal
from typing import Any

class ConstantFunction(sage.structure.sage_object.SageObject):
    """ConstantFunction(value)

    File: /build/sagemath/src/sage/src/sage/misc/constant_function.pyx (starting at line 20)

    A class for function objects implementing constant functions.

    EXAMPLES::

        sage: f = ConstantFunction(3)
        sage: f
        The constant function (...) -> 3
        sage: f()
        3
        sage: f(5)
        3

    Such a function could be implemented as a lambda expression, but
    this is not (currently) picklable::

        sage: g = lambda x: 3
        sage: g == loads(dumps(g))
        Traceback (most recent call last):
        ...
        PicklingError: Can't pickle ...: attribute lookup ... failed
        sage: f == loads(dumps(f))
        True

    Also, in the long run, the information that this function is
    constant could be used by some algorithms.

    .. TODO::

        - Should constant functions have unique representation?
        - Should the number of arguments be specified in the input?
        - Should this go into ``sage.categories.maps``?
          Then what should be the parent (e.g. for ``lambda x: True``)?

    TESTS:

    These tests do fail if we try to use ``UniqueRepresentation``::

        sage: f = ConstantFunction(True)
        sage: g = ConstantFunction(1)
        sage: f(), g()
        (True, 1)

    That's because ``1`` and ``True`` cannot be distinguished as keys
    in a dictionary (argl!)::

        sage: { 1: 'a', True: 'b' }
        {1: 'b'}"""
    def __init__(self, value) -> Any:
        """File: /build/sagemath/src/sage/src/sage/misc/constant_function.pyx (starting at line 72)

                EXAMPLES::

                    sage: ConstantFunction(1)()
                    1
        """
    def __call__(self, *args) -> Any:
        """ConstantFunction.__call__(self, *args)

        File: /build/sagemath/src/sage/src/sage/misc/constant_function.pyx (starting at line 99)

        EXAMPLES::

            sage: ConstantFunction(1)()
            1
            sage: ConstantFunction(1)(5,3)
            1
            sage: ConstantFunction(True)()
            True"""
    def __eq__(self, other: object) -> bool:
        """Return self==value."""
    def __ge__(self, other: object) -> bool:
        """Return self>=value."""
    def __gt__(self, other: object) -> bool:
        """Return self>value."""
    def __le__(self, other: object) -> bool:
        """Return self<=value."""
    def __lt__(self, other: object) -> bool:
        """Return self<value."""
    def __ne__(self, other: object) -> bool:
        """Return self!=value."""
    def __reduce__(self) -> Any:
        """ConstantFunction.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/misc/constant_function.pyx (starting at line 81)

        TESTS::

            sage: loads(dumps(ConstantFunction(5))) == ConstantFunction(5) # indirect doctest
            True"""
