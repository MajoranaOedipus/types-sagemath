import _cython_3_2_1
import cypari2.pari_instance
import sage.rings.polynomial.polynomial_element
from sage.categories.category import ZZ as ZZ
from sage.libs.ntl.ntl_ZZX import ZZX as ZZX
from sage.libs.ntl.ntl_ZZ_pX import ZZ_pX as ZZ_pX
from sage.rings.fraction_field_element import FractionFieldElement as FractionFieldElement
from sage.rings.infinity import infinity as infinity
from sage.structure.element import canonical_coercion as canonical_coercion, coerce_binop as coerce_binop, have_same_parent as have_same_parent, parent as parent
from typing import Any, ClassVar, overload

make_element: _cython_3_2_1.cython_function_or_method
pari: cypari2.pari_instance.Pari
small_roots: _cython_3_2_1.cython_function_or_method
zz_p_max: int

class Polynomial_dense_mod_n(sage.rings.polynomial.polynomial_element.Polynomial):
    """Polynomial_dense_mod_n(parent, x=None, check=True, is_gen=False, construct=False)

    File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_modn_dense_ntl.pyx (starting at line 66)

    A dense polynomial over the integers modulo n, where n is composite, with
    the underlying arithmetic done using NTL.

    EXAMPLES::

        sage: R.<x> = PolynomialRing(Integers(16), implementation='NTL')
        sage: f = x^3 - x + 17
        sage: f^2
        x^6 + 14*x^4 + 2*x^3 + x^2 + 14*x + 1

        sage: loads(f.dumps()) == f
        True

        sage: R.<x> = PolynomialRing(Integers(100), implementation='NTL')
        sage: p = 3*x
        sage: q = 7*x
        sage: p + q
        10*x
        sage: R.<x> = PolynomialRing(Integers(8), implementation='NTL')
        sage: parent(p)
        Univariate Polynomial Ring in x over Ring of integers modulo 100 (using NTL)
        sage: p + q
        10*x
        sage: R({10:-1})
        7*x^10

    TESTS::

        sage: f = Integers(5*2^100)['x'].random_element()
        sage: from sage.rings.polynomial.polynomial_modn_dense_ntl import Polynomial_dense_mod_n
        sage: isinstance(f, Polynomial_dense_mod_n)
        True"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, parent, x=..., check=..., is_gen=..., construct=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_modn_dense_ntl.pyx (starting at line 101)"""
    def compose_mod(self, other, modulus) -> Any:
        """Polynomial_dense_mod_n.compose_mod(self, other, modulus)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_modn_dense_ntl.pyx (starting at line 428)

        Compute `f(g) \\pmod h`.

        To be precise about the order fo compostion, given ``self``, ``other``
        and ``modulus`` as `f(x)`, `g(x)` and `h(x)` compute `f(g(x)) \\bmod h(x)`.

        INPUT:

        - ``other`` -- a polynomial `g(x)`
        - ``modulus`` -- a polynomial `h(x)`

        EXAMPLES::

            sage: R.<x> = GF(2**127 - 1)[]
            sage: f = R.random_element()
            sage: g = R.random_element()
            sage: g.compose_mod(g, f) == g(g) % f
            True

            sage: R.<x> = GF(163)[]
            sage: f = R([i for i in range(100)])
            sage: g = R([i**2 for i in range(100)])
            sage: h = 1 + x + x**5
            sage: f.compose_mod(g, h)
            82*x^4 + 56*x^3 + 45*x^2 + 60*x + 127
            sage: f.compose_mod(g, h) == f(g) % h
            True

        AUTHORS:

        - Giacomo Pope (2024-08) initial implementation"""
    @overload
    def degree(self, gen=...) -> Any:
        """Polynomial_dense_mod_n.degree(self, gen=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_modn_dense_ntl.pyx (starting at line 292)

        Return the degree of this polynomial.

        The zero polynomial has degree -1.

        EXAMPLES::

            sage: R.<x> = PolynomialRing(Integers(100), implementation='NTL')
            sage: (x^3 + 3*x - 17).degree()
            3
            sage: R.zero().degree()
            -1

        TESTS:

        Check output type (see :issue:`25182`)::

            sage: R.<x> = PolynomialRing(Integers(3), implementation='NTL')
            sage: isinstance(x.degree(), Integer)
            True"""
    @overload
    def degree(self) -> Any:
        """Polynomial_dense_mod_n.degree(self, gen=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_modn_dense_ntl.pyx (starting at line 292)

        Return the degree of this polynomial.

        The zero polynomial has degree -1.

        EXAMPLES::

            sage: R.<x> = PolynomialRing(Integers(100), implementation='NTL')
            sage: (x^3 + 3*x - 17).degree()
            3
            sage: R.zero().degree()
            -1

        TESTS:

        Check output type (see :issue:`25182`)::

            sage: R.<x> = PolynomialRing(Integers(3), implementation='NTL')
            sage: isinstance(x.degree(), Integer)
            True"""
    @overload
    def degree(self) -> Any:
        """Polynomial_dense_mod_n.degree(self, gen=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_modn_dense_ntl.pyx (starting at line 292)

        Return the degree of this polynomial.

        The zero polynomial has degree -1.

        EXAMPLES::

            sage: R.<x> = PolynomialRing(Integers(100), implementation='NTL')
            sage: (x^3 + 3*x - 17).degree()
            3
            sage: R.zero().degree()
            -1

        TESTS:

        Check output type (see :issue:`25182`)::

            sage: R.<x> = PolynomialRing(Integers(3), implementation='NTL')
            sage: isinstance(x.degree(), Integer)
            True"""
    @overload
    def degree(self) -> Any:
        """Polynomial_dense_mod_n.degree(self, gen=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_modn_dense_ntl.pyx (starting at line 292)

        Return the degree of this polynomial.

        The zero polynomial has degree -1.

        EXAMPLES::

            sage: R.<x> = PolynomialRing(Integers(100), implementation='NTL')
            sage: (x^3 + 3*x - 17).degree()
            3
            sage: R.zero().degree()
            -1

        TESTS:

        Check output type (see :issue:`25182`)::

            sage: R.<x> = PolynomialRing(Integers(3), implementation='NTL')
            sage: isinstance(x.degree(), Integer)
            True"""
    def int_list(self) -> Any:
        """Polynomial_dense_mod_n.int_list(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_modn_dense_ntl.pyx (starting at line 161)"""
    @overload
    def list(self, boolcopy=...) -> list:
        """Polynomial_dense_mod_n.list(self, bool copy=True) -> list

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_modn_dense_ntl.pyx (starting at line 316)

        Return a new copy of the list of the underlying
        elements of ``self``.

        EXAMPLES::

            sage: _.<x> = PolynomialRing(Integers(100), implementation='NTL')
            sage: f = x^3 + 3*x - 17
            sage: f.list()
            [83, 3, 0, 1]"""
    @overload
    def list(self) -> Any:
        """Polynomial_dense_mod_n.list(self, bool copy=True) -> list

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_modn_dense_ntl.pyx (starting at line 316)

        Return a new copy of the list of the underlying
        elements of ``self``.

        EXAMPLES::

            sage: _.<x> = PolynomialRing(Integers(100), implementation='NTL')
            sage: f = x^3 + 3*x - 17
            sage: f.list()
            [83, 3, 0, 1]"""
    @overload
    def minpoly_mod(self, other) -> Any:
        """Polynomial_dense_mod_n.minpoly_mod(self, other)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_modn_dense_ntl.pyx (starting at line 377)

        Compute the minimal polynomial of this polynomial modulo another
        polynomial in the same ring.

        ALGORITHM:

        NTL's ``MinPolyMod()``, which uses Shoup's algorithm [Sho1999]_.

        EXAMPLES::

            sage: R.<x> = PolynomialRing(GF(101), implementation='NTL')
            sage: f = x^17 + x^2 - 1
            sage: (x^2).minpoly_mod(f)
            x^17 + 100*x^2 + 2*x + 100

        TESTS:

        Random testing::

            sage: p = random_prime(2^99)
            sage: R.<x> = PolynomialRing(GF(p), implementation='NTL')
            sage: d = randrange(1,50)
            sage: f = R.random_element(d)
            sage: g = R.random_element((-1,5*d))
            sage: poly = g.minpoly_mod(f)
            sage: poly(R.quotient(f)(g))
            0"""
    @overload
    def minpoly_mod(self, f) -> Any:
        """Polynomial_dense_mod_n.minpoly_mod(self, other)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_modn_dense_ntl.pyx (starting at line 377)

        Compute the minimal polynomial of this polynomial modulo another
        polynomial in the same ring.

        ALGORITHM:

        NTL's ``MinPolyMod()``, which uses Shoup's algorithm [Sho1999]_.

        EXAMPLES::

            sage: R.<x> = PolynomialRing(GF(101), implementation='NTL')
            sage: f = x^17 + x^2 - 1
            sage: (x^2).minpoly_mod(f)
            x^17 + 100*x^2 + 2*x + 100

        TESTS:

        Random testing::

            sage: p = random_prime(2^99)
            sage: R.<x> = PolynomialRing(GF(p), implementation='NTL')
            sage: d = randrange(1,50)
            sage: f = R.random_element(d)
            sage: g = R.random_element((-1,5*d))
            sage: poly = g.minpoly_mod(f)
            sage: poly(R.quotient(f)(g))
            0"""
    @overload
    def minpoly_mod(self, f) -> Any:
        """Polynomial_dense_mod_n.minpoly_mod(self, other)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_modn_dense_ntl.pyx (starting at line 377)

        Compute the minimal polynomial of this polynomial modulo another
        polynomial in the same ring.

        ALGORITHM:

        NTL's ``MinPolyMod()``, which uses Shoup's algorithm [Sho1999]_.

        EXAMPLES::

            sage: R.<x> = PolynomialRing(GF(101), implementation='NTL')
            sage: f = x^17 + x^2 - 1
            sage: (x^2).minpoly_mod(f)
            x^17 + 100*x^2 + 2*x + 100

        TESTS:

        Random testing::

            sage: p = random_prime(2^99)
            sage: R.<x> = PolynomialRing(GF(p), implementation='NTL')
            sage: d = randrange(1,50)
            sage: f = R.random_element(d)
            sage: g = R.random_element((-1,5*d))
            sage: poly = g.minpoly_mod(f)
            sage: poly(R.quotient(f)(g))
            0"""
    def modular_composition(self, *args, **kwargs):
        """Polynomial_dense_mod_n.compose_mod(self, other, modulus)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_modn_dense_ntl.pyx (starting at line 428)

        Compute `f(g) \\pmod h`.

        To be precise about the order fo compostion, given ``self``, ``other``
        and ``modulus`` as `f(x)`, `g(x)` and `h(x)` compute `f(g(x)) \\bmod h(x)`.

        INPUT:

        - ``other`` -- a polynomial `g(x)`
        - ``modulus`` -- a polynomial `h(x)`

        EXAMPLES::

            sage: R.<x> = GF(2**127 - 1)[]
            sage: f = R.random_element()
            sage: g = R.random_element()
            sage: g.compose_mod(g, f) == g(g) % f
            True

            sage: R.<x> = GF(163)[]
            sage: f = R([i for i in range(100)])
            sage: g = R([i**2 for i in range(100)])
            sage: h = 1 + x + x**5
            sage: f.compose_mod(g, h)
            82*x^4 + 56*x^3 + 45*x^2 + 60*x + 127
            sage: f.compose_mod(g, h) == f(g) % h
            True

        AUTHORS:

        - Giacomo Pope (2024-08) initial implementation"""
    def ntl_ZZ_pX(self) -> Any:
        """Polynomial_dense_mod_n.ntl_ZZ_pX(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_modn_dense_ntl.pyx (starting at line 178)

        Return underlying NTL representation of this polynomial.  Additional
        ''bonus'' functionality is available through this function.

        .. warning::

            You must call ``ntl.set_modulus(ntl.ZZ(n))`` before doing
            arithmetic with this object!"""
    def ntl_set_directly(self, v) -> Any:
        """Polynomial_dense_mod_n.ntl_set_directly(self, v)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_modn_dense_ntl.pyx (starting at line 330)

        Set the value of this polynomial directly from a vector or string.

        Polynomials over the integers modulo n are stored internally using
        NTL's ``ZZ_pX`` class.  Use this function to set the value of this
        polynomial using the NTL constructor, which is potentially *very* fast.
        The input v is either a vector of ints or a string of the form ``[ n1
        n2 n3 ... ]`` where the ni are integers and there are no commas between
        them. The optimal input format is the string format, since that's what
        NTL uses by default.

        EXAMPLES::

            sage: R.<x> = PolynomialRing(Integers(100), implementation='NTL')
            sage: from sage.rings.polynomial.polynomial_modn_dense_ntl import Polynomial_dense_mod_n as poly_modn_dense
            sage: poly_modn_dense(R, ([1,-2,3]))
            3*x^2 + 98*x + 1
            sage: f = poly_modn_dense(R, 0)
            sage: f.ntl_set_directly([1,-2,3])
            sage: f
            3*x^2 + 98*x + 1
            sage: f.ntl_set_directly('[1 -2 3 4]')
            sage: f
            4*x^3 + 3*x^2 + 98*x + 1"""
    def quo_rem(self, right) -> Any:
        """Polynomial_dense_mod_n.quo_rem(self, right)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_modn_dense_ntl.pyx (starting at line 240)

        Return a tuple ``(quotient, remainder)`` where ``self = quotient*other +
        remainder``."""
    def shift(self, n) -> Any:
        """Polynomial_dense_mod_n.shift(self, n)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_modn_dense_ntl.pyx (starting at line 250)

        Return this polynomial multiplied by the power `x^n`. If `n` is negative,
        terms below `x^n` will be discarded. Does not change this polynomial.

        EXAMPLES::

            sage: R.<x> = PolynomialRing(Integers(12345678901234567890), implementation='NTL')
            sage: p = x^2 + 2*x + 4
            sage: p.shift(0)
             x^2 + 2*x + 4
            sage: p.shift(-1)
             x + 2
            sage: p.shift(-5)
             0
            sage: p.shift(2)
             x^4 + 2*x^3 + 4*x^2

        TESTS::

            sage: p = R(0)
            sage: p.shift(3).is_zero()
            True
            sage: p.shift(-3).is_zero()
            True

        AUTHOR:

        - David Harvey (2006-08-06)"""
    @overload
    def small_roots(self, *args, **kwds) -> Any:
        """Polynomial_dense_mod_n.small_roots(self, *args, **kwds)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_modn_dense_ntl.pyx (starting at line 412)

        See :func:`sage.rings.polynomial.polynomial_modn_dense_ntl.small_roots`
        for the documentation of this function.

        EXAMPLES::

            sage: N = 10001
            sage: K = Zmod(10001)
            sage: P.<x> = PolynomialRing(K, implementation='NTL')
            sage: f = x^3 + 10*x^2 + 5000*x - 222
            sage: f.small_roots()
            [4]"""
    @overload
    def small_roots(self) -> Any:
        """Polynomial_dense_mod_n.small_roots(self, *args, **kwds)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_modn_dense_ntl.pyx (starting at line 412)

        See :func:`sage.rings.polynomial.polynomial_modn_dense_ntl.small_roots`
        for the documentation of this function.

        EXAMPLES::

            sage: N = 10001
            sage: K = Zmod(10001)
            sage: P.<x> = PolynomialRing(K, implementation='NTL')
            sage: f = x^3 + 10*x^2 + 5000*x - 222
            sage: f.small_roots()
            [4]"""
    def __floordiv__(self, right) -> Any:
        """Polynomial_dense_mod_n.__floordiv__(self, right)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_modn_dense_ntl.pyx (starting at line 288)"""
    def __pari__(self, variable=...) -> Any:
        '''Polynomial_dense_mod_n.__pari__(self, variable=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_modn_dense_ntl.pyx (starting at line 164)

        EXAMPLES::

            sage: t = PolynomialRing(IntegerModRing(17), "t", implementation=\'NTL\').gen()
            sage: f = t^3 + 3*t - 17
            sage: pari(f)
            Mod(1, 17)*t^3 + Mod(3, 17)*t'''
    def __reduce__(self) -> Any:
        """Polynomial_dense_mod_n.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_modn_dense_ntl.pyx (starting at line 158)"""
    def __rfloordiv__(self, other):
        """Return value//self."""

