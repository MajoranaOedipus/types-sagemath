import sage.categories.map
import sage.categories.morphism
import sage.structure.element
from sage.categories.homset import Hom as Hom
from sage.rings.infinity import infinity as infinity
from sage.structure.element import coerce_binop as coerce_binop, have_same_parent as have_same_parent, parent as parent
from typing import Any, ClassVar, overload

__pyx_capi__: dict

class ConstantOrePolynomialSection(sage.categories.map.Map):
    """File: /build/sagemath/src/sage/src/sage/rings/polynomial/ore_polynomial_element.pyx (starting at line 2968)

        Representation of the canonical homomorphism from the constants of an Ore
        polynomial ring to the base ring.

        This class is necessary for automatic coercion from zero-degree Ore
        polynomial ring into the base ring.

        EXAMPLES::

            sage: from sage.rings.polynomial.ore_polynomial_element import ConstantOrePolynomialSection
            sage: R.<t> = QQ[]
            sage: sigma = R.hom([t+1])
            sage: S.<x> = R['x',sigma]
            sage: m = ConstantOrePolynomialSection(S, R); m
            Generic map:
                From: Ore Polynomial Ring in x over Univariate Polynomial Ring in t
                      over Rational Field twisted by t |--> t + 1
                To:   Univariate Polynomial Ring in t over Rational Field
    """
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, S, R) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

