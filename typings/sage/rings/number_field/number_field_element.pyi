import _cython_3_2_1
import cypari2.pari_instance
import sage as sage
import sage.rings.number_field.number_field_element_base
from sage.categories.category import ZZ as ZZ
from sage.categories.fields import Fields as Fields
from sage.libs.ntl.error import NTLError as NTLError
from sage.misc.superseded import deprecation as deprecation
from sage.rings.complex_mpfr import CC as CC, ComplexField as ComplexField
from sage.rings.infinity import infinity as infinity
from sage.rings.integer import Integer_sage as Integer_sage
from sage.rings.rational_field import QQ as QQ
from sage.rings.real_mpfi import RealInterval as RealInterval
from sage.structure.element import canonical_coercion as canonical_coercion, coerce_binop as coerce_binop, have_same_parent as have_same_parent, parent as parent
from sage.structure.richcmp import revop as revop, rich_to_bool as rich_to_bool, rich_to_bool_sgn as rich_to_bool_sgn, richcmp as richcmp, richcmp_not_equal as richcmp_not_equal
from typing import Any, ClassVar, overload

TUNE_CHARPOLY_NF: int
is_NumberFieldElement: _cython_3_2_1.cython_function_or_method
pari: cypari2.pari_instance.Pari

class CoordinateFunction:
    """File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 5595)

        This class provides a callable object which expresses
        elements in terms of powers of a fixed field generator `\\alpha`.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^2 + x + 3)
            sage: f = (a + 1).coordinates_in_terms_of_powers(); f
            Coordinate function that writes elements in terms of the powers of a + 1
            sage: f.__class__
            <class 'sage.rings.number_field.number_field_element.CoordinateFunction'>
            sage: f(a)
            [-1, 1]
            sage: f == loads(dumps(f))
            True
    """
    def __init__(self, NumberFieldElementalpha, W, to_V) -> Any:
        """CoordinateFunction.__init__(self, NumberFieldElement alpha, W, to_V)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 5613)

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^2 + x + 3)
            sage: f = (a + 1).coordinates_in_terms_of_powers(); f # indirect doctest
            Coordinate function that writes elements in terms of the powers of a + 1"""
    @overload
    def alpha(self) -> Any:
        """CoordinateFunction.alpha(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 5638)

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^3 + 2)
            sage: (a + 2).coordinates_in_terms_of_powers().alpha()
            a + 2"""
    @overload
    def alpha(self) -> Any:
        """CoordinateFunction.alpha(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 5638)

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^3 + 2)
            sage: (a + 2).coordinates_in_terms_of_powers().alpha()
            a + 2"""
    def __call__(self, x) -> Any:
        """CoordinateFunction.__call__(self, x)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 5649)

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^3 + 2)
            sage: f = (a + 2).coordinates_in_terms_of_powers()
            sage: f(1/a)
            [-2, 2, -1/2]
            sage: f(ZZ(2))
            [2, 0, 0]
            sage: L.<b> = K.extension(x^2 + 7)
            sage: g = (a + b).coordinates_in_terms_of_powers()
            sage: g(a/b)
            [-3379/5461, -371/10922, -4125/38227, -15/5461, -14/5461, -9/76454]
            sage: g(a)
            [4459/10922, -4838/5461, -273/5461, -980/5461, -9/10922, -42/5461]
            sage: f(b)
            Traceback (most recent call last):
            ...
            TypeError: Cannot coerce element into this number field"""
    def __eq__(self, other) -> Any:
        """CoordinateFunction.__eq__(self, other)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 5675)

        Test equality.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^3 + 2)
            sage: c = (a + 2).coordinates_in_terms_of_powers()
            sage: c == (a - 3).coordinates_in_terms_of_powers()
            False

            sage: K.<a> = NumberField(x^4 + 1)
            sage: f = (a + 1).coordinates_in_terms_of_powers()
            sage: f == loads(dumps(f))
            True
            sage: f == (a + 2).coordinates_in_terms_of_powers()
            False
            sage: f == NumberField(x^2 + 3,'b').gen().coordinates_in_terms_of_powers()
            False"""
    def __ne__(self, other) -> Any:
        """CoordinateFunction.__ne__(self, other)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 5701)

        Test inequality.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^3 + 2)
            sage: c = (a + 2).coordinates_in_terms_of_powers()
            sage: c != (a - 3).coordinates_in_terms_of_powers()
            True"""