class Polynomial_dense_mod_p(Polynomial_dense_mod_n):
    """File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_modn_dense_ntl.pyx (starting at line 1868)

        A dense polynomial over the integers modulo `p`, where `p` is prime.
    """
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    @overload
    def discriminant(self) -> Any:
        """Polynomial_dense_mod_p.discriminant(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_modn_dense_ntl.pyx (starting at line 2029)

        EXAMPLES::

            sage: _.<x> = PolynomialRing(GF(19), implementation='NTL')
            sage: f = x^3 + 3*x - 17
            sage: f.discriminant()
            12"""
    @overload
    def discriminant(self) -> Any:
        """Polynomial_dense_mod_p.discriminant(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_modn_dense_ntl.pyx (starting at line 2029)

        EXAMPLES::

            sage: _.<x> = PolynomialRing(GF(19), implementation='NTL')
            sage: f = x^3 + 3*x - 17
            sage: f.discriminant()
            12"""
    @overload
    def gcd(self, right) -> Any:
        '''Polynomial_dense_mod_p.gcd(self, right)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_modn_dense_ntl.pyx (starting at line 1954)

        Return the greatest common divisor of this polynomial and ``other``, as
        a monic polynomial.

        INPUT:

        - ``other`` -- a polynomial defined over the same ring as ``self``

        EXAMPLES::

            sage: R.<x> = PolynomialRing(GF(3), implementation="NTL")
            sage: f, g = x + 2, x^2 - 1
            sage: f.gcd(g)
            x + 2'''
    @overload
    def gcd(self, g) -> Any:
        '''Polynomial_dense_mod_p.gcd(self, right)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_modn_dense_ntl.pyx (starting at line 1954)

        Return the greatest common divisor of this polynomial and ``other``, as
        a monic polynomial.

        INPUT:

        - ``other`` -- a polynomial defined over the same ring as ``self``

        EXAMPLES::

            sage: R.<x> = PolynomialRing(GF(3), implementation="NTL")
            sage: f, g = x + 2, x^2 - 1
            sage: f.gcd(g)
            x + 2'''
    @overload
    def resultant(self, other) -> Any:
        """Polynomial_dense_mod_p.resultant(self, other)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_modn_dense_ntl.pyx (starting at line 2005)

        Return the resultant of ``self`` and ``other``, which must lie in the same
        polynomial ring.

        INPUT:

        - ``other`` -- a polynomial

        OUTPUT: an element of the base ring of the polynomial ring

        EXAMPLES::

            sage: R.<x> = PolynomialRing(GF(19), implementation='NTL')
            sage: f = x^3 + x + 1;  g = x^3 - x - 1
            sage: r = f.resultant(g); r
            11
            sage: r.parent() is GF(19)
            True"""
    @overload
    def resultant(self, g) -> Any:
        """Polynomial_dense_mod_p.resultant(self, other)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_modn_dense_ntl.pyx (starting at line 2005)

        Return the resultant of ``self`` and ``other``, which must lie in the same
        polynomial ring.

        INPUT:

        - ``other`` -- a polynomial

        OUTPUT: an element of the base ring of the polynomial ring

        EXAMPLES::

            sage: R.<x> = PolynomialRing(GF(19), implementation='NTL')
            sage: f = x^3 + x + 1;  g = x^3 - x - 1
            sage: r = f.resultant(g); r
            11
            sage: r.parent() is GF(19)
            True"""
    @overload
    def xgcd(self, other) -> Any:
        """Polynomial_dense_mod_p.xgcd(self, other)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_modn_dense_ntl.pyx (starting at line 1974)

        Compute the extended gcd of this element and ``other``.

        INPUT:

        - ``other`` -- an element in the same polynomial ring

        OUTPUT:

        A tuple ``(r,s,t)`` of elements in the polynomial ring such
        that ``r = s*self + t*other``.

        EXAMPLES::

            sage: R.<x> = PolynomialRing(GF(3), implementation='NTL')
            sage: x.xgcd(x)
            (x, 0, 1)
            sage: (x^2 - 1).xgcd(x - 1)
            (x + 2, 0, 1)
            sage: R.zero().xgcd(R.one())
            (1, 0, 1)
            sage: (x^3 - 1).xgcd((x - 1)^2)
            (x^2 + x + 1, 0, 1)
            sage: ((x - 1)*(x + 1)).xgcd(x*(x - 1))
            (x + 2, 1, 2)"""
    @overload
    def xgcd(self, x) -> Any:
        """Polynomial_dense_mod_p.xgcd(self, other)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_modn_dense_ntl.pyx (starting at line 1974)

        Compute the extended gcd of this element and ``other``.

        INPUT:

        - ``other`` -- an element in the same polynomial ring

        OUTPUT:

        A tuple ``(r,s,t)`` of elements in the polynomial ring such
        that ``r = s*self + t*other``.

        EXAMPLES::

            sage: R.<x> = PolynomialRing(GF(3), implementation='NTL')
            sage: x.xgcd(x)
            (x, 0, 1)
            sage: (x^2 - 1).xgcd(x - 1)
            (x + 2, 0, 1)
            sage: R.zero().xgcd(R.one())
            (1, 0, 1)
            sage: (x^3 - 1).xgcd((x - 1)^2)
            (x^2 + x + 1, 0, 1)
            sage: ((x - 1)*(x + 1)).xgcd(x*(x - 1))
            (x + 2, 1, 2)"""
    def __pow__(self, n, modulus) -> Any:
        '''Polynomial_dense_mod_p.__pow__(self, n, modulus)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_modn_dense_ntl.pyx (starting at line 1873)

        Exponentiation of ``self``.

        If ``modulus`` is not ``None``, the exponentiation is performed
        modulo the polynomial ``modulus``.

        EXAMPLES::

            sage: R.<x> = PolynomialRing(Integers(101), implementation=\'NTL\')
            sage: (x-1)^5
            x^5 + 96*x^4 + 10*x^3 + 91*x^2 + 5*x + 100
            sage: pow(x-1, 15, x^3+x+1)
            55*x^2 + 6*x + 46

        TESTS:

        Negative powers work but use the generic
        implementation of fraction fields::

            sage: R.<x> = PolynomialRing(Integers(101), implementation=\'NTL\')
            sage: f = (x-1)^(-5)
            sage: type(f)
            <class \'sage.rings.fraction_field_element.FractionFieldElement_1poly_field\'>
            sage: (f + 2).numerator()
            2*x^5 + 91*x^4 + 20*x^3 + 81*x^2 + 10*x + 100

        We define ``0^0`` to be unity, :issue:`13895`::

            sage: R.<x> = PolynomialRing(Integers(101), implementation=\'NTL\')
            sage: R(0)^0
            1

        The value returned from ``0^0`` should belong to our ring::

            sage: R.<x> = PolynomialRing(Integers(101), implementation=\'NTL\')
            sage: type(R(0)^0) == type(R(0))
            True

        The modulus can have smaller degree than ``self``::

            sage: R.<x> = PolynomialRing(GF(101), implementation="NTL")
            sage: pow(x^4 + 1, 100, x^2 + x + 1)
            100*x + 100

        Canonical coercion should apply::

            sage: R.<x> = PolynomialRing(GF(101), implementation="FLINT")
            sage: x_ZZ = ZZ["x"].gen()
            sage: pow(x+1, 100, 2)
            0
            sage: pow(x+1, 100, x_ZZ^2 + x_ZZ + 1)
            100*x + 100
            sage: pow(x+1, int(100), x_ZZ^2 + x_ZZ + 1)
            100*x + 100
            sage: xx = polygen(GF(97))
            sage: _ = pow(x + 1, 3, xx^3 + xx + 1)
            Traceback (most recent call last):
            ...
            TypeError: no common canonical parent for objects with parents: ...'''
    def __rpow__(self, other):
        """Return pow(value, self, mod)."""

