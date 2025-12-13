import _cython_3_2_1
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from typing import Any, ClassVar, overload

ZZ_pEContextDict: dict
ntl_ZZ_pEContext: _cython_3_2_1.cython_function_or_method

class ntl_ZZ_pEContext_class:
    """ntl_ZZ_pEContext_class(ntl_ZZ_pX f)"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, ntl_ZZ_pXf) -> Any:
        """File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pEContext.pyx (starting at line 34)

                EXAMPLES:

                You can construct contexts manually::

                    sage: c=ntl.ZZ_pEContext(ntl.ZZ_pX([4,1,6],25))
                    sage: n1=c.ZZ_pE([10,17,12])
                    sage: n1
                    [2 15]

                Or you can construct contexts implicitly::

                    sage: n2=ntl.ZZ_pE(12, ntl.ZZ_pX([1,1,1],7))
                    sage: n2
                    [5]
                    sage: n2+n1  # Mismatched moduli:  It will go BOOM!
                    Traceback (most recent call last):
                    ...
                    ValueError: You cannot perform arithmetic with elements of different moduli.
        """
    def ZZ_pE(self, v=...) -> Any:
        """ntl_ZZ_pEContext_class.ZZ_pE(self, v=None)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pEContext.pyx (starting at line 141)

        Return a ZZ_pE object with modulus ``self`` out of the data v.

        EXAMPLES::

            sage: c = ntl.ZZ_pEContext(ntl.ZZ_pX([1,1,1], 7))
            sage: c.ZZ_pE([4,3])
            [4 3]"""
    def ZZ_pEX(self, v=...) -> Any:
        """ntl_ZZ_pEContext_class.ZZ_pEX(self, v=None)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pEContext.pyx (starting at line 154)

        Return a ZZ_pE object with modulus ``self`` out of the data v.

        EXAMPLES::

            sage: c = ntl.ZZ_pEContext(ntl.ZZ_pX([1,1,1], 7))
            sage: c.ZZ_pEX([4,3])
            [[4] [3]]"""
    @overload
    def get_pc(self) -> Any:
        """ntl_ZZ_pEContext_class.get_pc(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pEContext.pyx (starting at line 87)

        Return the ZZ_pContext contained within ``self``.

        EXAMPLES::

            sage: c = ntl.ZZ_pEContext(ntl.ZZ_pX([1,1,1], 7)); c
            NTL modulus [1 1 1] (mod 7)
            sage: c.get_pc()
            NTL modulus 7"""
    @overload
    def get_pc(self) -> Any:
        """ntl_ZZ_pEContext_class.get_pc(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pEContext.pyx (starting at line 87)

        Return the ZZ_pContext contained within ``self``.

        EXAMPLES::

            sage: c = ntl.ZZ_pEContext(ntl.ZZ_pX([1,1,1], 7)); c
            NTL modulus [1 1 1] (mod 7)
            sage: c.get_pc()
            NTL modulus 7"""
    @overload
    def polynomial(self) -> Any:
        """ntl_ZZ_pEContext_class.polynomial(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pEContext.pyx (starting at line 100)

        Return the ZZ_pX polynomial defining ``self``.

        EXAMPLES::

            sage: c = ntl.ZZ_pEContext(ntl.ZZ_pX([1,1,1], 7))
            sage: c.polynomial()
            [1 1 1]"""
    @overload
    def polynomial(self) -> Any:
        """ntl_ZZ_pEContext_class.polynomial(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pEContext.pyx (starting at line 100)

        Return the ZZ_pX polynomial defining ``self``.

        EXAMPLES::

            sage: c = ntl.ZZ_pEContext(ntl.ZZ_pX([1,1,1], 7))
            sage: c.polynomial()
            [1 1 1]"""
    def restore(self) -> Any:
        """ntl_ZZ_pEContext_class.restore(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pEContext.pyx (starting at line 112)

        Manually set the global NTL modulus to be ``self``.

        This should be done automatically by all of the NTL wrapper classes.

        CRUCIAL: If you are writing your own classes that use ZZ_p_c, ZZ_pX_c, ZZ_pE_c, ZZ_pEX_c
        then you MUST restore the context before calling off to NTL for anything.  If the context has been
        switched by other code then behavior of operations is undefined.  See the NTL documentation for
        more details (or the wrappers in sage.libs.ntl)"""
    def __reduce__(self) -> Any:
        """ntl_ZZ_pEContext_class.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pEContext.pyx (starting at line 66)

        EXAMPLES::

           sage: c=ntl.ZZ_pEContext(ntl.ZZ_pX([1,1,1],7))
           sage: loads(dumps(c)) is c
           True"""