class NumberFieldElement(sage.rings.number_field.number_field_element_base.NumberFieldElement_base):
    """NumberFieldElement(parent, f)

    File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 162)

    An element of a number field.

    EXAMPLES::

        sage: x = polygen(ZZ, 'x')
        sage: k.<a> = NumberField(x^3 + x + 1)
        sage: a^3
        -a - 1"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, parent, f) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 209)

                INPUT:

                - ``parent`` -- a number field

                - ``f`` -- defines an element of a number field

                EXAMPLES:

                The following examples illustrate creation of elements of
                number fields, and some basic arithmetic.

                First we define a polynomial over Q::

                    sage: R.<x> = PolynomialRing(QQ)
                    sage: f = x^2 + 1

                Next we use f to define the number field::

                    sage: K.<a> = NumberField(f); K
                    Number Field in a with defining polynomial x^2 + 1
                    sage: a = K.gen()
                    sage: a^2
                    -1
                    sage: (a+1)^2
                    2*a
                    sage: a^2
                    -1
                    sage: z = K(5); 1/z
                    1/5

                We create a cube root of 2::

                    sage: K.<b> = NumberField(x^3 - 2)
                    sage: b = K.gen()
                    sage: b^3
                    2
                    sage: (b^2 + b + 1)^3
                    12*b^2 + 15*b + 19

                This example illustrates save and load::

                    sage: K.<a> = NumberField(x^17 - 2)
                    sage: s = a^15 - 19*a + 3
                    sage: loads(s.dumps()) == s
                    True

                If a real embedding is specified, then the element comparison works as expected::

                    sage: K.<g> = NumberField(x^3+2,embedding=1)
                    sage: RR(g)
                    -1.25992104989487
                    sage: -2 < g < -1
                    True
                    sage: g^2+1 < g + 1
                    False

                TESTS:

                Test round-trip conversion to PARI and back::

                    sage: x = polygen(QQ)
                    sage: K.<a> = NumberField(x^3 - 1/2*x + 1/3)
                    sage: b = K.random_element()
                    sage: K(pari(b)) == b
                    True
        """
    def abs(self, prec=..., i=...) -> Any:
        """NumberFieldElement.abs(self, prec=None, i=None)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 1312)
        Return the absolute value of this element.

                If ``i`` is provided, then the absolute value of the `i`-th
                embedding is given.

                Otherwise, if the number field has a coercion embedding into
                `\\RR`, the corresponding absolute value is returned as an
                element of the same field (unless ``prec`` is given).
                Otherwise, if it has a coercion embedding into
                `\\CC`, then the corresponding absolute value is returned.
                Finally, if there is no coercion embedding, `i` defaults to 0.

                For the computation, the complex field with ``prec`` bits of
                precision is used, defaulting to 53 bits of precision if
                ``prec`` is not provided. The result is in the corresponding
                real field.

                INPUT:

                - ``prec`` -- integer (default: ``None``); bits of precision

                - ``i`` -- integer (default: ``None``); which embedding to use

                EXAMPLES::

                    sage: z = CyclotomicField(7).gen()
                    sage: abs(z)
                    1.00000000000000
                    sage: abs(z^2 + 17*z - 3)
                    16.0604426799931
                    sage: x = polygen(ZZ, 'x')
                    sage: K.<a> = NumberField(x^3 + 17)
                    sage: abs(a)
                    2.57128159065824
                    sage: a.abs(prec=100)
                    2.5712815906582353554531872087
                    sage: a.abs(prec=100, i=1)
                    2.5712815906582353554531872087
                    sage: a.abs(100, 2)
                    2.5712815906582353554531872087

                Here's one where the absolute value depends on the embedding::

                    sage: K.<b> = NumberField(x^2 - 2)
                    sage: a = 1 + b
                    sage: a.abs(i=0)
                    0.414213562373095
                    sage: a.abs(i=1)
                    2.41421356237309

                Check that :issue:`16147` is fixed::

                    sage: x = polygen(ZZ)
                    sage: f = x^3 - x - 1
                    sage: beta = f.complex_roots()[0]; beta
                    1.32471795724475
                    sage: K.<b> = NumberField(f, embedding=beta)
                    sage: b.abs()
                    1.32471795724475

                Check that for fields with real coercion embeddings, absolute
                values are in the same field (:issue:`21105`)::

                    sage: x = polygen(ZZ)
                    sage: f = x^3 - x - 1
                    sage: K.<b> = NumberField(f, embedding=1.3)
                    sage: b.abs()
                    b

                However, if a specific embedding is requested, the behavior reverts
                to that of number fields without a coercion embedding into `\\RR`::

                    sage: b.abs(i=2)
                    1.32471795724475

                Also, if a precision is requested explicitly, the behavior reverts
                to that of number fields without a coercion embedding into `\\RR`::

                    sage: b.abs(prec=53)
                    1.32471795724475
        """
    @overload
    def abs_non_arch(self, P, prec=...) -> Any:
        """NumberFieldElement.abs_non_arch(self, P, prec=None)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 1408)

        Return the non-archimedean absolute value of this element with
        respect to the prime `P`, to the given precision.

        INPUT:

        - ``P`` -- a prime ideal of the parent of ``self``

        - ``prec`` -- integer (default: default :class:`RealField` precision);
          desired floating point precision

        OUTPUT:

        (real) the non-archimedean absolute value of this element with
        respect to the prime `P`, to the given precision.  This is the
        normalised absolute value, so that the underlying prime number
        `p` has absolute value `1/p`.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^2 + 5)
            sage: [1/K(2).abs_non_arch(P) for P in K.primes_above(2)]
            [2.00000000000000]
            sage: [1/K(3).abs_non_arch(P) for P in K.primes_above(3)]
            [3.00000000000000, 3.00000000000000]
            sage: [1/K(5).abs_non_arch(P) for P in K.primes_above(5)]
            [5.00000000000000]

        A relative example::

            sage: L.<b> = K.extension(x^2 - 5)
            sage: [b.abs_non_arch(P) for P in L.primes_above(b)]
            [0.447213595499958, 0.447213595499958]"""
    @overload
    def abs_non_arch(self, P) -> Any:
        """NumberFieldElement.abs_non_arch(self, P, prec=None)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 1408)

        Return the non-archimedean absolute value of this element with
        respect to the prime `P`, to the given precision.

        INPUT:

        - ``P`` -- a prime ideal of the parent of ``self``

        - ``prec`` -- integer (default: default :class:`RealField` precision);
          desired floating point precision

        OUTPUT:

        (real) the non-archimedean absolute value of this element with
        respect to the prime `P`, to the given precision.  This is the
        normalised absolute value, so that the underlying prime number
        `p` has absolute value `1/p`.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^2 + 5)
            sage: [1/K(2).abs_non_arch(P) for P in K.primes_above(2)]
            [2.00000000000000]
            sage: [1/K(3).abs_non_arch(P) for P in K.primes_above(3)]
            [3.00000000000000, 3.00000000000000]
            sage: [1/K(5).abs_non_arch(P) for P in K.primes_above(5)]
            [5.00000000000000]

        A relative example::

            sage: L.<b> = K.extension(x^2 - 5)
            sage: [b.abs_non_arch(P) for P in L.primes_above(b)]
            [0.447213595499958, 0.447213595499958]"""
    @overload
    def abs_non_arch(self, P) -> Any:
        """NumberFieldElement.abs_non_arch(self, P, prec=None)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 1408)

        Return the non-archimedean absolute value of this element with
        respect to the prime `P`, to the given precision.

        INPUT:

        - ``P`` -- a prime ideal of the parent of ``self``

        - ``prec`` -- integer (default: default :class:`RealField` precision);
          desired floating point precision

        OUTPUT:

        (real) the non-archimedean absolute value of this element with
        respect to the prime `P`, to the given precision.  This is the
        normalised absolute value, so that the underlying prime number
        `p` has absolute value `1/p`.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^2 + 5)
            sage: [1/K(2).abs_non_arch(P) for P in K.primes_above(2)]
            [2.00000000000000]
            sage: [1/K(3).abs_non_arch(P) for P in K.primes_above(3)]
            [3.00000000000000, 3.00000000000000]
            sage: [1/K(5).abs_non_arch(P) for P in K.primes_above(5)]
            [5.00000000000000]

        A relative example::

            sage: L.<b> = K.extension(x^2 - 5)
            sage: [b.abs_non_arch(P) for P in L.primes_above(b)]
            [0.447213595499958, 0.447213595499958]"""
    @overload
    def abs_non_arch(self, P) -> Any:
        """NumberFieldElement.abs_non_arch(self, P, prec=None)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 1408)

        Return the non-archimedean absolute value of this element with
        respect to the prime `P`, to the given precision.

        INPUT:

        - ``P`` -- a prime ideal of the parent of ``self``

        - ``prec`` -- integer (default: default :class:`RealField` precision);
          desired floating point precision

        OUTPUT:

        (real) the non-archimedean absolute value of this element with
        respect to the prime `P`, to the given precision.  This is the
        normalised absolute value, so that the underlying prime number
        `p` has absolute value `1/p`.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^2 + 5)
            sage: [1/K(2).abs_non_arch(P) for P in K.primes_above(2)]
            [2.00000000000000]
            sage: [1/K(3).abs_non_arch(P) for P in K.primes_above(3)]
            [3.00000000000000, 3.00000000000000]
            sage: [1/K(5).abs_non_arch(P) for P in K.primes_above(5)]
            [5.00000000000000]

        A relative example::

            sage: L.<b> = K.extension(x^2 - 5)
            sage: [b.abs_non_arch(P) for P in L.primes_above(b)]
            [0.447213595499958, 0.447213595499958]"""
    @overload
    def abs_non_arch(self, P) -> Any:
        """NumberFieldElement.abs_non_arch(self, P, prec=None)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 1408)

        Return the non-archimedean absolute value of this element with
        respect to the prime `P`, to the given precision.

        INPUT:

        - ``P`` -- a prime ideal of the parent of ``self``

        - ``prec`` -- integer (default: default :class:`RealField` precision);
          desired floating point precision

        OUTPUT:

        (real) the non-archimedean absolute value of this element with
        respect to the prime `P`, to the given precision.  This is the
        normalised absolute value, so that the underlying prime number
        `p` has absolute value `1/p`.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^2 + 5)
            sage: [1/K(2).abs_non_arch(P) for P in K.primes_above(2)]
            [2.00000000000000]
            sage: [1/K(3).abs_non_arch(P) for P in K.primes_above(3)]
            [3.00000000000000, 3.00000000000000]
            sage: [1/K(5).abs_non_arch(P) for P in K.primes_above(5)]
            [5.00000000000000]

        A relative example::

            sage: L.<b> = K.extension(x^2 - 5)
            sage: [b.abs_non_arch(P) for P in L.primes_above(b)]
            [0.447213595499958, 0.447213595499958]"""
    def absolute_different(self) -> Any:
        """NumberFieldElement.absolute_different(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 4638)

        Return the absolute different of this element.

        This means the different with respect to the base field `\\QQ`.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberFieldTower([x^2 - 17, x^3 - 2])
            sage: a.absolute_different()
            0

        .. SEEALSO::

            :meth:`different`"""
    @overload
    def absolute_norm(self) -> Any:
        """NumberFieldElement.absolute_norm(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 3611)

        Return the absolute norm of this number field element.

        EXAMPLES::

            sage: K1.<a1> = CyclotomicField(11)
            sage: x = polygen(ZZ, 'x')
            sage: K2.<a2> = K1.extension(x^2 - 3)
            sage: K3.<a3> = K2.extension(x^2 + 1)
            sage: (a1 + a2 + a3).absolute_norm()
            1353244757701

            sage: QQ(7/5).absolute_norm()
            7/5"""
    @overload
    def absolute_norm(self) -> Any:
        """NumberFieldElement.absolute_norm(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 3611)

        Return the absolute norm of this number field element.

        EXAMPLES::

            sage: K1.<a1> = CyclotomicField(11)
            sage: x = polygen(ZZ, 'x')
            sage: K2.<a2> = K1.extension(x^2 - 3)
            sage: K3.<a3> = K2.extension(x^2 + 1)
            sage: (a1 + a2 + a3).absolute_norm()
            1353244757701

            sage: QQ(7/5).absolute_norm()
            7/5"""
    @overload
    def absolute_norm(self) -> Any:
        """NumberFieldElement.absolute_norm(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 3611)

        Return the absolute norm of this number field element.

        EXAMPLES::

            sage: K1.<a1> = CyclotomicField(11)
            sage: x = polygen(ZZ, 'x')
            sage: K2.<a2> = K1.extension(x^2 - 3)
            sage: K3.<a3> = K2.extension(x^2 + 1)
            sage: (a1 + a2 + a3).absolute_norm()
            1353244757701

            sage: QQ(7/5).absolute_norm()
            7/5"""
    @overload
    def additive_order(self) -> Any:
        """NumberFieldElement.additive_order(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 3405)

        Return the additive order of this element (i.e., infinity if
        ``self != 0`` and 1 if ``self == 0``)

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<u> = NumberField(x^4 - 3*x^2 + 3)
            sage: u.additive_order()
            +Infinity
            sage: K(0).additive_order()
            1
            sage: K.ring_of_integers().characteristic()  # implicit doctest
            0"""
    @overload
    def additive_order(self) -> Any:
        """NumberFieldElement.additive_order(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 3405)

        Return the additive order of this element (i.e., infinity if
        ``self != 0`` and 1 if ``self == 0``)

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<u> = NumberField(x^4 - 3*x^2 + 3)
            sage: u.additive_order()
            +Infinity
            sage: K(0).additive_order()
            1
            sage: K.ring_of_integers().characteristic()  # implicit doctest
            0"""
    @overload
    def additive_order(self) -> Any:
        """NumberFieldElement.additive_order(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 3405)

        Return the additive order of this element (i.e., infinity if
        ``self != 0`` and 1 if ``self == 0``)

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<u> = NumberField(x^4 - 3*x^2 + 3)
            sage: u.additive_order()
            +Infinity
            sage: K(0).additive_order()
            1
            sage: K.ring_of_integers().characteristic()  # implicit doctest
            0"""
    @overload
    def ceil(self) -> Any:
        """NumberFieldElement.ceil(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 1206)

        Return the ceiling of this number field element.

        EXAMPLES::

            sage: x = polygen(ZZ)
            sage: p = x**7 - 5*x**2 + x + 1
            sage: a_AA = AA.polynomial_root(p, RIF(1,2))
            sage: K.<a> = NumberField(p, embedding=a_AA)
            sage: b = a**5 + a/2 - 1/7
            sage: RR(b)
            4.13444473767055
            sage: b.ceil()
            5

        This function always succeeds even if a tremendous precision is needed::

            sage: c = b - 5065701199253/1225243417356 + 2
            sage: c.ceil()
            3
            sage: RIF(c).unique_ceil()
            Traceback (most recent call last):
            ...
            ValueError: interval does not have a unique ceil

        If the number field is not embedded, this function is valid only if the
        element is rational::

            sage: p = x**5 - 3
            sage: K.<a> = NumberField(p)
            sage: K(2/3).ceil()
            1
            sage: a.ceil()
            Traceback (most recent call last):
            ...
            TypeError: ceil not uniquely defined since no real embedding is specified"""
    @overload
    def ceil(self) -> Any:
        """NumberFieldElement.ceil(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 1206)

        Return the ceiling of this number field element.

        EXAMPLES::

            sage: x = polygen(ZZ)
            sage: p = x**7 - 5*x**2 + x + 1
            sage: a_AA = AA.polynomial_root(p, RIF(1,2))
            sage: K.<a> = NumberField(p, embedding=a_AA)
            sage: b = a**5 + a/2 - 1/7
            sage: RR(b)
            4.13444473767055
            sage: b.ceil()
            5

        This function always succeeds even if a tremendous precision is needed::

            sage: c = b - 5065701199253/1225243417356 + 2
            sage: c.ceil()
            3
            sage: RIF(c).unique_ceil()
            Traceback (most recent call last):
            ...
            ValueError: interval does not have a unique ceil

        If the number field is not embedded, this function is valid only if the
        element is rational::

            sage: p = x**5 - 3
            sage: K.<a> = NumberField(p)
            sage: K(2/3).ceil()
            1
            sage: a.ceil()
            Traceback (most recent call last):
            ...
            TypeError: ceil not uniquely defined since no real embedding is specified"""
    @overload
    def ceil(self) -> Any:
        """NumberFieldElement.ceil(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 1206)

        Return the ceiling of this number field element.

        EXAMPLES::

            sage: x = polygen(ZZ)
            sage: p = x**7 - 5*x**2 + x + 1
            sage: a_AA = AA.polynomial_root(p, RIF(1,2))
            sage: K.<a> = NumberField(p, embedding=a_AA)
            sage: b = a**5 + a/2 - 1/7
            sage: RR(b)
            4.13444473767055
            sage: b.ceil()
            5

        This function always succeeds even if a tremendous precision is needed::

            sage: c = b - 5065701199253/1225243417356 + 2
            sage: c.ceil()
            3
            sage: RIF(c).unique_ceil()
            Traceback (most recent call last):
            ...
            ValueError: interval does not have a unique ceil

        If the number field is not embedded, this function is valid only if the
        element is rational::

            sage: p = x**5 - 3
            sage: K.<a> = NumberField(p)
            sage: K(2/3).ceil()
            1
            sage: a.ceil()
            Traceback (most recent call last):
            ...
            TypeError: ceil not uniquely defined since no real embedding is specified"""
    @overload
    def ceil(self) -> Any:
        """NumberFieldElement.ceil(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 1206)

        Return the ceiling of this number field element.

        EXAMPLES::

            sage: x = polygen(ZZ)
            sage: p = x**7 - 5*x**2 + x + 1
            sage: a_AA = AA.polynomial_root(p, RIF(1,2))
            sage: K.<a> = NumberField(p, embedding=a_AA)
            sage: b = a**5 + a/2 - 1/7
            sage: RR(b)
            4.13444473767055
            sage: b.ceil()
            5

        This function always succeeds even if a tremendous precision is needed::

            sage: c = b - 5065701199253/1225243417356 + 2
            sage: c.ceil()
            3
            sage: RIF(c).unique_ceil()
            Traceback (most recent call last):
            ...
            ValueError: interval does not have a unique ceil

        If the number field is not embedded, this function is valid only if the
        element is rational::

            sage: p = x**5 - 3
            sage: K.<a> = NumberField(p)
            sage: K(2/3).ceil()
            1
            sage: a.ceil()
            Traceback (most recent call last):
            ...
            TypeError: ceil not uniquely defined since no real embedding is specified"""
    @overload
    def ceil(self) -> Any:
        """NumberFieldElement.ceil(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 1206)

        Return the ceiling of this number field element.

        EXAMPLES::

            sage: x = polygen(ZZ)
            sage: p = x**7 - 5*x**2 + x + 1
            sage: a_AA = AA.polynomial_root(p, RIF(1,2))
            sage: K.<a> = NumberField(p, embedding=a_AA)
            sage: b = a**5 + a/2 - 1/7
            sage: RR(b)
            4.13444473767055
            sage: b.ceil()
            5

        This function always succeeds even if a tremendous precision is needed::

            sage: c = b - 5065701199253/1225243417356 + 2
            sage: c.ceil()
            3
            sage: RIF(c).unique_ceil()
            Traceback (most recent call last):
            ...
            ValueError: interval does not have a unique ceil

        If the number field is not embedded, this function is valid only if the
        element is rational::

            sage: p = x**5 - 3
            sage: K.<a> = NumberField(p)
            sage: K(2/3).ceil()
            1
            sage: a.ceil()
            Traceback (most recent call last):
            ...
            TypeError: ceil not uniquely defined since no real embedding is specified"""
    @overload
    def charpoly(self, var=...) -> Any:
        """NumberFieldElement.charpoly(self, var='x')

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 3677)

        Return the characteristic polynomial of this number field element.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^3 + 7)
            sage: a.charpoly()
            x^3 + 7
            sage: K(1).charpoly()
            x^3 - 3*x^2 + 3*x - 1"""
    @overload
    def charpoly(self) -> Any:
        """NumberFieldElement.charpoly(self, var='x')

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 3677)

        Return the characteristic polynomial of this number field element.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^3 + 7)
            sage: a.charpoly()
            x^3 + 7
            sage: K(1).charpoly()
            x^3 - 3*x^2 + 3*x - 1"""
    @overload
    def charpoly(self) -> Any:
        """NumberFieldElement.charpoly(self, var='x')

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 3677)

        Return the characteristic polynomial of this number field element.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^3 + 7)
            sage: a.charpoly()
            x^3 + 7
            sage: K(1).charpoly()
            x^3 - 3*x^2 + 3*x - 1"""
    @overload
    def complex_embedding(self, prec=..., i=...) -> Any:
        """NumberFieldElement.complex_embedding(self, prec=53, i=0)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 1543)

        Return the `i`-th embedding of ``self`` in the complex numbers, to the
        given precision.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: k.<a> = NumberField(x^3 - 2)
            sage: a.complex_embedding()
            -0.629960524947437 - 1.09112363597172*I
            sage: a.complex_embedding(10)
            -0.63 - 1.1*I
            sage: a.complex_embedding(100)
            -0.62996052494743658238360530364 - 1.0911236359717214035600726142*I
            sage: a.complex_embedding(20, 1)
            -0.62996 + 1.0911*I
            sage: a.complex_embedding(20, 2)
            1.2599"""
    @overload
    def complex_embedding(self) -> Any:
        """NumberFieldElement.complex_embedding(self, prec=53, i=0)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 1543)

        Return the `i`-th embedding of ``self`` in the complex numbers, to the
        given precision.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: k.<a> = NumberField(x^3 - 2)
            sage: a.complex_embedding()
            -0.629960524947437 - 1.09112363597172*I
            sage: a.complex_embedding(10)
            -0.63 - 1.1*I
            sage: a.complex_embedding(100)
            -0.62996052494743658238360530364 - 1.0911236359717214035600726142*I
            sage: a.complex_embedding(20, 1)
            -0.62996 + 1.0911*I
            sage: a.complex_embedding(20, 2)
            1.2599"""
    @overload
    def complex_embeddings(self, prec=...) -> Any:
        """NumberFieldElement.complex_embeddings(self, prec=53)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 1516)

        Return the images of this element in the floating point complex
        numbers, to the given bits of precision.

        INPUT:

        - ``prec`` -- integer (default: 53); bits of precision

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: k.<a> = NumberField(x^3 - 2)
            sage: a.complex_embeddings()
            [-0.629960524947437 - 1.09112363597172*I,
             -0.629960524947437 + 1.09112363597172*I,
             1.25992104989487]
            sage: a.complex_embeddings(10)
            [-0.63 - 1.1*I, -0.63 + 1.1*I, 1.3]
            sage: a.complex_embeddings(100)
            [-0.62996052494743658238360530364 - 1.0911236359717214035600726142*I,
             -0.62996052494743658238360530364 + 1.0911236359717214035600726142*I,
             1.2599210498948731647672106073]"""
    @overload
    def complex_embeddings(self) -> Any:
        """NumberFieldElement.complex_embeddings(self, prec=53)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 1516)

        Return the images of this element in the floating point complex
        numbers, to the given bits of precision.

        INPUT:

        - ``prec`` -- integer (default: 53); bits of precision

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: k.<a> = NumberField(x^3 - 2)
            sage: a.complex_embeddings()
            [-0.629960524947437 - 1.09112363597172*I,
             -0.629960524947437 + 1.09112363597172*I,
             1.25992104989487]
            sage: a.complex_embeddings(10)
            [-0.63 - 1.1*I, -0.63 + 1.1*I, 1.3]
            sage: a.complex_embeddings(100)
            [-0.62996052494743658238360530364 - 1.0911236359717214035600726142*I,
             -0.62996052494743658238360530364 + 1.0911236359717214035600726142*I,
             1.2599210498948731647672106073]"""
    @overload
    def conjugate(self) -> Any:
        """NumberFieldElement.conjugate(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 3093)

        Return the complex conjugate of the number field element.

        This is only well-defined for fields contained in CM fields
        (i.e. for totally real fields and CM fields). Recall that a CM
        field is a totally imaginary quadratic extension of a totally
        real field. For other fields, a :exc:`ValueError` is raised.

        EXAMPLES::

            sage: k.<I> = QuadraticField(-1)
            sage: I.conjugate()
            -I
            sage: (I/(1+I)).conjugate()
            -1/2*I + 1/2
            sage: z6 = CyclotomicField(6).gen(0)
            sage: (2*z6).conjugate()
            -2*zeta6 + 2

        The following example now works.

        ::

            sage: x = polygen(ZZ, 'x')
            sage: F.<b> = NumberField(x^2 - 2)
            sage: K.<j> = F.extension(x^2 + 1)
            sage: j.conjugate()
            -j

        Raise a :exc:`ValueError` if the field is not contained in a CM field.

        ::

            sage: K.<b> = NumberField(x^3 - 2)
            sage: b.conjugate()
            Traceback (most recent call last):
            ...
            ValueError: Complex conjugation is only well-defined
            for fields contained in CM fields.

        An example of a non-quadratic totally real field.

        ::

            sage: F.<a> = NumberField(x^4 + x^3 - 3*x^2 - x + 1)
            sage: a.conjugate()
            a

        An example of a non-cyclotomic CM field.

        ::

            sage: K.<a> = NumberField(x^4 - x^3 + 2*x^2 + x + 1)
            sage: a.conjugate()
            -1/2*a^3 - a - 1/2
            sage: (2*a^2 - 1).conjugate()
            a^3 - 2*a^2 - 2"""
    @overload
    def conjugate(self) -> Any:
        """NumberFieldElement.conjugate(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 3093)

        Return the complex conjugate of the number field element.

        This is only well-defined for fields contained in CM fields
        (i.e. for totally real fields and CM fields). Recall that a CM
        field is a totally imaginary quadratic extension of a totally
        real field. For other fields, a :exc:`ValueError` is raised.

        EXAMPLES::

            sage: k.<I> = QuadraticField(-1)
            sage: I.conjugate()
            -I
            sage: (I/(1+I)).conjugate()
            -1/2*I + 1/2
            sage: z6 = CyclotomicField(6).gen(0)
            sage: (2*z6).conjugate()
            -2*zeta6 + 2

        The following example now works.

        ::

            sage: x = polygen(ZZ, 'x')
            sage: F.<b> = NumberField(x^2 - 2)
            sage: K.<j> = F.extension(x^2 + 1)
            sage: j.conjugate()
            -j

        Raise a :exc:`ValueError` if the field is not contained in a CM field.

        ::

            sage: K.<b> = NumberField(x^3 - 2)
            sage: b.conjugate()
            Traceback (most recent call last):
            ...
            ValueError: Complex conjugation is only well-defined
            for fields contained in CM fields.

        An example of a non-quadratic totally real field.

        ::

            sage: F.<a> = NumberField(x^4 + x^3 - 3*x^2 - x + 1)
            sage: a.conjugate()
            a

        An example of a non-cyclotomic CM field.

        ::

            sage: K.<a> = NumberField(x^4 - x^3 + 2*x^2 + x + 1)
            sage: a.conjugate()
            -1/2*a^3 - a - 1/2
            sage: (2*a^2 - 1).conjugate()
            a^3 - 2*a^2 - 2"""
    @overload
    def conjugate(self) -> Any:
        """NumberFieldElement.conjugate(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 3093)

        Return the complex conjugate of the number field element.

        This is only well-defined for fields contained in CM fields
        (i.e. for totally real fields and CM fields). Recall that a CM
        field is a totally imaginary quadratic extension of a totally
        real field. For other fields, a :exc:`ValueError` is raised.

        EXAMPLES::

            sage: k.<I> = QuadraticField(-1)
            sage: I.conjugate()
            -I
            sage: (I/(1+I)).conjugate()
            -1/2*I + 1/2
            sage: z6 = CyclotomicField(6).gen(0)
            sage: (2*z6).conjugate()
            -2*zeta6 + 2

        The following example now works.

        ::

            sage: x = polygen(ZZ, 'x')
            sage: F.<b> = NumberField(x^2 - 2)
            sage: K.<j> = F.extension(x^2 + 1)
            sage: j.conjugate()
            -j

        Raise a :exc:`ValueError` if the field is not contained in a CM field.

        ::

            sage: K.<b> = NumberField(x^3 - 2)
            sage: b.conjugate()
            Traceback (most recent call last):
            ...
            ValueError: Complex conjugation is only well-defined
            for fields contained in CM fields.

        An example of a non-quadratic totally real field.

        ::

            sage: F.<a> = NumberField(x^4 + x^3 - 3*x^2 - x + 1)
            sage: a.conjugate()
            a

        An example of a non-cyclotomic CM field.

        ::

            sage: K.<a> = NumberField(x^4 - x^3 + 2*x^2 + x + 1)
            sage: a.conjugate()
            -1/2*a^3 - a - 1/2
            sage: (2*a^2 - 1).conjugate()
            a^3 - 2*a^2 - 2"""
    @overload
    def conjugate(self) -> Any:
        """NumberFieldElement.conjugate(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 3093)

        Return the complex conjugate of the number field element.

        This is only well-defined for fields contained in CM fields
        (i.e. for totally real fields and CM fields). Recall that a CM
        field is a totally imaginary quadratic extension of a totally
        real field. For other fields, a :exc:`ValueError` is raised.

        EXAMPLES::

            sage: k.<I> = QuadraticField(-1)
            sage: I.conjugate()
            -I
            sage: (I/(1+I)).conjugate()
            -1/2*I + 1/2
            sage: z6 = CyclotomicField(6).gen(0)
            sage: (2*z6).conjugate()
            -2*zeta6 + 2

        The following example now works.

        ::

            sage: x = polygen(ZZ, 'x')
            sage: F.<b> = NumberField(x^2 - 2)
            sage: K.<j> = F.extension(x^2 + 1)
            sage: j.conjugate()
            -j

        Raise a :exc:`ValueError` if the field is not contained in a CM field.

        ::

            sage: K.<b> = NumberField(x^3 - 2)
            sage: b.conjugate()
            Traceback (most recent call last):
            ...
            ValueError: Complex conjugation is only well-defined
            for fields contained in CM fields.

        An example of a non-quadratic totally real field.

        ::

            sage: F.<a> = NumberField(x^4 + x^3 - 3*x^2 - x + 1)
            sage: a.conjugate()
            a

        An example of a non-cyclotomic CM field.

        ::

            sage: K.<a> = NumberField(x^4 - x^3 + 2*x^2 + x + 1)
            sage: a.conjugate()
            -1/2*a^3 - a - 1/2
            sage: (2*a^2 - 1).conjugate()
            a^3 - 2*a^2 - 2"""
    @overload
    def conjugate(self) -> Any:
        """NumberFieldElement.conjugate(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 3093)

        Return the complex conjugate of the number field element.

        This is only well-defined for fields contained in CM fields
        (i.e. for totally real fields and CM fields). Recall that a CM
        field is a totally imaginary quadratic extension of a totally
        real field. For other fields, a :exc:`ValueError` is raised.

        EXAMPLES::

            sage: k.<I> = QuadraticField(-1)
            sage: I.conjugate()
            -I
            sage: (I/(1+I)).conjugate()
            -1/2*I + 1/2
            sage: z6 = CyclotomicField(6).gen(0)
            sage: (2*z6).conjugate()
            -2*zeta6 + 2

        The following example now works.

        ::

            sage: x = polygen(ZZ, 'x')
            sage: F.<b> = NumberField(x^2 - 2)
            sage: K.<j> = F.extension(x^2 + 1)
            sage: j.conjugate()
            -j

        Raise a :exc:`ValueError` if the field is not contained in a CM field.

        ::

            sage: K.<b> = NumberField(x^3 - 2)
            sage: b.conjugate()
            Traceback (most recent call last):
            ...
            ValueError: Complex conjugation is only well-defined
            for fields contained in CM fields.

        An example of a non-quadratic totally real field.

        ::

            sage: F.<a> = NumberField(x^4 + x^3 - 3*x^2 - x + 1)
            sage: a.conjugate()
            a

        An example of a non-cyclotomic CM field.

        ::

            sage: K.<a> = NumberField(x^4 - x^3 + 2*x^2 + x + 1)
            sage: a.conjugate()
            -1/2*a^3 - a - 1/2
            sage: (2*a^2 - 1).conjugate()
            a^3 - 2*a^2 - 2"""
    @overload
    def conjugate(self) -> Any:
        """NumberFieldElement.conjugate(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 3093)

        Return the complex conjugate of the number field element.

        This is only well-defined for fields contained in CM fields
        (i.e. for totally real fields and CM fields). Recall that a CM
        field is a totally imaginary quadratic extension of a totally
        real field. For other fields, a :exc:`ValueError` is raised.

        EXAMPLES::

            sage: k.<I> = QuadraticField(-1)
            sage: I.conjugate()
            -I
            sage: (I/(1+I)).conjugate()
            -1/2*I + 1/2
            sage: z6 = CyclotomicField(6).gen(0)
            sage: (2*z6).conjugate()
            -2*zeta6 + 2

        The following example now works.

        ::

            sage: x = polygen(ZZ, 'x')
            sage: F.<b> = NumberField(x^2 - 2)
            sage: K.<j> = F.extension(x^2 + 1)
            sage: j.conjugate()
            -j

        Raise a :exc:`ValueError` if the field is not contained in a CM field.

        ::

            sage: K.<b> = NumberField(x^3 - 2)
            sage: b.conjugate()
            Traceback (most recent call last):
            ...
            ValueError: Complex conjugation is only well-defined
            for fields contained in CM fields.

        An example of a non-quadratic totally real field.

        ::

            sage: F.<a> = NumberField(x^4 + x^3 - 3*x^2 - x + 1)
            sage: a.conjugate()
            a

        An example of a non-cyclotomic CM field.

        ::

            sage: K.<a> = NumberField(x^4 - x^3 + 2*x^2 + x + 1)
            sage: a.conjugate()
            -1/2*a^3 - a - 1/2
            sage: (2*a^2 - 1).conjugate()
            a^3 - 2*a^2 - 2"""
    @overload
    def conjugate(self) -> Any:
        """NumberFieldElement.conjugate(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 3093)

        Return the complex conjugate of the number field element.

        This is only well-defined for fields contained in CM fields
        (i.e. for totally real fields and CM fields). Recall that a CM
        field is a totally imaginary quadratic extension of a totally
        real field. For other fields, a :exc:`ValueError` is raised.

        EXAMPLES::

            sage: k.<I> = QuadraticField(-1)
            sage: I.conjugate()
            -I
            sage: (I/(1+I)).conjugate()
            -1/2*I + 1/2
            sage: z6 = CyclotomicField(6).gen(0)
            sage: (2*z6).conjugate()
            -2*zeta6 + 2

        The following example now works.

        ::

            sage: x = polygen(ZZ, 'x')
            sage: F.<b> = NumberField(x^2 - 2)
            sage: K.<j> = F.extension(x^2 + 1)
            sage: j.conjugate()
            -j

        Raise a :exc:`ValueError` if the field is not contained in a CM field.

        ::

            sage: K.<b> = NumberField(x^3 - 2)
            sage: b.conjugate()
            Traceback (most recent call last):
            ...
            ValueError: Complex conjugation is only well-defined
            for fields contained in CM fields.

        An example of a non-quadratic totally real field.

        ::

            sage: F.<a> = NumberField(x^4 + x^3 - 3*x^2 - x + 1)
            sage: a.conjugate()
            a

        An example of a non-cyclotomic CM field.

        ::

            sage: K.<a> = NumberField(x^4 - x^3 + 2*x^2 + x + 1)
            sage: a.conjugate()
            -1/2*a^3 - a - 1/2
            sage: (2*a^2 - 1).conjugate()
            a^3 - 2*a^2 - 2"""
    @overload
    def conjugate(self) -> Any:
        """NumberFieldElement.conjugate(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 3093)

        Return the complex conjugate of the number field element.

        This is only well-defined for fields contained in CM fields
        (i.e. for totally real fields and CM fields). Recall that a CM
        field is a totally imaginary quadratic extension of a totally
        real field. For other fields, a :exc:`ValueError` is raised.

        EXAMPLES::

            sage: k.<I> = QuadraticField(-1)
            sage: I.conjugate()
            -I
            sage: (I/(1+I)).conjugate()
            -1/2*I + 1/2
            sage: z6 = CyclotomicField(6).gen(0)
            sage: (2*z6).conjugate()
            -2*zeta6 + 2

        The following example now works.

        ::

            sage: x = polygen(ZZ, 'x')
            sage: F.<b> = NumberField(x^2 - 2)
            sage: K.<j> = F.extension(x^2 + 1)
            sage: j.conjugate()
            -j

        Raise a :exc:`ValueError` if the field is not contained in a CM field.

        ::

            sage: K.<b> = NumberField(x^3 - 2)
            sage: b.conjugate()
            Traceback (most recent call last):
            ...
            ValueError: Complex conjugation is only well-defined
            for fields contained in CM fields.

        An example of a non-quadratic totally real field.

        ::

            sage: F.<a> = NumberField(x^4 + x^3 - 3*x^2 - x + 1)
            sage: a.conjugate()
            a

        An example of a non-cyclotomic CM field.

        ::

            sage: K.<a> = NumberField(x^4 - x^3 + 2*x^2 + x + 1)
            sage: a.conjugate()
            -1/2*a^3 - a - 1/2
            sage: (2*a^2 - 1).conjugate()
            a^3 - 2*a^2 - 2"""
    @overload
    def conjugate(self) -> Any:
        """NumberFieldElement.conjugate(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 3093)

        Return the complex conjugate of the number field element.

        This is only well-defined for fields contained in CM fields
        (i.e. for totally real fields and CM fields). Recall that a CM
        field is a totally imaginary quadratic extension of a totally
        real field. For other fields, a :exc:`ValueError` is raised.

        EXAMPLES::

            sage: k.<I> = QuadraticField(-1)
            sage: I.conjugate()
            -I
            sage: (I/(1+I)).conjugate()
            -1/2*I + 1/2
            sage: z6 = CyclotomicField(6).gen(0)
            sage: (2*z6).conjugate()
            -2*zeta6 + 2

        The following example now works.

        ::

            sage: x = polygen(ZZ, 'x')
            sage: F.<b> = NumberField(x^2 - 2)
            sage: K.<j> = F.extension(x^2 + 1)
            sage: j.conjugate()
            -j

        Raise a :exc:`ValueError` if the field is not contained in a CM field.

        ::

            sage: K.<b> = NumberField(x^3 - 2)
            sage: b.conjugate()
            Traceback (most recent call last):
            ...
            ValueError: Complex conjugation is only well-defined
            for fields contained in CM fields.

        An example of a non-quadratic totally real field.

        ::

            sage: F.<a> = NumberField(x^4 + x^3 - 3*x^2 - x + 1)
            sage: a.conjugate()
            a

        An example of a non-cyclotomic CM field.

        ::

            sage: K.<a> = NumberField(x^4 - x^3 + 2*x^2 + x + 1)
            sage: a.conjugate()
            -1/2*a^3 - a - 1/2
            sage: (2*a^2 - 1).conjugate()
            a^3 - 2*a^2 - 2"""
    def coordinates_in_terms_of_powers(self) -> Any:
        """NumberFieldElement.coordinates_in_terms_of_powers(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 1456)

        Let `\\alpha` be ``self``. Return a callable object (of type
        :class:`~CoordinateFunction`) that takes any element of the
        parent of ``self`` in `\\QQ(\\alpha)` and writes it in terms of the
        powers of `\\alpha`: `1, \\alpha, \\alpha^2, ...`.

        (NOT CACHED).

        EXAMPLES:

        This function allows us to write elements of a number
        field in terms of a different generator without having to construct
        a whole separate number field.

        ::

            sage: y = polygen(QQ,'y'); K.<beta> = NumberField(y^3 - 2); K
            Number Field in beta with defining polynomial y^3 - 2
            sage: alpha = beta^2 + beta + 1
            sage: c = alpha.coordinates_in_terms_of_powers(); c
            Coordinate function that writes elements in terms of the powers of beta^2 + beta + 1
            sage: c(beta)
            [-2, -3, 1]
            sage: c(alpha)
            [0, 1, 0]
            sage: c((1+beta)^5)
            [3, 3, 3]
            sage: c((1+beta)^10)
            [54, 162, 189]

        This function works even if ``self`` only generates a subfield of this
        number field.

        ::

            sage: x = polygen(ZZ, 'x')
            sage: k.<a> = NumberField(x^6 - 5)
            sage: alpha = a^3
            sage: c = alpha.coordinates_in_terms_of_powers()
            sage: c((2/3)*a^3 - 5/3)
            [-5/3, 2/3]
            sage: c
            Coordinate function that writes elements in terms of the powers of a^3
            sage: c(a)
            Traceback (most recent call last):
            ...
            ArithmeticError: vector is not in free module"""
    @overload
    def denominator(self) -> Any:
        """NumberFieldElement.denominator(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 3297)

        Return the denominator of this element, which is by definition the
        denominator of the corresponding polynomial representation. I.e.,
        elements of number fields are represented as a polynomial (in
        reduced form) modulo the modulus of the number field, and the
        denominator is the denominator of this polynomial.

        EXAMPLES::

            sage: K.<z> = CyclotomicField(3)
            sage: a = 1/3 + (1/5)*z
            sage: a.denominator()
            15"""
    @overload
    def denominator(self) -> Any:
        """NumberFieldElement.denominator(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 3297)

        Return the denominator of this element, which is by definition the
        denominator of the corresponding polynomial representation. I.e.,
        elements of number fields are represented as a polynomial (in
        reduced form) modulo the modulus of the number field, and the
        denominator is the denominator of this polynomial.

        EXAMPLES::

            sage: K.<z> = CyclotomicField(3)
            sage: a = 1/3 + (1/5)*z
            sage: a.denominator()
            15"""
    @overload
    def denominator_ideal(self) -> Any:
        """NumberFieldElement.denominator_ideal(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 4229)

        Return the denominator ideal of this number field element.

        The denominator ideal of a number field element `a` is the
        integral ideal consisting of all elements of the ring of
        integers `R` whose product with `a` is also in `R`.

        .. SEEALSO::

            :meth:`numerator_ideal`

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^2 + 5)
            sage: b = (1+a)/2
            sage: b.norm()
            3/2
            sage: D = b.denominator_ideal(); D
            Fractional ideal (2, a + 1)
            sage: D.norm()
            2
            sage: (1/b).denominator_ideal()
            Fractional ideal (3, a + 1)
            sage: K(0).denominator_ideal()
            Fractional ideal (1)"""
    @overload
    def denominator_ideal(self) -> Any:
        """NumberFieldElement.denominator_ideal(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 4229)

        Return the denominator ideal of this number field element.

        The denominator ideal of a number field element `a` is the
        integral ideal consisting of all elements of the ring of
        integers `R` whose product with `a` is also in `R`.

        .. SEEALSO::

            :meth:`numerator_ideal`

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^2 + 5)
            sage: b = (1+a)/2
            sage: b.norm()
            3/2
            sage: D = b.denominator_ideal(); D
            Fractional ideal (2, a + 1)
            sage: D.norm()
            2
            sage: (1/b).denominator_ideal()
            Fractional ideal (3, a + 1)
            sage: K(0).denominator_ideal()
            Fractional ideal (1)"""
    @overload
    def denominator_ideal(self) -> Any:
        """NumberFieldElement.denominator_ideal(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 4229)

        Return the denominator ideal of this number field element.

        The denominator ideal of a number field element `a` is the
        integral ideal consisting of all elements of the ring of
        integers `R` whose product with `a` is also in `R`.

        .. SEEALSO::

            :meth:`numerator_ideal`

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^2 + 5)
            sage: b = (1+a)/2
            sage: b.norm()
            3/2
            sage: D = b.denominator_ideal(); D
            Fractional ideal (2, a + 1)
            sage: D.norm()
            2
            sage: (1/b).denominator_ideal()
            Fractional ideal (3, a + 1)
            sage: K(0).denominator_ideal()
            Fractional ideal (1)"""
    @overload
    def denominator_ideal(self) -> Any:
        """NumberFieldElement.denominator_ideal(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 4229)

        Return the denominator ideal of this number field element.

        The denominator ideal of a number field element `a` is the
        integral ideal consisting of all elements of the ring of
        integers `R` whose product with `a` is also in `R`.

        .. SEEALSO::

            :meth:`numerator_ideal`

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^2 + 5)
            sage: b = (1+a)/2
            sage: b.norm()
            3/2
            sage: D = b.denominator_ideal(); D
            Fractional ideal (2, a + 1)
            sage: D.norm()
            2
            sage: (1/b).denominator_ideal()
            Fractional ideal (3, a + 1)
            sage: K(0).denominator_ideal()
            Fractional ideal (1)"""
    def descend_mod_power(self, K=..., d=...) -> Any:
        """NumberFieldElement.descend_mod_power(self, K=QQ, d=2)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 4490)

        Return a list of elements of the subfield `K` equal to
        ``self`` modulo `d`-th powers.

        INPUT:

        - ``K`` -- number field (default: `\\QQ`); a subfield of the
          parent number field `L` of ``self``

        - ``d`` -- positive integer (default: 2); an integer at least 2

        OUTPUT:

        A list, possibly empty, of elements of `K` equal to ``self``
        modulo `d`-th powers, i.e. the preimages of ``self`` under the
        map `K^*/(K^*)^d \\rightarrow L^*/(L^*)^d` where `L` is the
        parent of ``self``.  A :exc:`ValueError` is raised if `K` does
        not embed into `L`.

        ALGORITHM:

        All preimages must lie in the Selmer group `K(S,d)` for a
        suitable finite set of primes `S`, which reduces the question
        to a finite set of possibilities.  We may take `S` to be the
        set of primes which ramify in `L` together with those for
        which the valuation of ``self`` is not divisible by `d`.

        EXAMPLES:

        A relative example::

            sage: Qi.<i> = QuadraticField(-1)
            sage: K.<zeta> = CyclotomicField(8)
            sage: f = Qi.embeddings(K)[0]
            sage: a = f(2+3*i) * (2-zeta)^2
            sage: a.descend_mod_power(Qi,2)
            [3*i + 2, 2*i - 3]

        An absolute example::

            sage: K.<zeta> = CyclotomicField(8)
            sage: K(1).descend_mod_power(QQ,2)
            [1, 2, -1, -2]
            sage: a = 17 * K._random_nonzero_element()^2
            sage: a.descend_mod_power(QQ,2)
            [17, 34, -17, -34]"""
    def different(self, K=...) -> Any:
        """NumberFieldElement.different(self, K=None)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 4578)

        Return the different of this element with respect to the given
        base field.

        The different of an element `a` in an extension of number fields `L/K`
        is defined as `\\mathrm{Diff}_{L/K}(a) = f'(a)` where `f` is the
        characteristic polynomial of `a` over `K`.

        INPUT:

        - ``K`` -- a subfield (embedding of a subfield) of the parent
          number field of ``self``. Default: ``None``, which will amount
          to ``self.parent().base_field()``.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^3 - 2)
            sage: a.different()
            3*a^2
            sage: a.different(K=K)
            1

        The optional argument ``K`` can be an embedding of a subfield::

            sage: K.<b> = NumberField(x^4 - 2)
            sage: (b^2).different()
            0
            sage: phi = K.base_field().embeddings(K)[0]
            sage: b.different(K=phi)
            4*b^3

        Compare the relative different and the absolute different
        for an element in a relative number field::

            sage: K.<a> = NumberFieldTower([x^2 - 17, x^3 - 2])
            sage: a.different()
            2*a0
            sage: a.different(K=QQ)
            0
            sage: a.absolute_different()
            0

        Observe that for the field extension `\\QQ(i)/\\QQ`, the different of
        the field extension is the ideal generated by the different of `i`::


            sage: K.<c> = NumberField(x^2 + 1)
            sage: K.different() == K.ideal(c.different())
            True

        .. SEEALSO::

            :meth:`absolute_different`
            :meth:`sage.rings.number_field.number_field_rel.NumberField_relative.different`"""
    @overload
    def factor(self) -> Any:
        """NumberFieldElement.factor(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 1975)

        Return factorization of this element into prime elements and a unit.

        OUTPUT:

        (:class:`Factorization`) If all the prime ideals in the support are
        principal, the output is a :class:`Factorization` as a product of prime
        elements raised to appropriate powers, with an appropriate
        unit factor.

        Raise :exc:`ValueError` if the factorization of the
        ideal (``self``) contains a non-principal prime ideal.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<i> = NumberField(x^2 + 1)
            sage: (6*i + 6).factor()
            (i - 1)^3 * 3

        In the following example, the class number is 2.  If a factorization
        in prime elements exists, we will find it::

            sage: K.<a> = NumberField(x^2 - 10)
            sage: factor(169*a + 531)
            (-6*a - 19) * (2*a - 9) * (3*a + 1)
            sage: factor(K(3))
            Traceback (most recent call last):
            ...
            ArithmeticError: non-principal ideal in factorization

        Factorization of 0 is not allowed::

            sage: K.<i> = QuadraticField(-1)
            sage: K(0).factor()
            Traceback (most recent call last):
            ...
            ArithmeticError: factorization of 0 is not defined"""
    @overload
    def factor(self) -> Any:
        """NumberFieldElement.factor(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 1975)

        Return factorization of this element into prime elements and a unit.

        OUTPUT:

        (:class:`Factorization`) If all the prime ideals in the support are
        principal, the output is a :class:`Factorization` as a product of prime
        elements raised to appropriate powers, with an appropriate
        unit factor.

        Raise :exc:`ValueError` if the factorization of the
        ideal (``self``) contains a non-principal prime ideal.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<i> = NumberField(x^2 + 1)
            sage: (6*i + 6).factor()
            (i - 1)^3 * 3

        In the following example, the class number is 2.  If a factorization
        in prime elements exists, we will find it::

            sage: K.<a> = NumberField(x^2 - 10)
            sage: factor(169*a + 531)
            (-6*a - 19) * (2*a - 9) * (3*a + 1)
            sage: factor(K(3))
            Traceback (most recent call last):
            ...
            ArithmeticError: non-principal ideal in factorization

        Factorization of 0 is not allowed::

            sage: K.<i> = QuadraticField(-1)
            sage: K(0).factor()
            Traceback (most recent call last):
            ...
            ArithmeticError: factorization of 0 is not defined"""
    @overload
    def factor(self) -> Any:
        """NumberFieldElement.factor(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 1975)

        Return factorization of this element into prime elements and a unit.

        OUTPUT:

        (:class:`Factorization`) If all the prime ideals in the support are
        principal, the output is a :class:`Factorization` as a product of prime
        elements raised to appropriate powers, with an appropriate
        unit factor.

        Raise :exc:`ValueError` if the factorization of the
        ideal (``self``) contains a non-principal prime ideal.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<i> = NumberField(x^2 + 1)
            sage: (6*i + 6).factor()
            (i - 1)^3 * 3

        In the following example, the class number is 2.  If a factorization
        in prime elements exists, we will find it::

            sage: K.<a> = NumberField(x^2 - 10)
            sage: factor(169*a + 531)
            (-6*a - 19) * (2*a - 9) * (3*a + 1)
            sage: factor(K(3))
            Traceback (most recent call last):
            ...
            ArithmeticError: non-principal ideal in factorization

        Factorization of 0 is not allowed::

            sage: K.<i> = QuadraticField(-1)
            sage: K(0).factor()
            Traceback (most recent call last):
            ...
            ArithmeticError: factorization of 0 is not defined"""
    @overload
    def floor(self) -> Any:
        """NumberFieldElement.floor(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 1103)

        Return the floor of this number field element.

        EXAMPLES::

            sage: x = polygen(ZZ)
            sage: p = x**7 - 5*x**2 + x + 1
            sage: a_AA = AA.polynomial_root(p, RIF(1,2))
            sage: K.<a> = NumberField(p, embedding=a_AA)
            sage: b = a**5 + a/2 - 1/7
            sage: RR(b)
            4.13444473767055
            sage: b.floor()
            4

            sage: K(125/7).floor()
            17

        This function always succeeds even if a tremendous precision is needed::

            sage: c = b - 4772404052447/1154303505127 + 2
            sage: c.floor()
            1
            sage: RIF(c).unique_floor()
            Traceback (most recent call last):
            ...
            ValueError: interval does not have a unique floor

        If the number field is not embedded, this function is valid only if the
        element is rational::

            sage: p = x**5 - 3
            sage: K.<a> = NumberField(p)
            sage: K(2/3).floor()
            0
            sage: a.floor()
            Traceback (most recent call last):
            ...
            TypeError: floor not uniquely defined since no real embedding is specified"""
    @overload
    def floor(self) -> Any:
        """NumberFieldElement.floor(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 1103)

        Return the floor of this number field element.

        EXAMPLES::

            sage: x = polygen(ZZ)
            sage: p = x**7 - 5*x**2 + x + 1
            sage: a_AA = AA.polynomial_root(p, RIF(1,2))
            sage: K.<a> = NumberField(p, embedding=a_AA)
            sage: b = a**5 + a/2 - 1/7
            sage: RR(b)
            4.13444473767055
            sage: b.floor()
            4

            sage: K(125/7).floor()
            17

        This function always succeeds even if a tremendous precision is needed::

            sage: c = b - 4772404052447/1154303505127 + 2
            sage: c.floor()
            1
            sage: RIF(c).unique_floor()
            Traceback (most recent call last):
            ...
            ValueError: interval does not have a unique floor

        If the number field is not embedded, this function is valid only if the
        element is rational::

            sage: p = x**5 - 3
            sage: K.<a> = NumberField(p)
            sage: K(2/3).floor()
            0
            sage: a.floor()
            Traceback (most recent call last):
            ...
            TypeError: floor not uniquely defined since no real embedding is specified"""
    @overload
    def floor(self) -> Any:
        """NumberFieldElement.floor(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 1103)

        Return the floor of this number field element.

        EXAMPLES::

            sage: x = polygen(ZZ)
            sage: p = x**7 - 5*x**2 + x + 1
            sage: a_AA = AA.polynomial_root(p, RIF(1,2))
            sage: K.<a> = NumberField(p, embedding=a_AA)
            sage: b = a**5 + a/2 - 1/7
            sage: RR(b)
            4.13444473767055
            sage: b.floor()
            4

            sage: K(125/7).floor()
            17

        This function always succeeds even if a tremendous precision is needed::

            sage: c = b - 4772404052447/1154303505127 + 2
            sage: c.floor()
            1
            sage: RIF(c).unique_floor()
            Traceback (most recent call last):
            ...
            ValueError: interval does not have a unique floor

        If the number field is not embedded, this function is valid only if the
        element is rational::

            sage: p = x**5 - 3
            sage: K.<a> = NumberField(p)
            sage: K(2/3).floor()
            0
            sage: a.floor()
            Traceback (most recent call last):
            ...
            TypeError: floor not uniquely defined since no real embedding is specified"""
    @overload
    def floor(self) -> Any:
        """NumberFieldElement.floor(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 1103)

        Return the floor of this number field element.

        EXAMPLES::

            sage: x = polygen(ZZ)
            sage: p = x**7 - 5*x**2 + x + 1
            sage: a_AA = AA.polynomial_root(p, RIF(1,2))
            sage: K.<a> = NumberField(p, embedding=a_AA)
            sage: b = a**5 + a/2 - 1/7
            sage: RR(b)
            4.13444473767055
            sage: b.floor()
            4

            sage: K(125/7).floor()
            17

        This function always succeeds even if a tremendous precision is needed::

            sage: c = b - 4772404052447/1154303505127 + 2
            sage: c.floor()
            1
            sage: RIF(c).unique_floor()
            Traceback (most recent call last):
            ...
            ValueError: interval does not have a unique floor

        If the number field is not embedded, this function is valid only if the
        element is rational::

            sage: p = x**5 - 3
            sage: K.<a> = NumberField(p)
            sage: K(2/3).floor()
            0
            sage: a.floor()
            Traceback (most recent call last):
            ...
            TypeError: floor not uniquely defined since no real embedding is specified"""
    @overload
    def floor(self) -> Any:
        """NumberFieldElement.floor(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 1103)

        Return the floor of this number field element.

        EXAMPLES::

            sage: x = polygen(ZZ)
            sage: p = x**7 - 5*x**2 + x + 1
            sage: a_AA = AA.polynomial_root(p, RIF(1,2))
            sage: K.<a> = NumberField(p, embedding=a_AA)
            sage: b = a**5 + a/2 - 1/7
            sage: RR(b)
            4.13444473767055
            sage: b.floor()
            4

            sage: K(125/7).floor()
            17

        This function always succeeds even if a tremendous precision is needed::

            sage: c = b - 4772404052447/1154303505127 + 2
            sage: c.floor()
            1
            sage: RIF(c).unique_floor()
            Traceback (most recent call last):
            ...
            ValueError: interval does not have a unique floor

        If the number field is not embedded, this function is valid only if the
        element is rational::

            sage: p = x**5 - 3
            sage: K.<a> = NumberField(p)
            sage: K(2/3).floor()
            0
            sage: a.floor()
            Traceback (most recent call last):
            ...
            TypeError: floor not uniquely defined since no real embedding is specified"""
    @overload
    def floor(self) -> Any:
        """NumberFieldElement.floor(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 1103)

        Return the floor of this number field element.

        EXAMPLES::

            sage: x = polygen(ZZ)
            sage: p = x**7 - 5*x**2 + x + 1
            sage: a_AA = AA.polynomial_root(p, RIF(1,2))
            sage: K.<a> = NumberField(p, embedding=a_AA)
            sage: b = a**5 + a/2 - 1/7
            sage: RR(b)
            4.13444473767055
            sage: b.floor()
            4

            sage: K(125/7).floor()
            17

        This function always succeeds even if a tremendous precision is needed::

            sage: c = b - 4772404052447/1154303505127 + 2
            sage: c.floor()
            1
            sage: RIF(c).unique_floor()
            Traceback (most recent call last):
            ...
            ValueError: interval does not have a unique floor

        If the number field is not embedded, this function is valid only if the
        element is rational::

            sage: p = x**5 - 3
            sage: K.<a> = NumberField(p)
            sage: K(2/3).floor()
            0
            sage: a.floor()
            Traceback (most recent call last):
            ...
            TypeError: floor not uniquely defined since no real embedding is specified"""
    @overload
    def galois_conjugates(self, K) -> Any:
        """NumberFieldElement.galois_conjugates(self, K)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 3040)

        Return all Gal(Qbar/Q)-conjugates of this number field element in
        the field `K`.

        EXAMPLES:

        In the first example the conjugates are obvious::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^2 - 2)
            sage: a.galois_conjugates(K)
            [a, -a]
            sage: K(3).galois_conjugates(K)
            [3]

        In this example the field is not Galois, so we have to pass to an
        extension to obtain the Galois conjugates.

        ::

            sage: K.<a> = NumberField(x^3 - 2)
            sage: c = a.galois_conjugates(K); c
            [a]
            sage: K.<a> = NumberField(x^3 - 2)
            sage: c = a.galois_conjugates(K.galois_closure('a1')); c                    # needs sage.groups
            [1/18*a1^4, -1/36*a1^4 + 1/2*a1, -1/36*a1^4 - 1/2*a1]
            sage: c[0]^3
            2
            sage: parent(c[0])
            Number Field in a1 with defining polynomial x^6 + 108
            sage: parent(c[0]).is_galois()                                              # needs sage.groups
            True

        There is only one Galois conjugate of `\\sqrt[3]{2}` in
        `\\QQ(\\sqrt[3]{2})`.

        ::

            sage: a.galois_conjugates(K)
            [a]

        Galois conjugates of `\\sqrt[3]{2}` in the field
        `\\QQ(\\zeta_3,\\sqrt[3]{2})`::

            sage: L.<a> = CyclotomicField(3).extension(x^3 - 2)
            sage: a.galois_conjugates(L)
            [a, (-zeta3 - 1)*a, zeta3*a]"""
    @overload
    def galois_conjugates(self, K) -> Any:
        """NumberFieldElement.galois_conjugates(self, K)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 3040)

        Return all Gal(Qbar/Q)-conjugates of this number field element in
        the field `K`.

        EXAMPLES:

        In the first example the conjugates are obvious::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^2 - 2)
            sage: a.galois_conjugates(K)
            [a, -a]
            sage: K(3).galois_conjugates(K)
            [3]

        In this example the field is not Galois, so we have to pass to an
        extension to obtain the Galois conjugates.

        ::

            sage: K.<a> = NumberField(x^3 - 2)
            sage: c = a.galois_conjugates(K); c
            [a]
            sage: K.<a> = NumberField(x^3 - 2)
            sage: c = a.galois_conjugates(K.galois_closure('a1')); c                    # needs sage.groups
            [1/18*a1^4, -1/36*a1^4 + 1/2*a1, -1/36*a1^4 - 1/2*a1]
            sage: c[0]^3
            2
            sage: parent(c[0])
            Number Field in a1 with defining polynomial x^6 + 108
            sage: parent(c[0]).is_galois()                                              # needs sage.groups
            True

        There is only one Galois conjugate of `\\sqrt[3]{2}` in
        `\\QQ(\\sqrt[3]{2})`.

        ::

            sage: a.galois_conjugates(K)
            [a]

        Galois conjugates of `\\sqrt[3]{2}` in the field
        `\\QQ(\\zeta_3,\\sqrt[3]{2})`::

            sage: L.<a> = CyclotomicField(3).extension(x^3 - 2)
            sage: a.galois_conjugates(L)
            [a, (-zeta3 - 1)*a, zeta3*a]"""
    @overload
    def galois_conjugates(self, K) -> Any:
        """NumberFieldElement.galois_conjugates(self, K)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 3040)

        Return all Gal(Qbar/Q)-conjugates of this number field element in
        the field `K`.

        EXAMPLES:

        In the first example the conjugates are obvious::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^2 - 2)
            sage: a.galois_conjugates(K)
            [a, -a]
            sage: K(3).galois_conjugates(K)
            [3]

        In this example the field is not Galois, so we have to pass to an
        extension to obtain the Galois conjugates.

        ::

            sage: K.<a> = NumberField(x^3 - 2)
            sage: c = a.galois_conjugates(K); c
            [a]
            sage: K.<a> = NumberField(x^3 - 2)
            sage: c = a.galois_conjugates(K.galois_closure('a1')); c                    # needs sage.groups
            [1/18*a1^4, -1/36*a1^4 + 1/2*a1, -1/36*a1^4 - 1/2*a1]
            sage: c[0]^3
            2
            sage: parent(c[0])
            Number Field in a1 with defining polynomial x^6 + 108
            sage: parent(c[0]).is_galois()                                              # needs sage.groups
            True

        There is only one Galois conjugate of `\\sqrt[3]{2}` in
        `\\QQ(\\sqrt[3]{2})`.

        ::

            sage: a.galois_conjugates(K)
            [a]

        Galois conjugates of `\\sqrt[3]{2}` in the field
        `\\QQ(\\zeta_3,\\sqrt[3]{2})`::

            sage: L.<a> = CyclotomicField(3).extension(x^3 - 2)
            sage: a.galois_conjugates(L)
            [a, (-zeta3 - 1)*a, zeta3*a]"""
    @overload
    def galois_conjugates(self, K) -> Any:
        """NumberFieldElement.galois_conjugates(self, K)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 3040)

        Return all Gal(Qbar/Q)-conjugates of this number field element in
        the field `K`.

        EXAMPLES:

        In the first example the conjugates are obvious::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^2 - 2)
            sage: a.galois_conjugates(K)
            [a, -a]
            sage: K(3).galois_conjugates(K)
            [3]

        In this example the field is not Galois, so we have to pass to an
        extension to obtain the Galois conjugates.

        ::

            sage: K.<a> = NumberField(x^3 - 2)
            sage: c = a.galois_conjugates(K); c
            [a]
            sage: K.<a> = NumberField(x^3 - 2)
            sage: c = a.galois_conjugates(K.galois_closure('a1')); c                    # needs sage.groups
            [1/18*a1^4, -1/36*a1^4 + 1/2*a1, -1/36*a1^4 - 1/2*a1]
            sage: c[0]^3
            2
            sage: parent(c[0])
            Number Field in a1 with defining polynomial x^6 + 108
            sage: parent(c[0]).is_galois()                                              # needs sage.groups
            True

        There is only one Galois conjugate of `\\sqrt[3]{2}` in
        `\\QQ(\\sqrt[3]{2})`.

        ::

            sage: a.galois_conjugates(K)
            [a]

        Galois conjugates of `\\sqrt[3]{2}` in the field
        `\\QQ(\\zeta_3,\\sqrt[3]{2})`::

            sage: L.<a> = CyclotomicField(3).extension(x^3 - 2)
            sage: a.galois_conjugates(L)
            [a, (-zeta3 - 1)*a, zeta3*a]"""
    def gcd(self, other) -> Any:
        """NumberFieldElement.gcd(self, other)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 2057)

        Return the greatest common divisor of ``self`` and ``other``.

        INPUT:

        - ``self``, ``other`` -- elements of a number field or maximal order

        OUTPUT:

        A generator of the ideal ``(self, other)``. If the parent is
        a number field, this always returns 0 or 1. For maximal orders,
        this raises :exc:`ArithmeticError` if the ideal is not principal.

        EXAMPLES::

            sage: K.<i> = QuadraticField(-1)
            sage: (i+1).gcd(2)
            1
            sage: K(1).gcd(0)
            1
            sage: K(0).gcd(0)
            0
            sage: R = K.maximal_order()
            sage: R(i+1).gcd(2)
            i - 1
            sage: R = K.order(2*i)
            sage: R(1).gcd(R(4*i))
            1

        The following field has class number 3, but if the ideal
        ``(self, other)`` happens to be principal, this still works::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^3 - 7)
            sage: K.class_number()
            3
            sage: a.gcd(7)
            1
            sage: R = K.maximal_order()
            sage: R(a).gcd(7)
            a
            sage: R(a+1).gcd(2)
            Traceback (most recent call last):
            ...
            ArithmeticError: ideal (a + 1, 2) is not principal, gcd is not defined
            sage: R(2*a - a^2).gcd(0)
            a
            sage: R(a).gcd(R(2*a)).parent()
            Maximal Order generated by a in Number Field in a with defining polynomial x^3 - 7"""
    @overload
    def global_height(self, prec=...) -> Any:
        """NumberFieldElement.global_height(self, prec=None)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 4146)

        Return the absolute logarithmic height of this number field element.

        INPUT:

        - ``prec`` -- integer (default: default :class:`RealField` precision);
          desired floating point precision

        OUTPUT:

        (real) The absolute logarithmic height of this number field
        element; that is, the sum of the local heights at all finite
        and infinite places, scaled by the degree to make the result independent of
        the parent field.

        EXAMPLES::

            sage: R.<x> = QQ[]
            sage: K.<a> = NumberField(x^4 + 3*x^2 - 17)
            sage: b = a/2
            sage: b.global_height()
            0.789780699008...
            sage: b.global_height(prec=200)
            0.78978069900813892060267152032141577237037181070060784564457

        The global height of an algebraic number is absolute, i.e. it
        does not depend on the parent field::

            sage: QQ(6).global_height()
            1.79175946922805
            sage: K(6).global_height()
            1.79175946922805

            sage: L.<b> = NumberField((a^2).minpoly())
            sage: L.degree()
            2
            sage: b.global_height() # element of L (degree 2 field)
            1.41660667202811
            sage: (a^2).global_height() # element of K (degree 4 field)
            1.41660667202811

        And of course every element has the same height as it's inverse::

            sage: K.<s> = QuadraticField(2)
            sage: s.global_height()
            0.346573590279973
            sage: (1/s).global_height()   #make sure that 11758 is fixed
            0.346573590279973"""
    @overload
    def global_height(self) -> Any:
        """NumberFieldElement.global_height(self, prec=None)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 4146)

        Return the absolute logarithmic height of this number field element.

        INPUT:

        - ``prec`` -- integer (default: default :class:`RealField` precision);
          desired floating point precision

        OUTPUT:

        (real) The absolute logarithmic height of this number field
        element; that is, the sum of the local heights at all finite
        and infinite places, scaled by the degree to make the result independent of
        the parent field.

        EXAMPLES::

            sage: R.<x> = QQ[]
            sage: K.<a> = NumberField(x^4 + 3*x^2 - 17)
            sage: b = a/2
            sage: b.global_height()
            0.789780699008...
            sage: b.global_height(prec=200)
            0.78978069900813892060267152032141577237037181070060784564457

        The global height of an algebraic number is absolute, i.e. it
        does not depend on the parent field::

            sage: QQ(6).global_height()
            1.79175946922805
            sage: K(6).global_height()
            1.79175946922805

            sage: L.<b> = NumberField((a^2).minpoly())
            sage: L.degree()
            2
            sage: b.global_height() # element of L (degree 2 field)
            1.41660667202811
            sage: (a^2).global_height() # element of K (degree 4 field)
            1.41660667202811

        And of course every element has the same height as it's inverse::

            sage: K.<s> = QuadraticField(2)
            sage: s.global_height()
            0.346573590279973
            sage: (1/s).global_height()   #make sure that 11758 is fixed
            0.346573590279973"""
    @overload
    def global_height(self, prec=...) -> Any:
        """NumberFieldElement.global_height(self, prec=None)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 4146)

        Return the absolute logarithmic height of this number field element.

        INPUT:

        - ``prec`` -- integer (default: default :class:`RealField` precision);
          desired floating point precision

        OUTPUT:

        (real) The absolute logarithmic height of this number field
        element; that is, the sum of the local heights at all finite
        and infinite places, scaled by the degree to make the result independent of
        the parent field.

        EXAMPLES::

            sage: R.<x> = QQ[]
            sage: K.<a> = NumberField(x^4 + 3*x^2 - 17)
            sage: b = a/2
            sage: b.global_height()
            0.789780699008...
            sage: b.global_height(prec=200)
            0.78978069900813892060267152032141577237037181070060784564457

        The global height of an algebraic number is absolute, i.e. it
        does not depend on the parent field::

            sage: QQ(6).global_height()
            1.79175946922805
            sage: K(6).global_height()
            1.79175946922805

            sage: L.<b> = NumberField((a^2).minpoly())
            sage: L.degree()
            2
            sage: b.global_height() # element of L (degree 2 field)
            1.41660667202811
            sage: (a^2).global_height() # element of K (degree 4 field)
            1.41660667202811

        And of course every element has the same height as it's inverse::

            sage: K.<s> = QuadraticField(2)
            sage: s.global_height()
            0.346573590279973
            sage: (1/s).global_height()   #make sure that 11758 is fixed
            0.346573590279973"""
    @overload
    def global_height(self) -> Any:
        """NumberFieldElement.global_height(self, prec=None)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 4146)

        Return the absolute logarithmic height of this number field element.

        INPUT:

        - ``prec`` -- integer (default: default :class:`RealField` precision);
          desired floating point precision

        OUTPUT:

        (real) The absolute logarithmic height of this number field
        element; that is, the sum of the local heights at all finite
        and infinite places, scaled by the degree to make the result independent of
        the parent field.

        EXAMPLES::

            sage: R.<x> = QQ[]
            sage: K.<a> = NumberField(x^4 + 3*x^2 - 17)
            sage: b = a/2
            sage: b.global_height()
            0.789780699008...
            sage: b.global_height(prec=200)
            0.78978069900813892060267152032141577237037181070060784564457

        The global height of an algebraic number is absolute, i.e. it
        does not depend on the parent field::

            sage: QQ(6).global_height()
            1.79175946922805
            sage: K(6).global_height()
            1.79175946922805

            sage: L.<b> = NumberField((a^2).minpoly())
            sage: L.degree()
            2
            sage: b.global_height() # element of L (degree 2 field)
            1.41660667202811
            sage: (a^2).global_height() # element of K (degree 4 field)
            1.41660667202811

        And of course every element has the same height as it's inverse::

            sage: K.<s> = QuadraticField(2)
            sage: s.global_height()
            0.346573590279973
            sage: (1/s).global_height()   #make sure that 11758 is fixed
            0.346573590279973"""
    @overload
    def global_height(self) -> Any:
        """NumberFieldElement.global_height(self, prec=None)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 4146)

        Return the absolute logarithmic height of this number field element.

        INPUT:

        - ``prec`` -- integer (default: default :class:`RealField` precision);
          desired floating point precision

        OUTPUT:

        (real) The absolute logarithmic height of this number field
        element; that is, the sum of the local heights at all finite
        and infinite places, scaled by the degree to make the result independent of
        the parent field.

        EXAMPLES::

            sage: R.<x> = QQ[]
            sage: K.<a> = NumberField(x^4 + 3*x^2 - 17)
            sage: b = a/2
            sage: b.global_height()
            0.789780699008...
            sage: b.global_height(prec=200)
            0.78978069900813892060267152032141577237037181070060784564457

        The global height of an algebraic number is absolute, i.e. it
        does not depend on the parent field::

            sage: QQ(6).global_height()
            1.79175946922805
            sage: K(6).global_height()
            1.79175946922805

            sage: L.<b> = NumberField((a^2).minpoly())
            sage: L.degree()
            2
            sage: b.global_height() # element of L (degree 2 field)
            1.41660667202811
            sage: (a^2).global_height() # element of K (degree 4 field)
            1.41660667202811

        And of course every element has the same height as it's inverse::

            sage: K.<s> = QuadraticField(2)
            sage: s.global_height()
            0.346573590279973
            sage: (1/s).global_height()   #make sure that 11758 is fixed
            0.346573590279973"""
    @overload
    def global_height(self) -> Any:
        """NumberFieldElement.global_height(self, prec=None)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 4146)

        Return the absolute logarithmic height of this number field element.

        INPUT:

        - ``prec`` -- integer (default: default :class:`RealField` precision);
          desired floating point precision

        OUTPUT:

        (real) The absolute logarithmic height of this number field
        element; that is, the sum of the local heights at all finite
        and infinite places, scaled by the degree to make the result independent of
        the parent field.

        EXAMPLES::

            sage: R.<x> = QQ[]
            sage: K.<a> = NumberField(x^4 + 3*x^2 - 17)
            sage: b = a/2
            sage: b.global_height()
            0.789780699008...
            sage: b.global_height(prec=200)
            0.78978069900813892060267152032141577237037181070060784564457

        The global height of an algebraic number is absolute, i.e. it
        does not depend on the parent field::

            sage: QQ(6).global_height()
            1.79175946922805
            sage: K(6).global_height()
            1.79175946922805

            sage: L.<b> = NumberField((a^2).minpoly())
            sage: L.degree()
            2
            sage: b.global_height() # element of L (degree 2 field)
            1.41660667202811
            sage: (a^2).global_height() # element of K (degree 4 field)
            1.41660667202811

        And of course every element has the same height as it's inverse::

            sage: K.<s> = QuadraticField(2)
            sage: s.global_height()
            0.346573590279973
            sage: (1/s).global_height()   #make sure that 11758 is fixed
            0.346573590279973"""
    @overload
    def global_height(self) -> Any:
        """NumberFieldElement.global_height(self, prec=None)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 4146)

        Return the absolute logarithmic height of this number field element.

        INPUT:

        - ``prec`` -- integer (default: default :class:`RealField` precision);
          desired floating point precision

        OUTPUT:

        (real) The absolute logarithmic height of this number field
        element; that is, the sum of the local heights at all finite
        and infinite places, scaled by the degree to make the result independent of
        the parent field.

        EXAMPLES::

            sage: R.<x> = QQ[]
            sage: K.<a> = NumberField(x^4 + 3*x^2 - 17)
            sage: b = a/2
            sage: b.global_height()
            0.789780699008...
            sage: b.global_height(prec=200)
            0.78978069900813892060267152032141577237037181070060784564457

        The global height of an algebraic number is absolute, i.e. it
        does not depend on the parent field::

            sage: QQ(6).global_height()
            1.79175946922805
            sage: K(6).global_height()
            1.79175946922805

            sage: L.<b> = NumberField((a^2).minpoly())
            sage: L.degree()
            2
            sage: b.global_height() # element of L (degree 2 field)
            1.41660667202811
            sage: (a^2).global_height() # element of K (degree 4 field)
            1.41660667202811

        And of course every element has the same height as it's inverse::

            sage: K.<s> = QuadraticField(2)
            sage: s.global_height()
            0.346573590279973
            sage: (1/s).global_height()   #make sure that 11758 is fixed
            0.346573590279973"""
    @overload
    def global_height_arch(self, prec=...) -> Any:
        """NumberFieldElement.global_height_arch(self, prec=None)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 4119)

        Return the total archimedean component of the height of ``self``.

        INPUT:

        - ``prec`` -- integer (default: default :class:`RealField` precision);
          desired floating point precision

        OUTPUT:

        (real) The total archimedean component of the height of
        this number field element; that is, the sum of the local
        heights at all infinite places.

        EXAMPLES::

            sage: R.<x> = QQ[]
            sage: K.<a> = NumberField(x^4 + 3*x^2 - 17)
            sage: b = a/2
            sage: b.global_height_arch()
            0.38653407379277..."""
    @overload
    def global_height_arch(self) -> Any:
        """NumberFieldElement.global_height_arch(self, prec=None)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 4119)

        Return the total archimedean component of the height of ``self``.

        INPUT:

        - ``prec`` -- integer (default: default :class:`RealField` precision);
          desired floating point precision

        OUTPUT:

        (real) The total archimedean component of the height of
        this number field element; that is, the sum of the local
        heights at all infinite places.

        EXAMPLES::

            sage: R.<x> = QQ[]
            sage: K.<a> = NumberField(x^4 + 3*x^2 - 17)
            sage: b = a/2
            sage: b.global_height_arch()
            0.38653407379277..."""
    def global_height_non_arch(self, prec=...) -> Any:
        """NumberFieldElement.global_height_non_arch(self, prec=None)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 4065)

        Return the total non-archimedean component of the height of ``self``.

        INPUT:

        - ``prec`` -- integer (default: default RealField precision); desired
          floating point precision

        OUTPUT:

        (real) The total non-archimedean component of the height of
        this number field element; that is, the sum of the local
        heights at all finite places, weighted by the local degrees.

        ALGORITHM:

        An alternative formula is `\\log(d)` where `d` is the norm of
        the denominator ideal; this is used to avoid factorization.

        EXAMPLES::

            sage: R.<x> = QQ[]
            sage: K.<a> = NumberField(x^4 + 3*x^2 - 17)
            sage: b = a/6
            sage: b.global_height_non_arch()
            7.16703787691222

        Check that this is equal to the sum of the non-archimedean
        local heights::

            sage: [b.local_height(P) for P in b.support()]
            [0.000000000000000, 0.693147180559945, 1.09861228866811, 1.09861228866811]
            sage: [b.local_height(P, weighted=True) for P in b.support()]
            [0.000000000000000, 2.77258872223978, 2.19722457733622, 2.19722457733622]
            sage: sum([b.local_height(P,weighted=True) for P in b.support()])
            7.16703787691222

        A relative example::

            sage: PK.<y> = K[]
            sage: L.<c> = NumberField(y^2 + a)
            sage: (c/10).global_height_non_arch()
            18.4206807439524"""
    def inverse_mod(self, I) -> Any:
        """NumberFieldElement.inverse_mod(self, I)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 4383)

        Return the inverse of ``self`` mod the integral ideal `I`.

        INPUT:

        - ``I`` -- may be an ideal of ``self.parent()``, or an element or list
          of elements of ``self.parent()`` generating a nonzero ideal. A
          :exc:`ValueError` is raised if `I` is non-integral or zero. A
          :exc:`ZeroDivisionError` is raised if `I + (x) \\neq (1)`.

        .. NOTE::

            It's not implemented yet for non-integral elements.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: k.<a> = NumberField(x^2 + 23)
            sage: N = k.ideal(3)
            sage: d = 3*a + 1
            sage: d.inverse_mod(N)
            1

        ::

            sage: k.<a> = NumberField(x^3 + 11)
            sage: d = a + 13
            sage: d.inverse_mod(a^2)*d - 1 in k.ideal(a^2)
            True
            sage: d.inverse_mod((5, a + 1))*d - 1 in k.ideal(5, a + 1)
            True
            sage: K.<b> = k.extension(x^2 + 3)
            sage: b.inverse_mod([37, a - b])
            7
            sage: 7*b - 1 in K.ideal(37, a - b)
            True
            sage: b.inverse_mod([37, a - b]).parent() == K
            True"""
    @overload
    def is_integer(self) -> Any:
        """NumberFieldElement.is_integer(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 3471)

        Test whether this number field element is an integer.

        .. SEEALSO::

            - :meth:`is_rational` to test if this element is a rational number
            - :meth:`is_integral` to test if this element is an algebraic integer

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<cbrt3> = NumberField(x^3 - 3)
            sage: cbrt3.is_integer()
            False
            sage: (cbrt3**2 - cbrt3 + 2).is_integer()
            False
            sage: K(-12).is_integer()
            True
            sage: K(0).is_integer()
            True
            sage: K(1/2).is_integer()
            False"""
    @overload
    def is_integer(self) -> Any:
        """NumberFieldElement.is_integer(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 3471)

        Test whether this number field element is an integer.

        .. SEEALSO::

            - :meth:`is_rational` to test if this element is a rational number
            - :meth:`is_integral` to test if this element is an algebraic integer

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<cbrt3> = NumberField(x^3 - 3)
            sage: cbrt3.is_integer()
            False
            sage: (cbrt3**2 - cbrt3 + 2).is_integer()
            False
            sage: K(-12).is_integer()
            True
            sage: K(0).is_integer()
            True
            sage: K(1/2).is_integer()
            False"""
    @overload
    def is_integer(self) -> Any:
        """NumberFieldElement.is_integer(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 3471)

        Test whether this number field element is an integer.

        .. SEEALSO::

            - :meth:`is_rational` to test if this element is a rational number
            - :meth:`is_integral` to test if this element is an algebraic integer

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<cbrt3> = NumberField(x^3 - 3)
            sage: cbrt3.is_integer()
            False
            sage: (cbrt3**2 - cbrt3 + 2).is_integer()
            False
            sage: K(-12).is_integer()
            True
            sage: K(0).is_integer()
            True
            sage: K(1/2).is_integer()
            False"""
    @overload
    def is_integer(self) -> Any:
        """NumberFieldElement.is_integer(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 3471)

        Test whether this number field element is an integer.

        .. SEEALSO::

            - :meth:`is_rational` to test if this element is a rational number
            - :meth:`is_integral` to test if this element is an algebraic integer

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<cbrt3> = NumberField(x^3 - 3)
            sage: cbrt3.is_integer()
            False
            sage: (cbrt3**2 - cbrt3 + 2).is_integer()
            False
            sage: K(-12).is_integer()
            True
            sage: K(0).is_integer()
            True
            sage: K(1/2).is_integer()
            False"""
    @overload
    def is_integer(self) -> Any:
        """NumberFieldElement.is_integer(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 3471)

        Test whether this number field element is an integer.

        .. SEEALSO::

            - :meth:`is_rational` to test if this element is a rational number
            - :meth:`is_integral` to test if this element is an algebraic integer

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<cbrt3> = NumberField(x^3 - 3)
            sage: cbrt3.is_integer()
            False
            sage: (cbrt3**2 - cbrt3 + 2).is_integer()
            False
            sage: K(-12).is_integer()
            True
            sage: K(0).is_integer()
            True
            sage: K(1/2).is_integer()
            False"""
    @overload
    def is_integer(self) -> Any:
        """NumberFieldElement.is_integer(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 3471)

        Test whether this number field element is an integer.

        .. SEEALSO::

            - :meth:`is_rational` to test if this element is a rational number
            - :meth:`is_integral` to test if this element is an algebraic integer

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<cbrt3> = NumberField(x^3 - 3)
            sage: cbrt3.is_integer()
            False
            sage: (cbrt3**2 - cbrt3 + 2).is_integer()
            False
            sage: K(-12).is_integer()
            True
            sage: K(0).is_integer()
            True
            sage: K(1/2).is_integer()
            False"""
    @overload
    def is_integral(self) -> Any:
        """NumberFieldElement.is_integral(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 3713)

        Determine if a number is in the ring of integers of this number
        field.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^2 + 23)
            sage: a.is_integral()
            True
            sage: t = (1+a)/2
            sage: t.is_integral()
            True
            sage: t.minpoly()
            x^2 - x + 6
            sage: t = a/2
            sage: t.is_integral()
            False
            sage: t.minpoly()
            x^2 + 23/4

        An example in a relative extension::

            sage: K.<a,b> = NumberField([x^2 + 1, x^2 + 3])
            sage: (a + b).is_integral()
            True
            sage: ((a-b)/2).is_integral()
            False"""
    @overload
    def is_integral(self) -> Any:
        """NumberFieldElement.is_integral(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 3713)

        Determine if a number is in the ring of integers of this number
        field.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^2 + 23)
            sage: a.is_integral()
            True
            sage: t = (1+a)/2
            sage: t.is_integral()
            True
            sage: t.minpoly()
            x^2 - x + 6
            sage: t = a/2
            sage: t.is_integral()
            False
            sage: t.minpoly()
            x^2 + 23/4

        An example in a relative extension::

            sage: K.<a,b> = NumberField([x^2 + 1, x^2 + 3])
            sage: (a + b).is_integral()
            True
            sage: ((a-b)/2).is_integral()
            False"""
    @overload
    def is_integral(self) -> Any:
        """NumberFieldElement.is_integral(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 3713)

        Determine if a number is in the ring of integers of this number
        field.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^2 + 23)
            sage: a.is_integral()
            True
            sage: t = (1+a)/2
            sage: t.is_integral()
            True
            sage: t.minpoly()
            x^2 - x + 6
            sage: t = a/2
            sage: t.is_integral()
            False
            sage: t.minpoly()
            x^2 + 23/4

        An example in a relative extension::

            sage: K.<a,b> = NumberField([x^2 + 1, x^2 + 3])
            sage: (a + b).is_integral()
            True
            sage: ((a-b)/2).is_integral()
            False"""
    @overload
    def is_integral(self) -> Any:
        """NumberFieldElement.is_integral(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 3713)

        Determine if a number is in the ring of integers of this number
        field.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^2 + 23)
            sage: a.is_integral()
            True
            sage: t = (1+a)/2
            sage: t.is_integral()
            True
            sage: t.minpoly()
            x^2 - x + 6
            sage: t = a/2
            sage: t.is_integral()
            False
            sage: t.minpoly()
            x^2 + 23/4

        An example in a relative extension::

            sage: K.<a,b> = NumberField([x^2 + 1, x^2 + 3])
            sage: (a + b).is_integral()
            True
            sage: ((a-b)/2).is_integral()
            False"""
    @overload
    def is_integral(self) -> Any:
        """NumberFieldElement.is_integral(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 3713)

        Determine if a number is in the ring of integers of this number
        field.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^2 + 23)
            sage: a.is_integral()
            True
            sage: t = (1+a)/2
            sage: t.is_integral()
            True
            sage: t.minpoly()
            x^2 - x + 6
            sage: t = a/2
            sage: t.is_integral()
            False
            sage: t.minpoly()
            x^2 + 23/4

        An example in a relative extension::

            sage: K.<a,b> = NumberField([x^2 + 1, x^2 + 3])
            sage: (a + b).is_integral()
            True
            sage: ((a-b)/2).is_integral()
            False"""
    @overload
    def is_integral(self) -> Any:
        """NumberFieldElement.is_integral(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 3713)

        Determine if a number is in the ring of integers of this number
        field.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^2 + 23)
            sage: a.is_integral()
            True
            sage: t = (1+a)/2
            sage: t.is_integral()
            True
            sage: t.minpoly()
            x^2 - x + 6
            sage: t = a/2
            sage: t.is_integral()
            False
            sage: t.minpoly()
            x^2 + 23/4

        An example in a relative extension::

            sage: K.<a,b> = NumberField([x^2 + 1, x^2 + 3])
            sage: (a + b).is_integral()
            True
            sage: ((a-b)/2).is_integral()
            False"""
    def is_norm(self, L, element=..., proof=...) -> Any:
        """NumberFieldElement.is_norm(self, L, element=False, proof=True)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 1596)

        Determine whether ``self`` is the relative norm of an element
        of `L/K`, where `K` is ``self.parent()``.

        INPUT:

        - ``L`` -- a number field containing `K` = ``self.parent()``
        - ``element`` -- boolean; whether to also output an element
          of which ``self`` is a norm
        - ``proof`` -- if ``True``, then the output is correct unconditionally;
          if ``False``, then the output is correct under GRH

        OUTPUT:

        If ``element`` is ``False``, then the output is a boolean `B`, which is
        ``True`` if and only if ``self`` is the relative norm of an element of `L`
        to `K`.

        If ``element`` is ``True``, then the output is a pair `(B, x)`, where
        `B` is as above. If `B` is ``True``, then `x` is an element of `L` such that
        ``self == x.norm(K)``. Otherwise, `x` is ``None``.

        ALGORITHM:

        Uses PARI's :pari:`rnfisnorm`. See :meth:`_rnfisnorm`.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<beta> = NumberField(x^3 + 5)
            sage: Q.<X> = K[]
            sage: L = K.extension(X^2 + X + beta, 'gamma')
            sage: (beta/2).is_norm(L)
            False
            sage: beta.is_norm(L)
            True

        With a relative base field::

            sage: K.<a, b> = NumberField([x^2 - 2, x^2 - 3])
            sage: L.<c> = K.extension(x^2 - 5)
            sage: (2*a*b).is_norm(L)
            True
            sage: _, v = (2*b*a).is_norm(L, element=True)
            sage: v.norm(K) == 2*a*b
            True

        Non-Galois number fields::

            sage: K.<a> = NumberField(x^2 + x + 1)
            sage: Q.<X> = K[]
            sage: L.<b> = NumberField(X^4 + a + 2)
            sage: (a/4).is_norm(L)
            True
            sage: (a/2).is_norm(L)                                                      # needs sage.groups
            Traceback (most recent call last):
            ...
            NotImplementedError: is_norm is not implemented unconditionally
            for norms from non-Galois number fields
            sage: (a/2).is_norm(L, proof=False)                                         # needs sage.groups
            False

            sage: K.<a> = NumberField(x^3 + x + 1)
            sage: Q.<X> = K[]
            sage: L.<b> = NumberField(X^4 + a)
            sage: t, u = (-a).is_norm(L, element=True); u  # random (not unique)
            b^3 + 1
            sage: t and u.norm(K) == -a
            True

        Verify that :issue:`27469` has been fixed::

            sage: L.<z24> = CyclotomicField(24); L
            Cyclotomic Field of order 24 and degree 8
            sage: K = L.subfield(z24^3, 'z8')[0]; K
            Number Field in z8 with defining polynomial x^4 + 1
             with z8 = 0.7071067811865475? + 0.7071067811865475?*I
            sage: flag, c = K(-7).is_norm(K, element=True); flag
            True
            sage: c.norm(K)
            -7
            sage: c in L
            True

        AUTHORS:

        - Craig Citro (2008-04-05)

        - Marco Streng (2010-12-03)"""
    def is_nth_power(self, n) -> Any:
        """NumberFieldElement.is_nth_power(self, n)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 2356)

        Return ``True`` if ``self`` is an `n`-th power in its parent `K`.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^4 - 7)
            sage: K(7).is_nth_power(2)
            True
            sage: K(7).is_nth_power(4)
            True
            sage: K(7).is_nth_power(8)
            False
            sage: K((a-3)^5).is_nth_power(5)
            True

        ALGORITHM: Use PARI to factor `x^n` - ``self`` in `K`."""
    @overload
    def is_one(self) -> bool:
        """NumberFieldElement.is_one(self) -> bool

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 3423)

        Test whether this number field element is `1`.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^3 + 3)
            sage: K(1).is_one()
            True
            sage: K(0).is_one()
            False
            sage: K(-1).is_one()
            False
            sage: K(1/2).is_one()
            False
            sage: a.is_one()
            False"""
    @overload
    def is_one(self) -> Any:
        """NumberFieldElement.is_one(self) -> bool

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 3423)

        Test whether this number field element is `1`.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^3 + 3)
            sage: K(1).is_one()
            True
            sage: K(0).is_one()
            False
            sage: K(-1).is_one()
            False
            sage: K(1/2).is_one()
            False
            sage: a.is_one()
            False"""
    @overload
    def is_one(self) -> Any:
        """NumberFieldElement.is_one(self) -> bool

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 3423)

        Test whether this number field element is `1`.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^3 + 3)
            sage: K(1).is_one()
            True
            sage: K(0).is_one()
            False
            sage: K(-1).is_one()
            False
            sage: K(1/2).is_one()
            False
            sage: a.is_one()
            False"""
    @overload
    def is_one(self) -> Any:
        """NumberFieldElement.is_one(self) -> bool

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 3423)

        Test whether this number field element is `1`.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^3 + 3)
            sage: K(1).is_one()
            True
            sage: K(0).is_one()
            False
            sage: K(-1).is_one()
            False
            sage: K(1/2).is_one()
            False
            sage: a.is_one()
            False"""
    @overload
    def is_one(self) -> Any:
        """NumberFieldElement.is_one(self) -> bool

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 3423)

        Test whether this number field element is `1`.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^3 + 3)
            sage: K(1).is_one()
            True
            sage: K(0).is_one()
            False
            sage: K(-1).is_one()
            False
            sage: K(1/2).is_one()
            False
            sage: a.is_one()
            False"""
    @overload
    def is_one(self) -> Any:
        """NumberFieldElement.is_one(self) -> bool

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 3423)

        Test whether this number field element is `1`.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^3 + 3)
            sage: K(1).is_one()
            True
            sage: K(0).is_one()
            False
            sage: K(-1).is_one()
            False
            sage: K(1/2).is_one()
            False
            sage: a.is_one()
            False"""
    @overload
    def is_padic_square(self, P, check=...) -> Any:
        """NumberFieldElement.is_padic_square(self, P, check=True)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 2225)

        Return if ``self`` is a square in the completion at the prime `P`.

        INPUT:

        - ``P`` -- a prime ideal
        - ``check`` -- boolean (default: ``True``); check if `P` is prime

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^2 + 2)
            sage: p = K.primes_above(2)[0]
            sage: K(5).is_padic_square(p)
            False"""
    @overload
    def is_padic_square(self, p) -> Any:
        """NumberFieldElement.is_padic_square(self, P, check=True)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 2225)

        Return if ``self`` is a square in the completion at the prime `P`.

        INPUT:

        - ``P`` -- a prime ideal
        - ``check`` -- boolean (default: ``True``); check if `P` is prime

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^2 + 2)
            sage: p = K.primes_above(2)[0]
            sage: K(5).is_padic_square(p)
            False"""
    @overload
    def is_prime(self) -> Any:
        """NumberFieldElement.is_prime(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 2033)

        Test whether this number-field element is prime as
        an algebraic integer.

        Note that the behavior of this method differs from the behavior
        of :meth:`~sage.structure.element.RingElement.is_prime` in a
        general ring, according to which (number) fields would have no
        nonzero prime elements.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<i> = NumberField(x^2 + 1)
            sage: (1 + i).is_prime()
            True
            sage: ((1+i)/2).is_prime()
            False"""
    @overload
    def is_prime(self) -> Any:
        """NumberFieldElement.is_prime(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 2033)

        Test whether this number-field element is prime as
        an algebraic integer.

        Note that the behavior of this method differs from the behavior
        of :meth:`~sage.structure.element.RingElement.is_prime` in a
        general ring, according to which (number) fields would have no
        nonzero prime elements.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<i> = NumberField(x^2 + 1)
            sage: (1 + i).is_prime()
            True
            sage: ((1+i)/2).is_prime()
            False"""
    @overload
    def is_prime(self) -> Any:
        """NumberFieldElement.is_prime(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 2033)

        Test whether this number-field element is prime as
        an algebraic integer.

        Note that the behavior of this method differs from the behavior
        of :meth:`~sage.structure.element.RingElement.is_prime` in a
        general ring, according to which (number) fields would have no
        nonzero prime elements.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<i> = NumberField(x^2 + 1)
            sage: (1 + i).is_prime()
            True
            sage: ((1+i)/2).is_prime()
            False"""
    @overload
    def is_rational(self) -> bool:
        """NumberFieldElement.is_rational(self) -> bool

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 3445)

        Test whether this number field element is a rational number.

        .. SEEALSO::

            - :meth:`is_integer` to test if this element is an integer
            - :meth:`is_integral` to test if this element is an algebraic integer

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<cbrt3> = NumberField(x^3 - 3)
            sage: cbrt3.is_rational()
            False
            sage: (cbrt3**2 - cbrt3 + 1/2).is_rational()
            False
            sage: K(-12).is_rational()
            True
            sage: K(0).is_rational()
            True
            sage: K(1/2).is_rational()
            True"""
    @overload
    def is_rational(self) -> Any:
        """NumberFieldElement.is_rational(self) -> bool

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 3445)

        Test whether this number field element is a rational number.

        .. SEEALSO::

            - :meth:`is_integer` to test if this element is an integer
            - :meth:`is_integral` to test if this element is an algebraic integer

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<cbrt3> = NumberField(x^3 - 3)
            sage: cbrt3.is_rational()
            False
            sage: (cbrt3**2 - cbrt3 + 1/2).is_rational()
            False
            sage: K(-12).is_rational()
            True
            sage: K(0).is_rational()
            True
            sage: K(1/2).is_rational()
            True"""
    @overload
    def is_rational(self) -> Any:
        """NumberFieldElement.is_rational(self) -> bool

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 3445)

        Test whether this number field element is a rational number.

        .. SEEALSO::

            - :meth:`is_integer` to test if this element is an integer
            - :meth:`is_integral` to test if this element is an algebraic integer

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<cbrt3> = NumberField(x^3 - 3)
            sage: cbrt3.is_rational()
            False
            sage: (cbrt3**2 - cbrt3 + 1/2).is_rational()
            False
            sage: K(-12).is_rational()
            True
            sage: K(0).is_rational()
            True
            sage: K(1/2).is_rational()
            True"""
    @overload
    def is_rational(self) -> Any:
        """NumberFieldElement.is_rational(self) -> bool

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 3445)

        Test whether this number field element is a rational number.

        .. SEEALSO::

            - :meth:`is_integer` to test if this element is an integer
            - :meth:`is_integral` to test if this element is an algebraic integer

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<cbrt3> = NumberField(x^3 - 3)
            sage: cbrt3.is_rational()
            False
            sage: (cbrt3**2 - cbrt3 + 1/2).is_rational()
            False
            sage: K(-12).is_rational()
            True
            sage: K(0).is_rational()
            True
            sage: K(1/2).is_rational()
            True"""
    @overload
    def is_rational(self) -> Any:
        """NumberFieldElement.is_rational(self) -> bool

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 3445)

        Test whether this number field element is a rational number.

        .. SEEALSO::

            - :meth:`is_integer` to test if this element is an integer
            - :meth:`is_integral` to test if this element is an algebraic integer

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<cbrt3> = NumberField(x^3 - 3)
            sage: cbrt3.is_rational()
            False
            sage: (cbrt3**2 - cbrt3 + 1/2).is_rational()
            False
            sage: K(-12).is_rational()
            True
            sage: K(0).is_rational()
            True
            sage: K(1/2).is_rational()
            True"""
    @overload
    def is_rational(self) -> Any:
        """NumberFieldElement.is_rational(self) -> bool

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 3445)

        Test whether this number field element is a rational number.

        .. SEEALSO::

            - :meth:`is_integer` to test if this element is an integer
            - :meth:`is_integral` to test if this element is an algebraic integer

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<cbrt3> = NumberField(x^3 - 3)
            sage: cbrt3.is_rational()
            False
            sage: (cbrt3**2 - cbrt3 + 1/2).is_rational()
            False
            sage: K(-12).is_rational()
            True
            sage: K(0).is_rational()
            True
            sage: K(1/2).is_rational()
            True"""
    @overload
    def is_square(self, root=...) -> Any:
        """NumberFieldElement.is_square(self, root=False)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 2172)

        Return ``True`` if ``self`` is a square in its parent number field and
        otherwise return ``False``.

        INPUT:

        - ``root`` -- if ``True``, also return a square root (or ``None`` if
          ``self`` is not a perfect square)

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: m.<b> = NumberField(x^4 - 1789)
            sage: b.is_square()
            False
            sage: c = (2/3*b + 5)^2; c
            4/9*b^2 + 20/3*b + 25
            sage: c.is_square()
            True
            sage: c.is_square(True)
            (True, 2/3*b + 5)

        We also test the functional notation.

        ::

            sage: is_square(c, True)
            (True, 2/3*b + 5)
            sage: is_square(c)
            True
            sage: is_square(c + 1)
            False

        TESTS:

        Test that :issue:`16894` is fixed::

            sage: K.<a> = QuadraticField(22)
            sage: u = K.units()[0]
            sage: (u^14).is_square()
            True"""
    @overload
    def is_square(self) -> Any:
        """NumberFieldElement.is_square(self, root=False)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 2172)

        Return ``True`` if ``self`` is a square in its parent number field and
        otherwise return ``False``.

        INPUT:

        - ``root`` -- if ``True``, also return a square root (or ``None`` if
          ``self`` is not a perfect square)

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: m.<b> = NumberField(x^4 - 1789)
            sage: b.is_square()
            False
            sage: c = (2/3*b + 5)^2; c
            4/9*b^2 + 20/3*b + 25
            sage: c.is_square()
            True
            sage: c.is_square(True)
            (True, 2/3*b + 5)

        We also test the functional notation.

        ::

            sage: is_square(c, True)
            (True, 2/3*b + 5)
            sage: is_square(c)
            True
            sage: is_square(c + 1)
            False

        TESTS:

        Test that :issue:`16894` is fixed::

            sage: K.<a> = QuadraticField(22)
            sage: u = K.units()[0]
            sage: (u^14).is_square()
            True"""
    @overload
    def is_square(self) -> Any:
        """NumberFieldElement.is_square(self, root=False)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 2172)

        Return ``True`` if ``self`` is a square in its parent number field and
        otherwise return ``False``.

        INPUT:

        - ``root`` -- if ``True``, also return a square root (or ``None`` if
          ``self`` is not a perfect square)

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: m.<b> = NumberField(x^4 - 1789)
            sage: b.is_square()
            False
            sage: c = (2/3*b + 5)^2; c
            4/9*b^2 + 20/3*b + 25
            sage: c.is_square()
            True
            sage: c.is_square(True)
            (True, 2/3*b + 5)

        We also test the functional notation.

        ::

            sage: is_square(c, True)
            (True, 2/3*b + 5)
            sage: is_square(c)
            True
            sage: is_square(c + 1)
            False

        TESTS:

        Test that :issue:`16894` is fixed::

            sage: K.<a> = QuadraticField(22)
            sage: u = K.units()[0]
            sage: (u^14).is_square()
            True"""
    @overload
    def is_square(self, _True) -> Any:
        """NumberFieldElement.is_square(self, root=False)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 2172)

        Return ``True`` if ``self`` is a square in its parent number field and
        otherwise return ``False``.

        INPUT:

        - ``root`` -- if ``True``, also return a square root (or ``None`` if
          ``self`` is not a perfect square)

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: m.<b> = NumberField(x^4 - 1789)
            sage: b.is_square()
            False
            sage: c = (2/3*b + 5)^2; c
            4/9*b^2 + 20/3*b + 25
            sage: c.is_square()
            True
            sage: c.is_square(True)
            (True, 2/3*b + 5)

        We also test the functional notation.

        ::

            sage: is_square(c, True)
            (True, 2/3*b + 5)
            sage: is_square(c)
            True
            sage: is_square(c + 1)
            False

        TESTS:

        Test that :issue:`16894` is fixed::

            sage: K.<a> = QuadraticField(22)
            sage: u = K.units()[0]
            sage: (u^14).is_square()
            True"""
    @overload
    def is_square(self, c, _True) -> Any:
        """NumberFieldElement.is_square(self, root=False)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 2172)

        Return ``True`` if ``self`` is a square in its parent number field and
        otherwise return ``False``.

        INPUT:

        - ``root`` -- if ``True``, also return a square root (or ``None`` if
          ``self`` is not a perfect square)

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: m.<b> = NumberField(x^4 - 1789)
            sage: b.is_square()
            False
            sage: c = (2/3*b + 5)^2; c
            4/9*b^2 + 20/3*b + 25
            sage: c.is_square()
            True
            sage: c.is_square(True)
            (True, 2/3*b + 5)

        We also test the functional notation.

        ::

            sage: is_square(c, True)
            (True, 2/3*b + 5)
            sage: is_square(c)
            True
            sage: is_square(c + 1)
            False

        TESTS:

        Test that :issue:`16894` is fixed::

            sage: K.<a> = QuadraticField(22)
            sage: u = K.units()[0]
            sage: (u^14).is_square()
            True"""
    @overload
    def is_square(self, c) -> Any:
        """NumberFieldElement.is_square(self, root=False)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 2172)

        Return ``True`` if ``self`` is a square in its parent number field and
        otherwise return ``False``.

        INPUT:

        - ``root`` -- if ``True``, also return a square root (or ``None`` if
          ``self`` is not a perfect square)

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: m.<b> = NumberField(x^4 - 1789)
            sage: b.is_square()
            False
            sage: c = (2/3*b + 5)^2; c
            4/9*b^2 + 20/3*b + 25
            sage: c.is_square()
            True
            sage: c.is_square(True)
            (True, 2/3*b + 5)

        We also test the functional notation.

        ::

            sage: is_square(c, True)
            (True, 2/3*b + 5)
            sage: is_square(c)
            True
            sage: is_square(c + 1)
            False

        TESTS:

        Test that :issue:`16894` is fixed::

            sage: K.<a> = QuadraticField(22)
            sage: u = K.units()[0]
            sage: (u^14).is_square()
            True"""
    @overload
    def is_square(self) -> Any:
        """NumberFieldElement.is_square(self, root=False)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 2172)

        Return ``True`` if ``self`` is a square in its parent number field and
        otherwise return ``False``.

        INPUT:

        - ``root`` -- if ``True``, also return a square root (or ``None`` if
          ``self`` is not a perfect square)

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: m.<b> = NumberField(x^4 - 1789)
            sage: b.is_square()
            False
            sage: c = (2/3*b + 5)^2; c
            4/9*b^2 + 20/3*b + 25
            sage: c.is_square()
            True
            sage: c.is_square(True)
            (True, 2/3*b + 5)

        We also test the functional notation.

        ::

            sage: is_square(c, True)
            (True, 2/3*b + 5)
            sage: is_square(c)
            True
            sage: is_square(c + 1)
            False

        TESTS:

        Test that :issue:`16894` is fixed::

            sage: K.<a> = QuadraticField(22)
            sage: u = K.units()[0]
            sage: (u^14).is_square()
            True"""
    @overload
    def is_totally_positive(self) -> Any:
        """NumberFieldElement.is_totally_positive(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 2127)

        Return ``True`` if ``self`` is positive for all real embeddings of its
        parent number field. We do nothing at complex places, so e.g. any
        element of a totally complex number field will return ``True``.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: F.<b> = NumberField(x^3 - 3*x - 1)
            sage: b.is_totally_positive()
            False
            sage: (b^2).is_totally_positive()
            True

        TESTS:

        Check that the output is correct even for numbers that are
        very close to zero (:issue:`9596`)::

            sage: K.<sqrt2> = QuadraticField(2)
            sage: a = 30122754096401; b = 21300003689580
            sage: (a/b)^2 > 2
            True
            sage: (a/b + sqrt2).is_totally_positive()
            True
            sage: r = RealField(3020)(2).sqrt()*2^3000
            sage: a = floor(r)/2^3000
            sage: b = ceil(r)/2^3000
            sage: (a + sqrt2).is_totally_positive()
            False
            sage: (b + sqrt2).is_totally_positive()
            True

        Check that 0 is handled correctly::

            sage: K.<a> = NumberField(x^5 + 4*x + 1)
            sage: K(0).is_totally_positive()
            False"""
    @overload
    def is_totally_positive(self) -> Any:
        """NumberFieldElement.is_totally_positive(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 2127)

        Return ``True`` if ``self`` is positive for all real embeddings of its
        parent number field. We do nothing at complex places, so e.g. any
        element of a totally complex number field will return ``True``.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: F.<b> = NumberField(x^3 - 3*x - 1)
            sage: b.is_totally_positive()
            False
            sage: (b^2).is_totally_positive()
            True

        TESTS:

        Check that the output is correct even for numbers that are
        very close to zero (:issue:`9596`)::

            sage: K.<sqrt2> = QuadraticField(2)
            sage: a = 30122754096401; b = 21300003689580
            sage: (a/b)^2 > 2
            True
            sage: (a/b + sqrt2).is_totally_positive()
            True
            sage: r = RealField(3020)(2).sqrt()*2^3000
            sage: a = floor(r)/2^3000
            sage: b = ceil(r)/2^3000
            sage: (a + sqrt2).is_totally_positive()
            False
            sage: (b + sqrt2).is_totally_positive()
            True

        Check that 0 is handled correctly::

            sage: K.<a> = NumberField(x^5 + 4*x + 1)
            sage: K(0).is_totally_positive()
            False"""
    @overload
    def is_totally_positive(self) -> Any:
        """NumberFieldElement.is_totally_positive(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 2127)

        Return ``True`` if ``self`` is positive for all real embeddings of its
        parent number field. We do nothing at complex places, so e.g. any
        element of a totally complex number field will return ``True``.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: F.<b> = NumberField(x^3 - 3*x - 1)
            sage: b.is_totally_positive()
            False
            sage: (b^2).is_totally_positive()
            True

        TESTS:

        Check that the output is correct even for numbers that are
        very close to zero (:issue:`9596`)::

            sage: K.<sqrt2> = QuadraticField(2)
            sage: a = 30122754096401; b = 21300003689580
            sage: (a/b)^2 > 2
            True
            sage: (a/b + sqrt2).is_totally_positive()
            True
            sage: r = RealField(3020)(2).sqrt()*2^3000
            sage: a = floor(r)/2^3000
            sage: b = ceil(r)/2^3000
            sage: (a + sqrt2).is_totally_positive()
            False
            sage: (b + sqrt2).is_totally_positive()
            True

        Check that 0 is handled correctly::

            sage: K.<a> = NumberField(x^5 + 4*x + 1)
            sage: K(0).is_totally_positive()
            False"""
    @overload
    def is_totally_positive(self) -> Any:
        """NumberFieldElement.is_totally_positive(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 2127)

        Return ``True`` if ``self`` is positive for all real embeddings of its
        parent number field. We do nothing at complex places, so e.g. any
        element of a totally complex number field will return ``True``.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: F.<b> = NumberField(x^3 - 3*x - 1)
            sage: b.is_totally_positive()
            False
            sage: (b^2).is_totally_positive()
            True

        TESTS:

        Check that the output is correct even for numbers that are
        very close to zero (:issue:`9596`)::

            sage: K.<sqrt2> = QuadraticField(2)
            sage: a = 30122754096401; b = 21300003689580
            sage: (a/b)^2 > 2
            True
            sage: (a/b + sqrt2).is_totally_positive()
            True
            sage: r = RealField(3020)(2).sqrt()*2^3000
            sage: a = floor(r)/2^3000
            sage: b = ceil(r)/2^3000
            sage: (a + sqrt2).is_totally_positive()
            False
            sage: (b + sqrt2).is_totally_positive()
            True

        Check that 0 is handled correctly::

            sage: K.<a> = NumberField(x^5 + 4*x + 1)
            sage: K(0).is_totally_positive()
            False"""
    @overload
    def is_totally_positive(self) -> Any:
        """NumberFieldElement.is_totally_positive(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 2127)

        Return ``True`` if ``self`` is positive for all real embeddings of its
        parent number field. We do nothing at complex places, so e.g. any
        element of a totally complex number field will return ``True``.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: F.<b> = NumberField(x^3 - 3*x - 1)
            sage: b.is_totally_positive()
            False
            sage: (b^2).is_totally_positive()
            True

        TESTS:

        Check that the output is correct even for numbers that are
        very close to zero (:issue:`9596`)::

            sage: K.<sqrt2> = QuadraticField(2)
            sage: a = 30122754096401; b = 21300003689580
            sage: (a/b)^2 > 2
            True
            sage: (a/b + sqrt2).is_totally_positive()
            True
            sage: r = RealField(3020)(2).sqrt()*2^3000
            sage: a = floor(r)/2^3000
            sage: b = ceil(r)/2^3000
            sage: (a + sqrt2).is_totally_positive()
            False
            sage: (b + sqrt2).is_totally_positive()
            True

        Check that 0 is handled correctly::

            sage: K.<a> = NumberField(x^5 + 4*x + 1)
            sage: K(0).is_totally_positive()
            False"""
    @overload
    def is_totally_positive(self) -> Any:
        """NumberFieldElement.is_totally_positive(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 2127)

        Return ``True`` if ``self`` is positive for all real embeddings of its
        parent number field. We do nothing at complex places, so e.g. any
        element of a totally complex number field will return ``True``.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: F.<b> = NumberField(x^3 - 3*x - 1)
            sage: b.is_totally_positive()
            False
            sage: (b^2).is_totally_positive()
            True

        TESTS:

        Check that the output is correct even for numbers that are
        very close to zero (:issue:`9596`)::

            sage: K.<sqrt2> = QuadraticField(2)
            sage: a = 30122754096401; b = 21300003689580
            sage: (a/b)^2 > 2
            True
            sage: (a/b + sqrt2).is_totally_positive()
            True
            sage: r = RealField(3020)(2).sqrt()*2^3000
            sage: a = floor(r)/2^3000
            sage: b = ceil(r)/2^3000
            sage: (a + sqrt2).is_totally_positive()
            False
            sage: (b + sqrt2).is_totally_positive()
            True

        Check that 0 is handled correctly::

            sage: K.<a> = NumberField(x^5 + 4*x + 1)
            sage: K(0).is_totally_positive()
            False"""
    @overload
    def is_totally_positive(self) -> Any:
        """NumberFieldElement.is_totally_positive(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 2127)

        Return ``True`` if ``self`` is positive for all real embeddings of its
        parent number field. We do nothing at complex places, so e.g. any
        element of a totally complex number field will return ``True``.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: F.<b> = NumberField(x^3 - 3*x - 1)
            sage: b.is_totally_positive()
            False
            sage: (b^2).is_totally_positive()
            True

        TESTS:

        Check that the output is correct even for numbers that are
        very close to zero (:issue:`9596`)::

            sage: K.<sqrt2> = QuadraticField(2)
            sage: a = 30122754096401; b = 21300003689580
            sage: (a/b)^2 > 2
            True
            sage: (a/b + sqrt2).is_totally_positive()
            True
            sage: r = RealField(3020)(2).sqrt()*2^3000
            sage: a = floor(r)/2^3000
            sage: b = ceil(r)/2^3000
            sage: (a + sqrt2).is_totally_positive()
            False
            sage: (b + sqrt2).is_totally_positive()
            True

        Check that 0 is handled correctly::

            sage: K.<a> = NumberField(x^5 + 4*x + 1)
            sage: K(0).is_totally_positive()
            False"""
    @overload
    def is_unit(self) -> Any:
        """NumberFieldElement.is_unit(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 1565)

        Return ``True`` if ``self`` is a unit in the ring where it is defined.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^2 - x - 1)
            sage: OK = K.ring_of_integers()
            sage: OK(a).is_unit()
            True
            sage: OK(13).is_unit()
            False
            sage: K(13).is_unit()
            True

        It also works for relative fields and orders::

            sage: K.<a,b> = NumberField([x^2 - 3, x^4 + x^3 + x^2 + x + 1])
            sage: OK = K.ring_of_integers()
            sage: OK(b).is_unit()
            True
            sage: OK(a).is_unit()
            False
            sage: a.is_unit()
            True"""
    @overload
    def is_unit(self) -> Any:
        """NumberFieldElement.is_unit(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 1565)

        Return ``True`` if ``self`` is a unit in the ring where it is defined.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^2 - x - 1)
            sage: OK = K.ring_of_integers()
            sage: OK(a).is_unit()
            True
            sage: OK(13).is_unit()
            False
            sage: K(13).is_unit()
            True

        It also works for relative fields and orders::

            sage: K.<a,b> = NumberField([x^2 - 3, x^4 + x^3 + x^2 + x + 1])
            sage: OK = K.ring_of_integers()
            sage: OK(b).is_unit()
            True
            sage: OK(a).is_unit()
            False
            sage: a.is_unit()
            True"""
    @overload
    def is_unit(self) -> Any:
        """NumberFieldElement.is_unit(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 1565)

        Return ``True`` if ``self`` is a unit in the ring where it is defined.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^2 - x - 1)
            sage: OK = K.ring_of_integers()
            sage: OK(a).is_unit()
            True
            sage: OK(13).is_unit()
            False
            sage: K(13).is_unit()
            True

        It also works for relative fields and orders::

            sage: K.<a,b> = NumberField([x^2 - 3, x^4 + x^3 + x^2 + x + 1])
            sage: OK = K.ring_of_integers()
            sage: OK(b).is_unit()
            True
            sage: OK(a).is_unit()
            False
            sage: a.is_unit()
            True"""
    @overload
    def is_unit(self) -> Any:
        """NumberFieldElement.is_unit(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 1565)

        Return ``True`` if ``self`` is a unit in the ring where it is defined.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^2 - x - 1)
            sage: OK = K.ring_of_integers()
            sage: OK(a).is_unit()
            True
            sage: OK(13).is_unit()
            False
            sage: K(13).is_unit()
            True

        It also works for relative fields and orders::

            sage: K.<a,b> = NumberField([x^2 - 3, x^4 + x^3 + x^2 + x + 1])
            sage: OK = K.ring_of_integers()
            sage: OK(b).is_unit()
            True
            sage: OK(a).is_unit()
            False
            sage: a.is_unit()
            True"""
    @overload
    def is_unit(self) -> Any:
        """NumberFieldElement.is_unit(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 1565)

        Return ``True`` if ``self`` is a unit in the ring where it is defined.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^2 - x - 1)
            sage: OK = K.ring_of_integers()
            sage: OK(a).is_unit()
            True
            sage: OK(13).is_unit()
            False
            sage: K(13).is_unit()
            True

        It also works for relative fields and orders::

            sage: K.<a,b> = NumberField([x^2 - 3, x^4 + x^3 + x^2 + x + 1])
            sage: OK = K.ring_of_integers()
            sage: OK(b).is_unit()
            True
            sage: OK(a).is_unit()
            False
            sage: a.is_unit()
            True"""
    @overload
    def is_unit(self) -> Any:
        """NumberFieldElement.is_unit(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 1565)

        Return ``True`` if ``self`` is a unit in the ring where it is defined.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^2 - x - 1)
            sage: OK = K.ring_of_integers()
            sage: OK(a).is_unit()
            True
            sage: OK(13).is_unit()
            False
            sage: K(13).is_unit()
            True

        It also works for relative fields and orders::

            sage: K.<a,b> = NumberField([x^2 - 3, x^4 + x^3 + x^2 + x + 1])
            sage: OK = K.ring_of_integers()
            sage: OK(b).is_unit()
            True
            sage: OK(a).is_unit()
            False
            sage: a.is_unit()
            True"""
    @overload
    def is_unit(self) -> Any:
        """NumberFieldElement.is_unit(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 1565)

        Return ``True`` if ``self`` is a unit in the ring where it is defined.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^2 - x - 1)
            sage: OK = K.ring_of_integers()
            sage: OK(a).is_unit()
            True
            sage: OK(13).is_unit()
            False
            sage: K(13).is_unit()
            True

        It also works for relative fields and orders::

            sage: K.<a,b> = NumberField([x^2 - 3, x^4 + x^3 + x^2 + x + 1])
            sage: OK = K.ring_of_integers()
            sage: OK(b).is_unit()
            True
            sage: OK(a).is_unit()
            False
            sage: a.is_unit()
            True"""
    @overload
    def list(self) -> Any:
        """NumberFieldElement.list(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 4368)

        Return the list of coefficients of ``self`` written in terms of a power
        basis.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^3 - x + 2); ((a + 1)/(a + 2)).list()
            [1/4, 1/2, -1/4]
            sage: K.<a, b> = NumberField([x^3 - x + 2, x^2 + 23]); ((a + b)/(a + 2)).list()
            [3/4*b - 1/2, -1/2*b + 1, 1/4*b - 1/2]"""
    @overload
    def list(self) -> Any:
        """NumberFieldElement.list(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 4368)

        Return the list of coefficients of ``self`` written in terms of a power
        basis.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^3 - x + 2); ((a + 1)/(a + 2)).list()
            [1/4, 1/2, -1/4]
            sage: K.<a, b> = NumberField([x^3 - x + 2, x^2 + 23]); ((a + b)/(a + 2)).list()
            [3/4*b - 1/2, -1/2*b + 1, 1/4*b - 1/2]"""
    @overload
    def list(self) -> Any:
        """NumberFieldElement.list(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 4368)

        Return the list of coefficients of ``self`` written in terms of a power
        basis.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^3 - x + 2); ((a + 1)/(a + 2)).list()
            [1/4, 1/2, -1/4]
            sage: K.<a, b> = NumberField([x^3 - x + 2, x^2 + 23]); ((a + b)/(a + 2)).list()
            [3/4*b - 1/2, -1/2*b + 1, 1/4*b - 1/2]"""
    @overload
    def local_height(self, P, prec=..., weighted=...) -> Any:
        """NumberFieldElement.local_height(self, P, prec=None, weighted=False)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 3949)

        Return the local height of ``self`` at a given prime ideal `P`.

        INPUT:

        - ``P`` -- a prime ideal of the parent of ``self``

        - ``prec`` -- integer; (default: default :class:`RealField` precision);
          desired floating point precision

        - ``weighted`` -- boolean (default: ``False``); if ``True``, apply local
          degree weighting

        OUTPUT:

        (real) The local height of this number field element at the
        place `P`.  If ``weighted`` is ``True``, this is multiplied by the
        local degree (as required for global heights).

        EXAMPLES::

            sage: R.<x> = QQ[]
            sage: K.<a> = NumberField(x^4 + 3*x^2 - 17)
            sage: P = K.ideal(61).factor()[0][0]
            sage: b = 1/(a^2 + 30)
            sage: b.local_height(P)
            4.11087386417331
            sage: b.local_height(P, weighted=True)
            8.22174772834662
            sage: b.local_height(P, 200)
            4.1108738641733112487513891034256147463156817430812610629374
            sage: (b^2).local_height(P)
            8.22174772834662
            sage: (b^-1).local_height(P)
            0.000000000000000

        A relative example::

            sage: PK.<y> = K[]
            sage: L.<c> = NumberField(y^2 + a)
            sage: L(1/4).local_height(L.ideal(2, c - a + 1))
            1.38629436111989"""
    @overload
    def local_height(self, P) -> Any:
        """NumberFieldElement.local_height(self, P, prec=None, weighted=False)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 3949)

        Return the local height of ``self`` at a given prime ideal `P`.

        INPUT:

        - ``P`` -- a prime ideal of the parent of ``self``

        - ``prec`` -- integer; (default: default :class:`RealField` precision);
          desired floating point precision

        - ``weighted`` -- boolean (default: ``False``); if ``True``, apply local
          degree weighting

        OUTPUT:

        (real) The local height of this number field element at the
        place `P`.  If ``weighted`` is ``True``, this is multiplied by the
        local degree (as required for global heights).

        EXAMPLES::

            sage: R.<x> = QQ[]
            sage: K.<a> = NumberField(x^4 + 3*x^2 - 17)
            sage: P = K.ideal(61).factor()[0][0]
            sage: b = 1/(a^2 + 30)
            sage: b.local_height(P)
            4.11087386417331
            sage: b.local_height(P, weighted=True)
            8.22174772834662
            sage: b.local_height(P, 200)
            4.1108738641733112487513891034256147463156817430812610629374
            sage: (b^2).local_height(P)
            8.22174772834662
            sage: (b^-1).local_height(P)
            0.000000000000000

        A relative example::

            sage: PK.<y> = K[]
            sage: L.<c> = NumberField(y^2 + a)
            sage: L(1/4).local_height(L.ideal(2, c - a + 1))
            1.38629436111989"""
    @overload
    def local_height(self, P, weighted=...) -> Any:
        """NumberFieldElement.local_height(self, P, prec=None, weighted=False)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 3949)

        Return the local height of ``self`` at a given prime ideal `P`.

        INPUT:

        - ``P`` -- a prime ideal of the parent of ``self``

        - ``prec`` -- integer; (default: default :class:`RealField` precision);
          desired floating point precision

        - ``weighted`` -- boolean (default: ``False``); if ``True``, apply local
          degree weighting

        OUTPUT:

        (real) The local height of this number field element at the
        place `P`.  If ``weighted`` is ``True``, this is multiplied by the
        local degree (as required for global heights).

        EXAMPLES::

            sage: R.<x> = QQ[]
            sage: K.<a> = NumberField(x^4 + 3*x^2 - 17)
            sage: P = K.ideal(61).factor()[0][0]
            sage: b = 1/(a^2 + 30)
            sage: b.local_height(P)
            4.11087386417331
            sage: b.local_height(P, weighted=True)
            8.22174772834662
            sage: b.local_height(P, 200)
            4.1108738641733112487513891034256147463156817430812610629374
            sage: (b^2).local_height(P)
            8.22174772834662
            sage: (b^-1).local_height(P)
            0.000000000000000

        A relative example::

            sage: PK.<y> = K[]
            sage: L.<c> = NumberField(y^2 + a)
            sage: L(1/4).local_height(L.ideal(2, c - a + 1))
            1.38629436111989"""
    @overload
    def local_height(self, P) -> Any:
        """NumberFieldElement.local_height(self, P, prec=None, weighted=False)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 3949)

        Return the local height of ``self`` at a given prime ideal `P`.

        INPUT:

        - ``P`` -- a prime ideal of the parent of ``self``

        - ``prec`` -- integer; (default: default :class:`RealField` precision);
          desired floating point precision

        - ``weighted`` -- boolean (default: ``False``); if ``True``, apply local
          degree weighting

        OUTPUT:

        (real) The local height of this number field element at the
        place `P`.  If ``weighted`` is ``True``, this is multiplied by the
        local degree (as required for global heights).

        EXAMPLES::

            sage: R.<x> = QQ[]
            sage: K.<a> = NumberField(x^4 + 3*x^2 - 17)
            sage: P = K.ideal(61).factor()[0][0]
            sage: b = 1/(a^2 + 30)
            sage: b.local_height(P)
            4.11087386417331
            sage: b.local_height(P, weighted=True)
            8.22174772834662
            sage: b.local_height(P, 200)
            4.1108738641733112487513891034256147463156817430812610629374
            sage: (b^2).local_height(P)
            8.22174772834662
            sage: (b^-1).local_height(P)
            0.000000000000000

        A relative example::

            sage: PK.<y> = K[]
            sage: L.<c> = NumberField(y^2 + a)
            sage: L(1/4).local_height(L.ideal(2, c - a + 1))
            1.38629436111989"""
    @overload
    def local_height(self, P) -> Any:
        """NumberFieldElement.local_height(self, P, prec=None, weighted=False)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 3949)

        Return the local height of ``self`` at a given prime ideal `P`.

        INPUT:

        - ``P`` -- a prime ideal of the parent of ``self``

        - ``prec`` -- integer; (default: default :class:`RealField` precision);
          desired floating point precision

        - ``weighted`` -- boolean (default: ``False``); if ``True``, apply local
          degree weighting

        OUTPUT:

        (real) The local height of this number field element at the
        place `P`.  If ``weighted`` is ``True``, this is multiplied by the
        local degree (as required for global heights).

        EXAMPLES::

            sage: R.<x> = QQ[]
            sage: K.<a> = NumberField(x^4 + 3*x^2 - 17)
            sage: P = K.ideal(61).factor()[0][0]
            sage: b = 1/(a^2 + 30)
            sage: b.local_height(P)
            4.11087386417331
            sage: b.local_height(P, weighted=True)
            8.22174772834662
            sage: b.local_height(P, 200)
            4.1108738641733112487513891034256147463156817430812610629374
            sage: (b^2).local_height(P)
            8.22174772834662
            sage: (b^-1).local_height(P)
            0.000000000000000

        A relative example::

            sage: PK.<y> = K[]
            sage: L.<c> = NumberField(y^2 + a)
            sage: L(1/4).local_height(L.ideal(2, c - a + 1))
            1.38629436111989"""
    @overload
    def local_height_arch(self, i, prec=..., weighted=...) -> Any:
        """NumberFieldElement.local_height_arch(self, i, prec=None, weighted=False)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 4005)

        Return the local height of ``self`` at the `i`-th infinite place.

        INPUT:

        - ``i`` -- integer in ``range(r+s)`` where `(r,s)` is the signature of
          the parent field (so `n=r+2s` is the degree)

        - ``prec`` -- integer (default: default :class:`RealField` precision);
          desired floating point precision

        - ``weighted`` -- boolean (default: ``False``); if ``True``, apply local
          degree weighting, i.e. double the value for complex places

        OUTPUT:

        (real) The archimedean local height of this number field
        element at the `i`-th infinite place.  If ``weighted`` is
        ``True``, this is multiplied by the local degree (as required for
        global heights), i.e. 1 for real places and 2 for complex
        places.

        EXAMPLES::

            sage: R.<x> = QQ[]
            sage: K.<a> = NumberField(x^4 + 3*x^2 - 17)
            sage: [p.codomain() for p in K.places()]
            [Real Field with 106 bits of precision,
             Real Field with 106 bits of precision,
             Complex Field with 53 bits of precision]
            sage: [a.local_height_arch(i) for i in range(3)]
            [0.5301924545717755083366563897519,
            0.5301924545717755083366563897519,
            0.886414217456333]
            sage: [a.local_height_arch(i, weighted=True) for i in range(3)]
            [0.5301924545717755083366563897519,
            0.5301924545717755083366563897519,
            1.77282843491267]

        A relative example::

            sage: L.<b, c> = NumberFieldTower([x^2 - 5, x^3 + x + 3])
            sage: [(b + c).local_height_arch(i) for i in range(4)]
            [1.238223390757884911842206617439,
            0.02240347229957875780769746914391,
            0.780028961749618,
            1.16048938497298]"""
    @overload
    def local_height_arch(self, i) -> Any:
        """NumberFieldElement.local_height_arch(self, i, prec=None, weighted=False)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 4005)

        Return the local height of ``self`` at the `i`-th infinite place.

        INPUT:

        - ``i`` -- integer in ``range(r+s)`` where `(r,s)` is the signature of
          the parent field (so `n=r+2s` is the degree)

        - ``prec`` -- integer (default: default :class:`RealField` precision);
          desired floating point precision

        - ``weighted`` -- boolean (default: ``False``); if ``True``, apply local
          degree weighting, i.e. double the value for complex places

        OUTPUT:

        (real) The archimedean local height of this number field
        element at the `i`-th infinite place.  If ``weighted`` is
        ``True``, this is multiplied by the local degree (as required for
        global heights), i.e. 1 for real places and 2 for complex
        places.

        EXAMPLES::

            sage: R.<x> = QQ[]
            sage: K.<a> = NumberField(x^4 + 3*x^2 - 17)
            sage: [p.codomain() for p in K.places()]
            [Real Field with 106 bits of precision,
             Real Field with 106 bits of precision,
             Complex Field with 53 bits of precision]
            sage: [a.local_height_arch(i) for i in range(3)]
            [0.5301924545717755083366563897519,
            0.5301924545717755083366563897519,
            0.886414217456333]
            sage: [a.local_height_arch(i, weighted=True) for i in range(3)]
            [0.5301924545717755083366563897519,
            0.5301924545717755083366563897519,
            1.77282843491267]

        A relative example::

            sage: L.<b, c> = NumberFieldTower([x^2 - 5, x^3 + x + 3])
            sage: [(b + c).local_height_arch(i) for i in range(4)]
            [1.238223390757884911842206617439,
            0.02240347229957875780769746914391,
            0.780028961749618,
            1.16048938497298]"""
    @overload
    def local_height_arch(self, i, weighted=...) -> Any:
        """NumberFieldElement.local_height_arch(self, i, prec=None, weighted=False)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 4005)

        Return the local height of ``self`` at the `i`-th infinite place.

        INPUT:

        - ``i`` -- integer in ``range(r+s)`` where `(r,s)` is the signature of
          the parent field (so `n=r+2s` is the degree)

        - ``prec`` -- integer (default: default :class:`RealField` precision);
          desired floating point precision

        - ``weighted`` -- boolean (default: ``False``); if ``True``, apply local
          degree weighting, i.e. double the value for complex places

        OUTPUT:

        (real) The archimedean local height of this number field
        element at the `i`-th infinite place.  If ``weighted`` is
        ``True``, this is multiplied by the local degree (as required for
        global heights), i.e. 1 for real places and 2 for complex
        places.

        EXAMPLES::

            sage: R.<x> = QQ[]
            sage: K.<a> = NumberField(x^4 + 3*x^2 - 17)
            sage: [p.codomain() for p in K.places()]
            [Real Field with 106 bits of precision,
             Real Field with 106 bits of precision,
             Complex Field with 53 bits of precision]
            sage: [a.local_height_arch(i) for i in range(3)]
            [0.5301924545717755083366563897519,
            0.5301924545717755083366563897519,
            0.886414217456333]
            sage: [a.local_height_arch(i, weighted=True) for i in range(3)]
            [0.5301924545717755083366563897519,
            0.5301924545717755083366563897519,
            1.77282843491267]

        A relative example::

            sage: L.<b, c> = NumberFieldTower([x^2 - 5, x^3 + x + 3])
            sage: [(b + c).local_height_arch(i) for i in range(4)]
            [1.238223390757884911842206617439,
            0.02240347229957875780769746914391,
            0.780028961749618,
            1.16048938497298]"""
    @overload
    def local_height_arch(self, i) -> Any:
        """NumberFieldElement.local_height_arch(self, i, prec=None, weighted=False)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 4005)

        Return the local height of ``self`` at the `i`-th infinite place.

        INPUT:

        - ``i`` -- integer in ``range(r+s)`` where `(r,s)` is the signature of
          the parent field (so `n=r+2s` is the degree)

        - ``prec`` -- integer (default: default :class:`RealField` precision);
          desired floating point precision

        - ``weighted`` -- boolean (default: ``False``); if ``True``, apply local
          degree weighting, i.e. double the value for complex places

        OUTPUT:

        (real) The archimedean local height of this number field
        element at the `i`-th infinite place.  If ``weighted`` is
        ``True``, this is multiplied by the local degree (as required for
        global heights), i.e. 1 for real places and 2 for complex
        places.

        EXAMPLES::

            sage: R.<x> = QQ[]
            sage: K.<a> = NumberField(x^4 + 3*x^2 - 17)
            sage: [p.codomain() for p in K.places()]
            [Real Field with 106 bits of precision,
             Real Field with 106 bits of precision,
             Complex Field with 53 bits of precision]
            sage: [a.local_height_arch(i) for i in range(3)]
            [0.5301924545717755083366563897519,
            0.5301924545717755083366563897519,
            0.886414217456333]
            sage: [a.local_height_arch(i, weighted=True) for i in range(3)]
            [0.5301924545717755083366563897519,
            0.5301924545717755083366563897519,
            1.77282843491267]

        A relative example::

            sage: L.<b, c> = NumberFieldTower([x^2 - 5, x^3 + x + 3])
            sage: [(b + c).local_height_arch(i) for i in range(4)]
            [1.238223390757884911842206617439,
            0.02240347229957875780769746914391,
            0.780028961749618,
            1.16048938497298]"""
    def matrix(self, base=...) -> Any:
        """NumberFieldElement.matrix(self, base=None)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 3745)

        If ``base`` is ``None``, return the matrix of right multiplication by the
        element on the power basis `1, x, x^2, \\ldots, x^{d-1}` for
        the number field. Thus the *rows* of this matrix give the images of
        each of the `x^i`.

        If ``base`` is not ``None``, then ``base`` must be either a field that embeds
        in the parent of ``self`` or a morphism to the parent of ``self``, in which
        case this function returns the matrix of multiplication by ``self`` on
        the power basis, where we view the parent field as a field over
        ``base``.

        Specifying ``base`` as the base field over which the parent of ``self``
        is a relative extension is equivalent to ``base`` being ``None``.

        INPUT:

        - ``base`` -- field or morphism

        EXAMPLES:

        Regular number field::

            sage: K.<a> = NumberField(QQ['x'].0^3 - 5)
            sage: M = a.matrix(); M
            [0 1 0]
            [0 0 1]
            [5 0 0]
            sage: M.base_ring() is QQ
            True

        Relative number field::

            sage: L.<b> = K.extension(K['x'].0^2 - 2)
            sage: M = b.matrix(); M
            [0 1]
            [2 0]
            sage: M.base_ring() is K
            True

        Absolute number field::

            sage: M = L.absolute_field('c').gen().matrix(); M
            [  0   1   0   0   0   0]
            [  0   0   1   0   0   0]
            [  0   0   0   1   0   0]
            [  0   0   0   0   1   0]
            [  0   0   0   0   0   1]
            [-17 -60 -12 -10   6   0]
            sage: M.base_ring() is QQ
            True

        More complicated relative number field::

            sage: L.<b> = K.extension(K['x'].0^2 - a); L
            Number Field in b with defining polynomial x^2 - a over its base field
            sage: M = b.matrix(); M
            [0 1]
            [a 0]
            sage: M.base_ring() is K
            True

        An example where we explicitly give the subfield or the embedding::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^4 + 1); L.<a2> = NumberField(x^2 + 1)
            sage: a.matrix(L)
            [ 0  1]
            [a2  0]

        Notice that if we compute all embeddings and choose a different
        one, then the matrix is changed as it should be::

            sage: v = L.embeddings(K)
            sage: a.matrix(v[1])
            [  0   1]
            [-a2   0]

        The norm is also changed::

            sage: a.norm(v[1])
            a2
            sage: a.norm(v[0])
            -a2

        TESTS::

            sage: F.<z> = CyclotomicField(5); t = 3*z**3 + 4*z**2 + 2
            sage: t.matrix(F)
            [3*z^3 + 4*z^2 + 2]
            sage: x = QQ['x'].gen()
            sage: K.<v> = NumberField(x^4 + 514*x^2 + 64321)
            sage: R.<r> = NumberField(x^2 + 4*v*x + 5*v^2 + 514)
            sage: r.matrix()
            [           0            1]
            [-5*v^2 - 514         -4*v]
            sage: r.matrix(K)
            [           0            1]
            [-5*v^2 - 514         -4*v]
            sage: r.matrix(R)
            [r]
            sage: foo = R.random_element()
            sage: foo.matrix(R) == matrix(1,1,[foo])
            True"""
    def minpoly(self, var=...) -> Any:
        """NumberFieldElement.minpoly(self, var='x')

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 3692)

        Return the minimal polynomial of this number field element.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^2 + 3)
            sage: a.minpoly('x')
            x^2 + 3
            sage: R.<X> = K['X']
            sage: L.<b> = K.extension(X^2 - (22 + a))
            sage: b.minpoly('t')
            t^2 - a - 22
            sage: b.absolute_minpoly('t')
            t^4 - 44*t^2 + 487
            sage: b^2 - (22+a)
            0"""
    @overload
    def multiplicative_order(self) -> Any:
        """NumberFieldElement.multiplicative_order(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 3345)

        Return the multiplicative order of this number field element.

        EXAMPLES::

            sage: K.<z> = CyclotomicField(5)
            sage: z.multiplicative_order()
            5
            sage: (-z).multiplicative_order()
            10
            sage: (1+z).multiplicative_order()
            +Infinity

            sage: x = polygen(QQ)
            sage: K.<a> = NumberField(x^40 - x^20 + 4)
            sage: u = 1/4*a^30 + 1/4*a^10 + 1/2
            sage: u.multiplicative_order()
            6
            sage: a.multiplicative_order()
            +Infinity

        An example in a relative extension::

            sage: K.<a, b> = NumberField([x^2 + x + 1, x^2 - 3])
            sage: z = (a - 1)*b/3
            sage: z.multiplicative_order()
            12
            sage: z^12==1 and z^6!=1 and z^4!=1
            True"""
    @overload
    def multiplicative_order(self) -> Any:
        """NumberFieldElement.multiplicative_order(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 3345)

        Return the multiplicative order of this number field element.

        EXAMPLES::

            sage: K.<z> = CyclotomicField(5)
            sage: z.multiplicative_order()
            5
            sage: (-z).multiplicative_order()
            10
            sage: (1+z).multiplicative_order()
            +Infinity

            sage: x = polygen(QQ)
            sage: K.<a> = NumberField(x^40 - x^20 + 4)
            sage: u = 1/4*a^30 + 1/4*a^10 + 1/2
            sage: u.multiplicative_order()
            6
            sage: a.multiplicative_order()
            +Infinity

        An example in a relative extension::

            sage: K.<a, b> = NumberField([x^2 + x + 1, x^2 - 3])
            sage: z = (a - 1)*b/3
            sage: z.multiplicative_order()
            12
            sage: z^12==1 and z^6!=1 and z^4!=1
            True"""
    @overload
    def multiplicative_order(self) -> Any:
        """NumberFieldElement.multiplicative_order(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 3345)

        Return the multiplicative order of this number field element.

        EXAMPLES::

            sage: K.<z> = CyclotomicField(5)
            sage: z.multiplicative_order()
            5
            sage: (-z).multiplicative_order()
            10
            sage: (1+z).multiplicative_order()
            +Infinity

            sage: x = polygen(QQ)
            sage: K.<a> = NumberField(x^40 - x^20 + 4)
            sage: u = 1/4*a^30 + 1/4*a^10 + 1/2
            sage: u.multiplicative_order()
            6
            sage: a.multiplicative_order()
            +Infinity

        An example in a relative extension::

            sage: K.<a, b> = NumberField([x^2 + x + 1, x^2 - 3])
            sage: z = (a - 1)*b/3
            sage: z.multiplicative_order()
            12
            sage: z^12==1 and z^6!=1 and z^4!=1
            True"""
    @overload
    def multiplicative_order(self) -> Any:
        """NumberFieldElement.multiplicative_order(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 3345)

        Return the multiplicative order of this number field element.

        EXAMPLES::

            sage: K.<z> = CyclotomicField(5)
            sage: z.multiplicative_order()
            5
            sage: (-z).multiplicative_order()
            10
            sage: (1+z).multiplicative_order()
            +Infinity

            sage: x = polygen(QQ)
            sage: K.<a> = NumberField(x^40 - x^20 + 4)
            sage: u = 1/4*a^30 + 1/4*a^10 + 1/2
            sage: u.multiplicative_order()
            6
            sage: a.multiplicative_order()
            +Infinity

        An example in a relative extension::

            sage: K.<a, b> = NumberField([x^2 + x + 1, x^2 - 3])
            sage: z = (a - 1)*b/3
            sage: z.multiplicative_order()
            12
            sage: z^12==1 and z^6!=1 and z^4!=1
            True"""
    @overload
    def multiplicative_order(self) -> Any:
        """NumberFieldElement.multiplicative_order(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 3345)

        Return the multiplicative order of this number field element.

        EXAMPLES::

            sage: K.<z> = CyclotomicField(5)
            sage: z.multiplicative_order()
            5
            sage: (-z).multiplicative_order()
            10
            sage: (1+z).multiplicative_order()
            +Infinity

            sage: x = polygen(QQ)
            sage: K.<a> = NumberField(x^40 - x^20 + 4)
            sage: u = 1/4*a^30 + 1/4*a^10 + 1/2
            sage: u.multiplicative_order()
            6
            sage: a.multiplicative_order()
            +Infinity

        An example in a relative extension::

            sage: K.<a, b> = NumberField([x^2 + x + 1, x^2 - 3])
            sage: z = (a - 1)*b/3
            sage: z.multiplicative_order()
            12
            sage: z^12==1 and z^6!=1 and z^4!=1
            True"""
    @overload
    def multiplicative_order(self) -> Any:
        """NumberFieldElement.multiplicative_order(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 3345)

        Return the multiplicative order of this number field element.

        EXAMPLES::

            sage: K.<z> = CyclotomicField(5)
            sage: z.multiplicative_order()
            5
            sage: (-z).multiplicative_order()
            10
            sage: (1+z).multiplicative_order()
            +Infinity

            sage: x = polygen(QQ)
            sage: K.<a> = NumberField(x^40 - x^20 + 4)
            sage: u = 1/4*a^30 + 1/4*a^10 + 1/2
            sage: u.multiplicative_order()
            6
            sage: a.multiplicative_order()
            +Infinity

        An example in a relative extension::

            sage: K.<a, b> = NumberField([x^2 + x + 1, x^2 - 3])
            sage: z = (a - 1)*b/3
            sage: z.multiplicative_order()
            12
            sage: z^12==1 and z^6!=1 and z^4!=1
            True"""
    @overload
    def multiplicative_order(self) -> Any:
        """NumberFieldElement.multiplicative_order(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 3345)

        Return the multiplicative order of this number field element.

        EXAMPLES::

            sage: K.<z> = CyclotomicField(5)
            sage: z.multiplicative_order()
            5
            sage: (-z).multiplicative_order()
            10
            sage: (1+z).multiplicative_order()
            +Infinity

            sage: x = polygen(QQ)
            sage: K.<a> = NumberField(x^40 - x^20 + 4)
            sage: u = 1/4*a^30 + 1/4*a^10 + 1/2
            sage: u.multiplicative_order()
            6
            sage: a.multiplicative_order()
            +Infinity

        An example in a relative extension::

            sage: K.<a, b> = NumberField([x^2 + x + 1, x^2 - 3])
            sage: z = (a - 1)*b/3
            sage: z.multiplicative_order()
            12
            sage: z^12==1 and z^6!=1 and z^4!=1
            True"""
    def norm(self, K=...) -> Any:
        """NumberFieldElement.norm(self, K=None)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 3534)

        Return the absolute or relative norm of this number field element.

        If `K` is given, then `K` must be a subfield of the parent `L` of ``self``, in
        which case the norm is the relative norm from `L` to `K`. In all other
        cases, the norm is the absolute norm down to `\\QQ`.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^3 + x^2 + x - 132/7); K
            Number Field in a with defining polynomial x^3 + x^2 + x - 132/7
            sage: a.norm()
            132/7
            sage: factor(a.norm())
            2^2 * 3 * 7^-1 * 11
            sage: K(0).norm()
            0

        Some complicated relatives norms in a tower of number fields.

        ::

            sage: K.<a,b,c> = NumberField([x^2 + 1, x^2 + 3, x^2 + 5])
            sage: L = K.base_field(); M = L.base_field()
            sage: a.norm()
            1
            sage: a.norm(L)
            1
            sage: a.norm(M)
            1
            sage: a
            a
            sage: (a + b + c).norm()
            121
            sage: (a + b + c).norm(L)
            2*c*b - 7
            sage: (a + b + c).norm(M)
            -11

        We illustrate that norm is compatible with towers::

            sage: z = (a + b + c).norm(L); z.norm(M)
            -11

        If we are in an order, the norm is an integer::

            sage: K.<a> = NumberField(x^3 - 2)
            sage: a.norm().parent()
            Rational Field
            sage: R = K.ring_of_integers()
            sage: R(a).norm().parent()
            Integer Ring

        When the base field is given by an embedding::

            sage: K.<a> = NumberField(x^4 + 1)
            sage: L.<a2> = NumberField(x^2 + 1)
            sage: v = L.embeddings(K)
            sage: a.norm(v[1])
            a2
            sage: a.norm(v[0])
            -a2

        TESTS::

            sage: F.<z> = CyclotomicField(5)
            sage: t = 3*z**3 + 4*z**2 + 2
            sage: t.norm(F)
            3*z^3 + 4*z^2 + 2"""
    def nth_root(self, n, all=...) -> Any:
        """NumberFieldElement.nth_root(self, n, all=False)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 2330)

        Return an `n`-th root of ``self`` in its parent `K`.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^4 - 7)
            sage: K(7).nth_root(2)
            a^2
            sage: K((a-3)^5).nth_root(5)
            a - 3

        ALGORITHM: Use PARI to factor `x^n` - ``self`` in `K`."""
    @overload
    def numerator_ideal(self) -> Any:
        """NumberFieldElement.numerator_ideal(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 4198)

        Return the numerator ideal of this number field element.

        The numerator ideal of a number field element `a` is the ideal of
        the ring of integers `R` obtained by intersecting `aR` with `R`.

        .. SEEALSO::

            :meth:`denominator_ideal`

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^2 + 5)
            sage: b = (1+a)/2
            sage: b.norm()
            3/2
            sage: N = b.numerator_ideal(); N
            Fractional ideal (3, a + 1)
            sage: N.norm()
            3
            sage: (1/b).numerator_ideal()
            Fractional ideal (2, a + 1)
            sage: K(0).numerator_ideal()
            Ideal (0) of Number Field in a with defining polynomial x^2 + 5"""
    @overload
    def numerator_ideal(self) -> Any:
        """NumberFieldElement.numerator_ideal(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 4198)

        Return the numerator ideal of this number field element.

        The numerator ideal of a number field element `a` is the ideal of
        the ring of integers `R` obtained by intersecting `aR` with `R`.

        .. SEEALSO::

            :meth:`denominator_ideal`

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^2 + 5)
            sage: b = (1+a)/2
            sage: b.norm()
            3/2
            sage: N = b.numerator_ideal(); N
            Fractional ideal (3, a + 1)
            sage: N.norm()
            3
            sage: (1/b).numerator_ideal()
            Fractional ideal (2, a + 1)
            sage: K(0).numerator_ideal()
            Ideal (0) of Number Field in a with defining polynomial x^2 + 5"""
    @overload
    def numerator_ideal(self) -> Any:
        """NumberFieldElement.numerator_ideal(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 4198)

        Return the numerator ideal of this number field element.

        The numerator ideal of a number field element `a` is the ideal of
        the ring of integers `R` obtained by intersecting `aR` with `R`.

        .. SEEALSO::

            :meth:`denominator_ideal`

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^2 + 5)
            sage: b = (1+a)/2
            sage: b.norm()
            3/2
            sage: N = b.numerator_ideal(); N
            Fractional ideal (3, a + 1)
            sage: N.norm()
            3
            sage: (1/b).numerator_ideal()
            Fractional ideal (2, a + 1)
            sage: K(0).numerator_ideal()
            Ideal (0) of Number Field in a with defining polynomial x^2 + 5"""
    @overload
    def numerator_ideal(self) -> Any:
        """NumberFieldElement.numerator_ideal(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 4198)

        Return the numerator ideal of this number field element.

        The numerator ideal of a number field element `a` is the ideal of
        the ring of integers `R` obtained by intersecting `aR` with `R`.

        .. SEEALSO::

            :meth:`denominator_ideal`

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^2 + 5)
            sage: b = (1+a)/2
            sage: b.norm()
            3/2
            sage: N = b.numerator_ideal(); N
            Fractional ideal (3, a + 1)
            sage: N.norm()
            3
            sage: (1/b).numerator_ideal()
            Fractional ideal (2, a + 1)
            sage: K(0).numerator_ideal()
            Ideal (0) of Number Field in a with defining polynomial x^2 + 5"""
    def ord(self, P) -> Any:
        """NumberFieldElement.valuation(self, P)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 3878)

        Return the valuation of ``self`` at a given prime ideal `P`.

        INPUT:

        - ``P`` -- a prime ideal of the parent of ``self``

        .. NOTE::

            The method :meth:`ord` is an alias for :meth:`valuation`.

        EXAMPLES::

            sage: R.<x> = QQ[]
            sage: K.<a> = NumberField(x^4 + 3*x^2 - 17)
            sage: P = K.ideal(61).factor()[0][0]
            sage: b = a^2 + 30
            sage: b.valuation(P)
            1
            sage: b.ord(P)
            1
            sage: type(b.valuation(P))
            <class 'sage.rings.integer.Integer'>

        The function can be applied to elements in relative number fields::

            sage: L.<b> = K.extension(x^2 - 3)
            sage: [L(6).valuation(P) for P in L.primes_above(2)]
            [4]
            sage: [L(6).valuation(P) for P in L.primes_above(3)]
            [2, 2]

        TESTS:

        Some checks for :issue:`29215`::

            sage: K = QuadraticField(-5)
            sage: v = QuadraticField(3).ideal(5)
            sage: K(33).valuation(v)
            Traceback (most recent call last):
            ...
            ValueError: P must be an ideal in the same number field

            sage: K(33).valuation(5)
            Traceback (most recent call last):
            ...
            TypeError: P must be an ideal

            sage: w = K.ideal(5)
            sage: K(33).valuation(w)
            Traceback (most recent call last):
            ...
            ValueError: P must be prime"""
    @overload
    def polynomial(self, var=...) -> Any:
        """NumberFieldElement.polynomial(self, var='x')

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 3156)

        Return the underlying polynomial corresponding to this number field
        element.

        The resulting polynomial is currently *not* cached.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^5 - x - 1)
            sage: f = (-2/3 + 1/3*a)^4; f
            1/81*a^4 - 8/81*a^3 + 8/27*a^2 - 32/81*a + 16/81
            sage: g = f.polynomial(); g
            1/81*x^4 - 8/81*x^3 + 8/27*x^2 - 32/81*x + 16/81
            sage: parent(g)
            Univariate Polynomial Ring in x over Rational Field

        Note that the result of this function is not cached (should this be
        changed?)::

            sage: g is f.polynomial()
            False

        Note that in relative number fields, this produces the polynomial of
        the internal representation of this element::

            sage: R.<y> = K[]
            sage: L.<b> = K.extension(y^2 - a)
            sage: b.polynomial()
            x

        In some cases this might not be what you are looking for::

            sage: K.<a> = NumberField(x^2 + x + 1)
            sage: R.<y> = K[]
            sage: L.<b> = K.extension(y^2 + y + 2)
            sage: b.polynomial()
            1/2*x^3 + 3*x - 1/2
            sage: R(list(b))
            y"""
    @overload
    def polynomial(self) -> Any:
        """NumberFieldElement.polynomial(self, var='x')

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 3156)

        Return the underlying polynomial corresponding to this number field
        element.

        The resulting polynomial is currently *not* cached.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^5 - x - 1)
            sage: f = (-2/3 + 1/3*a)^4; f
            1/81*a^4 - 8/81*a^3 + 8/27*a^2 - 32/81*a + 16/81
            sage: g = f.polynomial(); g
            1/81*x^4 - 8/81*x^3 + 8/27*x^2 - 32/81*x + 16/81
            sage: parent(g)
            Univariate Polynomial Ring in x over Rational Field

        Note that the result of this function is not cached (should this be
        changed?)::

            sage: g is f.polynomial()
            False

        Note that in relative number fields, this produces the polynomial of
        the internal representation of this element::

            sage: R.<y> = K[]
            sage: L.<b> = K.extension(y^2 - a)
            sage: b.polynomial()
            x

        In some cases this might not be what you are looking for::

            sage: K.<a> = NumberField(x^2 + x + 1)
            sage: R.<y> = K[]
            sage: L.<b> = K.extension(y^2 + y + 2)
            sage: b.polynomial()
            1/2*x^3 + 3*x - 1/2
            sage: R(list(b))
            y"""
    @overload
    def polynomial(self) -> Any:
        """NumberFieldElement.polynomial(self, var='x')

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 3156)

        Return the underlying polynomial corresponding to this number field
        element.

        The resulting polynomial is currently *not* cached.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^5 - x - 1)
            sage: f = (-2/3 + 1/3*a)^4; f
            1/81*a^4 - 8/81*a^3 + 8/27*a^2 - 32/81*a + 16/81
            sage: g = f.polynomial(); g
            1/81*x^4 - 8/81*x^3 + 8/27*x^2 - 32/81*x + 16/81
            sage: parent(g)
            Univariate Polynomial Ring in x over Rational Field

        Note that the result of this function is not cached (should this be
        changed?)::

            sage: g is f.polynomial()
            False

        Note that in relative number fields, this produces the polynomial of
        the internal representation of this element::

            sage: R.<y> = K[]
            sage: L.<b> = K.extension(y^2 - a)
            sage: b.polynomial()
            x

        In some cases this might not be what you are looking for::

            sage: K.<a> = NumberField(x^2 + x + 1)
            sage: R.<y> = K[]
            sage: L.<b> = K.extension(y^2 + y + 2)
            sage: b.polynomial()
            1/2*x^3 + 3*x - 1/2
            sage: R(list(b))
            y"""
    @overload
    def polynomial(self) -> Any:
        """NumberFieldElement.polynomial(self, var='x')

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 3156)

        Return the underlying polynomial corresponding to this number field
        element.

        The resulting polynomial is currently *not* cached.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^5 - x - 1)
            sage: f = (-2/3 + 1/3*a)^4; f
            1/81*a^4 - 8/81*a^3 + 8/27*a^2 - 32/81*a + 16/81
            sage: g = f.polynomial(); g
            1/81*x^4 - 8/81*x^3 + 8/27*x^2 - 32/81*x + 16/81
            sage: parent(g)
            Univariate Polynomial Ring in x over Rational Field

        Note that the result of this function is not cached (should this be
        changed?)::

            sage: g is f.polynomial()
            False

        Note that in relative number fields, this produces the polynomial of
        the internal representation of this element::

            sage: R.<y> = K[]
            sage: L.<b> = K.extension(y^2 - a)
            sage: b.polynomial()
            x

        In some cases this might not be what you are looking for::

            sage: K.<a> = NumberField(x^2 + x + 1)
            sage: R.<y> = K[]
            sage: L.<b> = K.extension(y^2 + y + 2)
            sage: b.polynomial()
            1/2*x^3 + 3*x - 1/2
            sage: R(list(b))
            y"""
    @overload
    def polynomial(self) -> Any:
        """NumberFieldElement.polynomial(self, var='x')

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 3156)

        Return the underlying polynomial corresponding to this number field
        element.

        The resulting polynomial is currently *not* cached.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^5 - x - 1)
            sage: f = (-2/3 + 1/3*a)^4; f
            1/81*a^4 - 8/81*a^3 + 8/27*a^2 - 32/81*a + 16/81
            sage: g = f.polynomial(); g
            1/81*x^4 - 8/81*x^3 + 8/27*x^2 - 32/81*x + 16/81
            sage: parent(g)
            Univariate Polynomial Ring in x over Rational Field

        Note that the result of this function is not cached (should this be
        changed?)::

            sage: g is f.polynomial()
            False

        Note that in relative number fields, this produces the polynomial of
        the internal representation of this element::

            sage: R.<y> = K[]
            sage: L.<b> = K.extension(y^2 - a)
            sage: b.polynomial()
            x

        In some cases this might not be what you are looking for::

            sage: K.<a> = NumberField(x^2 + x + 1)
            sage: R.<y> = K[]
            sage: L.<b> = K.extension(y^2 + y + 2)
            sage: b.polynomial()
            1/2*x^3 + 3*x - 1/2
            sage: R(list(b))
            y"""
    @overload
    def relative_norm(self) -> Any:
        """NumberFieldElement.relative_norm(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 3629)

        Return the relative norm of this number field element over the next field
        down in some tower of number fields.

        EXAMPLES::

            sage: K1.<a1> = CyclotomicField(11)
            sage: x = polygen(ZZ, 'x')
            sage: K2.<a2> = K1.extension(x^2 - 3)
            sage: (a1 + a2).relative_norm()
            a1^2 - 3
            sage: (a1 + a2).relative_norm().relative_norm() == (a1 + a2).absolute_norm()
            True

            sage: K.<x,y,z> = NumberField([x^2 + 1, x^3 - 3, x^2 - 5])
            sage: (x + y + z).relative_norm()
            y^2 + 2*z*y + 6"""
    @overload
    def relative_norm(self) -> Any:
        """NumberFieldElement.relative_norm(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 3629)

        Return the relative norm of this number field element over the next field
        down in some tower of number fields.

        EXAMPLES::

            sage: K1.<a1> = CyclotomicField(11)
            sage: x = polygen(ZZ, 'x')
            sage: K2.<a2> = K1.extension(x^2 - 3)
            sage: (a1 + a2).relative_norm()
            a1^2 - 3
            sage: (a1 + a2).relative_norm().relative_norm() == (a1 + a2).absolute_norm()
            True

            sage: K.<x,y,z> = NumberField([x^2 + 1, x^3 - 3, x^2 - 5])
            sage: (x + y + z).relative_norm()
            y^2 + 2*z*y + 6"""
    @overload
    def relative_norm(self) -> Any:
        """NumberFieldElement.relative_norm(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 3629)

        Return the relative norm of this number field element over the next field
        down in some tower of number fields.

        EXAMPLES::

            sage: K1.<a1> = CyclotomicField(11)
            sage: x = polygen(ZZ, 'x')
            sage: K2.<a2> = K1.extension(x^2 - 3)
            sage: (a1 + a2).relative_norm()
            a1^2 - 3
            sage: (a1 + a2).relative_norm().relative_norm() == (a1 + a2).absolute_norm()
            True

            sage: K.<x,y,z> = NumberField([x^2 + 1, x^3 - 3, x^2 - 5])
            sage: (x + y + z).relative_norm()
            y^2 + 2*z*y + 6"""
    @overload
    def relative_norm(self) -> Any:
        """NumberFieldElement.relative_norm(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 3629)

        Return the relative norm of this number field element over the next field
        down in some tower of number fields.

        EXAMPLES::

            sage: K1.<a1> = CyclotomicField(11)
            sage: x = polygen(ZZ, 'x')
            sage: K2.<a2> = K1.extension(x^2 - 3)
            sage: (a1 + a2).relative_norm()
            a1^2 - 3
            sage: (a1 + a2).relative_norm().relative_norm() == (a1 + a2).absolute_norm()
            True

            sage: K.<x,y,z> = NumberField([x^2 + 1, x^3 - 3, x^2 - 5])
            sage: (x + y + z).relative_norm()
            y^2 + 2*z*y + 6"""
    def residue_symbol(self, P, m, check=...) -> Any:
        """NumberFieldElement.residue_symbol(self, P, m, check=True)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 4429)

        The `m`-th power residue symbol for an element ``self`` and proper ideal `P`.

        .. MATH:: \\left(\\frac{\\alpha}{\\mathbf{P}}\\right) \\equiv \\alpha^{\\frac{N(\\mathbf{P})-1}{m}} \\operatorname{mod} \\mathbf{P}

        .. NOTE:: accepts `m=1`, in which case returns 1

        .. NOTE:: can also be called for an ideal from sage.rings.number_field_ideal.residue_symbol

        .. NOTE:: ``self`` is coerced into the number field of the ideal P

        .. NOTE::

            if `m=2`, ``self`` is an integer, and `P` is an ideal of a number field of absolute degree 1 (i.e. it is a copy of the rationals),
            then this calls :func:`kronecker_symbol`, which is implemented using GMP.

        INPUT:

        - ``P`` -- proper ideal of the number field (or an extension)

        - ``m`` -- positive integer

        OUTPUT: an `m`-th root of unity in the number field

        EXAMPLES:

        Quadratic Residue (11 is not a square modulo 17)::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x - 1)
            sage: K(11).residue_symbol(K.ideal(17),2)
            -1
            sage: kronecker_symbol(11, 17)
            -1

        The result depends on the number field of the ideal::

            sage: K.<a> = NumberField(x - 1)
            sage: L.<b> = K.extension(x^2 + 1)
            sage: K(7).residue_symbol(K.ideal(11),2)
            -1
            sage: K(7).residue_symbol(L.ideal(11),2)                                    # needs sage.libs.gap
            1

        Cubic Residue::

            sage: K.<w> = NumberField(x^2 - x + 1)
            sage: (w^2 + 3).residue_symbol(K.ideal(17),3)
            -w

        The field must contain the `m`-th roots of unity::

            sage: K.<w> = NumberField(x^2 - x + 1)
            sage: (w^2 + 3).residue_symbol(K.ideal(17),5)
            Traceback (most recent call last):
            ...
            ValueError: The residue symbol to that power is not defined for the number field"""
    @overload
    def round(self) -> Any:
        """NumberFieldElement.round(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 1262)

        Return the round (nearest integer) of this number field element. In case
        of ties, this relies on the default rounding for rational numbers.

        EXAMPLES::

            sage: x = polygen(ZZ)
            sage: p = x**7 - 5*x**2 + x + 1
            sage: a_AA = AA.polynomial_root(p, RIF(1,2))
            sage: K.<a> = NumberField(p, embedding=a_AA)
            sage: b = a**5 + a/2 - 1/7
            sage: RR(b)
            4.13444473767055
            sage: b.round()
            4
            sage: (-b).round()
            -4
            sage: (b + 1/2).round()
            5
            sage: (-b - 1/2).round()
            -5

        This function always succeeds even if a tremendous precision is needed::

            sage: c = b - 5678322907931/1225243417356 + 3
            sage: c.round()
            3
            sage: RIF(c).unique_round()
            Traceback (most recent call last):
            ...
            ValueError: interval does not have a unique round (nearest integer)

        If the number field is not embedded, this function is valid only if the
        element is rational::

            sage: p = x**5 - 3
            sage: K.<a> = NumberField(p)
            sage: [K(k/3).round() for k in range(-3,4)]
            [-1, -1, 0, 0, 0, 1, 1]
            sage: a.round()
            Traceback (most recent call last):
            ...
            TypeError: floor not uniquely defined since no real embedding is specified"""
    @overload
    def round(self, nearestinteger) -> Any:
        """NumberFieldElement.round(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 1262)

        Return the round (nearest integer) of this number field element. In case
        of ties, this relies on the default rounding for rational numbers.

        EXAMPLES::

            sage: x = polygen(ZZ)
            sage: p = x**7 - 5*x**2 + x + 1
            sage: a_AA = AA.polynomial_root(p, RIF(1,2))
            sage: K.<a> = NumberField(p, embedding=a_AA)
            sage: b = a**5 + a/2 - 1/7
            sage: RR(b)
            4.13444473767055
            sage: b.round()
            4
            sage: (-b).round()
            -4
            sage: (b + 1/2).round()
            5
            sage: (-b - 1/2).round()
            -5

        This function always succeeds even if a tremendous precision is needed::

            sage: c = b - 5678322907931/1225243417356 + 3
            sage: c.round()
            3
            sage: RIF(c).unique_round()
            Traceback (most recent call last):
            ...
            ValueError: interval does not have a unique round (nearest integer)

        If the number field is not embedded, this function is valid only if the
        element is rational::

            sage: p = x**5 - 3
            sage: K.<a> = NumberField(p)
            sage: [K(k/3).round() for k in range(-3,4)]
            [-1, -1, 0, 0, 0, 1, 1]
            sage: a.round()
            Traceback (most recent call last):
            ...
            TypeError: floor not uniquely defined since no real embedding is specified"""
    @overload
    def round(self) -> Any:
        """NumberFieldElement.round(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 1262)

        Return the round (nearest integer) of this number field element. In case
        of ties, this relies on the default rounding for rational numbers.

        EXAMPLES::

            sage: x = polygen(ZZ)
            sage: p = x**7 - 5*x**2 + x + 1
            sage: a_AA = AA.polynomial_root(p, RIF(1,2))
            sage: K.<a> = NumberField(p, embedding=a_AA)
            sage: b = a**5 + a/2 - 1/7
            sage: RR(b)
            4.13444473767055
            sage: b.round()
            4
            sage: (-b).round()
            -4
            sage: (b + 1/2).round()
            5
            sage: (-b - 1/2).round()
            -5

        This function always succeeds even if a tremendous precision is needed::

            sage: c = b - 5678322907931/1225243417356 + 3
            sage: c.round()
            3
            sage: RIF(c).unique_round()
            Traceback (most recent call last):
            ...
            ValueError: interval does not have a unique round (nearest integer)

        If the number field is not embedded, this function is valid only if the
        element is rational::

            sage: p = x**5 - 3
            sage: K.<a> = NumberField(p)
            sage: [K(k/3).round() for k in range(-3,4)]
            [-1, -1, 0, 0, 0, 1, 1]
            sage: a.round()
            Traceback (most recent call last):
            ...
            TypeError: floor not uniquely defined since no real embedding is specified"""
    @overload
    def round(self) -> Any:
        """NumberFieldElement.round(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 1262)

        Return the round (nearest integer) of this number field element. In case
        of ties, this relies on the default rounding for rational numbers.

        EXAMPLES::

            sage: x = polygen(ZZ)
            sage: p = x**7 - 5*x**2 + x + 1
            sage: a_AA = AA.polynomial_root(p, RIF(1,2))
            sage: K.<a> = NumberField(p, embedding=a_AA)
            sage: b = a**5 + a/2 - 1/7
            sage: RR(b)
            4.13444473767055
            sage: b.round()
            4
            sage: (-b).round()
            -4
            sage: (b + 1/2).round()
            5
            sage: (-b - 1/2).round()
            -5

        This function always succeeds even if a tremendous precision is needed::

            sage: c = b - 5678322907931/1225243417356 + 3
            sage: c.round()
            3
            sage: RIF(c).unique_round()
            Traceback (most recent call last):
            ...
            ValueError: interval does not have a unique round (nearest integer)

        If the number field is not embedded, this function is valid only if the
        element is rational::

            sage: p = x**5 - 3
            sage: K.<a> = NumberField(p)
            sage: [K(k/3).round() for k in range(-3,4)]
            [-1, -1, 0, 0, 0, 1, 1]
            sage: a.round()
            Traceback (most recent call last):
            ...
            TypeError: floor not uniquely defined since no real embedding is specified"""
    @overload
    def round(self) -> Any:
        """NumberFieldElement.round(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 1262)

        Return the round (nearest integer) of this number field element. In case
        of ties, this relies on the default rounding for rational numbers.

        EXAMPLES::

            sage: x = polygen(ZZ)
            sage: p = x**7 - 5*x**2 + x + 1
            sage: a_AA = AA.polynomial_root(p, RIF(1,2))
            sage: K.<a> = NumberField(p, embedding=a_AA)
            sage: b = a**5 + a/2 - 1/7
            sage: RR(b)
            4.13444473767055
            sage: b.round()
            4
            sage: (-b).round()
            -4
            sage: (b + 1/2).round()
            5
            sage: (-b - 1/2).round()
            -5

        This function always succeeds even if a tremendous precision is needed::

            sage: c = b - 5678322907931/1225243417356 + 3
            sage: c.round()
            3
            sage: RIF(c).unique_round()
            Traceback (most recent call last):
            ...
            ValueError: interval does not have a unique round (nearest integer)

        If the number field is not embedded, this function is valid only if the
        element is rational::

            sage: p = x**5 - 3
            sage: K.<a> = NumberField(p)
            sage: [K(k/3).round() for k in range(-3,4)]
            [-1, -1, 0, 0, 0, 1, 1]
            sage: a.round()
            Traceback (most recent call last):
            ...
            TypeError: floor not uniquely defined since no real embedding is specified"""
    @overload
    def round(self) -> Any:
        """NumberFieldElement.round(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 1262)

        Return the round (nearest integer) of this number field element. In case
        of ties, this relies on the default rounding for rational numbers.

        EXAMPLES::

            sage: x = polygen(ZZ)
            sage: p = x**7 - 5*x**2 + x + 1
            sage: a_AA = AA.polynomial_root(p, RIF(1,2))
            sage: K.<a> = NumberField(p, embedding=a_AA)
            sage: b = a**5 + a/2 - 1/7
            sage: RR(b)
            4.13444473767055
            sage: b.round()
            4
            sage: (-b).round()
            -4
            sage: (b + 1/2).round()
            5
            sage: (-b - 1/2).round()
            -5

        This function always succeeds even if a tremendous precision is needed::

            sage: c = b - 5678322907931/1225243417356 + 3
            sage: c.round()
            3
            sage: RIF(c).unique_round()
            Traceback (most recent call last):
            ...
            ValueError: interval does not have a unique round (nearest integer)

        If the number field is not embedded, this function is valid only if the
        element is rational::

            sage: p = x**5 - 3
            sage: K.<a> = NumberField(p)
            sage: [K(k/3).round() for k in range(-3,4)]
            [-1, -1, 0, 0, 0, 1, 1]
            sage: a.round()
            Traceback (most recent call last):
            ...
            TypeError: floor not uniquely defined since no real embedding is specified"""
    @overload
    def round(self) -> Any:
        """NumberFieldElement.round(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 1262)

        Return the round (nearest integer) of this number field element. In case
        of ties, this relies on the default rounding for rational numbers.

        EXAMPLES::

            sage: x = polygen(ZZ)
            sage: p = x**7 - 5*x**2 + x + 1
            sage: a_AA = AA.polynomial_root(p, RIF(1,2))
            sage: K.<a> = NumberField(p, embedding=a_AA)
            sage: b = a**5 + a/2 - 1/7
            sage: RR(b)
            4.13444473767055
            sage: b.round()
            4
            sage: (-b).round()
            -4
            sage: (b + 1/2).round()
            5
            sage: (-b - 1/2).round()
            -5

        This function always succeeds even if a tremendous precision is needed::

            sage: c = b - 5678322907931/1225243417356 + 3
            sage: c.round()
            3
            sage: RIF(c).unique_round()
            Traceback (most recent call last):
            ...
            ValueError: interval does not have a unique round (nearest integer)

        If the number field is not embedded, this function is valid only if the
        element is rational::

            sage: p = x**5 - 3
            sage: K.<a> = NumberField(p)
            sage: [K(k/3).round() for k in range(-3,4)]
            [-1, -1, 0, 0, 0, 1, 1]
            sage: a.round()
            Traceback (most recent call last):
            ...
            TypeError: floor not uniquely defined since no real embedding is specified"""
    @overload
    def round(self, nearestinteger) -> Any:
        """NumberFieldElement.round(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 1262)

        Return the round (nearest integer) of this number field element. In case
        of ties, this relies on the default rounding for rational numbers.

        EXAMPLES::

            sage: x = polygen(ZZ)
            sage: p = x**7 - 5*x**2 + x + 1
            sage: a_AA = AA.polynomial_root(p, RIF(1,2))
            sage: K.<a> = NumberField(p, embedding=a_AA)
            sage: b = a**5 + a/2 - 1/7
            sage: RR(b)
            4.13444473767055
            sage: b.round()
            4
            sage: (-b).round()
            -4
            sage: (b + 1/2).round()
            5
            sage: (-b - 1/2).round()
            -5

        This function always succeeds even if a tremendous precision is needed::

            sage: c = b - 5678322907931/1225243417356 + 3
            sage: c.round()
            3
            sage: RIF(c).unique_round()
            Traceback (most recent call last):
            ...
            ValueError: interval does not have a unique round (nearest integer)

        If the number field is not embedded, this function is valid only if the
        element is rational::

            sage: p = x**5 - 3
            sage: K.<a> = NumberField(p)
            sage: [K(k/3).round() for k in range(-3,4)]
            [-1, -1, 0, 0, 0, 1, 1]
            sage: a.round()
            Traceback (most recent call last):
            ...
            TypeError: floor not uniquely defined since no real embedding is specified"""
    @overload
    def round(self) -> Any:
        """NumberFieldElement.round(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 1262)

        Return the round (nearest integer) of this number field element. In case
        of ties, this relies on the default rounding for rational numbers.

        EXAMPLES::

            sage: x = polygen(ZZ)
            sage: p = x**7 - 5*x**2 + x + 1
            sage: a_AA = AA.polynomial_root(p, RIF(1,2))
            sage: K.<a> = NumberField(p, embedding=a_AA)
            sage: b = a**5 + a/2 - 1/7
            sage: RR(b)
            4.13444473767055
            sage: b.round()
            4
            sage: (-b).round()
            -4
            sage: (b + 1/2).round()
            5
            sage: (-b - 1/2).round()
            -5

        This function always succeeds even if a tremendous precision is needed::

            sage: c = b - 5678322907931/1225243417356 + 3
            sage: c.round()
            3
            sage: RIF(c).unique_round()
            Traceback (most recent call last):
            ...
            ValueError: interval does not have a unique round (nearest integer)

        If the number field is not embedded, this function is valid only if the
        element is rational::

            sage: p = x**5 - 3
            sage: K.<a> = NumberField(p)
            sage: [K(k/3).round() for k in range(-3,4)]
            [-1, -1, 0, 0, 0, 1, 1]
            sage: a.round()
            Traceback (most recent call last):
            ...
            TypeError: floor not uniquely defined since no real embedding is specified"""
    @overload
    def round(self) -> Any:
        """NumberFieldElement.round(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 1262)

        Return the round (nearest integer) of this number field element. In case
        of ties, this relies on the default rounding for rational numbers.

        EXAMPLES::

            sage: x = polygen(ZZ)
            sage: p = x**7 - 5*x**2 + x + 1
            sage: a_AA = AA.polynomial_root(p, RIF(1,2))
            sage: K.<a> = NumberField(p, embedding=a_AA)
            sage: b = a**5 + a/2 - 1/7
            sage: RR(b)
            4.13444473767055
            sage: b.round()
            4
            sage: (-b).round()
            -4
            sage: (b + 1/2).round()
            5
            sage: (-b - 1/2).round()
            -5

        This function always succeeds even if a tremendous precision is needed::

            sage: c = b - 5678322907931/1225243417356 + 3
            sage: c.round()
            3
            sage: RIF(c).unique_round()
            Traceback (most recent call last):
            ...
            ValueError: interval does not have a unique round (nearest integer)

        If the number field is not embedded, this function is valid only if the
        element is rational::

            sage: p = x**5 - 3
            sage: K.<a> = NumberField(p)
            sage: [K(k/3).round() for k in range(-3,4)]
            [-1, -1, 0, 0, 0, 1, 1]
            sage: a.round()
            Traceback (most recent call last):
            ...
            TypeError: floor not uniquely defined since no real embedding is specified"""
    @overload
    def sign(self) -> Any:
        """NumberFieldElement.sign(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 1051)

        Return the sign of this algebraic number (if a real embedding is well
        defined)

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^3 - 2, embedding=AA(2)**(1/3))
            sage: K.zero().sign()
            0
            sage: K.one().sign()
            1
            sage: (-K.one()).sign()
            -1
            sage: a.sign()
            1
            sage: (a - 234917380309015/186454048314072).sign()
            1
            sage: (a - 3741049304830488/2969272800976409).sign()
            -1

        If the field is not embedded in real numbers, this method will only work
        for rational elements::

            sage: L.<b> = NumberField(x^4 - x - 1)
            sage: b.sign()
            Traceback (most recent call last):
            ...
            TypeError: sign not well defined since no real embedding is
            specified
            sage: L(-33/125).sign()
            -1
            sage: L.zero().sign()
            0"""
    @overload
    def sign(self) -> Any:
        """NumberFieldElement.sign(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 1051)

        Return the sign of this algebraic number (if a real embedding is well
        defined)

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^3 - 2, embedding=AA(2)**(1/3))
            sage: K.zero().sign()
            0
            sage: K.one().sign()
            1
            sage: (-K.one()).sign()
            -1
            sage: a.sign()
            1
            sage: (a - 234917380309015/186454048314072).sign()
            1
            sage: (a - 3741049304830488/2969272800976409).sign()
            -1

        If the field is not embedded in real numbers, this method will only work
        for rational elements::

            sage: L.<b> = NumberField(x^4 - x - 1)
            sage: b.sign()
            Traceback (most recent call last):
            ...
            TypeError: sign not well defined since no real embedding is
            specified
            sage: L(-33/125).sign()
            -1
            sage: L.zero().sign()
            0"""
    @overload
    def sign(self) -> Any:
        """NumberFieldElement.sign(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 1051)

        Return the sign of this algebraic number (if a real embedding is well
        defined)

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^3 - 2, embedding=AA(2)**(1/3))
            sage: K.zero().sign()
            0
            sage: K.one().sign()
            1
            sage: (-K.one()).sign()
            -1
            sage: a.sign()
            1
            sage: (a - 234917380309015/186454048314072).sign()
            1
            sage: (a - 3741049304830488/2969272800976409).sign()
            -1

        If the field is not embedded in real numbers, this method will only work
        for rational elements::

            sage: L.<b> = NumberField(x^4 - x - 1)
            sage: b.sign()
            Traceback (most recent call last):
            ...
            TypeError: sign not well defined since no real embedding is
            specified
            sage: L(-33/125).sign()
            -1
            sage: L.zero().sign()
            0"""
    @overload
    def sign(self) -> Any:
        """NumberFieldElement.sign(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 1051)

        Return the sign of this algebraic number (if a real embedding is well
        defined)

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^3 - 2, embedding=AA(2)**(1/3))
            sage: K.zero().sign()
            0
            sage: K.one().sign()
            1
            sage: (-K.one()).sign()
            -1
            sage: a.sign()
            1
            sage: (a - 234917380309015/186454048314072).sign()
            1
            sage: (a - 3741049304830488/2969272800976409).sign()
            -1

        If the field is not embedded in real numbers, this method will only work
        for rational elements::

            sage: L.<b> = NumberField(x^4 - x - 1)
            sage: b.sign()
            Traceback (most recent call last):
            ...
            TypeError: sign not well defined since no real embedding is
            specified
            sage: L(-33/125).sign()
            -1
            sage: L.zero().sign()
            0"""
    @overload
    def sign(self) -> Any:
        """NumberFieldElement.sign(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 1051)

        Return the sign of this algebraic number (if a real embedding is well
        defined)

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^3 - 2, embedding=AA(2)**(1/3))
            sage: K.zero().sign()
            0
            sage: K.one().sign()
            1
            sage: (-K.one()).sign()
            -1
            sage: a.sign()
            1
            sage: (a - 234917380309015/186454048314072).sign()
            1
            sage: (a - 3741049304830488/2969272800976409).sign()
            -1

        If the field is not embedded in real numbers, this method will only work
        for rational elements::

            sage: L.<b> = NumberField(x^4 - x - 1)
            sage: b.sign()
            Traceback (most recent call last):
            ...
            TypeError: sign not well defined since no real embedding is
            specified
            sage: L(-33/125).sign()
            -1
            sage: L.zero().sign()
            0"""
    @overload
    def sign(self) -> Any:
        """NumberFieldElement.sign(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 1051)

        Return the sign of this algebraic number (if a real embedding is well
        defined)

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^3 - 2, embedding=AA(2)**(1/3))
            sage: K.zero().sign()
            0
            sage: K.one().sign()
            1
            sage: (-K.one()).sign()
            -1
            sage: a.sign()
            1
            sage: (a - 234917380309015/186454048314072).sign()
            1
            sage: (a - 3741049304830488/2969272800976409).sign()
            -1

        If the field is not embedded in real numbers, this method will only work
        for rational elements::

            sage: L.<b> = NumberField(x^4 - x - 1)
            sage: b.sign()
            Traceback (most recent call last):
            ...
            TypeError: sign not well defined since no real embedding is
            specified
            sage: L(-33/125).sign()
            -1
            sage: L.zero().sign()
            0"""
    @overload
    def sign(self) -> Any:
        """NumberFieldElement.sign(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 1051)

        Return the sign of this algebraic number (if a real embedding is well
        defined)

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^3 - 2, embedding=AA(2)**(1/3))
            sage: K.zero().sign()
            0
            sage: K.one().sign()
            1
            sage: (-K.one()).sign()
            -1
            sage: a.sign()
            1
            sage: (a - 234917380309015/186454048314072).sign()
            1
            sage: (a - 3741049304830488/2969272800976409).sign()
            -1

        If the field is not embedded in real numbers, this method will only work
        for rational elements::

            sage: L.<b> = NumberField(x^4 - x - 1)
            sage: b.sign()
            Traceback (most recent call last):
            ...
            TypeError: sign not well defined since no real embedding is
            specified
            sage: L(-33/125).sign()
            -1
            sage: L.zero().sign()
            0"""
    @overload
    def sign(self) -> Any:
        """NumberFieldElement.sign(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 1051)

        Return the sign of this algebraic number (if a real embedding is well
        defined)

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^3 - 2, embedding=AA(2)**(1/3))
            sage: K.zero().sign()
            0
            sage: K.one().sign()
            1
            sage: (-K.one()).sign()
            -1
            sage: a.sign()
            1
            sage: (a - 234917380309015/186454048314072).sign()
            1
            sage: (a - 3741049304830488/2969272800976409).sign()
            -1

        If the field is not embedded in real numbers, this method will only work
        for rational elements::

            sage: L.<b> = NumberField(x^4 - x - 1)
            sage: b.sign()
            Traceback (most recent call last):
            ...
            TypeError: sign not well defined since no real embedding is
            specified
            sage: L(-33/125).sign()
            -1
            sage: L.zero().sign()
            0"""
    @overload
    def sign(self) -> Any:
        """NumberFieldElement.sign(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 1051)

        Return the sign of this algebraic number (if a real embedding is well
        defined)

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^3 - 2, embedding=AA(2)**(1/3))
            sage: K.zero().sign()
            0
            sage: K.one().sign()
            1
            sage: (-K.one()).sign()
            -1
            sage: a.sign()
            1
            sage: (a - 234917380309015/186454048314072).sign()
            1
            sage: (a - 3741049304830488/2969272800976409).sign()
            -1

        If the field is not embedded in real numbers, this method will only work
        for rational elements::

            sage: L.<b> = NumberField(x^4 - x - 1)
            sage: b.sign()
            Traceback (most recent call last):
            ...
            TypeError: sign not well defined since no real embedding is
            specified
            sage: L(-33/125).sign()
            -1
            sage: L.zero().sign()
            0"""
    @overload
    def sign(self) -> Any:
        """NumberFieldElement.sign(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 1051)

        Return the sign of this algebraic number (if a real embedding is well
        defined)

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^3 - 2, embedding=AA(2)**(1/3))
            sage: K.zero().sign()
            0
            sage: K.one().sign()
            1
            sage: (-K.one()).sign()
            -1
            sage: a.sign()
            1
            sage: (a - 234917380309015/186454048314072).sign()
            1
            sage: (a - 3741049304830488/2969272800976409).sign()
            -1

        If the field is not embedded in real numbers, this method will only work
        for rational elements::

            sage: L.<b> = NumberField(x^4 - x - 1)
            sage: b.sign()
            Traceback (most recent call last):
            ...
            TypeError: sign not well defined since no real embedding is
            specified
            sage: L(-33/125).sign()
            -1
            sage: L.zero().sign()
            0"""
    @overload
    def sqrt(self, all=..., extend=...) -> Any:
        """NumberFieldElement.sqrt(self, all=False, extend=True)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 2244)

        Return the square root of this number in the given number field.

        INPUT:

        - ``all`` -- boolean (default: ``False``); whether to return
          both square roots

        - ``extend`` -- boolean (default: ``True``); whether to extend
          the field by adding the square roots if needed

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^2 - 3)
            sage: K(3).sqrt()
            a
            sage: K(3).sqrt(all=True)
            [a, -a]
            sage: K(a^10).sqrt()
            9*a
            sage: K(49).sqrt()
            7
            sage: K(1+a).sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: a + 1 not a square in Number Field in a with defining polynomial x^2 - 3
            sage: K(0).sqrt()
            0
            sage: K((7+a)^2).sqrt(all=True)
            [a + 7, -a - 7]

        ::

            sage: K.<a> = CyclotomicField(7)
            sage: a.sqrt()
            a^4

        ::

            sage: K.<a> = NumberField(x^5 - x + 1)
            sage: (a^4 + a^2 - 3*a + 2).sqrt()
            a^3 - a^2

        Using the ``extend`` keyword::

            sage: K = QuadraticField(-5)
            sage: z = K(-7).sqrt(extend=True); z                                        # needs sage.symbolic
            sqrt(-7)
            sage: CyclotomicField(4)(4).sqrt(extend=False)
            2

        If ``extend=False`` an error is raised, if ``self`` is not a square::

            sage: K = QuadraticField(-5)
            sage: K(-7).sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: -7 not a square in Number Field in a
            with defining polynomial x^2 + 5 with a = 2.236067977499790?*I

        ALGORITHM: Use PARI to factor `x^2` `-` ``self`` in `K`."""
    @overload
    def sqrt(self) -> Any:
        """NumberFieldElement.sqrt(self, all=False, extend=True)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 2244)

        Return the square root of this number in the given number field.

        INPUT:

        - ``all`` -- boolean (default: ``False``); whether to return
          both square roots

        - ``extend`` -- boolean (default: ``True``); whether to extend
          the field by adding the square roots if needed

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^2 - 3)
            sage: K(3).sqrt()
            a
            sage: K(3).sqrt(all=True)
            [a, -a]
            sage: K(a^10).sqrt()
            9*a
            sage: K(49).sqrt()
            7
            sage: K(1+a).sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: a + 1 not a square in Number Field in a with defining polynomial x^2 - 3
            sage: K(0).sqrt()
            0
            sage: K((7+a)^2).sqrt(all=True)
            [a + 7, -a - 7]

        ::

            sage: K.<a> = CyclotomicField(7)
            sage: a.sqrt()
            a^4

        ::

            sage: K.<a> = NumberField(x^5 - x + 1)
            sage: (a^4 + a^2 - 3*a + 2).sqrt()
            a^3 - a^2

        Using the ``extend`` keyword::

            sage: K = QuadraticField(-5)
            sage: z = K(-7).sqrt(extend=True); z                                        # needs sage.symbolic
            sqrt(-7)
            sage: CyclotomicField(4)(4).sqrt(extend=False)
            2

        If ``extend=False`` an error is raised, if ``self`` is not a square::

            sage: K = QuadraticField(-5)
            sage: K(-7).sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: -7 not a square in Number Field in a
            with defining polynomial x^2 + 5 with a = 2.236067977499790?*I

        ALGORITHM: Use PARI to factor `x^2` `-` ``self`` in `K`."""
    @overload
    def sqrt(self, all=...) -> Any:
        """NumberFieldElement.sqrt(self, all=False, extend=True)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 2244)

        Return the square root of this number in the given number field.

        INPUT:

        - ``all`` -- boolean (default: ``False``); whether to return
          both square roots

        - ``extend`` -- boolean (default: ``True``); whether to extend
          the field by adding the square roots if needed

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^2 - 3)
            sage: K(3).sqrt()
            a
            sage: K(3).sqrt(all=True)
            [a, -a]
            sage: K(a^10).sqrt()
            9*a
            sage: K(49).sqrt()
            7
            sage: K(1+a).sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: a + 1 not a square in Number Field in a with defining polynomial x^2 - 3
            sage: K(0).sqrt()
            0
            sage: K((7+a)^2).sqrt(all=True)
            [a + 7, -a - 7]

        ::

            sage: K.<a> = CyclotomicField(7)
            sage: a.sqrt()
            a^4

        ::

            sage: K.<a> = NumberField(x^5 - x + 1)
            sage: (a^4 + a^2 - 3*a + 2).sqrt()
            a^3 - a^2

        Using the ``extend`` keyword::

            sage: K = QuadraticField(-5)
            sage: z = K(-7).sqrt(extend=True); z                                        # needs sage.symbolic
            sqrt(-7)
            sage: CyclotomicField(4)(4).sqrt(extend=False)
            2

        If ``extend=False`` an error is raised, if ``self`` is not a square::

            sage: K = QuadraticField(-5)
            sage: K(-7).sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: -7 not a square in Number Field in a
            with defining polynomial x^2 + 5 with a = 2.236067977499790?*I

        ALGORITHM: Use PARI to factor `x^2` `-` ``self`` in `K`."""
    @overload
    def sqrt(self) -> Any:
        """NumberFieldElement.sqrt(self, all=False, extend=True)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 2244)

        Return the square root of this number in the given number field.

        INPUT:

        - ``all`` -- boolean (default: ``False``); whether to return
          both square roots

        - ``extend`` -- boolean (default: ``True``); whether to extend
          the field by adding the square roots if needed

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^2 - 3)
            sage: K(3).sqrt()
            a
            sage: K(3).sqrt(all=True)
            [a, -a]
            sage: K(a^10).sqrt()
            9*a
            sage: K(49).sqrt()
            7
            sage: K(1+a).sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: a + 1 not a square in Number Field in a with defining polynomial x^2 - 3
            sage: K(0).sqrt()
            0
            sage: K((7+a)^2).sqrt(all=True)
            [a + 7, -a - 7]

        ::

            sage: K.<a> = CyclotomicField(7)
            sage: a.sqrt()
            a^4

        ::

            sage: K.<a> = NumberField(x^5 - x + 1)
            sage: (a^4 + a^2 - 3*a + 2).sqrt()
            a^3 - a^2

        Using the ``extend`` keyword::

            sage: K = QuadraticField(-5)
            sage: z = K(-7).sqrt(extend=True); z                                        # needs sage.symbolic
            sqrt(-7)
            sage: CyclotomicField(4)(4).sqrt(extend=False)
            2

        If ``extend=False`` an error is raised, if ``self`` is not a square::

            sage: K = QuadraticField(-5)
            sage: K(-7).sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: -7 not a square in Number Field in a
            with defining polynomial x^2 + 5 with a = 2.236067977499790?*I

        ALGORITHM: Use PARI to factor `x^2` `-` ``self`` in `K`."""
    @overload
    def sqrt(self) -> Any:
        """NumberFieldElement.sqrt(self, all=False, extend=True)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 2244)

        Return the square root of this number in the given number field.

        INPUT:

        - ``all`` -- boolean (default: ``False``); whether to return
          both square roots

        - ``extend`` -- boolean (default: ``True``); whether to extend
          the field by adding the square roots if needed

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^2 - 3)
            sage: K(3).sqrt()
            a
            sage: K(3).sqrt(all=True)
            [a, -a]
            sage: K(a^10).sqrt()
            9*a
            sage: K(49).sqrt()
            7
            sage: K(1+a).sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: a + 1 not a square in Number Field in a with defining polynomial x^2 - 3
            sage: K(0).sqrt()
            0
            sage: K((7+a)^2).sqrt(all=True)
            [a + 7, -a - 7]

        ::

            sage: K.<a> = CyclotomicField(7)
            sage: a.sqrt()
            a^4

        ::

            sage: K.<a> = NumberField(x^5 - x + 1)
            sage: (a^4 + a^2 - 3*a + 2).sqrt()
            a^3 - a^2

        Using the ``extend`` keyword::

            sage: K = QuadraticField(-5)
            sage: z = K(-7).sqrt(extend=True); z                                        # needs sage.symbolic
            sqrt(-7)
            sage: CyclotomicField(4)(4).sqrt(extend=False)
            2

        If ``extend=False`` an error is raised, if ``self`` is not a square::

            sage: K = QuadraticField(-5)
            sage: K(-7).sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: -7 not a square in Number Field in a
            with defining polynomial x^2 + 5 with a = 2.236067977499790?*I

        ALGORITHM: Use PARI to factor `x^2` `-` ``self`` in `K`."""
    @overload
    def sqrt(self, extend=...) -> Any:
        """NumberFieldElement.sqrt(self, all=False, extend=True)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 2244)

        Return the square root of this number in the given number field.

        INPUT:

        - ``all`` -- boolean (default: ``False``); whether to return
          both square roots

        - ``extend`` -- boolean (default: ``True``); whether to extend
          the field by adding the square roots if needed

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^2 - 3)
            sage: K(3).sqrt()
            a
            sage: K(3).sqrt(all=True)
            [a, -a]
            sage: K(a^10).sqrt()
            9*a
            sage: K(49).sqrt()
            7
            sage: K(1+a).sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: a + 1 not a square in Number Field in a with defining polynomial x^2 - 3
            sage: K(0).sqrt()
            0
            sage: K((7+a)^2).sqrt(all=True)
            [a + 7, -a - 7]

        ::

            sage: K.<a> = CyclotomicField(7)
            sage: a.sqrt()
            a^4

        ::

            sage: K.<a> = NumberField(x^5 - x + 1)
            sage: (a^4 + a^2 - 3*a + 2).sqrt()
            a^3 - a^2

        Using the ``extend`` keyword::

            sage: K = QuadraticField(-5)
            sage: z = K(-7).sqrt(extend=True); z                                        # needs sage.symbolic
            sqrt(-7)
            sage: CyclotomicField(4)(4).sqrt(extend=False)
            2

        If ``extend=False`` an error is raised, if ``self`` is not a square::

            sage: K = QuadraticField(-5)
            sage: K(-7).sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: -7 not a square in Number Field in a
            with defining polynomial x^2 + 5 with a = 2.236067977499790?*I

        ALGORITHM: Use PARI to factor `x^2` `-` ``self`` in `K`."""
    @overload
    def sqrt(self) -> Any:
        """NumberFieldElement.sqrt(self, all=False, extend=True)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 2244)

        Return the square root of this number in the given number field.

        INPUT:

        - ``all`` -- boolean (default: ``False``); whether to return
          both square roots

        - ``extend`` -- boolean (default: ``True``); whether to extend
          the field by adding the square roots if needed

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^2 - 3)
            sage: K(3).sqrt()
            a
            sage: K(3).sqrt(all=True)
            [a, -a]
            sage: K(a^10).sqrt()
            9*a
            sage: K(49).sqrt()
            7
            sage: K(1+a).sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: a + 1 not a square in Number Field in a with defining polynomial x^2 - 3
            sage: K(0).sqrt()
            0
            sage: K((7+a)^2).sqrt(all=True)
            [a + 7, -a - 7]

        ::

            sage: K.<a> = CyclotomicField(7)
            sage: a.sqrt()
            a^4

        ::

            sage: K.<a> = NumberField(x^5 - x + 1)
            sage: (a^4 + a^2 - 3*a + 2).sqrt()
            a^3 - a^2

        Using the ``extend`` keyword::

            sage: K = QuadraticField(-5)
            sage: z = K(-7).sqrt(extend=True); z                                        # needs sage.symbolic
            sqrt(-7)
            sage: CyclotomicField(4)(4).sqrt(extend=False)
            2

        If ``extend=False`` an error is raised, if ``self`` is not a square::

            sage: K = QuadraticField(-5)
            sage: K(-7).sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: -7 not a square in Number Field in a
            with defining polynomial x^2 + 5 with a = 2.236067977499790?*I

        ALGORITHM: Use PARI to factor `x^2` `-` ``self`` in `K`."""
    @overload
    def sqrt(self, all=...) -> Any:
        """NumberFieldElement.sqrt(self, all=False, extend=True)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 2244)

        Return the square root of this number in the given number field.

        INPUT:

        - ``all`` -- boolean (default: ``False``); whether to return
          both square roots

        - ``extend`` -- boolean (default: ``True``); whether to extend
          the field by adding the square roots if needed

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^2 - 3)
            sage: K(3).sqrt()
            a
            sage: K(3).sqrt(all=True)
            [a, -a]
            sage: K(a^10).sqrt()
            9*a
            sage: K(49).sqrt()
            7
            sage: K(1+a).sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: a + 1 not a square in Number Field in a with defining polynomial x^2 - 3
            sage: K(0).sqrt()
            0
            sage: K((7+a)^2).sqrt(all=True)
            [a + 7, -a - 7]

        ::

            sage: K.<a> = CyclotomicField(7)
            sage: a.sqrt()
            a^4

        ::

            sage: K.<a> = NumberField(x^5 - x + 1)
            sage: (a^4 + a^2 - 3*a + 2).sqrt()
            a^3 - a^2

        Using the ``extend`` keyword::

            sage: K = QuadraticField(-5)
            sage: z = K(-7).sqrt(extend=True); z                                        # needs sage.symbolic
            sqrt(-7)
            sage: CyclotomicField(4)(4).sqrt(extend=False)
            2

        If ``extend=False`` an error is raised, if ``self`` is not a square::

            sage: K = QuadraticField(-5)
            sage: K(-7).sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: -7 not a square in Number Field in a
            with defining polynomial x^2 + 5 with a = 2.236067977499790?*I

        ALGORITHM: Use PARI to factor `x^2` `-` ``self`` in `K`."""
    @overload
    def sqrt(self) -> Any:
        """NumberFieldElement.sqrt(self, all=False, extend=True)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 2244)

        Return the square root of this number in the given number field.

        INPUT:

        - ``all`` -- boolean (default: ``False``); whether to return
          both square roots

        - ``extend`` -- boolean (default: ``True``); whether to extend
          the field by adding the square roots if needed

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^2 - 3)
            sage: K(3).sqrt()
            a
            sage: K(3).sqrt(all=True)
            [a, -a]
            sage: K(a^10).sqrt()
            9*a
            sage: K(49).sqrt()
            7
            sage: K(1+a).sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: a + 1 not a square in Number Field in a with defining polynomial x^2 - 3
            sage: K(0).sqrt()
            0
            sage: K((7+a)^2).sqrt(all=True)
            [a + 7, -a - 7]

        ::

            sage: K.<a> = CyclotomicField(7)
            sage: a.sqrt()
            a^4

        ::

            sage: K.<a> = NumberField(x^5 - x + 1)
            sage: (a^4 + a^2 - 3*a + 2).sqrt()
            a^3 - a^2

        Using the ``extend`` keyword::

            sage: K = QuadraticField(-5)
            sage: z = K(-7).sqrt(extend=True); z                                        # needs sage.symbolic
            sqrt(-7)
            sage: CyclotomicField(4)(4).sqrt(extend=False)
            2

        If ``extend=False`` an error is raised, if ``self`` is not a square::

            sage: K = QuadraticField(-5)
            sage: K(-7).sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: -7 not a square in Number Field in a
            with defining polynomial x^2 + 5 with a = 2.236067977499790?*I

        ALGORITHM: Use PARI to factor `x^2` `-` ``self`` in `K`."""
    @overload
    def sqrt(self) -> Any:
        """NumberFieldElement.sqrt(self, all=False, extend=True)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 2244)

        Return the square root of this number in the given number field.

        INPUT:

        - ``all`` -- boolean (default: ``False``); whether to return
          both square roots

        - ``extend`` -- boolean (default: ``True``); whether to extend
          the field by adding the square roots if needed

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^2 - 3)
            sage: K(3).sqrt()
            a
            sage: K(3).sqrt(all=True)
            [a, -a]
            sage: K(a^10).sqrt()
            9*a
            sage: K(49).sqrt()
            7
            sage: K(1+a).sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: a + 1 not a square in Number Field in a with defining polynomial x^2 - 3
            sage: K(0).sqrt()
            0
            sage: K((7+a)^2).sqrt(all=True)
            [a + 7, -a - 7]

        ::

            sage: K.<a> = CyclotomicField(7)
            sage: a.sqrt()
            a^4

        ::

            sage: K.<a> = NumberField(x^5 - x + 1)
            sage: (a^4 + a^2 - 3*a + 2).sqrt()
            a^3 - a^2

        Using the ``extend`` keyword::

            sage: K = QuadraticField(-5)
            sage: z = K(-7).sqrt(extend=True); z                                        # needs sage.symbolic
            sqrt(-7)
            sage: CyclotomicField(4)(4).sqrt(extend=False)
            2

        If ``extend=False`` an error is raised, if ``self`` is not a square::

            sage: K = QuadraticField(-5)
            sage: K(-7).sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: -7 not a square in Number Field in a
            with defining polynomial x^2 + 5 with a = 2.236067977499790?*I

        ALGORITHM: Use PARI to factor `x^2` `-` ``self`` in `K`."""
    @overload
    def sqrt(self, extend=...) -> Any:
        """NumberFieldElement.sqrt(self, all=False, extend=True)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 2244)

        Return the square root of this number in the given number field.

        INPUT:

        - ``all`` -- boolean (default: ``False``); whether to return
          both square roots

        - ``extend`` -- boolean (default: ``True``); whether to extend
          the field by adding the square roots if needed

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^2 - 3)
            sage: K(3).sqrt()
            a
            sage: K(3).sqrt(all=True)
            [a, -a]
            sage: K(a^10).sqrt()
            9*a
            sage: K(49).sqrt()
            7
            sage: K(1+a).sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: a + 1 not a square in Number Field in a with defining polynomial x^2 - 3
            sage: K(0).sqrt()
            0
            sage: K((7+a)^2).sqrt(all=True)
            [a + 7, -a - 7]

        ::

            sage: K.<a> = CyclotomicField(7)
            sage: a.sqrt()
            a^4

        ::

            sage: K.<a> = NumberField(x^5 - x + 1)
            sage: (a^4 + a^2 - 3*a + 2).sqrt()
            a^3 - a^2

        Using the ``extend`` keyword::

            sage: K = QuadraticField(-5)
            sage: z = K(-7).sqrt(extend=True); z                                        # needs sage.symbolic
            sqrt(-7)
            sage: CyclotomicField(4)(4).sqrt(extend=False)
            2

        If ``extend=False`` an error is raised, if ``self`` is not a square::

            sage: K = QuadraticField(-5)
            sage: K(-7).sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: -7 not a square in Number Field in a
            with defining polynomial x^2 + 5 with a = 2.236067977499790?*I

        ALGORITHM: Use PARI to factor `x^2` `-` ``self`` in `K`."""
    @overload
    def sqrt(self, extend=...) -> Any:
        """NumberFieldElement.sqrt(self, all=False, extend=True)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 2244)

        Return the square root of this number in the given number field.

        INPUT:

        - ``all`` -- boolean (default: ``False``); whether to return
          both square roots

        - ``extend`` -- boolean (default: ``True``); whether to extend
          the field by adding the square roots if needed

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^2 - 3)
            sage: K(3).sqrt()
            a
            sage: K(3).sqrt(all=True)
            [a, -a]
            sage: K(a^10).sqrt()
            9*a
            sage: K(49).sqrt()
            7
            sage: K(1+a).sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: a + 1 not a square in Number Field in a with defining polynomial x^2 - 3
            sage: K(0).sqrt()
            0
            sage: K((7+a)^2).sqrt(all=True)
            [a + 7, -a - 7]

        ::

            sage: K.<a> = CyclotomicField(7)
            sage: a.sqrt()
            a^4

        ::

            sage: K.<a> = NumberField(x^5 - x + 1)
            sage: (a^4 + a^2 - 3*a + 2).sqrt()
            a^3 - a^2

        Using the ``extend`` keyword::

            sage: K = QuadraticField(-5)
            sage: z = K(-7).sqrt(extend=True); z                                        # needs sage.symbolic
            sqrt(-7)
            sage: CyclotomicField(4)(4).sqrt(extend=False)
            2

        If ``extend=False`` an error is raised, if ``self`` is not a square::

            sage: K = QuadraticField(-5)
            sage: K(-7).sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: -7 not a square in Number Field in a
            with defining polynomial x^2 + 5 with a = 2.236067977499790?*I

        ALGORITHM: Use PARI to factor `x^2` `-` ``self`` in `K`."""
    @overload
    def sqrt(self, extend=...) -> Any:
        """NumberFieldElement.sqrt(self, all=False, extend=True)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 2244)

        Return the square root of this number in the given number field.

        INPUT:

        - ``all`` -- boolean (default: ``False``); whether to return
          both square roots

        - ``extend`` -- boolean (default: ``True``); whether to extend
          the field by adding the square roots if needed

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^2 - 3)
            sage: K(3).sqrt()
            a
            sage: K(3).sqrt(all=True)
            [a, -a]
            sage: K(a^10).sqrt()
            9*a
            sage: K(49).sqrt()
            7
            sage: K(1+a).sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: a + 1 not a square in Number Field in a with defining polynomial x^2 - 3
            sage: K(0).sqrt()
            0
            sage: K((7+a)^2).sqrt(all=True)
            [a + 7, -a - 7]

        ::

            sage: K.<a> = CyclotomicField(7)
            sage: a.sqrt()
            a^4

        ::

            sage: K.<a> = NumberField(x^5 - x + 1)
            sage: (a^4 + a^2 - 3*a + 2).sqrt()
            a^3 - a^2

        Using the ``extend`` keyword::

            sage: K = QuadraticField(-5)
            sage: z = K(-7).sqrt(extend=True); z                                        # needs sage.symbolic
            sqrt(-7)
            sage: CyclotomicField(4)(4).sqrt(extend=False)
            2

        If ``extend=False`` an error is raised, if ``self`` is not a square::

            sage: K = QuadraticField(-5)
            sage: K(-7).sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: -7 not a square in Number Field in a
            with defining polynomial x^2 + 5 with a = 2.236067977499790?*I

        ALGORITHM: Use PARI to factor `x^2` `-` ``self`` in `K`."""
    @overload
    def support(self) -> Any:
        """NumberFieldElement.support(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 4261)

        Return the support of this number field element.

        OUTPUT: a sorted list of the prime ideals at which this number
        field element has nonzero valuation. An error is raised if the
        element is zero.

        EXAMPLES::

            sage: x = ZZ['x'].gen()
            sage: F.<t> = NumberField(x^3 - 2)

        ::

            sage: P5s = F(5).support()
            sage: P5s
            [Fractional ideal (t^2 + 1), Fractional ideal (t^2 - 2*t - 1)]
            sage: all(5 in P5 for P5 in P5s)
            True
            sage: all(P5.is_prime() for P5 in P5s)
            True
            sage: [ P5.norm() for P5 in P5s ]
            [5, 25]

        TESTS:

        It doesn't make sense to factor the ideal (0)::

            sage: F(0).support()
            Traceback (most recent call last):
            ...
            ArithmeticError: Support of 0 is not defined."""
    @overload
    def support(self) -> Any:
        """NumberFieldElement.support(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 4261)

        Return the support of this number field element.

        OUTPUT: a sorted list of the prime ideals at which this number
        field element has nonzero valuation. An error is raised if the
        element is zero.

        EXAMPLES::

            sage: x = ZZ['x'].gen()
            sage: F.<t> = NumberField(x^3 - 2)

        ::

            sage: P5s = F(5).support()
            sage: P5s
            [Fractional ideal (t^2 + 1), Fractional ideal (t^2 - 2*t - 1)]
            sage: all(5 in P5 for P5 in P5s)
            True
            sage: all(P5.is_prime() for P5 in P5s)
            True
            sage: [ P5.norm() for P5 in P5s ]
            [5, 25]

        TESTS:

        It doesn't make sense to factor the ideal (0)::

            sage: F(0).support()
            Traceback (most recent call last):
            ...
            ArithmeticError: Support of 0 is not defined."""
    def trace(self, K=...) -> Any:
        """NumberFieldElement.trace(self, K=None)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 3497)

        Return the absolute or relative trace of this number field
        element.

        If `K` is given, then `K` must be a subfield of the parent `L` of ``self``, in
        which case the trace is the relative trace from `L` to `K`. In all
        other cases, the trace is the absolute trace down to `\\QQ`.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^3 - 132/7*x^2 + x + 1); K
            Number Field in a with defining polynomial x^3 - 132/7*x^2 + x + 1
            sage: a.trace()
            132/7
            sage: (a + 1).trace() == a.trace() + 3
            True

        If we are in an order, the trace is an integer::

            sage: K.<zeta> = CyclotomicField(17)
            sage: R = K.ring_of_integers()
            sage: R(zeta).trace().parent()
            Integer Ring

        TESTS::

            sage: F.<z> = CyclotomicField(5); t = 3*z**3 + 4*z**2 + 2
            sage: t.trace(F)
            3*z^3 + 4*z^2 + 2"""
    @overload
    def valuation(self, P) -> Any:
        """NumberFieldElement.valuation(self, P)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 3878)

        Return the valuation of ``self`` at a given prime ideal `P`.

        INPUT:

        - ``P`` -- a prime ideal of the parent of ``self``

        .. NOTE::

            The method :meth:`ord` is an alias for :meth:`valuation`.

        EXAMPLES::

            sage: R.<x> = QQ[]
            sage: K.<a> = NumberField(x^4 + 3*x^2 - 17)
            sage: P = K.ideal(61).factor()[0][0]
            sage: b = a^2 + 30
            sage: b.valuation(P)
            1
            sage: b.ord(P)
            1
            sage: type(b.valuation(P))
            <class 'sage.rings.integer.Integer'>

        The function can be applied to elements in relative number fields::

            sage: L.<b> = K.extension(x^2 - 3)
            sage: [L(6).valuation(P) for P in L.primes_above(2)]
            [4]
            sage: [L(6).valuation(P) for P in L.primes_above(3)]
            [2, 2]

        TESTS:

        Some checks for :issue:`29215`::

            sage: K = QuadraticField(-5)
            sage: v = QuadraticField(3).ideal(5)
            sage: K(33).valuation(v)
            Traceback (most recent call last):
            ...
            ValueError: P must be an ideal in the same number field

            sage: K(33).valuation(5)
            Traceback (most recent call last):
            ...
            TypeError: P must be an ideal

            sage: w = K.ideal(5)
            sage: K(33).valuation(w)
            Traceback (most recent call last):
            ...
            ValueError: P must be prime"""
    @overload
    def valuation(self, P) -> Any:
        """NumberFieldElement.valuation(self, P)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 3878)

        Return the valuation of ``self`` at a given prime ideal `P`.

        INPUT:

        - ``P`` -- a prime ideal of the parent of ``self``

        .. NOTE::

            The method :meth:`ord` is an alias for :meth:`valuation`.

        EXAMPLES::

            sage: R.<x> = QQ[]
            sage: K.<a> = NumberField(x^4 + 3*x^2 - 17)
            sage: P = K.ideal(61).factor()[0][0]
            sage: b = a^2 + 30
            sage: b.valuation(P)
            1
            sage: b.ord(P)
            1
            sage: type(b.valuation(P))
            <class 'sage.rings.integer.Integer'>

        The function can be applied to elements in relative number fields::

            sage: L.<b> = K.extension(x^2 - 3)
            sage: [L(6).valuation(P) for P in L.primes_above(2)]
            [4]
            sage: [L(6).valuation(P) for P in L.primes_above(3)]
            [2, 2]

        TESTS:

        Some checks for :issue:`29215`::

            sage: K = QuadraticField(-5)
            sage: v = QuadraticField(3).ideal(5)
            sage: K(33).valuation(v)
            Traceback (most recent call last):
            ...
            ValueError: P must be an ideal in the same number field

            sage: K(33).valuation(5)
            Traceback (most recent call last):
            ...
            TypeError: P must be an ideal

            sage: w = K.ideal(5)
            sage: K(33).valuation(w)
            Traceback (most recent call last):
            ...
            ValueError: P must be prime"""
    @overload
    def valuation(self, P) -> Any:
        """NumberFieldElement.valuation(self, P)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 3878)

        Return the valuation of ``self`` at a given prime ideal `P`.

        INPUT:

        - ``P`` -- a prime ideal of the parent of ``self``

        .. NOTE::

            The method :meth:`ord` is an alias for :meth:`valuation`.

        EXAMPLES::

            sage: R.<x> = QQ[]
            sage: K.<a> = NumberField(x^4 + 3*x^2 - 17)
            sage: P = K.ideal(61).factor()[0][0]
            sage: b = a^2 + 30
            sage: b.valuation(P)
            1
            sage: b.ord(P)
            1
            sage: type(b.valuation(P))
            <class 'sage.rings.integer.Integer'>

        The function can be applied to elements in relative number fields::

            sage: L.<b> = K.extension(x^2 - 3)
            sage: [L(6).valuation(P) for P in L.primes_above(2)]
            [4]
            sage: [L(6).valuation(P) for P in L.primes_above(3)]
            [2, 2]

        TESTS:

        Some checks for :issue:`29215`::

            sage: K = QuadraticField(-5)
            sage: v = QuadraticField(3).ideal(5)
            sage: K(33).valuation(v)
            Traceback (most recent call last):
            ...
            ValueError: P must be an ideal in the same number field

            sage: K(33).valuation(5)
            Traceback (most recent call last):
            ...
            TypeError: P must be an ideal

            sage: w = K.ideal(5)
            sage: K(33).valuation(w)
            Traceback (most recent call last):
            ...
            ValueError: P must be prime"""
    @overload
    def valuation(self, P) -> Any:
        """NumberFieldElement.valuation(self, P)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 3878)

        Return the valuation of ``self`` at a given prime ideal `P`.

        INPUT:

        - ``P`` -- a prime ideal of the parent of ``self``

        .. NOTE::

            The method :meth:`ord` is an alias for :meth:`valuation`.

        EXAMPLES::

            sage: R.<x> = QQ[]
            sage: K.<a> = NumberField(x^4 + 3*x^2 - 17)
            sage: P = K.ideal(61).factor()[0][0]
            sage: b = a^2 + 30
            sage: b.valuation(P)
            1
            sage: b.ord(P)
            1
            sage: type(b.valuation(P))
            <class 'sage.rings.integer.Integer'>

        The function can be applied to elements in relative number fields::

            sage: L.<b> = K.extension(x^2 - 3)
            sage: [L(6).valuation(P) for P in L.primes_above(2)]
            [4]
            sage: [L(6).valuation(P) for P in L.primes_above(3)]
            [2, 2]

        TESTS:

        Some checks for :issue:`29215`::

            sage: K = QuadraticField(-5)
            sage: v = QuadraticField(3).ideal(5)
            sage: K(33).valuation(v)
            Traceback (most recent call last):
            ...
            ValueError: P must be an ideal in the same number field

            sage: K(33).valuation(5)
            Traceback (most recent call last):
            ...
            TypeError: P must be an ideal

            sage: w = K.ideal(5)
            sage: K(33).valuation(w)
            Traceback (most recent call last):
            ...
            ValueError: P must be prime"""
    @overload
    def valuation(self, P) -> Any:
        """NumberFieldElement.valuation(self, P)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 3878)

        Return the valuation of ``self`` at a given prime ideal `P`.

        INPUT:

        - ``P`` -- a prime ideal of the parent of ``self``

        .. NOTE::

            The method :meth:`ord` is an alias for :meth:`valuation`.

        EXAMPLES::

            sage: R.<x> = QQ[]
            sage: K.<a> = NumberField(x^4 + 3*x^2 - 17)
            sage: P = K.ideal(61).factor()[0][0]
            sage: b = a^2 + 30
            sage: b.valuation(P)
            1
            sage: b.ord(P)
            1
            sage: type(b.valuation(P))
            <class 'sage.rings.integer.Integer'>

        The function can be applied to elements in relative number fields::

            sage: L.<b> = K.extension(x^2 - 3)
            sage: [L(6).valuation(P) for P in L.primes_above(2)]
            [4]
            sage: [L(6).valuation(P) for P in L.primes_above(3)]
            [2, 2]

        TESTS:

        Some checks for :issue:`29215`::

            sage: K = QuadraticField(-5)
            sage: v = QuadraticField(3).ideal(5)
            sage: K(33).valuation(v)
            Traceback (most recent call last):
            ...
            ValueError: P must be an ideal in the same number field

            sage: K(33).valuation(5)
            Traceback (most recent call last):
            ...
            TypeError: P must be an ideal

            sage: w = K.ideal(5)
            sage: K(33).valuation(w)
            Traceback (most recent call last):
            ...
            ValueError: P must be prime"""
    @overload
    def valuation(self, v) -> Any:
        """NumberFieldElement.valuation(self, P)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 3878)

        Return the valuation of ``self`` at a given prime ideal `P`.

        INPUT:

        - ``P`` -- a prime ideal of the parent of ``self``

        .. NOTE::

            The method :meth:`ord` is an alias for :meth:`valuation`.

        EXAMPLES::

            sage: R.<x> = QQ[]
            sage: K.<a> = NumberField(x^4 + 3*x^2 - 17)
            sage: P = K.ideal(61).factor()[0][0]
            sage: b = a^2 + 30
            sage: b.valuation(P)
            1
            sage: b.ord(P)
            1
            sage: type(b.valuation(P))
            <class 'sage.rings.integer.Integer'>

        The function can be applied to elements in relative number fields::

            sage: L.<b> = K.extension(x^2 - 3)
            sage: [L(6).valuation(P) for P in L.primes_above(2)]
            [4]
            sage: [L(6).valuation(P) for P in L.primes_above(3)]
            [2, 2]

        TESTS:

        Some checks for :issue:`29215`::

            sage: K = QuadraticField(-5)
            sage: v = QuadraticField(3).ideal(5)
            sage: K(33).valuation(v)
            Traceback (most recent call last):
            ...
            ValueError: P must be an ideal in the same number field

            sage: K(33).valuation(5)
            Traceback (most recent call last):
            ...
            TypeError: P must be an ideal

            sage: w = K.ideal(5)
            sage: K(33).valuation(w)
            Traceback (most recent call last):
            ...
            ValueError: P must be prime"""
    @overload
    def valuation(self, w) -> Any:
        """NumberFieldElement.valuation(self, P)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 3878)

        Return the valuation of ``self`` at a given prime ideal `P`.

        INPUT:

        - ``P`` -- a prime ideal of the parent of ``self``

        .. NOTE::

            The method :meth:`ord` is an alias for :meth:`valuation`.

        EXAMPLES::

            sage: R.<x> = QQ[]
            sage: K.<a> = NumberField(x^4 + 3*x^2 - 17)
            sage: P = K.ideal(61).factor()[0][0]
            sage: b = a^2 + 30
            sage: b.valuation(P)
            1
            sage: b.ord(P)
            1
            sage: type(b.valuation(P))
            <class 'sage.rings.integer.Integer'>

        The function can be applied to elements in relative number fields::

            sage: L.<b> = K.extension(x^2 - 3)
            sage: [L(6).valuation(P) for P in L.primes_above(2)]
            [4]
            sage: [L(6).valuation(P) for P in L.primes_above(3)]
            [2, 2]

        TESTS:

        Some checks for :issue:`29215`::

            sage: K = QuadraticField(-5)
            sage: v = QuadraticField(3).ideal(5)
            sage: K(33).valuation(v)
            Traceback (most recent call last):
            ...
            ValueError: P must be an ideal in the same number field

            sage: K(33).valuation(5)
            Traceback (most recent call last):
            ...
            TypeError: P must be an ideal

            sage: w = K.ideal(5)
            sage: K(33).valuation(w)
            Traceback (most recent call last):
            ...
            ValueError: P must be prime"""
    @overload
    def vector(self) -> Any:
        """NumberFieldElement.vector(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 3650)

        Return vector representation of ``self`` in terms of the basis for the
        ambient number field.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^2 + 1)
            sage: (2/3*a - 5/6).vector()
            (-5/6, 2/3)
            sage: (-5/6, 2/3)
            (-5/6, 2/3)
            sage: O = K.order(2*a)
            sage: (O.1).vector()
            (0, 2)
            sage: K.<a,b> = NumberField([x^2 + 1, x^2 - 3])
            sage: (a + b).vector()
            (b, 1)
            sage: O = K.order([a,b])
            sage: (O.1).vector()
            (-b, 1)
            sage: (O.2).vector()
            (1, -b)"""
    @overload
    def vector(self) -> Any:
        """NumberFieldElement.vector(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 3650)

        Return vector representation of ``self`` in terms of the basis for the
        ambient number field.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^2 + 1)
            sage: (2/3*a - 5/6).vector()
            (-5/6, 2/3)
            sage: (-5/6, 2/3)
            (-5/6, 2/3)
            sage: O = K.order(2*a)
            sage: (O.1).vector()
            (0, 2)
            sage: K.<a,b> = NumberField([x^2 + 1, x^2 - 3])
            sage: (a + b).vector()
            (b, 1)
            sage: O = K.order([a,b])
            sage: (O.1).vector()
            (-b, 1)
            sage: (O.2).vector()
            (1, -b)"""
    @overload
    def vector(self) -> Any:
        """NumberFieldElement.vector(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 3650)

        Return vector representation of ``self`` in terms of the basis for the
        ambient number field.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^2 + 1)
            sage: (2/3*a - 5/6).vector()
            (-5/6, 2/3)
            sage: (-5/6, 2/3)
            (-5/6, 2/3)
            sage: O = K.order(2*a)
            sage: (O.1).vector()
            (0, 2)
            sage: K.<a,b> = NumberField([x^2 + 1, x^2 - 3])
            sage: (a + b).vector()
            (b, 1)
            sage: O = K.order([a,b])
            sage: (O.1).vector()
            (-b, 1)
            sage: (O.2).vector()
            (1, -b)"""
    @overload
    def vector(self) -> Any:
        """NumberFieldElement.vector(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 3650)

        Return vector representation of ``self`` in terms of the basis for the
        ambient number field.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^2 + 1)
            sage: (2/3*a - 5/6).vector()
            (-5/6, 2/3)
            sage: (-5/6, 2/3)
            (-5/6, 2/3)
            sage: O = K.order(2*a)
            sage: (O.1).vector()
            (0, 2)
            sage: K.<a,b> = NumberField([x^2 + 1, x^2 - 3])
            sage: (a + b).vector()
            (b, 1)
            sage: O = K.order([a,b])
            sage: (O.1).vector()
            (-b, 1)
            sage: (O.2).vector()
            (1, -b)"""
    @overload
    def vector(self) -> Any:
        """NumberFieldElement.vector(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 3650)

        Return vector representation of ``self`` in terms of the basis for the
        ambient number field.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^2 + 1)
            sage: (2/3*a - 5/6).vector()
            (-5/6, 2/3)
            sage: (-5/6, 2/3)
            (-5/6, 2/3)
            sage: O = K.order(2*a)
            sage: (O.1).vector()
            (0, 2)
            sage: K.<a,b> = NumberField([x^2 + 1, x^2 - 3])
            sage: (a + b).vector()
            (b, 1)
            sage: O = K.order([a,b])
            sage: (O.1).vector()
            (-b, 1)
            sage: (O.2).vector()
            (1, -b)"""
    @overload
    def vector(self) -> Any:
        """NumberFieldElement.vector(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 3650)

        Return vector representation of ``self`` in terms of the basis for the
        ambient number field.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^2 + 1)
            sage: (2/3*a - 5/6).vector()
            (-5/6, 2/3)
            sage: (-5/6, 2/3)
            (-5/6, 2/3)
            sage: O = K.order(2*a)
            sage: (O.1).vector()
            (0, 2)
            sage: K.<a,b> = NumberField([x^2 + 1, x^2 - 3])
            sage: (a + b).vector()
            (b, 1)
            sage: O = K.order([a,b])
            sage: (O.1).vector()
            (-b, 1)
            sage: (O.2).vector()
            (1, -b)"""
    def __abs__(self) -> Any:
        """NumberFieldElement.__abs__(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 1010)

        Return the absolute value of this number field element.

        If a real-valued coercion embedding is defined, the
        returned absolute value is an element of the same field.

        Otherwise, it is the numerical absolute value with respect to
        the first archimedean embedding, to double precision.

        This is the :func:`abs` Python function. If you want a
        different embedding or precision, use ``self.abs(...)``.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: k.<a> = NumberField(x^3 - 2)
            sage: abs(a)
            1.25992104989487
            sage: a.abs()
            1.25992104989487
            sage: abs(a)^3
            2.00000000000000
            sage: a.abs()^3
            2.00000000000000
            sage: a.abs(prec=128)
            1.2599210498948731647672106072782283506

        Number field with a real-valued coercion embedding
        (:issue:`21105`)::

            sage: k.<cbrt2> = NumberField(x^3 - 2, embedding=1.26)
            sage: abs(cbrt2)
            cbrt2
            sage: cbrt2.abs()
            cbrt2
            sage: abs(cbrt2)^3
            2"""
    def __bool__(self) -> bool:
        """True if self else False"""
    @overload
    def __complex__(self) -> Any:
        """NumberFieldElement.__complex__(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 1962)

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: k.<a> = NumberField(x^2 + 1)
            sage: complex(a)
            1j
            sage: a.__complex__()
            1j"""
    @overload
    def __complex__(self) -> Any:
        """NumberFieldElement.__complex__(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 1962)

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: k.<a> = NumberField(x^2 + 1)
            sage: complex(a)
            1j
            sage: a.__complex__()
            1j"""
    def __copy__(self) -> Any:
        """NumberFieldElement.__copy__(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 2717)

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^3 + 2)
            sage: b = copy(a)
            sage: b is a
            True"""
    def __deepcopy__(self, memo) -> Any:
        """NumberFieldElement.__deepcopy__(self, memo)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 2730)

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^3 + 2)
            sage: b = deepcopy(a)
            sage: b is a
            True"""
    @overload
    def __float__(self) -> Any:
        """NumberFieldElement.__float__(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 1923)

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: k.<a> = NumberField(x^2 + 1)
            sage: float(a^2)
            -1.0
            sage: float(a)
            Traceback (most recent call last):
            ...
            TypeError: Unable to coerce a to a rational
            sage: (a^2).__float__()
            -1.0
            sage: k.<a> = NumberField(x^2 + 1,embedding=I)
            sage: float(a)
            Traceback (most recent call last):
            ...
            TypeError: unable to coerce to a real number"""
    @overload
    def __float__(self) -> Any:
        """NumberFieldElement.__float__(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 1923)

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: k.<a> = NumberField(x^2 + 1)
            sage: float(a^2)
            -1.0
            sage: float(a)
            Traceback (most recent call last):
            ...
            TypeError: Unable to coerce a to a rational
            sage: (a^2).__float__()
            -1.0
            sage: k.<a> = NumberField(x^2 + 1,embedding=I)
            sage: float(a)
            Traceback (most recent call last):
            ...
            TypeError: unable to coerce to a real number"""
    def __getitem__(self, n) -> Any:
        """NumberFieldElement.__getitem__(self, n)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 739)

        Return the ``n``-th coefficient of this number field element, written
        as a polynomial in the generator.

        Note that ``n`` must be between `0` and `d-1`, where
        `d` is the degree of the number field.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: m.<b> = NumberField(x^4 - 1789)
            sage: c = (2/3-4/5*b)^3; c
            -64/125*b^3 + 32/25*b^2 - 16/15*b + 8/27
            sage: c[0]
            8/27
            sage: c[2]
            32/25
            sage: c[3]
            -64/125

        We illustrate bounds checking::

            sage: c[-1]
            Traceback (most recent call last):
            ...
            IndexError: index must be between 0 and degree minus 1
            sage: c[4]
            Traceback (most recent call last):
            ...
            IndexError: index must be between 0 and degree minus 1

        The :func:`list` function implicitly calls :meth:`__getitem__`::

            sage: list(c)
            [8/27, -16/15, 32/25, -64/125]
            sage: m(list(c)) == c
            True"""
    def __hash__(self) -> Any:
        """NumberFieldElement.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 3201)

        Return hash of this number field element.

        It respects the hash values of rational numbers.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<b> = NumberField(x^3 - 2)
            sage: hash(b^2 + 1)   # random
            175247765440
            sage: hash(K(13)) == hash(13)
            True
            sage: hash(K(-2/3)) == hash(-2/3)
            True

        No collisions (even on low bits)::

            sage: from itertools import product
            sage: elts = []
            sage: for (i,j,k) in product((-1,0,1,2,3), repeat=3):
            ....:     x = i + j*b + k*b^2
            ....:     elts.append(x)
            ....:     if gcd([2,i,j,k]) == 1:
            ....:         elts.append(x / 2)
            ....:     if gcd([3,i,j,k]) == 1:
            ....:         elts.append(x / 3)
            sage: len(set(map(hash, elts))) == len(elts)
            True
            sage: len(set(hash(x)%(2^18) for x in elts)) == len(elts)
            True"""
    def __int__(self) -> Any:
        """NumberFieldElement.__int__(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 2743)

        Attempt to convert this number field element to a Python integer,
        if possible.

        EXAMPLES::

            sage: C.<I>=CyclotomicField(4)
            sage: int(1/I)
            Traceback (most recent call last):
            ...
            TypeError: cannot convert nonconstant polynomial
            sage: int(I*I)
            -1

        ::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^10 - x - 1)
            sage: int(a)
            Traceback (most recent call last):
            ...
            TypeError: cannot convert nonconstant polynomial
            sage: int(K(9390283))
            9390283

        The semantics are like in Python, so the value does not have to
        preserved.

        ::

            sage: int(K(393/29))
            13"""
    @overload
    def __invert__(self) -> Any:
        """NumberFieldElement.__invert__(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 2779)

        Return the multiplicative inverse of ``self`` in the number field.

        EXAMPLES::

            sage: C.<I>=CyclotomicField(4)
            sage: ~I
            -I
            sage: (2*I).__invert__()
            -1/2*I

        We check that :issue:`20693` has been resolved, i.e. number
        field elements with huge denominator can be inverted::

            sage: K.<zeta22> = CyclotomicField(22)
            sage: x = polygen(K)
            sage: f = x^9 + (zeta22^9 - zeta22^6 + zeta22^4 + 1)*x^8 + (2*zeta22^8 + 4*zeta22^7 - 6*zeta22^5 - 205*zeta22^4 - 6*zeta22^3 + 4*zeta22 + 2)*x^7 + (181*zeta22^9 - 354*zeta22^8 + 145*zeta22^7 - 253*zeta22^6 + 145*zeta22^5 - 354*zeta22^4 + 181*zeta22^3 + 189*zeta22 - 189)*x^6 + (902*zeta22^9 + 13116*zeta22^8 + 902*zeta22^7 - 500*zeta22^5 - 322*zeta22^4 - 176*zeta22^3 + 176*zeta22^2 + 322*zeta22 + 500)*x^5 + (13196*zeta22^9 + 548*zeta22^8 + 9176*zeta22^7 - 17964*zeta22^6 + 8512*zeta22^5 - 8512*zeta22^4 + 17964*zeta22^3 - 9176*zeta22^2 - 548*zeta22 - 13196)*x^4 + (17104*zeta22^9 + 23456*zeta22^8 + 8496*zeta22^7 - 8496*zeta22^6 - 23456*zeta22^5 - 17104*zeta22^4 + 39680*zeta22^2 + 283184*zeta22 + 39680)*x^3 + (118736*zeta22^9 - 118736*zeta22^8 - 93520*zeta22^6 + 225600*zeta22^5 + 66496*zeta22^4 + 373744*zeta22^3 + 66496*zeta22^2 + 225600*zeta22 - 93520)*x^2 + (342176*zeta22^9 + 388928*zeta22^8 + 4800*zeta22^7 - 234464*zeta22^6 - 1601152*zeta22^5 - 234464*zeta22^4 + 4800*zeta22^3 + 388928*zeta22^2 + 342176*zeta22)*x + 431552*zeta22^9 - 1830400*zeta22^8 - 1196800*zeta22^7 - 1830400*zeta22^6 + 431552*zeta22^5 + 1196096*zeta22^3 - 12672*zeta22^2 + 12672*zeta22 - 1196096
            sage: L.<a> = K.extension(f)
            sage: alpha = (a^8 + (zeta22^9 - zeta22^6 + 2*zeta22^4 + 33)*a^7)/(10**2555) #long time"""
    @overload
    def __invert__(self) -> Any:
        """NumberFieldElement.__invert__(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 2779)

        Return the multiplicative inverse of ``self`` in the number field.

        EXAMPLES::

            sage: C.<I>=CyclotomicField(4)
            sage: ~I
            -I
            sage: (2*I).__invert__()
            -1/2*I

        We check that :issue:`20693` has been resolved, i.e. number
        field elements with huge denominator can be inverted::

            sage: K.<zeta22> = CyclotomicField(22)
            sage: x = polygen(K)
            sage: f = x^9 + (zeta22^9 - zeta22^6 + zeta22^4 + 1)*x^8 + (2*zeta22^8 + 4*zeta22^7 - 6*zeta22^5 - 205*zeta22^4 - 6*zeta22^3 + 4*zeta22 + 2)*x^7 + (181*zeta22^9 - 354*zeta22^8 + 145*zeta22^7 - 253*zeta22^6 + 145*zeta22^5 - 354*zeta22^4 + 181*zeta22^3 + 189*zeta22 - 189)*x^6 + (902*zeta22^9 + 13116*zeta22^8 + 902*zeta22^7 - 500*zeta22^5 - 322*zeta22^4 - 176*zeta22^3 + 176*zeta22^2 + 322*zeta22 + 500)*x^5 + (13196*zeta22^9 + 548*zeta22^8 + 9176*zeta22^7 - 17964*zeta22^6 + 8512*zeta22^5 - 8512*zeta22^4 + 17964*zeta22^3 - 9176*zeta22^2 - 548*zeta22 - 13196)*x^4 + (17104*zeta22^9 + 23456*zeta22^8 + 8496*zeta22^7 - 8496*zeta22^6 - 23456*zeta22^5 - 17104*zeta22^4 + 39680*zeta22^2 + 283184*zeta22 + 39680)*x^3 + (118736*zeta22^9 - 118736*zeta22^8 - 93520*zeta22^6 + 225600*zeta22^5 + 66496*zeta22^4 + 373744*zeta22^3 + 66496*zeta22^2 + 225600*zeta22 - 93520)*x^2 + (342176*zeta22^9 + 388928*zeta22^8 + 4800*zeta22^7 - 234464*zeta22^6 - 1601152*zeta22^5 - 234464*zeta22^4 + 4800*zeta22^3 + 388928*zeta22^2 + 342176*zeta22)*x + 431552*zeta22^9 - 1830400*zeta22^8 - 1196800*zeta22^7 - 1830400*zeta22^6 + 431552*zeta22^5 + 1196096*zeta22^3 - 12672*zeta22^2 + 12672*zeta22 - 1196096
            sage: L.<a> = K.extension(f)
            sage: alpha = (a^8 + (zeta22^9 - zeta22^6 + 2*zeta22^4 + 33)*a^7)/(10**2555) #long time"""
    @overload
    def __pari__(self, name=...) -> Any:
        """NumberFieldElement.__pari__(self, name='y')

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 599)

        Return PARI representation of ``self``.

        The returned element is a PARI ``POLMOD`` in the variable
        ``name``, which is by default 'y' - not the name of the generator
        of the number field.

        INPUT:

        - ``name`` -- (default: ``'y'``) the PARI variable name used

        EXAMPLES::

            sage: # needs sage.libs.pari
            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^3 + 2)
            sage: K(1).__pari__()
            Mod(1, y^3 + 2)
            sage: (a + 2).__pari__()
            Mod(y + 2, y^3 + 2)
            sage: L.<b> = K.extension(x^2 + 2)
            sage: (b + a).__pari__()
            Mod(24/101*y^5 - 9/101*y^4 + 160/101*y^3 - 156/101*y^2 + 397/101*y + 364/101, y^6 + 6*y^4 - 4*y^3 + 12*y^2 + 24*y + 12)

        ::

            sage: k.<j> = QuadraticField(-1)
            sage: j.__pari__('j')                                                       # needs sage.libs.pari
            Mod(j, j^2 + 1)
            sage: pari(j)                                                               # needs sage.libs.pari
            Mod(y, y^2 + 1)

        By default the variable name is 'y'. This allows 'x' to be used
        as polynomial variable::

            sage: P.<a> = PolynomialRing(QQ)
            sage: K.<b> = NumberField(a^2 + 1)
            sage: R.<x> = PolynomialRing(K)
            sage: pari(b*x)                                                             # needs sage.libs.pari
            Mod(y, y^2 + 1)*x

        In PARI many variable names are reserved, for example ``theta``
        and ``I``::

            sage: R.<theta> = PolynomialRing(QQ)
            sage: K.<theta> = NumberField(theta^2 + 1)
            sage: theta.__pari__('theta')                                               # needs sage.libs.pari
            Traceback (most recent call last):
            ...
            PariError: theta already exists with incompatible valence
            sage: theta.__pari__()                                                      # needs sage.libs.pari
            Mod(y, y^2 + 1)
            sage: k.<I> = QuadraticField(-1)
            sage: I.__pari__('I')                                                       # needs sage.libs.pari
            Traceback (most recent call last):
            ...
            PariError: I already exists with incompatible valence

        Instead, request the variable be named different for the coercion::

            sage: pari(I)                                                               # needs sage.libs.pari
            Mod(y, y^2 + 1)
            sage: I.__pari__('i')                                                       # needs sage.libs.pari
            Mod(i, i^2 + 1)
            sage: I.__pari__('II')                                                      # needs sage.libs.pari
            Mod(II, II^2 + 1)

        Examples with relative number fields, which always yield an
        *absolute* representation of the element::

            sage: y = QQ['y'].gen()
            sage: k.<j> = NumberField([y^2 - 7, y^3 - 2])
            sage: pari(j)                                                               # needs sage.libs.pari
            Mod(42/5515*y^5 - 9/11030*y^4 - 196/1103*y^3 + 273/5515*y^2 + 10281/5515*y + 4459/11030, y^6 - 21*y^4 + 4*y^3 + 147*y^2 + 84*y - 339)
            sage: j^2
            7
            sage: pari(j)^2                                                             # needs sage.libs.pari
            Mod(7, y^6 - 21*y^4 + 4*y^3 + 147*y^2 + 84*y - 339)
            sage: (j^2).__pari__('x')                                                   # needs sage.libs.pari
            Mod(7, x^6 - 21*x^4 + 4*x^3 + 147*x^2 + 84*x - 339)

        A tower of three number fields::

            sage: x = polygen(QQ)
            sage: K.<a> = NumberField(x^2 + 2)
            sage: L.<b> = NumberField(polygen(K)^2 + a)
            sage: M.<c> = NumberField(polygen(L)^3 + b)
            sage: L(b).__pari__()                                                       # needs sage.libs.pari
            Mod(y, y^4 + 2)
            sage: M(b).__pari__('c')                                                    # needs sage.libs.pari
            Mod(-c^3, c^12 + 2)
            sage: c.__pari__('c')                                                       # needs sage.libs.pari
            Mod(c, c^12 + 2)"""
    @overload
    def __pari__(self) -> Any:
        """NumberFieldElement.__pari__(self, name='y')

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 599)

        Return PARI representation of ``self``.

        The returned element is a PARI ``POLMOD`` in the variable
        ``name``, which is by default 'y' - not the name of the generator
        of the number field.

        INPUT:

        - ``name`` -- (default: ``'y'``) the PARI variable name used

        EXAMPLES::

            sage: # needs sage.libs.pari
            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^3 + 2)
            sage: K(1).__pari__()
            Mod(1, y^3 + 2)
            sage: (a + 2).__pari__()
            Mod(y + 2, y^3 + 2)
            sage: L.<b> = K.extension(x^2 + 2)
            sage: (b + a).__pari__()
            Mod(24/101*y^5 - 9/101*y^4 + 160/101*y^3 - 156/101*y^2 + 397/101*y + 364/101, y^6 + 6*y^4 - 4*y^3 + 12*y^2 + 24*y + 12)

        ::

            sage: k.<j> = QuadraticField(-1)
            sage: j.__pari__('j')                                                       # needs sage.libs.pari
            Mod(j, j^2 + 1)
            sage: pari(j)                                                               # needs sage.libs.pari
            Mod(y, y^2 + 1)

        By default the variable name is 'y'. This allows 'x' to be used
        as polynomial variable::

            sage: P.<a> = PolynomialRing(QQ)
            sage: K.<b> = NumberField(a^2 + 1)
            sage: R.<x> = PolynomialRing(K)
            sage: pari(b*x)                                                             # needs sage.libs.pari
            Mod(y, y^2 + 1)*x

        In PARI many variable names are reserved, for example ``theta``
        and ``I``::

            sage: R.<theta> = PolynomialRing(QQ)
            sage: K.<theta> = NumberField(theta^2 + 1)
            sage: theta.__pari__('theta')                                               # needs sage.libs.pari
            Traceback (most recent call last):
            ...
            PariError: theta already exists with incompatible valence
            sage: theta.__pari__()                                                      # needs sage.libs.pari
            Mod(y, y^2 + 1)
            sage: k.<I> = QuadraticField(-1)
            sage: I.__pari__('I')                                                       # needs sage.libs.pari
            Traceback (most recent call last):
            ...
            PariError: I already exists with incompatible valence

        Instead, request the variable be named different for the coercion::

            sage: pari(I)                                                               # needs sage.libs.pari
            Mod(y, y^2 + 1)
            sage: I.__pari__('i')                                                       # needs sage.libs.pari
            Mod(i, i^2 + 1)
            sage: I.__pari__('II')                                                      # needs sage.libs.pari
            Mod(II, II^2 + 1)

        Examples with relative number fields, which always yield an
        *absolute* representation of the element::

            sage: y = QQ['y'].gen()
            sage: k.<j> = NumberField([y^2 - 7, y^3 - 2])
            sage: pari(j)                                                               # needs sage.libs.pari
            Mod(42/5515*y^5 - 9/11030*y^4 - 196/1103*y^3 + 273/5515*y^2 + 10281/5515*y + 4459/11030, y^6 - 21*y^4 + 4*y^3 + 147*y^2 + 84*y - 339)
            sage: j^2
            7
            sage: pari(j)^2                                                             # needs sage.libs.pari
            Mod(7, y^6 - 21*y^4 + 4*y^3 + 147*y^2 + 84*y - 339)
            sage: (j^2).__pari__('x')                                                   # needs sage.libs.pari
            Mod(7, x^6 - 21*x^4 + 4*x^3 + 147*x^2 + 84*x - 339)

        A tower of three number fields::

            sage: x = polygen(QQ)
            sage: K.<a> = NumberField(x^2 + 2)
            sage: L.<b> = NumberField(polygen(K)^2 + a)
            sage: M.<c> = NumberField(polygen(L)^3 + b)
            sage: L(b).__pari__()                                                       # needs sage.libs.pari
            Mod(y, y^4 + 2)
            sage: M(b).__pari__('c')                                                    # needs sage.libs.pari
            Mod(-c^3, c^12 + 2)
            sage: c.__pari__('c')                                                       # needs sage.libs.pari
            Mod(c, c^12 + 2)"""
    @overload
    def __pari__(self) -> Any:
        """NumberFieldElement.__pari__(self, name='y')

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 599)

        Return PARI representation of ``self``.

        The returned element is a PARI ``POLMOD`` in the variable
        ``name``, which is by default 'y' - not the name of the generator
        of the number field.

        INPUT:

        - ``name`` -- (default: ``'y'``) the PARI variable name used

        EXAMPLES::

            sage: # needs sage.libs.pari
            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^3 + 2)
            sage: K(1).__pari__()
            Mod(1, y^3 + 2)
            sage: (a + 2).__pari__()
            Mod(y + 2, y^3 + 2)
            sage: L.<b> = K.extension(x^2 + 2)
            sage: (b + a).__pari__()
            Mod(24/101*y^5 - 9/101*y^4 + 160/101*y^3 - 156/101*y^2 + 397/101*y + 364/101, y^6 + 6*y^4 - 4*y^3 + 12*y^2 + 24*y + 12)

        ::

            sage: k.<j> = QuadraticField(-1)
            sage: j.__pari__('j')                                                       # needs sage.libs.pari
            Mod(j, j^2 + 1)
            sage: pari(j)                                                               # needs sage.libs.pari
            Mod(y, y^2 + 1)

        By default the variable name is 'y'. This allows 'x' to be used
        as polynomial variable::

            sage: P.<a> = PolynomialRing(QQ)
            sage: K.<b> = NumberField(a^2 + 1)
            sage: R.<x> = PolynomialRing(K)
            sage: pari(b*x)                                                             # needs sage.libs.pari
            Mod(y, y^2 + 1)*x

        In PARI many variable names are reserved, for example ``theta``
        and ``I``::

            sage: R.<theta> = PolynomialRing(QQ)
            sage: K.<theta> = NumberField(theta^2 + 1)
            sage: theta.__pari__('theta')                                               # needs sage.libs.pari
            Traceback (most recent call last):
            ...
            PariError: theta already exists with incompatible valence
            sage: theta.__pari__()                                                      # needs sage.libs.pari
            Mod(y, y^2 + 1)
            sage: k.<I> = QuadraticField(-1)
            sage: I.__pari__('I')                                                       # needs sage.libs.pari
            Traceback (most recent call last):
            ...
            PariError: I already exists with incompatible valence

        Instead, request the variable be named different for the coercion::

            sage: pari(I)                                                               # needs sage.libs.pari
            Mod(y, y^2 + 1)
            sage: I.__pari__('i')                                                       # needs sage.libs.pari
            Mod(i, i^2 + 1)
            sage: I.__pari__('II')                                                      # needs sage.libs.pari
            Mod(II, II^2 + 1)

        Examples with relative number fields, which always yield an
        *absolute* representation of the element::

            sage: y = QQ['y'].gen()
            sage: k.<j> = NumberField([y^2 - 7, y^3 - 2])
            sage: pari(j)                                                               # needs sage.libs.pari
            Mod(42/5515*y^5 - 9/11030*y^4 - 196/1103*y^3 + 273/5515*y^2 + 10281/5515*y + 4459/11030, y^6 - 21*y^4 + 4*y^3 + 147*y^2 + 84*y - 339)
            sage: j^2
            7
            sage: pari(j)^2                                                             # needs sage.libs.pari
            Mod(7, y^6 - 21*y^4 + 4*y^3 + 147*y^2 + 84*y - 339)
            sage: (j^2).__pari__('x')                                                   # needs sage.libs.pari
            Mod(7, x^6 - 21*x^4 + 4*x^3 + 147*x^2 + 84*x - 339)

        A tower of three number fields::

            sage: x = polygen(QQ)
            sage: K.<a> = NumberField(x^2 + 2)
            sage: L.<b> = NumberField(polygen(K)^2 + a)
            sage: M.<c> = NumberField(polygen(L)^3 + b)
            sage: L(b).__pari__()                                                       # needs sage.libs.pari
            Mod(y, y^4 + 2)
            sage: M(b).__pari__('c')                                                    # needs sage.libs.pari
            Mod(-c^3, c^12 + 2)
            sage: c.__pari__('c')                                                       # needs sage.libs.pari
            Mod(c, c^12 + 2)"""
    @overload
    def __pari__(self) -> Any:
        """NumberFieldElement.__pari__(self, name='y')

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 599)

        Return PARI representation of ``self``.

        The returned element is a PARI ``POLMOD`` in the variable
        ``name``, which is by default 'y' - not the name of the generator
        of the number field.

        INPUT:

        - ``name`` -- (default: ``'y'``) the PARI variable name used

        EXAMPLES::

            sage: # needs sage.libs.pari
            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^3 + 2)
            sage: K(1).__pari__()
            Mod(1, y^3 + 2)
            sage: (a + 2).__pari__()
            Mod(y + 2, y^3 + 2)
            sage: L.<b> = K.extension(x^2 + 2)
            sage: (b + a).__pari__()
            Mod(24/101*y^5 - 9/101*y^4 + 160/101*y^3 - 156/101*y^2 + 397/101*y + 364/101, y^6 + 6*y^4 - 4*y^3 + 12*y^2 + 24*y + 12)

        ::

            sage: k.<j> = QuadraticField(-1)
            sage: j.__pari__('j')                                                       # needs sage.libs.pari
            Mod(j, j^2 + 1)
            sage: pari(j)                                                               # needs sage.libs.pari
            Mod(y, y^2 + 1)

        By default the variable name is 'y'. This allows 'x' to be used
        as polynomial variable::

            sage: P.<a> = PolynomialRing(QQ)
            sage: K.<b> = NumberField(a^2 + 1)
            sage: R.<x> = PolynomialRing(K)
            sage: pari(b*x)                                                             # needs sage.libs.pari
            Mod(y, y^2 + 1)*x

        In PARI many variable names are reserved, for example ``theta``
        and ``I``::

            sage: R.<theta> = PolynomialRing(QQ)
            sage: K.<theta> = NumberField(theta^2 + 1)
            sage: theta.__pari__('theta')                                               # needs sage.libs.pari
            Traceback (most recent call last):
            ...
            PariError: theta already exists with incompatible valence
            sage: theta.__pari__()                                                      # needs sage.libs.pari
            Mod(y, y^2 + 1)
            sage: k.<I> = QuadraticField(-1)
            sage: I.__pari__('I')                                                       # needs sage.libs.pari
            Traceback (most recent call last):
            ...
            PariError: I already exists with incompatible valence

        Instead, request the variable be named different for the coercion::

            sage: pari(I)                                                               # needs sage.libs.pari
            Mod(y, y^2 + 1)
            sage: I.__pari__('i')                                                       # needs sage.libs.pari
            Mod(i, i^2 + 1)
            sage: I.__pari__('II')                                                      # needs sage.libs.pari
            Mod(II, II^2 + 1)

        Examples with relative number fields, which always yield an
        *absolute* representation of the element::

            sage: y = QQ['y'].gen()
            sage: k.<j> = NumberField([y^2 - 7, y^3 - 2])
            sage: pari(j)                                                               # needs sage.libs.pari
            Mod(42/5515*y^5 - 9/11030*y^4 - 196/1103*y^3 + 273/5515*y^2 + 10281/5515*y + 4459/11030, y^6 - 21*y^4 + 4*y^3 + 147*y^2 + 84*y - 339)
            sage: j^2
            7
            sage: pari(j)^2                                                             # needs sage.libs.pari
            Mod(7, y^6 - 21*y^4 + 4*y^3 + 147*y^2 + 84*y - 339)
            sage: (j^2).__pari__('x')                                                   # needs sage.libs.pari
            Mod(7, x^6 - 21*x^4 + 4*x^3 + 147*x^2 + 84*x - 339)

        A tower of three number fields::

            sage: x = polygen(QQ)
            sage: K.<a> = NumberField(x^2 + 2)
            sage: L.<b> = NumberField(polygen(K)^2 + a)
            sage: M.<c> = NumberField(polygen(L)^3 + b)
            sage: L(b).__pari__()                                                       # needs sage.libs.pari
            Mod(y, y^4 + 2)
            sage: M(b).__pari__('c')                                                    # needs sage.libs.pari
            Mod(-c^3, c^12 + 2)
            sage: c.__pari__('c')                                                       # needs sage.libs.pari
            Mod(c, c^12 + 2)"""
    @overload
    def __pari__(self) -> Any:
        """NumberFieldElement.__pari__(self, name='y')

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 599)

        Return PARI representation of ``self``.

        The returned element is a PARI ``POLMOD`` in the variable
        ``name``, which is by default 'y' - not the name of the generator
        of the number field.

        INPUT:

        - ``name`` -- (default: ``'y'``) the PARI variable name used

        EXAMPLES::

            sage: # needs sage.libs.pari
            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^3 + 2)
            sage: K(1).__pari__()
            Mod(1, y^3 + 2)
            sage: (a + 2).__pari__()
            Mod(y + 2, y^3 + 2)
            sage: L.<b> = K.extension(x^2 + 2)
            sage: (b + a).__pari__()
            Mod(24/101*y^5 - 9/101*y^4 + 160/101*y^3 - 156/101*y^2 + 397/101*y + 364/101, y^6 + 6*y^4 - 4*y^3 + 12*y^2 + 24*y + 12)

        ::

            sage: k.<j> = QuadraticField(-1)
            sage: j.__pari__('j')                                                       # needs sage.libs.pari
            Mod(j, j^2 + 1)
            sage: pari(j)                                                               # needs sage.libs.pari
            Mod(y, y^2 + 1)

        By default the variable name is 'y'. This allows 'x' to be used
        as polynomial variable::

            sage: P.<a> = PolynomialRing(QQ)
            sage: K.<b> = NumberField(a^2 + 1)
            sage: R.<x> = PolynomialRing(K)
            sage: pari(b*x)                                                             # needs sage.libs.pari
            Mod(y, y^2 + 1)*x

        In PARI many variable names are reserved, for example ``theta``
        and ``I``::

            sage: R.<theta> = PolynomialRing(QQ)
            sage: K.<theta> = NumberField(theta^2 + 1)
            sage: theta.__pari__('theta')                                               # needs sage.libs.pari
            Traceback (most recent call last):
            ...
            PariError: theta already exists with incompatible valence
            sage: theta.__pari__()                                                      # needs sage.libs.pari
            Mod(y, y^2 + 1)
            sage: k.<I> = QuadraticField(-1)
            sage: I.__pari__('I')                                                       # needs sage.libs.pari
            Traceback (most recent call last):
            ...
            PariError: I already exists with incompatible valence

        Instead, request the variable be named different for the coercion::

            sage: pari(I)                                                               # needs sage.libs.pari
            Mod(y, y^2 + 1)
            sage: I.__pari__('i')                                                       # needs sage.libs.pari
            Mod(i, i^2 + 1)
            sage: I.__pari__('II')                                                      # needs sage.libs.pari
            Mod(II, II^2 + 1)

        Examples with relative number fields, which always yield an
        *absolute* representation of the element::

            sage: y = QQ['y'].gen()
            sage: k.<j> = NumberField([y^2 - 7, y^3 - 2])
            sage: pari(j)                                                               # needs sage.libs.pari
            Mod(42/5515*y^5 - 9/11030*y^4 - 196/1103*y^3 + 273/5515*y^2 + 10281/5515*y + 4459/11030, y^6 - 21*y^4 + 4*y^3 + 147*y^2 + 84*y - 339)
            sage: j^2
            7
            sage: pari(j)^2                                                             # needs sage.libs.pari
            Mod(7, y^6 - 21*y^4 + 4*y^3 + 147*y^2 + 84*y - 339)
            sage: (j^2).__pari__('x')                                                   # needs sage.libs.pari
            Mod(7, x^6 - 21*x^4 + 4*x^3 + 147*x^2 + 84*x - 339)

        A tower of three number fields::

            sage: x = polygen(QQ)
            sage: K.<a> = NumberField(x^2 + 2)
            sage: L.<b> = NumberField(polygen(K)^2 + a)
            sage: M.<c> = NumberField(polygen(L)^3 + b)
            sage: L(b).__pari__()                                                       # needs sage.libs.pari
            Mod(y, y^4 + 2)
            sage: M(b).__pari__('c')                                                    # needs sage.libs.pari
            Mod(-c^3, c^12 + 2)
            sage: c.__pari__('c')                                                       # needs sage.libs.pari
            Mod(c, c^12 + 2)"""
    @overload
    def __pari__(self) -> Any:
        """NumberFieldElement.__pari__(self, name='y')

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 599)

        Return PARI representation of ``self``.

        The returned element is a PARI ``POLMOD`` in the variable
        ``name``, which is by default 'y' - not the name of the generator
        of the number field.

        INPUT:

        - ``name`` -- (default: ``'y'``) the PARI variable name used

        EXAMPLES::

            sage: # needs sage.libs.pari
            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^3 + 2)
            sage: K(1).__pari__()
            Mod(1, y^3 + 2)
            sage: (a + 2).__pari__()
            Mod(y + 2, y^3 + 2)
            sage: L.<b> = K.extension(x^2 + 2)
            sage: (b + a).__pari__()
            Mod(24/101*y^5 - 9/101*y^4 + 160/101*y^3 - 156/101*y^2 + 397/101*y + 364/101, y^6 + 6*y^4 - 4*y^3 + 12*y^2 + 24*y + 12)

        ::

            sage: k.<j> = QuadraticField(-1)
            sage: j.__pari__('j')                                                       # needs sage.libs.pari
            Mod(j, j^2 + 1)
            sage: pari(j)                                                               # needs sage.libs.pari
            Mod(y, y^2 + 1)

        By default the variable name is 'y'. This allows 'x' to be used
        as polynomial variable::

            sage: P.<a> = PolynomialRing(QQ)
            sage: K.<b> = NumberField(a^2 + 1)
            sage: R.<x> = PolynomialRing(K)
            sage: pari(b*x)                                                             # needs sage.libs.pari
            Mod(y, y^2 + 1)*x

        In PARI many variable names are reserved, for example ``theta``
        and ``I``::

            sage: R.<theta> = PolynomialRing(QQ)
            sage: K.<theta> = NumberField(theta^2 + 1)
            sage: theta.__pari__('theta')                                               # needs sage.libs.pari
            Traceback (most recent call last):
            ...
            PariError: theta already exists with incompatible valence
            sage: theta.__pari__()                                                      # needs sage.libs.pari
            Mod(y, y^2 + 1)
            sage: k.<I> = QuadraticField(-1)
            sage: I.__pari__('I')                                                       # needs sage.libs.pari
            Traceback (most recent call last):
            ...
            PariError: I already exists with incompatible valence

        Instead, request the variable be named different for the coercion::

            sage: pari(I)                                                               # needs sage.libs.pari
            Mod(y, y^2 + 1)
            sage: I.__pari__('i')                                                       # needs sage.libs.pari
            Mod(i, i^2 + 1)
            sage: I.__pari__('II')                                                      # needs sage.libs.pari
            Mod(II, II^2 + 1)

        Examples with relative number fields, which always yield an
        *absolute* representation of the element::

            sage: y = QQ['y'].gen()
            sage: k.<j> = NumberField([y^2 - 7, y^3 - 2])
            sage: pari(j)                                                               # needs sage.libs.pari
            Mod(42/5515*y^5 - 9/11030*y^4 - 196/1103*y^3 + 273/5515*y^2 + 10281/5515*y + 4459/11030, y^6 - 21*y^4 + 4*y^3 + 147*y^2 + 84*y - 339)
            sage: j^2
            7
            sage: pari(j)^2                                                             # needs sage.libs.pari
            Mod(7, y^6 - 21*y^4 + 4*y^3 + 147*y^2 + 84*y - 339)
            sage: (j^2).__pari__('x')                                                   # needs sage.libs.pari
            Mod(7, x^6 - 21*x^4 + 4*x^3 + 147*x^2 + 84*x - 339)

        A tower of three number fields::

            sage: x = polygen(QQ)
            sage: K.<a> = NumberField(x^2 + 2)
            sage: L.<b> = NumberField(polygen(K)^2 + a)
            sage: M.<c> = NumberField(polygen(L)^3 + b)
            sage: L(b).__pari__()                                                       # needs sage.libs.pari
            Mod(y, y^4 + 2)
            sage: M(b).__pari__('c')                                                    # needs sage.libs.pari
            Mod(-c^3, c^12 + 2)
            sage: c.__pari__('c')                                                       # needs sage.libs.pari
            Mod(c, c^12 + 2)"""
    def __pow__(self, base, exp, dummy) -> Any:
        """NumberFieldElement.__pow__(base, exp, dummy)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 2377)

        EXAMPLES::

            sage: K.<sqrt2> = QuadraticField(2)
            sage: sqrt2^2
            2
            sage: sqrt2^5
            4*sqrt2
            sage: (1+sqrt2)^100
            66992092050551637663438906713182313772*sqrt2 + 94741125149636933417873079920900017937
            sage: (1+sqrt2)^-1
            sqrt2 - 1

        If the exponent is not integral, perform this operation in
        the symbolic ring::

            sage: sqrt2^(1/5)                                                           # needs sage.symbolic
            2^(1/10)
            sage: sqrt2^sqrt2                                                           # needs sage.symbolic
            2^(1/2*sqrt(2))

        Sage follows Python's convention `0^0 = 1`::

            sage: a = K(0)^0; a
            1
            sage: a.parent()
            Number Field in sqrt2 with defining polynomial x^2 - 2 with sqrt2 = 1.414213562373095?

        TESTS::

            sage: 2^I                                                                   # needs sage.symbolic
            2^I

        Test :issue:`14895`::

            sage: K.<sqrt2> = QuadraticField(2)
            sage: 2^sqrt2                                                               # needs sage.symbolic
            2^sqrt(2)
            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^2+1)
            sage: 2^a                                                                   # needs sage.symbolic
            Traceback (most recent call last):
            ...
            TypeError: no canonical coercion from Number Field in a with defining polynomial x^2 + 1 to Symbolic Ring"""
    @overload
    def __reduce__(self) -> Any:
        """NumberFieldElement.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 391)

        Used in pickling number field elements.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: k.<a> = NumberField(x^3 - 17*x^2 + 1)
            sage: t = a.__reduce__(); t
            (<class 'sage.rings.number_field.number_field_element.NumberFieldElement_absolute'>,
             (Number Field in a with defining polynomial x^3 - 17*x^2 + 1, x))
            sage: t[0](*t[1]) == a
            True

        ::

            sage: k.<a> = NumberField(x^3 - 2)
            sage: loads(dumps(a+1)) == a + 1 # indirect doctest
            True

        This also gets called for unpickling order elements; we check that
        :issue:`6462` is fixed::

            sage: L = NumberField(x^3 - x - 1,'a'); OL = L.maximal_order(); w = OL.0
            sage: loads(dumps(w)) == w # indirect doctest
            True"""
    @overload
    def __reduce__(self) -> Any:
        """NumberFieldElement.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 391)

        Used in pickling number field elements.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: k.<a> = NumberField(x^3 - 17*x^2 + 1)
            sage: t = a.__reduce__(); t
            (<class 'sage.rings.number_field.number_field_element.NumberFieldElement_absolute'>,
             (Number Field in a with defining polynomial x^3 - 17*x^2 + 1, x))
            sage: t[0](*t[1]) == a
            True

        ::

            sage: k.<a> = NumberField(x^3 - 2)
            sage: loads(dumps(a+1)) == a + 1 # indirect doctest
            True

        This also gets called for unpickling order elements; we check that
        :issue:`6462` is fixed::

            sage: L = NumberField(x^3 - x - 1,'a'); OL = L.maximal_order(); w = OL.0
            sage: loads(dumps(w)) == w # indirect doctest
            True"""
    def __rpow__(self, other):
        """Return pow(value, self, mod)."""

