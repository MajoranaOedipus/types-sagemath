import _cython_3_2_1
import sage.rings.padics.local_generic_element
from sage.arith.srange import srange as srange
from sage.categories.category import ZZ as ZZ
from sage.rings.infinity import infinity as infinity
from sage.rings.padics.precision_error import PrecisionError as PrecisionError
from sage.structure.element import coerce_binop as coerce_binop, have_same_parent as have_same_parent, parent as parent
from sage.structure.richcmp import revop as revop, rich_to_bool as rich_to_bool, rich_to_bool_sgn as rich_to_bool_sgn, richcmp as richcmp, richcmp_not_equal as richcmp_not_equal
from typing import Any, ClassVar, overload

__pyx_capi__: dict
dwork_mahler_coeffs: _cython_3_2_1.cython_function_or_method
evaluate_dwork_mahler: _cython_3_2_1.cython_function_or_method
gauss_table: _cython_3_2_1.cython_function_or_method

class pAdicGenericElement(sage.rings.padics.local_generic_element.LocalGenericElement):
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    @overload
    def abs(self, prec=...) -> Any:
        """pAdicGenericElement.abs(self, prec=None)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_generic_element.pyx (starting at line 3961)

        Return the `p`-adic absolute value of ``self``.

        This is normalized so that the absolute value of `p` is `1/p`.

        INPUT:

        - ``prec`` -- integer; the precision of the real field in which
          the answer is returned.  If ``None``, returns a rational for
          absolutely unramified fields, or a real with 53 bits of
          precision for ramified fields.

        EXAMPLES::

            sage: a = Qp(5)(15); a.abs()
            1/5
            sage: a.abs(53)                                                             # needs sage.rings.real_mpfr
            0.200000000000000
            sage: Qp(7)(0).abs()
            0
            sage: Qp(7)(0).abs(prec=20)                                                 # needs sage.rings.real_mpfr
            0.00000

        An unramified extension::

            sage: # needs sage.libs.ntl
            sage: R = Zp(5,5)
            sage: P.<x> = PolynomialRing(R)
            sage: Z25.<u> = R.ext(x^2 - 3)
            sage: u.abs()
            1
            sage: (u^24-1).abs()
            1/5

        A ramified extension::

            sage: # needs sage.libs.ntl
            sage: W.<w> = R.ext(x^5 + 75*x^3 - 15*x^2 + 125*x - 5)
            sage: w.abs()
            0.724779663677696
            sage: W(0).abs()
            0.000000000000000"""
    @overload
    def abs(self) -> Any:
        """pAdicGenericElement.abs(self, prec=None)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_generic_element.pyx (starting at line 3961)

        Return the `p`-adic absolute value of ``self``.

        This is normalized so that the absolute value of `p` is `1/p`.

        INPUT:

        - ``prec`` -- integer; the precision of the real field in which
          the answer is returned.  If ``None``, returns a rational for
          absolutely unramified fields, or a real with 53 bits of
          precision for ramified fields.

        EXAMPLES::

            sage: a = Qp(5)(15); a.abs()
            1/5
            sage: a.abs(53)                                                             # needs sage.rings.real_mpfr
            0.200000000000000
            sage: Qp(7)(0).abs()
            0
            sage: Qp(7)(0).abs(prec=20)                                                 # needs sage.rings.real_mpfr
            0.00000

        An unramified extension::

            sage: # needs sage.libs.ntl
            sage: R = Zp(5,5)
            sage: P.<x> = PolynomialRing(R)
            sage: Z25.<u> = R.ext(x^2 - 3)
            sage: u.abs()
            1
            sage: (u^24-1).abs()
            1/5

        A ramified extension::

            sage: # needs sage.libs.ntl
            sage: W.<w> = R.ext(x^5 + 75*x^3 - 15*x^2 + 125*x - 5)
            sage: w.abs()
            0.724779663677696
            sage: W(0).abs()
            0.000000000000000"""
    @overload
    def abs(self) -> Any:
        """pAdicGenericElement.abs(self, prec=None)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_generic_element.pyx (starting at line 3961)

        Return the `p`-adic absolute value of ``self``.

        This is normalized so that the absolute value of `p` is `1/p`.

        INPUT:

        - ``prec`` -- integer; the precision of the real field in which
          the answer is returned.  If ``None``, returns a rational for
          absolutely unramified fields, or a real with 53 bits of
          precision for ramified fields.

        EXAMPLES::

            sage: a = Qp(5)(15); a.abs()
            1/5
            sage: a.abs(53)                                                             # needs sage.rings.real_mpfr
            0.200000000000000
            sage: Qp(7)(0).abs()
            0
            sage: Qp(7)(0).abs(prec=20)                                                 # needs sage.rings.real_mpfr
            0.00000

        An unramified extension::

            sage: # needs sage.libs.ntl
            sage: R = Zp(5,5)
            sage: P.<x> = PolynomialRing(R)
            sage: Z25.<u> = R.ext(x^2 - 3)
            sage: u.abs()
            1
            sage: (u^24-1).abs()
            1/5

        A ramified extension::

            sage: # needs sage.libs.ntl
            sage: W.<w> = R.ext(x^5 + 75*x^3 - 15*x^2 + 125*x - 5)
            sage: w.abs()
            0.724779663677696
            sage: W(0).abs()
            0.000000000000000"""
    @overload
    def abs(self, prec=...) -> Any:
        """pAdicGenericElement.abs(self, prec=None)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_generic_element.pyx (starting at line 3961)

        Return the `p`-adic absolute value of ``self``.

        This is normalized so that the absolute value of `p` is `1/p`.

        INPUT:

        - ``prec`` -- integer; the precision of the real field in which
          the answer is returned.  If ``None``, returns a rational for
          absolutely unramified fields, or a real with 53 bits of
          precision for ramified fields.

        EXAMPLES::

            sage: a = Qp(5)(15); a.abs()
            1/5
            sage: a.abs(53)                                                             # needs sage.rings.real_mpfr
            0.200000000000000
            sage: Qp(7)(0).abs()
            0
            sage: Qp(7)(0).abs(prec=20)                                                 # needs sage.rings.real_mpfr
            0.00000

        An unramified extension::

            sage: # needs sage.libs.ntl
            sage: R = Zp(5,5)
            sage: P.<x> = PolynomialRing(R)
            sage: Z25.<u> = R.ext(x^2 - 3)
            sage: u.abs()
            1
            sage: (u^24-1).abs()
            1/5

        A ramified extension::

            sage: # needs sage.libs.ntl
            sage: W.<w> = R.ext(x^5 + 75*x^3 - 15*x^2 + 125*x - 5)
            sage: w.abs()
            0.724779663677696
            sage: W(0).abs()
            0.000000000000000"""
    @overload
    def abs(self) -> Any:
        """pAdicGenericElement.abs(self, prec=None)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_generic_element.pyx (starting at line 3961)

        Return the `p`-adic absolute value of ``self``.

        This is normalized so that the absolute value of `p` is `1/p`.

        INPUT:

        - ``prec`` -- integer; the precision of the real field in which
          the answer is returned.  If ``None``, returns a rational for
          absolutely unramified fields, or a real with 53 bits of
          precision for ramified fields.

        EXAMPLES::

            sage: a = Qp(5)(15); a.abs()
            1/5
            sage: a.abs(53)                                                             # needs sage.rings.real_mpfr
            0.200000000000000
            sage: Qp(7)(0).abs()
            0
            sage: Qp(7)(0).abs(prec=20)                                                 # needs sage.rings.real_mpfr
            0.00000

        An unramified extension::

            sage: # needs sage.libs.ntl
            sage: R = Zp(5,5)
            sage: P.<x> = PolynomialRing(R)
            sage: Z25.<u> = R.ext(x^2 - 3)
            sage: u.abs()
            1
            sage: (u^24-1).abs()
            1/5

        A ramified extension::

            sage: # needs sage.libs.ntl
            sage: W.<w> = R.ext(x^5 + 75*x^3 - 15*x^2 + 125*x - 5)
            sage: w.abs()
            0.724779663677696
            sage: W(0).abs()
            0.000000000000000"""
    @overload
    def abs(self) -> Any:
        """pAdicGenericElement.abs(self, prec=None)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_generic_element.pyx (starting at line 3961)

        Return the `p`-adic absolute value of ``self``.

        This is normalized so that the absolute value of `p` is `1/p`.

        INPUT:

        - ``prec`` -- integer; the precision of the real field in which
          the answer is returned.  If ``None``, returns a rational for
          absolutely unramified fields, or a real with 53 bits of
          precision for ramified fields.

        EXAMPLES::

            sage: a = Qp(5)(15); a.abs()
            1/5
            sage: a.abs(53)                                                             # needs sage.rings.real_mpfr
            0.200000000000000
            sage: Qp(7)(0).abs()
            0
            sage: Qp(7)(0).abs(prec=20)                                                 # needs sage.rings.real_mpfr
            0.00000

        An unramified extension::

            sage: # needs sage.libs.ntl
            sage: R = Zp(5,5)
            sage: P.<x> = PolynomialRing(R)
            sage: Z25.<u> = R.ext(x^2 - 3)
            sage: u.abs()
            1
            sage: (u^24-1).abs()
            1/5

        A ramified extension::

            sage: # needs sage.libs.ntl
            sage: W.<w> = R.ext(x^5 + 75*x^3 - 15*x^2 + 125*x - 5)
            sage: w.abs()
            0.724779663677696
            sage: W(0).abs()
            0.000000000000000"""
    @overload
    def abs(self) -> Any:
        """pAdicGenericElement.abs(self, prec=None)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_generic_element.pyx (starting at line 3961)

        Return the `p`-adic absolute value of ``self``.

        This is normalized so that the absolute value of `p` is `1/p`.

        INPUT:

        - ``prec`` -- integer; the precision of the real field in which
          the answer is returned.  If ``None``, returns a rational for
          absolutely unramified fields, or a real with 53 bits of
          precision for ramified fields.

        EXAMPLES::

            sage: a = Qp(5)(15); a.abs()
            1/5
            sage: a.abs(53)                                                             # needs sage.rings.real_mpfr
            0.200000000000000
            sage: Qp(7)(0).abs()
            0
            sage: Qp(7)(0).abs(prec=20)                                                 # needs sage.rings.real_mpfr
            0.00000

        An unramified extension::

            sage: # needs sage.libs.ntl
            sage: R = Zp(5,5)
            sage: P.<x> = PolynomialRing(R)
            sage: Z25.<u> = R.ext(x^2 - 3)
            sage: u.abs()
            1
            sage: (u^24-1).abs()
            1/5

        A ramified extension::

            sage: # needs sage.libs.ntl
            sage: W.<w> = R.ext(x^5 + 75*x^3 - 15*x^2 + 125*x - 5)
            sage: w.abs()
            0.724779663677696
            sage: W(0).abs()
            0.000000000000000"""
    @overload
    def abs(self) -> Any:
        """pAdicGenericElement.abs(self, prec=None)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_generic_element.pyx (starting at line 3961)

        Return the `p`-adic absolute value of ``self``.

        This is normalized so that the absolute value of `p` is `1/p`.

        INPUT:

        - ``prec`` -- integer; the precision of the real field in which
          the answer is returned.  If ``None``, returns a rational for
          absolutely unramified fields, or a real with 53 bits of
          precision for ramified fields.

        EXAMPLES::

            sage: a = Qp(5)(15); a.abs()
            1/5
            sage: a.abs(53)                                                             # needs sage.rings.real_mpfr
            0.200000000000000
            sage: Qp(7)(0).abs()
            0
            sage: Qp(7)(0).abs(prec=20)                                                 # needs sage.rings.real_mpfr
            0.00000

        An unramified extension::

            sage: # needs sage.libs.ntl
            sage: R = Zp(5,5)
            sage: P.<x> = PolynomialRing(R)
            sage: Z25.<u> = R.ext(x^2 - 3)
            sage: u.abs()
            1
            sage: (u^24-1).abs()
            1/5

        A ramified extension::

            sage: # needs sage.libs.ntl
            sage: W.<w> = R.ext(x^5 + 75*x^3 - 15*x^2 + 125*x - 5)
            sage: w.abs()
            0.724779663677696
            sage: W(0).abs()
            0.000000000000000"""
    def additive_order(self, prec=...) -> Any:
        """pAdicGenericElement.additive_order(self, prec=None)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_generic_element.pyx (starting at line 571)

        Return the additive order of this element truncated
        at precision ``prec``.

        INPUT:

        - ``prec`` -- integer or ``None`` (default: ``None``)

        OUTPUT: the additive order of this element

        EXAMPLES::

            sage: R = Zp(7, 4, 'capped-rel', 'series'); a = R(7^3); a.additive_order(3)
            1
            sage: a.additive_order(4)
            +Infinity
            sage: R = Zp(7, 4, 'fixed-mod', 'series'); a = R(7^5); a.additive_order(6)
            1"""
    def algdep(self, *args, **kwargs):
        """pAdicGenericElement.algebraic_dependency(self, n)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_generic_element.pyx (starting at line 1121)

        Return a polynomial of degree at most `n` which is approximately
        satisfied by this number.

        Note that the returned polynomial need not be irreducible, and
        indeed usually will not be if this number is a good
        approximation to an algebraic number of degree less than `n`.

        ALGORITHM: Uses the PARI C-library :pari:`algdep` command.

        INPUT:

        - ``self`` -- a `p`-adic element
        - ``n`` -- integer

        OUTPUT:

        polynomial; degree `n` polynomial approximately satisfied by ``self``

        EXAMPLES::

            sage: K = Qp(3,20,'capped-rel','series'); R = Zp(3,20,'capped-rel','series')
            sage: a = K(7/19); a
            1 + 2*3 + 3^2 + 3^3 + 2*3^4 + 2*3^5 + 3^8 + 2*3^9 + 3^11 + 3^12
              + 2*3^15 + 2*3^16 + 3^17 + 2*3^19 + O(3^20)
            sage: a.algebraic_dependency(1)
            19*x - 7
            sage: K2 = Qp(7,20,'capped-rel')
            sage: b = K2.zeta(); b.algebraic_dependency(2)
            x^2 - x + 1
            sage: K2 = Qp(11,20,'capped-rel')
            sage: b = K2.zeta(); b.algebraic_dependency(4)
            x^4 - x^3 + x^2 - x + 1
            sage: a = R(7/19); a
            1 + 2*3 + 3^2 + 3^3 + 2*3^4 + 2*3^5 + 3^8 + 2*3^9 + 3^11 + 3^12
              + 2*3^15 + 2*3^16 + 3^17 + 2*3^19 + O(3^20)
            sage: a.algebraic_dependency(1)
            19*x - 7
            sage: R2 = Zp(7,20,'capped-rel')
            sage: b = R2.zeta(); b.algebraic_dependency(2)
            x^2 - x + 1
            sage: R2 = Zp(11,20,'capped-rel')
            sage: b = R2.zeta(); b.algebraic_dependency(4)
            x^4 - x^3 + x^2 - x + 1"""
    def algebraic_dependency(self, n) -> Any:
        """pAdicGenericElement.algebraic_dependency(self, n)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_generic_element.pyx (starting at line 1121)

        Return a polynomial of degree at most `n` which is approximately
        satisfied by this number.

        Note that the returned polynomial need not be irreducible, and
        indeed usually will not be if this number is a good
        approximation to an algebraic number of degree less than `n`.

        ALGORITHM: Uses the PARI C-library :pari:`algdep` command.

        INPUT:

        - ``self`` -- a `p`-adic element
        - ``n`` -- integer

        OUTPUT:

        polynomial; degree `n` polynomial approximately satisfied by ``self``

        EXAMPLES::

            sage: K = Qp(3,20,'capped-rel','series'); R = Zp(3,20,'capped-rel','series')
            sage: a = K(7/19); a
            1 + 2*3 + 3^2 + 3^3 + 2*3^4 + 2*3^5 + 3^8 + 2*3^9 + 3^11 + 3^12
              + 2*3^15 + 2*3^16 + 3^17 + 2*3^19 + O(3^20)
            sage: a.algebraic_dependency(1)
            19*x - 7
            sage: K2 = Qp(7,20,'capped-rel')
            sage: b = K2.zeta(); b.algebraic_dependency(2)
            x^2 - x + 1
            sage: K2 = Qp(11,20,'capped-rel')
            sage: b = K2.zeta(); b.algebraic_dependency(4)
            x^4 - x^3 + x^2 - x + 1
            sage: a = R(7/19); a
            1 + 2*3 + 3^2 + 3^3 + 2*3^4 + 2*3^5 + 3^8 + 2*3^9 + 3^11 + 3^12
              + 2*3^15 + 2*3^16 + 3^17 + 2*3^19 + O(3^20)
            sage: a.algebraic_dependency(1)
            19*x - 7
            sage: R2 = Zp(7,20,'capped-rel')
            sage: b = R2.zeta(); b.algebraic_dependency(2)
            x^2 - x + 1
            sage: R2 = Zp(11,20,'capped-rel')
            sage: b = R2.zeta(); b.algebraic_dependency(4)
            x^4 - x^3 + x^2 - x + 1"""
    def artin_hasse_exp(self, prec=..., algorithm=...) -> Any:
        """pAdicGenericElement.artin_hasse_exp(self, prec=None, algorithm=None)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_generic_element.pyx (starting at line 596)

        Return the Artin-Hasse exponential of this element.

        INPUT:

        - ``prec`` -- integer or ``None`` (default: ``None``);
          the desired precision on the result; if ``None``, the
          precision is derived from the precision on the input

        - ``algorithm`` -- ``'direct'``, ``'series'``, ``'newton'`` or
          ``None`` (default)

          The direct algorithm computes the Artin-Hasse exponential
          of `x`, namely ``AH(x)`` as

          .. MATH::

              AH(x) = \\exp(x + \\frac{x^p}{p} + \\frac{x^{p^2}}{p^2} + \\dots

          It runs roughly as fast as the computation of the exponential
          (since the computation of the argument is not that costly).

          The series algorithm computes the series defining the
          Artin-Hasse exponential and evaluates it.

          The ``'newton'`` algorithm solves the equation

          .. MATH::

              \\log(AH(x)) = x + \\frac{x^p}{p} + \\frac{x^{p^2}}{p^2} + \\dots

          using a Newton scheme. It runs roughly as fast as the computation
          of the logarithm.

          By default, we use the ``'direct'`` algorithm if a fast algorithm for
          computing the exponential is available.
          If not, we use the ``'newton'`` algorithm if a fast algorithm for
          computing the logarithm is available.
          Otherwise we switch to the ``'series'`` algorithm.

        OUTPUT: the Artin-Hasse exponential of this element

        See :wikipedia:`Artin-Hasse_exponential` for more information.

        EXAMPLES::

            sage: x = Zp(5)(45/7)
            sage: y = x.artin_hasse_exp(); y
            1 + 2*5 + 4*5^2 + 3*5^3 + 5^7 + 2*5^8 + 3*5^10 + 2*5^11 + 2*5^12 +
            2*5^13 + 5^14 + 3*5^17 + 2*5^18 + 2*5^19 + O(5^20)

            sage: y * (-x).artin_hasse_exp()
            1 + O(5^20)

        The function respects your precision::

            sage: x = Zp(3,30)(45/7)
            sage: x.artin_hasse_exp()
            1 + 2*3^2 + 3^4 + 2*3^5 + 3^6 + 2*3^7 + 2*3^8 + 3^9 + 2*3^10 + 3^11 +
            3^13 + 2*3^15 + 2*3^16 + 2*3^17 + 3^19 + 3^20 + 2*3^21 + 3^23 + 3^24 +
            3^26 + 3^27 + 2*3^28 + O(3^30)

        Unless you tell it not to::

            sage: x = Zp(3,30)(45/7)
            sage: x.artin_hasse_exp()
            1 + 2*3^2 + 3^4 + 2*3^5 + 3^6 + 2*3^7 + 2*3^8 + 3^9 + 2*3^10 + 3^11 +
            3^13 + 2*3^15 + 2*3^16 + 2*3^17 + 3^19 + 3^20 + 2*3^21 + 3^23 + 3^24 +
            3^26 + 3^27 + 2*3^28 + O(3^30)
            sage: x.artin_hasse_exp(10)
            1 + 2*3^2 + 3^4 + 2*3^5 + 3^6 + 2*3^7 + 2*3^8 + 3^9 + O(3^10)

        For precision 1 the function just returns 1 since the
        exponential is always a 1-unit::

            sage: x = Zp(3).random_element()
            sage: while x.dist(0) >= 1:
            ....:     x = Zp(3).random_element()
            sage: x.artin_hasse_exp(1)
            1 + O(3)

        TESTS:

        Using Theorem 2.5 of [Conr]_::

            sage: x1 = 5*Zp(5).random_element()
            sage: x2 = 5*Zp(5).random_element()
            sage: y1 = x1.artin_hasse_exp()
            sage: y2 = x2.artin_hasse_exp()
            sage: (y1 - y2).abs() == (x1 - x2).abs()
            True

        Comparing with the formal power series definition::

            sage: x = PowerSeriesRing(QQ, 'x', default_prec=82).gen()
            sage: AH = sum(x**(3**i)/(3**i) for i in range(5)).O(82).exp()
            sage: z = Zp(3)(33/7)
            sage: ahz = AH(z); ahz                                                      # needs sage.libs.ntl
            1 + 2*3 + 3^2 + 3^3 + 2*3^5 + 3^6 + 2*3^7 + 3^9 + 3^11 + 3^12 +
            3^13 + 3^14 + 2*3^15 + 3^16 + 2*3^18 + 2*3^19 + O(3^20)
            sage: ahz - z.artin_hasse_exp()                                             # needs sage.libs.ntl
            O(3^20)

        Out of convergence domain::

            sage: Zp(5)(1).artin_hasse_exp()
            Traceback (most recent call last):
            ...
            ValueError: Artin-Hasse exponential does not converge on this input

        AUTHORS:

        - Mitchell Owen, Sebastian Pancrantz (2012-02): initial version.

        - Xavier Caruso (2018-08): extend to any p-adic rings and fields
          and implement several algorithms."""
    def dwork_expansion(self, bd=..., a=...) -> Any:
        """pAdicGenericElement.dwork_expansion(self, bd=20, a=0)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_generic_element.pyx (starting at line 1182)

        Return the value of a function defined by Dwork.

        Used to compute the `p`-adic Gamma function, see :meth:`gamma`.

        INPUT:

        - ``bd`` -- integer (default: 20); precision bound
        - ``a`` -- integer (default: 0); offset parameter

        OUTPUT: a `p`-adic integer

        .. NOTE::

            This is based on GP code written by Fernando Rodriguez
            Villegas (http://www.ma.utexas.edu/cnt/cnt-frames.html).
            William Stein sped it up for GP
            (http://sage.math.washington.edu/home/wstein/www/home/wbhart/pari-2.4.2.alpha/src/basemath/trans2.c).
            The output is a `p`-adic integer from Dwork's expansion,
            used to compute the `p`-adic gamma function as in [RV2007]_
            section 6.2.
            The coefficients of the expansion are now cached to speed up
            multiple evaluation, as in the trace formula for hypergeometric
            motives.

        EXAMPLES::

            sage: R = Zp(17)
            sage: x = R(5+3*17+13*17^2+6*17^3+12*17^5+10*17^(14)+5*17^(17)+O(17^(19)))
            sage: x.dwork_expansion(18)
            16 + 7*17 + 11*17^2 + 4*17^3 + 8*17^4 + 10*17^5 + 11*17^6 + 6*17^7
            + 17^8 + 8*17^10 + 13*17^11 + 9*17^12 + 15*17^13  + 2*17^14 + 6*17^15
            + 7*17^16 + 6*17^17 + O(17^18)

            sage: R = Zp(5)
            sage: x = R(3*5^2+4*5^3+1*5^4+2*5^5+1*5^(10)+O(5^(20)))
            sage: x.dwork_expansion()
            4 + 4*5 + 4*5^2 + 4*5^3 + 2*5^4 + 4*5^5 + 5^7 + 3*5^9 + 4*5^10 + 3*5^11
            + 5^13 + 4*5^14 + 2*5^15 + 2*5^16 + 2*5^17 + 3*5^18 + O(5^20)

        TESTS:

        This test was added in :issue:`24433`::

            sage: F = Qp(7)
            sage: F(4).gamma()
            6 + O(7^20)
            sage: -F(1).dwork_expansion(a=3)
            6 + 4*7^19 + O(7^20)"""
    def exp(self, aprec=..., algorithm=...) -> Any:
        """pAdicGenericElement.exp(self, aprec=None, algorithm=None)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_generic_element.pyx (starting at line 3106)

        Compute the `p`-adic exponential of this element if the exponential
        series converges.

        INPUT:

        - ``aprec`` -- integer or ``None`` (default: ``None``); if
          specified, computes only up to the indicated precision

        - ``algorithm`` -- ``'generic'``, ``'binary_splitting'``, ``'newton'``
          or ``None`` (default)

          The ``'generic'`` algorithm evaluates naively the series defining the
          exponential, namely

          .. MATH::

              \\exp(x) = 1 + x + x^2/2 + x^3/6 + x^4/24 + \\cdots.

          Its binary complexity is quadratic with respect to the precision.

          The ``'binary_splitting'`` algorithm is faster, it has a quasi-linear
          complexity.

          The ``'newton'`` algorithms solve the equation `\\log(x) =` ``self``
          using a Newton scheme. It runs roughly as fast as the computation
          of the logarithm.

          By default, we use the ``'binary_splitting'`` if it is available.
          If it is not, we use the ``'newton'`` algorithm if a fast algorithm for
          computing the logarithm is available.
          Otherwise we switch to the ``'generic'`` algorithm.

        EXAMPLES:

        :meth:`log` and :meth:`exp` are inverse to each other::

            sage: Z13 = Zp(13, 10)
            sage: a = Z13(14); a
            1 + 13 + O(13^10)
            sage: a.log().exp()
            1 + 13 + O(13^10)

        An error occurs if this is called with an element for which the
        exponential series does not converge::

            sage: Z13.one().exp()
            Traceback (most recent call last):
            ...
            ValueError: Exponential does not converge for that input.

        The next few examples illustrate precision when computing `p`-adic
        exponentials::

            sage: R = Zp(5,10)
            sage: e = R(2*5 + 2*5**2 + 4*5**3 + 3*5**4
            ....:        + 5**5 + 3*5**7 + 2*5**8 + 4*5**9).add_bigoh(10); e
            2*5 + 2*5^2 + 4*5^3 + 3*5^4 + 5^5 + 3*5^7 + 2*5^8 + 4*5^9 + O(5^10)
            sage: e.exp()*R.teichmuller(4)
            4 + 2*5 + 3*5^3 + O(5^10)

        ::

            sage: K = Qp(5,10)
            sage: e = K(2*5 + 2*5**2 + 4*5**3 + 3*5**4
            ....:        + 5**5 + 3*5**7 + 2*5**8 + 4*5**9).add_bigoh(10); e
            2*5 + 2*5^2 + 4*5^3 + 3*5^4 + 5^5 + 3*5^7 + 2*5^8 + 4*5^9 + O(5^10)
            sage: e.exp()*K.teichmuller(4)
            4 + 2*5 + 3*5^3 + O(5^10)

        Logarithms and exponentials in extension fields. First, in an
        Eisenstein extension::

            sage: # needs sage.libs.ntl
            sage: R = Zp(5,5)
            sage: S.<x> = R[]
            sage: f = x^4 + 15*x^2 + 625*x - 5
            sage: W.<w> = R.ext(f)
            sage: z = 1 + w^2 + 4*w^7; z
            1 + w^2 + 4*w^7 + O(w^20)
            sage: z.log().exp()
            1 + w^2 + 4*w^7 + O(w^20)

        Now an unramified example::

            sage: # needs sage.libs.ntl
            sage: R = Zp(5,5)
            sage: S.<x> = R[]
            sage: g = x^3 + 3*x + 3
            sage: A.<a> = R.ext(g)
            sage: b = 1 + 5*(1 + a^2) + 5^3*(3 + 2*a); b
            1 + (a^2 + 1)*5 + (2*a + 3)*5^3 + O(5^5)
            sage: b.log().exp()
            1 + (a^2 + 1)*5 + (2*a + 3)*5^3 + O(5^5)

        TESTS:

        Check that results are consistent over a range of precision::

            sage: max_prec = 40
            sage: p = 3
            sage: K = Zp(p, max_prec)
            sage: full_exp = (K(p)).exp()
            sage: for prec in range(2, max_prec):
            ....:     ll = (K(p).add_bigoh(prec)).exp()
            ....:     assert ll == full_exp
            ....:     assert ll.precision_absolute() == prec
            sage: K = Qp(p, max_prec)
            sage: full_exp = (K(p)).exp()
            sage: for prec in range(2, max_prec):
            ....:     ll = (K(p).add_bigoh(prec)).exp()
            ....:     assert ll == full_exp
            ....:     assert ll.precision_absolute() == prec

        Check that this also works for capped-absolute implementations::

            sage: Z13 = ZpCA(13, 10)
            sage: a = Z13(14); a
            1 + 13 + O(13^10)
            sage: a.log().exp()
            1 + 13 + O(13^10)

            sage: # needs sage.libs.ntl
            sage: R = ZpCA(5,5)
            sage: S.<x> = R[]
            sage: f = x^4 + 15*x^2 + 625*x - 5
            sage: W.<w> = R.ext(f)
            sage: z = 1 + w^2 + 4*w^7; z
            1 + w^2 + 4*w^7 + O(w^20)
            sage: z.log().exp()
            1 + w^2 + 4*w^7 + O(w^20)

        Check that this also works for fixed-mod implementations::

            sage: Z13 = ZpFM(13, 10)
            sage: a = Z13(14); a
            1 + 13
            sage: a.log().exp()
            1 + 13

            sage: # needs sage.libs.ntl
            sage: R = ZpFM(5,5)
            sage: S.<x> = R[]
            sage: f = x^4 + 15*x^2 + 625*x - 5
            sage: W.<w> = R.ext(f)
            sage: z = 1 + w^2 + 4*w^7; z
            1 + w^2 + 4*w^7
            sage: z.log().exp()
            1 + w^2 + 4*w^7

        Some corner cases::

            sage: Z2 = Zp(2, 5)
            sage: Z2(2).exp()
            Traceback (most recent call last):
            ...
            ValueError: Exponential does not converge for that input.

            sage: # needs sage.libs.ntl
            sage: S.<x> = Z2[]
            sage: W.<w> = Z2.ext(x^3-2)
            sage: (w^2).exp()
            Traceback (most recent call last):
            ...
            ValueError: Exponential does not converge for that input.
            sage: (w^3).exp()
            Traceback (most recent call last):
            ...
            ValueError: Exponential does not converge for that input.
            sage: (w^4).exp()
            1 + w^4 + w^5 + w^7 + w^9 + w^10 + w^14 + O(w^15)

        Check that all algorithms output the same result::

            sage: R = Zp(5,50)
            sage: a = 5 * R.random_element()
            sage: bg = a.exp(algorithm='generic')
            sage: bbs = a.exp(algorithm='binary_splitting')
            sage: bn = a.exp(algorithm='newton')
            sage: bg == bbs
            True
            sage: bg == bn
            True

        Performances::

            sage: R = Zp(17,10^5)
            sage: a = 17 * R.random_element()
            sage: b = a.exp()    # should be rather fast

        AUTHORS:

        - Genya Zaytman (2007-02-15)

        - Amnon Besser, Marc Masdeu (2012-02-23): Complete rewrite

        - Julian Rueth (2013-02-14): Added doctests, fixed some corner cases

        - Xavier Caruso (2017-06): Added binary splitting and Newton algorithms"""
    @overload
    def gamma(self, algorithm=...) -> Any:
        """pAdicGenericElement.gamma(self, algorithm='pari')

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_generic_element.pyx (starting at line 1248)

        Return the value of the `p`-adic Gamma function.

        INPUT:

        - ``algorithm`` -- string. Can be set to ``'pari'`` to call
          the PARI function, or ``'sage'`` to call the function
          implemented in Sage. The default is ``'pari'`` since
          PARI is about 10 times faster than Sage.

        OUTPUT: a `p`-adic integer

        .. NOTE::

            This is based on GP code written by Fernando Rodriguez
            Villegas (http://www.ma.utexas.edu/cnt/cnt-frames.html).
            William Stein sped it up for GP
            (http://sage.math.washington.edu/home/wstein/www/home/wbhart/pari-2.4.2.alpha/src/basemath/trans2.c).
            The ``'sage'`` version uses dwork_expansion() to compute the
            `p`-adic gamma function of ``self`` as in [RV2007]_ section 6.2.

        EXAMPLES:

        This example illustrates ``x.gamma()`` for `x` a `p`-adic unit::

            sage: R = Zp(7)
            sage: x = R(2+3*7^2+4*7^3+O(7^20))
            sage: x.gamma('pari')
            1 + 2*7^2 + 4*7^3 + 5*7^4 + 3*7^5 + 7^8 + 7^9 + 4*7^10 + 3*7^12
            + 7^13 + 5*7^14 + 3*7^15 + 2*7^16 + 2*7^17 + 5*7^18 + 4*7^19 + O(7^20)
            sage: x.gamma('sage')
            1 + 2*7^2 + 4*7^3 + 5*7^4 + 3*7^5 + 7^8 + 7^9 + 4*7^10 + 3*7^12
            + 7^13 + 5*7^14 + 3*7^15 + 2*7^16 + 2*7^17 + 5*7^18 + 4*7^19 + O(7^20)
            sage: x.gamma('pari') == x.gamma('sage')
            True

        Now ``x.gamma()`` for `x` a `p`-adic integer but not a unit::

            sage: R = Zp(17)
            sage: x = R(17+17^2+3*17^3+12*17^8+O(17^13))
            sage: x.gamma('pari')
            1 + 12*17 + 13*17^2 + 13*17^3 + 10*17^4 + 7*17^5 + 16*17^7
            + 13*17^9 + 4*17^10 + 9*17^11 + 17^12 + O(17^13)
            sage: x.gamma('sage')
            1 + 12*17 + 13*17^2 + 13*17^3 + 10*17^4 + 7*17^5 + 16*17^7
            + 13*17^9 + 4*17^10 + 9*17^11 + 17^12 + O(17^13)
            sage: x.gamma('pari') == x.gamma('sage')
            True

        Finally, this function is not defined if `x` is not a `p`-adic integer::

            sage: K = Qp(7)
            sage: x = K(7^-5 + 2*7^-4 + 5*7^-3 + 2*7^-2 + 3*7^-1 + 3 + 3*7
            ....:       + 7^3 + 4*7^4 + 5*7^5 + 6*7^8 + 3*7^9 + 6*7^10 + 5*7^11 + 6*7^12
            ....:       + 3*7^13 + 5*7^14 + O(7^15))
            sage: x.gamma()
            Traceback (most recent call last):
            ...
            ValueError: The p-adic gamma function only works on elements of Zp

        TESTS:

        We check that :issue:`23784` is resolved::

            sage: Zp(5)(0).gamma()
            1 + O(5^20)

        Check the cached version of ``dwork_expansion`` from :issue:`24433`::

            sage: p = next_prime(200)
            sage: F = Qp(p)
            sage: l1 = [F(a/(p-1)).gamma(algorithm='pari') for a in range(p-1)]     # long time
            sage: l2 = [F(a/(p-1)).gamma(algorithm='sage') for a in range(p-1)]     # long time
            sage: all(l1[i] == l2[i] for i in range(p-1))  # long time
            True

        The `p`-adic Gamma function has anomalous behavior for the prime 2::

            sage: F = Qp(2)
            sage: x = F(-1) + O(2^2)
            sage: x.gamma(algorithm='pari')
            1 + O(2)
            sage: x.gamma(algorithm='sage')
            1 + O(2)
            sage: x = F(-1) + O(2^3)
            sage: x.gamma(algorithm='pari')
            1 + O(2^3)
            sage: x.gamma(algorithm='sage')
            1 + O(2^3)"""
    @overload
    def gamma(self) -> Any:
        """pAdicGenericElement.gamma(self, algorithm='pari')

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_generic_element.pyx (starting at line 1248)

        Return the value of the `p`-adic Gamma function.

        INPUT:

        - ``algorithm`` -- string. Can be set to ``'pari'`` to call
          the PARI function, or ``'sage'`` to call the function
          implemented in Sage. The default is ``'pari'`` since
          PARI is about 10 times faster than Sage.

        OUTPUT: a `p`-adic integer

        .. NOTE::

            This is based on GP code written by Fernando Rodriguez
            Villegas (http://www.ma.utexas.edu/cnt/cnt-frames.html).
            William Stein sped it up for GP
            (http://sage.math.washington.edu/home/wstein/www/home/wbhart/pari-2.4.2.alpha/src/basemath/trans2.c).
            The ``'sage'`` version uses dwork_expansion() to compute the
            `p`-adic gamma function of ``self`` as in [RV2007]_ section 6.2.

        EXAMPLES:

        This example illustrates ``x.gamma()`` for `x` a `p`-adic unit::

            sage: R = Zp(7)
            sage: x = R(2+3*7^2+4*7^3+O(7^20))
            sage: x.gamma('pari')
            1 + 2*7^2 + 4*7^3 + 5*7^4 + 3*7^5 + 7^8 + 7^9 + 4*7^10 + 3*7^12
            + 7^13 + 5*7^14 + 3*7^15 + 2*7^16 + 2*7^17 + 5*7^18 + 4*7^19 + O(7^20)
            sage: x.gamma('sage')
            1 + 2*7^2 + 4*7^3 + 5*7^4 + 3*7^5 + 7^8 + 7^9 + 4*7^10 + 3*7^12
            + 7^13 + 5*7^14 + 3*7^15 + 2*7^16 + 2*7^17 + 5*7^18 + 4*7^19 + O(7^20)
            sage: x.gamma('pari') == x.gamma('sage')
            True

        Now ``x.gamma()`` for `x` a `p`-adic integer but not a unit::

            sage: R = Zp(17)
            sage: x = R(17+17^2+3*17^3+12*17^8+O(17^13))
            sage: x.gamma('pari')
            1 + 12*17 + 13*17^2 + 13*17^3 + 10*17^4 + 7*17^5 + 16*17^7
            + 13*17^9 + 4*17^10 + 9*17^11 + 17^12 + O(17^13)
            sage: x.gamma('sage')
            1 + 12*17 + 13*17^2 + 13*17^3 + 10*17^4 + 7*17^5 + 16*17^7
            + 13*17^9 + 4*17^10 + 9*17^11 + 17^12 + O(17^13)
            sage: x.gamma('pari') == x.gamma('sage')
            True

        Finally, this function is not defined if `x` is not a `p`-adic integer::

            sage: K = Qp(7)
            sage: x = K(7^-5 + 2*7^-4 + 5*7^-3 + 2*7^-2 + 3*7^-1 + 3 + 3*7
            ....:       + 7^3 + 4*7^4 + 5*7^5 + 6*7^8 + 3*7^9 + 6*7^10 + 5*7^11 + 6*7^12
            ....:       + 3*7^13 + 5*7^14 + O(7^15))
            sage: x.gamma()
            Traceback (most recent call last):
            ...
            ValueError: The p-adic gamma function only works on elements of Zp

        TESTS:

        We check that :issue:`23784` is resolved::

            sage: Zp(5)(0).gamma()
            1 + O(5^20)

        Check the cached version of ``dwork_expansion`` from :issue:`24433`::

            sage: p = next_prime(200)
            sage: F = Qp(p)
            sage: l1 = [F(a/(p-1)).gamma(algorithm='pari') for a in range(p-1)]     # long time
            sage: l2 = [F(a/(p-1)).gamma(algorithm='sage') for a in range(p-1)]     # long time
            sage: all(l1[i] == l2[i] for i in range(p-1))  # long time
            True

        The `p`-adic Gamma function has anomalous behavior for the prime 2::

            sage: F = Qp(2)
            sage: x = F(-1) + O(2^2)
            sage: x.gamma(algorithm='pari')
            1 + O(2)
            sage: x.gamma(algorithm='sage')
            1 + O(2)
            sage: x = F(-1) + O(2^3)
            sage: x.gamma(algorithm='pari')
            1 + O(2^3)
            sage: x.gamma(algorithm='sage')
            1 + O(2^3)"""
    @overload
    def gamma(self) -> Any:
        """pAdicGenericElement.gamma(self, algorithm='pari')

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_generic_element.pyx (starting at line 1248)

        Return the value of the `p`-adic Gamma function.

        INPUT:

        - ``algorithm`` -- string. Can be set to ``'pari'`` to call
          the PARI function, or ``'sage'`` to call the function
          implemented in Sage. The default is ``'pari'`` since
          PARI is about 10 times faster than Sage.

        OUTPUT: a `p`-adic integer

        .. NOTE::

            This is based on GP code written by Fernando Rodriguez
            Villegas (http://www.ma.utexas.edu/cnt/cnt-frames.html).
            William Stein sped it up for GP
            (http://sage.math.washington.edu/home/wstein/www/home/wbhart/pari-2.4.2.alpha/src/basemath/trans2.c).
            The ``'sage'`` version uses dwork_expansion() to compute the
            `p`-adic gamma function of ``self`` as in [RV2007]_ section 6.2.

        EXAMPLES:

        This example illustrates ``x.gamma()`` for `x` a `p`-adic unit::

            sage: R = Zp(7)
            sage: x = R(2+3*7^2+4*7^3+O(7^20))
            sage: x.gamma('pari')
            1 + 2*7^2 + 4*7^3 + 5*7^4 + 3*7^5 + 7^8 + 7^9 + 4*7^10 + 3*7^12
            + 7^13 + 5*7^14 + 3*7^15 + 2*7^16 + 2*7^17 + 5*7^18 + 4*7^19 + O(7^20)
            sage: x.gamma('sage')
            1 + 2*7^2 + 4*7^3 + 5*7^4 + 3*7^5 + 7^8 + 7^9 + 4*7^10 + 3*7^12
            + 7^13 + 5*7^14 + 3*7^15 + 2*7^16 + 2*7^17 + 5*7^18 + 4*7^19 + O(7^20)
            sage: x.gamma('pari') == x.gamma('sage')
            True

        Now ``x.gamma()`` for `x` a `p`-adic integer but not a unit::

            sage: R = Zp(17)
            sage: x = R(17+17^2+3*17^3+12*17^8+O(17^13))
            sage: x.gamma('pari')
            1 + 12*17 + 13*17^2 + 13*17^3 + 10*17^4 + 7*17^5 + 16*17^7
            + 13*17^9 + 4*17^10 + 9*17^11 + 17^12 + O(17^13)
            sage: x.gamma('sage')
            1 + 12*17 + 13*17^2 + 13*17^3 + 10*17^4 + 7*17^5 + 16*17^7
            + 13*17^9 + 4*17^10 + 9*17^11 + 17^12 + O(17^13)
            sage: x.gamma('pari') == x.gamma('sage')
            True

        Finally, this function is not defined if `x` is not a `p`-adic integer::

            sage: K = Qp(7)
            sage: x = K(7^-5 + 2*7^-4 + 5*7^-3 + 2*7^-2 + 3*7^-1 + 3 + 3*7
            ....:       + 7^3 + 4*7^4 + 5*7^5 + 6*7^8 + 3*7^9 + 6*7^10 + 5*7^11 + 6*7^12
            ....:       + 3*7^13 + 5*7^14 + O(7^15))
            sage: x.gamma()
            Traceback (most recent call last):
            ...
            ValueError: The p-adic gamma function only works on elements of Zp

        TESTS:

        We check that :issue:`23784` is resolved::

            sage: Zp(5)(0).gamma()
            1 + O(5^20)

        Check the cached version of ``dwork_expansion`` from :issue:`24433`::

            sage: p = next_prime(200)
            sage: F = Qp(p)
            sage: l1 = [F(a/(p-1)).gamma(algorithm='pari') for a in range(p-1)]     # long time
            sage: l2 = [F(a/(p-1)).gamma(algorithm='sage') for a in range(p-1)]     # long time
            sage: all(l1[i] == l2[i] for i in range(p-1))  # long time
            True

        The `p`-adic Gamma function has anomalous behavior for the prime 2::

            sage: F = Qp(2)
            sage: x = F(-1) + O(2^2)
            sage: x.gamma(algorithm='pari')
            1 + O(2)
            sage: x.gamma(algorithm='sage')
            1 + O(2)
            sage: x = F(-1) + O(2^3)
            sage: x.gamma(algorithm='pari')
            1 + O(2^3)
            sage: x.gamma(algorithm='sage')
            1 + O(2^3)"""
    @overload
    def gamma(self) -> Any:
        """pAdicGenericElement.gamma(self, algorithm='pari')

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_generic_element.pyx (starting at line 1248)

        Return the value of the `p`-adic Gamma function.

        INPUT:

        - ``algorithm`` -- string. Can be set to ``'pari'`` to call
          the PARI function, or ``'sage'`` to call the function
          implemented in Sage. The default is ``'pari'`` since
          PARI is about 10 times faster than Sage.

        OUTPUT: a `p`-adic integer

        .. NOTE::

            This is based on GP code written by Fernando Rodriguez
            Villegas (http://www.ma.utexas.edu/cnt/cnt-frames.html).
            William Stein sped it up for GP
            (http://sage.math.washington.edu/home/wstein/www/home/wbhart/pari-2.4.2.alpha/src/basemath/trans2.c).
            The ``'sage'`` version uses dwork_expansion() to compute the
            `p`-adic gamma function of ``self`` as in [RV2007]_ section 6.2.

        EXAMPLES:

        This example illustrates ``x.gamma()`` for `x` a `p`-adic unit::

            sage: R = Zp(7)
            sage: x = R(2+3*7^2+4*7^3+O(7^20))
            sage: x.gamma('pari')
            1 + 2*7^2 + 4*7^3 + 5*7^4 + 3*7^5 + 7^8 + 7^9 + 4*7^10 + 3*7^12
            + 7^13 + 5*7^14 + 3*7^15 + 2*7^16 + 2*7^17 + 5*7^18 + 4*7^19 + O(7^20)
            sage: x.gamma('sage')
            1 + 2*7^2 + 4*7^3 + 5*7^4 + 3*7^5 + 7^8 + 7^9 + 4*7^10 + 3*7^12
            + 7^13 + 5*7^14 + 3*7^15 + 2*7^16 + 2*7^17 + 5*7^18 + 4*7^19 + O(7^20)
            sage: x.gamma('pari') == x.gamma('sage')
            True

        Now ``x.gamma()`` for `x` a `p`-adic integer but not a unit::

            sage: R = Zp(17)
            sage: x = R(17+17^2+3*17^3+12*17^8+O(17^13))
            sage: x.gamma('pari')
            1 + 12*17 + 13*17^2 + 13*17^3 + 10*17^4 + 7*17^5 + 16*17^7
            + 13*17^9 + 4*17^10 + 9*17^11 + 17^12 + O(17^13)
            sage: x.gamma('sage')
            1 + 12*17 + 13*17^2 + 13*17^3 + 10*17^4 + 7*17^5 + 16*17^7
            + 13*17^9 + 4*17^10 + 9*17^11 + 17^12 + O(17^13)
            sage: x.gamma('pari') == x.gamma('sage')
            True

        Finally, this function is not defined if `x` is not a `p`-adic integer::

            sage: K = Qp(7)
            sage: x = K(7^-5 + 2*7^-4 + 5*7^-3 + 2*7^-2 + 3*7^-1 + 3 + 3*7
            ....:       + 7^3 + 4*7^4 + 5*7^5 + 6*7^8 + 3*7^9 + 6*7^10 + 5*7^11 + 6*7^12
            ....:       + 3*7^13 + 5*7^14 + O(7^15))
            sage: x.gamma()
            Traceback (most recent call last):
            ...
            ValueError: The p-adic gamma function only works on elements of Zp

        TESTS:

        We check that :issue:`23784` is resolved::

            sage: Zp(5)(0).gamma()
            1 + O(5^20)

        Check the cached version of ``dwork_expansion`` from :issue:`24433`::

            sage: p = next_prime(200)
            sage: F = Qp(p)
            sage: l1 = [F(a/(p-1)).gamma(algorithm='pari') for a in range(p-1)]     # long time
            sage: l2 = [F(a/(p-1)).gamma(algorithm='sage') for a in range(p-1)]     # long time
            sage: all(l1[i] == l2[i] for i in range(p-1))  # long time
            True

        The `p`-adic Gamma function has anomalous behavior for the prime 2::

            sage: F = Qp(2)
            sage: x = F(-1) + O(2^2)
            sage: x.gamma(algorithm='pari')
            1 + O(2)
            sage: x.gamma(algorithm='sage')
            1 + O(2)
            sage: x = F(-1) + O(2^3)
            sage: x.gamma(algorithm='pari')
            1 + O(2^3)
            sage: x.gamma(algorithm='sage')
            1 + O(2^3)"""
    @overload
    def gamma(self) -> Any:
        """pAdicGenericElement.gamma(self, algorithm='pari')

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_generic_element.pyx (starting at line 1248)

        Return the value of the `p`-adic Gamma function.

        INPUT:

        - ``algorithm`` -- string. Can be set to ``'pari'`` to call
          the PARI function, or ``'sage'`` to call the function
          implemented in Sage. The default is ``'pari'`` since
          PARI is about 10 times faster than Sage.

        OUTPUT: a `p`-adic integer

        .. NOTE::

            This is based on GP code written by Fernando Rodriguez
            Villegas (http://www.ma.utexas.edu/cnt/cnt-frames.html).
            William Stein sped it up for GP
            (http://sage.math.washington.edu/home/wstein/www/home/wbhart/pari-2.4.2.alpha/src/basemath/trans2.c).
            The ``'sage'`` version uses dwork_expansion() to compute the
            `p`-adic gamma function of ``self`` as in [RV2007]_ section 6.2.

        EXAMPLES:

        This example illustrates ``x.gamma()`` for `x` a `p`-adic unit::

            sage: R = Zp(7)
            sage: x = R(2+3*7^2+4*7^3+O(7^20))
            sage: x.gamma('pari')
            1 + 2*7^2 + 4*7^3 + 5*7^4 + 3*7^5 + 7^8 + 7^9 + 4*7^10 + 3*7^12
            + 7^13 + 5*7^14 + 3*7^15 + 2*7^16 + 2*7^17 + 5*7^18 + 4*7^19 + O(7^20)
            sage: x.gamma('sage')
            1 + 2*7^2 + 4*7^3 + 5*7^4 + 3*7^5 + 7^8 + 7^9 + 4*7^10 + 3*7^12
            + 7^13 + 5*7^14 + 3*7^15 + 2*7^16 + 2*7^17 + 5*7^18 + 4*7^19 + O(7^20)
            sage: x.gamma('pari') == x.gamma('sage')
            True

        Now ``x.gamma()`` for `x` a `p`-adic integer but not a unit::

            sage: R = Zp(17)
            sage: x = R(17+17^2+3*17^3+12*17^8+O(17^13))
            sage: x.gamma('pari')
            1 + 12*17 + 13*17^2 + 13*17^3 + 10*17^4 + 7*17^5 + 16*17^7
            + 13*17^9 + 4*17^10 + 9*17^11 + 17^12 + O(17^13)
            sage: x.gamma('sage')
            1 + 12*17 + 13*17^2 + 13*17^3 + 10*17^4 + 7*17^5 + 16*17^7
            + 13*17^9 + 4*17^10 + 9*17^11 + 17^12 + O(17^13)
            sage: x.gamma('pari') == x.gamma('sage')
            True

        Finally, this function is not defined if `x` is not a `p`-adic integer::

            sage: K = Qp(7)
            sage: x = K(7^-5 + 2*7^-4 + 5*7^-3 + 2*7^-2 + 3*7^-1 + 3 + 3*7
            ....:       + 7^3 + 4*7^4 + 5*7^5 + 6*7^8 + 3*7^9 + 6*7^10 + 5*7^11 + 6*7^12
            ....:       + 3*7^13 + 5*7^14 + O(7^15))
            sage: x.gamma()
            Traceback (most recent call last):
            ...
            ValueError: The p-adic gamma function only works on elements of Zp

        TESTS:

        We check that :issue:`23784` is resolved::

            sage: Zp(5)(0).gamma()
            1 + O(5^20)

        Check the cached version of ``dwork_expansion`` from :issue:`24433`::

            sage: p = next_prime(200)
            sage: F = Qp(p)
            sage: l1 = [F(a/(p-1)).gamma(algorithm='pari') for a in range(p-1)]     # long time
            sage: l2 = [F(a/(p-1)).gamma(algorithm='sage') for a in range(p-1)]     # long time
            sage: all(l1[i] == l2[i] for i in range(p-1))  # long time
            True

        The `p`-adic Gamma function has anomalous behavior for the prime 2::

            sage: F = Qp(2)
            sage: x = F(-1) + O(2^2)
            sage: x.gamma(algorithm='pari')
            1 + O(2)
            sage: x.gamma(algorithm='sage')
            1 + O(2)
            sage: x = F(-1) + O(2^3)
            sage: x.gamma(algorithm='pari')
            1 + O(2^3)
            sage: x.gamma(algorithm='sage')
            1 + O(2^3)"""
    @overload
    def gamma(self, algorithm=...) -> Any:
        """pAdicGenericElement.gamma(self, algorithm='pari')

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_generic_element.pyx (starting at line 1248)

        Return the value of the `p`-adic Gamma function.

        INPUT:

        - ``algorithm`` -- string. Can be set to ``'pari'`` to call
          the PARI function, or ``'sage'`` to call the function
          implemented in Sage. The default is ``'pari'`` since
          PARI is about 10 times faster than Sage.

        OUTPUT: a `p`-adic integer

        .. NOTE::

            This is based on GP code written by Fernando Rodriguez
            Villegas (http://www.ma.utexas.edu/cnt/cnt-frames.html).
            William Stein sped it up for GP
            (http://sage.math.washington.edu/home/wstein/www/home/wbhart/pari-2.4.2.alpha/src/basemath/trans2.c).
            The ``'sage'`` version uses dwork_expansion() to compute the
            `p`-adic gamma function of ``self`` as in [RV2007]_ section 6.2.

        EXAMPLES:

        This example illustrates ``x.gamma()`` for `x` a `p`-adic unit::

            sage: R = Zp(7)
            sage: x = R(2+3*7^2+4*7^3+O(7^20))
            sage: x.gamma('pari')
            1 + 2*7^2 + 4*7^3 + 5*7^4 + 3*7^5 + 7^8 + 7^9 + 4*7^10 + 3*7^12
            + 7^13 + 5*7^14 + 3*7^15 + 2*7^16 + 2*7^17 + 5*7^18 + 4*7^19 + O(7^20)
            sage: x.gamma('sage')
            1 + 2*7^2 + 4*7^3 + 5*7^4 + 3*7^5 + 7^8 + 7^9 + 4*7^10 + 3*7^12
            + 7^13 + 5*7^14 + 3*7^15 + 2*7^16 + 2*7^17 + 5*7^18 + 4*7^19 + O(7^20)
            sage: x.gamma('pari') == x.gamma('sage')
            True

        Now ``x.gamma()`` for `x` a `p`-adic integer but not a unit::

            sage: R = Zp(17)
            sage: x = R(17+17^2+3*17^3+12*17^8+O(17^13))
            sage: x.gamma('pari')
            1 + 12*17 + 13*17^2 + 13*17^3 + 10*17^4 + 7*17^5 + 16*17^7
            + 13*17^9 + 4*17^10 + 9*17^11 + 17^12 + O(17^13)
            sage: x.gamma('sage')
            1 + 12*17 + 13*17^2 + 13*17^3 + 10*17^4 + 7*17^5 + 16*17^7
            + 13*17^9 + 4*17^10 + 9*17^11 + 17^12 + O(17^13)
            sage: x.gamma('pari') == x.gamma('sage')
            True

        Finally, this function is not defined if `x` is not a `p`-adic integer::

            sage: K = Qp(7)
            sage: x = K(7^-5 + 2*7^-4 + 5*7^-3 + 2*7^-2 + 3*7^-1 + 3 + 3*7
            ....:       + 7^3 + 4*7^4 + 5*7^5 + 6*7^8 + 3*7^9 + 6*7^10 + 5*7^11 + 6*7^12
            ....:       + 3*7^13 + 5*7^14 + O(7^15))
            sage: x.gamma()
            Traceback (most recent call last):
            ...
            ValueError: The p-adic gamma function only works on elements of Zp

        TESTS:

        We check that :issue:`23784` is resolved::

            sage: Zp(5)(0).gamma()
            1 + O(5^20)

        Check the cached version of ``dwork_expansion`` from :issue:`24433`::

            sage: p = next_prime(200)
            sage: F = Qp(p)
            sage: l1 = [F(a/(p-1)).gamma(algorithm='pari') for a in range(p-1)]     # long time
            sage: l2 = [F(a/(p-1)).gamma(algorithm='sage') for a in range(p-1)]     # long time
            sage: all(l1[i] == l2[i] for i in range(p-1))  # long time
            True

        The `p`-adic Gamma function has anomalous behavior for the prime 2::

            sage: F = Qp(2)
            sage: x = F(-1) + O(2^2)
            sage: x.gamma(algorithm='pari')
            1 + O(2)
            sage: x.gamma(algorithm='sage')
            1 + O(2)
            sage: x = F(-1) + O(2^3)
            sage: x.gamma(algorithm='pari')
            1 + O(2^3)
            sage: x.gamma(algorithm='sage')
            1 + O(2^3)"""
    @overload
    def gamma(self, algorithm=...) -> Any:
        """pAdicGenericElement.gamma(self, algorithm='pari')

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_generic_element.pyx (starting at line 1248)

        Return the value of the `p`-adic Gamma function.

        INPUT:

        - ``algorithm`` -- string. Can be set to ``'pari'`` to call
          the PARI function, or ``'sage'`` to call the function
          implemented in Sage. The default is ``'pari'`` since
          PARI is about 10 times faster than Sage.

        OUTPUT: a `p`-adic integer

        .. NOTE::

            This is based on GP code written by Fernando Rodriguez
            Villegas (http://www.ma.utexas.edu/cnt/cnt-frames.html).
            William Stein sped it up for GP
            (http://sage.math.washington.edu/home/wstein/www/home/wbhart/pari-2.4.2.alpha/src/basemath/trans2.c).
            The ``'sage'`` version uses dwork_expansion() to compute the
            `p`-adic gamma function of ``self`` as in [RV2007]_ section 6.2.

        EXAMPLES:

        This example illustrates ``x.gamma()`` for `x` a `p`-adic unit::

            sage: R = Zp(7)
            sage: x = R(2+3*7^2+4*7^3+O(7^20))
            sage: x.gamma('pari')
            1 + 2*7^2 + 4*7^3 + 5*7^4 + 3*7^5 + 7^8 + 7^9 + 4*7^10 + 3*7^12
            + 7^13 + 5*7^14 + 3*7^15 + 2*7^16 + 2*7^17 + 5*7^18 + 4*7^19 + O(7^20)
            sage: x.gamma('sage')
            1 + 2*7^2 + 4*7^3 + 5*7^4 + 3*7^5 + 7^8 + 7^9 + 4*7^10 + 3*7^12
            + 7^13 + 5*7^14 + 3*7^15 + 2*7^16 + 2*7^17 + 5*7^18 + 4*7^19 + O(7^20)
            sage: x.gamma('pari') == x.gamma('sage')
            True

        Now ``x.gamma()`` for `x` a `p`-adic integer but not a unit::

            sage: R = Zp(17)
            sage: x = R(17+17^2+3*17^3+12*17^8+O(17^13))
            sage: x.gamma('pari')
            1 + 12*17 + 13*17^2 + 13*17^3 + 10*17^4 + 7*17^5 + 16*17^7
            + 13*17^9 + 4*17^10 + 9*17^11 + 17^12 + O(17^13)
            sage: x.gamma('sage')
            1 + 12*17 + 13*17^2 + 13*17^3 + 10*17^4 + 7*17^5 + 16*17^7
            + 13*17^9 + 4*17^10 + 9*17^11 + 17^12 + O(17^13)
            sage: x.gamma('pari') == x.gamma('sage')
            True

        Finally, this function is not defined if `x` is not a `p`-adic integer::

            sage: K = Qp(7)
            sage: x = K(7^-5 + 2*7^-4 + 5*7^-3 + 2*7^-2 + 3*7^-1 + 3 + 3*7
            ....:       + 7^3 + 4*7^4 + 5*7^5 + 6*7^8 + 3*7^9 + 6*7^10 + 5*7^11 + 6*7^12
            ....:       + 3*7^13 + 5*7^14 + O(7^15))
            sage: x.gamma()
            Traceback (most recent call last):
            ...
            ValueError: The p-adic gamma function only works on elements of Zp

        TESTS:

        We check that :issue:`23784` is resolved::

            sage: Zp(5)(0).gamma()
            1 + O(5^20)

        Check the cached version of ``dwork_expansion`` from :issue:`24433`::

            sage: p = next_prime(200)
            sage: F = Qp(p)
            sage: l1 = [F(a/(p-1)).gamma(algorithm='pari') for a in range(p-1)]     # long time
            sage: l2 = [F(a/(p-1)).gamma(algorithm='sage') for a in range(p-1)]     # long time
            sage: all(l1[i] == l2[i] for i in range(p-1))  # long time
            True

        The `p`-adic Gamma function has anomalous behavior for the prime 2::

            sage: F = Qp(2)
            sage: x = F(-1) + O(2^2)
            sage: x.gamma(algorithm='pari')
            1 + O(2)
            sage: x.gamma(algorithm='sage')
            1 + O(2)
            sage: x = F(-1) + O(2^3)
            sage: x.gamma(algorithm='pari')
            1 + O(2^3)
            sage: x.gamma(algorithm='sage')
            1 + O(2^3)"""
    @overload
    def gamma(self, algorithm=...) -> Any:
        """pAdicGenericElement.gamma(self, algorithm='pari')

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_generic_element.pyx (starting at line 1248)

        Return the value of the `p`-adic Gamma function.

        INPUT:

        - ``algorithm`` -- string. Can be set to ``'pari'`` to call
          the PARI function, or ``'sage'`` to call the function
          implemented in Sage. The default is ``'pari'`` since
          PARI is about 10 times faster than Sage.

        OUTPUT: a `p`-adic integer

        .. NOTE::

            This is based on GP code written by Fernando Rodriguez
            Villegas (http://www.ma.utexas.edu/cnt/cnt-frames.html).
            William Stein sped it up for GP
            (http://sage.math.washington.edu/home/wstein/www/home/wbhart/pari-2.4.2.alpha/src/basemath/trans2.c).
            The ``'sage'`` version uses dwork_expansion() to compute the
            `p`-adic gamma function of ``self`` as in [RV2007]_ section 6.2.

        EXAMPLES:

        This example illustrates ``x.gamma()`` for `x` a `p`-adic unit::

            sage: R = Zp(7)
            sage: x = R(2+3*7^2+4*7^3+O(7^20))
            sage: x.gamma('pari')
            1 + 2*7^2 + 4*7^3 + 5*7^4 + 3*7^5 + 7^8 + 7^9 + 4*7^10 + 3*7^12
            + 7^13 + 5*7^14 + 3*7^15 + 2*7^16 + 2*7^17 + 5*7^18 + 4*7^19 + O(7^20)
            sage: x.gamma('sage')
            1 + 2*7^2 + 4*7^3 + 5*7^4 + 3*7^5 + 7^8 + 7^9 + 4*7^10 + 3*7^12
            + 7^13 + 5*7^14 + 3*7^15 + 2*7^16 + 2*7^17 + 5*7^18 + 4*7^19 + O(7^20)
            sage: x.gamma('pari') == x.gamma('sage')
            True

        Now ``x.gamma()`` for `x` a `p`-adic integer but not a unit::

            sage: R = Zp(17)
            sage: x = R(17+17^2+3*17^3+12*17^8+O(17^13))
            sage: x.gamma('pari')
            1 + 12*17 + 13*17^2 + 13*17^3 + 10*17^4 + 7*17^5 + 16*17^7
            + 13*17^9 + 4*17^10 + 9*17^11 + 17^12 + O(17^13)
            sage: x.gamma('sage')
            1 + 12*17 + 13*17^2 + 13*17^3 + 10*17^4 + 7*17^5 + 16*17^7
            + 13*17^9 + 4*17^10 + 9*17^11 + 17^12 + O(17^13)
            sage: x.gamma('pari') == x.gamma('sage')
            True

        Finally, this function is not defined if `x` is not a `p`-adic integer::

            sage: K = Qp(7)
            sage: x = K(7^-5 + 2*7^-4 + 5*7^-3 + 2*7^-2 + 3*7^-1 + 3 + 3*7
            ....:       + 7^3 + 4*7^4 + 5*7^5 + 6*7^8 + 3*7^9 + 6*7^10 + 5*7^11 + 6*7^12
            ....:       + 3*7^13 + 5*7^14 + O(7^15))
            sage: x.gamma()
            Traceback (most recent call last):
            ...
            ValueError: The p-adic gamma function only works on elements of Zp

        TESTS:

        We check that :issue:`23784` is resolved::

            sage: Zp(5)(0).gamma()
            1 + O(5^20)

        Check the cached version of ``dwork_expansion`` from :issue:`24433`::

            sage: p = next_prime(200)
            sage: F = Qp(p)
            sage: l1 = [F(a/(p-1)).gamma(algorithm='pari') for a in range(p-1)]     # long time
            sage: l2 = [F(a/(p-1)).gamma(algorithm='sage') for a in range(p-1)]     # long time
            sage: all(l1[i] == l2[i] for i in range(p-1))  # long time
            True

        The `p`-adic Gamma function has anomalous behavior for the prime 2::

            sage: F = Qp(2)
            sage: x = F(-1) + O(2^2)
            sage: x.gamma(algorithm='pari')
            1 + O(2)
            sage: x.gamma(algorithm='sage')
            1 + O(2)
            sage: x = F(-1) + O(2^3)
            sage: x.gamma(algorithm='pari')
            1 + O(2^3)
            sage: x.gamma(algorithm='sage')
            1 + O(2^3)"""
    @overload
    def gamma(self, algorithm=...) -> Any:
        """pAdicGenericElement.gamma(self, algorithm='pari')

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_generic_element.pyx (starting at line 1248)

        Return the value of the `p`-adic Gamma function.

        INPUT:

        - ``algorithm`` -- string. Can be set to ``'pari'`` to call
          the PARI function, or ``'sage'`` to call the function
          implemented in Sage. The default is ``'pari'`` since
          PARI is about 10 times faster than Sage.

        OUTPUT: a `p`-adic integer

        .. NOTE::

            This is based on GP code written by Fernando Rodriguez
            Villegas (http://www.ma.utexas.edu/cnt/cnt-frames.html).
            William Stein sped it up for GP
            (http://sage.math.washington.edu/home/wstein/www/home/wbhart/pari-2.4.2.alpha/src/basemath/trans2.c).
            The ``'sage'`` version uses dwork_expansion() to compute the
            `p`-adic gamma function of ``self`` as in [RV2007]_ section 6.2.

        EXAMPLES:

        This example illustrates ``x.gamma()`` for `x` a `p`-adic unit::

            sage: R = Zp(7)
            sage: x = R(2+3*7^2+4*7^3+O(7^20))
            sage: x.gamma('pari')
            1 + 2*7^2 + 4*7^3 + 5*7^4 + 3*7^5 + 7^8 + 7^9 + 4*7^10 + 3*7^12
            + 7^13 + 5*7^14 + 3*7^15 + 2*7^16 + 2*7^17 + 5*7^18 + 4*7^19 + O(7^20)
            sage: x.gamma('sage')
            1 + 2*7^2 + 4*7^3 + 5*7^4 + 3*7^5 + 7^8 + 7^9 + 4*7^10 + 3*7^12
            + 7^13 + 5*7^14 + 3*7^15 + 2*7^16 + 2*7^17 + 5*7^18 + 4*7^19 + O(7^20)
            sage: x.gamma('pari') == x.gamma('sage')
            True

        Now ``x.gamma()`` for `x` a `p`-adic integer but not a unit::

            sage: R = Zp(17)
            sage: x = R(17+17^2+3*17^3+12*17^8+O(17^13))
            sage: x.gamma('pari')
            1 + 12*17 + 13*17^2 + 13*17^3 + 10*17^4 + 7*17^5 + 16*17^7
            + 13*17^9 + 4*17^10 + 9*17^11 + 17^12 + O(17^13)
            sage: x.gamma('sage')
            1 + 12*17 + 13*17^2 + 13*17^3 + 10*17^4 + 7*17^5 + 16*17^7
            + 13*17^9 + 4*17^10 + 9*17^11 + 17^12 + O(17^13)
            sage: x.gamma('pari') == x.gamma('sage')
            True

        Finally, this function is not defined if `x` is not a `p`-adic integer::

            sage: K = Qp(7)
            sage: x = K(7^-5 + 2*7^-4 + 5*7^-3 + 2*7^-2 + 3*7^-1 + 3 + 3*7
            ....:       + 7^3 + 4*7^4 + 5*7^5 + 6*7^8 + 3*7^9 + 6*7^10 + 5*7^11 + 6*7^12
            ....:       + 3*7^13 + 5*7^14 + O(7^15))
            sage: x.gamma()
            Traceback (most recent call last):
            ...
            ValueError: The p-adic gamma function only works on elements of Zp

        TESTS:

        We check that :issue:`23784` is resolved::

            sage: Zp(5)(0).gamma()
            1 + O(5^20)

        Check the cached version of ``dwork_expansion`` from :issue:`24433`::

            sage: p = next_prime(200)
            sage: F = Qp(p)
            sage: l1 = [F(a/(p-1)).gamma(algorithm='pari') for a in range(p-1)]     # long time
            sage: l2 = [F(a/(p-1)).gamma(algorithm='sage') for a in range(p-1)]     # long time
            sage: all(l1[i] == l2[i] for i in range(p-1))  # long time
            True

        The `p`-adic Gamma function has anomalous behavior for the prime 2::

            sage: F = Qp(2)
            sage: x = F(-1) + O(2^2)
            sage: x.gamma(algorithm='pari')
            1 + O(2)
            sage: x.gamma(algorithm='sage')
            1 + O(2)
            sage: x = F(-1) + O(2^3)
            sage: x.gamma(algorithm='pari')
            1 + O(2^3)
            sage: x.gamma(algorithm='sage')
            1 + O(2^3)"""
    @overload
    def gamma(self, algorithm=...) -> Any:
        """pAdicGenericElement.gamma(self, algorithm='pari')

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_generic_element.pyx (starting at line 1248)

        Return the value of the `p`-adic Gamma function.

        INPUT:

        - ``algorithm`` -- string. Can be set to ``'pari'`` to call
          the PARI function, or ``'sage'`` to call the function
          implemented in Sage. The default is ``'pari'`` since
          PARI is about 10 times faster than Sage.

        OUTPUT: a `p`-adic integer

        .. NOTE::

            This is based on GP code written by Fernando Rodriguez
            Villegas (http://www.ma.utexas.edu/cnt/cnt-frames.html).
            William Stein sped it up for GP
            (http://sage.math.washington.edu/home/wstein/www/home/wbhart/pari-2.4.2.alpha/src/basemath/trans2.c).
            The ``'sage'`` version uses dwork_expansion() to compute the
            `p`-adic gamma function of ``self`` as in [RV2007]_ section 6.2.

        EXAMPLES:

        This example illustrates ``x.gamma()`` for `x` a `p`-adic unit::

            sage: R = Zp(7)
            sage: x = R(2+3*7^2+4*7^3+O(7^20))
            sage: x.gamma('pari')
            1 + 2*7^2 + 4*7^3 + 5*7^4 + 3*7^5 + 7^8 + 7^9 + 4*7^10 + 3*7^12
            + 7^13 + 5*7^14 + 3*7^15 + 2*7^16 + 2*7^17 + 5*7^18 + 4*7^19 + O(7^20)
            sage: x.gamma('sage')
            1 + 2*7^2 + 4*7^3 + 5*7^4 + 3*7^5 + 7^8 + 7^9 + 4*7^10 + 3*7^12
            + 7^13 + 5*7^14 + 3*7^15 + 2*7^16 + 2*7^17 + 5*7^18 + 4*7^19 + O(7^20)
            sage: x.gamma('pari') == x.gamma('sage')
            True

        Now ``x.gamma()`` for `x` a `p`-adic integer but not a unit::

            sage: R = Zp(17)
            sage: x = R(17+17^2+3*17^3+12*17^8+O(17^13))
            sage: x.gamma('pari')
            1 + 12*17 + 13*17^2 + 13*17^3 + 10*17^4 + 7*17^5 + 16*17^7
            + 13*17^9 + 4*17^10 + 9*17^11 + 17^12 + O(17^13)
            sage: x.gamma('sage')
            1 + 12*17 + 13*17^2 + 13*17^3 + 10*17^4 + 7*17^5 + 16*17^7
            + 13*17^9 + 4*17^10 + 9*17^11 + 17^12 + O(17^13)
            sage: x.gamma('pari') == x.gamma('sage')
            True

        Finally, this function is not defined if `x` is not a `p`-adic integer::

            sage: K = Qp(7)
            sage: x = K(7^-5 + 2*7^-4 + 5*7^-3 + 2*7^-2 + 3*7^-1 + 3 + 3*7
            ....:       + 7^3 + 4*7^4 + 5*7^5 + 6*7^8 + 3*7^9 + 6*7^10 + 5*7^11 + 6*7^12
            ....:       + 3*7^13 + 5*7^14 + O(7^15))
            sage: x.gamma()
            Traceback (most recent call last):
            ...
            ValueError: The p-adic gamma function only works on elements of Zp

        TESTS:

        We check that :issue:`23784` is resolved::

            sage: Zp(5)(0).gamma()
            1 + O(5^20)

        Check the cached version of ``dwork_expansion`` from :issue:`24433`::

            sage: p = next_prime(200)
            sage: F = Qp(p)
            sage: l1 = [F(a/(p-1)).gamma(algorithm='pari') for a in range(p-1)]     # long time
            sage: l2 = [F(a/(p-1)).gamma(algorithm='sage') for a in range(p-1)]     # long time
            sage: all(l1[i] == l2[i] for i in range(p-1))  # long time
            True

        The `p`-adic Gamma function has anomalous behavior for the prime 2::

            sage: F = Qp(2)
            sage: x = F(-1) + O(2^2)
            sage: x.gamma(algorithm='pari')
            1 + O(2)
            sage: x.gamma(algorithm='sage')
            1 + O(2)
            sage: x = F(-1) + O(2^3)
            sage: x.gamma(algorithm='pari')
            1 + O(2^3)
            sage: x.gamma(algorithm='sage')
            1 + O(2^3)"""
    @overload
    def gamma(self, algorithm=...) -> Any:
        """pAdicGenericElement.gamma(self, algorithm='pari')

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_generic_element.pyx (starting at line 1248)

        Return the value of the `p`-adic Gamma function.

        INPUT:

        - ``algorithm`` -- string. Can be set to ``'pari'`` to call
          the PARI function, or ``'sage'`` to call the function
          implemented in Sage. The default is ``'pari'`` since
          PARI is about 10 times faster than Sage.

        OUTPUT: a `p`-adic integer

        .. NOTE::

            This is based on GP code written by Fernando Rodriguez
            Villegas (http://www.ma.utexas.edu/cnt/cnt-frames.html).
            William Stein sped it up for GP
            (http://sage.math.washington.edu/home/wstein/www/home/wbhart/pari-2.4.2.alpha/src/basemath/trans2.c).
            The ``'sage'`` version uses dwork_expansion() to compute the
            `p`-adic gamma function of ``self`` as in [RV2007]_ section 6.2.

        EXAMPLES:

        This example illustrates ``x.gamma()`` for `x` a `p`-adic unit::

            sage: R = Zp(7)
            sage: x = R(2+3*7^2+4*7^3+O(7^20))
            sage: x.gamma('pari')
            1 + 2*7^2 + 4*7^3 + 5*7^4 + 3*7^5 + 7^8 + 7^9 + 4*7^10 + 3*7^12
            + 7^13 + 5*7^14 + 3*7^15 + 2*7^16 + 2*7^17 + 5*7^18 + 4*7^19 + O(7^20)
            sage: x.gamma('sage')
            1 + 2*7^2 + 4*7^3 + 5*7^4 + 3*7^5 + 7^8 + 7^9 + 4*7^10 + 3*7^12
            + 7^13 + 5*7^14 + 3*7^15 + 2*7^16 + 2*7^17 + 5*7^18 + 4*7^19 + O(7^20)
            sage: x.gamma('pari') == x.gamma('sage')
            True

        Now ``x.gamma()`` for `x` a `p`-adic integer but not a unit::

            sage: R = Zp(17)
            sage: x = R(17+17^2+3*17^3+12*17^8+O(17^13))
            sage: x.gamma('pari')
            1 + 12*17 + 13*17^2 + 13*17^3 + 10*17^4 + 7*17^5 + 16*17^7
            + 13*17^9 + 4*17^10 + 9*17^11 + 17^12 + O(17^13)
            sage: x.gamma('sage')
            1 + 12*17 + 13*17^2 + 13*17^3 + 10*17^4 + 7*17^5 + 16*17^7
            + 13*17^9 + 4*17^10 + 9*17^11 + 17^12 + O(17^13)
            sage: x.gamma('pari') == x.gamma('sage')
            True

        Finally, this function is not defined if `x` is not a `p`-adic integer::

            sage: K = Qp(7)
            sage: x = K(7^-5 + 2*7^-4 + 5*7^-3 + 2*7^-2 + 3*7^-1 + 3 + 3*7
            ....:       + 7^3 + 4*7^4 + 5*7^5 + 6*7^8 + 3*7^9 + 6*7^10 + 5*7^11 + 6*7^12
            ....:       + 3*7^13 + 5*7^14 + O(7^15))
            sage: x.gamma()
            Traceback (most recent call last):
            ...
            ValueError: The p-adic gamma function only works on elements of Zp

        TESTS:

        We check that :issue:`23784` is resolved::

            sage: Zp(5)(0).gamma()
            1 + O(5^20)

        Check the cached version of ``dwork_expansion`` from :issue:`24433`::

            sage: p = next_prime(200)
            sage: F = Qp(p)
            sage: l1 = [F(a/(p-1)).gamma(algorithm='pari') for a in range(p-1)]     # long time
            sage: l2 = [F(a/(p-1)).gamma(algorithm='sage') for a in range(p-1)]     # long time
            sage: all(l1[i] == l2[i] for i in range(p-1))  # long time
            True

        The `p`-adic Gamma function has anomalous behavior for the prime 2::

            sage: F = Qp(2)
            sage: x = F(-1) + O(2^2)
            sage: x.gamma(algorithm='pari')
            1 + O(2)
            sage: x.gamma(algorithm='sage')
            1 + O(2)
            sage: x = F(-1) + O(2^3)
            sage: x.gamma(algorithm='pari')
            1 + O(2^3)
            sage: x.gamma(algorithm='sage')
            1 + O(2^3)"""
    def gcd(self, other) -> Any:
        """pAdicGenericElement.gcd(self, other)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_generic_element.pyx (starting at line 1356)

        Return a greatest common divisor of ``self`` and ``other``.

        INPUT:

        - ``other`` -- an element in the same ring as ``self``

        AUTHORS:

        - Julian Rueth (2012-10-19): initial version

        .. NOTE::

            Since the elements are only given with finite precision,
            their greatest common divisor is in general not unique (not even up
            to units). For example `O(3)` is a representative for the elements
            0 and 3 in the 3-adic ring `\\ZZ_3`. The greatest common
            divisor of `O(3)` and `O(3)` could be (among others) 3 or 0 which
            have different valuation. The algorithm implemented here, will
            return an element of minimal valuation among the possible greatest
            common divisors.

        EXAMPLES:

        The greatest common divisor is either zero or a power of the
        uniformizing parameter::

            sage: R = Zp(3)
            sage: R.zero().gcd(R.zero())
            0
            sage: R(3).gcd(9)
            3 + O(3^21)

        A nonzero result is always lifted to the maximal precision possible in
        the ring::

            sage: a = R(3,2); a
            3 + O(3^2)
            sage: b = R(9,3); b
            3^2 + O(3^3)
            sage: a.gcd(b)
            3 + O(3^21)
            sage: a.gcd(0)
            3 + O(3^21)

        If both elements are zero, then the result is zero with the precision
        set to the smallest of their precisions::

            sage: a = R.zero(); a
            0
            sage: b = R(0,2); b
            O(3^2)
            sage: a.gcd(b)
            O(3^2)

        One could argue that it is mathematically correct to return `9 +
        O(3^{22})` instead. However, this would lead to some confusing
        behaviour::

            sage: alternative_gcd = R(9,22); alternative_gcd
            3^2 + O(3^22)
            sage: a.is_zero()
            True
            sage: b.is_zero()
            True
            sage: alternative_gcd.is_zero()
            False

        If exactly one element is zero, then the result depends on the
        valuation of the other element::

            sage: R(0,3).gcd(3^4)
            O(3^3)
            sage: R(0,4).gcd(3^4)
            O(3^4)
            sage: R(0,5).gcd(3^4)
            3^4 + O(3^24)

        Over a field, the greatest common divisor is either zero (possibly with
        finite precision) or one::

            sage: K = Qp(3)
            sage: K(3).gcd(0)
            1 + O(3^20)
            sage: K.zero().gcd(0)
            0
            sage: K.zero().gcd(K(0,2))
            O(3^2)
            sage: K(3).gcd(4)
            1 + O(3^20)

        TESTS:

        The implementation also works over extensions::

            sage: # needs sage.libs.ntl
            sage: K = Qp(3)
            sage: R.<a> = K[]
            sage: L.<a> = K.extension(a^3-3)
            sage: (a+3).gcd(3)
            1 + O(a^60)
            sage: R = Zp(3)
            sage: S.<a> = R[]
            sage: S.<a> = R.extension(a^3-3)
            sage: (a+3).gcd(3)
            a + O(a^61)
            sage: K = Qp(3)
            sage: R.<a> = K[]
            sage: L.<a> = K.extension(a^2-2)
            sage: (a+3).gcd(3)
            1 + O(3^20)
            sage: R = Zp(3)
            sage: S.<a> = R[]
            sage: S.<a> = R.extension(a^2-2)
            sage: (a+3).gcd(3)
            1 + O(3^20)

        For elements with a fixed modulus::

            sage: R = ZpFM(3)
            sage: R(3).gcd(9)
            3

        And elements with a capped absolute precision::

            sage: R = ZpCA(3)
            sage: R(3).gcd(9)
            3 + O(3^20)"""
    @overload
    def is_prime(self) -> Any:
        """pAdicGenericElement.is_prime(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_generic_element.pyx (starting at line 2109)

        Return whether this element is prime in its parent.

        EXAMPLES::

            sage: A = Zp(2)
            sage: A(1).is_prime()
            False
            sage: A(2).is_prime()
            True

            sage: K = A.fraction_field()
            sage: K(2).is_prime()
            False

        ::

            sage: # needs sage.libs.ntl
            sage: x = polygen(ZZ, 'x')
            sage: B.<pi> = A.extension(x^5 - 2)
            sage: pi.is_prime()                                                         # needs sage.symbolic
            True
            sage: B(2).is_prime()
            False"""
    @overload
    def is_prime(self) -> Any:
        """pAdicGenericElement.is_prime(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_generic_element.pyx (starting at line 2109)

        Return whether this element is prime in its parent.

        EXAMPLES::

            sage: A = Zp(2)
            sage: A(1).is_prime()
            False
            sage: A(2).is_prime()
            True

            sage: K = A.fraction_field()
            sage: K(2).is_prime()
            False

        ::

            sage: # needs sage.libs.ntl
            sage: x = polygen(ZZ, 'x')
            sage: B.<pi> = A.extension(x^5 - 2)
            sage: pi.is_prime()                                                         # needs sage.symbolic
            True
            sage: B(2).is_prime()
            False"""
    @overload
    def is_prime(self) -> Any:
        """pAdicGenericElement.is_prime(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_generic_element.pyx (starting at line 2109)

        Return whether this element is prime in its parent.

        EXAMPLES::

            sage: A = Zp(2)
            sage: A(1).is_prime()
            False
            sage: A(2).is_prime()
            True

            sage: K = A.fraction_field()
            sage: K(2).is_prime()
            False

        ::

            sage: # needs sage.libs.ntl
            sage: x = polygen(ZZ, 'x')
            sage: B.<pi> = A.extension(x^5 - 2)
            sage: pi.is_prime()                                                         # needs sage.symbolic
            True
            sage: B(2).is_prime()
            False"""
    @overload
    def is_prime(self) -> Any:
        """pAdicGenericElement.is_prime(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_generic_element.pyx (starting at line 2109)

        Return whether this element is prime in its parent.

        EXAMPLES::

            sage: A = Zp(2)
            sage: A(1).is_prime()
            False
            sage: A(2).is_prime()
            True

            sage: K = A.fraction_field()
            sage: K(2).is_prime()
            False

        ::

            sage: # needs sage.libs.ntl
            sage: x = polygen(ZZ, 'x')
            sage: B.<pi> = A.extension(x^5 - 2)
            sage: pi.is_prime()                                                         # needs sage.symbolic
            True
            sage: B(2).is_prime()
            False"""
    @overload
    def is_prime(self) -> Any:
        """pAdicGenericElement.is_prime(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_generic_element.pyx (starting at line 2109)

        Return whether this element is prime in its parent.

        EXAMPLES::

            sage: A = Zp(2)
            sage: A(1).is_prime()
            False
            sage: A(2).is_prime()
            True

            sage: K = A.fraction_field()
            sage: K(2).is_prime()
            False

        ::

            sage: # needs sage.libs.ntl
            sage: x = polygen(ZZ, 'x')
            sage: B.<pi> = A.extension(x^5 - 2)
            sage: pi.is_prime()                                                         # needs sage.symbolic
            True
            sage: B(2).is_prime()
            False"""
    @overload
    def is_prime(self) -> Any:
        """pAdicGenericElement.is_prime(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_generic_element.pyx (starting at line 2109)

        Return whether this element is prime in its parent.

        EXAMPLES::

            sage: A = Zp(2)
            sage: A(1).is_prime()
            False
            sage: A(2).is_prime()
            True

            sage: K = A.fraction_field()
            sage: K(2).is_prime()
            False

        ::

            sage: # needs sage.libs.ntl
            sage: x = polygen(ZZ, 'x')
            sage: B.<pi> = A.extension(x^5 - 2)
            sage: pi.is_prime()                                                         # needs sage.symbolic
            True
            sage: B(2).is_prime()
            False"""
    @overload
    def is_square(self) -> Any:
        """pAdicGenericElement.is_square(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_generic_element.pyx (starting at line 1675)

        Return whether this element is a square.

        INPUT:

        - ``self`` -- a `p`-adic element

        EXAMPLES::

            sage: R = Zp(3,20,'capped-rel')
            sage: R(0).is_square()
            True
            sage: R(1).is_square()
            True
            sage: R(2).is_square()
            False

        TESTS::

            sage: R(3).is_square()
            False
            sage: R(4).is_square()
            True
            sage: R(6).is_square()
            False
            sage: R(9).is_square()
            True

            sage: R2 = Zp(2,20,'capped-rel')
            sage: R2(0).is_square()
            True
            sage: R2(1).is_square()
            True
            sage: R2(2).is_square()
            False
            sage: R2(3).is_square()
            False
            sage: R2(4).is_square()
            True
            sage: R2(5).is_square()
            False
            sage: R2(6).is_square()
            False
            sage: R2(7).is_square()
            False
            sage: R2(8).is_square()
            False
            sage: R2(9).is_square()
            True

            sage: K = Qp(3,20,'capped-rel')
            sage: K(0).is_square()
            True
            sage: K(1).is_square()
            True
            sage: K(2).is_square()
            False
            sage: K(3).is_square()
            False
            sage: K(4).is_square()
            True
            sage: K(6).is_square()
            False
            sage: K(9).is_square()
            True
            sage: K(1/3).is_square()
            False
            sage: K(1/9).is_square()
            True

            sage: K2 = Qp(2,20,'capped-rel')
            sage: K2(0).is_square()
            True
            sage: K2(1).is_square()
            True
            sage: K2(2).is_square()
            False
            sage: K2(3).is_square()
            False
            sage: K2(4).is_square()
            True
            sage: K2(5).is_square()
            False
            sage: K2(6).is_square()
            False
            sage: K2(7).is_square()
            False
            sage: K2(8).is_square()
            False
            sage: K2(9).is_square()
            True
            sage: K2(1/2).is_square()
            False
            sage: K2(1/4).is_square()
            True"""
    @overload
    def is_square(self) -> Any:
        """pAdicGenericElement.is_square(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_generic_element.pyx (starting at line 1675)

        Return whether this element is a square.

        INPUT:

        - ``self`` -- a `p`-adic element

        EXAMPLES::

            sage: R = Zp(3,20,'capped-rel')
            sage: R(0).is_square()
            True
            sage: R(1).is_square()
            True
            sage: R(2).is_square()
            False

        TESTS::

            sage: R(3).is_square()
            False
            sage: R(4).is_square()
            True
            sage: R(6).is_square()
            False
            sage: R(9).is_square()
            True

            sage: R2 = Zp(2,20,'capped-rel')
            sage: R2(0).is_square()
            True
            sage: R2(1).is_square()
            True
            sage: R2(2).is_square()
            False
            sage: R2(3).is_square()
            False
            sage: R2(4).is_square()
            True
            sage: R2(5).is_square()
            False
            sage: R2(6).is_square()
            False
            sage: R2(7).is_square()
            False
            sage: R2(8).is_square()
            False
            sage: R2(9).is_square()
            True

            sage: K = Qp(3,20,'capped-rel')
            sage: K(0).is_square()
            True
            sage: K(1).is_square()
            True
            sage: K(2).is_square()
            False
            sage: K(3).is_square()
            False
            sage: K(4).is_square()
            True
            sage: K(6).is_square()
            False
            sage: K(9).is_square()
            True
            sage: K(1/3).is_square()
            False
            sage: K(1/9).is_square()
            True

            sage: K2 = Qp(2,20,'capped-rel')
            sage: K2(0).is_square()
            True
            sage: K2(1).is_square()
            True
            sage: K2(2).is_square()
            False
            sage: K2(3).is_square()
            False
            sage: K2(4).is_square()
            True
            sage: K2(5).is_square()
            False
            sage: K2(6).is_square()
            False
            sage: K2(7).is_square()
            False
            sage: K2(8).is_square()
            False
            sage: K2(9).is_square()
            True
            sage: K2(1/2).is_square()
            False
            sage: K2(1/4).is_square()
            True"""
    @overload
    def is_square(self) -> Any:
        """pAdicGenericElement.is_square(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_generic_element.pyx (starting at line 1675)

        Return whether this element is a square.

        INPUT:

        - ``self`` -- a `p`-adic element

        EXAMPLES::

            sage: R = Zp(3,20,'capped-rel')
            sage: R(0).is_square()
            True
            sage: R(1).is_square()
            True
            sage: R(2).is_square()
            False

        TESTS::

            sage: R(3).is_square()
            False
            sage: R(4).is_square()
            True
            sage: R(6).is_square()
            False
            sage: R(9).is_square()
            True

            sage: R2 = Zp(2,20,'capped-rel')
            sage: R2(0).is_square()
            True
            sage: R2(1).is_square()
            True
            sage: R2(2).is_square()
            False
            sage: R2(3).is_square()
            False
            sage: R2(4).is_square()
            True
            sage: R2(5).is_square()
            False
            sage: R2(6).is_square()
            False
            sage: R2(7).is_square()
            False
            sage: R2(8).is_square()
            False
            sage: R2(9).is_square()
            True

            sage: K = Qp(3,20,'capped-rel')
            sage: K(0).is_square()
            True
            sage: K(1).is_square()
            True
            sage: K(2).is_square()
            False
            sage: K(3).is_square()
            False
            sage: K(4).is_square()
            True
            sage: K(6).is_square()
            False
            sage: K(9).is_square()
            True
            sage: K(1/3).is_square()
            False
            sage: K(1/9).is_square()
            True

            sage: K2 = Qp(2,20,'capped-rel')
            sage: K2(0).is_square()
            True
            sage: K2(1).is_square()
            True
            sage: K2(2).is_square()
            False
            sage: K2(3).is_square()
            False
            sage: K2(4).is_square()
            True
            sage: K2(5).is_square()
            False
            sage: K2(6).is_square()
            False
            sage: K2(7).is_square()
            False
            sage: K2(8).is_square()
            False
            sage: K2(9).is_square()
            True
            sage: K2(1/2).is_square()
            False
            sage: K2(1/4).is_square()
            True"""
    @overload
    def is_square(self) -> Any:
        """pAdicGenericElement.is_square(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_generic_element.pyx (starting at line 1675)

        Return whether this element is a square.

        INPUT:

        - ``self`` -- a `p`-adic element

        EXAMPLES::

            sage: R = Zp(3,20,'capped-rel')
            sage: R(0).is_square()
            True
            sage: R(1).is_square()
            True
            sage: R(2).is_square()
            False

        TESTS::

            sage: R(3).is_square()
            False
            sage: R(4).is_square()
            True
            sage: R(6).is_square()
            False
            sage: R(9).is_square()
            True

            sage: R2 = Zp(2,20,'capped-rel')
            sage: R2(0).is_square()
            True
            sage: R2(1).is_square()
            True
            sage: R2(2).is_square()
            False
            sage: R2(3).is_square()
            False
            sage: R2(4).is_square()
            True
            sage: R2(5).is_square()
            False
            sage: R2(6).is_square()
            False
            sage: R2(7).is_square()
            False
            sage: R2(8).is_square()
            False
            sage: R2(9).is_square()
            True

            sage: K = Qp(3,20,'capped-rel')
            sage: K(0).is_square()
            True
            sage: K(1).is_square()
            True
            sage: K(2).is_square()
            False
            sage: K(3).is_square()
            False
            sage: K(4).is_square()
            True
            sage: K(6).is_square()
            False
            sage: K(9).is_square()
            True
            sage: K(1/3).is_square()
            False
            sage: K(1/9).is_square()
            True

            sage: K2 = Qp(2,20,'capped-rel')
            sage: K2(0).is_square()
            True
            sage: K2(1).is_square()
            True
            sage: K2(2).is_square()
            False
            sage: K2(3).is_square()
            False
            sage: K2(4).is_square()
            True
            sage: K2(5).is_square()
            False
            sage: K2(6).is_square()
            False
            sage: K2(7).is_square()
            False
            sage: K2(8).is_square()
            False
            sage: K2(9).is_square()
            True
            sage: K2(1/2).is_square()
            False
            sage: K2(1/4).is_square()
            True"""
    @overload
    def is_square(self) -> Any:
        """pAdicGenericElement.is_square(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_generic_element.pyx (starting at line 1675)

        Return whether this element is a square.

        INPUT:

        - ``self`` -- a `p`-adic element

        EXAMPLES::

            sage: R = Zp(3,20,'capped-rel')
            sage: R(0).is_square()
            True
            sage: R(1).is_square()
            True
            sage: R(2).is_square()
            False

        TESTS::

            sage: R(3).is_square()
            False
            sage: R(4).is_square()
            True
            sage: R(6).is_square()
            False
            sage: R(9).is_square()
            True

            sage: R2 = Zp(2,20,'capped-rel')
            sage: R2(0).is_square()
            True
            sage: R2(1).is_square()
            True
            sage: R2(2).is_square()
            False
            sage: R2(3).is_square()
            False
            sage: R2(4).is_square()
            True
            sage: R2(5).is_square()
            False
            sage: R2(6).is_square()
            False
            sage: R2(7).is_square()
            False
            sage: R2(8).is_square()
            False
            sage: R2(9).is_square()
            True

            sage: K = Qp(3,20,'capped-rel')
            sage: K(0).is_square()
            True
            sage: K(1).is_square()
            True
            sage: K(2).is_square()
            False
            sage: K(3).is_square()
            False
            sage: K(4).is_square()
            True
            sage: K(6).is_square()
            False
            sage: K(9).is_square()
            True
            sage: K(1/3).is_square()
            False
            sage: K(1/9).is_square()
            True

            sage: K2 = Qp(2,20,'capped-rel')
            sage: K2(0).is_square()
            True
            sage: K2(1).is_square()
            True
            sage: K2(2).is_square()
            False
            sage: K2(3).is_square()
            False
            sage: K2(4).is_square()
            True
            sage: K2(5).is_square()
            False
            sage: K2(6).is_square()
            False
            sage: K2(7).is_square()
            False
            sage: K2(8).is_square()
            False
            sage: K2(9).is_square()
            True
            sage: K2(1/2).is_square()
            False
            sage: K2(1/4).is_square()
            True"""
    @overload
    def is_square(self) -> Any:
        """pAdicGenericElement.is_square(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_generic_element.pyx (starting at line 1675)

        Return whether this element is a square.

        INPUT:

        - ``self`` -- a `p`-adic element

        EXAMPLES::

            sage: R = Zp(3,20,'capped-rel')
            sage: R(0).is_square()
            True
            sage: R(1).is_square()
            True
            sage: R(2).is_square()
            False

        TESTS::

            sage: R(3).is_square()
            False
            sage: R(4).is_square()
            True
            sage: R(6).is_square()
            False
            sage: R(9).is_square()
            True

            sage: R2 = Zp(2,20,'capped-rel')
            sage: R2(0).is_square()
            True
            sage: R2(1).is_square()
            True
            sage: R2(2).is_square()
            False
            sage: R2(3).is_square()
            False
            sage: R2(4).is_square()
            True
            sage: R2(5).is_square()
            False
            sage: R2(6).is_square()
            False
            sage: R2(7).is_square()
            False
            sage: R2(8).is_square()
            False
            sage: R2(9).is_square()
            True

            sage: K = Qp(3,20,'capped-rel')
            sage: K(0).is_square()
            True
            sage: K(1).is_square()
            True
            sage: K(2).is_square()
            False
            sage: K(3).is_square()
            False
            sage: K(4).is_square()
            True
            sage: K(6).is_square()
            False
            sage: K(9).is_square()
            True
            sage: K(1/3).is_square()
            False
            sage: K(1/9).is_square()
            True

            sage: K2 = Qp(2,20,'capped-rel')
            sage: K2(0).is_square()
            True
            sage: K2(1).is_square()
            True
            sage: K2(2).is_square()
            False
            sage: K2(3).is_square()
            False
            sage: K2(4).is_square()
            True
            sage: K2(5).is_square()
            False
            sage: K2(6).is_square()
            False
            sage: K2(7).is_square()
            False
            sage: K2(8).is_square()
            False
            sage: K2(9).is_square()
            True
            sage: K2(1/2).is_square()
            False
            sage: K2(1/4).is_square()
            True"""
    @overload
    def is_square(self) -> Any:
        """pAdicGenericElement.is_square(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_generic_element.pyx (starting at line 1675)

        Return whether this element is a square.

        INPUT:

        - ``self`` -- a `p`-adic element

        EXAMPLES::

            sage: R = Zp(3,20,'capped-rel')
            sage: R(0).is_square()
            True
            sage: R(1).is_square()
            True
            sage: R(2).is_square()
            False

        TESTS::

            sage: R(3).is_square()
            False
            sage: R(4).is_square()
            True
            sage: R(6).is_square()
            False
            sage: R(9).is_square()
            True

            sage: R2 = Zp(2,20,'capped-rel')
            sage: R2(0).is_square()
            True
            sage: R2(1).is_square()
            True
            sage: R2(2).is_square()
            False
            sage: R2(3).is_square()
            False
            sage: R2(4).is_square()
            True
            sage: R2(5).is_square()
            False
            sage: R2(6).is_square()
            False
            sage: R2(7).is_square()
            False
            sage: R2(8).is_square()
            False
            sage: R2(9).is_square()
            True

            sage: K = Qp(3,20,'capped-rel')
            sage: K(0).is_square()
            True
            sage: K(1).is_square()
            True
            sage: K(2).is_square()
            False
            sage: K(3).is_square()
            False
            sage: K(4).is_square()
            True
            sage: K(6).is_square()
            False
            sage: K(9).is_square()
            True
            sage: K(1/3).is_square()
            False
            sage: K(1/9).is_square()
            True

            sage: K2 = Qp(2,20,'capped-rel')
            sage: K2(0).is_square()
            True
            sage: K2(1).is_square()
            True
            sage: K2(2).is_square()
            False
            sage: K2(3).is_square()
            False
            sage: K2(4).is_square()
            True
            sage: K2(5).is_square()
            False
            sage: K2(6).is_square()
            False
            sage: K2(7).is_square()
            False
            sage: K2(8).is_square()
            False
            sage: K2(9).is_square()
            True
            sage: K2(1/2).is_square()
            False
            sage: K2(1/4).is_square()
            True"""
    @overload
    def is_square(self) -> Any:
        """pAdicGenericElement.is_square(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_generic_element.pyx (starting at line 1675)

        Return whether this element is a square.

        INPUT:

        - ``self`` -- a `p`-adic element

        EXAMPLES::

            sage: R = Zp(3,20,'capped-rel')
            sage: R(0).is_square()
            True
            sage: R(1).is_square()
            True
            sage: R(2).is_square()
            False

        TESTS::

            sage: R(3).is_square()
            False
            sage: R(4).is_square()
            True
            sage: R(6).is_square()
            False
            sage: R(9).is_square()
            True

            sage: R2 = Zp(2,20,'capped-rel')
            sage: R2(0).is_square()
            True
            sage: R2(1).is_square()
            True
            sage: R2(2).is_square()
            False
            sage: R2(3).is_square()
            False
            sage: R2(4).is_square()
            True
            sage: R2(5).is_square()
            False
            sage: R2(6).is_square()
            False
            sage: R2(7).is_square()
            False
            sage: R2(8).is_square()
            False
            sage: R2(9).is_square()
            True

            sage: K = Qp(3,20,'capped-rel')
            sage: K(0).is_square()
            True
            sage: K(1).is_square()
            True
            sage: K(2).is_square()
            False
            sage: K(3).is_square()
            False
            sage: K(4).is_square()
            True
            sage: K(6).is_square()
            False
            sage: K(9).is_square()
            True
            sage: K(1/3).is_square()
            False
            sage: K(1/9).is_square()
            True

            sage: K2 = Qp(2,20,'capped-rel')
            sage: K2(0).is_square()
            True
            sage: K2(1).is_square()
            True
            sage: K2(2).is_square()
            False
            sage: K2(3).is_square()
            False
            sage: K2(4).is_square()
            True
            sage: K2(5).is_square()
            False
            sage: K2(6).is_square()
            False
            sage: K2(7).is_square()
            False
            sage: K2(8).is_square()
            False
            sage: K2(9).is_square()
            True
            sage: K2(1/2).is_square()
            False
            sage: K2(1/4).is_square()
            True"""
    @overload
    def is_square(self) -> Any:
        """pAdicGenericElement.is_square(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_generic_element.pyx (starting at line 1675)

        Return whether this element is a square.

        INPUT:

        - ``self`` -- a `p`-adic element

        EXAMPLES::

            sage: R = Zp(3,20,'capped-rel')
            sage: R(0).is_square()
            True
            sage: R(1).is_square()
            True
            sage: R(2).is_square()
            False

        TESTS::

            sage: R(3).is_square()
            False
            sage: R(4).is_square()
            True
            sage: R(6).is_square()
            False
            sage: R(9).is_square()
            True

            sage: R2 = Zp(2,20,'capped-rel')
            sage: R2(0).is_square()
            True
            sage: R2(1).is_square()
            True
            sage: R2(2).is_square()
            False
            sage: R2(3).is_square()
            False
            sage: R2(4).is_square()
            True
            sage: R2(5).is_square()
            False
            sage: R2(6).is_square()
            False
            sage: R2(7).is_square()
            False
            sage: R2(8).is_square()
            False
            sage: R2(9).is_square()
            True

            sage: K = Qp(3,20,'capped-rel')
            sage: K(0).is_square()
            True
            sage: K(1).is_square()
            True
            sage: K(2).is_square()
            False
            sage: K(3).is_square()
            False
            sage: K(4).is_square()
            True
            sage: K(6).is_square()
            False
            sage: K(9).is_square()
            True
            sage: K(1/3).is_square()
            False
            sage: K(1/9).is_square()
            True

            sage: K2 = Qp(2,20,'capped-rel')
            sage: K2(0).is_square()
            True
            sage: K2(1).is_square()
            True
            sage: K2(2).is_square()
            False
            sage: K2(3).is_square()
            False
            sage: K2(4).is_square()
            True
            sage: K2(5).is_square()
            False
            sage: K2(6).is_square()
            False
            sage: K2(7).is_square()
            False
            sage: K2(8).is_square()
            False
            sage: K2(9).is_square()
            True
            sage: K2(1/2).is_square()
            False
            sage: K2(1/4).is_square()
            True"""
    @overload
    def is_square(self) -> Any:
        """pAdicGenericElement.is_square(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_generic_element.pyx (starting at line 1675)

        Return whether this element is a square.

        INPUT:

        - ``self`` -- a `p`-adic element

        EXAMPLES::

            sage: R = Zp(3,20,'capped-rel')
            sage: R(0).is_square()
            True
            sage: R(1).is_square()
            True
            sage: R(2).is_square()
            False

        TESTS::

            sage: R(3).is_square()
            False
            sage: R(4).is_square()
            True
            sage: R(6).is_square()
            False
            sage: R(9).is_square()
            True

            sage: R2 = Zp(2,20,'capped-rel')
            sage: R2(0).is_square()
            True
            sage: R2(1).is_square()
            True
            sage: R2(2).is_square()
            False
            sage: R2(3).is_square()
            False
            sage: R2(4).is_square()
            True
            sage: R2(5).is_square()
            False
            sage: R2(6).is_square()
            False
            sage: R2(7).is_square()
            False
            sage: R2(8).is_square()
            False
            sage: R2(9).is_square()
            True

            sage: K = Qp(3,20,'capped-rel')
            sage: K(0).is_square()
            True
            sage: K(1).is_square()
            True
            sage: K(2).is_square()
            False
            sage: K(3).is_square()
            False
            sage: K(4).is_square()
            True
            sage: K(6).is_square()
            False
            sage: K(9).is_square()
            True
            sage: K(1/3).is_square()
            False
            sage: K(1/9).is_square()
            True

            sage: K2 = Qp(2,20,'capped-rel')
            sage: K2(0).is_square()
            True
            sage: K2(1).is_square()
            True
            sage: K2(2).is_square()
            False
            sage: K2(3).is_square()
            False
            sage: K2(4).is_square()
            True
            sage: K2(5).is_square()
            False
            sage: K2(6).is_square()
            False
            sage: K2(7).is_square()
            False
            sage: K2(8).is_square()
            False
            sage: K2(9).is_square()
            True
            sage: K2(1/2).is_square()
            False
            sage: K2(1/4).is_square()
            True"""
    @overload
    def is_square(self) -> Any:
        """pAdicGenericElement.is_square(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_generic_element.pyx (starting at line 1675)

        Return whether this element is a square.

        INPUT:

        - ``self`` -- a `p`-adic element

        EXAMPLES::

            sage: R = Zp(3,20,'capped-rel')
            sage: R(0).is_square()
            True
            sage: R(1).is_square()
            True
            sage: R(2).is_square()
            False

        TESTS::

            sage: R(3).is_square()
            False
            sage: R(4).is_square()
            True
            sage: R(6).is_square()
            False
            sage: R(9).is_square()
            True

            sage: R2 = Zp(2,20,'capped-rel')
            sage: R2(0).is_square()
            True
            sage: R2(1).is_square()
            True
            sage: R2(2).is_square()
            False
            sage: R2(3).is_square()
            False
            sage: R2(4).is_square()
            True
            sage: R2(5).is_square()
            False
            sage: R2(6).is_square()
            False
            sage: R2(7).is_square()
            False
            sage: R2(8).is_square()
            False
            sage: R2(9).is_square()
            True

            sage: K = Qp(3,20,'capped-rel')
            sage: K(0).is_square()
            True
            sage: K(1).is_square()
            True
            sage: K(2).is_square()
            False
            sage: K(3).is_square()
            False
            sage: K(4).is_square()
            True
            sage: K(6).is_square()
            False
            sage: K(9).is_square()
            True
            sage: K(1/3).is_square()
            False
            sage: K(1/9).is_square()
            True

            sage: K2 = Qp(2,20,'capped-rel')
            sage: K2(0).is_square()
            True
            sage: K2(1).is_square()
            True
            sage: K2(2).is_square()
            False
            sage: K2(3).is_square()
            False
            sage: K2(4).is_square()
            True
            sage: K2(5).is_square()
            False
            sage: K2(6).is_square()
            False
            sage: K2(7).is_square()
            False
            sage: K2(8).is_square()
            False
            sage: K2(9).is_square()
            True
            sage: K2(1/2).is_square()
            False
            sage: K2(1/4).is_square()
            True"""
    @overload
    def is_square(self) -> Any:
        """pAdicGenericElement.is_square(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_generic_element.pyx (starting at line 1675)

        Return whether this element is a square.

        INPUT:

        - ``self`` -- a `p`-adic element

        EXAMPLES::

            sage: R = Zp(3,20,'capped-rel')
            sage: R(0).is_square()
            True
            sage: R(1).is_square()
            True
            sage: R(2).is_square()
            False

        TESTS::

            sage: R(3).is_square()
            False
            sage: R(4).is_square()
            True
            sage: R(6).is_square()
            False
            sage: R(9).is_square()
            True

            sage: R2 = Zp(2,20,'capped-rel')
            sage: R2(0).is_square()
            True
            sage: R2(1).is_square()
            True
            sage: R2(2).is_square()
            False
            sage: R2(3).is_square()
            False
            sage: R2(4).is_square()
            True
            sage: R2(5).is_square()
            False
            sage: R2(6).is_square()
            False
            sage: R2(7).is_square()
            False
            sage: R2(8).is_square()
            False
            sage: R2(9).is_square()
            True

            sage: K = Qp(3,20,'capped-rel')
            sage: K(0).is_square()
            True
            sage: K(1).is_square()
            True
            sage: K(2).is_square()
            False
            sage: K(3).is_square()
            False
            sage: K(4).is_square()
            True
            sage: K(6).is_square()
            False
            sage: K(9).is_square()
            True
            sage: K(1/3).is_square()
            False
            sage: K(1/9).is_square()
            True

            sage: K2 = Qp(2,20,'capped-rel')
            sage: K2(0).is_square()
            True
            sage: K2(1).is_square()
            True
            sage: K2(2).is_square()
            False
            sage: K2(3).is_square()
            False
            sage: K2(4).is_square()
            True
            sage: K2(5).is_square()
            False
            sage: K2(6).is_square()
            False
            sage: K2(7).is_square()
            False
            sage: K2(8).is_square()
            False
            sage: K2(9).is_square()
            True
            sage: K2(1/2).is_square()
            False
            sage: K2(1/4).is_square()
            True"""
    @overload
    def is_square(self) -> Any:
        """pAdicGenericElement.is_square(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_generic_element.pyx (starting at line 1675)

        Return whether this element is a square.

        INPUT:

        - ``self`` -- a `p`-adic element

        EXAMPLES::

            sage: R = Zp(3,20,'capped-rel')
            sage: R(0).is_square()
            True
            sage: R(1).is_square()
            True
            sage: R(2).is_square()
            False

        TESTS::

            sage: R(3).is_square()
            False
            sage: R(4).is_square()
            True
            sage: R(6).is_square()
            False
            sage: R(9).is_square()
            True

            sage: R2 = Zp(2,20,'capped-rel')
            sage: R2(0).is_square()
            True
            sage: R2(1).is_square()
            True
            sage: R2(2).is_square()
            False
            sage: R2(3).is_square()
            False
            sage: R2(4).is_square()
            True
            sage: R2(5).is_square()
            False
            sage: R2(6).is_square()
            False
            sage: R2(7).is_square()
            False
            sage: R2(8).is_square()
            False
            sage: R2(9).is_square()
            True

            sage: K = Qp(3,20,'capped-rel')
            sage: K(0).is_square()
            True
            sage: K(1).is_square()
            True
            sage: K(2).is_square()
            False
            sage: K(3).is_square()
            False
            sage: K(4).is_square()
            True
            sage: K(6).is_square()
            False
            sage: K(9).is_square()
            True
            sage: K(1/3).is_square()
            False
            sage: K(1/9).is_square()
            True

            sage: K2 = Qp(2,20,'capped-rel')
            sage: K2(0).is_square()
            True
            sage: K2(1).is_square()
            True
            sage: K2(2).is_square()
            False
            sage: K2(3).is_square()
            False
            sage: K2(4).is_square()
            True
            sage: K2(5).is_square()
            False
            sage: K2(6).is_square()
            False
            sage: K2(7).is_square()
            False
            sage: K2(8).is_square()
            False
            sage: K2(9).is_square()
            True
            sage: K2(1/2).is_square()
            False
            sage: K2(1/4).is_square()
            True"""
    @overload
    def is_square(self) -> Any:
        """pAdicGenericElement.is_square(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_generic_element.pyx (starting at line 1675)

        Return whether this element is a square.

        INPUT:

        - ``self`` -- a `p`-adic element

        EXAMPLES::

            sage: R = Zp(3,20,'capped-rel')
            sage: R(0).is_square()
            True
            sage: R(1).is_square()
            True
            sage: R(2).is_square()
            False

        TESTS::

            sage: R(3).is_square()
            False
            sage: R(4).is_square()
            True
            sage: R(6).is_square()
            False
            sage: R(9).is_square()
            True

            sage: R2 = Zp(2,20,'capped-rel')
            sage: R2(0).is_square()
            True
            sage: R2(1).is_square()
            True
            sage: R2(2).is_square()
            False
            sage: R2(3).is_square()
            False
            sage: R2(4).is_square()
            True
            sage: R2(5).is_square()
            False
            sage: R2(6).is_square()
            False
            sage: R2(7).is_square()
            False
            sage: R2(8).is_square()
            False
            sage: R2(9).is_square()
            True

            sage: K = Qp(3,20,'capped-rel')
            sage: K(0).is_square()
            True
            sage: K(1).is_square()
            True
            sage: K(2).is_square()
            False
            sage: K(3).is_square()
            False
            sage: K(4).is_square()
            True
            sage: K(6).is_square()
            False
            sage: K(9).is_square()
            True
            sage: K(1/3).is_square()
            False
            sage: K(1/9).is_square()
            True

            sage: K2 = Qp(2,20,'capped-rel')
            sage: K2(0).is_square()
            True
            sage: K2(1).is_square()
            True
            sage: K2(2).is_square()
            False
            sage: K2(3).is_square()
            False
            sage: K2(4).is_square()
            True
            sage: K2(5).is_square()
            False
            sage: K2(6).is_square()
            False
            sage: K2(7).is_square()
            False
            sage: K2(8).is_square()
            False
            sage: K2(9).is_square()
            True
            sage: K2(1/2).is_square()
            False
            sage: K2(1/4).is_square()
            True"""
    @overload
    def is_square(self) -> Any:
        """pAdicGenericElement.is_square(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_generic_element.pyx (starting at line 1675)

        Return whether this element is a square.

        INPUT:

        - ``self`` -- a `p`-adic element

        EXAMPLES::

            sage: R = Zp(3,20,'capped-rel')
            sage: R(0).is_square()
            True
            sage: R(1).is_square()
            True
            sage: R(2).is_square()
            False

        TESTS::

            sage: R(3).is_square()
            False
            sage: R(4).is_square()
            True
            sage: R(6).is_square()
            False
            sage: R(9).is_square()
            True

            sage: R2 = Zp(2,20,'capped-rel')
            sage: R2(0).is_square()
            True
            sage: R2(1).is_square()
            True
            sage: R2(2).is_square()
            False
            sage: R2(3).is_square()
            False
            sage: R2(4).is_square()
            True
            sage: R2(5).is_square()
            False
            sage: R2(6).is_square()
            False
            sage: R2(7).is_square()
            False
            sage: R2(8).is_square()
            False
            sage: R2(9).is_square()
            True

            sage: K = Qp(3,20,'capped-rel')
            sage: K(0).is_square()
            True
            sage: K(1).is_square()
            True
            sage: K(2).is_square()
            False
            sage: K(3).is_square()
            False
            sage: K(4).is_square()
            True
            sage: K(6).is_square()
            False
            sage: K(9).is_square()
            True
            sage: K(1/3).is_square()
            False
            sage: K(1/9).is_square()
            True

            sage: K2 = Qp(2,20,'capped-rel')
            sage: K2(0).is_square()
            True
            sage: K2(1).is_square()
            True
            sage: K2(2).is_square()
            False
            sage: K2(3).is_square()
            False
            sage: K2(4).is_square()
            True
            sage: K2(5).is_square()
            False
            sage: K2(6).is_square()
            False
            sage: K2(7).is_square()
            False
            sage: K2(8).is_square()
            False
            sage: K2(9).is_square()
            True
            sage: K2(1/2).is_square()
            False
            sage: K2(1/4).is_square()
            True"""
    @overload
    def is_square(self) -> Any:
        """pAdicGenericElement.is_square(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_generic_element.pyx (starting at line 1675)

        Return whether this element is a square.

        INPUT:

        - ``self`` -- a `p`-adic element

        EXAMPLES::

            sage: R = Zp(3,20,'capped-rel')
            sage: R(0).is_square()
            True
            sage: R(1).is_square()
            True
            sage: R(2).is_square()
            False

        TESTS::

            sage: R(3).is_square()
            False
            sage: R(4).is_square()
            True
            sage: R(6).is_square()
            False
            sage: R(9).is_square()
            True

            sage: R2 = Zp(2,20,'capped-rel')
            sage: R2(0).is_square()
            True
            sage: R2(1).is_square()
            True
            sage: R2(2).is_square()
            False
            sage: R2(3).is_square()
            False
            sage: R2(4).is_square()
            True
            sage: R2(5).is_square()
            False
            sage: R2(6).is_square()
            False
            sage: R2(7).is_square()
            False
            sage: R2(8).is_square()
            False
            sage: R2(9).is_square()
            True

            sage: K = Qp(3,20,'capped-rel')
            sage: K(0).is_square()
            True
            sage: K(1).is_square()
            True
            sage: K(2).is_square()
            False
            sage: K(3).is_square()
            False
            sage: K(4).is_square()
            True
            sage: K(6).is_square()
            False
            sage: K(9).is_square()
            True
            sage: K(1/3).is_square()
            False
            sage: K(1/9).is_square()
            True

            sage: K2 = Qp(2,20,'capped-rel')
            sage: K2(0).is_square()
            True
            sage: K2(1).is_square()
            True
            sage: K2(2).is_square()
            False
            sage: K2(3).is_square()
            False
            sage: K2(4).is_square()
            True
            sage: K2(5).is_square()
            False
            sage: K2(6).is_square()
            False
            sage: K2(7).is_square()
            False
            sage: K2(8).is_square()
            False
            sage: K2(9).is_square()
            True
            sage: K2(1/2).is_square()
            False
            sage: K2(1/4).is_square()
            True"""
    @overload
    def is_square(self) -> Any:
        """pAdicGenericElement.is_square(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_generic_element.pyx (starting at line 1675)

        Return whether this element is a square.

        INPUT:

        - ``self`` -- a `p`-adic element

        EXAMPLES::

            sage: R = Zp(3,20,'capped-rel')
            sage: R(0).is_square()
            True
            sage: R(1).is_square()
            True
            sage: R(2).is_square()
            False

        TESTS::

            sage: R(3).is_square()
            False
            sage: R(4).is_square()
            True
            sage: R(6).is_square()
            False
            sage: R(9).is_square()
            True

            sage: R2 = Zp(2,20,'capped-rel')
            sage: R2(0).is_square()
            True
            sage: R2(1).is_square()
            True
            sage: R2(2).is_square()
            False
            sage: R2(3).is_square()
            False
            sage: R2(4).is_square()
            True
            sage: R2(5).is_square()
            False
            sage: R2(6).is_square()
            False
            sage: R2(7).is_square()
            False
            sage: R2(8).is_square()
            False
            sage: R2(9).is_square()
            True

            sage: K = Qp(3,20,'capped-rel')
            sage: K(0).is_square()
            True
            sage: K(1).is_square()
            True
            sage: K(2).is_square()
            False
            sage: K(3).is_square()
            False
            sage: K(4).is_square()
            True
            sage: K(6).is_square()
            False
            sage: K(9).is_square()
            True
            sage: K(1/3).is_square()
            False
            sage: K(1/9).is_square()
            True

            sage: K2 = Qp(2,20,'capped-rel')
            sage: K2(0).is_square()
            True
            sage: K2(1).is_square()
            True
            sage: K2(2).is_square()
            False
            sage: K2(3).is_square()
            False
            sage: K2(4).is_square()
            True
            sage: K2(5).is_square()
            False
            sage: K2(6).is_square()
            False
            sage: K2(7).is_square()
            False
            sage: K2(8).is_square()
            False
            sage: K2(9).is_square()
            True
            sage: K2(1/2).is_square()
            False
            sage: K2(1/4).is_square()
            True"""
    @overload
    def is_square(self) -> Any:
        """pAdicGenericElement.is_square(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_generic_element.pyx (starting at line 1675)

        Return whether this element is a square.

        INPUT:

        - ``self`` -- a `p`-adic element

        EXAMPLES::

            sage: R = Zp(3,20,'capped-rel')
            sage: R(0).is_square()
            True
            sage: R(1).is_square()
            True
            sage: R(2).is_square()
            False

        TESTS::

            sage: R(3).is_square()
            False
            sage: R(4).is_square()
            True
            sage: R(6).is_square()
            False
            sage: R(9).is_square()
            True

            sage: R2 = Zp(2,20,'capped-rel')
            sage: R2(0).is_square()
            True
            sage: R2(1).is_square()
            True
            sage: R2(2).is_square()
            False
            sage: R2(3).is_square()
            False
            sage: R2(4).is_square()
            True
            sage: R2(5).is_square()
            False
            sage: R2(6).is_square()
            False
            sage: R2(7).is_square()
            False
            sage: R2(8).is_square()
            False
            sage: R2(9).is_square()
            True

            sage: K = Qp(3,20,'capped-rel')
            sage: K(0).is_square()
            True
            sage: K(1).is_square()
            True
            sage: K(2).is_square()
            False
            sage: K(3).is_square()
            False
            sage: K(4).is_square()
            True
            sage: K(6).is_square()
            False
            sage: K(9).is_square()
            True
            sage: K(1/3).is_square()
            False
            sage: K(1/9).is_square()
            True

            sage: K2 = Qp(2,20,'capped-rel')
            sage: K2(0).is_square()
            True
            sage: K2(1).is_square()
            True
            sage: K2(2).is_square()
            False
            sage: K2(3).is_square()
            False
            sage: K2(4).is_square()
            True
            sage: K2(5).is_square()
            False
            sage: K2(6).is_square()
            False
            sage: K2(7).is_square()
            False
            sage: K2(8).is_square()
            False
            sage: K2(9).is_square()
            True
            sage: K2(1/2).is_square()
            False
            sage: K2(1/4).is_square()
            True"""
    @overload
    def is_square(self) -> Any:
        """pAdicGenericElement.is_square(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_generic_element.pyx (starting at line 1675)

        Return whether this element is a square.

        INPUT:

        - ``self`` -- a `p`-adic element

        EXAMPLES::

            sage: R = Zp(3,20,'capped-rel')
            sage: R(0).is_square()
            True
            sage: R(1).is_square()
            True
            sage: R(2).is_square()
            False

        TESTS::

            sage: R(3).is_square()
            False
            sage: R(4).is_square()
            True
            sage: R(6).is_square()
            False
            sage: R(9).is_square()
            True

            sage: R2 = Zp(2,20,'capped-rel')
            sage: R2(0).is_square()
            True
            sage: R2(1).is_square()
            True
            sage: R2(2).is_square()
            False
            sage: R2(3).is_square()
            False
            sage: R2(4).is_square()
            True
            sage: R2(5).is_square()
            False
            sage: R2(6).is_square()
            False
            sage: R2(7).is_square()
            False
            sage: R2(8).is_square()
            False
            sage: R2(9).is_square()
            True

            sage: K = Qp(3,20,'capped-rel')
            sage: K(0).is_square()
            True
            sage: K(1).is_square()
            True
            sage: K(2).is_square()
            False
            sage: K(3).is_square()
            False
            sage: K(4).is_square()
            True
            sage: K(6).is_square()
            False
            sage: K(9).is_square()
            True
            sage: K(1/3).is_square()
            False
            sage: K(1/9).is_square()
            True

            sage: K2 = Qp(2,20,'capped-rel')
            sage: K2(0).is_square()
            True
            sage: K2(1).is_square()
            True
            sage: K2(2).is_square()
            False
            sage: K2(3).is_square()
            False
            sage: K2(4).is_square()
            True
            sage: K2(5).is_square()
            False
            sage: K2(6).is_square()
            False
            sage: K2(7).is_square()
            False
            sage: K2(8).is_square()
            False
            sage: K2(9).is_square()
            True
            sage: K2(1/2).is_square()
            False
            sage: K2(1/4).is_square()
            True"""
    @overload
    def is_square(self) -> Any:
        """pAdicGenericElement.is_square(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_generic_element.pyx (starting at line 1675)

        Return whether this element is a square.

        INPUT:

        - ``self`` -- a `p`-adic element

        EXAMPLES::

            sage: R = Zp(3,20,'capped-rel')
            sage: R(0).is_square()
            True
            sage: R(1).is_square()
            True
            sage: R(2).is_square()
            False

        TESTS::

            sage: R(3).is_square()
            False
            sage: R(4).is_square()
            True
            sage: R(6).is_square()
            False
            sage: R(9).is_square()
            True

            sage: R2 = Zp(2,20,'capped-rel')
            sage: R2(0).is_square()
            True
            sage: R2(1).is_square()
            True
            sage: R2(2).is_square()
            False
            sage: R2(3).is_square()
            False
            sage: R2(4).is_square()
            True
            sage: R2(5).is_square()
            False
            sage: R2(6).is_square()
            False
            sage: R2(7).is_square()
            False
            sage: R2(8).is_square()
            False
            sage: R2(9).is_square()
            True

            sage: K = Qp(3,20,'capped-rel')
            sage: K(0).is_square()
            True
            sage: K(1).is_square()
            True
            sage: K(2).is_square()
            False
            sage: K(3).is_square()
            False
            sage: K(4).is_square()
            True
            sage: K(6).is_square()
            False
            sage: K(9).is_square()
            True
            sage: K(1/3).is_square()
            False
            sage: K(1/9).is_square()
            True

            sage: K2 = Qp(2,20,'capped-rel')
            sage: K2(0).is_square()
            True
            sage: K2(1).is_square()
            True
            sage: K2(2).is_square()
            False
            sage: K2(3).is_square()
            False
            sage: K2(4).is_square()
            True
            sage: K2(5).is_square()
            False
            sage: K2(6).is_square()
            False
            sage: K2(7).is_square()
            False
            sage: K2(8).is_square()
            False
            sage: K2(9).is_square()
            True
            sage: K2(1/2).is_square()
            False
            sage: K2(1/4).is_square()
            True"""
    @overload
    def is_square(self) -> Any:
        """pAdicGenericElement.is_square(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_generic_element.pyx (starting at line 1675)

        Return whether this element is a square.

        INPUT:

        - ``self`` -- a `p`-adic element

        EXAMPLES::

            sage: R = Zp(3,20,'capped-rel')
            sage: R(0).is_square()
            True
            sage: R(1).is_square()
            True
            sage: R(2).is_square()
            False

        TESTS::

            sage: R(3).is_square()
            False
            sage: R(4).is_square()
            True
            sage: R(6).is_square()
            False
            sage: R(9).is_square()
            True

            sage: R2 = Zp(2,20,'capped-rel')
            sage: R2(0).is_square()
            True
            sage: R2(1).is_square()
            True
            sage: R2(2).is_square()
            False
            sage: R2(3).is_square()
            False
            sage: R2(4).is_square()
            True
            sage: R2(5).is_square()
            False
            sage: R2(6).is_square()
            False
            sage: R2(7).is_square()
            False
            sage: R2(8).is_square()
            False
            sage: R2(9).is_square()
            True

            sage: K = Qp(3,20,'capped-rel')
            sage: K(0).is_square()
            True
            sage: K(1).is_square()
            True
            sage: K(2).is_square()
            False
            sage: K(3).is_square()
            False
            sage: K(4).is_square()
            True
            sage: K(6).is_square()
            False
            sage: K(9).is_square()
            True
            sage: K(1/3).is_square()
            False
            sage: K(1/9).is_square()
            True

            sage: K2 = Qp(2,20,'capped-rel')
            sage: K2(0).is_square()
            True
            sage: K2(1).is_square()
            True
            sage: K2(2).is_square()
            False
            sage: K2(3).is_square()
            False
            sage: K2(4).is_square()
            True
            sage: K2(5).is_square()
            False
            sage: K2(6).is_square()
            False
            sage: K2(7).is_square()
            False
            sage: K2(8).is_square()
            False
            sage: K2(9).is_square()
            True
            sage: K2(1/2).is_square()
            False
            sage: K2(1/4).is_square()
            True"""
    @overload
    def is_square(self) -> Any:
        """pAdicGenericElement.is_square(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_generic_element.pyx (starting at line 1675)

        Return whether this element is a square.

        INPUT:

        - ``self`` -- a `p`-adic element

        EXAMPLES::

            sage: R = Zp(3,20,'capped-rel')
            sage: R(0).is_square()
            True
            sage: R(1).is_square()
            True
            sage: R(2).is_square()
            False

        TESTS::

            sage: R(3).is_square()
            False
            sage: R(4).is_square()
            True
            sage: R(6).is_square()
            False
            sage: R(9).is_square()
            True

            sage: R2 = Zp(2,20,'capped-rel')
            sage: R2(0).is_square()
            True
            sage: R2(1).is_square()
            True
            sage: R2(2).is_square()
            False
            sage: R2(3).is_square()
            False
            sage: R2(4).is_square()
            True
            sage: R2(5).is_square()
            False
            sage: R2(6).is_square()
            False
            sage: R2(7).is_square()
            False
            sage: R2(8).is_square()
            False
            sage: R2(9).is_square()
            True

            sage: K = Qp(3,20,'capped-rel')
            sage: K(0).is_square()
            True
            sage: K(1).is_square()
            True
            sage: K(2).is_square()
            False
            sage: K(3).is_square()
            False
            sage: K(4).is_square()
            True
            sage: K(6).is_square()
            False
            sage: K(9).is_square()
            True
            sage: K(1/3).is_square()
            False
            sage: K(1/9).is_square()
            True

            sage: K2 = Qp(2,20,'capped-rel')
            sage: K2(0).is_square()
            True
            sage: K2(1).is_square()
            True
            sage: K2(2).is_square()
            False
            sage: K2(3).is_square()
            False
            sage: K2(4).is_square()
            True
            sage: K2(5).is_square()
            False
            sage: K2(6).is_square()
            False
            sage: K2(7).is_square()
            False
            sage: K2(8).is_square()
            False
            sage: K2(9).is_square()
            True
            sage: K2(1/2).is_square()
            False
            sage: K2(1/4).is_square()
            True"""
    @overload
    def is_square(self) -> Any:
        """pAdicGenericElement.is_square(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_generic_element.pyx (starting at line 1675)

        Return whether this element is a square.

        INPUT:

        - ``self`` -- a `p`-adic element

        EXAMPLES::

            sage: R = Zp(3,20,'capped-rel')
            sage: R(0).is_square()
            True
            sage: R(1).is_square()
            True
            sage: R(2).is_square()
            False

        TESTS::

            sage: R(3).is_square()
            False
            sage: R(4).is_square()
            True
            sage: R(6).is_square()
            False
            sage: R(9).is_square()
            True

            sage: R2 = Zp(2,20,'capped-rel')
            sage: R2(0).is_square()
            True
            sage: R2(1).is_square()
            True
            sage: R2(2).is_square()
            False
            sage: R2(3).is_square()
            False
            sage: R2(4).is_square()
            True
            sage: R2(5).is_square()
            False
            sage: R2(6).is_square()
            False
            sage: R2(7).is_square()
            False
            sage: R2(8).is_square()
            False
            sage: R2(9).is_square()
            True

            sage: K = Qp(3,20,'capped-rel')
            sage: K(0).is_square()
            True
            sage: K(1).is_square()
            True
            sage: K(2).is_square()
            False
            sage: K(3).is_square()
            False
            sage: K(4).is_square()
            True
            sage: K(6).is_square()
            False
            sage: K(9).is_square()
            True
            sage: K(1/3).is_square()
            False
            sage: K(1/9).is_square()
            True

            sage: K2 = Qp(2,20,'capped-rel')
            sage: K2(0).is_square()
            True
            sage: K2(1).is_square()
            True
            sage: K2(2).is_square()
            False
            sage: K2(3).is_square()
            False
            sage: K2(4).is_square()
            True
            sage: K2(5).is_square()
            False
            sage: K2(6).is_square()
            False
            sage: K2(7).is_square()
            False
            sage: K2(8).is_square()
            False
            sage: K2(9).is_square()
            True
            sage: K2(1/2).is_square()
            False
            sage: K2(1/4).is_square()
            True"""
    @overload
    def is_square(self) -> Any:
        """pAdicGenericElement.is_square(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_generic_element.pyx (starting at line 1675)

        Return whether this element is a square.

        INPUT:

        - ``self`` -- a `p`-adic element

        EXAMPLES::

            sage: R = Zp(3,20,'capped-rel')
            sage: R(0).is_square()
            True
            sage: R(1).is_square()
            True
            sage: R(2).is_square()
            False

        TESTS::

            sage: R(3).is_square()
            False
            sage: R(4).is_square()
            True
            sage: R(6).is_square()
            False
            sage: R(9).is_square()
            True

            sage: R2 = Zp(2,20,'capped-rel')
            sage: R2(0).is_square()
            True
            sage: R2(1).is_square()
            True
            sage: R2(2).is_square()
            False
            sage: R2(3).is_square()
            False
            sage: R2(4).is_square()
            True
            sage: R2(5).is_square()
            False
            sage: R2(6).is_square()
            False
            sage: R2(7).is_square()
            False
            sage: R2(8).is_square()
            False
            sage: R2(9).is_square()
            True

            sage: K = Qp(3,20,'capped-rel')
            sage: K(0).is_square()
            True
            sage: K(1).is_square()
            True
            sage: K(2).is_square()
            False
            sage: K(3).is_square()
            False
            sage: K(4).is_square()
            True
            sage: K(6).is_square()
            False
            sage: K(9).is_square()
            True
            sage: K(1/3).is_square()
            False
            sage: K(1/9).is_square()
            True

            sage: K2 = Qp(2,20,'capped-rel')
            sage: K2(0).is_square()
            True
            sage: K2(1).is_square()
            True
            sage: K2(2).is_square()
            False
            sage: K2(3).is_square()
            False
            sage: K2(4).is_square()
            True
            sage: K2(5).is_square()
            False
            sage: K2(6).is_square()
            False
            sage: K2(7).is_square()
            False
            sage: K2(8).is_square()
            False
            sage: K2(9).is_square()
            True
            sage: K2(1/2).is_square()
            False
            sage: K2(1/4).is_square()
            True"""
    @overload
    def is_square(self) -> Any:
        """pAdicGenericElement.is_square(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_generic_element.pyx (starting at line 1675)

        Return whether this element is a square.

        INPUT:

        - ``self`` -- a `p`-adic element

        EXAMPLES::

            sage: R = Zp(3,20,'capped-rel')
            sage: R(0).is_square()
            True
            sage: R(1).is_square()
            True
            sage: R(2).is_square()
            False

        TESTS::

            sage: R(3).is_square()
            False
            sage: R(4).is_square()
            True
            sage: R(6).is_square()
            False
            sage: R(9).is_square()
            True

            sage: R2 = Zp(2,20,'capped-rel')
            sage: R2(0).is_square()
            True
            sage: R2(1).is_square()
            True
            sage: R2(2).is_square()
            False
            sage: R2(3).is_square()
            False
            sage: R2(4).is_square()
            True
            sage: R2(5).is_square()
            False
            sage: R2(6).is_square()
            False
            sage: R2(7).is_square()
            False
            sage: R2(8).is_square()
            False
            sage: R2(9).is_square()
            True

            sage: K = Qp(3,20,'capped-rel')
            sage: K(0).is_square()
            True
            sage: K(1).is_square()
            True
            sage: K(2).is_square()
            False
            sage: K(3).is_square()
            False
            sage: K(4).is_square()
            True
            sage: K(6).is_square()
            False
            sage: K(9).is_square()
            True
            sage: K(1/3).is_square()
            False
            sage: K(1/9).is_square()
            True

            sage: K2 = Qp(2,20,'capped-rel')
            sage: K2(0).is_square()
            True
            sage: K2(1).is_square()
            True
            sage: K2(2).is_square()
            False
            sage: K2(3).is_square()
            False
            sage: K2(4).is_square()
            True
            sage: K2(5).is_square()
            False
            sage: K2(6).is_square()
            False
            sage: K2(7).is_square()
            False
            sage: K2(8).is_square()
            False
            sage: K2(9).is_square()
            True
            sage: K2(1/2).is_square()
            False
            sage: K2(1/4).is_square()
            True"""
    @overload
    def is_square(self) -> Any:
        """pAdicGenericElement.is_square(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_generic_element.pyx (starting at line 1675)

        Return whether this element is a square.

        INPUT:

        - ``self`` -- a `p`-adic element

        EXAMPLES::

            sage: R = Zp(3,20,'capped-rel')
            sage: R(0).is_square()
            True
            sage: R(1).is_square()
            True
            sage: R(2).is_square()
            False

        TESTS::

            sage: R(3).is_square()
            False
            sage: R(4).is_square()
            True
            sage: R(6).is_square()
            False
            sage: R(9).is_square()
            True

            sage: R2 = Zp(2,20,'capped-rel')
            sage: R2(0).is_square()
            True
            sage: R2(1).is_square()
            True
            sage: R2(2).is_square()
            False
            sage: R2(3).is_square()
            False
            sage: R2(4).is_square()
            True
            sage: R2(5).is_square()
            False
            sage: R2(6).is_square()
            False
            sage: R2(7).is_square()
            False
            sage: R2(8).is_square()
            False
            sage: R2(9).is_square()
            True

            sage: K = Qp(3,20,'capped-rel')
            sage: K(0).is_square()
            True
            sage: K(1).is_square()
            True
            sage: K(2).is_square()
            False
            sage: K(3).is_square()
            False
            sage: K(4).is_square()
            True
            sage: K(6).is_square()
            False
            sage: K(9).is_square()
            True
            sage: K(1/3).is_square()
            False
            sage: K(1/9).is_square()
            True

            sage: K2 = Qp(2,20,'capped-rel')
            sage: K2(0).is_square()
            True
            sage: K2(1).is_square()
            True
            sage: K2(2).is_square()
            False
            sage: K2(3).is_square()
            False
            sage: K2(4).is_square()
            True
            sage: K2(5).is_square()
            False
            sage: K2(6).is_square()
            False
            sage: K2(7).is_square()
            False
            sage: K2(8).is_square()
            False
            sage: K2(9).is_square()
            True
            sage: K2(1/2).is_square()
            False
            sage: K2(1/4).is_square()
            True"""
    @overload
    def is_square(self) -> Any:
        """pAdicGenericElement.is_square(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_generic_element.pyx (starting at line 1675)

        Return whether this element is a square.

        INPUT:

        - ``self`` -- a `p`-adic element

        EXAMPLES::

            sage: R = Zp(3,20,'capped-rel')
            sage: R(0).is_square()
            True
            sage: R(1).is_square()
            True
            sage: R(2).is_square()
            False

        TESTS::

            sage: R(3).is_square()
            False
            sage: R(4).is_square()
            True
            sage: R(6).is_square()
            False
            sage: R(9).is_square()
            True

            sage: R2 = Zp(2,20,'capped-rel')
            sage: R2(0).is_square()
            True
            sage: R2(1).is_square()
            True
            sage: R2(2).is_square()
            False
            sage: R2(3).is_square()
            False
            sage: R2(4).is_square()
            True
            sage: R2(5).is_square()
            False
            sage: R2(6).is_square()
            False
            sage: R2(7).is_square()
            False
            sage: R2(8).is_square()
            False
            sage: R2(9).is_square()
            True

            sage: K = Qp(3,20,'capped-rel')
            sage: K(0).is_square()
            True
            sage: K(1).is_square()
            True
            sage: K(2).is_square()
            False
            sage: K(3).is_square()
            False
            sage: K(4).is_square()
            True
            sage: K(6).is_square()
            False
            sage: K(9).is_square()
            True
            sage: K(1/3).is_square()
            False
            sage: K(1/9).is_square()
            True

            sage: K2 = Qp(2,20,'capped-rel')
            sage: K2(0).is_square()
            True
            sage: K2(1).is_square()
            True
            sage: K2(2).is_square()
            False
            sage: K2(3).is_square()
            False
            sage: K2(4).is_square()
            True
            sage: K2(5).is_square()
            False
            sage: K2(6).is_square()
            False
            sage: K2(7).is_square()
            False
            sage: K2(8).is_square()
            False
            sage: K2(9).is_square()
            True
            sage: K2(1/2).is_square()
            False
            sage: K2(1/4).is_square()
            True"""
    @overload
    def is_square(self) -> Any:
        """pAdicGenericElement.is_square(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_generic_element.pyx (starting at line 1675)

        Return whether this element is a square.

        INPUT:

        - ``self`` -- a `p`-adic element

        EXAMPLES::

            sage: R = Zp(3,20,'capped-rel')
            sage: R(0).is_square()
            True
            sage: R(1).is_square()
            True
            sage: R(2).is_square()
            False

        TESTS::

            sage: R(3).is_square()
            False
            sage: R(4).is_square()
            True
            sage: R(6).is_square()
            False
            sage: R(9).is_square()
            True

            sage: R2 = Zp(2,20,'capped-rel')
            sage: R2(0).is_square()
            True
            sage: R2(1).is_square()
            True
            sage: R2(2).is_square()
            False
            sage: R2(3).is_square()
            False
            sage: R2(4).is_square()
            True
            sage: R2(5).is_square()
            False
            sage: R2(6).is_square()
            False
            sage: R2(7).is_square()
            False
            sage: R2(8).is_square()
            False
            sage: R2(9).is_square()
            True

            sage: K = Qp(3,20,'capped-rel')
            sage: K(0).is_square()
            True
            sage: K(1).is_square()
            True
            sage: K(2).is_square()
            False
            sage: K(3).is_square()
            False
            sage: K(4).is_square()
            True
            sage: K(6).is_square()
            False
            sage: K(9).is_square()
            True
            sage: K(1/3).is_square()
            False
            sage: K(1/9).is_square()
            True

            sage: K2 = Qp(2,20,'capped-rel')
            sage: K2(0).is_square()
            True
            sage: K2(1).is_square()
            True
            sage: K2(2).is_square()
            False
            sage: K2(3).is_square()
            False
            sage: K2(4).is_square()
            True
            sage: K2(5).is_square()
            False
            sage: K2(6).is_square()
            False
            sage: K2(7).is_square()
            False
            sage: K2(8).is_square()
            False
            sage: K2(9).is_square()
            True
            sage: K2(1/2).is_square()
            False
            sage: K2(1/4).is_square()
            True"""
    @overload
    def is_square(self) -> Any:
        """pAdicGenericElement.is_square(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_generic_element.pyx (starting at line 1675)

        Return whether this element is a square.

        INPUT:

        - ``self`` -- a `p`-adic element

        EXAMPLES::

            sage: R = Zp(3,20,'capped-rel')
            sage: R(0).is_square()
            True
            sage: R(1).is_square()
            True
            sage: R(2).is_square()
            False

        TESTS::

            sage: R(3).is_square()
            False
            sage: R(4).is_square()
            True
            sage: R(6).is_square()
            False
            sage: R(9).is_square()
            True

            sage: R2 = Zp(2,20,'capped-rel')
            sage: R2(0).is_square()
            True
            sage: R2(1).is_square()
            True
            sage: R2(2).is_square()
            False
            sage: R2(3).is_square()
            False
            sage: R2(4).is_square()
            True
            sage: R2(5).is_square()
            False
            sage: R2(6).is_square()
            False
            sage: R2(7).is_square()
            False
            sage: R2(8).is_square()
            False
            sage: R2(9).is_square()
            True

            sage: K = Qp(3,20,'capped-rel')
            sage: K(0).is_square()
            True
            sage: K(1).is_square()
            True
            sage: K(2).is_square()
            False
            sage: K(3).is_square()
            False
            sage: K(4).is_square()
            True
            sage: K(6).is_square()
            False
            sage: K(9).is_square()
            True
            sage: K(1/3).is_square()
            False
            sage: K(1/9).is_square()
            True

            sage: K2 = Qp(2,20,'capped-rel')
            sage: K2(0).is_square()
            True
            sage: K2(1).is_square()
            True
            sage: K2(2).is_square()
            False
            sage: K2(3).is_square()
            False
            sage: K2(4).is_square()
            True
            sage: K2(5).is_square()
            False
            sage: K2(6).is_square()
            False
            sage: K2(7).is_square()
            False
            sage: K2(8).is_square()
            False
            sage: K2(9).is_square()
            True
            sage: K2(1/2).is_square()
            False
            sage: K2(1/4).is_square()
            True"""
    @overload
    def is_square(self) -> Any:
        """pAdicGenericElement.is_square(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_generic_element.pyx (starting at line 1675)

        Return whether this element is a square.

        INPUT:

        - ``self`` -- a `p`-adic element

        EXAMPLES::

            sage: R = Zp(3,20,'capped-rel')
            sage: R(0).is_square()
            True
            sage: R(1).is_square()
            True
            sage: R(2).is_square()
            False

        TESTS::

            sage: R(3).is_square()
            False
            sage: R(4).is_square()
            True
            sage: R(6).is_square()
            False
            sage: R(9).is_square()
            True

            sage: R2 = Zp(2,20,'capped-rel')
            sage: R2(0).is_square()
            True
            sage: R2(1).is_square()
            True
            sage: R2(2).is_square()
            False
            sage: R2(3).is_square()
            False
            sage: R2(4).is_square()
            True
            sage: R2(5).is_square()
            False
            sage: R2(6).is_square()
            False
            sage: R2(7).is_square()
            False
            sage: R2(8).is_square()
            False
            sage: R2(9).is_square()
            True

            sage: K = Qp(3,20,'capped-rel')
            sage: K(0).is_square()
            True
            sage: K(1).is_square()
            True
            sage: K(2).is_square()
            False
            sage: K(3).is_square()
            False
            sage: K(4).is_square()
            True
            sage: K(6).is_square()
            False
            sage: K(9).is_square()
            True
            sage: K(1/3).is_square()
            False
            sage: K(1/9).is_square()
            True

            sage: K2 = Qp(2,20,'capped-rel')
            sage: K2(0).is_square()
            True
            sage: K2(1).is_square()
            True
            sage: K2(2).is_square()
            False
            sage: K2(3).is_square()
            False
            sage: K2(4).is_square()
            True
            sage: K2(5).is_square()
            False
            sage: K2(6).is_square()
            False
            sage: K2(7).is_square()
            False
            sage: K2(8).is_square()
            False
            sage: K2(9).is_square()
            True
            sage: K2(1/2).is_square()
            False
            sage: K2(1/4).is_square()
            True"""
    @overload
    def is_square(self) -> Any:
        """pAdicGenericElement.is_square(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_generic_element.pyx (starting at line 1675)

        Return whether this element is a square.

        INPUT:

        - ``self`` -- a `p`-adic element

        EXAMPLES::

            sage: R = Zp(3,20,'capped-rel')
            sage: R(0).is_square()
            True
            sage: R(1).is_square()
            True
            sage: R(2).is_square()
            False

        TESTS::

            sage: R(3).is_square()
            False
            sage: R(4).is_square()
            True
            sage: R(6).is_square()
            False
            sage: R(9).is_square()
            True

            sage: R2 = Zp(2,20,'capped-rel')
            sage: R2(0).is_square()
            True
            sage: R2(1).is_square()
            True
            sage: R2(2).is_square()
            False
            sage: R2(3).is_square()
            False
            sage: R2(4).is_square()
            True
            sage: R2(5).is_square()
            False
            sage: R2(6).is_square()
            False
            sage: R2(7).is_square()
            False
            sage: R2(8).is_square()
            False
            sage: R2(9).is_square()
            True

            sage: K = Qp(3,20,'capped-rel')
            sage: K(0).is_square()
            True
            sage: K(1).is_square()
            True
            sage: K(2).is_square()
            False
            sage: K(3).is_square()
            False
            sage: K(4).is_square()
            True
            sage: K(6).is_square()
            False
            sage: K(9).is_square()
            True
            sage: K(1/3).is_square()
            False
            sage: K(1/9).is_square()
            True

            sage: K2 = Qp(2,20,'capped-rel')
            sage: K2(0).is_square()
            True
            sage: K2(1).is_square()
            True
            sage: K2(2).is_square()
            False
            sage: K2(3).is_square()
            False
            sage: K2(4).is_square()
            True
            sage: K2(5).is_square()
            False
            sage: K2(6).is_square()
            False
            sage: K2(7).is_square()
            False
            sage: K2(8).is_square()
            False
            sage: K2(9).is_square()
            True
            sage: K2(1/2).is_square()
            False
            sage: K2(1/4).is_square()
            True"""
    @overload
    def is_square(self) -> Any:
        """pAdicGenericElement.is_square(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_generic_element.pyx (starting at line 1675)

        Return whether this element is a square.

        INPUT:

        - ``self`` -- a `p`-adic element

        EXAMPLES::

            sage: R = Zp(3,20,'capped-rel')
            sage: R(0).is_square()
            True
            sage: R(1).is_square()
            True
            sage: R(2).is_square()
            False

        TESTS::

            sage: R(3).is_square()
            False
            sage: R(4).is_square()
            True
            sage: R(6).is_square()
            False
            sage: R(9).is_square()
            True

            sage: R2 = Zp(2,20,'capped-rel')
            sage: R2(0).is_square()
            True
            sage: R2(1).is_square()
            True
            sage: R2(2).is_square()
            False
            sage: R2(3).is_square()
            False
            sage: R2(4).is_square()
            True
            sage: R2(5).is_square()
            False
            sage: R2(6).is_square()
            False
            sage: R2(7).is_square()
            False
            sage: R2(8).is_square()
            False
            sage: R2(9).is_square()
            True

            sage: K = Qp(3,20,'capped-rel')
            sage: K(0).is_square()
            True
            sage: K(1).is_square()
            True
            sage: K(2).is_square()
            False
            sage: K(3).is_square()
            False
            sage: K(4).is_square()
            True
            sage: K(6).is_square()
            False
            sage: K(9).is_square()
            True
            sage: K(1/3).is_square()
            False
            sage: K(1/9).is_square()
            True

            sage: K2 = Qp(2,20,'capped-rel')
            sage: K2(0).is_square()
            True
            sage: K2(1).is_square()
            True
            sage: K2(2).is_square()
            False
            sage: K2(3).is_square()
            False
            sage: K2(4).is_square()
            True
            sage: K2(5).is_square()
            False
            sage: K2(6).is_square()
            False
            sage: K2(7).is_square()
            False
            sage: K2(8).is_square()
            False
            sage: K2(9).is_square()
            True
            sage: K2(1/2).is_square()
            False
            sage: K2(1/4).is_square()
            True"""
    @overload
    def is_square(self) -> Any:
        """pAdicGenericElement.is_square(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_generic_element.pyx (starting at line 1675)

        Return whether this element is a square.

        INPUT:

        - ``self`` -- a `p`-adic element

        EXAMPLES::

            sage: R = Zp(3,20,'capped-rel')
            sage: R(0).is_square()
            True
            sage: R(1).is_square()
            True
            sage: R(2).is_square()
            False

        TESTS::

            sage: R(3).is_square()
            False
            sage: R(4).is_square()
            True
            sage: R(6).is_square()
            False
            sage: R(9).is_square()
            True

            sage: R2 = Zp(2,20,'capped-rel')
            sage: R2(0).is_square()
            True
            sage: R2(1).is_square()
            True
            sage: R2(2).is_square()
            False
            sage: R2(3).is_square()
            False
            sage: R2(4).is_square()
            True
            sage: R2(5).is_square()
            False
            sage: R2(6).is_square()
            False
            sage: R2(7).is_square()
            False
            sage: R2(8).is_square()
            False
            sage: R2(9).is_square()
            True

            sage: K = Qp(3,20,'capped-rel')
            sage: K(0).is_square()
            True
            sage: K(1).is_square()
            True
            sage: K(2).is_square()
            False
            sage: K(3).is_square()
            False
            sage: K(4).is_square()
            True
            sage: K(6).is_square()
            False
            sage: K(9).is_square()
            True
            sage: K(1/3).is_square()
            False
            sage: K(1/9).is_square()
            True

            sage: K2 = Qp(2,20,'capped-rel')
            sage: K2(0).is_square()
            True
            sage: K2(1).is_square()
            True
            sage: K2(2).is_square()
            False
            sage: K2(3).is_square()
            False
            sage: K2(4).is_square()
            True
            sage: K2(5).is_square()
            False
            sage: K2(6).is_square()
            False
            sage: K2(7).is_square()
            False
            sage: K2(8).is_square()
            False
            sage: K2(9).is_square()
            True
            sage: K2(1/2).is_square()
            False
            sage: K2(1/4).is_square()
            True"""
    @overload
    def is_square(self) -> Any:
        """pAdicGenericElement.is_square(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_generic_element.pyx (starting at line 1675)

        Return whether this element is a square.

        INPUT:

        - ``self`` -- a `p`-adic element

        EXAMPLES::

            sage: R = Zp(3,20,'capped-rel')
            sage: R(0).is_square()
            True
            sage: R(1).is_square()
            True
            sage: R(2).is_square()
            False

        TESTS::

            sage: R(3).is_square()
            False
            sage: R(4).is_square()
            True
            sage: R(6).is_square()
            False
            sage: R(9).is_square()
            True

            sage: R2 = Zp(2,20,'capped-rel')
            sage: R2(0).is_square()
            True
            sage: R2(1).is_square()
            True
            sage: R2(2).is_square()
            False
            sage: R2(3).is_square()
            False
            sage: R2(4).is_square()
            True
            sage: R2(5).is_square()
            False
            sage: R2(6).is_square()
            False
            sage: R2(7).is_square()
            False
            sage: R2(8).is_square()
            False
            sage: R2(9).is_square()
            True

            sage: K = Qp(3,20,'capped-rel')
            sage: K(0).is_square()
            True
            sage: K(1).is_square()
            True
            sage: K(2).is_square()
            False
            sage: K(3).is_square()
            False
            sage: K(4).is_square()
            True
            sage: K(6).is_square()
            False
            sage: K(9).is_square()
            True
            sage: K(1/3).is_square()
            False
            sage: K(1/9).is_square()
            True

            sage: K2 = Qp(2,20,'capped-rel')
            sage: K2(0).is_square()
            True
            sage: K2(1).is_square()
            True
            sage: K2(2).is_square()
            False
            sage: K2(3).is_square()
            False
            sage: K2(4).is_square()
            True
            sage: K2(5).is_square()
            False
            sage: K2(6).is_square()
            False
            sage: K2(7).is_square()
            False
            sage: K2(8).is_square()
            False
            sage: K2(9).is_square()
            True
            sage: K2(1/2).is_square()
            False
            sage: K2(1/4).is_square()
            True"""
    @overload
    def is_square(self) -> Any:
        """pAdicGenericElement.is_square(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_generic_element.pyx (starting at line 1675)

        Return whether this element is a square.

        INPUT:

        - ``self`` -- a `p`-adic element

        EXAMPLES::

            sage: R = Zp(3,20,'capped-rel')
            sage: R(0).is_square()
            True
            sage: R(1).is_square()
            True
            sage: R(2).is_square()
            False

        TESTS::

            sage: R(3).is_square()
            False
            sage: R(4).is_square()
            True
            sage: R(6).is_square()
            False
            sage: R(9).is_square()
            True

            sage: R2 = Zp(2,20,'capped-rel')
            sage: R2(0).is_square()
            True
            sage: R2(1).is_square()
            True
            sage: R2(2).is_square()
            False
            sage: R2(3).is_square()
            False
            sage: R2(4).is_square()
            True
            sage: R2(5).is_square()
            False
            sage: R2(6).is_square()
            False
            sage: R2(7).is_square()
            False
            sage: R2(8).is_square()
            False
            sage: R2(9).is_square()
            True

            sage: K = Qp(3,20,'capped-rel')
            sage: K(0).is_square()
            True
            sage: K(1).is_square()
            True
            sage: K(2).is_square()
            False
            sage: K(3).is_square()
            False
            sage: K(4).is_square()
            True
            sage: K(6).is_square()
            False
            sage: K(9).is_square()
            True
            sage: K(1/3).is_square()
            False
            sage: K(1/9).is_square()
            True

            sage: K2 = Qp(2,20,'capped-rel')
            sage: K2(0).is_square()
            True
            sage: K2(1).is_square()
            True
            sage: K2(2).is_square()
            False
            sage: K2(3).is_square()
            False
            sage: K2(4).is_square()
            True
            sage: K2(5).is_square()
            False
            sage: K2(6).is_square()
            False
            sage: K2(7).is_square()
            False
            sage: K2(8).is_square()
            False
            sage: K2(9).is_square()
            True
            sage: K2(1/2).is_square()
            False
            sage: K2(1/4).is_square()
            True"""
    @overload
    def is_square(self) -> Any:
        """pAdicGenericElement.is_square(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_generic_element.pyx (starting at line 1675)

        Return whether this element is a square.

        INPUT:

        - ``self`` -- a `p`-adic element

        EXAMPLES::

            sage: R = Zp(3,20,'capped-rel')
            sage: R(0).is_square()
            True
            sage: R(1).is_square()
            True
            sage: R(2).is_square()
            False

        TESTS::

            sage: R(3).is_square()
            False
            sage: R(4).is_square()
            True
            sage: R(6).is_square()
            False
            sage: R(9).is_square()
            True

            sage: R2 = Zp(2,20,'capped-rel')
            sage: R2(0).is_square()
            True
            sage: R2(1).is_square()
            True
            sage: R2(2).is_square()
            False
            sage: R2(3).is_square()
            False
            sage: R2(4).is_square()
            True
            sage: R2(5).is_square()
            False
            sage: R2(6).is_square()
            False
            sage: R2(7).is_square()
            False
            sage: R2(8).is_square()
            False
            sage: R2(9).is_square()
            True

            sage: K = Qp(3,20,'capped-rel')
            sage: K(0).is_square()
            True
            sage: K(1).is_square()
            True
            sage: K(2).is_square()
            False
            sage: K(3).is_square()
            False
            sage: K(4).is_square()
            True
            sage: K(6).is_square()
            False
            sage: K(9).is_square()
            True
            sage: K(1/3).is_square()
            False
            sage: K(1/9).is_square()
            True

            sage: K2 = Qp(2,20,'capped-rel')
            sage: K2(0).is_square()
            True
            sage: K2(1).is_square()
            True
            sage: K2(2).is_square()
            False
            sage: K2(3).is_square()
            False
            sage: K2(4).is_square()
            True
            sage: K2(5).is_square()
            False
            sage: K2(6).is_square()
            False
            sage: K2(7).is_square()
            False
            sage: K2(8).is_square()
            False
            sage: K2(9).is_square()
            True
            sage: K2(1/2).is_square()
            False
            sage: K2(1/4).is_square()
            True"""
    @overload
    def is_square(self) -> Any:
        """pAdicGenericElement.is_square(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_generic_element.pyx (starting at line 1675)

        Return whether this element is a square.

        INPUT:

        - ``self`` -- a `p`-adic element

        EXAMPLES::

            sage: R = Zp(3,20,'capped-rel')
            sage: R(0).is_square()
            True
            sage: R(1).is_square()
            True
            sage: R(2).is_square()
            False

        TESTS::

            sage: R(3).is_square()
            False
            sage: R(4).is_square()
            True
            sage: R(6).is_square()
            False
            sage: R(9).is_square()
            True

            sage: R2 = Zp(2,20,'capped-rel')
            sage: R2(0).is_square()
            True
            sage: R2(1).is_square()
            True
            sage: R2(2).is_square()
            False
            sage: R2(3).is_square()
            False
            sage: R2(4).is_square()
            True
            sage: R2(5).is_square()
            False
            sage: R2(6).is_square()
            False
            sage: R2(7).is_square()
            False
            sage: R2(8).is_square()
            False
            sage: R2(9).is_square()
            True

            sage: K = Qp(3,20,'capped-rel')
            sage: K(0).is_square()
            True
            sage: K(1).is_square()
            True
            sage: K(2).is_square()
            False
            sage: K(3).is_square()
            False
            sage: K(4).is_square()
            True
            sage: K(6).is_square()
            False
            sage: K(9).is_square()
            True
            sage: K(1/3).is_square()
            False
            sage: K(1/9).is_square()
            True

            sage: K2 = Qp(2,20,'capped-rel')
            sage: K2(0).is_square()
            True
            sage: K2(1).is_square()
            True
            sage: K2(2).is_square()
            False
            sage: K2(3).is_square()
            False
            sage: K2(4).is_square()
            True
            sage: K2(5).is_square()
            False
            sage: K2(6).is_square()
            False
            sage: K2(7).is_square()
            False
            sage: K2(8).is_square()
            False
            sage: K2(9).is_square()
            True
            sage: K2(1/2).is_square()
            False
            sage: K2(1/4).is_square()
            True"""
    @overload
    def is_square(self) -> Any:
        """pAdicGenericElement.is_square(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_generic_element.pyx (starting at line 1675)

        Return whether this element is a square.

        INPUT:

        - ``self`` -- a `p`-adic element

        EXAMPLES::

            sage: R = Zp(3,20,'capped-rel')
            sage: R(0).is_square()
            True
            sage: R(1).is_square()
            True
            sage: R(2).is_square()
            False

        TESTS::

            sage: R(3).is_square()
            False
            sage: R(4).is_square()
            True
            sage: R(6).is_square()
            False
            sage: R(9).is_square()
            True

            sage: R2 = Zp(2,20,'capped-rel')
            sage: R2(0).is_square()
            True
            sage: R2(1).is_square()
            True
            sage: R2(2).is_square()
            False
            sage: R2(3).is_square()
            False
            sage: R2(4).is_square()
            True
            sage: R2(5).is_square()
            False
            sage: R2(6).is_square()
            False
            sage: R2(7).is_square()
            False
            sage: R2(8).is_square()
            False
            sage: R2(9).is_square()
            True

            sage: K = Qp(3,20,'capped-rel')
            sage: K(0).is_square()
            True
            sage: K(1).is_square()
            True
            sage: K(2).is_square()
            False
            sage: K(3).is_square()
            False
            sage: K(4).is_square()
            True
            sage: K(6).is_square()
            False
            sage: K(9).is_square()
            True
            sage: K(1/3).is_square()
            False
            sage: K(1/9).is_square()
            True

            sage: K2 = Qp(2,20,'capped-rel')
            sage: K2(0).is_square()
            True
            sage: K2(1).is_square()
            True
            sage: K2(2).is_square()
            False
            sage: K2(3).is_square()
            False
            sage: K2(4).is_square()
            True
            sage: K2(5).is_square()
            False
            sage: K2(6).is_square()
            False
            sage: K2(7).is_square()
            False
            sage: K2(8).is_square()
            False
            sage: K2(9).is_square()
            True
            sage: K2(1/2).is_square()
            False
            sage: K2(1/4).is_square()
            True"""
    @overload
    def is_square(self) -> Any:
        """pAdicGenericElement.is_square(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_generic_element.pyx (starting at line 1675)

        Return whether this element is a square.

        INPUT:

        - ``self`` -- a `p`-adic element

        EXAMPLES::

            sage: R = Zp(3,20,'capped-rel')
            sage: R(0).is_square()
            True
            sage: R(1).is_square()
            True
            sage: R(2).is_square()
            False

        TESTS::

            sage: R(3).is_square()
            False
            sage: R(4).is_square()
            True
            sage: R(6).is_square()
            False
            sage: R(9).is_square()
            True

            sage: R2 = Zp(2,20,'capped-rel')
            sage: R2(0).is_square()
            True
            sage: R2(1).is_square()
            True
            sage: R2(2).is_square()
            False
            sage: R2(3).is_square()
            False
            sage: R2(4).is_square()
            True
            sage: R2(5).is_square()
            False
            sage: R2(6).is_square()
            False
            sage: R2(7).is_square()
            False
            sage: R2(8).is_square()
            False
            sage: R2(9).is_square()
            True

            sage: K = Qp(3,20,'capped-rel')
            sage: K(0).is_square()
            True
            sage: K(1).is_square()
            True
            sage: K(2).is_square()
            False
            sage: K(3).is_square()
            False
            sage: K(4).is_square()
            True
            sage: K(6).is_square()
            False
            sage: K(9).is_square()
            True
            sage: K(1/3).is_square()
            False
            sage: K(1/9).is_square()
            True

            sage: K2 = Qp(2,20,'capped-rel')
            sage: K2(0).is_square()
            True
            sage: K2(1).is_square()
            True
            sage: K2(2).is_square()
            False
            sage: K2(3).is_square()
            False
            sage: K2(4).is_square()
            True
            sage: K2(5).is_square()
            False
            sage: K2(6).is_square()
            False
            sage: K2(7).is_square()
            False
            sage: K2(8).is_square()
            False
            sage: K2(9).is_square()
            True
            sage: K2(1/2).is_square()
            False
            sage: K2(1/4).is_square()
            True"""
    @overload
    def is_squarefree(self) -> Any:
        """pAdicGenericElement.is_squarefree(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_generic_element.pyx (starting at line 1789)

        Return whether this element is squarefree, i.e., whether there exists
        no non-unit `g` such that `g^2` divides this element.

        EXAMPLES:

        The zero element is never squarefree::

            sage: K = Qp(2)
            sage: K.zero().is_squarefree()
            False

        In `p`-adic rings, only elements of valuation at most 1 are
        squarefree::

            sage: R = Zp(2)
            sage: R(1).is_squarefree()
            True
            sage: R(2).is_squarefree()
            True
            sage: R(4).is_squarefree()
            False

        This works only if the precision is known sufficiently well::

            sage: R(0,1).is_squarefree()
            Traceback (most recent call last):
            ...
            PrecisionError: element not known to sufficient precision to decide squarefreeness
            sage: R(0,2).is_squarefree()
            False
            sage: R(1,1).is_squarefree()
            True

        For fields we are not so strict about the precision and treat inexact
        zeros as the zero element::

            K(0,0).is_squarefree()
            False"""
    @overload
    def is_squarefree(self) -> Any:
        """pAdicGenericElement.is_squarefree(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_generic_element.pyx (starting at line 1789)

        Return whether this element is squarefree, i.e., whether there exists
        no non-unit `g` such that `g^2` divides this element.

        EXAMPLES:

        The zero element is never squarefree::

            sage: K = Qp(2)
            sage: K.zero().is_squarefree()
            False

        In `p`-adic rings, only elements of valuation at most 1 are
        squarefree::

            sage: R = Zp(2)
            sage: R(1).is_squarefree()
            True
            sage: R(2).is_squarefree()
            True
            sage: R(4).is_squarefree()
            False

        This works only if the precision is known sufficiently well::

            sage: R(0,1).is_squarefree()
            Traceback (most recent call last):
            ...
            PrecisionError: element not known to sufficient precision to decide squarefreeness
            sage: R(0,2).is_squarefree()
            False
            sage: R(1,1).is_squarefree()
            True

        For fields we are not so strict about the precision and treat inexact
        zeros as the zero element::

            K(0,0).is_squarefree()
            False"""
    @overload
    def is_squarefree(self) -> Any:
        """pAdicGenericElement.is_squarefree(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_generic_element.pyx (starting at line 1789)

        Return whether this element is squarefree, i.e., whether there exists
        no non-unit `g` such that `g^2` divides this element.

        EXAMPLES:

        The zero element is never squarefree::

            sage: K = Qp(2)
            sage: K.zero().is_squarefree()
            False

        In `p`-adic rings, only elements of valuation at most 1 are
        squarefree::

            sage: R = Zp(2)
            sage: R(1).is_squarefree()
            True
            sage: R(2).is_squarefree()
            True
            sage: R(4).is_squarefree()
            False

        This works only if the precision is known sufficiently well::

            sage: R(0,1).is_squarefree()
            Traceback (most recent call last):
            ...
            PrecisionError: element not known to sufficient precision to decide squarefreeness
            sage: R(0,2).is_squarefree()
            False
            sage: R(1,1).is_squarefree()
            True

        For fields we are not so strict about the precision and treat inexact
        zeros as the zero element::

            K(0,0).is_squarefree()
            False"""
    @overload
    def is_squarefree(self) -> Any:
        """pAdicGenericElement.is_squarefree(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_generic_element.pyx (starting at line 1789)

        Return whether this element is squarefree, i.e., whether there exists
        no non-unit `g` such that `g^2` divides this element.

        EXAMPLES:

        The zero element is never squarefree::

            sage: K = Qp(2)
            sage: K.zero().is_squarefree()
            False

        In `p`-adic rings, only elements of valuation at most 1 are
        squarefree::

            sage: R = Zp(2)
            sage: R(1).is_squarefree()
            True
            sage: R(2).is_squarefree()
            True
            sage: R(4).is_squarefree()
            False

        This works only if the precision is known sufficiently well::

            sage: R(0,1).is_squarefree()
            Traceback (most recent call last):
            ...
            PrecisionError: element not known to sufficient precision to decide squarefreeness
            sage: R(0,2).is_squarefree()
            False
            sage: R(1,1).is_squarefree()
            True

        For fields we are not so strict about the precision and treat inexact
        zeros as the zero element::

            K(0,0).is_squarefree()
            False"""
    @overload
    def is_squarefree(self) -> Any:
        """pAdicGenericElement.is_squarefree(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_generic_element.pyx (starting at line 1789)

        Return whether this element is squarefree, i.e., whether there exists
        no non-unit `g` such that `g^2` divides this element.

        EXAMPLES:

        The zero element is never squarefree::

            sage: K = Qp(2)
            sage: K.zero().is_squarefree()
            False

        In `p`-adic rings, only elements of valuation at most 1 are
        squarefree::

            sage: R = Zp(2)
            sage: R(1).is_squarefree()
            True
            sage: R(2).is_squarefree()
            True
            sage: R(4).is_squarefree()
            False

        This works only if the precision is known sufficiently well::

            sage: R(0,1).is_squarefree()
            Traceback (most recent call last):
            ...
            PrecisionError: element not known to sufficient precision to decide squarefreeness
            sage: R(0,2).is_squarefree()
            False
            sage: R(1,1).is_squarefree()
            True

        For fields we are not so strict about the precision and treat inexact
        zeros as the zero element::

            K(0,0).is_squarefree()
            False"""
    @overload
    def is_squarefree(self) -> Any:
        """pAdicGenericElement.is_squarefree(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_generic_element.pyx (starting at line 1789)

        Return whether this element is squarefree, i.e., whether there exists
        no non-unit `g` such that `g^2` divides this element.

        EXAMPLES:

        The zero element is never squarefree::

            sage: K = Qp(2)
            sage: K.zero().is_squarefree()
            False

        In `p`-adic rings, only elements of valuation at most 1 are
        squarefree::

            sage: R = Zp(2)
            sage: R(1).is_squarefree()
            True
            sage: R(2).is_squarefree()
            True
            sage: R(4).is_squarefree()
            False

        This works only if the precision is known sufficiently well::

            sage: R(0,1).is_squarefree()
            Traceback (most recent call last):
            ...
            PrecisionError: element not known to sufficient precision to decide squarefreeness
            sage: R(0,2).is_squarefree()
            False
            sage: R(1,1).is_squarefree()
            True

        For fields we are not so strict about the precision and treat inexact
        zeros as the zero element::

            K(0,0).is_squarefree()
            False"""
    @overload
    def is_squarefree(self) -> Any:
        """pAdicGenericElement.is_squarefree(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_generic_element.pyx (starting at line 1789)

        Return whether this element is squarefree, i.e., whether there exists
        no non-unit `g` such that `g^2` divides this element.

        EXAMPLES:

        The zero element is never squarefree::

            sage: K = Qp(2)
            sage: K.zero().is_squarefree()
            False

        In `p`-adic rings, only elements of valuation at most 1 are
        squarefree::

            sage: R = Zp(2)
            sage: R(1).is_squarefree()
            True
            sage: R(2).is_squarefree()
            True
            sage: R(4).is_squarefree()
            False

        This works only if the precision is known sufficiently well::

            sage: R(0,1).is_squarefree()
            Traceback (most recent call last):
            ...
            PrecisionError: element not known to sufficient precision to decide squarefreeness
            sage: R(0,2).is_squarefree()
            False
            sage: R(1,1).is_squarefree()
            True

        For fields we are not so strict about the precision and treat inexact
        zeros as the zero element::

            K(0,0).is_squarefree()
            False"""
    @overload
    def is_squarefree(self) -> Any:
        """pAdicGenericElement.is_squarefree(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_generic_element.pyx (starting at line 1789)

        Return whether this element is squarefree, i.e., whether there exists
        no non-unit `g` such that `g^2` divides this element.

        EXAMPLES:

        The zero element is never squarefree::

            sage: K = Qp(2)
            sage: K.zero().is_squarefree()
            False

        In `p`-adic rings, only elements of valuation at most 1 are
        squarefree::

            sage: R = Zp(2)
            sage: R(1).is_squarefree()
            True
            sage: R(2).is_squarefree()
            True
            sage: R(4).is_squarefree()
            False

        This works only if the precision is known sufficiently well::

            sage: R(0,1).is_squarefree()
            Traceback (most recent call last):
            ...
            PrecisionError: element not known to sufficient precision to decide squarefreeness
            sage: R(0,2).is_squarefree()
            False
            sage: R(1,1).is_squarefree()
            True

        For fields we are not so strict about the precision and treat inexact
        zeros as the zero element::

            K(0,0).is_squarefree()
            False"""
    @overload
    def is_squarefree(self) -> Any:
        """pAdicGenericElement.is_squarefree(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_generic_element.pyx (starting at line 1789)

        Return whether this element is squarefree, i.e., whether there exists
        no non-unit `g` such that `g^2` divides this element.

        EXAMPLES:

        The zero element is never squarefree::

            sage: K = Qp(2)
            sage: K.zero().is_squarefree()
            False

        In `p`-adic rings, only elements of valuation at most 1 are
        squarefree::

            sage: R = Zp(2)
            sage: R(1).is_squarefree()
            True
            sage: R(2).is_squarefree()
            True
            sage: R(4).is_squarefree()
            False

        This works only if the precision is known sufficiently well::

            sage: R(0,1).is_squarefree()
            Traceback (most recent call last):
            ...
            PrecisionError: element not known to sufficient precision to decide squarefreeness
            sage: R(0,2).is_squarefree()
            False
            sage: R(1,1).is_squarefree()
            True

        For fields we are not so strict about the precision and treat inexact
        zeros as the zero element::

            K(0,0).is_squarefree()
            False"""
    def log(self, p_branch=..., pi_branch=..., aprec=..., change_frac=..., algorithm=...) -> Any:
        """pAdicGenericElement.log(self, p_branch=None, pi_branch=None, aprec=None, change_frac=False, algorithm=None)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_generic_element.pyx (starting at line 2459)

        Compute the `p`-adic logarithm of this element.

        The usual power series for the logarithm with values in the additive
        group of a `p`-adic ring only converges for 1-units (units congruent to
        1 modulo `p`).  However, there is a unique extension of the logarithm
        to a homomorphism defined on all the units: If `u = a \\cdot v` is a
        unit with `v \\equiv 1 \\pmod{p}` and `a` a Teichmuller representative,
        then we define `log(u) = log(v)`.  This is the correct extension
        because the units `U` split as a product `U = V \\times \\langle w
        \\rangle`, where `V` is the subgroup of 1-units and `w` is a fundamental
        root of unity.  The `\\langle w \\rangle` factor is torsion, so must go
        to 0 under any homomorphism to the fraction field, which is a torsion
        free group.

        INPUT:

        - ``p_branch`` -- an element in the base ring or its fraction
          field; the implementation will choose the branch of the
          logarithm which sends `p` to ``branch``

        - ``pi_branch`` -- an element in the base ring or its fraction
          field; the implementation will choose the branch of the
          logarithm which sends the uniformizer to ``branch``; you
          may specify at most one of ``p_branch`` and ``pi_branch``,
          and must specify one of them if this element is not a unit

        - ``aprec`` -- integer or ``None`` (default: ``None``); if not
          ``None``, then the result will only be correct to precision
          ``aprec``

        - ``change_frac`` -- in general the codomain of the logarithm should be
          in the `p`-adic field, however, for most neighborhoods of 1, it lies
          in the ring of integers. This flag decides if the codomain should be
          the same as the input (default) or if it should change to the
          fraction field of the input.

        - ``algorithm`` -- ``'generic'``, ``'binary_splitting'`` or ``None`` (default)
          The generic algorithm evaluates naively the series defining the log,
          namely

          .. MATH::

              \\log(1-x) = -x - 1/2 x^2 - 1/3 x^3 - 1/4 x^4 - 1/5 x^5 - \\cdots.

          Its binary complexity is quadratic with respect to the precision.

          The ``'binary_splitting'`` algorithm is faster, it has a quasi-linear
          complexity.
          By default, we use ``'binary_splitting'`` if it is available. Otherwise
          we switch to the ``'generic'`` algorithm.

        .. NOTE::

            What some other systems do:

            - PARI: Seems to define the logarithm for units not congruent
              to 1 as we do.

            - MAGMA: Only implements logarithm for 1-units (version 2.19-2)

        .. TODO::

            There is a soft-linear time algorithm for logarithm described
            by Dan Bernstein at
            http://cr.yp.to/lineartime/multapps-20041007.pdf

        EXAMPLES::

            sage: Z13 = Zp(13, 10)
            sage: a = Z13(14); a
            1 + 13 + O(13^10)
            sage: a.log()
            13 + 6*13^2 + 2*13^3 + 5*13^4 + 10*13^6 + 13^7 + 11*13^8 + 8*13^9 + O(13^10)

            sage: Q13 = Qp(13, 10)
            sage: a = Q13(14); a
            1 + 13 + O(13^10)
            sage: a.log()
            13 + 6*13^2 + 2*13^3 + 5*13^4 + 10*13^6 + 13^7 + 11*13^8 + 8*13^9 + O(13^10)

        Note that the relative precision decreases when we take log.
        Precisely the absolute precision on ``log(a)`` agrees with the relative
        precision on ``a`` thanks to the relation `d\\log(a) = da/a`.

        The call ``log(a)`` works as well::

            sage: log(a)
            13 + 6*13^2 + 2*13^3 + 5*13^4 + 10*13^6 + 13^7 + 11*13^8 + 8*13^9 + O(13^10)
            sage: log(a) == a.log()
            True

        The logarithm is not only defined for 1-units::

            sage: R = Zp(5,10)
            sage: a = R(2)
            sage: a.log()
            2*5 + 3*5^2 + 2*5^3 + 4*5^4 + 2*5^6 + 2*5^7 + 4*5^8 + 2*5^9 + O(5^10)

        If you want to take the logarithm of a non-unit you must specify either
        ``p_branch`` or ``pi_branch``::

            sage: b = R(5)
            sage: b.log()
            Traceback (most recent call last):
            ...
            ValueError: you must specify a branch of the logarithm for non-units
            sage: b.log(p_branch=4)
            4 + O(5^10)
            sage: c = R(10)
            sage: c.log(p_branch=4)
            4 + 2*5 + 3*5^2 + 2*5^3 + 4*5^4 + 2*5^6 + 2*5^7 + 4*5^8 + 2*5^9 + O(5^10)

        The branch parameters are only relevant for elements of nonzero
        valuation::

            sage: a.log(p_branch=0)
            2*5 + 3*5^2 + 2*5^3 + 4*5^4 + 2*5^6 + 2*5^7 + 4*5^8 + 2*5^9 + O(5^10)
            sage: a.log(p_branch=1)
            2*5 + 3*5^2 + 2*5^3 + 4*5^4 + 2*5^6 + 2*5^7 + 4*5^8 + 2*5^9 + O(5^10)

        Logarithms can also be computed in extension fields. First, in an
        Eisenstein extension::

            sage: R = Zp(5,5)
            sage: S.<x> = ZZ[]
            sage: f = x^4 + 15*x^2 + 625*x - 5
            sage: W.<w> = R.ext(f)                                                      # needs sage.libs.ntl
            sage: z = 1 + w^2 + 4*w^7; z                                                # needs sage.libs.ntl
            1 + w^2 + 4*w^7 + O(w^20)
            sage: z.log()                                                               # needs sage.libs.ntl
            w^2 + 2*w^4 + 3*w^6 + 4*w^7 + w^9 + 4*w^10 + 4*w^11 + 4*w^12
             + 3*w^14 + w^15 + w^17 + 3*w^18 + 3*w^19 + O(w^20)

        In an extension, there will usually be a difference between
        specifying ``p_branch`` and ``pi_branch``::

            sage: # needs sage.libs.ntl
            sage: b = W(5)
            sage: b.log()
            Traceback (most recent call last):
            ...
            ValueError: you must specify a branch of the logarithm for non-units
            sage: b.log(p_branch=0)
            O(w^20)
            sage: b.log(p_branch=w)
            w + O(w^20)
            sage: b.log(pi_branch=0)
            3*w^2 + 2*w^4 + 2*w^6 + 3*w^8 + 4*w^10 + w^13 + w^14 + 2*w^15
             + 2*w^16 + w^18 + 4*w^19 + O(w^20)
            sage: b.unit_part().log()
            3*w^2 + 2*w^4 + 2*w^6 + 3*w^8 + 4*w^10 + w^13 + w^14 + 2*w^15
             + 2*w^16 + w^18 + 4*w^19 + O(w^20)
            sage: y = w^2 * 4*w^7; y
            4*w^9 + O(w^29)
            sage: y.log(p_branch=0)
            2*w^2 + 2*w^4 + 2*w^6 + 2*w^8 + w^10 + w^12 + 4*w^13 + 4*w^14 + 3*w^15
             + 4*w^16 + 4*w^17 + w^18 + 4*w^19 + O(w^20)
            sage: y.log(p_branch=w)
            w + 2*w^2 + 2*w^4 + 4*w^5 + 2*w^6 + 2*w^7 + 2*w^8 + 4*w^9 + w^10
             + 3*w^11 + w^12 + 4*w^14 + 4*w^16 + 2*w^17 + w^19 + O(w^20)

        Check that log is multiplicative::

            sage: y.log(p_branch=0) + z.log() - (y*z).log(p_branch=0)                   # needs sage.libs.ntl
            O(w^20)

        Now an unramified example::

            sage: # needs sage.libs.ntl
            sage: g = x^3 + 3*x + 3
            sage: A.<a> = R.ext(g)
            sage: b = 1 + 5*(1 + a^2) + 5^3*(3 + 2*a)
            sage: b.log()
            (a^2 + 1)*5 + (3*a^2 + 4*a + 2)*5^2 + (3*a^2 + 2*a)*5^3
             + (3*a^2 + 2*a + 2)*5^4 + O(5^5)

        Check that log is multiplicative::

            sage: # needs sage.libs.ntl
            sage: c = 3 + 5^2*(2 + 4*a)
            sage: b.log() + c.log() - (b*c).log()
            O(5^5)

        We illustrate the effect of the ``precision`` argument::

            sage: R = ZpCA(7,10)
            sage: x = R(41152263); x
            5 + 3*7^2 + 4*7^3 + 3*7^4 + 5*7^5 + 6*7^6 + 7^9 + O(7^10)
            sage: x.log(aprec = 5)
            7 + 3*7^2 + 4*7^3 + 3*7^4 + O(7^5)
            sage: x.log(aprec = 7)
            7 + 3*7^2 + 4*7^3 + 3*7^4 + 7^5 + 3*7^6 + O(7^7)
            sage: x.log()
            7 + 3*7^2 + 4*7^3 + 3*7^4 + 7^5 + 3*7^6 + 7^7 + 3*7^8 + 4*7^9 + O(7^10)

        The logarithm is not defined for zero::

            sage: R.zero().log()
            Traceback (most recent call last):
            ...
            ValueError: logarithm is not defined at zero

        For elements in a `p`-adic ring, the logarithm will be returned in the
        same ring::

            sage: x = R(2)
            sage: x.log().parent()
            7-adic Ring with capped absolute precision 10
            sage: x = R(14)
            sage: x.log(p_branch=0).parent()
            7-adic Ring with capped absolute precision 10

        This is not possible if the logarithm has negative valuation::

            sage: R = ZpCA(3,10)
            sage: S.<x> = R[]
            sage: f = x^3 - 3
            sage: W.<w> = R.ext(f)                                                      # needs sage.libs.ntl sage.rings.padics
            sage: w.log(p_branch=2)                                                     # needs sage.libs.ntl sage.rings.padics
            Traceback (most recent call last):
            ...
            ValueError: logarithm is not integral, use change_frac=True
            to obtain a result in the fraction field
            sage: w.log(p_branch=2, change_frac=True)                                   # needs sage.libs.ntl sage.rings.padics
            2*w^-3 + O(w^24)

        TESTS:

        Check that the generic algorithm and the binary splitting algorithm
        returns the same answers::

            sage: p = 17
            sage: R = Zp(p)
            sage: a = 1 + p*R.random_element()
            sage: l1 = a.log(algorithm='generic')
            sage: l2 = a.log(algorithm='binary_splitting')
            sage: l1 == l2
            True
            sage: l1.precision_absolute() == l2.precision_absolute()
            True

        Check multiplicativity::

            sage: p = 11
            sage: R = Zp(p, prec=1000)

            sage: x = 1 + p*R.random_element()
            sage: y = 1 + p*R.random_element()
            sage: log(x*y) == log(x) + log(y)
            True

            sage: x = y = 0
            sage: while x == 0:
            ....:     x = R.random_element()
            sage: while y == 0:
            ....:     y = R.random_element()
            sage: branch = R.random_element()
            sage: (x*y).log(p_branch=branch) == x.log(p_branch=branch) + y.log(p_branch=branch)
            True

        Note that multiplicativity may fail in the fixed modulus setting
        due to rounding errors::

            sage: R = ZpFM(2, prec=5)
            sage: R(180).log(p_branch=0) == R(30).log(p_branch=0) + R(6).log(p_branch=0)
            False

        Check that log is the inverse of exp::

            sage: p = 11
            sage: R = Zp(p, prec=1000)
            sage: a = 1 + p*R.random_element()
            sage: exp(log(a)) == a
            True

            sage: a = p*R.random_element()
            sage: log(exp(a)) == a
            True

        Check that results are consistent over a range of precision::

            sage: max_prec = 40
            sage: p = 3
            sage: K = Zp(p, max_prec)
            sage: full_log = (K(1 + p)).log()
            sage: for prec in range(2, max_prec):
            ....:     ll1 = (K(1+p).add_bigoh(prec)).log()
            ....:     ll2 = K(1+p).log(prec)
            ....:     assert ll1 == full_log
            ....:     assert ll2 == full_log
            ....:     assert ll1.precision_absolute() == prec

        Check that ``aprec`` works for fixed-mod elements::

            sage: R = ZpFM(7,10)
            sage: x = R(41152263); x
            5 + 3*7^2 + 4*7^3 + 3*7^4 + 5*7^5 + 6*7^6 + 7^9
            sage: x.log(aprec = 5)
            7 + 3*7^2 + 4*7^3 + 3*7^4
            sage: x.log(aprec = 7)
            7 + 3*7^2 + 4*7^3 + 3*7^4 + 7^5 + 3*7^6
            sage: x.log()                                                               # needs sage.symbolic
            7 + 3*7^2 + 4*7^3 + 3*7^4 + 7^5 + 3*7^6 + 7^7 + 3*7^8 + 4*7^9

        Check that precision is computed correctly in highly ramified
        extensions::

            sage: S.<x> = ZZ[]
            sage: K = Qp(5,5)
            sage: f = x^625 - 5*x - 5

            sage: # needs sage.libs.ntl sage.rings.padics
            sage: W.<w> = K.extension(f)
            sage: z = 1 - w^2 + O(w^11)
            sage: x = 1 - z
            sage: z.log().precision_absolute()
            -975
            sage: (x^5/5).precision_absolute()
            -570
            sage: (x^25/25).precision_absolute()
            -975
            sage: (x^125/125).precision_absolute()
            -775

            sage: # needs sage.libs.ntl
            sage: z = 1 - w + O(w^2)
            sage: x = 1 - z
            sage: z.log().precision_absolute()                                          # needs sage.rings.padics
            -1625
            sage: (x^5/5).precision_absolute()
            -615
            sage: (x^25/25).precision_absolute()
            -1200
            sage: (x^125/125).precision_absolute()
            -1625
            sage: (x^625/625).precision_absolute()
            -1250

            sage: z.log().precision_relative()                                          # needs sage.libs.ntl sage.rings.padics
            250

        Performances::

            sage: R = Zp(17, prec=10^5)
            sage: a = R.random_element()
            sage: b = a.log(p_branch=0)   # should be rather fast

        AUTHORS:

        - William Stein: initial version

        - David Harvey (2006-09-13): corrected subtle precision bug (need to
          take denominators into account! -- see :issue:`53`)

        - Genya Zaytman (2007-02-14): adapted to new `p`-adic class

        - Amnon Besser, Marc Masdeu (2012-02-21): complete rewrite, valid for
          generic `p`-adic rings.

        - Soroosh Yazdani (2013-02-1): Fixed a precision issue in
          :meth:`_log_generic`.  This should really fix the issue with
          divisions.

        - Julian Rueth (2013-02-14): Added doctests, some changes for
          capped-absolute implementations.

        - Xavier Caruso (2017-06): Added binary splitting type algorithms
          over Qp"""
    @overload
    def minimal_polynomial(self, name=..., base=...) -> Any:
        """pAdicGenericElement.minimal_polynomial(self, name='x', base=None)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_generic_element.pyx (starting at line 965)

        Return the minimal polynomial of this element over ``base``.

        INPUT:

        - ``name`` -- string (default: ``'x'``); the name of the variable

        - ``base`` -- a ring (default: the base ring of the parent);
          the base ring over which the minimal polynomial is computed

        EXAMPLES::

            sage: Zp(5,5)(1/3).minimal_polynomial('x')                                  # needs sage.libs.ntl
            (1 + O(5^5))*x + 3 + 5 + 3*5^2 + 5^3 + 3*5^4 + O(5^5)

            sage: Zp(5,5)(1/3).minimal_polynomial('foo')                                # needs sage.libs.ntl
            (1 + O(5^5))*foo + 3 + 5 + 3*5^2 + 5^3 + 3*5^4 + O(5^5)

        ::

            sage: # needs sage.libs.ntl
            sage: K.<a> = QqCR(2^3,5)
            sage: S.<x> = K[]
            sage: L.<pi> = K.extension(x^4 - 2*a)
            sage: pi.minimal_polynomial()                                               # needs sage.symbolic
            (1 + O(2^5))*x^4 + a*2 + a*2^2 + a*2^3 + a*2^4 + a*2^5 + O(2^6)
            sage: (pi^2).minimal_polynomial()                                           # needs sage.symbolic
            (1 + O(2^5))*x^2 + a*2 + a*2^2 + a*2^3 + a*2^4 + a*2^5 + O(2^6)
            sage: (1/pi).minimal_polynomial()                                           # needs sage.symbolic
            (1 + O(2^5))*x^4 + (a^2 + 1)*2^-1 + O(2^4)
            sage: elt = L.random_element()
            sage: P = elt.minimal_polynomial()  # not tested, known bug (see :issue:`32111`)
            sage: P(elt) == 0  # not tested
            True"""
    @overload
    def minimal_polynomial(self) -> Any:
        """pAdicGenericElement.minimal_polynomial(self, name='x', base=None)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_generic_element.pyx (starting at line 965)

        Return the minimal polynomial of this element over ``base``.

        INPUT:

        - ``name`` -- string (default: ``'x'``); the name of the variable

        - ``base`` -- a ring (default: the base ring of the parent);
          the base ring over which the minimal polynomial is computed

        EXAMPLES::

            sage: Zp(5,5)(1/3).minimal_polynomial('x')                                  # needs sage.libs.ntl
            (1 + O(5^5))*x + 3 + 5 + 3*5^2 + 5^3 + 3*5^4 + O(5^5)

            sage: Zp(5,5)(1/3).minimal_polynomial('foo')                                # needs sage.libs.ntl
            (1 + O(5^5))*foo + 3 + 5 + 3*5^2 + 5^3 + 3*5^4 + O(5^5)

        ::

            sage: # needs sage.libs.ntl
            sage: K.<a> = QqCR(2^3,5)
            sage: S.<x> = K[]
            sage: L.<pi> = K.extension(x^4 - 2*a)
            sage: pi.minimal_polynomial()                                               # needs sage.symbolic
            (1 + O(2^5))*x^4 + a*2 + a*2^2 + a*2^3 + a*2^4 + a*2^5 + O(2^6)
            sage: (pi^2).minimal_polynomial()                                           # needs sage.symbolic
            (1 + O(2^5))*x^2 + a*2 + a*2^2 + a*2^3 + a*2^4 + a*2^5 + O(2^6)
            sage: (1/pi).minimal_polynomial()                                           # needs sage.symbolic
            (1 + O(2^5))*x^4 + (a^2 + 1)*2^-1 + O(2^4)
            sage: elt = L.random_element()
            sage: P = elt.minimal_polynomial()  # not tested, known bug (see :issue:`32111`)
            sage: P(elt) == 0  # not tested
            True"""
    @overload
    def minimal_polynomial(self) -> Any:
        """pAdicGenericElement.minimal_polynomial(self, name='x', base=None)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_generic_element.pyx (starting at line 965)

        Return the minimal polynomial of this element over ``base``.

        INPUT:

        - ``name`` -- string (default: ``'x'``); the name of the variable

        - ``base`` -- a ring (default: the base ring of the parent);
          the base ring over which the minimal polynomial is computed

        EXAMPLES::

            sage: Zp(5,5)(1/3).minimal_polynomial('x')                                  # needs sage.libs.ntl
            (1 + O(5^5))*x + 3 + 5 + 3*5^2 + 5^3 + 3*5^4 + O(5^5)

            sage: Zp(5,5)(1/3).minimal_polynomial('foo')                                # needs sage.libs.ntl
            (1 + O(5^5))*foo + 3 + 5 + 3*5^2 + 5^3 + 3*5^4 + O(5^5)

        ::

            sage: # needs sage.libs.ntl
            sage: K.<a> = QqCR(2^3,5)
            sage: S.<x> = K[]
            sage: L.<pi> = K.extension(x^4 - 2*a)
            sage: pi.minimal_polynomial()                                               # needs sage.symbolic
            (1 + O(2^5))*x^4 + a*2 + a*2^2 + a*2^3 + a*2^4 + a*2^5 + O(2^6)
            sage: (pi^2).minimal_polynomial()                                           # needs sage.symbolic
            (1 + O(2^5))*x^2 + a*2 + a*2^2 + a*2^3 + a*2^4 + a*2^5 + O(2^6)
            sage: (1/pi).minimal_polynomial()                                           # needs sage.symbolic
            (1 + O(2^5))*x^4 + (a^2 + 1)*2^-1 + O(2^4)
            sage: elt = L.random_element()
            sage: P = elt.minimal_polynomial()  # not tested, known bug (see :issue:`32111`)
            sage: P(elt) == 0  # not tested
            True"""
    @overload
    def minimal_polynomial(self) -> Any:
        """pAdicGenericElement.minimal_polynomial(self, name='x', base=None)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_generic_element.pyx (starting at line 965)

        Return the minimal polynomial of this element over ``base``.

        INPUT:

        - ``name`` -- string (default: ``'x'``); the name of the variable

        - ``base`` -- a ring (default: the base ring of the parent);
          the base ring over which the minimal polynomial is computed

        EXAMPLES::

            sage: Zp(5,5)(1/3).minimal_polynomial('x')                                  # needs sage.libs.ntl
            (1 + O(5^5))*x + 3 + 5 + 3*5^2 + 5^3 + 3*5^4 + O(5^5)

            sage: Zp(5,5)(1/3).minimal_polynomial('foo')                                # needs sage.libs.ntl
            (1 + O(5^5))*foo + 3 + 5 + 3*5^2 + 5^3 + 3*5^4 + O(5^5)

        ::

            sage: # needs sage.libs.ntl
            sage: K.<a> = QqCR(2^3,5)
            sage: S.<x> = K[]
            sage: L.<pi> = K.extension(x^4 - 2*a)
            sage: pi.minimal_polynomial()                                               # needs sage.symbolic
            (1 + O(2^5))*x^4 + a*2 + a*2^2 + a*2^3 + a*2^4 + a*2^5 + O(2^6)
            sage: (pi^2).minimal_polynomial()                                           # needs sage.symbolic
            (1 + O(2^5))*x^2 + a*2 + a*2^2 + a*2^3 + a*2^4 + a*2^5 + O(2^6)
            sage: (1/pi).minimal_polynomial()                                           # needs sage.symbolic
            (1 + O(2^5))*x^4 + (a^2 + 1)*2^-1 + O(2^4)
            sage: elt = L.random_element()
            sage: P = elt.minimal_polynomial()  # not tested, known bug (see :issue:`32111`)
            sage: P(elt) == 0  # not tested
            True"""
    @overload
    def minimal_polynomial(self) -> Any:
        """pAdicGenericElement.minimal_polynomial(self, name='x', base=None)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_generic_element.pyx (starting at line 965)

        Return the minimal polynomial of this element over ``base``.

        INPUT:

        - ``name`` -- string (default: ``'x'``); the name of the variable

        - ``base`` -- a ring (default: the base ring of the parent);
          the base ring over which the minimal polynomial is computed

        EXAMPLES::

            sage: Zp(5,5)(1/3).minimal_polynomial('x')                                  # needs sage.libs.ntl
            (1 + O(5^5))*x + 3 + 5 + 3*5^2 + 5^3 + 3*5^4 + O(5^5)

            sage: Zp(5,5)(1/3).minimal_polynomial('foo')                                # needs sage.libs.ntl
            (1 + O(5^5))*foo + 3 + 5 + 3*5^2 + 5^3 + 3*5^4 + O(5^5)

        ::

            sage: # needs sage.libs.ntl
            sage: K.<a> = QqCR(2^3,5)
            sage: S.<x> = K[]
            sage: L.<pi> = K.extension(x^4 - 2*a)
            sage: pi.minimal_polynomial()                                               # needs sage.symbolic
            (1 + O(2^5))*x^4 + a*2 + a*2^2 + a*2^3 + a*2^4 + a*2^5 + O(2^6)
            sage: (pi^2).minimal_polynomial()                                           # needs sage.symbolic
            (1 + O(2^5))*x^2 + a*2 + a*2^2 + a*2^3 + a*2^4 + a*2^5 + O(2^6)
            sage: (1/pi).minimal_polynomial()                                           # needs sage.symbolic
            (1 + O(2^5))*x^4 + (a^2 + 1)*2^-1 + O(2^4)
            sage: elt = L.random_element()
            sage: P = elt.minimal_polynomial()  # not tested, known bug (see :issue:`32111`)
            sage: P(elt) == 0  # not tested
            True"""
    def multiplicative_order(self, prec=...) -> Any:
        """pAdicGenericElement.multiplicative_order(self, prec=None)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_generic_element.pyx (starting at line 1846)

        Return the multiplicative order of ``self``, where ``self`` is
        considered to be one if it is one modulo `p^{\\mbox{prec}}`.

        INPUT:

        - ``self`` -- a `p`-adic element
        - ``prec`` -- integer

        OUTPUT: integer; the multiplicative order of ``self``

        EXAMPLES::

            sage: K = Qp(5,20,'capped-rel')
            sage: K(-1).multiplicative_order(20)
            2
            sage: K(1).multiplicative_order(20)
            1
            sage: K(2).multiplicative_order(20)
            +Infinity
            sage: K(5).multiplicative_order(20)
            +Infinity
            sage: K(1/5).multiplicative_order(20)
            +Infinity
            sage: K.zeta().multiplicative_order(20)
            4

        Over unramified extensions::

            sage: # needs sage.libs.ntl
            sage: L1.<a> = Qq(5^3)
            sage: c = L1.teichmuller(a)
            sage: c.multiplicative_order()
            124
            sage: c^124
            1 + O(5^20)

        Over totally ramified extensions::

            sage: # needs sage.libs.ntl
            sage: x = polygen(ZZ, 'x')
            sage: L2.<pi> = Qp(5).extension(x^4 + 5*x^3 + 10*x^2 + 10*x + 5)
            sage: u = 1 + pi
            sage: u.multiplicative_order()
            5
            sage: v = L2.teichmuller(2)
            sage: v.multiplicative_order()
            4
            sage: (u*v).multiplicative_order()
            20

        TESTS::

            sage: R = Zp(5,20,'capped-rel')
            sage: R(-1).multiplicative_order(20)
            2
            sage: R(1).multiplicative_order(20)
            1
            sage: R(2).multiplicative_order(20)
            +Infinity
            sage: R(3).multiplicative_order(20)
            +Infinity
            sage: R(4).multiplicative_order(20)
            +Infinity
            sage: R(5).multiplicative_order(20)
            +Infinity
            sage: R(25).multiplicative_order(20)
            +Infinity
            sage: R.zeta().multiplicative_order(20)
            4"""
    @overload
    def norm(self, base=...) -> Any:
        """pAdicGenericElement.norm(self, base=None)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_generic_element.pyx (starting at line 1032)

        Return the norm of this `p`-adic element over ``base``.

        .. WARNING::

            This is not the `p`-adic absolute value.  This is a field
            theoretic norm down to a base ring.  If you want the
            `p`-adic absolute value, use the method :meth:`abs`
            instead.

        INPUT:

        - ``base`` -- a subring of the parent (default: base ring)

        OUTPUT: the norm of this `p`-adic element over the given base

        EXAMPLES::

            sage: Zp(5)(5).norm()                                                       # needs sage.libs.ntl
            5 + O(5^21)

        ::

            sage: # needs sage.libs.ntl
            sage: K.<a> = QqCR(2^3,5)
            sage: S.<x> = K[]
            sage: L.<pi> = K.extension(x^4 - 2*a)
            sage: pi.norm()  # norm over K                                              # needs sage.symbolic
            a*2 + a*2^2 + a*2^3 + a*2^4 + a*2^5 + O(2^6)
            sage: (pi^2).norm()                                                         # needs sage.symbolic
            a^2*2^2 + O(2^7)
            sage: pi.norm()^2                                                           # needs sage.symbolic
            a^2*2^2 + O(2^7)

        TESTS::

            sage: x = L.random_element()                                                # needs sage.libs.ntl
            sage: y = L.random_element()                                                # needs sage.libs.ntl
            sage: (x*y).norm() == x.norm() * y.norm()  # not tested, known bug (see :issue:`32085`)
            True"""
    @overload
    def norm(self) -> Any:
        """pAdicGenericElement.norm(self, base=None)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_generic_element.pyx (starting at line 1032)

        Return the norm of this `p`-adic element over ``base``.

        .. WARNING::

            This is not the `p`-adic absolute value.  This is a field
            theoretic norm down to a base ring.  If you want the
            `p`-adic absolute value, use the method :meth:`abs`
            instead.

        INPUT:

        - ``base`` -- a subring of the parent (default: base ring)

        OUTPUT: the norm of this `p`-adic element over the given base

        EXAMPLES::

            sage: Zp(5)(5).norm()                                                       # needs sage.libs.ntl
            5 + O(5^21)

        ::

            sage: # needs sage.libs.ntl
            sage: K.<a> = QqCR(2^3,5)
            sage: S.<x> = K[]
            sage: L.<pi> = K.extension(x^4 - 2*a)
            sage: pi.norm()  # norm over K                                              # needs sage.symbolic
            a*2 + a*2^2 + a*2^3 + a*2^4 + a*2^5 + O(2^6)
            sage: (pi^2).norm()                                                         # needs sage.symbolic
            a^2*2^2 + O(2^7)
            sage: pi.norm()^2                                                           # needs sage.symbolic
            a^2*2^2 + O(2^7)

        TESTS::

            sage: x = L.random_element()                                                # needs sage.libs.ntl
            sage: y = L.random_element()                                                # needs sage.libs.ntl
            sage: (x*y).norm() == x.norm() * y.norm()  # not tested, known bug (see :issue:`32085`)
            True"""
    @overload
    def norm(self) -> Any:
        """pAdicGenericElement.norm(self, base=None)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_generic_element.pyx (starting at line 1032)

        Return the norm of this `p`-adic element over ``base``.

        .. WARNING::

            This is not the `p`-adic absolute value.  This is a field
            theoretic norm down to a base ring.  If you want the
            `p`-adic absolute value, use the method :meth:`abs`
            instead.

        INPUT:

        - ``base`` -- a subring of the parent (default: base ring)

        OUTPUT: the norm of this `p`-adic element over the given base

        EXAMPLES::

            sage: Zp(5)(5).norm()                                                       # needs sage.libs.ntl
            5 + O(5^21)

        ::

            sage: # needs sage.libs.ntl
            sage: K.<a> = QqCR(2^3,5)
            sage: S.<x> = K[]
            sage: L.<pi> = K.extension(x^4 - 2*a)
            sage: pi.norm()  # norm over K                                              # needs sage.symbolic
            a*2 + a*2^2 + a*2^3 + a*2^4 + a*2^5 + O(2^6)
            sage: (pi^2).norm()                                                         # needs sage.symbolic
            a^2*2^2 + O(2^7)
            sage: pi.norm()^2                                                           # needs sage.symbolic
            a^2*2^2 + O(2^7)

        TESTS::

            sage: x = L.random_element()                                                # needs sage.libs.ntl
            sage: y = L.random_element()                                                # needs sage.libs.ntl
            sage: (x*y).norm() == x.norm() * y.norm()  # not tested, known bug (see :issue:`32085`)
            True"""
    @overload
    def norm(self) -> Any:
        """pAdicGenericElement.norm(self, base=None)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_generic_element.pyx (starting at line 1032)

        Return the norm of this `p`-adic element over ``base``.

        .. WARNING::

            This is not the `p`-adic absolute value.  This is a field
            theoretic norm down to a base ring.  If you want the
            `p`-adic absolute value, use the method :meth:`abs`
            instead.

        INPUT:

        - ``base`` -- a subring of the parent (default: base ring)

        OUTPUT: the norm of this `p`-adic element over the given base

        EXAMPLES::

            sage: Zp(5)(5).norm()                                                       # needs sage.libs.ntl
            5 + O(5^21)

        ::

            sage: # needs sage.libs.ntl
            sage: K.<a> = QqCR(2^3,5)
            sage: S.<x> = K[]
            sage: L.<pi> = K.extension(x^4 - 2*a)
            sage: pi.norm()  # norm over K                                              # needs sage.symbolic
            a*2 + a*2^2 + a*2^3 + a*2^4 + a*2^5 + O(2^6)
            sage: (pi^2).norm()                                                         # needs sage.symbolic
            a^2*2^2 + O(2^7)
            sage: pi.norm()^2                                                           # needs sage.symbolic
            a^2*2^2 + O(2^7)

        TESTS::

            sage: x = L.random_element()                                                # needs sage.libs.ntl
            sage: y = L.random_element()                                                # needs sage.libs.ntl
            sage: (x*y).norm() == x.norm() * y.norm()  # not tested, known bug (see :issue:`32085`)
            True"""
    @overload
    def norm(self) -> Any:
        """pAdicGenericElement.norm(self, base=None)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_generic_element.pyx (starting at line 1032)

        Return the norm of this `p`-adic element over ``base``.

        .. WARNING::

            This is not the `p`-adic absolute value.  This is a field
            theoretic norm down to a base ring.  If you want the
            `p`-adic absolute value, use the method :meth:`abs`
            instead.

        INPUT:

        - ``base`` -- a subring of the parent (default: base ring)

        OUTPUT: the norm of this `p`-adic element over the given base

        EXAMPLES::

            sage: Zp(5)(5).norm()                                                       # needs sage.libs.ntl
            5 + O(5^21)

        ::

            sage: # needs sage.libs.ntl
            sage: K.<a> = QqCR(2^3,5)
            sage: S.<x> = K[]
            sage: L.<pi> = K.extension(x^4 - 2*a)
            sage: pi.norm()  # norm over K                                              # needs sage.symbolic
            a*2 + a*2^2 + a*2^3 + a*2^4 + a*2^5 + O(2^6)
            sage: (pi^2).norm()                                                         # needs sage.symbolic
            a^2*2^2 + O(2^7)
            sage: pi.norm()^2                                                           # needs sage.symbolic
            a^2*2^2 + O(2^7)

        TESTS::

            sage: x = L.random_element()                                                # needs sage.libs.ntl
            sage: y = L.random_element()                                                # needs sage.libs.ntl
            sage: (x*y).norm() == x.norm() * y.norm()  # not tested, known bug (see :issue:`32085`)
            True"""
    @overload
    def norm(self) -> Any:
        """pAdicGenericElement.norm(self, base=None)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_generic_element.pyx (starting at line 1032)

        Return the norm of this `p`-adic element over ``base``.

        .. WARNING::

            This is not the `p`-adic absolute value.  This is a field
            theoretic norm down to a base ring.  If you want the
            `p`-adic absolute value, use the method :meth:`abs`
            instead.

        INPUT:

        - ``base`` -- a subring of the parent (default: base ring)

        OUTPUT: the norm of this `p`-adic element over the given base

        EXAMPLES::

            sage: Zp(5)(5).norm()                                                       # needs sage.libs.ntl
            5 + O(5^21)

        ::

            sage: # needs sage.libs.ntl
            sage: K.<a> = QqCR(2^3,5)
            sage: S.<x> = K[]
            sage: L.<pi> = K.extension(x^4 - 2*a)
            sage: pi.norm()  # norm over K                                              # needs sage.symbolic
            a*2 + a*2^2 + a*2^3 + a*2^4 + a*2^5 + O(2^6)
            sage: (pi^2).norm()                                                         # needs sage.symbolic
            a^2*2^2 + O(2^7)
            sage: pi.norm()^2                                                           # needs sage.symbolic
            a^2*2^2 + O(2^7)

        TESTS::

            sage: x = L.random_element()                                                # needs sage.libs.ntl
            sage: y = L.random_element()                                                # needs sage.libs.ntl
            sage: (x*y).norm() == x.norm() * y.norm()  # not tested, known bug (see :issue:`32085`)
            True"""
    def nth_root(self, n, all=...) -> Any:
        """pAdicGenericElement.nth_root(self, n, all=False)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_generic_element.pyx (starting at line 3538)

        Return the `n`-th root of this element.

        INPUT:

        - ``n`` -- integer

        - ``all`` -- boolean (default: ``False``); if ``True``,
          return all `n`-th roots of this element, instead of just one

        EXAMPLES::

            sage: A = Zp(5,10)
            sage: x = A(61376); x
            1 + 5^3 + 3*5^4 + 4*5^5 + 3*5^6 + O(5^10)
            sage: y = x.nth_root(4); y
            2 + 5 + 2*5^2 + 4*5^3 + 3*5^4 + 5^6 + O(5^10)
            sage: y^4 == x
            True

            sage: x.nth_root(4, all=True)
            [2 + 5 + 2*5^2 + 4*5^3 + 3*5^4 + 5^6 + O(5^10),
             4 + 4*5 + 4*5^2 + 4*5^4 + 3*5^5 + 5^6 + 3*5^7 + 5^8 + 5^9 + O(5^10),
             3 + 3*5 + 2*5^2 + 5^4 + 4*5^5 + 3*5^6 + 4*5^7 + 4*5^8 + 4*5^9 + O(5^10),
             1 + 4*5^3 + 5^5 + 3*5^6 + 5^7 + 3*5^8 + 3*5^9 + O(5^10)]

        When `n` is divisible by the underlying prime `p`, we
        are losing precision (which is consistent with the fact
        that raising to the `p`-th power increases precision)::

            sage: z = x.nth_root(5); z
            1 + 5^2 + 3*5^3 + 2*5^4 + 5^5 + 3*5^7 + 2*5^8 + O(5^9)
            sage: z^5
            1 + 5^3 + 3*5^4 + 4*5^5 + 3*5^6 + O(5^10)

        Everything works over extensions as well::

            sage: # needs sage.libs.ntl
            sage: W.<a> = Zq(5^3)
            sage: S.<x> = W[]
            sage: R.<pi> = W.extension(x^7 - 5)
            sage: R(5).nth_root(7)
            pi + O(pi^141)
            sage: R(5).nth_root(7, all=True)
            [pi + O(pi^141)]

        An error is raised if the given element is not an `n`-th power
        in the ring::

            sage: R(5).nth_root(11)                                                     # needs sage.libs.ntl
            Traceback (most recent call last):
            ...
            ValueError: this element is not a nth power

        Similarly, when precision on the input is too small, an error
        is raised::

            sage: # needs sage.libs.ntl
            sage: x = R(1,6); x
            1 + O(pi^6)
            sage: x.nth_root(5)
            Traceback (most recent call last):
            ...
            PrecisionError: not enough precision to be sure that this element is a nth power

        Check that :issue:`30314` is fixed::

            sage: # needs sage.libs.ntl
            sage: K = Qp(29)
            sage: x = polygen(K)
            sage: L.<a> = K.extension(x^2 - 29)
            sage: L(4).nth_root(2)
            2 + O(a^40)

        TESTS:

        We check that it works over different fields::

            sage: # needs sage.libs.ntl
            sage: K.<a> = Qq(2^3)
            sage: S.<x> = K[]
            sage: L.<pi> = K.extension(x^2 + 2*x + 2)
            sage: elt = L.random_element()
            sage: elt in (elt^8).nth_root(8, all=True)
            True
            sage: elt = L.random_element()
            sage: elt in (elt^16).nth_root(16, all=True)
            True
            sage: elt = L.random_element()
            sage: elt in (elt^56).nth_root(56, all=True)
            True

            sage: # needs sage.libs.ntl
            sage: K.<a> = Qq(3^2)
            sage: S.<x> = K[]
            sage: Z = (1+x)^3
            sage: E = Z^2 + Z + 1
            sage: L.<pi> = K.extension(E)
            sage: elt = L.random_element()
            sage: elt in (elt^9).nth_root(9, all=True)
            True
            sage: elt = L.random_element()
            sage: elt in (elt^27).nth_root(27, all=True)
            True
            sage: elt = L.random_element()
            sage: elt in (elt^108).nth_root(108, all=True)
            True

            sage: # needs sage.libs.flint sage.libs.ntl
            sage: K.<a> = ZqCA(3^2)
            sage: S.<x> = K[]
            sage: Z = (1+x)^3 + 3*x^2
            sage: E = Z^2 + Z + 1
            sage: L.<pi> = K.extension(E)
            sage: elt = L.random_element()
            sage: elt in (elt^9).nth_root(9, all=True)
            True
            sage: elt = L.random_element()
            sage: try:                                                                  # needs sage.rings.real_double
            ....:     assert elt in (elt^27).nth_root(27, all=True)
            ....: except sage.rings.padics.precision_error.PrecisionError:
            ....:     pass
            sage: elt = L.random_element()
            sage: try:                                                                  # needs sage.rings.real_double
            ....:     assert elt in (elt^108).nth_root(108, all=True)
            ....: except sage.rings.padics.precision_error.PrecisionError:
            ....:     pass

            sage: # needs sage.libs.ntl
            sage: K.<a> = Qq(3^2)
            sage: S.<x> = K[]
            sage: Z = (1+x)^3 + 3*x^3
            sage: E = (Z^2 + Z + 1)(a*x).monic()
            sage: L.<pi> = K.extension(E)
            sage: elt = L.random_element()
            sage: elt in (elt^9).nth_root(9, all=True)
            True
            sage: elt = L.random_element()
            sage: elt in (elt^27).nth_root(27, all=True)
            True
            sage: elt = L.random_element()
            sage: elt in (elt^108).nth_root(108, all=True)
            True"""
    @overload
    def ordp(self, p=...) -> Any:
        """pAdicGenericElement.ordp(self, p=None)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_generic_element.pyx (starting at line 2068)

        Return the valuation of ``self``, normalized so that the valuation of `p` is 1.

        INPUT:

        - ``self`` -- a `p`-adic element
        - ``p`` -- a prime (default: ``None``); if specified, will make sure
          that ``p == self.parent().prime()``

        .. NOTE::

            The optional argument `p` is used for consistency with the valuation
            methods on integers and rationals.

        OUTPUT:

        integer -- the valuation of ``self``, normalized so that the valuation of `p` is 1

        EXAMPLES::

            sage: R = Zp(5,20,'capped-rel')
            sage: R(0).ordp()
            +Infinity
            sage: R(1).ordp()
            0
            sage: R(2).ordp()
            0
            sage: R(5).ordp()
            1
            sage: R(10).ordp()
            1
            sage: R(25).ordp()
            2
            sage: R(50).ordp()
            2
            sage: R(1/2).ordp()
            0"""
    @overload
    def ordp(self) -> Any:
        """pAdicGenericElement.ordp(self, p=None)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_generic_element.pyx (starting at line 2068)

        Return the valuation of ``self``, normalized so that the valuation of `p` is 1.

        INPUT:

        - ``self`` -- a `p`-adic element
        - ``p`` -- a prime (default: ``None``); if specified, will make sure
          that ``p == self.parent().prime()``

        .. NOTE::

            The optional argument `p` is used for consistency with the valuation
            methods on integers and rationals.

        OUTPUT:

        integer -- the valuation of ``self``, normalized so that the valuation of `p` is 1

        EXAMPLES::

            sage: R = Zp(5,20,'capped-rel')
            sage: R(0).ordp()
            +Infinity
            sage: R(1).ordp()
            0
            sage: R(2).ordp()
            0
            sage: R(5).ordp()
            1
            sage: R(10).ordp()
            1
            sage: R(25).ordp()
            2
            sage: R(50).ordp()
            2
            sage: R(1/2).ordp()
            0"""
    @overload
    def ordp(self) -> Any:
        """pAdicGenericElement.ordp(self, p=None)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_generic_element.pyx (starting at line 2068)

        Return the valuation of ``self``, normalized so that the valuation of `p` is 1.

        INPUT:

        - ``self`` -- a `p`-adic element
        - ``p`` -- a prime (default: ``None``); if specified, will make sure
          that ``p == self.parent().prime()``

        .. NOTE::

            The optional argument `p` is used for consistency with the valuation
            methods on integers and rationals.

        OUTPUT:

        integer -- the valuation of ``self``, normalized so that the valuation of `p` is 1

        EXAMPLES::

            sage: R = Zp(5,20,'capped-rel')
            sage: R(0).ordp()
            +Infinity
            sage: R(1).ordp()
            0
            sage: R(2).ordp()
            0
            sage: R(5).ordp()
            1
            sage: R(10).ordp()
            1
            sage: R(25).ordp()
            2
            sage: R(50).ordp()
            2
            sage: R(1/2).ordp()
            0"""
    @overload
    def ordp(self) -> Any:
        """pAdicGenericElement.ordp(self, p=None)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_generic_element.pyx (starting at line 2068)

        Return the valuation of ``self``, normalized so that the valuation of `p` is 1.

        INPUT:

        - ``self`` -- a `p`-adic element
        - ``p`` -- a prime (default: ``None``); if specified, will make sure
          that ``p == self.parent().prime()``

        .. NOTE::

            The optional argument `p` is used for consistency with the valuation
            methods on integers and rationals.

        OUTPUT:

        integer -- the valuation of ``self``, normalized so that the valuation of `p` is 1

        EXAMPLES::

            sage: R = Zp(5,20,'capped-rel')
            sage: R(0).ordp()
            +Infinity
            sage: R(1).ordp()
            0
            sage: R(2).ordp()
            0
            sage: R(5).ordp()
            1
            sage: R(10).ordp()
            1
            sage: R(25).ordp()
            2
            sage: R(50).ordp()
            2
            sage: R(1/2).ordp()
            0"""
    @overload
    def ordp(self) -> Any:
        """pAdicGenericElement.ordp(self, p=None)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_generic_element.pyx (starting at line 2068)

        Return the valuation of ``self``, normalized so that the valuation of `p` is 1.

        INPUT:

        - ``self`` -- a `p`-adic element
        - ``p`` -- a prime (default: ``None``); if specified, will make sure
          that ``p == self.parent().prime()``

        .. NOTE::

            The optional argument `p` is used for consistency with the valuation
            methods on integers and rationals.

        OUTPUT:

        integer -- the valuation of ``self``, normalized so that the valuation of `p` is 1

        EXAMPLES::

            sage: R = Zp(5,20,'capped-rel')
            sage: R(0).ordp()
            +Infinity
            sage: R(1).ordp()
            0
            sage: R(2).ordp()
            0
            sage: R(5).ordp()
            1
            sage: R(10).ordp()
            1
            sage: R(25).ordp()
            2
            sage: R(50).ordp()
            2
            sage: R(1/2).ordp()
            0"""
    @overload
    def ordp(self) -> Any:
        """pAdicGenericElement.ordp(self, p=None)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_generic_element.pyx (starting at line 2068)

        Return the valuation of ``self``, normalized so that the valuation of `p` is 1.

        INPUT:

        - ``self`` -- a `p`-adic element
        - ``p`` -- a prime (default: ``None``); if specified, will make sure
          that ``p == self.parent().prime()``

        .. NOTE::

            The optional argument `p` is used for consistency with the valuation
            methods on integers and rationals.

        OUTPUT:

        integer -- the valuation of ``self``, normalized so that the valuation of `p` is 1

        EXAMPLES::

            sage: R = Zp(5,20,'capped-rel')
            sage: R(0).ordp()
            +Infinity
            sage: R(1).ordp()
            0
            sage: R(2).ordp()
            0
            sage: R(5).ordp()
            1
            sage: R(10).ordp()
            1
            sage: R(25).ordp()
            2
            sage: R(50).ordp()
            2
            sage: R(1/2).ordp()
            0"""
    @overload
    def ordp(self) -> Any:
        """pAdicGenericElement.ordp(self, p=None)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_generic_element.pyx (starting at line 2068)

        Return the valuation of ``self``, normalized so that the valuation of `p` is 1.

        INPUT:

        - ``self`` -- a `p`-adic element
        - ``p`` -- a prime (default: ``None``); if specified, will make sure
          that ``p == self.parent().prime()``

        .. NOTE::

            The optional argument `p` is used for consistency with the valuation
            methods on integers and rationals.

        OUTPUT:

        integer -- the valuation of ``self``, normalized so that the valuation of `p` is 1

        EXAMPLES::

            sage: R = Zp(5,20,'capped-rel')
            sage: R(0).ordp()
            +Infinity
            sage: R(1).ordp()
            0
            sage: R(2).ordp()
            0
            sage: R(5).ordp()
            1
            sage: R(10).ordp()
            1
            sage: R(25).ordp()
            2
            sage: R(50).ordp()
            2
            sage: R(1/2).ordp()
            0"""
    @overload
    def ordp(self) -> Any:
        """pAdicGenericElement.ordp(self, p=None)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_generic_element.pyx (starting at line 2068)

        Return the valuation of ``self``, normalized so that the valuation of `p` is 1.

        INPUT:

        - ``self`` -- a `p`-adic element
        - ``p`` -- a prime (default: ``None``); if specified, will make sure
          that ``p == self.parent().prime()``

        .. NOTE::

            The optional argument `p` is used for consistency with the valuation
            methods on integers and rationals.

        OUTPUT:

        integer -- the valuation of ``self``, normalized so that the valuation of `p` is 1

        EXAMPLES::

            sage: R = Zp(5,20,'capped-rel')
            sage: R(0).ordp()
            +Infinity
            sage: R(1).ordp()
            0
            sage: R(2).ordp()
            0
            sage: R(5).ordp()
            1
            sage: R(10).ordp()
            1
            sage: R(25).ordp()
            2
            sage: R(50).ordp()
            2
            sage: R(1/2).ordp()
            0"""
    @overload
    def ordp(self) -> Any:
        """pAdicGenericElement.ordp(self, p=None)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_generic_element.pyx (starting at line 2068)

        Return the valuation of ``self``, normalized so that the valuation of `p` is 1.

        INPUT:

        - ``self`` -- a `p`-adic element
        - ``p`` -- a prime (default: ``None``); if specified, will make sure
          that ``p == self.parent().prime()``

        .. NOTE::

            The optional argument `p` is used for consistency with the valuation
            methods on integers and rationals.

        OUTPUT:

        integer -- the valuation of ``self``, normalized so that the valuation of `p` is 1

        EXAMPLES::

            sage: R = Zp(5,20,'capped-rel')
            sage: R(0).ordp()
            +Infinity
            sage: R(1).ordp()
            0
            sage: R(2).ordp()
            0
            sage: R(5).ordp()
            1
            sage: R(10).ordp()
            1
            sage: R(25).ordp()
            2
            sage: R(50).ordp()
            2
            sage: R(1/2).ordp()
            0"""
    def polylog(self, n, p_branch=...) -> Any:
        """pAdicGenericElement.polylog(self, n, p_branch=0)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_generic_element.pyx (starting at line 4120)

        Return `Li_n(\\mathrm{self})`, the `n`-th `p`-adic polylogarithm
        of this element.

        INPUT:

        - ``n`` -- nonnegative integer
        - ``p_branch`` -- an element in the base ring or its fraction
          field; the implementation will choose the branch of the
          logarithm which sends `p` to ``p_branch``

        EXAMPLES:

        The `n`-th polylogarithm of `-1` is `0` for even `n`::

            sage: Qp(13)(-1).polylog(6) == 0                                            # needs sage.rings.real_mpfr sage.symbolic
            True

        We can check some identities, for example those mentioned in [DCW2016]_::

            sage: x = Qp(7, prec=30)(1/3)
            sage: (x^2).polylog(4) - 8*x.polylog(4) - 8*(-x).polylog(4) == 0            # needs sage.symbolic
            True

        ::

            sage: x = Qp(5, prec=30)(4)
            sage: x.polylog(2) + (1/x).polylog(2) + x.log(0)**2/2 == 0                  # needs sage.symbolic
            True

        ::

            sage: x = Qp(11, prec=30)(2)
            sage: x.polylog(2) + (1-x).polylog(2) + x.log(0)**2*(1-x).log(0) == 0       # needs sage.symbolic
            True

        `Li_1(z) = -\\log(1-z)` for `|z| < 1`::

            sage: Qp(5)(10).polylog(1) == -Qp(5)(1-10).log(0)
            True

        The dilogarithm of 1 is zero::

            sage: Qp(5)(1).polylog(2)                                                   # needs sage.rings.real_mpfr sage.symbolic
            O(5^20)

        The cubing relation holds for the trilogarithm at 1::

            sage: K = Qp(7)
            sage: z = K.zeta(3)
            sage: -8*K(1).polylog(3) == 9*(K(z).polylog(3) + K(z^2).polylog(3))         # needs sage.rings.padics sage.rings.real_mpfr sage.symbolic
            True

        The polylogarithm of 0 is 0::

            sage: Qp(11)(0).polylog(7)
            0

        Only polylogarithms for positive `n` are defined::

            sage: Qp(11)(2).polylog(-1)
            Traceback (most recent call last):
            ...
            ValueError: polylogarithm only implemented for n at least 0

        Check that :issue:`29222` is fixed::

            sage: K = Qp(7)
            sage: print(K(1 + 7^11).polylog(4))                                         # needs sage.symbolic
            6*7^14 + 3*7^15 + 7^16 + 7^17 + O(7^18)

        ALGORITHM:

        The algorithm of Besser-de Jeu, as described in [BdJ2008]_ is used.

        AUTHORS:

        - Jennifer Balakrishnan - Initial implementation
        - Alex J. Best (2017-07-21) - Extended to other residue disks

        .. TODO::

            - Implement for extensions.
            - Use the change method to create K from ``self.parent()``."""
    @overload
    def rational_reconstruction(self) -> Any:
        """pAdicGenericElement.rational_reconstruction(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_generic_element.pyx (starting at line 2141)

        Return a rational approximation to this `p`-adic number.

        This will raise an :exc:`ArithmeticError` if there are no valid
        approximations to the unit part with numerator and
        denominator bounded by ``sqrt(p^absprec / 2)``.

        .. SEEALSO::

            :meth:`_rational_`

        OUTPUT: rational; an approximation to ``self``

        EXAMPLES::

            sage: R = Zp(5,20,'capped-rel')
            sage: for i in range(11):
            ....:     for j in range(1,10):
            ....:         if j == 5:
            ....:             continue
            ....:         assert i/j == R(i/j).rational_reconstruction()"""
    @overload
    def rational_reconstruction(self) -> Any:
        """pAdicGenericElement.rational_reconstruction(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_generic_element.pyx (starting at line 2141)

        Return a rational approximation to this `p`-adic number.

        This will raise an :exc:`ArithmeticError` if there are no valid
        approximations to the unit part with numerator and
        denominator bounded by ``sqrt(p^absprec / 2)``.

        .. SEEALSO::

            :meth:`_rational_`

        OUTPUT: rational; an approximation to ``self``

        EXAMPLES::

            sage: R = Zp(5,20,'capped-rel')
            sage: for i in range(11):
            ....:     for j in range(1,10):
            ....:         if j == 5:
            ....:             continue
            ....:         assert i/j == R(i/j).rational_reconstruction()"""
    def square_root(self, extend=..., all=..., algorithm=...) -> Any:
        """pAdicGenericElement.square_root(self, extend=True, all=False, algorithm=None)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_generic_element.pyx (starting at line 3336)

        Return the square root of this `p`-adic number.

        INPUT:

        - ``self`` -- a `p`-adic element

        - ``extend`` -- boolean (default: ``True``); if ``True``, return a
          square root in an extension if necessary; if ``False`` and no root
          exists in the given ring or field, raise a :exc:`ValueError`.

        - ``all`` -- boolean (default: ``False``); if ``True``, return a
          list of all square roots

        - ``algorithm`` -- ``'pari'``, ``'sage'`` or ``None`` (default:
          ``None``); Sage provides an implementation for any extension of
          `\\QQ_p`, whereas only square roots over `\\QQ_p` are implemented in
          PARI. The default is ``'pari'`` if the ground field is `\\QQ_p`,
          ``'sage'`` otherwise.

        OUTPUT:

        The square root or the list of all square roots of this `p`-adic
        number.

        NOTE:

        The square root is chosen (resp. the square roots are ordered) in
        a deterministic way.

        EXAMPLES::

            sage: R = Zp(3, 20)
            sage: R(0).square_root()
            0

            sage: R(1).square_root()
            1 + O(3^20)

            sage: R(2).square_root(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: element is not a square

            sage: -R(4).square_root()
            2 + O(3^20)

            sage: R(9).square_root()
            3 + O(3^21)

        When `p = 2`, the precision of the square root is less
        than the input::

            sage: R2 = Zp(2, 20)
            sage: R2(1).square_root()
            1 + O(2^19)
            sage: R2(4).square_root()
            2 + O(2^20)

            sage: R.<t> = Zq(2^10, 10)                                                  # needs sage.libs.ntl
            sage: u = 1 + 8*t                                                           # needs sage.libs.ntl
            sage: u.square_root()                                                       # needs sage.libs.ntl
            1 + t*2^2 + t^2*2^3 + t^2*2^4 + (t^4 + t^3 + t^2)*2^5 + (t^4 + t^2)*2^6
             + (t^5 + t^2)*2^7 + (t^6 + t^5 + t^4 + t^2)*2^8 + O(2^9)

            sage: # needs sage.libs.ntl
            sage: x = polygen(ZZ, 'x')
            sage: R.<a> = Zp(2).extension(x^3 - 2)
            sage: u = R(1 + a^4 + a^5 + a^7 + a^8, 10); u
            1 + a^4 + a^5 + a^7 + a^8 + O(a^10)
            sage: v = u.square_root(); v
            1 + a^2 + a^4 + a^6 + O(a^7)

        However, observe that the precision increases to its original value
        when we recompute the square of the square root::

            sage: v^2                                                                   # needs sage.libs.ntl
            1 + a^4 + a^5 + a^7 + a^8 + O(a^10)

        If the input does not have enough precision in order to determine if
        the given element has a square root in the ground field, an error is
        raised::

            sage: # needs sage.libs.ntl
            sage: R(1, 6).square_root()
            Traceback (most recent call last):
            ...
            PrecisionError: not enough precision to be sure that this element has a square root
            sage: R(1, 7).square_root()
            1 + O(a^4)
            sage: R(1+a^6, 7).square_root(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: element is not a square

        In particular, an error is raised when we try to compute the square
        root of an inexact zero.

        TESTS::

            sage: R = Qp(5, 100)
            sage: c = R.random_element()
            sage: s = (c^2).square_root()
            sage: s == c or s == -c
            True

            sage: Q2 = Qp(2,20,'capped-rel')
            sage: Q2(1).square_root()
            1 + O(2^19)
            sage: Q2(4).square_root()
            2 + O(2^20)

            sage: Q5 = Qp(5,20,'capped-rel')
            sage: Q5(1).square_root()
            1 + O(5^20)
            sage: Q5(-1).square_root() == Q5.teichmuller(2) or Q5(-1).square_root() == Q5.teichmuller(3)
            True

            sage: Z3 = Zp(3,20,'capped-abs')
            sage: Z3(1).square_root()
            1 + O(3^20)
            sage: Z3(4).square_root() in [ Z3(2), -Z3(2) ]
            True
            sage: Z3(9).square_root()
            3 + O(3^19)

            sage: Z2 = Zp(2,20,'capped-abs')
            sage: Z2(1).square_root()
            1 + O(2^19)
            sage: Z2(4).square_root()
            2 + O(2^18)
            sage: Z2(9).square_root() in [ Z2(3), -Z2(3) ]
            True
            sage: Z2(17).square_root()
            1 + 2^3 + 2^5 + 2^6 + 2^7 + 2^9 + 2^10 + 2^13 + 2^16 + 2^17 + O(2^19)

            sage: Z5 = Zp(5,20,'capped-abs')
            sage: Z5(1).square_root()
            1 + O(5^20)
            sage: Z5(-1).square_root() == Z5.teichmuller(2) or Z5(-1).square_root() == Z5.teichmuller(3)
            True"""
    @overload
    def str(self, mode=...) -> Any:
        """pAdicGenericElement.str(self, mode=None)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_generic_element.pyx (starting at line 533)

        Return a string representation of ``self``.

        EXAMPLES::

            sage: Zp(5,5,print_mode='bars')(1/3).str()[3:]
            '1|3|1|3|2'"""
    @overload
    def str(self) -> Any:
        """pAdicGenericElement.str(self, mode=None)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_generic_element.pyx (starting at line 533)

        Return a string representation of ``self``.

        EXAMPLES::

            sage: Zp(5,5,print_mode='bars')(1/3).str()[3:]
            '1|3|1|3|2'"""
    @overload
    def trace(self, base=...) -> Any:
        """pAdicGenericElement.trace(self, base=None)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_generic_element.pyx (starting at line 1082)

        Return the trace of this `p`-adic element over the base ring.

        INPUT:

        - ``base`` -- a subring of the parent (default: base ring)

        OUTPUT: the trace of this `p`-adic element over the given base

        EXAMPLES::

            sage: Zp(5,5)(5).trace()                                                    # needs sage.libs.ntl
            5 + O(5^6)

            sage: # needs sage.libs.ntl
            sage: K.<a> = QqCR(2^3,7)
            sage: S.<x> = K[]
            sage: L.<pi> = K.extension(x^4 - 4*a*x^3 + 2*a)
            sage: pi.trace()  # trace over K                                            # needs sage.symbolic
            a*2^2 + O(2^8)
            sage: (pi+1).trace()                                                        # needs sage.symbolic
            (a + 1)*2^2 + O(2^7)

        TESTS::

            sage: x = L.random_element()                                                # needs sage.libs.ntl
            sage: y = L.random_element()                                                # needs sage.libs.ntl
            sage: (x+y).trace() == x.trace() + y.trace()  # not tested, known bug (see :issue:`32085`)
            True"""
    @overload
    def trace(self) -> Any:
        """pAdicGenericElement.trace(self, base=None)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_generic_element.pyx (starting at line 1082)

        Return the trace of this `p`-adic element over the base ring.

        INPUT:

        - ``base`` -- a subring of the parent (default: base ring)

        OUTPUT: the trace of this `p`-adic element over the given base

        EXAMPLES::

            sage: Zp(5,5)(5).trace()                                                    # needs sage.libs.ntl
            5 + O(5^6)

            sage: # needs sage.libs.ntl
            sage: K.<a> = QqCR(2^3,7)
            sage: S.<x> = K[]
            sage: L.<pi> = K.extension(x^4 - 4*a*x^3 + 2*a)
            sage: pi.trace()  # trace over K                                            # needs sage.symbolic
            a*2^2 + O(2^8)
            sage: (pi+1).trace()                                                        # needs sage.symbolic
            (a + 1)*2^2 + O(2^7)

        TESTS::

            sage: x = L.random_element()                                                # needs sage.libs.ntl
            sage: y = L.random_element()                                                # needs sage.libs.ntl
            sage: (x+y).trace() == x.trace() + y.trace()  # not tested, known bug (see :issue:`32085`)
            True"""
    @overload
    def trace(self) -> Any:
        """pAdicGenericElement.trace(self, base=None)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_generic_element.pyx (starting at line 1082)

        Return the trace of this `p`-adic element over the base ring.

        INPUT:

        - ``base`` -- a subring of the parent (default: base ring)

        OUTPUT: the trace of this `p`-adic element over the given base

        EXAMPLES::

            sage: Zp(5,5)(5).trace()                                                    # needs sage.libs.ntl
            5 + O(5^6)

            sage: # needs sage.libs.ntl
            sage: K.<a> = QqCR(2^3,7)
            sage: S.<x> = K[]
            sage: L.<pi> = K.extension(x^4 - 4*a*x^3 + 2*a)
            sage: pi.trace()  # trace over K                                            # needs sage.symbolic
            a*2^2 + O(2^8)
            sage: (pi+1).trace()                                                        # needs sage.symbolic
            (a + 1)*2^2 + O(2^7)

        TESTS::

            sage: x = L.random_element()                                                # needs sage.libs.ntl
            sage: y = L.random_element()                                                # needs sage.libs.ntl
            sage: (x+y).trace() == x.trace() + y.trace()  # not tested, known bug (see :issue:`32085`)
            True"""
    @overload
    def trace(self) -> Any:
        """pAdicGenericElement.trace(self, base=None)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_generic_element.pyx (starting at line 1082)

        Return the trace of this `p`-adic element over the base ring.

        INPUT:

        - ``base`` -- a subring of the parent (default: base ring)

        OUTPUT: the trace of this `p`-adic element over the given base

        EXAMPLES::

            sage: Zp(5,5)(5).trace()                                                    # needs sage.libs.ntl
            5 + O(5^6)

            sage: # needs sage.libs.ntl
            sage: K.<a> = QqCR(2^3,7)
            sage: S.<x> = K[]
            sage: L.<pi> = K.extension(x^4 - 4*a*x^3 + 2*a)
            sage: pi.trace()  # trace over K                                            # needs sage.symbolic
            a*2^2 + O(2^8)
            sage: (pi+1).trace()                                                        # needs sage.symbolic
            (a + 1)*2^2 + O(2^7)

        TESTS::

            sage: x = L.random_element()                                                # needs sage.libs.ntl
            sage: y = L.random_element()                                                # needs sage.libs.ntl
            sage: (x+y).trace() == x.trace() + y.trace()  # not tested, known bug (see :issue:`32085`)
            True"""
    @overload
    def trace(self) -> Any:
        """pAdicGenericElement.trace(self, base=None)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_generic_element.pyx (starting at line 1082)

        Return the trace of this `p`-adic element over the base ring.

        INPUT:

        - ``base`` -- a subring of the parent (default: base ring)

        OUTPUT: the trace of this `p`-adic element over the given base

        EXAMPLES::

            sage: Zp(5,5)(5).trace()                                                    # needs sage.libs.ntl
            5 + O(5^6)

            sage: # needs sage.libs.ntl
            sage: K.<a> = QqCR(2^3,7)
            sage: S.<x> = K[]
            sage: L.<pi> = K.extension(x^4 - 4*a*x^3 + 2*a)
            sage: pi.trace()  # trace over K                                            # needs sage.symbolic
            a*2^2 + O(2^8)
            sage: (pi+1).trace()                                                        # needs sage.symbolic
            (a + 1)*2^2 + O(2^7)

        TESTS::

            sage: x = L.random_element()                                                # needs sage.libs.ntl
            sage: y = L.random_element()                                                # needs sage.libs.ntl
            sage: (x+y).trace() == x.trace() + y.trace()  # not tested, known bug (see :issue:`32085`)
            True"""
    @overload
    def val_unit(self) -> Any:
        """pAdicGenericElement.val_unit(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_generic_element.pyx (starting at line 2056)

        Return ``(self.valuation(), self.unit_part())``. To be overridden in
        derived classes.

        EXAMPLES::

            sage: Zp(5,5)(5).val_unit()
            (1, 1 + O(5^5))"""
    @overload
    def val_unit(self) -> Any:
        """pAdicGenericElement.val_unit(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_generic_element.pyx (starting at line 2056)

        Return ``(self.valuation(), self.unit_part())``. To be overridden in
        derived classes.

        EXAMPLES::

            sage: Zp(5,5)(5).val_unit()
            (1, 1 + O(5^5))"""
    @overload
    def valuation(self, p=...) -> Any:
        """pAdicGenericElement.valuation(self, p=None)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_generic_element.pyx (starting at line 1944)

        Return the valuation of this element.

        INPUT:

        - ``self`` -- a `p`-adic element
        - ``p`` -- a prime (default: ``None``); if specified, will make sure
          that ``p == self.parent().prime()``

        .. NOTE::

            The optional argument `p` is used for consistency with the valuation
            methods on integers and rationals.

        OUTPUT: integer; the valuation of ``self``

        EXAMPLES::

            sage: R = Zp(17, 4,'capped-rel')
            sage: a = R(2*17^2)
            sage: a.valuation()
            2
            sage: R = Zp(5, 4,'capped-rel')
            sage: R(0).valuation()
            +Infinity

        TESTS::

            sage: R(1).valuation()
            0
            sage: R(2).valuation()
            0
            sage: R(5).valuation()
            1
            sage: R(10).valuation()
            1
            sage: R(25).valuation()
            2
            sage: R(50).valuation()
            2
            sage: R = Qp(17, 4)
            sage: a = R(2*17^2)
            sage: a.valuation()
            2
            sage: R = Qp(5, 4)
            sage: R(0).valuation()
            +Infinity
            sage: R(1).valuation()
            0
            sage: R(2).valuation()
            0
            sage: R(5).valuation()
            1
            sage: R(10).valuation()
            1
            sage: R(25).valuation()
            2
            sage: R(50).valuation()
            2
            sage: R(1/2).valuation()
            0
            sage: R(1/5).valuation()
            -1
            sage: R(1/10).valuation()
            -1
            sage: R(1/25).valuation()
            -2
            sage: R(1/50).valuation()
            -2

            sage: K.<a> = Qq(25)                                                        # needs sage.libs.ntl
            sage: K(0).valuation()                                                      # needs sage.libs.ntl
            +Infinity

            sage: R(1/50).valuation(5)
            -2
            sage: R(1/50).valuation(3)
            Traceback (most recent call last):
            ...
            ValueError: Ring (5-adic Field with capped relative precision 4) residue field of the wrong characteristic."""
    @overload
    def valuation(self) -> Any:
        """pAdicGenericElement.valuation(self, p=None)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_generic_element.pyx (starting at line 1944)

        Return the valuation of this element.

        INPUT:

        - ``self`` -- a `p`-adic element
        - ``p`` -- a prime (default: ``None``); if specified, will make sure
          that ``p == self.parent().prime()``

        .. NOTE::

            The optional argument `p` is used for consistency with the valuation
            methods on integers and rationals.

        OUTPUT: integer; the valuation of ``self``

        EXAMPLES::

            sage: R = Zp(17, 4,'capped-rel')
            sage: a = R(2*17^2)
            sage: a.valuation()
            2
            sage: R = Zp(5, 4,'capped-rel')
            sage: R(0).valuation()
            +Infinity

        TESTS::

            sage: R(1).valuation()
            0
            sage: R(2).valuation()
            0
            sage: R(5).valuation()
            1
            sage: R(10).valuation()
            1
            sage: R(25).valuation()
            2
            sage: R(50).valuation()
            2
            sage: R = Qp(17, 4)
            sage: a = R(2*17^2)
            sage: a.valuation()
            2
            sage: R = Qp(5, 4)
            sage: R(0).valuation()
            +Infinity
            sage: R(1).valuation()
            0
            sage: R(2).valuation()
            0
            sage: R(5).valuation()
            1
            sage: R(10).valuation()
            1
            sage: R(25).valuation()
            2
            sage: R(50).valuation()
            2
            sage: R(1/2).valuation()
            0
            sage: R(1/5).valuation()
            -1
            sage: R(1/10).valuation()
            -1
            sage: R(1/25).valuation()
            -2
            sage: R(1/50).valuation()
            -2

            sage: K.<a> = Qq(25)                                                        # needs sage.libs.ntl
            sage: K(0).valuation()                                                      # needs sage.libs.ntl
            +Infinity

            sage: R(1/50).valuation(5)
            -2
            sage: R(1/50).valuation(3)
            Traceback (most recent call last):
            ...
            ValueError: Ring (5-adic Field with capped relative precision 4) residue field of the wrong characteristic."""
    @overload
    def valuation(self) -> Any:
        """pAdicGenericElement.valuation(self, p=None)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_generic_element.pyx (starting at line 1944)

        Return the valuation of this element.

        INPUT:

        - ``self`` -- a `p`-adic element
        - ``p`` -- a prime (default: ``None``); if specified, will make sure
          that ``p == self.parent().prime()``

        .. NOTE::

            The optional argument `p` is used for consistency with the valuation
            methods on integers and rationals.

        OUTPUT: integer; the valuation of ``self``

        EXAMPLES::

            sage: R = Zp(17, 4,'capped-rel')
            sage: a = R(2*17^2)
            sage: a.valuation()
            2
            sage: R = Zp(5, 4,'capped-rel')
            sage: R(0).valuation()
            +Infinity

        TESTS::

            sage: R(1).valuation()
            0
            sage: R(2).valuation()
            0
            sage: R(5).valuation()
            1
            sage: R(10).valuation()
            1
            sage: R(25).valuation()
            2
            sage: R(50).valuation()
            2
            sage: R = Qp(17, 4)
            sage: a = R(2*17^2)
            sage: a.valuation()
            2
            sage: R = Qp(5, 4)
            sage: R(0).valuation()
            +Infinity
            sage: R(1).valuation()
            0
            sage: R(2).valuation()
            0
            sage: R(5).valuation()
            1
            sage: R(10).valuation()
            1
            sage: R(25).valuation()
            2
            sage: R(50).valuation()
            2
            sage: R(1/2).valuation()
            0
            sage: R(1/5).valuation()
            -1
            sage: R(1/10).valuation()
            -1
            sage: R(1/25).valuation()
            -2
            sage: R(1/50).valuation()
            -2

            sage: K.<a> = Qq(25)                                                        # needs sage.libs.ntl
            sage: K(0).valuation()                                                      # needs sage.libs.ntl
            +Infinity

            sage: R(1/50).valuation(5)
            -2
            sage: R(1/50).valuation(3)
            Traceback (most recent call last):
            ...
            ValueError: Ring (5-adic Field with capped relative precision 4) residue field of the wrong characteristic."""
    @overload
    def valuation(self) -> Any:
        """pAdicGenericElement.valuation(self, p=None)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_generic_element.pyx (starting at line 1944)

        Return the valuation of this element.

        INPUT:

        - ``self`` -- a `p`-adic element
        - ``p`` -- a prime (default: ``None``); if specified, will make sure
          that ``p == self.parent().prime()``

        .. NOTE::

            The optional argument `p` is used for consistency with the valuation
            methods on integers and rationals.

        OUTPUT: integer; the valuation of ``self``

        EXAMPLES::

            sage: R = Zp(17, 4,'capped-rel')
            sage: a = R(2*17^2)
            sage: a.valuation()
            2
            sage: R = Zp(5, 4,'capped-rel')
            sage: R(0).valuation()
            +Infinity

        TESTS::

            sage: R(1).valuation()
            0
            sage: R(2).valuation()
            0
            sage: R(5).valuation()
            1
            sage: R(10).valuation()
            1
            sage: R(25).valuation()
            2
            sage: R(50).valuation()
            2
            sage: R = Qp(17, 4)
            sage: a = R(2*17^2)
            sage: a.valuation()
            2
            sage: R = Qp(5, 4)
            sage: R(0).valuation()
            +Infinity
            sage: R(1).valuation()
            0
            sage: R(2).valuation()
            0
            sage: R(5).valuation()
            1
            sage: R(10).valuation()
            1
            sage: R(25).valuation()
            2
            sage: R(50).valuation()
            2
            sage: R(1/2).valuation()
            0
            sage: R(1/5).valuation()
            -1
            sage: R(1/10).valuation()
            -1
            sage: R(1/25).valuation()
            -2
            sage: R(1/50).valuation()
            -2

            sage: K.<a> = Qq(25)                                                        # needs sage.libs.ntl
            sage: K(0).valuation()                                                      # needs sage.libs.ntl
            +Infinity

            sage: R(1/50).valuation(5)
            -2
            sage: R(1/50).valuation(3)
            Traceback (most recent call last):
            ...
            ValueError: Ring (5-adic Field with capped relative precision 4) residue field of the wrong characteristic."""
    @overload
    def valuation(self) -> Any:
        """pAdicGenericElement.valuation(self, p=None)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_generic_element.pyx (starting at line 1944)

        Return the valuation of this element.

        INPUT:

        - ``self`` -- a `p`-adic element
        - ``p`` -- a prime (default: ``None``); if specified, will make sure
          that ``p == self.parent().prime()``

        .. NOTE::

            The optional argument `p` is used for consistency with the valuation
            methods on integers and rationals.

        OUTPUT: integer; the valuation of ``self``

        EXAMPLES::

            sage: R = Zp(17, 4,'capped-rel')
            sage: a = R(2*17^2)
            sage: a.valuation()
            2
            sage: R = Zp(5, 4,'capped-rel')
            sage: R(0).valuation()
            +Infinity

        TESTS::

            sage: R(1).valuation()
            0
            sage: R(2).valuation()
            0
            sage: R(5).valuation()
            1
            sage: R(10).valuation()
            1
            sage: R(25).valuation()
            2
            sage: R(50).valuation()
            2
            sage: R = Qp(17, 4)
            sage: a = R(2*17^2)
            sage: a.valuation()
            2
            sage: R = Qp(5, 4)
            sage: R(0).valuation()
            +Infinity
            sage: R(1).valuation()
            0
            sage: R(2).valuation()
            0
            sage: R(5).valuation()
            1
            sage: R(10).valuation()
            1
            sage: R(25).valuation()
            2
            sage: R(50).valuation()
            2
            sage: R(1/2).valuation()
            0
            sage: R(1/5).valuation()
            -1
            sage: R(1/10).valuation()
            -1
            sage: R(1/25).valuation()
            -2
            sage: R(1/50).valuation()
            -2

            sage: K.<a> = Qq(25)                                                        # needs sage.libs.ntl
            sage: K(0).valuation()                                                      # needs sage.libs.ntl
            +Infinity

            sage: R(1/50).valuation(5)
            -2
            sage: R(1/50).valuation(3)
            Traceback (most recent call last):
            ...
            ValueError: Ring (5-adic Field with capped relative precision 4) residue field of the wrong characteristic."""
    @overload
    def valuation(self) -> Any:
        """pAdicGenericElement.valuation(self, p=None)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_generic_element.pyx (starting at line 1944)

        Return the valuation of this element.

        INPUT:

        - ``self`` -- a `p`-adic element
        - ``p`` -- a prime (default: ``None``); if specified, will make sure
          that ``p == self.parent().prime()``

        .. NOTE::

            The optional argument `p` is used for consistency with the valuation
            methods on integers and rationals.

        OUTPUT: integer; the valuation of ``self``

        EXAMPLES::

            sage: R = Zp(17, 4,'capped-rel')
            sage: a = R(2*17^2)
            sage: a.valuation()
            2
            sage: R = Zp(5, 4,'capped-rel')
            sage: R(0).valuation()
            +Infinity

        TESTS::

            sage: R(1).valuation()
            0
            sage: R(2).valuation()
            0
            sage: R(5).valuation()
            1
            sage: R(10).valuation()
            1
            sage: R(25).valuation()
            2
            sage: R(50).valuation()
            2
            sage: R = Qp(17, 4)
            sage: a = R(2*17^2)
            sage: a.valuation()
            2
            sage: R = Qp(5, 4)
            sage: R(0).valuation()
            +Infinity
            sage: R(1).valuation()
            0
            sage: R(2).valuation()
            0
            sage: R(5).valuation()
            1
            sage: R(10).valuation()
            1
            sage: R(25).valuation()
            2
            sage: R(50).valuation()
            2
            sage: R(1/2).valuation()
            0
            sage: R(1/5).valuation()
            -1
            sage: R(1/10).valuation()
            -1
            sage: R(1/25).valuation()
            -2
            sage: R(1/50).valuation()
            -2

            sage: K.<a> = Qq(25)                                                        # needs sage.libs.ntl
            sage: K(0).valuation()                                                      # needs sage.libs.ntl
            +Infinity

            sage: R(1/50).valuation(5)
            -2
            sage: R(1/50).valuation(3)
            Traceback (most recent call last):
            ...
            ValueError: Ring (5-adic Field with capped relative precision 4) residue field of the wrong characteristic."""
    @overload
    def valuation(self) -> Any:
        """pAdicGenericElement.valuation(self, p=None)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_generic_element.pyx (starting at line 1944)

        Return the valuation of this element.

        INPUT:

        - ``self`` -- a `p`-adic element
        - ``p`` -- a prime (default: ``None``); if specified, will make sure
          that ``p == self.parent().prime()``

        .. NOTE::

            The optional argument `p` is used for consistency with the valuation
            methods on integers and rationals.

        OUTPUT: integer; the valuation of ``self``

        EXAMPLES::

            sage: R = Zp(17, 4,'capped-rel')
            sage: a = R(2*17^2)
            sage: a.valuation()
            2
            sage: R = Zp(5, 4,'capped-rel')
            sage: R(0).valuation()
            +Infinity

        TESTS::

            sage: R(1).valuation()
            0
            sage: R(2).valuation()
            0
            sage: R(5).valuation()
            1
            sage: R(10).valuation()
            1
            sage: R(25).valuation()
            2
            sage: R(50).valuation()
            2
            sage: R = Qp(17, 4)
            sage: a = R(2*17^2)
            sage: a.valuation()
            2
            sage: R = Qp(5, 4)
            sage: R(0).valuation()
            +Infinity
            sage: R(1).valuation()
            0
            sage: R(2).valuation()
            0
            sage: R(5).valuation()
            1
            sage: R(10).valuation()
            1
            sage: R(25).valuation()
            2
            sage: R(50).valuation()
            2
            sage: R(1/2).valuation()
            0
            sage: R(1/5).valuation()
            -1
            sage: R(1/10).valuation()
            -1
            sage: R(1/25).valuation()
            -2
            sage: R(1/50).valuation()
            -2

            sage: K.<a> = Qq(25)                                                        # needs sage.libs.ntl
            sage: K(0).valuation()                                                      # needs sage.libs.ntl
            +Infinity

            sage: R(1/50).valuation(5)
            -2
            sage: R(1/50).valuation(3)
            Traceback (most recent call last):
            ...
            ValueError: Ring (5-adic Field with capped relative precision 4) residue field of the wrong characteristic."""
    @overload
    def valuation(self) -> Any:
        """pAdicGenericElement.valuation(self, p=None)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_generic_element.pyx (starting at line 1944)

        Return the valuation of this element.

        INPUT:

        - ``self`` -- a `p`-adic element
        - ``p`` -- a prime (default: ``None``); if specified, will make sure
          that ``p == self.parent().prime()``

        .. NOTE::

            The optional argument `p` is used for consistency with the valuation
            methods on integers and rationals.

        OUTPUT: integer; the valuation of ``self``

        EXAMPLES::

            sage: R = Zp(17, 4,'capped-rel')
            sage: a = R(2*17^2)
            sage: a.valuation()
            2
            sage: R = Zp(5, 4,'capped-rel')
            sage: R(0).valuation()
            +Infinity

        TESTS::

            sage: R(1).valuation()
            0
            sage: R(2).valuation()
            0
            sage: R(5).valuation()
            1
            sage: R(10).valuation()
            1
            sage: R(25).valuation()
            2
            sage: R(50).valuation()
            2
            sage: R = Qp(17, 4)
            sage: a = R(2*17^2)
            sage: a.valuation()
            2
            sage: R = Qp(5, 4)
            sage: R(0).valuation()
            +Infinity
            sage: R(1).valuation()
            0
            sage: R(2).valuation()
            0
            sage: R(5).valuation()
            1
            sage: R(10).valuation()
            1
            sage: R(25).valuation()
            2
            sage: R(50).valuation()
            2
            sage: R(1/2).valuation()
            0
            sage: R(1/5).valuation()
            -1
            sage: R(1/10).valuation()
            -1
            sage: R(1/25).valuation()
            -2
            sage: R(1/50).valuation()
            -2

            sage: K.<a> = Qq(25)                                                        # needs sage.libs.ntl
            sage: K(0).valuation()                                                      # needs sage.libs.ntl
            +Infinity

            sage: R(1/50).valuation(5)
            -2
            sage: R(1/50).valuation(3)
            Traceback (most recent call last):
            ...
            ValueError: Ring (5-adic Field with capped relative precision 4) residue field of the wrong characteristic."""
    @overload
    def valuation(self) -> Any:
        """pAdicGenericElement.valuation(self, p=None)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_generic_element.pyx (starting at line 1944)

        Return the valuation of this element.

        INPUT:

        - ``self`` -- a `p`-adic element
        - ``p`` -- a prime (default: ``None``); if specified, will make sure
          that ``p == self.parent().prime()``

        .. NOTE::

            The optional argument `p` is used for consistency with the valuation
            methods on integers and rationals.

        OUTPUT: integer; the valuation of ``self``

        EXAMPLES::

            sage: R = Zp(17, 4,'capped-rel')
            sage: a = R(2*17^2)
            sage: a.valuation()
            2
            sage: R = Zp(5, 4,'capped-rel')
            sage: R(0).valuation()
            +Infinity

        TESTS::

            sage: R(1).valuation()
            0
            sage: R(2).valuation()
            0
            sage: R(5).valuation()
            1
            sage: R(10).valuation()
            1
            sage: R(25).valuation()
            2
            sage: R(50).valuation()
            2
            sage: R = Qp(17, 4)
            sage: a = R(2*17^2)
            sage: a.valuation()
            2
            sage: R = Qp(5, 4)
            sage: R(0).valuation()
            +Infinity
            sage: R(1).valuation()
            0
            sage: R(2).valuation()
            0
            sage: R(5).valuation()
            1
            sage: R(10).valuation()
            1
            sage: R(25).valuation()
            2
            sage: R(50).valuation()
            2
            sage: R(1/2).valuation()
            0
            sage: R(1/5).valuation()
            -1
            sage: R(1/10).valuation()
            -1
            sage: R(1/25).valuation()
            -2
            sage: R(1/50).valuation()
            -2

            sage: K.<a> = Qq(25)                                                        # needs sage.libs.ntl
            sage: K(0).valuation()                                                      # needs sage.libs.ntl
            +Infinity

            sage: R(1/50).valuation(5)
            -2
            sage: R(1/50).valuation(3)
            Traceback (most recent call last):
            ...
            ValueError: Ring (5-adic Field with capped relative precision 4) residue field of the wrong characteristic."""
    @overload
    def valuation(self) -> Any:
        """pAdicGenericElement.valuation(self, p=None)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_generic_element.pyx (starting at line 1944)

        Return the valuation of this element.

        INPUT:

        - ``self`` -- a `p`-adic element
        - ``p`` -- a prime (default: ``None``); if specified, will make sure
          that ``p == self.parent().prime()``

        .. NOTE::

            The optional argument `p` is used for consistency with the valuation
            methods on integers and rationals.

        OUTPUT: integer; the valuation of ``self``

        EXAMPLES::

            sage: R = Zp(17, 4,'capped-rel')
            sage: a = R(2*17^2)
            sage: a.valuation()
            2
            sage: R = Zp(5, 4,'capped-rel')
            sage: R(0).valuation()
            +Infinity

        TESTS::

            sage: R(1).valuation()
            0
            sage: R(2).valuation()
            0
            sage: R(5).valuation()
            1
            sage: R(10).valuation()
            1
            sage: R(25).valuation()
            2
            sage: R(50).valuation()
            2
            sage: R = Qp(17, 4)
            sage: a = R(2*17^2)
            sage: a.valuation()
            2
            sage: R = Qp(5, 4)
            sage: R(0).valuation()
            +Infinity
            sage: R(1).valuation()
            0
            sage: R(2).valuation()
            0
            sage: R(5).valuation()
            1
            sage: R(10).valuation()
            1
            sage: R(25).valuation()
            2
            sage: R(50).valuation()
            2
            sage: R(1/2).valuation()
            0
            sage: R(1/5).valuation()
            -1
            sage: R(1/10).valuation()
            -1
            sage: R(1/25).valuation()
            -2
            sage: R(1/50).valuation()
            -2

            sage: K.<a> = Qq(25)                                                        # needs sage.libs.ntl
            sage: K(0).valuation()                                                      # needs sage.libs.ntl
            +Infinity

            sage: R(1/50).valuation(5)
            -2
            sage: R(1/50).valuation(3)
            Traceback (most recent call last):
            ...
            ValueError: Ring (5-adic Field with capped relative precision 4) residue field of the wrong characteristic."""
    @overload
    def valuation(self) -> Any:
        """pAdicGenericElement.valuation(self, p=None)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_generic_element.pyx (starting at line 1944)

        Return the valuation of this element.

        INPUT:

        - ``self`` -- a `p`-adic element
        - ``p`` -- a prime (default: ``None``); if specified, will make sure
          that ``p == self.parent().prime()``

        .. NOTE::

            The optional argument `p` is used for consistency with the valuation
            methods on integers and rationals.

        OUTPUT: integer; the valuation of ``self``

        EXAMPLES::

            sage: R = Zp(17, 4,'capped-rel')
            sage: a = R(2*17^2)
            sage: a.valuation()
            2
            sage: R = Zp(5, 4,'capped-rel')
            sage: R(0).valuation()
            +Infinity

        TESTS::

            sage: R(1).valuation()
            0
            sage: R(2).valuation()
            0
            sage: R(5).valuation()
            1
            sage: R(10).valuation()
            1
            sage: R(25).valuation()
            2
            sage: R(50).valuation()
            2
            sage: R = Qp(17, 4)
            sage: a = R(2*17^2)
            sage: a.valuation()
            2
            sage: R = Qp(5, 4)
            sage: R(0).valuation()
            +Infinity
            sage: R(1).valuation()
            0
            sage: R(2).valuation()
            0
            sage: R(5).valuation()
            1
            sage: R(10).valuation()
            1
            sage: R(25).valuation()
            2
            sage: R(50).valuation()
            2
            sage: R(1/2).valuation()
            0
            sage: R(1/5).valuation()
            -1
            sage: R(1/10).valuation()
            -1
            sage: R(1/25).valuation()
            -2
            sage: R(1/50).valuation()
            -2

            sage: K.<a> = Qq(25)                                                        # needs sage.libs.ntl
            sage: K(0).valuation()                                                      # needs sage.libs.ntl
            +Infinity

            sage: R(1/50).valuation(5)
            -2
            sage: R(1/50).valuation(3)
            Traceback (most recent call last):
            ...
            ValueError: Ring (5-adic Field with capped relative precision 4) residue field of the wrong characteristic."""
    @overload
    def valuation(self) -> Any:
        """pAdicGenericElement.valuation(self, p=None)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_generic_element.pyx (starting at line 1944)

        Return the valuation of this element.

        INPUT:

        - ``self`` -- a `p`-adic element
        - ``p`` -- a prime (default: ``None``); if specified, will make sure
          that ``p == self.parent().prime()``

        .. NOTE::

            The optional argument `p` is used for consistency with the valuation
            methods on integers and rationals.

        OUTPUT: integer; the valuation of ``self``

        EXAMPLES::

            sage: R = Zp(17, 4,'capped-rel')
            sage: a = R(2*17^2)
            sage: a.valuation()
            2
            sage: R = Zp(5, 4,'capped-rel')
            sage: R(0).valuation()
            +Infinity

        TESTS::

            sage: R(1).valuation()
            0
            sage: R(2).valuation()
            0
            sage: R(5).valuation()
            1
            sage: R(10).valuation()
            1
            sage: R(25).valuation()
            2
            sage: R(50).valuation()
            2
            sage: R = Qp(17, 4)
            sage: a = R(2*17^2)
            sage: a.valuation()
            2
            sage: R = Qp(5, 4)
            sage: R(0).valuation()
            +Infinity
            sage: R(1).valuation()
            0
            sage: R(2).valuation()
            0
            sage: R(5).valuation()
            1
            sage: R(10).valuation()
            1
            sage: R(25).valuation()
            2
            sage: R(50).valuation()
            2
            sage: R(1/2).valuation()
            0
            sage: R(1/5).valuation()
            -1
            sage: R(1/10).valuation()
            -1
            sage: R(1/25).valuation()
            -2
            sage: R(1/50).valuation()
            -2

            sage: K.<a> = Qq(25)                                                        # needs sage.libs.ntl
            sage: K(0).valuation()                                                      # needs sage.libs.ntl
            +Infinity

            sage: R(1/50).valuation(5)
            -2
            sage: R(1/50).valuation(3)
            Traceback (most recent call last):
            ...
            ValueError: Ring (5-adic Field with capped relative precision 4) residue field of the wrong characteristic."""
    @overload
    def valuation(self) -> Any:
        """pAdicGenericElement.valuation(self, p=None)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_generic_element.pyx (starting at line 1944)

        Return the valuation of this element.

        INPUT:

        - ``self`` -- a `p`-adic element
        - ``p`` -- a prime (default: ``None``); if specified, will make sure
          that ``p == self.parent().prime()``

        .. NOTE::

            The optional argument `p` is used for consistency with the valuation
            methods on integers and rationals.

        OUTPUT: integer; the valuation of ``self``

        EXAMPLES::

            sage: R = Zp(17, 4,'capped-rel')
            sage: a = R(2*17^2)
            sage: a.valuation()
            2
            sage: R = Zp(5, 4,'capped-rel')
            sage: R(0).valuation()
            +Infinity

        TESTS::

            sage: R(1).valuation()
            0
            sage: R(2).valuation()
            0
            sage: R(5).valuation()
            1
            sage: R(10).valuation()
            1
            sage: R(25).valuation()
            2
            sage: R(50).valuation()
            2
            sage: R = Qp(17, 4)
            sage: a = R(2*17^2)
            sage: a.valuation()
            2
            sage: R = Qp(5, 4)
            sage: R(0).valuation()
            +Infinity
            sage: R(1).valuation()
            0
            sage: R(2).valuation()
            0
            sage: R(5).valuation()
            1
            sage: R(10).valuation()
            1
            sage: R(25).valuation()
            2
            sage: R(50).valuation()
            2
            sage: R(1/2).valuation()
            0
            sage: R(1/5).valuation()
            -1
            sage: R(1/10).valuation()
            -1
            sage: R(1/25).valuation()
            -2
            sage: R(1/50).valuation()
            -2

            sage: K.<a> = Qq(25)                                                        # needs sage.libs.ntl
            sage: K(0).valuation()                                                      # needs sage.libs.ntl
            +Infinity

            sage: R(1/50).valuation(5)
            -2
            sage: R(1/50).valuation(3)
            Traceback (most recent call last):
            ...
            ValueError: Ring (5-adic Field with capped relative precision 4) residue field of the wrong characteristic."""
    @overload
    def valuation(self) -> Any:
        """pAdicGenericElement.valuation(self, p=None)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_generic_element.pyx (starting at line 1944)

        Return the valuation of this element.

        INPUT:

        - ``self`` -- a `p`-adic element
        - ``p`` -- a prime (default: ``None``); if specified, will make sure
          that ``p == self.parent().prime()``

        .. NOTE::

            The optional argument `p` is used for consistency with the valuation
            methods on integers and rationals.

        OUTPUT: integer; the valuation of ``self``

        EXAMPLES::

            sage: R = Zp(17, 4,'capped-rel')
            sage: a = R(2*17^2)
            sage: a.valuation()
            2
            sage: R = Zp(5, 4,'capped-rel')
            sage: R(0).valuation()
            +Infinity

        TESTS::

            sage: R(1).valuation()
            0
            sage: R(2).valuation()
            0
            sage: R(5).valuation()
            1
            sage: R(10).valuation()
            1
            sage: R(25).valuation()
            2
            sage: R(50).valuation()
            2
            sage: R = Qp(17, 4)
            sage: a = R(2*17^2)
            sage: a.valuation()
            2
            sage: R = Qp(5, 4)
            sage: R(0).valuation()
            +Infinity
            sage: R(1).valuation()
            0
            sage: R(2).valuation()
            0
            sage: R(5).valuation()
            1
            sage: R(10).valuation()
            1
            sage: R(25).valuation()
            2
            sage: R(50).valuation()
            2
            sage: R(1/2).valuation()
            0
            sage: R(1/5).valuation()
            -1
            sage: R(1/10).valuation()
            -1
            sage: R(1/25).valuation()
            -2
            sage: R(1/50).valuation()
            -2

            sage: K.<a> = Qq(25)                                                        # needs sage.libs.ntl
            sage: K(0).valuation()                                                      # needs sage.libs.ntl
            +Infinity

            sage: R(1/50).valuation(5)
            -2
            sage: R(1/50).valuation(3)
            Traceback (most recent call last):
            ...
            ValueError: Ring (5-adic Field with capped relative precision 4) residue field of the wrong characteristic."""
    @overload
    def valuation(self) -> Any:
        """pAdicGenericElement.valuation(self, p=None)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_generic_element.pyx (starting at line 1944)

        Return the valuation of this element.

        INPUT:

        - ``self`` -- a `p`-adic element
        - ``p`` -- a prime (default: ``None``); if specified, will make sure
          that ``p == self.parent().prime()``

        .. NOTE::

            The optional argument `p` is used for consistency with the valuation
            methods on integers and rationals.

        OUTPUT: integer; the valuation of ``self``

        EXAMPLES::

            sage: R = Zp(17, 4,'capped-rel')
            sage: a = R(2*17^2)
            sage: a.valuation()
            2
            sage: R = Zp(5, 4,'capped-rel')
            sage: R(0).valuation()
            +Infinity

        TESTS::

            sage: R(1).valuation()
            0
            sage: R(2).valuation()
            0
            sage: R(5).valuation()
            1
            sage: R(10).valuation()
            1
            sage: R(25).valuation()
            2
            sage: R(50).valuation()
            2
            sage: R = Qp(17, 4)
            sage: a = R(2*17^2)
            sage: a.valuation()
            2
            sage: R = Qp(5, 4)
            sage: R(0).valuation()
            +Infinity
            sage: R(1).valuation()
            0
            sage: R(2).valuation()
            0
            sage: R(5).valuation()
            1
            sage: R(10).valuation()
            1
            sage: R(25).valuation()
            2
            sage: R(50).valuation()
            2
            sage: R(1/2).valuation()
            0
            sage: R(1/5).valuation()
            -1
            sage: R(1/10).valuation()
            -1
            sage: R(1/25).valuation()
            -2
            sage: R(1/50).valuation()
            -2

            sage: K.<a> = Qq(25)                                                        # needs sage.libs.ntl
            sage: K(0).valuation()                                                      # needs sage.libs.ntl
            +Infinity

            sage: R(1/50).valuation(5)
            -2
            sage: R(1/50).valuation(3)
            Traceback (most recent call last):
            ...
            ValueError: Ring (5-adic Field with capped relative precision 4) residue field of the wrong characteristic."""
    @overload
    def valuation(self) -> Any:
        """pAdicGenericElement.valuation(self, p=None)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_generic_element.pyx (starting at line 1944)

        Return the valuation of this element.

        INPUT:

        - ``self`` -- a `p`-adic element
        - ``p`` -- a prime (default: ``None``); if specified, will make sure
          that ``p == self.parent().prime()``

        .. NOTE::

            The optional argument `p` is used for consistency with the valuation
            methods on integers and rationals.

        OUTPUT: integer; the valuation of ``self``

        EXAMPLES::

            sage: R = Zp(17, 4,'capped-rel')
            sage: a = R(2*17^2)
            sage: a.valuation()
            2
            sage: R = Zp(5, 4,'capped-rel')
            sage: R(0).valuation()
            +Infinity

        TESTS::

            sage: R(1).valuation()
            0
            sage: R(2).valuation()
            0
            sage: R(5).valuation()
            1
            sage: R(10).valuation()
            1
            sage: R(25).valuation()
            2
            sage: R(50).valuation()
            2
            sage: R = Qp(17, 4)
            sage: a = R(2*17^2)
            sage: a.valuation()
            2
            sage: R = Qp(5, 4)
            sage: R(0).valuation()
            +Infinity
            sage: R(1).valuation()
            0
            sage: R(2).valuation()
            0
            sage: R(5).valuation()
            1
            sage: R(10).valuation()
            1
            sage: R(25).valuation()
            2
            sage: R(50).valuation()
            2
            sage: R(1/2).valuation()
            0
            sage: R(1/5).valuation()
            -1
            sage: R(1/10).valuation()
            -1
            sage: R(1/25).valuation()
            -2
            sage: R(1/50).valuation()
            -2

            sage: K.<a> = Qq(25)                                                        # needs sage.libs.ntl
            sage: K(0).valuation()                                                      # needs sage.libs.ntl
            +Infinity

            sage: R(1/50).valuation(5)
            -2
            sage: R(1/50).valuation(3)
            Traceback (most recent call last):
            ...
            ValueError: Ring (5-adic Field with capped relative precision 4) residue field of the wrong characteristic."""
    @overload
    def valuation(self) -> Any:
        """pAdicGenericElement.valuation(self, p=None)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_generic_element.pyx (starting at line 1944)

        Return the valuation of this element.

        INPUT:

        - ``self`` -- a `p`-adic element
        - ``p`` -- a prime (default: ``None``); if specified, will make sure
          that ``p == self.parent().prime()``

        .. NOTE::

            The optional argument `p` is used for consistency with the valuation
            methods on integers and rationals.

        OUTPUT: integer; the valuation of ``self``

        EXAMPLES::

            sage: R = Zp(17, 4,'capped-rel')
            sage: a = R(2*17^2)
            sage: a.valuation()
            2
            sage: R = Zp(5, 4,'capped-rel')
            sage: R(0).valuation()
            +Infinity

        TESTS::

            sage: R(1).valuation()
            0
            sage: R(2).valuation()
            0
            sage: R(5).valuation()
            1
            sage: R(10).valuation()
            1
            sage: R(25).valuation()
            2
            sage: R(50).valuation()
            2
            sage: R = Qp(17, 4)
            sage: a = R(2*17^2)
            sage: a.valuation()
            2
            sage: R = Qp(5, 4)
            sage: R(0).valuation()
            +Infinity
            sage: R(1).valuation()
            0
            sage: R(2).valuation()
            0
            sage: R(5).valuation()
            1
            sage: R(10).valuation()
            1
            sage: R(25).valuation()
            2
            sage: R(50).valuation()
            2
            sage: R(1/2).valuation()
            0
            sage: R(1/5).valuation()
            -1
            sage: R(1/10).valuation()
            -1
            sage: R(1/25).valuation()
            -2
            sage: R(1/50).valuation()
            -2

            sage: K.<a> = Qq(25)                                                        # needs sage.libs.ntl
            sage: K(0).valuation()                                                      # needs sage.libs.ntl
            +Infinity

            sage: R(1/50).valuation(5)
            -2
            sage: R(1/50).valuation(3)
            Traceback (most recent call last):
            ...
            ValueError: Ring (5-adic Field with capped relative precision 4) residue field of the wrong characteristic."""
    @overload
    def valuation(self) -> Any:
        """pAdicGenericElement.valuation(self, p=None)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_generic_element.pyx (starting at line 1944)

        Return the valuation of this element.

        INPUT:

        - ``self`` -- a `p`-adic element
        - ``p`` -- a prime (default: ``None``); if specified, will make sure
          that ``p == self.parent().prime()``

        .. NOTE::

            The optional argument `p` is used for consistency with the valuation
            methods on integers and rationals.

        OUTPUT: integer; the valuation of ``self``

        EXAMPLES::

            sage: R = Zp(17, 4,'capped-rel')
            sage: a = R(2*17^2)
            sage: a.valuation()
            2
            sage: R = Zp(5, 4,'capped-rel')
            sage: R(0).valuation()
            +Infinity

        TESTS::

            sage: R(1).valuation()
            0
            sage: R(2).valuation()
            0
            sage: R(5).valuation()
            1
            sage: R(10).valuation()
            1
            sage: R(25).valuation()
            2
            sage: R(50).valuation()
            2
            sage: R = Qp(17, 4)
            sage: a = R(2*17^2)
            sage: a.valuation()
            2
            sage: R = Qp(5, 4)
            sage: R(0).valuation()
            +Infinity
            sage: R(1).valuation()
            0
            sage: R(2).valuation()
            0
            sage: R(5).valuation()
            1
            sage: R(10).valuation()
            1
            sage: R(25).valuation()
            2
            sage: R(50).valuation()
            2
            sage: R(1/2).valuation()
            0
            sage: R(1/5).valuation()
            -1
            sage: R(1/10).valuation()
            -1
            sage: R(1/25).valuation()
            -2
            sage: R(1/50).valuation()
            -2

            sage: K.<a> = Qq(25)                                                        # needs sage.libs.ntl
            sage: K(0).valuation()                                                      # needs sage.libs.ntl
            +Infinity

            sage: R(1/50).valuation(5)
            -2
            sage: R(1/50).valuation(3)
            Traceback (most recent call last):
            ...
            ValueError: Ring (5-adic Field with capped relative precision 4) residue field of the wrong characteristic."""
    @overload
    def valuation(self) -> Any:
        """pAdicGenericElement.valuation(self, p=None)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_generic_element.pyx (starting at line 1944)

        Return the valuation of this element.

        INPUT:

        - ``self`` -- a `p`-adic element
        - ``p`` -- a prime (default: ``None``); if specified, will make sure
          that ``p == self.parent().prime()``

        .. NOTE::

            The optional argument `p` is used for consistency with the valuation
            methods on integers and rationals.

        OUTPUT: integer; the valuation of ``self``

        EXAMPLES::

            sage: R = Zp(17, 4,'capped-rel')
            sage: a = R(2*17^2)
            sage: a.valuation()
            2
            sage: R = Zp(5, 4,'capped-rel')
            sage: R(0).valuation()
            +Infinity

        TESTS::

            sage: R(1).valuation()
            0
            sage: R(2).valuation()
            0
            sage: R(5).valuation()
            1
            sage: R(10).valuation()
            1
            sage: R(25).valuation()
            2
            sage: R(50).valuation()
            2
            sage: R = Qp(17, 4)
            sage: a = R(2*17^2)
            sage: a.valuation()
            2
            sage: R = Qp(5, 4)
            sage: R(0).valuation()
            +Infinity
            sage: R(1).valuation()
            0
            sage: R(2).valuation()
            0
            sage: R(5).valuation()
            1
            sage: R(10).valuation()
            1
            sage: R(25).valuation()
            2
            sage: R(50).valuation()
            2
            sage: R(1/2).valuation()
            0
            sage: R(1/5).valuation()
            -1
            sage: R(1/10).valuation()
            -1
            sage: R(1/25).valuation()
            -2
            sage: R(1/50).valuation()
            -2

            sage: K.<a> = Qq(25)                                                        # needs sage.libs.ntl
            sage: K(0).valuation()                                                      # needs sage.libs.ntl
            +Infinity

            sage: R(1/50).valuation(5)
            -2
            sage: R(1/50).valuation(3)
            Traceback (most recent call last):
            ...
            ValueError: Ring (5-adic Field with capped relative precision 4) residue field of the wrong characteristic."""
    @overload
    def valuation(self) -> Any:
        """pAdicGenericElement.valuation(self, p=None)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_generic_element.pyx (starting at line 1944)

        Return the valuation of this element.

        INPUT:

        - ``self`` -- a `p`-adic element
        - ``p`` -- a prime (default: ``None``); if specified, will make sure
          that ``p == self.parent().prime()``

        .. NOTE::

            The optional argument `p` is used for consistency with the valuation
            methods on integers and rationals.

        OUTPUT: integer; the valuation of ``self``

        EXAMPLES::

            sage: R = Zp(17, 4,'capped-rel')
            sage: a = R(2*17^2)
            sage: a.valuation()
            2
            sage: R = Zp(5, 4,'capped-rel')
            sage: R(0).valuation()
            +Infinity

        TESTS::

            sage: R(1).valuation()
            0
            sage: R(2).valuation()
            0
            sage: R(5).valuation()
            1
            sage: R(10).valuation()
            1
            sage: R(25).valuation()
            2
            sage: R(50).valuation()
            2
            sage: R = Qp(17, 4)
            sage: a = R(2*17^2)
            sage: a.valuation()
            2
            sage: R = Qp(5, 4)
            sage: R(0).valuation()
            +Infinity
            sage: R(1).valuation()
            0
            sage: R(2).valuation()
            0
            sage: R(5).valuation()
            1
            sage: R(10).valuation()
            1
            sage: R(25).valuation()
            2
            sage: R(50).valuation()
            2
            sage: R(1/2).valuation()
            0
            sage: R(1/5).valuation()
            -1
            sage: R(1/10).valuation()
            -1
            sage: R(1/25).valuation()
            -2
            sage: R(1/50).valuation()
            -2

            sage: K.<a> = Qq(25)                                                        # needs sage.libs.ntl
            sage: K(0).valuation()                                                      # needs sage.libs.ntl
            +Infinity

            sage: R(1/50).valuation(5)
            -2
            sage: R(1/50).valuation(3)
            Traceback (most recent call last):
            ...
            ValueError: Ring (5-adic Field with capped relative precision 4) residue field of the wrong characteristic."""
    @overload
    def valuation(self) -> Any:
        """pAdicGenericElement.valuation(self, p=None)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_generic_element.pyx (starting at line 1944)

        Return the valuation of this element.

        INPUT:

        - ``self`` -- a `p`-adic element
        - ``p`` -- a prime (default: ``None``); if specified, will make sure
          that ``p == self.parent().prime()``

        .. NOTE::

            The optional argument `p` is used for consistency with the valuation
            methods on integers and rationals.

        OUTPUT: integer; the valuation of ``self``

        EXAMPLES::

            sage: R = Zp(17, 4,'capped-rel')
            sage: a = R(2*17^2)
            sage: a.valuation()
            2
            sage: R = Zp(5, 4,'capped-rel')
            sage: R(0).valuation()
            +Infinity

        TESTS::

            sage: R(1).valuation()
            0
            sage: R(2).valuation()
            0
            sage: R(5).valuation()
            1
            sage: R(10).valuation()
            1
            sage: R(25).valuation()
            2
            sage: R(50).valuation()
            2
            sage: R = Qp(17, 4)
            sage: a = R(2*17^2)
            sage: a.valuation()
            2
            sage: R = Qp(5, 4)
            sage: R(0).valuation()
            +Infinity
            sage: R(1).valuation()
            0
            sage: R(2).valuation()
            0
            sage: R(5).valuation()
            1
            sage: R(10).valuation()
            1
            sage: R(25).valuation()
            2
            sage: R(50).valuation()
            2
            sage: R(1/2).valuation()
            0
            sage: R(1/5).valuation()
            -1
            sage: R(1/10).valuation()
            -1
            sage: R(1/25).valuation()
            -2
            sage: R(1/50).valuation()
            -2

            sage: K.<a> = Qq(25)                                                        # needs sage.libs.ntl
            sage: K(0).valuation()                                                      # needs sage.libs.ntl
            +Infinity

            sage: R(1/50).valuation(5)
            -2
            sage: R(1/50).valuation(3)
            Traceback (most recent call last):
            ...
            ValueError: Ring (5-adic Field with capped relative precision 4) residue field of the wrong characteristic."""
    @overload
    def valuation(self) -> Any:
        """pAdicGenericElement.valuation(self, p=None)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_generic_element.pyx (starting at line 1944)

        Return the valuation of this element.

        INPUT:

        - ``self`` -- a `p`-adic element
        - ``p`` -- a prime (default: ``None``); if specified, will make sure
          that ``p == self.parent().prime()``

        .. NOTE::

            The optional argument `p` is used for consistency with the valuation
            methods on integers and rationals.

        OUTPUT: integer; the valuation of ``self``

        EXAMPLES::

            sage: R = Zp(17, 4,'capped-rel')
            sage: a = R(2*17^2)
            sage: a.valuation()
            2
            sage: R = Zp(5, 4,'capped-rel')
            sage: R(0).valuation()
            +Infinity

        TESTS::

            sage: R(1).valuation()
            0
            sage: R(2).valuation()
            0
            sage: R(5).valuation()
            1
            sage: R(10).valuation()
            1
            sage: R(25).valuation()
            2
            sage: R(50).valuation()
            2
            sage: R = Qp(17, 4)
            sage: a = R(2*17^2)
            sage: a.valuation()
            2
            sage: R = Qp(5, 4)
            sage: R(0).valuation()
            +Infinity
            sage: R(1).valuation()
            0
            sage: R(2).valuation()
            0
            sage: R(5).valuation()
            1
            sage: R(10).valuation()
            1
            sage: R(25).valuation()
            2
            sage: R(50).valuation()
            2
            sage: R(1/2).valuation()
            0
            sage: R(1/5).valuation()
            -1
            sage: R(1/10).valuation()
            -1
            sage: R(1/25).valuation()
            -2
            sage: R(1/50).valuation()
            -2

            sage: K.<a> = Qq(25)                                                        # needs sage.libs.ntl
            sage: K(0).valuation()                                                      # needs sage.libs.ntl
            +Infinity

            sage: R(1/50).valuation(5)
            -2
            sage: R(1/50).valuation(3)
            Traceback (most recent call last):
            ...
            ValueError: Ring (5-adic Field with capped relative precision 4) residue field of the wrong characteristic."""
    @overload
    def valuation(self) -> Any:
        """pAdicGenericElement.valuation(self, p=None)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_generic_element.pyx (starting at line 1944)

        Return the valuation of this element.

        INPUT:

        - ``self`` -- a `p`-adic element
        - ``p`` -- a prime (default: ``None``); if specified, will make sure
          that ``p == self.parent().prime()``

        .. NOTE::

            The optional argument `p` is used for consistency with the valuation
            methods on integers and rationals.

        OUTPUT: integer; the valuation of ``self``

        EXAMPLES::

            sage: R = Zp(17, 4,'capped-rel')
            sage: a = R(2*17^2)
            sage: a.valuation()
            2
            sage: R = Zp(5, 4,'capped-rel')
            sage: R(0).valuation()
            +Infinity

        TESTS::

            sage: R(1).valuation()
            0
            sage: R(2).valuation()
            0
            sage: R(5).valuation()
            1
            sage: R(10).valuation()
            1
            sage: R(25).valuation()
            2
            sage: R(50).valuation()
            2
            sage: R = Qp(17, 4)
            sage: a = R(2*17^2)
            sage: a.valuation()
            2
            sage: R = Qp(5, 4)
            sage: R(0).valuation()
            +Infinity
            sage: R(1).valuation()
            0
            sage: R(2).valuation()
            0
            sage: R(5).valuation()
            1
            sage: R(10).valuation()
            1
            sage: R(25).valuation()
            2
            sage: R(50).valuation()
            2
            sage: R(1/2).valuation()
            0
            sage: R(1/5).valuation()
            -1
            sage: R(1/10).valuation()
            -1
            sage: R(1/25).valuation()
            -2
            sage: R(1/50).valuation()
            -2

            sage: K.<a> = Qq(25)                                                        # needs sage.libs.ntl
            sage: K(0).valuation()                                                      # needs sage.libs.ntl
            +Infinity

            sage: R(1/50).valuation(5)
            -2
            sage: R(1/50).valuation(3)
            Traceback (most recent call last):
            ...
            ValueError: Ring (5-adic Field with capped relative precision 4) residue field of the wrong characteristic."""
    def xgcd(self, other) -> Any:
        """pAdicGenericElement.xgcd(self, other)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_generic_element.pyx (starting at line 1503)

        Compute the extended gcd of this element and ``other``.

        INPUT:

        - ``other`` -- an element in the same ring

        OUTPUT:

        A tuple ``r``, ``s``, ``t`` such that ``r`` is a greatest common
        divisor of this element and ``other`` and ``r = s*self + t*other``.

        AUTHORS:

        - Julian Rueth (2012-10-19): initial version

        .. NOTE::

            Since the elements are only given with finite precision, their
            greatest common divisor is in general not unique (not even up to
            units). For example `O(3)` is a representative for the elements 0
            and 3 in the 3-adic ring `\\ZZ_3`. The greatest common
            divisor of `O(3)` and `O(3)` could be (among others) 3 or 0 which
            have different valuation. The algorithm implemented here, will
            return an element of minimal valuation among the possible greatest
            common divisors.

        EXAMPLES:

        The greatest common divisor is either zero or a power of the
        uniformizing parameter::

            sage: R = Zp(3)
            sage: R.zero().xgcd(R.zero())
            (0, 1 + O(3^20), 0)
            sage: R(3).xgcd(9)
            (3 + O(3^21), 1 + O(3^20), 0)

        Unlike for :meth:`gcd`, the result is not lifted to the maximal
        precision possible in the ring; it is such that ``r = s*self +
        t*other`` holds true::

            sage: a = R(3,2); a
            3 + O(3^2)
            sage: b = R(9,3); b
            3^2 + O(3^3)
            sage: a.xgcd(b)
            (3 + O(3^2), 1 + O(3), 0)
            sage: a.xgcd(0)
            (3 + O(3^2), 1 + O(3), 0)

        If both elements are zero, then the result is zero with
        the precision set to the smallest of their precisions::

            sage: a = R.zero(); a
            0
            sage: b = R(0,2); b
            O(3^2)
            sage: a.xgcd(b)
            (O(3^2), 0, 1 + O(3^20))

        If only one element is zero, then the result depends on its precision::

            sage: # needs sage.rings.padics
            sage: R(9).xgcd(R(0,1))
            (O(3), 0, 1 + O(3^20))
            sage: R(9).xgcd(R(0,2))
            (O(3^2), 0, 1 + O(3^20))
            sage: R(9).xgcd(R(0,3))
            (3^2 + O(3^22), 1 + O(3^20), 0)
            sage: R(9).xgcd(R(0,4))
            (3^2 + O(3^22), 1 + O(3^20), 0)

        Over a field, the greatest common divisor is either zero (possibly with
        finite precision) or one::

            sage: K = Qp(3)
            sage: K(3).xgcd(0)
            (1 + O(3^20), 3^-1 + O(3^19), 0)
            sage: K.zero().xgcd(0)
            (0, 1 + O(3^20), 0)
            sage: K.zero().xgcd(K(0,2))
            (O(3^2), 0, 1 + O(3^20))
            sage: K(3).xgcd(4)
            (1 + O(3^20), 3^-1 + O(3^19), 0)

        TESTS:

        The implementation also works over extensions::

            sage: # needs sage.libs.ntl
            sage: K = Qp(3)
            sage: R.<a> = K[]
            sage: L.<a> = K.extension(a^3-3)
            sage: (a+3).xgcd(3)
            (1 + O(a^60),
             a^-1 + 2*a + a^3 + 2*a^4 + 2*a^5 + 2*a^8 + 2*a^9
              + 2*a^12 + 2*a^13 + 2*a^16 + 2*a^17 + 2*a^20 + 2*a^21 + 2*a^24
              + 2*a^25 + 2*a^28 + 2*a^29 + 2*a^32 + 2*a^33 + 2*a^36 + 2*a^37
              + 2*a^40 + 2*a^41 + 2*a^44 + 2*a^45 + 2*a^48 + 2*a^49 + 2*a^52
              + 2*a^53 + 2*a^56 + 2*a^57 + O(a^59),
             0)
            sage: R = Zp(3)
            sage: S.<a> = R[]
            sage: S.<a> = R.extension(a^3-3)
            sage: (a+3).xgcd(3)
            (a + O(a^61),
             1 + 2*a^2 + a^4 + 2*a^5 + 2*a^6 + 2*a^9 + 2*a^10
              + 2*a^13 + 2*a^14 + 2*a^17 + 2*a^18 + 2*a^21 + 2*a^22 + 2*a^25
              + 2*a^26 + 2*a^29 + 2*a^30 + 2*a^33 + 2*a^34 + 2*a^37 + 2*a^38
              + 2*a^41 + 2*a^42 + 2*a^45 + 2*a^46 + 2*a^49 + 2*a^50 + 2*a^53
              + 2*a^54 + 2*a^57 + 2*a^58 + O(a^60),
             0)
            sage: K = Qp(3)
            sage: R.<a> = K[]
            sage: L.<a> = K.extension(a^2-2)
            sage: (a+3).xgcd(3)
            (1 + O(3^20),
             2*a + (a + 1)*3 + (2*a + 1)*3^2 + (a + 2)*3^4 + 3^5
              + (2*a + 2)*3^6 + a*3^7 + (2*a + 1)*3^8 + (a + 2)*3^10 + 3^11
              + (2*a + 2)*3^12 + a*3^13 + (2*a + 1)*3^14 + (a + 2)*3^16
              + 3^17 + (2*a + 2)*3^18 + a*3^19 + O(3^20),
             0)
            sage: R = Zp(3)
            sage: S.<a> = R[]
            sage: S.<a> = R.extension(a^2-2)
            sage: (a+3).xgcd(3)
            (1 + O(3^20),
             2*a + (a + 1)*3 + (2*a + 1)*3^2 + (a + 2)*3^4 + 3^5
              + (2*a + 2)*3^6 + a*3^7 + (2*a + 1)*3^8 + (a + 2)*3^10 + 3^11
              + (2*a + 2)*3^12 + a*3^13 + (2*a + 1)*3^14 + (a + 2)*3^16 + 3^17
              + (2*a + 2)*3^18 + a*3^19 + O(3^20),
             0)

        For elements with a fixed modulus::

            sage: R = ZpFM(3)
            sage: R(3).xgcd(9)
            (3, 1, 0)

        And elements with a capped absolute precision::

            sage: R = ZpCA(3)
            sage: R(3).xgcd(9)
            (3 + O(3^20), 1 + O(3^19), O(3^20))"""
    def __abs__(self) -> Any:
        """pAdicGenericElement.__abs__(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_generic_element.pyx (starting at line 3926)

        Return the `p`-adic absolute value of ``self``.

        This is normalized so that the absolute value of `p` is `1/p`.

        EXAMPLES::

            sage: abs(Qp(5)(15))
            1/5
            sage: abs(Qp(7)(0))
            0

        An unramified extension::

            sage: # needs sage.libs.ntl
            sage: R = Zp(5,5)
            sage: P.<x> = PolynomialRing(R)
            sage: Z25.<u> = R.ext(x^2 - 3)
            sage: abs(u)
            1
            sage: abs(u^24-1)
            1/5

        A ramified extension::

            sage: # needs sage.libs.ntl
            sage: W.<w> = R.ext(x^5 + 75*x^3 - 15*x^2 + 125*x - 5)
            sage: abs(w)
            0.724779663677696
            sage: abs(W(0))
            0.000000000000000"""
    def __floordiv__(self, right) -> Any:
        """pAdicGenericElement.__floordiv__(self, right)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_generic_element.pyx (starting at line 279)

        Divide ``self`` by ``right`` and throws away the nonintegral part if
        ``self.parent()`` is not a field.

        There are a number of reasonable definitions for floor
        division.  Any definition should satisfy the following
        identity:

        (1) a = (a // b) * b + a % b

        If a and b lie in a field, then setting a % b = 0 and a // b =
        a / b provides a canonical way of satisfying this equation.

        However, for elements of integer rings, there are many choices
        of definitions for a // b and a % b that satisfy this
        equation.  Since `p`-adic rings in Sage come equipped with a
        uniformizer pi, we can use the choice of uniformizer in our
        definitions.  Here are some other criteria we might ask for:

        (2) If b = pi^k, the series expansion (in terms of pi) of a //
        b is just the series expansion of a, shifted over by k terms.

        (2') The series expansion of a % pi^k has no terms above
        pi^(k-1).

        The conditions (2) and (2') are equivalent.  But when we
        generalize these conditions to arbitrary b they diverge.

        (3) For general b, the series expansion of a // b is just the
        series expansion of a / b, truncating terms with negative
        exponents of pi.

        (4) For general b, the series expansion of a % b has no terms
        above b.valuation() - 1.

        In order to satisfy (3), one defines

        a // b = (a / b.unit_part()) >> b.valuation()
        a % b = a - (a // b) * b

        In order to satisfy (4), one defines

        a % b = a.lift() % pi.lift()^b.valuation()
        a // b = ((a - a % b) >> b.valuation()) / b.unit_part()


        In Sage we choose option (4) since it has better precision behavior.

        EXAMPLES::

            sage: R = ZpCA(5); a = R(129378); b = R(2398125)
            sage: a // b  # indirect doctest
            1 + 2*5 + 2*5^3 + 4*5^4 + 5^6 + 5^7 + 5^8 + 4*5^9 + 2*5^10 + 4*5^11 + 4*5^12 + 2*5^13 + 3*5^14 + O(5^16)
            sage: a / b
            4*5^-4 + 3*5^-3 + 2*5^-2 + 5^-1 + 3 + 3*5 + 4*5^2 + 2*5^4 + 2*5^6 + 4*5^7 + 5^9 + 5^10 + 5^11 + O(5^12)
            sage: a % b
            3 + O(5^20)
            sage: a
            3 + 2*5^4 + 5^5 + 3*5^6 + 5^7 + O(5^20)
            sage: (a // b) * b + a % b
            3 + 2*5^4 + 5^5 + 3*5^6 + 5^7 + O(5^20)

        The alternative definition::

            sage: c = (a // b.unit_part()) >> b.valuation(); c
            3 + 3*5 + 4*5^2 + 2*5^4 + 2*5^6 + 4*5^7 + 5^9 + 5^10 + 5^11 + O(5^12)
            sage: othermod = a - c*b; othermod
            3 + 5^4 + 3*5^5 + 2*5^6 + 4*5^7 + 5^8 + O(5^16)"""
    def __getitem__(self, n) -> Any:
        '''pAdicGenericElement.__getitem__(self, n)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_generic_element.pyx (starting at line 368)

        Return the coefficient of `p^n` in the series expansion of this
        element, as an integer in the range `0` to `p-1`.

        EXAMPLES::

            sage: R = Zp(7,4,\'capped-rel\',\'series\'); a = R(1/3); a
            5 + 4*7 + 4*7^2 + 4*7^3 + O(7^4)
            sage: a[0]  # indirect doctest
            doctest:warning
            ...
            DeprecationWarning: __getitem__ is changing to match the behavior of number fields. Please use expansion instead.
            See https://github.com/sagemath/sage/issues/14825 for details.
            5
            sage: a[1]
            4

        Negative indices do not have the special meaning they have for regular
        python lists. In the following example, ``a[-1]`` is simply the
        coefficient of `7^{-1}`::

            sage: K = Qp(7,4,\'capped-rel\')
            sage: b = K(1/7 + 7); b
            7^-1 + 7 + O(7^3)
            sage: b[-2]
            0
            sage: b[-1]
            1
            sage: b[0]
            0
            sage: b[1]
            1
            sage: b[2]
            0

        It is an error to access coefficients which are beyond the precision
        bound::

            sage: b[3]
            Traceback (most recent call last):
            ...
            PrecisionError
            sage: b[-2]
            0

        Slices also work::

            sage: a[0:2]
            5 + 4*7 + O(7^2)
            sage: a[-1:3:2]
            5 + 4*7^2 + O(7^3)
            sage: b[0:2]
            7 + O(7^2)
            sage: b[-1:3:2]
            7^-1 + 7 + O(7^3)

        If the slice includes coefficients which are beyond the precision
        bound, they are ignored. This is similar to the behaviour of slices of
        python lists::

            sage: a[3:7]
            4*7^3 + O(7^4)
            sage: b[3:7]
            O(7^3)

        For extension elements, "zeros" match the behavior of
        ``list``::

            sage: # needs sage.libs.ntl
            sage: S.<a> = Qq(125)
            sage: a[-2]                                                                 # needs sage.rings.padics
            []

        .. SEEALSO::

            :meth:`sage.rings.padics.local_generic_element.LocalGenericElement.slice`'''
    def __invert__(self) -> Any:
        """pAdicGenericElement.__invert__(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/padic_generic_element.pyx (starting at line 450)

        Return the multiplicative inverse of ``self``.

        EXAMPLES::

            sage: R = Zp(7,4,'capped-rel','series'); a = R(3); a
            3 + O(7^4)
            sage: ~a  # indirect doctest
            5 + 4*7 + 4*7^2 + 4*7^3 + O(7^4)

        .. NOTE::

            The element returned is an element of the fraction field."""
    def __rfloordiv__(self, other):
        """Return value//self."""
