import _cython_3_2_1
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from typing import Any, ClassVar, overload

ntl_zz_pContext: _cython_3_2_1.cython_function_or_method
zz_pContextDict: dict

class ntl_zz_pContext_class:
    """ntl_zz_pContext_class(long v)"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, longv) -> Any:
        """File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_lzz_pContext.pyx (starting at line 27)

                EXAMPLES::

                    # You can construct contexts manually.
                    sage: c = ntl.zz_pContext(11)
                    sage: n1 = ntl.zz_p(12,c)
                    sage: n1
                    1

                    # or You can construct contexts implicitly.
                    sage: n2=ntl.zz_p(12, 7)
                    sage: n2
                    5
                    sage: ntl.zz_p(2,3)+ntl.zz_p(1,3)
                    0
                    sage: n2+n1  # Mismatched moduli:  It will go BOOM!
                    Traceback (most recent call last):
                    ...
                    ValueError: arithmetic operands must have the same modulus.
        """
    @overload
    def modulus(self) -> Any:
        """ntl_zz_pContext_class.modulus(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_lzz_pContext.pyx (starting at line 71)

        Print the modulus for ``self``.

        EXAMPLES::

            sage: c1 = ntl.zz_pContext(36)
            sage: c1.modulus()
            36"""
    @overload
    def modulus(self) -> Any:
        """ntl_zz_pContext_class.modulus(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_lzz_pContext.pyx (starting at line 71)

        Print the modulus for ``self``.

        EXAMPLES::

            sage: c1 = ntl.zz_pContext(36)
            sage: c1.modulus()
            36"""
    @overload
    def restore(self) -> Any:
        """ntl_zz_pContext_class.restore(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_lzz_pContext.pyx (starting at line 83)

        Restore a zz_pContext.

        EXAMPLES::

            sage: c = ntl.zz_pContext(5)
            sage: m = ntl.zz_p(4,7)
            sage: c.restore()"""
    @overload
    def restore(self) -> Any:
        """ntl_zz_pContext_class.restore(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_lzz_pContext.pyx (starting at line 83)

        Restore a zz_pContext.

        EXAMPLES::

            sage: c = ntl.zz_pContext(5)
            sage: m = ntl.zz_p(4,7)
            sage: c.restore()"""
    def __reduce__(self) -> Any:
        """ntl_zz_pContext_class.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_lzz_pContext.pyx (starting at line 61)

        EXAMPLES::

            sage: c=ntl.zz_pContext(13)
            sage: loads(dumps(c)) is c
            True"""
