import _cython_3_2_1
from typing import Any, ClassVar, overload

GF2EContextDict: dict
ntl_GF2EContext: _cython_3_2_1.cython_function_or_method

class ntl_GF2EContext_class:
    """ntl_GF2EContext_class(ntl_GF2X v)"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, ntl_GF2Xv) -> Any:
        """File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_GF2EContext.pyx (starting at line 31)

                EXAMPLES::

                    # You can construct contexts manually.
                    sage: ctx = ntl.GF2EContext(ntl.GF2X([1,1,0,1]))
                    sage: n1 = ntl.GF2E([1,1],ctx)
                    sage: n1
                    [1 1]

                    # or You can construct contexts implicitly.
                    sage: n2 = ntl.GF2E([0,1], ntl.GF2X([1,1,0,1]))
                    sage: n2
                    [0 1]
                    sage: ntl.GF2E(2, GF(2^8,'a'))+ntl.GF2E([0,1],ctx)
                    Traceback (most recent call last):
                    ...
                    ValueError: You cannot perform arithmetic with elements in different fields.

                    sage: n2+n1  # Mismatched moduli:  It will go BOOM!
                    [1]
        """
    @overload
    def modulus(self) -> Any:
        """ntl_GF2EContext_class.modulus(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_GF2EContext.pyx (starting at line 81)

        Return the current modulus associated to this
        context.

        EXAMPLES::

            sage: c = ntl.GF2EContext(GF(2^7,'foo'))
            sage: c.modulus()
            [1 1 0 0 0 0 0 1]"""
    @overload
    def modulus(self) -> Any:
        """ntl_GF2EContext_class.modulus(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_GF2EContext.pyx (starting at line 81)

        Return the current modulus associated to this
        context.

        EXAMPLES::

            sage: c = ntl.GF2EContext(GF(2^7,'foo'))
            sage: c.modulus()
            [1 1 0 0 0 0 0 1]"""
    def restore(self) -> Any:
        """ntl_GF2EContext_class.restore(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_GF2EContext.pyx (starting at line 94)

        EXAMPLES::

            sage: c1 = ntl.GF2E([0,1],GF(2^4,'a')) ; c2 = ntl.GF2E([1,0,1],GF(2^4,'a'))
            sage: c1+c2
            [1 1 1]
            sage: d1 = ntl.GF2E([0,1],GF(2^5,'a')) ; d2 = ntl.GF2E([0,0,1],GF(2^5,'a'))
            sage: d1*d2 ## indirect doctest
            [0 0 0 1]"""
    def __reduce__(self) -> Any:
        """ntl_GF2EContext_class.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_GF2EContext.pyx (starting at line 59)

        EXAMPLES::

            sage: c = ntl.GF2EContext(GF(2^5,'b'))
            sage: loads(dumps(c)) is c
            True"""
