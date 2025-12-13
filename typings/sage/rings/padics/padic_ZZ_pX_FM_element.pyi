import _cython_3_2_1
import sage.rings.padics.padic_ZZ_pX_element
from sage.interfaces.abc import GpElement as GpElement
from sage.rings.finite_rings.integer_mod import IntegerMod_abstract as IntegerMod_abstract
from sage.rings.finite_rings.integer_mod_ring import IntegerModRing as IntegerModRing
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from sage.structure.richcmp import revop as revop, rich_to_bool as rich_to_bool, rich_to_bool_sgn as rich_to_bool_sgn, richcmp as richcmp, richcmp_not_equal as richcmp_not_equal
from typing import Any, ClassVar, overload

make_ZZpXFMElement: _cython_3_2_1.cython_function_or_method

class pAdicZZpXFMElement(sage.rings.padics.padic_ZZ_pX_element.pAdicZZpXElement):
    """pAdicZZpXFMElement(parent, x, absprec=None, relprec=None, empty=False)"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, parent, x, absprec=..., relprec=..., empty=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/padics/padic_ZZ_pX_FM_element.pyx (starting at line 153)

                Create an element of a fixed modulus, unramified or
                eisenstein extension of `\\ZZ_p` or `\\QQ_p`.

                INPUT:

                - ``parent`` -- either an ``EisensteinRingFixedMod`` or
                  ``UnramifiedRingFixedMod``

                - ``x`` -- integer, rational, `p`-adic element, polynomial,
                  list, integer_mod, pari int/frac/poly_t/pol_mod, an
                  ``ntl_ZZ_pX``, an ``ntl_ZZX``, an ``ntl_ZZ``, or an
                  ``ntl_ZZ_p``

                - ``absprec`` -- not used

                - ``relprec`` -- not used

                - ``empty`` -- whether to return after initializing to zero
                  (without setting anything)

                EXAMPLES::

                    sage: R = ZpFM(5,5)
                    sage: S.<x> = R[]
                    sage: f = x^5 + 75*x^3 - 15*x^2 + 125*x - 5
                    sage: W.<w> = R.ext(f)
                    sage: z = (1+w)^5; z  # indirect doctest
                    1 + w^5 + w^6 + 2*w^7 + 4*w^8 + 3*w^10 + w^12 + 4*w^13 + 4*w^14 + 4*w^15 + 4*w^16 + 4*w^17 + 4*w^20 + w^21 + 4*w^24

                TESTS:

                Check that :issue:`3865` is fixed::

                    sage: W(gp('2 + O(5^2)'))
                    2

                Check that :issue:`13612` has been fixed::

                    sage: # needs sage.libs.flint
                    sage: R = ZpFM(3)
                    sage: S.<a> = R[]
                    sage: W.<a> = R.extension(a^2 + 1)
                    sage: W(W.residue_field().zero())
                    0
        """
    def add_bigoh(self, absprec) -> Any:
        """pAdicZZpXFMElement.add_bigoh(self, absprec)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_ZZ_pX_FM_element.pyx (starting at line 921)

        Return a new element truncated modulo `\\pi^{\\text{absprec}}`.

        This is only implemented for unramified extension at
        this point.

        INPUT:

        - ``absprec`` -- integer

        OUTPUT: a new element truncated modulo `\\pi^{\\mbox{absprec}}`

        EXAMPLES::

            sage: R = Zp(7,4,'fixed-mod')
            sage: a = R(1 + 7 + 7^2)
            sage: a.add_bigoh(1)
            1"""
    @overload
    def expansion(self, n=..., lift_mode=...) -> Any:
        """pAdicZZpXFMElement.expansion(self, n=None, lift_mode='simple')

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_ZZ_pX_FM_element.pyx (starting at line 1275)

        Return a list giving a series representation of this element.

        - If ``lift_mode == 'simple' or 'smallest'``, the returned list will
          consist of

          * integers (in the eisenstein case) or

          * lists of integers (in the unramified case).

        - this element can be reconstructed as

          * a sum of elements of the list times powers of the
            uniformiser (in the eisenstein case), or

          * as a sum of powers of the `p` times polynomials in the
            generator (in the unramified case).

        - If ``lift_mode == 'simple'``, all integers will be in the range
          `[0,p-1]`,

        - If ``lift_mode == 'smallest'`` they will be in the range `[(1-p)/2,
          p/2]`.

        - If ``lift_mode == 'teichmuller'``, returns a list of
          ``pAdicZZpXCRElements``, all of which are Teichmuller representatives
          and such that this element is the sum of that list times powers of the
          uniformizer.

        INPUT:

        - ``n`` -- integer (default: ``None``); if given, returns the
          corresponding entry in the expansion

        EXAMPLES::

            sage: R = ZpFM(5,5)
            sage: S.<x> = R[]
            sage: f = x^5 + 75*x^3 - 15*x^2 + 125*x - 5
            sage: W.<w> = R.ext(f)
            sage: y = W(775); y
            w^10 + 4*w^12 + 2*w^14 + w^15 + 2*w^16 + 4*w^17 + w^18 + w^20 + 2*w^21 + 3*w^22 + w^23 + w^24
            sage: (y>>9).expansion()
            [0, 1, 0, 4, 0, 2, 1, 2, 4, 1, 0, 1, 2, 3, 1, 1, 4, 1, 2, 4, 1, 0, 0, 3]
            sage: (y>>9).expansion(lift_mode='smallest')
            [0, 1, 0, -1, 0, 2, 1, 2, 0, 1, 2, 1, 1, -1, -1, 2, -2, 0, -2, -2, -2, 0, -2, -2, 2]
            sage: w^10 - w^12 + 2*w^14 + w^15 + 2*w^16 + w^18 + 2*w^19 + w^20 + w^21 - w^22 - w^23 + 2*w^24
            w^10 + 4*w^12 + 2*w^14 + w^15 + 2*w^16 + 4*w^17 + w^18 + w^20 + 2*w^21 + 3*w^22 + w^23 + w^24
            sage: g = x^3 + 3*x + 3

            sage: # needs sage.libs.flint
            sage: A.<a> = R.ext(g)
            sage: y = 75 + 45*a + 1200*a^2; y
            4*a*5 + (3*a^2 + a + 3)*5^2 + 4*a^2*5^3 + a^2*5^4
            sage: E = y.expansion(); E
            5-adic expansion of 4*a*5 + (3*a^2 + a + 3)*5^2 + 4*a^2*5^3 + a^2*5^4
            sage: list(E)
            [[], [0, 4], [3, 1, 3], [0, 0, 4], [0, 0, 1]]
            sage: list(y.expansion(lift_mode='smallest'))
            [[], [0, -1], [-2, 2, -2], [1], [0, 0, 2]]
            sage: 5*((-2*5 + 25) + (-1 + 2*5)*a + (-2*5 + 2*125)*a^2)
            4*a*5 + (3*a^2 + a + 3)*5^2 + 4*a^2*5^3 + a^2*5^4
            sage: W(0).expansion()
            []
            sage: list(A(0,4).expansion())
            []

        Check that :issue:`25879` has been resolved::

            sage: K = ZpCA(3,5)
            sage: R.<a> = K[]
            sage: L.<a> = K.extension(a^2 - 3)
            sage: a.residue()
            0"""
    @overload
    def expansion(self) -> Any:
        """pAdicZZpXFMElement.expansion(self, n=None, lift_mode='simple')

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_ZZ_pX_FM_element.pyx (starting at line 1275)

        Return a list giving a series representation of this element.

        - If ``lift_mode == 'simple' or 'smallest'``, the returned list will
          consist of

          * integers (in the eisenstein case) or

          * lists of integers (in the unramified case).

        - this element can be reconstructed as

          * a sum of elements of the list times powers of the
            uniformiser (in the eisenstein case), or

          * as a sum of powers of the `p` times polynomials in the
            generator (in the unramified case).

        - If ``lift_mode == 'simple'``, all integers will be in the range
          `[0,p-1]`,

        - If ``lift_mode == 'smallest'`` they will be in the range `[(1-p)/2,
          p/2]`.

        - If ``lift_mode == 'teichmuller'``, returns a list of
          ``pAdicZZpXCRElements``, all of which are Teichmuller representatives
          and such that this element is the sum of that list times powers of the
          uniformizer.

        INPUT:

        - ``n`` -- integer (default: ``None``); if given, returns the
          corresponding entry in the expansion

        EXAMPLES::

            sage: R = ZpFM(5,5)
            sage: S.<x> = R[]
            sage: f = x^5 + 75*x^3 - 15*x^2 + 125*x - 5
            sage: W.<w> = R.ext(f)
            sage: y = W(775); y
            w^10 + 4*w^12 + 2*w^14 + w^15 + 2*w^16 + 4*w^17 + w^18 + w^20 + 2*w^21 + 3*w^22 + w^23 + w^24
            sage: (y>>9).expansion()
            [0, 1, 0, 4, 0, 2, 1, 2, 4, 1, 0, 1, 2, 3, 1, 1, 4, 1, 2, 4, 1, 0, 0, 3]
            sage: (y>>9).expansion(lift_mode='smallest')
            [0, 1, 0, -1, 0, 2, 1, 2, 0, 1, 2, 1, 1, -1, -1, 2, -2, 0, -2, -2, -2, 0, -2, -2, 2]
            sage: w^10 - w^12 + 2*w^14 + w^15 + 2*w^16 + w^18 + 2*w^19 + w^20 + w^21 - w^22 - w^23 + 2*w^24
            w^10 + 4*w^12 + 2*w^14 + w^15 + 2*w^16 + 4*w^17 + w^18 + w^20 + 2*w^21 + 3*w^22 + w^23 + w^24
            sage: g = x^3 + 3*x + 3

            sage: # needs sage.libs.flint
            sage: A.<a> = R.ext(g)
            sage: y = 75 + 45*a + 1200*a^2; y
            4*a*5 + (3*a^2 + a + 3)*5^2 + 4*a^2*5^3 + a^2*5^4
            sage: E = y.expansion(); E
            5-adic expansion of 4*a*5 + (3*a^2 + a + 3)*5^2 + 4*a^2*5^3 + a^2*5^4
            sage: list(E)
            [[], [0, 4], [3, 1, 3], [0, 0, 4], [0, 0, 1]]
            sage: list(y.expansion(lift_mode='smallest'))
            [[], [0, -1], [-2, 2, -2], [1], [0, 0, 2]]
            sage: 5*((-2*5 + 25) + (-1 + 2*5)*a + (-2*5 + 2*125)*a^2)
            4*a*5 + (3*a^2 + a + 3)*5^2 + 4*a^2*5^3 + a^2*5^4
            sage: W(0).expansion()
            []
            sage: list(A(0,4).expansion())
            []

        Check that :issue:`25879` has been resolved::

            sage: K = ZpCA(3,5)
            sage: R.<a> = K[]
            sage: L.<a> = K.extension(a^2 - 3)
            sage: a.residue()
            0"""
    @overload
    def expansion(self, lift_mode=...) -> Any:
        """pAdicZZpXFMElement.expansion(self, n=None, lift_mode='simple')

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_ZZ_pX_FM_element.pyx (starting at line 1275)

        Return a list giving a series representation of this element.

        - If ``lift_mode == 'simple' or 'smallest'``, the returned list will
          consist of

          * integers (in the eisenstein case) or

          * lists of integers (in the unramified case).

        - this element can be reconstructed as

          * a sum of elements of the list times powers of the
            uniformiser (in the eisenstein case), or

          * as a sum of powers of the `p` times polynomials in the
            generator (in the unramified case).

        - If ``lift_mode == 'simple'``, all integers will be in the range
          `[0,p-1]`,

        - If ``lift_mode == 'smallest'`` they will be in the range `[(1-p)/2,
          p/2]`.

        - If ``lift_mode == 'teichmuller'``, returns a list of
          ``pAdicZZpXCRElements``, all of which are Teichmuller representatives
          and such that this element is the sum of that list times powers of the
          uniformizer.

        INPUT:

        - ``n`` -- integer (default: ``None``); if given, returns the
          corresponding entry in the expansion

        EXAMPLES::

            sage: R = ZpFM(5,5)
            sage: S.<x> = R[]
            sage: f = x^5 + 75*x^3 - 15*x^2 + 125*x - 5
            sage: W.<w> = R.ext(f)
            sage: y = W(775); y
            w^10 + 4*w^12 + 2*w^14 + w^15 + 2*w^16 + 4*w^17 + w^18 + w^20 + 2*w^21 + 3*w^22 + w^23 + w^24
            sage: (y>>9).expansion()
            [0, 1, 0, 4, 0, 2, 1, 2, 4, 1, 0, 1, 2, 3, 1, 1, 4, 1, 2, 4, 1, 0, 0, 3]
            sage: (y>>9).expansion(lift_mode='smallest')
            [0, 1, 0, -1, 0, 2, 1, 2, 0, 1, 2, 1, 1, -1, -1, 2, -2, 0, -2, -2, -2, 0, -2, -2, 2]
            sage: w^10 - w^12 + 2*w^14 + w^15 + 2*w^16 + w^18 + 2*w^19 + w^20 + w^21 - w^22 - w^23 + 2*w^24
            w^10 + 4*w^12 + 2*w^14 + w^15 + 2*w^16 + 4*w^17 + w^18 + w^20 + 2*w^21 + 3*w^22 + w^23 + w^24
            sage: g = x^3 + 3*x + 3

            sage: # needs sage.libs.flint
            sage: A.<a> = R.ext(g)
            sage: y = 75 + 45*a + 1200*a^2; y
            4*a*5 + (3*a^2 + a + 3)*5^2 + 4*a^2*5^3 + a^2*5^4
            sage: E = y.expansion(); E
            5-adic expansion of 4*a*5 + (3*a^2 + a + 3)*5^2 + 4*a^2*5^3 + a^2*5^4
            sage: list(E)
            [[], [0, 4], [3, 1, 3], [0, 0, 4], [0, 0, 1]]
            sage: list(y.expansion(lift_mode='smallest'))
            [[], [0, -1], [-2, 2, -2], [1], [0, 0, 2]]
            sage: 5*((-2*5 + 25) + (-1 + 2*5)*a + (-2*5 + 2*125)*a^2)
            4*a*5 + (3*a^2 + a + 3)*5^2 + 4*a^2*5^3 + a^2*5^4
            sage: W(0).expansion()
            []
            sage: list(A(0,4).expansion())
            []

        Check that :issue:`25879` has been resolved::

            sage: K = ZpCA(3,5)
            sage: R.<a> = K[]
            sage: L.<a> = K.extension(a^2 - 3)
            sage: a.residue()
            0"""
    @overload
    def expansion(self) -> Any:
        """pAdicZZpXFMElement.expansion(self, n=None, lift_mode='simple')

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_ZZ_pX_FM_element.pyx (starting at line 1275)

        Return a list giving a series representation of this element.

        - If ``lift_mode == 'simple' or 'smallest'``, the returned list will
          consist of

          * integers (in the eisenstein case) or

          * lists of integers (in the unramified case).

        - this element can be reconstructed as

          * a sum of elements of the list times powers of the
            uniformiser (in the eisenstein case), or

          * as a sum of powers of the `p` times polynomials in the
            generator (in the unramified case).

        - If ``lift_mode == 'simple'``, all integers will be in the range
          `[0,p-1]`,

        - If ``lift_mode == 'smallest'`` they will be in the range `[(1-p)/2,
          p/2]`.

        - If ``lift_mode == 'teichmuller'``, returns a list of
          ``pAdicZZpXCRElements``, all of which are Teichmuller representatives
          and such that this element is the sum of that list times powers of the
          uniformizer.

        INPUT:

        - ``n`` -- integer (default: ``None``); if given, returns the
          corresponding entry in the expansion

        EXAMPLES::

            sage: R = ZpFM(5,5)
            sage: S.<x> = R[]
            sage: f = x^5 + 75*x^3 - 15*x^2 + 125*x - 5
            sage: W.<w> = R.ext(f)
            sage: y = W(775); y
            w^10 + 4*w^12 + 2*w^14 + w^15 + 2*w^16 + 4*w^17 + w^18 + w^20 + 2*w^21 + 3*w^22 + w^23 + w^24
            sage: (y>>9).expansion()
            [0, 1, 0, 4, 0, 2, 1, 2, 4, 1, 0, 1, 2, 3, 1, 1, 4, 1, 2, 4, 1, 0, 0, 3]
            sage: (y>>9).expansion(lift_mode='smallest')
            [0, 1, 0, -1, 0, 2, 1, 2, 0, 1, 2, 1, 1, -1, -1, 2, -2, 0, -2, -2, -2, 0, -2, -2, 2]
            sage: w^10 - w^12 + 2*w^14 + w^15 + 2*w^16 + w^18 + 2*w^19 + w^20 + w^21 - w^22 - w^23 + 2*w^24
            w^10 + 4*w^12 + 2*w^14 + w^15 + 2*w^16 + 4*w^17 + w^18 + w^20 + 2*w^21 + 3*w^22 + w^23 + w^24
            sage: g = x^3 + 3*x + 3

            sage: # needs sage.libs.flint
            sage: A.<a> = R.ext(g)
            sage: y = 75 + 45*a + 1200*a^2; y
            4*a*5 + (3*a^2 + a + 3)*5^2 + 4*a^2*5^3 + a^2*5^4
            sage: E = y.expansion(); E
            5-adic expansion of 4*a*5 + (3*a^2 + a + 3)*5^2 + 4*a^2*5^3 + a^2*5^4
            sage: list(E)
            [[], [0, 4], [3, 1, 3], [0, 0, 4], [0, 0, 1]]
            sage: list(y.expansion(lift_mode='smallest'))
            [[], [0, -1], [-2, 2, -2], [1], [0, 0, 2]]
            sage: 5*((-2*5 + 25) + (-1 + 2*5)*a + (-2*5 + 2*125)*a^2)
            4*a*5 + (3*a^2 + a + 3)*5^2 + 4*a^2*5^3 + a^2*5^4
            sage: W(0).expansion()
            []
            sage: list(A(0,4).expansion())
            []

        Check that :issue:`25879` has been resolved::

            sage: K = ZpCA(3,5)
            sage: R.<a> = K[]
            sage: L.<a> = K.extension(a^2 - 3)
            sage: a.residue()
            0"""
    @overload
    def expansion(self, lift_mode=...) -> Any:
        """pAdicZZpXFMElement.expansion(self, n=None, lift_mode='simple')

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_ZZ_pX_FM_element.pyx (starting at line 1275)

        Return a list giving a series representation of this element.

        - If ``lift_mode == 'simple' or 'smallest'``, the returned list will
          consist of

          * integers (in the eisenstein case) or

          * lists of integers (in the unramified case).

        - this element can be reconstructed as

          * a sum of elements of the list times powers of the
            uniformiser (in the eisenstein case), or

          * as a sum of powers of the `p` times polynomials in the
            generator (in the unramified case).

        - If ``lift_mode == 'simple'``, all integers will be in the range
          `[0,p-1]`,

        - If ``lift_mode == 'smallest'`` they will be in the range `[(1-p)/2,
          p/2]`.

        - If ``lift_mode == 'teichmuller'``, returns a list of
          ``pAdicZZpXCRElements``, all of which are Teichmuller representatives
          and such that this element is the sum of that list times powers of the
          uniformizer.

        INPUT:

        - ``n`` -- integer (default: ``None``); if given, returns the
          corresponding entry in the expansion

        EXAMPLES::

            sage: R = ZpFM(5,5)
            sage: S.<x> = R[]
            sage: f = x^5 + 75*x^3 - 15*x^2 + 125*x - 5
            sage: W.<w> = R.ext(f)
            sage: y = W(775); y
            w^10 + 4*w^12 + 2*w^14 + w^15 + 2*w^16 + 4*w^17 + w^18 + w^20 + 2*w^21 + 3*w^22 + w^23 + w^24
            sage: (y>>9).expansion()
            [0, 1, 0, 4, 0, 2, 1, 2, 4, 1, 0, 1, 2, 3, 1, 1, 4, 1, 2, 4, 1, 0, 0, 3]
            sage: (y>>9).expansion(lift_mode='smallest')
            [0, 1, 0, -1, 0, 2, 1, 2, 0, 1, 2, 1, 1, -1, -1, 2, -2, 0, -2, -2, -2, 0, -2, -2, 2]
            sage: w^10 - w^12 + 2*w^14 + w^15 + 2*w^16 + w^18 + 2*w^19 + w^20 + w^21 - w^22 - w^23 + 2*w^24
            w^10 + 4*w^12 + 2*w^14 + w^15 + 2*w^16 + 4*w^17 + w^18 + w^20 + 2*w^21 + 3*w^22 + w^23 + w^24
            sage: g = x^3 + 3*x + 3

            sage: # needs sage.libs.flint
            sage: A.<a> = R.ext(g)
            sage: y = 75 + 45*a + 1200*a^2; y
            4*a*5 + (3*a^2 + a + 3)*5^2 + 4*a^2*5^3 + a^2*5^4
            sage: E = y.expansion(); E
            5-adic expansion of 4*a*5 + (3*a^2 + a + 3)*5^2 + 4*a^2*5^3 + a^2*5^4
            sage: list(E)
            [[], [0, 4], [3, 1, 3], [0, 0, 4], [0, 0, 1]]
            sage: list(y.expansion(lift_mode='smallest'))
            [[], [0, -1], [-2, 2, -2], [1], [0, 0, 2]]
            sage: 5*((-2*5 + 25) + (-1 + 2*5)*a + (-2*5 + 2*125)*a^2)
            4*a*5 + (3*a^2 + a + 3)*5^2 + 4*a^2*5^3 + a^2*5^4
            sage: W(0).expansion()
            []
            sage: list(A(0,4).expansion())
            []

        Check that :issue:`25879` has been resolved::

            sage: K = ZpCA(3,5)
            sage: R.<a> = K[]
            sage: L.<a> = K.extension(a^2 - 3)
            sage: a.residue()
            0"""
    @overload
    def expansion(self) -> Any:
        """pAdicZZpXFMElement.expansion(self, n=None, lift_mode='simple')

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_ZZ_pX_FM_element.pyx (starting at line 1275)

        Return a list giving a series representation of this element.

        - If ``lift_mode == 'simple' or 'smallest'``, the returned list will
          consist of

          * integers (in the eisenstein case) or

          * lists of integers (in the unramified case).

        - this element can be reconstructed as

          * a sum of elements of the list times powers of the
            uniformiser (in the eisenstein case), or

          * as a sum of powers of the `p` times polynomials in the
            generator (in the unramified case).

        - If ``lift_mode == 'simple'``, all integers will be in the range
          `[0,p-1]`,

        - If ``lift_mode == 'smallest'`` they will be in the range `[(1-p)/2,
          p/2]`.

        - If ``lift_mode == 'teichmuller'``, returns a list of
          ``pAdicZZpXCRElements``, all of which are Teichmuller representatives
          and such that this element is the sum of that list times powers of the
          uniformizer.

        INPUT:

        - ``n`` -- integer (default: ``None``); if given, returns the
          corresponding entry in the expansion

        EXAMPLES::

            sage: R = ZpFM(5,5)
            sage: S.<x> = R[]
            sage: f = x^5 + 75*x^3 - 15*x^2 + 125*x - 5
            sage: W.<w> = R.ext(f)
            sage: y = W(775); y
            w^10 + 4*w^12 + 2*w^14 + w^15 + 2*w^16 + 4*w^17 + w^18 + w^20 + 2*w^21 + 3*w^22 + w^23 + w^24
            sage: (y>>9).expansion()
            [0, 1, 0, 4, 0, 2, 1, 2, 4, 1, 0, 1, 2, 3, 1, 1, 4, 1, 2, 4, 1, 0, 0, 3]
            sage: (y>>9).expansion(lift_mode='smallest')
            [0, 1, 0, -1, 0, 2, 1, 2, 0, 1, 2, 1, 1, -1, -1, 2, -2, 0, -2, -2, -2, 0, -2, -2, 2]
            sage: w^10 - w^12 + 2*w^14 + w^15 + 2*w^16 + w^18 + 2*w^19 + w^20 + w^21 - w^22 - w^23 + 2*w^24
            w^10 + 4*w^12 + 2*w^14 + w^15 + 2*w^16 + 4*w^17 + w^18 + w^20 + 2*w^21 + 3*w^22 + w^23 + w^24
            sage: g = x^3 + 3*x + 3

            sage: # needs sage.libs.flint
            sage: A.<a> = R.ext(g)
            sage: y = 75 + 45*a + 1200*a^2; y
            4*a*5 + (3*a^2 + a + 3)*5^2 + 4*a^2*5^3 + a^2*5^4
            sage: E = y.expansion(); E
            5-adic expansion of 4*a*5 + (3*a^2 + a + 3)*5^2 + 4*a^2*5^3 + a^2*5^4
            sage: list(E)
            [[], [0, 4], [3, 1, 3], [0, 0, 4], [0, 0, 1]]
            sage: list(y.expansion(lift_mode='smallest'))
            [[], [0, -1], [-2, 2, -2], [1], [0, 0, 2]]
            sage: 5*((-2*5 + 25) + (-1 + 2*5)*a + (-2*5 + 2*125)*a^2)
            4*a*5 + (3*a^2 + a + 3)*5^2 + 4*a^2*5^3 + a^2*5^4
            sage: W(0).expansion()
            []
            sage: list(A(0,4).expansion())
            []

        Check that :issue:`25879` has been resolved::

            sage: K = ZpCA(3,5)
            sage: R.<a> = K[]
            sage: L.<a> = K.extension(a^2 - 3)
            sage: a.residue()
            0"""
    @overload
    def expansion(self) -> Any:
        """pAdicZZpXFMElement.expansion(self, n=None, lift_mode='simple')

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_ZZ_pX_FM_element.pyx (starting at line 1275)

        Return a list giving a series representation of this element.

        - If ``lift_mode == 'simple' or 'smallest'``, the returned list will
          consist of

          * integers (in the eisenstein case) or

          * lists of integers (in the unramified case).

        - this element can be reconstructed as

          * a sum of elements of the list times powers of the
            uniformiser (in the eisenstein case), or

          * as a sum of powers of the `p` times polynomials in the
            generator (in the unramified case).

        - If ``lift_mode == 'simple'``, all integers will be in the range
          `[0,p-1]`,

        - If ``lift_mode == 'smallest'`` they will be in the range `[(1-p)/2,
          p/2]`.

        - If ``lift_mode == 'teichmuller'``, returns a list of
          ``pAdicZZpXCRElements``, all of which are Teichmuller representatives
          and such that this element is the sum of that list times powers of the
          uniformizer.

        INPUT:

        - ``n`` -- integer (default: ``None``); if given, returns the
          corresponding entry in the expansion

        EXAMPLES::

            sage: R = ZpFM(5,5)
            sage: S.<x> = R[]
            sage: f = x^5 + 75*x^3 - 15*x^2 + 125*x - 5
            sage: W.<w> = R.ext(f)
            sage: y = W(775); y
            w^10 + 4*w^12 + 2*w^14 + w^15 + 2*w^16 + 4*w^17 + w^18 + w^20 + 2*w^21 + 3*w^22 + w^23 + w^24
            sage: (y>>9).expansion()
            [0, 1, 0, 4, 0, 2, 1, 2, 4, 1, 0, 1, 2, 3, 1, 1, 4, 1, 2, 4, 1, 0, 0, 3]
            sage: (y>>9).expansion(lift_mode='smallest')
            [0, 1, 0, -1, 0, 2, 1, 2, 0, 1, 2, 1, 1, -1, -1, 2, -2, 0, -2, -2, -2, 0, -2, -2, 2]
            sage: w^10 - w^12 + 2*w^14 + w^15 + 2*w^16 + w^18 + 2*w^19 + w^20 + w^21 - w^22 - w^23 + 2*w^24
            w^10 + 4*w^12 + 2*w^14 + w^15 + 2*w^16 + 4*w^17 + w^18 + w^20 + 2*w^21 + 3*w^22 + w^23 + w^24
            sage: g = x^3 + 3*x + 3

            sage: # needs sage.libs.flint
            sage: A.<a> = R.ext(g)
            sage: y = 75 + 45*a + 1200*a^2; y
            4*a*5 + (3*a^2 + a + 3)*5^2 + 4*a^2*5^3 + a^2*5^4
            sage: E = y.expansion(); E
            5-adic expansion of 4*a*5 + (3*a^2 + a + 3)*5^2 + 4*a^2*5^3 + a^2*5^4
            sage: list(E)
            [[], [0, 4], [3, 1, 3], [0, 0, 4], [0, 0, 1]]
            sage: list(y.expansion(lift_mode='smallest'))
            [[], [0, -1], [-2, 2, -2], [1], [0, 0, 2]]
            sage: 5*((-2*5 + 25) + (-1 + 2*5)*a + (-2*5 + 2*125)*a^2)
            4*a*5 + (3*a^2 + a + 3)*5^2 + 4*a^2*5^3 + a^2*5^4
            sage: W(0).expansion()
            []
            sage: list(A(0,4).expansion())
            []

        Check that :issue:`25879` has been resolved::

            sage: K = ZpCA(3,5)
            sage: R.<a> = K[]
            sage: L.<a> = K.extension(a^2 - 3)
            sage: a.residue()
            0"""
    @overload
    def is_equal_to(self, right, absprec=...) -> Any:
        """pAdicZZpXFMElement.is_equal_to(self, right, absprec=None)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_ZZ_pX_FM_element.pyx (starting at line 1228)

        Return whether ``self`` is equal to ``right`` modulo
        ``self.uniformizer()^absprec``.

        If ``absprec`` is ``None``, returns if ``self`` is equal to
        ``right`` modulo the precision cap.

        EXAMPLES::

            sage: R = Zp(5,5)
            sage: S.<x> = R[]
            sage: f = x^5 + 75*x^3 - 15*x^2 + 125*x - 5
            sage: W.<w> = R.ext(f)
            sage: a = W(47); b = W(47 + 25)
            sage: a.is_equal_to(b)
            False
            sage: a.is_equal_to(b, 7)
            True"""
    @overload
    def is_equal_to(self, b) -> Any:
        """pAdicZZpXFMElement.is_equal_to(self, right, absprec=None)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_ZZ_pX_FM_element.pyx (starting at line 1228)

        Return whether ``self`` is equal to ``right`` modulo
        ``self.uniformizer()^absprec``.

        If ``absprec`` is ``None``, returns if ``self`` is equal to
        ``right`` modulo the precision cap.

        EXAMPLES::

            sage: R = Zp(5,5)
            sage: S.<x> = R[]
            sage: f = x^5 + 75*x^3 - 15*x^2 + 125*x - 5
            sage: W.<w> = R.ext(f)
            sage: a = W(47); b = W(47 + 25)
            sage: a.is_equal_to(b)
            False
            sage: a.is_equal_to(b, 7)
            True"""
    @overload
    def is_zero(self, absprec=...) -> Any:
        """pAdicZZpXFMElement.is_zero(self, absprec=None)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_ZZ_pX_FM_element.pyx (starting at line 882)

        Return whether the valuation of ``self`` is at least
        ``absprec``; if ``absprec`` is ``None``, return whether
        ``self`` is indistinguishable from zero.

        EXAMPLES::

            sage: R = ZpFM(5,5)
            sage: S.<x> = R[]
            sage: f = x^5 + 75*x^3 - 15*x^2 + 125*x - 5
            sage: W.<w> = R.ext(f)
            sage: O(w^189).is_zero()
            True
            sage: W(0).is_zero()
            True
            sage: a = W(675)
            sage: a.is_zero()
            False
            sage: a.is_zero(7)
            True
            sage: a.is_zero(21)
            False"""
    @overload
    def is_zero(self) -> Any:
        """pAdicZZpXFMElement.is_zero(self, absprec=None)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_ZZ_pX_FM_element.pyx (starting at line 882)

        Return whether the valuation of ``self`` is at least
        ``absprec``; if ``absprec`` is ``None``, return whether
        ``self`` is indistinguishable from zero.

        EXAMPLES::

            sage: R = ZpFM(5,5)
            sage: S.<x> = R[]
            sage: f = x^5 + 75*x^3 - 15*x^2 + 125*x - 5
            sage: W.<w> = R.ext(f)
            sage: O(w^189).is_zero()
            True
            sage: W(0).is_zero()
            True
            sage: a = W(675)
            sage: a.is_zero()
            False
            sage: a.is_zero(7)
            True
            sage: a.is_zero(21)
            False"""
    @overload
    def is_zero(self) -> Any:
        """pAdicZZpXFMElement.is_zero(self, absprec=None)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_ZZ_pX_FM_element.pyx (starting at line 882)

        Return whether the valuation of ``self`` is at least
        ``absprec``; if ``absprec`` is ``None``, return whether
        ``self`` is indistinguishable from zero.

        EXAMPLES::

            sage: R = ZpFM(5,5)
            sage: S.<x> = R[]
            sage: f = x^5 + 75*x^3 - 15*x^2 + 125*x - 5
            sage: W.<w> = R.ext(f)
            sage: O(w^189).is_zero()
            True
            sage: W(0).is_zero()
            True
            sage: a = W(675)
            sage: a.is_zero()
            False
            sage: a.is_zero(7)
            True
            sage: a.is_zero(21)
            False"""
    @overload
    def is_zero(self) -> Any:
        """pAdicZZpXFMElement.is_zero(self, absprec=None)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_ZZ_pX_FM_element.pyx (starting at line 882)

        Return whether the valuation of ``self`` is at least
        ``absprec``; if ``absprec`` is ``None``, return whether
        ``self`` is indistinguishable from zero.

        EXAMPLES::

            sage: R = ZpFM(5,5)
            sage: S.<x> = R[]
            sage: f = x^5 + 75*x^3 - 15*x^2 + 125*x - 5
            sage: W.<w> = R.ext(f)
            sage: O(w^189).is_zero()
            True
            sage: W(0).is_zero()
            True
            sage: a = W(675)
            sage: a.is_zero()
            False
            sage: a.is_zero(7)
            True
            sage: a.is_zero(21)
            False"""
    def lift_to_precision(self, absprec=...) -> Any:
        """pAdicZZpXFMElement.lift_to_precision(self, absprec=None)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_ZZ_pX_FM_element.pyx (starting at line 1260)

        Return ``self``.

        EXAMPLES::

            sage: R = ZpFM(5,5)
            sage: S.<x> = R[]
            sage: f = x^5 + 75*x^3 - 15*x^2 + 125*x - 5
            sage: W.<w> = R.ext(f)
            sage: w.lift_to_precision(10000)
            w"""
    def matrix_mod_pn(self) -> Any:
        """pAdicZZpXFMElement.matrix_mod_pn(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_ZZ_pX_FM_element.pyx (starting at line 998)

        Return the matrix of right multiplication by the element on
        the power basis `1, x, x^2, \\ldots, x^{d-1}` for this
        extension field.

        The **rows** of this matrix give the images of each of the `x^i`.
        The entries of the matrices are ``IntegerMod`` elements,
        defined modulo ``p^(self.absprec() / e)``.

        Raises an error if ``self`` has negative valuation.

        EXAMPLES::

            sage: R = ZpFM(5,5)
            sage: S.<x> = R[]
            sage: f = x^5 + 75*x^3 - 15*x^2 + 125*x - 5
            sage: W.<w> = R.ext(f)
            sage: a = (3+w)^7
            sage: a.matrix_mod_pn()                                                     # needs sage.geometry.polyhedron
            [2757  333 1068  725 2510]
            [  50 1507  483  318  725]
            [ 500   50 3007 2358  318]
            [1590 1375 1695 1032 2358]
            [2415  590 2370 2970 1032]"""
    def norm(self, base=...) -> Any:
        """pAdicZZpXFMElement.norm(self, base=None)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_ZZ_pX_FM_element.pyx (starting at line 1060)

        Return the absolute or relative norm of this element.

        .. NOTE::

            This is not the `p`-adic absolute value.  This is a
            field theoretic norm down to a ground ring.

        If you want the `p`-adic absolute value, use the :func:`abs()`
        function instead.

        If `K` is given then `K` must be a subfield of the parent `L` of
        ``self``, in which case the norm is the relative norm from `L` to `K`.
        In all other cases, the norm is the absolute norm down to `\\QQ_p`
        or `\\ZZ_p`.

        EXAMPLES::

            sage: R = ZpCR(5,5)
            sage: S.<x> = R[]
            sage: f = x^5 + 75*x^3 - 15*x^2 + 125*x - 5
            sage: W.<w> = R.ext(f)
            sage: ((1+2*w)^5).norm()
            1 + 5^2 + O(5^5)
            sage: ((1+2*w)).norm()^5
            1 + 5^2 + O(5^5)"""
    @overload
    def polynomial(self, var=...) -> Any:
        """pAdicZZpXFMElement.polynomial(self, var='x')

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_ZZ_pX_FM_element.pyx (starting at line 1188)

        Return a polynomial over the base ring that yields this element
        when evaluated at the generator of the parent.

        INPUT:

        - ``var`` -- string, the variable name for the polynomial

        EXAMPLES::

            sage: S.<x> = ZZ[]
            sage: W.<w> = ZpFM(5).extension(x^2 - 5)
            sage: (w + 5).polynomial()
            x + 5"""
    @overload
    def polynomial(self) -> Any:
        """pAdicZZpXFMElement.polynomial(self, var='x')

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_ZZ_pX_FM_element.pyx (starting at line 1188)

        Return a polynomial over the base ring that yields this element
        when evaluated at the generator of the parent.

        INPUT:

        - ``var`` -- string, the variable name for the polynomial

        EXAMPLES::

            sage: S.<x> = ZZ[]
            sage: W.<w> = ZpFM(5).extension(x^2 - 5)
            sage: (w + 5).polynomial()
            x + 5"""
    @overload
    def precision_absolute(self) -> Any:
        """pAdicZZpXFMElement.precision_absolute(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_ZZ_pX_FM_element.pyx (starting at line 1543)

        Return the absolute precision of ``self``, ie the precision cap
        of ``self.parent()``.

        EXAMPLES::

            sage: R = ZpFM(5,5)
            sage: S.<x> = R[]
            sage: f = x^5 + 75*x^3 - 15*x^2 + 125*x - 5
            sage: W.<w> = R.ext(f)
            sage: a = W(75); a
            3*w^10 + 2*w^12 + w^14 + w^16 + w^17 + 3*w^18 + 3*w^19 + 2*w^21 + 3*w^22 + 3*w^23
            sage: a.valuation()
            10
            sage: a.precision_absolute()
            25
            sage: a.precision_relative()
            15
            sage: a.unit_part()
            3 + 2*w^2 + w^4 + w^6 + w^7 + 3*w^8 + 3*w^9 + 2*w^11 + 3*w^12
             + 3*w^13 + w^15 + 4*w^16 + 2*w^17 + w^18 + 3*w^21 + w^22 + 3*w^24"""
    @overload
    def precision_absolute(self) -> Any:
        """pAdicZZpXFMElement.precision_absolute(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_ZZ_pX_FM_element.pyx (starting at line 1543)

        Return the absolute precision of ``self``, ie the precision cap
        of ``self.parent()``.

        EXAMPLES::

            sage: R = ZpFM(5,5)
            sage: S.<x> = R[]
            sage: f = x^5 + 75*x^3 - 15*x^2 + 125*x - 5
            sage: W.<w> = R.ext(f)
            sage: a = W(75); a
            3*w^10 + 2*w^12 + w^14 + w^16 + w^17 + 3*w^18 + 3*w^19 + 2*w^21 + 3*w^22 + 3*w^23
            sage: a.valuation()
            10
            sage: a.precision_absolute()
            25
            sage: a.precision_relative()
            15
            sage: a.unit_part()
            3 + 2*w^2 + w^4 + w^6 + w^7 + 3*w^8 + 3*w^9 + 2*w^11 + 3*w^12
             + 3*w^13 + w^15 + 4*w^16 + 2*w^17 + w^18 + 3*w^21 + w^22 + 3*w^24"""
    @overload
    def precision_relative(self) -> Any:
        """pAdicZZpXFMElement.precision_relative(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_ZZ_pX_FM_element.pyx (starting at line 1570)

        Return the relative precision of ``self``, ie the precision cap
        of ``self.parent()`` minus the ``valuation of self``.

        EXAMPLES::

            sage: R = ZpFM(5,5)
            sage: S.<x> = R[]
            sage: f = x^5 + 75*x^3 - 15*x^2 + 125*x - 5
            sage: W.<w> = R.ext(f)
            sage: a = W(75); a
            3*w^10 + 2*w^12 + w^14 + w^16 + w^17 + 3*w^18 + 3*w^19 + 2*w^21 + 3*w^22 + 3*w^23
            sage: a.valuation()
            10
            sage: a.precision_absolute()
            25
            sage: a.precision_relative()
            15
            sage: a.unit_part()
            3 + 2*w^2 + w^4 + w^6 + w^7 + 3*w^8 + 3*w^9 + 2*w^11 + 3*w^12
             + 3*w^13 + w^15 + 4*w^16 + 2*w^17 + w^18 + 3*w^21 + w^22 + 3*w^24"""
    @overload
    def precision_relative(self) -> Any:
        """pAdicZZpXFMElement.precision_relative(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_ZZ_pX_FM_element.pyx (starting at line 1570)

        Return the relative precision of ``self``, ie the precision cap
        of ``self.parent()`` minus the ``valuation of self``.

        EXAMPLES::

            sage: R = ZpFM(5,5)
            sage: S.<x> = R[]
            sage: f = x^5 + 75*x^3 - 15*x^2 + 125*x - 5
            sage: W.<w> = R.ext(f)
            sage: a = W(75); a
            3*w^10 + 2*w^12 + w^14 + w^16 + w^17 + 3*w^18 + 3*w^19 + 2*w^21 + 3*w^22 + 3*w^23
            sage: a.valuation()
            10
            sage: a.precision_absolute()
            25
            sage: a.precision_relative()
            15
            sage: a.unit_part()
            3 + 2*w^2 + w^4 + w^6 + w^7 + 3*w^8 + 3*w^9 + 2*w^11 + 3*w^12
             + 3*w^13 + w^15 + 4*w^16 + 2*w^17 + w^18 + 3*w^21 + w^22 + 3*w^24"""
    def teichmuller_expansion(self, n=...) -> Any:
        """pAdicZZpXFMElement.teichmuller_expansion(self, n=None)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_ZZ_pX_FM_element.pyx (starting at line 1383)

        Return a list `[a_0, a_1, \\ldots, a_n]` such that.

        - `a_i^q = a_i`
        - ``self.unit_part()`` = `\\sum_{i = 0}^n a_i \\pi^i`, where `\\pi` is a
          uniformizer of ``self.parent()``

        INPUT:

        - ``n`` -- integer (default: ``None``); if given, returns the corresponding
          entry in the expansion

        EXAMPLES::

            sage: # needs sage.libs.flint
            sage: R.<a> = ZqFM(5^4,4)
            sage: E = a.teichmuller_expansion(); E
            5-adic expansion of a (teichmuller)
            sage: list(E)
            [a + (2*a^3 + 2*a^2 + 3*a + 4)*5 + (4*a^3 + 3*a^2 + 3*a + 2)*5^2 + (4*a^2 + 2*a + 2)*5^3,
             (3*a^3 + 3*a^2 + 2*a + 1) + (a^3 + 4*a^2 + 1)*5 + (a^2 + 4*a + 4)*5^2 + (4*a^2 + a + 3)*5^3,
             (4*a^3 + 2*a^2 + a + 1) + (2*a^3 + 2*a^2 + 2*a + 4)*5 + (3*a^3 + 2*a^2 + a + 1)*5^2 + (a^3 + a^2 + 2)*5^3,
             (a^3 + a^2 + a + 4) + (3*a^3 + 1)*5 + (3*a^3 + a + 2)*5^2 + (3*a^3 + 3*a^2 + 3*a + 1)*5^3]
            sage: sum([c * 5^i for i, c in enumerate(E)])
            a
            sage: all(c^625 == c for c in E)
            True

            sage: S.<x> = ZZ[]
            sage: f = x^3 - 98*x + 7
            sage: W.<w> = ZpFM(7,3).ext(f)
            sage: b = (1+w)^5; L = b.teichmuller_expansion(); L
            [1,
             5 + 5*w^3 + w^6 + 4*w^7,
             3 + 3*w^3 + w^7,
             3 + 3*w^3 + w^7,
             0,
             4 + 5*w^3 + w^6 + 4*w^7,
             3 + 3*w^3 + w^7,
             6 + w^3 + 5*w^7,
             6 + w^3 + 5*w^7]
            sage: sum([w^i*L[i] for i in range(len(L))]) == b
            True
            sage: all(L[i]^(7^3) == L[i] for i in range(9))
            True

            sage: L = W(3).teichmuller_expansion(); L
            [3 + 3*w^3 + w^7,
             0,
             0,
             4 + 5*w^3 + w^6 + 4*w^7,
             0,
             0,
             3 + 3*w^3 + w^7,
             6 + w^3 + 5*w^7]
            sage: sum([w^i*L[i] for i in range(len(L))])
            3"""
    def trace(self, base=...) -> Any:
        """pAdicZZpXFMElement.trace(self, base=None)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_ZZ_pX_FM_element.pyx (starting at line 1100)

        Return the absolute or relative trace of this element.

        If `K` is given then `K` must be a subfield of the parent `L` of
        ``self``, in which case the norm is the relative norm from `L` to `K`.
        In all other cases, the norm is the absolute norm down to `\\QQ_p`
        or `\\ZZ_p`.

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
            4*5 + 5^2 + 5^3 + 2*5^4 + O(5^5)"""
    @overload
    def unit_part(self) -> pAdicZZpXFMElement:
        """pAdicZZpXFMElement.unit_part(self) -> pAdicZZpXFMElement

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_ZZ_pX_FM_element.pyx (starting at line 1597)

        Return the unit part of ``self``, ie
        ``self / uniformizer^(self.valuation())``

        .. WARNING::

            If this element has positive valuation then the unit part
            is not defined to the full precision of the ring.  Asking
            for the unit part of ``ZpFM(5)(0)`` will not raise an error,
            but rather return itself.

        EXAMPLES::

            sage: R = ZpFM(5,5)
            sage: S.<x> = R[]
            sage: f = x^5 + 75*x^3 - 15*x^2 + 125*x - 5
            sage: W.<w> = R.ext(f)
            sage: a = W(75); a
            3*w^10 + 2*w^12 + w^14 + w^16 + w^17 + 3*w^18 + 3*w^19 + 2*w^21 + 3*w^22 + 3*w^23
            sage: a.valuation()
            10
            sage: a.precision_absolute()
            25
            sage: a.precision_relative()
            15
            sage: a.unit_part()
            3 + 2*w^2 + w^4 + w^6 + w^7 + 3*w^8 + 3*w^9 + 2*w^11 + 3*w^12
             + 3*w^13 + w^15 + 4*w^16 + 2*w^17 + w^18 + 3*w^21 + w^22 + 3*w^24

        The unit part inserts nonsense digits if this element has
        positive valuation::

            sage: (a-a).unit_part()
            0"""
    @overload
    def unit_part(self) -> Any:
        """pAdicZZpXFMElement.unit_part(self) -> pAdicZZpXFMElement

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_ZZ_pX_FM_element.pyx (starting at line 1597)

        Return the unit part of ``self``, ie
        ``self / uniformizer^(self.valuation())``

        .. WARNING::

            If this element has positive valuation then the unit part
            is not defined to the full precision of the ring.  Asking
            for the unit part of ``ZpFM(5)(0)`` will not raise an error,
            but rather return itself.

        EXAMPLES::

            sage: R = ZpFM(5,5)
            sage: S.<x> = R[]
            sage: f = x^5 + 75*x^3 - 15*x^2 + 125*x - 5
            sage: W.<w> = R.ext(f)
            sage: a = W(75); a
            3*w^10 + 2*w^12 + w^14 + w^16 + w^17 + 3*w^18 + 3*w^19 + 2*w^21 + 3*w^22 + 3*w^23
            sage: a.valuation()
            10
            sage: a.precision_absolute()
            25
            sage: a.precision_relative()
            15
            sage: a.unit_part()
            3 + 2*w^2 + w^4 + w^6 + w^7 + 3*w^8 + 3*w^9 + 2*w^11 + 3*w^12
             + 3*w^13 + w^15 + 4*w^16 + 2*w^17 + w^18 + 3*w^21 + w^22 + 3*w^24

        The unit part inserts nonsense digits if this element has
        positive valuation::

            sage: (a-a).unit_part()
            0"""
    @overload
    def unit_part(self) -> Any:
        """pAdicZZpXFMElement.unit_part(self) -> pAdicZZpXFMElement

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_ZZ_pX_FM_element.pyx (starting at line 1597)

        Return the unit part of ``self``, ie
        ``self / uniformizer^(self.valuation())``

        .. WARNING::

            If this element has positive valuation then the unit part
            is not defined to the full precision of the ring.  Asking
            for the unit part of ``ZpFM(5)(0)`` will not raise an error,
            but rather return itself.

        EXAMPLES::

            sage: R = ZpFM(5,5)
            sage: S.<x> = R[]
            sage: f = x^5 + 75*x^3 - 15*x^2 + 125*x - 5
            sage: W.<w> = R.ext(f)
            sage: a = W(75); a
            3*w^10 + 2*w^12 + w^14 + w^16 + w^17 + 3*w^18 + 3*w^19 + 2*w^21 + 3*w^22 + 3*w^23
            sage: a.valuation()
            10
            sage: a.precision_absolute()
            25
            sage: a.precision_relative()
            15
            sage: a.unit_part()
            3 + 2*w^2 + w^4 + w^6 + w^7 + 3*w^8 + 3*w^9 + 2*w^11 + 3*w^12
             + 3*w^13 + w^15 + 4*w^16 + 2*w^17 + w^18 + 3*w^21 + w^22 + 3*w^24

        The unit part inserts nonsense digits if this element has
        positive valuation::

            sage: (a-a).unit_part()
            0"""
    def __copy__(self) -> Any:
        """pAdicZZpXFMElement.__copy__(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_ZZ_pX_FM_element.pyx (starting at line 859)

        Return a copy of ``self``.

        EXAMPLES::

            sage: R = ZpFM(5,5)
            sage: S.<x> = R[]
            sage: f = x^5 + 75*x^3 - 15*x^2 + 125*x - 5
            sage: W.<w> = R.ext(f)
            sage: b = W(45); b
            4*w^5 + 3*w^7 + w^9 + w^10 + 2*w^11 + w^12 + w^13 + 3*w^14 + w^16
             + 2*w^17 + w^19 + 4*w^20 + w^21 + 3*w^22 + 3*w^23 + 4*w^24
            sage: c = copy(b); c
            4*w^5 + 3*w^7 + w^9 + w^10 + 2*w^11 + w^12 + w^13 + 3*w^14 + w^16
             + 2*w^17 + w^19 + 4*w^20 + w^21 + 3*w^22 + 3*w^23 + 4*w^24
            sage: c is b
            False"""
    def __invert__(self) -> Any:
        """pAdicZZpXFMElement.__invert__(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_ZZ_pX_FM_element.pyx (starting at line 475)

        Return the inverse of ``self``, as long as ``self`` is a unit.

        If ``self`` is not a unit, raises a :exc:`ValueError`.

        EXAMPLES::

            sage: R = ZpFM(5,5)
            sage: S.<x> = R[]
            sage: f = x^5 + 75*x^3 - 15*x^2 + 125*x - 5
            sage: W.<w> = R.ext(f)
            sage: z = (1 + w)^5
            sage: y = ~z; y  # indirect doctest
            1 + 4*w^5 + 4*w^6 + 3*w^7 + w^8 + 2*w^10 + w^11 + w^12 + 2*w^14 + 3*w^16
             + 3*w^17 + 4*w^18 + 4*w^19 + 2*w^20 + 2*w^21 + 4*w^22 + 3*w^23 + 3*w^24
            sage: y.parent()
            5-adic Eisenstein Extension Ring in w defined by x^5 + 75*x^3 - 15*x^2 + 125*x - 5
            sage: z = z - 1
            sage: ~z
            Traceback (most recent call last):
            ...
            ValueError: cannot invert non-unit"""
    def __lshift__(self, pAdicZZpXFMElementself, shift) -> Any:
        """pAdicZZpXFMElement.__lshift__(pAdicZZpXFMElement self, shift)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_ZZ_pX_FM_element.pyx (starting at line 542)

        Multiply ``self`` by the uniformizer raised to the power ``n``.

        If ``n`` is negative, right shifts by ``-n``.

        EXAMPLES::

            sage: R = ZpFM(5,5)
            sage: S.<x> = R[]
            sage: f = x^5 + 75*x^3 - 15*x^2 + 125*x - 5
            sage: W.<w> = R.ext(f)
            sage: z = (1 + w)^5
            sage: z
            1 + w^5 + w^6 + 2*w^7 + 4*w^8 + 3*w^10 + w^12 + 4*w^13 + 4*w^14 + 4*w^15 + 4*w^16 + 4*w^17 + 4*w^20 + w^21 + 4*w^24
            sage: z << 17  # indirect doctest
            w^17 + w^22 + w^23 + 2*w^24
            sage: z << (-1)
            w^4 + w^5 + 2*w^6 + 4*w^7 + 3*w^9 + w^11 + 4*w^12 + 4*w^13 + 4*w^14 + 4*w^15 + 4*w^16 + 4*w^19 + w^20 + 4*w^23 + 4*w^24"""
    def __pow__(self, pAdicZZpXFMElementself, right, m) -> Any:
        """pAdicZZpXFMElement.__pow__(pAdicZZpXFMElement self, right, m)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_ZZ_pX_FM_element.pyx (starting at line 687)

        Compute ``self`` ^ ``right``.

        EXAMPLES::

            sage: R = ZpFM(5,5)
            sage: S.<x> = R[]
            sage: f = x^5 + 75*x^3 - 15*x^2 + 125*x - 5
            sage: W.<w> = R.ext(f)
            sage: (1 + w)^5  # indirect doctest
            1 + w^5 + w^6 + 2*w^7 + 4*w^8 + 3*w^10 + w^12 + 4*w^13 + 4*w^14
             + 4*w^15 + 4*w^16 + 4*w^17 + 4*w^20 + w^21 + 4*w^24
            sage: (1 + w)^-5
            1 + 4*w^5 + 4*w^6 + 3*w^7 + w^8 + 2*w^10 + w^11 + w^12 + 2*w^14
             + 3*w^16 + 3*w^17 + 4*w^18 + 4*w^19 + 2*w^20 + 2*w^21 + 4*w^22 + 3*w^23 + 3*w^24

        TESTS:

        We define ``0^0`` to be unity, :issue:`13786`::

            sage: R = ZpFM(5,5)
            sage: S.<x> = R[]
            sage: f = x^5 + 75*x^3 - 15*x^2 + 125*x - 5
            sage: W.<w> = R.ext(f)
            sage: type(W(0))
            <class 'sage.rings.padics.padic_ZZ_pX_FM_element.pAdicZZpXFMElement'>
            sage: W(0)^0
            1
            sage: W(0)^0 == W(1)
            True

        The value returned from ``0^0`` should belong to our ring::

            sage: R = ZpFM(5,5)
            sage: S.<x> = R[]
            sage: f = x^5 + 75*x^3 - 15*x^2 + 125*x - 5
            sage: W.<w> = R.ext(f)
            sage: type(W(0)^0) == type(W(0))
            True"""
    def __reduce__(self) -> Any:
        """pAdicZZpXFMElement.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_ZZ_pX_FM_element.pyx (starting at line 401)

        Pickle ``self``.

        EXAMPLES::

            sage: R = ZpFM(5,5)
            sage: S.<x> = R[]
            sage: f = x^5 + 75*x^3 - 15*x^2 + 125*x - 5
            sage: W.<w> = R.ext(f)
            sage: z = (1 + w)^5 - 1
            sage: loads(dumps(z)) == z  # indirect doctest
            True"""
    def __rlshift__(self, other):
        """Return value<<self."""
    def __rpow__(self, other):
        """Return pow(value, self, mod)."""
    def __rrshift__(self, other):
        """Return value>>self."""
    def __rshift__(self, pAdicZZpXFMElementself, shift) -> Any:
        """pAdicZZpXFMElement.__rshift__(pAdicZZpXFMElement self, shift)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_ZZ_pX_FM_element.pyx (starting at line 629)

        Divide ``self`` by the uniformizer raised to the power ``n``.

        Throws away the nonpositive part of the series expansion.
        The top digits will be garbage.  If ``n`` is negative, left
        shifts by ``-n``.

        EXAMPLES::

            sage: R = ZpFM(5,5)
            sage: S.<x> = R[]
            sage: f = x^5 + 75*x^3 - 15*x^2 + 125*x - 5
            sage: W.<w> = R.ext(f)
            sage: z = (1 + w)^5
            sage: z
            1 + w^5 + w^6 + 2*w^7 + 4*w^8 + 3*w^10 + w^12 + 4*w^13 + 4*w^14
             + 4*w^15 + 4*w^16 + 4*w^17 + 4*w^20 + w^21 + 4*w^24
            sage: z >> (6)  # indirect doctest
            1 + 2*w + 4*w^2 + 3*w^4 + w^6 + 4*w^7 + 4*w^8 + 4*w^9 + 4*w^10 + 4*w^11
             + 4*w^14 + w^15 + 4*w^18 + 4*w^19 + 2*w^20 + 3*w^21 + 2*w^22 + 3*w^24
            sage: z >> (-4)
            w^4 + w^9 + w^10 + 2*w^11 + 4*w^12 + 3*w^14 + w^16 + 4*w^17
             + 4*w^18 + 4*w^19 + 4*w^20 + 4*w^21 + 4*w^24"""
