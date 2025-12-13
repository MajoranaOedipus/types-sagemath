import _cython_3_2_1
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from typing import Any, ClassVar, overload

ZZ_pContext_factory: ntl_ZZ_pContext_factory
ntl_ZZ_pContext: _cython_3_2_1.cython_function_or_method

class ntl_ZZ_pContext_class:
    """ntl_ZZ_pContext_class(ntl_ZZ v)"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, ntl_ZZv) -> Any:
        """File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pContext.pyx (starting at line 32)

                EXAMPLES::

                    # You can construct contexts manually.
                    sage: c = ntl.ZZ_pContext(11)
                    sage: n1 = ntl.ZZ_p(12,c)
                    sage: n1
                    1

                    # or You can construct contexts implicitly.
                    sage: n2 = ntl.ZZ_p(12, 7)
                    sage: n2
                    5
                    sage: ntl.ZZ_p(2,3)+ntl.ZZ_p(1,3)
                    0
                    sage: n2+n1  # Mismatched moduli:  It will go BOOM!
                    Traceback (most recent call last):
                    ...
                    ValueError: You cannot perform arithmetic with elements of different moduli.
        """
    @overload
    def modulus(self) -> Any:
        """ntl_ZZ_pContext_class.modulus(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pContext.pyx (starting at line 85)

        Return the current modulus associated to this
        context.

        EXAMPLES::

            sage: c = ntl.ZZ_pContext(7)
            sage: c.modulus()
            7

            sage: c = ntl.ZZ_pContext(10^30)
            sage: type(c.modulus())
            <class 'sage.rings.integer.Integer'>
            sage: c.modulus() == 10^30
            True"""
    @overload
    def modulus(self) -> Any:
        """ntl_ZZ_pContext_class.modulus(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pContext.pyx (starting at line 85)

        Return the current modulus associated to this
        context.

        EXAMPLES::

            sage: c = ntl.ZZ_pContext(7)
            sage: c.modulus()
            7

            sage: c = ntl.ZZ_pContext(10^30)
            sage: type(c.modulus())
            <class 'sage.rings.integer.Integer'>
            sage: c.modulus() == 10^30
            True"""
    @overload
    def modulus(self) -> Any:
        """ntl_ZZ_pContext_class.modulus(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pContext.pyx (starting at line 85)

        Return the current modulus associated to this
        context.

        EXAMPLES::

            sage: c = ntl.ZZ_pContext(7)
            sage: c.modulus()
            7

            sage: c = ntl.ZZ_pContext(10^30)
            sage: type(c.modulus())
            <class 'sage.rings.integer.Integer'>
            sage: c.modulus() == 10^30
            True"""
    @overload
    def modulus(self) -> Any:
        """ntl_ZZ_pContext_class.modulus(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pContext.pyx (starting at line 85)

        Return the current modulus associated to this
        context.

        EXAMPLES::

            sage: c = ntl.ZZ_pContext(7)
            sage: c.modulus()
            7

            sage: c = ntl.ZZ_pContext(10^30)
            sage: type(c.modulus())
            <class 'sage.rings.integer.Integer'>
            sage: c.modulus() == 10^30
            True"""
    def restore(self) -> Any:
        """ntl_ZZ_pContext_class.restore(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pContext.pyx (starting at line 104)

        EXAMPLES::

            sage: c1 = ntl.ZZ_p(5,92) ; c2 = ntl.ZZ_p(7,92)
            sage: c1+c2
            12
            sage: d1 = ntl.ZZ_p(38,91) ; d2 = ntl.ZZ_p(3,91)
            sage: d1*d2 ## indirect doctest
            23"""
    def __hash__(self) -> Any:
        """ntl_ZZ_pContext_class.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pContext.pyx (starting at line 82)"""
    def __reduce__(self) -> Any:
        """ntl_ZZ_pContext_class.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pContext.pyx (starting at line 60)

        EXAMPLES::

            sage: c = ntl.ZZ_pContext(13)
            sage: loads(dumps(c)) is c
            True"""

class ntl_ZZ_pContext_factory:
    """ntl_ZZ_pContext_factory()"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self) -> Any:
        """File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pContext.pyx (starting at line 162)"""
