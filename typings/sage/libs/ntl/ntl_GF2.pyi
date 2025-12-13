import _cython_3_2_1
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from typing import Any

unpickle_class_args: _cython_3_2_1.cython_function_or_method
unpickle_class_value: _cython_3_2_1.cython_function_or_method

class ntl_GF2:
    """ntl_GF2(v=None)

    File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_GF2.pyx (starting at line 35)

    The \\class{GF2} represents the field GF(2). Computationally
    speaking, it is not a particularly useful class.  Its main use is
    to make the interfaces to the various finite field classes as
    uniform as possible."""
    def __init__(self, v=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_GF2.pyx (starting at line 42)

                Initialize a NTL bit.

                EXAMPLES::

                    sage: ntl.GF2(1)
                    1
                    sage: ntl.GF2(int(2))
                    0
                    sage: ntl.GF2('1')
                    1
        """
    def __add__(self, other) -> Any:
        """ntl_GF2.__add__(self, other)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_GF2.pyx (starting at line 185)

        EXAMPLES::

            sage: o = ntl.GF2(1)
            sage: z = ntl.GF2(0)
            sage: o+o
            0
            sage: o+z
            1
            sage: z+o
            1
            sage: z+z
            0"""
    def __eq__(self, other: object) -> bool:
        """Return self==value."""
    def __ge__(self, other: object) -> bool:
        """Return self>=value."""
    def __gt__(self, other: object) -> bool:
        """Return self>value."""
    def __int__(self) -> Any:
        """ntl_GF2.__int__(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_GF2.pyx (starting at line 238)

        Return ``self`` as an int.

        EXAMPLES::

            sage: o = ntl.GF2(1)
            sage: z = ntl.GF2(0)
            sage: int(z)
            0
            sage: int(o)
            1"""
    def __le__(self, other: object) -> bool:
        """Return self<=value."""
    def __lt__(self, other: object) -> bool:
        """Return self<value."""
    def __mul__(self, other) -> Any:
        """ntl_GF2.__mul__(self, other)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_GF2.pyx (starting at line 115)

        EXAMPLES::

            sage: o = ntl.GF2(1)
            sage: z = ntl.GF2(0)
            sage: o*o
            1
            sage: o*z
            0
            sage: z*o
            0
            sage: z*z
            0"""
    def __ne__(self, other: object) -> bool:
        """Return self!=value."""
    def __neg__(self) -> Any:
        """ntl_GF2.__neg__(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_GF2.pyx (starting at line 208)

        EXAMPLES::

            sage: o = ntl.GF2(1)
            sage: z = ntl.GF2(0)
            sage: -z
            0
            sage: -o
            1"""
    def __pow__(self, ntl_GF2self, longe, ignored) -> Any:
        """ntl_GF2.__pow__(ntl_GF2 self, long e, ignored)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_GF2.pyx (starting at line 223)

        EXAMPLES::

            sage: o = ntl.GF2(1)
            sage: z = ntl.GF2(0)
            sage: z^2
            0
            sage: o^2
            1"""
    def __radd__(self, other):
        """Return value+self."""
    def __reduce__(self) -> Any:
        """ntl_GF2.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_GF2.pyx (starting at line 73)

        Serialize ``self``.

        EXAMPLES::

            sage: a = ntl.GF2(1)
            sage: loads(dumps(a))
            1"""
    def __rmul__(self, other):
        """Return value*self."""
    def __rpow__(self, other):
        """Return pow(value, self, mod)."""
    def __rsub__(self, other):
        """Return value-self."""
    def __rtruediv__(self, other):
        """Return value/self."""
    def __sub__(self, other) -> Any:
        """ntl_GF2.__sub__(self, other)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_GF2.pyx (starting at line 162)

        EXAMPLES::

            sage: o = ntl.GF2(1)
            sage: z = ntl.GF2(0)
            sage: o-o
            0
            sage: o-z
            1
            sage: z-o
            1
            sage: z-z
            0"""
    def __truediv__(self, other) -> Any:
        """ntl_GF2.__truediv__(self, other)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_GF2.pyx (starting at line 138)

        EXAMPLES::

            sage: o = ntl.GF2(1)
            sage: z = ntl.GF2(0)
            sage: o/o
            1
            sage: o/z
            Traceback (most recent call last):
            ...
            ZeroDivisionError"""