class OrePolynomial(sage.structure.element.AlgebraElement):
    """OrePolynomial(parent, construct=False)

    File: /build/sagemath/src/sage/src/sage/rings/polynomial/ore_polynomial_element.pyx (starting at line 50)

    Abstract base class for Ore polynomials.

    This class must be inherited from and have key methods overridden.

    .. RUBRIC:: Definition

    Let `R` be a commutative ring equipped with an automorphism `\\sigma`
    and a `\\sigma`-derivation `\\partial`.

    An Ore polynomial is given by the equation:

    .. MATH::

        F(X) = a_{n} X^{n} + \\cdots + a_0,

    where the coefficients `a_i \\in R` and `X` is a formal variable.

    Addition between two Ore polynomials is defined by the usual addition
    operation and the modified multiplication is defined by the rule
    `X a = \\sigma(a) X + \\partial(a)` for all `a` in `R`.
    Ore polynomials are thus non-commutative and the degree of a product
    is equal to the sum of the degrees of the factors.

    Let `a` and `b` be two Ore polynomials in the same ring `S`.
    The *right (resp. left) Euclidean division* of `a` by `b` is a couple
    `(q,r)` of elements in `S` such that

    - `a = q b + r` (resp. `a = b q + r`)

    - the degree of `r` is less than the degree of `b`

    `q` (resp. `r`) is called the *quotient* (resp. the remainder)
    of this Euclidean division.

    .. RUBRIC:: Properties

    Keeping the previous notation, if the leading coefficient of `b`
    is a unit (e.g. if `b` is monic) then the quotient and the remainder
    in the *right* Euclidean division exist and are unique.

    The same result holds for the *left* Euclidean division if in addition
    the twisting morphism defining the Ore polynomial ring is invertible.

    EXAMPLES:

    We illustrate some functionalities implemented in this class.

    We create the Ore polynomial ring (here the derivation is zero)::

        sage: R.<t> = ZZ[]
        sage: sigma = R.hom([t+1])
        sage: S.<x> = R['x',sigma]; S
        Ore Polynomial Ring in x over Univariate Polynomial Ring in t over Integer Ring
         twisted by t |--> t + 1

    and some elements in it::

        sage: a = t + x + 1; a
        x + t + 1
        sage: b = S([t^2,t+1,1]); b
        x^2 + (t + 1)*x + t^2
        sage: c = S.random_element(degree=3,monic=True)
        sage: c.parent() is S
        True

    Ring operations are supported::

        sage: a + b
        x^2 + (t + 2)*x + t^2 + t + 1
        sage: a - b
        -x^2 - t*x - t^2 + t + 1

        sage: a * b
        x^3 + (2*t + 3)*x^2 + (2*t^2 + 4*t + 2)*x + t^3 + t^2
        sage: b * a
        x^3 + (2*t + 4)*x^2 + (2*t^2 + 3*t + 2)*x + t^3 + t^2
        sage: a * b == b * a
        False

        sage: b^2
        x^4 + (2*t + 4)*x^3 + (3*t^2 + 7*t + 6)*x^2
         + (2*t^3 + 4*t^2 + 3*t + 1)*x + t^4
        sage: b^2 == b*b
        True

    Sage also implements arithmetic over Ore polynomial rings. You will find
    below a short panorama::

        sage: q,r = c.right_quo_rem(b)
        sage: c == q*b + r
        True

    The operators ``//`` and ``%`` give respectively the quotient
    and the remainder of the *right* Euclidean division::

        sage: q == c // b
        True
        sage: r == c % b
        True

    Here we can see the effect of the operator evaluation compared to the usual
    polynomial evaluation::

        sage: a = x^2
        sage: a(t)
        doctest:...: FutureWarning: This class/method/function is marked as experimental.
        It, its functionality or its interface might change without a formal deprecation.
        See https://github.com/sagemath/sage/issues/13215 for details.
        t + 2

    Here is another example over a finite field::

        sage: # needs sage.rings.finite_rings
        sage: k.<t> = GF(5^3)
        sage: Frob = k.frobenius_endomorphism()
        sage: S.<x> = k['x',Frob]
        sage: a = x^4 + (4*t + 1)*x^3 + (t^2 + 3*t + 3)*x^2 + (3*t^2 + 2*t + 2)*x + (3*t^2 + 3*t + 1)
        sage: b = (2*t^2 + 3)*x^2 + (3*t^2 + 1)*x + 4*t + 2
        sage: q, r = a.left_quo_rem(b)
        sage: q
        (4*t^2 + t + 1)*x^2 + (2*t^2 + 2*t + 2)*x + 2*t^2 + 4*t + 3
        sage: r
        (t + 2)*x + 3*t^2 + 2*t + 4
        sage: a == b*q + r
        True

    Once we have Euclidean divisions, we have for free gcd and lcm
    (at least if the base ring is a field)::

        sage: # needs sage.rings.finite_rings
        sage: a = (x + t) * (x + t^2)^2
        sage: b = (x + t) * (t*x + t + 1) * (x + t^2)
        sage: a.right_gcd(b)
        x + t^2
        sage: a.left_gcd(b)
        x + t

    The left lcm has the following meaning: given Ore polynomials `a` and `b`,
    their left lcm is the least degree polynomial `c = ua = vb` for some Ore
    polynomials `u, v`. Such a `c` always exist if the base ring is a field::

        sage: c = a.left_lcm(b); c                                                      # needs sage.rings.finite_rings
        x^5 + (4*t^2 + t + 3)*x^4 + (3*t^2 + 4*t)*x^3 + 2*t^2*x^2 + (2*t^2 + t)*x + 4*t^2 + 4
        sage: c.is_right_divisible_by(a)                                                # needs sage.rings.finite_rings
        True
        sage: c.is_right_divisible_by(b)                                                # needs sage.rings.finite_rings
        True

    The right lcm is defined similarly as the least degree polynomial `c = au =
    bv` for some `u,v`::

        sage: d = a.right_lcm(b); d                                                     # needs sage.rings.finite_rings
        x^5 + (t^2 + 1)*x^4 + (3*t^2 + 3*t + 3)*x^3 + (3*t^2 + t + 2)*x^2 + (4*t^2 + 3*t)*x + 4*t + 4
        sage: d.is_left_divisible_by(a)                                                 # needs sage.rings.finite_rings
        True
        sage: d.is_left_divisible_by(b)                                                 # needs sage.rings.finite_rings
        True

    .. SEEALSO::

        - :mod:`sage.rings.polynomial.ore_polynomial_ring`"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, parent, construct=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/polynomial/ore_polynomial_element.pyx (starting at line 214)

                Initialize ``self``.

                INPUT:

                - ``parent`` -- parent of ``self``

                - ``construct`` -- boolean (default: ``False``)

                TESTS::

                    sage: R.<t> = ZZ[]
                    sage: sigma = R.hom([t+1])
                    sage: S.<x> = R['x',sigma]
                    sage: P = x + t
                    sage: TestSuite(P).run()
                    sage: Q = S([1, t, t+2])
                    sage: TestSuite(Q).run()
        """
    @overload
    def base_ring(self) -> Any:
        """OrePolynomial.base_ring(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/ore_polynomial_element.pyx (starting at line 1758)

        Return the base ring of ``self``.

        EXAMPLES::

            sage: R.<t> = ZZ[]
            sage: sigma = R.hom([t+1])
            sage: S.<x> = R['x',sigma]
            sage: a = S.random_element()
            sage: a.base_ring()
            Univariate Polynomial Ring in t over Integer Ring
            sage: a.base_ring() is R
            True"""
    @overload
    def base_ring(self) -> Any:
        """OrePolynomial.base_ring(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/ore_polynomial_element.pyx (starting at line 1758)

        Return the base ring of ``self``.

        EXAMPLES::

            sage: R.<t> = ZZ[]
            sage: sigma = R.hom([t+1])
            sage: S.<x> = R['x',sigma]
            sage: a = S.random_element()
            sage: a.base_ring()
            Univariate Polynomial Ring in t over Integer Ring
            sage: a.base_ring() is R
            True"""
    @overload
    def base_ring(self) -> Any:
        """OrePolynomial.base_ring(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/ore_polynomial_element.pyx (starting at line 1758)

        Return the base ring of ``self``.

        EXAMPLES::

            sage: R.<t> = ZZ[]
            sage: sigma = R.hom([t+1])
            sage: S.<x> = R['x',sigma]
            sage: a = S.random_element()
            sage: a.base_ring()
            Univariate Polynomial Ring in t over Integer Ring
            sage: a.base_ring() is R
            True"""
    def change_variable_name(self, var) -> Any:
        """OrePolynomial.change_variable_name(self, var)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/ore_polynomial_element.pyx (starting at line 1845)

        Change the name of the variable of ``self``.

        This will create the Ore polynomial ring with the new name but same
        base ring, twisting morphism and twisting derivation. The returned
        Ore polynomial will be an element of that Ore polynomial ring.

        INPUT:

        - ``var`` -- the name of the new variable

        EXAMPLES::

            sage: R.<t> = ZZ[]
            sage: sigma = R.hom([t+1])
            sage: S.<x> = R['x', sigma]
            sage: a = x^3 + (2*t + 1)*x  + t^2 + 3*t + 5
            sage: b = a.change_variable_name('y'); b
            y^3 + (2*t + 1)*y  + t^2 + 3*t + 5

        Note that a new parent is created at the same time::

            sage: b.parent()
            Ore Polynomial Ring in y over Univariate Polynomial Ring in t over Integer Ring
             twisted by t |--> t + 1"""
    @overload
    def coefficients(self, sparse=...) -> list:
        """OrePolynomial.coefficients(self, sparse=True) -> list

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/ore_polynomial_element.pyx (starting at line 1937)

        Return the coefficients of the monomials appearing in ``self``.

        If ``sparse=True`` (the default), return only the nonzero coefficients.
        Otherwise, return the same value as ``self.list()``.

        .. NOTE::

            This should be overridden in subclasses.

        EXAMPLES::

            sage: R.<t> = QQ[]
            sage: sigma = R.hom([t+1])
            sage: S.<x> = R['x',sigma]
            sage: a = 1 + x^4 + (t+1)*x^2 + t^2
            sage: a.coefficients()
            [t^2 + 1, t + 1, 1]
            sage: a.coefficients(sparse=False)
            [t^2 + 1, 0, t + 1, 0, 1]"""
    @overload
    def coefficients(self) -> Any:
        """OrePolynomial.coefficients(self, sparse=True) -> list

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/ore_polynomial_element.pyx (starting at line 1937)

        Return the coefficients of the monomials appearing in ``self``.

        If ``sparse=True`` (the default), return only the nonzero coefficients.
        Otherwise, return the same value as ``self.list()``.

        .. NOTE::

            This should be overridden in subclasses.

        EXAMPLES::

            sage: R.<t> = QQ[]
            sage: sigma = R.hom([t+1])
            sage: S.<x> = R['x',sigma]
            sage: a = 1 + x^4 + (t+1)*x^2 + t^2
            sage: a.coefficients()
            [t^2 + 1, t + 1, 1]
            sage: a.coefficients(sparse=False)
            [t^2 + 1, 0, t + 1, 0, 1]"""
    @overload
    def coefficients(self, sparse=...) -> Any:
        """OrePolynomial.coefficients(self, sparse=True) -> list

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/ore_polynomial_element.pyx (starting at line 1937)

        Return the coefficients of the monomials appearing in ``self``.

        If ``sparse=True`` (the default), return only the nonzero coefficients.
        Otherwise, return the same value as ``self.list()``.

        .. NOTE::

            This should be overridden in subclasses.

        EXAMPLES::

            sage: R.<t> = QQ[]
            sage: sigma = R.hom([t+1])
            sage: S.<x> = R['x',sigma]
            sage: a = 1 + x^4 + (t+1)*x^2 + t^2
            sage: a.coefficients()
            [t^2 + 1, t + 1, 1]
            sage: a.coefficients(sparse=False)
            [t^2 + 1, 0, t + 1, 0, 1]"""
    @overload
    def constant_coefficient(self) -> Any:
        """OrePolynomial.constant_coefficient(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/ore_polynomial_element.pyx (starting at line 350)

        Return the constant coefficient (i.e., the coefficient of term
        of degree `0`) of ``self``.

        EXAMPLES::

            sage: R.<t> = ZZ[]
            sage: sigma = R.hom([t+1])
            sage: S.<x> = R['x',sigma]
            sage: a = x + t^2 + 2
            sage: a.constant_coefficient()
            t^2 + 2"""
    @overload
    def constant_coefficient(self) -> Any:
        """OrePolynomial.constant_coefficient(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/ore_polynomial_element.pyx (starting at line 350)

        Return the constant coefficient (i.e., the coefficient of term
        of degree `0`) of ``self``.

        EXAMPLES::

            sage: R.<t> = ZZ[]
            sage: sigma = R.hom([t+1])
            sage: S.<x> = R['x',sigma]
            sage: a = x + t^2 + 2
            sage: a.constant_coefficient()
            t^2 + 2"""
    @overload
    def degree(self) -> Integer:
        """OrePolynomial.degree(self) -> Integer

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/ore_polynomial_element.pyx (starting at line 254)

        Return the degree of ``self``.

        By convention, the zero Ore polynomial has degree `-1`.

        EXAMPLES::

            sage: R.<t> = ZZ[]
            sage: sigma = R.hom([t+1])
            sage: S.<x> = R['x',sigma]
            sage: a = x^2 + t*x^3 + t^2*x + 1
            sage: a.degree()
            3
            sage: S.zero().degree()
            -1
            sage: S(5).degree()
            0"""
    @overload
    def degree(self) -> Any:
        """OrePolynomial.degree(self) -> Integer

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/ore_polynomial_element.pyx (starting at line 254)

        Return the degree of ``self``.

        By convention, the zero Ore polynomial has degree `-1`.

        EXAMPLES::

            sage: R.<t> = ZZ[]
            sage: sigma = R.hom([t+1])
            sage: S.<x> = R['x',sigma]
            sage: a = x^2 + t*x^3 + t^2*x + 1
            sage: a.degree()
            3
            sage: S.zero().degree()
            -1
            sage: S(5).degree()
            0"""
    @overload
    def degree(self) -> Any:
        """OrePolynomial.degree(self) -> Integer

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/ore_polynomial_element.pyx (starting at line 254)

        Return the degree of ``self``.

        By convention, the zero Ore polynomial has degree `-1`.

        EXAMPLES::

            sage: R.<t> = ZZ[]
            sage: sigma = R.hom([t+1])
            sage: S.<x> = R['x',sigma]
            sage: a = x^2 + t*x^3 + t^2*x + 1
            sage: a.degree()
            3
            sage: S.zero().degree()
            -1
            sage: S(5).degree()
            0"""
    @overload
    def degree(self) -> Any:
        """OrePolynomial.degree(self) -> Integer

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/ore_polynomial_element.pyx (starting at line 254)

        Return the degree of ``self``.

        By convention, the zero Ore polynomial has degree `-1`.

        EXAMPLES::

            sage: R.<t> = ZZ[]
            sage: sigma = R.hom([t+1])
            sage: S.<x> = R['x',sigma]
            sage: a = x^2 + t*x^3 + t^2*x + 1
            sage: a.degree()
            3
            sage: S.zero().degree()
            -1
            sage: S(5).degree()
            0"""
    @overload
    def exponents(self) -> Any:
        """OrePolynomial.exponents(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/ore_polynomial_element.pyx (starting at line 2093)

        Return the exponents of the monomials appearing in ``self``.

        EXAMPLES::

            sage: R.<t> = QQ[]
            sage: sigma = R.hom([t+1])
            sage: S.<x> = R['x',sigma]
            sage: a = 1 + x^4 + (t+1)*x^2 + t^2
            sage: a.exponents()
            [0, 2, 4]"""
    @overload
    def exponents(self) -> Any:
        """OrePolynomial.exponents(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/ore_polynomial_element.pyx (starting at line 2093)

        Return the exponents of the monomials appearing in ``self``.

        EXAMPLES::

            sage: R.<t> = QQ[]
            sage: sigma = R.hom([t+1])
            sage: S.<x> = R['x',sigma]
            sage: a = 1 + x^4 + (t+1)*x^2 + t^2
            sage: a.exponents()
            [0, 2, 4]"""
    def hamming_weight(self) -> Any:
        """OrePolynomial.number_of_terms(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/ore_polynomial_element.pyx (starting at line 1961)

        Return the number of nonzero coefficients of ``self``.

        This is also known as the weight, hamming weight or sparsity.

        EXAMPLES::

            sage: R.<t> = QQ[]
            sage: sigma = R.hom([t+1])
            sage: S.<x> = R['x',sigma]
            sage: a = 1 + x^4 + (t+1)*x^2 + t^2
            sage: a.number_of_terms()
            3

        This is also an alias for ``hamming_weight``::

            sage: a.hamming_weight()
            3"""
    @overload
    def is_constant(self) -> Any:
        """OrePolynomial.is_constant(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/ore_polynomial_element.pyx (starting at line 2077)

        Return whether ``self`` is a constant polynomial.

        EXAMPLES::

            sage: R.<t> = QQ[]
            sage: sigma = R.hom([t+1])
            sage: S.<x> = R['x',sigma]
            sage: R(2).is_constant()
            True
            sage: (x + 1).is_constant()
            False"""
    @overload
    def is_constant(self) -> Any:
        """OrePolynomial.is_constant(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/ore_polynomial_element.pyx (starting at line 2077)

        Return whether ``self`` is a constant polynomial.

        EXAMPLES::

            sage: R.<t> = QQ[]
            sage: sigma = R.hom([t+1])
            sage: S.<x> = R['x',sigma]
            sage: R(2).is_constant()
            True
            sage: (x + 1).is_constant()
            False"""
    @overload
    def is_constant(self) -> Any:
        """OrePolynomial.is_constant(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/ore_polynomial_element.pyx (starting at line 2077)

        Return whether ``self`` is a constant polynomial.

        EXAMPLES::

            sage: R.<t> = QQ[]
            sage: sigma = R.hom([t+1])
            sage: S.<x> = R['x',sigma]
            sage: R(2).is_constant()
            True
            sage: (x + 1).is_constant()
            False"""
    @overload
    def is_left_divisible_by(self, other) -> Any:
        """OrePolynomial.is_left_divisible_by(self, other)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/ore_polynomial_element.pyx (starting at line 655)

        Check if ``self`` is divisible by ``other`` on the left.

        INPUT:

        - ``other`` -- an Ore polynomial in the same ring as ``self``

        OUTPUT: boolean

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: k.<t> = GF(5^3)
            sage: Frob = k.frobenius_endomorphism()
            sage: S.<x> = k['x',Frob]
            sage: a = x^2 + t*x + t^2 + 3
            sage: b = x^3 + (t + 1)*x^2 + 1
            sage: c = a*b
            sage: c.is_left_divisible_by(a)
            True
            sage: c.is_left_divisible_by(b)
            False

        Divisibility by `0` does not make sense::

            sage: c.is_left_divisible_by(S(0))                                          # needs sage.rings.finite_rings
            Traceback (most recent call last):
            ...
            ZeroDivisionError: division by zero is not valid"""
    @overload
    def is_left_divisible_by(self, a) -> Any:
        """OrePolynomial.is_left_divisible_by(self, other)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/ore_polynomial_element.pyx (starting at line 655)

        Check if ``self`` is divisible by ``other`` on the left.

        INPUT:

        - ``other`` -- an Ore polynomial in the same ring as ``self``

        OUTPUT: boolean

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: k.<t> = GF(5^3)
            sage: Frob = k.frobenius_endomorphism()
            sage: S.<x> = k['x',Frob]
            sage: a = x^2 + t*x + t^2 + 3
            sage: b = x^3 + (t + 1)*x^2 + 1
            sage: c = a*b
            sage: c.is_left_divisible_by(a)
            True
            sage: c.is_left_divisible_by(b)
            False

        Divisibility by `0` does not make sense::

            sage: c.is_left_divisible_by(S(0))                                          # needs sage.rings.finite_rings
            Traceback (most recent call last):
            ...
            ZeroDivisionError: division by zero is not valid"""
    @overload
    def is_left_divisible_by(self, b) -> Any:
        """OrePolynomial.is_left_divisible_by(self, other)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/ore_polynomial_element.pyx (starting at line 655)

        Check if ``self`` is divisible by ``other`` on the left.

        INPUT:

        - ``other`` -- an Ore polynomial in the same ring as ``self``

        OUTPUT: boolean

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: k.<t> = GF(5^3)
            sage: Frob = k.frobenius_endomorphism()
            sage: S.<x> = k['x',Frob]
            sage: a = x^2 + t*x + t^2 + 3
            sage: b = x^3 + (t + 1)*x^2 + 1
            sage: c = a*b
            sage: c.is_left_divisible_by(a)
            True
            sage: c.is_left_divisible_by(b)
            False

        Divisibility by `0` does not make sense::

            sage: c.is_left_divisible_by(S(0))                                          # needs sage.rings.finite_rings
            Traceback (most recent call last):
            ...
            ZeroDivisionError: division by zero is not valid"""
    @overload
    def is_monic(self) -> Any:
        """OrePolynomial.is_monic(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/ore_polynomial_element.pyx (starting at line 451)

        Return ``True`` if this Ore polynomial is monic.

        The zero polynomial is by definition not monic.

        EXAMPLES::

            sage: R.<t> = ZZ[]
            sage: sigma = R.hom([t+1])
            sage: S.<x> = R['x',sigma]
            sage: a = x + t
            sage: a.is_monic()
            True
            sage: a = 0*x
            sage: a.is_monic()
            False
            sage: a = t*x^3 + x^4 + (t+1)*x^2
            sage: a.is_monic()
            True
            sage: a = (t^2 + 2*t)*x^2 + x^3 + t^10*x^5
            sage: a.is_monic()
            False"""
    @overload
    def is_monic(self) -> Any:
        """OrePolynomial.is_monic(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/ore_polynomial_element.pyx (starting at line 451)

        Return ``True`` if this Ore polynomial is monic.

        The zero polynomial is by definition not monic.

        EXAMPLES::

            sage: R.<t> = ZZ[]
            sage: sigma = R.hom([t+1])
            sage: S.<x> = R['x',sigma]
            sage: a = x + t
            sage: a.is_monic()
            True
            sage: a = 0*x
            sage: a.is_monic()
            False
            sage: a = t*x^3 + x^4 + (t+1)*x^2
            sage: a.is_monic()
            True
            sage: a = (t^2 + 2*t)*x^2 + x^3 + t^10*x^5
            sage: a.is_monic()
            False"""
    @overload
    def is_monic(self) -> Any:
        """OrePolynomial.is_monic(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/ore_polynomial_element.pyx (starting at line 451)

        Return ``True`` if this Ore polynomial is monic.

        The zero polynomial is by definition not monic.

        EXAMPLES::

            sage: R.<t> = ZZ[]
            sage: sigma = R.hom([t+1])
            sage: S.<x> = R['x',sigma]
            sage: a = x + t
            sage: a.is_monic()
            True
            sage: a = 0*x
            sage: a.is_monic()
            False
            sage: a = t*x^3 + x^4 + (t+1)*x^2
            sage: a.is_monic()
            True
            sage: a = (t^2 + 2*t)*x^2 + x^3 + t^10*x^5
            sage: a.is_monic()
            False"""
    @overload
    def is_monic(self) -> Any:
        """OrePolynomial.is_monic(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/ore_polynomial_element.pyx (starting at line 451)

        Return ``True`` if this Ore polynomial is monic.

        The zero polynomial is by definition not monic.

        EXAMPLES::

            sage: R.<t> = ZZ[]
            sage: sigma = R.hom([t+1])
            sage: S.<x> = R['x',sigma]
            sage: a = x + t
            sage: a.is_monic()
            True
            sage: a = 0*x
            sage: a.is_monic()
            False
            sage: a = t*x^3 + x^4 + (t+1)*x^2
            sage: a.is_monic()
            True
            sage: a = (t^2 + 2*t)*x^2 + x^3 + t^10*x^5
            sage: a.is_monic()
            False"""
    @overload
    def is_monic(self) -> Any:
        """OrePolynomial.is_monic(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/ore_polynomial_element.pyx (starting at line 451)

        Return ``True`` if this Ore polynomial is monic.

        The zero polynomial is by definition not monic.

        EXAMPLES::

            sage: R.<t> = ZZ[]
            sage: sigma = R.hom([t+1])
            sage: S.<x> = R['x',sigma]
            sage: a = x + t
            sage: a.is_monic()
            True
            sage: a = 0*x
            sage: a.is_monic()
            False
            sage: a = t*x^3 + x^4 + (t+1)*x^2
            sage: a.is_monic()
            True
            sage: a = (t^2 + 2*t)*x^2 + x^3 + t^10*x^5
            sage: a.is_monic()
            False"""
    @overload
    def is_monomial(self) -> Any:
        """OrePolynomial.is_monomial(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/ore_polynomial_element.pyx (starting at line 1902)

        Return ``True`` if ``self`` is a monomial, i.e., a power of
        the generator.

        EXAMPLES::

            sage: R.<t> = ZZ[]
            sage: sigma = R.hom([t+1])
            sage: S.<x> = R['x',sigma]
            sage: x.is_monomial()
            True
            sage: (x+1).is_monomial()
            False
            sage: (x^2).is_monomial()
            True
            sage: S(1).is_monomial()
            True

        The coefficient must be 1::

            sage: (2*x^5).is_monomial()
            False
            sage: S(t).is_monomial()
            False

        To allow a non-1 leading coefficient, use is_term()::

            sage: (2*x^5).is_term()
            True
            sage: S(t).is_term()
            True"""
    @overload
    def is_monomial(self) -> Any:
        """OrePolynomial.is_monomial(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/ore_polynomial_element.pyx (starting at line 1902)

        Return ``True`` if ``self`` is a monomial, i.e., a power of
        the generator.

        EXAMPLES::

            sage: R.<t> = ZZ[]
            sage: sigma = R.hom([t+1])
            sage: S.<x> = R['x',sigma]
            sage: x.is_monomial()
            True
            sage: (x+1).is_monomial()
            False
            sage: (x^2).is_monomial()
            True
            sage: S(1).is_monomial()
            True

        The coefficient must be 1::

            sage: (2*x^5).is_monomial()
            False
            sage: S(t).is_monomial()
            False

        To allow a non-1 leading coefficient, use is_term()::

            sage: (2*x^5).is_term()
            True
            sage: S(t).is_term()
            True"""
    @overload
    def is_monomial(self) -> Any:
        """OrePolynomial.is_monomial(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/ore_polynomial_element.pyx (starting at line 1902)

        Return ``True`` if ``self`` is a monomial, i.e., a power of
        the generator.

        EXAMPLES::

            sage: R.<t> = ZZ[]
            sage: sigma = R.hom([t+1])
            sage: S.<x> = R['x',sigma]
            sage: x.is_monomial()
            True
            sage: (x+1).is_monomial()
            False
            sage: (x^2).is_monomial()
            True
            sage: S(1).is_monomial()
            True

        The coefficient must be 1::

            sage: (2*x^5).is_monomial()
            False
            sage: S(t).is_monomial()
            False

        To allow a non-1 leading coefficient, use is_term()::

            sage: (2*x^5).is_term()
            True
            sage: S(t).is_term()
            True"""
    @overload
    def is_monomial(self) -> Any:
        """OrePolynomial.is_monomial(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/ore_polynomial_element.pyx (starting at line 1902)

        Return ``True`` if ``self`` is a monomial, i.e., a power of
        the generator.

        EXAMPLES::

            sage: R.<t> = ZZ[]
            sage: sigma = R.hom([t+1])
            sage: S.<x> = R['x',sigma]
            sage: x.is_monomial()
            True
            sage: (x+1).is_monomial()
            False
            sage: (x^2).is_monomial()
            True
            sage: S(1).is_monomial()
            True

        The coefficient must be 1::

            sage: (2*x^5).is_monomial()
            False
            sage: S(t).is_monomial()
            False

        To allow a non-1 leading coefficient, use is_term()::

            sage: (2*x^5).is_term()
            True
            sage: S(t).is_term()
            True"""
    @overload
    def is_monomial(self) -> Any:
        """OrePolynomial.is_monomial(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/ore_polynomial_element.pyx (starting at line 1902)

        Return ``True`` if ``self`` is a monomial, i.e., a power of
        the generator.

        EXAMPLES::

            sage: R.<t> = ZZ[]
            sage: sigma = R.hom([t+1])
            sage: S.<x> = R['x',sigma]
            sage: x.is_monomial()
            True
            sage: (x+1).is_monomial()
            False
            sage: (x^2).is_monomial()
            True
            sage: S(1).is_monomial()
            True

        The coefficient must be 1::

            sage: (2*x^5).is_monomial()
            False
            sage: S(t).is_monomial()
            False

        To allow a non-1 leading coefficient, use is_term()::

            sage: (2*x^5).is_term()
            True
            sage: S(t).is_term()
            True"""
    @overload
    def is_monomial(self) -> Any:
        """OrePolynomial.is_monomial(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/ore_polynomial_element.pyx (starting at line 1902)

        Return ``True`` if ``self`` is a monomial, i.e., a power of
        the generator.

        EXAMPLES::

            sage: R.<t> = ZZ[]
            sage: sigma = R.hom([t+1])
            sage: S.<x> = R['x',sigma]
            sage: x.is_monomial()
            True
            sage: (x+1).is_monomial()
            False
            sage: (x^2).is_monomial()
            True
            sage: S(1).is_monomial()
            True

        The coefficient must be 1::

            sage: (2*x^5).is_monomial()
            False
            sage: S(t).is_monomial()
            False

        To allow a non-1 leading coefficient, use is_term()::

            sage: (2*x^5).is_term()
            True
            sage: S(t).is_term()
            True"""
    @overload
    def is_monomial(self) -> Any:
        """OrePolynomial.is_monomial(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/ore_polynomial_element.pyx (starting at line 1902)

        Return ``True`` if ``self`` is a monomial, i.e., a power of
        the generator.

        EXAMPLES::

            sage: R.<t> = ZZ[]
            sage: sigma = R.hom([t+1])
            sage: S.<x> = R['x',sigma]
            sage: x.is_monomial()
            True
            sage: (x+1).is_monomial()
            False
            sage: (x^2).is_monomial()
            True
            sage: S(1).is_monomial()
            True

        The coefficient must be 1::

            sage: (2*x^5).is_monomial()
            False
            sage: S(t).is_monomial()
            False

        To allow a non-1 leading coefficient, use is_term()::

            sage: (2*x^5).is_term()
            True
            sage: S(t).is_term()
            True"""
    def is_nilpotent(self) -> Any:
        '''OrePolynomial.is_nilpotent(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/ore_polynomial_element.pyx (starting at line 426)

        Check if ``self`` is nilpotent.

        .. NOTE::

            The paper "Nilpotents and units in skew polynomial rings
            over commutative rings" by M. Rimmer and K.R. Pearson describes
            a method to check whether a given skew polynomial is nilpotent.
            That method however, requires one to know the order of the
            automorphism which is not available in Sage. This method is thus
            not yet implemented.

        EXAMPLES::

            sage: R.<t> = ZZ[]
            sage: sigma = R.hom([t+1])
            sage: S.<x> = R[\'x\',sigma]
            sage: x.is_nilpotent()
            Traceback (most recent call last):
            ...
            NotImplementedError'''
    @overload
    def is_one(self) -> bool:
        """OrePolynomial.is_one(self) -> bool

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/ore_polynomial_element.pyx (starting at line 2023)

        Test whether this polynomial is `1`.

        EXAMPLES::

            sage: R.<t> = QQ[]
            sage: sigma = R.hom([t+1])
            sage: S.<x> = R['x',sigma]
            sage: R(1).is_one()
            True
            sage: (x + 3).is_one()
            False"""
    @overload
    def is_one(self) -> Any:
        """OrePolynomial.is_one(self) -> bool

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/ore_polynomial_element.pyx (starting at line 2023)

        Test whether this polynomial is `1`.

        EXAMPLES::

            sage: R.<t> = QQ[]
            sage: sigma = R.hom([t+1])
            sage: S.<x> = R['x',sigma]
            sage: R(1).is_one()
            True
            sage: (x + 3).is_one()
            False"""
    @overload
    def is_one(self) -> Any:
        """OrePolynomial.is_one(self) -> bool

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/ore_polynomial_element.pyx (starting at line 2023)

        Test whether this polynomial is `1`.

        EXAMPLES::

            sage: R.<t> = QQ[]
            sage: sigma = R.hom([t+1])
            sage: S.<x> = R['x',sigma]
            sage: R(1).is_one()
            True
            sage: (x + 3).is_one()
            False"""
    @overload
    def is_right_divisible_by(self, other) -> Any:
        """OrePolynomial.is_right_divisible_by(self, other)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/ore_polynomial_element.pyx (starting at line 689)

        Check if ``self`` is divisible by ``other`` on the right.

        INPUT:

        - ``other`` -- an Ore polynomial in the same ring as ``self``

        OUTPUT: boolean

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: k.<t> = GF(5^3)
            sage: Frob = k.frobenius_endomorphism()
            sage: S.<x> = k['x',Frob]
            sage: a = x^2 + t*x + t^2 + 3
            sage: b = x^3 + (t + 1)*x^2 + 1
            sage: c = a*b
            sage: c.is_right_divisible_by(a)
            False
            sage: c.is_right_divisible_by(b)
            True

        Divisibility by `0` does not make sense::

            sage: c.is_right_divisible_by(S(0))                                         # needs sage.rings.finite_rings
            Traceback (most recent call last):
            ...
            ZeroDivisionError: division by zero is not valid

        This function does not work if the leading coefficient of the divisor
        is not a unit::

            sage: R.<t> = QQ[]
            sage: sigma = R.hom([t+1])
            sage: S.<x> = R['x',sigma]
            sage: a = x^2 + 2*x + t
            sage: b = (t+1)*x + t^2
            sage: c = a*b
            sage: c.is_right_divisible_by(b)
            Traceback (most recent call last):
            ...
            NotImplementedError: the leading coefficient of the divisor is not invertible"""
    @overload
    def is_right_divisible_by(self, a) -> Any:
        """OrePolynomial.is_right_divisible_by(self, other)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/ore_polynomial_element.pyx (starting at line 689)

        Check if ``self`` is divisible by ``other`` on the right.

        INPUT:

        - ``other`` -- an Ore polynomial in the same ring as ``self``

        OUTPUT: boolean

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: k.<t> = GF(5^3)
            sage: Frob = k.frobenius_endomorphism()
            sage: S.<x> = k['x',Frob]
            sage: a = x^2 + t*x + t^2 + 3
            sage: b = x^3 + (t + 1)*x^2 + 1
            sage: c = a*b
            sage: c.is_right_divisible_by(a)
            False
            sage: c.is_right_divisible_by(b)
            True

        Divisibility by `0` does not make sense::

            sage: c.is_right_divisible_by(S(0))                                         # needs sage.rings.finite_rings
            Traceback (most recent call last):
            ...
            ZeroDivisionError: division by zero is not valid

        This function does not work if the leading coefficient of the divisor
        is not a unit::

            sage: R.<t> = QQ[]
            sage: sigma = R.hom([t+1])
            sage: S.<x> = R['x',sigma]
            sage: a = x^2 + 2*x + t
            sage: b = (t+1)*x + t^2
            sage: c = a*b
            sage: c.is_right_divisible_by(b)
            Traceback (most recent call last):
            ...
            NotImplementedError: the leading coefficient of the divisor is not invertible"""
    @overload
    def is_right_divisible_by(self, b) -> Any:
        """OrePolynomial.is_right_divisible_by(self, other)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/ore_polynomial_element.pyx (starting at line 689)

        Check if ``self`` is divisible by ``other`` on the right.

        INPUT:

        - ``other`` -- an Ore polynomial in the same ring as ``self``

        OUTPUT: boolean

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: k.<t> = GF(5^3)
            sage: Frob = k.frobenius_endomorphism()
            sage: S.<x> = k['x',Frob]
            sage: a = x^2 + t*x + t^2 + 3
            sage: b = x^3 + (t + 1)*x^2 + 1
            sage: c = a*b
            sage: c.is_right_divisible_by(a)
            False
            sage: c.is_right_divisible_by(b)
            True

        Divisibility by `0` does not make sense::

            sage: c.is_right_divisible_by(S(0))                                         # needs sage.rings.finite_rings
            Traceback (most recent call last):
            ...
            ZeroDivisionError: division by zero is not valid

        This function does not work if the leading coefficient of the divisor
        is not a unit::

            sage: R.<t> = QQ[]
            sage: sigma = R.hom([t+1])
            sage: S.<x> = R['x',sigma]
            sage: a = x^2 + 2*x + t
            sage: b = (t+1)*x + t^2
            sage: c = a*b
            sage: c.is_right_divisible_by(b)
            Traceback (most recent call last):
            ...
            NotImplementedError: the leading coefficient of the divisor is not invertible"""
    @overload
    def is_right_divisible_by(self, b) -> Any:
        """OrePolynomial.is_right_divisible_by(self, other)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/ore_polynomial_element.pyx (starting at line 689)

        Check if ``self`` is divisible by ``other`` on the right.

        INPUT:

        - ``other`` -- an Ore polynomial in the same ring as ``self``

        OUTPUT: boolean

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: k.<t> = GF(5^3)
            sage: Frob = k.frobenius_endomorphism()
            sage: S.<x> = k['x',Frob]
            sage: a = x^2 + t*x + t^2 + 3
            sage: b = x^3 + (t + 1)*x^2 + 1
            sage: c = a*b
            sage: c.is_right_divisible_by(a)
            False
            sage: c.is_right_divisible_by(b)
            True

        Divisibility by `0` does not make sense::

            sage: c.is_right_divisible_by(S(0))                                         # needs sage.rings.finite_rings
            Traceback (most recent call last):
            ...
            ZeroDivisionError: division by zero is not valid

        This function does not work if the leading coefficient of the divisor
        is not a unit::

            sage: R.<t> = QQ[]
            sage: sigma = R.hom([t+1])
            sage: S.<x> = R['x',sigma]
            sage: a = x^2 + 2*x + t
            sage: b = (t+1)*x + t^2
            sage: c = a*b
            sage: c.is_right_divisible_by(b)
            Traceback (most recent call last):
            ...
            NotImplementedError: the leading coefficient of the divisor is not invertible"""
    @overload
    def is_term(self) -> Any:
        """OrePolynomial.is_term(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/ore_polynomial_element.pyx (starting at line 1875)

        Return ``True`` if ``self`` is an element of the base ring times a
        power of the generator.

        EXAMPLES::

            sage: R.<t> = ZZ[]
            sage: sigma = R.hom([t+1])
            sage: S.<x> = R['x',sigma]
            sage: x.is_term()
            True
            sage: R(1).is_term()
            True
            sage: (3*x^5).is_term()
            True
            sage: (1+3*x^5).is_term()
            False

        If you want to test that ``self`` also has leading coefficient 1, use
        :meth:`is_monomial()` instead::

            sage: (3*x^5).is_monomial()
            False"""
    @overload
    def is_term(self) -> Any:
        """OrePolynomial.is_term(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/ore_polynomial_element.pyx (starting at line 1875)

        Return ``True`` if ``self`` is an element of the base ring times a
        power of the generator.

        EXAMPLES::

            sage: R.<t> = ZZ[]
            sage: sigma = R.hom([t+1])
            sage: S.<x> = R['x',sigma]
            sage: x.is_term()
            True
            sage: R(1).is_term()
            True
            sage: (3*x^5).is_term()
            True
            sage: (1+3*x^5).is_term()
            False

        If you want to test that ``self`` also has leading coefficient 1, use
        :meth:`is_monomial()` instead::

            sage: (3*x^5).is_monomial()
            False"""
    @overload
    def is_term(self) -> Any:
        """OrePolynomial.is_term(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/ore_polynomial_element.pyx (starting at line 1875)

        Return ``True`` if ``self`` is an element of the base ring times a
        power of the generator.

        EXAMPLES::

            sage: R.<t> = ZZ[]
            sage: sigma = R.hom([t+1])
            sage: S.<x> = R['x',sigma]
            sage: x.is_term()
            True
            sage: R(1).is_term()
            True
            sage: (3*x^5).is_term()
            True
            sage: (1+3*x^5).is_term()
            False

        If you want to test that ``self`` also has leading coefficient 1, use
        :meth:`is_monomial()` instead::

            sage: (3*x^5).is_monomial()
            False"""
    @overload
    def is_term(self) -> Any:
        """OrePolynomial.is_term(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/ore_polynomial_element.pyx (starting at line 1875)

        Return ``True`` if ``self`` is an element of the base ring times a
        power of the generator.

        EXAMPLES::

            sage: R.<t> = ZZ[]
            sage: sigma = R.hom([t+1])
            sage: S.<x> = R['x',sigma]
            sage: x.is_term()
            True
            sage: R(1).is_term()
            True
            sage: (3*x^5).is_term()
            True
            sage: (1+3*x^5).is_term()
            False

        If you want to test that ``self`` also has leading coefficient 1, use
        :meth:`is_monomial()` instead::

            sage: (3*x^5).is_monomial()
            False"""
    @overload
    def is_term(self) -> Any:
        """OrePolynomial.is_term(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/ore_polynomial_element.pyx (starting at line 1875)

        Return ``True`` if ``self`` is an element of the base ring times a
        power of the generator.

        EXAMPLES::

            sage: R.<t> = ZZ[]
            sage: sigma = R.hom([t+1])
            sage: S.<x> = R['x',sigma]
            sage: x.is_term()
            True
            sage: R(1).is_term()
            True
            sage: (3*x^5).is_term()
            True
            sage: (1+3*x^5).is_term()
            False

        If you want to test that ``self`` also has leading coefficient 1, use
        :meth:`is_monomial()` instead::

            sage: (3*x^5).is_monomial()
            False"""
    @overload
    def is_unit(self) -> Any:
        """OrePolynomial.is_unit(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/ore_polynomial_element.pyx (starting at line 393)

        Return ``True`` if this Ore polynomial is a unit.

        When the base ring `R` is an integral domain, then an Ore polynomial `f`
        is a unit if and only if degree of `f` is `0` and `f` is then a unit in
        `R`.

        .. NOTE::

            The case when `R` is not an integral domain is not yet implemented.

        EXAMPLES::

            sage: R.<t> = ZZ[]
            sage: sigma = R.hom([t+1])
            sage: S.<x> = R['x',sigma]
            sage: a = x + (t+1)*x^5 + t^2*x^3 - x^5
            sage: a.is_unit()
            False"""
    @overload
    def is_unit(self) -> Any:
        """OrePolynomial.is_unit(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/ore_polynomial_element.pyx (starting at line 393)

        Return ``True`` if this Ore polynomial is a unit.

        When the base ring `R` is an integral domain, then an Ore polynomial `f`
        is a unit if and only if degree of `f` is `0` and `f` is then a unit in
        `R`.

        .. NOTE::

            The case when `R` is not an integral domain is not yet implemented.

        EXAMPLES::

            sage: R.<t> = ZZ[]
            sage: sigma = R.hom([t+1])
            sage: S.<x> = R['x',sigma]
            sage: a = x + (t+1)*x^5 + t^2*x^3 - x^5
            sage: a.is_unit()
            False"""
    @overload
    def is_zero(self) -> bool:
        """OrePolynomial.is_zero(self) -> bool

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/ore_polynomial_element.pyx (starting at line 2005)

        Return ``True`` if ``self`` is the zero polynomial.

        EXAMPLES::

            sage: R.<t> = ZZ[]
            sage: sigma = R.hom([t+1])
            sage: S.<x> = R['x',sigma]
            sage: a = x + 1
            sage: a.is_zero()
            False
            sage: b = S.zero()
            sage: b.is_zero()
            True"""
    @overload
    def is_zero(self) -> Any:
        """OrePolynomial.is_zero(self) -> bool

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/ore_polynomial_element.pyx (starting at line 2005)

        Return ``True`` if ``self`` is the zero polynomial.

        EXAMPLES::

            sage: R.<t> = ZZ[]
            sage: sigma = R.hom([t+1])
            sage: S.<x> = R['x',sigma]
            sage: a = x + 1
            sage: a.is_zero()
            False
            sage: b = S.zero()
            sage: b.is_zero()
            True"""
    @overload
    def is_zero(self) -> Any:
        """OrePolynomial.is_zero(self) -> bool

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/ore_polynomial_element.pyx (starting at line 2005)

        Return ``True`` if ``self`` is the zero polynomial.

        EXAMPLES::

            sage: R.<t> = ZZ[]
            sage: sigma = R.hom([t+1])
            sage: S.<x> = R['x',sigma]
            sage: a = x + 1
            sage: a.is_zero()
            False
            sage: b = S.zero()
            sage: b.is_zero()
            True"""
    @overload
    def leading_coefficient(self) -> Any:
        """OrePolynomial.leading_coefficient(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/ore_polynomial_element.pyx (starting at line 369)

        Return the coefficient of the highest-degree monomial of ``self``.

        EXAMPLES::

            sage: R.<t> = ZZ[]
            sage: sigma = R.hom([t+1])
            sage: S.<x> = R['x',sigma]
            sage: a = (t+1)*x^5 + t^2*x^3 + x
            sage: a.leading_coefficient()
            t + 1

        By convention, the leading coefficient to the zero polynomial is
        zero::

            sage: S(0).leading_coefficient()
            0"""
    @overload
    def leading_coefficient(self) -> Any:
        """OrePolynomial.leading_coefficient(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/ore_polynomial_element.pyx (starting at line 369)

        Return the coefficient of the highest-degree monomial of ``self``.

        EXAMPLES::

            sage: R.<t> = ZZ[]
            sage: sigma = R.hom([t+1])
            sage: S.<x> = R['x',sigma]
            sage: a = (t+1)*x^5 + t^2*x^3 + x
            sage: a.leading_coefficient()
            t + 1

        By convention, the leading coefficient to the zero polynomial is
        zero::

            sage: S(0).leading_coefficient()
            0"""
    @overload
    def leading_coefficient(self) -> Any:
        """OrePolynomial.leading_coefficient(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/ore_polynomial_element.pyx (starting at line 369)

        Return the coefficient of the highest-degree monomial of ``self``.

        EXAMPLES::

            sage: R.<t> = ZZ[]
            sage: sigma = R.hom([t+1])
            sage: S.<x> = R['x',sigma]
            sage: a = (t+1)*x^5 + t^2*x^3 + x
            sage: a.leading_coefficient()
            t + 1

        By convention, the leading coefficient to the zero polynomial is
        zero::

            sage: S(0).leading_coefficient()
            0"""
    @overload
    def left_divides(self, other) -> Any:
        """OrePolynomial.left_divides(self, other)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/ore_polynomial_element.pyx (starting at line 737)

        Check if ``self`` divides ``other`` on the left.

        INPUT:

        - ``other`` -- an Ore polynomial in the same ring as ``self``

        OUTPUT: boolean

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: k.<t> = GF(5^3)
            sage: Frob = k.frobenius_endomorphism()
            sage: S.<x> = k['x',Frob]
            sage: a = x^2 + t*x + t^2 + 3
            sage: b = x^3 + (t + 1)*x^2 + 1
            sage: c = a * b
            sage: a.left_divides(c)
            True
            sage: b.left_divides(c)
            False

        Divisibility by `0` does not make sense::

            sage: S(0).left_divides(c)                                                  # needs sage.rings.finite_rings
            Traceback (most recent call last):
            ...
            ZeroDivisionError: division by zero is not valid"""
    @overload
    def left_divides(self, c) -> Any:
        """OrePolynomial.left_divides(self, other)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/ore_polynomial_element.pyx (starting at line 737)

        Check if ``self`` divides ``other`` on the left.

        INPUT:

        - ``other`` -- an Ore polynomial in the same ring as ``self``

        OUTPUT: boolean

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: k.<t> = GF(5^3)
            sage: Frob = k.frobenius_endomorphism()
            sage: S.<x> = k['x',Frob]
            sage: a = x^2 + t*x + t^2 + 3
            sage: b = x^3 + (t + 1)*x^2 + 1
            sage: c = a * b
            sage: a.left_divides(c)
            True
            sage: b.left_divides(c)
            False

        Divisibility by `0` does not make sense::

            sage: S(0).left_divides(c)                                                  # needs sage.rings.finite_rings
            Traceback (most recent call last):
            ...
            ZeroDivisionError: division by zero is not valid"""
    @overload
    def left_divides(self, c) -> Any:
        """OrePolynomial.left_divides(self, other)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/ore_polynomial_element.pyx (starting at line 737)

        Check if ``self`` divides ``other`` on the left.

        INPUT:

        - ``other`` -- an Ore polynomial in the same ring as ``self``

        OUTPUT: boolean

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: k.<t> = GF(5^3)
            sage: Frob = k.frobenius_endomorphism()
            sage: S.<x> = k['x',Frob]
            sage: a = x^2 + t*x + t^2 + 3
            sage: b = x^3 + (t + 1)*x^2 + 1
            sage: c = a * b
            sage: a.left_divides(c)
            True
            sage: b.left_divides(c)
            False

        Divisibility by `0` does not make sense::

            sage: S(0).left_divides(c)                                                  # needs sage.rings.finite_rings
            Traceback (most recent call last):
            ...
            ZeroDivisionError: division by zero is not valid"""
    @overload
    def left_divides(self, c) -> Any:
        """OrePolynomial.left_divides(self, other)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/ore_polynomial_element.pyx (starting at line 737)

        Check if ``self`` divides ``other`` on the left.

        INPUT:

        - ``other`` -- an Ore polynomial in the same ring as ``self``

        OUTPUT: boolean

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: k.<t> = GF(5^3)
            sage: Frob = k.frobenius_endomorphism()
            sage: S.<x> = k['x',Frob]
            sage: a = x^2 + t*x + t^2 + 3
            sage: b = x^3 + (t + 1)*x^2 + 1
            sage: c = a * b
            sage: a.left_divides(c)
            True
            sage: b.left_divides(c)
            False

        Divisibility by `0` does not make sense::

            sage: S(0).left_divides(c)                                                  # needs sage.rings.finite_rings
            Traceback (most recent call last):
            ...
            ZeroDivisionError: division by zero is not valid"""
    @overload
    def left_gcd(self, other, monic=...) -> Any:
        """OrePolynomial.left_gcd(self, other, monic=True)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/ore_polynomial_element.pyx (starting at line 1218)

        Return the left gcd of ``self`` and ``other``.

        INPUT:

        - ``other`` -- an Ore polynomial in the same ring as ``self``

        - ``monic`` -- boolean (default: ``True``); return whether the left gcd
          should be normalized to be monic

        OUTPUT:

        The left gcd of ``self`` and ``other``, that is an Ore polynomial
        `g` with the following property: any Ore polynomial is
        divisible on the left by `g` iff it is divisible on the left
        by both ``self`` and ``other``.
        If monic is ``True``, `g` is in addition monic. (With this
        extra condition, it is uniquely determined.)

        .. NOTE::

            Works only if following two conditions are fulfilled
            (otherwise left gcd do not exist in general):
            1) the base ring is a field and
            2) the twisting morphism is bijective.

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: k.<t> = GF(5^3)
            sage: Frob = k.frobenius_endomorphism()
            sage: S.<x> = k['x',Frob]
            sage: a = (x + t) * (x^2 + t*x + 1)
            sage: b = 2 * (x + t) * (x^3 + (t+1)*x^2 + t^2)
            sage: a.left_gcd(b)
            x + t

        Specifying ``monic=False``, we *can* get a nonmonic gcd::

            sage: a.left_gcd(b,monic=False)                                             # needs sage.rings.finite_rings
            2*t*x + 4*t + 2

        The base ring needs to be a field::

            sage: # needs sage.rings.finite_rings
            sage: R.<t> = QQ[]
            sage: sigma = R.hom([t + 1])
            sage: S.<x> = R['x',sigma]
            sage: a = (x + t) * (x^2 + t*x + 1)
            sage: b = 2 * (x + t) * (x^3 + (t+1)*x^2 + t^2)
            sage: a.left_gcd(b)
            Traceback (most recent call last):
            ...
            TypeError: the base ring must be a field

        And the twisting morphism needs to be bijective::

            sage: # needs sage.rings.finite_rings
            sage: FR = R.fraction_field()
            sage: f = FR.hom([FR(t)^2])
            sage: S.<x> = FR['x',f]
            sage: a = (x + t) * (x^2 + t*x + 1)
            sage: b = 2 * (x + t) * (x^3 + (t+1)*x^2 + t^2)
            sage: a.left_gcd(b)
            Traceback (most recent call last):
            ...
            NotImplementedError: inversion of the twisting morphism Ring endomorphism
            of Fraction Field of Univariate Polynomial Ring in t over Rational Field
                Defn: t |--> t^2"""
    @overload
    def left_gcd(self, b) -> Any:
        """OrePolynomial.left_gcd(self, other, monic=True)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/ore_polynomial_element.pyx (starting at line 1218)

        Return the left gcd of ``self`` and ``other``.

        INPUT:

        - ``other`` -- an Ore polynomial in the same ring as ``self``

        - ``monic`` -- boolean (default: ``True``); return whether the left gcd
          should be normalized to be monic

        OUTPUT:

        The left gcd of ``self`` and ``other``, that is an Ore polynomial
        `g` with the following property: any Ore polynomial is
        divisible on the left by `g` iff it is divisible on the left
        by both ``self`` and ``other``.
        If monic is ``True``, `g` is in addition monic. (With this
        extra condition, it is uniquely determined.)

        .. NOTE::

            Works only if following two conditions are fulfilled
            (otherwise left gcd do not exist in general):
            1) the base ring is a field and
            2) the twisting morphism is bijective.

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: k.<t> = GF(5^3)
            sage: Frob = k.frobenius_endomorphism()
            sage: S.<x> = k['x',Frob]
            sage: a = (x + t) * (x^2 + t*x + 1)
            sage: b = 2 * (x + t) * (x^3 + (t+1)*x^2 + t^2)
            sage: a.left_gcd(b)
            x + t

        Specifying ``monic=False``, we *can* get a nonmonic gcd::

            sage: a.left_gcd(b,monic=False)                                             # needs sage.rings.finite_rings
            2*t*x + 4*t + 2

        The base ring needs to be a field::

            sage: # needs sage.rings.finite_rings
            sage: R.<t> = QQ[]
            sage: sigma = R.hom([t + 1])
            sage: S.<x> = R['x',sigma]
            sage: a = (x + t) * (x^2 + t*x + 1)
            sage: b = 2 * (x + t) * (x^3 + (t+1)*x^2 + t^2)
            sage: a.left_gcd(b)
            Traceback (most recent call last):
            ...
            TypeError: the base ring must be a field

        And the twisting morphism needs to be bijective::

            sage: # needs sage.rings.finite_rings
            sage: FR = R.fraction_field()
            sage: f = FR.hom([FR(t)^2])
            sage: S.<x> = FR['x',f]
            sage: a = (x + t) * (x^2 + t*x + 1)
            sage: b = 2 * (x + t) * (x^3 + (t+1)*x^2 + t^2)
            sage: a.left_gcd(b)
            Traceback (most recent call last):
            ...
            NotImplementedError: inversion of the twisting morphism Ring endomorphism
            of Fraction Field of Univariate Polynomial Ring in t over Rational Field
                Defn: t |--> t^2"""
    @overload
    def left_gcd(self, b, monic=...) -> Any:
        """OrePolynomial.left_gcd(self, other, monic=True)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/ore_polynomial_element.pyx (starting at line 1218)

        Return the left gcd of ``self`` and ``other``.

        INPUT:

        - ``other`` -- an Ore polynomial in the same ring as ``self``

        - ``monic`` -- boolean (default: ``True``); return whether the left gcd
          should be normalized to be monic

        OUTPUT:

        The left gcd of ``self`` and ``other``, that is an Ore polynomial
        `g` with the following property: any Ore polynomial is
        divisible on the left by `g` iff it is divisible on the left
        by both ``self`` and ``other``.
        If monic is ``True``, `g` is in addition monic. (With this
        extra condition, it is uniquely determined.)

        .. NOTE::

            Works only if following two conditions are fulfilled
            (otherwise left gcd do not exist in general):
            1) the base ring is a field and
            2) the twisting morphism is bijective.

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: k.<t> = GF(5^3)
            sage: Frob = k.frobenius_endomorphism()
            sage: S.<x> = k['x',Frob]
            sage: a = (x + t) * (x^2 + t*x + 1)
            sage: b = 2 * (x + t) * (x^3 + (t+1)*x^2 + t^2)
            sage: a.left_gcd(b)
            x + t

        Specifying ``monic=False``, we *can* get a nonmonic gcd::

            sage: a.left_gcd(b,monic=False)                                             # needs sage.rings.finite_rings
            2*t*x + 4*t + 2

        The base ring needs to be a field::

            sage: # needs sage.rings.finite_rings
            sage: R.<t> = QQ[]
            sage: sigma = R.hom([t + 1])
            sage: S.<x> = R['x',sigma]
            sage: a = (x + t) * (x^2 + t*x + 1)
            sage: b = 2 * (x + t) * (x^3 + (t+1)*x^2 + t^2)
            sage: a.left_gcd(b)
            Traceback (most recent call last):
            ...
            TypeError: the base ring must be a field

        And the twisting morphism needs to be bijective::

            sage: # needs sage.rings.finite_rings
            sage: FR = R.fraction_field()
            sage: f = FR.hom([FR(t)^2])
            sage: S.<x> = FR['x',f]
            sage: a = (x + t) * (x^2 + t*x + 1)
            sage: b = 2 * (x + t) * (x^3 + (t+1)*x^2 + t^2)
            sage: a.left_gcd(b)
            Traceback (most recent call last):
            ...
            NotImplementedError: inversion of the twisting morphism Ring endomorphism
            of Fraction Field of Univariate Polynomial Ring in t over Rational Field
                Defn: t |--> t^2"""
    @overload
    def left_gcd(self, b) -> Any:
        """OrePolynomial.left_gcd(self, other, monic=True)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/ore_polynomial_element.pyx (starting at line 1218)

        Return the left gcd of ``self`` and ``other``.

        INPUT:

        - ``other`` -- an Ore polynomial in the same ring as ``self``

        - ``monic`` -- boolean (default: ``True``); return whether the left gcd
          should be normalized to be monic

        OUTPUT:

        The left gcd of ``self`` and ``other``, that is an Ore polynomial
        `g` with the following property: any Ore polynomial is
        divisible on the left by `g` iff it is divisible on the left
        by both ``self`` and ``other``.
        If monic is ``True``, `g` is in addition monic. (With this
        extra condition, it is uniquely determined.)

        .. NOTE::

            Works only if following two conditions are fulfilled
            (otherwise left gcd do not exist in general):
            1) the base ring is a field and
            2) the twisting morphism is bijective.

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: k.<t> = GF(5^3)
            sage: Frob = k.frobenius_endomorphism()
            sage: S.<x> = k['x',Frob]
            sage: a = (x + t) * (x^2 + t*x + 1)
            sage: b = 2 * (x + t) * (x^3 + (t+1)*x^2 + t^2)
            sage: a.left_gcd(b)
            x + t

        Specifying ``monic=False``, we *can* get a nonmonic gcd::

            sage: a.left_gcd(b,monic=False)                                             # needs sage.rings.finite_rings
            2*t*x + 4*t + 2

        The base ring needs to be a field::

            sage: # needs sage.rings.finite_rings
            sage: R.<t> = QQ[]
            sage: sigma = R.hom([t + 1])
            sage: S.<x> = R['x',sigma]
            sage: a = (x + t) * (x^2 + t*x + 1)
            sage: b = 2 * (x + t) * (x^3 + (t+1)*x^2 + t^2)
            sage: a.left_gcd(b)
            Traceback (most recent call last):
            ...
            TypeError: the base ring must be a field

        And the twisting morphism needs to be bijective::

            sage: # needs sage.rings.finite_rings
            sage: FR = R.fraction_field()
            sage: f = FR.hom([FR(t)^2])
            sage: S.<x> = FR['x',f]
            sage: a = (x + t) * (x^2 + t*x + 1)
            sage: b = 2 * (x + t) * (x^3 + (t+1)*x^2 + t^2)
            sage: a.left_gcd(b)
            Traceback (most recent call last):
            ...
            NotImplementedError: inversion of the twisting morphism Ring endomorphism
            of Fraction Field of Univariate Polynomial Ring in t over Rational Field
                Defn: t |--> t^2"""
    @overload
    def left_gcd(self, b) -> Any:
        """OrePolynomial.left_gcd(self, other, monic=True)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/ore_polynomial_element.pyx (starting at line 1218)

        Return the left gcd of ``self`` and ``other``.

        INPUT:

        - ``other`` -- an Ore polynomial in the same ring as ``self``

        - ``monic`` -- boolean (default: ``True``); return whether the left gcd
          should be normalized to be monic

        OUTPUT:

        The left gcd of ``self`` and ``other``, that is an Ore polynomial
        `g` with the following property: any Ore polynomial is
        divisible on the left by `g` iff it is divisible on the left
        by both ``self`` and ``other``.
        If monic is ``True``, `g` is in addition monic. (With this
        extra condition, it is uniquely determined.)

        .. NOTE::

            Works only if following two conditions are fulfilled
            (otherwise left gcd do not exist in general):
            1) the base ring is a field and
            2) the twisting morphism is bijective.

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: k.<t> = GF(5^3)
            sage: Frob = k.frobenius_endomorphism()
            sage: S.<x> = k['x',Frob]
            sage: a = (x + t) * (x^2 + t*x + 1)
            sage: b = 2 * (x + t) * (x^3 + (t+1)*x^2 + t^2)
            sage: a.left_gcd(b)
            x + t

        Specifying ``monic=False``, we *can* get a nonmonic gcd::

            sage: a.left_gcd(b,monic=False)                                             # needs sage.rings.finite_rings
            2*t*x + 4*t + 2

        The base ring needs to be a field::

            sage: # needs sage.rings.finite_rings
            sage: R.<t> = QQ[]
            sage: sigma = R.hom([t + 1])
            sage: S.<x> = R['x',sigma]
            sage: a = (x + t) * (x^2 + t*x + 1)
            sage: b = 2 * (x + t) * (x^3 + (t+1)*x^2 + t^2)
            sage: a.left_gcd(b)
            Traceback (most recent call last):
            ...
            TypeError: the base ring must be a field

        And the twisting morphism needs to be bijective::

            sage: # needs sage.rings.finite_rings
            sage: FR = R.fraction_field()
            sage: f = FR.hom([FR(t)^2])
            sage: S.<x> = FR['x',f]
            sage: a = (x + t) * (x^2 + t*x + 1)
            sage: b = 2 * (x + t) * (x^3 + (t+1)*x^2 + t^2)
            sage: a.left_gcd(b)
            Traceback (most recent call last):
            ...
            NotImplementedError: inversion of the twisting morphism Ring endomorphism
            of Fraction Field of Univariate Polynomial Ring in t over Rational Field
                Defn: t |--> t^2"""
    @overload
    def left_lcm(self, other, monic=...) -> Any:
        """OrePolynomial.left_lcm(self, other, monic=True)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/ore_polynomial_element.pyx (starting at line 1468)

        Return the left lcm of ``self`` and ``other``.

        INPUT:

        - ``other`` -- an Ore polynomial in the same ring as ``self``

        - ``monic`` -- boolean (default: ``True``); return whether the left lcm
          should be normalized to be monic

        OUTPUT:

        The left lcm of ``self`` and ``other``, that is an Ore polynomial
        `l` with the following property: any Ore polynomial is a left multiple of `l` (right divisible by `l`)
        iff it is a left multiple of both ``self`` and ``other`` (right divisible by ``self`` and ``other``).
        If monic is ``True``, `l` is in addition monic. (With this
        extra condition, it is uniquely determined.)

        .. NOTE::

            Works only if the base ring is a field (otherwise left
            lcm do not exist in general).

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: k.<t> = GF(5^3)
            sage: Frob = k.frobenius_endomorphism()
            sage: S.<x> = k['x',Frob]
            sage: a = (x + t^2) * (x + t)
            sage: b = 2 * (x^2 + t + 1) * (x * t)
            sage: c = a.left_lcm(b); c
            x^5 + (2*t^2 + t + 4)*x^4 + (3*t^2 + 4)*x^3 + (3*t^2 + 3*t + 2)*x^2 + (t^2 + t + 2)*x
            sage: c.is_right_divisible_by(a)
            True
            sage: c.is_right_divisible_by(b)
            True
            sage: a.degree() + b.degree() == c.degree() + a.right_gcd(b).degree()
            True

        Specifying ``monic=False``, we *can* get a nonmonic lcm::

            sage: a.left_lcm(b,monic=False)                                             # needs sage.rings.finite_rings
            (t^2 + t)*x^5 + (4*t^2 + 4*t + 1)*x^4 + (t + 1)*x^3 + (t^2 + 2)*x^2 + (3*t + 4)*x

        The base ring needs to be a field::

            sage: R.<t> = QQ[]
            sage: sigma = R.hom([t+1])
            sage: S.<x> = R['x',sigma]
            sage: a = (x + t^2) * (x + t)
            sage: b = 2 * (x^2 + t + 1) * (x * t)
            sage: a.left_lcm(b)
            Traceback (most recent call last):
            ...
            TypeError: the base ring must be a field"""
    @overload
    def left_lcm(self, b) -> Any:
        """OrePolynomial.left_lcm(self, other, monic=True)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/ore_polynomial_element.pyx (starting at line 1468)

        Return the left lcm of ``self`` and ``other``.

        INPUT:

        - ``other`` -- an Ore polynomial in the same ring as ``self``

        - ``monic`` -- boolean (default: ``True``); return whether the left lcm
          should be normalized to be monic

        OUTPUT:

        The left lcm of ``self`` and ``other``, that is an Ore polynomial
        `l` with the following property: any Ore polynomial is a left multiple of `l` (right divisible by `l`)
        iff it is a left multiple of both ``self`` and ``other`` (right divisible by ``self`` and ``other``).
        If monic is ``True``, `l` is in addition monic. (With this
        extra condition, it is uniquely determined.)

        .. NOTE::

            Works only if the base ring is a field (otherwise left
            lcm do not exist in general).

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: k.<t> = GF(5^3)
            sage: Frob = k.frobenius_endomorphism()
            sage: S.<x> = k['x',Frob]
            sage: a = (x + t^2) * (x + t)
            sage: b = 2 * (x^2 + t + 1) * (x * t)
            sage: c = a.left_lcm(b); c
            x^5 + (2*t^2 + t + 4)*x^4 + (3*t^2 + 4)*x^3 + (3*t^2 + 3*t + 2)*x^2 + (t^2 + t + 2)*x
            sage: c.is_right_divisible_by(a)
            True
            sage: c.is_right_divisible_by(b)
            True
            sage: a.degree() + b.degree() == c.degree() + a.right_gcd(b).degree()
            True

        Specifying ``monic=False``, we *can* get a nonmonic lcm::

            sage: a.left_lcm(b,monic=False)                                             # needs sage.rings.finite_rings
            (t^2 + t)*x^5 + (4*t^2 + 4*t + 1)*x^4 + (t + 1)*x^3 + (t^2 + 2)*x^2 + (3*t + 4)*x

        The base ring needs to be a field::

            sage: R.<t> = QQ[]
            sage: sigma = R.hom([t+1])
            sage: S.<x> = R['x',sigma]
            sage: a = (x + t^2) * (x + t)
            sage: b = 2 * (x^2 + t + 1) * (x * t)
            sage: a.left_lcm(b)
            Traceback (most recent call last):
            ...
            TypeError: the base ring must be a field"""
    @overload
    def left_lcm(self, b, monic=...) -> Any:
        """OrePolynomial.left_lcm(self, other, monic=True)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/ore_polynomial_element.pyx (starting at line 1468)

        Return the left lcm of ``self`` and ``other``.

        INPUT:

        - ``other`` -- an Ore polynomial in the same ring as ``self``

        - ``monic`` -- boolean (default: ``True``); return whether the left lcm
          should be normalized to be monic

        OUTPUT:

        The left lcm of ``self`` and ``other``, that is an Ore polynomial
        `l` with the following property: any Ore polynomial is a left multiple of `l` (right divisible by `l`)
        iff it is a left multiple of both ``self`` and ``other`` (right divisible by ``self`` and ``other``).
        If monic is ``True``, `l` is in addition monic. (With this
        extra condition, it is uniquely determined.)

        .. NOTE::

            Works only if the base ring is a field (otherwise left
            lcm do not exist in general).

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: k.<t> = GF(5^3)
            sage: Frob = k.frobenius_endomorphism()
            sage: S.<x> = k['x',Frob]
            sage: a = (x + t^2) * (x + t)
            sage: b = 2 * (x^2 + t + 1) * (x * t)
            sage: c = a.left_lcm(b); c
            x^5 + (2*t^2 + t + 4)*x^4 + (3*t^2 + 4)*x^3 + (3*t^2 + 3*t + 2)*x^2 + (t^2 + t + 2)*x
            sage: c.is_right_divisible_by(a)
            True
            sage: c.is_right_divisible_by(b)
            True
            sage: a.degree() + b.degree() == c.degree() + a.right_gcd(b).degree()
            True

        Specifying ``monic=False``, we *can* get a nonmonic lcm::

            sage: a.left_lcm(b,monic=False)                                             # needs sage.rings.finite_rings
            (t^2 + t)*x^5 + (4*t^2 + 4*t + 1)*x^4 + (t + 1)*x^3 + (t^2 + 2)*x^2 + (3*t + 4)*x

        The base ring needs to be a field::

            sage: R.<t> = QQ[]
            sage: sigma = R.hom([t+1])
            sage: S.<x> = R['x',sigma]
            sage: a = (x + t^2) * (x + t)
            sage: b = 2 * (x^2 + t + 1) * (x * t)
            sage: a.left_lcm(b)
            Traceback (most recent call last):
            ...
            TypeError: the base ring must be a field"""
    @overload
    def left_lcm(self, b) -> Any:
        """OrePolynomial.left_lcm(self, other, monic=True)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/ore_polynomial_element.pyx (starting at line 1468)

        Return the left lcm of ``self`` and ``other``.

        INPUT:

        - ``other`` -- an Ore polynomial in the same ring as ``self``

        - ``monic`` -- boolean (default: ``True``); return whether the left lcm
          should be normalized to be monic

        OUTPUT:

        The left lcm of ``self`` and ``other``, that is an Ore polynomial
        `l` with the following property: any Ore polynomial is a left multiple of `l` (right divisible by `l`)
        iff it is a left multiple of both ``self`` and ``other`` (right divisible by ``self`` and ``other``).
        If monic is ``True``, `l` is in addition monic. (With this
        extra condition, it is uniquely determined.)

        .. NOTE::

            Works only if the base ring is a field (otherwise left
            lcm do not exist in general).

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: k.<t> = GF(5^3)
            sage: Frob = k.frobenius_endomorphism()
            sage: S.<x> = k['x',Frob]
            sage: a = (x + t^2) * (x + t)
            sage: b = 2 * (x^2 + t + 1) * (x * t)
            sage: c = a.left_lcm(b); c
            x^5 + (2*t^2 + t + 4)*x^4 + (3*t^2 + 4)*x^3 + (3*t^2 + 3*t + 2)*x^2 + (t^2 + t + 2)*x
            sage: c.is_right_divisible_by(a)
            True
            sage: c.is_right_divisible_by(b)
            True
            sage: a.degree() + b.degree() == c.degree() + a.right_gcd(b).degree()
            True

        Specifying ``monic=False``, we *can* get a nonmonic lcm::

            sage: a.left_lcm(b,monic=False)                                             # needs sage.rings.finite_rings
            (t^2 + t)*x^5 + (4*t^2 + 4*t + 1)*x^4 + (t + 1)*x^3 + (t^2 + 2)*x^2 + (3*t + 4)*x

        The base ring needs to be a field::

            sage: R.<t> = QQ[]
            sage: sigma = R.hom([t+1])
            sage: S.<x> = R['x',sigma]
            sage: a = (x + t^2) * (x + t)
            sage: b = 2 * (x^2 + t + 1) * (x * t)
            sage: a.left_lcm(b)
            Traceback (most recent call last):
            ...
            TypeError: the base ring must be a field"""
    @overload
    def left_mod(self, other) -> Any:
        """OrePolynomial.left_mod(self, other)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/ore_polynomial_element.pyx (starting at line 2058)

        Return the remainder of left division of ``self`` by ``other``.

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: k.<t> = GF(5^3)
            sage: Frob = k.frobenius_endomorphism()
            sage: S.<x> = k['x',Frob]
            sage: a = 1 + t*x^2
            sage: b = x + 1
            sage: a.left_mod(b)
            2*t^2 + 4*t"""
    @overload
    def left_mod(self, b) -> Any:
        """OrePolynomial.left_mod(self, other)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/ore_polynomial_element.pyx (starting at line 2058)

        Return the remainder of left division of ``self`` by ``other``.

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: k.<t> = GF(5^3)
            sage: Frob = k.frobenius_endomorphism()
            sage: S.<x> = k['x',Frob]
            sage: a = 1 + t*x^2
            sage: b = x + 1
            sage: a.left_mod(b)
            2*t^2 + 4*t"""
    def left_monic(self) -> Any:
        """OrePolynomial.left_monic(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/ore_polynomial_element.pyx (starting at line 477)

        Return the unique monic Ore polynomial `m` which divides this
        polynomial on the left and has the same degree.

        Given an Ore polynomial `P` of degree `n`, its left monic is given by
        `P \\cdot \\sigma^{-n}(1/k)`, where `k` is the leading coefficient of
        `P` and `\\sigma` is the twisting morphism.

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: k.<t> = GF(5^3)
            sage: Frob = k.frobenius_endomorphism()
            sage: S.<x> = k['x',Frob]
            sage: a = (3*t^2 + 3*t + 2)*x^3 + (2*t^2 + 3)*x^2 + (4*t^2 + t + 4)*x + 2*t^2 + 2
            sage: b = a.left_monic(); b
            x^3 + (4*t^2 + 3*t)*x^2 + (4*t + 2)*x + 2*t^2 + 4*t + 3

        Check list::

            sage: # needs sage.rings.finite_rings
            sage: b.degree() == a.degree()
            True
            sage: a.is_left_divisible_by(b)
            True
            sage: twist = S.twisting_morphism(-a.degree())
            sage: a == b * twist(a.leading_coefficient())
            True

        Note that `b` does not divide `a` on the right::

            sage: a.is_right_divisible_by(b)                                            # needs sage.rings.finite_rings
            False

        This function does not work if the leading coefficient is not a
        unit::

            sage: R.<t> = QQ[]
            sage: der = R.derivation()
            sage: S.<x> = R['x', der]
            sage: a = t*x
            sage: a.left_monic()
            Traceback (most recent call last):
            ...
            NotImplementedError: the leading coefficient is not a unit"""
    def left_quo_rem(self, other) -> Any:
        """OrePolynomial.left_quo_rem(self, other)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/ore_polynomial_element.pyx (starting at line 944)

        Return the quotient and remainder of the left Euclidean
        division of ``self`` by ``other``.

        INPUT:

        - ``other`` -- an Ore polynomial in the same ring as ``self``

        OUTPUT:

        - the quotient and the remainder of the left Euclidean
          division of this Ore polynomial by ``other``

        .. NOTE::

            This will fail if the leading coefficient of ``other`` is not a unit
            or if Sage can't invert the twisting morphism.

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: k.<t> = GF(5^3)
            sage: Frob = k.frobenius_endomorphism()
            sage: S.<x> = k['x',Frob]
            sage: a = (3*t^2 + 3*t + 2)*x^3 + (2*t^2 + 3)*x^2 + (4*t^2 + t + 4)*x + 2*t^2 + 2
            sage: b = (3*t^2 + 4*t + 2)*x^2 + (2*t^2 + 4*t + 3)*x + 2*t^2 + t + 1
            sage: q,r = a.left_quo_rem(b)
            sage: a == b*q + r
            True

        In the following example, Sage does not know the inverse
        of the twisting morphism::

            sage: R.<t> = QQ[]
            sage: K = R.fraction_field()
            sage: sigma = K.hom([(t+1)/(t-1)])
            sage: S.<x> = K['x',sigma]
            sage: a = (-2*t^2 - t + 1)*x^3 + (-t^2 + t)*x^2 + (-12*t - 2)*x - t^2 - 95*t + 1
            sage: b = x^2 + (5*t - 6)*x - 4*t^2 + 4*t - 1
            sage: a.left_quo_rem(b)
            Traceback (most recent call last):
            ...
            NotImplementedError: inversion of the twisting morphism Ring endomorphism of Fraction Field of Univariate Polynomial Ring in t over Rational Field
              Defn: t |--> (t + 1)/(t - 1)"""
    def left_xgcd(self, other, monic=...) -> Any:
        """OrePolynomial.left_xgcd(self, other, monic=True)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/ore_polynomial_element.pyx (starting at line 819)

        Return the left gcd of ``self`` and ``other`` along with the
        coefficients for the linear combination.

        If `a` is ``self`` and `b` is ``other``, then there are Ore polynomials
        `u` and `v` such that `g = a u + b v`, where `g` is the left gcd of `a`
        and `b`. This method returns `(g, u, v)`.

        INPUT:

        - ``other`` -- an Ore polynomial in the same ring as ``self``

        - ``monic`` -- boolean (default: ``True``); return whether the left gcd
          should be normalized to be monic

        OUTPUT:

        - The left gcd of ``self`` and ``other``, that is an Ore polynomial
          `g` with the following property: any Ore polynomial is
          divisible on the left by `g` iff it is divisible on the left
          by both ``self`` and ``other``.
          If monic is ``True``, `g` is in addition monic. (With this
          extra condition, it is uniquely determined.)

        - Two Ore polynomials `u` and `v` such that:

          .. MATH::

              g = a \\cdot u + b \\cdot v,

          where `s` is ``self`` and `b` is ``other``.

        .. NOTE::

            Works only if following two conditions are fulfilled
            (otherwise left gcd do not exist in general):
            1) the base ring is a field and
            2) the twisting morphism is bijective.

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: k.<t> = GF(5^3)
            sage: Frob = k.frobenius_endomorphism()
            sage: S.<x> = k['x',Frob]
            sage: a = (x + t) * (x^2 + t*x + 1)
            sage: b = 2 * (x + t) * (x^3 + (t+1)*x^2 + t^2)
            sage: g,u,v = a.left_xgcd(b); g
            x + t
            sage: a*u + b*v == g
            True

        Specifying ``monic=False``, we *can* get a nonmonic gcd::

            sage: g,u,v = a.left_xgcd(b, monic=False); g                                # needs sage.rings.finite_rings
            2*t*x + 4*t + 2
            sage: a*u + b*v == g                                                        # needs sage.rings.finite_rings
            True

        The base ring must be a field::

            sage: R.<t> = QQ[]
            sage: sigma = R.hom([t+1])
            sage: S.<x> = R['x',sigma]
            sage: a = (x + t) * (x^2 + t*x + 1)
            sage: b = 2 * (x + t) * (x^3 + (t+1)*x^2 + t^2)
            sage: a.left_xgcd(b)
            Traceback (most recent call last):
            ...
            TypeError: the base ring must be a field

        And the twisting morphism must be bijective::

            sage: FR = R.fraction_field()
            sage: f = FR.hom([FR(t)^2])
            sage: S.<x> = FR['x',f]
            sage: a = (x + t) * (x^2 + t*x + 1)
            sage: b = 2 * (x + t) * (x^3 + (t+1)*x^2 + t^2)
            sage: a.left_xgcd(b)
            Traceback (most recent call last):
            ...
            NotImplementedError: inversion of the twisting morphism Ring endomorphism of Fraction Field of Univariate Polynomial Ring in t over Rational Field
                Defn: t |--> t^2"""
    def left_xlcm(self, other, monic=...) -> Any:
        """OrePolynomial.left_xlcm(self, other, monic=True)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/ore_polynomial_element.pyx (starting at line 1343)

        Return the left lcm `L` of ``self`` and ``other`` together
        with two Ore polynomials `U` and `V` such that

        .. MATH::

            U \\cdot \\text{self} = V \\cdot \\text{other} = L.

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: k.<t> = GF(5^3)
            sage: Frob = k.frobenius_endomorphism()
            sage: S.<x> = k['x',Frob]
            sage: P = (x + t^2) * (x + t)
            sage: Q = 2 * (x^2 + t + 1) * (x * t)
            sage: L, U, V = P.left_xlcm(Q)
            sage: L
            x^5 + (2*t^2 + t + 4)*x^4 + (3*t^2 + 4)*x^3 + (3*t^2 + 3*t + 2)*x^2 + (t^2 + t + 2)*x

            sage: U * P == L                                                            # needs sage.rings.finite_rings
            True
            sage: V * Q == L                                                            # needs sage.rings.finite_rings
            True"""
    @overload
    def number_of_terms(self) -> Any:
        """OrePolynomial.number_of_terms(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/ore_polynomial_element.pyx (starting at line 1961)

        Return the number of nonzero coefficients of ``self``.

        This is also known as the weight, hamming weight or sparsity.

        EXAMPLES::

            sage: R.<t> = QQ[]
            sage: sigma = R.hom([t+1])
            sage: S.<x> = R['x',sigma]
            sage: a = 1 + x^4 + (t+1)*x^2 + t^2
            sage: a.number_of_terms()
            3

        This is also an alias for ``hamming_weight``::

            sage: a.hamming_weight()
            3"""
    @overload
    def number_of_terms(self) -> Any:
        """OrePolynomial.number_of_terms(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/ore_polynomial_element.pyx (starting at line 1961)

        Return the number of nonzero coefficients of ``self``.

        This is also known as the weight, hamming weight or sparsity.

        EXAMPLES::

            sage: R.<t> = QQ[]
            sage: sigma = R.hom([t+1])
            sage: S.<x> = R['x',sigma]
            sage: a = 1 + x^4 + (t+1)*x^2 + t^2
            sage: a.number_of_terms()
            3

        This is also an alias for ``hamming_weight``::

            sage: a.hamming_weight()
            3"""
    @overload
    def padded_list(self, n=...) -> Any:
        """OrePolynomial.padded_list(self, n=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/ore_polynomial_element.pyx (starting at line 2125)

        Return list of coefficients of ``self`` up to (but not including)
        degree `n`.

        Includes `0`s in the list on the right so that the list always has length
        exactly `n`.

        INPUT:

        - ``n`` -- (default: ``None``) if given, an integer that
          is at least `0`

        EXAMPLES::

            sage: R.<t> = QQ[]
            sage: sigma = R.hom([t+1])
            sage: S.<x> = R['x',sigma]
            sage: a = 1 + t*x^3 + t^2*x^5
            sage: a.padded_list()
            [1, 0, 0, t, 0, t^2]
            sage: a.padded_list(10)
            [1, 0, 0, t, 0, t^2, 0, 0, 0, 0]
            sage: len(a.padded_list(10))
            10
            sage: a.padded_list(3)
            [1, 0, 0]
            sage: a.padded_list(0)
            []
            sage: a.padded_list(-1)
            Traceback (most recent call last):
            ...
            ValueError: n must be at least 0"""
    @overload
    def padded_list(self) -> Any:
        """OrePolynomial.padded_list(self, n=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/ore_polynomial_element.pyx (starting at line 2125)

        Return list of coefficients of ``self`` up to (but not including)
        degree `n`.

        Includes `0`s in the list on the right so that the list always has length
        exactly `n`.

        INPUT:

        - ``n`` -- (default: ``None``) if given, an integer that
          is at least `0`

        EXAMPLES::

            sage: R.<t> = QQ[]
            sage: sigma = R.hom([t+1])
            sage: S.<x> = R['x',sigma]
            sage: a = 1 + t*x^3 + t^2*x^5
            sage: a.padded_list()
            [1, 0, 0, t, 0, t^2]
            sage: a.padded_list(10)
            [1, 0, 0, t, 0, t^2, 0, 0, 0, 0]
            sage: len(a.padded_list(10))
            10
            sage: a.padded_list(3)
            [1, 0, 0]
            sage: a.padded_list(0)
            []
            sage: a.padded_list(-1)
            Traceback (most recent call last):
            ...
            ValueError: n must be at least 0"""
    @overload
    def prec(self) -> Any:
        """OrePolynomial.prec(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/ore_polynomial_element.pyx (starting at line 2108)

        Return the precision of ``self``.

        This is always infinity, since polynomials are of infinite precision by
        definition (there is no big-oh).

        EXAMPLES::

            sage: R.<t> = QQ[]
            sage: sigma = R.hom([t+1])
            sage: S.<x> = R['x',sigma]
            sage: x.prec()
            +Infinity"""
    @overload
    def prec(self) -> Any:
        """OrePolynomial.prec(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/ore_polynomial_element.pyx (starting at line 2108)

        Return the precision of ``self``.

        This is always infinity, since polynomials are of infinite precision by
        definition (there is no big-oh).

        EXAMPLES::

            sage: R.<t> = QQ[]
            sage: sigma = R.hom([t+1])
            sage: S.<x> = R['x',sigma]
            sage: x.prec()
            +Infinity"""
    @overload
    def right_divides(self, other) -> Any:
        """OrePolynomial.right_divides(self, other)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/ore_polynomial_element.pyx (starting at line 771)

        Check if ``self`` divides ``other`` on the right.

        INPUT:

        - ``other`` -- an Ore polynomial in the same ring as ``self``

        OUTPUT: boolean

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: k.<t> = GF(5^3)
            sage: Frob = k.frobenius_endomorphism()
            sage: S.<x> = k['x',Frob]
            sage: a = x^2 + t*x + t^2 + 3
            sage: b = x^3 + (t + 1)*x^2 + 1
            sage: c = a * b
            sage: a.right_divides(c)
            False
            sage: b.right_divides(c)
            True

        Divisibility by `0` does not make sense::

            sage: S(0).right_divides(c)                                                 # needs sage.rings.finite_rings
            Traceback (most recent call last):
            ...
            ZeroDivisionError: division by zero is not valid

        This function does not work if the leading coefficient of the divisor
        is not a unit::

            sage: R.<t> = QQ[]
            sage: sigma = R.hom([t+1])
            sage: S.<x> = R['x',sigma]
            sage: a = x^2 + 2*x + t
            sage: b = (t+1)*x + t^2
            sage: c = a*b
            sage: b.right_divides(c)
            Traceback (most recent call last):
            ...
            NotImplementedError: the leading coefficient of the divisor is not invertible"""
    @overload
    def right_divides(self, c) -> Any:
        """OrePolynomial.right_divides(self, other)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/ore_polynomial_element.pyx (starting at line 771)

        Check if ``self`` divides ``other`` on the right.

        INPUT:

        - ``other`` -- an Ore polynomial in the same ring as ``self``

        OUTPUT: boolean

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: k.<t> = GF(5^3)
            sage: Frob = k.frobenius_endomorphism()
            sage: S.<x> = k['x',Frob]
            sage: a = x^2 + t*x + t^2 + 3
            sage: b = x^3 + (t + 1)*x^2 + 1
            sage: c = a * b
            sage: a.right_divides(c)
            False
            sage: b.right_divides(c)
            True

        Divisibility by `0` does not make sense::

            sage: S(0).right_divides(c)                                                 # needs sage.rings.finite_rings
            Traceback (most recent call last):
            ...
            ZeroDivisionError: division by zero is not valid

        This function does not work if the leading coefficient of the divisor
        is not a unit::

            sage: R.<t> = QQ[]
            sage: sigma = R.hom([t+1])
            sage: S.<x> = R['x',sigma]
            sage: a = x^2 + 2*x + t
            sage: b = (t+1)*x + t^2
            sage: c = a*b
            sage: b.right_divides(c)
            Traceback (most recent call last):
            ...
            NotImplementedError: the leading coefficient of the divisor is not invertible"""
    @overload
    def right_divides(self, c) -> Any:
        """OrePolynomial.right_divides(self, other)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/ore_polynomial_element.pyx (starting at line 771)

        Check if ``self`` divides ``other`` on the right.

        INPUT:

        - ``other`` -- an Ore polynomial in the same ring as ``self``

        OUTPUT: boolean

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: k.<t> = GF(5^3)
            sage: Frob = k.frobenius_endomorphism()
            sage: S.<x> = k['x',Frob]
            sage: a = x^2 + t*x + t^2 + 3
            sage: b = x^3 + (t + 1)*x^2 + 1
            sage: c = a * b
            sage: a.right_divides(c)
            False
            sage: b.right_divides(c)
            True

        Divisibility by `0` does not make sense::

            sage: S(0).right_divides(c)                                                 # needs sage.rings.finite_rings
            Traceback (most recent call last):
            ...
            ZeroDivisionError: division by zero is not valid

        This function does not work if the leading coefficient of the divisor
        is not a unit::

            sage: R.<t> = QQ[]
            sage: sigma = R.hom([t+1])
            sage: S.<x> = R['x',sigma]
            sage: a = x^2 + 2*x + t
            sage: b = (t+1)*x + t^2
            sage: c = a*b
            sage: b.right_divides(c)
            Traceback (most recent call last):
            ...
            NotImplementedError: the leading coefficient of the divisor is not invertible"""
    @overload
    def right_divides(self, c) -> Any:
        """OrePolynomial.right_divides(self, other)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/ore_polynomial_element.pyx (starting at line 771)

        Check if ``self`` divides ``other`` on the right.

        INPUT:

        - ``other`` -- an Ore polynomial in the same ring as ``self``

        OUTPUT: boolean

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: k.<t> = GF(5^3)
            sage: Frob = k.frobenius_endomorphism()
            sage: S.<x> = k['x',Frob]
            sage: a = x^2 + t*x + t^2 + 3
            sage: b = x^3 + (t + 1)*x^2 + 1
            sage: c = a * b
            sage: a.right_divides(c)
            False
            sage: b.right_divides(c)
            True

        Divisibility by `0` does not make sense::

            sage: S(0).right_divides(c)                                                 # needs sage.rings.finite_rings
            Traceback (most recent call last):
            ...
            ZeroDivisionError: division by zero is not valid

        This function does not work if the leading coefficient of the divisor
        is not a unit::

            sage: R.<t> = QQ[]
            sage: sigma = R.hom([t+1])
            sage: S.<x> = R['x',sigma]
            sage: a = x^2 + 2*x + t
            sage: b = (t+1)*x + t^2
            sage: c = a*b
            sage: b.right_divides(c)
            Traceback (most recent call last):
            ...
            NotImplementedError: the leading coefficient of the divisor is not invertible"""
    @overload
    def right_divides(self, c) -> Any:
        """OrePolynomial.right_divides(self, other)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/ore_polynomial_element.pyx (starting at line 771)

        Check if ``self`` divides ``other`` on the right.

        INPUT:

        - ``other`` -- an Ore polynomial in the same ring as ``self``

        OUTPUT: boolean

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: k.<t> = GF(5^3)
            sage: Frob = k.frobenius_endomorphism()
            sage: S.<x> = k['x',Frob]
            sage: a = x^2 + t*x + t^2 + 3
            sage: b = x^3 + (t + 1)*x^2 + 1
            sage: c = a * b
            sage: a.right_divides(c)
            False
            sage: b.right_divides(c)
            True

        Divisibility by `0` does not make sense::

            sage: S(0).right_divides(c)                                                 # needs sage.rings.finite_rings
            Traceback (most recent call last):
            ...
            ZeroDivisionError: division by zero is not valid

        This function does not work if the leading coefficient of the divisor
        is not a unit::

            sage: R.<t> = QQ[]
            sage: sigma = R.hom([t+1])
            sage: S.<x> = R['x',sigma]
            sage: a = x^2 + 2*x + t
            sage: b = (t+1)*x + t^2
            sage: c = a*b
            sage: b.right_divides(c)
            Traceback (most recent call last):
            ...
            NotImplementedError: the leading coefficient of the divisor is not invertible"""
    @overload
    def right_gcd(self, other, monic=...) -> Any:
        """OrePolynomial.right_gcd(self, other, monic=True)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/ore_polynomial_element.pyx (starting at line 1152)

        Return the right gcd of ``self`` and ``other``.

        INPUT:

        - ``other`` -- an Ore polynomial in the same ring as ``self``

        - ``monic`` -- boolean (default: ``True``); return whether the right gcd
          should be normalized to be monic

        OUTPUT:

        The right gcd of ``self`` and ``other``, that is an Ore polynomial
        `g` with the following property: any Ore polynomial is
        divisible on the right by `g` iff it is divisible on the right
        by both ``self`` and ``other``.
        If monic is ``True``, `g` is in addition monic. (With this
        extra condition, it is uniquely determined.)

        .. NOTE::

            Works only if the base ring is a field (otherwise right
            gcd do not exist in general).

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: k.<t> = GF(5^3)
            sage: Frob = k.frobenius_endomorphism()
            sage: S.<x> = k['x',Frob]
            sage: a = (x^2 + t*x + 1) * (x + t)
            sage: b = 2 * (x^3 + (t+1)*x^2 + t^2) * (x + t)
            sage: a.right_gcd(b)
            x + t

        Specifying ``monic=False``, we *can* get a nonmonic gcd::

            sage: a.right_gcd(b,monic=False)                                            # needs sage.rings.finite_rings
            (4*t^2 + 4*t + 1)*x + 4*t^2 + 4*t + 3

        The base ring need to be a field::

            sage: R.<t> = QQ[]
            sage: sigma = R.hom([t+1])
            sage: S.<x> = R['x',sigma]
            sage: a = (x^2 + t*x + 1) * (x + t)
            sage: b = 2 * (x^3 + (t+1)*x^2 + t^2) * (x + t)
            sage: a.right_gcd(b)
            Traceback (most recent call last):
            ...
            TypeError: the base ring must be a field"""
    @overload
    def right_gcd(self, b) -> Any:
        """OrePolynomial.right_gcd(self, other, monic=True)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/ore_polynomial_element.pyx (starting at line 1152)

        Return the right gcd of ``self`` and ``other``.

        INPUT:

        - ``other`` -- an Ore polynomial in the same ring as ``self``

        - ``monic`` -- boolean (default: ``True``); return whether the right gcd
          should be normalized to be monic

        OUTPUT:

        The right gcd of ``self`` and ``other``, that is an Ore polynomial
        `g` with the following property: any Ore polynomial is
        divisible on the right by `g` iff it is divisible on the right
        by both ``self`` and ``other``.
        If monic is ``True``, `g` is in addition monic. (With this
        extra condition, it is uniquely determined.)

        .. NOTE::

            Works only if the base ring is a field (otherwise right
            gcd do not exist in general).

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: k.<t> = GF(5^3)
            sage: Frob = k.frobenius_endomorphism()
            sage: S.<x> = k['x',Frob]
            sage: a = (x^2 + t*x + 1) * (x + t)
            sage: b = 2 * (x^3 + (t+1)*x^2 + t^2) * (x + t)
            sage: a.right_gcd(b)
            x + t

        Specifying ``monic=False``, we *can* get a nonmonic gcd::

            sage: a.right_gcd(b,monic=False)                                            # needs sage.rings.finite_rings
            (4*t^2 + 4*t + 1)*x + 4*t^2 + 4*t + 3

        The base ring need to be a field::

            sage: R.<t> = QQ[]
            sage: sigma = R.hom([t+1])
            sage: S.<x> = R['x',sigma]
            sage: a = (x^2 + t*x + 1) * (x + t)
            sage: b = 2 * (x^3 + (t+1)*x^2 + t^2) * (x + t)
            sage: a.right_gcd(b)
            Traceback (most recent call last):
            ...
            TypeError: the base ring must be a field"""
    @overload
    def right_gcd(self, b, monic=...) -> Any:
        """OrePolynomial.right_gcd(self, other, monic=True)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/ore_polynomial_element.pyx (starting at line 1152)

        Return the right gcd of ``self`` and ``other``.

        INPUT:

        - ``other`` -- an Ore polynomial in the same ring as ``self``

        - ``monic`` -- boolean (default: ``True``); return whether the right gcd
          should be normalized to be monic

        OUTPUT:

        The right gcd of ``self`` and ``other``, that is an Ore polynomial
        `g` with the following property: any Ore polynomial is
        divisible on the right by `g` iff it is divisible on the right
        by both ``self`` and ``other``.
        If monic is ``True``, `g` is in addition monic. (With this
        extra condition, it is uniquely determined.)

        .. NOTE::

            Works only if the base ring is a field (otherwise right
            gcd do not exist in general).

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: k.<t> = GF(5^3)
            sage: Frob = k.frobenius_endomorphism()
            sage: S.<x> = k['x',Frob]
            sage: a = (x^2 + t*x + 1) * (x + t)
            sage: b = 2 * (x^3 + (t+1)*x^2 + t^2) * (x + t)
            sage: a.right_gcd(b)
            x + t

        Specifying ``monic=False``, we *can* get a nonmonic gcd::

            sage: a.right_gcd(b,monic=False)                                            # needs sage.rings.finite_rings
            (4*t^2 + 4*t + 1)*x + 4*t^2 + 4*t + 3

        The base ring need to be a field::

            sage: R.<t> = QQ[]
            sage: sigma = R.hom([t+1])
            sage: S.<x> = R['x',sigma]
            sage: a = (x^2 + t*x + 1) * (x + t)
            sage: b = 2 * (x^3 + (t+1)*x^2 + t^2) * (x + t)
            sage: a.right_gcd(b)
            Traceback (most recent call last):
            ...
            TypeError: the base ring must be a field"""
    @overload
    def right_gcd(self, b) -> Any:
        """OrePolynomial.right_gcd(self, other, monic=True)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/ore_polynomial_element.pyx (starting at line 1152)

        Return the right gcd of ``self`` and ``other``.

        INPUT:

        - ``other`` -- an Ore polynomial in the same ring as ``self``

        - ``monic`` -- boolean (default: ``True``); return whether the right gcd
          should be normalized to be monic

        OUTPUT:

        The right gcd of ``self`` and ``other``, that is an Ore polynomial
        `g` with the following property: any Ore polynomial is
        divisible on the right by `g` iff it is divisible on the right
        by both ``self`` and ``other``.
        If monic is ``True``, `g` is in addition monic. (With this
        extra condition, it is uniquely determined.)

        .. NOTE::

            Works only if the base ring is a field (otherwise right
            gcd do not exist in general).

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: k.<t> = GF(5^3)
            sage: Frob = k.frobenius_endomorphism()
            sage: S.<x> = k['x',Frob]
            sage: a = (x^2 + t*x + 1) * (x + t)
            sage: b = 2 * (x^3 + (t+1)*x^2 + t^2) * (x + t)
            sage: a.right_gcd(b)
            x + t

        Specifying ``monic=False``, we *can* get a nonmonic gcd::

            sage: a.right_gcd(b,monic=False)                                            # needs sage.rings.finite_rings
            (4*t^2 + 4*t + 1)*x + 4*t^2 + 4*t + 3

        The base ring need to be a field::

            sage: R.<t> = QQ[]
            sage: sigma = R.hom([t+1])
            sage: S.<x> = R['x',sigma]
            sage: a = (x^2 + t*x + 1) * (x + t)
            sage: b = 2 * (x^3 + (t+1)*x^2 + t^2) * (x + t)
            sage: a.right_gcd(b)
            Traceback (most recent call last):
            ...
            TypeError: the base ring must be a field"""
    @overload
    def right_lcm(self, other, monic=...) -> Any:
        """OrePolynomial.right_lcm(self, other, monic=True)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/ore_polynomial_element.pyx (starting at line 1536)

        Return the right lcm of ``self`` and ``other``.

        INPUT:

        - ``other`` -- an Ore polynomial in the same ring as ``self``

        - ``monic`` -- boolean (default: ``True``); return whether the right lcm
          should be normalized to be monic

        OUTPUT:

        The right lcm of ``self`` and ``other``, that is an Ore polynomial
        `l` with the following property: any Ore polynomial is a right multiple of `g` (left divisible by `l`)
        iff it is a right multiple of both ``self`` and ``other`` (left divisible by ``self`` and ``other``).
        If monic is ``True``, `g` is in addition monic. (With this
        extra condition, it is uniquely determined.)

        .. NOTE::

            Works only if two following conditions are fulfilled
            (otherwise right lcm do not exist in general):
            1) the base ring is a field and 2) the twisting morphism on
            this field is bijective.

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: k.<t> = GF(5^3)
            sage: Frob = k.frobenius_endomorphism()
            sage: S.<x> = k['x',Frob]
            sage: a = (x + t) * (x + t^2)
            sage: b = 2 * (x + t) * (x^2 + t + 1)
            sage: c = a.right_lcm(b); c
            x^4 + (2*t^2 + t + 2)*x^3 + (3*t^2 + 4*t + 1)*x^2 + (3*t^2 + 4*t + 1)*x + t^2 + 4
            sage: c.is_left_divisible_by(a)
            True
            sage: c.is_left_divisible_by(b)
            True
            sage: a.degree() + b.degree() == c.degree() + a.left_gcd(b).degree()
            True

        Specifying ``monic=False``, we *can* get a nonmonic gcd::

            sage: a.right_lcm(b,monic=False)                                            # needs sage.rings.finite_rings
            2*t*x^4 + (3*t + 1)*x^3 + (4*t^2 + 4*t + 3)*x^2
             + (3*t^2 + 4*t + 2)*x + 3*t^2 + 2*t + 3

        The base ring needs to be a field::

            sage: R.<t> = QQ[]
            sage: sigma = R.hom([t+1])
            sage: S.<x> = R['x',sigma]
            sage: a = (x + t) * (x + t^2)
            sage: b = 2 * (x + t) * (x^2 + t + 1)
            sage: a.right_lcm(b)
            Traceback (most recent call last):
            ...
            TypeError: the base ring must be a field

        And the twisting morphism needs to be bijective::

            sage: FR = R.fraction_field()
            sage: f = FR.hom([FR(t)^2])
            sage: S.<x> = FR['x',f]
            sage: a = (x + t) * (x + t^2)
            sage: b = 2 * (x + t) * (x^2 + t + 1)
            sage: a.right_lcm(b)
            Traceback (most recent call last):
            ...
            NotImplementedError: inversion of the twisting morphism Ring endomorphism of
            Fraction Field of Univariate Polynomial Ring in t over Rational Field
                Defn: t |--> t^2"""
    @overload
    def right_lcm(self, b) -> Any:
        """OrePolynomial.right_lcm(self, other, monic=True)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/ore_polynomial_element.pyx (starting at line 1536)

        Return the right lcm of ``self`` and ``other``.

        INPUT:

        - ``other`` -- an Ore polynomial in the same ring as ``self``

        - ``monic`` -- boolean (default: ``True``); return whether the right lcm
          should be normalized to be monic

        OUTPUT:

        The right lcm of ``self`` and ``other``, that is an Ore polynomial
        `l` with the following property: any Ore polynomial is a right multiple of `g` (left divisible by `l`)
        iff it is a right multiple of both ``self`` and ``other`` (left divisible by ``self`` and ``other``).
        If monic is ``True``, `g` is in addition monic. (With this
        extra condition, it is uniquely determined.)

        .. NOTE::

            Works only if two following conditions are fulfilled
            (otherwise right lcm do not exist in general):
            1) the base ring is a field and 2) the twisting morphism on
            this field is bijective.

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: k.<t> = GF(5^3)
            sage: Frob = k.frobenius_endomorphism()
            sage: S.<x> = k['x',Frob]
            sage: a = (x + t) * (x + t^2)
            sage: b = 2 * (x + t) * (x^2 + t + 1)
            sage: c = a.right_lcm(b); c
            x^4 + (2*t^2 + t + 2)*x^3 + (3*t^2 + 4*t + 1)*x^2 + (3*t^2 + 4*t + 1)*x + t^2 + 4
            sage: c.is_left_divisible_by(a)
            True
            sage: c.is_left_divisible_by(b)
            True
            sage: a.degree() + b.degree() == c.degree() + a.left_gcd(b).degree()
            True

        Specifying ``monic=False``, we *can* get a nonmonic gcd::

            sage: a.right_lcm(b,monic=False)                                            # needs sage.rings.finite_rings
            2*t*x^4 + (3*t + 1)*x^3 + (4*t^2 + 4*t + 3)*x^2
             + (3*t^2 + 4*t + 2)*x + 3*t^2 + 2*t + 3

        The base ring needs to be a field::

            sage: R.<t> = QQ[]
            sage: sigma = R.hom([t+1])
            sage: S.<x> = R['x',sigma]
            sage: a = (x + t) * (x + t^2)
            sage: b = 2 * (x + t) * (x^2 + t + 1)
            sage: a.right_lcm(b)
            Traceback (most recent call last):
            ...
            TypeError: the base ring must be a field

        And the twisting morphism needs to be bijective::

            sage: FR = R.fraction_field()
            sage: f = FR.hom([FR(t)^2])
            sage: S.<x> = FR['x',f]
            sage: a = (x + t) * (x + t^2)
            sage: b = 2 * (x + t) * (x^2 + t + 1)
            sage: a.right_lcm(b)
            Traceback (most recent call last):
            ...
            NotImplementedError: inversion of the twisting morphism Ring endomorphism of
            Fraction Field of Univariate Polynomial Ring in t over Rational Field
                Defn: t |--> t^2"""
    @overload
    def right_lcm(self, b, monic=...) -> Any:
        """OrePolynomial.right_lcm(self, other, monic=True)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/ore_polynomial_element.pyx (starting at line 1536)

        Return the right lcm of ``self`` and ``other``.

        INPUT:

        - ``other`` -- an Ore polynomial in the same ring as ``self``

        - ``monic`` -- boolean (default: ``True``); return whether the right lcm
          should be normalized to be monic

        OUTPUT:

        The right lcm of ``self`` and ``other``, that is an Ore polynomial
        `l` with the following property: any Ore polynomial is a right multiple of `g` (left divisible by `l`)
        iff it is a right multiple of both ``self`` and ``other`` (left divisible by ``self`` and ``other``).
        If monic is ``True``, `g` is in addition monic. (With this
        extra condition, it is uniquely determined.)

        .. NOTE::

            Works only if two following conditions are fulfilled
            (otherwise right lcm do not exist in general):
            1) the base ring is a field and 2) the twisting morphism on
            this field is bijective.

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: k.<t> = GF(5^3)
            sage: Frob = k.frobenius_endomorphism()
            sage: S.<x> = k['x',Frob]
            sage: a = (x + t) * (x + t^2)
            sage: b = 2 * (x + t) * (x^2 + t + 1)
            sage: c = a.right_lcm(b); c
            x^4 + (2*t^2 + t + 2)*x^3 + (3*t^2 + 4*t + 1)*x^2 + (3*t^2 + 4*t + 1)*x + t^2 + 4
            sage: c.is_left_divisible_by(a)
            True
            sage: c.is_left_divisible_by(b)
            True
            sage: a.degree() + b.degree() == c.degree() + a.left_gcd(b).degree()
            True

        Specifying ``monic=False``, we *can* get a nonmonic gcd::

            sage: a.right_lcm(b,monic=False)                                            # needs sage.rings.finite_rings
            2*t*x^4 + (3*t + 1)*x^3 + (4*t^2 + 4*t + 3)*x^2
             + (3*t^2 + 4*t + 2)*x + 3*t^2 + 2*t + 3

        The base ring needs to be a field::

            sage: R.<t> = QQ[]
            sage: sigma = R.hom([t+1])
            sage: S.<x> = R['x',sigma]
            sage: a = (x + t) * (x + t^2)
            sage: b = 2 * (x + t) * (x^2 + t + 1)
            sage: a.right_lcm(b)
            Traceback (most recent call last):
            ...
            TypeError: the base ring must be a field

        And the twisting morphism needs to be bijective::

            sage: FR = R.fraction_field()
            sage: f = FR.hom([FR(t)^2])
            sage: S.<x> = FR['x',f]
            sage: a = (x + t) * (x + t^2)
            sage: b = 2 * (x + t) * (x^2 + t + 1)
            sage: a.right_lcm(b)
            Traceback (most recent call last):
            ...
            NotImplementedError: inversion of the twisting morphism Ring endomorphism of
            Fraction Field of Univariate Polynomial Ring in t over Rational Field
                Defn: t |--> t^2"""
    @overload
    def right_lcm(self, b) -> Any:
        """OrePolynomial.right_lcm(self, other, monic=True)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/ore_polynomial_element.pyx (starting at line 1536)

        Return the right lcm of ``self`` and ``other``.

        INPUT:

        - ``other`` -- an Ore polynomial in the same ring as ``self``

        - ``monic`` -- boolean (default: ``True``); return whether the right lcm
          should be normalized to be monic

        OUTPUT:

        The right lcm of ``self`` and ``other``, that is an Ore polynomial
        `l` with the following property: any Ore polynomial is a right multiple of `g` (left divisible by `l`)
        iff it is a right multiple of both ``self`` and ``other`` (left divisible by ``self`` and ``other``).
        If monic is ``True``, `g` is in addition monic. (With this
        extra condition, it is uniquely determined.)

        .. NOTE::

            Works only if two following conditions are fulfilled
            (otherwise right lcm do not exist in general):
            1) the base ring is a field and 2) the twisting morphism on
            this field is bijective.

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: k.<t> = GF(5^3)
            sage: Frob = k.frobenius_endomorphism()
            sage: S.<x> = k['x',Frob]
            sage: a = (x + t) * (x + t^2)
            sage: b = 2 * (x + t) * (x^2 + t + 1)
            sage: c = a.right_lcm(b); c
            x^4 + (2*t^2 + t + 2)*x^3 + (3*t^2 + 4*t + 1)*x^2 + (3*t^2 + 4*t + 1)*x + t^2 + 4
            sage: c.is_left_divisible_by(a)
            True
            sage: c.is_left_divisible_by(b)
            True
            sage: a.degree() + b.degree() == c.degree() + a.left_gcd(b).degree()
            True

        Specifying ``monic=False``, we *can* get a nonmonic gcd::

            sage: a.right_lcm(b,monic=False)                                            # needs sage.rings.finite_rings
            2*t*x^4 + (3*t + 1)*x^3 + (4*t^2 + 4*t + 3)*x^2
             + (3*t^2 + 4*t + 2)*x + 3*t^2 + 2*t + 3

        The base ring needs to be a field::

            sage: R.<t> = QQ[]
            sage: sigma = R.hom([t+1])
            sage: S.<x> = R['x',sigma]
            sage: a = (x + t) * (x + t^2)
            sage: b = 2 * (x + t) * (x^2 + t + 1)
            sage: a.right_lcm(b)
            Traceback (most recent call last):
            ...
            TypeError: the base ring must be a field

        And the twisting morphism needs to be bijective::

            sage: FR = R.fraction_field()
            sage: f = FR.hom([FR(t)^2])
            sage: S.<x> = FR['x',f]
            sage: a = (x + t) * (x + t^2)
            sage: b = 2 * (x + t) * (x^2 + t + 1)
            sage: a.right_lcm(b)
            Traceback (most recent call last):
            ...
            NotImplementedError: inversion of the twisting morphism Ring endomorphism of
            Fraction Field of Univariate Polynomial Ring in t over Rational Field
                Defn: t |--> t^2"""
    @overload
    def right_lcm(self, b) -> Any:
        """OrePolynomial.right_lcm(self, other, monic=True)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/ore_polynomial_element.pyx (starting at line 1536)

        Return the right lcm of ``self`` and ``other``.

        INPUT:

        - ``other`` -- an Ore polynomial in the same ring as ``self``

        - ``monic`` -- boolean (default: ``True``); return whether the right lcm
          should be normalized to be monic

        OUTPUT:

        The right lcm of ``self`` and ``other``, that is an Ore polynomial
        `l` with the following property: any Ore polynomial is a right multiple of `g` (left divisible by `l`)
        iff it is a right multiple of both ``self`` and ``other`` (left divisible by ``self`` and ``other``).
        If monic is ``True``, `g` is in addition monic. (With this
        extra condition, it is uniquely determined.)

        .. NOTE::

            Works only if two following conditions are fulfilled
            (otherwise right lcm do not exist in general):
            1) the base ring is a field and 2) the twisting morphism on
            this field is bijective.

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: k.<t> = GF(5^3)
            sage: Frob = k.frobenius_endomorphism()
            sage: S.<x> = k['x',Frob]
            sage: a = (x + t) * (x + t^2)
            sage: b = 2 * (x + t) * (x^2 + t + 1)
            sage: c = a.right_lcm(b); c
            x^4 + (2*t^2 + t + 2)*x^3 + (3*t^2 + 4*t + 1)*x^2 + (3*t^2 + 4*t + 1)*x + t^2 + 4
            sage: c.is_left_divisible_by(a)
            True
            sage: c.is_left_divisible_by(b)
            True
            sage: a.degree() + b.degree() == c.degree() + a.left_gcd(b).degree()
            True

        Specifying ``monic=False``, we *can* get a nonmonic gcd::

            sage: a.right_lcm(b,monic=False)                                            # needs sage.rings.finite_rings
            2*t*x^4 + (3*t + 1)*x^3 + (4*t^2 + 4*t + 3)*x^2
             + (3*t^2 + 4*t + 2)*x + 3*t^2 + 2*t + 3

        The base ring needs to be a field::

            sage: R.<t> = QQ[]
            sage: sigma = R.hom([t+1])
            sage: S.<x> = R['x',sigma]
            sage: a = (x + t) * (x + t^2)
            sage: b = 2 * (x + t) * (x^2 + t + 1)
            sage: a.right_lcm(b)
            Traceback (most recent call last):
            ...
            TypeError: the base ring must be a field

        And the twisting morphism needs to be bijective::

            sage: FR = R.fraction_field()
            sage: f = FR.hom([FR(t)^2])
            sage: S.<x> = FR['x',f]
            sage: a = (x + t) * (x + t^2)
            sage: b = 2 * (x + t) * (x^2 + t + 1)
            sage: a.right_lcm(b)
            Traceback (most recent call last):
            ...
            NotImplementedError: inversion of the twisting morphism Ring endomorphism of
            Fraction Field of Univariate Polynomial Ring in t over Rational Field
                Defn: t |--> t^2"""
    def right_mod(self, other) -> Any:
        """OrePolynomial.right_mod(self, other)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/ore_polynomial_element.pyx (starting at line 2039)

        Return the remainder of right division of ``self`` by ``other``.

        EXAMPLES::

            sage: R.<t> = QQ[]
            sage: sigma = R.hom([t+1])
            sage: S.<x> = R['x',sigma]
            sage: a = 1 + t*x^2
            sage: b = x + 1
            sage: a % b
            t + 1
            sage: (x^3 + x - 1).right_mod(x^2 - 1)
            2*x - 1"""
    def right_monic(self) -> Any:
        """OrePolynomial.right_monic(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/ore_polynomial_element.pyx (starting at line 533)

        Return the unique monic Ore polynomial which divides this polynomial
        on the right and has the same degree.

        Given an Ore polynomial `P` of degree `n`, its right monic is given by
        `(1/k) \\cdot P`, where `k` is the leading coefficient of `P`.

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: k.<t> = GF(5^3)
            sage: Frob = k.frobenius_endomorphism()
            sage: S.<x> = k['x',Frob]
            sage: a = (3*t^2 + 3*t + 2)*x^3 + (2*t^2 + 3)*x^2 + (4*t^2 + t + 4)*x + 2*t^2 + 2
            sage: b = a.right_monic(); b
            x^3 + (2*t^2 + 3*t + 4)*x^2 + (3*t^2 + 4*t + 1)*x + 2*t^2 + 4*t + 3

        Check list::

            sage: b.degree() == a.degree()                                              # needs sage.rings.finite_rings
            True
            sage: a.is_right_divisible_by(b)                                            # needs sage.rings.finite_rings
            True
            sage: a == a.leading_coefficient() * b                                      # needs sage.rings.finite_rings
            True

        Note that `b` does not divide `a` on the right::

            sage: a.is_left_divisible_by(b)                                             # needs sage.rings.finite_rings
            False

        This function does not work if the leading coefficient is not a
        unit::

            sage: R.<t> = QQ[]
            sage: der = R.derivation()
            sage: S.<x> = R['x', der]
            sage: a = t*x
            sage: a.right_monic()
            Traceback (most recent call last):
            ...
            NotImplementedError: the leading coefficient is not a unit"""
    @overload
    def right_quo_rem(self, other) -> Any:
        """OrePolynomial.right_quo_rem(self, other)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/ore_polynomial_element.pyx (starting at line 1004)

        Return the quotient and remainder of the right Euclidean
        division of ``self`` by ``other``.

        INPUT:

        - ``other`` -- an Ore polynomial in the same ring as ``self``

        OUTPUT:

        - the quotient and the remainder of the right Euclidean
          division of this Ore polynomial by ``other``

        .. NOTE::

            This will fail if the leading coefficient of the divisor
            is not a unit.

        EXAMPLES::

            sage: R.<t> = ZZ[]
            sage: sigma = R.hom([t+1])
            sage: S.<x> = R['x',sigma]
            sage: a = S.random_element(degree=4)
            sage: b = S.random_element(monic=True)
            sage: q,r = a.right_quo_rem(b)
            sage: a == q*b + r
            True

        The leading coefficient of the divisor need to be invertible::

            sage: a.right_quo_rem(S(0))
            Traceback (most recent call last):
            ...
            ZeroDivisionError: division by zero is not valid
            sage: c = S.random_element()
            sage: while not c or c.leading_coefficient().is_unit():
            ....:     c = S.random_element()
            sage: while a.degree() < c.degree():
            ....:     a = S.random_element(degree=4)
            sage: a.right_quo_rem(c)
            Traceback (most recent call last):
            ...
            NotImplementedError: the leading coefficient of the divisor is not invertible"""
    @overload
    def right_quo_rem(self, b) -> Any:
        """OrePolynomial.right_quo_rem(self, other)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/ore_polynomial_element.pyx (starting at line 1004)

        Return the quotient and remainder of the right Euclidean
        division of ``self`` by ``other``.

        INPUT:

        - ``other`` -- an Ore polynomial in the same ring as ``self``

        OUTPUT:

        - the quotient and the remainder of the right Euclidean
          division of this Ore polynomial by ``other``

        .. NOTE::

            This will fail if the leading coefficient of the divisor
            is not a unit.

        EXAMPLES::

            sage: R.<t> = ZZ[]
            sage: sigma = R.hom([t+1])
            sage: S.<x> = R['x',sigma]
            sage: a = S.random_element(degree=4)
            sage: b = S.random_element(monic=True)
            sage: q,r = a.right_quo_rem(b)
            sage: a == q*b + r
            True

        The leading coefficient of the divisor need to be invertible::

            sage: a.right_quo_rem(S(0))
            Traceback (most recent call last):
            ...
            ZeroDivisionError: division by zero is not valid
            sage: c = S.random_element()
            sage: while not c or c.leading_coefficient().is_unit():
            ....:     c = S.random_element()
            sage: while a.degree() < c.degree():
            ....:     a = S.random_element(degree=4)
            sage: a.right_quo_rem(c)
            Traceback (most recent call last):
            ...
            NotImplementedError: the leading coefficient of the divisor is not invertible"""
    @overload
    def right_quo_rem(self, c) -> Any:
        """OrePolynomial.right_quo_rem(self, other)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/ore_polynomial_element.pyx (starting at line 1004)

        Return the quotient and remainder of the right Euclidean
        division of ``self`` by ``other``.

        INPUT:

        - ``other`` -- an Ore polynomial in the same ring as ``self``

        OUTPUT:

        - the quotient and the remainder of the right Euclidean
          division of this Ore polynomial by ``other``

        .. NOTE::

            This will fail if the leading coefficient of the divisor
            is not a unit.

        EXAMPLES::

            sage: R.<t> = ZZ[]
            sage: sigma = R.hom([t+1])
            sage: S.<x> = R['x',sigma]
            sage: a = S.random_element(degree=4)
            sage: b = S.random_element(monic=True)
            sage: q,r = a.right_quo_rem(b)
            sage: a == q*b + r
            True

        The leading coefficient of the divisor need to be invertible::

            sage: a.right_quo_rem(S(0))
            Traceback (most recent call last):
            ...
            ZeroDivisionError: division by zero is not valid
            sage: c = S.random_element()
            sage: while not c or c.leading_coefficient().is_unit():
            ....:     c = S.random_element()
            sage: while a.degree() < c.degree():
            ....:     a = S.random_element(degree=4)
            sage: a.right_quo_rem(c)
            Traceback (most recent call last):
            ...
            NotImplementedError: the leading coefficient of the divisor is not invertible"""
    def right_xgcd(self, other, monic=...) -> Any:
        """OrePolynomial.right_xgcd(self, other, monic=True)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/ore_polynomial_element.pyx (starting at line 1055)

        Return the right gcd of ``self`` and ``other`` along with the
        coefficients for the linear combination.

        If `a` is ``self`` and `b` is ``other``, then there are Ore polynomials
        `u` and `v` such that `g = u a + v b`, where `g` is the right gcd of `a`
        and `b`. This method returns `(g, u, v)`.

        INPUT:

        - ``other`` -- an Ore polynomial in the same ring as ``self``

        - ``monic`` -- boolean (default: ``True``); return whether the right gcd
          should be normalized to be monic

        OUTPUT:

        - The right gcd of ``self`` and ``other``, that is an Ore polynomial
          `g` with the following property: any Ore polynomial is
          divisible on the right by `g` iff it is divisible on the right
          by both ``self`` and ``other``.
          If monic is ``True``, `g` is in addition monic. (With this
          extra condition, it is uniquely determined.)

        - Two Ore polynomials `u` and `v` such that:

          .. MATH::

              g = u \\cdot a + v \\cdot b

          where `a` is ``self`` and `b` is ``other``.

        .. NOTE::

            Works only if the base ring is a field (otherwise right
            gcd do not exist in general).

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: k.<t> = GF(5^3)
            sage: Frob = k.frobenius_endomorphism()
            sage: S.<x> = k['x',Frob]
            sage: a = (x^2 + t*x + 1) * (x + t)
            sage: b = 2 * (x^3 + (t+1)*x^2 + t^2) * (x + t)
            sage: g,u,v = a.right_xgcd(b); g
            x + t
            sage: u*a + v*b == g
            True

        Specifying ``monic=False``, we *can* get a nonmonic gcd::

            sage: g,u,v = a.right_xgcd(b, monic=False); g                               # needs sage.rings.finite_rings
            (4*t^2 + 4*t + 1)*x + 4*t^2 + 4*t + 3
            sage: u*a + v*b == g                                                        # needs sage.rings.finite_rings
            True

        The base ring must be a field::

            sage: R.<t> = QQ[]
            sage: sigma = R.hom([t+1])
            sage: S.<x> = R['x',sigma]
            sage: a = (x^2 + t*x + 1) * (x + t)
            sage: b = 2 * (x^3 + (t+1)*x^2 + t^2) * (x + t)
            sage: a.right_xgcd(b)
            Traceback (most recent call last):
            ...
            TypeError: the base ring must be a field"""
    def right_xlcm(self, other, monic=...) -> Any:
        """OrePolynomial.right_xlcm(self, other, monic=True)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/ore_polynomial_element.pyx (starting at line 1421)

        Return the right lcm `L` of ``self`` and ``other`` together
        with two Ore polynomials `U` and `V` such that

        .. MATH::

            \\text{self} \\cdot U = \\text{other} \\cdot V = L.

        INPUT:

        - ``other`` -- an Ore polynomial in the same ring as ``self``

        - ``monic`` -- boolean (default: ``True``); whether the right lcm
          should be normalized to be monic

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: k.<t> = GF(5^3)
            sage: Frob = k.frobenius_endomorphism()
            sage: S.<x> = k['x',Frob]
            sage: P = (x + t) * (x + t^2)
            sage: Q = 2 * (x + t) * (x^2 + t + 1)
            sage: L, U, V = P.right_xlcm(Q)
            sage: L
            x^4 + (2*t^2 + t + 2)*x^3 + (3*t^2 + 4*t + 1)*x^2 + (3*t^2 + 4*t + 1)*x + t^2 + 4
            sage: P * U == L
            True
            sage: Q * V == L
            True"""
    def shift(self, n) -> Any:
        """OrePolynomial.shift(self, n)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/ore_polynomial_element.pyx (starting at line 1775)

        Return ``self`` multiplied on the right by the power `x^n`.

        If `n` is negative, terms below `x^n` will be discarded.

        EXAMPLES::

            sage: R.<t> = QQ[]
            sage: sigma = R.hom([t+1])
            sage: S.<x> = R['x',sigma]
            sage: a = x^5 + t^4*x^4 + t^2*x^2 + t^10
            sage: a.shift(0)
            x^5 + t^4*x^4 + t^2*x^2 + t^10
            sage: a.shift(-1)
            x^4 + t^4*x^3 + t^2*x
            sage: a.shift(-5)
            1
            sage: a.shift(2)
            x^7 + t^4*x^6 + t^2*x^4 + t^10*x^2

        One can also use the infix shift operator::

            sage: a >> 2
            x^3 + t^4*x^2 + t^2
            sage: a << 2
            x^7 + t^4*x^6 + t^2*x^4 + t^10*x^2"""
    @overload
    def square(self) -> Any:
        """OrePolynomial.square(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/ore_polynomial_element.pyx (starting at line 327)

        Return the square of ``self``.

        EXAMPLES::

            sage: R.<t> = QQ[]
            sage: sigma = R.hom([t+1])
            sage: S.<x> = R['x', sigma]
            sage: a = x + t; a
            x + t
            sage: a.square()
            x^2 + (2*t + 1)*x + t^2
            sage: a.square() == a*a
            True

            sage: der = R.derivation()
            sage: A.<d> = R['d', der]
            sage: (d + t).square()
            d^2 + 2*t*d + t^2 + 1"""
    @overload
    def square(self) -> Any:
        """OrePolynomial.square(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/ore_polynomial_element.pyx (starting at line 327)

        Return the square of ``self``.

        EXAMPLES::

            sage: R.<t> = QQ[]
            sage: sigma = R.hom([t+1])
            sage: S.<x> = R['x', sigma]
            sage: a = x + t; a
            x + t
            sage: a.square()
            x^2 + (2*t + 1)*x + t^2
            sage: a.square() == a*a
            True

            sage: der = R.derivation()
            sage: A.<d> = R['d', der]
            sage: (d + t).square()
            d^2 + 2*t*d + t^2 + 1"""
    @overload
    def square(self) -> Any:
        """OrePolynomial.square(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/ore_polynomial_element.pyx (starting at line 327)

        Return the square of ``self``.

        EXAMPLES::

            sage: R.<t> = QQ[]
            sage: sigma = R.hom([t+1])
            sage: S.<x> = R['x', sigma]
            sage: a = x + t; a
            x + t
            sage: a.square()
            x^2 + (2*t + 1)*x + t^2
            sage: a.square() == a*a
            True

            sage: der = R.derivation()
            sage: A.<d> = R['d', der]
            sage: (d + t).square()
            d^2 + 2*t*d + t^2 + 1"""
    @overload
    def square(self) -> Any:
        """OrePolynomial.square(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/ore_polynomial_element.pyx (starting at line 327)

        Return the square of ``self``.

        EXAMPLES::

            sage: R.<t> = QQ[]
            sage: sigma = R.hom([t+1])
            sage: S.<x> = R['x', sigma]
            sage: a = x + t; a
            x + t
            sage: a.square()
            x^2 + (2*t + 1)*x + t^2
            sage: a.square() == a*a
            True

            sage: der = R.derivation()
            sage: A.<d> = R['d', der]
            sage: (d + t).square()
            d^2 + 2*t*d + t^2 + 1"""
    @overload
    def variable_name(self) -> Any:
        """OrePolynomial.variable_name(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/ore_polynomial_element.pyx (starting at line 2169)

        Return the string name of the variable used in ``self``.

        EXAMPLES::

            sage: R.<t> = QQ[]
            sage: sigma = R.hom([t+1])
            sage: S.<x> = R['x',sigma]
            sage: a = x + t
            sage: a.variable_name()
            'x'"""
    @overload
    def variable_name(self) -> Any:
        """OrePolynomial.variable_name(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/ore_polynomial_element.pyx (starting at line 2169)

        Return the string name of the variable used in ``self``.

        EXAMPLES::

            sage: R.<t> = QQ[]
            sage: sigma = R.hom([t+1])
            sage: S.<x> = R['x',sigma]
            sage: a = x + t
            sage: a.variable_name()
            'x'"""
    def __bool__(self) -> bool:
        """True if self else False"""
    def __copy__(self) -> Any:
        '''OrePolynomial.__copy__(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/ore_polynomial_element.pyx (starting at line 1986)

        Return a "copy" of ``self``.

        In Sage, since Ore polynomials are immutable, this just returns
        ``self`` again.

        EXAMPLES::

            sage: R.<t> = QQ[]
            sage: sigma = R.hom([t+1])
            sage: S.<x> = R[\'x\',sigma]
            sage: a = 1 + x^4 + (t+1)*x^2 + t^2
            sage: b = copy(a)
            sage: b is a
            True'''
    def __delitem__(self, other) -> None:
        """Delete self[key]."""
    def __hash__(self) -> Any:
        """OrePolynomial.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/ore_polynomial_element.pyx (starting at line 239)

        Return hash of ``self``.

        EXAMPLES::

            sage: R.<t> = QQ[]
            sage: sigma = R.hom([t+1])
            sage: S.<x> = R['x',sigma]
            sage: a = 1 + x^4 + (t+1)*x^2 + t^2
            sage: hash(a) == hash(a)
            True"""
    def __lshift__(self, k) -> Any:
        """OrePolynomial.__lshift__(self, k)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/ore_polynomial_element.pyx (starting at line 1813)

        Return ``self`` multiplied on the right by the power `x^k`.

        EXAMPLES::

            sage: R.<t> = QQ[]
            sage: sigma = R.hom([t+1])
            sage: S.<x> = R['x',sigma]
            sage: a = x^5 + t^4*x^4 + t^2*x^2 + t^10
            sage: a << 2
            x^7 + t^4*x^6 + t^2*x^4 + t^10*x^2"""
    def __rlshift__(self, other):
        """Return value<<self."""
    def __rrshift__(self, other):
        """Return value>>self."""
    def __rshift__(self, k) -> Any:
        """OrePolynomial.__rshift__(self, k)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/ore_polynomial_element.pyx (starting at line 1828)

        Return ``self`` multiplied on the right by the power `x^(-k)`.

        If `n` is negative, terms below `x^n` will be discarded.

        EXAMPLES::

            sage: R.<t> = QQ[]
            sage: sigma = R.hom([t+1])
            sage: S.<x> = R['x',sigma]
            sage: a = x^5 + t^4*x^4 + t^2*x^2 + t^10
            sage: a >> 2
            x^3 + t^4*x^2 + t^2"""
    def __setitem__(self, n, value) -> Any:
        """OrePolynomial.__setitem__(self, n, value)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/ore_polynomial_element.pyx (starting at line 306)

        Set the ``n``-th coefficient of ``self``.

        This always raises an :exc:`IndexError`, since polynomials are immutable in
        Sage.

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: k.<t> = GF(5^3)
            sage: Frob = k.frobenius_endomorphism()
            sage: S.<x> = k['x',Frob]
            sage: a = x + t
            sage: a[1] = t + 1
            Traceback (most recent call last):
            ...
            IndexError: Ore polynomials are immutable"""

