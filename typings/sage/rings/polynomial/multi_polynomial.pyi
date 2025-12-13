import _cython_3_2_1
import sage.rings.polynomial.commutative_polynomial
from sage.categories.category import ZZ as ZZ
from sage.misc.derivative import multi_derivative as multi_derivative
from sage.misc.misc_c import prod as prod
from sage.misc.superseded import deprecated_function_alias as deprecated_function_alias
from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing as PolynomialRing
from sage.rings.rational_field import QQ as QQ
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from typing import Any, ClassVar, overload

is_MPolynomial: _cython_3_2_1.cython_function_or_method

class MPolynomial(sage.rings.polynomial.commutative_polynomial.CommutativePolynomial):
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    @overload
    def args(self) -> Any:
        """MPolynomial.args(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 655)

        Return the names of the arguments of ``self``, in the
        order they are accepted from call.

        EXAMPLES::

            sage: R.<x,y> = ZZ[]
            sage: x.args()
            (x, y)"""
    @overload
    def args(self) -> Any:
        """MPolynomial.args(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 655)

        Return the names of the arguments of ``self``, in the
        order they are accepted from call.

        EXAMPLES::

            sage: R.<x,y> = ZZ[]
            sage: x.args()
            (x, y)"""
    @overload
    def canonical_associate(self) -> Any:
        """MPolynomial.canonical_associate(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 2937)

        Return a canonical associate.

        EXAMPLES::

            sage: R.<x,y>=QQ[]
            sage: (-2*x^2+3*x+5*y).canonical_associate()
            (x^2 - 3/2*x - 5/2*y, -2)
            sage: R.<x,y>=ZZ[]
            sage: (-2*x^2+3*x+5*y).canonical_associate()
            (2*x^2 - 3*x - 5*y, -1)"""
    @overload
    def canonical_associate(self) -> Any:
        """MPolynomial.canonical_associate(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 2937)

        Return a canonical associate.

        EXAMPLES::

            sage: R.<x,y>=QQ[]
            sage: (-2*x^2+3*x+5*y).canonical_associate()
            (x^2 - 3/2*x - 5/2*y, -2)
            sage: R.<x,y>=ZZ[]
            sage: (-2*x^2+3*x+5*y).canonical_associate()
            (2*x^2 - 3*x - 5*y, -1)"""
    @overload
    def canonical_associate(self) -> Any:
        """MPolynomial.canonical_associate(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 2937)

        Return a canonical associate.

        EXAMPLES::

            sage: R.<x,y>=QQ[]
            sage: (-2*x^2+3*x+5*y).canonical_associate()
            (x^2 - 3/2*x - 5/2*y, -2)
            sage: R.<x,y>=ZZ[]
            sage: (-2*x^2+3*x+5*y).canonical_associate()
            (2*x^2 - 3*x - 5*y, -1)"""
    @overload
    def change_ring(self, R) -> Any:
        """MPolynomial.change_ring(self, R)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 890)

        Return this polynomial with coefficients converted to ``R``.

        INPUT:

        - ``R`` -- a ring or morphism; if a morphism, the coefficients
          are mapped to the codomain of ``R``

        OUTPUT: a new polynomial with the base ring changed to ``R``

        EXAMPLES::

            sage: R.<x,y> = QQ[]
            sage: f = x^3 + 3/5*y + 1
            sage: f.change_ring(GF(7))
            x^3 + 2*y + 1
            sage: g = x^2 + 5*y
            sage: g.change_ring(GF(5))
            x^2

        ::

            sage: # needs sage.rings.finite_rings
            sage: R.<x,y> = GF(9,'a')[]
            sage: (x+2*y).change_ring(GF(3))
            x - y

        ::

            sage: # needs sage.rings.finite_rings
            sage: F.<a> = GF(7^2)
            sage: R.<x,y> = F[]
            sage: f = x^2 + a^2*y^2 + a*x + a^3*y
            sage: g = f.change_ring(F.frobenius_endomorphism()); g
            x^2 + (-a - 2)*y^2 + (-a + 1)*x + (2*a + 2)*y
            sage: g.change_ring(F.frobenius_endomorphism()) == f
            True

        ::

            sage: # needs sage.rings.number_field
            sage: K.<z> = CyclotomicField(3)
            sage: R.<x,y> = K[]
            sage: f = x^2 + z*y
            sage: f.change_ring(K.embeddings(CC)[1])
            x^2 + (-0.500000000000000 - 0.866025403784438*I)*y

        ::

            sage: # needs sage.rings.number_field
            sage: K.<w> = CyclotomicField(5)
            sage: R.<x,y> = K[]
            sage: f = x^2 + w*y
            sage: f.change_ring(K.embeddings(QQbar)[1])
            x^2 + (-0.8090169943749474? + 0.5877852522924731?*I)*y

        TESTS:

        Check that :issue:`25022` is fixed::

            sage: # needs sage.rings.number_field sage.symbolic
            sage: K.<x,y> = ZZ[]
            sage: (x*y).change_ring(SR).monomials()
            [x*y]

        Check that :issue:`36832` is fixed::

            sage: F = GF(11)
            sage: phi = Hom(F,F).an_element()
            sage: R.<x,y> = F[]
            sage: x.change_ring(phi)
            x"""
    @overload
    def change_ring(self, SR) -> Any:
        """MPolynomial.change_ring(self, R)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 890)

        Return this polynomial with coefficients converted to ``R``.

        INPUT:

        - ``R`` -- a ring or morphism; if a morphism, the coefficients
          are mapped to the codomain of ``R``

        OUTPUT: a new polynomial with the base ring changed to ``R``

        EXAMPLES::

            sage: R.<x,y> = QQ[]
            sage: f = x^3 + 3/5*y + 1
            sage: f.change_ring(GF(7))
            x^3 + 2*y + 1
            sage: g = x^2 + 5*y
            sage: g.change_ring(GF(5))
            x^2

        ::

            sage: # needs sage.rings.finite_rings
            sage: R.<x,y> = GF(9,'a')[]
            sage: (x+2*y).change_ring(GF(3))
            x - y

        ::

            sage: # needs sage.rings.finite_rings
            sage: F.<a> = GF(7^2)
            sage: R.<x,y> = F[]
            sage: f = x^2 + a^2*y^2 + a*x + a^3*y
            sage: g = f.change_ring(F.frobenius_endomorphism()); g
            x^2 + (-a - 2)*y^2 + (-a + 1)*x + (2*a + 2)*y
            sage: g.change_ring(F.frobenius_endomorphism()) == f
            True

        ::

            sage: # needs sage.rings.number_field
            sage: K.<z> = CyclotomicField(3)
            sage: R.<x,y> = K[]
            sage: f = x^2 + z*y
            sage: f.change_ring(K.embeddings(CC)[1])
            x^2 + (-0.500000000000000 - 0.866025403784438*I)*y

        ::

            sage: # needs sage.rings.number_field
            sage: K.<w> = CyclotomicField(5)
            sage: R.<x,y> = K[]
            sage: f = x^2 + w*y
            sage: f.change_ring(K.embeddings(QQbar)[1])
            x^2 + (-0.8090169943749474? + 0.5877852522924731?*I)*y

        TESTS:

        Check that :issue:`25022` is fixed::

            sage: # needs sage.rings.number_field sage.symbolic
            sage: K.<x,y> = ZZ[]
            sage: (x*y).change_ring(SR).monomials()
            [x*y]

        Check that :issue:`36832` is fixed::

            sage: F = GF(11)
            sage: phi = Hom(F,F).an_element()
            sage: R.<x,y> = F[]
            sage: x.change_ring(phi)
            x"""
    @overload
    def change_ring(self, phi) -> Any:
        """MPolynomial.change_ring(self, R)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 890)

        Return this polynomial with coefficients converted to ``R``.

        INPUT:

        - ``R`` -- a ring or morphism; if a morphism, the coefficients
          are mapped to the codomain of ``R``

        OUTPUT: a new polynomial with the base ring changed to ``R``

        EXAMPLES::

            sage: R.<x,y> = QQ[]
            sage: f = x^3 + 3/5*y + 1
            sage: f.change_ring(GF(7))
            x^3 + 2*y + 1
            sage: g = x^2 + 5*y
            sage: g.change_ring(GF(5))
            x^2

        ::

            sage: # needs sage.rings.finite_rings
            sage: R.<x,y> = GF(9,'a')[]
            sage: (x+2*y).change_ring(GF(3))
            x - y

        ::

            sage: # needs sage.rings.finite_rings
            sage: F.<a> = GF(7^2)
            sage: R.<x,y> = F[]
            sage: f = x^2 + a^2*y^2 + a*x + a^3*y
            sage: g = f.change_ring(F.frobenius_endomorphism()); g
            x^2 + (-a - 2)*y^2 + (-a + 1)*x + (2*a + 2)*y
            sage: g.change_ring(F.frobenius_endomorphism()) == f
            True

        ::

            sage: # needs sage.rings.number_field
            sage: K.<z> = CyclotomicField(3)
            sage: R.<x,y> = K[]
            sage: f = x^2 + z*y
            sage: f.change_ring(K.embeddings(CC)[1])
            x^2 + (-0.500000000000000 - 0.866025403784438*I)*y

        ::

            sage: # needs sage.rings.number_field
            sage: K.<w> = CyclotomicField(5)
            sage: R.<x,y> = K[]
            sage: f = x^2 + w*y
            sage: f.change_ring(K.embeddings(QQbar)[1])
            x^2 + (-0.8090169943749474? + 0.5877852522924731?*I)*y

        TESTS:

        Check that :issue:`25022` is fixed::

            sage: # needs sage.rings.number_field sage.symbolic
            sage: K.<x,y> = ZZ[]
            sage: (x*y).change_ring(SR).monomials()
            [x*y]

        Check that :issue:`36832` is fixed::

            sage: F = GF(11)
            sage: phi = Hom(F,F).an_element()
            sage: R.<x,y> = F[]
            sage: x.change_ring(phi)
            x"""
    @overload
    def coefficients(self) -> Any:
        """MPolynomial.coefficients(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 261)

        Return the nonzero coefficients of this polynomial in a list.

        The returned list is decreasingly ordered by the term ordering
        of ``self.parent()``, i.e. the list of coefficients matches the list
        of monomials returned by
        :meth:`sage.rings.polynomial.multi_polynomial_libsingular.MPolynomial_libsingular.monomials`.

        EXAMPLES::

            sage: R.<x,y,z> = PolynomialRing(QQ, 3, order='degrevlex')
            sage: f = 23*x^6*y^7 + x^3*y+6*x^7*z
            sage: f.coefficients()
            [23, 6, 1]
            sage: R.<x,y,z> = PolynomialRing(QQ, 3, order='lex')
            sage: f = 23*x^6*y^7 + x^3*y+6*x^7*z
            sage: f.coefficients()
            [6, 23, 1]

        Test the same stuff with base ring `\\ZZ` -- different implementation::

            sage: R.<x,y,z> = PolynomialRing(ZZ, 3, order='degrevlex')
            sage: f = 23*x^6*y^7 + x^3*y+6*x^7*z
            sage: f.coefficients()
            [23, 6, 1]
            sage: R.<x,y,z> = PolynomialRing(ZZ, 3, order='lex')
            sage: f = 23*x^6*y^7 + x^3*y+6*x^7*z
            sage: f.coefficients()
            [6, 23, 1]

        AUTHOR:

        - Didier Deshommes"""
    @overload
    def coefficients(self) -> Any:
        """MPolynomial.coefficients(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 261)

        Return the nonzero coefficients of this polynomial in a list.

        The returned list is decreasingly ordered by the term ordering
        of ``self.parent()``, i.e. the list of coefficients matches the list
        of monomials returned by
        :meth:`sage.rings.polynomial.multi_polynomial_libsingular.MPolynomial_libsingular.monomials`.

        EXAMPLES::

            sage: R.<x,y,z> = PolynomialRing(QQ, 3, order='degrevlex')
            sage: f = 23*x^6*y^7 + x^3*y+6*x^7*z
            sage: f.coefficients()
            [23, 6, 1]
            sage: R.<x,y,z> = PolynomialRing(QQ, 3, order='lex')
            sage: f = 23*x^6*y^7 + x^3*y+6*x^7*z
            sage: f.coefficients()
            [6, 23, 1]

        Test the same stuff with base ring `\\ZZ` -- different implementation::

            sage: R.<x,y,z> = PolynomialRing(ZZ, 3, order='degrevlex')
            sage: f = 23*x^6*y^7 + x^3*y+6*x^7*z
            sage: f.coefficients()
            [23, 6, 1]
            sage: R.<x,y,z> = PolynomialRing(ZZ, 3, order='lex')
            sage: f = 23*x^6*y^7 + x^3*y+6*x^7*z
            sage: f.coefficients()
            [6, 23, 1]

        AUTHOR:

        - Didier Deshommes"""
    @overload
    def coefficients(self) -> Any:
        """MPolynomial.coefficients(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 261)

        Return the nonzero coefficients of this polynomial in a list.

        The returned list is decreasingly ordered by the term ordering
        of ``self.parent()``, i.e. the list of coefficients matches the list
        of monomials returned by
        :meth:`sage.rings.polynomial.multi_polynomial_libsingular.MPolynomial_libsingular.monomials`.

        EXAMPLES::

            sage: R.<x,y,z> = PolynomialRing(QQ, 3, order='degrevlex')
            sage: f = 23*x^6*y^7 + x^3*y+6*x^7*z
            sage: f.coefficients()
            [23, 6, 1]
            sage: R.<x,y,z> = PolynomialRing(QQ, 3, order='lex')
            sage: f = 23*x^6*y^7 + x^3*y+6*x^7*z
            sage: f.coefficients()
            [6, 23, 1]

        Test the same stuff with base ring `\\ZZ` -- different implementation::

            sage: R.<x,y,z> = PolynomialRing(ZZ, 3, order='degrevlex')
            sage: f = 23*x^6*y^7 + x^3*y+6*x^7*z
            sage: f.coefficients()
            [23, 6, 1]
            sage: R.<x,y,z> = PolynomialRing(ZZ, 3, order='lex')
            sage: f = 23*x^6*y^7 + x^3*y+6*x^7*z
            sage: f.coefficients()
            [6, 23, 1]

        AUTHOR:

        - Didier Deshommes"""
    @overload
    def content(self) -> Any:
        """MPolynomial.content(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 1284)

        Return the content of this polynomial.  Here, we define content as
        the gcd of the coefficients in the base ring.

        .. SEEALSO::

            :meth:`content_ideal`

        EXAMPLES::

            sage: R.<x,y> = ZZ[]
            sage: f = 4*x+6*y
            sage: f.content()
            2
            sage: f.content().parent()
            Integer Ring

        TESTS:

        Since :issue:`10771`, the gcd in QQ restricts to the gcd in ZZ::

            sage: R.<x,y> = QQ[]
            sage: f = 4*x+6*y
            sage: f.content(); f.content().parent()
            2
            Rational Field"""
    @overload
    def content(self) -> Any:
        """MPolynomial.content(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 1284)

        Return the content of this polynomial.  Here, we define content as
        the gcd of the coefficients in the base ring.

        .. SEEALSO::

            :meth:`content_ideal`

        EXAMPLES::

            sage: R.<x,y> = ZZ[]
            sage: f = 4*x+6*y
            sage: f.content()
            2
            sage: f.content().parent()
            Integer Ring

        TESTS:

        Since :issue:`10771`, the gcd in QQ restricts to the gcd in ZZ::

            sage: R.<x,y> = QQ[]
            sage: f = 4*x+6*y
            sage: f.content(); f.content().parent()
            2
            Rational Field"""
    @overload
    def content(self) -> Any:
        """MPolynomial.content(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 1284)

        Return the content of this polynomial.  Here, we define content as
        the gcd of the coefficients in the base ring.

        .. SEEALSO::

            :meth:`content_ideal`

        EXAMPLES::

            sage: R.<x,y> = ZZ[]
            sage: f = 4*x+6*y
            sage: f.content()
            2
            sage: f.content().parent()
            Integer Ring

        TESTS:

        Since :issue:`10771`, the gcd in QQ restricts to the gcd in ZZ::

            sage: R.<x,y> = QQ[]
            sage: f = 4*x+6*y
            sage: f.content(); f.content().parent()
            2
            Rational Field"""
    @overload
    def content(self) -> Any:
        """MPolynomial.content(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 1284)

        Return the content of this polynomial.  Here, we define content as
        the gcd of the coefficients in the base ring.

        .. SEEALSO::

            :meth:`content_ideal`

        EXAMPLES::

            sage: R.<x,y> = ZZ[]
            sage: f = 4*x+6*y
            sage: f.content()
            2
            sage: f.content().parent()
            Integer Ring

        TESTS:

        Since :issue:`10771`, the gcd in QQ restricts to the gcd in ZZ::

            sage: R.<x,y> = QQ[]
            sage: f = 4*x+6*y
            sage: f.content(); f.content().parent()
            2
            Rational Field"""
    @overload
    def content_ideal(self) -> Any:
        """MPolynomial.content_ideal(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 1315)

        Return the content ideal of this polynomial, defined as the ideal
        generated by its coefficients.

        .. SEEALSO::

            :meth:`content`

        EXAMPLES::

            sage: R.<x,y> = ZZ[]
            sage: f = 2*x*y + 6*x - 4*y + 2
            sage: f.content_ideal()
            Principal ideal (2) of Integer Ring
            sage: S.<z,t> = R[]
            sage: g = x*z + y*t
            sage: g.content_ideal()
            Ideal (x, y) of Multivariate Polynomial Ring in x, y over Integer Ring"""
    @overload
    def content_ideal(self) -> Any:
        """MPolynomial.content_ideal(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 1315)

        Return the content ideal of this polynomial, defined as the ideal
        generated by its coefficients.

        .. SEEALSO::

            :meth:`content`

        EXAMPLES::

            sage: R.<x,y> = ZZ[]
            sage: f = 2*x*y + 6*x - 4*y + 2
            sage: f.content_ideal()
            Principal ideal (2) of Integer Ring
            sage: S.<z,t> = R[]
            sage: g = x*z + y*t
            sage: g.content_ideal()
            Ideal (x, y) of Multivariate Polynomial Ring in x, y over Integer Ring"""
    @overload
    def content_ideal(self) -> Any:
        """MPolynomial.content_ideal(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 1315)

        Return the content ideal of this polynomial, defined as the ideal
        generated by its coefficients.

        .. SEEALSO::

            :meth:`content`

        EXAMPLES::

            sage: R.<x,y> = ZZ[]
            sage: f = 2*x*y + 6*x - 4*y + 2
            sage: f.content_ideal()
            Principal ideal (2) of Integer Ring
            sage: S.<z,t> = R[]
            sage: g = x*z + y*t
            sage: g.content_ideal()
            Ideal (x, y) of Multivariate Polynomial Ring in x, y over Integer Ring"""
    def crt(self, y, m, n) -> Any:
        '''MPolynomial.crt(self, y, m, n)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 2906)

        Return a polynomial congruent to ``self`` modulo ``m`` and
        to ``y`` modulo ``n``.

        INPUT:

        - ``y`` -- a polynomial in the same ring as ``self``
        - ``m``, ``n`` -- polynomials or ideals in the same ring as ``self``; ideals
          may also be specified as a list/tuple of generators

        EXAMPLES::

            sage: R.<x> = PolynomialRing(QQ, implementation="singular")
            sage: f = R(3)
            sage: f.crt(5, x-1, x-2) % ((x-1)*(x-2))
            2*x + 1
            sage: f.crt(5, R.ideal(x-1), [x-2]) % ((x-1)*(x-2))
            2*x + 1'''
    @overload
    def denominator(self) -> Any:
        """MPolynomial.denominator(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 1829)

        Return a denominator of ``self``.

        First, the lcm of the denominators of the entries of ``self``
        is computed and returned. If this computation fails, the
        unit of the parent of ``self`` is returned.

        Note that some subclasses may implement its own denominator
        function.

        .. warning::

           This is not the denominator of the rational function
           defined by ``self``, which would always be 1 since ``self`` is a
           polynomial.

        EXAMPLES:

        First we compute the denominator of a polynomial with
        integer coefficients, which is of course 1.

        ::

            sage: R.<x,y> = ZZ[]
            sage: f = x^3 + 17*y + x + y
            sage: f.denominator()
            1

        Next we compute the denominator of a polynomial over a number field.

        ::

            sage: # needs sage.rings.number_field sage.symbolic
            sage: R.<x,y> = NumberField(symbolic_expression(x^2+3),'a')['x,y']
            sage: f = (1/17)*x^19 + (1/6)*y - (2/3)*x + 1/3; f
            1/17*x^19 - 2/3*x + 1/6*y + 1/3
            sage: f.denominator()
            102

        Finally, we try to compute the denominator of a polynomial with
        coefficients in the real numbers, which is a ring whose elements do
        not have a denominator method.

        ::

            sage: # needs sage.rings.real_mpfr
            sage: R.<a,b,c> = RR[]
            sage: f = a + b + RR('0.3'); f
            a + b + 0.300000000000000
            sage: f.denominator()
            1.00000000000000

        Check that the denominator is an element over the base whenever the base
        has no denominator function. This closes :issue:`9063`::

            sage: R.<a,b,c> = GF(5)[]
            sage: x = R(0)
            sage: x.denominator()
            1
            sage: type(x.denominator())
            <class 'sage.rings.finite_rings.integer_mod.IntegerMod_int'>
            sage: type(a.denominator())
            <class 'sage.rings.finite_rings.integer_mod.IntegerMod_int'>
            sage: from sage.rings.polynomial.multi_polynomial_element import MPolynomial
            sage: isinstance(a / b, MPolynomial)
            False
            sage: isinstance(a.numerator() / a.denominator(), MPolynomial)
            True"""
    @overload
    def denominator(self) -> Any:
        """MPolynomial.denominator(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 1829)

        Return a denominator of ``self``.

        First, the lcm of the denominators of the entries of ``self``
        is computed and returned. If this computation fails, the
        unit of the parent of ``self`` is returned.

        Note that some subclasses may implement its own denominator
        function.

        .. warning::

           This is not the denominator of the rational function
           defined by ``self``, which would always be 1 since ``self`` is a
           polynomial.

        EXAMPLES:

        First we compute the denominator of a polynomial with
        integer coefficients, which is of course 1.

        ::

            sage: R.<x,y> = ZZ[]
            sage: f = x^3 + 17*y + x + y
            sage: f.denominator()
            1

        Next we compute the denominator of a polynomial over a number field.

        ::

            sage: # needs sage.rings.number_field sage.symbolic
            sage: R.<x,y> = NumberField(symbolic_expression(x^2+3),'a')['x,y']
            sage: f = (1/17)*x^19 + (1/6)*y - (2/3)*x + 1/3; f
            1/17*x^19 - 2/3*x + 1/6*y + 1/3
            sage: f.denominator()
            102

        Finally, we try to compute the denominator of a polynomial with
        coefficients in the real numbers, which is a ring whose elements do
        not have a denominator method.

        ::

            sage: # needs sage.rings.real_mpfr
            sage: R.<a,b,c> = RR[]
            sage: f = a + b + RR('0.3'); f
            a + b + 0.300000000000000
            sage: f.denominator()
            1.00000000000000

        Check that the denominator is an element over the base whenever the base
        has no denominator function. This closes :issue:`9063`::

            sage: R.<a,b,c> = GF(5)[]
            sage: x = R(0)
            sage: x.denominator()
            1
            sage: type(x.denominator())
            <class 'sage.rings.finite_rings.integer_mod.IntegerMod_int'>
            sage: type(a.denominator())
            <class 'sage.rings.finite_rings.integer_mod.IntegerMod_int'>
            sage: from sage.rings.polynomial.multi_polynomial_element import MPolynomial
            sage: isinstance(a / b, MPolynomial)
            False
            sage: isinstance(a.numerator() / a.denominator(), MPolynomial)
            True"""
    @overload
    def denominator(self) -> Any:
        """MPolynomial.denominator(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 1829)

        Return a denominator of ``self``.

        First, the lcm of the denominators of the entries of ``self``
        is computed and returned. If this computation fails, the
        unit of the parent of ``self`` is returned.

        Note that some subclasses may implement its own denominator
        function.

        .. warning::

           This is not the denominator of the rational function
           defined by ``self``, which would always be 1 since ``self`` is a
           polynomial.

        EXAMPLES:

        First we compute the denominator of a polynomial with
        integer coefficients, which is of course 1.

        ::

            sage: R.<x,y> = ZZ[]
            sage: f = x^3 + 17*y + x + y
            sage: f.denominator()
            1

        Next we compute the denominator of a polynomial over a number field.

        ::

            sage: # needs sage.rings.number_field sage.symbolic
            sage: R.<x,y> = NumberField(symbolic_expression(x^2+3),'a')['x,y']
            sage: f = (1/17)*x^19 + (1/6)*y - (2/3)*x + 1/3; f
            1/17*x^19 - 2/3*x + 1/6*y + 1/3
            sage: f.denominator()
            102

        Finally, we try to compute the denominator of a polynomial with
        coefficients in the real numbers, which is a ring whose elements do
        not have a denominator method.

        ::

            sage: # needs sage.rings.real_mpfr
            sage: R.<a,b,c> = RR[]
            sage: f = a + b + RR('0.3'); f
            a + b + 0.300000000000000
            sage: f.denominator()
            1.00000000000000

        Check that the denominator is an element over the base whenever the base
        has no denominator function. This closes :issue:`9063`::

            sage: R.<a,b,c> = GF(5)[]
            sage: x = R(0)
            sage: x.denominator()
            1
            sage: type(x.denominator())
            <class 'sage.rings.finite_rings.integer_mod.IntegerMod_int'>
            sage: type(a.denominator())
            <class 'sage.rings.finite_rings.integer_mod.IntegerMod_int'>
            sage: from sage.rings.polynomial.multi_polynomial_element import MPolynomial
            sage: isinstance(a / b, MPolynomial)
            False
            sage: isinstance(a.numerator() / a.denominator(), MPolynomial)
            True"""
    @overload
    def denominator(self) -> Any:
        """MPolynomial.denominator(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 1829)

        Return a denominator of ``self``.

        First, the lcm of the denominators of the entries of ``self``
        is computed and returned. If this computation fails, the
        unit of the parent of ``self`` is returned.

        Note that some subclasses may implement its own denominator
        function.

        .. warning::

           This is not the denominator of the rational function
           defined by ``self``, which would always be 1 since ``self`` is a
           polynomial.

        EXAMPLES:

        First we compute the denominator of a polynomial with
        integer coefficients, which is of course 1.

        ::

            sage: R.<x,y> = ZZ[]
            sage: f = x^3 + 17*y + x + y
            sage: f.denominator()
            1

        Next we compute the denominator of a polynomial over a number field.

        ::

            sage: # needs sage.rings.number_field sage.symbolic
            sage: R.<x,y> = NumberField(symbolic_expression(x^2+3),'a')['x,y']
            sage: f = (1/17)*x^19 + (1/6)*y - (2/3)*x + 1/3; f
            1/17*x^19 - 2/3*x + 1/6*y + 1/3
            sage: f.denominator()
            102

        Finally, we try to compute the denominator of a polynomial with
        coefficients in the real numbers, which is a ring whose elements do
        not have a denominator method.

        ::

            sage: # needs sage.rings.real_mpfr
            sage: R.<a,b,c> = RR[]
            sage: f = a + b + RR('0.3'); f
            a + b + 0.300000000000000
            sage: f.denominator()
            1.00000000000000

        Check that the denominator is an element over the base whenever the base
        has no denominator function. This closes :issue:`9063`::

            sage: R.<a,b,c> = GF(5)[]
            sage: x = R(0)
            sage: x.denominator()
            1
            sage: type(x.denominator())
            <class 'sage.rings.finite_rings.integer_mod.IntegerMod_int'>
            sage: type(a.denominator())
            <class 'sage.rings.finite_rings.integer_mod.IntegerMod_int'>
            sage: from sage.rings.polynomial.multi_polynomial_element import MPolynomial
            sage: isinstance(a / b, MPolynomial)
            False
            sage: isinstance(a.numerator() / a.denominator(), MPolynomial)
            True"""
    @overload
    def denominator(self) -> Any:
        """MPolynomial.denominator(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 1829)

        Return a denominator of ``self``.

        First, the lcm of the denominators of the entries of ``self``
        is computed and returned. If this computation fails, the
        unit of the parent of ``self`` is returned.

        Note that some subclasses may implement its own denominator
        function.

        .. warning::

           This is not the denominator of the rational function
           defined by ``self``, which would always be 1 since ``self`` is a
           polynomial.

        EXAMPLES:

        First we compute the denominator of a polynomial with
        integer coefficients, which is of course 1.

        ::

            sage: R.<x,y> = ZZ[]
            sage: f = x^3 + 17*y + x + y
            sage: f.denominator()
            1

        Next we compute the denominator of a polynomial over a number field.

        ::

            sage: # needs sage.rings.number_field sage.symbolic
            sage: R.<x,y> = NumberField(symbolic_expression(x^2+3),'a')['x,y']
            sage: f = (1/17)*x^19 + (1/6)*y - (2/3)*x + 1/3; f
            1/17*x^19 - 2/3*x + 1/6*y + 1/3
            sage: f.denominator()
            102

        Finally, we try to compute the denominator of a polynomial with
        coefficients in the real numbers, which is a ring whose elements do
        not have a denominator method.

        ::

            sage: # needs sage.rings.real_mpfr
            sage: R.<a,b,c> = RR[]
            sage: f = a + b + RR('0.3'); f
            a + b + 0.300000000000000
            sage: f.denominator()
            1.00000000000000

        Check that the denominator is an element over the base whenever the base
        has no denominator function. This closes :issue:`9063`::

            sage: R.<a,b,c> = GF(5)[]
            sage: x = R(0)
            sage: x.denominator()
            1
            sage: type(x.denominator())
            <class 'sage.rings.finite_rings.integer_mod.IntegerMod_int'>
            sage: type(a.denominator())
            <class 'sage.rings.finite_rings.integer_mod.IntegerMod_int'>
            sage: from sage.rings.polynomial.multi_polynomial_element import MPolynomial
            sage: isinstance(a / b, MPolynomial)
            False
            sage: isinstance(a.numerator() / a.denominator(), MPolynomial)
            True"""
    @overload
    def denominator(self) -> Any:
        """MPolynomial.denominator(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 1829)

        Return a denominator of ``self``.

        First, the lcm of the denominators of the entries of ``self``
        is computed and returned. If this computation fails, the
        unit of the parent of ``self`` is returned.

        Note that some subclasses may implement its own denominator
        function.

        .. warning::

           This is not the denominator of the rational function
           defined by ``self``, which would always be 1 since ``self`` is a
           polynomial.

        EXAMPLES:

        First we compute the denominator of a polynomial with
        integer coefficients, which is of course 1.

        ::

            sage: R.<x,y> = ZZ[]
            sage: f = x^3 + 17*y + x + y
            sage: f.denominator()
            1

        Next we compute the denominator of a polynomial over a number field.

        ::

            sage: # needs sage.rings.number_field sage.symbolic
            sage: R.<x,y> = NumberField(symbolic_expression(x^2+3),'a')['x,y']
            sage: f = (1/17)*x^19 + (1/6)*y - (2/3)*x + 1/3; f
            1/17*x^19 - 2/3*x + 1/6*y + 1/3
            sage: f.denominator()
            102

        Finally, we try to compute the denominator of a polynomial with
        coefficients in the real numbers, which is a ring whose elements do
        not have a denominator method.

        ::

            sage: # needs sage.rings.real_mpfr
            sage: R.<a,b,c> = RR[]
            sage: f = a + b + RR('0.3'); f
            a + b + 0.300000000000000
            sage: f.denominator()
            1.00000000000000

        Check that the denominator is an element over the base whenever the base
        has no denominator function. This closes :issue:`9063`::

            sage: R.<a,b,c> = GF(5)[]
            sage: x = R(0)
            sage: x.denominator()
            1
            sage: type(x.denominator())
            <class 'sage.rings.finite_rings.integer_mod.IntegerMod_int'>
            sage: type(a.denominator())
            <class 'sage.rings.finite_rings.integer_mod.IntegerMod_int'>
            sage: from sage.rings.polynomial.multi_polynomial_element import MPolynomial
            sage: isinstance(a / b, MPolynomial)
            False
            sage: isinstance(a.numerator() / a.denominator(), MPolynomial)
            True"""
    @overload
    def denominator(self) -> Any:
        """MPolynomial.denominator(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 1829)

        Return a denominator of ``self``.

        First, the lcm of the denominators of the entries of ``self``
        is computed and returned. If this computation fails, the
        unit of the parent of ``self`` is returned.

        Note that some subclasses may implement its own denominator
        function.

        .. warning::

           This is not the denominator of the rational function
           defined by ``self``, which would always be 1 since ``self`` is a
           polynomial.

        EXAMPLES:

        First we compute the denominator of a polynomial with
        integer coefficients, which is of course 1.

        ::

            sage: R.<x,y> = ZZ[]
            sage: f = x^3 + 17*y + x + y
            sage: f.denominator()
            1

        Next we compute the denominator of a polynomial over a number field.

        ::

            sage: # needs sage.rings.number_field sage.symbolic
            sage: R.<x,y> = NumberField(symbolic_expression(x^2+3),'a')['x,y']
            sage: f = (1/17)*x^19 + (1/6)*y - (2/3)*x + 1/3; f
            1/17*x^19 - 2/3*x + 1/6*y + 1/3
            sage: f.denominator()
            102

        Finally, we try to compute the denominator of a polynomial with
        coefficients in the real numbers, which is a ring whose elements do
        not have a denominator method.

        ::

            sage: # needs sage.rings.real_mpfr
            sage: R.<a,b,c> = RR[]
            sage: f = a + b + RR('0.3'); f
            a + b + 0.300000000000000
            sage: f.denominator()
            1.00000000000000

        Check that the denominator is an element over the base whenever the base
        has no denominator function. This closes :issue:`9063`::

            sage: R.<a,b,c> = GF(5)[]
            sage: x = R(0)
            sage: x.denominator()
            1
            sage: type(x.denominator())
            <class 'sage.rings.finite_rings.integer_mod.IntegerMod_int'>
            sage: type(a.denominator())
            <class 'sage.rings.finite_rings.integer_mod.IntegerMod_int'>
            sage: from sage.rings.polynomial.multi_polynomial_element import MPolynomial
            sage: isinstance(a / b, MPolynomial)
            False
            sage: isinstance(a.numerator() / a.denominator(), MPolynomial)
            True"""
    @overload
    def denominator(self) -> Any:
        """MPolynomial.denominator(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 1829)

        Return a denominator of ``self``.

        First, the lcm of the denominators of the entries of ``self``
        is computed and returned. If this computation fails, the
        unit of the parent of ``self`` is returned.

        Note that some subclasses may implement its own denominator
        function.

        .. warning::

           This is not the denominator of the rational function
           defined by ``self``, which would always be 1 since ``self`` is a
           polynomial.

        EXAMPLES:

        First we compute the denominator of a polynomial with
        integer coefficients, which is of course 1.

        ::

            sage: R.<x,y> = ZZ[]
            sage: f = x^3 + 17*y + x + y
            sage: f.denominator()
            1

        Next we compute the denominator of a polynomial over a number field.

        ::

            sage: # needs sage.rings.number_field sage.symbolic
            sage: R.<x,y> = NumberField(symbolic_expression(x^2+3),'a')['x,y']
            sage: f = (1/17)*x^19 + (1/6)*y - (2/3)*x + 1/3; f
            1/17*x^19 - 2/3*x + 1/6*y + 1/3
            sage: f.denominator()
            102

        Finally, we try to compute the denominator of a polynomial with
        coefficients in the real numbers, which is a ring whose elements do
        not have a denominator method.

        ::

            sage: # needs sage.rings.real_mpfr
            sage: R.<a,b,c> = RR[]
            sage: f = a + b + RR('0.3'); f
            a + b + 0.300000000000000
            sage: f.denominator()
            1.00000000000000

        Check that the denominator is an element over the base whenever the base
        has no denominator function. This closes :issue:`9063`::

            sage: R.<a,b,c> = GF(5)[]
            sage: x = R(0)
            sage: x.denominator()
            1
            sage: type(x.denominator())
            <class 'sage.rings.finite_rings.integer_mod.IntegerMod_int'>
            sage: type(a.denominator())
            <class 'sage.rings.finite_rings.integer_mod.IntegerMod_int'>
            sage: from sage.rings.polynomial.multi_polynomial_element import MPolynomial
            sage: isinstance(a / b, MPolynomial)
            False
            sage: isinstance(a.numerator() / a.denominator(), MPolynomial)
            True"""
    @overload
    def derivative(self, *args) -> Any:
        '''MPolynomial.derivative(self, *args)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 358)

        The formal derivative of this polynomial, with respect to
        variables supplied in ``args``.

        Multiple variables and iteration counts may be supplied; see
        documentation for the global function :func:`derivative` for more details.

        .. SEEALSO:: :meth:`._derivative`

        EXAMPLES:

        Polynomials implemented via Singular::

            sage: # needs sage.libs.singular
            sage: R.<x, y> = PolynomialRing(FiniteField(5))
            sage: f = x^3*y^5 + x^7*y
            sage: type(f)
            <class \'sage.rings.polynomial.multi_polynomial_libsingular.MPolynomial_libsingular\'>
            sage: f.derivative(x)
            2*x^6*y - 2*x^2*y^5
            sage: f.derivative(y)
            x^7

        Generic multivariate polynomials::

            sage: R.<t> = PowerSeriesRing(QQ)
            sage: S.<x, y> = PolynomialRing(R)
            sage: f = (t^2 + O(t^3))*x^2*y^3 + (37*t^4 + O(t^5))*x^3
            sage: type(f)
            <class \'sage.rings.polynomial.multi_polynomial_element.MPolynomial_polydict\'>
            sage: f.derivative(x)       # with respect to x
            (2*t^2 + O(t^3))*x*y^3 + (111*t^4 + O(t^5))*x^2
            sage: f.derivative(y)       # with respect to y
            (3*t^2 + O(t^3))*x^2*y^2
            sage: f.derivative(t)       # with respect to t (recurses into base ring)
            (2*t + O(t^2))*x^2*y^3 + (148*t^3 + O(t^4))*x^3
            sage: f.derivative(x, y)    # with respect to x and then y
            (6*t^2 + O(t^3))*x*y^2
            sage: f.derivative(y, 3)    # with respect to y three times
            (6*t^2 + O(t^3))*x^2
            sage: f.derivative()        # can\'t figure out the variable
            Traceback (most recent call last):
            ...
            ValueError: must specify which variable to differentiate with respect to

        Polynomials over the symbolic ring (just for fun....)::

            sage: # needs sage.symbolic
            sage: x = var("x")
            sage: S.<u, v> = PolynomialRing(SR)
            sage: f = u*v*x
            sage: f.derivative(x) == u*v
            True
            sage: f.derivative(u) == v*x
            True'''
    @overload
    def derivative(self, x) -> Any:
        '''MPolynomial.derivative(self, *args)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 358)

        The formal derivative of this polynomial, with respect to
        variables supplied in ``args``.

        Multiple variables and iteration counts may be supplied; see
        documentation for the global function :func:`derivative` for more details.

        .. SEEALSO:: :meth:`._derivative`

        EXAMPLES:

        Polynomials implemented via Singular::

            sage: # needs sage.libs.singular
            sage: R.<x, y> = PolynomialRing(FiniteField(5))
            sage: f = x^3*y^5 + x^7*y
            sage: type(f)
            <class \'sage.rings.polynomial.multi_polynomial_libsingular.MPolynomial_libsingular\'>
            sage: f.derivative(x)
            2*x^6*y - 2*x^2*y^5
            sage: f.derivative(y)
            x^7

        Generic multivariate polynomials::

            sage: R.<t> = PowerSeriesRing(QQ)
            sage: S.<x, y> = PolynomialRing(R)
            sage: f = (t^2 + O(t^3))*x^2*y^3 + (37*t^4 + O(t^5))*x^3
            sage: type(f)
            <class \'sage.rings.polynomial.multi_polynomial_element.MPolynomial_polydict\'>
            sage: f.derivative(x)       # with respect to x
            (2*t^2 + O(t^3))*x*y^3 + (111*t^4 + O(t^5))*x^2
            sage: f.derivative(y)       # with respect to y
            (3*t^2 + O(t^3))*x^2*y^2
            sage: f.derivative(t)       # with respect to t (recurses into base ring)
            (2*t + O(t^2))*x^2*y^3 + (148*t^3 + O(t^4))*x^3
            sage: f.derivative(x, y)    # with respect to x and then y
            (6*t^2 + O(t^3))*x*y^2
            sage: f.derivative(y, 3)    # with respect to y three times
            (6*t^2 + O(t^3))*x^2
            sage: f.derivative()        # can\'t figure out the variable
            Traceback (most recent call last):
            ...
            ValueError: must specify which variable to differentiate with respect to

        Polynomials over the symbolic ring (just for fun....)::

            sage: # needs sage.symbolic
            sage: x = var("x")
            sage: S.<u, v> = PolynomialRing(SR)
            sage: f = u*v*x
            sage: f.derivative(x) == u*v
            True
            sage: f.derivative(u) == v*x
            True'''
    @overload
    def derivative(self, y) -> Any:
        '''MPolynomial.derivative(self, *args)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 358)

        The formal derivative of this polynomial, with respect to
        variables supplied in ``args``.

        Multiple variables and iteration counts may be supplied; see
        documentation for the global function :func:`derivative` for more details.

        .. SEEALSO:: :meth:`._derivative`

        EXAMPLES:

        Polynomials implemented via Singular::

            sage: # needs sage.libs.singular
            sage: R.<x, y> = PolynomialRing(FiniteField(5))
            sage: f = x^3*y^5 + x^7*y
            sage: type(f)
            <class \'sage.rings.polynomial.multi_polynomial_libsingular.MPolynomial_libsingular\'>
            sage: f.derivative(x)
            2*x^6*y - 2*x^2*y^5
            sage: f.derivative(y)
            x^7

        Generic multivariate polynomials::

            sage: R.<t> = PowerSeriesRing(QQ)
            sage: S.<x, y> = PolynomialRing(R)
            sage: f = (t^2 + O(t^3))*x^2*y^3 + (37*t^4 + O(t^5))*x^3
            sage: type(f)
            <class \'sage.rings.polynomial.multi_polynomial_element.MPolynomial_polydict\'>
            sage: f.derivative(x)       # with respect to x
            (2*t^2 + O(t^3))*x*y^3 + (111*t^4 + O(t^5))*x^2
            sage: f.derivative(y)       # with respect to y
            (3*t^2 + O(t^3))*x^2*y^2
            sage: f.derivative(t)       # with respect to t (recurses into base ring)
            (2*t + O(t^2))*x^2*y^3 + (148*t^3 + O(t^4))*x^3
            sage: f.derivative(x, y)    # with respect to x and then y
            (6*t^2 + O(t^3))*x*y^2
            sage: f.derivative(y, 3)    # with respect to y three times
            (6*t^2 + O(t^3))*x^2
            sage: f.derivative()        # can\'t figure out the variable
            Traceback (most recent call last):
            ...
            ValueError: must specify which variable to differentiate with respect to

        Polynomials over the symbolic ring (just for fun....)::

            sage: # needs sage.symbolic
            sage: x = var("x")
            sage: S.<u, v> = PolynomialRing(SR)
            sage: f = u*v*x
            sage: f.derivative(x) == u*v
            True
            sage: f.derivative(u) == v*x
            True'''
    @overload
    def derivative(self, x) -> Any:
        '''MPolynomial.derivative(self, *args)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 358)

        The formal derivative of this polynomial, with respect to
        variables supplied in ``args``.

        Multiple variables and iteration counts may be supplied; see
        documentation for the global function :func:`derivative` for more details.

        .. SEEALSO:: :meth:`._derivative`

        EXAMPLES:

        Polynomials implemented via Singular::

            sage: # needs sage.libs.singular
            sage: R.<x, y> = PolynomialRing(FiniteField(5))
            sage: f = x^3*y^5 + x^7*y
            sage: type(f)
            <class \'sage.rings.polynomial.multi_polynomial_libsingular.MPolynomial_libsingular\'>
            sage: f.derivative(x)
            2*x^6*y - 2*x^2*y^5
            sage: f.derivative(y)
            x^7

        Generic multivariate polynomials::

            sage: R.<t> = PowerSeriesRing(QQ)
            sage: S.<x, y> = PolynomialRing(R)
            sage: f = (t^2 + O(t^3))*x^2*y^3 + (37*t^4 + O(t^5))*x^3
            sage: type(f)
            <class \'sage.rings.polynomial.multi_polynomial_element.MPolynomial_polydict\'>
            sage: f.derivative(x)       # with respect to x
            (2*t^2 + O(t^3))*x*y^3 + (111*t^4 + O(t^5))*x^2
            sage: f.derivative(y)       # with respect to y
            (3*t^2 + O(t^3))*x^2*y^2
            sage: f.derivative(t)       # with respect to t (recurses into base ring)
            (2*t + O(t^2))*x^2*y^3 + (148*t^3 + O(t^4))*x^3
            sage: f.derivative(x, y)    # with respect to x and then y
            (6*t^2 + O(t^3))*x*y^2
            sage: f.derivative(y, 3)    # with respect to y three times
            (6*t^2 + O(t^3))*x^2
            sage: f.derivative()        # can\'t figure out the variable
            Traceback (most recent call last):
            ...
            ValueError: must specify which variable to differentiate with respect to

        Polynomials over the symbolic ring (just for fun....)::

            sage: # needs sage.symbolic
            sage: x = var("x")
            sage: S.<u, v> = PolynomialRing(SR)
            sage: f = u*v*x
            sage: f.derivative(x) == u*v
            True
            sage: f.derivative(u) == v*x
            True'''
    @overload
    def derivative(self, y) -> Any:
        '''MPolynomial.derivative(self, *args)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 358)

        The formal derivative of this polynomial, with respect to
        variables supplied in ``args``.

        Multiple variables and iteration counts may be supplied; see
        documentation for the global function :func:`derivative` for more details.

        .. SEEALSO:: :meth:`._derivative`

        EXAMPLES:

        Polynomials implemented via Singular::

            sage: # needs sage.libs.singular
            sage: R.<x, y> = PolynomialRing(FiniteField(5))
            sage: f = x^3*y^5 + x^7*y
            sage: type(f)
            <class \'sage.rings.polynomial.multi_polynomial_libsingular.MPolynomial_libsingular\'>
            sage: f.derivative(x)
            2*x^6*y - 2*x^2*y^5
            sage: f.derivative(y)
            x^7

        Generic multivariate polynomials::

            sage: R.<t> = PowerSeriesRing(QQ)
            sage: S.<x, y> = PolynomialRing(R)
            sage: f = (t^2 + O(t^3))*x^2*y^3 + (37*t^4 + O(t^5))*x^3
            sage: type(f)
            <class \'sage.rings.polynomial.multi_polynomial_element.MPolynomial_polydict\'>
            sage: f.derivative(x)       # with respect to x
            (2*t^2 + O(t^3))*x*y^3 + (111*t^4 + O(t^5))*x^2
            sage: f.derivative(y)       # with respect to y
            (3*t^2 + O(t^3))*x^2*y^2
            sage: f.derivative(t)       # with respect to t (recurses into base ring)
            (2*t + O(t^2))*x^2*y^3 + (148*t^3 + O(t^4))*x^3
            sage: f.derivative(x, y)    # with respect to x and then y
            (6*t^2 + O(t^3))*x*y^2
            sage: f.derivative(y, 3)    # with respect to y three times
            (6*t^2 + O(t^3))*x^2
            sage: f.derivative()        # can\'t figure out the variable
            Traceback (most recent call last):
            ...
            ValueError: must specify which variable to differentiate with respect to

        Polynomials over the symbolic ring (just for fun....)::

            sage: # needs sage.symbolic
            sage: x = var("x")
            sage: S.<u, v> = PolynomialRing(SR)
            sage: f = u*v*x
            sage: f.derivative(x) == u*v
            True
            sage: f.derivative(u) == v*x
            True'''
    @overload
    def derivative(self, t) -> Any:
        '''MPolynomial.derivative(self, *args)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 358)

        The formal derivative of this polynomial, with respect to
        variables supplied in ``args``.

        Multiple variables and iteration counts may be supplied; see
        documentation for the global function :func:`derivative` for more details.

        .. SEEALSO:: :meth:`._derivative`

        EXAMPLES:

        Polynomials implemented via Singular::

            sage: # needs sage.libs.singular
            sage: R.<x, y> = PolynomialRing(FiniteField(5))
            sage: f = x^3*y^5 + x^7*y
            sage: type(f)
            <class \'sage.rings.polynomial.multi_polynomial_libsingular.MPolynomial_libsingular\'>
            sage: f.derivative(x)
            2*x^6*y - 2*x^2*y^5
            sage: f.derivative(y)
            x^7

        Generic multivariate polynomials::

            sage: R.<t> = PowerSeriesRing(QQ)
            sage: S.<x, y> = PolynomialRing(R)
            sage: f = (t^2 + O(t^3))*x^2*y^3 + (37*t^4 + O(t^5))*x^3
            sage: type(f)
            <class \'sage.rings.polynomial.multi_polynomial_element.MPolynomial_polydict\'>
            sage: f.derivative(x)       # with respect to x
            (2*t^2 + O(t^3))*x*y^3 + (111*t^4 + O(t^5))*x^2
            sage: f.derivative(y)       # with respect to y
            (3*t^2 + O(t^3))*x^2*y^2
            sage: f.derivative(t)       # with respect to t (recurses into base ring)
            (2*t + O(t^2))*x^2*y^3 + (148*t^3 + O(t^4))*x^3
            sage: f.derivative(x, y)    # with respect to x and then y
            (6*t^2 + O(t^3))*x*y^2
            sage: f.derivative(y, 3)    # with respect to y three times
            (6*t^2 + O(t^3))*x^2
            sage: f.derivative()        # can\'t figure out the variable
            Traceback (most recent call last):
            ...
            ValueError: must specify which variable to differentiate with respect to

        Polynomials over the symbolic ring (just for fun....)::

            sage: # needs sage.symbolic
            sage: x = var("x")
            sage: S.<u, v> = PolynomialRing(SR)
            sage: f = u*v*x
            sage: f.derivative(x) == u*v
            True
            sage: f.derivative(u) == v*x
            True'''
    @overload
    def derivative(self, x, y) -> Any:
        '''MPolynomial.derivative(self, *args)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 358)

        The formal derivative of this polynomial, with respect to
        variables supplied in ``args``.

        Multiple variables and iteration counts may be supplied; see
        documentation for the global function :func:`derivative` for more details.

        .. SEEALSO:: :meth:`._derivative`

        EXAMPLES:

        Polynomials implemented via Singular::

            sage: # needs sage.libs.singular
            sage: R.<x, y> = PolynomialRing(FiniteField(5))
            sage: f = x^3*y^5 + x^7*y
            sage: type(f)
            <class \'sage.rings.polynomial.multi_polynomial_libsingular.MPolynomial_libsingular\'>
            sage: f.derivative(x)
            2*x^6*y - 2*x^2*y^5
            sage: f.derivative(y)
            x^7

        Generic multivariate polynomials::

            sage: R.<t> = PowerSeriesRing(QQ)
            sage: S.<x, y> = PolynomialRing(R)
            sage: f = (t^2 + O(t^3))*x^2*y^3 + (37*t^4 + O(t^5))*x^3
            sage: type(f)
            <class \'sage.rings.polynomial.multi_polynomial_element.MPolynomial_polydict\'>
            sage: f.derivative(x)       # with respect to x
            (2*t^2 + O(t^3))*x*y^3 + (111*t^4 + O(t^5))*x^2
            sage: f.derivative(y)       # with respect to y
            (3*t^2 + O(t^3))*x^2*y^2
            sage: f.derivative(t)       # with respect to t (recurses into base ring)
            (2*t + O(t^2))*x^2*y^3 + (148*t^3 + O(t^4))*x^3
            sage: f.derivative(x, y)    # with respect to x and then y
            (6*t^2 + O(t^3))*x*y^2
            sage: f.derivative(y, 3)    # with respect to y three times
            (6*t^2 + O(t^3))*x^2
            sage: f.derivative()        # can\'t figure out the variable
            Traceback (most recent call last):
            ...
            ValueError: must specify which variable to differentiate with respect to

        Polynomials over the symbolic ring (just for fun....)::

            sage: # needs sage.symbolic
            sage: x = var("x")
            sage: S.<u, v> = PolynomialRing(SR)
            sage: f = u*v*x
            sage: f.derivative(x) == u*v
            True
            sage: f.derivative(u) == v*x
            True'''
    @overload
    def derivative(self) -> Any:
        '''MPolynomial.derivative(self, *args)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 358)

        The formal derivative of this polynomial, with respect to
        variables supplied in ``args``.

        Multiple variables and iteration counts may be supplied; see
        documentation for the global function :func:`derivative` for more details.

        .. SEEALSO:: :meth:`._derivative`

        EXAMPLES:

        Polynomials implemented via Singular::

            sage: # needs sage.libs.singular
            sage: R.<x, y> = PolynomialRing(FiniteField(5))
            sage: f = x^3*y^5 + x^7*y
            sage: type(f)
            <class \'sage.rings.polynomial.multi_polynomial_libsingular.MPolynomial_libsingular\'>
            sage: f.derivative(x)
            2*x^6*y - 2*x^2*y^5
            sage: f.derivative(y)
            x^7

        Generic multivariate polynomials::

            sage: R.<t> = PowerSeriesRing(QQ)
            sage: S.<x, y> = PolynomialRing(R)
            sage: f = (t^2 + O(t^3))*x^2*y^3 + (37*t^4 + O(t^5))*x^3
            sage: type(f)
            <class \'sage.rings.polynomial.multi_polynomial_element.MPolynomial_polydict\'>
            sage: f.derivative(x)       # with respect to x
            (2*t^2 + O(t^3))*x*y^3 + (111*t^4 + O(t^5))*x^2
            sage: f.derivative(y)       # with respect to y
            (3*t^2 + O(t^3))*x^2*y^2
            sage: f.derivative(t)       # with respect to t (recurses into base ring)
            (2*t + O(t^2))*x^2*y^3 + (148*t^3 + O(t^4))*x^3
            sage: f.derivative(x, y)    # with respect to x and then y
            (6*t^2 + O(t^3))*x*y^2
            sage: f.derivative(y, 3)    # with respect to y three times
            (6*t^2 + O(t^3))*x^2
            sage: f.derivative()        # can\'t figure out the variable
            Traceback (most recent call last):
            ...
            ValueError: must specify which variable to differentiate with respect to

        Polynomials over the symbolic ring (just for fun....)::

            sage: # needs sage.symbolic
            sage: x = var("x")
            sage: S.<u, v> = PolynomialRing(SR)
            sage: f = u*v*x
            sage: f.derivative(x) == u*v
            True
            sage: f.derivative(u) == v*x
            True'''
    @overload
    def derivative(self, x) -> Any:
        '''MPolynomial.derivative(self, *args)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 358)

        The formal derivative of this polynomial, with respect to
        variables supplied in ``args``.

        Multiple variables and iteration counts may be supplied; see
        documentation for the global function :func:`derivative` for more details.

        .. SEEALSO:: :meth:`._derivative`

        EXAMPLES:

        Polynomials implemented via Singular::

            sage: # needs sage.libs.singular
            sage: R.<x, y> = PolynomialRing(FiniteField(5))
            sage: f = x^3*y^5 + x^7*y
            sage: type(f)
            <class \'sage.rings.polynomial.multi_polynomial_libsingular.MPolynomial_libsingular\'>
            sage: f.derivative(x)
            2*x^6*y - 2*x^2*y^5
            sage: f.derivative(y)
            x^7

        Generic multivariate polynomials::

            sage: R.<t> = PowerSeriesRing(QQ)
            sage: S.<x, y> = PolynomialRing(R)
            sage: f = (t^2 + O(t^3))*x^2*y^3 + (37*t^4 + O(t^5))*x^3
            sage: type(f)
            <class \'sage.rings.polynomial.multi_polynomial_element.MPolynomial_polydict\'>
            sage: f.derivative(x)       # with respect to x
            (2*t^2 + O(t^3))*x*y^3 + (111*t^4 + O(t^5))*x^2
            sage: f.derivative(y)       # with respect to y
            (3*t^2 + O(t^3))*x^2*y^2
            sage: f.derivative(t)       # with respect to t (recurses into base ring)
            (2*t + O(t^2))*x^2*y^3 + (148*t^3 + O(t^4))*x^3
            sage: f.derivative(x, y)    # with respect to x and then y
            (6*t^2 + O(t^3))*x*y^2
            sage: f.derivative(y, 3)    # with respect to y three times
            (6*t^2 + O(t^3))*x^2
            sage: f.derivative()        # can\'t figure out the variable
            Traceback (most recent call last):
            ...
            ValueError: must specify which variable to differentiate with respect to

        Polynomials over the symbolic ring (just for fun....)::

            sage: # needs sage.symbolic
            sage: x = var("x")
            sage: S.<u, v> = PolynomialRing(SR)
            sage: f = u*v*x
            sage: f.derivative(x) == u*v
            True
            sage: f.derivative(u) == v*x
            True'''
    @overload
    def derivative(self, u) -> Any:
        '''MPolynomial.derivative(self, *args)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 358)

        The formal derivative of this polynomial, with respect to
        variables supplied in ``args``.

        Multiple variables and iteration counts may be supplied; see
        documentation for the global function :func:`derivative` for more details.

        .. SEEALSO:: :meth:`._derivative`

        EXAMPLES:

        Polynomials implemented via Singular::

            sage: # needs sage.libs.singular
            sage: R.<x, y> = PolynomialRing(FiniteField(5))
            sage: f = x^3*y^5 + x^7*y
            sage: type(f)
            <class \'sage.rings.polynomial.multi_polynomial_libsingular.MPolynomial_libsingular\'>
            sage: f.derivative(x)
            2*x^6*y - 2*x^2*y^5
            sage: f.derivative(y)
            x^7

        Generic multivariate polynomials::

            sage: R.<t> = PowerSeriesRing(QQ)
            sage: S.<x, y> = PolynomialRing(R)
            sage: f = (t^2 + O(t^3))*x^2*y^3 + (37*t^4 + O(t^5))*x^3
            sage: type(f)
            <class \'sage.rings.polynomial.multi_polynomial_element.MPolynomial_polydict\'>
            sage: f.derivative(x)       # with respect to x
            (2*t^2 + O(t^3))*x*y^3 + (111*t^4 + O(t^5))*x^2
            sage: f.derivative(y)       # with respect to y
            (3*t^2 + O(t^3))*x^2*y^2
            sage: f.derivative(t)       # with respect to t (recurses into base ring)
            (2*t + O(t^2))*x^2*y^3 + (148*t^3 + O(t^4))*x^3
            sage: f.derivative(x, y)    # with respect to x and then y
            (6*t^2 + O(t^3))*x*y^2
            sage: f.derivative(y, 3)    # with respect to y three times
            (6*t^2 + O(t^3))*x^2
            sage: f.derivative()        # can\'t figure out the variable
            Traceback (most recent call last):
            ...
            ValueError: must specify which variable to differentiate with respect to

        Polynomials over the symbolic ring (just for fun....)::

            sage: # needs sage.symbolic
            sage: x = var("x")
            sage: S.<u, v> = PolynomialRing(SR)
            sage: f = u*v*x
            sage: f.derivative(x) == u*v
            True
            sage: f.derivative(u) == v*x
            True'''
    @overload
    def discriminant(self, variable) -> Any:
        """MPolynomial.discriminant(self, variable)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 1609)

        Return the discriminant of ``self`` with respect to the given variable.

        INPUT:

        - ``variable`` -- the variable with respect to which we compute
          the discriminant

        OUTPUT: an element of the base ring of the polynomial ring

        EXAMPLES::

            sage: R.<x,y,z> = QQ[]
            sage: f = 4*x*y^2 + 1/4*x*y*z + 3/2*x*z^2 - 1/2*z^2
            sage: f.discriminant(x)                                                     # needs sage.libs.singular
            1
            sage: f.discriminant(y)                                                     # needs sage.libs.singular
            -383/16*x^2*z^2 + 8*x*z^2
            sage: f.discriminant(z)                                                     # needs sage.libs.singular
            -383/16*x^2*y^2 + 8*x*y^2

        Note that, unlike the univariate case, the result lives in
        the same ring as the polynomial::

            sage: R.<x,y> = QQ[]
            sage: f = x^5*y + 3*x^2*y^2 - 2*x + y - 1
            sage: f.discriminant(y)                                                     # needs sage.libs.singular
            x^10 + 2*x^5 + 24*x^3 + 12*x^2 + 1
            sage: f.polynomial(y).discriminant()                                        # needs sage.libs.pari sage.modules
            x^10 + 2*x^5 + 24*x^3 + 12*x^2 + 1
            sage: f.discriminant(y).parent() == f.polynomial(y).discriminant().parent()             # needs sage.libs.singular sage.modules
            False

        TESTS:

        Test polynomials over QQbar (:issue:`25265`)::

            sage: # needs sage.rings.number_field
            sage: R.<x,y> = QQbar[]
            sage: f = x^5*y + 3*x^2*y^2 - 2*x + y - 1
            sage: f.discriminant(y)                                                     # needs sage.libs.singular
            x^10 + 2*x^5 + 24*x^3 + 12*x^2 + 1

        AUTHOR: Miguel Marco"""
    @overload
    def discriminant(self, x) -> Any:
        """MPolynomial.discriminant(self, variable)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 1609)

        Return the discriminant of ``self`` with respect to the given variable.

        INPUT:

        - ``variable`` -- the variable with respect to which we compute
          the discriminant

        OUTPUT: an element of the base ring of the polynomial ring

        EXAMPLES::

            sage: R.<x,y,z> = QQ[]
            sage: f = 4*x*y^2 + 1/4*x*y*z + 3/2*x*z^2 - 1/2*z^2
            sage: f.discriminant(x)                                                     # needs sage.libs.singular
            1
            sage: f.discriminant(y)                                                     # needs sage.libs.singular
            -383/16*x^2*z^2 + 8*x*z^2
            sage: f.discriminant(z)                                                     # needs sage.libs.singular
            -383/16*x^2*y^2 + 8*x*y^2

        Note that, unlike the univariate case, the result lives in
        the same ring as the polynomial::

            sage: R.<x,y> = QQ[]
            sage: f = x^5*y + 3*x^2*y^2 - 2*x + y - 1
            sage: f.discriminant(y)                                                     # needs sage.libs.singular
            x^10 + 2*x^5 + 24*x^3 + 12*x^2 + 1
            sage: f.polynomial(y).discriminant()                                        # needs sage.libs.pari sage.modules
            x^10 + 2*x^5 + 24*x^3 + 12*x^2 + 1
            sage: f.discriminant(y).parent() == f.polynomial(y).discriminant().parent()             # needs sage.libs.singular sage.modules
            False

        TESTS:

        Test polynomials over QQbar (:issue:`25265`)::

            sage: # needs sage.rings.number_field
            sage: R.<x,y> = QQbar[]
            sage: f = x^5*y + 3*x^2*y^2 - 2*x + y - 1
            sage: f.discriminant(y)                                                     # needs sage.libs.singular
            x^10 + 2*x^5 + 24*x^3 + 12*x^2 + 1

        AUTHOR: Miguel Marco"""
    @overload
    def discriminant(self, y) -> Any:
        """MPolynomial.discriminant(self, variable)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 1609)

        Return the discriminant of ``self`` with respect to the given variable.

        INPUT:

        - ``variable`` -- the variable with respect to which we compute
          the discriminant

        OUTPUT: an element of the base ring of the polynomial ring

        EXAMPLES::

            sage: R.<x,y,z> = QQ[]
            sage: f = 4*x*y^2 + 1/4*x*y*z + 3/2*x*z^2 - 1/2*z^2
            sage: f.discriminant(x)                                                     # needs sage.libs.singular
            1
            sage: f.discriminant(y)                                                     # needs sage.libs.singular
            -383/16*x^2*z^2 + 8*x*z^2
            sage: f.discriminant(z)                                                     # needs sage.libs.singular
            -383/16*x^2*y^2 + 8*x*y^2

        Note that, unlike the univariate case, the result lives in
        the same ring as the polynomial::

            sage: R.<x,y> = QQ[]
            sage: f = x^5*y + 3*x^2*y^2 - 2*x + y - 1
            sage: f.discriminant(y)                                                     # needs sage.libs.singular
            x^10 + 2*x^5 + 24*x^3 + 12*x^2 + 1
            sage: f.polynomial(y).discriminant()                                        # needs sage.libs.pari sage.modules
            x^10 + 2*x^5 + 24*x^3 + 12*x^2 + 1
            sage: f.discriminant(y).parent() == f.polynomial(y).discriminant().parent()             # needs sage.libs.singular sage.modules
            False

        TESTS:

        Test polynomials over QQbar (:issue:`25265`)::

            sage: # needs sage.rings.number_field
            sage: R.<x,y> = QQbar[]
            sage: f = x^5*y + 3*x^2*y^2 - 2*x + y - 1
            sage: f.discriminant(y)                                                     # needs sage.libs.singular
            x^10 + 2*x^5 + 24*x^3 + 12*x^2 + 1

        AUTHOR: Miguel Marco"""
    @overload
    def discriminant(self, z) -> Any:
        """MPolynomial.discriminant(self, variable)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 1609)

        Return the discriminant of ``self`` with respect to the given variable.

        INPUT:

        - ``variable`` -- the variable with respect to which we compute
          the discriminant

        OUTPUT: an element of the base ring of the polynomial ring

        EXAMPLES::

            sage: R.<x,y,z> = QQ[]
            sage: f = 4*x*y^2 + 1/4*x*y*z + 3/2*x*z^2 - 1/2*z^2
            sage: f.discriminant(x)                                                     # needs sage.libs.singular
            1
            sage: f.discriminant(y)                                                     # needs sage.libs.singular
            -383/16*x^2*z^2 + 8*x*z^2
            sage: f.discriminant(z)                                                     # needs sage.libs.singular
            -383/16*x^2*y^2 + 8*x*y^2

        Note that, unlike the univariate case, the result lives in
        the same ring as the polynomial::

            sage: R.<x,y> = QQ[]
            sage: f = x^5*y + 3*x^2*y^2 - 2*x + y - 1
            sage: f.discriminant(y)                                                     # needs sage.libs.singular
            x^10 + 2*x^5 + 24*x^3 + 12*x^2 + 1
            sage: f.polynomial(y).discriminant()                                        # needs sage.libs.pari sage.modules
            x^10 + 2*x^5 + 24*x^3 + 12*x^2 + 1
            sage: f.discriminant(y).parent() == f.polynomial(y).discriminant().parent()             # needs sage.libs.singular sage.modules
            False

        TESTS:

        Test polynomials over QQbar (:issue:`25265`)::

            sage: # needs sage.rings.number_field
            sage: R.<x,y> = QQbar[]
            sage: f = x^5*y + 3*x^2*y^2 - 2*x + y - 1
            sage: f.discriminant(y)                                                     # needs sage.libs.singular
            x^10 + 2*x^5 + 24*x^3 + 12*x^2 + 1

        AUTHOR: Miguel Marco"""
    @overload
    def discriminant(self, y) -> Any:
        """MPolynomial.discriminant(self, variable)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 1609)

        Return the discriminant of ``self`` with respect to the given variable.

        INPUT:

        - ``variable`` -- the variable with respect to which we compute
          the discriminant

        OUTPUT: an element of the base ring of the polynomial ring

        EXAMPLES::

            sage: R.<x,y,z> = QQ[]
            sage: f = 4*x*y^2 + 1/4*x*y*z + 3/2*x*z^2 - 1/2*z^2
            sage: f.discriminant(x)                                                     # needs sage.libs.singular
            1
            sage: f.discriminant(y)                                                     # needs sage.libs.singular
            -383/16*x^2*z^2 + 8*x*z^2
            sage: f.discriminant(z)                                                     # needs sage.libs.singular
            -383/16*x^2*y^2 + 8*x*y^2

        Note that, unlike the univariate case, the result lives in
        the same ring as the polynomial::

            sage: R.<x,y> = QQ[]
            sage: f = x^5*y + 3*x^2*y^2 - 2*x + y - 1
            sage: f.discriminant(y)                                                     # needs sage.libs.singular
            x^10 + 2*x^5 + 24*x^3 + 12*x^2 + 1
            sage: f.polynomial(y).discriminant()                                        # needs sage.libs.pari sage.modules
            x^10 + 2*x^5 + 24*x^3 + 12*x^2 + 1
            sage: f.discriminant(y).parent() == f.polynomial(y).discriminant().parent()             # needs sage.libs.singular sage.modules
            False

        TESTS:

        Test polynomials over QQbar (:issue:`25265`)::

            sage: # needs sage.rings.number_field
            sage: R.<x,y> = QQbar[]
            sage: f = x^5*y + 3*x^2*y^2 - 2*x + y - 1
            sage: f.discriminant(y)                                                     # needs sage.libs.singular
            x^10 + 2*x^5 + 24*x^3 + 12*x^2 + 1

        AUTHOR: Miguel Marco"""
    @overload
    def discriminant(self) -> Any:
        """MPolynomial.discriminant(self, variable)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 1609)

        Return the discriminant of ``self`` with respect to the given variable.

        INPUT:

        - ``variable`` -- the variable with respect to which we compute
          the discriminant

        OUTPUT: an element of the base ring of the polynomial ring

        EXAMPLES::

            sage: R.<x,y,z> = QQ[]
            sage: f = 4*x*y^2 + 1/4*x*y*z + 3/2*x*z^2 - 1/2*z^2
            sage: f.discriminant(x)                                                     # needs sage.libs.singular
            1
            sage: f.discriminant(y)                                                     # needs sage.libs.singular
            -383/16*x^2*z^2 + 8*x*z^2
            sage: f.discriminant(z)                                                     # needs sage.libs.singular
            -383/16*x^2*y^2 + 8*x*y^2

        Note that, unlike the univariate case, the result lives in
        the same ring as the polynomial::

            sage: R.<x,y> = QQ[]
            sage: f = x^5*y + 3*x^2*y^2 - 2*x + y - 1
            sage: f.discriminant(y)                                                     # needs sage.libs.singular
            x^10 + 2*x^5 + 24*x^3 + 12*x^2 + 1
            sage: f.polynomial(y).discriminant()                                        # needs sage.libs.pari sage.modules
            x^10 + 2*x^5 + 24*x^3 + 12*x^2 + 1
            sage: f.discriminant(y).parent() == f.polynomial(y).discriminant().parent()             # needs sage.libs.singular sage.modules
            False

        TESTS:

        Test polynomials over QQbar (:issue:`25265`)::

            sage: # needs sage.rings.number_field
            sage: R.<x,y> = QQbar[]
            sage: f = x^5*y + 3*x^2*y^2 - 2*x + y - 1
            sage: f.discriminant(y)                                                     # needs sage.libs.singular
            x^10 + 2*x^5 + 24*x^3 + 12*x^2 + 1

        AUTHOR: Miguel Marco"""
    @overload
    def discriminant(self, y) -> Any:
        """MPolynomial.discriminant(self, variable)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 1609)

        Return the discriminant of ``self`` with respect to the given variable.

        INPUT:

        - ``variable`` -- the variable with respect to which we compute
          the discriminant

        OUTPUT: an element of the base ring of the polynomial ring

        EXAMPLES::

            sage: R.<x,y,z> = QQ[]
            sage: f = 4*x*y^2 + 1/4*x*y*z + 3/2*x*z^2 - 1/2*z^2
            sage: f.discriminant(x)                                                     # needs sage.libs.singular
            1
            sage: f.discriminant(y)                                                     # needs sage.libs.singular
            -383/16*x^2*z^2 + 8*x*z^2
            sage: f.discriminant(z)                                                     # needs sage.libs.singular
            -383/16*x^2*y^2 + 8*x*y^2

        Note that, unlike the univariate case, the result lives in
        the same ring as the polynomial::

            sage: R.<x,y> = QQ[]
            sage: f = x^5*y + 3*x^2*y^2 - 2*x + y - 1
            sage: f.discriminant(y)                                                     # needs sage.libs.singular
            x^10 + 2*x^5 + 24*x^3 + 12*x^2 + 1
            sage: f.polynomial(y).discriminant()                                        # needs sage.libs.pari sage.modules
            x^10 + 2*x^5 + 24*x^3 + 12*x^2 + 1
            sage: f.discriminant(y).parent() == f.polynomial(y).discriminant().parent()             # needs sage.libs.singular sage.modules
            False

        TESTS:

        Test polynomials over QQbar (:issue:`25265`)::

            sage: # needs sage.rings.number_field
            sage: R.<x,y> = QQbar[]
            sage: f = x^5*y + 3*x^2*y^2 - 2*x + y - 1
            sage: f.discriminant(y)                                                     # needs sage.libs.singular
            x^10 + 2*x^5 + 24*x^3 + 12*x^2 + 1

        AUTHOR: Miguel Marco"""
    @overload
    def discriminant(self, y) -> Any:
        """MPolynomial.discriminant(self, variable)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 1609)

        Return the discriminant of ``self`` with respect to the given variable.

        INPUT:

        - ``variable`` -- the variable with respect to which we compute
          the discriminant

        OUTPUT: an element of the base ring of the polynomial ring

        EXAMPLES::

            sage: R.<x,y,z> = QQ[]
            sage: f = 4*x*y^2 + 1/4*x*y*z + 3/2*x*z^2 - 1/2*z^2
            sage: f.discriminant(x)                                                     # needs sage.libs.singular
            1
            sage: f.discriminant(y)                                                     # needs sage.libs.singular
            -383/16*x^2*z^2 + 8*x*z^2
            sage: f.discriminant(z)                                                     # needs sage.libs.singular
            -383/16*x^2*y^2 + 8*x*y^2

        Note that, unlike the univariate case, the result lives in
        the same ring as the polynomial::

            sage: R.<x,y> = QQ[]
            sage: f = x^5*y + 3*x^2*y^2 - 2*x + y - 1
            sage: f.discriminant(y)                                                     # needs sage.libs.singular
            x^10 + 2*x^5 + 24*x^3 + 12*x^2 + 1
            sage: f.polynomial(y).discriminant()                                        # needs sage.libs.pari sage.modules
            x^10 + 2*x^5 + 24*x^3 + 12*x^2 + 1
            sage: f.discriminant(y).parent() == f.polynomial(y).discriminant().parent()             # needs sage.libs.singular sage.modules
            False

        TESTS:

        Test polynomials over QQbar (:issue:`25265`)::

            sage: # needs sage.rings.number_field
            sage: R.<x,y> = QQbar[]
            sage: f = x^5*y + 3*x^2*y^2 - 2*x + y - 1
            sage: f.discriminant(y)                                                     # needs sage.libs.singular
            x^10 + 2*x^5 + 24*x^3 + 12*x^2 + 1

        AUTHOR: Miguel Marco"""
    @overload
    def gcd(self, other) -> Any:
        """MPolynomial.gcd(self, other)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 2156)

        Return a greatest common divisor of this polynomial and ``other``.

        INPUT:

        - ``other`` -- a polynomial with the same parent as this polynomial

        EXAMPLES::

            sage: Q.<z> = Frac(QQ['z'])
            sage: R.<x,y> = Q[]
            sage: r = x*y - (2*z-1)/(z^2+z+1) * x + y/z
            sage: p = r * (x + z*y - 1/z^2)
            sage: q = r * (x*y*z + 1)
            sage: gcd(p, q)
            (z^3 + z^2 + z)*x*y + (-2*z^2 + z)*x + (z^2 + z + 1)*y

        Polynomials over polynomial rings are converted to a simpler polynomial
        ring with all variables to compute the gcd::

            sage: A.<z,t> = ZZ[]
            sage: B.<x,y> = A[]
            sage: r = x*y*z*t + 1
            sage: p = r * (x - y + z - t + 1)
            sage: q = r * (x*z - y*t)
            sage: gcd(p, q)                                                             # needs sage.libs.singular
            z*t*x*y + 1
            sage: _.parent()
            Multivariate Polynomial Ring in x, y over
             Multivariate Polynomial Ring in z, t over Integer Ring

        Some multivariate polynomial rings have no gcd implementation::

            sage: R.<x,y> = GaussianIntegers()[]                                        # needs sage.rings.number_field
            sage: x.gcd(x)
            Traceback (most recent call last):
            ...
            NotImplementedError: GCD is not implemented for multivariate polynomials over
            Gaussian Integers generated by I in Number Field in I with defining polynomial x^2 + 1 with I = 1*I

        TESTS::

            sage: Pol = QQ['x']['x','y']
            sage: Pol.one().gcd(1)
            1

            sage: P = PolynomialRing(QQ, 'x', 0)
            sage: P.gens()
            ()"""
    @overload
    def gcd(self, p, q) -> Any:
        """MPolynomial.gcd(self, other)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 2156)

        Return a greatest common divisor of this polynomial and ``other``.

        INPUT:

        - ``other`` -- a polynomial with the same parent as this polynomial

        EXAMPLES::

            sage: Q.<z> = Frac(QQ['z'])
            sage: R.<x,y> = Q[]
            sage: r = x*y - (2*z-1)/(z^2+z+1) * x + y/z
            sage: p = r * (x + z*y - 1/z^2)
            sage: q = r * (x*y*z + 1)
            sage: gcd(p, q)
            (z^3 + z^2 + z)*x*y + (-2*z^2 + z)*x + (z^2 + z + 1)*y

        Polynomials over polynomial rings are converted to a simpler polynomial
        ring with all variables to compute the gcd::

            sage: A.<z,t> = ZZ[]
            sage: B.<x,y> = A[]
            sage: r = x*y*z*t + 1
            sage: p = r * (x - y + z - t + 1)
            sage: q = r * (x*z - y*t)
            sage: gcd(p, q)                                                             # needs sage.libs.singular
            z*t*x*y + 1
            sage: _.parent()
            Multivariate Polynomial Ring in x, y over
             Multivariate Polynomial Ring in z, t over Integer Ring

        Some multivariate polynomial rings have no gcd implementation::

            sage: R.<x,y> = GaussianIntegers()[]                                        # needs sage.rings.number_field
            sage: x.gcd(x)
            Traceback (most recent call last):
            ...
            NotImplementedError: GCD is not implemented for multivariate polynomials over
            Gaussian Integers generated by I in Number Field in I with defining polynomial x^2 + 1 with I = 1*I

        TESTS::

            sage: Pol = QQ['x']['x','y']
            sage: Pol.one().gcd(1)
            1

            sage: P = PolynomialRing(QQ, 'x', 0)
            sage: P.gens()
            ()"""
    @overload
    def gcd(self, p, q) -> Any:
        """MPolynomial.gcd(self, other)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 2156)

        Return a greatest common divisor of this polynomial and ``other``.

        INPUT:

        - ``other`` -- a polynomial with the same parent as this polynomial

        EXAMPLES::

            sage: Q.<z> = Frac(QQ['z'])
            sage: R.<x,y> = Q[]
            sage: r = x*y - (2*z-1)/(z^2+z+1) * x + y/z
            sage: p = r * (x + z*y - 1/z^2)
            sage: q = r * (x*y*z + 1)
            sage: gcd(p, q)
            (z^3 + z^2 + z)*x*y + (-2*z^2 + z)*x + (z^2 + z + 1)*y

        Polynomials over polynomial rings are converted to a simpler polynomial
        ring with all variables to compute the gcd::

            sage: A.<z,t> = ZZ[]
            sage: B.<x,y> = A[]
            sage: r = x*y*z*t + 1
            sage: p = r * (x - y + z - t + 1)
            sage: q = r * (x*z - y*t)
            sage: gcd(p, q)                                                             # needs sage.libs.singular
            z*t*x*y + 1
            sage: _.parent()
            Multivariate Polynomial Ring in x, y over
             Multivariate Polynomial Ring in z, t over Integer Ring

        Some multivariate polynomial rings have no gcd implementation::

            sage: R.<x,y> = GaussianIntegers()[]                                        # needs sage.rings.number_field
            sage: x.gcd(x)
            Traceback (most recent call last):
            ...
            NotImplementedError: GCD is not implemented for multivariate polynomials over
            Gaussian Integers generated by I in Number Field in I with defining polynomial x^2 + 1 with I = 1*I

        TESTS::

            sage: Pol = QQ['x']['x','y']
            sage: Pol.one().gcd(1)
            1

            sage: P = PolynomialRing(QQ, 'x', 0)
            sage: P.gens()
            ()"""
    @overload
    def gcd(self, x) -> Any:
        """MPolynomial.gcd(self, other)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 2156)

        Return a greatest common divisor of this polynomial and ``other``.

        INPUT:

        - ``other`` -- a polynomial with the same parent as this polynomial

        EXAMPLES::

            sage: Q.<z> = Frac(QQ['z'])
            sage: R.<x,y> = Q[]
            sage: r = x*y - (2*z-1)/(z^2+z+1) * x + y/z
            sage: p = r * (x + z*y - 1/z^2)
            sage: q = r * (x*y*z + 1)
            sage: gcd(p, q)
            (z^3 + z^2 + z)*x*y + (-2*z^2 + z)*x + (z^2 + z + 1)*y

        Polynomials over polynomial rings are converted to a simpler polynomial
        ring with all variables to compute the gcd::

            sage: A.<z,t> = ZZ[]
            sage: B.<x,y> = A[]
            sage: r = x*y*z*t + 1
            sage: p = r * (x - y + z - t + 1)
            sage: q = r * (x*z - y*t)
            sage: gcd(p, q)                                                             # needs sage.libs.singular
            z*t*x*y + 1
            sage: _.parent()
            Multivariate Polynomial Ring in x, y over
             Multivariate Polynomial Ring in z, t over Integer Ring

        Some multivariate polynomial rings have no gcd implementation::

            sage: R.<x,y> = GaussianIntegers()[]                                        # needs sage.rings.number_field
            sage: x.gcd(x)
            Traceback (most recent call last):
            ...
            NotImplementedError: GCD is not implemented for multivariate polynomials over
            Gaussian Integers generated by I in Number Field in I with defining polynomial x^2 + 1 with I = 1*I

        TESTS::

            sage: Pol = QQ['x']['x','y']
            sage: Pol.one().gcd(1)
            1

            sage: P = PolynomialRing(QQ, 'x', 0)
            sage: P.gens()
            ()"""
    @overload
    def gradient(self) -> Any:
        """MPolynomial.gradient(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 1183)

        Return a list of partial derivatives of this polynomial,
        ordered by the variables of ``self.parent()``.

        EXAMPLES::

           sage: P.<x,y,z> = PolynomialRing(ZZ, 3)
           sage: f = x*y + 1
           sage: f.gradient()
           [y, x, 0]"""
    @overload
    def gradient(self) -> Any:
        """MPolynomial.gradient(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 1183)

        Return a list of partial derivatives of this polynomial,
        ordered by the variables of ``self.parent()``.

        EXAMPLES::

           sage: P.<x,y,z> = PolynomialRing(ZZ, 3)
           sage: f = x*y + 1
           sage: f.gradient()
           [y, x, 0]"""
    @overload
    def homogeneous_components(self) -> Any:
        """MPolynomial.homogeneous_components(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 831)

        Return the homogeneous components of this polynomial.

        OUTPUT: a dictionary mapping degrees to homogeneous polynomials

        EXAMPLES::

            sage: R.<x,y> = QQ[]
            sage: (x^3 + 2*x*y^3 + 4*y^3 + y).homogeneous_components()
            {1: y, 3: x^3 + 4*y^3, 4: 2*x*y^3}
            sage: R.zero().homogeneous_components()
            {}

        In case of weighted term orders, the polynomials are homogeneous with
        respect to the weights::

             sage: S.<a,b,c> = PolynomialRing(ZZ, order=TermOrder('wdegrevlex', (1,2,3)))
             sage: (a^6 + b^3 + b*c + a^2*c + c + a + 1).homogeneous_components()
             {0: 1, 1: a, 3: c, 5: a^2*c + b*c, 6: a^6 + b^3}"""
    @overload
    def homogeneous_components(self) -> Any:
        """MPolynomial.homogeneous_components(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 831)

        Return the homogeneous components of this polynomial.

        OUTPUT: a dictionary mapping degrees to homogeneous polynomials

        EXAMPLES::

            sage: R.<x,y> = QQ[]
            sage: (x^3 + 2*x*y^3 + 4*y^3 + y).homogeneous_components()
            {1: y, 3: x^3 + 4*y^3, 4: 2*x*y^3}
            sage: R.zero().homogeneous_components()
            {}

        In case of weighted term orders, the polynomials are homogeneous with
        respect to the weights::

             sage: S.<a,b,c> = PolynomialRing(ZZ, order=TermOrder('wdegrevlex', (1,2,3)))
             sage: (a^6 + b^3 + b*c + a^2*c + c + a + 1).homogeneous_components()
             {0: 1, 1: a, 3: c, 5: a^2*c + b*c, 6: a^6 + b^3}"""
    @overload
    def homogeneous_components(self) -> Any:
        """MPolynomial.homogeneous_components(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 831)

        Return the homogeneous components of this polynomial.

        OUTPUT: a dictionary mapping degrees to homogeneous polynomials

        EXAMPLES::

            sage: R.<x,y> = QQ[]
            sage: (x^3 + 2*x*y^3 + 4*y^3 + y).homogeneous_components()
            {1: y, 3: x^3 + 4*y^3, 4: 2*x*y^3}
            sage: R.zero().homogeneous_components()
            {}

        In case of weighted term orders, the polynomials are homogeneous with
        respect to the weights::

             sage: S.<a,b,c> = PolynomialRing(ZZ, order=TermOrder('wdegrevlex', (1,2,3)))
             sage: (a^6 + b^3 + b*c + a^2*c + c + a + 1).homogeneous_components()
             {0: 1, 1: a, 3: c, 5: a^2*c + b*c, 6: a^6 + b^3}"""
    @overload
    def homogeneous_components(self) -> Any:
        """MPolynomial.homogeneous_components(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 831)

        Return the homogeneous components of this polynomial.

        OUTPUT: a dictionary mapping degrees to homogeneous polynomials

        EXAMPLES::

            sage: R.<x,y> = QQ[]
            sage: (x^3 + 2*x*y^3 + 4*y^3 + y).homogeneous_components()
            {1: y, 3: x^3 + 4*y^3, 4: 2*x*y^3}
            sage: R.zero().homogeneous_components()
            {}

        In case of weighted term orders, the polynomials are homogeneous with
        respect to the weights::

             sage: S.<a,b,c> = PolynomialRing(ZZ, order=TermOrder('wdegrevlex', (1,2,3)))
             sage: (a^6 + b^3 + b*c + a^2*c + c + a + 1).homogeneous_components()
             {0: 1, 1: a, 3: c, 5: a^2*c + b*c, 6: a^6 + b^3}"""
    @overload
    def homogenize(self, var=...) -> Any:
        """MPolynomial.homogenize(self, var='h')

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 668)

        Return the homogenization of this polynomial.

        The polynomial itself is returned if it is homogeneous already.
        Otherwise, the monomials are multiplied with the smallest powers of
        ``var`` such that they all have the same total degree.

        INPUT:

        - ``var`` -- a variable in the polynomial ring (as a string, an element of
          the ring, or a zero-based index in the list of variables) or a name
          for a new variable (default: ``'h'``)

        OUTPUT:

        If ``var`` specifies a variable in the polynomial ring, then a
        homogeneous element in that ring is returned. Otherwise, a homogeneous
        element is returned in a polynomial ring with an extra last variable
        ``var``.

        EXAMPLES::

            sage: R.<x,y> = QQ[]
            sage: f = x^2 + y + 1 + 5*x*y^10
            sage: f.homogenize()
            5*x*y^10 + x^2*h^9 + y*h^10 + h^11

        The parameter ``var`` can be used to specify the name of the variable::

            sage: g = f.homogenize('z'); g
            5*x*y^10 + x^2*z^9 + y*z^10 + z^11
            sage: g.parent()
            Multivariate Polynomial Ring in x, y, z over Rational Field

        However, if the polynomial is homogeneous already, then that parameter
        is ignored and no extra variable is added to the polynomial ring::

            sage: f = x^2 + y^2
            sage: g = f.homogenize('z'); g
            x^2 + y^2
            sage: g.parent()
            Multivariate Polynomial Ring in x, y over Rational Field

        If you want the ring of the result to be independent of whether the
        polynomial is homogenized, you can use ``var`` to use an existing
        variable to homogenize::

            sage: R.<x,y,z> = QQ[]
            sage: f = x^2 + y^2
            sage: g = f.homogenize(z); g
            x^2 + y^2
            sage: g.parent()
            Multivariate Polynomial Ring in x, y, z over Rational Field
            sage: f = x^2 - y
            sage: g = f.homogenize(z); g
            x^2 - y*z
            sage: g.parent()
            Multivariate Polynomial Ring in x, y, z over Rational Field

        The parameter ``var`` can also be given as a zero-based index in the
        list of variables::

            sage: g = f.homogenize(2); g
            x^2 - y*z

        If the variable specified by ``var`` is not present in the polynomial,
        then setting it to 1 yields the original polynomial::

            sage: g(x,y,1)
            x^2 - y

        If it is present already, this might not be the case::

            sage: g = f.homogenize(x); g
            x^2 - x*y
            sage: g(1,y,z)
            -y + 1

        In particular, this can be surprising in positive characteristic::

            sage: R.<x,y> = GF(2)[]
            sage: f = x + 1
            sage: f.homogenize(x)
            0

        TESTS::

            sage: R = PolynomialRing(QQ, 'x', 5)
            sage: p = R.random_element()
            sage: q1 = p.homogenize()
            sage: q2 = p.homogenize()
            sage: q1.parent() is q2.parent()
            True"""
    @overload
    def homogenize(self) -> Any:
        """MPolynomial.homogenize(self, var='h')

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 668)

        Return the homogenization of this polynomial.

        The polynomial itself is returned if it is homogeneous already.
        Otherwise, the monomials are multiplied with the smallest powers of
        ``var`` such that they all have the same total degree.

        INPUT:

        - ``var`` -- a variable in the polynomial ring (as a string, an element of
          the ring, or a zero-based index in the list of variables) or a name
          for a new variable (default: ``'h'``)

        OUTPUT:

        If ``var`` specifies a variable in the polynomial ring, then a
        homogeneous element in that ring is returned. Otherwise, a homogeneous
        element is returned in a polynomial ring with an extra last variable
        ``var``.

        EXAMPLES::

            sage: R.<x,y> = QQ[]
            sage: f = x^2 + y + 1 + 5*x*y^10
            sage: f.homogenize()
            5*x*y^10 + x^2*h^9 + y*h^10 + h^11

        The parameter ``var`` can be used to specify the name of the variable::

            sage: g = f.homogenize('z'); g
            5*x*y^10 + x^2*z^9 + y*z^10 + z^11
            sage: g.parent()
            Multivariate Polynomial Ring in x, y, z over Rational Field

        However, if the polynomial is homogeneous already, then that parameter
        is ignored and no extra variable is added to the polynomial ring::

            sage: f = x^2 + y^2
            sage: g = f.homogenize('z'); g
            x^2 + y^2
            sage: g.parent()
            Multivariate Polynomial Ring in x, y over Rational Field

        If you want the ring of the result to be independent of whether the
        polynomial is homogenized, you can use ``var`` to use an existing
        variable to homogenize::

            sage: R.<x,y,z> = QQ[]
            sage: f = x^2 + y^2
            sage: g = f.homogenize(z); g
            x^2 + y^2
            sage: g.parent()
            Multivariate Polynomial Ring in x, y, z over Rational Field
            sage: f = x^2 - y
            sage: g = f.homogenize(z); g
            x^2 - y*z
            sage: g.parent()
            Multivariate Polynomial Ring in x, y, z over Rational Field

        The parameter ``var`` can also be given as a zero-based index in the
        list of variables::

            sage: g = f.homogenize(2); g
            x^2 - y*z

        If the variable specified by ``var`` is not present in the polynomial,
        then setting it to 1 yields the original polynomial::

            sage: g(x,y,1)
            x^2 - y

        If it is present already, this might not be the case::

            sage: g = f.homogenize(x); g
            x^2 - x*y
            sage: g(1,y,z)
            -y + 1

        In particular, this can be surprising in positive characteristic::

            sage: R.<x,y> = GF(2)[]
            sage: f = x + 1
            sage: f.homogenize(x)
            0

        TESTS::

            sage: R = PolynomialRing(QQ, 'x', 5)
            sage: p = R.random_element()
            sage: q1 = p.homogenize()
            sage: q2 = p.homogenize()
            sage: q1.parent() is q2.parent()
            True"""
    @overload
    def homogenize(self, z) -> Any:
        """MPolynomial.homogenize(self, var='h')

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 668)

        Return the homogenization of this polynomial.

        The polynomial itself is returned if it is homogeneous already.
        Otherwise, the monomials are multiplied with the smallest powers of
        ``var`` such that they all have the same total degree.

        INPUT:

        - ``var`` -- a variable in the polynomial ring (as a string, an element of
          the ring, or a zero-based index in the list of variables) or a name
          for a new variable (default: ``'h'``)

        OUTPUT:

        If ``var`` specifies a variable in the polynomial ring, then a
        homogeneous element in that ring is returned. Otherwise, a homogeneous
        element is returned in a polynomial ring with an extra last variable
        ``var``.

        EXAMPLES::

            sage: R.<x,y> = QQ[]
            sage: f = x^2 + y + 1 + 5*x*y^10
            sage: f.homogenize()
            5*x*y^10 + x^2*h^9 + y*h^10 + h^11

        The parameter ``var`` can be used to specify the name of the variable::

            sage: g = f.homogenize('z'); g
            5*x*y^10 + x^2*z^9 + y*z^10 + z^11
            sage: g.parent()
            Multivariate Polynomial Ring in x, y, z over Rational Field

        However, if the polynomial is homogeneous already, then that parameter
        is ignored and no extra variable is added to the polynomial ring::

            sage: f = x^2 + y^2
            sage: g = f.homogenize('z'); g
            x^2 + y^2
            sage: g.parent()
            Multivariate Polynomial Ring in x, y over Rational Field

        If you want the ring of the result to be independent of whether the
        polynomial is homogenized, you can use ``var`` to use an existing
        variable to homogenize::

            sage: R.<x,y,z> = QQ[]
            sage: f = x^2 + y^2
            sage: g = f.homogenize(z); g
            x^2 + y^2
            sage: g.parent()
            Multivariate Polynomial Ring in x, y, z over Rational Field
            sage: f = x^2 - y
            sage: g = f.homogenize(z); g
            x^2 - y*z
            sage: g.parent()
            Multivariate Polynomial Ring in x, y, z over Rational Field

        The parameter ``var`` can also be given as a zero-based index in the
        list of variables::

            sage: g = f.homogenize(2); g
            x^2 - y*z

        If the variable specified by ``var`` is not present in the polynomial,
        then setting it to 1 yields the original polynomial::

            sage: g(x,y,1)
            x^2 - y

        If it is present already, this might not be the case::

            sage: g = f.homogenize(x); g
            x^2 - x*y
            sage: g(1,y,z)
            -y + 1

        In particular, this can be surprising in positive characteristic::

            sage: R.<x,y> = GF(2)[]
            sage: f = x + 1
            sage: f.homogenize(x)
            0

        TESTS::

            sage: R = PolynomialRing(QQ, 'x', 5)
            sage: p = R.random_element()
            sage: q1 = p.homogenize()
            sage: q2 = p.homogenize()
            sage: q1.parent() is q2.parent()
            True"""
    @overload
    def homogenize(self, z) -> Any:
        """MPolynomial.homogenize(self, var='h')

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 668)

        Return the homogenization of this polynomial.

        The polynomial itself is returned if it is homogeneous already.
        Otherwise, the monomials are multiplied with the smallest powers of
        ``var`` such that they all have the same total degree.

        INPUT:

        - ``var`` -- a variable in the polynomial ring (as a string, an element of
          the ring, or a zero-based index in the list of variables) or a name
          for a new variable (default: ``'h'``)

        OUTPUT:

        If ``var`` specifies a variable in the polynomial ring, then a
        homogeneous element in that ring is returned. Otherwise, a homogeneous
        element is returned in a polynomial ring with an extra last variable
        ``var``.

        EXAMPLES::

            sage: R.<x,y> = QQ[]
            sage: f = x^2 + y + 1 + 5*x*y^10
            sage: f.homogenize()
            5*x*y^10 + x^2*h^9 + y*h^10 + h^11

        The parameter ``var`` can be used to specify the name of the variable::

            sage: g = f.homogenize('z'); g
            5*x*y^10 + x^2*z^9 + y*z^10 + z^11
            sage: g.parent()
            Multivariate Polynomial Ring in x, y, z over Rational Field

        However, if the polynomial is homogeneous already, then that parameter
        is ignored and no extra variable is added to the polynomial ring::

            sage: f = x^2 + y^2
            sage: g = f.homogenize('z'); g
            x^2 + y^2
            sage: g.parent()
            Multivariate Polynomial Ring in x, y over Rational Field

        If you want the ring of the result to be independent of whether the
        polynomial is homogenized, you can use ``var`` to use an existing
        variable to homogenize::

            sage: R.<x,y,z> = QQ[]
            sage: f = x^2 + y^2
            sage: g = f.homogenize(z); g
            x^2 + y^2
            sage: g.parent()
            Multivariate Polynomial Ring in x, y, z over Rational Field
            sage: f = x^2 - y
            sage: g = f.homogenize(z); g
            x^2 - y*z
            sage: g.parent()
            Multivariate Polynomial Ring in x, y, z over Rational Field

        The parameter ``var`` can also be given as a zero-based index in the
        list of variables::

            sage: g = f.homogenize(2); g
            x^2 - y*z

        If the variable specified by ``var`` is not present in the polynomial,
        then setting it to 1 yields the original polynomial::

            sage: g(x,y,1)
            x^2 - y

        If it is present already, this might not be the case::

            sage: g = f.homogenize(x); g
            x^2 - x*y
            sage: g(1,y,z)
            -y + 1

        In particular, this can be surprising in positive characteristic::

            sage: R.<x,y> = GF(2)[]
            sage: f = x + 1
            sage: f.homogenize(x)
            0

        TESTS::

            sage: R = PolynomialRing(QQ, 'x', 5)
            sage: p = R.random_element()
            sage: q1 = p.homogenize()
            sage: q2 = p.homogenize()
            sage: q1.parent() is q2.parent()
            True"""
    @overload
    def homogenize(self, x) -> Any:
        """MPolynomial.homogenize(self, var='h')

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 668)

        Return the homogenization of this polynomial.

        The polynomial itself is returned if it is homogeneous already.
        Otherwise, the monomials are multiplied with the smallest powers of
        ``var`` such that they all have the same total degree.

        INPUT:

        - ``var`` -- a variable in the polynomial ring (as a string, an element of
          the ring, or a zero-based index in the list of variables) or a name
          for a new variable (default: ``'h'``)

        OUTPUT:

        If ``var`` specifies a variable in the polynomial ring, then a
        homogeneous element in that ring is returned. Otherwise, a homogeneous
        element is returned in a polynomial ring with an extra last variable
        ``var``.

        EXAMPLES::

            sage: R.<x,y> = QQ[]
            sage: f = x^2 + y + 1 + 5*x*y^10
            sage: f.homogenize()
            5*x*y^10 + x^2*h^9 + y*h^10 + h^11

        The parameter ``var`` can be used to specify the name of the variable::

            sage: g = f.homogenize('z'); g
            5*x*y^10 + x^2*z^9 + y*z^10 + z^11
            sage: g.parent()
            Multivariate Polynomial Ring in x, y, z over Rational Field

        However, if the polynomial is homogeneous already, then that parameter
        is ignored and no extra variable is added to the polynomial ring::

            sage: f = x^2 + y^2
            sage: g = f.homogenize('z'); g
            x^2 + y^2
            sage: g.parent()
            Multivariate Polynomial Ring in x, y over Rational Field

        If you want the ring of the result to be independent of whether the
        polynomial is homogenized, you can use ``var`` to use an existing
        variable to homogenize::

            sage: R.<x,y,z> = QQ[]
            sage: f = x^2 + y^2
            sage: g = f.homogenize(z); g
            x^2 + y^2
            sage: g.parent()
            Multivariate Polynomial Ring in x, y, z over Rational Field
            sage: f = x^2 - y
            sage: g = f.homogenize(z); g
            x^2 - y*z
            sage: g.parent()
            Multivariate Polynomial Ring in x, y, z over Rational Field

        The parameter ``var`` can also be given as a zero-based index in the
        list of variables::

            sage: g = f.homogenize(2); g
            x^2 - y*z

        If the variable specified by ``var`` is not present in the polynomial,
        then setting it to 1 yields the original polynomial::

            sage: g(x,y,1)
            x^2 - y

        If it is present already, this might not be the case::

            sage: g = f.homogenize(x); g
            x^2 - x*y
            sage: g(1,y,z)
            -y + 1

        In particular, this can be surprising in positive characteristic::

            sage: R.<x,y> = GF(2)[]
            sage: f = x + 1
            sage: f.homogenize(x)
            0

        TESTS::

            sage: R = PolynomialRing(QQ, 'x', 5)
            sage: p = R.random_element()
            sage: q1 = p.homogenize()
            sage: q2 = p.homogenize()
            sage: q1.parent() is q2.parent()
            True"""
    @overload
    def homogenize(self, x) -> Any:
        """MPolynomial.homogenize(self, var='h')

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 668)

        Return the homogenization of this polynomial.

        The polynomial itself is returned if it is homogeneous already.
        Otherwise, the monomials are multiplied with the smallest powers of
        ``var`` such that they all have the same total degree.

        INPUT:

        - ``var`` -- a variable in the polynomial ring (as a string, an element of
          the ring, or a zero-based index in the list of variables) or a name
          for a new variable (default: ``'h'``)

        OUTPUT:

        If ``var`` specifies a variable in the polynomial ring, then a
        homogeneous element in that ring is returned. Otherwise, a homogeneous
        element is returned in a polynomial ring with an extra last variable
        ``var``.

        EXAMPLES::

            sage: R.<x,y> = QQ[]
            sage: f = x^2 + y + 1 + 5*x*y^10
            sage: f.homogenize()
            5*x*y^10 + x^2*h^9 + y*h^10 + h^11

        The parameter ``var`` can be used to specify the name of the variable::

            sage: g = f.homogenize('z'); g
            5*x*y^10 + x^2*z^9 + y*z^10 + z^11
            sage: g.parent()
            Multivariate Polynomial Ring in x, y, z over Rational Field

        However, if the polynomial is homogeneous already, then that parameter
        is ignored and no extra variable is added to the polynomial ring::

            sage: f = x^2 + y^2
            sage: g = f.homogenize('z'); g
            x^2 + y^2
            sage: g.parent()
            Multivariate Polynomial Ring in x, y over Rational Field

        If you want the ring of the result to be independent of whether the
        polynomial is homogenized, you can use ``var`` to use an existing
        variable to homogenize::

            sage: R.<x,y,z> = QQ[]
            sage: f = x^2 + y^2
            sage: g = f.homogenize(z); g
            x^2 + y^2
            sage: g.parent()
            Multivariate Polynomial Ring in x, y, z over Rational Field
            sage: f = x^2 - y
            sage: g = f.homogenize(z); g
            x^2 - y*z
            sage: g.parent()
            Multivariate Polynomial Ring in x, y, z over Rational Field

        The parameter ``var`` can also be given as a zero-based index in the
        list of variables::

            sage: g = f.homogenize(2); g
            x^2 - y*z

        If the variable specified by ``var`` is not present in the polynomial,
        then setting it to 1 yields the original polynomial::

            sage: g(x,y,1)
            x^2 - y

        If it is present already, this might not be the case::

            sage: g = f.homogenize(x); g
            x^2 - x*y
            sage: g(1,y,z)
            -y + 1

        In particular, this can be surprising in positive characteristic::

            sage: R.<x,y> = GF(2)[]
            sage: f = x + 1
            sage: f.homogenize(x)
            0

        TESTS::

            sage: R = PolynomialRing(QQ, 'x', 5)
            sage: p = R.random_element()
            sage: q1 = p.homogenize()
            sage: q2 = p.homogenize()
            sage: q1.parent() is q2.parent()
            True"""
    @overload
    def homogenize(self) -> Any:
        """MPolynomial.homogenize(self, var='h')

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 668)

        Return the homogenization of this polynomial.

        The polynomial itself is returned if it is homogeneous already.
        Otherwise, the monomials are multiplied with the smallest powers of
        ``var`` such that they all have the same total degree.

        INPUT:

        - ``var`` -- a variable in the polynomial ring (as a string, an element of
          the ring, or a zero-based index in the list of variables) or a name
          for a new variable (default: ``'h'``)

        OUTPUT:

        If ``var`` specifies a variable in the polynomial ring, then a
        homogeneous element in that ring is returned. Otherwise, a homogeneous
        element is returned in a polynomial ring with an extra last variable
        ``var``.

        EXAMPLES::

            sage: R.<x,y> = QQ[]
            sage: f = x^2 + y + 1 + 5*x*y^10
            sage: f.homogenize()
            5*x*y^10 + x^2*h^9 + y*h^10 + h^11

        The parameter ``var`` can be used to specify the name of the variable::

            sage: g = f.homogenize('z'); g
            5*x*y^10 + x^2*z^9 + y*z^10 + z^11
            sage: g.parent()
            Multivariate Polynomial Ring in x, y, z over Rational Field

        However, if the polynomial is homogeneous already, then that parameter
        is ignored and no extra variable is added to the polynomial ring::

            sage: f = x^2 + y^2
            sage: g = f.homogenize('z'); g
            x^2 + y^2
            sage: g.parent()
            Multivariate Polynomial Ring in x, y over Rational Field

        If you want the ring of the result to be independent of whether the
        polynomial is homogenized, you can use ``var`` to use an existing
        variable to homogenize::

            sage: R.<x,y,z> = QQ[]
            sage: f = x^2 + y^2
            sage: g = f.homogenize(z); g
            x^2 + y^2
            sage: g.parent()
            Multivariate Polynomial Ring in x, y, z over Rational Field
            sage: f = x^2 - y
            sage: g = f.homogenize(z); g
            x^2 - y*z
            sage: g.parent()
            Multivariate Polynomial Ring in x, y, z over Rational Field

        The parameter ``var`` can also be given as a zero-based index in the
        list of variables::

            sage: g = f.homogenize(2); g
            x^2 - y*z

        If the variable specified by ``var`` is not present in the polynomial,
        then setting it to 1 yields the original polynomial::

            sage: g(x,y,1)
            x^2 - y

        If it is present already, this might not be the case::

            sage: g = f.homogenize(x); g
            x^2 - x*y
            sage: g(1,y,z)
            -y + 1

        In particular, this can be surprising in positive characteristic::

            sage: R.<x,y> = GF(2)[]
            sage: f = x + 1
            sage: f.homogenize(x)
            0

        TESTS::

            sage: R = PolynomialRing(QQ, 'x', 5)
            sage: p = R.random_element()
            sage: q1 = p.homogenize()
            sage: q2 = p.homogenize()
            sage: q1.parent() is q2.parent()
            True"""
    @overload
    def homogenize(self) -> Any:
        """MPolynomial.homogenize(self, var='h')

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 668)

        Return the homogenization of this polynomial.

        The polynomial itself is returned if it is homogeneous already.
        Otherwise, the monomials are multiplied with the smallest powers of
        ``var`` such that they all have the same total degree.

        INPUT:

        - ``var`` -- a variable in the polynomial ring (as a string, an element of
          the ring, or a zero-based index in the list of variables) or a name
          for a new variable (default: ``'h'``)

        OUTPUT:

        If ``var`` specifies a variable in the polynomial ring, then a
        homogeneous element in that ring is returned. Otherwise, a homogeneous
        element is returned in a polynomial ring with an extra last variable
        ``var``.

        EXAMPLES::

            sage: R.<x,y> = QQ[]
            sage: f = x^2 + y + 1 + 5*x*y^10
            sage: f.homogenize()
            5*x*y^10 + x^2*h^9 + y*h^10 + h^11

        The parameter ``var`` can be used to specify the name of the variable::

            sage: g = f.homogenize('z'); g
            5*x*y^10 + x^2*z^9 + y*z^10 + z^11
            sage: g.parent()
            Multivariate Polynomial Ring in x, y, z over Rational Field

        However, if the polynomial is homogeneous already, then that parameter
        is ignored and no extra variable is added to the polynomial ring::

            sage: f = x^2 + y^2
            sage: g = f.homogenize('z'); g
            x^2 + y^2
            sage: g.parent()
            Multivariate Polynomial Ring in x, y over Rational Field

        If you want the ring of the result to be independent of whether the
        polynomial is homogenized, you can use ``var`` to use an existing
        variable to homogenize::

            sage: R.<x,y,z> = QQ[]
            sage: f = x^2 + y^2
            sage: g = f.homogenize(z); g
            x^2 + y^2
            sage: g.parent()
            Multivariate Polynomial Ring in x, y, z over Rational Field
            sage: f = x^2 - y
            sage: g = f.homogenize(z); g
            x^2 - y*z
            sage: g.parent()
            Multivariate Polynomial Ring in x, y, z over Rational Field

        The parameter ``var`` can also be given as a zero-based index in the
        list of variables::

            sage: g = f.homogenize(2); g
            x^2 - y*z

        If the variable specified by ``var`` is not present in the polynomial,
        then setting it to 1 yields the original polynomial::

            sage: g(x,y,1)
            x^2 - y

        If it is present already, this might not be the case::

            sage: g = f.homogenize(x); g
            x^2 - x*y
            sage: g(1,y,z)
            -y + 1

        In particular, this can be surprising in positive characteristic::

            sage: R.<x,y> = GF(2)[]
            sage: f = x + 1
            sage: f.homogenize(x)
            0

        TESTS::

            sage: R = PolynomialRing(QQ, 'x', 5)
            sage: p = R.random_element()
            sage: q1 = p.homogenize()
            sage: q2 = p.homogenize()
            sage: q1.parent() is q2.parent()
            True"""
    @overload
    def inverse_mod(self, I) -> Any:
        """MPolynomial.inverse_mod(self, I)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 2000)

        Return an inverse of ``self`` modulo the polynomial ideal `I`,
        namely a multivariate polynomial `f` such that
        ``self * f - 1`` belongs to `I`.

        INPUT:

        - ``I`` -- an ideal of the polynomial ring in which ``self`` lives,
          or a single polynomial

        OUTPUT: a multivariate polynomial representing the inverse of ``f`` modulo `I`

        EXAMPLES::

            sage: R.<x1,x2> = QQ[]
            sage: I = R.ideal(x2**2 + x1 - 2, x1**2 - 1)
            sage: f = x1 + 3*x2^2; g = f.inverse_mod(I); g                               # needs sage.libs.singular
            1/16*x1 + 3/16
            sage: (f*g).reduce(I)                                                        # needs sage.libs.singular
            1

        Test a non-invertible element::

            sage: R.<x1,x2> = QQ[]
            sage: I = R.ideal(x2**2 + x1 - 2, x1**2 - 1)
            sage: f = x1 + x2
            sage: f.inverse_mod(I)                                                       # needs sage.libs.singular
            Traceback (most recent call last):
            ...
            ArithmeticError: element is non-invertible

        TESTS::

            sage: R.<x,y> = ZZ[]
            sage: x.inverse_mod(x*y-1)
            y"""
    @overload
    def inverse_mod(self, I) -> Any:
        """MPolynomial.inverse_mod(self, I)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 2000)

        Return an inverse of ``self`` modulo the polynomial ideal `I`,
        namely a multivariate polynomial `f` such that
        ``self * f - 1`` belongs to `I`.

        INPUT:

        - ``I`` -- an ideal of the polynomial ring in which ``self`` lives,
          or a single polynomial

        OUTPUT: a multivariate polynomial representing the inverse of ``f`` modulo `I`

        EXAMPLES::

            sage: R.<x1,x2> = QQ[]
            sage: I = R.ideal(x2**2 + x1 - 2, x1**2 - 1)
            sage: f = x1 + 3*x2^2; g = f.inverse_mod(I); g                               # needs sage.libs.singular
            1/16*x1 + 3/16
            sage: (f*g).reduce(I)                                                        # needs sage.libs.singular
            1

        Test a non-invertible element::

            sage: R.<x1,x2> = QQ[]
            sage: I = R.ideal(x2**2 + x1 - 2, x1**2 - 1)
            sage: f = x1 + x2
            sage: f.inverse_mod(I)                                                       # needs sage.libs.singular
            Traceback (most recent call last):
            ...
            ArithmeticError: element is non-invertible

        TESTS::

            sage: R.<x,y> = ZZ[]
            sage: x.inverse_mod(x*y-1)
            y"""
    @overload
    def inverse_mod(self, I) -> Any:
        """MPolynomial.inverse_mod(self, I)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 2000)

        Return an inverse of ``self`` modulo the polynomial ideal `I`,
        namely a multivariate polynomial `f` such that
        ``self * f - 1`` belongs to `I`.

        INPUT:

        - ``I`` -- an ideal of the polynomial ring in which ``self`` lives,
          or a single polynomial

        OUTPUT: a multivariate polynomial representing the inverse of ``f`` modulo `I`

        EXAMPLES::

            sage: R.<x1,x2> = QQ[]
            sage: I = R.ideal(x2**2 + x1 - 2, x1**2 - 1)
            sage: f = x1 + 3*x2^2; g = f.inverse_mod(I); g                               # needs sage.libs.singular
            1/16*x1 + 3/16
            sage: (f*g).reduce(I)                                                        # needs sage.libs.singular
            1

        Test a non-invertible element::

            sage: R.<x1,x2> = QQ[]
            sage: I = R.ideal(x2**2 + x1 - 2, x1**2 - 1)
            sage: f = x1 + x2
            sage: f.inverse_mod(I)                                                       # needs sage.libs.singular
            Traceback (most recent call last):
            ...
            ArithmeticError: element is non-invertible

        TESTS::

            sage: R.<x,y> = ZZ[]
            sage: x.inverse_mod(x*y-1)
            y"""
    @overload
    def is_gen(self) -> Any:
        """MPolynomial.is_gen(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 1337)

        Return ``True`` if this polynomial is a generator of its parent.

        EXAMPLES::

            sage: R.<x,y> = ZZ[]
            sage: x.is_gen()
            True
            sage: (x + y - y).is_gen()
            True
            sage: (x*y).is_gen()
            False
            sage: R.<x,y> = QQ[]
            sage: x.is_gen()
            True
            sage: (x + y - y).is_gen()
            True
            sage: (x*y).is_gen()
            False

        TESTS::

            sage: R.<x,y> = ZZ[]
            sage: x.is_generator()
            doctest:warning...:
            DeprecationWarning: is_generator is deprecated. Please use is_gen instead.
            See https://github.com/sagemath/sage/issues/38942 for details.
            True"""
    @overload
    def is_gen(self) -> Any:
        """MPolynomial.is_gen(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 1337)

        Return ``True`` if this polynomial is a generator of its parent.

        EXAMPLES::

            sage: R.<x,y> = ZZ[]
            sage: x.is_gen()
            True
            sage: (x + y - y).is_gen()
            True
            sage: (x*y).is_gen()
            False
            sage: R.<x,y> = QQ[]
            sage: x.is_gen()
            True
            sage: (x + y - y).is_gen()
            True
            sage: (x*y).is_gen()
            False

        TESTS::

            sage: R.<x,y> = ZZ[]
            sage: x.is_generator()
            doctest:warning...:
            DeprecationWarning: is_generator is deprecated. Please use is_gen instead.
            See https://github.com/sagemath/sage/issues/38942 for details.
            True"""
    @overload
    def is_gen(self) -> Any:
        """MPolynomial.is_gen(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 1337)

        Return ``True`` if this polynomial is a generator of its parent.

        EXAMPLES::

            sage: R.<x,y> = ZZ[]
            sage: x.is_gen()
            True
            sage: (x + y - y).is_gen()
            True
            sage: (x*y).is_gen()
            False
            sage: R.<x,y> = QQ[]
            sage: x.is_gen()
            True
            sage: (x + y - y).is_gen()
            True
            sage: (x*y).is_gen()
            False

        TESTS::

            sage: R.<x,y> = ZZ[]
            sage: x.is_generator()
            doctest:warning...:
            DeprecationWarning: is_generator is deprecated. Please use is_gen instead.
            See https://github.com/sagemath/sage/issues/38942 for details.
            True"""
    @overload
    def is_gen(self) -> Any:
        """MPolynomial.is_gen(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 1337)

        Return ``True`` if this polynomial is a generator of its parent.

        EXAMPLES::

            sage: R.<x,y> = ZZ[]
            sage: x.is_gen()
            True
            sage: (x + y - y).is_gen()
            True
            sage: (x*y).is_gen()
            False
            sage: R.<x,y> = QQ[]
            sage: x.is_gen()
            True
            sage: (x + y - y).is_gen()
            True
            sage: (x*y).is_gen()
            False

        TESTS::

            sage: R.<x,y> = ZZ[]
            sage: x.is_generator()
            doctest:warning...:
            DeprecationWarning: is_generator is deprecated. Please use is_gen instead.
            See https://github.com/sagemath/sage/issues/38942 for details.
            True"""
    @overload
    def is_gen(self) -> Any:
        """MPolynomial.is_gen(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 1337)

        Return ``True`` if this polynomial is a generator of its parent.

        EXAMPLES::

            sage: R.<x,y> = ZZ[]
            sage: x.is_gen()
            True
            sage: (x + y - y).is_gen()
            True
            sage: (x*y).is_gen()
            False
            sage: R.<x,y> = QQ[]
            sage: x.is_gen()
            True
            sage: (x + y - y).is_gen()
            True
            sage: (x*y).is_gen()
            False

        TESTS::

            sage: R.<x,y> = ZZ[]
            sage: x.is_generator()
            doctest:warning...:
            DeprecationWarning: is_generator is deprecated. Please use is_gen instead.
            See https://github.com/sagemath/sage/issues/38942 for details.
            True"""
    @overload
    def is_gen(self) -> Any:
        """MPolynomial.is_gen(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 1337)

        Return ``True`` if this polynomial is a generator of its parent.

        EXAMPLES::

            sage: R.<x,y> = ZZ[]
            sage: x.is_gen()
            True
            sage: (x + y - y).is_gen()
            True
            sage: (x*y).is_gen()
            False
            sage: R.<x,y> = QQ[]
            sage: x.is_gen()
            True
            sage: (x + y - y).is_gen()
            True
            sage: (x*y).is_gen()
            False

        TESTS::

            sage: R.<x,y> = ZZ[]
            sage: x.is_generator()
            doctest:warning...:
            DeprecationWarning: is_generator is deprecated. Please use is_gen instead.
            See https://github.com/sagemath/sage/issues/38942 for details.
            True"""
    @overload
    def is_gen(self) -> Any:
        """MPolynomial.is_gen(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 1337)

        Return ``True`` if this polynomial is a generator of its parent.

        EXAMPLES::

            sage: R.<x,y> = ZZ[]
            sage: x.is_gen()
            True
            sage: (x + y - y).is_gen()
            True
            sage: (x*y).is_gen()
            False
            sage: R.<x,y> = QQ[]
            sage: x.is_gen()
            True
            sage: (x + y - y).is_gen()
            True
            sage: (x*y).is_gen()
            False

        TESTS::

            sage: R.<x,y> = ZZ[]
            sage: x.is_generator()
            doctest:warning...:
            DeprecationWarning: is_generator is deprecated. Please use is_gen instead.
            See https://github.com/sagemath/sage/issues/38942 for details.
            True"""
    def is_generator(self, *args, **kwargs):
        """Deprecated: Use :meth:`is_gen` instead.
        See :issue:`38942` for details.

        """
    def is_homogeneous(self) -> Any:
        """MPolynomial.is_homogeneous(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 795)

        Return ``True`` if ``self`` is a homogeneous polynomial.

        TESTS::

            sage: from sage.rings.polynomial.multi_polynomial import MPolynomial
            sage: P.<x, y> = PolynomialRing(QQ, 2)
            sage: MPolynomial.is_homogeneous(x+y)
            True
            sage: MPolynomial.is_homogeneous(P(0))
            True
            sage: MPolynomial.is_homogeneous(x+y^2)
            False
            sage: MPolynomial.is_homogeneous(x^2 + y^2)
            True
            sage: MPolynomial.is_homogeneous(x^2 + y^2*x)
            False
            sage: MPolynomial.is_homogeneous(x^2*y + y^2*x)
            True

        .. NOTE::

            This is a generic implementation which is likely overridden by
            subclasses."""
    def is_lorentzian(self, explain=...) -> Any:
        """MPolynomial.is_lorentzian(self, explain=False)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 2763)

        Return whether this is a Lorentzian polynomial.

        INPUT:

        - ``explain`` -- boolean (default: ``False``); if ``True``
          return a tuple whose first element is the boolean result of the test,
          and the second element is a string describing the reason the test failed,
          or ``None`` if the test succeeded.

        Lorentzian polynomials are a class of polynomials connected with the area
        of discrete convex analysis.  A polynomial `f` with positive real coefficients
        is Lorentzian if:

        - `f` is homogeneous;

        - the support of `f` is `M`-convex

        - `f` has degree less than `2`, or if its degree is at least two,
          the collection of sequential partial derivatives of `f` which are
          quadratic forms have Gram matrices with at most one positive eigenvalue.

        Note in particular that the zero polynomial is Lorentzian.  Examples of
        Lorentzian polynomials include homogeneous stable polynomials, volume
        polynomials of convex bodies and projective varieties, and Schur polynomials
        after renormalizing the coefficient of each monomial `x^\\alpha` by `1/\\alpha!`.

        EXAMPLES:

        Renormalized Schur polynomials are Lorentzian, but not in general if the
        renormalization is skipped::

            sage: P.<x,y> = QQ[]
            sage: p = (x^2 / 2) + x*y + (y^2 / 2)
            sage: p.is_lorentzian()
            True
            sage: p = x^2 + x*y + y^2
            sage: p.is_lorentzian()
            False

        Homogeneous linear forms and constant polynomials with positive
        coefficients are Lorentzian, as well as the zero polynomial::

            sage: p = x + 2*y
            sage: p.is_lorentzian()
            True
            sage: p = P(5)
            sage: p.is_lorentzian()
            True
            sage: P.zero().is_lorentzian()
            True

        Inhomogeneous polynomials and polynomials with negative coefficients
        are not Lorentzian::

            sage: p = x^2 + 2*x + y^2
            sage: p.is_lorentzian()
            False
            sage: p = 2*x^2 - y^2
            sage: p.is_lorentzian()
            False

        It is an error to check if a polynomial is Lorentzian if its base ring
        is not a subring of the real numbers, as the notion is not defined in
        this case::

            sage: # needs sage.rings.real_mpfr
            sage: Q.<z,w> = CC[]
            sage: q = z^2 + w^2
            sage: q.is_lorentzian()
            Traceback (most recent call last):
            ...
            NotImplementedError: is_lorentzian only implemented for real polynomials

        The method can give a reason for a polynomial failing to be Lorentzian::

            sage: p = x^2 + 2*x + y^2
            sage: p.is_lorentzian(explain=True)
            (False, 'inhomogeneous')

        REFERENCES:

        For full definitions and related discussion, see [BrHu2019]_ and
        [HMMS2019]_.  The second reference gives the characterization of
        Lorentzian polynomials applied in this implementation explicitly."""
    @overload
    def is_nilpotent(self) -> Any:
        """MPolynomial.is_nilpotent(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 2692)

        Return ``True`` if ``self`` is nilpotent, i.e., some power of ``self``
        is 0.

        EXAMPLES::

            sage: R.<x,y> = QQbar[]                                                     # needs sage.rings.number_field
            sage: (x + y).is_nilpotent()                                                # needs sage.rings.number_field
            False
            sage: R(0).is_nilpotent()                                                   # needs sage.rings.number_field
            True
            sage: _.<x,y> = Zmod(4)[]
            sage: (2*x).is_nilpotent()
            True
            sage: (2 + y*x).is_nilpotent()
            False
            sage: _.<x,y> = Zmod(36)[]
            sage: (4 + 6*x).is_nilpotent()
            False
            sage: (6*x + 12*y + 18*x*y + 24*(x^2+y^2)).is_nilpotent()
            True"""
    @overload
    def is_nilpotent(self) -> Any:
        """MPolynomial.is_nilpotent(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 2692)

        Return ``True`` if ``self`` is nilpotent, i.e., some power of ``self``
        is 0.

        EXAMPLES::

            sage: R.<x,y> = QQbar[]                                                     # needs sage.rings.number_field
            sage: (x + y).is_nilpotent()                                                # needs sage.rings.number_field
            False
            sage: R(0).is_nilpotent()                                                   # needs sage.rings.number_field
            True
            sage: _.<x,y> = Zmod(4)[]
            sage: (2*x).is_nilpotent()
            True
            sage: (2 + y*x).is_nilpotent()
            False
            sage: _.<x,y> = Zmod(36)[]
            sage: (4 + 6*x).is_nilpotent()
            False
            sage: (6*x + 12*y + 18*x*y + 24*(x^2+y^2)).is_nilpotent()
            True"""
    @overload
    def is_nilpotent(self) -> Any:
        """MPolynomial.is_nilpotent(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 2692)

        Return ``True`` if ``self`` is nilpotent, i.e., some power of ``self``
        is 0.

        EXAMPLES::

            sage: R.<x,y> = QQbar[]                                                     # needs sage.rings.number_field
            sage: (x + y).is_nilpotent()                                                # needs sage.rings.number_field
            False
            sage: R(0).is_nilpotent()                                                   # needs sage.rings.number_field
            True
            sage: _.<x,y> = Zmod(4)[]
            sage: (2*x).is_nilpotent()
            True
            sage: (2 + y*x).is_nilpotent()
            False
            sage: _.<x,y> = Zmod(36)[]
            sage: (4 + 6*x).is_nilpotent()
            False
            sage: (6*x + 12*y + 18*x*y + 24*(x^2+y^2)).is_nilpotent()
            True"""
    @overload
    def is_nilpotent(self) -> Any:
        """MPolynomial.is_nilpotent(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 2692)

        Return ``True`` if ``self`` is nilpotent, i.e., some power of ``self``
        is 0.

        EXAMPLES::

            sage: R.<x,y> = QQbar[]                                                     # needs sage.rings.number_field
            sage: (x + y).is_nilpotent()                                                # needs sage.rings.number_field
            False
            sage: R(0).is_nilpotent()                                                   # needs sage.rings.number_field
            True
            sage: _.<x,y> = Zmod(4)[]
            sage: (2*x).is_nilpotent()
            True
            sage: (2 + y*x).is_nilpotent()
            False
            sage: _.<x,y> = Zmod(36)[]
            sage: (4 + 6*x).is_nilpotent()
            False
            sage: (6*x + 12*y + 18*x*y + 24*(x^2+y^2)).is_nilpotent()
            True"""
    @overload
    def is_nilpotent(self) -> Any:
        """MPolynomial.is_nilpotent(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 2692)

        Return ``True`` if ``self`` is nilpotent, i.e., some power of ``self``
        is 0.

        EXAMPLES::

            sage: R.<x,y> = QQbar[]                                                     # needs sage.rings.number_field
            sage: (x + y).is_nilpotent()                                                # needs sage.rings.number_field
            False
            sage: R(0).is_nilpotent()                                                   # needs sage.rings.number_field
            True
            sage: _.<x,y> = Zmod(4)[]
            sage: (2*x).is_nilpotent()
            True
            sage: (2 + y*x).is_nilpotent()
            False
            sage: _.<x,y> = Zmod(36)[]
            sage: (4 + 6*x).is_nilpotent()
            False
            sage: (6*x + 12*y + 18*x*y + 24*(x^2+y^2)).is_nilpotent()
            True"""
    @overload
    def is_nilpotent(self) -> Any:
        """MPolynomial.is_nilpotent(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 2692)

        Return ``True`` if ``self`` is nilpotent, i.e., some power of ``self``
        is 0.

        EXAMPLES::

            sage: R.<x,y> = QQbar[]                                                     # needs sage.rings.number_field
            sage: (x + y).is_nilpotent()                                                # needs sage.rings.number_field
            False
            sage: R(0).is_nilpotent()                                                   # needs sage.rings.number_field
            True
            sage: _.<x,y> = Zmod(4)[]
            sage: (2*x).is_nilpotent()
            True
            sage: (2 + y*x).is_nilpotent()
            False
            sage: _.<x,y> = Zmod(36)[]
            sage: (4 + 6*x).is_nilpotent()
            False
            sage: (6*x + 12*y + 18*x*y + 24*(x^2+y^2)).is_nilpotent()
            True"""
    @overload
    def is_nilpotent(self) -> Any:
        """MPolynomial.is_nilpotent(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 2692)

        Return ``True`` if ``self`` is nilpotent, i.e., some power of ``self``
        is 0.

        EXAMPLES::

            sage: R.<x,y> = QQbar[]                                                     # needs sage.rings.number_field
            sage: (x + y).is_nilpotent()                                                # needs sage.rings.number_field
            False
            sage: R(0).is_nilpotent()                                                   # needs sage.rings.number_field
            True
            sage: _.<x,y> = Zmod(4)[]
            sage: (2*x).is_nilpotent()
            True
            sage: (2 + y*x).is_nilpotent()
            False
            sage: _.<x,y> = Zmod(36)[]
            sage: (4 + 6*x).is_nilpotent()
            False
            sage: (6*x + 12*y + 18*x*y + 24*(x^2+y^2)).is_nilpotent()
            True"""
    @overload
    def is_square(self, root=...) -> Any:
        """MPolynomial.is_square(self, root=False)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 2292)

        Test whether this polynomial is a square.

        INPUT:

        - ``root`` -- if set to ``True``, return a pair ``(True, root)``
          where ``root`` is a square root or ``(False, None)`` if
          it is not a square.

        EXAMPLES::

            sage: R.<a,b> = QQ[]
            sage: a.is_square()
            False
            sage: ((1+a*b^2)^2).is_square()
            True
            sage: ((1+a*b^2)^2).is_square(root=True)
            (True, a*b^2 + 1)"""
    @overload
    def is_square(self) -> Any:
        """MPolynomial.is_square(self, root=False)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 2292)

        Test whether this polynomial is a square.

        INPUT:

        - ``root`` -- if set to ``True``, return a pair ``(True, root)``
          where ``root`` is a square root or ``(False, None)`` if
          it is not a square.

        EXAMPLES::

            sage: R.<a,b> = QQ[]
            sage: a.is_square()
            False
            sage: ((1+a*b^2)^2).is_square()
            True
            sage: ((1+a*b^2)^2).is_square(root=True)
            (True, a*b^2 + 1)"""
    @overload
    def is_square(self) -> Any:
        """MPolynomial.is_square(self, root=False)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 2292)

        Test whether this polynomial is a square.

        INPUT:

        - ``root`` -- if set to ``True``, return a pair ``(True, root)``
          where ``root`` is a square root or ``(False, None)`` if
          it is not a square.

        EXAMPLES::

            sage: R.<a,b> = QQ[]
            sage: a.is_square()
            False
            sage: ((1+a*b^2)^2).is_square()
            True
            sage: ((1+a*b^2)^2).is_square(root=True)
            (True, a*b^2 + 1)"""
    @overload
    def is_square(self, root=...) -> Any:
        """MPolynomial.is_square(self, root=False)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 2292)

        Test whether this polynomial is a square.

        INPUT:

        - ``root`` -- if set to ``True``, return a pair ``(True, root)``
          where ``root`` is a square root or ``(False, None)`` if
          it is not a square.

        EXAMPLES::

            sage: R.<a,b> = QQ[]
            sage: a.is_square()
            False
            sage: ((1+a*b^2)^2).is_square()
            True
            sage: ((1+a*b^2)^2).is_square(root=True)
            (True, a*b^2 + 1)"""
    @overload
    def is_symmetric(self, group=...) -> Any:
        """MPolynomial.is_symmetric(self, group=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 968)

        Return whether this polynomial is symmetric.

        INPUT:

        - ``group`` -- (default: symmetric group) if set, test whether the
          polynomial is invariant with respect to the given permutation group

        EXAMPLES::

            sage: # needs sage.groups
            sage: R.<x,y,z> = QQ[]
            sage: p = (x+y+z)**2 - 3 * (x+y)*(x+z)*(y+z)
            sage: p.is_symmetric()
            True
            sage: (x + y - z).is_symmetric()
            False
            sage: R.one().is_symmetric()
            True
            sage: p = (x-y)*(y-z)*(z-x)
            sage: p.is_symmetric()
            False
            sage: p.is_symmetric(AlternatingGroup(3))
            True

            sage: R.<x,y> = QQ[]
            sage: ((x + y)**2).is_symmetric()                                           # needs sage.groups
            True
            sage: R.one().is_symmetric()                                                # needs sage.groups
            True
            sage: (x + 2*y).is_symmetric()                                              # needs sage.groups
            False

        An example with a GAP permutation group (here the quaternions)::

            sage: R = PolynomialRing(QQ, 'x', 8)
            sage: x = R.gens()
            sage: p = sum(prod(x[i] for i in e)
            ....:         for e in [(0,1,2), (0,1,7), (0,2,7), (1,2,7),
            ....:                   (3,4,5), (3,4,6), (3,5,6), (4,5,6)])
            sage: p.is_symmetric(libgap.TransitiveGroup(8, 5))                          # needs sage.groups
            True
            sage: p = sum(prod(x[i] for i in e)
            ....:     for e in [(0,1,2), (0,1,7), (0,2,7), (1,2,7),
            ....:               (3,4,5), (3,4,6), (3,5,6)])
            sage: p.is_symmetric(libgap.TransitiveGroup(8, 5))                          # needs sage.groups
            False

        TESTS::

            sage: R = PolynomialRing(QQ, 'x', 3)
            sage: R.one().is_symmetric(3)                                               # needs sage.groups
            Traceback (most recent call last):
            ...
            ValueError: argument must be a permutation group

            sage: R.one().is_symmetric(SymmetricGroup(4))                               # needs sage.groups
            Traceback (most recent call last):
            ...
            ValueError: invalid data to initialize a permutation"""
    @overload
    def is_symmetric(self) -> Any:
        """MPolynomial.is_symmetric(self, group=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 968)

        Return whether this polynomial is symmetric.

        INPUT:

        - ``group`` -- (default: symmetric group) if set, test whether the
          polynomial is invariant with respect to the given permutation group

        EXAMPLES::

            sage: # needs sage.groups
            sage: R.<x,y,z> = QQ[]
            sage: p = (x+y+z)**2 - 3 * (x+y)*(x+z)*(y+z)
            sage: p.is_symmetric()
            True
            sage: (x + y - z).is_symmetric()
            False
            sage: R.one().is_symmetric()
            True
            sage: p = (x-y)*(y-z)*(z-x)
            sage: p.is_symmetric()
            False
            sage: p.is_symmetric(AlternatingGroup(3))
            True

            sage: R.<x,y> = QQ[]
            sage: ((x + y)**2).is_symmetric()                                           # needs sage.groups
            True
            sage: R.one().is_symmetric()                                                # needs sage.groups
            True
            sage: (x + 2*y).is_symmetric()                                              # needs sage.groups
            False

        An example with a GAP permutation group (here the quaternions)::

            sage: R = PolynomialRing(QQ, 'x', 8)
            sage: x = R.gens()
            sage: p = sum(prod(x[i] for i in e)
            ....:         for e in [(0,1,2), (0,1,7), (0,2,7), (1,2,7),
            ....:                   (3,4,5), (3,4,6), (3,5,6), (4,5,6)])
            sage: p.is_symmetric(libgap.TransitiveGroup(8, 5))                          # needs sage.groups
            True
            sage: p = sum(prod(x[i] for i in e)
            ....:     for e in [(0,1,2), (0,1,7), (0,2,7), (1,2,7),
            ....:               (3,4,5), (3,4,6), (3,5,6)])
            sage: p.is_symmetric(libgap.TransitiveGroup(8, 5))                          # needs sage.groups
            False

        TESTS::

            sage: R = PolynomialRing(QQ, 'x', 3)
            sage: R.one().is_symmetric(3)                                               # needs sage.groups
            Traceback (most recent call last):
            ...
            ValueError: argument must be a permutation group

            sage: R.one().is_symmetric(SymmetricGroup(4))                               # needs sage.groups
            Traceback (most recent call last):
            ...
            ValueError: invalid data to initialize a permutation"""
    @overload
    def is_symmetric(self) -> Any:
        """MPolynomial.is_symmetric(self, group=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 968)

        Return whether this polynomial is symmetric.

        INPUT:

        - ``group`` -- (default: symmetric group) if set, test whether the
          polynomial is invariant with respect to the given permutation group

        EXAMPLES::

            sage: # needs sage.groups
            sage: R.<x,y,z> = QQ[]
            sage: p = (x+y+z)**2 - 3 * (x+y)*(x+z)*(y+z)
            sage: p.is_symmetric()
            True
            sage: (x + y - z).is_symmetric()
            False
            sage: R.one().is_symmetric()
            True
            sage: p = (x-y)*(y-z)*(z-x)
            sage: p.is_symmetric()
            False
            sage: p.is_symmetric(AlternatingGroup(3))
            True

            sage: R.<x,y> = QQ[]
            sage: ((x + y)**2).is_symmetric()                                           # needs sage.groups
            True
            sage: R.one().is_symmetric()                                                # needs sage.groups
            True
            sage: (x + 2*y).is_symmetric()                                              # needs sage.groups
            False

        An example with a GAP permutation group (here the quaternions)::

            sage: R = PolynomialRing(QQ, 'x', 8)
            sage: x = R.gens()
            sage: p = sum(prod(x[i] for i in e)
            ....:         for e in [(0,1,2), (0,1,7), (0,2,7), (1,2,7),
            ....:                   (3,4,5), (3,4,6), (3,5,6), (4,5,6)])
            sage: p.is_symmetric(libgap.TransitiveGroup(8, 5))                          # needs sage.groups
            True
            sage: p = sum(prod(x[i] for i in e)
            ....:     for e in [(0,1,2), (0,1,7), (0,2,7), (1,2,7),
            ....:               (3,4,5), (3,4,6), (3,5,6)])
            sage: p.is_symmetric(libgap.TransitiveGroup(8, 5))                          # needs sage.groups
            False

        TESTS::

            sage: R = PolynomialRing(QQ, 'x', 3)
            sage: R.one().is_symmetric(3)                                               # needs sage.groups
            Traceback (most recent call last):
            ...
            ValueError: argument must be a permutation group

            sage: R.one().is_symmetric(SymmetricGroup(4))                               # needs sage.groups
            Traceback (most recent call last):
            ...
            ValueError: invalid data to initialize a permutation"""
    @overload
    def is_symmetric(self) -> Any:
        """MPolynomial.is_symmetric(self, group=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 968)

        Return whether this polynomial is symmetric.

        INPUT:

        - ``group`` -- (default: symmetric group) if set, test whether the
          polynomial is invariant with respect to the given permutation group

        EXAMPLES::

            sage: # needs sage.groups
            sage: R.<x,y,z> = QQ[]
            sage: p = (x+y+z)**2 - 3 * (x+y)*(x+z)*(y+z)
            sage: p.is_symmetric()
            True
            sage: (x + y - z).is_symmetric()
            False
            sage: R.one().is_symmetric()
            True
            sage: p = (x-y)*(y-z)*(z-x)
            sage: p.is_symmetric()
            False
            sage: p.is_symmetric(AlternatingGroup(3))
            True

            sage: R.<x,y> = QQ[]
            sage: ((x + y)**2).is_symmetric()                                           # needs sage.groups
            True
            sage: R.one().is_symmetric()                                                # needs sage.groups
            True
            sage: (x + 2*y).is_symmetric()                                              # needs sage.groups
            False

        An example with a GAP permutation group (here the quaternions)::

            sage: R = PolynomialRing(QQ, 'x', 8)
            sage: x = R.gens()
            sage: p = sum(prod(x[i] for i in e)
            ....:         for e in [(0,1,2), (0,1,7), (0,2,7), (1,2,7),
            ....:                   (3,4,5), (3,4,6), (3,5,6), (4,5,6)])
            sage: p.is_symmetric(libgap.TransitiveGroup(8, 5))                          # needs sage.groups
            True
            sage: p = sum(prod(x[i] for i in e)
            ....:     for e in [(0,1,2), (0,1,7), (0,2,7), (1,2,7),
            ....:               (3,4,5), (3,4,6), (3,5,6)])
            sage: p.is_symmetric(libgap.TransitiveGroup(8, 5))                          # needs sage.groups
            False

        TESTS::

            sage: R = PolynomialRing(QQ, 'x', 3)
            sage: R.one().is_symmetric(3)                                               # needs sage.groups
            Traceback (most recent call last):
            ...
            ValueError: argument must be a permutation group

            sage: R.one().is_symmetric(SymmetricGroup(4))                               # needs sage.groups
            Traceback (most recent call last):
            ...
            ValueError: invalid data to initialize a permutation"""
    @overload
    def is_symmetric(self) -> Any:
        """MPolynomial.is_symmetric(self, group=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 968)

        Return whether this polynomial is symmetric.

        INPUT:

        - ``group`` -- (default: symmetric group) if set, test whether the
          polynomial is invariant with respect to the given permutation group

        EXAMPLES::

            sage: # needs sage.groups
            sage: R.<x,y,z> = QQ[]
            sage: p = (x+y+z)**2 - 3 * (x+y)*(x+z)*(y+z)
            sage: p.is_symmetric()
            True
            sage: (x + y - z).is_symmetric()
            False
            sage: R.one().is_symmetric()
            True
            sage: p = (x-y)*(y-z)*(z-x)
            sage: p.is_symmetric()
            False
            sage: p.is_symmetric(AlternatingGroup(3))
            True

            sage: R.<x,y> = QQ[]
            sage: ((x + y)**2).is_symmetric()                                           # needs sage.groups
            True
            sage: R.one().is_symmetric()                                                # needs sage.groups
            True
            sage: (x + 2*y).is_symmetric()                                              # needs sage.groups
            False

        An example with a GAP permutation group (here the quaternions)::

            sage: R = PolynomialRing(QQ, 'x', 8)
            sage: x = R.gens()
            sage: p = sum(prod(x[i] for i in e)
            ....:         for e in [(0,1,2), (0,1,7), (0,2,7), (1,2,7),
            ....:                   (3,4,5), (3,4,6), (3,5,6), (4,5,6)])
            sage: p.is_symmetric(libgap.TransitiveGroup(8, 5))                          # needs sage.groups
            True
            sage: p = sum(prod(x[i] for i in e)
            ....:     for e in [(0,1,2), (0,1,7), (0,2,7), (1,2,7),
            ....:               (3,4,5), (3,4,6), (3,5,6)])
            sage: p.is_symmetric(libgap.TransitiveGroup(8, 5))                          # needs sage.groups
            False

        TESTS::

            sage: R = PolynomialRing(QQ, 'x', 3)
            sage: R.one().is_symmetric(3)                                               # needs sage.groups
            Traceback (most recent call last):
            ...
            ValueError: argument must be a permutation group

            sage: R.one().is_symmetric(SymmetricGroup(4))                               # needs sage.groups
            Traceback (most recent call last):
            ...
            ValueError: invalid data to initialize a permutation"""
    @overload
    def is_symmetric(self) -> Any:
        """MPolynomial.is_symmetric(self, group=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 968)

        Return whether this polynomial is symmetric.

        INPUT:

        - ``group`` -- (default: symmetric group) if set, test whether the
          polynomial is invariant with respect to the given permutation group

        EXAMPLES::

            sage: # needs sage.groups
            sage: R.<x,y,z> = QQ[]
            sage: p = (x+y+z)**2 - 3 * (x+y)*(x+z)*(y+z)
            sage: p.is_symmetric()
            True
            sage: (x + y - z).is_symmetric()
            False
            sage: R.one().is_symmetric()
            True
            sage: p = (x-y)*(y-z)*(z-x)
            sage: p.is_symmetric()
            False
            sage: p.is_symmetric(AlternatingGroup(3))
            True

            sage: R.<x,y> = QQ[]
            sage: ((x + y)**2).is_symmetric()                                           # needs sage.groups
            True
            sage: R.one().is_symmetric()                                                # needs sage.groups
            True
            sage: (x + 2*y).is_symmetric()                                              # needs sage.groups
            False

        An example with a GAP permutation group (here the quaternions)::

            sage: R = PolynomialRing(QQ, 'x', 8)
            sage: x = R.gens()
            sage: p = sum(prod(x[i] for i in e)
            ....:         for e in [(0,1,2), (0,1,7), (0,2,7), (1,2,7),
            ....:                   (3,4,5), (3,4,6), (3,5,6), (4,5,6)])
            sage: p.is_symmetric(libgap.TransitiveGroup(8, 5))                          # needs sage.groups
            True
            sage: p = sum(prod(x[i] for i in e)
            ....:     for e in [(0,1,2), (0,1,7), (0,2,7), (1,2,7),
            ....:               (3,4,5), (3,4,6), (3,5,6)])
            sage: p.is_symmetric(libgap.TransitiveGroup(8, 5))                          # needs sage.groups
            False

        TESTS::

            sage: R = PolynomialRing(QQ, 'x', 3)
            sage: R.one().is_symmetric(3)                                               # needs sage.groups
            Traceback (most recent call last):
            ...
            ValueError: argument must be a permutation group

            sage: R.one().is_symmetric(SymmetricGroup(4))                               # needs sage.groups
            Traceback (most recent call last):
            ...
            ValueError: invalid data to initialize a permutation"""
    @overload
    def is_symmetric(self) -> Any:
        """MPolynomial.is_symmetric(self, group=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 968)

        Return whether this polynomial is symmetric.

        INPUT:

        - ``group`` -- (default: symmetric group) if set, test whether the
          polynomial is invariant with respect to the given permutation group

        EXAMPLES::

            sage: # needs sage.groups
            sage: R.<x,y,z> = QQ[]
            sage: p = (x+y+z)**2 - 3 * (x+y)*(x+z)*(y+z)
            sage: p.is_symmetric()
            True
            sage: (x + y - z).is_symmetric()
            False
            sage: R.one().is_symmetric()
            True
            sage: p = (x-y)*(y-z)*(z-x)
            sage: p.is_symmetric()
            False
            sage: p.is_symmetric(AlternatingGroup(3))
            True

            sage: R.<x,y> = QQ[]
            sage: ((x + y)**2).is_symmetric()                                           # needs sage.groups
            True
            sage: R.one().is_symmetric()                                                # needs sage.groups
            True
            sage: (x + 2*y).is_symmetric()                                              # needs sage.groups
            False

        An example with a GAP permutation group (here the quaternions)::

            sage: R = PolynomialRing(QQ, 'x', 8)
            sage: x = R.gens()
            sage: p = sum(prod(x[i] for i in e)
            ....:         for e in [(0,1,2), (0,1,7), (0,2,7), (1,2,7),
            ....:                   (3,4,5), (3,4,6), (3,5,6), (4,5,6)])
            sage: p.is_symmetric(libgap.TransitiveGroup(8, 5))                          # needs sage.groups
            True
            sage: p = sum(prod(x[i] for i in e)
            ....:     for e in [(0,1,2), (0,1,7), (0,2,7), (1,2,7),
            ....:               (3,4,5), (3,4,6), (3,5,6)])
            sage: p.is_symmetric(libgap.TransitiveGroup(8, 5))                          # needs sage.groups
            False

        TESTS::

            sage: R = PolynomialRing(QQ, 'x', 3)
            sage: R.one().is_symmetric(3)                                               # needs sage.groups
            Traceback (most recent call last):
            ...
            ValueError: argument must be a permutation group

            sage: R.one().is_symmetric(SymmetricGroup(4))                               # needs sage.groups
            Traceback (most recent call last):
            ...
            ValueError: invalid data to initialize a permutation"""
    @overload
    def is_symmetric(self) -> Any:
        """MPolynomial.is_symmetric(self, group=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 968)

        Return whether this polynomial is symmetric.

        INPUT:

        - ``group`` -- (default: symmetric group) if set, test whether the
          polynomial is invariant with respect to the given permutation group

        EXAMPLES::

            sage: # needs sage.groups
            sage: R.<x,y,z> = QQ[]
            sage: p = (x+y+z)**2 - 3 * (x+y)*(x+z)*(y+z)
            sage: p.is_symmetric()
            True
            sage: (x + y - z).is_symmetric()
            False
            sage: R.one().is_symmetric()
            True
            sage: p = (x-y)*(y-z)*(z-x)
            sage: p.is_symmetric()
            False
            sage: p.is_symmetric(AlternatingGroup(3))
            True

            sage: R.<x,y> = QQ[]
            sage: ((x + y)**2).is_symmetric()                                           # needs sage.groups
            True
            sage: R.one().is_symmetric()                                                # needs sage.groups
            True
            sage: (x + 2*y).is_symmetric()                                              # needs sage.groups
            False

        An example with a GAP permutation group (here the quaternions)::

            sage: R = PolynomialRing(QQ, 'x', 8)
            sage: x = R.gens()
            sage: p = sum(prod(x[i] for i in e)
            ....:         for e in [(0,1,2), (0,1,7), (0,2,7), (1,2,7),
            ....:                   (3,4,5), (3,4,6), (3,5,6), (4,5,6)])
            sage: p.is_symmetric(libgap.TransitiveGroup(8, 5))                          # needs sage.groups
            True
            sage: p = sum(prod(x[i] for i in e)
            ....:     for e in [(0,1,2), (0,1,7), (0,2,7), (1,2,7),
            ....:               (3,4,5), (3,4,6), (3,5,6)])
            sage: p.is_symmetric(libgap.TransitiveGroup(8, 5))                          # needs sage.groups
            False

        TESTS::

            sage: R = PolynomialRing(QQ, 'x', 3)
            sage: R.one().is_symmetric(3)                                               # needs sage.groups
            Traceback (most recent call last):
            ...
            ValueError: argument must be a permutation group

            sage: R.one().is_symmetric(SymmetricGroup(4))                               # needs sage.groups
            Traceback (most recent call last):
            ...
            ValueError: invalid data to initialize a permutation"""
    @overload
    def is_unit(self) -> bool:
        """MPolynomial.is_unit(self) -> bool

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 2646)

        Return ``True`` if ``self`` is a unit, that is, has a
        multiplicative inverse.

        EXAMPLES::

            sage: # needs sage.rings.number_field
            sage: R.<x,y> = QQbar[]
            sage: (x + y).is_unit()
            False
            sage: R(0).is_unit()
            False
            sage: R(-1).is_unit()
            True
            sage: R(-1 + x).is_unit()
            False
            sage: R(2).is_unit()
            True

        Check that :issue:`22454` is fixed::

            sage: _.<x,y> = Zmod(4)[]
            sage: (1 + 2*x).is_unit()
            True
            sage: (x*y).is_unit()
            False
            sage: _.<x,y> = Zmod(36)[]
            sage: (7+ 6*x + 12*y - 18*x*y).is_unit()
            True"""
    @overload
    def is_unit(self) -> Any:
        """MPolynomial.is_unit(self) -> bool

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 2646)

        Return ``True`` if ``self`` is a unit, that is, has a
        multiplicative inverse.

        EXAMPLES::

            sage: # needs sage.rings.number_field
            sage: R.<x,y> = QQbar[]
            sage: (x + y).is_unit()
            False
            sage: R(0).is_unit()
            False
            sage: R(-1).is_unit()
            True
            sage: R(-1 + x).is_unit()
            False
            sage: R(2).is_unit()
            True

        Check that :issue:`22454` is fixed::

            sage: _.<x,y> = Zmod(4)[]
            sage: (1 + 2*x).is_unit()
            True
            sage: (x*y).is_unit()
            False
            sage: _.<x,y> = Zmod(36)[]
            sage: (7+ 6*x + 12*y - 18*x*y).is_unit()
            True"""
    @overload
    def is_unit(self) -> Any:
        """MPolynomial.is_unit(self) -> bool

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 2646)

        Return ``True`` if ``self`` is a unit, that is, has a
        multiplicative inverse.

        EXAMPLES::

            sage: # needs sage.rings.number_field
            sage: R.<x,y> = QQbar[]
            sage: (x + y).is_unit()
            False
            sage: R(0).is_unit()
            False
            sage: R(-1).is_unit()
            True
            sage: R(-1 + x).is_unit()
            False
            sage: R(2).is_unit()
            True

        Check that :issue:`22454` is fixed::

            sage: _.<x,y> = Zmod(4)[]
            sage: (1 + 2*x).is_unit()
            True
            sage: (x*y).is_unit()
            False
            sage: _.<x,y> = Zmod(36)[]
            sage: (7+ 6*x + 12*y - 18*x*y).is_unit()
            True"""
    @overload
    def is_unit(self) -> Any:
        """MPolynomial.is_unit(self) -> bool

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 2646)

        Return ``True`` if ``self`` is a unit, that is, has a
        multiplicative inverse.

        EXAMPLES::

            sage: # needs sage.rings.number_field
            sage: R.<x,y> = QQbar[]
            sage: (x + y).is_unit()
            False
            sage: R(0).is_unit()
            False
            sage: R(-1).is_unit()
            True
            sage: R(-1 + x).is_unit()
            False
            sage: R(2).is_unit()
            True

        Check that :issue:`22454` is fixed::

            sage: _.<x,y> = Zmod(4)[]
            sage: (1 + 2*x).is_unit()
            True
            sage: (x*y).is_unit()
            False
            sage: _.<x,y> = Zmod(36)[]
            sage: (7+ 6*x + 12*y - 18*x*y).is_unit()
            True"""
    @overload
    def is_unit(self) -> Any:
        """MPolynomial.is_unit(self) -> bool

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 2646)

        Return ``True`` if ``self`` is a unit, that is, has a
        multiplicative inverse.

        EXAMPLES::

            sage: # needs sage.rings.number_field
            sage: R.<x,y> = QQbar[]
            sage: (x + y).is_unit()
            False
            sage: R(0).is_unit()
            False
            sage: R(-1).is_unit()
            True
            sage: R(-1 + x).is_unit()
            False
            sage: R(2).is_unit()
            True

        Check that :issue:`22454` is fixed::

            sage: _.<x,y> = Zmod(4)[]
            sage: (1 + 2*x).is_unit()
            True
            sage: (x*y).is_unit()
            False
            sage: _.<x,y> = Zmod(36)[]
            sage: (7+ 6*x + 12*y - 18*x*y).is_unit()
            True"""
    @overload
    def is_unit(self) -> Any:
        """MPolynomial.is_unit(self) -> bool

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 2646)

        Return ``True`` if ``self`` is a unit, that is, has a
        multiplicative inverse.

        EXAMPLES::

            sage: # needs sage.rings.number_field
            sage: R.<x,y> = QQbar[]
            sage: (x + y).is_unit()
            False
            sage: R(0).is_unit()
            False
            sage: R(-1).is_unit()
            True
            sage: R(-1 + x).is_unit()
            False
            sage: R(2).is_unit()
            True

        Check that :issue:`22454` is fixed::

            sage: _.<x,y> = Zmod(4)[]
            sage: (1 + 2*x).is_unit()
            True
            sage: (x*y).is_unit()
            False
            sage: _.<x,y> = Zmod(36)[]
            sage: (7+ 6*x + 12*y - 18*x*y).is_unit()
            True"""
    @overload
    def is_unit(self) -> Any:
        """MPolynomial.is_unit(self) -> bool

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 2646)

        Return ``True`` if ``self`` is a unit, that is, has a
        multiplicative inverse.

        EXAMPLES::

            sage: # needs sage.rings.number_field
            sage: R.<x,y> = QQbar[]
            sage: (x + y).is_unit()
            False
            sage: R(0).is_unit()
            False
            sage: R(-1).is_unit()
            True
            sage: R(-1 + x).is_unit()
            False
            sage: R(2).is_unit()
            True

        Check that :issue:`22454` is fixed::

            sage: _.<x,y> = Zmod(4)[]
            sage: (1 + 2*x).is_unit()
            True
            sage: (x*y).is_unit()
            False
            sage: _.<x,y> = Zmod(36)[]
            sage: (7+ 6*x + 12*y - 18*x*y).is_unit()
            True"""
    @overload
    def is_unit(self) -> Any:
        """MPolynomial.is_unit(self) -> bool

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 2646)

        Return ``True`` if ``self`` is a unit, that is, has a
        multiplicative inverse.

        EXAMPLES::

            sage: # needs sage.rings.number_field
            sage: R.<x,y> = QQbar[]
            sage: (x + y).is_unit()
            False
            sage: R(0).is_unit()
            False
            sage: R(-1).is_unit()
            True
            sage: R(-1 + x).is_unit()
            False
            sage: R(2).is_unit()
            True

        Check that :issue:`22454` is fixed::

            sage: _.<x,y> = Zmod(4)[]
            sage: (1 + 2*x).is_unit()
            True
            sage: (x*y).is_unit()
            False
            sage: _.<x,y> = Zmod(36)[]
            sage: (7+ 6*x + 12*y - 18*x*y).is_unit()
            True"""
    @overload
    def is_unit(self) -> Any:
        """MPolynomial.is_unit(self) -> bool

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 2646)

        Return ``True`` if ``self`` is a unit, that is, has a
        multiplicative inverse.

        EXAMPLES::

            sage: # needs sage.rings.number_field
            sage: R.<x,y> = QQbar[]
            sage: (x + y).is_unit()
            False
            sage: R(0).is_unit()
            False
            sage: R(-1).is_unit()
            True
            sage: R(-1 + x).is_unit()
            False
            sage: R(2).is_unit()
            True

        Check that :issue:`22454` is fixed::

            sage: _.<x,y> = Zmod(4)[]
            sage: (1 + 2*x).is_unit()
            True
            sage: (x*y).is_unit()
            False
            sage: _.<x,y> = Zmod(36)[]
            sage: (7+ 6*x + 12*y - 18*x*y).is_unit()
            True"""
    @overload
    def iterator_exp_coeff(self, as_ETuples=...) -> Any:
        """MPolynomial.iterator_exp_coeff(self, as_ETuples=True)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 1258)

        Iterate over ``self`` as pairs of ((E)Tuple, coefficient).

        INPUT:

        - ``as_ETuples`` -- boolean (default: ``True``); if ``True``, iterate over
          pairs whose first element is an :class:`ETuple`, otherwise as a tuples

        EXAMPLES::

            sage: R.<a,b,c> = QQ[]
            sage: f = a*c^3 + a^2*b + 2*b^4
            sage: list(f.iterator_exp_coeff())
            [((0, 4, 0), 2), ((1, 0, 3), 1), ((2, 1, 0), 1)]
            sage: list(f.iterator_exp_coeff(as_ETuples=False))
            [((0, 4, 0), 2), ((1, 0, 3), 1), ((2, 1, 0), 1)]

            sage: R.<a,b,c> = PolynomialRing(QQ, 3, order='lex')
            sage: f = a*c^3 + a^2*b + 2*b^4
            sage: list(f.iterator_exp_coeff())
            [((2, 1, 0), 1), ((1, 0, 3), 1), ((0, 4, 0), 2)]"""
    @overload
    def iterator_exp_coeff(self) -> Any:
        """MPolynomial.iterator_exp_coeff(self, as_ETuples=True)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 1258)

        Iterate over ``self`` as pairs of ((E)Tuple, coefficient).

        INPUT:

        - ``as_ETuples`` -- boolean (default: ``True``); if ``True``, iterate over
          pairs whose first element is an :class:`ETuple`, otherwise as a tuples

        EXAMPLES::

            sage: R.<a,b,c> = QQ[]
            sage: f = a*c^3 + a^2*b + 2*b^4
            sage: list(f.iterator_exp_coeff())
            [((0, 4, 0), 2), ((1, 0, 3), 1), ((2, 1, 0), 1)]
            sage: list(f.iterator_exp_coeff(as_ETuples=False))
            [((0, 4, 0), 2), ((1, 0, 3), 1), ((2, 1, 0), 1)]

            sage: R.<a,b,c> = PolynomialRing(QQ, 3, order='lex')
            sage: f = a*c^3 + a^2*b + 2*b^4
            sage: list(f.iterator_exp_coeff())
            [((2, 1, 0), 1), ((1, 0, 3), 1), ((0, 4, 0), 2)]"""
    @overload
    def iterator_exp_coeff(self, as_ETuples=...) -> Any:
        """MPolynomial.iterator_exp_coeff(self, as_ETuples=True)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 1258)

        Iterate over ``self`` as pairs of ((E)Tuple, coefficient).

        INPUT:

        - ``as_ETuples`` -- boolean (default: ``True``); if ``True``, iterate over
          pairs whose first element is an :class:`ETuple`, otherwise as a tuples

        EXAMPLES::

            sage: R.<a,b,c> = QQ[]
            sage: f = a*c^3 + a^2*b + 2*b^4
            sage: list(f.iterator_exp_coeff())
            [((0, 4, 0), 2), ((1, 0, 3), 1), ((2, 1, 0), 1)]
            sage: list(f.iterator_exp_coeff(as_ETuples=False))
            [((0, 4, 0), 2), ((1, 0, 3), 1), ((2, 1, 0), 1)]

            sage: R.<a,b,c> = PolynomialRing(QQ, 3, order='lex')
            sage: f = a*c^3 + a^2*b + 2*b^4
            sage: list(f.iterator_exp_coeff())
            [((2, 1, 0), 1), ((1, 0, 3), 1), ((0, 4, 0), 2)]"""
    @overload
    def iterator_exp_coeff(self) -> Any:
        """MPolynomial.iterator_exp_coeff(self, as_ETuples=True)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 1258)

        Iterate over ``self`` as pairs of ((E)Tuple, coefficient).

        INPUT:

        - ``as_ETuples`` -- boolean (default: ``True``); if ``True``, iterate over
          pairs whose first element is an :class:`ETuple`, otherwise as a tuples

        EXAMPLES::

            sage: R.<a,b,c> = QQ[]
            sage: f = a*c^3 + a^2*b + 2*b^4
            sage: list(f.iterator_exp_coeff())
            [((0, 4, 0), 2), ((1, 0, 3), 1), ((2, 1, 0), 1)]
            sage: list(f.iterator_exp_coeff(as_ETuples=False))
            [((0, 4, 0), 2), ((1, 0, 3), 1), ((2, 1, 0), 1)]

            sage: R.<a,b,c> = PolynomialRing(QQ, 3, order='lex')
            sage: f = a*c^3 + a^2*b + 2*b^4
            sage: list(f.iterator_exp_coeff())
            [((2, 1, 0), 1), ((1, 0, 3), 1), ((0, 4, 0), 2)]"""
    @overload
    def jacobian_ideal(self) -> Any:
        """MPolynomial.jacobian_ideal(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 1197)

        Return the Jacobian ideal of the polynomial ``self``.

        EXAMPLES::

            sage: R.<x,y,z> = QQ[]
            sage: f = x^3 + y^3 + z^3
            sage: f.jacobian_ideal()
            Ideal (3*x^2, 3*y^2, 3*z^2) of
             Multivariate Polynomial Ring in x, y, z over Rational Field"""
    @overload
    def jacobian_ideal(self) -> Any:
        """MPolynomial.jacobian_ideal(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 1197)

        Return the Jacobian ideal of the polynomial ``self``.

        EXAMPLES::

            sage: R.<x,y,z> = QQ[]
            sage: f = x^3 + y^3 + z^3
            sage: f.jacobian_ideal()
            Ideal (3*x^2, 3*y^2, 3*z^2) of
             Multivariate Polynomial Ring in x, y, z over Rational Field"""
    @overload
    def leading_support(self, *args, **kwds) -> Any:
        """MPolynomial.leading_support(self, *args, **kwds)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 211)

        Return the maximal element of the support of ``self``,
        according to the term order.

        If the term ordering of the basis elements is not what is
        desired, a comparison key, ``key(x)``, can be provided.

        EXAMPLES::

            sage: R.<x,y,z> = PolynomialRing(QQ)
            sage: (3*x*y^2 + 2*y*z^3 + y^4 + 4*x*y*z).leading_support()
            (0, 4, 0)
            sage: R.<x,y,z> = PolynomialRing(QQ, order='lex')
            sage: (3*x*y^2 + 2*y*z^3 + y^4 + 4*x*y*z).leading_support()
            (1, 2, 0)
            sage: R.<x,y,z> = PolynomialRing(QQ, order='invlex')
            sage: (3*x*y^2 + 2*y*z^3 + y^4 + 4*x*y*z).leading_support()
            (0, 1, 3)"""
    @overload
    def leading_support(self) -> Any:
        """MPolynomial.leading_support(self, *args, **kwds)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 211)

        Return the maximal element of the support of ``self``,
        according to the term order.

        If the term ordering of the basis elements is not what is
        desired, a comparison key, ``key(x)``, can be provided.

        EXAMPLES::

            sage: R.<x,y,z> = PolynomialRing(QQ)
            sage: (3*x*y^2 + 2*y*z^3 + y^4 + 4*x*y*z).leading_support()
            (0, 4, 0)
            sage: R.<x,y,z> = PolynomialRing(QQ, order='lex')
            sage: (3*x*y^2 + 2*y*z^3 + y^4 + 4*x*y*z).leading_support()
            (1, 2, 0)
            sage: R.<x,y,z> = PolynomialRing(QQ, order='invlex')
            sage: (3*x*y^2 + 2*y*z^3 + y^4 + 4*x*y*z).leading_support()
            (0, 1, 3)"""
    @overload
    def leading_support(self) -> Any:
        """MPolynomial.leading_support(self, *args, **kwds)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 211)

        Return the maximal element of the support of ``self``,
        according to the term order.

        If the term ordering of the basis elements is not what is
        desired, a comparison key, ``key(x)``, can be provided.

        EXAMPLES::

            sage: R.<x,y,z> = PolynomialRing(QQ)
            sage: (3*x*y^2 + 2*y*z^3 + y^4 + 4*x*y*z).leading_support()
            (0, 4, 0)
            sage: R.<x,y,z> = PolynomialRing(QQ, order='lex')
            sage: (3*x*y^2 + 2*y*z^3 + y^4 + 4*x*y*z).leading_support()
            (1, 2, 0)
            sage: R.<x,y,z> = PolynomialRing(QQ, order='invlex')
            sage: (3*x*y^2 + 2*y*z^3 + y^4 + 4*x*y*z).leading_support()
            (0, 1, 3)"""
    @overload
    def leading_support(self) -> Any:
        """MPolynomial.leading_support(self, *args, **kwds)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 211)

        Return the maximal element of the support of ``self``,
        according to the term order.

        If the term ordering of the basis elements is not what is
        desired, a comparison key, ``key(x)``, can be provided.

        EXAMPLES::

            sage: R.<x,y,z> = PolynomialRing(QQ)
            sage: (3*x*y^2 + 2*y*z^3 + y^4 + 4*x*y*z).leading_support()
            (0, 4, 0)
            sage: R.<x,y,z> = PolynomialRing(QQ, order='lex')
            sage: (3*x*y^2 + 2*y*z^3 + y^4 + 4*x*y*z).leading_support()
            (1, 2, 0)
            sage: R.<x,y,z> = PolynomialRing(QQ, order='invlex')
            sage: (3*x*y^2 + 2*y*z^3 + y^4 + 4*x*y*z).leading_support()
            (0, 1, 3)"""
    def lift(self, I) -> Any:
        """MPolynomial.lift(self, I)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 1978)

        Given an ideal `I = (f_1,\\dots,f_r)` that contains ``self``,
        find `s_1,\\dots,s_r` such that ``self`` `= s_1 f_1 + ... + s_r f_r`.

        INPUT:

        - ``I`` -- an ideal in ``self.parent()`` or tuple of generators of that ideal

        EXAMPLES::

            sage: # needs sage.rings.real_mpfr
            sage: A.<x,y> = PolynomialRing(CC, 2, order='degrevlex')
            sage: I = A.ideal([x^10 + x^9*y^2, y^8 - x^2*y^7 ])
            sage: f = x*y^13 + y^12
            sage: M = f.lift(I); M                                                      # needs sage.libs.singular
            [y^7, x^7*y^2 + x^8 + x^5*y^3 + x^6*y + x^3*y^4 + x^4*y^2 + x*y^5 + x^2*y^3 + y^4]
            sage: sum(map(mul, zip(M, I.gens()))) == f                                  # needs sage.libs.singular
            True"""
    def macaulay_resultant(self, *args) -> Any:
        """MPolynomial.macaulay_resultant(self, *args)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 1699)

        This is an implementation of the Macaulay resultant. It computes
        the resultant of universal polynomials as well as polynomials
        with constant coefficients. This is a project done in
        sage days 55. It's based on the implementation in Maple by
        Manfred Minimair, which in turn is based on the references [CLO], [Can], [Mac].
        It calculates the Macaulay resultant for a list of Polynomials,
        up to sign!

        AUTHORS:

        - Hao Chen, Solomon Vishkautsan (7-2014)

        INPUT:

        - ``args`` -- list of `n-1` homogeneous polynomials in `n` variables;
          works when ``args[0]`` is the list of polynomials, or ``args`` is
          itself the list of polynomials

        OUTPUT: the Macaulay resultant

        EXAMPLES:

        The number of polynomials has to match the number of variables::

            sage: R.<x,y,z> = PolynomialRing(QQ, 3)
            sage: y.macaulay_resultant(x + z)                                           # needs sage.modules
            Traceback (most recent call last):
            ...
            TypeError: number of polynomials(= 2) must equal number of variables (= 3)

        The polynomials need to be all homogeneous::

            sage: R.<x,y,z> = PolynomialRing(QQ, 3)
            sage: y.macaulay_resultant([x + z, z + x^3])                                # needs sage.modules
            Traceback (most recent call last):
            ...
            TypeError: resultant for non-homogeneous polynomials is not supported

        All polynomials must be in the same ring::

            sage: R.<x,y,z> = PolynomialRing(QQ, 3)
            sage: S.<x,y> = PolynomialRing(QQ, 2)
            sage: y.macaulay_resultant(z + x, z)                                        # needs sage.modules
            Traceback (most recent call last):
            ...
            TypeError: not all inputs are polynomials in the calling ring

        The following example recreates Proposition 2.10 in Ch.3 of Using Algebraic Geometry::

            sage: K.<x,y> = PolynomialRing(ZZ, 2)
            sage: flist, R = K._macaulay_resultant_universal_polynomials([1,1,2])
            sage: flist[0].macaulay_resultant(flist[1:])                                # needs sage.modules
            u2^2*u4^2*u6 - 2*u1*u2*u4*u5*u6 + u1^2*u5^2*u6 - u2^2*u3*u4*u7 + u1*u2*u3*u5*u7
            + u0*u2*u4*u5*u7 - u0*u1*u5^2*u7 + u1*u2*u3*u4*u8 - u0*u2*u4^2*u8 - u1^2*u3*u5*u8
            + u0*u1*u4*u5*u8 + u2^2*u3^2*u9 - 2*u0*u2*u3*u5*u9 + u0^2*u5^2*u9
            - u1*u2*u3^2*u10 + u0*u2*u3*u4*u10 + u0*u1*u3*u5*u10 - u0^2*u4*u5*u10
            + u1^2*u3^2*u11 - 2*u0*u1*u3*u4*u11 + u0^2*u4^2*u11

        The following example degenerates into the determinant of a `3\\times 3` matrix::

            sage: K.<x,y> = PolynomialRing(ZZ, 2)
            sage: flist, R = K._macaulay_resultant_universal_polynomials([1,1,1])
            sage: flist[0].macaulay_resultant(flist[1:])                                # needs sage.modules
            -u2*u4*u6 + u1*u5*u6 + u2*u3*u7 - u0*u5*u7 - u1*u3*u8 + u0*u4*u8

        The following example is by Patrick Ingram (:arxiv:`1310.4114`)::

            sage: U = PolynomialRing(ZZ,'y',2); y0,y1 = U.gens()
            sage: R = PolynomialRing(U,'x',3); x0,x1,x2 = R.gens()
            sage: f0 = y0*x2^2 - x0^2 + 2*x1*x2
            sage: f1 = y1*x2^2 - x1^2 + 2*x0*x2
            sage: f2 = x0*x1 - x2^2
            sage: f0.macaulay_resultant(f1, f2)                                         # needs sage.modules
            y0^2*y1^2 - 4*y0^3 - 4*y1^3 + 18*y0*y1 - 27

        a simple example with constant rational coefficients::

            sage: R.<x,y,z,w> = PolynomialRing(QQ, 4)
            sage: w.macaulay_resultant([z, y, x])                                       # needs sage.modules
            1

        an example where the resultant vanishes::

            sage: R.<x,y,z> = PolynomialRing(QQ, 3)
            sage: (x + y).macaulay_resultant([y^2, x])                                  # needs sage.modules
            0

        an example of bad reduction at a prime ``p = 5``::

            sage: R.<x,y,z> = PolynomialRing(QQ, 3)
            sage: y.macaulay_resultant([x^3 + 25*y^2*x, 5*z])                           # needs sage.libs.pari sage.modules
            125

        The input can given as an unpacked list of polynomials::

            sage: R.<x,y,z> = PolynomialRing(QQ, 3)
            sage: y.macaulay_resultant(x^3 + 25*y^2*x, 5*z)                             # needs sage.libs.pari sage.modules
            125

        an example when the coefficients live in a finite field::

            sage: F = FiniteField(11)
            sage: R.<x,y,z,w> = PolynomialRing(F, 4)
            sage: z.macaulay_resultant([x^3, 5*y, w])                                   # needs sage.modules sage.rings.finite_rings
            4

        example when the denominator in the algorithm vanishes(in this case
        the resultant is the constant term of the quotient of
        char polynomials of numerator/denominator)::

            sage: R.<x,y,z> = PolynomialRing(QQ, 3)
            sage: y.macaulay_resultant([x + z, z^2])                                    # needs sage.libs.pari sage.modules
            -1

        When there are only 2 polynomials, the Macaulay resultant degenerates to the traditional resultant::

            sage: R.<x> = PolynomialRing(QQ, 1)
            sage: f = x^2 + 1; g = x^5 + 1
            sage: fh = f.homogenize()
            sage: gh = g.homogenize()
            sage: RH = fh.parent()
            sage: f.resultant(g) == fh.macaulay_resultant(gh)                           # needs sage.modules
            True"""
    @overload
    def map_coefficients(self, f, new_base_ring=...) -> Any:
        """MPolynomial.map_coefficients(self, f, new_base_ring=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 1371)

        Return the polynomial obtained by applying ``f`` to the nonzero
        coefficients of ``self``.

        If ``f`` is a :class:`sage.categories.map.Map`, then the resulting
        polynomial will be defined over the codomain of ``f``. Otherwise, the
        resulting polynomial will be over the same ring as ``self``. Set
        ``new_base_ring`` to override this behaviour.

        INPUT:

        - ``f`` -- a callable that will be applied to the coefficients of ``self``

        - ``new_base_ring`` -- (optional) if given, the resulting polynomial
          will be defined over this ring

        EXAMPLES::

            sage: k.<a> = GF(9); R.<x,y> = k[];  f = x*a + 2*x^3*y*a + a                # needs sage.rings.finite_rings
            sage: f.map_coefficients(lambda a: a + 1)                                   # needs sage.rings.finite_rings
            (-a + 1)*x^3*y + (a + 1)*x + (a + 1)

        Examples with different base ring::

            sage: # needs sage.rings.finite_rings
            sage: R.<r> = GF(9); S.<s> = GF(81)
            sage: h = Hom(R,S)[0]; h
            Ring morphism:
              From: Finite Field in r of size 3^2
              To:   Finite Field in s of size 3^4
              Defn: r |--> 2*s^3 + 2*s^2 + 1
            sage: T.<X,Y> = R[]
            sage: f = r*X + Y
            sage: g = f.map_coefficients(h); g
            (-s^3 - s^2 + 1)*X + Y
            sage: g.parent()
            Multivariate Polynomial Ring in X, Y over Finite Field in s of size 3^4
            sage: h = lambda x: x.trace()
            sage: g = f.map_coefficients(h); g
            X - Y
            sage: g.parent()
            Multivariate Polynomial Ring in X, Y over Finite Field in r of size 3^2
            sage: g = f.map_coefficients(h, new_base_ring=GF(3)); g
            X - Y
            sage: g.parent()
            Multivariate Polynomial Ring in X, Y over Finite Field of size 3"""
    @overload
    def map_coefficients(self, lambdaa) -> Any:
        """MPolynomial.map_coefficients(self, f, new_base_ring=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 1371)

        Return the polynomial obtained by applying ``f`` to the nonzero
        coefficients of ``self``.

        If ``f`` is a :class:`sage.categories.map.Map`, then the resulting
        polynomial will be defined over the codomain of ``f``. Otherwise, the
        resulting polynomial will be over the same ring as ``self``. Set
        ``new_base_ring`` to override this behaviour.

        INPUT:

        - ``f`` -- a callable that will be applied to the coefficients of ``self``

        - ``new_base_ring`` -- (optional) if given, the resulting polynomial
          will be defined over this ring

        EXAMPLES::

            sage: k.<a> = GF(9); R.<x,y> = k[];  f = x*a + 2*x^3*y*a + a                # needs sage.rings.finite_rings
            sage: f.map_coefficients(lambda a: a + 1)                                   # needs sage.rings.finite_rings
            (-a + 1)*x^3*y + (a + 1)*x + (a + 1)

        Examples with different base ring::

            sage: # needs sage.rings.finite_rings
            sage: R.<r> = GF(9); S.<s> = GF(81)
            sage: h = Hom(R,S)[0]; h
            Ring morphism:
              From: Finite Field in r of size 3^2
              To:   Finite Field in s of size 3^4
              Defn: r |--> 2*s^3 + 2*s^2 + 1
            sage: T.<X,Y> = R[]
            sage: f = r*X + Y
            sage: g = f.map_coefficients(h); g
            (-s^3 - s^2 + 1)*X + Y
            sage: g.parent()
            Multivariate Polynomial Ring in X, Y over Finite Field in s of size 3^4
            sage: h = lambda x: x.trace()
            sage: g = f.map_coefficients(h); g
            X - Y
            sage: g.parent()
            Multivariate Polynomial Ring in X, Y over Finite Field in r of size 3^2
            sage: g = f.map_coefficients(h, new_base_ring=GF(3)); g
            X - Y
            sage: g.parent()
            Multivariate Polynomial Ring in X, Y over Finite Field of size 3"""
    @overload
    def map_coefficients(self, h) -> Any:
        """MPolynomial.map_coefficients(self, f, new_base_ring=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 1371)

        Return the polynomial obtained by applying ``f`` to the nonzero
        coefficients of ``self``.

        If ``f`` is a :class:`sage.categories.map.Map`, then the resulting
        polynomial will be defined over the codomain of ``f``. Otherwise, the
        resulting polynomial will be over the same ring as ``self``. Set
        ``new_base_ring`` to override this behaviour.

        INPUT:

        - ``f`` -- a callable that will be applied to the coefficients of ``self``

        - ``new_base_ring`` -- (optional) if given, the resulting polynomial
          will be defined over this ring

        EXAMPLES::

            sage: k.<a> = GF(9); R.<x,y> = k[];  f = x*a + 2*x^3*y*a + a                # needs sage.rings.finite_rings
            sage: f.map_coefficients(lambda a: a + 1)                                   # needs sage.rings.finite_rings
            (-a + 1)*x^3*y + (a + 1)*x + (a + 1)

        Examples with different base ring::

            sage: # needs sage.rings.finite_rings
            sage: R.<r> = GF(9); S.<s> = GF(81)
            sage: h = Hom(R,S)[0]; h
            Ring morphism:
              From: Finite Field in r of size 3^2
              To:   Finite Field in s of size 3^4
              Defn: r |--> 2*s^3 + 2*s^2 + 1
            sage: T.<X,Y> = R[]
            sage: f = r*X + Y
            sage: g = f.map_coefficients(h); g
            (-s^3 - s^2 + 1)*X + Y
            sage: g.parent()
            Multivariate Polynomial Ring in X, Y over Finite Field in s of size 3^4
            sage: h = lambda x: x.trace()
            sage: g = f.map_coefficients(h); g
            X - Y
            sage: g.parent()
            Multivariate Polynomial Ring in X, Y over Finite Field in r of size 3^2
            sage: g = f.map_coefficients(h, new_base_ring=GF(3)); g
            X - Y
            sage: g.parent()
            Multivariate Polynomial Ring in X, Y over Finite Field of size 3"""
    @overload
    def map_coefficients(self, h) -> Any:
        """MPolynomial.map_coefficients(self, f, new_base_ring=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 1371)

        Return the polynomial obtained by applying ``f`` to the nonzero
        coefficients of ``self``.

        If ``f`` is a :class:`sage.categories.map.Map`, then the resulting
        polynomial will be defined over the codomain of ``f``. Otherwise, the
        resulting polynomial will be over the same ring as ``self``. Set
        ``new_base_ring`` to override this behaviour.

        INPUT:

        - ``f`` -- a callable that will be applied to the coefficients of ``self``

        - ``new_base_ring`` -- (optional) if given, the resulting polynomial
          will be defined over this ring

        EXAMPLES::

            sage: k.<a> = GF(9); R.<x,y> = k[];  f = x*a + 2*x^3*y*a + a                # needs sage.rings.finite_rings
            sage: f.map_coefficients(lambda a: a + 1)                                   # needs sage.rings.finite_rings
            (-a + 1)*x^3*y + (a + 1)*x + (a + 1)

        Examples with different base ring::

            sage: # needs sage.rings.finite_rings
            sage: R.<r> = GF(9); S.<s> = GF(81)
            sage: h = Hom(R,S)[0]; h
            Ring morphism:
              From: Finite Field in r of size 3^2
              To:   Finite Field in s of size 3^4
              Defn: r |--> 2*s^3 + 2*s^2 + 1
            sage: T.<X,Y> = R[]
            sage: f = r*X + Y
            sage: g = f.map_coefficients(h); g
            (-s^3 - s^2 + 1)*X + Y
            sage: g.parent()
            Multivariate Polynomial Ring in X, Y over Finite Field in s of size 3^4
            sage: h = lambda x: x.trace()
            sage: g = f.map_coefficients(h); g
            X - Y
            sage: g.parent()
            Multivariate Polynomial Ring in X, Y over Finite Field in r of size 3^2
            sage: g = f.map_coefficients(h, new_base_ring=GF(3)); g
            X - Y
            sage: g.parent()
            Multivariate Polynomial Ring in X, Y over Finite Field of size 3"""
    @overload
    def map_coefficients(self, h, new_base_ring=...) -> Any:
        """MPolynomial.map_coefficients(self, f, new_base_ring=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 1371)

        Return the polynomial obtained by applying ``f`` to the nonzero
        coefficients of ``self``.

        If ``f`` is a :class:`sage.categories.map.Map`, then the resulting
        polynomial will be defined over the codomain of ``f``. Otherwise, the
        resulting polynomial will be over the same ring as ``self``. Set
        ``new_base_ring`` to override this behaviour.

        INPUT:

        - ``f`` -- a callable that will be applied to the coefficients of ``self``

        - ``new_base_ring`` -- (optional) if given, the resulting polynomial
          will be defined over this ring

        EXAMPLES::

            sage: k.<a> = GF(9); R.<x,y> = k[];  f = x*a + 2*x^3*y*a + a                # needs sage.rings.finite_rings
            sage: f.map_coefficients(lambda a: a + 1)                                   # needs sage.rings.finite_rings
            (-a + 1)*x^3*y + (a + 1)*x + (a + 1)

        Examples with different base ring::

            sage: # needs sage.rings.finite_rings
            sage: R.<r> = GF(9); S.<s> = GF(81)
            sage: h = Hom(R,S)[0]; h
            Ring morphism:
              From: Finite Field in r of size 3^2
              To:   Finite Field in s of size 3^4
              Defn: r |--> 2*s^3 + 2*s^2 + 1
            sage: T.<X,Y> = R[]
            sage: f = r*X + Y
            sage: g = f.map_coefficients(h); g
            (-s^3 - s^2 + 1)*X + Y
            sage: g.parent()
            Multivariate Polynomial Ring in X, Y over Finite Field in s of size 3^4
            sage: h = lambda x: x.trace()
            sage: g = f.map_coefficients(h); g
            X - Y
            sage: g.parent()
            Multivariate Polynomial Ring in X, Y over Finite Field in r of size 3^2
            sage: g = f.map_coefficients(h, new_base_ring=GF(3)); g
            X - Y
            sage: g.parent()
            Multivariate Polynomial Ring in X, Y over Finite Field of size 3"""
    @overload
    def newton_polytope(self) -> Any:
        """MPolynomial.newton_polytope(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 1211)

        Return the Newton polytope of this polynomial.

        EXAMPLES::

            sage: R.<x,y> = QQ[]
            sage: f = 1 + x*y + x^3 + y^3
            sage: P = f.newton_polytope(); P                                            # needs sage.geometry.polyhedron
            A 2-dimensional polyhedron in ZZ^2 defined as the convex hull of 3 vertices
            sage: P.is_simple()                                                         # needs sage.geometry.polyhedron
            True

        TESTS::

            sage: R.<x,y> = QQ[]
            sage: R(0).newton_polytope()                                                # needs sage.geometry.polyhedron
            The empty polyhedron in ZZ^0
            sage: R(1).newton_polytope()                                                # needs sage.geometry.polyhedron
            A 0-dimensional polyhedron in ZZ^2 defined as the convex hull of 1 vertex
            sage: R(x^2+y^2).newton_polytope().integral_points()                        # needs sage.geometry.polyhedron
            ((0, 2), (1, 1), (2, 0))"""
    @overload
    def newton_polytope(self) -> Any:
        """MPolynomial.newton_polytope(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 1211)

        Return the Newton polytope of this polynomial.

        EXAMPLES::

            sage: R.<x,y> = QQ[]
            sage: f = 1 + x*y + x^3 + y^3
            sage: P = f.newton_polytope(); P                                            # needs sage.geometry.polyhedron
            A 2-dimensional polyhedron in ZZ^2 defined as the convex hull of 3 vertices
            sage: P.is_simple()                                                         # needs sage.geometry.polyhedron
            True

        TESTS::

            sage: R.<x,y> = QQ[]
            sage: R(0).newton_polytope()                                                # needs sage.geometry.polyhedron
            The empty polyhedron in ZZ^0
            sage: R(1).newton_polytope()                                                # needs sage.geometry.polyhedron
            A 0-dimensional polyhedron in ZZ^2 defined as the convex hull of 1 vertex
            sage: R(x^2+y^2).newton_polytope().integral_points()                        # needs sage.geometry.polyhedron
            ((0, 2), (1, 1), (2, 0))"""
    @overload
    def newton_polytope(self) -> Any:
        """MPolynomial.newton_polytope(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 1211)

        Return the Newton polytope of this polynomial.

        EXAMPLES::

            sage: R.<x,y> = QQ[]
            sage: f = 1 + x*y + x^3 + y^3
            sage: P = f.newton_polytope(); P                                            # needs sage.geometry.polyhedron
            A 2-dimensional polyhedron in ZZ^2 defined as the convex hull of 3 vertices
            sage: P.is_simple()                                                         # needs sage.geometry.polyhedron
            True

        TESTS::

            sage: R.<x,y> = QQ[]
            sage: R(0).newton_polytope()                                                # needs sage.geometry.polyhedron
            The empty polyhedron in ZZ^0
            sage: R(1).newton_polytope()                                                # needs sage.geometry.polyhedron
            A 0-dimensional polyhedron in ZZ^2 defined as the convex hull of 1 vertex
            sage: R(x^2+y^2).newton_polytope().integral_points()                        # needs sage.geometry.polyhedron
            ((0, 2), (1, 1), (2, 0))"""
    @overload
    def newton_polytope(self) -> Any:
        """MPolynomial.newton_polytope(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 1211)

        Return the Newton polytope of this polynomial.

        EXAMPLES::

            sage: R.<x,y> = QQ[]
            sage: f = 1 + x*y + x^3 + y^3
            sage: P = f.newton_polytope(); P                                            # needs sage.geometry.polyhedron
            A 2-dimensional polyhedron in ZZ^2 defined as the convex hull of 3 vertices
            sage: P.is_simple()                                                         # needs sage.geometry.polyhedron
            True

        TESTS::

            sage: R.<x,y> = QQ[]
            sage: R(0).newton_polytope()                                                # needs sage.geometry.polyhedron
            The empty polyhedron in ZZ^0
            sage: R(1).newton_polytope()                                                # needs sage.geometry.polyhedron
            A 0-dimensional polyhedron in ZZ^2 defined as the convex hull of 1 vertex
            sage: R(x^2+y^2).newton_polytope().integral_points()                        # needs sage.geometry.polyhedron
            ((0, 2), (1, 1), (2, 0))"""
    @overload
    def newton_polytope(self) -> Any:
        """MPolynomial.newton_polytope(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 1211)

        Return the Newton polytope of this polynomial.

        EXAMPLES::

            sage: R.<x,y> = QQ[]
            sage: f = 1 + x*y + x^3 + y^3
            sage: P = f.newton_polytope(); P                                            # needs sage.geometry.polyhedron
            A 2-dimensional polyhedron in ZZ^2 defined as the convex hull of 3 vertices
            sage: P.is_simple()                                                         # needs sage.geometry.polyhedron
            True

        TESTS::

            sage: R.<x,y> = QQ[]
            sage: R(0).newton_polytope()                                                # needs sage.geometry.polyhedron
            The empty polyhedron in ZZ^0
            sage: R(1).newton_polytope()                                                # needs sage.geometry.polyhedron
            A 0-dimensional polyhedron in ZZ^2 defined as the convex hull of 1 vertex
            sage: R(x^2+y^2).newton_polytope().integral_points()                        # needs sage.geometry.polyhedron
            ((0, 2), (1, 1), (2, 0))"""
    def nth_root(self, n) -> Any:
        """MPolynomial.nth_root(self, n)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 2236)

        Return a `n`-th root of this element.

        If there is no such root, a :exc:`ValueError` is raised.

        EXAMPLES::

            sage: R.<x,y,z> = QQ[]
            sage: a = 32 * (x*y + 1)^5 * (x+y+z)^5
            sage: a.nth_root(5)
            2*x^2*y + 2*x*y^2 + 2*x*y*z + 2*x + 2*y + 2*z
            sage: b = x + 2*y + 3*z
            sage: b.nth_root(42)
            Traceback (most recent call last):
            ...
            ValueError: not a 42nd power

            sage: R.<x,y> = QQ[]
            sage: S.<z,t> = R[]
            sage: T.<u,v> = S[]
            sage: p = (1 + x*u + y + v) * (1 + z*t)
            sage: (p**3).nth_root(3)
            (x*z*t + x)*u + (z*t + 1)*v + (y + 1)*z*t + y + 1
            sage: (p**3).nth_root(3).parent() is p.parent()
            True
            sage: ((1+x+z+t)**2).nth_root(3)
            Traceback (most recent call last):
            ...
            ValueError: not a 3rd power"""
    @overload
    def numerator(self) -> Any:
        """MPolynomial.numerator(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 1910)

        Return a numerator of ``self``, computed as ``self * self.denominator()``.

        Note that some subclasses may implement its own numerator
        function.

        .. warning::

           This is not the numerator of the rational function
           defined by ``self``, which would always be ``self`` since ``self`` is a
           polynomial.

        EXAMPLES:

        First we compute the numerator of a polynomial with
        integer coefficients, which is of course ``self``.

        ::

            sage: R.<x, y> = ZZ[]
            sage: f = x^3 + 17*x + y + 1
            sage: f.numerator()
            x^3 + 17*x + y + 1
            sage: f == f.numerator()
            True

        Next we compute the numerator of a polynomial over a number field.

        ::

            sage: # needs sage.rings.number_field sage.symbolic
            sage: R.<x,y> = NumberField(symbolic_expression(x^2+3), 'a')['x,y']
            sage: f = (1/17)*y^19 - (2/3)*x + 1/3; f
            1/17*y^19 - 2/3*x + 1/3
            sage: f.numerator()
            3*y^19 - 34*x + 17
            sage: f == f.numerator()
            False

        We try to compute the numerator of a polynomial with coefficients in
        the finite field of 3 elements.

        ::

            sage: K.<x,y,z> = GF(3)['x, y, z']
            sage: f = 2*x*z + 2*z^2 + 2*y + 1; f
            -x*z - z^2 - y + 1
            sage: f.numerator()
            -x*z - z^2 - y + 1

        We check that the computation the numerator and denominator
        are valid.

        ::

            sage: # needs sage.rings.number_field sage.symbolic
            sage: K = NumberField(symbolic_expression('x^3+2'), 'a')['x']['s,t']
            sage: f = K.random_element()
            sage: f.numerator() / f.denominator() == f
            True
            sage: R = RR['x,y,z']
            sage: f = R.random_element()
            sage: f.numerator() / f.denominator() == f
            True"""
    @overload
    def numerator(self) -> Any:
        """MPolynomial.numerator(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 1910)

        Return a numerator of ``self``, computed as ``self * self.denominator()``.

        Note that some subclasses may implement its own numerator
        function.

        .. warning::

           This is not the numerator of the rational function
           defined by ``self``, which would always be ``self`` since ``self`` is a
           polynomial.

        EXAMPLES:

        First we compute the numerator of a polynomial with
        integer coefficients, which is of course ``self``.

        ::

            sage: R.<x, y> = ZZ[]
            sage: f = x^3 + 17*x + y + 1
            sage: f.numerator()
            x^3 + 17*x + y + 1
            sage: f == f.numerator()
            True

        Next we compute the numerator of a polynomial over a number field.

        ::

            sage: # needs sage.rings.number_field sage.symbolic
            sage: R.<x,y> = NumberField(symbolic_expression(x^2+3), 'a')['x,y']
            sage: f = (1/17)*y^19 - (2/3)*x + 1/3; f
            1/17*y^19 - 2/3*x + 1/3
            sage: f.numerator()
            3*y^19 - 34*x + 17
            sage: f == f.numerator()
            False

        We try to compute the numerator of a polynomial with coefficients in
        the finite field of 3 elements.

        ::

            sage: K.<x,y,z> = GF(3)['x, y, z']
            sage: f = 2*x*z + 2*z^2 + 2*y + 1; f
            -x*z - z^2 - y + 1
            sage: f.numerator()
            -x*z - z^2 - y + 1

        We check that the computation the numerator and denominator
        are valid.

        ::

            sage: # needs sage.rings.number_field sage.symbolic
            sage: K = NumberField(symbolic_expression('x^3+2'), 'a')['x']['s,t']
            sage: f = K.random_element()
            sage: f.numerator() / f.denominator() == f
            True
            sage: R = RR['x,y,z']
            sage: f = R.random_element()
            sage: f.numerator() / f.denominator() == f
            True"""
    @overload
    def numerator(self) -> Any:
        """MPolynomial.numerator(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 1910)

        Return a numerator of ``self``, computed as ``self * self.denominator()``.

        Note that some subclasses may implement its own numerator
        function.

        .. warning::

           This is not the numerator of the rational function
           defined by ``self``, which would always be ``self`` since ``self`` is a
           polynomial.

        EXAMPLES:

        First we compute the numerator of a polynomial with
        integer coefficients, which is of course ``self``.

        ::

            sage: R.<x, y> = ZZ[]
            sage: f = x^3 + 17*x + y + 1
            sage: f.numerator()
            x^3 + 17*x + y + 1
            sage: f == f.numerator()
            True

        Next we compute the numerator of a polynomial over a number field.

        ::

            sage: # needs sage.rings.number_field sage.symbolic
            sage: R.<x,y> = NumberField(symbolic_expression(x^2+3), 'a')['x,y']
            sage: f = (1/17)*y^19 - (2/3)*x + 1/3; f
            1/17*y^19 - 2/3*x + 1/3
            sage: f.numerator()
            3*y^19 - 34*x + 17
            sage: f == f.numerator()
            False

        We try to compute the numerator of a polynomial with coefficients in
        the finite field of 3 elements.

        ::

            sage: K.<x,y,z> = GF(3)['x, y, z']
            sage: f = 2*x*z + 2*z^2 + 2*y + 1; f
            -x*z - z^2 - y + 1
            sage: f.numerator()
            -x*z - z^2 - y + 1

        We check that the computation the numerator and denominator
        are valid.

        ::

            sage: # needs sage.rings.number_field sage.symbolic
            sage: K = NumberField(symbolic_expression('x^3+2'), 'a')['x']['s,t']
            sage: f = K.random_element()
            sage: f.numerator() / f.denominator() == f
            True
            sage: R = RR['x,y,z']
            sage: f = R.random_element()
            sage: f.numerator() / f.denominator() == f
            True"""
    @overload
    def numerator(self) -> Any:
        """MPolynomial.numerator(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 1910)

        Return a numerator of ``self``, computed as ``self * self.denominator()``.

        Note that some subclasses may implement its own numerator
        function.

        .. warning::

           This is not the numerator of the rational function
           defined by ``self``, which would always be ``self`` since ``self`` is a
           polynomial.

        EXAMPLES:

        First we compute the numerator of a polynomial with
        integer coefficients, which is of course ``self``.

        ::

            sage: R.<x, y> = ZZ[]
            sage: f = x^3 + 17*x + y + 1
            sage: f.numerator()
            x^3 + 17*x + y + 1
            sage: f == f.numerator()
            True

        Next we compute the numerator of a polynomial over a number field.

        ::

            sage: # needs sage.rings.number_field sage.symbolic
            sage: R.<x,y> = NumberField(symbolic_expression(x^2+3), 'a')['x,y']
            sage: f = (1/17)*y^19 - (2/3)*x + 1/3; f
            1/17*y^19 - 2/3*x + 1/3
            sage: f.numerator()
            3*y^19 - 34*x + 17
            sage: f == f.numerator()
            False

        We try to compute the numerator of a polynomial with coefficients in
        the finite field of 3 elements.

        ::

            sage: K.<x,y,z> = GF(3)['x, y, z']
            sage: f = 2*x*z + 2*z^2 + 2*y + 1; f
            -x*z - z^2 - y + 1
            sage: f.numerator()
            -x*z - z^2 - y + 1

        We check that the computation the numerator and denominator
        are valid.

        ::

            sage: # needs sage.rings.number_field sage.symbolic
            sage: K = NumberField(symbolic_expression('x^3+2'), 'a')['x']['s,t']
            sage: f = K.random_element()
            sage: f.numerator() / f.denominator() == f
            True
            sage: R = RR['x,y,z']
            sage: f = R.random_element()
            sage: f.numerator() / f.denominator() == f
            True"""
    @overload
    def numerator(self) -> Any:
        """MPolynomial.numerator(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 1910)

        Return a numerator of ``self``, computed as ``self * self.denominator()``.

        Note that some subclasses may implement its own numerator
        function.

        .. warning::

           This is not the numerator of the rational function
           defined by ``self``, which would always be ``self`` since ``self`` is a
           polynomial.

        EXAMPLES:

        First we compute the numerator of a polynomial with
        integer coefficients, which is of course ``self``.

        ::

            sage: R.<x, y> = ZZ[]
            sage: f = x^3 + 17*x + y + 1
            sage: f.numerator()
            x^3 + 17*x + y + 1
            sage: f == f.numerator()
            True

        Next we compute the numerator of a polynomial over a number field.

        ::

            sage: # needs sage.rings.number_field sage.symbolic
            sage: R.<x,y> = NumberField(symbolic_expression(x^2+3), 'a')['x,y']
            sage: f = (1/17)*y^19 - (2/3)*x + 1/3; f
            1/17*y^19 - 2/3*x + 1/3
            sage: f.numerator()
            3*y^19 - 34*x + 17
            sage: f == f.numerator()
            False

        We try to compute the numerator of a polynomial with coefficients in
        the finite field of 3 elements.

        ::

            sage: K.<x,y,z> = GF(3)['x, y, z']
            sage: f = 2*x*z + 2*z^2 + 2*y + 1; f
            -x*z - z^2 - y + 1
            sage: f.numerator()
            -x*z - z^2 - y + 1

        We check that the computation the numerator and denominator
        are valid.

        ::

            sage: # needs sage.rings.number_field sage.symbolic
            sage: K = NumberField(symbolic_expression('x^3+2'), 'a')['x']['s,t']
            sage: f = K.random_element()
            sage: f.numerator() / f.denominator() == f
            True
            sage: R = RR['x,y,z']
            sage: f = R.random_element()
            sage: f.numerator() / f.denominator() == f
            True"""
    @overload
    def numerator(self) -> Any:
        """MPolynomial.numerator(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 1910)

        Return a numerator of ``self``, computed as ``self * self.denominator()``.

        Note that some subclasses may implement its own numerator
        function.

        .. warning::

           This is not the numerator of the rational function
           defined by ``self``, which would always be ``self`` since ``self`` is a
           polynomial.

        EXAMPLES:

        First we compute the numerator of a polynomial with
        integer coefficients, which is of course ``self``.

        ::

            sage: R.<x, y> = ZZ[]
            sage: f = x^3 + 17*x + y + 1
            sage: f.numerator()
            x^3 + 17*x + y + 1
            sage: f == f.numerator()
            True

        Next we compute the numerator of a polynomial over a number field.

        ::

            sage: # needs sage.rings.number_field sage.symbolic
            sage: R.<x,y> = NumberField(symbolic_expression(x^2+3), 'a')['x,y']
            sage: f = (1/17)*y^19 - (2/3)*x + 1/3; f
            1/17*y^19 - 2/3*x + 1/3
            sage: f.numerator()
            3*y^19 - 34*x + 17
            sage: f == f.numerator()
            False

        We try to compute the numerator of a polynomial with coefficients in
        the finite field of 3 elements.

        ::

            sage: K.<x,y,z> = GF(3)['x, y, z']
            sage: f = 2*x*z + 2*z^2 + 2*y + 1; f
            -x*z - z^2 - y + 1
            sage: f.numerator()
            -x*z - z^2 - y + 1

        We check that the computation the numerator and denominator
        are valid.

        ::

            sage: # needs sage.rings.number_field sage.symbolic
            sage: K = NumberField(symbolic_expression('x^3+2'), 'a')['x']['s,t']
            sage: f = K.random_element()
            sage: f.numerator() / f.denominator() == f
            True
            sage: R = RR['x,y,z']
            sage: f = R.random_element()
            sage: f.numerator() / f.denominator() == f
            True"""
    @overload
    def numerator(self) -> Any:
        """MPolynomial.numerator(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 1910)

        Return a numerator of ``self``, computed as ``self * self.denominator()``.

        Note that some subclasses may implement its own numerator
        function.

        .. warning::

           This is not the numerator of the rational function
           defined by ``self``, which would always be ``self`` since ``self`` is a
           polynomial.

        EXAMPLES:

        First we compute the numerator of a polynomial with
        integer coefficients, which is of course ``self``.

        ::

            sage: R.<x, y> = ZZ[]
            sage: f = x^3 + 17*x + y + 1
            sage: f.numerator()
            x^3 + 17*x + y + 1
            sage: f == f.numerator()
            True

        Next we compute the numerator of a polynomial over a number field.

        ::

            sage: # needs sage.rings.number_field sage.symbolic
            sage: R.<x,y> = NumberField(symbolic_expression(x^2+3), 'a')['x,y']
            sage: f = (1/17)*y^19 - (2/3)*x + 1/3; f
            1/17*y^19 - 2/3*x + 1/3
            sage: f.numerator()
            3*y^19 - 34*x + 17
            sage: f == f.numerator()
            False

        We try to compute the numerator of a polynomial with coefficients in
        the finite field of 3 elements.

        ::

            sage: K.<x,y,z> = GF(3)['x, y, z']
            sage: f = 2*x*z + 2*z^2 + 2*y + 1; f
            -x*z - z^2 - y + 1
            sage: f.numerator()
            -x*z - z^2 - y + 1

        We check that the computation the numerator and denominator
        are valid.

        ::

            sage: # needs sage.rings.number_field sage.symbolic
            sage: K = NumberField(symbolic_expression('x^3+2'), 'a')['x']['s,t']
            sage: f = K.random_element()
            sage: f.numerator() / f.denominator() == f
            True
            sage: R = RR['x,y,z']
            sage: f = R.random_element()
            sage: f.numerator() / f.denominator() == f
            True"""
    @overload
    def numerator(self) -> Any:
        """MPolynomial.numerator(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 1910)

        Return a numerator of ``self``, computed as ``self * self.denominator()``.

        Note that some subclasses may implement its own numerator
        function.

        .. warning::

           This is not the numerator of the rational function
           defined by ``self``, which would always be ``self`` since ``self`` is a
           polynomial.

        EXAMPLES:

        First we compute the numerator of a polynomial with
        integer coefficients, which is of course ``self``.

        ::

            sage: R.<x, y> = ZZ[]
            sage: f = x^3 + 17*x + y + 1
            sage: f.numerator()
            x^3 + 17*x + y + 1
            sage: f == f.numerator()
            True

        Next we compute the numerator of a polynomial over a number field.

        ::

            sage: # needs sage.rings.number_field sage.symbolic
            sage: R.<x,y> = NumberField(symbolic_expression(x^2+3), 'a')['x,y']
            sage: f = (1/17)*y^19 - (2/3)*x + 1/3; f
            1/17*y^19 - 2/3*x + 1/3
            sage: f.numerator()
            3*y^19 - 34*x + 17
            sage: f == f.numerator()
            False

        We try to compute the numerator of a polynomial with coefficients in
        the finite field of 3 elements.

        ::

            sage: K.<x,y,z> = GF(3)['x, y, z']
            sage: f = 2*x*z + 2*z^2 + 2*y + 1; f
            -x*z - z^2 - y + 1
            sage: f.numerator()
            -x*z - z^2 - y + 1

        We check that the computation the numerator and denominator
        are valid.

        ::

            sage: # needs sage.rings.number_field sage.symbolic
            sage: K = NumberField(symbolic_expression('x^3+2'), 'a')['x']['s,t']
            sage: f = K.random_element()
            sage: f.numerator() / f.denominator() == f
            True
            sage: R = RR['x,y,z']
            sage: f = R.random_element()
            sage: f.numerator() / f.denominator() == f
            True"""
    @overload
    def polynomial(self, var) -> Any:
        """MPolynomial.polynomial(self, var)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 417)

        Let ``var`` be one of the variables of the parent of ``self``.  This
        returns ``self`` viewed as a univariate polynomial in ``var`` over the
        polynomial ring generated by all the other variables of the parent.

        EXAMPLES::

            sage: R.<x,w,z> = QQ[]
            sage: f = x^3 + 3*w*x + w^5 + (17*w^3)*x + z^5
            sage: f.polynomial(x)
            x^3 + (17*w^3 + 3*w)*x + w^5 + z^5
            sage: parent(f.polynomial(x))
            Univariate Polynomial Ring in x
             over Multivariate Polynomial Ring in w, z over Rational Field

            sage: f.polynomial(w)
            w^5 + 17*x*w^3 + 3*x*w + z^5 + x^3
            sage: f.polynomial(z)
            z^5 + w^5 + 17*x*w^3 + x^3 + 3*x*w
            sage: R.<x,w,z,k> = ZZ[]
            sage: f = x^3 + 3*w*x + w^5 + (17*w^3)*x + z^5 +x*w*z*k + 5
            sage: f.polynomial(x)
            x^3 + (17*w^3 + w*z*k + 3*w)*x + w^5 + z^5 + 5
            sage: f.polynomial(w)
            w^5 + 17*x*w^3 + (x*z*k + 3*x)*w + z^5 + x^3 + 5
            sage: f.polynomial(z)
            z^5 + x*w*k*z + w^5 + 17*x*w^3 + x^3 + 3*x*w + 5
            sage: f.polynomial(k)
            x*w*z*k + w^5 + z^5 + 17*x*w^3 + x^3 + 3*x*w + 5
            sage: R.<x,y> = GF(5)[]
            sage: f = x^2 + x + y
            sage: f.polynomial(x)
            x^2 + x + y
            sage: f.polynomial(y)
            y + x^2 + x"""
    @overload
    def polynomial(self, x) -> Any:
        """MPolynomial.polynomial(self, var)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 417)

        Let ``var`` be one of the variables of the parent of ``self``.  This
        returns ``self`` viewed as a univariate polynomial in ``var`` over the
        polynomial ring generated by all the other variables of the parent.

        EXAMPLES::

            sage: R.<x,w,z> = QQ[]
            sage: f = x^3 + 3*w*x + w^5 + (17*w^3)*x + z^5
            sage: f.polynomial(x)
            x^3 + (17*w^3 + 3*w)*x + w^5 + z^5
            sage: parent(f.polynomial(x))
            Univariate Polynomial Ring in x
             over Multivariate Polynomial Ring in w, z over Rational Field

            sage: f.polynomial(w)
            w^5 + 17*x*w^3 + 3*x*w + z^5 + x^3
            sage: f.polynomial(z)
            z^5 + w^5 + 17*x*w^3 + x^3 + 3*x*w
            sage: R.<x,w,z,k> = ZZ[]
            sage: f = x^3 + 3*w*x + w^5 + (17*w^3)*x + z^5 +x*w*z*k + 5
            sage: f.polynomial(x)
            x^3 + (17*w^3 + w*z*k + 3*w)*x + w^5 + z^5 + 5
            sage: f.polynomial(w)
            w^5 + 17*x*w^3 + (x*z*k + 3*x)*w + z^5 + x^3 + 5
            sage: f.polynomial(z)
            z^5 + x*w*k*z + w^5 + 17*x*w^3 + x^3 + 3*x*w + 5
            sage: f.polynomial(k)
            x*w*z*k + w^5 + z^5 + 17*x*w^3 + x^3 + 3*x*w + 5
            sage: R.<x,y> = GF(5)[]
            sage: f = x^2 + x + y
            sage: f.polynomial(x)
            x^2 + x + y
            sage: f.polynomial(y)
            y + x^2 + x"""
    @overload
    def polynomial(self, x) -> Any:
        """MPolynomial.polynomial(self, var)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 417)

        Let ``var`` be one of the variables of the parent of ``self``.  This
        returns ``self`` viewed as a univariate polynomial in ``var`` over the
        polynomial ring generated by all the other variables of the parent.

        EXAMPLES::

            sage: R.<x,w,z> = QQ[]
            sage: f = x^3 + 3*w*x + w^5 + (17*w^3)*x + z^5
            sage: f.polynomial(x)
            x^3 + (17*w^3 + 3*w)*x + w^5 + z^5
            sage: parent(f.polynomial(x))
            Univariate Polynomial Ring in x
             over Multivariate Polynomial Ring in w, z over Rational Field

            sage: f.polynomial(w)
            w^5 + 17*x*w^3 + 3*x*w + z^5 + x^3
            sage: f.polynomial(z)
            z^5 + w^5 + 17*x*w^3 + x^3 + 3*x*w
            sage: R.<x,w,z,k> = ZZ[]
            sage: f = x^3 + 3*w*x + w^5 + (17*w^3)*x + z^5 +x*w*z*k + 5
            sage: f.polynomial(x)
            x^3 + (17*w^3 + w*z*k + 3*w)*x + w^5 + z^5 + 5
            sage: f.polynomial(w)
            w^5 + 17*x*w^3 + (x*z*k + 3*x)*w + z^5 + x^3 + 5
            sage: f.polynomial(z)
            z^5 + x*w*k*z + w^5 + 17*x*w^3 + x^3 + 3*x*w + 5
            sage: f.polynomial(k)
            x*w*z*k + w^5 + z^5 + 17*x*w^3 + x^3 + 3*x*w + 5
            sage: R.<x,y> = GF(5)[]
            sage: f = x^2 + x + y
            sage: f.polynomial(x)
            x^2 + x + y
            sage: f.polynomial(y)
            y + x^2 + x"""
    @overload
    def polynomial(self, w) -> Any:
        """MPolynomial.polynomial(self, var)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 417)

        Let ``var`` be one of the variables of the parent of ``self``.  This
        returns ``self`` viewed as a univariate polynomial in ``var`` over the
        polynomial ring generated by all the other variables of the parent.

        EXAMPLES::

            sage: R.<x,w,z> = QQ[]
            sage: f = x^3 + 3*w*x + w^5 + (17*w^3)*x + z^5
            sage: f.polynomial(x)
            x^3 + (17*w^3 + 3*w)*x + w^5 + z^5
            sage: parent(f.polynomial(x))
            Univariate Polynomial Ring in x
             over Multivariate Polynomial Ring in w, z over Rational Field

            sage: f.polynomial(w)
            w^5 + 17*x*w^3 + 3*x*w + z^5 + x^3
            sage: f.polynomial(z)
            z^5 + w^5 + 17*x*w^3 + x^3 + 3*x*w
            sage: R.<x,w,z,k> = ZZ[]
            sage: f = x^3 + 3*w*x + w^5 + (17*w^3)*x + z^5 +x*w*z*k + 5
            sage: f.polynomial(x)
            x^3 + (17*w^3 + w*z*k + 3*w)*x + w^5 + z^5 + 5
            sage: f.polynomial(w)
            w^5 + 17*x*w^3 + (x*z*k + 3*x)*w + z^5 + x^3 + 5
            sage: f.polynomial(z)
            z^5 + x*w*k*z + w^5 + 17*x*w^3 + x^3 + 3*x*w + 5
            sage: f.polynomial(k)
            x*w*z*k + w^5 + z^5 + 17*x*w^3 + x^3 + 3*x*w + 5
            sage: R.<x,y> = GF(5)[]
            sage: f = x^2 + x + y
            sage: f.polynomial(x)
            x^2 + x + y
            sage: f.polynomial(y)
            y + x^2 + x"""
    @overload
    def polynomial(self, z) -> Any:
        """MPolynomial.polynomial(self, var)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 417)

        Let ``var`` be one of the variables of the parent of ``self``.  This
        returns ``self`` viewed as a univariate polynomial in ``var`` over the
        polynomial ring generated by all the other variables of the parent.

        EXAMPLES::

            sage: R.<x,w,z> = QQ[]
            sage: f = x^3 + 3*w*x + w^5 + (17*w^3)*x + z^5
            sage: f.polynomial(x)
            x^3 + (17*w^3 + 3*w)*x + w^5 + z^5
            sage: parent(f.polynomial(x))
            Univariate Polynomial Ring in x
             over Multivariate Polynomial Ring in w, z over Rational Field

            sage: f.polynomial(w)
            w^5 + 17*x*w^3 + 3*x*w + z^5 + x^3
            sage: f.polynomial(z)
            z^5 + w^5 + 17*x*w^3 + x^3 + 3*x*w
            sage: R.<x,w,z,k> = ZZ[]
            sage: f = x^3 + 3*w*x + w^5 + (17*w^3)*x + z^5 +x*w*z*k + 5
            sage: f.polynomial(x)
            x^3 + (17*w^3 + w*z*k + 3*w)*x + w^5 + z^5 + 5
            sage: f.polynomial(w)
            w^5 + 17*x*w^3 + (x*z*k + 3*x)*w + z^5 + x^3 + 5
            sage: f.polynomial(z)
            z^5 + x*w*k*z + w^5 + 17*x*w^3 + x^3 + 3*x*w + 5
            sage: f.polynomial(k)
            x*w*z*k + w^5 + z^5 + 17*x*w^3 + x^3 + 3*x*w + 5
            sage: R.<x,y> = GF(5)[]
            sage: f = x^2 + x + y
            sage: f.polynomial(x)
            x^2 + x + y
            sage: f.polynomial(y)
            y + x^2 + x"""
    @overload
    def polynomial(self, x) -> Any:
        """MPolynomial.polynomial(self, var)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 417)

        Let ``var`` be one of the variables of the parent of ``self``.  This
        returns ``self`` viewed as a univariate polynomial in ``var`` over the
        polynomial ring generated by all the other variables of the parent.

        EXAMPLES::

            sage: R.<x,w,z> = QQ[]
            sage: f = x^3 + 3*w*x + w^5 + (17*w^3)*x + z^5
            sage: f.polynomial(x)
            x^3 + (17*w^3 + 3*w)*x + w^5 + z^5
            sage: parent(f.polynomial(x))
            Univariate Polynomial Ring in x
             over Multivariate Polynomial Ring in w, z over Rational Field

            sage: f.polynomial(w)
            w^5 + 17*x*w^3 + 3*x*w + z^5 + x^3
            sage: f.polynomial(z)
            z^5 + w^5 + 17*x*w^3 + x^3 + 3*x*w
            sage: R.<x,w,z,k> = ZZ[]
            sage: f = x^3 + 3*w*x + w^5 + (17*w^3)*x + z^5 +x*w*z*k + 5
            sage: f.polynomial(x)
            x^3 + (17*w^3 + w*z*k + 3*w)*x + w^5 + z^5 + 5
            sage: f.polynomial(w)
            w^5 + 17*x*w^3 + (x*z*k + 3*x)*w + z^5 + x^3 + 5
            sage: f.polynomial(z)
            z^5 + x*w*k*z + w^5 + 17*x*w^3 + x^3 + 3*x*w + 5
            sage: f.polynomial(k)
            x*w*z*k + w^5 + z^5 + 17*x*w^3 + x^3 + 3*x*w + 5
            sage: R.<x,y> = GF(5)[]
            sage: f = x^2 + x + y
            sage: f.polynomial(x)
            x^2 + x + y
            sage: f.polynomial(y)
            y + x^2 + x"""
    @overload
    def polynomial(self, w) -> Any:
        """MPolynomial.polynomial(self, var)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 417)

        Let ``var`` be one of the variables of the parent of ``self``.  This
        returns ``self`` viewed as a univariate polynomial in ``var`` over the
        polynomial ring generated by all the other variables of the parent.

        EXAMPLES::

            sage: R.<x,w,z> = QQ[]
            sage: f = x^3 + 3*w*x + w^5 + (17*w^3)*x + z^5
            sage: f.polynomial(x)
            x^3 + (17*w^3 + 3*w)*x + w^5 + z^5
            sage: parent(f.polynomial(x))
            Univariate Polynomial Ring in x
             over Multivariate Polynomial Ring in w, z over Rational Field

            sage: f.polynomial(w)
            w^5 + 17*x*w^3 + 3*x*w + z^5 + x^3
            sage: f.polynomial(z)
            z^5 + w^5 + 17*x*w^3 + x^3 + 3*x*w
            sage: R.<x,w,z,k> = ZZ[]
            sage: f = x^3 + 3*w*x + w^5 + (17*w^3)*x + z^5 +x*w*z*k + 5
            sage: f.polynomial(x)
            x^3 + (17*w^3 + w*z*k + 3*w)*x + w^5 + z^5 + 5
            sage: f.polynomial(w)
            w^5 + 17*x*w^3 + (x*z*k + 3*x)*w + z^5 + x^3 + 5
            sage: f.polynomial(z)
            z^5 + x*w*k*z + w^5 + 17*x*w^3 + x^3 + 3*x*w + 5
            sage: f.polynomial(k)
            x*w*z*k + w^5 + z^5 + 17*x*w^3 + x^3 + 3*x*w + 5
            sage: R.<x,y> = GF(5)[]
            sage: f = x^2 + x + y
            sage: f.polynomial(x)
            x^2 + x + y
            sage: f.polynomial(y)
            y + x^2 + x"""
    @overload
    def polynomial(self, z) -> Any:
        """MPolynomial.polynomial(self, var)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 417)

        Let ``var`` be one of the variables of the parent of ``self``.  This
        returns ``self`` viewed as a univariate polynomial in ``var`` over the
        polynomial ring generated by all the other variables of the parent.

        EXAMPLES::

            sage: R.<x,w,z> = QQ[]
            sage: f = x^3 + 3*w*x + w^5 + (17*w^3)*x + z^5
            sage: f.polynomial(x)
            x^3 + (17*w^3 + 3*w)*x + w^5 + z^5
            sage: parent(f.polynomial(x))
            Univariate Polynomial Ring in x
             over Multivariate Polynomial Ring in w, z over Rational Field

            sage: f.polynomial(w)
            w^5 + 17*x*w^3 + 3*x*w + z^5 + x^3
            sage: f.polynomial(z)
            z^5 + w^5 + 17*x*w^3 + x^3 + 3*x*w
            sage: R.<x,w,z,k> = ZZ[]
            sage: f = x^3 + 3*w*x + w^5 + (17*w^3)*x + z^5 +x*w*z*k + 5
            sage: f.polynomial(x)
            x^3 + (17*w^3 + w*z*k + 3*w)*x + w^5 + z^5 + 5
            sage: f.polynomial(w)
            w^5 + 17*x*w^3 + (x*z*k + 3*x)*w + z^5 + x^3 + 5
            sage: f.polynomial(z)
            z^5 + x*w*k*z + w^5 + 17*x*w^3 + x^3 + 3*x*w + 5
            sage: f.polynomial(k)
            x*w*z*k + w^5 + z^5 + 17*x*w^3 + x^3 + 3*x*w + 5
            sage: R.<x,y> = GF(5)[]
            sage: f = x^2 + x + y
            sage: f.polynomial(x)
            x^2 + x + y
            sage: f.polynomial(y)
            y + x^2 + x"""
    @overload
    def polynomial(self, k) -> Any:
        """MPolynomial.polynomial(self, var)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 417)

        Let ``var`` be one of the variables of the parent of ``self``.  This
        returns ``self`` viewed as a univariate polynomial in ``var`` over the
        polynomial ring generated by all the other variables of the parent.

        EXAMPLES::

            sage: R.<x,w,z> = QQ[]
            sage: f = x^3 + 3*w*x + w^5 + (17*w^3)*x + z^5
            sage: f.polynomial(x)
            x^3 + (17*w^3 + 3*w)*x + w^5 + z^5
            sage: parent(f.polynomial(x))
            Univariate Polynomial Ring in x
             over Multivariate Polynomial Ring in w, z over Rational Field

            sage: f.polynomial(w)
            w^5 + 17*x*w^3 + 3*x*w + z^5 + x^3
            sage: f.polynomial(z)
            z^5 + w^5 + 17*x*w^3 + x^3 + 3*x*w
            sage: R.<x,w,z,k> = ZZ[]
            sage: f = x^3 + 3*w*x + w^5 + (17*w^3)*x + z^5 +x*w*z*k + 5
            sage: f.polynomial(x)
            x^3 + (17*w^3 + w*z*k + 3*w)*x + w^5 + z^5 + 5
            sage: f.polynomial(w)
            w^5 + 17*x*w^3 + (x*z*k + 3*x)*w + z^5 + x^3 + 5
            sage: f.polynomial(z)
            z^5 + x*w*k*z + w^5 + 17*x*w^3 + x^3 + 3*x*w + 5
            sage: f.polynomial(k)
            x*w*z*k + w^5 + z^5 + 17*x*w^3 + x^3 + 3*x*w + 5
            sage: R.<x,y> = GF(5)[]
            sage: f = x^2 + x + y
            sage: f.polynomial(x)
            x^2 + x + y
            sage: f.polynomial(y)
            y + x^2 + x"""
    @overload
    def polynomial(self, x) -> Any:
        """MPolynomial.polynomial(self, var)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 417)

        Let ``var`` be one of the variables of the parent of ``self``.  This
        returns ``self`` viewed as a univariate polynomial in ``var`` over the
        polynomial ring generated by all the other variables of the parent.

        EXAMPLES::

            sage: R.<x,w,z> = QQ[]
            sage: f = x^3 + 3*w*x + w^5 + (17*w^3)*x + z^5
            sage: f.polynomial(x)
            x^3 + (17*w^3 + 3*w)*x + w^5 + z^5
            sage: parent(f.polynomial(x))
            Univariate Polynomial Ring in x
             over Multivariate Polynomial Ring in w, z over Rational Field

            sage: f.polynomial(w)
            w^5 + 17*x*w^3 + 3*x*w + z^5 + x^3
            sage: f.polynomial(z)
            z^5 + w^5 + 17*x*w^3 + x^3 + 3*x*w
            sage: R.<x,w,z,k> = ZZ[]
            sage: f = x^3 + 3*w*x + w^5 + (17*w^3)*x + z^5 +x*w*z*k + 5
            sage: f.polynomial(x)
            x^3 + (17*w^3 + w*z*k + 3*w)*x + w^5 + z^5 + 5
            sage: f.polynomial(w)
            w^5 + 17*x*w^3 + (x*z*k + 3*x)*w + z^5 + x^3 + 5
            sage: f.polynomial(z)
            z^5 + x*w*k*z + w^5 + 17*x*w^3 + x^3 + 3*x*w + 5
            sage: f.polynomial(k)
            x*w*z*k + w^5 + z^5 + 17*x*w^3 + x^3 + 3*x*w + 5
            sage: R.<x,y> = GF(5)[]
            sage: f = x^2 + x + y
            sage: f.polynomial(x)
            x^2 + x + y
            sage: f.polynomial(y)
            y + x^2 + x"""
    @overload
    def polynomial(self, y) -> Any:
        """MPolynomial.polynomial(self, var)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 417)

        Let ``var`` be one of the variables of the parent of ``self``.  This
        returns ``self`` viewed as a univariate polynomial in ``var`` over the
        polynomial ring generated by all the other variables of the parent.

        EXAMPLES::

            sage: R.<x,w,z> = QQ[]
            sage: f = x^3 + 3*w*x + w^5 + (17*w^3)*x + z^5
            sage: f.polynomial(x)
            x^3 + (17*w^3 + 3*w)*x + w^5 + z^5
            sage: parent(f.polynomial(x))
            Univariate Polynomial Ring in x
             over Multivariate Polynomial Ring in w, z over Rational Field

            sage: f.polynomial(w)
            w^5 + 17*x*w^3 + 3*x*w + z^5 + x^3
            sage: f.polynomial(z)
            z^5 + w^5 + 17*x*w^3 + x^3 + 3*x*w
            sage: R.<x,w,z,k> = ZZ[]
            sage: f = x^3 + 3*w*x + w^5 + (17*w^3)*x + z^5 +x*w*z*k + 5
            sage: f.polynomial(x)
            x^3 + (17*w^3 + w*z*k + 3*w)*x + w^5 + z^5 + 5
            sage: f.polynomial(w)
            w^5 + 17*x*w^3 + (x*z*k + 3*x)*w + z^5 + x^3 + 5
            sage: f.polynomial(z)
            z^5 + x*w*k*z + w^5 + 17*x*w^3 + x^3 + 3*x*w + 5
            sage: f.polynomial(k)
            x*w*z*k + w^5 + z^5 + 17*x*w^3 + x^3 + 3*x*w + 5
            sage: R.<x,y> = GF(5)[]
            sage: f = x^2 + x + y
            sage: f.polynomial(x)
            x^2 + x + y
            sage: f.polynomial(y)
            y + x^2 + x"""
    def reduced_form(self, **kwds) -> Any:
        '''MPolynomial.reduced_form(self, **kwds)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 2370)

        Return a reduced form of this polynomial.

        The algorithm is from Stoll and Cremona\'s "On the Reduction Theory of
        Binary Forms" [CS2003]_. This takes a two variable homogeneous polynomial and
        finds a reduced form. This is a `SL(2,\\ZZ)`-equivalent binary form
        whose covariant in the upper half plane is in the fundamental domain.
        If the polynomial has multiple roots, they are removed and the algorithm
        is applied to the portion without multiple roots.

        This reduction should also minimize the sum of the squares of the coefficients,
        but this is not always the case.  By default the coefficient minimizing
        algorithm in [HS2018]_ is applied. The coefficients can be minimized
        either with respect to the sum of their squares or the maximum of their
        global heights.

        A portion of the algorithm uses Newton\'s method to find a solution to
        a system of equations. If Newton\'s method fails to converge to a point
        in the upper half plane, the function will use the less precise `z_0`
        covariant from the `Q_0` form as defined on page 7 of [CS2003]_.
        Additionally, if this polynomial has
        a root with multiplicity at least half the total degree of the polynomial,
        then we must also use the `z_0` covariant. See [CS2003]_ for details.

        Note that, if the covariant is within ``error_limit`` of the boundary
        but outside the fundamental domain, our function will erroneously move
        it to within the fundamental domain, hence our conjugation will be off
        by 1. If you don\'t want this to happen, decrease your ``error_limit``
        and increase your precision.

        Implemented by Rebecca Lauren Miller as part of GSOC 2016. Smallest
        coefficients added by Ben Hutz July 2018.

        INPUT: keyword arguments:

        - ``prec`` -- integer (default: 300); sets the precision

        - ``return_conjugation`` -- boolean (default: ``True``); whether to
          return element of `SL(2, \\ZZ)`

        - ``error_limit`` -- sets the error tolerance (default: 0.000001)

        - ``smallest_coeffs`` -- boolean (default: ``True``); whether to find the
          model with smallest coefficients

        - ``norm_type`` -- either ``\'norm\'`` or ``\'height\'``; what type of norm
          to use for smallest coefficients

        - ``emb`` -- (optional) embedding of based field into ``CC``

        OUTPUT:

        - a polynomial (reduced binary form)

        - a matrix (element of `SL(2, \\ZZ)`)

        .. TODO::

            When Newton\'s Method doesn\'t converge to a root in the upper half plane.
            Now we just return `z_0`. It would be better to modify and find the unique root
            in the upper half plane.

        EXAMPLES::

            sage: R.<x,h> = PolynomialRing(QQ)
            sage: f = 19*x^8 - 262*x^7*h + 1507*x^6*h^2 - 4784*x^5*h^3 + 9202*x^4*h^4\\\n            ....: -10962*x^3*h^5 + 7844*x^2*h^6 - 3040*x*h^7 + 475*h^8
            sage: f.reduced_form(prec=200, smallest_coeffs=False)                       # needs sage.modules sage.rings.complex_interval_field
            (
            -x^8 - 2*x^7*h + 7*x^6*h^2 + 16*x^5*h^3 + 2*x^4*h^4 - 2*x^3*h^5 + 4*x^2*h^6 - 5*h^8,
            <BLANKLINE>
            [ 1 -2]
            [ 1 -1]
            )

        An example where the multiplicity is too high::

            sage: R.<x,y> = PolynomialRing(QQ)
            sage: f = x^3 + 378666*x^2*y - 12444444*x*y^2 + 1234567890*y^3
            sage: j = f * (x-545*y)^9
            sage: j.reduced_form(prec=200, smallest_coeffs=False)                       # needs sage.modules sage.rings.complex_interval_field
            Traceback (most recent call last):
            ...
            ValueError: cannot have a root with multiplicity >= 12/2

        An example where Newton\'s Method does not find the right root::

            sage: R.<x,y> = PolynomialRing(QQ)
            sage: F = x^6 + 3*x^5*y - 8*x^4*y^2 - 2*x^3*y^3 - 44*x^2*y^4 - 8*x*y^5
            sage: F.reduced_form(smallest_coeffs=False, prec=400)                       # needs sage.modules sage.rings.complex_interval_field
            Traceback (most recent call last):
            ...
            ArithmeticError: Newton\'s method converged to z not in the upper half plane

        An example with covariant on the boundary, therefore a non-unique form::

            sage: R.<x,y> = PolynomialRing(QQ)
            sage: F = 5*x^2*y - 5*x*y^2 - 30*y^3
            sage: F.reduced_form(smallest_coeffs=False)                                 # needs sage.modules sage.rings.complex_interval_field
            (
                                        [1 1]
            5*x^2*y + 5*x*y^2 - 30*y^3, [0 1]
            )

        An example where precision needs to be increased::

            sage: R.<x,y> = PolynomialRing(QQ)
            sage: F = (-16*x^7 - 114*x^6*y - 345*x^5*y^2 - 599*x^4*y^3
            ....:      - 666*x^3*y^4 - 481*x^2*y^5 - 207*x*y^6 - 40*y^7)
            sage: F.reduced_form(prec=50, smallest_coeffs=False)                        # needs sage.modules sage.rings.complex_interval_field
            Traceback (most recent call last):
            ...
            ValueError: accuracy of Newton\'s root not within tolerance(0.000012... > 1e-06),
            increase precision
            sage: F.reduced_form(prec=100, smallest_coeffs=False)                       # needs sage.modules sage.rings.complex_interval_field
            (
                                                                  [-1 -1]
            -x^5*y^2 - 24*x^3*y^4 - 3*x^2*y^5 - 2*x*y^6 + 16*y^7, [ 1  0]
            )

        ::

            sage: R.<x,y> = PolynomialRing(QQ)
            sage: F = - 8*x^4 - 3933*x^3*y - 725085*x^2*y^2 - 59411592*x*y^3 - 1825511633*y^4
            sage: F.reduced_form(return_conjugation=False)                              # needs sage.modules sage.rings.complex_interval_field
            x^4 + 9*x^3*y - 3*x*y^3 - 8*y^4

        ::

            sage: R.<x,y> = QQ[]
            sage: F = -2*x^3 + 2*x^2*y + 3*x*y^2 + 127*y^3
            sage: F.reduced_form()                                                      # needs sage.modules sage.rings.complex_interval_field
            (
                                                   [1 4]
            -2*x^3 - 22*x^2*y - 77*x*y^2 + 43*y^3, [0 1]
            )

        ::

            sage: R.<x,y> = QQ[]
            sage: F = -2*x^3 + 2*x^2*y + 3*x*y^2 + 127*y^3
            sage: F.reduced_form(norm_type=\'height\')                                    # needs sage.modules sage.rings.complex_interval_field
            (
                                                    [5 4]
            -58*x^3 - 47*x^2*y + 52*x*y^2 + 43*y^3, [1 1]
            )

        ::

            sage: R.<x,y,z> = PolynomialRing(QQ)
            sage: F = x^4 + x^3*y*z + y^2*z
            sage: F.reduced_form()                                                      # needs sage.modules sage.rings.complex_interval_field
            Traceback (most recent call last):
            ...
            ValueError: (=x^3*y*z + x^4 + y^2*z) must have two variables

        ::

            sage: R.<x,y> = PolynomialRing(ZZ)
            sage: F = - 8*x^6 - 3933*x^3*y - 725085*x^2*y^2 - 59411592*x*y^3 - 99*y^6
            sage: F.reduced_form(return_conjugation=False)                              # needs sage.modules sage.rings.complex_interval_field
            Traceback (most recent call last):
            ...
            ValueError: (=-8*x^6 - 99*y^6 - 3933*x^3*y - 725085*x^2*y^2 -
            59411592*x*y^3) must be homogeneous

        ::

            sage: R.<x,y> = PolynomialRing(RR)
            sage: F = (217.992172373276*x^3 + 96023.1505442490*x^2*y
            ....:      + 1.40987971253579e7*x*y^2 + 6.90016027113216e8*y^3)
            sage: F.reduced_form(smallest_coeffs=False)  # tol 1e-8                     # needs sage.modules sage.rings.complex_interval_field
            (
            -39.5673942565918*x^3 + 111.874026298523*x^2*y
             + 231.052762985229*x*y^2 - 138.380829811096*y^3,
            <BLANKLINE>
            [-147 -148]
            [   1    1]
            )

        ::

            sage: R.<x,y> = PolynomialRing(CC)                                          # needs sage.rings.real_mpfr
            sage: F = ((0.759099196558145 + 0.845425869641446*CC.0)*x^3                 # needs sage.rings.real_mpfr
            ....:      + (84.8317207268542 + 93.8840848648033*CC.0)*x^2*y
            ....:      + (3159.07040755858 + 3475.33037377779*CC.0)*x*y^2
            ....:      + (39202.5965389079 + 42882.5139724962*CC.0)*y^3)
            sage: F.reduced_form(smallest_coeffs=False)  # tol 1e-11                    # needs sage.modules sage.rings.complex_interval_field sage.rings.real_mpfr
            (
            (-0.759099196558145 - 0.845425869641446*I)*x^3
            + (-0.571709908900118 - 0.0418133346027929*I)*x^2*y
            + (0.856525964330103 - 0.0721403997649759*I)*x*y^2
            + (-0.965531044130330 + 0.754252314465703*I)*y^3,
            <BLANKLINE>
            [-1 37]
            [ 0 -1]
            )'''
    def specialization(self, D=..., phi=...) -> Any:
        """MPolynomial.specialization(self, D=None, phi=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 2319)

        Specialization of this polynomial.

        Given a family of polynomials defined over a polynomial ring. A specialization
        is a particular member of that family. The specialization can be specified either
        by a dictionary or a :class:`SpecializationMorphism`.

        INPUT:

        - ``D`` -- dictionary (optional)

        - ``phi`` -- :class:`SpecializationMorphism` (optional)

        OUTPUT: a new polynomial

        EXAMPLES::

            sage: R.<c> = PolynomialRing(QQ)
            sage: S.<x,y> = PolynomialRing(R)
            sage: F = x^2 + c*y^2
            sage: F.specialization({c:2})
            x^2 + 2*y^2

        ::

            sage: S.<a,b> = PolynomialRing(QQ)
            sage: P.<x,y,z> = PolynomialRing(S)
            sage: RR.<c,d> = PolynomialRing(P)
            sage: f = a*x^2 + b*y^3 + c*y^2 - b*a*d + d^2 - a*c*b*z^2
            sage: f.specialization({a:2, z:4, d:2})
            (y^2 - 32*b)*c + b*y^3 + 2*x^2 - 4*b + 4

        Check that we preserve multi- versus uni-variate::

            sage: R.<l> = PolynomialRing(QQ, 1)
            sage: S.<k> = PolynomialRing(R)
            sage: K.<a, b, c> = PolynomialRing(S)
            sage: F = a*k^2 + b*l + c^2
            sage: F.specialization({b:56, c:5}).parent()
            Univariate Polynomial Ring in a over Univariate Polynomial Ring in k
            over Multivariate Polynomial Ring in l over Rational Field"""
    @overload
    def subresultants(self, other, variable=...) -> Any:
        """MPolynomial.subresultants(self, other, variable=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 1668)

        Return the nonzero subresultant polynomials of ``self`` and ``other``.

        INPUT:

        - ``other`` -- a polynomial

        OUTPUT: list of polynomials in the same ring as ``self``

        EXAMPLES::

            sage: R.<x,y> = QQ[]
            sage: p = (y^2 + 6)*(x - 1) - y*(x^2 + 1)
            sage: q = (x^2 + 6)*(y - 1) - x*(y^2 + 1)
            sage: p.subresultants(q, y)
            [2*x^6 - 22*x^5 + 102*x^4 - 274*x^3 + 488*x^2 - 552*x + 288,
             -x^3 - x^2*y + 6*x^2 + 5*x*y - 11*x - 6*y + 6]
            sage: p.subresultants(q, x)
            [2*y^6 - 22*y^5 + 102*y^4 - 274*y^3 + 488*y^2 - 552*y + 288,
             x*y^2 + y^3 - 5*x*y - 6*y^2 + 6*x + 11*y - 6]"""
    @overload
    def subresultants(self, q, y) -> Any:
        """MPolynomial.subresultants(self, other, variable=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 1668)

        Return the nonzero subresultant polynomials of ``self`` and ``other``.

        INPUT:

        - ``other`` -- a polynomial

        OUTPUT: list of polynomials in the same ring as ``self``

        EXAMPLES::

            sage: R.<x,y> = QQ[]
            sage: p = (y^2 + 6)*(x - 1) - y*(x^2 + 1)
            sage: q = (x^2 + 6)*(y - 1) - x*(y^2 + 1)
            sage: p.subresultants(q, y)
            [2*x^6 - 22*x^5 + 102*x^4 - 274*x^3 + 488*x^2 - 552*x + 288,
             -x^3 - x^2*y + 6*x^2 + 5*x*y - 11*x - 6*y + 6]
            sage: p.subresultants(q, x)
            [2*y^6 - 22*y^5 + 102*y^4 - 274*y^3 + 488*y^2 - 552*y + 288,
             x*y^2 + y^3 - 5*x*y - 6*y^2 + 6*x + 11*y - 6]"""
    @overload
    def subresultants(self, q, x) -> Any:
        """MPolynomial.subresultants(self, other, variable=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 1668)

        Return the nonzero subresultant polynomials of ``self`` and ``other``.

        INPUT:

        - ``other`` -- a polynomial

        OUTPUT: list of polynomials in the same ring as ``self``

        EXAMPLES::

            sage: R.<x,y> = QQ[]
            sage: p = (y^2 + 6)*(x - 1) - y*(x^2 + 1)
            sage: q = (x^2 + 6)*(y - 1) - x*(y^2 + 1)
            sage: p.subresultants(q, y)
            [2*x^6 - 22*x^5 + 102*x^4 - 274*x^3 + 488*x^2 - 552*x + 288,
             -x^3 - x^2*y + 6*x^2 + 5*x*y - 11*x - 6*y + 6]
            sage: p.subresultants(q, x)
            [2*y^6 - 22*y^5 + 102*y^4 - 274*y^3 + 488*y^2 - 552*y + 288,
             x*y^2 + y^3 - 5*x*y - 6*y^2 + 6*x + 11*y - 6]"""
    @overload
    def sylvester_matrix(self, right, variable=...) -> Any:
        """MPolynomial.sylvester_matrix(self, right, variable=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 1455)

        Given two nonzero polynomials ``self`` and ``right``, return the Sylvester
        matrix of the polynomials with respect to a given variable.

        Note that the Sylvester matrix is not defined if one of the polynomials
        is zero.

        INPUT:

        - ``self``, ``right`` -- multivariate polynomials
        - ``variable`` -- (optional) compute the Sylvester matrix with respect
          to this variable. If ``variable`` is not provided, the first variable
          of the polynomial ring is used.

        OUTPUT: the Sylvester matrix of ``self`` and ``right``

        EXAMPLES::

            sage: R.<x, y> = PolynomialRing(ZZ)
            sage: f = (y + 1)*x + 3*x**2
            sage: g = (y + 2)*x + 4*x**2
            sage: M = f.sylvester_matrix(g, x)                                          # needs sage.modules
            sage: M                                                                     # needs sage.modules
            [    3 y + 1     0     0]
            [    0     3 y + 1     0]
            [    4 y + 2     0     0]
            [    0     4 y + 2     0]

        If the polynomials share a non-constant common factor then the
        determinant of the Sylvester matrix will be zero::

            sage: M.determinant()                                                       # needs sage.modules
            0

            sage: f.sylvester_matrix(1 + g, x).determinant()                            # needs sage.modules
            y^2 - y + 7

        If both polynomials are of positive degree with respect to ``variable``, the
        determinant of the Sylvester matrix is the resultant::

            sage: f = R.random_element(4) or (x^2 * y^2)
            sage: g = R.random_element(4) or (x^2 * y^2)
            sage: f.sylvester_matrix(g, x).determinant() == f.resultant(g, x)           # needs sage.libs.singular sage.modules
            True

        TESTS:

        The variable is optional::

            sage: f = x + y
            sage: g = x + y
            sage: f.sylvester_matrix(g)                                                 # needs sage.modules
            [1 y]
            [1 y]

        Polynomials must be defined over compatible base rings::

            sage: # needs sage.modules
            sage: K.<x, y> = QQ[]
            sage: f = x + y
            sage: L.<x, y> = ZZ[]
            sage: g = x + y
            sage: R.<x, y> = GF(25, 'a')[]                                              # needs sage.rings.finite_rings
            sage: h = x + y
            sage: f.sylvester_matrix(g, 'x')
            [1 y]
            [1 y]
            sage: g.sylvester_matrix(h, 'x')                                            # needs sage.rings.finite_rings
            [1 y]
            [1 y]
            sage: f.sylvester_matrix(h, 'x')                                            # needs sage.rings.finite_rings
            Traceback (most recent call last):
            ...
            TypeError: no common canonical parent for objects with parents:
            'Multivariate Polynomial Ring in x, y over Rational Field' and
            'Multivariate Polynomial Ring in x, y over Finite Field in a of size 5^2'
            sage: K.<x, y, z> = QQ[]
            sage: f = x + y
            sage: L.<x, z> = QQ[]
            sage: g = x + z
            sage: f.sylvester_matrix(g)
            [1 y]
            [1 z]

        Corner cases::

            sage: # needs sage.modules
            sage: K.<x, y> = QQ[]
            sage: f = x^2 + 1
            sage: g = K(0)
            sage: f.sylvester_matrix(g)
            Traceback (most recent call last):
            ...
            ValueError: The Sylvester matrix is not defined for zero polynomials
            sage: g.sylvester_matrix(f)
            Traceback (most recent call last):
            ...
            ValueError: The Sylvester matrix is not defined for zero polynomials
            sage: g.sylvester_matrix(g)
            Traceback (most recent call last):
            ...
            ValueError: The Sylvester matrix is not defined for zero polynomials
            sage: K(3).sylvester_matrix(x^2)
            [3 0]
            [0 3]
            sage: K(3).sylvester_matrix(K(4))
            []"""
    @overload
    def sylvester_matrix(self, g, x) -> Any:
        """MPolynomial.sylvester_matrix(self, right, variable=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 1455)

        Given two nonzero polynomials ``self`` and ``right``, return the Sylvester
        matrix of the polynomials with respect to a given variable.

        Note that the Sylvester matrix is not defined if one of the polynomials
        is zero.

        INPUT:

        - ``self``, ``right`` -- multivariate polynomials
        - ``variable`` -- (optional) compute the Sylvester matrix with respect
          to this variable. If ``variable`` is not provided, the first variable
          of the polynomial ring is used.

        OUTPUT: the Sylvester matrix of ``self`` and ``right``

        EXAMPLES::

            sage: R.<x, y> = PolynomialRing(ZZ)
            sage: f = (y + 1)*x + 3*x**2
            sage: g = (y + 2)*x + 4*x**2
            sage: M = f.sylvester_matrix(g, x)                                          # needs sage.modules
            sage: M                                                                     # needs sage.modules
            [    3 y + 1     0     0]
            [    0     3 y + 1     0]
            [    4 y + 2     0     0]
            [    0     4 y + 2     0]

        If the polynomials share a non-constant common factor then the
        determinant of the Sylvester matrix will be zero::

            sage: M.determinant()                                                       # needs sage.modules
            0

            sage: f.sylvester_matrix(1 + g, x).determinant()                            # needs sage.modules
            y^2 - y + 7

        If both polynomials are of positive degree with respect to ``variable``, the
        determinant of the Sylvester matrix is the resultant::

            sage: f = R.random_element(4) or (x^2 * y^2)
            sage: g = R.random_element(4) or (x^2 * y^2)
            sage: f.sylvester_matrix(g, x).determinant() == f.resultant(g, x)           # needs sage.libs.singular sage.modules
            True

        TESTS:

        The variable is optional::

            sage: f = x + y
            sage: g = x + y
            sage: f.sylvester_matrix(g)                                                 # needs sage.modules
            [1 y]
            [1 y]

        Polynomials must be defined over compatible base rings::

            sage: # needs sage.modules
            sage: K.<x, y> = QQ[]
            sage: f = x + y
            sage: L.<x, y> = ZZ[]
            sage: g = x + y
            sage: R.<x, y> = GF(25, 'a')[]                                              # needs sage.rings.finite_rings
            sage: h = x + y
            sage: f.sylvester_matrix(g, 'x')
            [1 y]
            [1 y]
            sage: g.sylvester_matrix(h, 'x')                                            # needs sage.rings.finite_rings
            [1 y]
            [1 y]
            sage: f.sylvester_matrix(h, 'x')                                            # needs sage.rings.finite_rings
            Traceback (most recent call last):
            ...
            TypeError: no common canonical parent for objects with parents:
            'Multivariate Polynomial Ring in x, y over Rational Field' and
            'Multivariate Polynomial Ring in x, y over Finite Field in a of size 5^2'
            sage: K.<x, y, z> = QQ[]
            sage: f = x + y
            sage: L.<x, z> = QQ[]
            sage: g = x + z
            sage: f.sylvester_matrix(g)
            [1 y]
            [1 z]

        Corner cases::

            sage: # needs sage.modules
            sage: K.<x, y> = QQ[]
            sage: f = x^2 + 1
            sage: g = K(0)
            sage: f.sylvester_matrix(g)
            Traceback (most recent call last):
            ...
            ValueError: The Sylvester matrix is not defined for zero polynomials
            sage: g.sylvester_matrix(f)
            Traceback (most recent call last):
            ...
            ValueError: The Sylvester matrix is not defined for zero polynomials
            sage: g.sylvester_matrix(g)
            Traceback (most recent call last):
            ...
            ValueError: The Sylvester matrix is not defined for zero polynomials
            sage: K(3).sylvester_matrix(x^2)
            [3 0]
            [0 3]
            sage: K(3).sylvester_matrix(K(4))
            []"""
    @overload
    def sylvester_matrix(self, g, x) -> Any:
        """MPolynomial.sylvester_matrix(self, right, variable=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 1455)

        Given two nonzero polynomials ``self`` and ``right``, return the Sylvester
        matrix of the polynomials with respect to a given variable.

        Note that the Sylvester matrix is not defined if one of the polynomials
        is zero.

        INPUT:

        - ``self``, ``right`` -- multivariate polynomials
        - ``variable`` -- (optional) compute the Sylvester matrix with respect
          to this variable. If ``variable`` is not provided, the first variable
          of the polynomial ring is used.

        OUTPUT: the Sylvester matrix of ``self`` and ``right``

        EXAMPLES::

            sage: R.<x, y> = PolynomialRing(ZZ)
            sage: f = (y + 1)*x + 3*x**2
            sage: g = (y + 2)*x + 4*x**2
            sage: M = f.sylvester_matrix(g, x)                                          # needs sage.modules
            sage: M                                                                     # needs sage.modules
            [    3 y + 1     0     0]
            [    0     3 y + 1     0]
            [    4 y + 2     0     0]
            [    0     4 y + 2     0]

        If the polynomials share a non-constant common factor then the
        determinant of the Sylvester matrix will be zero::

            sage: M.determinant()                                                       # needs sage.modules
            0

            sage: f.sylvester_matrix(1 + g, x).determinant()                            # needs sage.modules
            y^2 - y + 7

        If both polynomials are of positive degree with respect to ``variable``, the
        determinant of the Sylvester matrix is the resultant::

            sage: f = R.random_element(4) or (x^2 * y^2)
            sage: g = R.random_element(4) or (x^2 * y^2)
            sage: f.sylvester_matrix(g, x).determinant() == f.resultant(g, x)           # needs sage.libs.singular sage.modules
            True

        TESTS:

        The variable is optional::

            sage: f = x + y
            sage: g = x + y
            sage: f.sylvester_matrix(g)                                                 # needs sage.modules
            [1 y]
            [1 y]

        Polynomials must be defined over compatible base rings::

            sage: # needs sage.modules
            sage: K.<x, y> = QQ[]
            sage: f = x + y
            sage: L.<x, y> = ZZ[]
            sage: g = x + y
            sage: R.<x, y> = GF(25, 'a')[]                                              # needs sage.rings.finite_rings
            sage: h = x + y
            sage: f.sylvester_matrix(g, 'x')
            [1 y]
            [1 y]
            sage: g.sylvester_matrix(h, 'x')                                            # needs sage.rings.finite_rings
            [1 y]
            [1 y]
            sage: f.sylvester_matrix(h, 'x')                                            # needs sage.rings.finite_rings
            Traceback (most recent call last):
            ...
            TypeError: no common canonical parent for objects with parents:
            'Multivariate Polynomial Ring in x, y over Rational Field' and
            'Multivariate Polynomial Ring in x, y over Finite Field in a of size 5^2'
            sage: K.<x, y, z> = QQ[]
            sage: f = x + y
            sage: L.<x, z> = QQ[]
            sage: g = x + z
            sage: f.sylvester_matrix(g)
            [1 y]
            [1 z]

        Corner cases::

            sage: # needs sage.modules
            sage: K.<x, y> = QQ[]
            sage: f = x^2 + 1
            sage: g = K(0)
            sage: f.sylvester_matrix(g)
            Traceback (most recent call last):
            ...
            ValueError: The Sylvester matrix is not defined for zero polynomials
            sage: g.sylvester_matrix(f)
            Traceback (most recent call last):
            ...
            ValueError: The Sylvester matrix is not defined for zero polynomials
            sage: g.sylvester_matrix(g)
            Traceback (most recent call last):
            ...
            ValueError: The Sylvester matrix is not defined for zero polynomials
            sage: K(3).sylvester_matrix(x^2)
            [3 0]
            [0 3]
            sage: K(3).sylvester_matrix(K(4))
            []"""
    @overload
    def sylvester_matrix(self, g) -> Any:
        """MPolynomial.sylvester_matrix(self, right, variable=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 1455)

        Given two nonzero polynomials ``self`` and ``right``, return the Sylvester
        matrix of the polynomials with respect to a given variable.

        Note that the Sylvester matrix is not defined if one of the polynomials
        is zero.

        INPUT:

        - ``self``, ``right`` -- multivariate polynomials
        - ``variable`` -- (optional) compute the Sylvester matrix with respect
          to this variable. If ``variable`` is not provided, the first variable
          of the polynomial ring is used.

        OUTPUT: the Sylvester matrix of ``self`` and ``right``

        EXAMPLES::

            sage: R.<x, y> = PolynomialRing(ZZ)
            sage: f = (y + 1)*x + 3*x**2
            sage: g = (y + 2)*x + 4*x**2
            sage: M = f.sylvester_matrix(g, x)                                          # needs sage.modules
            sage: M                                                                     # needs sage.modules
            [    3 y + 1     0     0]
            [    0     3 y + 1     0]
            [    4 y + 2     0     0]
            [    0     4 y + 2     0]

        If the polynomials share a non-constant common factor then the
        determinant of the Sylvester matrix will be zero::

            sage: M.determinant()                                                       # needs sage.modules
            0

            sage: f.sylvester_matrix(1 + g, x).determinant()                            # needs sage.modules
            y^2 - y + 7

        If both polynomials are of positive degree with respect to ``variable``, the
        determinant of the Sylvester matrix is the resultant::

            sage: f = R.random_element(4) or (x^2 * y^2)
            sage: g = R.random_element(4) or (x^2 * y^2)
            sage: f.sylvester_matrix(g, x).determinant() == f.resultant(g, x)           # needs sage.libs.singular sage.modules
            True

        TESTS:

        The variable is optional::

            sage: f = x + y
            sage: g = x + y
            sage: f.sylvester_matrix(g)                                                 # needs sage.modules
            [1 y]
            [1 y]

        Polynomials must be defined over compatible base rings::

            sage: # needs sage.modules
            sage: K.<x, y> = QQ[]
            sage: f = x + y
            sage: L.<x, y> = ZZ[]
            sage: g = x + y
            sage: R.<x, y> = GF(25, 'a')[]                                              # needs sage.rings.finite_rings
            sage: h = x + y
            sage: f.sylvester_matrix(g, 'x')
            [1 y]
            [1 y]
            sage: g.sylvester_matrix(h, 'x')                                            # needs sage.rings.finite_rings
            [1 y]
            [1 y]
            sage: f.sylvester_matrix(h, 'x')                                            # needs sage.rings.finite_rings
            Traceback (most recent call last):
            ...
            TypeError: no common canonical parent for objects with parents:
            'Multivariate Polynomial Ring in x, y over Rational Field' and
            'Multivariate Polynomial Ring in x, y over Finite Field in a of size 5^2'
            sage: K.<x, y, z> = QQ[]
            sage: f = x + y
            sage: L.<x, z> = QQ[]
            sage: g = x + z
            sage: f.sylvester_matrix(g)
            [1 y]
            [1 z]

        Corner cases::

            sage: # needs sage.modules
            sage: K.<x, y> = QQ[]
            sage: f = x^2 + 1
            sage: g = K(0)
            sage: f.sylvester_matrix(g)
            Traceback (most recent call last):
            ...
            ValueError: The Sylvester matrix is not defined for zero polynomials
            sage: g.sylvester_matrix(f)
            Traceback (most recent call last):
            ...
            ValueError: The Sylvester matrix is not defined for zero polynomials
            sage: g.sylvester_matrix(g)
            Traceback (most recent call last):
            ...
            ValueError: The Sylvester matrix is not defined for zero polynomials
            sage: K(3).sylvester_matrix(x^2)
            [3 0]
            [0 3]
            sage: K(3).sylvester_matrix(K(4))
            []"""
    @overload
    def sylvester_matrix(self, g) -> Any:
        """MPolynomial.sylvester_matrix(self, right, variable=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 1455)

        Given two nonzero polynomials ``self`` and ``right``, return the Sylvester
        matrix of the polynomials with respect to a given variable.

        Note that the Sylvester matrix is not defined if one of the polynomials
        is zero.

        INPUT:

        - ``self``, ``right`` -- multivariate polynomials
        - ``variable`` -- (optional) compute the Sylvester matrix with respect
          to this variable. If ``variable`` is not provided, the first variable
          of the polynomial ring is used.

        OUTPUT: the Sylvester matrix of ``self`` and ``right``

        EXAMPLES::

            sage: R.<x, y> = PolynomialRing(ZZ)
            sage: f = (y + 1)*x + 3*x**2
            sage: g = (y + 2)*x + 4*x**2
            sage: M = f.sylvester_matrix(g, x)                                          # needs sage.modules
            sage: M                                                                     # needs sage.modules
            [    3 y + 1     0     0]
            [    0     3 y + 1     0]
            [    4 y + 2     0     0]
            [    0     4 y + 2     0]

        If the polynomials share a non-constant common factor then the
        determinant of the Sylvester matrix will be zero::

            sage: M.determinant()                                                       # needs sage.modules
            0

            sage: f.sylvester_matrix(1 + g, x).determinant()                            # needs sage.modules
            y^2 - y + 7

        If both polynomials are of positive degree with respect to ``variable``, the
        determinant of the Sylvester matrix is the resultant::

            sage: f = R.random_element(4) or (x^2 * y^2)
            sage: g = R.random_element(4) or (x^2 * y^2)
            sage: f.sylvester_matrix(g, x).determinant() == f.resultant(g, x)           # needs sage.libs.singular sage.modules
            True

        TESTS:

        The variable is optional::

            sage: f = x + y
            sage: g = x + y
            sage: f.sylvester_matrix(g)                                                 # needs sage.modules
            [1 y]
            [1 y]

        Polynomials must be defined over compatible base rings::

            sage: # needs sage.modules
            sage: K.<x, y> = QQ[]
            sage: f = x + y
            sage: L.<x, y> = ZZ[]
            sage: g = x + y
            sage: R.<x, y> = GF(25, 'a')[]                                              # needs sage.rings.finite_rings
            sage: h = x + y
            sage: f.sylvester_matrix(g, 'x')
            [1 y]
            [1 y]
            sage: g.sylvester_matrix(h, 'x')                                            # needs sage.rings.finite_rings
            [1 y]
            [1 y]
            sage: f.sylvester_matrix(h, 'x')                                            # needs sage.rings.finite_rings
            Traceback (most recent call last):
            ...
            TypeError: no common canonical parent for objects with parents:
            'Multivariate Polynomial Ring in x, y over Rational Field' and
            'Multivariate Polynomial Ring in x, y over Finite Field in a of size 5^2'
            sage: K.<x, y, z> = QQ[]
            sage: f = x + y
            sage: L.<x, z> = QQ[]
            sage: g = x + z
            sage: f.sylvester_matrix(g)
            [1 y]
            [1 z]

        Corner cases::

            sage: # needs sage.modules
            sage: K.<x, y> = QQ[]
            sage: f = x^2 + 1
            sage: g = K(0)
            sage: f.sylvester_matrix(g)
            Traceback (most recent call last):
            ...
            ValueError: The Sylvester matrix is not defined for zero polynomials
            sage: g.sylvester_matrix(f)
            Traceback (most recent call last):
            ...
            ValueError: The Sylvester matrix is not defined for zero polynomials
            sage: g.sylvester_matrix(g)
            Traceback (most recent call last):
            ...
            ValueError: The Sylvester matrix is not defined for zero polynomials
            sage: K(3).sylvester_matrix(x^2)
            [3 0]
            [0 3]
            sage: K(3).sylvester_matrix(K(4))
            []"""
    @overload
    def sylvester_matrix(self, g) -> Any:
        """MPolynomial.sylvester_matrix(self, right, variable=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 1455)

        Given two nonzero polynomials ``self`` and ``right``, return the Sylvester
        matrix of the polynomials with respect to a given variable.

        Note that the Sylvester matrix is not defined if one of the polynomials
        is zero.

        INPUT:

        - ``self``, ``right`` -- multivariate polynomials
        - ``variable`` -- (optional) compute the Sylvester matrix with respect
          to this variable. If ``variable`` is not provided, the first variable
          of the polynomial ring is used.

        OUTPUT: the Sylvester matrix of ``self`` and ``right``

        EXAMPLES::

            sage: R.<x, y> = PolynomialRing(ZZ)
            sage: f = (y + 1)*x + 3*x**2
            sage: g = (y + 2)*x + 4*x**2
            sage: M = f.sylvester_matrix(g, x)                                          # needs sage.modules
            sage: M                                                                     # needs sage.modules
            [    3 y + 1     0     0]
            [    0     3 y + 1     0]
            [    4 y + 2     0     0]
            [    0     4 y + 2     0]

        If the polynomials share a non-constant common factor then the
        determinant of the Sylvester matrix will be zero::

            sage: M.determinant()                                                       # needs sage.modules
            0

            sage: f.sylvester_matrix(1 + g, x).determinant()                            # needs sage.modules
            y^2 - y + 7

        If both polynomials are of positive degree with respect to ``variable``, the
        determinant of the Sylvester matrix is the resultant::

            sage: f = R.random_element(4) or (x^2 * y^2)
            sage: g = R.random_element(4) or (x^2 * y^2)
            sage: f.sylvester_matrix(g, x).determinant() == f.resultant(g, x)           # needs sage.libs.singular sage.modules
            True

        TESTS:

        The variable is optional::

            sage: f = x + y
            sage: g = x + y
            sage: f.sylvester_matrix(g)                                                 # needs sage.modules
            [1 y]
            [1 y]

        Polynomials must be defined over compatible base rings::

            sage: # needs sage.modules
            sage: K.<x, y> = QQ[]
            sage: f = x + y
            sage: L.<x, y> = ZZ[]
            sage: g = x + y
            sage: R.<x, y> = GF(25, 'a')[]                                              # needs sage.rings.finite_rings
            sage: h = x + y
            sage: f.sylvester_matrix(g, 'x')
            [1 y]
            [1 y]
            sage: g.sylvester_matrix(h, 'x')                                            # needs sage.rings.finite_rings
            [1 y]
            [1 y]
            sage: f.sylvester_matrix(h, 'x')                                            # needs sage.rings.finite_rings
            Traceback (most recent call last):
            ...
            TypeError: no common canonical parent for objects with parents:
            'Multivariate Polynomial Ring in x, y over Rational Field' and
            'Multivariate Polynomial Ring in x, y over Finite Field in a of size 5^2'
            sage: K.<x, y, z> = QQ[]
            sage: f = x + y
            sage: L.<x, z> = QQ[]
            sage: g = x + z
            sage: f.sylvester_matrix(g)
            [1 y]
            [1 z]

        Corner cases::

            sage: # needs sage.modules
            sage: K.<x, y> = QQ[]
            sage: f = x^2 + 1
            sage: g = K(0)
            sage: f.sylvester_matrix(g)
            Traceback (most recent call last):
            ...
            ValueError: The Sylvester matrix is not defined for zero polynomials
            sage: g.sylvester_matrix(f)
            Traceback (most recent call last):
            ...
            ValueError: The Sylvester matrix is not defined for zero polynomials
            sage: g.sylvester_matrix(g)
            Traceback (most recent call last):
            ...
            ValueError: The Sylvester matrix is not defined for zero polynomials
            sage: K(3).sylvester_matrix(x^2)
            [3 0]
            [0 3]
            sage: K(3).sylvester_matrix(K(4))
            []"""
    @overload
    def sylvester_matrix(self, f) -> Any:
        """MPolynomial.sylvester_matrix(self, right, variable=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 1455)

        Given two nonzero polynomials ``self`` and ``right``, return the Sylvester
        matrix of the polynomials with respect to a given variable.

        Note that the Sylvester matrix is not defined if one of the polynomials
        is zero.

        INPUT:

        - ``self``, ``right`` -- multivariate polynomials
        - ``variable`` -- (optional) compute the Sylvester matrix with respect
          to this variable. If ``variable`` is not provided, the first variable
          of the polynomial ring is used.

        OUTPUT: the Sylvester matrix of ``self`` and ``right``

        EXAMPLES::

            sage: R.<x, y> = PolynomialRing(ZZ)
            sage: f = (y + 1)*x + 3*x**2
            sage: g = (y + 2)*x + 4*x**2
            sage: M = f.sylvester_matrix(g, x)                                          # needs sage.modules
            sage: M                                                                     # needs sage.modules
            [    3 y + 1     0     0]
            [    0     3 y + 1     0]
            [    4 y + 2     0     0]
            [    0     4 y + 2     0]

        If the polynomials share a non-constant common factor then the
        determinant of the Sylvester matrix will be zero::

            sage: M.determinant()                                                       # needs sage.modules
            0

            sage: f.sylvester_matrix(1 + g, x).determinant()                            # needs sage.modules
            y^2 - y + 7

        If both polynomials are of positive degree with respect to ``variable``, the
        determinant of the Sylvester matrix is the resultant::

            sage: f = R.random_element(4) or (x^2 * y^2)
            sage: g = R.random_element(4) or (x^2 * y^2)
            sage: f.sylvester_matrix(g, x).determinant() == f.resultant(g, x)           # needs sage.libs.singular sage.modules
            True

        TESTS:

        The variable is optional::

            sage: f = x + y
            sage: g = x + y
            sage: f.sylvester_matrix(g)                                                 # needs sage.modules
            [1 y]
            [1 y]

        Polynomials must be defined over compatible base rings::

            sage: # needs sage.modules
            sage: K.<x, y> = QQ[]
            sage: f = x + y
            sage: L.<x, y> = ZZ[]
            sage: g = x + y
            sage: R.<x, y> = GF(25, 'a')[]                                              # needs sage.rings.finite_rings
            sage: h = x + y
            sage: f.sylvester_matrix(g, 'x')
            [1 y]
            [1 y]
            sage: g.sylvester_matrix(h, 'x')                                            # needs sage.rings.finite_rings
            [1 y]
            [1 y]
            sage: f.sylvester_matrix(h, 'x')                                            # needs sage.rings.finite_rings
            Traceback (most recent call last):
            ...
            TypeError: no common canonical parent for objects with parents:
            'Multivariate Polynomial Ring in x, y over Rational Field' and
            'Multivariate Polynomial Ring in x, y over Finite Field in a of size 5^2'
            sage: K.<x, y, z> = QQ[]
            sage: f = x + y
            sage: L.<x, z> = QQ[]
            sage: g = x + z
            sage: f.sylvester_matrix(g)
            [1 y]
            [1 z]

        Corner cases::

            sage: # needs sage.modules
            sage: K.<x, y> = QQ[]
            sage: f = x^2 + 1
            sage: g = K(0)
            sage: f.sylvester_matrix(g)
            Traceback (most recent call last):
            ...
            ValueError: The Sylvester matrix is not defined for zero polynomials
            sage: g.sylvester_matrix(f)
            Traceback (most recent call last):
            ...
            ValueError: The Sylvester matrix is not defined for zero polynomials
            sage: g.sylvester_matrix(g)
            Traceback (most recent call last):
            ...
            ValueError: The Sylvester matrix is not defined for zero polynomials
            sage: K(3).sylvester_matrix(x^2)
            [3 0]
            [0 3]
            sage: K(3).sylvester_matrix(K(4))
            []"""
    @overload
    def sylvester_matrix(self, g) -> Any:
        """MPolynomial.sylvester_matrix(self, right, variable=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 1455)

        Given two nonzero polynomials ``self`` and ``right``, return the Sylvester
        matrix of the polynomials with respect to a given variable.

        Note that the Sylvester matrix is not defined if one of the polynomials
        is zero.

        INPUT:

        - ``self``, ``right`` -- multivariate polynomials
        - ``variable`` -- (optional) compute the Sylvester matrix with respect
          to this variable. If ``variable`` is not provided, the first variable
          of the polynomial ring is used.

        OUTPUT: the Sylvester matrix of ``self`` and ``right``

        EXAMPLES::

            sage: R.<x, y> = PolynomialRing(ZZ)
            sage: f = (y + 1)*x + 3*x**2
            sage: g = (y + 2)*x + 4*x**2
            sage: M = f.sylvester_matrix(g, x)                                          # needs sage.modules
            sage: M                                                                     # needs sage.modules
            [    3 y + 1     0     0]
            [    0     3 y + 1     0]
            [    4 y + 2     0     0]
            [    0     4 y + 2     0]

        If the polynomials share a non-constant common factor then the
        determinant of the Sylvester matrix will be zero::

            sage: M.determinant()                                                       # needs sage.modules
            0

            sage: f.sylvester_matrix(1 + g, x).determinant()                            # needs sage.modules
            y^2 - y + 7

        If both polynomials are of positive degree with respect to ``variable``, the
        determinant of the Sylvester matrix is the resultant::

            sage: f = R.random_element(4) or (x^2 * y^2)
            sage: g = R.random_element(4) or (x^2 * y^2)
            sage: f.sylvester_matrix(g, x).determinant() == f.resultant(g, x)           # needs sage.libs.singular sage.modules
            True

        TESTS:

        The variable is optional::

            sage: f = x + y
            sage: g = x + y
            sage: f.sylvester_matrix(g)                                                 # needs sage.modules
            [1 y]
            [1 y]

        Polynomials must be defined over compatible base rings::

            sage: # needs sage.modules
            sage: K.<x, y> = QQ[]
            sage: f = x + y
            sage: L.<x, y> = ZZ[]
            sage: g = x + y
            sage: R.<x, y> = GF(25, 'a')[]                                              # needs sage.rings.finite_rings
            sage: h = x + y
            sage: f.sylvester_matrix(g, 'x')
            [1 y]
            [1 y]
            sage: g.sylvester_matrix(h, 'x')                                            # needs sage.rings.finite_rings
            [1 y]
            [1 y]
            sage: f.sylvester_matrix(h, 'x')                                            # needs sage.rings.finite_rings
            Traceback (most recent call last):
            ...
            TypeError: no common canonical parent for objects with parents:
            'Multivariate Polynomial Ring in x, y over Rational Field' and
            'Multivariate Polynomial Ring in x, y over Finite Field in a of size 5^2'
            sage: K.<x, y, z> = QQ[]
            sage: f = x + y
            sage: L.<x, z> = QQ[]
            sage: g = x + z
            sage: f.sylvester_matrix(g)
            [1 y]
            [1 z]

        Corner cases::

            sage: # needs sage.modules
            sage: K.<x, y> = QQ[]
            sage: f = x^2 + 1
            sage: g = K(0)
            sage: f.sylvester_matrix(g)
            Traceback (most recent call last):
            ...
            ValueError: The Sylvester matrix is not defined for zero polynomials
            sage: g.sylvester_matrix(f)
            Traceback (most recent call last):
            ...
            ValueError: The Sylvester matrix is not defined for zero polynomials
            sage: g.sylvester_matrix(g)
            Traceback (most recent call last):
            ...
            ValueError: The Sylvester matrix is not defined for zero polynomials
            sage: K(3).sylvester_matrix(x^2)
            [3 0]
            [0 3]
            sage: K(3).sylvester_matrix(K(4))
            []"""
    @overload
    def trailing_support(self, *args, **kwds) -> Any:
        """MPolynomial.trailing_support(self, *args, **kwds)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 236)

        Return the minimal element of the support of ``self``,
        according to the term order.

        If the term ordering of the basis elements is not what is
        desired, a comparison key, ``key(x)``, can be provided.

        EXAMPLES::

            sage: R.<x,y,z> = PolynomialRing(QQ)
            sage: (3*x*y^2 + 2*y*z^3 + y^4 + 4*x*y*z).trailing_support()
            (1, 1, 1)
            sage: R.<x,y,z> = PolynomialRing(QQ, order='lex')
            sage: (3*x*y^2 + 2*y*z^3 + y^4 + 4*x*y*z).trailing_support()
            (0, 1, 3)
            sage: R.<x,y,z> = PolynomialRing(QQ, order='invlex')
            sage: (3*x*y^2 + 2*y*z^3 + y^4 + 4*x*y*z).trailing_support()
            (1, 2, 0)"""
    @overload
    def trailing_support(self) -> Any:
        """MPolynomial.trailing_support(self, *args, **kwds)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 236)

        Return the minimal element of the support of ``self``,
        according to the term order.

        If the term ordering of the basis elements is not what is
        desired, a comparison key, ``key(x)``, can be provided.

        EXAMPLES::

            sage: R.<x,y,z> = PolynomialRing(QQ)
            sage: (3*x*y^2 + 2*y*z^3 + y^4 + 4*x*y*z).trailing_support()
            (1, 1, 1)
            sage: R.<x,y,z> = PolynomialRing(QQ, order='lex')
            sage: (3*x*y^2 + 2*y*z^3 + y^4 + 4*x*y*z).trailing_support()
            (0, 1, 3)
            sage: R.<x,y,z> = PolynomialRing(QQ, order='invlex')
            sage: (3*x*y^2 + 2*y*z^3 + y^4 + 4*x*y*z).trailing_support()
            (1, 2, 0)"""
    @overload
    def trailing_support(self) -> Any:
        """MPolynomial.trailing_support(self, *args, **kwds)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 236)

        Return the minimal element of the support of ``self``,
        according to the term order.

        If the term ordering of the basis elements is not what is
        desired, a comparison key, ``key(x)``, can be provided.

        EXAMPLES::

            sage: R.<x,y,z> = PolynomialRing(QQ)
            sage: (3*x*y^2 + 2*y*z^3 + y^4 + 4*x*y*z).trailing_support()
            (1, 1, 1)
            sage: R.<x,y,z> = PolynomialRing(QQ, order='lex')
            sage: (3*x*y^2 + 2*y*z^3 + y^4 + 4*x*y*z).trailing_support()
            (0, 1, 3)
            sage: R.<x,y,z> = PolynomialRing(QQ, order='invlex')
            sage: (3*x*y^2 + 2*y*z^3 + y^4 + 4*x*y*z).trailing_support()
            (1, 2, 0)"""
    @overload
    def trailing_support(self) -> Any:
        """MPolynomial.trailing_support(self, *args, **kwds)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 236)

        Return the minimal element of the support of ``self``,
        according to the term order.

        If the term ordering of the basis elements is not what is
        desired, a comparison key, ``key(x)``, can be provided.

        EXAMPLES::

            sage: R.<x,y,z> = PolynomialRing(QQ)
            sage: (3*x*y^2 + 2*y*z^3 + y^4 + 4*x*y*z).trailing_support()
            (1, 1, 1)
            sage: R.<x,y,z> = PolynomialRing(QQ, order='lex')
            sage: (3*x*y^2 + 2*y*z^3 + y^4 + 4*x*y*z).trailing_support()
            (0, 1, 3)
            sage: R.<x,y,z> = PolynomialRing(QQ, order='invlex')
            sage: (3*x*y^2 + 2*y*z^3 + y^4 + 4*x*y*z).trailing_support()
            (1, 2, 0)"""
    def truncate(self, var, n) -> Any:
        """MPolynomial.truncate(self, var, n)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 299)

        Return a new multivariate polynomial obtained from ``self`` by
        deleting all terms that involve the given variable to a power
        at least ``n``."""
    @overload
    def weighted_degree(self, *weights) -> Any:
        """MPolynomial.weighted_degree(self, *weights)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 2047)

        Return the weighted degree of ``self``, which is the maximum weighted
        degree of all monomials in ``self``; the weighted degree of a monomial
        is the sum of all powers of the variables in the monomial, each power
        multiplied with its respective weight in ``weights``.

        This method is given for convenience. It is faster to use polynomial
        rings with weighted term orders and the standard ``degree`` function.

        INPUT:

        - ``weights`` -- either individual numbers, an iterable or a dictionary,
          specifying the weights of each variable. If it is a dictionary, it
          maps each variable of ``self`` to its weight. If it is a sequence of
          individual numbers or a tuple, the weights are specified in the order
          of the generators as given by ``self.parent().gens()``.

        EXAMPLES::

            sage: R.<x,y,z> = GF(7)[]
            sage: p = x^3 + y + x*z^2
            sage: p.weighted_degree({z:0, x:1, y:2})
            3
            sage: p.weighted_degree(1, 2, 0)
            3
            sage: p.weighted_degree((1, 4, 2))
            5
            sage: p.weighted_degree((1, 4, 1))
            4
            sage: p.weighted_degree(2**64, 2**50, 2**128)
            680564733841876926945195958937245974528
            sage: q = R.random_element(100, 20)
            sage: q.weighted_degree(1, 1, 1) == q.total_degree()
            True

        You may also work with negative weights

        ::

            sage: p.weighted_degree(-1, -2, -1)
            -2

        Note that only integer weights are allowed

        ::

            sage: p.weighted_degree(x, 1, 1)
            Traceback (most recent call last):
            ...
            TypeError: unable to convert non-constant polynomial x to Integer Ring
            sage: p.weighted_degree(2/1, 1, 1)
            6

        The :meth:`weighted_degree` coincides with the :meth:`degree` of a weighted
        polynomial ring, but the latter is faster.

        ::

            sage: K = PolynomialRing(QQ, 'x,y', order=TermOrder('wdegrevlex', (2,3)))
            sage: p = K.random_element(10)
            sage: p.degree() == p.weighted_degree(2,3)
            True

        TESTS::

            sage: # needs sage.modules
            sage: R = PolynomialRing(QQ, 'a', 5)
            sage: f = R.random_element(terms=20)
            sage: w = random_vector(ZZ,5)
            sage: d1 = f.weighted_degree(w)
            sage: d2 = (f*1.0).weighted_degree(w)
            sage: d1 == d2
            True"""
    @overload
    def weighted_degree(self, w) -> Any:
        """MPolynomial.weighted_degree(self, *weights)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 2047)

        Return the weighted degree of ``self``, which is the maximum weighted
        degree of all monomials in ``self``; the weighted degree of a monomial
        is the sum of all powers of the variables in the monomial, each power
        multiplied with its respective weight in ``weights``.

        This method is given for convenience. It is faster to use polynomial
        rings with weighted term orders and the standard ``degree`` function.

        INPUT:

        - ``weights`` -- either individual numbers, an iterable or a dictionary,
          specifying the weights of each variable. If it is a dictionary, it
          maps each variable of ``self`` to its weight. If it is a sequence of
          individual numbers or a tuple, the weights are specified in the order
          of the generators as given by ``self.parent().gens()``.

        EXAMPLES::

            sage: R.<x,y,z> = GF(7)[]
            sage: p = x^3 + y + x*z^2
            sage: p.weighted_degree({z:0, x:1, y:2})
            3
            sage: p.weighted_degree(1, 2, 0)
            3
            sage: p.weighted_degree((1, 4, 2))
            5
            sage: p.weighted_degree((1, 4, 1))
            4
            sage: p.weighted_degree(2**64, 2**50, 2**128)
            680564733841876926945195958937245974528
            sage: q = R.random_element(100, 20)
            sage: q.weighted_degree(1, 1, 1) == q.total_degree()
            True

        You may also work with negative weights

        ::

            sage: p.weighted_degree(-1, -2, -1)
            -2

        Note that only integer weights are allowed

        ::

            sage: p.weighted_degree(x, 1, 1)
            Traceback (most recent call last):
            ...
            TypeError: unable to convert non-constant polynomial x to Integer Ring
            sage: p.weighted_degree(2/1, 1, 1)
            6

        The :meth:`weighted_degree` coincides with the :meth:`degree` of a weighted
        polynomial ring, but the latter is faster.

        ::

            sage: K = PolynomialRing(QQ, 'x,y', order=TermOrder('wdegrevlex', (2,3)))
            sage: p = K.random_element(10)
            sage: p.degree() == p.weighted_degree(2,3)
            True

        TESTS::

            sage: # needs sage.modules
            sage: R = PolynomialRing(QQ, 'a', 5)
            sage: f = R.random_element(terms=20)
            sage: w = random_vector(ZZ,5)
            sage: d1 = f.weighted_degree(w)
            sage: d2 = (f*1.0).weighted_degree(w)
            sage: d1 == d2
            True"""
    @overload
    def weighted_degree(self, w) -> Any:
        """MPolynomial.weighted_degree(self, *weights)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 2047)

        Return the weighted degree of ``self``, which is the maximum weighted
        degree of all monomials in ``self``; the weighted degree of a monomial
        is the sum of all powers of the variables in the monomial, each power
        multiplied with its respective weight in ``weights``.

        This method is given for convenience. It is faster to use polynomial
        rings with weighted term orders and the standard ``degree`` function.

        INPUT:

        - ``weights`` -- either individual numbers, an iterable or a dictionary,
          specifying the weights of each variable. If it is a dictionary, it
          maps each variable of ``self`` to its weight. If it is a sequence of
          individual numbers or a tuple, the weights are specified in the order
          of the generators as given by ``self.parent().gens()``.

        EXAMPLES::

            sage: R.<x,y,z> = GF(7)[]
            sage: p = x^3 + y + x*z^2
            sage: p.weighted_degree({z:0, x:1, y:2})
            3
            sage: p.weighted_degree(1, 2, 0)
            3
            sage: p.weighted_degree((1, 4, 2))
            5
            sage: p.weighted_degree((1, 4, 1))
            4
            sage: p.weighted_degree(2**64, 2**50, 2**128)
            680564733841876926945195958937245974528
            sage: q = R.random_element(100, 20)
            sage: q.weighted_degree(1, 1, 1) == q.total_degree()
            True

        You may also work with negative weights

        ::

            sage: p.weighted_degree(-1, -2, -1)
            -2

        Note that only integer weights are allowed

        ::

            sage: p.weighted_degree(x, 1, 1)
            Traceback (most recent call last):
            ...
            TypeError: unable to convert non-constant polynomial x to Integer Ring
            sage: p.weighted_degree(2/1, 1, 1)
            6

        The :meth:`weighted_degree` coincides with the :meth:`degree` of a weighted
        polynomial ring, but the latter is faster.

        ::

            sage: K = PolynomialRing(QQ, 'x,y', order=TermOrder('wdegrevlex', (2,3)))
            sage: p = K.random_element(10)
            sage: p.degree() == p.weighted_degree(2,3)
            True

        TESTS::

            sage: # needs sage.modules
            sage: R = PolynomialRing(QQ, 'a', 5)
            sage: f = R.random_element(terms=20)
            sage: w = random_vector(ZZ,5)
            sage: d1 = f.weighted_degree(w)
            sage: d2 = (f*1.0).weighted_degree(w)
            sage: d1 == d2
            True"""
    def __float__(self) -> Any:
        """MPolynomial.__float__(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 160)

        TESTS::

            sage: float(RR['x,y'](0))  # indirect doctest
            0.0
            sage: float(ZZ['x,y'].gen(0))
            Traceback (most recent call last):
            ...
            TypeError: unable to convert non-constant polynomial x to <class 'float'>"""
    def __hash__(self) -> Any:
        """MPolynomial.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 652)"""
    def __int__(self) -> Any:
        """MPolynomial.__int__(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 129)

        TESTS::

            sage: type(RR['x,y'])
            <class 'sage.rings.polynomial.multi_polynomial_ring.MPolynomialRing_polydict_domain_with_category'>
            sage: type(RR['x, y'](0))
            <class 'sage.rings.polynomial.multi_polynomial_element.MPolynomial_polydict'>

            sage: int(RR['x,y'](0))  # indirect doctest
            0
            sage: int(RR['x,y'](10))
            10
            sage: int(ZZ['x,y'].gen(0))
            Traceback (most recent call last):
            ...
            TypeError: unable to convert non-constant polynomial x to <class 'int'>

            sage: ZZ(RR['x,y'](0))  # indirect doctest
            0
            sage: ZZ(RR['x,y'](0.5))                                                    # needs sage.rings.real_mpfr
            Traceback (most recent call last):
            ...
            TypeError: Attempt to coerce non-integral RealNumber to Integer
            sage: ZZ(RR['x,y'].gen(0))
            Traceback (most recent call last):
            ...
            TypeError: unable to convert non-constant polynomial x to Integer Ring"""
    def __iter__(self) -> Any:
        """MPolynomial.__iter__(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 1239)

        Facilitates iterating over the monomials of ``self``,
        returning tuples of the form ``(coeff, mon)`` for each
        nonzero monomial.

        EXAMPLES::

            sage: P.<x,y,z> = PolynomialRing(QQ,3)
            sage: f = 3*x^3*y + 16*x + 7
            sage: [(c,m) for c,m in f]
            [(3, x^3*y), (16, x), (7, 1)]
            sage: f = P.random_element(12,14)
            sage: sum(c*m for c,m in f) == f
            True"""

class MPolynomial_libsingular(MPolynomial):
    """File: /build/sagemath/src/sage/src/sage/rings/polynomial/multi_polynomial.pyx (starting at line 3052)

        Abstract base class for :class:`~sage.rings.polynomial.multi_polynomial_libsingular.MPolynomial_libsingular`.

        This class is defined for the purpose of :func:`isinstance` tests.  It should not be
        instantiated.

        EXAMPLES::

            sage: from sage.rings.polynomial.multi_polynomial import MPolynomial_libsingular
            sage: R1.<x> = QQ[]
            sage: isinstance(x, MPolynomial_libsingular)
            False
            sage: R2.<y,z> = QQ[]
            sage: isinstance(y, MPolynomial_libsingular)                                    # needs sage.libs.singular
            True

        By design, there is a unique direct subclass::

            sage: len(sage.rings.polynomial.multi_polynomial.MPolynomial_libsingular.__subclasses__()) <= 1
            True
    """
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
