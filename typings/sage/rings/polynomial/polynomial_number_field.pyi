import sage.rings.polynomial.polynomial_element_generic
from sage.rings.polynomial.polynomial_element_generic import Polynomial_generic_dense_field as Polynomial_generic_dense_field
from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing as PolynomialRing
from sage.rings.rational_field import QQ as QQ
from sage.structure.element import coerce_binop as coerce_binop
from typing import Any, overload

class Polynomial_absolute_number_field_dense(sage.rings.polynomial.polynomial_element_generic.Polynomial_generic_dense_field):
    """File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_number_field.pyx (starting at line 81)

        Class of dense univariate polynomials over an absolute number field.
    """
    def __init__(self, parent, x=..., check=..., is_gen=..., construct=...) -> Any:
        """Polynomial_absolute_number_field_dense.__init__(self, parent, x=None, check=True, is_gen=False, construct=False)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_number_field.pyx (starting at line 85)

        Create a new polynomial in the polynomial ring ``parent``.

        INPUT:

        - ``parent`` -- the polynomial ring in which to construct the
          element

        - ``x`` -- (default: ``None``) an object representing the
          polynomial, e.g. a list of coefficients.  See
          :meth:`sage.rings.polynomial.polynomial_element_generic.Polynomial_generic_dense_field.__init__`
          for more details.

        - ``check`` -- boolean (default: ``True``); if ``True``, make sure that
          the coefficients of the polynomial are in the base ring

        - ``is_gen`` -- boolean (default: ``False``); if ``True``, `x` is the
          distinguished generator of the polynomial ring

        - ``construct`` -- boolean (default: ``False``); unused

        EXAMPLES::

            sage: P.<x> = QQ[I][]
            sage: f = P.random_element()
            sage: from sage.rings.polynomial.polynomial_number_field import Polynomial_absolute_number_field_dense
            sage: isinstance(f, Polynomial_absolute_number_field_dense)
            True
            sage: a = P(x)
            sage: a.is_gen()
            True"""
    @overload
    def gcd(self, other) -> Any:
        """Polynomial_absolute_number_field_dense.gcd(self, other)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_number_field.pyx (starting at line 120)

        Compute the monic gcd of two univariate polynomials using PARI.

        INPUT:

        - ``other`` -- a polynomial with the same parent as ``self``

        OUTPUT: the monic gcd of ``self`` and ``other``

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: N.<a> = NumberField(x^3 - 1/2, 'a')
            sage: R.<r> = N['r']
            sage: f = (5/4*a^2 - 2*a + 4)*r^2 + (5*a^2 - 81/5*a - 17/2)*r + 4/5*a^2 + 24*a + 6
            sage: g = (5/4*a^2 - 2*a + 4)*r^2 + (-11*a^2 + 79/5*a - 7/2)*r - 4/5*a^2 - 24*a - 6
            sage: gcd(f, g**2)
            r - 60808/96625*a^2 - 69936/96625*a - 149212/96625
            sage: R = QQ[I]['x']
            sage: f = R.random_element(2)
            sage: g = f + 1
            sage: h = R.random_element(2).monic()
            sage: f *= h
            sage: g *= h
            sage: gcd(f, g) - h
            0
            sage: f.gcd(g) - h
            0

        TESTS:

        Test for degree one extensions::

            sage: x = polygen(ZZ, 'x')
            sage: N = NumberField(x - 3, 'a')
            sage: a = N.gen()
            sage: R = N['x']
            sage: f = R._random_nonzero_element()
            sage: g1 = R._random_nonzero_element()
            sage: g2 = g1 * R._random_nonzero_element() + 1
            sage: g1 *= f
            sage: g2 *= f
            sage: d = gcd(g1, g2)
            sage: f.monic() - d
            0
            sage: d.parent() is R
            True

        Test for coercion with other rings and force weird variables
        to test PARI behavior::

            sage: r = polygen(ZZ, 'r')
            sage: N = NumberField(r^2 - 2, 'r')
            sage: a = N.gen()
            sage: R = N['r']
            sage: r = R.gen()
            sage: f = N.random_element(4)*r + 1
            sage: g = ZZ['r']([1, 2, 3, 4, 5, 6, 7]); g
            7*r^6 + 6*r^5 + 5*r^4 + 4*r^3 + 3*r^2 + 2*r + 1
            sage: gcd(f, g) == gcd(g, f)
            True
            sage: h = f.gcd(g); h
            1
            sage: h.parent()
            Univariate Polynomial Ring in r over
             Number Field in r with defining polynomial r^2 - 2
            sage: gcd([a*r + 2, r^2 - 2])
            r + r"""
    @overload
    def gcd(self, f, g) -> Any:
        """Polynomial_absolute_number_field_dense.gcd(self, other)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_number_field.pyx (starting at line 120)

        Compute the monic gcd of two univariate polynomials using PARI.

        INPUT:

        - ``other`` -- a polynomial with the same parent as ``self``

        OUTPUT: the monic gcd of ``self`` and ``other``

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: N.<a> = NumberField(x^3 - 1/2, 'a')
            sage: R.<r> = N['r']
            sage: f = (5/4*a^2 - 2*a + 4)*r^2 + (5*a^2 - 81/5*a - 17/2)*r + 4/5*a^2 + 24*a + 6
            sage: g = (5/4*a^2 - 2*a + 4)*r^2 + (-11*a^2 + 79/5*a - 7/2)*r - 4/5*a^2 - 24*a - 6
            sage: gcd(f, g**2)
            r - 60808/96625*a^2 - 69936/96625*a - 149212/96625
            sage: R = QQ[I]['x']
            sage: f = R.random_element(2)
            sage: g = f + 1
            sage: h = R.random_element(2).monic()
            sage: f *= h
            sage: g *= h
            sage: gcd(f, g) - h
            0
            sage: f.gcd(g) - h
            0

        TESTS:

        Test for degree one extensions::

            sage: x = polygen(ZZ, 'x')
            sage: N = NumberField(x - 3, 'a')
            sage: a = N.gen()
            sage: R = N['x']
            sage: f = R._random_nonzero_element()
            sage: g1 = R._random_nonzero_element()
            sage: g2 = g1 * R._random_nonzero_element() + 1
            sage: g1 *= f
            sage: g2 *= f
            sage: d = gcd(g1, g2)
            sage: f.monic() - d
            0
            sage: d.parent() is R
            True

        Test for coercion with other rings and force weird variables
        to test PARI behavior::

            sage: r = polygen(ZZ, 'r')
            sage: N = NumberField(r^2 - 2, 'r')
            sage: a = N.gen()
            sage: R = N['r']
            sage: r = R.gen()
            sage: f = N.random_element(4)*r + 1
            sage: g = ZZ['r']([1, 2, 3, 4, 5, 6, 7]); g
            7*r^6 + 6*r^5 + 5*r^4 + 4*r^3 + 3*r^2 + 2*r + 1
            sage: gcd(f, g) == gcd(g, f)
            True
            sage: h = f.gcd(g); h
            1
            sage: h.parent()
            Univariate Polynomial Ring in r over
             Number Field in r with defining polynomial r^2 - 2
            sage: gcd([a*r + 2, r^2 - 2])
            r + r"""
    @overload
    def gcd(self, g) -> Any:
        """Polynomial_absolute_number_field_dense.gcd(self, other)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_number_field.pyx (starting at line 120)

        Compute the monic gcd of two univariate polynomials using PARI.

        INPUT:

        - ``other`` -- a polynomial with the same parent as ``self``

        OUTPUT: the monic gcd of ``self`` and ``other``

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: N.<a> = NumberField(x^3 - 1/2, 'a')
            sage: R.<r> = N['r']
            sage: f = (5/4*a^2 - 2*a + 4)*r^2 + (5*a^2 - 81/5*a - 17/2)*r + 4/5*a^2 + 24*a + 6
            sage: g = (5/4*a^2 - 2*a + 4)*r^2 + (-11*a^2 + 79/5*a - 7/2)*r - 4/5*a^2 - 24*a - 6
            sage: gcd(f, g**2)
            r - 60808/96625*a^2 - 69936/96625*a - 149212/96625
            sage: R = QQ[I]['x']
            sage: f = R.random_element(2)
            sage: g = f + 1
            sage: h = R.random_element(2).monic()
            sage: f *= h
            sage: g *= h
            sage: gcd(f, g) - h
            0
            sage: f.gcd(g) - h
            0

        TESTS:

        Test for degree one extensions::

            sage: x = polygen(ZZ, 'x')
            sage: N = NumberField(x - 3, 'a')
            sage: a = N.gen()
            sage: R = N['x']
            sage: f = R._random_nonzero_element()
            sage: g1 = R._random_nonzero_element()
            sage: g2 = g1 * R._random_nonzero_element() + 1
            sage: g1 *= f
            sage: g2 *= f
            sage: d = gcd(g1, g2)
            sage: f.monic() - d
            0
            sage: d.parent() is R
            True

        Test for coercion with other rings and force weird variables
        to test PARI behavior::

            sage: r = polygen(ZZ, 'r')
            sage: N = NumberField(r^2 - 2, 'r')
            sage: a = N.gen()
            sage: R = N['r']
            sage: r = R.gen()
            sage: f = N.random_element(4)*r + 1
            sage: g = ZZ['r']([1, 2, 3, 4, 5, 6, 7]); g
            7*r^6 + 6*r^5 + 5*r^4 + 4*r^3 + 3*r^2 + 2*r + 1
            sage: gcd(f, g) == gcd(g, f)
            True
            sage: h = f.gcd(g); h
            1
            sage: h.parent()
            Univariate Polynomial Ring in r over
             Number Field in r with defining polynomial r^2 - 2
            sage: gcd([a*r + 2, r^2 - 2])
            r + r"""
    @overload
    def gcd(self, g1, g2) -> Any:
        """Polynomial_absolute_number_field_dense.gcd(self, other)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_number_field.pyx (starting at line 120)

        Compute the monic gcd of two univariate polynomials using PARI.

        INPUT:

        - ``other`` -- a polynomial with the same parent as ``self``

        OUTPUT: the monic gcd of ``self`` and ``other``

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: N.<a> = NumberField(x^3 - 1/2, 'a')
            sage: R.<r> = N['r']
            sage: f = (5/4*a^2 - 2*a + 4)*r^2 + (5*a^2 - 81/5*a - 17/2)*r + 4/5*a^2 + 24*a + 6
            sage: g = (5/4*a^2 - 2*a + 4)*r^2 + (-11*a^2 + 79/5*a - 7/2)*r - 4/5*a^2 - 24*a - 6
            sage: gcd(f, g**2)
            r - 60808/96625*a^2 - 69936/96625*a - 149212/96625
            sage: R = QQ[I]['x']
            sage: f = R.random_element(2)
            sage: g = f + 1
            sage: h = R.random_element(2).monic()
            sage: f *= h
            sage: g *= h
            sage: gcd(f, g) - h
            0
            sage: f.gcd(g) - h
            0

        TESTS:

        Test for degree one extensions::

            sage: x = polygen(ZZ, 'x')
            sage: N = NumberField(x - 3, 'a')
            sage: a = N.gen()
            sage: R = N['x']
            sage: f = R._random_nonzero_element()
            sage: g1 = R._random_nonzero_element()
            sage: g2 = g1 * R._random_nonzero_element() + 1
            sage: g1 *= f
            sage: g2 *= f
            sage: d = gcd(g1, g2)
            sage: f.monic() - d
            0
            sage: d.parent() is R
            True

        Test for coercion with other rings and force weird variables
        to test PARI behavior::

            sage: r = polygen(ZZ, 'r')
            sage: N = NumberField(r^2 - 2, 'r')
            sage: a = N.gen()
            sage: R = N['r']
            sage: r = R.gen()
            sage: f = N.random_element(4)*r + 1
            sage: g = ZZ['r']([1, 2, 3, 4, 5, 6, 7]); g
            7*r^6 + 6*r^5 + 5*r^4 + 4*r^3 + 3*r^2 + 2*r + 1
            sage: gcd(f, g) == gcd(g, f)
            True
            sage: h = f.gcd(g); h
            1
            sage: h.parent()
            Univariate Polynomial Ring in r over
             Number Field in r with defining polynomial r^2 - 2
            sage: gcd([a*r + 2, r^2 - 2])
            r + r"""
    @overload
    def gcd(self, g) -> Any:
        """Polynomial_absolute_number_field_dense.gcd(self, other)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_number_field.pyx (starting at line 120)

        Compute the monic gcd of two univariate polynomials using PARI.

        INPUT:

        - ``other`` -- a polynomial with the same parent as ``self``

        OUTPUT: the monic gcd of ``self`` and ``other``

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: N.<a> = NumberField(x^3 - 1/2, 'a')
            sage: R.<r> = N['r']
            sage: f = (5/4*a^2 - 2*a + 4)*r^2 + (5*a^2 - 81/5*a - 17/2)*r + 4/5*a^2 + 24*a + 6
            sage: g = (5/4*a^2 - 2*a + 4)*r^2 + (-11*a^2 + 79/5*a - 7/2)*r - 4/5*a^2 - 24*a - 6
            sage: gcd(f, g**2)
            r - 60808/96625*a^2 - 69936/96625*a - 149212/96625
            sage: R = QQ[I]['x']
            sage: f = R.random_element(2)
            sage: g = f + 1
            sage: h = R.random_element(2).monic()
            sage: f *= h
            sage: g *= h
            sage: gcd(f, g) - h
            0
            sage: f.gcd(g) - h
            0

        TESTS:

        Test for degree one extensions::

            sage: x = polygen(ZZ, 'x')
            sage: N = NumberField(x - 3, 'a')
            sage: a = N.gen()
            sage: R = N['x']
            sage: f = R._random_nonzero_element()
            sage: g1 = R._random_nonzero_element()
            sage: g2 = g1 * R._random_nonzero_element() + 1
            sage: g1 *= f
            sage: g2 *= f
            sage: d = gcd(g1, g2)
            sage: f.monic() - d
            0
            sage: d.parent() is R
            True

        Test for coercion with other rings and force weird variables
        to test PARI behavior::

            sage: r = polygen(ZZ, 'r')
            sage: N = NumberField(r^2 - 2, 'r')
            sage: a = N.gen()
            sage: R = N['r']
            sage: r = R.gen()
            sage: f = N.random_element(4)*r + 1
            sage: g = ZZ['r']([1, 2, 3, 4, 5, 6, 7]); g
            7*r^6 + 6*r^5 + 5*r^4 + 4*r^3 + 3*r^2 + 2*r + 1
            sage: gcd(f, g) == gcd(g, f)
            True
            sage: h = f.gcd(g); h
            1
            sage: h.parent()
            Univariate Polynomial Ring in r over
             Number Field in r with defining polynomial r^2 - 2
            sage: gcd([a*r + 2, r^2 - 2])
            r + r"""