class Polynomial_dense_modn_ntl_ZZ(Polynomial_dense_mod_n):
    """Polynomial_dense_modn_ntl_ZZ(parent, v=None, check=True, is_gen=False, construct=False)"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, parent, v=..., check=..., is_gen=..., construct=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_modn_dense_ntl.pyx (starting at line 1298)"""
    @overload
    def degree(self) -> Any:
        """Polynomial_dense_modn_ntl_ZZ.degree(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_modn_dense_ntl.pyx (starting at line 1777)

        EXAMPLES::

            sage: R.<x> = PolynomialRing(Integers(14^34), implementation='NTL')
            sage: f = x^4 - x - 1
            sage: f.degree()
            4
            sage: f = 14^43*x + 1
            sage: f.degree()
            0"""
    @overload
    def degree(self) -> Any:
        """Polynomial_dense_modn_ntl_ZZ.degree(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_modn_dense_ntl.pyx (starting at line 1777)

        EXAMPLES::

            sage: R.<x> = PolynomialRing(Integers(14^34), implementation='NTL')
            sage: f = x^4 - x - 1
            sage: f.degree()
            4
            sage: f = 14^43*x + 1
            sage: f.degree()
            0"""
    @overload
    def degree(self) -> Any:
        """Polynomial_dense_modn_ntl_ZZ.degree(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_modn_dense_ntl.pyx (starting at line 1777)

        EXAMPLES::

            sage: R.<x> = PolynomialRing(Integers(14^34), implementation='NTL')
            sage: f = x^4 - x - 1
            sage: f.degree()
            4
            sage: f = 14^43*x + 1
            sage: f.degree()
            0"""
    def is_gen(self) -> Any:
        """Polynomial_dense_modn_ntl_ZZ.is_gen(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_modn_dense_ntl.pyx (starting at line 1736)"""
    def list(self, boolcopy=...) -> list:
        """Polynomial_dense_modn_ntl_ZZ.list(self, bool copy=True) -> list

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_modn_dense_ntl.pyx (starting at line 1322)"""
    def quo_rem(self, right) -> Any:
        """Polynomial_dense_modn_ntl_ZZ.quo_rem(self, right)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_modn_dense_ntl.pyx (starting at line 1532)

        Return `q` and `r`, with the degree of `r` less than the degree of ``right``,
        such that `q \\cdot` ``right`` `+ r =` ``self``.

        EXAMPLES::

            sage: R.<x> = PolynomialRing(Integers(10^30), implementation='NTL')
            sage: f = x^5+1; g = (x+1)^2
            sage: q, r = f.quo_rem(g)
            sage: q
            x^3 + 999999999999999999999999999998*x^2 + 3*x + 999999999999999999999999999996
            sage: r
            5*x + 5
            sage: q*g + r
            x^5 + 1"""
    @overload
    def reverse(self, degree=...) -> Any:
        """Polynomial_dense_modn_ntl_ZZ.reverse(self, degree=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_modn_dense_ntl.pyx (starting at line 1694)

        Return the reverse of the input polynomial thought as a polynomial of
        degree ``degree``.

        If `f` is a degree-`d` polynomial, its reverse is `x^d f(1/x)`.

        INPUT:

        - ``degree`` -- ``None`` or integer; if specified, truncate or zero
          pad the list of coefficients to this degree before reversing it

        EXAMPLES::

            sage: R.<x> = PolynomialRing(Integers(12^29), implementation='NTL')
            sage: f = x^4 + 2*x + 5
            sage: f.reverse()
            5*x^4 + 2*x^3 + 1
            sage: f = x^3 + x
            sage: f.reverse()
            x^2 + 1
            sage: f.reverse(1)
            1
            sage: f.reverse(5)
            x^4 + x^2

        TESTS:

        We check that this implementation is compatible with the generic one::

            sage: all(f.reverse(d) == Polynomial.reverse(f, d)
            ....:     for d in [None, 0, 1, 2, 3, 4, 5])
            True"""
    @overload
    def reverse(self) -> Any:
        """Polynomial_dense_modn_ntl_ZZ.reverse(self, degree=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_modn_dense_ntl.pyx (starting at line 1694)

        Return the reverse of the input polynomial thought as a polynomial of
        degree ``degree``.

        If `f` is a degree-`d` polynomial, its reverse is `x^d f(1/x)`.

        INPUT:

        - ``degree`` -- ``None`` or integer; if specified, truncate or zero
          pad the list of coefficients to this degree before reversing it

        EXAMPLES::

            sage: R.<x> = PolynomialRing(Integers(12^29), implementation='NTL')
            sage: f = x^4 + 2*x + 5
            sage: f.reverse()
            5*x^4 + 2*x^3 + 1
            sage: f = x^3 + x
            sage: f.reverse()
            x^2 + 1
            sage: f.reverse(1)
            1
            sage: f.reverse(5)
            x^4 + x^2

        TESTS:

        We check that this implementation is compatible with the generic one::

            sage: all(f.reverse(d) == Polynomial.reverse(f, d)
            ....:     for d in [None, 0, 1, 2, 3, 4, 5])
            True"""
    @overload
    def reverse(self) -> Any:
        """Polynomial_dense_modn_ntl_ZZ.reverse(self, degree=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_modn_dense_ntl.pyx (starting at line 1694)

        Return the reverse of the input polynomial thought as a polynomial of
        degree ``degree``.

        If `f` is a degree-`d` polynomial, its reverse is `x^d f(1/x)`.

        INPUT:

        - ``degree`` -- ``None`` or integer; if specified, truncate or zero
          pad the list of coefficients to this degree before reversing it

        EXAMPLES::

            sage: R.<x> = PolynomialRing(Integers(12^29), implementation='NTL')
            sage: f = x^4 + 2*x + 5
            sage: f.reverse()
            5*x^4 + 2*x^3 + 1
            sage: f = x^3 + x
            sage: f.reverse()
            x^2 + 1
            sage: f.reverse(1)
            1
            sage: f.reverse(5)
            x^4 + x^2

        TESTS:

        We check that this implementation is compatible with the generic one::

            sage: all(f.reverse(d) == Polynomial.reverse(f, d)
            ....:     for d in [None, 0, 1, 2, 3, 4, 5])
            True"""
    def shift(self, n) -> Any:
        """Polynomial_dense_modn_ntl_ZZ.shift(self, n)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_modn_dense_ntl.pyx (starting at line 1603)

        Shift ``self`` to left by `n`, which is multiplication by `x^n`,
        truncating if `n` is negative.

        EXAMPLES::

            sage: R.<x> = PolynomialRing(Integers(12^30), implementation='NTL')
            sage: f = x^7 + x + 1
            sage: f.shift(1)
            x^8 + x^2 + x
            sage: f.shift(-1)
            x^6 + 1
            sage: f.shift(10).shift(-10) == f
            True

        TESTS::

            sage: p = R(0)
            sage: p.shift(3).is_zero()
            True
            sage: p.shift(-3).is_zero()
            True"""
    def truncate(self, longn) -> Polynomial:
        """Polynomial_dense_modn_ntl_ZZ.truncate(self, long n) -> Polynomial

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_modn_dense_ntl.pyx (starting at line 1791)

        Return this polynomial mod `x^n`.

        EXAMPLES::

            sage: R.<x> = PolynomialRing(Integers(15^30), implementation='NTL')
            sage: f = sum(x^n for n in range(10)); f
            x^9 + x^8 + x^7 + x^6 + x^5 + x^4 + x^3 + x^2 + x + 1
            sage: f.truncate(6)
            x^5 + x^4 + x^3 + x^2 + x + 1"""
    @overload
    def valuation(self) -> Any:
        """Polynomial_dense_modn_ntl_ZZ.valuation(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_modn_dense_ntl.pyx (starting at line 1739)

        Return the valuation of ``self``, that is, the power of the
        lowest nonzero monomial of ``self``.

        EXAMPLES::

            sage: R.<x> = PolynomialRing(Integers(10^50), implementation='NTL')
            sage: x.valuation()
            1
            sage: f = x - 3; f.valuation()
            0
            sage: f = x^99; f.valuation()
            99
            sage: f = x - x; f.valuation()
            +Infinity"""
    @overload
    def valuation(self) -> Any:
        """Polynomial_dense_modn_ntl_ZZ.valuation(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_modn_dense_ntl.pyx (starting at line 1739)

        Return the valuation of ``self``, that is, the power of the
        lowest nonzero monomial of ``self``.

        EXAMPLES::

            sage: R.<x> = PolynomialRing(Integers(10^50), implementation='NTL')
            sage: x.valuation()
            1
            sage: f = x - 3; f.valuation()
            0
            sage: f = x^99; f.valuation()
            99
            sage: f = x - x; f.valuation()
            +Infinity"""
    @overload
    def valuation(self) -> Any:
        """Polynomial_dense_modn_ntl_ZZ.valuation(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_modn_dense_ntl.pyx (starting at line 1739)

        Return the valuation of ``self``, that is, the power of the
        lowest nonzero monomial of ``self``.

        EXAMPLES::

            sage: R.<x> = PolynomialRing(Integers(10^50), implementation='NTL')
            sage: x.valuation()
            1
            sage: f = x - 3; f.valuation()
            0
            sage: f = x^99; f.valuation()
            99
            sage: f = x - x; f.valuation()
            +Infinity"""
    @overload
    def valuation(self) -> Any:
        """Polynomial_dense_modn_ntl_ZZ.valuation(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_modn_dense_ntl.pyx (starting at line 1739)

        Return the valuation of ``self``, that is, the power of the
        lowest nonzero monomial of ``self``.

        EXAMPLES::

            sage: R.<x> = PolynomialRing(Integers(10^50), implementation='NTL')
            sage: x.valuation()
            1
            sage: f = x - 3; f.valuation()
            0
            sage: f = x^99; f.valuation()
            99
            sage: f = x - x; f.valuation()
            +Infinity"""
    @overload
    def valuation(self) -> Any:
        """Polynomial_dense_modn_ntl_ZZ.valuation(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_modn_dense_ntl.pyx (starting at line 1739)

        Return the valuation of ``self``, that is, the power of the
        lowest nonzero monomial of ``self``.

        EXAMPLES::

            sage: R.<x> = PolynomialRing(Integers(10^50), implementation='NTL')
            sage: x.valuation()
            1
            sage: f = x - 3; f.valuation()
            0
            sage: f = x^99; f.valuation()
            99
            sage: f = x - x; f.valuation()
            +Infinity"""
    def __bool__(self) -> bool:
        """True if self else False"""
    def __call__(self, *args, **kwds) -> Any:
        """Polynomial_dense_modn_ntl_ZZ.__call__(self, *args, **kwds)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_modn_dense_ntl.pyx (starting at line 1807)

        Evaluate ``self`` at ``x``. If ``x`` is a single argument coercible into
        the base ring of ``self``, this is done directly in NTL, otherwise
        the generic Polynomial call code is used.

        EXAMPLES::

            sage: R.<x> = PolynomialRing(Integers(10^30), implementation='NTL')
            sage: f = x^3 + 7
            sage: f(5)
            132
            sage: f(5r)
            132
            sage: f(mod(5, 10^50))
            132
            sage: f(x)
            x^3 + 7
            sage: S.<y> = PolynomialRing(Integers(5), implementation='NTL')
            sage: f(y)
            y^3 + 2

        TESTS::

            sage: R.<x> = PolynomialRing(Integers(10^30), implementation='NTL')
            sage: f = x^3 + 7
            sage: f(1).parent() == R.base_ring()
            True
            sage: f(int(1)).parent() == R.base_ring()
            True
            sage: f(x + 1).parent() == f.parent()
            True

            sage: R.<x> = PolynomialRing(Zmod(10^30), 'x', implementation='NTL')
            sage: u = Zmod(10^29)(3)
            sage: x(u).parent() == u.parent()
            True
            sage: v = Zmod(10)(3)
            sage: x(v).parent() == v.parent()
            True"""
    def __lshift__(self, Polynomial_dense_modn_ntl_ZZself, longn) -> Any:
        """Polynomial_dense_modn_ntl_ZZ.__lshift__(Polynomial_dense_modn_ntl_ZZ self, long n)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_modn_dense_ntl.pyx (starting at line 1629)

        TESTS::

            sage: R.<x> = PolynomialRing(Integers(14^30), implementation='NTL')
            sage: f = x^5 + 2*x + 1
            sage: f << 3
            x^8 + 2*x^4 + x^3"""
    def __pow__(self, Polynomial_dense_modn_ntl_ZZself, ee, modulus) -> Any:
        """Polynomial_dense_modn_ntl_ZZ.__pow__(Polynomial_dense_modn_ntl_ZZ self, ee, modulus)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_modn_dense_ntl.pyx (starting at line 1476)

        TESTS::

            sage: R.<x> = PolynomialRing(Integers(10^30), implementation='NTL')
            sage: (x+1)^5
            x^5 + 5*x^4 + 10*x^3 + 10*x^2 + 5*x + 1

        We define ``0^0`` to be unity, :issue:`13895`::

            sage: R.<x> = PolynomialRing(Integers(10^30), implementation='NTL')
            sage: R(0)^0
            1

        The value returned from ``0^0`` should belong to our ring::

            sage: R.<x> = PolynomialRing(Integers(10^30), implementation='NTL')
            sage: type(R(0)^0) == type(R(0))
            True"""
    def __rlshift__(self, other):
        """Return value<<self."""
    def __rpow__(self, other):
        """Return pow(value, self, mod)."""
    def __rrshift__(self, other):
        """Return value>>self."""
    def __rshift__(self, Polynomial_dense_modn_ntl_ZZself, longn) -> Any:
        """Polynomial_dense_modn_ntl_ZZ.__rshift__(Polynomial_dense_modn_ntl_ZZ self, long n)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_modn_dense_ntl.pyx (starting at line 1642)

        TESTS::

            sage: R.<x> = PolynomialRing(Integers(15^30), implementation='NTL')
            sage: f = x^5 + 2*x + 1
            sage: f >> 3
            x^2"""

