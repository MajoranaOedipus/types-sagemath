import _cython_3_2_1
from sage.libs.ntl.ntl_GF2EContext import ntl_GF2EContext as ntl_GF2EContext
from sage.libs.ntl.ntl_ZZ import unpickle_class_args as unpickle_class_args
from typing import Any, ClassVar, overload

ntl_GF2E_random: _cython_3_2_1.cython_function_or_method

class ntl_GF2E:
    """ntl_GF2E(x=None, modulus=None)

    File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_GF2E.pyx (starting at line 75)

    The :class:`GF2E` represents a finite extension field over GF(2)
    using NTL. Elements are represented as polynomials over GF(2)
    modulo a modulus.

    This modulus must be set by creating a GF2EContext first and pass
    that context to the constructor of all elements."""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, x=..., modulus=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_GF2E.pyx (starting at line 85)

                Construct a new finite field element in GF(2**x).

                If you pass a string to the constructor please note that byte
                sequences and the hexadecimal notation are Little Endian in
                NTL.  So e.g. '[0 1]' == '0x2' == x.

                INPUT:

                - ``x`` -- value to be assigned to this element. Same types as
                  ``ntl.GF2X()`` are accepted.
                - ``modulus`` -- the context/modulus of the field

                OUTPUT: a new ``ntl.GF2E`` element

                EXAMPLES::

                    sage: k.<a> = GF(2^8)
                    sage: e = ntl.GF2E(a,k); e
                    [0 1]
                    sage: ctx = e.modulus_context()
                    sage: ntl.GF2E('0x1c', ctx)
                    [1 0 0 0 0 0 1 1]
                    sage: ntl.GF2E('[1 0 1 0]', ctx)
                    [1 0 1]
                    sage: ntl.GF2E([1,0,1,0], ctx)
                    [1 0 1]
                    sage: ntl.GF2E(ntl.GF2(1),ctx)
                    [1]
        """
    @overload
    def IsOne(self) -> Any:
        """ntl_GF2E.IsOne(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_GF2E.pyx (starting at line 366)

        Return ``True`` if this element equals one, ``False`` otherwise.

        EXAMPLES::

            sage: ctx = ntl.GF2EContext(ntl.GF2X([1,1,0,1,1,0,0,0,1]))
            sage: x = ntl.GF2E([1,0,1,0,1], ctx) ; y = ntl.GF2E([0,1,0,1,1,0,0,0,1], ctx)
            sage: x.IsOne()
            False
            sage: y.IsOne()
            True"""
    @overload
    def IsOne(self) -> Any:
        """ntl_GF2E.IsOne(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_GF2E.pyx (starting at line 366)

        Return ``True`` if this element equals one, ``False`` otherwise.

        EXAMPLES::

            sage: ctx = ntl.GF2EContext(ntl.GF2X([1,1,0,1,1,0,0,0,1]))
            sage: x = ntl.GF2E([1,0,1,0,1], ctx) ; y = ntl.GF2E([0,1,0,1,1,0,0,0,1], ctx)
            sage: x.IsOne()
            False
            sage: y.IsOne()
            True"""
    @overload
    def IsOne(self) -> Any:
        """ntl_GF2E.IsOne(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_GF2E.pyx (starting at line 366)

        Return ``True`` if this element equals one, ``False`` otherwise.

        EXAMPLES::

            sage: ctx = ntl.GF2EContext(ntl.GF2X([1,1,0,1,1,0,0,0,1]))
            sage: x = ntl.GF2E([1,0,1,0,1], ctx) ; y = ntl.GF2E([0,1,0,1,1,0,0,0,1], ctx)
            sage: x.IsOne()
            False
            sage: y.IsOne()
            True"""
    @overload
    def IsZero(self) -> Any:
        """ntl_GF2E.IsZero(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_GF2E.pyx (starting at line 351)

        Return ``True`` if this element equals zero, ``False`` otherwise.

        EXAMPLES::

            sage: ctx = ntl.GF2EContext(ntl.GF2X([1,1,0,1,1,0,0,0,1]))
            sage: x = ntl.GF2E([1,0,1,0,1], ctx) ; y = ntl.GF2E([1,1,0,1,1,0,0,0,1], ctx)
            sage: x.IsZero()
            False
            sage: y.IsZero()
            True"""
    @overload
    def IsZero(self) -> Any:
        """ntl_GF2E.IsZero(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_GF2E.pyx (starting at line 351)

        Return ``True`` if this element equals zero, ``False`` otherwise.

        EXAMPLES::

            sage: ctx = ntl.GF2EContext(ntl.GF2X([1,1,0,1,1,0,0,0,1]))
            sage: x = ntl.GF2E([1,0,1,0,1], ctx) ; y = ntl.GF2E([1,1,0,1,1,0,0,0,1], ctx)
            sage: x.IsZero()
            False
            sage: y.IsZero()
            True"""
    @overload
    def IsZero(self) -> Any:
        """ntl_GF2E.IsZero(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_GF2E.pyx (starting at line 351)

        Return ``True`` if this element equals zero, ``False`` otherwise.

        EXAMPLES::

            sage: ctx = ntl.GF2EContext(ntl.GF2X([1,1,0,1,1,0,0,0,1]))
            sage: x = ntl.GF2E([1,0,1,0,1], ctx) ; y = ntl.GF2E([1,1,0,1,1,0,0,0,1], ctx)
            sage: x.IsZero()
            False
            sage: y.IsZero()
            True"""
    @overload
    def list(self) -> Any:
        """ntl_GF2E.list(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_GF2E.pyx (starting at line 415)

        Represent this element as a list of binary digits.

        EXAMPLES::

             sage: e=ntl.GF2E([0,1,1],GF(2^4,'a'))
             sage: e.list()
             [0, 1, 1]
             sage: e=ntl.GF2E('0xff',GF(2^8,'a'))
             sage: e.list()
             [1, 1, 1, 1, 1, 1, 1, 1]

        OUTPUT: list of digits representing the coefficients in this element's
        polynomial representation"""
    @overload
    def list(self) -> Any:
        """ntl_GF2E.list(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_GF2E.pyx (starting at line 415)

        Represent this element as a list of binary digits.

        EXAMPLES::

             sage: e=ntl.GF2E([0,1,1],GF(2^4,'a'))
             sage: e.list()
             [0, 1, 1]
             sage: e=ntl.GF2E('0xff',GF(2^8,'a'))
             sage: e.list()
             [1, 1, 1, 1, 1, 1, 1, 1]

        OUTPUT: list of digits representing the coefficients in this element's
        polynomial representation"""
    @overload
    def list(self) -> Any:
        """ntl_GF2E.list(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_GF2E.pyx (starting at line 415)

        Represent this element as a list of binary digits.

        EXAMPLES::

             sage: e=ntl.GF2E([0,1,1],GF(2^4,'a'))
             sage: e.list()
             [0, 1, 1]
             sage: e=ntl.GF2E('0xff',GF(2^8,'a'))
             sage: e.list()
             [1, 1, 1, 1, 1, 1, 1, 1]

        OUTPUT: list of digits representing the coefficients in this element's
        polynomial representation"""
    @overload
    def modulus_context(self) -> Any:
        """ntl_GF2E.modulus_context(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_GF2E.pyx (starting at line 177)

        Return the structure that holds the underlying NTL GF2E modulus.

        EXAMPLES::

            sage: ctx = ntl.GF2EContext( ntl.GF2X([1,1,0,1,1,0,0,0,1]) )
            sage: a = ntl.GF2E(ntl.ZZ_pX([1,1,3],2), ctx)
            sage: cty = a.modulus_context(); cty
            NTL modulus [1 1 0 1 1 0 0 0 1]
            sage: ctx == cty
            True"""
    @overload
    def modulus_context(self) -> Any:
        """ntl_GF2E.modulus_context(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_GF2E.pyx (starting at line 177)

        Return the structure that holds the underlying NTL GF2E modulus.

        EXAMPLES::

            sage: ctx = ntl.GF2EContext( ntl.GF2X([1,1,0,1,1,0,0,0,1]) )
            sage: a = ntl.GF2E(ntl.ZZ_pX([1,1,3],2), ctx)
            sage: cty = a.modulus_context(); cty
            NTL modulus [1 1 0 1 1 0 0 0 1]
            sage: ctx == cty
            True"""
    @overload
    def rep(self) -> Any:
        """ntl_GF2E.rep(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_GF2E.pyx (starting at line 398)

        Return a ntl.GF2X copy of this element.

        EXAMPLES::

            sage: ctx = ntl.GF2EContext(ntl.GF2X([1,1,0,1,1,0,0,0,1]))
            sage: a = ntl.GF2E('0x1c', ctx)
            sage: a.rep()
            [1 0 0 0 0 0 1 1]
            sage: type(a.rep())
            <class 'sage.libs.ntl.ntl_GF2X.ntl_GF2X'>"""
    @overload
    def rep(self) -> Any:
        """ntl_GF2E.rep(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_GF2E.pyx (starting at line 398)

        Return a ntl.GF2X copy of this element.

        EXAMPLES::

            sage: ctx = ntl.GF2EContext(ntl.GF2X([1,1,0,1,1,0,0,0,1]))
            sage: a = ntl.GF2E('0x1c', ctx)
            sage: a.rep()
            [1 0 0 0 0 0 1 1]
            sage: type(a.rep())
            <class 'sage.libs.ntl.ntl_GF2X.ntl_GF2X'>"""
    @overload
    def rep(self) -> Any:
        """ntl_GF2E.rep(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_GF2E.pyx (starting at line 398)

        Return a ntl.GF2X copy of this element.

        EXAMPLES::

            sage: ctx = ntl.GF2EContext(ntl.GF2X([1,1,0,1,1,0,0,0,1]))
            sage: a = ntl.GF2E('0x1c', ctx)
            sage: a.rep()
            [1 0 0 0 0 0 1 1]
            sage: type(a.rep())
            <class 'sage.libs.ntl.ntl_GF2X.ntl_GF2X'>"""
    @overload
    def trace(self) -> Any:
        """ntl_GF2E.trace(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_GF2E.pyx (starting at line 381)

        Return the trace of this element.

        EXAMPLES::

            sage: ctx = ntl.GF2EContext(ntl.GF2X([1,1,0,1,1,0,0,0,1]))
            sage: x = ntl.GF2E([1,0,1,0,1], ctx) ; y = ntl.GF2E([0,1,1,0,1,1], ctx)
            sage: x.trace()
            0
            sage: y.trace()
            1"""
    @overload
    def trace(self) -> Any:
        """ntl_GF2E.trace(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_GF2E.pyx (starting at line 381)

        Return the trace of this element.

        EXAMPLES::

            sage: ctx = ntl.GF2EContext(ntl.GF2X([1,1,0,1,1,0,0,0,1]))
            sage: x = ntl.GF2E([1,0,1,0,1], ctx) ; y = ntl.GF2E([0,1,1,0,1,1], ctx)
            sage: x.trace()
            0
            sage: y.trace()
            1"""
    @overload
    def trace(self) -> Any:
        """ntl_GF2E.trace(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_GF2E.pyx (starting at line 381)

        Return the trace of this element.

        EXAMPLES::

            sage: ctx = ntl.GF2EContext(ntl.GF2X([1,1,0,1,1,0,0,0,1]))
            sage: x = ntl.GF2E([1,0,1,0,1], ctx) ; y = ntl.GF2E([0,1,1,0,1,1], ctx)
            sage: x.trace()
            0
            sage: y.trace()
            1"""
    def __add__(self, ntl_GF2Eself, other) -> Any:
        """ntl_GF2E.__add__(ntl_GF2E self, other)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_GF2E.pyx (starting at line 258)

        EXAMPLES::

            sage: ctx = ntl.GF2EContext(ntl.GF2X([1,1,0,1,1,0,0,0,1]))
            sage: x = ntl.GF2E([1,0,1,0,1], ctx) ; y = ntl.GF2E([1,1,0,1,1], ctx)
            sage: x+y ## indirect doctest
            [0 1 1 1]"""
    def __copy__(self) -> Any:
        """ntl_GF2E.__copy__(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_GF2E.pyx (starting at line 205)

        Return a copy of ``self``.

        EXAMPLES::

            sage: x = ntl.GF2E([0,1,1],GF(2^4,'a'))
            sage: y = copy(x)
            sage: x == y
            True
            sage: x is y
            False"""
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
    def __mul__(self, ntl_GF2Eself, other) -> Any:
        """ntl_GF2E.__mul__(ntl_GF2E self, other)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_GF2E.pyx (starting at line 222)

        EXAMPLES::

            sage: ctx = ntl.GF2EContext(ntl.GF2X([1,1,0,1,1,0,0,0,1]))
            sage: x = ntl.GF2E([1,0,1,0,1], ctx) ; y = ntl.GF2E([1,1,0,1,1], ctx)
            sage: x*y ## indirect doctest
            [0 0 1 1 1 0 1 1]"""
    def __ne__(self, other: object) -> bool:
        """Return self!=value."""
    def __neg__(self) -> Any:
        """ntl_GF2E.__neg__(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_GF2E.pyx (starting at line 294)

        EXAMPLES::

            sage: ctx = ntl.GF2EContext(ntl.GF2X([1,1,0,1,1,0,0,0,1]))
            sage: x = ntl.GF2E([1,0,1,0,1], ctx)
            sage: -x ## indirect doctest
            [1 0 1 0 1]"""
    def __pow__(self, ntl_GF2Eself, longe, ignored) -> Any:
        """ntl_GF2E.__pow__(ntl_GF2E self, long e, ignored)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_GF2E.pyx (starting at line 307)

        EXAMPLES::

            sage: ctx = ntl.GF2EContext(ntl.GF2X([1,1,0,1,1,0,0,0,1]))
            sage: x = ntl.GF2E([1,0,1,0,1], ctx)
            sage: x**2 ## indirect doctest
            [0 1 0 1]"""
    def __radd__(self, other):
        """Return value+self."""
    def __reduce__(self) -> Any:
        """ntl_GF2E.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_GF2E.pyx (starting at line 166)

        EXAMPLES::

            sage: ctx = ntl.GF2EContext( ntl.GF2X([1,1,0,1,1,0,0,0,1]) )
            sage: a = ntl.GF2E(ntl.ZZ_pX([1,1,3],2), ctx)
            sage: loads(dumps(a)) == a
            True"""
    def __rmul__(self, other):
        """Return value*self."""
    def __rpow__(self, other):
        """Return pow(value, self, mod)."""
    def __rsub__(self, other):
        """Return value-self."""
    def __rtruediv__(self, other):
        """Return value/self."""
    def __sub__(self, ntl_GF2Eself, other) -> Any:
        """ntl_GF2E.__sub__(ntl_GF2E self, other)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_GF2E.pyx (starting at line 240)

        EXAMPLES::

            sage: ctx = ntl.GF2EContext(ntl.GF2X([1,1,0,1,1,0,0,0,1]))
            sage: x = ntl.GF2E([1,0,1,0,1], ctx) ; y = ntl.GF2E([1,1,0,1,1], ctx)
            sage: x - y ## indirect doctest
            [0 1 1 1]"""
    def __truediv__(self, ntl_GF2Eself, other) -> Any:
        """ntl_GF2E.__truediv__(ntl_GF2E self, other)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_GF2E.pyx (starting at line 276)

        EXAMPLES::

            sage: ctx = ntl.GF2EContext(ntl.GF2X([1,1,0,1,1,0,0,0,1]))
            sage: x = ntl.GF2E([1,0,1,0,1], ctx) ; y = ntl.GF2E([1,1,0,1,1], ctx)
            sage: x/y ## indirect doctest
            [1 0 1 0 0 1 0 1]"""