class Polynomial_relative_number_field_dense(sage.rings.polynomial.polynomial_element_generic.Polynomial_generic_dense_field):
    """File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_number_field.pyx (starting at line 215)

        Class of dense univariate polynomials over a relative number field.
    """
    def __init__(self, parent, x=..., check=..., is_gen=..., construct=...) -> Any:
        """Polynomial_relative_number_field_dense.__init__(self, parent, x=None, check=True, is_gen=False, construct=False)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_number_field.pyx (starting at line 219)

        Create a new polynomial in the polynomial ring ``parent``.

        INPUT:

        - ``parent`` -- polynomial ring in which to construct the
          element

        - ``x`` -- (default: ``None``) an object representing the
          polynomial, e.g. a list of coefficients. See
          :meth:`sage.rings.polynomial.polynomial_element_generic.Polynomial_generic_dense_field.__init__`
          for more details.

        - ``check`` -- boolean (default: ``True``); if ``True``, make sure that
          the coefficients of the polynomial are in the base ring

        - ``is_gen`` -- boolean (default: ``False``); if ``True``, ``x`` is the
          distinguished generator of the polynomial ring

        - ``construct`` -- boolean (default: ``False``); unused

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: f = NumberField([x^2 - 2, x^2 - 3], 'a')['x'].random_element()
            sage: from sage.rings.polynomial.polynomial_number_field import Polynomial_relative_number_field_dense
            sage: isinstance(f, Polynomial_relative_number_field_dense)
            True"""
    @overload
    def gcd(self, other) -> Any:
        """Polynomial_relative_number_field_dense.gcd(self, other)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_number_field.pyx (starting at line 251)

        Compute the monic gcd of two polynomials.

        Currently, the method checks corner cases in which one of the
        polynomials is zero or a constant. Then, computes an absolute
        extension and performs the computations there.

        INPUT:

        - ``other`` -- a polynomial with the same parent as ``self``

        OUTPUT: the monic gcd of ``self`` and ``other``

        See :meth:`Polynomial_absolute_number_field_dense.gcd` for
        more details.

        EXAMPLES::

            sage: # needs sage.symbolic
            sage: N = QQ[sqrt(2), sqrt(3)]
            sage: s2, s3 = N.gens()
            sage: x = polygen(N)
            sage: f = x^4 - 5*x^2 + 6
            sage: g = x^3 + (-2*s2 + s3)*x^2 + (-2*s3*s2 + 2)*x + 2*s3
            sage: gcd(f, g)
            x^2 + (-sqrt2 + sqrt3)*x - sqrt3*sqrt2
            sage: f.gcd(g)
            x^2 + (-sqrt2 + sqrt3)*x - sqrt3*sqrt2

        TESTS::

            sage: x = polygen(ZZ, 'x')
            sage: R = NumberField([x^2 - 2, x^2 - 3], 'a')['x']
            sage: f = R._random_nonzero_element()
            sage: g1 = R.random_element()
            sage: g2 = R.random_element()*g1 + 1
            sage: g1 *= f
            sage: g2 *= f
            sage: f.monic() - g1.gcd(g2)
            0

        Test for degree one extensions::

            sage: R = NumberField([x - 2, x + 1, x - 3], 'a')['x']
            sage: f = R.random_element(2)
            sage: g1 = R.random_element(2)
            sage: g2 = R.random_element(2)*g1 + 1
            sage: g1 *= f
            sage: g2 *= f
            sage: d = gcd(g1, g2)
            sage: d - f.monic()
            0
            sage: d.parent() is R
            True

        Test for hardcoded variables::

            sage: # needs sage.symbolic
            sage: R = N['sqrt2sqrt3']
            sage: x = R.gen()
            sage: f = x^2 - 2
            sage: g1 = x^2 - s3
            sage: g2 = x - s2
            sage: gcd(f, g1)
            1
            sage: gcd(f, g2)
            sqrt2sqrt3 - sqrt2"""
    @overload
    def gcd(self, f, g) -> Any:
        """Polynomial_relative_number_field_dense.gcd(self, other)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_number_field.pyx (starting at line 251)

        Compute the monic gcd of two polynomials.

        Currently, the method checks corner cases in which one of the
        polynomials is zero or a constant. Then, computes an absolute
        extension and performs the computations there.

        INPUT:

        - ``other`` -- a polynomial with the same parent as ``self``

        OUTPUT: the monic gcd of ``self`` and ``other``

        See :meth:`Polynomial_absolute_number_field_dense.gcd` for
        more details.

        EXAMPLES::

            sage: # needs sage.symbolic
            sage: N = QQ[sqrt(2), sqrt(3)]
            sage: s2, s3 = N.gens()
            sage: x = polygen(N)
            sage: f = x^4 - 5*x^2 + 6
            sage: g = x^3 + (-2*s2 + s3)*x^2 + (-2*s3*s2 + 2)*x + 2*s3
            sage: gcd(f, g)
            x^2 + (-sqrt2 + sqrt3)*x - sqrt3*sqrt2
            sage: f.gcd(g)
            x^2 + (-sqrt2 + sqrt3)*x - sqrt3*sqrt2

        TESTS::

            sage: x = polygen(ZZ, 'x')
            sage: R = NumberField([x^2 - 2, x^2 - 3], 'a')['x']
            sage: f = R._random_nonzero_element()
            sage: g1 = R.random_element()
            sage: g2 = R.random_element()*g1 + 1
            sage: g1 *= f
            sage: g2 *= f
            sage: f.monic() - g1.gcd(g2)
            0

        Test for degree one extensions::

            sage: R = NumberField([x - 2, x + 1, x - 3], 'a')['x']
            sage: f = R.random_element(2)
            sage: g1 = R.random_element(2)
            sage: g2 = R.random_element(2)*g1 + 1
            sage: g1 *= f
            sage: g2 *= f
            sage: d = gcd(g1, g2)
            sage: d - f.monic()
            0
            sage: d.parent() is R
            True

        Test for hardcoded variables::

            sage: # needs sage.symbolic
            sage: R = N['sqrt2sqrt3']
            sage: x = R.gen()
            sage: f = x^2 - 2
            sage: g1 = x^2 - s3
            sage: g2 = x - s2
            sage: gcd(f, g1)
            1
            sage: gcd(f, g2)
            sqrt2sqrt3 - sqrt2"""
    @overload
    def gcd(self, g) -> Any:
        """Polynomial_relative_number_field_dense.gcd(self, other)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_number_field.pyx (starting at line 251)

        Compute the monic gcd of two polynomials.

        Currently, the method checks corner cases in which one of the
        polynomials is zero or a constant. Then, computes an absolute
        extension and performs the computations there.

        INPUT:

        - ``other`` -- a polynomial with the same parent as ``self``

        OUTPUT: the monic gcd of ``self`` and ``other``

        See :meth:`Polynomial_absolute_number_field_dense.gcd` for
        more details.

        EXAMPLES::

            sage: # needs sage.symbolic
            sage: N = QQ[sqrt(2), sqrt(3)]
            sage: s2, s3 = N.gens()
            sage: x = polygen(N)
            sage: f = x^4 - 5*x^2 + 6
            sage: g = x^3 + (-2*s2 + s3)*x^2 + (-2*s3*s2 + 2)*x + 2*s3
            sage: gcd(f, g)
            x^2 + (-sqrt2 + sqrt3)*x - sqrt3*sqrt2
            sage: f.gcd(g)
            x^2 + (-sqrt2 + sqrt3)*x - sqrt3*sqrt2

        TESTS::

            sage: x = polygen(ZZ, 'x')
            sage: R = NumberField([x^2 - 2, x^2 - 3], 'a')['x']
            sage: f = R._random_nonzero_element()
            sage: g1 = R.random_element()
            sage: g2 = R.random_element()*g1 + 1
            sage: g1 *= f
            sage: g2 *= f
            sage: f.monic() - g1.gcd(g2)
            0

        Test for degree one extensions::

            sage: R = NumberField([x - 2, x + 1, x - 3], 'a')['x']
            sage: f = R.random_element(2)
            sage: g1 = R.random_element(2)
            sage: g2 = R.random_element(2)*g1 + 1
            sage: g1 *= f
            sage: g2 *= f
            sage: d = gcd(g1, g2)
            sage: d - f.monic()
            0
            sage: d.parent() is R
            True

        Test for hardcoded variables::

            sage: # needs sage.symbolic
            sage: R = N['sqrt2sqrt3']
            sage: x = R.gen()
            sage: f = x^2 - 2
            sage: g1 = x^2 - s3
            sage: g2 = x - s2
            sage: gcd(f, g1)
            1
            sage: gcd(f, g2)
            sqrt2sqrt3 - sqrt2"""
    @overload
    def gcd(self, g2) -> Any:
        """Polynomial_relative_number_field_dense.gcd(self, other)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_number_field.pyx (starting at line 251)

        Compute the monic gcd of two polynomials.

        Currently, the method checks corner cases in which one of the
        polynomials is zero or a constant. Then, computes an absolute
        extension and performs the computations there.

        INPUT:

        - ``other`` -- a polynomial with the same parent as ``self``

        OUTPUT: the monic gcd of ``self`` and ``other``

        See :meth:`Polynomial_absolute_number_field_dense.gcd` for
        more details.

        EXAMPLES::

            sage: # needs sage.symbolic
            sage: N = QQ[sqrt(2), sqrt(3)]
            sage: s2, s3 = N.gens()
            sage: x = polygen(N)
            sage: f = x^4 - 5*x^2 + 6
            sage: g = x^3 + (-2*s2 + s3)*x^2 + (-2*s3*s2 + 2)*x + 2*s3
            sage: gcd(f, g)
            x^2 + (-sqrt2 + sqrt3)*x - sqrt3*sqrt2
            sage: f.gcd(g)
            x^2 + (-sqrt2 + sqrt3)*x - sqrt3*sqrt2

        TESTS::

            sage: x = polygen(ZZ, 'x')
            sage: R = NumberField([x^2 - 2, x^2 - 3], 'a')['x']
            sage: f = R._random_nonzero_element()
            sage: g1 = R.random_element()
            sage: g2 = R.random_element()*g1 + 1
            sage: g1 *= f
            sage: g2 *= f
            sage: f.monic() - g1.gcd(g2)
            0

        Test for degree one extensions::

            sage: R = NumberField([x - 2, x + 1, x - 3], 'a')['x']
            sage: f = R.random_element(2)
            sage: g1 = R.random_element(2)
            sage: g2 = R.random_element(2)*g1 + 1
            sage: g1 *= f
            sage: g2 *= f
            sage: d = gcd(g1, g2)
            sage: d - f.monic()
            0
            sage: d.parent() is R
            True

        Test for hardcoded variables::

            sage: # needs sage.symbolic
            sage: R = N['sqrt2sqrt3']
            sage: x = R.gen()
            sage: f = x^2 - 2
            sage: g1 = x^2 - s3
            sage: g2 = x - s2
            sage: gcd(f, g1)
            1
            sage: gcd(f, g2)
            sqrt2sqrt3 - sqrt2"""
    @overload
    def gcd(self, g1, g2) -> Any:
        """Polynomial_relative_number_field_dense.gcd(self, other)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_number_field.pyx (starting at line 251)

        Compute the monic gcd of two polynomials.

        Currently, the method checks corner cases in which one of the
        polynomials is zero or a constant. Then, computes an absolute
        extension and performs the computations there.

        INPUT:

        - ``other`` -- a polynomial with the same parent as ``self``

        OUTPUT: the monic gcd of ``self`` and ``other``

        See :meth:`Polynomial_absolute_number_field_dense.gcd` for
        more details.

        EXAMPLES::

            sage: # needs sage.symbolic
            sage: N = QQ[sqrt(2), sqrt(3)]
            sage: s2, s3 = N.gens()
            sage: x = polygen(N)
            sage: f = x^4 - 5*x^2 + 6
            sage: g = x^3 + (-2*s2 + s3)*x^2 + (-2*s3*s2 + 2)*x + 2*s3
            sage: gcd(f, g)
            x^2 + (-sqrt2 + sqrt3)*x - sqrt3*sqrt2
            sage: f.gcd(g)
            x^2 + (-sqrt2 + sqrt3)*x - sqrt3*sqrt2

        TESTS::

            sage: x = polygen(ZZ, 'x')
            sage: R = NumberField([x^2 - 2, x^2 - 3], 'a')['x']
            sage: f = R._random_nonzero_element()
            sage: g1 = R.random_element()
            sage: g2 = R.random_element()*g1 + 1
            sage: g1 *= f
            sage: g2 *= f
            sage: f.monic() - g1.gcd(g2)
            0

        Test for degree one extensions::

            sage: R = NumberField([x - 2, x + 1, x - 3], 'a')['x']
            sage: f = R.random_element(2)
            sage: g1 = R.random_element(2)
            sage: g2 = R.random_element(2)*g1 + 1
            sage: g1 *= f
            sage: g2 *= f
            sage: d = gcd(g1, g2)
            sage: d - f.monic()
            0
            sage: d.parent() is R
            True

        Test for hardcoded variables::

            sage: # needs sage.symbolic
            sage: R = N['sqrt2sqrt3']
            sage: x = R.gen()
            sage: f = x^2 - 2
            sage: g1 = x^2 - s3
            sage: g2 = x - s2
            sage: gcd(f, g1)
            1
            sage: gcd(f, g2)
            sqrt2sqrt3 - sqrt2"""
    @overload
    def gcd(self, f, g1) -> Any:
        """Polynomial_relative_number_field_dense.gcd(self, other)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_number_field.pyx (starting at line 251)

        Compute the monic gcd of two polynomials.

        Currently, the method checks corner cases in which one of the
        polynomials is zero or a constant. Then, computes an absolute
        extension and performs the computations there.

        INPUT:

        - ``other`` -- a polynomial with the same parent as ``self``

        OUTPUT: the monic gcd of ``self`` and ``other``

        See :meth:`Polynomial_absolute_number_field_dense.gcd` for
        more details.

        EXAMPLES::

            sage: # needs sage.symbolic
            sage: N = QQ[sqrt(2), sqrt(3)]
            sage: s2, s3 = N.gens()
            sage: x = polygen(N)
            sage: f = x^4 - 5*x^2 + 6
            sage: g = x^3 + (-2*s2 + s3)*x^2 + (-2*s3*s2 + 2)*x + 2*s3
            sage: gcd(f, g)
            x^2 + (-sqrt2 + sqrt3)*x - sqrt3*sqrt2
            sage: f.gcd(g)
            x^2 + (-sqrt2 + sqrt3)*x - sqrt3*sqrt2

        TESTS::

            sage: x = polygen(ZZ, 'x')
            sage: R = NumberField([x^2 - 2, x^2 - 3], 'a')['x']
            sage: f = R._random_nonzero_element()
            sage: g1 = R.random_element()
            sage: g2 = R.random_element()*g1 + 1
            sage: g1 *= f
            sage: g2 *= f
            sage: f.monic() - g1.gcd(g2)
            0

        Test for degree one extensions::

            sage: R = NumberField([x - 2, x + 1, x - 3], 'a')['x']
            sage: f = R.random_element(2)
            sage: g1 = R.random_element(2)
            sage: g2 = R.random_element(2)*g1 + 1
            sage: g1 *= f
            sage: g2 *= f
            sage: d = gcd(g1, g2)
            sage: d - f.monic()
            0
            sage: d.parent() is R
            True

        Test for hardcoded variables::

            sage: # needs sage.symbolic
            sage: R = N['sqrt2sqrt3']
            sage: x = R.gen()
            sage: f = x^2 - 2
            sage: g1 = x^2 - s3
            sage: g2 = x - s2
            sage: gcd(f, g1)
            1
            sage: gcd(f, g2)
            sqrt2sqrt3 - sqrt2"""
    @overload
    def gcd(self, f, g2) -> Any:
        """Polynomial_relative_number_field_dense.gcd(self, other)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_number_field.pyx (starting at line 251)

        Compute the monic gcd of two polynomials.

        Currently, the method checks corner cases in which one of the
        polynomials is zero or a constant. Then, computes an absolute
        extension and performs the computations there.

        INPUT:

        - ``other`` -- a polynomial with the same parent as ``self``

        OUTPUT: the monic gcd of ``self`` and ``other``

        See :meth:`Polynomial_absolute_number_field_dense.gcd` for
        more details.

        EXAMPLES::

            sage: # needs sage.symbolic
            sage: N = QQ[sqrt(2), sqrt(3)]
            sage: s2, s3 = N.gens()
            sage: x = polygen(N)
            sage: f = x^4 - 5*x^2 + 6
            sage: g = x^3 + (-2*s2 + s3)*x^2 + (-2*s3*s2 + 2)*x + 2*s3
            sage: gcd(f, g)
            x^2 + (-sqrt2 + sqrt3)*x - sqrt3*sqrt2
            sage: f.gcd(g)
            x^2 + (-sqrt2 + sqrt3)*x - sqrt3*sqrt2

        TESTS::

            sage: x = polygen(ZZ, 'x')
            sage: R = NumberField([x^2 - 2, x^2 - 3], 'a')['x']
            sage: f = R._random_nonzero_element()
            sage: g1 = R.random_element()
            sage: g2 = R.random_element()*g1 + 1
            sage: g1 *= f
            sage: g2 *= f
            sage: f.monic() - g1.gcd(g2)
            0

        Test for degree one extensions::

            sage: R = NumberField([x - 2, x + 1, x - 3], 'a')['x']
            sage: f = R.random_element(2)
            sage: g1 = R.random_element(2)
            sage: g2 = R.random_element(2)*g1 + 1
            sage: g1 *= f
            sage: g2 *= f
            sage: d = gcd(g1, g2)
            sage: d - f.monic()
            0
            sage: d.parent() is R
            True

        Test for hardcoded variables::

            sage: # needs sage.symbolic
            sage: R = N['sqrt2sqrt3']
            sage: x = R.gen()
            sage: f = x^2 - 2
            sage: g1 = x^2 - s3
            sage: g2 = x - s2
            sage: gcd(f, g1)
            1
            sage: gcd(f, g2)
            sqrt2sqrt3 - sqrt2"""