class Polynomial_dense_modn_ntl_zz(Polynomial_dense_mod_n):
    """Polynomial_dense_modn_ntl_zz(parent, v=None, check=True, is_gen=False, construct=False)

    File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_modn_dense_ntl.pyx (starting at line 671)

    Polynomial on `\\ZZ/n\\ZZ` implemented via NTL.

    .. automethod:: _add_
    .. automethod:: _sub_
    .. automethod:: _lmul_
    .. automethod:: _rmul_
    .. automethod:: _mul_
    .. automethod:: _mul_trunc_"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, parent, v=..., check=..., is_gen=..., construct=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_modn_dense_ntl.pyx (starting at line 682)

                EXAMPLES::

                    sage: R = Integers(5**21)
                    sage: S.<x> = PolynomialRing(R, implementation='NTL')
                    sage: S(1/4)
                    357627868652344
        """
    @overload
    def degree(self) -> Any:
        """Polynomial_dense_modn_ntl_zz.degree(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_modn_dense_ntl.pyx (starting at line 1206)

        EXAMPLES::

            sage: R.<x> = PolynomialRing(Integers(77), implementation='NTL')
            sage: f = x^4 - x - 1
            sage: f.degree()
            4
            sage: f = 77*x + 1
            sage: f.degree()
            0"""
    @overload
    def degree(self) -> Any:
        """Polynomial_dense_modn_ntl_zz.degree(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_modn_dense_ntl.pyx (starting at line 1206)

        EXAMPLES::

            sage: R.<x> = PolynomialRing(Integers(77), implementation='NTL')
            sage: f = x^4 - x - 1
            sage: f.degree()
            4
            sage: f = 77*x + 1
            sage: f.degree()
            0"""
    @overload
    def degree(self) -> Any:
        """Polynomial_dense_modn_ntl_zz.degree(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_modn_dense_ntl.pyx (starting at line 1206)

        EXAMPLES::

            sage: R.<x> = PolynomialRing(Integers(77), implementation='NTL')
            sage: f = x^4 - x - 1
            sage: f.degree()
            4
            sage: f = 77*x + 1
            sage: f.degree()
            0"""
    @overload
    def int_list(self) -> Any:
        """Polynomial_dense_modn_ntl_zz.int_list(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_modn_dense_ntl.pyx (starting at line 725)

        Return the coefficients of ``self`` as efficiently as possible as a
        list of python ints.

        EXAMPLES::

            sage: R.<x> = PolynomialRing(Integers(100), implementation='NTL')
            sage: from sage.rings.polynomial.polynomial_modn_dense_ntl import Polynomial_dense_mod_n as poly_modn_dense
            sage: f = poly_modn_dense(R,[5,0,0,1])
            sage: f.int_list()
            [5, 0, 0, 1]
            sage: [type(a) for a in f.int_list()]
            [<... 'int'>, <... 'int'>, <... 'int'>, <... 'int'>]"""
    @overload
    def int_list(self) -> Any:
        """Polynomial_dense_modn_ntl_zz.int_list(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_modn_dense_ntl.pyx (starting at line 725)

        Return the coefficients of ``self`` as efficiently as possible as a
        list of python ints.

        EXAMPLES::

            sage: R.<x> = PolynomialRing(Integers(100), implementation='NTL')
            sage: from sage.rings.polynomial.polynomial_modn_dense_ntl import Polynomial_dense_mod_n as poly_modn_dense
            sage: f = poly_modn_dense(R,[5,0,0,1])
            sage: f.int_list()
            [5, 0, 0, 1]
            sage: [type(a) for a in f.int_list()]
            [<... 'int'>, <... 'int'>, <... 'int'>, <... 'int'>]"""
    @overload
    def int_list(self) -> Any:
        """Polynomial_dense_modn_ntl_zz.int_list(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_modn_dense_ntl.pyx (starting at line 725)

        Return the coefficients of ``self`` as efficiently as possible as a
        list of python ints.

        EXAMPLES::

            sage: R.<x> = PolynomialRing(Integers(100), implementation='NTL')
            sage: from sage.rings.polynomial.polynomial_modn_dense_ntl import Polynomial_dense_mod_n as poly_modn_dense
            sage: f = poly_modn_dense(R,[5,0,0,1])
            sage: f.int_list()
            [5, 0, 0, 1]
            sage: [type(a) for a in f.int_list()]
            [<... 'int'>, <... 'int'>, <... 'int'>, <... 'int'>]"""
    def is_gen(self) -> Any:
        """Polynomial_dense_modn_ntl_zz.is_gen(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_modn_dense_ntl.pyx (starting at line 1167)"""
    def ntl_set_directly(self, v) -> Any:
        """Polynomial_dense_modn_ntl_zz.ntl_set_directly(self, v)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_modn_dense_ntl.pyx (starting at line 709)"""
    def quo_rem(self, right) -> Any:
        """Polynomial_dense_modn_ntl_zz.quo_rem(self, right)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_modn_dense_ntl.pyx (starting at line 963)

        Return `q` and `r`, with the degree of `r` less than the degree of ``right``,
        such that `q \\cdot` ``right`` `{}+ r =` ``self``.

        EXAMPLES::

            sage: R.<x> = PolynomialRing(Integers(125), implementation='NTL')
            sage: f = x^5+1; g = (x+1)^2
            sage: q, r = f.quo_rem(g)
            sage: q
            x^3 + 123*x^2 + 3*x + 121
            sage: r
            5*x + 5
            sage: q*g + r
            x^5 + 1"""
    @overload
    def reverse(self, degree=...) -> Any:
        """Polynomial_dense_modn_ntl_zz.reverse(self, degree=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_modn_dense_ntl.pyx (starting at line 1125)

        Return the reverse of the input polynomial thought as a polynomial of
        degree ``degree``.

        If `f` is a degree-`d` polynomial, its reverse is `x^d f(1/x)`.

        INPUT:

        - ``degree`` -- ``None`` or integer; if specified, truncate or zero
          pad the list of coefficients to this degree before reversing it

        EXAMPLES::

            sage: R.<x> = PolynomialRing(Integers(77), implementation='NTL')
            sage: f = x^4 - x - 1
            sage: f.reverse()
            76*x^4 + 76*x^3 + 1
            sage: f.reverse(2)
            76*x^2 + 76*x
            sage: f.reverse(5)
            76*x^5 + 76*x^4 + x
            sage: g = x^3 - x
            sage: g.reverse()
            76*x^2 + 1

        TESTS:

        We check that this implementation is compatible with the generic one::

            sage: all(f.reverse(d) == Polynomial.reverse(f, d)
            ....:     for d in [None, 0, 1, 2, 3, 4, 5])
            True"""
    @overload
    def reverse(self) -> Any:
        """Polynomial_dense_modn_ntl_zz.reverse(self, degree=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_modn_dense_ntl.pyx (starting at line 1125)

        Return the reverse of the input polynomial thought as a polynomial of
        degree ``degree``.

        If `f` is a degree-`d` polynomial, its reverse is `x^d f(1/x)`.

        INPUT:

        - ``degree`` -- ``None`` or integer; if specified, truncate or zero
          pad the list of coefficients to this degree before reversing it

        EXAMPLES::

            sage: R.<x> = PolynomialRing(Integers(77), implementation='NTL')
            sage: f = x^4 - x - 1
            sage: f.reverse()
            76*x^4 + 76*x^3 + 1
            sage: f.reverse(2)
            76*x^2 + 76*x
            sage: f.reverse(5)
            76*x^5 + 76*x^4 + x
            sage: g = x^3 - x
            sage: g.reverse()
            76*x^2 + 1

        TESTS:

        We check that this implementation is compatible with the generic one::

            sage: all(f.reverse(d) == Polynomial.reverse(f, d)
            ....:     for d in [None, 0, 1, 2, 3, 4, 5])
            True"""
    @overload
    def reverse(self) -> Any:
        """Polynomial_dense_modn_ntl_zz.reverse(self, degree=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_modn_dense_ntl.pyx (starting at line 1125)

        Return the reverse of the input polynomial thought as a polynomial of
        degree ``degree``.

        If `f` is a degree-`d` polynomial, its reverse is `x^d f(1/x)`.

        INPUT:

        - ``degree`` -- ``None`` or integer; if specified, truncate or zero
          pad the list of coefficients to this degree before reversing it

        EXAMPLES::

            sage: R.<x> = PolynomialRing(Integers(77), implementation='NTL')
            sage: f = x^4 - x - 1
            sage: f.reverse()
            76*x^4 + 76*x^3 + 1
            sage: f.reverse(2)
            76*x^2 + 76*x
            sage: f.reverse(5)
            76*x^5 + 76*x^4 + x
            sage: g = x^3 - x
            sage: g.reverse()
            76*x^2 + 1

        TESTS:

        We check that this implementation is compatible with the generic one::

            sage: all(f.reverse(d) == Polynomial.reverse(f, d)
            ....:     for d in [None, 0, 1, 2, 3, 4, 5])
            True"""
    def shift(self, n) -> Any:
        """Polynomial_dense_modn_ntl_zz.shift(self, n)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_modn_dense_ntl.pyx (starting at line 1034)

        Shift ``self`` to left by `n`, which is multiplication by `x^n`,
        truncating if `n` is negative.

        EXAMPLES::

            sage: R.<x> = PolynomialRing(Integers(77), implementation='NTL')
            sage: f = x^7 + x + 1
            sage: f.shift(1)
            x^8 + x^2 + x
            sage: f.shift(-1)
            x^6 + 1
            sage: f.shift(10).shift(-10) == f
            True

        TESTS::

            sage: p = R(0)
            sage: p.shift(3).is_zero()
            True
            sage: p.shift(-3).is_zero()
            True"""
    def truncate(self, longn) -> Polynomial:
        """Polynomial_dense_modn_ntl_zz.truncate(self, long n) -> Polynomial

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_modn_dense_ntl.pyx (starting at line 1220)

        Return this polynomial mod `x^n`.

        EXAMPLES::

            sage: R.<x> = PolynomialRing(Integers(77), implementation='NTL')
            sage: f = sum(x^n for n in range(10)); f
            x^9 + x^8 + x^7 + x^6 + x^5 + x^4 + x^3 + x^2 + x + 1
            sage: f.truncate(6)
            x^5 + x^4 + x^3 + x^2 + x + 1"""
    @overload
    def valuation(self) -> Any:
        """Polynomial_dense_modn_ntl_zz.valuation(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_modn_dense_ntl.pyx (starting at line 1183)

        Return the valuation of ``self``, that is, the power of the
        lowest nonzero monomial of ``self``.

        EXAMPLES::

            sage: R.<x> = PolynomialRing(Integers(10), implementation='NTL')
            sage: x.valuation()
            1
            sage: f = x-3; f.valuation()
            0
            sage: f = x^99; f.valuation()
            99
            sage: f = x-x; f.valuation()
            +Infinity"""
    @overload
    def valuation(self) -> Any:
        """Polynomial_dense_modn_ntl_zz.valuation(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_modn_dense_ntl.pyx (starting at line 1183)

        Return the valuation of ``self``, that is, the power of the
        lowest nonzero monomial of ``self``.

        EXAMPLES::

            sage: R.<x> = PolynomialRing(Integers(10), implementation='NTL')
            sage: x.valuation()
            1
            sage: f = x-3; f.valuation()
            0
            sage: f = x^99; f.valuation()
            99
            sage: f = x-x; f.valuation()
            +Infinity"""
    @overload
    def valuation(self) -> Any:
        """Polynomial_dense_modn_ntl_zz.valuation(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_modn_dense_ntl.pyx (starting at line 1183)

        Return the valuation of ``self``, that is, the power of the
        lowest nonzero monomial of ``self``.

        EXAMPLES::

            sage: R.<x> = PolynomialRing(Integers(10), implementation='NTL')
            sage: x.valuation()
            1
            sage: f = x-3; f.valuation()
            0
            sage: f = x^99; f.valuation()
            99
            sage: f = x-x; f.valuation()
            +Infinity"""
    @overload
    def valuation(self) -> Any:
        """Polynomial_dense_modn_ntl_zz.valuation(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_modn_dense_ntl.pyx (starting at line 1183)

        Return the valuation of ``self``, that is, the power of the
        lowest nonzero monomial of ``self``.

        EXAMPLES::

            sage: R.<x> = PolynomialRing(Integers(10), implementation='NTL')
            sage: x.valuation()
            1
            sage: f = x-3; f.valuation()
            0
            sage: f = x^99; f.valuation()
            99
            sage: f = x-x; f.valuation()
            +Infinity"""
    @overload
    def valuation(self) -> Any:
        """Polynomial_dense_modn_ntl_zz.valuation(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_modn_dense_ntl.pyx (starting at line 1183)

        Return the valuation of ``self``, that is, the power of the
        lowest nonzero monomial of ``self``.

        EXAMPLES::

            sage: R.<x> = PolynomialRing(Integers(10), implementation='NTL')
            sage: x.valuation()
            1
            sage: f = x-3; f.valuation()
            0
            sage: f = x^99; f.valuation()
            99
            sage: f = x-x; f.valuation()
            +Infinity"""
    def __bool__(self) -> bool:
        """True if self else False"""
    def __call__(self, *args, **kwds) -> Any:
        """Polynomial_dense_modn_ntl_zz.__call__(self, *args, **kwds)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_modn_dense_ntl.pyx (starting at line 1236)

        Evaluate ``self`` at ``x``. If ``x`` is a single argument coercible into
        the base ring of ``self``, this is done directly in NTL, otherwise
        the generic Polynomial call code is used.

        EXAMPLES::

            sage: R.<x> = PolynomialRing(Integers(100), implementation='NTL')
            sage: f = x^3 + 7
            sage: f(5)
            32
            sage: f(5r)
            32
            sage: f(mod(5, 1000))
            32
            sage: f(x)
            x^3 + 7
            sage: S.<y> = PolynomialRing(Integers(5), implementation='NTL')
            sage: f(y)
            y^3 + 2

        TESTS::

            sage: R.<x> = PolynomialRing(Integers(100), implementation='NTL')
            sage: f = x^3 + 7
            sage: f(1).parent() == R.base_ring()
            True
            sage: f(int(1)).parent() == R.base_ring()
            True
            sage: f(x + 1).parent() == f.parent()
            True

            sage: R.<x> = PolynomialRing(Zmod(12), 'x', implementation='NTL')
            sage: u = Zmod(4)(3)
            sage: x(u).parent() == u.parent()
            True"""
    def __lshift__(self, Polynomial_dense_modn_ntl_zzself, longn) -> Any:
        """Polynomial_dense_modn_ntl_zz.__lshift__(Polynomial_dense_modn_ntl_zz self, long n)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_modn_dense_ntl.pyx (starting at line 1060)

        TESTS::

            sage: R.<x> = PolynomialRing(Integers(77), implementation='NTL')
            sage: f = x^5 + 2*x + 1
            sage: f << 3
            x^8 + 2*x^4 + x^3"""
    def __pow__(self, Polynomial_dense_modn_ntl_zzself, ee, modulus) -> Any:
        """Polynomial_dense_modn_ntl_zz.__pow__(Polynomial_dense_modn_ntl_zz self, ee, modulus)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_modn_dense_ntl.pyx (starting at line 889)

        TESTS::

            sage: R.<x> = PolynomialRing(Integers(100), implementation='NTL')
            sage: (x-1)^5
            x^5 + 95*x^4 + 10*x^3 + 90*x^2 + 5*x + 99

        We define ``0^0`` to be unity, :issue:`13895`::

            sage: R.<x> = PolynomialRing(Integers(100), implementation='NTL')
            sage: R(0)^0
            1

        The value returned from ``0^0`` should belong to our ring::

            sage: R.<x> = PolynomialRing(Integers(100), implementation='NTL')
            sage: type(R(0)^0) == type(R(0))
            True

        Negative powers work (over prime fields) but use the generic
        implementation of fraction fields::

            sage: R.<x> = PolynomialRing(Integers(101), implementation='NTL')
            sage: f = (x-1)^(-5)
            sage: type(f)
            <class 'sage.rings.fraction_field_element.FractionFieldElement_1poly_field'>
            sage: (f + 2).numerator()
            2*x^5 + 91*x^4 + 20*x^3 + 81*x^2 + 10*x + 100

            sage: R.<x> = PolynomialRing(Integers(100), implementation='NTL')
            sage: (x-1)^(-5)
            Traceback (most recent call last):
            ...
            TypeError: ..."""
    def __rlshift__(self, other):
        """Return value<<self."""
    def __rpow__(self, other):
        """Return pow(value, self, mod)."""
    def __rrshift__(self, other):
        """Return value>>self."""
    def __rshift__(self, Polynomial_dense_modn_ntl_zzself, longn) -> Any:
        """Polynomial_dense_modn_ntl_zz.__rshift__(Polynomial_dense_modn_ntl_zz self, long n)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_modn_dense_ntl.pyx (starting at line 1073)

        TESTS::

            sage: R.<x> = PolynomialRing(Integers(77), implementation='NTL')
            sage: f = x^5 + 2*x + 1
            sage: f >> 3
            x^2"""