class NumberFieldElement_absolute(NumberFieldElement):
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    def absolute_charpoly(self, var=..., algorithm=...) -> Any:
        """NumberFieldElement_absolute.absolute_charpoly(self, var='x', algorithm=None)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 4701)

        Return the characteristic polynomial of this element over `\\QQ`.

        For the meaning of the optional argument ``algorithm``, see :meth:`charpoly`.

        EXAMPLES::

            sage: x = ZZ['x'].0
            sage: K.<a> = NumberField(x^4 + 2, 'a')
            sage: a.absolute_charpoly()
            x^4 + 2
            sage: a.absolute_charpoly('y')
            y^4 + 2
            sage: (-a^2).absolute_charpoly()
            x^4 + 4*x^2 + 4
            sage: (-a^2).absolute_minpoly()
            x^2 + 2

            sage: a.absolute_charpoly(algorithm='pari') == a.absolute_charpoly(algorithm='sage')
            True"""
    def absolute_minpoly(self, var=..., algorithm=...) -> Any:
        """NumberFieldElement_absolute.absolute_minpoly(self, var='x', algorithm=None)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 4725)

        Return the minimal polynomial of this element over
        `\\QQ`.

        For the meaning of the optional argument algorithm, see :meth:`charpoly`.

        EXAMPLES::

            sage: x = ZZ['x'].0
            sage: f = (x^10 - 5*x^9 + 15*x^8 - 68*x^7 + 81*x^6 - 221*x^5
            ....:       + 141*x^4 - 242*x^3 - 13*x^2 - 33*x - 135)
            sage: K.<a> = NumberField(f, 'a')
            sage: a.absolute_charpoly()
            x^10 - 5*x^9 + 15*x^8 - 68*x^7 + 81*x^6 - 221*x^5
             + 141*x^4 - 242*x^3 - 13*x^2 - 33*x - 135
            sage: a.absolute_charpoly('y')
            y^10 - 5*y^9 + 15*y^8 - 68*y^7 + 81*y^6 - 221*y^5
             + 141*y^4 - 242*y^3 - 13*y^2 - 33*y - 135
            sage: b = (-79/9995*a^9 + 52/9995*a^8 + 271/9995*a^7 + 1663/9995*a^6
            ....:       + 13204/9995*a^5 + 5573/9995*a^4 + 8435/1999*a^3
            ....:       - 3116/9995*a^2 + 7734/1999*a + 1620/1999)
            sage: b.absolute_charpoly()
            x^10 + 10*x^9 + 25*x^8 - 80*x^7 - 438*x^6 + 80*x^5
             + 2950*x^4 + 1520*x^3 - 10439*x^2 - 5130*x + 18225
            sage: b.absolute_minpoly()
            x^5 + 5*x^4 - 40*x^2 - 19*x + 135

            sage: b.absolute_minpoly(algorithm='pari') == b.absolute_minpoly(algorithm='sage')      # needs sage.libs.pari
            True"""
    def charpoly(self, var=..., algorithm=...) -> Any:
        """NumberFieldElement_absolute.charpoly(self, var='x', algorithm=None)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 4758)

        The characteristic polynomial of this element, over
        `\\QQ` if ``self`` is an element of a field, and over
        `\\ZZ` is ``self`` is an element of an order.

        This is the same as :meth:`absolute_charpoly` since
        this is an element of an absolute extension.

        The optional argument ``algorithm`` controls how the
        characteristic polynomial is computed: ``'pari'`` uses PARI,
        ``'sage'`` uses ``charpoly`` for Sage matrices.  The default value
        ``None`` means that ``'pari'`` is used for small degrees (up to the
        value of the constant ``TUNE_CHARPOLY_NF``, currently at 25),
        otherwise ``'sage'`` is used.  The constant ``TUNE_CHARPOLY_NF``
        should give reasonable performance on all architectures;
        however, if you feel the need to customize it to your own
        machine, see :issue:`5213` for a tuning script.

        EXAMPLES:

        We compute the characteristic polynomial of the cube root of `2`.

        ::

            sage: R.<x> = QQ[]
            sage: K.<a> = NumberField(x^3 - 2)
            sage: a.charpoly('x')
            x^3 - 2
            sage: a.charpoly('y').parent()
            Univariate Polynomial Ring in y over Rational Field

        TESTS::

            sage: R = K.ring_of_integers()
            sage: R(a).charpoly()
            x^3 - 2
            sage: R(a).charpoly().parent()
            Univariate Polynomial Ring in x over Integer Ring

            sage: R(a).charpoly(algorithm='pari') == R(a).charpoly(algorithm='sage')    # needs sage.libs.pari
            True"""
    def is_real_positive(self, min_prec=...) -> Any:
        """NumberFieldElement_absolute.is_real_positive(self, min_prec=53)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 4878)

        Using the ``n`` method of approximation, return ``True`` if
        ``self`` is a real positive number and ``False`` otherwise.
        This method is completely dependent of the embedding used by
        the ``n`` method.

        The algorithm first checks that ``self`` is not a strictly
        complex number. Then if ``self`` is not zero, by approximation
        more and more precise, the method answers ``True`` if the
        number is positive. Using :class:`RealInterval`, the result is
        guaranteed to be correct.

        For :class:`CyclotomicField`, the embedding is the natural one
        sending ``zetan`` on `\\cos(2*\\pi/n)`.

        EXAMPLES::

            sage: K.<a> = CyclotomicField(3)
            sage: (a + a^2).is_real_positive()
            False
            sage: (-a - a^2).is_real_positive()
            True
            sage: K.<a> = CyclotomicField(1000)
            sage: (a + a^(-1)).is_real_positive()
            True
            sage: K.<a> = CyclotomicField(1009)
            sage: d = a^252
            sage: (d + d.conjugate()).is_real_positive()
            True
            sage: d = a^253
            sage: (d + d.conjugate()).is_real_positive()
            False
            sage: K.<a> = QuadraticField(3)
            sage: a.is_real_positive()
            True
            sage: K.<a> = QuadraticField(-3)
            sage: a.is_real_positive()
            False
            sage: (a - a).is_real_positive()
            False"""
    def lift(self, var=...) -> Any:
        """NumberFieldElement_absolute.lift(self, var='x')

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 4864)

        Return an element of `\\QQ[x]`, where this number field element
        lives in `\\QQ[x]/(f(x))`.

        EXAMPLES::

            sage: K.<a> = QuadraticField(-3)
            sage: a.lift()
            x"""
    @overload
    def list(self) -> Any:
        """NumberFieldElement_absolute.list(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 4844)

        Return the list of coefficients of ``self`` written in terms of a power
        basis.

        EXAMPLES::

            sage: K.<z> = CyclotomicField(3)
            sage: (2 + 3/5*z).list()
            [2, 3/5]
            sage: (5*z).list()
            [0, 5]
            sage: K(3).list()
            [3, 0]"""
    @overload
    def list(self) -> Any:
        """NumberFieldElement_absolute.list(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 4844)

        Return the list of coefficients of ``self`` written in terms of a power
        basis.

        EXAMPLES::

            sage: K.<z> = CyclotomicField(3)
            sage: (2 + 3/5*z).list()
            [2, 3/5]
            sage: (5*z).list()
            [0, 5]
            sage: K(3).list()
            [3, 0]"""
    @overload
    def list(self) -> Any:
        """NumberFieldElement_absolute.list(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 4844)

        Return the list of coefficients of ``self`` written in terms of a power
        basis.

        EXAMPLES::

            sage: K.<z> = CyclotomicField(3)
            sage: (2 + 3/5*z).list()
            [2, 3/5]
            sage: (5*z).list()
            [0, 5]
            sage: K(3).list()
            [3, 0]"""
    @overload
    def list(self) -> Any:
        """NumberFieldElement_absolute.list(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 4844)

        Return the list of coefficients of ``self`` written in terms of a power
        basis.

        EXAMPLES::

            sage: K.<z> = CyclotomicField(3)
            sage: (2 + 3/5*z).list()
            [2, 3/5]
            sage: (5*z).list()
            [0, 5]
            sage: K(3).list()
            [3, 0]"""
    @overload
    def minpoly(self, var=..., algorithm=...) -> Any:
        """NumberFieldElement_absolute.minpoly(self, var='x', algorithm=None)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 4812)

        Return the minimal polynomial of this number field element.

        For the meaning of the optional argument ``algorithm``, see :meth:`charpoly`.

        EXAMPLES:

        We compute the characteristic polynomial of cube root of `2`.

        ::

            sage: R.<x> = QQ[]
            sage: K.<a> = NumberField(x^3 - 2)
            sage: a.minpoly('x')
            x^3 - 2
            sage: a.minpoly('y').parent()
            Univariate Polynomial Ring in y over Rational Field

        TESTS::

            sage: R = K.ring_of_integers()
            sage: R(a).minpoly()
            x^3 - 2
            sage: R(a).minpoly().parent()
            Univariate Polynomial Ring in x over Integer Ring

            sage: R(a).minpoly(algorithm='pari') == R(a).minpoly(algorithm='sage')
            True"""
    @overload
    def minpoly(self) -> Any:
        """NumberFieldElement_absolute.minpoly(self, var='x', algorithm=None)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 4812)

        Return the minimal polynomial of this number field element.

        For the meaning of the optional argument ``algorithm``, see :meth:`charpoly`.

        EXAMPLES:

        We compute the characteristic polynomial of cube root of `2`.

        ::

            sage: R.<x> = QQ[]
            sage: K.<a> = NumberField(x^3 - 2)
            sage: a.minpoly('x')
            x^3 - 2
            sage: a.minpoly('y').parent()
            Univariate Polynomial Ring in y over Rational Field

        TESTS::

            sage: R = K.ring_of_integers()
            sage: R(a).minpoly()
            x^3 - 2
            sage: R(a).minpoly().parent()
            Univariate Polynomial Ring in x over Integer Ring

            sage: R(a).minpoly(algorithm='pari') == R(a).minpoly(algorithm='sage')
            True"""
    @overload
    def minpoly(self) -> Any:
        """NumberFieldElement_absolute.minpoly(self, var='x', algorithm=None)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 4812)

        Return the minimal polynomial of this number field element.

        For the meaning of the optional argument ``algorithm``, see :meth:`charpoly`.

        EXAMPLES:

        We compute the characteristic polynomial of cube root of `2`.

        ::

            sage: R.<x> = QQ[]
            sage: K.<a> = NumberField(x^3 - 2)
            sage: a.minpoly('x')
            x^3 - 2
            sage: a.minpoly('y').parent()
            Univariate Polynomial Ring in y over Rational Field

        TESTS::

            sage: R = K.ring_of_integers()
            sage: R(a).minpoly()
            x^3 - 2
            sage: R(a).minpoly().parent()
            Univariate Polynomial Ring in x over Integer Ring

            sage: R(a).minpoly(algorithm='pari') == R(a).minpoly(algorithm='sage')
            True"""

