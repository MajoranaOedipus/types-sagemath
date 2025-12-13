import sage.rings.padics.padic_ext_element
from sage.categories.category import big as big, one as one, two as two, zero as zero
from sage.libs.ntl.ntl_ZZ_pContext import ntl_ZZ_pContext as ntl_ZZ_pContext
from sage.rings.finite_rings.integer_mod import IntegerMod_abstract as IntegerMod_abstract
from sage.rings.rational_field import QQ as QQ
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from typing import Any, ClassVar

class pAdicZZpXElement(sage.rings.padics.padic_ext_element.pAdicExtElement):
    """pAdicZZpXElement(parent)"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, parent) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/padics/padic_ZZ_pX_element.pyx (starting at line 56)

                Initialization.

                EXAMPLES::

                    sage: A = Zp(next_prime(50000),10)
                    sage: S.<x> = A[]
                    sage: B.<t> = A.ext(x^2 + next_prime(50000))  # indirect doctest
        """
    def norm(self, base=...) -> Any:
        """pAdicZZpXElement.norm(self, base=None)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_ZZ_pX_element.pyx (starting at line 354)

        Return the absolute or relative norm of this element.

        .. NOTE::

            This is not the `p`-adic absolute value.  This is a
            field theoretic norm down to a ground ring.  If you want the
            `p`-adic absolute value, use the ``abs()`` function instead.

        If ``base`` is given then ``base`` must be a subfield of the
        parent `L` of ``self``, in which case the norm is the relative
        norm from L to ``base``.

        In all other cases, the norm is the absolute norm down to
        `\\QQ_p` or `\\ZZ_p`.

        EXAMPLES::

            sage: R = ZpCR(5,5)
            sage: S.<x> = R[]
            sage: f = x^5 + 75*x^3 - 15*x^2 + 125*x - 5
            sage: W.<w> = R.ext(f)
            sage: ((1+2*w)^5).norm()
            1 + 5^2 + O(5^5)
            sage: ((1+2*w)).norm()^5
            1 + 5^2 + O(5^5)

        TESTS::

           sage: R = ZpCA(5,5)
           sage: S.<x> = ZZ[]
           sage: f = x^5 + 75*x^3 - 15*x^2 + 125*x - 5
           sage: W.<w> = R.ext(f)
           sage: ((1+2*w)^5).norm()                                                     # needs sage.geometry.polyhedron
           1 + 5^2 + O(5^5)
           sage: ((1+2*w)).norm()^5                                                     # needs sage.geometry.polyhedron
           1 + 5^2 + O(5^5)
           sage: R = ZpFM(5,5)
           sage: S.<x> = ZZ[]
           sage: f = x^5 + 75*x^3 - 15*x^2 + 125*x - 5
           sage: W.<w> = R.ext(f)
           sage: ((1+2*w)^5).norm()                                                     # needs sage.geometry.polyhedron
           1 + 5^2
           sage: ((1+2*w)).norm()^5                                                     # needs sage.geometry.polyhedron
           1 + 5^2

        Check that :issue:`11586` has been resolved::

            sage: R.<x> = QQ[]
            sage: f = x^2 + 3*x + 1
            sage: M.<a> = Qp(7).extension(f)
            sage: M(7).norm()
            7^2 + O(7^22)
            sage: b = 7*a + 35
            sage: b.norm()
            4*7^2 + 7^3 + O(7^22)
            sage: b*b.frobenius()
            4*7^2 + 7^3 + O(7^22)"""
    def trace(self, base=...) -> Any:
        """pAdicZZpXElement.trace(self, base=None)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_ZZ_pX_element.pyx (starting at line 432)

        Return the absolute or relative trace of this element.

        If ``base`` is given then ``base`` must be a subfield of the
        parent `L` of ``self``, in which case the norm is the relative
        norm from `L` to ``base``.

        In all other cases, the norm is the absolute norm down to
        `\\QQ_p` or `\\ZZ_p`.

        EXAMPLES::

            sage: R = ZpCR(5,5)
            sage: S.<x> = R[]
            sage: f = x^5 + 75*x^3 - 15*x^2 + 125*x - 5
            sage: W.<w> = R.ext(f)
            sage: a = (2+3*w)^7
            sage: b = (6+w^3)^5
            sage: a.trace()
            3*5 + 2*5^2 + 3*5^3 + 2*5^4 + O(5^5)
            sage: a.trace() + b.trace()
            4*5 + 5^2 + 5^3 + 2*5^4 + O(5^5)
            sage: (a+b).trace()
            4*5 + 5^2 + 5^3 + 2*5^4 + O(5^5)

        TESTS::

            sage: # needs sage.geometry.polyhedron
            sage: R = ZpCA(5,5)
            sage: S.<x> = ZZ[]
            sage: f = x^5 + 75*x^3 - 15*x^2 + 125*x - 5
            sage: W.<w> = R.ext(f)
            sage: a = (2+3*w)^7
            sage: b = (6+w^3)^5
            sage: a.trace()
            3*5 + 2*5^2 + 3*5^3 + 2*5^4 + O(5^5)
            sage: a.trace() + b.trace()
            4*5 + 5^2 + 5^3 + 2*5^4 + O(5^5)
            sage: (a+b).trace()
            4*5 + 5^2 + 5^3 + 2*5^4 + O(5^5)
            sage: R = ZpFM(5,5)
            sage: S.<x> = R[]
            sage: f = x^5 + 75*x^3 - 15*x^2 + 125*x - 5
            sage: W.<w> = R.ext(f)
            sage: a = (2+3*w)^7
            sage: b = (6+w^3)^5
            sage: a.trace()
            3*5 + 2*5^2 + 3*5^3 + 2*5^4
            sage: a.trace() + b.trace()
            4*5 + 5^2 + 5^3 + 2*5^4
            sage: (a+b).trace()
            4*5 + 5^2 + 5^3 + 2*5^4

        TESTS:

        We check that :issue:`32072` is resolved::

            sage: F = Qp(2)
            sage: S.<x> = F[]
            sage: L.<w> = F.ext(x^2 - 2)
            sage: L(0, 20).trace()
            O(2^10)"""
