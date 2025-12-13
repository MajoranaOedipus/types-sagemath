import _cython_3_2_1
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from typing import Any, ClassVar, overload

ntl_setSeed: _cython_3_2_1.cython_function_or_method
randomBits: _cython_3_2_1.cython_function_or_method
randomBnd: _cython_3_2_1.cython_function_or_method
unpickle_class_args: _cython_3_2_1.cython_function_or_method
unpickle_class_value: _cython_3_2_1.cython_function_or_method

class ntl_ZZ:
    """ntl_ZZ(v=None)

    File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ.pyx (starting at line 48)

    The \\class{ZZ} class is used to represent signed, arbitrary length integers.

    Routines are provided for all of the basic arithmetic operations, as
    well as for some more advanced operations such as primality testing.
    Space is automatically managed by the constructors and destructors.

    This module also provides routines for generating small primes, and
    fast routines for performing modular arithmetic on single-precision
    numbers."""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, v=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ.pyx (starting at line 61)

                Initialize and NTL integer.

                EXAMPLES::

                    sage: ntl.ZZ(12r)
                    12
                    sage: ntl.ZZ(Integer(95413094))
                    95413094
                    sage: ntl.ZZ('-1')
                    -1
                    sage: ntl.ZZ('1L')
                    1
                    sage: ntl.ZZ('-1r')
                    -1

                TESTS::

                    sage: ntl.ZZ(int(2**40))
                    1099511627776

                AUTHOR: Joel B. Mohler (2007-06-14)
        """
    @overload
    def get_as_int_doctest(self) -> Any:
        """ntl_ZZ.get_as_int_doctest(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ.pyx (starting at line 284)

        This method exists solely for automated testing of get_as_int().

        EXAMPLES::

            sage: x = ntl.ZZ(42)
            sage: i = x.get_as_int_doctest()
            sage: i
             42
            sage: type(i)
             <... 'int'>"""
    @overload
    def get_as_int_doctest(self) -> Any:
        """ntl_ZZ.get_as_int_doctest(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ.pyx (starting at line 284)

        This method exists solely for automated testing of get_as_int().

        EXAMPLES::

            sage: x = ntl.ZZ(42)
            sage: i = x.get_as_int_doctest()
            sage: i
             42
            sage: type(i)
             <... 'int'>"""
    def set_from_int_doctest(self, value) -> Any:
        """ntl_ZZ.set_from_int_doctest(self, value)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ.pyx (starting at line 342)

        This method exists solely for automated testing of set_from_int().

        EXAMPLES::

            sage: x = ntl.ZZ()
            sage: x.set_from_int_doctest(42)
            sage: x
             42"""
    def set_from_sage_int(self, Integervalue) -> Any:
        """ntl_ZZ.set_from_sage_int(self, Integer value)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ.pyx (starting at line 323)

        Set the value from a sage int.

        EXAMPLES::

            sage: n=ntl.ZZ(2983)
            sage: n
            2983
            sage: n.set_from_sage_int(1234)
            sage: n
            1234

        AUTHOR: Joel B. Mohler"""
    @overload
    def val_unit(self, ntl_ZZprime) -> Any:
        """ntl_ZZ.val_unit(self, ntl_ZZ prime)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ.pyx (starting at line 384)

        Uses code in ``ntlwrap_impl.h`` to compute `p`-adic valuation and
        unit of ``self``.

        EXAMPLES::

            sage: a = ntl.ZZ(5^7*3^4)
            sage: p = ntl.ZZ(-5)
            sage: a.val_unit(p)
            (7, -81)
            sage: a.val_unit(ntl.ZZ(-3))
            (4, 78125)
            sage: a.val_unit(ntl.ZZ(2))
            (0, 6328125)"""
    @overload
    def val_unit(self, p) -> Any:
        """ntl_ZZ.val_unit(self, ntl_ZZ prime)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ.pyx (starting at line 384)

        Uses code in ``ntlwrap_impl.h`` to compute `p`-adic valuation and
        unit of ``self``.

        EXAMPLES::

            sage: a = ntl.ZZ(5^7*3^4)
            sage: p = ntl.ZZ(-5)
            sage: a.val_unit(p)
            (7, -81)
            sage: a.val_unit(ntl.ZZ(-3))
            (4, 78125)
            sage: a.val_unit(ntl.ZZ(2))
            (0, 6328125)"""
    @overload
    def valuation(self, ntl_ZZprime) -> Any:
        """ntl_ZZ.valuation(self, ntl_ZZ prime)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ.pyx (starting at line 355)

        Uses code in ``ntlwrap_impl.h`` to compute the number of times
        prime divides ``self``.

        EXAMPLES::

            sage: a = ntl.ZZ(5^7*3^4)
            sage: p = ntl.ZZ(5)
            sage: a.valuation(p)
            7
            sage: a.valuation(-p)
            7
            sage: b = ntl.ZZ(0)
            sage: b.valuation(p)
            +Infinity"""
    @overload
    def valuation(self, p) -> Any:
        """ntl_ZZ.valuation(self, ntl_ZZ prime)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ.pyx (starting at line 355)

        Uses code in ``ntlwrap_impl.h`` to compute the number of times
        prime divides ``self``.

        EXAMPLES::

            sage: a = ntl.ZZ(5^7*3^4)
            sage: p = ntl.ZZ(5)
            sage: a.valuation(p)
            7
            sage: a.valuation(-p)
            7
            sage: b = ntl.ZZ(0)
            sage: b.valuation(p)
            +Infinity"""
    @overload
    def valuation(self, p) -> Any:
        """ntl_ZZ.valuation(self, ntl_ZZ prime)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ.pyx (starting at line 355)

        Uses code in ``ntlwrap_impl.h`` to compute the number of times
        prime divides ``self``.

        EXAMPLES::

            sage: a = ntl.ZZ(5^7*3^4)
            sage: p = ntl.ZZ(5)
            sage: a.valuation(p)
            7
            sage: a.valuation(-p)
            7
            sage: b = ntl.ZZ(0)
            sage: b.valuation(p)
            +Infinity"""
    def __add__(self, other) -> Any:
        """ntl_ZZ.__add__(self, other)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ.pyx (starting at line 209)

        EXAMPLES::

            sage: n=ntl.ZZ(2983)+ntl.ZZ(2)
            sage: n
            2985
            sage: ntl.ZZ(23)+2
            25"""
    def __eq__(self, other: object) -> bool:
        """Return self==value."""
    def __ge__(self, other: object) -> bool:
        """Return self>=value."""
    def __gt__(self, other: object) -> bool:
        """Return self>value."""
    def __hash__(self) -> Any:
        """ntl_ZZ.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ.pyx (starting at line 163)

        Return the hash of this integer.

        Agrees with the hash of the corresponding sage integer."""
    @overload
    def __int__(self) -> Any:
        """ntl_ZZ.__int__(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ.pyx (starting at line 254)

        Return ``self`` as an int.

        EXAMPLES::

            sage: ntl.ZZ(22).__int__()
            22
            sage: type(ntl.ZZ(22).__int__())
            <... 'int'>

            sage: ntl.ZZ(10^30).__int__()
            1000000000000000000000000000000
            sage: type(ntl.ZZ(10^30).__int__())
            <class 'int'>"""
    @overload
    def __int__(self) -> Any:
        """ntl_ZZ.__int__(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ.pyx (starting at line 254)

        Return ``self`` as an int.

        EXAMPLES::

            sage: ntl.ZZ(22).__int__()
            22
            sage: type(ntl.ZZ(22).__int__())
            <... 'int'>

            sage: ntl.ZZ(10^30).__int__()
            1000000000000000000000000000000
            sage: type(ntl.ZZ(10^30).__int__())
            <class 'int'>"""
    @overload
    def __int__(self) -> Any:
        """ntl_ZZ.__int__(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ.pyx (starting at line 254)

        Return ``self`` as an int.

        EXAMPLES::

            sage: ntl.ZZ(22).__int__()
            22
            sage: type(ntl.ZZ(22).__int__())
            <... 'int'>

            sage: ntl.ZZ(10^30).__int__()
            1000000000000000000000000000000
            sage: type(ntl.ZZ(10^30).__int__())
            <class 'int'>"""
    @overload
    def __int__(self) -> Any:
        """ntl_ZZ.__int__(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ.pyx (starting at line 254)

        Return ``self`` as an int.

        EXAMPLES::

            sage: ntl.ZZ(22).__int__()
            22
            sage: type(ntl.ZZ(22).__int__())
            <... 'int'>

            sage: ntl.ZZ(10^30).__int__()
            1000000000000000000000000000000
            sage: type(ntl.ZZ(10^30).__int__())
            <class 'int'>"""
    @overload
    def __int__(self) -> Any:
        """ntl_ZZ.__int__(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ.pyx (starting at line 254)

        Return ``self`` as an int.

        EXAMPLES::

            sage: ntl.ZZ(22).__int__()
            22
            sage: type(ntl.ZZ(22).__int__())
            <... 'int'>

            sage: ntl.ZZ(10^30).__int__()
            1000000000000000000000000000000
            sage: type(ntl.ZZ(10^30).__int__())
            <class 'int'>"""
    def __le__(self, other: object) -> bool:
        """Return self<=value."""
    def __lt__(self, other: object) -> bool:
        """Return self<value."""
    def __mul__(self, other) -> Any:
        """ntl_ZZ.__mul__(self, other)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ.pyx (starting at line 173)

        EXAMPLES::

            sage: n=ntl.ZZ(2983)*ntl.ZZ(2)
            sage: n
            5966"""
    def __ne__(self, other: object) -> bool:
        """Return self!=value."""
    @overload
    def __neg__(self) -> Any:
        """ntl_ZZ.__neg__(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ.pyx (starting at line 227)

        EXAMPLES::

            sage: x = ntl.ZZ(38)
            sage: -x
            -38
            sage: x.__neg__()
            -38"""
    @overload
    def __neg__(self) -> Any:
        """ntl_ZZ.__neg__(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ.pyx (starting at line 227)

        EXAMPLES::

            sage: x = ntl.ZZ(38)
            sage: -x
            -38
            sage: x.__neg__()
            -38"""
    def __pow__(self, ntl_ZZself, longe, ignored) -> Any:
        """ntl_ZZ.__pow__(ntl_ZZ self, long e, ignored)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ.pyx (starting at line 241)

        EXAMPLES::

            sage: ntl.ZZ(23)^50
            122008981252869411022491112993141891091036959856659100591281395343249"""
    def __radd__(self, other):
        """Return value+self."""
    def __reduce__(self) -> Any:
        """ntl_ZZ.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ.pyx (starting at line 112)

        sage: from sage.libs.ntl.ntl_ZZ import ntl_ZZ
        sage: a = ntl_ZZ(-7)
        sage: loads(dumps(a))
        -7"""
    def __rmul__(self, other):
        """Return value*self."""
    def __rpow__(self, other):
        """Return pow(value, self, mod)."""
    def __rsub__(self, other):
        """Return value-self."""
    def __sub__(self, other) -> Any:
        """ntl_ZZ.__sub__(self, other)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ.pyx (starting at line 191)

        EXAMPLES::

            sage: n=ntl.ZZ(2983)-ntl.ZZ(2)
            sage: n
            2981
            sage: ntl.ZZ(2983)-2
            2981"""
