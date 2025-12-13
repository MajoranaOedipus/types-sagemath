import _cython_3_2_1
import sage.rings.padics.padic_ZZ_pX_element
from sage.interfaces.abc import GpElement as GpElement
from sage.rings.finite_rings.integer_mod import IntegerMod_abstract as IntegerMod_abstract
from sage.rings.finite_rings.integer_mod_ring import IntegerModRing as IntegerModRing
from sage.rings.padics.precision_error import PrecisionError as PrecisionError
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from typing import Any, ClassVar, overload

make_ZZpXCRElement: _cython_3_2_1.cython_function_or_method

class pAdicZZpXCRElement(sage.rings.padics.padic_ZZ_pX_element.pAdicZZpXElement):
    """pAdicZZpXCRElement(parent, x, absprec=infinity, relprec=infinity, empty=False)"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, parent, x, absprec=..., relprec=..., empty=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/padics/padic_ZZ_pX_CR_element.pyx (starting at line 226)

                Create an element of a capped relative precision, unramified
                or Eisenstein extension of `\\ZZ_p` or `\\QQ_p`.

                INPUT:

                - ``parent`` -- either an ``EisensteinRingCappedRelative`` or
                  ``UnramifiedRingCappedRelative``

                - ``x`` -- integer; rational, `p`-adic element, polynomial,
                  list, integer_mod, pari int/frac/poly_t/pol_mod, an
                  ``ntl_ZZ_pX``, an ``ntl_ZZ``, an ``ntl_ZZ_p``, an
                  ``ntl_ZZX``, or something convertible into parent.residue_field()

                - ``absprec`` -- an upper bound on the absolute precision of the
                  element created

                - ``relprec`` -- an upper bound on the relative precision of
                  the element created

                - ``empty`` -- whether to return after initializing to zero
                  (without setting the valuation)

                EXAMPLES::

                    sage: R = Zp(5,5)
                    sage: S.<x> = R[]
                    sage: f = x^5 + 75*x^3 - 15*x^2 + 125*x - 5
                    sage: W.<w> = R.ext(f)
                    sage: z = (1+w)^5; z  # indirect doctest
                    1 + w^5 + w^6 + 2*w^7 + 4*w^8 + 3*w^10 + w^12 + 4*w^13 + 4*w^14 + 4*w^15 + 4*w^16 + 4*w^17 + 4*w^20 + w^21 + 4*w^24 + O(w^25)
                    sage: W(pari('3 + O(5^3)'))
                    3 + O(w^15)
                    sage: W(R(3,3))
                    3 + O(w^15)
                    sage: W.<w> = R.ext(x^625 + 915*x^17 - 95)
                    sage: W(3)
                    3 + O(w^3125)
                    sage: W(w, 14)
                    w + O(w^14)

                TESTS:

                Check that :issue:`3865` is fixed::

                    sage: W(gp('3 + O(5^10)'))
                    3 + O(w^3125)


                Check that :issue:`13612` has been fixed::

                    sage: R = Zp(3)
                    sage: S.<a> = R[]
                    sage: W.<a> = R.extension(a^2 + 1)
                    sage: W(W.residue_field().zero())
                    O(3)

                    sage: K = Qp(3)
                    sage: S.<a> = K[]
                    sage: L.<a> = K.extension(a^2 + 1)
                    sage: L(L.residue_field().zero())
                    O(3)
        """
    @overload
    def expansion(self, n=..., lift_mode=...) -> Any:
        """pAdicZZpXCRElement.expansion(self, n=None, lift_mode='simple')

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_ZZ_pX_CR_element.pyx (starting at line 2710)

        Return a list giving a series representation of ``self``.

        - If ``lift_mode == 'simple'`` or ``'smallest'``, the returned
          list will consist of integers (in the Eisenstein case) or a
          list of lists of integers (in the unramified case).  ``self``
          can be reconstructed as a sum of elements of the list times
          powers of the uniformiser (in the Eisenstein case), or as a
          sum of powers of the `p` times polynomials in the generator
          (in the unramified case).

          + If ``lift_mode == 'simple'``, all integers will be in the interval
            `[0,p-1]`.

          + If ``lift_mode == 'smallest'`` they will be in the
            interval `[(1-p)/2, p/2]`.

        - If ``lift_mode == 'teichmuller'``, returns a list of
          ``pAdicZZpXCRElements``, all of which are Teichmuller
          representatives and such that ``self`` is the sum of that list
          times powers of the uniformizer.

        Note that zeros are truncated from the returned list if
        ``self.parent()`` is a field, so you must use the
        ``valuation`` function to fully reconstruct ``self``.

        INPUT:

        - ``n`` -- integer (default: ``None``); if given, returns the
          corresponding entry in the expansion

        EXAMPLES::

            sage: R = Zp(5,5)
            sage: S.<x> = R[]
            sage: f = x^5 + 75*x^3 - 15*x^2 + 125*x - 5
            sage: W.<w> = R.ext(f)
            sage: y = W(775, 19); y
            w^10 + 4*w^12 + 2*w^14 + w^15 + 2*w^16 + 4*w^17 + w^18 + O(w^19)
            sage: (y>>9).expansion()
            [0, 1, 0, 4, 0, 2, 1, 2, 4, 1]
            sage: (y>>9).expansion(lift_mode='smallest')
            [0, 1, 0, -1, 0, 2, 1, 2, 0, 1]
            sage: w^10 - w^12 + 2*w^14 + w^15 + 2*w^16 + w^18 + O(w^19)
            w^10 + 4*w^12 + 2*w^14 + w^15 + 2*w^16 + 4*w^17 + w^18 + O(w^19)
            sage: g = x^3 + 3*x + 3
            sage: A.<a> = R.ext(g)
            sage: y = 75 + 45*a + 1200*a^2; y
            4*a*5 + (3*a^2 + a + 3)*5^2 + 4*a^2*5^3 + a^2*5^4 + O(5^6)
            sage: E = y.expansion(); E
            5-adic expansion of 4*a*5 + (3*a^2 + a + 3)*5^2 + 4*a^2*5^3 + a^2*5^4 + O(5^6)
            sage: list(E)
            [[], [0, 4], [3, 1, 3], [0, 0, 4], [0, 0, 1], []]
            sage: list(y.expansion(lift_mode='smallest'))
            [[], [0, -1], [-2, 2, -2], [1], [0, 0, 2], []]
            sage: 5*((-2*5 + 25) + (-1 + 2*5)*a + (-2*5 + 2*125)*a^2)
            4*a*5 + (3*a^2 + a + 3)*5^2 + 4*a^2*5^3 + a^2*5^4 + O(5^6)
            sage: list(W(0).expansion())
            []
            sage: list(W(0,4).expansion())
            []
            sage: list(A(0,4).expansion())
            []

        TESTS:

        We check that :issue:`24949` is fixed::

            sage: R = Zp(2)
            sage: S.<x> = R[]
            sage: A.<a> = R.extension(x^10 + 2)
            sage: u = a^4 + a^5
            sage: v = a^2 + a^3
            sage: w = u - v^2
            sage: w.expansion(4)
            0"""
    @overload
    def expansion(self) -> Any:
        """pAdicZZpXCRElement.expansion(self, n=None, lift_mode='simple')

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_ZZ_pX_CR_element.pyx (starting at line 2710)

        Return a list giving a series representation of ``self``.

        - If ``lift_mode == 'simple'`` or ``'smallest'``, the returned
          list will consist of integers (in the Eisenstein case) or a
          list of lists of integers (in the unramified case).  ``self``
          can be reconstructed as a sum of elements of the list times
          powers of the uniformiser (in the Eisenstein case), or as a
          sum of powers of the `p` times polynomials in the generator
          (in the unramified case).

          + If ``lift_mode == 'simple'``, all integers will be in the interval
            `[0,p-1]`.

          + If ``lift_mode == 'smallest'`` they will be in the
            interval `[(1-p)/2, p/2]`.

        - If ``lift_mode == 'teichmuller'``, returns a list of
          ``pAdicZZpXCRElements``, all of which are Teichmuller
          representatives and such that ``self`` is the sum of that list
          times powers of the uniformizer.

        Note that zeros are truncated from the returned list if
        ``self.parent()`` is a field, so you must use the
        ``valuation`` function to fully reconstruct ``self``.

        INPUT:

        - ``n`` -- integer (default: ``None``); if given, returns the
          corresponding entry in the expansion

        EXAMPLES::

            sage: R = Zp(5,5)
            sage: S.<x> = R[]
            sage: f = x^5 + 75*x^3 - 15*x^2 + 125*x - 5
            sage: W.<w> = R.ext(f)
            sage: y = W(775, 19); y
            w^10 + 4*w^12 + 2*w^14 + w^15 + 2*w^16 + 4*w^17 + w^18 + O(w^19)
            sage: (y>>9).expansion()
            [0, 1, 0, 4, 0, 2, 1, 2, 4, 1]
            sage: (y>>9).expansion(lift_mode='smallest')
            [0, 1, 0, -1, 0, 2, 1, 2, 0, 1]
            sage: w^10 - w^12 + 2*w^14 + w^15 + 2*w^16 + w^18 + O(w^19)
            w^10 + 4*w^12 + 2*w^14 + w^15 + 2*w^16 + 4*w^17 + w^18 + O(w^19)
            sage: g = x^3 + 3*x + 3
            sage: A.<a> = R.ext(g)
            sage: y = 75 + 45*a + 1200*a^2; y
            4*a*5 + (3*a^2 + a + 3)*5^2 + 4*a^2*5^3 + a^2*5^4 + O(5^6)
            sage: E = y.expansion(); E
            5-adic expansion of 4*a*5 + (3*a^2 + a + 3)*5^2 + 4*a^2*5^3 + a^2*5^4 + O(5^6)
            sage: list(E)
            [[], [0, 4], [3, 1, 3], [0, 0, 4], [0, 0, 1], []]
            sage: list(y.expansion(lift_mode='smallest'))
            [[], [0, -1], [-2, 2, -2], [1], [0, 0, 2], []]
            sage: 5*((-2*5 + 25) + (-1 + 2*5)*a + (-2*5 + 2*125)*a^2)
            4*a*5 + (3*a^2 + a + 3)*5^2 + 4*a^2*5^3 + a^2*5^4 + O(5^6)
            sage: list(W(0).expansion())
            []
            sage: list(W(0,4).expansion())
            []
            sage: list(A(0,4).expansion())
            []

        TESTS:

        We check that :issue:`24949` is fixed::

            sage: R = Zp(2)
            sage: S.<x> = R[]
            sage: A.<a> = R.extension(x^10 + 2)
            sage: u = a^4 + a^5
            sage: v = a^2 + a^3
            sage: w = u - v^2
            sage: w.expansion(4)
            0"""
    @overload
    def expansion(self, lift_mode=...) -> Any:
        """pAdicZZpXCRElement.expansion(self, n=None, lift_mode='simple')

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_ZZ_pX_CR_element.pyx (starting at line 2710)

        Return a list giving a series representation of ``self``.

        - If ``lift_mode == 'simple'`` or ``'smallest'``, the returned
          list will consist of integers (in the Eisenstein case) or a
          list of lists of integers (in the unramified case).  ``self``
          can be reconstructed as a sum of elements of the list times
          powers of the uniformiser (in the Eisenstein case), or as a
          sum of powers of the `p` times polynomials in the generator
          (in the unramified case).

          + If ``lift_mode == 'simple'``, all integers will be in the interval
            `[0,p-1]`.

          + If ``lift_mode == 'smallest'`` they will be in the
            interval `[(1-p)/2, p/2]`.

        - If ``lift_mode == 'teichmuller'``, returns a list of
          ``pAdicZZpXCRElements``, all of which are Teichmuller
          representatives and such that ``self`` is the sum of that list
          times powers of the uniformizer.

        Note that zeros are truncated from the returned list if
        ``self.parent()`` is a field, so you must use the
        ``valuation`` function to fully reconstruct ``self``.

        INPUT:

        - ``n`` -- integer (default: ``None``); if given, returns the
          corresponding entry in the expansion

        EXAMPLES::

            sage: R = Zp(5,5)
            sage: S.<x> = R[]
            sage: f = x^5 + 75*x^3 - 15*x^2 + 125*x - 5
            sage: W.<w> = R.ext(f)
            sage: y = W(775, 19); y
            w^10 + 4*w^12 + 2*w^14 + w^15 + 2*w^16 + 4*w^17 + w^18 + O(w^19)
            sage: (y>>9).expansion()
            [0, 1, 0, 4, 0, 2, 1, 2, 4, 1]
            sage: (y>>9).expansion(lift_mode='smallest')
            [0, 1, 0, -1, 0, 2, 1, 2, 0, 1]
            sage: w^10 - w^12 + 2*w^14 + w^15 + 2*w^16 + w^18 + O(w^19)
            w^10 + 4*w^12 + 2*w^14 + w^15 + 2*w^16 + 4*w^17 + w^18 + O(w^19)
            sage: g = x^3 + 3*x + 3
            sage: A.<a> = R.ext(g)
            sage: y = 75 + 45*a + 1200*a^2; y
            4*a*5 + (3*a^2 + a + 3)*5^2 + 4*a^2*5^3 + a^2*5^4 + O(5^6)
            sage: E = y.expansion(); E
            5-adic expansion of 4*a*5 + (3*a^2 + a + 3)*5^2 + 4*a^2*5^3 + a^2*5^4 + O(5^6)
            sage: list(E)
            [[], [0, 4], [3, 1, 3], [0, 0, 4], [0, 0, 1], []]
            sage: list(y.expansion(lift_mode='smallest'))
            [[], [0, -1], [-2, 2, -2], [1], [0, 0, 2], []]
            sage: 5*((-2*5 + 25) + (-1 + 2*5)*a + (-2*5 + 2*125)*a^2)
            4*a*5 + (3*a^2 + a + 3)*5^2 + 4*a^2*5^3 + a^2*5^4 + O(5^6)
            sage: list(W(0).expansion())
            []
            sage: list(W(0,4).expansion())
            []
            sage: list(A(0,4).expansion())
            []

        TESTS:

        We check that :issue:`24949` is fixed::

            sage: R = Zp(2)
            sage: S.<x> = R[]
            sage: A.<a> = R.extension(x^10 + 2)
            sage: u = a^4 + a^5
            sage: v = a^2 + a^3
            sage: w = u - v^2
            sage: w.expansion(4)
            0"""
    @overload
    def expansion(self) -> Any:
        """pAdicZZpXCRElement.expansion(self, n=None, lift_mode='simple')

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_ZZ_pX_CR_element.pyx (starting at line 2710)

        Return a list giving a series representation of ``self``.

        - If ``lift_mode == 'simple'`` or ``'smallest'``, the returned
          list will consist of integers (in the Eisenstein case) or a
          list of lists of integers (in the unramified case).  ``self``
          can be reconstructed as a sum of elements of the list times
          powers of the uniformiser (in the Eisenstein case), or as a
          sum of powers of the `p` times polynomials in the generator
          (in the unramified case).

          + If ``lift_mode == 'simple'``, all integers will be in the interval
            `[0,p-1]`.

          + If ``lift_mode == 'smallest'`` they will be in the
            interval `[(1-p)/2, p/2]`.

        - If ``lift_mode == 'teichmuller'``, returns a list of
          ``pAdicZZpXCRElements``, all of which are Teichmuller
          representatives and such that ``self`` is the sum of that list
          times powers of the uniformizer.

        Note that zeros are truncated from the returned list if
        ``self.parent()`` is a field, so you must use the
        ``valuation`` function to fully reconstruct ``self``.

        INPUT:

        - ``n`` -- integer (default: ``None``); if given, returns the
          corresponding entry in the expansion

        EXAMPLES::

            sage: R = Zp(5,5)
            sage: S.<x> = R[]
            sage: f = x^5 + 75*x^3 - 15*x^2 + 125*x - 5
            sage: W.<w> = R.ext(f)
            sage: y = W(775, 19); y
            w^10 + 4*w^12 + 2*w^14 + w^15 + 2*w^16 + 4*w^17 + w^18 + O(w^19)
            sage: (y>>9).expansion()
            [0, 1, 0, 4, 0, 2, 1, 2, 4, 1]
            sage: (y>>9).expansion(lift_mode='smallest')
            [0, 1, 0, -1, 0, 2, 1, 2, 0, 1]
            sage: w^10 - w^12 + 2*w^14 + w^15 + 2*w^16 + w^18 + O(w^19)
            w^10 + 4*w^12 + 2*w^14 + w^15 + 2*w^16 + 4*w^17 + w^18 + O(w^19)
            sage: g = x^3 + 3*x + 3
            sage: A.<a> = R.ext(g)
            sage: y = 75 + 45*a + 1200*a^2; y
            4*a*5 + (3*a^2 + a + 3)*5^2 + 4*a^2*5^3 + a^2*5^4 + O(5^6)
            sage: E = y.expansion(); E
            5-adic expansion of 4*a*5 + (3*a^2 + a + 3)*5^2 + 4*a^2*5^3 + a^2*5^4 + O(5^6)
            sage: list(E)
            [[], [0, 4], [3, 1, 3], [0, 0, 4], [0, 0, 1], []]
            sage: list(y.expansion(lift_mode='smallest'))
            [[], [0, -1], [-2, 2, -2], [1], [0, 0, 2], []]
            sage: 5*((-2*5 + 25) + (-1 + 2*5)*a + (-2*5 + 2*125)*a^2)
            4*a*5 + (3*a^2 + a + 3)*5^2 + 4*a^2*5^3 + a^2*5^4 + O(5^6)
            sage: list(W(0).expansion())
            []
            sage: list(W(0,4).expansion())
            []
            sage: list(A(0,4).expansion())
            []

        TESTS:

        We check that :issue:`24949` is fixed::

            sage: R = Zp(2)
            sage: S.<x> = R[]
            sage: A.<a> = R.extension(x^10 + 2)
            sage: u = a^4 + a^5
            sage: v = a^2 + a^3
            sage: w = u - v^2
            sage: w.expansion(4)
            0"""
    @overload
    def expansion(self, lift_mode=...) -> Any:
        """pAdicZZpXCRElement.expansion(self, n=None, lift_mode='simple')

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_ZZ_pX_CR_element.pyx (starting at line 2710)

        Return a list giving a series representation of ``self``.

        - If ``lift_mode == 'simple'`` or ``'smallest'``, the returned
          list will consist of integers (in the Eisenstein case) or a
          list of lists of integers (in the unramified case).  ``self``
          can be reconstructed as a sum of elements of the list times
          powers of the uniformiser (in the Eisenstein case), or as a
          sum of powers of the `p` times polynomials in the generator
          (in the unramified case).

          + If ``lift_mode == 'simple'``, all integers will be in the interval
            `[0,p-1]`.

          + If ``lift_mode == 'smallest'`` they will be in the
            interval `[(1-p)/2, p/2]`.

        - If ``lift_mode == 'teichmuller'``, returns a list of
          ``pAdicZZpXCRElements``, all of which are Teichmuller
          representatives and such that ``self`` is the sum of that list
          times powers of the uniformizer.

        Note that zeros are truncated from the returned list if
        ``self.parent()`` is a field, so you must use the
        ``valuation`` function to fully reconstruct ``self``.

        INPUT:

        - ``n`` -- integer (default: ``None``); if given, returns the
          corresponding entry in the expansion

        EXAMPLES::

            sage: R = Zp(5,5)
            sage: S.<x> = R[]
            sage: f = x^5 + 75*x^3 - 15*x^2 + 125*x - 5
            sage: W.<w> = R.ext(f)
            sage: y = W(775, 19); y
            w^10 + 4*w^12 + 2*w^14 + w^15 + 2*w^16 + 4*w^17 + w^18 + O(w^19)
            sage: (y>>9).expansion()
            [0, 1, 0, 4, 0, 2, 1, 2, 4, 1]
            sage: (y>>9).expansion(lift_mode='smallest')
            [0, 1, 0, -1, 0, 2, 1, 2, 0, 1]
            sage: w^10 - w^12 + 2*w^14 + w^15 + 2*w^16 + w^18 + O(w^19)
            w^10 + 4*w^12 + 2*w^14 + w^15 + 2*w^16 + 4*w^17 + w^18 + O(w^19)
            sage: g = x^3 + 3*x + 3
            sage: A.<a> = R.ext(g)
            sage: y = 75 + 45*a + 1200*a^2; y
            4*a*5 + (3*a^2 + a + 3)*5^2 + 4*a^2*5^3 + a^2*5^4 + O(5^6)
            sage: E = y.expansion(); E
            5-adic expansion of 4*a*5 + (3*a^2 + a + 3)*5^2 + 4*a^2*5^3 + a^2*5^4 + O(5^6)
            sage: list(E)
            [[], [0, 4], [3, 1, 3], [0, 0, 4], [0, 0, 1], []]
            sage: list(y.expansion(lift_mode='smallest'))
            [[], [0, -1], [-2, 2, -2], [1], [0, 0, 2], []]
            sage: 5*((-2*5 + 25) + (-1 + 2*5)*a + (-2*5 + 2*125)*a^2)
            4*a*5 + (3*a^2 + a + 3)*5^2 + 4*a^2*5^3 + a^2*5^4 + O(5^6)
            sage: list(W(0).expansion())
            []
            sage: list(W(0,4).expansion())
            []
            sage: list(A(0,4).expansion())
            []

        TESTS:

        We check that :issue:`24949` is fixed::

            sage: R = Zp(2)
            sage: S.<x> = R[]
            sage: A.<a> = R.extension(x^10 + 2)
            sage: u = a^4 + a^5
            sage: v = a^2 + a^3
            sage: w = u - v^2
            sage: w.expansion(4)
            0"""
    @overload
    def expansion(self) -> Any:
        """pAdicZZpXCRElement.expansion(self, n=None, lift_mode='simple')

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_ZZ_pX_CR_element.pyx (starting at line 2710)

        Return a list giving a series representation of ``self``.

        - If ``lift_mode == 'simple'`` or ``'smallest'``, the returned
          list will consist of integers (in the Eisenstein case) or a
          list of lists of integers (in the unramified case).  ``self``
          can be reconstructed as a sum of elements of the list times
          powers of the uniformiser (in the Eisenstein case), or as a
          sum of powers of the `p` times polynomials in the generator
          (in the unramified case).

          + If ``lift_mode == 'simple'``, all integers will be in the interval
            `[0,p-1]`.

          + If ``lift_mode == 'smallest'`` they will be in the
            interval `[(1-p)/2, p/2]`.

        - If ``lift_mode == 'teichmuller'``, returns a list of
          ``pAdicZZpXCRElements``, all of which are Teichmuller
          representatives and such that ``self`` is the sum of that list
          times powers of the uniformizer.

        Note that zeros are truncated from the returned list if
        ``self.parent()`` is a field, so you must use the
        ``valuation`` function to fully reconstruct ``self``.

        INPUT:

        - ``n`` -- integer (default: ``None``); if given, returns the
          corresponding entry in the expansion

        EXAMPLES::

            sage: R = Zp(5,5)
            sage: S.<x> = R[]
            sage: f = x^5 + 75*x^3 - 15*x^2 + 125*x - 5
            sage: W.<w> = R.ext(f)
            sage: y = W(775, 19); y
            w^10 + 4*w^12 + 2*w^14 + w^15 + 2*w^16 + 4*w^17 + w^18 + O(w^19)
            sage: (y>>9).expansion()
            [0, 1, 0, 4, 0, 2, 1, 2, 4, 1]
            sage: (y>>9).expansion(lift_mode='smallest')
            [0, 1, 0, -1, 0, 2, 1, 2, 0, 1]
            sage: w^10 - w^12 + 2*w^14 + w^15 + 2*w^16 + w^18 + O(w^19)
            w^10 + 4*w^12 + 2*w^14 + w^15 + 2*w^16 + 4*w^17 + w^18 + O(w^19)
            sage: g = x^3 + 3*x + 3
            sage: A.<a> = R.ext(g)
            sage: y = 75 + 45*a + 1200*a^2; y
            4*a*5 + (3*a^2 + a + 3)*5^2 + 4*a^2*5^3 + a^2*5^4 + O(5^6)
            sage: E = y.expansion(); E
            5-adic expansion of 4*a*5 + (3*a^2 + a + 3)*5^2 + 4*a^2*5^3 + a^2*5^4 + O(5^6)
            sage: list(E)
            [[], [0, 4], [3, 1, 3], [0, 0, 4], [0, 0, 1], []]
            sage: list(y.expansion(lift_mode='smallest'))
            [[], [0, -1], [-2, 2, -2], [1], [0, 0, 2], []]
            sage: 5*((-2*5 + 25) + (-1 + 2*5)*a + (-2*5 + 2*125)*a^2)
            4*a*5 + (3*a^2 + a + 3)*5^2 + 4*a^2*5^3 + a^2*5^4 + O(5^6)
            sage: list(W(0).expansion())
            []
            sage: list(W(0,4).expansion())
            []
            sage: list(A(0,4).expansion())
            []

        TESTS:

        We check that :issue:`24949` is fixed::

            sage: R = Zp(2)
            sage: S.<x> = R[]
            sage: A.<a> = R.extension(x^10 + 2)
            sage: u = a^4 + a^5
            sage: v = a^2 + a^3
            sage: w = u - v^2
            sage: w.expansion(4)
            0"""
    @overload
    def expansion(self) -> Any:
        """pAdicZZpXCRElement.expansion(self, n=None, lift_mode='simple')

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_ZZ_pX_CR_element.pyx (starting at line 2710)

        Return a list giving a series representation of ``self``.

        - If ``lift_mode == 'simple'`` or ``'smallest'``, the returned
          list will consist of integers (in the Eisenstein case) or a
          list of lists of integers (in the unramified case).  ``self``
          can be reconstructed as a sum of elements of the list times
          powers of the uniformiser (in the Eisenstein case), or as a
          sum of powers of the `p` times polynomials in the generator
          (in the unramified case).

          + If ``lift_mode == 'simple'``, all integers will be in the interval
            `[0,p-1]`.

          + If ``lift_mode == 'smallest'`` they will be in the
            interval `[(1-p)/2, p/2]`.

        - If ``lift_mode == 'teichmuller'``, returns a list of
          ``pAdicZZpXCRElements``, all of which are Teichmuller
          representatives and such that ``self`` is the sum of that list
          times powers of the uniformizer.

        Note that zeros are truncated from the returned list if
        ``self.parent()`` is a field, so you must use the
        ``valuation`` function to fully reconstruct ``self``.

        INPUT:

        - ``n`` -- integer (default: ``None``); if given, returns the
          corresponding entry in the expansion

        EXAMPLES::

            sage: R = Zp(5,5)
            sage: S.<x> = R[]
            sage: f = x^5 + 75*x^3 - 15*x^2 + 125*x - 5
            sage: W.<w> = R.ext(f)
            sage: y = W(775, 19); y
            w^10 + 4*w^12 + 2*w^14 + w^15 + 2*w^16 + 4*w^17 + w^18 + O(w^19)
            sage: (y>>9).expansion()
            [0, 1, 0, 4, 0, 2, 1, 2, 4, 1]
            sage: (y>>9).expansion(lift_mode='smallest')
            [0, 1, 0, -1, 0, 2, 1, 2, 0, 1]
            sage: w^10 - w^12 + 2*w^14 + w^15 + 2*w^16 + w^18 + O(w^19)
            w^10 + 4*w^12 + 2*w^14 + w^15 + 2*w^16 + 4*w^17 + w^18 + O(w^19)
            sage: g = x^3 + 3*x + 3
            sage: A.<a> = R.ext(g)
            sage: y = 75 + 45*a + 1200*a^2; y
            4*a*5 + (3*a^2 + a + 3)*5^2 + 4*a^2*5^3 + a^2*5^4 + O(5^6)
            sage: E = y.expansion(); E
            5-adic expansion of 4*a*5 + (3*a^2 + a + 3)*5^2 + 4*a^2*5^3 + a^2*5^4 + O(5^6)
            sage: list(E)
            [[], [0, 4], [3, 1, 3], [0, 0, 4], [0, 0, 1], []]
            sage: list(y.expansion(lift_mode='smallest'))
            [[], [0, -1], [-2, 2, -2], [1], [0, 0, 2], []]
            sage: 5*((-2*5 + 25) + (-1 + 2*5)*a + (-2*5 + 2*125)*a^2)
            4*a*5 + (3*a^2 + a + 3)*5^2 + 4*a^2*5^3 + a^2*5^4 + O(5^6)
            sage: list(W(0).expansion())
            []
            sage: list(W(0,4).expansion())
            []
            sage: list(A(0,4).expansion())
            []

        TESTS:

        We check that :issue:`24949` is fixed::

            sage: R = Zp(2)
            sage: S.<x> = R[]
            sage: A.<a> = R.extension(x^10 + 2)
            sage: u = a^4 + a^5
            sage: v = a^2 + a^3
            sage: w = u - v^2
            sage: w.expansion(4)
            0"""
    @overload
    def expansion(self) -> Any:
        """pAdicZZpXCRElement.expansion(self, n=None, lift_mode='simple')

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_ZZ_pX_CR_element.pyx (starting at line 2710)

        Return a list giving a series representation of ``self``.

        - If ``lift_mode == 'simple'`` or ``'smallest'``, the returned
          list will consist of integers (in the Eisenstein case) or a
          list of lists of integers (in the unramified case).  ``self``
          can be reconstructed as a sum of elements of the list times
          powers of the uniformiser (in the Eisenstein case), or as a
          sum of powers of the `p` times polynomials in the generator
          (in the unramified case).

          + If ``lift_mode == 'simple'``, all integers will be in the interval
            `[0,p-1]`.

          + If ``lift_mode == 'smallest'`` they will be in the
            interval `[(1-p)/2, p/2]`.

        - If ``lift_mode == 'teichmuller'``, returns a list of
          ``pAdicZZpXCRElements``, all of which are Teichmuller
          representatives and such that ``self`` is the sum of that list
          times powers of the uniformizer.

        Note that zeros are truncated from the returned list if
        ``self.parent()`` is a field, so you must use the
        ``valuation`` function to fully reconstruct ``self``.

        INPUT:

        - ``n`` -- integer (default: ``None``); if given, returns the
          corresponding entry in the expansion

        EXAMPLES::

            sage: R = Zp(5,5)
            sage: S.<x> = R[]
            sage: f = x^5 + 75*x^3 - 15*x^2 + 125*x - 5
            sage: W.<w> = R.ext(f)
            sage: y = W(775, 19); y
            w^10 + 4*w^12 + 2*w^14 + w^15 + 2*w^16 + 4*w^17 + w^18 + O(w^19)
            sage: (y>>9).expansion()
            [0, 1, 0, 4, 0, 2, 1, 2, 4, 1]
            sage: (y>>9).expansion(lift_mode='smallest')
            [0, 1, 0, -1, 0, 2, 1, 2, 0, 1]
            sage: w^10 - w^12 + 2*w^14 + w^15 + 2*w^16 + w^18 + O(w^19)
            w^10 + 4*w^12 + 2*w^14 + w^15 + 2*w^16 + 4*w^17 + w^18 + O(w^19)
            sage: g = x^3 + 3*x + 3
            sage: A.<a> = R.ext(g)
            sage: y = 75 + 45*a + 1200*a^2; y
            4*a*5 + (3*a^2 + a + 3)*5^2 + 4*a^2*5^3 + a^2*5^4 + O(5^6)
            sage: E = y.expansion(); E
            5-adic expansion of 4*a*5 + (3*a^2 + a + 3)*5^2 + 4*a^2*5^3 + a^2*5^4 + O(5^6)
            sage: list(E)
            [[], [0, 4], [3, 1, 3], [0, 0, 4], [0, 0, 1], []]
            sage: list(y.expansion(lift_mode='smallest'))
            [[], [0, -1], [-2, 2, -2], [1], [0, 0, 2], []]
            sage: 5*((-2*5 + 25) + (-1 + 2*5)*a + (-2*5 + 2*125)*a^2)
            4*a*5 + (3*a^2 + a + 3)*5^2 + 4*a^2*5^3 + a^2*5^4 + O(5^6)
            sage: list(W(0).expansion())
            []
            sage: list(W(0,4).expansion())
            []
            sage: list(A(0,4).expansion())
            []

        TESTS:

        We check that :issue:`24949` is fixed::

            sage: R = Zp(2)
            sage: S.<x> = R[]
            sage: A.<a> = R.extension(x^10 + 2)
            sage: u = a^4 + a^5
            sage: v = a^2 + a^3
            sage: w = u - v^2
            sage: w.expansion(4)
            0"""
    @overload
    def is_equal_to(self, right, absprec=...) -> Any:
        """pAdicZZpXCRElement.is_equal_to(self, right, absprec=None)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_ZZ_pX_CR_element.pyx (starting at line 2592)

        Return whether this element is equal to ``right`` modulo ``self.uniformizer()^absprec``.

        If ``absprec`` is ``None``, checks whether this element is equal to ``right``
        modulo the lower of their two precisions.

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
        """pAdicZZpXCRElement.is_equal_to(self, right, absprec=None)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_ZZ_pX_CR_element.pyx (starting at line 2592)

        Return whether this element is equal to ``right`` modulo ``self.uniformizer()^absprec``.

        If ``absprec`` is ``None``, checks whether this element is equal to ``right``
        modulo the lower of their two precisions.

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
        """pAdicZZpXCRElement.is_zero(self, absprec=None)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_ZZ_pX_CR_element.pyx (starting at line 2334)

        Return whether the valuation of this element is at least
        ``absprec``.  If ``absprec`` is ``None``, checks if this element
        is indistinguishable from zero.

        If this element is an inexact zero of valuation less than ``absprec``,
        raises a :exc:`PrecisionError`.

        EXAMPLES::

            sage: R = Zp(5,5)
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
        """pAdicZZpXCRElement.is_zero(self, absprec=None)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_ZZ_pX_CR_element.pyx (starting at line 2334)

        Return whether the valuation of this element is at least
        ``absprec``.  If ``absprec`` is ``None``, checks if this element
        is indistinguishable from zero.

        If this element is an inexact zero of valuation less than ``absprec``,
        raises a :exc:`PrecisionError`.

        EXAMPLES::

            sage: R = Zp(5,5)
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
        """pAdicZZpXCRElement.is_zero(self, absprec=None)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_ZZ_pX_CR_element.pyx (starting at line 2334)

        Return whether the valuation of this element is at least
        ``absprec``.  If ``absprec`` is ``None``, checks if this element
        is indistinguishable from zero.

        If this element is an inexact zero of valuation less than ``absprec``,
        raises a :exc:`PrecisionError`.

        EXAMPLES::

            sage: R = Zp(5,5)
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
        """pAdicZZpXCRElement.is_zero(self, absprec=None)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_ZZ_pX_CR_element.pyx (starting at line 2334)

        Return whether the valuation of this element is at least
        ``absprec``.  If ``absprec`` is ``None``, checks if this element
        is indistinguishable from zero.

        If this element is an inexact zero of valuation less than ``absprec``,
        raises a :exc:`PrecisionError`.

        EXAMPLES::

            sage: R = Zp(5,5)
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
    def lift_to_precision(self, absprec=...) -> pAdicZZpXCRElement:
        """pAdicZZpXCRElement.lift_to_precision(self, absprec=None) -> pAdicZZpXCRElement

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_ZZ_pX_CR_element.pyx (starting at line 2623)

        Return a ``pAdicZZpXCRElement`` congruent to this element but with
        absolute precision at least ``absprec``.

        INPUT:

        - ``absprec`` -- (default: ``None``) the absolute precision of
          the result.  If ``None``, lifts to the maximum precision
          allowed.

        .. NOTE::

            If setting ``absprec`` that high would violate the
            precision cap, raises a precision error.  If ``self`` is an
            inexact zero and ``absprec`` is greater than the maximum
            allowed valuation, raises an error.

            Note that the new digits will not necessarily be zero.

        EXAMPLES::

            sage: R = Zp(5,5)
            sage: S.<x> = R[]
            sage: f = x^5 + 75*x^3 - 15*x^2 + 125*x - 5
            sage: W.<w> = R.ext(f)
            sage: a = W(345, 17); a
            4*w^5 + 3*w^7 + w^9 + 3*w^10 + 2*w^11 + 4*w^12 + w^13 + 2*w^14 + 2*w^15 + O(w^17)
            sage: b = a.lift_to_precision(19); b
            4*w^5 + 3*w^7 + w^9 + 3*w^10 + 2*w^11 + 4*w^12 + w^13 + 2*w^14 + 2*w^15
             + w^17 + 2*w^18 + O(w^19)
            sage: c = a.lift_to_precision(24); c
            4*w^5 + 3*w^7 + w^9 + 3*w^10 + 2*w^11 + 4*w^12 + w^13 + 2*w^14 + 2*w^15
             + w^17 + 2*w^18 + 4*w^19 + 4*w^20 + 2*w^21 + 4*w^23 + O(w^24)
            sage: a._ntl_rep()
            [19 35 118 60 121]
            sage: b._ntl_rep()
            [19 35 118 60 121]
            sage: c._ntl_rep()
            [19 35 118 60 121]
            sage: a.lift_to_precision().precision_relative() == W.precision_cap()
            True"""
    @overload
    def lift_to_precision(self) -> Any:
        """pAdicZZpXCRElement.lift_to_precision(self, absprec=None) -> pAdicZZpXCRElement

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_ZZ_pX_CR_element.pyx (starting at line 2623)

        Return a ``pAdicZZpXCRElement`` congruent to this element but with
        absolute precision at least ``absprec``.

        INPUT:

        - ``absprec`` -- (default: ``None``) the absolute precision of
          the result.  If ``None``, lifts to the maximum precision
          allowed.

        .. NOTE::

            If setting ``absprec`` that high would violate the
            precision cap, raises a precision error.  If ``self`` is an
            inexact zero and ``absprec`` is greater than the maximum
            allowed valuation, raises an error.

            Note that the new digits will not necessarily be zero.

        EXAMPLES::

            sage: R = Zp(5,5)
            sage: S.<x> = R[]
            sage: f = x^5 + 75*x^3 - 15*x^2 + 125*x - 5
            sage: W.<w> = R.ext(f)
            sage: a = W(345, 17); a
            4*w^5 + 3*w^7 + w^9 + 3*w^10 + 2*w^11 + 4*w^12 + w^13 + 2*w^14 + 2*w^15 + O(w^17)
            sage: b = a.lift_to_precision(19); b
            4*w^5 + 3*w^7 + w^9 + 3*w^10 + 2*w^11 + 4*w^12 + w^13 + 2*w^14 + 2*w^15
             + w^17 + 2*w^18 + O(w^19)
            sage: c = a.lift_to_precision(24); c
            4*w^5 + 3*w^7 + w^9 + 3*w^10 + 2*w^11 + 4*w^12 + w^13 + 2*w^14 + 2*w^15
             + w^17 + 2*w^18 + 4*w^19 + 4*w^20 + 2*w^21 + 4*w^23 + O(w^24)
            sage: a._ntl_rep()
            [19 35 118 60 121]
            sage: b._ntl_rep()
            [19 35 118 60 121]
            sage: c._ntl_rep()
            [19 35 118 60 121]
            sage: a.lift_to_precision().precision_relative() == W.precision_cap()
            True"""
    def matrix_mod_pn(self) -> Any:
        """pAdicZZpXCRElement.matrix_mod_pn(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_ZZ_pX_CR_element.pyx (starting at line 2824)

        Return the matrix of right multiplication by the element on
        the power basis `1, x, x^2, \\ldots, x^{d-1}` for this
        extension field.  Thus the *rows* of this matrix give the
        images of each of the `x^i`.  The entries of the matrices are
        :class:`IntegerMod` elements, defined modulo `p^{N / e}` where `N` is
        the absolute precision of this element (unless this element is
        zero to arbitrary precision; in that case the entries are
        integer zeros.)

        Raises an error if this element has negative valuation.

        EXAMPLES::

            sage: R = ZpCR(5,5)
            sage: S.<x> = R[]
            sage: f = x^5 + 75*x^3 - 15*x^2 + 125*x - 5
            sage: W.<w> = R.ext(f)
            sage: a = (3+w)^7
            sage: a.matrix_mod_pn()
            [2757  333 1068  725 2510]
            [  50 1507  483  318  725]
            [ 500   50 3007 2358  318]
            [1590 1375 1695 1032 2358]
            [2415  590 2370 2970 1032]

        TESTS:

        Check that :issue:`13617` has been fixed::

            sage: W.zero().matrix_mod_pn()
            [0 0 0 0 0]
            [0 0 0 0 0]
            [0 0 0 0 0]
            [0 0 0 0 0]
            [0 0 0 0 0]"""
    @overload
    def polynomial(self, var=...) -> Any:
        """pAdicZZpXCRElement.polynomial(self, var='x')

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_ZZ_pX_CR_element.pyx (starting at line 2554)

        Return a polynomial over the base ring that yields this element
        when evaluated at the generator of the parent.

        INPUT:

        - ``var`` -- string, the variable name for the polynomial

        EXAMPLES::

            sage: S.<x> = ZZ[]
            sage: W.<w> = Zp(5).extension(x^2 - 5)
            sage: (w + W(5, 7)).polynomial()
            (1 + O(5^3))*x + 5 + O(5^4)"""
    @overload
    def polynomial(self) -> Any:
        """pAdicZZpXCRElement.polynomial(self, var='x')

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_ZZ_pX_CR_element.pyx (starting at line 2554)

        Return a polynomial over the base ring that yields this element
        when evaluated at the generator of the parent.

        INPUT:

        - ``var`` -- string, the variable name for the polynomial

        EXAMPLES::

            sage: S.<x> = ZZ[]
            sage: W.<w> = Zp(5).extension(x^2 - 5)
            sage: (w + W(5, 7)).polynomial()
            (1 + O(5^3))*x + 5 + O(5^4)"""
    @overload
    def precision_absolute(self) -> Any:
        """pAdicZZpXCRElement.precision_absolute(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_ZZ_pX_CR_element.pyx (starting at line 3078)

        Return the absolute precision of this element, i.e., the power of the
        uniformizer modulo which this element is defined.

        EXAMPLES::

            sage: R = Zp(5,5)
            sage: S.<x> = R[]
            sage: f = x^5 + 75*x^3 - 15*x^2 + 125*x - 5
            sage: W.<w> = R.ext(f)
            sage: a = W(75, 19); a
            3*w^10 + 2*w^12 + w^14 + w^16 + w^17 + 3*w^18 + O(w^19)
            sage: a.valuation()
            10
            sage: a.precision_absolute()
            19
            sage: a.precision_relative()
            9
            sage: a.unit_part()
            3 + 2*w^2 + w^4 + w^6 + w^7 + 3*w^8 + O(w^9)
            sage: (a.unit_part() - 3).precision_absolute()
            9"""
    @overload
    def precision_absolute(self) -> Any:
        """pAdicZZpXCRElement.precision_absolute(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_ZZ_pX_CR_element.pyx (starting at line 3078)

        Return the absolute precision of this element, i.e., the power of the
        uniformizer modulo which this element is defined.

        EXAMPLES::

            sage: R = Zp(5,5)
            sage: S.<x> = R[]
            sage: f = x^5 + 75*x^3 - 15*x^2 + 125*x - 5
            sage: W.<w> = R.ext(f)
            sage: a = W(75, 19); a
            3*w^10 + 2*w^12 + w^14 + w^16 + w^17 + 3*w^18 + O(w^19)
            sage: a.valuation()
            10
            sage: a.precision_absolute()
            19
            sage: a.precision_relative()
            9
            sage: a.unit_part()
            3 + 2*w^2 + w^4 + w^6 + w^7 + 3*w^8 + O(w^9)
            sage: (a.unit_part() - 3).precision_absolute()
            9"""
    @overload
    def precision_absolute(self) -> Any:
        """pAdicZZpXCRElement.precision_absolute(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_ZZ_pX_CR_element.pyx (starting at line 3078)

        Return the absolute precision of this element, i.e., the power of the
        uniformizer modulo which this element is defined.

        EXAMPLES::

            sage: R = Zp(5,5)
            sage: S.<x> = R[]
            sage: f = x^5 + 75*x^3 - 15*x^2 + 125*x - 5
            sage: W.<w> = R.ext(f)
            sage: a = W(75, 19); a
            3*w^10 + 2*w^12 + w^14 + w^16 + w^17 + 3*w^18 + O(w^19)
            sage: a.valuation()
            10
            sage: a.precision_absolute()
            19
            sage: a.precision_relative()
            9
            sage: a.unit_part()
            3 + 2*w^2 + w^4 + w^6 + w^7 + 3*w^8 + O(w^9)
            sage: (a.unit_part() - 3).precision_absolute()
            9"""
    @overload
    def precision_relative(self) -> Any:
        """pAdicZZpXCRElement.precision_relative(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_ZZ_pX_CR_element.pyx (starting at line 3113)

        Return the relative precision of this element, i.e., the power of the
        uniformizer modulo which the unit part of ``self`` is defined.

        EXAMPLES::

            sage: R = Zp(5,5)
            sage: S.<x> = R[]
            sage: f = x^5 + 75*x^3 - 15*x^2 + 125*x - 5
            sage: W.<w> = R.ext(f)
            sage: a = W(75, 19); a
            3*w^10 + 2*w^12 + w^14 + w^16 + w^17 + 3*w^18 + O(w^19)
            sage: a.valuation()
            10
            sage: a.precision_absolute()
            19
            sage: a.precision_relative()
            9
            sage: a.unit_part()
            3 + 2*w^2 + w^4 + w^6 + w^7 + 3*w^8 + O(w^9)"""
    @overload
    def precision_relative(self) -> Any:
        """pAdicZZpXCRElement.precision_relative(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_ZZ_pX_CR_element.pyx (starting at line 3113)

        Return the relative precision of this element, i.e., the power of the
        uniformizer modulo which the unit part of ``self`` is defined.

        EXAMPLES::

            sage: R = Zp(5,5)
            sage: S.<x> = R[]
            sage: f = x^5 + 75*x^3 - 15*x^2 + 125*x - 5
            sage: W.<w> = R.ext(f)
            sage: a = W(75, 19); a
            3*w^10 + 2*w^12 + w^14 + w^16 + w^17 + 3*w^18 + O(w^19)
            sage: a.valuation()
            10
            sage: a.precision_absolute()
            19
            sage: a.precision_relative()
            9
            sage: a.unit_part()
            3 + 2*w^2 + w^4 + w^6 + w^7 + 3*w^8 + O(w^9)"""
    def teichmuller_expansion(self, n=...) -> Any:
        """pAdicZZpXCRElement.teichmuller_expansion(self, n=None)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_ZZ_pX_CR_element.pyx (starting at line 2922)

        Return a list [`a_0`, `a_1`,..., `a_n`] such that:

        - `a_i^q = a_i`
        - ``self.unit_part()`` = `\\sum_{i = 0}^n a_i \\pi^i`, where `\\pi` is a
          uniformizer of ``self.parent()``
        - if `a_i \\ne 0`, the absolute precision of `a_i` is
          ``self.precision_relative() - i``

        INPUT:

        - ``n`` -- integer (default: ``None``); if given, returns the
          corresponding entry in the expansion

        EXAMPLES::

            sage: R.<a> = ZqCR(5^4,4)
            sage: E = a.teichmuller_expansion(); E
            5-adic expansion of a + O(5^4) (teichmuller)
            sage: list(E)
            [a + (2*a^3 + 2*a^2 + 3*a + 4)*5 + (4*a^3 + 3*a^2 + 3*a + 2)*5^2
               + (4*a^2 + 2*a + 2)*5^3 + O(5^4),
             (3*a^3 + 3*a^2 + 2*a + 1) + (a^3 + 4*a^2 + 1)*5 + (a^2 + 4*a + 4)*5^2 + O(5^3),
             (4*a^3 + 2*a^2 + a + 1) + (2*a^3 + 2*a^2 + 2*a + 4)*5 + O(5^2),
             (a^3 + a^2 + a + 4) + O(5)]
            sage: sum([c * 5^i for i, c in enumerate(E)])
            a + O(5^4)
            sage: all(c^625 == c for c in E)
            True

            sage: S.<x> = ZZ[]
            sage: f = x^3 - 98*x + 7
            sage: W.<w> = ZpCR(7,3).ext(f)
            sage: b = (1+w)^5; L = b.teichmuller_expansion(); L
            [1 + O(w^9), 5 + 5*w^3 + w^6 + 4*w^7 + O(w^8), 3 + 3*w^3 + O(w^7),
             3 + 3*w^3 + O(w^6), O(w^5), 4 + 5*w^3 + O(w^4), 3 + O(w^3),
             6 + O(w^2), 6 + O(w)]
            sage: sum([w^i*L[i] for i in range(9)]) == b
            True
            sage: all(L[i]^(7^3) == L[i] for i in range(9))
            True

            sage: L = W(3).teichmuller_expansion(); L
            [3 + 3*w^3 + w^7 + O(w^9), O(w^8), O(w^7), 4 + 5*w^3 + O(w^6),
             O(w^5), O(w^4), 3 + O(w^3), 6 + O(w^2)]
            sage: sum([w^i*L[i] for i in range(len(L))])
            3 + O(w^9)"""
    @overload
    def unit_part(self) -> pAdicZZpXCRElement:
        """pAdicZZpXCRElement.unit_part(self) -> pAdicZZpXCRElement

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_ZZ_pX_CR_element.pyx (starting at line 3170)

        Return the unit part of this element, ie ``self / uniformizer^(self.valuation())``.

        EXAMPLES::

            sage: R = Zp(5,5)
            sage: S.<x> = R[]
            sage: f = x^5 + 75*x^3 - 15*x^2 + 125*x - 5
            sage: W.<w> = R.ext(f)
            sage: a = W(75, 19); a
            3*w^10 + 2*w^12 + w^14 + w^16 + w^17 + 3*w^18 + O(w^19)
            sage: a.valuation()
            10
            sage: a.precision_absolute()
            19
            sage: a.precision_relative()
            9
            sage: a.unit_part()
            3 + 2*w^2 + w^4 + w^6 + w^7 + 3*w^8 + O(w^9)

        TESTS:

        We check that :issue:`13616` is resolved::

            sage: z = (1+w)^5
            sage: y = z - 1
            sage: t = y - y
            sage: t.unit_part()
            O(w^0)"""
    @overload
    def unit_part(self) -> Any:
        """pAdicZZpXCRElement.unit_part(self) -> pAdicZZpXCRElement

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_ZZ_pX_CR_element.pyx (starting at line 3170)

        Return the unit part of this element, ie ``self / uniformizer^(self.valuation())``.

        EXAMPLES::

            sage: R = Zp(5,5)
            sage: S.<x> = R[]
            sage: f = x^5 + 75*x^3 - 15*x^2 + 125*x - 5
            sage: W.<w> = R.ext(f)
            sage: a = W(75, 19); a
            3*w^10 + 2*w^12 + w^14 + w^16 + w^17 + 3*w^18 + O(w^19)
            sage: a.valuation()
            10
            sage: a.precision_absolute()
            19
            sage: a.precision_relative()
            9
            sage: a.unit_part()
            3 + 2*w^2 + w^4 + w^6 + w^7 + 3*w^8 + O(w^9)

        TESTS:

        We check that :issue:`13616` is resolved::

            sage: z = (1+w)^5
            sage: y = z - 1
            sage: t = y - y
            sage: t.unit_part()
            O(w^0)"""
    @overload
    def unit_part(self) -> Any:
        """pAdicZZpXCRElement.unit_part(self) -> pAdicZZpXCRElement

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_ZZ_pX_CR_element.pyx (starting at line 3170)

        Return the unit part of this element, ie ``self / uniformizer^(self.valuation())``.

        EXAMPLES::

            sage: R = Zp(5,5)
            sage: S.<x> = R[]
            sage: f = x^5 + 75*x^3 - 15*x^2 + 125*x - 5
            sage: W.<w> = R.ext(f)
            sage: a = W(75, 19); a
            3*w^10 + 2*w^12 + w^14 + w^16 + w^17 + 3*w^18 + O(w^19)
            sage: a.valuation()
            10
            sage: a.precision_absolute()
            19
            sage: a.precision_relative()
            9
            sage: a.unit_part()
            3 + 2*w^2 + w^4 + w^6 + w^7 + 3*w^8 + O(w^9)

        TESTS:

        We check that :issue:`13616` is resolved::

            sage: z = (1+w)^5
            sage: y = z - 1
            sage: t = y - y
            sage: t.unit_part()
            O(w^0)"""
    def __copy__(self) -> Any:
        """pAdicZZpXCRElement.__copy__(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_ZZ_pX_CR_element.pyx (starting at line 2272)

        Return a copy of this element.

        EXAMPLES::

            sage: R = Zp(5,5)
            sage: S.<x> = R[]
            sage: f = x^5 + 75*x^3 - 15*x^2 + 125*x - 5
            sage: W.<w> = R.ext(f)
            sage: b = W(45, 17); b
            4*w^5 + 3*w^7 + w^9 + w^10 + 2*w^11 + w^12 + w^13 + 3*w^14 + w^16 + O(w^17)
            sage: c = copy(b); c
            4*w^5 + 3*w^7 + w^9 + w^10 + 2*w^11 + w^12 + w^13 + 3*w^14 + w^16 + O(w^17)
            sage: c is b
            False"""
    def __invert__(self) -> Any:
        """pAdicZZpXCRElement.__invert__(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_ZZ_pX_CR_element.pyx (starting at line 1560)

        Return the inverse of this element.

        EXAMPLES::

            sage: R = Zp(5,5)
            sage: S.<x> = R[]
            sage: f = x^5 + 75*x^3 - 15*x^2 + 125*x - 5
            sage: W.<w> = R.ext(f)
            sage: z = (1 + w)^5
            sage: y = ~z; y  # indirect doctest
            1 + 4*w^5 + 4*w^6 + 3*w^7 + w^8 + 2*w^10 + w^11 + w^12 + 2*w^14 + 3*w^16 + 3*w^17 + 4*w^18 + 4*w^19 + 2*w^20 + 2*w^21 + 4*w^22 + 3*w^23 + 3*w^24 + O(w^25)
            sage: y.parent()
            5-adic Eisenstein Extension Field in w defined by x^5 + 75*x^3 - 15*x^2 + 125*x - 5
            sage: z = z - 1
            sage: ~z
            w^-5 + 4*w^-4 + 4*w^-3 + 4*w^-2 + 2*w^-1 + 1 + w + 4*w^2 + 4*w^3 + 4*w^4 + w^5 + w^6 + w^7 + 4*w^8 + 4*w^9 + 2*w^10 + w^11 + 2*w^12 + 4*w^13 + 4*w^14 + O(w^15)
            sage: ~z * z
            1 + O(w^20)"""
    def __lshift__(self, pAdicZZpXCRElementself, shift) -> Any:
        """pAdicZZpXCRElement.__lshift__(pAdicZZpXCRElement self, shift)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_ZZ_pX_CR_element.pyx (starting at line 1632)

        Multiply ``self`` by the uniformizer raised to the power ``n``.  If
        ``n`` is negative, right shifts by ``-n``.

        EXAMPLES::

            sage: R = Zp(5,5)
            sage: S.<x> = R[]
            sage: f = x^5 + 75*x^3 - 15*x^2 + 125*x - 5
            sage: W.<w> = R.ext(f)
            sage: z = (1 + w)^5
            sage: z
            1 + w^5 + w^6 + 2*w^7 + 4*w^8 + 3*w^10 + w^12 + 4*w^13 + 4*w^14 + 4*w^15 + 4*w^16 + 4*w^17 + 4*w^20 + w^21 + 4*w^24 + O(w^25)
            sage: z << 17  # indirect doctest
            w^17 + w^22 + w^23 + 2*w^24 + 4*w^25 + 3*w^27 + w^29 + 4*w^30 + 4*w^31 + 4*w^32 + 4*w^33 + 4*w^34 + 4*w^37 + w^38 + 4*w^41 + O(w^42)
            sage: z << (-1)
            w^4 + w^5 + 2*w^6 + 4*w^7 + 3*w^9 + w^11 + 4*w^12 + 4*w^13 + 4*w^14 + 4*w^15 + 4*w^16 + 4*w^19 + w^20 + 4*w^23 + O(w^24)"""
    def __pow__(self, pAdicZZpXCRElementself, _right, m) -> Any:
        """pAdicZZpXCRElement.__pow__(pAdicZZpXCRElement self, _right, m)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_ZZ_pX_CR_element.pyx (starting at line 1800)

        Compute ``self^right``.

        Note: when ``right`` is divisible by `p` then one can get more
        precision than expected.

        Lemma 2.1 (Constructing Class Fields over Local Fields, Sebastian Pauli):

        Let `\\alpha` be in `\\mathcal{O}_K`.  Let

        .. MATH::

            p = -\\pi_K^{e_K} \\epsilon

        be the factorization of `p` where `\\epsilon` is a unit.  Then
        the `p`-th power of `1 + \\alpha \\pi_K^{\\lambda}` satisfies

        .. MATH::

            (1 + \\alpha \\pi^{\\lambda})^p \\equiv \\left{ \\begin{array}{lll}
            1 + \\alpha^p \\pi_K^{p \\lambda} & \\mod \\mathfrak{p}_K^{p \\lambda + 1} & \\mbox{if $1 \\le \\lambda < \\frac{e_K}{p-1}$} \\\\\n            1 + (\\alpha^p - \\epsilon \\alpha) \\pi_K^{p \\lambda} & \\mod \\mathfrak{p}_K^{p \\lambda + 1} & \\mbox{if $\\lambda = \\frac{e_K}{p-1}$} \\\\\n            1 - \\epsilon \\alpha \\pi_K^{\\lambda + e} & \\mod \\mathfrak{p}_K^{\\lambda + e + 1} & \\mbox{if $\\lambda > \\frac{e_K}{p-1}$}
            \\end{array} \\right.


        So if ``right`` is divisible by `p^k` we can multiply the
        relative precision by `p` until we exceed `e/(p-1)`, then add
        `e` until we have done a total of `k` things: the precision of
        the result can therefore be greater than the precision of
        ``self``.

        There is also the issue of `p`-adic exponents, and determining
        how the precision of the exponent affects the precision of the
        result.

        In computing `(a + O(\\pi^k))^{b + O(p^m)}`, one needs that the
        reduction of `a` mod `\\pi` is in the prime field
        `\\GF{p}` (so that the `p^m` power of the Teichmuller
        part is constant as `m` increases).  Given this restriction,
        we can factor out the Teichmuller part and use the above lemma
        to find the first spot where

        .. MATH::

            (1 + \\alpha \\pi^{\\lambda})^{p^m}

        differs from 1.  We compare this with the precision bound
        given by computing `(a + O(\\pi^k))^b` and take the lesser of
        the two.

        In order to do this we need to compute the valuation of ``(self
        / self.parent().teichmuller(self)) - 1``.

        EXAMPLES::

            sage: R = Zp(5,5)
            sage: S.<x> = R[]
            sage: f = x^5 + 75*x^3 - 15*x^2 + 125*x - 5
            sage: W.<w> = R.ext(f)
            sage: (1 + w)^5  # indirect doctest
            1 + w^5 + w^6 + 2*w^7 + 4*w^8 + 3*w^10 + w^12 + 4*w^13 + 4*w^14 + 4*w^15 + 4*w^16 + 4*w^17 + 4*w^20 + w^21 + 4*w^24 + O(w^25)
            sage: (1 + w)^-5
            1 + 4*w^5 + 4*w^6 + 3*w^7 + w^8 + 2*w^10 + w^11 + w^12 + 2*w^14 + 3*w^16 + 3*w^17 + 4*w^18 + 4*w^19 + 2*w^20 + 2*w^21 + 4*w^22 + 3*w^23 + 3*w^24 + O(w^25)
            sage: (1 + w + O(w^19))^5
            1 + w^5 + w^6 + 2*w^7 + 4*w^8 + 3*w^10 + w^12 + 4*w^13 + 4*w^14 + 4*w^15 + 4*w^16 + 4*w^17 + 4*w^20 + w^21 + O(w^24)
            sage: (1 + O(w))^5
            1 + O(w^5)
            sage: (1 + w + O(w^3))^25
            1 + w^10 + w^11 + 4*w^12 + O(w^13)
            sage: (3 + 2*w + w^2 + O(w^6))^(15 + O(125))
            2 + 4*w^6 + w^7 + 3*w^8 + 3*w^9 + 4*w^10 + O(w^11)
            sage: (3 + 2*w + w^2 + O(w^6))^(15 + O(25))
            2 + 4*w^6 + w^7 + 3*w^8 + 3*w^9 + O(w^10)
            sage: (3 + w^2 + O(w^6))^(15+O(25))
            2 + w^5 + 4*w^7 + w^9 + 3*w^10 + O(w^11)
            sage: R = Zp(2, 10)
            sage: S.<x> = R[]
            sage: f = x^34 + 18*x^5 - 72*x^3 + 2
            sage: W.<w> = R.ext(f)
            sage: (1+w+O(w^2))^8
            1 + w^8 + O(w^16)
            sage: (1+w+O(w^2))^16
            1 + w^16 + O(w^32)
            sage: (1+w+O(w^2))^32
            1 + w^32 + w^50 + w^55 + w^60 + O(w^64)
            sage: (1+w+O(w^2))^64
            1 + w^64 + w^66 + w^71 + w^76 + w^81 + w^84 + w^86 + w^91 + w^94 + w^96 + O(w^98)

        TESTS:

            We define ``0^0`` to be unity, :issue:`13786`::

            sage: R = Zp(5,5)
            sage: S.<x> = R[]
            sage: f = x^5 + 75*x^3 - 15*x^2 + 125*x - 5
            sage: W.<w> = R.ext(f)
            sage: type(W(0))
            <class 'sage.rings.padics.padic_ZZ_pX_CR_element.pAdicZZpXCRElement'>
            sage: W(0)^0
            1 + O(w^25)
            sage: W(0)^0 == W(1)
            True

        The value returned from ``0^0`` should belong to our ring::

            sage: R = Zp(5,5)
            sage: S.<x> = R[]
            sage: f = x^5 + 75*x^3 - 15*x^2 + 125*x - 5
            sage: W.<w> = R.ext(f)
            sage: type(W(0)^0) == type(W(0))
            True"""
    def __reduce__(self) -> Any:
        """pAdicZZpXCRElement.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_ZZ_pX_CR_element.pyx (starting at line 1504)

        Pickles ``self``.

        EXAMPLES::

            sage: R = Qp(5,5)
            sage: S.<x> = R[]
            sage: f = x^5 + 75*x^3 - 15*x^2 + 125*x - 5
            sage: W.<w> = R.ext(f)
            sage: z = (1 + w)^5 - 1
            sage: loads(dumps(z)) == z
            True"""
    def __rlshift__(self, other):
        """Return value<<self."""
    def __rpow__(self, other):
        """Return pow(value, self, mod)."""
    def __rrshift__(self, other):
        """Return value>>self."""
    def __rshift__(self, pAdicZZpXCRElementself, shift) -> Any:
        """pAdicZZpXCRElement.__rshift__(pAdicZZpXCRElement self, shift)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_ZZ_pX_CR_element.pyx (starting at line 1730)

        Divide ``self`` by the uniformizer raised to the power ``n``.  If
        parent is not a field, throws away the nonpositive part of
        the series expansion.  If ``n`` is negative, left shifts by ``-n``.

        EXAMPLES::

            sage: R = Zp(5,5)
            sage: S.<x> = R[]
            sage: f = x^5 + 75*x^3 - 15*x^2 + 125*x - 5
            sage: W.<w> = R.ext(f)
            sage: z = (1 + w)^5
            sage: z
            1 + w^5 + w^6 + 2*w^7 + 4*w^8 + 3*w^10 + w^12 + 4*w^13 + 4*w^14 + 4*w^15 + 4*w^16 + 4*w^17 + 4*w^20 + w^21 + 4*w^24 + O(w^25)
            sage: z >> (6)  # indirect doctest
            1 + 2*w + 4*w^2 + 3*w^4 + w^6 + 4*w^7 + 4*w^8 + 4*w^9 + 4*w^10 + 4*w^11 + 4*w^14 + w^15 + 4*w^18 + O(w^19)
            sage: z >> (-4)
            w^4 + w^9 + w^10 + 2*w^11 + 4*w^12 + 3*w^14 + w^16 + 4*w^17 + 4*w^18 + 4*w^19 + 4*w^20 + 4*w^21 + 4*w^24 + w^25 + 4*w^28 + O(w^29)
            sage: F = W.fraction_field()
            sage: z = F(z)
            sage: z >> 7
            w^-7 + w^-2 + w^-1 + 2 + 4*w + 3*w^3 + w^5 + 4*w^6 + 4*w^7 + 4*w^8 + 4*w^9 + 4*w^10 + 4*w^13 + w^14 + 4*w^17 + O(w^18)"""