class OrePolynomialBaseringInjection(sage.categories.morphism.Morphism):
    """OrePolynomialBaseringInjection(domain, codomain)

    File: /build/sagemath/src/sage/src/sage/rings/polynomial/ore_polynomial_element.pyx (starting at line 3021)

    Representation of the canonical homomorphism from a ring `R` into an Ore
    polynomial ring over `R`.

    This class is necessary for automatic coercion from the base ring to the Ore
    polynomial ring.

    .. SEEALSO::

        :class:`~sage.rings.polynomial.polynomial_element.PolynomialBaseringInjection`

    EXAMPLES::

        sage: R.<t> = QQ[]
        sage: sigma = R.hom([t+1])
        sage: S.<x> = R['x',sigma]
        sage: S.coerce_map_from(S.base_ring()) #indirect doctest
        Ore Polynomial base injection morphism:
          From: Univariate Polynomial Ring in t over Rational Field
          To:   Ore Polynomial Ring in x over Univariate Polynomial Ring in t
                over Rational Field twisted by t |--> t + 1"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, domain, codomain) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/polynomial/ore_polynomial_element.pyx (starting at line 3044)

                Construct a Skew Polynomial Basering Injection.

                INPUT:

                - ``domain`` -- a ring `R`; this will be the domain of the injection

                - ``codomain`` -- an Ore polynomial ring over ``domain``; this will be
                  the codomain

                TESTS::

                    sage: # needs sage.rings.finite_rings
                    sage: from sage.rings.polynomial.ore_polynomial_element import OrePolynomialBaseringInjection
                    sage: k.<t> = GF(5^3)
                    sage: Frob = k.frobenius_endomorphism()
                    sage: S.<x> = k['x',Frob]
                    sage: OrePolynomialBaseringInjection(k, k['x', Frob])
                    Ore Polynomial base injection morphism:
                      From: Finite Field in t of size 5^3
                      To:   Ore Polynomial Ring in x over Finite Field in t of size 5^3 twisted by t |--> t^5
                    sage: R.<t> = QQ[]
                    sage: OrePolynomialBaseringInjection(QQ, k['x', Frob])
                    Traceback (most recent call last):
                    ...
                    AssertionError: the domain of the injection must be the base ring of the Ore polynomial ring
        """
    @overload
    def an_element(self) -> Any:
        """OrePolynomialBaseringInjection.an_element(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/ore_polynomial_element.pyx (starting at line 3079)

        Return an element of the codomain of the ring homomorphism.

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: from sage.rings.polynomial.ore_polynomial_element import OrePolynomialBaseringInjection
            sage: k.<t> = GF(5^3)
            sage: Frob = k.frobenius_endomorphism()
            sage: S.<x> = k['x',Frob]
            sage: m = OrePolynomialBaseringInjection(k, k['x', Frob])
            sage: m.an_element()
            x"""
    @overload
    def an_element(self) -> Any:
        """OrePolynomialBaseringInjection.an_element(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/ore_polynomial_element.pyx (starting at line 3079)

        Return an element of the codomain of the ring homomorphism.

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: from sage.rings.polynomial.ore_polynomial_element import OrePolynomialBaseringInjection
            sage: k.<t> = GF(5^3)
            sage: Frob = k.frobenius_endomorphism()
            sage: S.<x> = k['x',Frob]
            sage: m = OrePolynomialBaseringInjection(k, k['x', Frob])
            sage: m.an_element()
            x"""
    @overload
    def section(self) -> Any:
        """OrePolynomialBaseringInjection.section(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/ore_polynomial_element.pyx (starting at line 3125)

        Return the canonical homomorphism from the constants of an Ore
        polynomial ring to the base ring according to ``self``.

        TESTS::

            sage: # needs sage.rings.finite_rings
            sage: from sage.rings.polynomial.ore_polynomial_element import OrePolynomialBaseringInjection
            sage: k.<t> = GF(5^3)
            sage: Frob = k.frobenius_endomorphism()
            sage: S.<x> = k['x',Frob]
            sage: m = OrePolynomialBaseringInjection(k, k['x', Frob])
            sage: m.section()
            Generic map:
              From: Ore Polynomial Ring in x over Finite Field in t of size 5^3
                    twisted by t |--> t^5
              To:   Finite Field in t of size 5^3"""
    @overload
    def section(self) -> Any:
        """OrePolynomialBaseringInjection.section(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/ore_polynomial_element.pyx (starting at line 3125)

        Return the canonical homomorphism from the constants of an Ore
        polynomial ring to the base ring according to ``self``.

        TESTS::

            sage: # needs sage.rings.finite_rings
            sage: from sage.rings.polynomial.ore_polynomial_element import OrePolynomialBaseringInjection
            sage: k.<t> = GF(5^3)
            sage: Frob = k.frobenius_endomorphism()
            sage: S.<x> = k['x',Frob]
            sage: m = OrePolynomialBaseringInjection(k, k['x', Frob])
            sage: m.section()
            Generic map:
              From: Ore Polynomial Ring in x over Finite Field in t of size 5^3
                    twisted by t |--> t^5
              To:   Finite Field in t of size 5^3"""