class NumberFieldElement_relative(NumberFieldElement):
    """NumberFieldElement_relative(parent, f)

    File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 4932)

    The current relative number field element implementation
    does everything in terms of absolute polynomials.

    All conversions from relative polynomials, lists, vectors, etc.
    should happen in the parent."""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, parent, f) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 4940)

                EXAMPLES::

                    sage: x = polygen(ZZ, 'x')
                    sage: L.<a, b> = NumberField([x^2 + 1, x^2 + 2])
                    sage: type(a) # indirect doctest
                    <class 'sage.rings.number_field.number_field_element.NumberFieldElement_relative'>
        """
    def absolute_charpoly(self, var=..., algorithm=...) -> Any:
        """NumberFieldElement_relative.absolute_charpoly(self, var='x', algorithm=None)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 5115)

        The characteristic polynomial of this element over
        `\\QQ`.

        We construct a relative extension and find the characteristic
        polynomial over `\\QQ`.

        The optional argument ``algorithm`` controls how the
        characteristic polynomial is computed: ``'pari'`` uses PARI,
        ``'sage'`` uses ``charpoly`` for Sage matrices.  The default value
        ``None`` means that ``'pari'`` is used for small degrees (up to the
        value of the constant ``TUNE_CHARPOLY_NF``, currently at 25),
        otherwise ``'sage'`` is used.  The constant ``TUNE_CHARPOLY_NF``
        should give reasonable performance on all architectures;
        however, if you feel the need to customize it to your own
        machine, see :issue:`5213` for a tuning script.

        EXAMPLES::

            sage: R.<x> = QQ[]
            sage: K.<a> = NumberField(x^3-2)
            sage: S.<X> = K[]
            sage: L.<b> = NumberField(X^3 + 17); L
            Number Field in b with defining polynomial X^3 + 17 over its base field
            sage: b.absolute_charpoly()
            x^9 + 51*x^6 + 867*x^3 + 4913
            sage: b.charpoly()(b)
            0
            sage: a = L.0; a
            b
            sage: a.absolute_charpoly('x')
            x^9 + 51*x^6 + 867*x^3 + 4913
            sage: a.absolute_charpoly('y')
            y^9 + 51*y^6 + 867*y^3 + 4913

            sage: a.absolute_charpoly(algorithm='pari') == a.absolute_charpoly(algorithm='sage')    # needs sage.libs.pari
            True"""
    def absolute_minpoly(self, var=..., algorithm=...) -> Any:
        """NumberFieldElement_relative.absolute_minpoly(self, var='x', algorithm=None)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 5169)

        Return the minimal polynomial over `\\QQ` of this element.

        For the meaning of the optional argument ``algorithm``, see :meth:`absolute_charpoly`.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a, b> = NumberField([x^2 + 2, x^2 + 1000*x + 1])
            sage: y = K['y'].0
            sage: L.<c> = K.extension(y^2 + a*y + b)
            sage: c.absolute_charpoly()
            x^8 - 1996*x^6 + 996006*x^4 + 1997996*x^2 + 1
            sage: c.absolute_minpoly()
            x^8 - 1996*x^6 + 996006*x^4 + 1997996*x^2 + 1
            sage: L(a).absolute_charpoly()
            x^8 + 8*x^6 + 24*x^4 + 32*x^2 + 16
            sage: L(a).absolute_minpoly()
            x^2 + 2
            sage: L(b).absolute_charpoly()
            x^8 + 4000*x^7 + 6000004*x^6 + 4000012000*x^5 + 1000012000006*x^4
             + 4000012000*x^3 + 6000004*x^2 + 4000*x + 1
            sage: L(b).absolute_minpoly()
            x^2 + 1000*x + 1"""
    @overload
    def charpoly(self, var=...) -> Any:
        """NumberFieldElement_relative.charpoly(self, var='x')

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 5081)

        The characteristic polynomial of this element over its base field.

        EXAMPLES::

            sage: x = ZZ['x'].0
            sage: K.<a, b> = QQ.extension([x^2 + 2, x^5 + 400*x^4 + 11*x^2 + 2])
            sage: a.charpoly()
            x^2 + 2
            sage: b.charpoly()
            x^2 - 2*b*x + b^2
            sage: b.minpoly()
            x - b

            sage: K.<a, b> = NumberField([x^2 + 2, x^2 + 1000*x + 1])
            sage: y = K['y'].0
            sage: L.<c> = K.extension(y^2 + a*y + b)
            sage: c.charpoly()
            x^2 + a*x + b
            sage: c.minpoly()
            x^2 + a*x + b
            sage: L(a).charpoly()
            x^2 - 2*a*x - 2
            sage: L(a).minpoly()
            x - a
            sage: L(b).charpoly()
            x^2 - 2*b*x - 1000*b - 1
            sage: L(b).minpoly()
            x - b"""
    @overload
    def charpoly(self) -> Any:
        """NumberFieldElement_relative.charpoly(self, var='x')

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 5081)

        The characteristic polynomial of this element over its base field.

        EXAMPLES::

            sage: x = ZZ['x'].0
            sage: K.<a, b> = QQ.extension([x^2 + 2, x^5 + 400*x^4 + 11*x^2 + 2])
            sage: a.charpoly()
            x^2 + 2
            sage: b.charpoly()
            x^2 - 2*b*x + b^2
            sage: b.minpoly()
            x - b

            sage: K.<a, b> = NumberField([x^2 + 2, x^2 + 1000*x + 1])
            sage: y = K['y'].0
            sage: L.<c> = K.extension(y^2 + a*y + b)
            sage: c.charpoly()
            x^2 + a*x + b
            sage: c.minpoly()
            x^2 + a*x + b
            sage: L(a).charpoly()
            x^2 - 2*a*x - 2
            sage: L(a).minpoly()
            x - a
            sage: L(b).charpoly()
            x^2 - 2*b*x - 1000*b - 1
            sage: L(b).minpoly()
            x - b"""
    @overload
    def charpoly(self) -> Any:
        """NumberFieldElement_relative.charpoly(self, var='x')

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 5081)

        The characteristic polynomial of this element over its base field.

        EXAMPLES::

            sage: x = ZZ['x'].0
            sage: K.<a, b> = QQ.extension([x^2 + 2, x^5 + 400*x^4 + 11*x^2 + 2])
            sage: a.charpoly()
            x^2 + 2
            sage: b.charpoly()
            x^2 - 2*b*x + b^2
            sage: b.minpoly()
            x - b

            sage: K.<a, b> = NumberField([x^2 + 2, x^2 + 1000*x + 1])
            sage: y = K['y'].0
            sage: L.<c> = K.extension(y^2 + a*y + b)
            sage: c.charpoly()
            x^2 + a*x + b
            sage: c.minpoly()
            x^2 + a*x + b
            sage: L(a).charpoly()
            x^2 - 2*a*x - 2
            sage: L(a).minpoly()
            x - a
            sage: L(b).charpoly()
            x^2 - 2*b*x - 1000*b - 1
            sage: L(b).minpoly()
            x - b"""
    @overload
    def charpoly(self) -> Any:
        """NumberFieldElement_relative.charpoly(self, var='x')

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 5081)

        The characteristic polynomial of this element over its base field.

        EXAMPLES::

            sage: x = ZZ['x'].0
            sage: K.<a, b> = QQ.extension([x^2 + 2, x^5 + 400*x^4 + 11*x^2 + 2])
            sage: a.charpoly()
            x^2 + 2
            sage: b.charpoly()
            x^2 - 2*b*x + b^2
            sage: b.minpoly()
            x - b

            sage: K.<a, b> = NumberField([x^2 + 2, x^2 + 1000*x + 1])
            sage: y = K['y'].0
            sage: L.<c> = K.extension(y^2 + a*y + b)
            sage: c.charpoly()
            x^2 + a*x + b
            sage: c.minpoly()
            x^2 + a*x + b
            sage: L(a).charpoly()
            x^2 - 2*a*x - 2
            sage: L(a).minpoly()
            x - a
            sage: L(b).charpoly()
            x^2 - 2*b*x - 1000*b - 1
            sage: L(b).minpoly()
            x - b"""
    @overload
    def charpoly(self) -> Any:
        """NumberFieldElement_relative.charpoly(self, var='x')

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 5081)

        The characteristic polynomial of this element over its base field.

        EXAMPLES::

            sage: x = ZZ['x'].0
            sage: K.<a, b> = QQ.extension([x^2 + 2, x^5 + 400*x^4 + 11*x^2 + 2])
            sage: a.charpoly()
            x^2 + 2
            sage: b.charpoly()
            x^2 - 2*b*x + b^2
            sage: b.minpoly()
            x - b

            sage: K.<a, b> = NumberField([x^2 + 2, x^2 + 1000*x + 1])
            sage: y = K['y'].0
            sage: L.<c> = K.extension(y^2 + a*y + b)
            sage: c.charpoly()
            x^2 + a*x + b
            sage: c.minpoly()
            x^2 + a*x + b
            sage: L(a).charpoly()
            x^2 - 2*a*x - 2
            sage: L(a).minpoly()
            x - a
            sage: L(b).charpoly()
            x^2 - 2*b*x - 1000*b - 1
            sage: L(b).minpoly()
            x - b"""
    @overload
    def charpoly(self) -> Any:
        """NumberFieldElement_relative.charpoly(self, var='x')

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 5081)

        The characteristic polynomial of this element over its base field.

        EXAMPLES::

            sage: x = ZZ['x'].0
            sage: K.<a, b> = QQ.extension([x^2 + 2, x^5 + 400*x^4 + 11*x^2 + 2])
            sage: a.charpoly()
            x^2 + 2
            sage: b.charpoly()
            x^2 - 2*b*x + b^2
            sage: b.minpoly()
            x - b

            sage: K.<a, b> = NumberField([x^2 + 2, x^2 + 1000*x + 1])
            sage: y = K['y'].0
            sage: L.<c> = K.extension(y^2 + a*y + b)
            sage: c.charpoly()
            x^2 + a*x + b
            sage: c.minpoly()
            x^2 + a*x + b
            sage: L(a).charpoly()
            x^2 - 2*a*x - 2
            sage: L(a).minpoly()
            x - a
            sage: L(b).charpoly()
            x^2 - 2*b*x - 1000*b - 1
            sage: L(b).minpoly()
            x - b"""
    @overload
    def lift(self, var=...) -> Any:
        """NumberFieldElement_relative.lift(self, var='x')

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 5021)

        Return an element of `K[x]`, where this number field element
        lives in the relative number field `K[x]/(f(x))`.

        EXAMPLES::

            sage: K.<a> = QuadraticField(-3)
            sage: x = polygen(K)
            sage: L.<b> = K.extension(x^7 + 5)
            sage: u = L(1/2*a + 1/2 + b + (a-9)*b^5)
            sage: u.lift()
            (a - 9)*x^5 + x + 1/2*a + 1/2"""
    @overload
    def lift(self) -> Any:
        """NumberFieldElement_relative.lift(self, var='x')

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 5021)

        Return an element of `K[x]`, where this number field element
        lives in the relative number field `K[x]/(f(x))`.

        EXAMPLES::

            sage: K.<a> = QuadraticField(-3)
            sage: x = polygen(K)
            sage: L.<b> = K.extension(x^7 + 5)
            sage: u = L(1/2*a + 1/2 + b + (a-9)*b^5)
            sage: u.lift()
            (a - 9)*x^5 + x + 1/2*a + 1/2"""
    @overload
    def list(self) -> Any:
        """NumberFieldElement_relative.list(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 5003)

        Return the list of coefficients of ``self`` written in terms of a power
        basis.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a,b> = NumberField([x^3 + 2, x^2 + 1])
            sage: a.list()
            [0, 1, 0]
            sage: v = (K.base_field().0 + a)^2; v
            a^2 + 2*b*a - 1
            sage: v.list()
            [-1, 2*b, 1]"""
    @overload
    def list(self) -> Any:
        """NumberFieldElement_relative.list(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 5003)

        Return the list of coefficients of ``self`` written in terms of a power
        basis.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a,b> = NumberField([x^3 + 2, x^2 + 1])
            sage: a.list()
            [0, 1, 0]
            sage: v = (K.base_field().0 + a)^2; v
            a^2 + 2*b*a - 1
            sage: v.list()
            [-1, 2*b, 1]"""
    @overload
    def list(self) -> Any:
        """NumberFieldElement_relative.list(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 5003)

        Return the list of coefficients of ``self`` written in terms of a power
        basis.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a,b> = NumberField([x^3 + 2, x^2 + 1])
            sage: a.list()
            [0, 1, 0]
            sage: v = (K.base_field().0 + a)^2; v
            a^2 + 2*b*a - 1
            sage: v.list()
            [-1, 2*b, 1]"""
    @overload
    def valuation(self, P) -> Any:
        """NumberFieldElement_relative.valuation(self, P)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 5197)

        Return the valuation of ``self`` at a given prime ideal `P`.

        INPUT:

        - ``P`` -- a prime ideal of relative number field which is the parent
          of ``self``

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a, b, c> = NumberField([x^2 - 2, x^2 - 3, x^2 - 5])
            sage: P = K.prime_factors(5)[1]
            sage: (2*a + b - c).valuation(P)
            1"""
    @overload
    def valuation(self, P) -> Any:
        """NumberFieldElement_relative.valuation(self, P)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 5197)

        Return the valuation of ``self`` at a given prime ideal `P`.

        INPUT:

        - ``P`` -- a prime ideal of relative number field which is the parent
          of ``self``

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a, b, c> = NumberField([x^2 - 2, x^2 - 3, x^2 - 5])
            sage: P = K.prime_factors(5)[1]
            sage: (2*a + b - c).valuation(P)
            1"""
    def __getitem__(self, n) -> Any:
        """NumberFieldElement_relative.__getitem__(self, n)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 4951)

        Return the `n`-th coefficient of this relative number field element, written
        as a polynomial in the generator.

        Note that `n` must be between 0 and `d-1`, where
        `d` is the relative degree of the number field.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a, b> = NumberField([x^3 - 5, x^2 + 3])
            sage: c = (a + b)^3; c
            3*b*a^2 - 9*a - 3*b + 5
            sage: c[0]
            -3*b + 5

        We illustrate bounds checking::

            sage: c[-1]
            Traceback (most recent call last):
            ...
            IndexError: index must be between 0 and the relative degree minus 1.
            sage: c[4]
            Traceback (most recent call last):
            ...
            IndexError: index must be between 0 and the relative degree minus 1.

        The list method implicitly calls ``__getitem__``::

            sage: list(c)
            [-3*b + 5, -9, 3*b]
            sage: K(list(c)) == c
            True"""

class OrderElement_absolute(NumberFieldElement_absolute):
    """OrderElement_absolute(order, f)

    File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 5220)

    Element of an order in an absolute number field.

    EXAMPLES::

        sage: x = polygen(ZZ, 'x')
        sage: K.<a> = NumberField(x^2 + 1)
        sage: O2 = K.order(2*a)
        sage: w = O2.1; w
        2*a
        sage: parent(w)
        Order of conductor 2 generated by 2*a in Number Field in a with defining polynomial x^2 + 1

        sage: w.absolute_charpoly()
        x^2 + 4
        sage: w.absolute_charpoly().parent()
        Univariate Polynomial Ring in x over Integer Ring
        sage: w.absolute_minpoly()
        x^2 + 4
        sage: w.absolute_minpoly().parent()
        Univariate Polynomial Ring in x over Integer Ring"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, order, f) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 5243)

                EXAMPLES::

                    sage: x = polygen(ZZ, 'x')
                    sage: K.<a> = NumberField(x^3 + 2)
                    sage: O2 = K.order(2*a)
                    sage: type(O2.1) # indirect doctest
                    <class 'sage.rings.number_field.number_field_element.OrderElement_absolute'>
        """
    @overload
    def canonical_associate(self) -> Any:
        """OrderElement_absolute.canonical_associate(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 5346)

        Return a canonical associate.

        Only implemented here because order elements inherit from field elements,
        but the canonical associate implemented there does not apply here.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K = NumberField(x^3 - x + 2, 'a')
            sage: OK = K.ring_of_integers()
            sage: (OK.1).canonical_associate()
            NotImplemented"""
    @overload
    def canonical_associate(self) -> Any:
        """OrderElement_absolute.canonical_associate(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 5346)

        Return a canonical associate.

        Only implemented here because order elements inherit from field elements,
        but the canonical associate implemented there does not apply here.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K = NumberField(x^3 - x + 2, 'a')
            sage: OK = K.ring_of_integers()
            sage: (OK.1).canonical_associate()
            NotImplemented"""
    def inverse_mod(self, I) -> Any:
        """OrderElement_absolute.inverse_mod(self, I)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 5295)

        Return an inverse of ``self`` modulo the given ideal.

        INPUT:

        - ``I`` -- may be an ideal of ``self.parent()``, or an element or list
          of elements of ``self.parent()`` generating a nonzero ideal. A
          :exc:`ValueError` is raised if `I` is non-integral or is zero. A
          :exc:`ZeroDivisionError` is raised if `I + (x) \\neq (1)`.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: OE.<w> = EquationOrder(x^3 - x + 2)
            sage: w.inverse_mod(13)
            6*w^2 - 6
            sage: w * (w.inverse_mod(13)) - 1 in 13*OE.number_field()
            True
            sage: w.inverse_mod(13).parent() == OE
            True
            sage: w.inverse_mod(2)
            Traceback (most recent call last):
            ...
            ZeroDivisionError: w is not invertible modulo Fractional ideal (2)"""
    def __invert__(self) -> Any:
        """OrderElement_absolute.__invert__(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 5324)

        Implement inversion, checking that the return value has the right
        parent.

        See :issue:`4190`.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K = NumberField(x^3 - x + 2, 'a')
            sage: OK = K.ring_of_integers()
            sage: a = OK(K.gen())
            sage: (~a).parent() is K
            True
            sage: (~a) in OK
            False
            sage: a**(-1) in OK
            False"""

class OrderElement_relative(NumberFieldElement_relative):
    """OrderElement_relative(order, f)

    File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 5364)

    Element of an order in a relative number field.

    EXAMPLES::

        sage: x = polygen(ZZ, 'x')
        sage: O = EquationOrder([x^2 + x + 1, x^3 - 2], 'a,b')
        sage: c = O.1; c
        (-2*b^2 - 2)*a - 2*b^2 - b
        sage: type(c)
        <class 'sage.rings.number_field.number_field_element.OrderElement_relative'>"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, order, f) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 5377)

                EXAMPLES::

                    sage: x = polygen(ZZ, 'x')
                    sage: O = EquationOrder([x^2 + x + 1, x^3 - 2], 'a,b')
                    sage: type(O.1)  # indirect doctest
                    <class 'sage.rings.number_field.number_field_element.OrderElement_relative'>
        """
    def absolute_charpoly(self, var=...) -> Any:
        """OrderElement_relative.absolute_charpoly(self, var='x')

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 5530)

        The absolute characteristic polynomial of this order element over `\\ZZ`.

        EXAMPLES::

            sage: x = ZZ['x'].0
            sage: K.<a,b> = NumberField([x^2 + 1, x^2 - 3])
            sage: OK = K.maximal_order()
            sage: _, u, _, v = OK.basis()
            sage: t = 2*u - v; t
            -b
            sage: t.absolute_charpoly()
            x^4 - 6*x^2 + 9
            sage: t.absolute_minpoly()
            x^2 - 3
            sage: t.absolute_charpoly().parent()
            Univariate Polynomial Ring in x over Integer Ring"""
    def absolute_minpoly(self, var=...) -> Any:
        """OrderElement_relative.absolute_minpoly(self, var='x')

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 5553)

        The absolute minimal polynomial of this order element over `\\ZZ`.

        EXAMPLES::

            sage: x = ZZ['x'].0
            sage: K.<a,b> = NumberField([x^2 + 1, x^2 - 3])
            sage: OK = K.maximal_order()
            sage: _, u, _, v = OK.basis()
            sage: t = 2*u - v; t
            -b
            sage: t.absolute_charpoly()
            x^4 - 6*x^2 + 9
            sage: t.absolute_minpoly()
            x^2 - 3
            sage: t.absolute_minpoly().parent()
            Univariate Polynomial Ring in x over Integer Ring"""
    @overload
    def canonical_associate(self) -> Any:
        """OrderElement_relative.canonical_associate(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 5576)

        Return a canonical associate.

        Only implemented here because order elements inherit from
        field elements, but the canonical associate implemented there
        does not apply here.

        EXAMPLES::

            sage: x = ZZ['x'].0
            sage: K.<a,b> = NumberField([x^2 + 1, x^2 - 3])
            sage: OK = K.maximal_order()
            sage: (OK.1).canonical_associate()
            NotImplemented"""
    @overload
    def canonical_associate(self) -> Any:
        """OrderElement_relative.canonical_associate(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 5576)

        Return a canonical associate.

        Only implemented here because order elements inherit from
        field elements, but the canonical associate implemented there
        does not apply here.

        EXAMPLES::

            sage: x = ZZ['x'].0
            sage: K.<a,b> = NumberField([x^2 + 1, x^2 - 3])
            sage: OK = K.maximal_order()
            sage: (OK.1).canonical_associate()
            NotImplemented"""
    def charpoly(self, var=...) -> Any:
        """OrderElement_relative.charpoly(self, var='x')

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 5469)

        The characteristic polynomial of this order element over its base ring.

        This special implementation works around :issue:`4738`.  At this
        time the base ring of relative order elements is `\\ZZ`; it should
        be the ring of integers of the base field.

        EXAMPLES::

            sage: x = ZZ['x'].0
            sage: K.<a,b> = NumberField([x^2 + 1, x^2 - 3])
            sage: OK = K.maximal_order(); OK.basis()
            [1, 1/2*a - 1/2*b, -1/2*b*a + 1/2, a]
            sage: charpoly(OK.1)
            x^2 + b*x + 1
            sage: charpoly(OK.1).parent()
            Univariate Polynomial Ring in x over Maximal Order generated by b
             in Number Field in b with defining polynomial x^2 - 3
            sage: [ charpoly(t) for t in OK.basis() ]
            [x^2 - 2*x + 1, x^2 + b*x + 1, x^2 - x + 1, x^2 + 1]"""
    def inverse_mod(self, I) -> Any:
        """OrderElement_relative.inverse_mod(self, I)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 5444)

        Return an inverse of ``self`` modulo the given ideal.

        INPUT:

        - ``I`` -- may be an ideal of ``self.parent()``, or an
          element or list of elements of ``self.parent()`` generating a nonzero
          ideal. A :exc:`ValueError` is raised if `I` is non-integral or is zero.
          A :exc:`ZeroDivisionError` is raised if `I + (x) \\neq (1)`.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: E.<a,b> = NumberField([x^2 - x + 2, x^2 + 1])
            sage: OE = E.ring_of_integers()
            sage: t = OE(b - a).inverse_mod(17*b)
            sage: t*(b - a) - 1 in E.ideal(17*b)
            True
            sage: t.parent() == OE
            True"""
    def minpoly(self, var=...) -> Any:
        """OrderElement_relative.minpoly(self, var='x')

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 5494)

        The minimal polynomial of this order element over its base ring.

        This special implementation works around :issue:`4738`.  At this
        time the base ring of relative order elements is `\\ZZ`; it should
        be the ring of integers of the base field.

        EXAMPLES::

            sage: x = ZZ['x'].0
            sage: K.<a,b> = NumberField([x^2 + 1, x^2 - 3])
            sage: OK = K.maximal_order(); OK.basis()
            [1, 1/2*a - 1/2*b, -1/2*b*a + 1/2, a]
            sage: minpoly(OK.1)
            x^2 + b*x + 1
            sage: charpoly(OK.1).parent()
            Univariate Polynomial Ring in x over Maximal Order generated by b
             in Number Field in b with defining polynomial x^2 - 3
            sage: _, u, _, v = OK.basis()
            sage: t = 2*u - v; t
            -b
            sage: t.charpoly()
            x^2 + 2*b*x + 3
            sage: t.minpoly()
            x + b

            sage: t.absolute_charpoly()
            x^4 - 6*x^2 + 9
            sage: t.absolute_minpoly()
            x^2 - 3"""
    def __invert__(self) -> Any:
        """OrderElement_relative.__invert__(self)

        File: /build/sagemath/src/sage/src/sage/rings/number_field/number_field_element.pyx (starting at line 5418)

        Implement division, checking that the result has the right parent.

        See :issue:`4190`.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K1.<a> = NumberField(x^3 - 17)
            sage: R.<y> = K1[]
            sage: K2 = K1.extension(y^2 - a, 'b')
            sage: OK2 = K2.order(K2.gen()) # (not maximal)
            sage: b = OK2.basis()[1]; b
            b
            sage: b.parent() is OK2
            True
            sage: (~b).parent() is K2
            True
            sage: (~b) in OK2 # indirect doctest
            False
            sage: b**(-1) in OK2 # indirect doctest
            False"""