class OrePolynomial_generic_dense(OrePolynomial):
    """OrePolynomial_generic_dense(parent, x=None, int check=1, int construct=0, **kwds)

    File: /build/sagemath/src/sage/src/sage/rings/polynomial/ore_polynomial_element.pyx (starting at line 2212)

    Generic implementation of dense Ore polynomial supporting any valid base
    ring, twisting morphism and twisting derivation."""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, parent, x=..., intcheck=..., intconstruct=..., **kwds) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/polynomial/ore_polynomial_element.pyx (starting at line 2217)

                Construct an Ore polynomial over the given parent with the given
                coefficients.

                INPUT:

                - ``parent`` -- parent of ``self``

                - ``x`` -- list of coefficients from which ``self`` can be constructed

                - ``check`` -- flag variable to normalize the polynomial

                - ``construct`` -- boolean (default: ``False``)

                TESTS::

                    sage: R.<t> = QQ[]
                    sage: sigma = R.hom([t+1])
                    sage: S.<x> = R['x',sigma]

                We create an Ore polynomial from a list::

                    sage: S([t,1])
                    x + t

                from another Ore polynomial::

                    sage: S(x^2 + t)
                    x^2 + t

                from a constant::

                    sage: x = S(t^2 + 1); x
                    t^2 + 1
                    sage: x.parent() is S
                    True
        """
    @overload
    def coefficients(self, sparse=...) -> list:
        """OrePolynomial_generic_dense.coefficients(self, sparse=True) -> list

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/ore_polynomial_element.pyx (starting at line 2852)

        Return the coefficients of the monomials appearing in ``self``.

        If ``sparse=True`` (the default), return only the nonzero coefficients.
        Otherwise, return the same value as ``self.list()``.

        EXAMPLES::

            sage: R.<t> = QQ[]
            sage: sigma = R.hom([t+1])
            sage: S.<x> = R['x',sigma]
            sage: a = 1 + x^4 + (t+1)*x^2 + t^2
            sage: a.coefficients()
            [t^2 + 1, t + 1, 1]
            sage: a.coefficients(sparse=False)
            [t^2 + 1, 0, t + 1, 0, 1]"""
    @overload
    def coefficients(self) -> Any:
        """OrePolynomial_generic_dense.coefficients(self, sparse=True) -> list

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/ore_polynomial_element.pyx (starting at line 2852)

        Return the coefficients of the monomials appearing in ``self``.

        If ``sparse=True`` (the default), return only the nonzero coefficients.
        Otherwise, return the same value as ``self.list()``.

        EXAMPLES::

            sage: R.<t> = QQ[]
            sage: sigma = R.hom([t+1])
            sage: S.<x> = R['x',sigma]
            sage: a = 1 + x^4 + (t+1)*x^2 + t^2
            sage: a.coefficients()
            [t^2 + 1, t + 1, 1]
            sage: a.coefficients(sparse=False)
            [t^2 + 1, 0, t + 1, 0, 1]"""
    @overload
    def coefficients(self, sparse=...) -> Any:
        """OrePolynomial_generic_dense.coefficients(self, sparse=True) -> list

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/ore_polynomial_element.pyx (starting at line 2852)

        Return the coefficients of the monomials appearing in ``self``.

        If ``sparse=True`` (the default), return only the nonzero coefficients.
        Otherwise, return the same value as ``self.list()``.

        EXAMPLES::

            sage: R.<t> = QQ[]
            sage: sigma = R.hom([t+1])
            sage: S.<x> = R['x',sigma]
            sage: a = 1 + x^4 + (t+1)*x^2 + t^2
            sage: a.coefficients()
            [t^2 + 1, t + 1, 1]
            sage: a.coefficients(sparse=False)
            [t^2 + 1, 0, t + 1, 0, 1]"""
    @overload
    def degree(self) -> Integer:
        """OrePolynomial_generic_dense.degree(self) -> Integer

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/ore_polynomial_element.pyx (starting at line 2513)

        Return the degree of ``self``.

        By convention, the zero Ore polynomial has degree `-1`.

        EXAMPLES::

            sage: R.<t> = ZZ[]
            sage: sigma = R.hom([t+1])
            sage: S.<x> = R['x',sigma]
            sage: a = x^2 + t*x^3 + t^2*x + 1
            sage: a.degree()
            3

        By convention, the degree of `0` is `-1`::

            sage: S(0).degree()
            -1

        TESTS:

        We check that the degree is an ``Integer`` object (see #35519)::

            sage: R.<t> = ZZ[]
            sage: sigma = R.hom([t+1])
            sage: S.<x> = R['x',sigma]
            sage: a = x^2 + t*x^3 + t^2*x + 1
            sage: isinstance(a.degree(), Integer)
            True

        ::

            sage: R.<t> = OrePolynomialRing(GF(5)['T'], GF(5)['T'].frobenius_endomorphism())
            sage: isinstance((t + 1).degree(), Integer)
            True"""
    @overload
    def degree(self) -> Any:
        """OrePolynomial_generic_dense.degree(self) -> Integer

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/ore_polynomial_element.pyx (starting at line 2513)

        Return the degree of ``self``.

        By convention, the zero Ore polynomial has degree `-1`.

        EXAMPLES::

            sage: R.<t> = ZZ[]
            sage: sigma = R.hom([t+1])
            sage: S.<x> = R['x',sigma]
            sage: a = x^2 + t*x^3 + t^2*x + 1
            sage: a.degree()
            3

        By convention, the degree of `0` is `-1`::

            sage: S(0).degree()
            -1

        TESTS:

        We check that the degree is an ``Integer`` object (see #35519)::

            sage: R.<t> = ZZ[]
            sage: sigma = R.hom([t+1])
            sage: S.<x> = R['x',sigma]
            sage: a = x^2 + t*x^3 + t^2*x + 1
            sage: isinstance(a.degree(), Integer)
            True

        ::

            sage: R.<t> = OrePolynomialRing(GF(5)['T'], GF(5)['T'].frobenius_endomorphism())
            sage: isinstance((t + 1).degree(), Integer)
            True"""
    @overload
    def degree(self) -> Any:
        """OrePolynomial_generic_dense.degree(self) -> Integer

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/ore_polynomial_element.pyx (starting at line 2513)

        Return the degree of ``self``.

        By convention, the zero Ore polynomial has degree `-1`.

        EXAMPLES::

            sage: R.<t> = ZZ[]
            sage: sigma = R.hom([t+1])
            sage: S.<x> = R['x',sigma]
            sage: a = x^2 + t*x^3 + t^2*x + 1
            sage: a.degree()
            3

        By convention, the degree of `0` is `-1`::

            sage: S(0).degree()
            -1

        TESTS:

        We check that the degree is an ``Integer`` object (see #35519)::

            sage: R.<t> = ZZ[]
            sage: sigma = R.hom([t+1])
            sage: S.<x> = R['x',sigma]
            sage: a = x^2 + t*x^3 + t^2*x + 1
            sage: isinstance(a.degree(), Integer)
            True

        ::

            sage: R.<t> = OrePolynomialRing(GF(5)['T'], GF(5)['T'].frobenius_endomorphism())
            sage: isinstance((t + 1).degree(), Integer)
            True"""
    def dict(self) -> Any:
        """OrePolynomial_generic_dense.monomial_coefficients(self) -> dict

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/ore_polynomial_element.pyx (starting at line 2484)

        Return a dictionary representation of ``self``.

        EXAMPLES::

            sage: R.<t> = ZZ[]
            sage: sigma = R.hom([t+1])
            sage: S.<x> = R['x',sigma]
            sage: a = x^2012 + t*x^1006 + t^3 + 2*t
            sage: a.monomial_coefficients()
            {0: t^3 + 2*t, 1006: t, 2012: 1}

        ``dict`` is an alias::

            sage: a.dict()
            {0: t^3 + 2*t, 1006: t, 2012: 1}"""
    @overload
    def hilbert_shift(self, s, var=...) -> Any:
        """OrePolynomial_generic_dense.hilbert_shift(self, s, var=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/ore_polynomial_element.pyx (starting at line 2875)

        Return this Ore polynomial with variable shifted by `s`.

        If this Ore polynomial is `P(x)`, this returns `P(x+s)`.

        INPUT:

        - ``s`` -- an element in the base ring

        - ``var`` -- string; the variable name

        EXAMPLES::

            sage: R.<t> = GF(7)[]
            sage: der = R.derivation()
            sage: A.<d> = R['d', der]

            sage: L = d^3 + t*d^2
            sage: L.hilbert_shift(t)
            d^3 + 4*t*d^2 + (5*t^2 + 3)*d + 2*t^3 + 4*t
            sage: (d+t)^3 + t*(d+t)^2
            d^3 + 4*t*d^2 + (5*t^2 + 3)*d + 2*t^3 + 4*t

        One can specify another variable name::

            sage: L.hilbert_shift(t, var='x')
            x^3 + 4*t*x^2 + (5*t^2 + 3)*x + 2*t^3 + 4*t

        When the twisting morphism is not trivial, the output lies
        in a different Ore polynomial ring::

            sage: # needs sage.rings.finite_rings
            sage: k.<a> = GF(5^3)
            sage: Frob = k.frobenius_endomorphism()
            sage: S.<x> = k['x', Frob]
            sage: P = x^2 + a*x + a^2
            sage: Q = P.hilbert_shift(a); Q
            x^2 + (2*a^2 + a + 4)*x + a^2 + 3*a + 4
            sage: Q.parent()
            Ore Polynomial Ring in x over
             Finite Field in a of size 5^3 twisted by a |--> a^5 and a*([a |--> a^5] - id)
            sage: Q.parent() is S
            False

        This behavior ensures that the Hilbert shift by a fixed element
        defines a homomorphism of rings::

            sage: # needs sage.rings.finite_rings
            sage: U = S.random_element(degree=5)
            sage: V = S.random_element(degree=5)
            sage: s = k.random_element()
            sage: (U+V).hilbert_shift(s) == U.hilbert_shift(s) + V.hilbert_shift(s)
            True
            sage: (U*V).hilbert_shift(s) == U.hilbert_shift(s) * V.hilbert_shift(s)
            True

        We check that shifting by an element and then by its opposite
        gives back the initial Ore polynomial::

            sage: # needs sage.rings.finite_rings
            sage: P = S.random_element(degree=10)
            sage: s = k.random_element()
            sage: P.hilbert_shift(s).hilbert_shift(-s) == P
            True"""
    @overload
    def hilbert_shift(self, t) -> Any:
        """OrePolynomial_generic_dense.hilbert_shift(self, s, var=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/ore_polynomial_element.pyx (starting at line 2875)

        Return this Ore polynomial with variable shifted by `s`.

        If this Ore polynomial is `P(x)`, this returns `P(x+s)`.

        INPUT:

        - ``s`` -- an element in the base ring

        - ``var`` -- string; the variable name

        EXAMPLES::

            sage: R.<t> = GF(7)[]
            sage: der = R.derivation()
            sage: A.<d> = R['d', der]

            sage: L = d^3 + t*d^2
            sage: L.hilbert_shift(t)
            d^3 + 4*t*d^2 + (5*t^2 + 3)*d + 2*t^3 + 4*t
            sage: (d+t)^3 + t*(d+t)^2
            d^3 + 4*t*d^2 + (5*t^2 + 3)*d + 2*t^3 + 4*t

        One can specify another variable name::

            sage: L.hilbert_shift(t, var='x')
            x^3 + 4*t*x^2 + (5*t^2 + 3)*x + 2*t^3 + 4*t

        When the twisting morphism is not trivial, the output lies
        in a different Ore polynomial ring::

            sage: # needs sage.rings.finite_rings
            sage: k.<a> = GF(5^3)
            sage: Frob = k.frobenius_endomorphism()
            sage: S.<x> = k['x', Frob]
            sage: P = x^2 + a*x + a^2
            sage: Q = P.hilbert_shift(a); Q
            x^2 + (2*a^2 + a + 4)*x + a^2 + 3*a + 4
            sage: Q.parent()
            Ore Polynomial Ring in x over
             Finite Field in a of size 5^3 twisted by a |--> a^5 and a*([a |--> a^5] - id)
            sage: Q.parent() is S
            False

        This behavior ensures that the Hilbert shift by a fixed element
        defines a homomorphism of rings::

            sage: # needs sage.rings.finite_rings
            sage: U = S.random_element(degree=5)
            sage: V = S.random_element(degree=5)
            sage: s = k.random_element()
            sage: (U+V).hilbert_shift(s) == U.hilbert_shift(s) + V.hilbert_shift(s)
            True
            sage: (U*V).hilbert_shift(s) == U.hilbert_shift(s) * V.hilbert_shift(s)
            True

        We check that shifting by an element and then by its opposite
        gives back the initial Ore polynomial::

            sage: # needs sage.rings.finite_rings
            sage: P = S.random_element(degree=10)
            sage: s = k.random_element()
            sage: P.hilbert_shift(s).hilbert_shift(-s) == P
            True"""
    @overload
    def hilbert_shift(self, t, var=...) -> Any:
        """OrePolynomial_generic_dense.hilbert_shift(self, s, var=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/ore_polynomial_element.pyx (starting at line 2875)

        Return this Ore polynomial with variable shifted by `s`.

        If this Ore polynomial is `P(x)`, this returns `P(x+s)`.

        INPUT:

        - ``s`` -- an element in the base ring

        - ``var`` -- string; the variable name

        EXAMPLES::

            sage: R.<t> = GF(7)[]
            sage: der = R.derivation()
            sage: A.<d> = R['d', der]

            sage: L = d^3 + t*d^2
            sage: L.hilbert_shift(t)
            d^3 + 4*t*d^2 + (5*t^2 + 3)*d + 2*t^3 + 4*t
            sage: (d+t)^3 + t*(d+t)^2
            d^3 + 4*t*d^2 + (5*t^2 + 3)*d + 2*t^3 + 4*t

        One can specify another variable name::

            sage: L.hilbert_shift(t, var='x')
            x^3 + 4*t*x^2 + (5*t^2 + 3)*x + 2*t^3 + 4*t

        When the twisting morphism is not trivial, the output lies
        in a different Ore polynomial ring::

            sage: # needs sage.rings.finite_rings
            sage: k.<a> = GF(5^3)
            sage: Frob = k.frobenius_endomorphism()
            sage: S.<x> = k['x', Frob]
            sage: P = x^2 + a*x + a^2
            sage: Q = P.hilbert_shift(a); Q
            x^2 + (2*a^2 + a + 4)*x + a^2 + 3*a + 4
            sage: Q.parent()
            Ore Polynomial Ring in x over
             Finite Field in a of size 5^3 twisted by a |--> a^5 and a*([a |--> a^5] - id)
            sage: Q.parent() is S
            False

        This behavior ensures that the Hilbert shift by a fixed element
        defines a homomorphism of rings::

            sage: # needs sage.rings.finite_rings
            sage: U = S.random_element(degree=5)
            sage: V = S.random_element(degree=5)
            sage: s = k.random_element()
            sage: (U+V).hilbert_shift(s) == U.hilbert_shift(s) + V.hilbert_shift(s)
            True
            sage: (U*V).hilbert_shift(s) == U.hilbert_shift(s) * V.hilbert_shift(s)
            True

        We check that shifting by an element and then by its opposite
        gives back the initial Ore polynomial::

            sage: # needs sage.rings.finite_rings
            sage: P = S.random_element(degree=10)
            sage: s = k.random_element()
            sage: P.hilbert_shift(s).hilbert_shift(-s) == P
            True"""
    @overload
    def hilbert_shift(self, a) -> Any:
        """OrePolynomial_generic_dense.hilbert_shift(self, s, var=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/ore_polynomial_element.pyx (starting at line 2875)

        Return this Ore polynomial with variable shifted by `s`.

        If this Ore polynomial is `P(x)`, this returns `P(x+s)`.

        INPUT:

        - ``s`` -- an element in the base ring

        - ``var`` -- string; the variable name

        EXAMPLES::

            sage: R.<t> = GF(7)[]
            sage: der = R.derivation()
            sage: A.<d> = R['d', der]

            sage: L = d^3 + t*d^2
            sage: L.hilbert_shift(t)
            d^3 + 4*t*d^2 + (5*t^2 + 3)*d + 2*t^3 + 4*t
            sage: (d+t)^3 + t*(d+t)^2
            d^3 + 4*t*d^2 + (5*t^2 + 3)*d + 2*t^3 + 4*t

        One can specify another variable name::

            sage: L.hilbert_shift(t, var='x')
            x^3 + 4*t*x^2 + (5*t^2 + 3)*x + 2*t^3 + 4*t

        When the twisting morphism is not trivial, the output lies
        in a different Ore polynomial ring::

            sage: # needs sage.rings.finite_rings
            sage: k.<a> = GF(5^3)
            sage: Frob = k.frobenius_endomorphism()
            sage: S.<x> = k['x', Frob]
            sage: P = x^2 + a*x + a^2
            sage: Q = P.hilbert_shift(a); Q
            x^2 + (2*a^2 + a + 4)*x + a^2 + 3*a + 4
            sage: Q.parent()
            Ore Polynomial Ring in x over
             Finite Field in a of size 5^3 twisted by a |--> a^5 and a*([a |--> a^5] - id)
            sage: Q.parent() is S
            False

        This behavior ensures that the Hilbert shift by a fixed element
        defines a homomorphism of rings::

            sage: # needs sage.rings.finite_rings
            sage: U = S.random_element(degree=5)
            sage: V = S.random_element(degree=5)
            sage: s = k.random_element()
            sage: (U+V).hilbert_shift(s) == U.hilbert_shift(s) + V.hilbert_shift(s)
            True
            sage: (U*V).hilbert_shift(s) == U.hilbert_shift(s) * V.hilbert_shift(s)
            True

        We check that shifting by an element and then by its opposite
        gives back the initial Ore polynomial::

            sage: # needs sage.rings.finite_rings
            sage: P = S.random_element(degree=10)
            sage: s = k.random_element()
            sage: P.hilbert_shift(s).hilbert_shift(-s) == P
            True"""
    @overload
    def list(self, boolcopy=...) -> list:
        """OrePolynomial_generic_dense.list(self, bool copy=True) -> list

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/ore_polynomial_element.pyx (starting at line 2456)

        Return a list of the coefficients of ``self``.

        EXAMPLES::

            sage: R.<t> = QQ[]
            sage: sigma = R.hom([t+1])
            sage: S.<x> = R['x',sigma]
            sage: a = 1 + x^4 + (t+1)*x^2 + t^2
            sage: l = a.list(); l
            [t^2 + 1, 0, t + 1, 0, 1]

        Note that `l` is a list, it is mutable, and each call to the list
        method returns a new list::

            sage: type(l)
            <... 'list'>
            sage: l[0] = 5
            sage: a.list()
            [t^2 + 1, 0, t + 1, 0, 1]"""
    @overload
    def list(self) -> Any:
        """OrePolynomial_generic_dense.list(self, bool copy=True) -> list

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/ore_polynomial_element.pyx (starting at line 2456)

        Return a list of the coefficients of ``self``.

        EXAMPLES::

            sage: R.<t> = QQ[]
            sage: sigma = R.hom([t+1])
            sage: S.<x> = R['x',sigma]
            sage: a = 1 + x^4 + (t+1)*x^2 + t^2
            sage: l = a.list(); l
            [t^2 + 1, 0, t + 1, 0, 1]

        Note that `l` is a list, it is mutable, and each call to the list
        method returns a new list::

            sage: type(l)
            <... 'list'>
            sage: l[0] = 5
            sage: a.list()
            [t^2 + 1, 0, t + 1, 0, 1]"""
    @overload
    def list(self) -> Any:
        """OrePolynomial_generic_dense.list(self, bool copy=True) -> list

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/ore_polynomial_element.pyx (starting at line 2456)

        Return a list of the coefficients of ``self``.

        EXAMPLES::

            sage: R.<t> = QQ[]
            sage: sigma = R.hom([t+1])
            sage: S.<x> = R['x',sigma]
            sage: a = 1 + x^4 + (t+1)*x^2 + t^2
            sage: l = a.list(); l
            [t^2 + 1, 0, t + 1, 0, 1]

        Note that `l` is a list, it is mutable, and each call to the list
        method returns a new list::

            sage: type(l)
            <... 'list'>
            sage: l[0] = 5
            sage: a.list()
            [t^2 + 1, 0, t + 1, 0, 1]"""
    @overload
    def monomial_coefficients(self) -> dict:
        """OrePolynomial_generic_dense.monomial_coefficients(self) -> dict

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/ore_polynomial_element.pyx (starting at line 2484)

        Return a dictionary representation of ``self``.

        EXAMPLES::

            sage: R.<t> = ZZ[]
            sage: sigma = R.hom([t+1])
            sage: S.<x> = R['x',sigma]
            sage: a = x^2012 + t*x^1006 + t^3 + 2*t
            sage: a.monomial_coefficients()
            {0: t^3 + 2*t, 1006: t, 2012: 1}

        ``dict`` is an alias::

            sage: a.dict()
            {0: t^3 + 2*t, 1006: t, 2012: 1}"""
    @overload
    def monomial_coefficients(self) -> Any:
        """OrePolynomial_generic_dense.monomial_coefficients(self) -> dict

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/ore_polynomial_element.pyx (starting at line 2484)

        Return a dictionary representation of ``self``.

        EXAMPLES::

            sage: R.<t> = ZZ[]
            sage: sigma = R.hom([t+1])
            sage: S.<x> = R['x',sigma]
            sage: a = x^2012 + t*x^1006 + t^3 + 2*t
            sage: a.monomial_coefficients()
            {0: t^3 + 2*t, 1006: t, 2012: 1}

        ``dict`` is an alias::

            sage: a.dict()
            {0: t^3 + 2*t, 1006: t, 2012: 1}"""
    def truncate(self, n) -> Any:
        """OrePolynomial_generic_dense.truncate(self, n)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/ore_polynomial_element.pyx (starting at line 2660)

        Return the polynomial resulting from discarding all monomials of degree
        at least `n`.

        EXAMPLES::

            sage: R.<t> = ZZ[]
            sage: sigma = R.hom([t+1])
            sage: S.<x> = R['x',sigma]
            sage: a = t*x^3 + x^4 + (t+1)*x^2
            sage: a.truncate(4)
            t*x^3 + (t + 1)*x^2
            sage: a.truncate(3)
            (t + 1)*x^2"""
    def valuation(self) -> Any:
        """OrePolynomial_generic_dense.valuation(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/ore_polynomial_element.pyx (starting at line 2632)

        Return the minimal degree of a nonzero monomial of ``self``.

        By convention, the zero Ore polynomial has valuation `+\\infty`.

        EXAMPLES::

            sage: R.<t> = ZZ[]
            sage: sigma = R.hom([t+1])
            sage: S.<x> = R['x',sigma]
            sage: a = x^2 + t*x^3 + t^2*x
            sage: a.valuation()
            1

        By convention, the valuation of `0` is `+\\infty`::

            sage: S(0).valuation()
            +Infinity"""
    def __getitem__(self, n) -> Any:
        """OrePolynomial_generic_dense.__getitem__(self, n)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/ore_polynomial_element.pyx (starting at line 2430)

        Return the `n`-th coefficient of ``self``.

        INPUT:

        - ``n`` -- integer

        OUTPUT: the ``n``-th coefficient of ``self``

        EXAMPLES::

            sage: R.<t> = QQ[]
            sage: sigma = R.hom([t+1])
            sage: S.<x> = R['x',sigma]
            sage: a = t*x^2 + (t + 3/7)*x + t^2
            sage: a[1]
            t + 3/7
            sage: a[3]
            0"""
    def __iter__(self) -> Any:
        """OrePolynomial_generic_dense.__iter__(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/ore_polynomial_element.pyx (starting at line 2415)

        Iterate over the list of coefficients of ``self``.

        EXAMPLES::

            sage: R.<t> = QQ[]
            sage: sigma = R.hom([t+1])
            sage: S.<x> = R['x',sigma]
            sage: P = S([1, 2, 3])
            sage: [y for y in iter(P)]
            [1, 2, 3]"""
    def __reduce__(self) -> Any:
        """OrePolynomial_generic_dense.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/ore_polynomial_element.pyx (starting at line 2301)

        Return the generic dense Ore polynomial corresponding to the
        current parameters provided ``self``.

        EXAMPLES::

            sage: R.<t> = QQ[]
            sage: sigma = R.hom([t+1])
            sage: S.<x> = R['x',sigma]
            sage: loads(dumps(x)) == x
            True
            sage: loads(dumps(x))
            x"""
