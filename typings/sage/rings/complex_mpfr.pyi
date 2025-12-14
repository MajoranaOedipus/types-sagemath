import _cython_3_2_1
import sage as sage
import sage.categories.map
import sage.rings.abc
import sage.rings.infinity asRealField: _cython_3_2_1.cython_function_or_method
 infinity
import sage.structure.element
from _typeshed import Incomplete
from sage.categories.category import CDF as CDF, ZZ as ZZ
from sage.categories.category import JoinCategory
from sage.rings.number_field.number_field_element_quadratic import NumberFieldElement_quadratic as NumberFieldElement_quadratic
from sage.rings.qqbar import AA as AA, QQbar as QQbar
from sage.rings.real_lazy import CLF as CLF, RLF as RLF
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from sage.structure.richcmp import revop as revop, rich_to_bool as rich_to_bool, rich_to_bool_sgn as rich_to_bool_sgn, richcmp as richcmp, richcmp_not_equal as richcmp_not_equal
from typing import Any, ClassVar, overload

def ComplexField(prec=53, names=None) -> ComplexField_class: 
    r"""ComplexField(prec=53, names=None)

File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 165)

Return the complex field with real and imaginary parts having prec
*bits* of precision.

EXAMPLES::

    sage: ComplexField()
    Complex Field with 53 bits of precision
    sage: ComplexField(100)
    Complex Field with 100 bits of precision
    sage: ComplexField(100).base_ring()
    Real Field with 100 bits of precision
    sage: i = ComplexField(200).gen()
    sage: i^2
    -1.0000000000000000000000000000000000000000000000000000000000

.. SEEALSO::

    - :class:`~sage.rings.complex_mpfr.ComplexField_class`
    - :class:`~sage.rings.real_arb.ComplexBallField` (complex numbers with
      rigorous error bounds)
"""
    ...
cache: dict
cmp_abs: _cython_3_2_1.cython_function_or_method
create_ComplexNumber: _cython_3_2_1.cython_function_or_method
is_ComplexNumber: _cython_3_2_1.cython_function_or_method
late_import: _cython_3_2_1.cython_function_or_method
make_ComplexNumber0: _cython_3_2_1.cython_function_or_method
set_global_complex_round_mode: _cython_3_2_1.cython_function_or_method

class ComplexField_class(sage.rings.abc.ComplexField):
    """File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 199)

        An approximation to the field of complex numbers using floating
        point numbers with any specified precision. Answers derived from
        calculations in this approximation may differ from what they would
        be if those calculations were performed in the true field of
        complex numbers. This is due to the rounding errors inherent to
        finite precision calculations.

        EXAMPLES::

            sage: C = ComplexField(); C
            Complex Field with 53 bits of precision
            sage: Q = RationalField()
            sage: C(1/3)
            0.333333333333333
            sage: C(1/3, 2)
            0.333333333333333 + 2.00000000000000*I
            sage: C(RR.pi())
            3.14159265358979
            sage: C(RR.log2(), RR.pi())
            0.693147180559945 + 3.14159265358979*I

        We can also coerce rational numbers and integers into C, but
        coercing a polynomial will raise an exception::

            sage: Q = RationalField()
            sage: C(1/3)
            0.333333333333333
            sage: S = PolynomialRing(Q, 'x')
            sage: C(S.gen())
            Traceback (most recent call last):
            ...
            TypeError: cannot convert nonconstant polynomial

        This illustrates precision::

            sage: CC = ComplexField(10); CC(1/3, 2/3)
            0.33 + 0.67*I
            sage: CC
            Complex Field with 10 bits of precision
            sage: CC = ComplexField(100); CC
            Complex Field with 100 bits of precision
            sage: z = CC(1/3, 2/3); z
            0.33333333333333333333333333333 + 0.66666666666666666666666666667*I

        We can load and save complex numbers and the complex field::

            sage: loads(z.dumps()) == z
            True
            sage: loads(CC.dumps()) == CC
            True
            sage: k = ComplexField(100)
            sage: loads(dumps(k)) == k
            True

        This illustrates basic properties of a complex field::

            sage: CC = ComplexField(200)
            sage: CC.is_field()
            True
            sage: CC.characteristic()
            0
            sage: CC.precision()
            200
            sage: CC.variable_name()
            'I'
            sage: CC == ComplexField(200)
            True
            sage: CC == ComplexField(53)
            False
            sage: CC == 1.1
            False

        .. SEEALSO::

            - :func:`~sage.rings.complex_mpfr.ComplexField` (constructor)
            - :class:`~sage.rings.real_arb.ComplexBallField` (complex numbers with
              rigorous error bounds)
            - :mod:`~sage.rings.real_mpfr`
    """
    def __init__(self, prec=...):
        """ComplexField_class.__init__(self, prec=53)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 280)

        Initialize ``self``.

        TESTS::

            sage: C = ComplexField(200)
            sage: C.category()
            Join of Category of fields and Category of infinite sets and Category of complete metric spaces
            sage: TestSuite(C).run()

            sage: CC.is_field()
            True

            sage: CC.is_finite()
            False"""
    @overload
    def algebraic_closure(self) -> Any:
        """ComplexField_class.algebraic_closure(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 834)

        Return the algebraic closure of ``self`` (which is itself).

        EXAMPLES::

            sage: CC
            Complex Field with 53 bits of precision
            sage: CC.algebraic_closure()
            Complex Field with 53 bits of precision
            sage: CC = ComplexField(1000)
            sage: CC.algebraic_closure() is CC
            True"""
    @overload
    def algebraic_closure(self) -> Any:
        """ComplexField_class.algebraic_closure(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 834)

        Return the algebraic closure of ``self`` (which is itself).

        EXAMPLES::

            sage: CC
            Complex Field with 53 bits of precision
            sage: CC.algebraic_closure()
            Complex Field with 53 bits of precision
            sage: CC = ComplexField(1000)
            sage: CC.algebraic_closure() is CC
            True"""
    @overload
    def algebraic_closure(self) -> Any:
        """ComplexField_class.algebraic_closure(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 834)

        Return the algebraic closure of ``self`` (which is itself).

        EXAMPLES::

            sage: CC
            Complex Field with 53 bits of precision
            sage: CC.algebraic_closure()
            Complex Field with 53 bits of precision
            sage: CC = ComplexField(1000)
            sage: CC.algebraic_closure() is CC
            True"""
    def characteristic(self) -> Any:
        """ComplexField_class.characteristic(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 681)

        Return the characteristic of `\\CC`, which is 0.

        EXAMPLES::

            sage: ComplexField().characteristic()
            0"""
    @overload
    def construction(self) -> Any:
        """ComplexField_class.construction(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 705)

        Return the functorial construction of ``self``, namely the algebraic
        closure of the real field with the same precision.

        EXAMPLES::

            sage: c, S = CC.construction(); S
            Real Field with 53 bits of precision
            sage: CC == c(S)
            True"""
    @overload
    def construction(self) -> Any:
        """ComplexField_class.construction(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 705)

        Return the functorial construction of ``self``, namely the algebraic
        closure of the real field with the same precision.

        EXAMPLES::

            sage: c, S = CC.construction(); S
            Real Field with 53 bits of precision
            sage: CC == c(S)
            True"""
    def gen(self, n=...) -> Any:
        """ComplexField_class.gen(self, n=0)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 692)

        Return the generator of the complex field.

        EXAMPLES::

            sage: ComplexField().gen(0)
            1.00000000000000*I"""
    @overload
    def is_exact(self) -> Any:
        """ComplexField_class.is_exact(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 316)

        Return whether or not this field is exact, which is always ``False``.

        EXAMPLES::

            sage: ComplexField().is_exact()
            False"""
    @overload
    def is_exact(self) -> Any:
        """ComplexField_class.is_exact(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 316)

        Return whether or not this field is exact, which is always ``False``.

        EXAMPLES::

            sage: ComplexField().is_exact()
            False"""
    def ngens(self) -> Any:
        """ComplexField_class.ngens(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 767)

        The number of generators of this complex field as an `\\RR`-algebra.

        There is one generator, namely ``sqrt(-1)``.

        EXAMPLES::

            sage: ComplexField().ngens()
            1"""
    def pi(self) -> Any:
        """ComplexField_class.pi(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 754)

        Return `\\pi` as a complex number.

        EXAMPLES::

            sage: ComplexField().pi()
            3.14159265358979
            sage: ComplexField(100).pi()
            3.1415926535897932384626433833"""
    @overload
    def prec(self) -> Any:
        """ComplexField_class.prec(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 327)

        Return the precision of this complex field.

        EXAMPLES::

            sage: ComplexField().prec()
            53
            sage: ComplexField(15).prec()
            15"""
    @overload
    def prec(self) -> Any:
        """ComplexField_class.prec(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 327)

        Return the precision of this complex field.

        EXAMPLES::

            sage: ComplexField().prec()
            53
            sage: ComplexField(15).prec()
            15"""
    @overload
    def prec(self) -> Any:
        """ComplexField_class.prec(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 327)

        Return the precision of this complex field.

        EXAMPLES::

            sage: ComplexField().prec()
            53
            sage: ComplexField(15).prec()
            15"""
    def precision(self, *args, **kwargs):
        """ComplexField_class.prec(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 327)

        Return the precision of this complex field.

        EXAMPLES::

            sage: ComplexField().prec()
            53
            sage: ComplexField(15).prec()
            15"""
    def random_element(self, component_max=..., *args, **kwds) -> Any:
        """ComplexField_class.random_element(self, component_max=1, *args, **kwds)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 720)

        Return a uniformly distributed random number inside a square
        centered on the origin (by default, the square `[-1,1] \\times [-1,1]`).

        Passes additional arguments and keywords to underlying real field.

        EXAMPLES::

            sage: CC.random_element().parent() is CC
            True
            sage: re, im = CC.random_element()
            sage: -1 <= re <= 1, -1 <= im <= 1
            (True, True)
            sage: CC6 = ComplexField(6)
            sage: CC6.random_element().parent() is CC6
            True
            sage: re, im = CC6.random_element(2^-20)
            sage: -2^-20 <= re <= 2^-20, -2^-20 <= im <= 2^-20
            (True, True)
            sage: re, im = CC6.random_element(pi^20)                                    # needs sage.symbolic
            sage: bool(-pi^20 <= re <= pi^20), bool(-pi^20 <= im <= pi^20)              # needs sage.symbolic
            (True, True)

        Passes extra positional or keyword arguments through::

            sage: CC.random_element(distribution='1/n').parent() is CC
            True"""
    @overload
    def scientific_notation(self, status=...) -> Any:
        """ComplexField_class.scientific_notation(self, status=None)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 813)

        Set or return the scientific notation printing flag.

        If this flag is ``True`` then complex numbers with this space as parent
        print using scientific notation.

        EXAMPLES::

            sage: C = ComplexField()
            sage: C((0.025, 2))
            0.0250000000000000 + 2.00000000000000*I
            sage: C.scientific_notation(True)
            sage: C((0.025, 2))
            2.50000000000000e-2 + 2.00000000000000e0*I
            sage: C.scientific_notation(False)
            sage: C((0.025, 2))
            0.0250000000000000 + 2.00000000000000*I"""
    @overload
    def scientific_notation(self, _True) -> Any:
        """ComplexField_class.scientific_notation(self, status=None)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 813)

        Set or return the scientific notation printing flag.

        If this flag is ``True`` then complex numbers with this space as parent
        print using scientific notation.

        EXAMPLES::

            sage: C = ComplexField()
            sage: C((0.025, 2))
            0.0250000000000000 + 2.00000000000000*I
            sage: C.scientific_notation(True)
            sage: C((0.025, 2))
            2.50000000000000e-2 + 2.00000000000000e0*I
            sage: C.scientific_notation(False)
            sage: C((0.025, 2))
            0.0250000000000000 + 2.00000000000000*I"""
    @overload
    def scientific_notation(self, _False) -> Any:
        """ComplexField_class.scientific_notation(self, status=None)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 813)

        Set or return the scientific notation printing flag.

        If this flag is ``True`` then complex numbers with this space as parent
        print using scientific notation.

        EXAMPLES::

            sage: C = ComplexField()
            sage: C((0.025, 2))
            0.0250000000000000 + 2.00000000000000*I
            sage: C.scientific_notation(True)
            sage: C((0.025, 2))
            2.50000000000000e-2 + 2.00000000000000e0*I
            sage: C.scientific_notation(False)
            sage: C((0.025, 2))
            0.0250000000000000 + 2.00000000000000*I"""
    def to_prec(self, prec) -> Any:
        """ComplexField_class.to_prec(self, prec)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 363)

        Return the complex field to the specified precision.

        EXAMPLES::

            sage: CC.to_prec(10)
            Complex Field with 10 bits of precision
            sage: CC.to_prec(100)
            Complex Field with 100 bits of precision"""
    def zeta(self, n=...) -> Any:
        """ComplexField_class.zeta(self, n=2)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 780)

        Return a primitive `n`-th root of unity.

        INPUT:

        - ``n`` -- integer (default: 2)

        OUTPUT: a complex `n`-th root of unity

        EXAMPLES::

            sage: C = ComplexField()
            sage: C.zeta(2)
            -1.00000000000000
            sage: C.zeta(5)
            0.309016994374947 + 0.951056516295154*I"""
    def __call__(self, x=..., im=...) -> Any:
        """ComplexField_class.__call__(self, x=None, im=None)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 440)

        Create a complex number.

        EXAMPLES::

            sage: CC(2) # indirect doctest
            2.00000000000000
            sage: CC(CC.0)
            1.00000000000000*I
            sage: CC('1+I')
            1.00000000000000 + 1.00000000000000*I
            sage: CC(2,3)
            2.00000000000000 + 3.00000000000000*I
            sage: CC(QQ[I].gen())                                                       # needs sage.symbolic
            1.00000000000000*I
            sage: CC.gen() + QQ[I].gen()                                                # needs sage.symbolic
            2.00000000000000*I
            sage: x = polygen(ZZ, 'x')
            sage: CC.gen() + QQ.extension(x^2 + 1, 'I', embedding=None).gen()           # needs sage.rings.number_field
            Traceback (most recent call last):
            ...
            TypeError: unsupported operand parent(s) for +:
            'Complex Field with 53 bits of precision' and
            'Number Field in I with defining polynomial x^2 + 1'

        In the absence of arguments we return zero::

            sage: a = CC(); a
            0.000000000000000
            sage: a.parent()
            Complex Field with 53 bits of precision"""
    def __eq__(self, other) -> Any:
        """ComplexField_class.__eq__(self, other)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 395)

        Check whether ``self`` is not equal to ``other``.

        If ``other`` is not a :class:`ComplexField_class`, then this
        return ``False``. Otherwise it compares their precision.

        EXAMPLES::

            sage: ComplexField() == ComplexField()
            True
            sage: ComplexField(10) == ComplexField(15)
            False"""
    def __hash__(self) -> Any:
        """ComplexField_class.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 413)

        Return the hash.

        EXAMPLES::

            sage: C = ComplexField(200)
            sage: from sage.rings.complex_mpfr import ComplexField_class
            sage: D = ComplexField_class(200)
            sage: hash(C) == hash(D)
            True"""
    def __ne__(self, other) -> Any:
        """ComplexField_class.__ne__(self, other)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 427)

        Check whether ``self`` is not equal to ``other``.

        EXAMPLES::

            sage: ComplexField() != ComplexField()
            False
            sage: ComplexField(10) != ComplexField(15)
            True"""
    def __reduce__(self) -> Any:
        """ComplexField_class.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 305)

        For pickling.

        EXAMPLES::

            sage: loads(dumps(ComplexField())) == ComplexField()
            True"""

class ComplexNumber(sage.structure.element.FieldElement):
    """ComplexNumber(parent, real, imag=None)

    File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 903)

    A floating point approximation to a complex number using any
    specified precision. Answers derived from calculations with such
    approximations may differ from what they would be if those
    calculations were performed with true complex numbers. This is due
    to the rounding errors inherent to finite precision calculations.

    EXAMPLES::

        sage: I = CC.0
        sage: b = 1.5 + 2.5*I
        sage: loads(b.dumps()) == b
        True"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    __array_interface__: Incomplete
    def __init__(self, parent, real, imag=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 944)

                Initialize :class:`ComplexNumber` instance.

                EXAMPLES::

                    sage: a = ComplexNumber(2,1)
                    sage: a.__init__(CC,2,1)
                    sage: a
                    2.00000000000000 + 1.00000000000000*I
                    sage: parent(a)
                    Complex Field with 53 bits of precision
                    sage: real(a)
                    2.00000000000000
                    sage: imag(a)
                    1.00000000000000

                Conversion from gmpy2 numbers::

                    sage: from gmpy2 import *
                    sage: c = mpc('2.0+1.0j')
                    sage: CC(c)
                    2.00000000000000 + 1.00000000000000*I
        """
    @overload
    def additive_order(self) -> Any:
        """ComplexNumber.additive_order(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 2972)

        Return the additive order of ``self``.

        EXAMPLES::

            sage: CC(0).additive_order()
            1
            sage: CC.gen().additive_order()
            +Infinity"""
    @overload
    def additive_order(self) -> Any:
        """ComplexNumber.additive_order(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 2972)

        Return the additive order of ``self``.

        EXAMPLES::

            sage: CC(0).additive_order()
            1
            sage: CC.gen().additive_order()
            +Infinity"""
    @overload
    def additive_order(self) -> Any:
        """ComplexNumber.additive_order(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 2972)

        Return the additive order of ``self``.

        EXAMPLES::

            sage: CC(0).additive_order()
            1
            sage: CC.gen().additive_order()
            +Infinity"""
    def agm(self, right, algorithm=...) -> Any:
        """ComplexNumber.agm(self, right, algorithm='optimal')

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 2541)

        Return the Arithmetic-Geometric Mean (AGM) of ``self`` and ``right``.

        INPUT:

        - ``right`` -- complex; another complex number

        - ``algorithm`` -- string (default: ``'optimal'``); the algorithm to use
          (see below)

        OUTPUT:

        (complex) A value of the AGM of ``self`` and ``right``.  Note that
        this is a multi-valued function, and the algorithm used
        affects the value returned, as follows:

        - ``'pari'``: Call the :pari:`agm` function from the PARI library.

        - ``'optimal'``: Use the AGM sequence such that at each stage
          `(a,b)` is replaced by `(a_1,b_1)=((a+b)/2,\\pm\\sqrt{ab})`
          where the sign is chosen so that `|a_1-b_1|\\le|a_1+b_1|`, or
          equivalently `\\Re(b_1/a_1)\\ge 0`.  The resulting limit is
          maximal among all possible values.

        - ``'principal'``: Use the AGM sequence such that at each stage
          `(a,b)` is replaced by `(a_1,b_1)=((a+b)/2,\\pm\\sqrt{ab})`
          where the sign is chosen so that `\\Re(b_1)\\ge 0` (the
          so-called principal branch of the square root).

        The values `AGM(a,0)`, `AGM(0,a)`, and `AGM(a,-a)` are all taken to be 0.

        EXAMPLES::

            sage: a = CC(1,1)
            sage: b = CC(2,-1)
            sage: a.agm(b)
            1.62780548487271 + 0.136827548397369*I
            sage: a.agm(b, algorithm='optimal')
            1.62780548487271 + 0.136827548397369*I
            sage: a.agm(b, algorithm='principal')
            1.62780548487271 + 0.136827548397369*I
            sage: a.agm(b, algorithm='pari')                                            # needs sage.libs.pari
            1.62780548487271 + 0.136827548397369*I

        An example to show that the returned value depends on the algorithm
        parameter::

            sage: a = CC(-0.95,-0.65)
            sage: b = CC(0.683,0.747)
            sage: a.agm(b, algorithm='optimal')
            -0.371591652351761 + 0.319894660206830*I
            sage: a.agm(b, algorithm='principal')
            0.338175462986180 - 0.0135326969565405*I
            sage: a.agm(b, algorithm='pari')                                            # needs sage.libs.pari
            -0.371591652351761 + 0.319894660206830*I
            sage: a.agm(b, algorithm='optimal').abs()
            0.490319232466314
            sage: a.agm(b, algorithm='principal').abs()
            0.338446122230459
            sage: a.agm(b, algorithm='pari').abs()                                      # needs sage.libs.pari
            0.490319232466314

        TESTS:

        An example which came up in testing::

            sage: I = CC(I)
            sage: a =  0.501648970493109 + 1.11877240294744*I
            sage: b =  1.05946309435930 + 1.05946309435930*I
            sage: a.agm(b)
            0.774901870587681 + 1.10254945079875*I

            sage: a = CC(-0.32599972608379413, 0.60395514542928641)
            sage: b = CC( 0.6062314525690593,  0.1425693337776659)
            sage: a.agm(b)
            0.199246281325876 + 0.478401702759654*I
            sage: a.agm(-a)
            0.000000000000000
            sage: a.agm(0)
            0.000000000000000
            sage: CC(0).agm(a)
            0.000000000000000

        Consistency::

            sage: a = 1 + 0.5*I
            sage: b = 2 - 0.25*I
            sage: a.agm(b) - ComplexField(100)(a).agm(b)
            0.000000000000000
            sage: ComplexField(200)(a).agm(b) - ComplexField(500)(a).agm(b)
            0.00000000000000000000000000000000000000000000000000000000000
            sage: ComplexField(500)(a).agm(b) - ComplexField(1000)(a).agm(b)
            0.000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"""
    def algdep(self, *args, **kwargs):
        """ComplexNumber.algebraic_dependency(self, n, **kwds)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 3253)

        Return an irreducible polynomial of degree at most `n` which is
        approximately satisfied by this complex number.

        ALGORITHM: Uses the PARI C-library :pari:`algdep` command.

        INPUT: Type ``algebraic_dependency?`` at the top level prompt.

        All additional parameters are passed onto the top-level
        :func:`algebraic_dependency` command.

        EXAMPLES::

            sage: C = ComplexField()
            sage: z = (1/2)*(1 + sqrt(3.0) *C.0); z
            0.500000000000000 + 0.866025403784439*I
            sage: p = z.algebraic_dependency(5); p
            x^2 - x + 1
            sage: p(z)
            1.11022302462516e-16"""
    def algebraic_dependency(self, n, **kwds) -> Any:
        """ComplexNumber.algebraic_dependency(self, n, **kwds)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 3253)

        Return an irreducible polynomial of degree at most `n` which is
        approximately satisfied by this complex number.

        ALGORITHM: Uses the PARI C-library :pari:`algdep` command.

        INPUT: Type ``algebraic_dependency?`` at the top level prompt.

        All additional parameters are passed onto the top-level
        :func:`algebraic_dependency` command.

        EXAMPLES::

            sage: C = ComplexField()
            sage: z = (1/2)*(1 + sqrt(3.0) *C.0); z
            0.500000000000000 + 0.866025403784439*I
            sage: p = z.algebraic_dependency(5); p
            x^2 - x + 1
            sage: p(z)
            1.11022302462516e-16"""
    @overload
    def arccos(self) -> Any:
        """ComplexNumber.arccos(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 2109)

        Return the arccosine of ``self``.

        EXAMPLES::

            sage: (1+CC(I)).arccos()                                                    # needs sage.libs.pari
            0.904556894302381 - 1.06127506190504*I"""
    @overload
    def arccos(self) -> Any:
        """ComplexNumber.arccos(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 2109)

        Return the arccosine of ``self``.

        EXAMPLES::

            sage: (1+CC(I)).arccos()                                                    # needs sage.libs.pari
            0.904556894302381 - 1.06127506190504*I"""
    @overload
    def arccosh(self) -> Any:
        """ComplexNumber.arccosh(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 2120)

        Return the hyperbolic arccosine of ``self``.

        EXAMPLES::

            sage: (1+CC(I)).arccosh()                                                   # needs sage.libs.pari
            1.06127506190504 + 0.904556894302381*I"""
    @overload
    def arccosh(self) -> Any:
        """ComplexNumber.arccosh(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 2120)

        Return the hyperbolic arccosine of ``self``.

        EXAMPLES::

            sage: (1+CC(I)).arccosh()                                                   # needs sage.libs.pari
            1.06127506190504 + 0.904556894302381*I"""
    @overload
    def arccoth(self) -> Any:
        """ComplexNumber.arccoth(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 2186)

        Return the hyperbolic arccotangent of ``self``.

        EXAMPLES::

            sage: ComplexField(100)(1,1).arccoth()                                      # needs sage.libs.pari
            0.40235947810852509365018983331 - 0.55357435889704525150853273009*I"""
    @overload
    def arccoth(self) -> Any:
        """ComplexNumber.arccoth(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 2186)

        Return the hyperbolic arccotangent of ``self``.

        EXAMPLES::

            sage: ComplexField(100)(1,1).arccoth()                                      # needs sage.libs.pari
            0.40235947810852509365018983331 - 0.55357435889704525150853273009*I"""
    @overload
    def arccsch(self) -> Any:
        """ComplexNumber.arccsch(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 2219)

        Return the hyperbolic arccosecant of ``self``.

        EXAMPLES::

            sage: ComplexField(100)(1,1).arccsch()                                      # needs sage.libs.pari
            0.53063753095251782601650945811 - 0.45227844715119068206365839783*I"""
    @overload
    def arccsch(self) -> Any:
        """ComplexNumber.arccsch(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 2219)

        Return the hyperbolic arccosecant of ``self``.

        EXAMPLES::

            sage: ComplexField(100)(1,1).arccsch()                                      # needs sage.libs.pari
            0.53063753095251782601650945811 - 0.45227844715119068206365839783*I"""
    @overload
    def arcsech(self) -> Any:
        """ComplexNumber.arcsech(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 2252)

        Return the hyperbolic arcsecant of ``self``.

        EXAMPLES::

            sage: ComplexField(100)(1,1).arcsech()                                      # needs sage.libs.pari
            0.53063753095251782601650945811 - 1.1185178796437059371676632938*I"""
    @overload
    def arcsech(self) -> Any:
        """ComplexNumber.arcsech(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 2252)

        Return the hyperbolic arcsecant of ``self``.

        EXAMPLES::

            sage: ComplexField(100)(1,1).arcsech()                                      # needs sage.libs.pari
            0.53063753095251782601650945811 - 1.1185178796437059371676632938*I"""
    @overload
    def arcsin(self) -> Any:
        """ComplexNumber.arcsin(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 2131)

        Return the arcsine of ``self``.

        EXAMPLES::

            sage: (1+CC(I)).arcsin()                                                    # needs sage.libs.pari
            0.666239432492515 + 1.06127506190504*I"""
    @overload
    def arcsin(self) -> Any:
        """ComplexNumber.arcsin(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 2131)

        Return the arcsine of ``self``.

        EXAMPLES::

            sage: (1+CC(I)).arcsin()                                                    # needs sage.libs.pari
            0.666239432492515 + 1.06127506190504*I"""
    @overload
    def arcsinh(self) -> Any:
        """ComplexNumber.arcsinh(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 2142)

        Return the hyperbolic arcsine of ``self``.

        EXAMPLES::

            sage: (1+CC(I)).arcsinh()                                                   # needs sage.libs.pari
            1.06127506190504 + 0.666239432492515*I"""
    @overload
    def arcsinh(self) -> Any:
        """ComplexNumber.arcsinh(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 2142)

        Return the hyperbolic arcsine of ``self``.

        EXAMPLES::

            sage: (1+CC(I)).arcsinh()                                                   # needs sage.libs.pari
            1.06127506190504 + 0.666239432492515*I"""
    @overload
    def arctan(self) -> Any:
        """ComplexNumber.arctan(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 2153)

        Return the arctangent of ``self``.

        EXAMPLES::

            sage: (1+CC(I)).arctan()                                                    # needs sage.libs.pari
            1.01722196789785 + 0.402359478108525*I"""
    @overload
    def arctan(self) -> Any:
        """ComplexNumber.arctan(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 2153)

        Return the arctangent of ``self``.

        EXAMPLES::

            sage: (1+CC(I)).arctan()                                                    # needs sage.libs.pari
            1.01722196789785 + 0.402359478108525*I"""
    @overload
    def arctanh(self) -> Any:
        """ComplexNumber.arctanh(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 2164)

        Return the hyperbolic arctangent of ``self``.

        EXAMPLES::

            sage: (1+CC(I)).arctanh()                                                   # needs sage.libs.pari
            0.402359478108525 + 1.01722196789785*I"""
    @overload
    def arctanh(self) -> Any:
        """ComplexNumber.arctanh(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 2164)

        Return the hyperbolic arctangent of ``self``.

        EXAMPLES::

            sage: (1+CC(I)).arctanh()                                                   # needs sage.libs.pari
            0.402359478108525 + 1.01722196789785*I"""
    @overload
    def arg(self) -> Any:
        """ComplexNumber.arg(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 2768)

        See :meth:`argument`.

        EXAMPLES::

            sage: i = CC.0
            sage: (i^2).arg()
            3.14159265358979"""
    @overload
    def arg(self) -> Any:
        """ComplexNumber.arg(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 2768)

        See :meth:`argument`.

        EXAMPLES::

            sage: i = CC.0
            sage: (i^2).arg()
            3.14159265358979"""
    @overload
    def argument(self) -> Any:
        """ComplexNumber.argument(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 2744)

        The argument (angle) of the complex number, normalized so that
        `-\\pi < \\theta \\leq \\pi`.

        EXAMPLES::

            sage: i = CC.0
            sage: (i^2).argument()
            3.14159265358979
            sage: (1+i).argument()
            0.785398163397448
            sage: i.argument()
            1.57079632679490
            sage: (-i).argument()
            -1.57079632679490
            sage: (RR('-0.001') - i).argument()
            -1.57179632646156"""
    @overload
    def argument(self, angle) -> Any:
        """ComplexNumber.argument(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 2744)

        The argument (angle) of the complex number, normalized so that
        `-\\pi < \\theta \\leq \\pi`.

        EXAMPLES::

            sage: i = CC.0
            sage: (i^2).argument()
            3.14159265358979
            sage: (1+i).argument()
            0.785398163397448
            sage: i.argument()
            1.57079632679490
            sage: (-i).argument()
            -1.57079632679490
            sage: (RR('-0.001') - i).argument()
            -1.57179632646156"""
    @overload
    def conjugate(self) -> Any:
        """ComplexNumber.conjugate(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 2780)

        Return the complex conjugate of this complex number.

        EXAMPLES::

            sage: i = CC.0
            sage: (1+i).conjugate()
            1.00000000000000 - 1.00000000000000*I"""
    @overload
    def conjugate(self) -> Any:
        """ComplexNumber.conjugate(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 2780)

        Return the complex conjugate of this complex number.

        EXAMPLES::

            sage: i = CC.0
            sage: (1+i).conjugate()
            1.00000000000000 - 1.00000000000000*I"""
    @overload
    def cos(self) -> Any:
        """ComplexNumber.cos(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 2288)

        Return the cosine of ``self``.

        EXAMPLES::

            sage: (1+CC(I)).cos()
            0.833730025131149 - 0.988897705762865*I"""
    @overload
    def cos(self) -> Any:
        """ComplexNumber.cos(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 2288)

        Return the cosine of ``self``.

        EXAMPLES::

            sage: (1+CC(I)).cos()
            0.833730025131149 - 0.988897705762865*I"""
    @overload
    def cosh(self) -> Any:
        """ComplexNumber.cosh(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 2316)

        Return the hyperbolic cosine of ``self``.

        EXAMPLES::

            sage: (1+CC(I)).cosh()
            0.833730025131149 + 0.988897705762865*I"""
    @overload
    def cosh(self) -> Any:
        """ComplexNumber.cosh(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 2316)

        Return the hyperbolic cosine of ``self``.

        EXAMPLES::

            sage: (1+CC(I)).cosh()
            0.833730025131149 + 0.988897705762865*I"""
    @overload
    def cot(self) -> Any:
        """ComplexNumber.cot(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 2263)

        Return the cotangent of ``self``.

        EXAMPLES::

            sage: # needs sage.libs.pari
            sage: (1+CC(I)).cot()
            0.217621561854403 - 0.868014142895925*I
            sage: i = ComplexField(200).0
            sage: (1+i).cot()
            0.21762156185440268136513424360523807352075436916785404091068 - 0.86801414289592494863584920891627388827343874994609327121115*I
            sage: i = ComplexField(220).0
            sage: (1+i).cot()
            0.21762156185440268136513424360523807352075436916785404091068124239 - 0.86801414289592494863584920891627388827343874994609327121115071646*I

        TESTS:

        Verify that :issue:`29409` is fixed::

            sage: cot(1 + I).n()
            0.217621561854403 - 0.868014142895925*I"""
    @overload
    def cot(self) -> Any:
        """ComplexNumber.cot(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 2263)

        Return the cotangent of ``self``.

        EXAMPLES::

            sage: # needs sage.libs.pari
            sage: (1+CC(I)).cot()
            0.217621561854403 - 0.868014142895925*I
            sage: i = ComplexField(200).0
            sage: (1+i).cot()
            0.21762156185440268136513424360523807352075436916785404091068 - 0.86801414289592494863584920891627388827343874994609327121115*I
            sage: i = ComplexField(220).0
            sage: (1+i).cot()
            0.21762156185440268136513424360523807352075436916785404091068124239 - 0.86801414289592494863584920891627388827343874994609327121115071646*I

        TESTS:

        Verify that :issue:`29409` is fixed::

            sage: cot(1 + I).n()
            0.217621561854403 - 0.868014142895925*I"""
    @overload
    def cot(self) -> Any:
        """ComplexNumber.cot(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 2263)

        Return the cotangent of ``self``.

        EXAMPLES::

            sage: # needs sage.libs.pari
            sage: (1+CC(I)).cot()
            0.217621561854403 - 0.868014142895925*I
            sage: i = ComplexField(200).0
            sage: (1+i).cot()
            0.21762156185440268136513424360523807352075436916785404091068 - 0.86801414289592494863584920891627388827343874994609327121115*I
            sage: i = ComplexField(220).0
            sage: (1+i).cot()
            0.21762156185440268136513424360523807352075436916785404091068124239 - 0.86801414289592494863584920891627388827343874994609327121115071646*I

        TESTS:

        Verify that :issue:`29409` is fixed::

            sage: cot(1 + I).n()
            0.217621561854403 - 0.868014142895925*I"""
    @overload
    def cot(self) -> Any:
        """ComplexNumber.cot(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 2263)

        Return the cotangent of ``self``.

        EXAMPLES::

            sage: # needs sage.libs.pari
            sage: (1+CC(I)).cot()
            0.217621561854403 - 0.868014142895925*I
            sage: i = ComplexField(200).0
            sage: (1+i).cot()
            0.21762156185440268136513424360523807352075436916785404091068 - 0.86801414289592494863584920891627388827343874994609327121115*I
            sage: i = ComplexField(220).0
            sage: (1+i).cot()
            0.21762156185440268136513424360523807352075436916785404091068124239 - 0.86801414289592494863584920891627388827343874994609327121115071646*I

        TESTS:

        Verify that :issue:`29409` is fixed::

            sage: cot(1 + I).n()
            0.217621561854403 - 0.868014142895925*I"""
    @overload
    def coth(self) -> Any:
        """ComplexNumber.coth(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 2175)

        Return the hyperbolic cotangent of ``self``.

        EXAMPLES::

            sage: ComplexField(100)(1,1).coth()                                         # needs sage.libs.pari
            0.86801414289592494863584920892 - 0.21762156185440268136513424361*I"""
    @overload
    def coth(self) -> Any:
        """ComplexNumber.coth(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 2175)

        Return the hyperbolic cotangent of ``self``.

        EXAMPLES::

            sage: ComplexField(100)(1,1).coth()                                         # needs sage.libs.pari
            0.86801414289592494863584920892 - 0.21762156185440268136513424361*I"""
    @overload
    def csc(self) -> Any:
        """ComplexNumber.csc(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 2197)

        Return the cosecant of ``self``.

        EXAMPLES::

            sage: ComplexField(100)(1,1).csc()                                          # needs sage.libs.pari
            0.62151801717042842123490780586 - 0.30393100162842645033448560451*I"""
    @overload
    def csc(self) -> Any:
        """ComplexNumber.csc(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 2197)

        Return the cosecant of ``self``.

        EXAMPLES::

            sage: ComplexField(100)(1,1).csc()                                          # needs sage.libs.pari
            0.62151801717042842123490780586 - 0.30393100162842645033448560451*I"""
    @overload
    def csch(self) -> Any:
        """ComplexNumber.csch(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 2208)

        Return the hyperbolic cosecant of ``self``.

        EXAMPLES::

            sage: ComplexField(100)(1,1).csch()                                         # needs sage.libs.pari
            0.30393100162842645033448560451 - 0.62151801717042842123490780586*I"""
    @overload
    def csch(self) -> Any:
        """ComplexNumber.csch(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 2208)

        Return the hyperbolic cosecant of ``self``.

        EXAMPLES::

            sage: ComplexField(100)(1,1).csch()                                         # needs sage.libs.pari
            0.30393100162842645033448560451 - 0.62151801717042842123490780586*I"""
    def dilog(self) -> Any:
        """ComplexNumber.dilog(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 2801)

        Return the complex dilogarithm of ``self``.

        The complex dilogarithm, or Spence's function, is defined by

        .. MATH::

            Li_2(z) = - \\int_0^z \\frac{\\log|1-\\zeta|}{\\zeta} d(\\zeta)
            = \\sum_{k=1}^\\infty \\frac{z^k}{k}

        Note that the series definition can only be used for `|z| < 1`.

        EXAMPLES::

            sage: a = ComplexNumber(1,0)
            sage: a.dilog()                                                             # needs sage.libs.pari
            1.64493406684823
            sage: float(pi^2/6)                                                         # needs sage.symbolic
            1.6449340668482262

        ::

            sage: b = ComplexNumber(0,1)
            sage: b.dilog()                                                             # needs sage.libs.pari
            -0.205616758356028 + 0.915965594177219*I

        ::

            sage: c = ComplexNumber(0,0)
            sage: c.dilog()                                                             # needs sage.libs.pari
            0.000000000000000"""
    def eta(self, omit_frac=...) -> Any:
        """ComplexNumber.eta(self, omit_frac=False)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 2343)

        Return the value of the Dedekind `\\eta` function on ``self``,
        intelligently computed using `\\mathbb{SL}(2,\\ZZ)`
        transformations.

        The `\\eta` function is

        .. MATH::

            \\eta(z) = e^{\\pi i z / 12} \\prod_{n=1}^{\\infty}(1-e^{2\\pi inz})

        INPUT:

        - ``self`` -- element of the upper half plane (if not,
          raises a :exc:`ValueError`)

        - ``omit_frac`` -- -- boolean (default: ``False``); if ``True``,
          omit the `e^{\\pi i z / 12}` factor

        OUTPUT: a complex number

        ALGORITHM: Uses the PARI C library.

        EXAMPLES:

        First we compute `\\eta(1+i)`::

            sage: i = CC.0
            sage: z = 1 + i; z.eta()                                                    # needs sage.libs.pari
            0.742048775836565 + 0.198831370229911*I

        We compute eta to low precision directly from the definition::

            sage: pi = CC(pi)        # otherwise we will get a symbolic result.         # needs sage.symbolic
            sage: exp(pi * i * z / 12) * prod(1 - exp(2*pi*i*n*z)                       # needs sage.libs.pari sage.symbolic
            ....:                             for n in range(1,10))
            0.742048775836565 + 0.198831370229911*I

        The optional argument allows us to omit the fractional part::

            sage: z.eta(omit_frac=True)                                                 # needs sage.libs.pari
            0.998129069925959
            sage: prod(1 - exp(2*pi*i*n*z) for n in range(1,10))                        # needs sage.libs.pari sage.symbolic
            0.998129069925958 + 4.59099857829247e-19*I

        We illustrate what happens when `z` is not in the upper
        half plane::

            sage: z = CC(1)
            sage: z.eta()                                                               # needs sage.libs.pari
            Traceback (most recent call last):
            ...
            ValueError: value must be in the upper half plane

        You can also use functional notation::

            sage: eta(1 + CC(I))                                                        # needs sage.libs.pari
            0.742048775836565 + 0.198831370229911*I"""
    def exp(self) -> Any:
        """ComplexNumber.exp(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 2836)

        Compute `e^z` or `\\exp(z)`.

        EXAMPLES::

            sage: i = ComplexField(300).0
            sage: z = 1 + i
            sage: z.exp()
            1.46869393991588515713896759732660426132695673662900872279767567631093696585951213872272450 + 2.28735528717884239120817190670050180895558625666835568093865811410364716018934540926734485*I"""
    @overload
    def gamma(self) -> Any:
        """ComplexNumber.gamma(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 2860)

        Return the Gamma function evaluated at this complex number.

        EXAMPLES::

            sage: i = ComplexField(30).0
            sage: (1 + i).gamma()                                                       # needs sage.libs.pari
            0.49801567 - 0.15494983*I

        TESTS::

            sage: CC(0).gamma()                                                         # needs sage.libs.pari
            Infinity

        ::

            sage: CC(-1).gamma()                                                        # needs sage.libs.pari
            Infinity"""
    @overload
    def gamma(self) -> Any:
        """ComplexNumber.gamma(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 2860)

        Return the Gamma function evaluated at this complex number.

        EXAMPLES::

            sage: i = ComplexField(30).0
            sage: (1 + i).gamma()                                                       # needs sage.libs.pari
            0.49801567 - 0.15494983*I

        TESTS::

            sage: CC(0).gamma()                                                         # needs sage.libs.pari
            Infinity

        ::

            sage: CC(-1).gamma()                                                        # needs sage.libs.pari
            Infinity"""
    @overload
    def gamma(self) -> Any:
        """ComplexNumber.gamma(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 2860)

        Return the Gamma function evaluated at this complex number.

        EXAMPLES::

            sage: i = ComplexField(30).0
            sage: (1 + i).gamma()                                                       # needs sage.libs.pari
            0.49801567 - 0.15494983*I

        TESTS::

            sage: CC(0).gamma()                                                         # needs sage.libs.pari
            Infinity

        ::

            sage: CC(-1).gamma()                                                        # needs sage.libs.pari
            Infinity"""
    @overload
    def gamma(self) -> Any:
        """ComplexNumber.gamma(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 2860)

        Return the Gamma function evaluated at this complex number.

        EXAMPLES::

            sage: i = ComplexField(30).0
            sage: (1 + i).gamma()                                                       # needs sage.libs.pari
            0.49801567 - 0.15494983*I

        TESTS::

            sage: CC(0).gamma()                                                         # needs sage.libs.pari
            Infinity

        ::

            sage: CC(-1).gamma()                                                        # needs sage.libs.pari
            Infinity"""
    def gamma_inc(self, t) -> Any:
        """ComplexNumber.gamma_inc(self, t)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 2886)

        Return the incomplete Gamma function evaluated at this complex
        number.

        EXAMPLES::

            sage: # needs sage.libs.pari
            sage: C, i = ComplexField(30).objgen()
            sage: (1+i).gamma_inc(2 + 3*i)  # abs tol 2e-10
            0.0020969149 - 0.059981914*I
            sage: (1+i).gamma_inc(5)
            -0.0013781309 + 0.0065198200*I
            sage: C(2).gamma_inc(1 + i)
            0.70709210 - 0.42035364*I
            sage: CC(2).gamma_inc(5)
            0.0404276819945128

        TESTS:

        Check that :issue:`7099` is fixed::

            sage: C = ComplexField(400)
            sage: C(2 + I).gamma_inc(C(3 + I))  # abs tol 1e-120                        # needs sage.libs.pari
            0.121515644664508695525971545977439666159749344176962379708992904126499444842886620664991650378432544392118359044438541515 + 0.101533909079826033296475736021224621546966200987295663190553587086145836461236284668967411665020429964946098113930918850*I"""
    @overload
    def imag(self) -> Any:
        """ComplexNumber.imag(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 1805)

        Return imaginary part of ``self``.

        EXAMPLES::

            sage: i = ComplexField(100).0
            sage: z = 2 + 3*i
            sage: x = z.imag(); x
            3.0000000000000000000000000000
            sage: x.parent()
            Real Field with 100 bits of precision
            sage: z.imag_part()
            3.0000000000000000000000000000"""
    @overload
    def imag(self) -> Any:
        """ComplexNumber.imag(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 1805)

        Return imaginary part of ``self``.

        EXAMPLES::

            sage: i = ComplexField(100).0
            sage: z = 2 + 3*i
            sage: x = z.imag(); x
            3.0000000000000000000000000000
            sage: x.parent()
            Real Field with 100 bits of precision
            sage: z.imag_part()
            3.0000000000000000000000000000"""
    def imag_part(self) -> Any:
        """ComplexNumber.imag(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 1805)

        Return imaginary part of ``self``.

        EXAMPLES::

            sage: i = ComplexField(100).0
            sage: z = 2 + 3*i
            sage: x = z.imag(); x
            3.0000000000000000000000000000
            sage: x.parent()
            Real Field with 100 bits of precision
            sage: z.imag_part()
            3.0000000000000000000000000000"""
    @overload
    def is_NaN(self) -> Any:
        """ComplexNumber.is_NaN(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 3218)

        Check if ``self`` is not-a-number.

        EXAMPLES::

            sage: CC(1, 2).is_NaN()
            False
            sage: CC(NaN).is_NaN()
            True
            sage: CC(NaN,2).log().is_NaN()
            True"""
    @overload
    def is_NaN(self) -> Any:
        """ComplexNumber.is_NaN(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 3218)

        Check if ``self`` is not-a-number.

        EXAMPLES::

            sage: CC(1, 2).is_NaN()
            False
            sage: CC(NaN).is_NaN()
            True
            sage: CC(NaN,2).log().is_NaN()
            True"""
    @overload
    def is_NaN(self) -> Any:
        """ComplexNumber.is_NaN(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 3218)

        Check if ``self`` is not-a-number.

        EXAMPLES::

            sage: CC(1, 2).is_NaN()
            False
            sage: CC(NaN).is_NaN()
            True
            sage: CC(NaN,2).log().is_NaN()
            True"""
    @overload
    def is_NaN(self) -> Any:
        """ComplexNumber.is_NaN(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 3218)

        Check if ``self`` is not-a-number.

        EXAMPLES::

            sage: CC(1, 2).is_NaN()
            False
            sage: CC(NaN).is_NaN()
            True
            sage: CC(NaN,2).log().is_NaN()
            True"""
    @overload
    def is_imaginary(self) -> Any:
        """ComplexNumber.is_imaginary(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 3149)

        Return ``True`` if ``self`` is imaginary, i.e., has real part zero.

        EXAMPLES::

            sage: CC(1.23*i).is_imaginary()
            True
            sage: CC(1+i).is_imaginary()
            False"""
    @overload
    def is_imaginary(self) -> Any:
        """ComplexNumber.is_imaginary(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 3149)

        Return ``True`` if ``self`` is imaginary, i.e., has real part zero.

        EXAMPLES::

            sage: CC(1.23*i).is_imaginary()
            True
            sage: CC(1+i).is_imaginary()
            False"""
    @overload
    def is_imaginary(self) -> Any:
        """ComplexNumber.is_imaginary(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 3149)

        Return ``True`` if ``self`` is imaginary, i.e., has real part zero.

        EXAMPLES::

            sage: CC(1.23*i).is_imaginary()
            True
            sage: CC(1+i).is_imaginary()
            False"""
    def is_infinity(self) -> Any:
        """ComplexNumber.is_infinity(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 3205)

        Check if ``self`` is `\\infty`.

        EXAMPLES::

            sage: CC(1, 2).is_infinity()
            False
            sage: CC(0, oo).is_infinity()
            True"""
    @overload
    def is_integer(self) -> Any:
        """ComplexNumber.is_integer(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 3162)

        Return ``True`` if ``self`` is an integer.

        EXAMPLES::

            sage: CC(3).is_integer()
            True
            sage: CC(1,2).is_integer()
            False"""
    @overload
    def is_integer(self) -> Any:
        """ComplexNumber.is_integer(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 3162)

        Return ``True`` if ``self`` is an integer.

        EXAMPLES::

            sage: CC(3).is_integer()
            True
            sage: CC(1,2).is_integer()
            False"""
    @overload
    def is_integer(self) -> Any:
        """ComplexNumber.is_integer(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 3162)

        Return ``True`` if ``self`` is an integer.

        EXAMPLES::

            sage: CC(3).is_integer()
            True
            sage: CC(1,2).is_integer()
            False"""
    def is_negative_infinity(self) -> Any:
        """ComplexNumber.is_negative_infinity(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 3190)

        Check if ``self`` is `-\\infty`.

        EXAMPLES::

            sage: CC(1, 2).is_negative_infinity()
            False
            sage: CC(-oo, 0).is_negative_infinity()
            True
            sage: CC(0, -oo).is_negative_infinity()
            False"""
    def is_positive_infinity(self) -> Any:
        """ComplexNumber.is_positive_infinity(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 3175)

        Check if ``self`` is `+\\infty`.

        EXAMPLES::

            sage: CC(1, 2).is_positive_infinity()
            False
            sage: CC(oo, 0).is_positive_infinity()
            True
            sage: CC(0, oo).is_positive_infinity()
            False"""
    @overload
    def is_real(self) -> Any:
        """ComplexNumber.is_real(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 3136)

        Return ``True`` if ``self`` is real, i.e., has imaginary part zero.

        EXAMPLES::

            sage: CC(1.23).is_real()
            True
            sage: CC(1+i).is_real()
            False"""
    @overload
    def is_real(self) -> Any:
        """ComplexNumber.is_real(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 3136)

        Return ``True`` if ``self`` is real, i.e., has imaginary part zero.

        EXAMPLES::

            sage: CC(1.23).is_real()
            True
            sage: CC(1+i).is_real()
            False"""
    @overload
    def is_real(self) -> Any:
        """ComplexNumber.is_real(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 3136)

        Return ``True`` if ``self`` is real, i.e., has imaginary part zero.

        EXAMPLES::

            sage: CC(1.23).is_real()
            True
            sage: CC(1+i).is_real()
            False"""
    def is_square(self) -> Any:
        """ComplexNumber.is_square(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 3117)

        This function always returns true as `\\CC` is algebraically closed.

        EXAMPLES::

            sage: a = ComplexNumber(2,1)
            sage: a.is_square()
            True

        `\\CC` is algebraically closed, hence every element
        is a square::

            sage: b = ComplexNumber(5)
            sage: b.is_square()
            True"""
    def log(self, base=...) -> Any:
        """ComplexNumber.log(self, base=None)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 2914)

        Complex logarithm of `z` with branch chosen as follows: Write
        `z = \\rho e^{i \\theta}` with `-\\pi < \\theta \\leq \\pi`. Then
        `\\log(z) = \\log(\\rho) + i \\theta`.

        .. WARNING::

           Currently the real log is computed using floats, so there
           is potential precision loss.

        EXAMPLES::

            sage: a = ComplexNumber(2,1)
            sage: a.log()
            0.804718956217050 + 0.463647609000806*I
            sage: log(a.abs())
            0.804718956217050
            sage: a.argument()
            0.463647609000806

        ::

            sage: b = ComplexNumber(float(exp(42)),0)
            sage: b.log()  # abs tol 1e-12
            41.99999999999971

        ::

            sage: c = ComplexNumber(-1,0)
            sage: c.log()
            3.14159265358979*I

        The option of a base is included for compatibility with other logs::

            sage: c = ComplexNumber(-1,0)
            sage: c.log(2)
            4.53236014182719*I

        If either component (real or imaginary) of the complex number
        is NaN (not a number), log will return the complex NaN::

            sage: c = ComplexNumber(NaN,2)
            sage: c.log()
            NaN + NaN*I"""
    @overload
    def multiplicative_order(self) -> Any:
        """ComplexNumber.multiplicative_order(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 2030)

        Return the multiplicative order of this complex number, if known,
        or raise a :exc:`NotImplementedError`.

        EXAMPLES::

            sage: C.<i> = ComplexField()
            sage: i.multiplicative_order()
            4
            sage: C(1).multiplicative_order()
            1
            sage: C(-1).multiplicative_order()
            2
            sage: C(i^2).multiplicative_order()
            2
            sage: C(-i).multiplicative_order()
            4
            sage: C(2).multiplicative_order()
            +Infinity
            sage: w = (1+sqrt(-3.0))/2; w
            0.500000000000000 + 0.866025403784439*I
            sage: abs(w)
            1.00000000000000
            sage: w.multiplicative_order()
            Traceback (most recent call last):
            ...
            NotImplementedError: order of element not known"""
    @overload
    def multiplicative_order(self) -> Any:
        """ComplexNumber.multiplicative_order(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 2030)

        Return the multiplicative order of this complex number, if known,
        or raise a :exc:`NotImplementedError`.

        EXAMPLES::

            sage: C.<i> = ComplexField()
            sage: i.multiplicative_order()
            4
            sage: C(1).multiplicative_order()
            1
            sage: C(-1).multiplicative_order()
            2
            sage: C(i^2).multiplicative_order()
            2
            sage: C(-i).multiplicative_order()
            4
            sage: C(2).multiplicative_order()
            +Infinity
            sage: w = (1+sqrt(-3.0))/2; w
            0.500000000000000 + 0.866025403784439*I
            sage: abs(w)
            1.00000000000000
            sage: w.multiplicative_order()
            Traceback (most recent call last):
            ...
            NotImplementedError: order of element not known"""
    @overload
    def multiplicative_order(self) -> Any:
        """ComplexNumber.multiplicative_order(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 2030)

        Return the multiplicative order of this complex number, if known,
        or raise a :exc:`NotImplementedError`.

        EXAMPLES::

            sage: C.<i> = ComplexField()
            sage: i.multiplicative_order()
            4
            sage: C(1).multiplicative_order()
            1
            sage: C(-1).multiplicative_order()
            2
            sage: C(i^2).multiplicative_order()
            2
            sage: C(-i).multiplicative_order()
            4
            sage: C(2).multiplicative_order()
            +Infinity
            sage: w = (1+sqrt(-3.0))/2; w
            0.500000000000000 + 0.866025403784439*I
            sage: abs(w)
            1.00000000000000
            sage: w.multiplicative_order()
            Traceback (most recent call last):
            ...
            NotImplementedError: order of element not known"""
    @overload
    def multiplicative_order(self) -> Any:
        """ComplexNumber.multiplicative_order(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 2030)

        Return the multiplicative order of this complex number, if known,
        or raise a :exc:`NotImplementedError`.

        EXAMPLES::

            sage: C.<i> = ComplexField()
            sage: i.multiplicative_order()
            4
            sage: C(1).multiplicative_order()
            1
            sage: C(-1).multiplicative_order()
            2
            sage: C(i^2).multiplicative_order()
            2
            sage: C(-i).multiplicative_order()
            4
            sage: C(2).multiplicative_order()
            +Infinity
            sage: w = (1+sqrt(-3.0))/2; w
            0.500000000000000 + 0.866025403784439*I
            sage: abs(w)
            1.00000000000000
            sage: w.multiplicative_order()
            Traceback (most recent call last):
            ...
            NotImplementedError: order of element not known"""
    @overload
    def multiplicative_order(self) -> Any:
        """ComplexNumber.multiplicative_order(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 2030)

        Return the multiplicative order of this complex number, if known,
        or raise a :exc:`NotImplementedError`.

        EXAMPLES::

            sage: C.<i> = ComplexField()
            sage: i.multiplicative_order()
            4
            sage: C(1).multiplicative_order()
            1
            sage: C(-1).multiplicative_order()
            2
            sage: C(i^2).multiplicative_order()
            2
            sage: C(-i).multiplicative_order()
            4
            sage: C(2).multiplicative_order()
            +Infinity
            sage: w = (1+sqrt(-3.0))/2; w
            0.500000000000000 + 0.866025403784439*I
            sage: abs(w)
            1.00000000000000
            sage: w.multiplicative_order()
            Traceback (most recent call last):
            ...
            NotImplementedError: order of element not known"""
    @overload
    def multiplicative_order(self) -> Any:
        """ComplexNumber.multiplicative_order(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 2030)

        Return the multiplicative order of this complex number, if known,
        or raise a :exc:`NotImplementedError`.

        EXAMPLES::

            sage: C.<i> = ComplexField()
            sage: i.multiplicative_order()
            4
            sage: C(1).multiplicative_order()
            1
            sage: C(-1).multiplicative_order()
            2
            sage: C(i^2).multiplicative_order()
            2
            sage: C(-i).multiplicative_order()
            4
            sage: C(2).multiplicative_order()
            +Infinity
            sage: w = (1+sqrt(-3.0))/2; w
            0.500000000000000 + 0.866025403784439*I
            sage: abs(w)
            1.00000000000000
            sage: w.multiplicative_order()
            Traceback (most recent call last):
            ...
            NotImplementedError: order of element not known"""
    @overload
    def multiplicative_order(self) -> Any:
        """ComplexNumber.multiplicative_order(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 2030)

        Return the multiplicative order of this complex number, if known,
        or raise a :exc:`NotImplementedError`.

        EXAMPLES::

            sage: C.<i> = ComplexField()
            sage: i.multiplicative_order()
            4
            sage: C(1).multiplicative_order()
            1
            sage: C(-1).multiplicative_order()
            2
            sage: C(i^2).multiplicative_order()
            2
            sage: C(-i).multiplicative_order()
            4
            sage: C(2).multiplicative_order()
            +Infinity
            sage: w = (1+sqrt(-3.0))/2; w
            0.500000000000000 + 0.866025403784439*I
            sage: abs(w)
            1.00000000000000
            sage: w.multiplicative_order()
            Traceback (most recent call last):
            ...
            NotImplementedError: order of element not known"""
    @overload
    def multiplicative_order(self) -> Any:
        """ComplexNumber.multiplicative_order(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 2030)

        Return the multiplicative order of this complex number, if known,
        or raise a :exc:`NotImplementedError`.

        EXAMPLES::

            sage: C.<i> = ComplexField()
            sage: i.multiplicative_order()
            4
            sage: C(1).multiplicative_order()
            1
            sage: C(-1).multiplicative_order()
            2
            sage: C(i^2).multiplicative_order()
            2
            sage: C(-i).multiplicative_order()
            4
            sage: C(2).multiplicative_order()
            +Infinity
            sage: w = (1+sqrt(-3.0))/2; w
            0.500000000000000 + 0.866025403784439*I
            sage: abs(w)
            1.00000000000000
            sage: w.multiplicative_order()
            Traceback (most recent call last):
            ...
            NotImplementedError: order of element not known"""
    def norm(self) -> Any:
        """ComplexNumber.norm(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 1563)

        Return the norm of this complex number.

        If `c = a + bi` is a complex number, then the norm of `c` is defined as
        the product of `c` and its complex conjugate:

        .. MATH::

            \\text{norm}(c)
            =
            \\text{norm}(a + bi)
            =
            c \\cdot \\overline{c}
            =
            a^2 + b^2.

        The norm of a complex number is different from its absolute value.
        The absolute value of a complex number is defined to be the square
        root of its norm. A typical use of the complex norm is in the
        integral domain `\\ZZ[i]` of Gaussian integers, where the norm of
        each Gaussian integer `c = a + bi` is defined as its complex norm.

        .. SEEALSO::

            - :func:`sage.misc.functional.norm`

            - :meth:`sage.rings.complex_double.ComplexDoubleElement.norm`

        EXAMPLES:

        This indeed acts as the square function when the
        imaginary component of ``self`` is equal to zero::

            sage: a = ComplexNumber(2,1)
            sage: a.norm()
            5.00000000000000
            sage: b = ComplexNumber(4.2,0)
            sage: b.norm()
            17.6400000000000
            sage: b^2
            17.6400000000000"""
    def nth_root(self, n, all=...) -> Any:
        """ComplexNumber.nth_root(self, n, all=False)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 3058)

        The `n`-th root function.

        INPUT:

        - ``all`` -- boolean (default: ``False``); if ``True``, return a
          list of all `n`-th roots

        EXAMPLES::

            sage: a = CC(27)
            sage: a.nth_root(3)
            3.00000000000000
            sage: a.nth_root(3, all=True)
            [3.00000000000000,
             -1.50000000000000 + 2.59807621135332*I,
             -1.50000000000000 - 2.59807621135332*I]
            sage: a = ComplexField(20)(2,1)
            sage: [r^7 for r in a.nth_root(7, all=True)]
            [2.0000 + 1.0000*I, 2.0000 + 1.0000*I, 2.0000 + 1.0000*I, 2.0000 + 1.0000*I,
             2.0000 + 1.0000*I, 2.0000 + 1.0001*I, 2.0000 + 1.0001*I]"""
    @overload
    def plot(self, **kargs) -> Any:
        """ComplexNumber.plot(self, **kargs)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 2077)

        Plots this complex number as a point in the plane.

        The accepted options are the ones of :meth:`~sage.plot.point.point2d`.
        Type ``point2d.options`` to see all options.

        .. NOTE::

            Just wraps the sage.plot.point.point2d method

        EXAMPLES:

        You can either use the indirect::

            sage: z = CC(0,1)
            sage: plot(z)                                                               # needs sage.plot
            Graphics object consisting of 1 graphics primitive

        or the more direct::

            sage: z = CC(0,1)
            sage: z.plot()                                                              # needs sage.plot
            Graphics object consisting of 1 graphics primitive"""
    @overload
    def plot(self, z) -> Any:
        """ComplexNumber.plot(self, **kargs)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 2077)

        Plots this complex number as a point in the plane.

        The accepted options are the ones of :meth:`~sage.plot.point.point2d`.
        Type ``point2d.options`` to see all options.

        .. NOTE::

            Just wraps the sage.plot.point.point2d method

        EXAMPLES:

        You can either use the indirect::

            sage: z = CC(0,1)
            sage: plot(z)                                                               # needs sage.plot
            Graphics object consisting of 1 graphics primitive

        or the more direct::

            sage: z = CC(0,1)
            sage: z.plot()                                                              # needs sage.plot
            Graphics object consisting of 1 graphics primitive"""
    @overload
    def plot(self) -> Any:
        """ComplexNumber.plot(self, **kargs)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 2077)

        Plots this complex number as a point in the plane.

        The accepted options are the ones of :meth:`~sage.plot.point.point2d`.
        Type ``point2d.options`` to see all options.

        .. NOTE::

            Just wraps the sage.plot.point.point2d method

        EXAMPLES:

        You can either use the indirect::

            sage: z = CC(0,1)
            sage: plot(z)                                                               # needs sage.plot
            Graphics object consisting of 1 graphics primitive

        or the more direct::

            sage: z = CC(0,1)
            sage: z.plot()                                                              # needs sage.plot
            Graphics object consisting of 1 graphics primitive"""
    @overload
    def prec(self) -> Any:
        """ComplexNumber.prec(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 1771)

        Return precision of this complex number.

        EXAMPLES::

            sage: i = ComplexField(2000).0
            sage: i.prec()
            2000"""
    @overload
    def prec(self) -> Any:
        """ComplexNumber.prec(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 1771)

        Return precision of this complex number.

        EXAMPLES::

            sage: i = ComplexField(2000).0
            sage: i.prec()
            2000"""
    @overload
    def real(self) -> Any:
        """ComplexNumber.real(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 1783)

        Return real part of ``self``.

        EXAMPLES::

            sage: i = ComplexField(100).0
            sage: z = 2 + 3*i
            sage: x = z.real(); x
            2.0000000000000000000000000000
            sage: x.parent()
            Real Field with 100 bits of precision
            sage: z.real_part()
            2.0000000000000000000000000000"""
    @overload
    def real(self) -> Any:
        """ComplexNumber.real(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 1783)

        Return real part of ``self``.

        EXAMPLES::

            sage: i = ComplexField(100).0
            sage: z = 2 + 3*i
            sage: x = z.real(); x
            2.0000000000000000000000000000
            sage: x.parent()
            Real Field with 100 bits of precision
            sage: z.real_part()
            2.0000000000000000000000000000"""
    def real_part(self) -> Any:
        """ComplexNumber.real(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 1783)

        Return real part of ``self``.

        EXAMPLES::

            sage: i = ComplexField(100).0
            sage: z = 2 + 3*i
            sage: x = z.real(); x
            2.0000000000000000000000000000
            sage: x.parent()
            Real Field with 100 bits of precision
            sage: z.real_part()
            2.0000000000000000000000000000"""
    @overload
    def sec(self) -> Any:
        """ComplexNumber.sec(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 2230)

        Return the secant of ``self``.

        EXAMPLES::

            sage: ComplexField(100)(1,1).sec()                                          # needs sage.libs.pari
            0.49833703055518678521380589177 + 0.59108384172104504805039169297*I"""
    @overload
    def sec(self) -> Any:
        """ComplexNumber.sec(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 2230)

        Return the secant of ``self``.

        EXAMPLES::

            sage: ComplexField(100)(1,1).sec()                                          # needs sage.libs.pari
            0.49833703055518678521380589177 + 0.59108384172104504805039169297*I"""
    @overload
    def sech(self) -> Any:
        """ComplexNumber.sech(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 2241)

        Return the hyperbolic secant of ``self``.

        EXAMPLES::

            sage: ComplexField(100)(1,1).sech()                                         # needs sage.libs.pari
            0.49833703055518678521380589177 - 0.59108384172104504805039169297*I"""
    @overload
    def sech(self) -> Any:
        """ComplexNumber.sech(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 2241)

        Return the hyperbolic secant of ``self``.

        EXAMPLES::

            sage: ComplexField(100)(1,1).sech()                                         # needs sage.libs.pari
            0.49833703055518678521380589177 - 0.59108384172104504805039169297*I"""
    @overload
    def sin(self) -> Any:
        """ComplexNumber.sin(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 2408)

        Return the sine of ``self``.

        EXAMPLES::

            sage: (1+CC(I)).sin()
            1.29845758141598 + 0.634963914784736*I"""
    @overload
    def sin(self) -> Any:
        """ComplexNumber.sin(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 2408)

        Return the sine of ``self``.

        EXAMPLES::

            sage: (1+CC(I)).sin()
            1.29845758141598 + 0.634963914784736*I"""
    @overload
    def sinh(self) -> Any:
        """ComplexNumber.sinh(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 2435)

        Return the hyperbolic sine of ``self``.

        EXAMPLES::

            sage: (1+CC(I)).sinh()
            0.634963914784736 + 1.29845758141598*I"""
    @overload
    def sinh(self) -> Any:
        """ComplexNumber.sinh(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 2435)

        Return the hyperbolic sine of ``self``.

        EXAMPLES::

            sage: (1+CC(I)).sinh()
            0.634963914784736 + 1.29845758141598*I"""
    @overload
    def sqrt(self, all=...) -> Any:
        """ComplexNumber.sqrt(self, all=False)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 2988)

        The square root function, taking the branch cut to be the negative
        real axis.

        INPUT:

        - ``all`` -- boolean (default: ``False``); if ``True``, return a
          list of all square roots

        EXAMPLES::

            sage: C.<i> = ComplexField(30)
            sage: i.sqrt()
            0.70710678 + 0.70710678*I
            sage: (1+i).sqrt()
            1.0986841 + 0.45508986*I
            sage: (C(-1)).sqrt()
            1.0000000*I
            sage: (1 + 1e-100*i).sqrt()^2
            1.0000000 + 1.0000000e-100*I
            sage: i = ComplexField(200).0
            sage: i.sqrt()
            0.70710678118654752440084436210484903928483593768847403658834 + 0.70710678118654752440084436210484903928483593768847403658834*I"""
    @overload
    def sqrt(self) -> Any:
        """ComplexNumber.sqrt(self, all=False)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 2988)

        The square root function, taking the branch cut to be the negative
        real axis.

        INPUT:

        - ``all`` -- boolean (default: ``False``); if ``True``, return a
          list of all square roots

        EXAMPLES::

            sage: C.<i> = ComplexField(30)
            sage: i.sqrt()
            0.70710678 + 0.70710678*I
            sage: (1+i).sqrt()
            1.0986841 + 0.45508986*I
            sage: (C(-1)).sqrt()
            1.0000000*I
            sage: (1 + 1e-100*i).sqrt()^2
            1.0000000 + 1.0000000e-100*I
            sage: i = ComplexField(200).0
            sage: i.sqrt()
            0.70710678118654752440084436210484903928483593768847403658834 + 0.70710678118654752440084436210484903928483593768847403658834*I"""
    @overload
    def sqrt(self) -> Any:
        """ComplexNumber.sqrt(self, all=False)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 2988)

        The square root function, taking the branch cut to be the negative
        real axis.

        INPUT:

        - ``all`` -- boolean (default: ``False``); if ``True``, return a
          list of all square roots

        EXAMPLES::

            sage: C.<i> = ComplexField(30)
            sage: i.sqrt()
            0.70710678 + 0.70710678*I
            sage: (1+i).sqrt()
            1.0986841 + 0.45508986*I
            sage: (C(-1)).sqrt()
            1.0000000*I
            sage: (1 + 1e-100*i).sqrt()^2
            1.0000000 + 1.0000000e-100*I
            sage: i = ComplexField(200).0
            sage: i.sqrt()
            0.70710678118654752440084436210484903928483593768847403658834 + 0.70710678118654752440084436210484903928483593768847403658834*I"""
    @overload
    def sqrt(self) -> Any:
        """ComplexNumber.sqrt(self, all=False)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 2988)

        The square root function, taking the branch cut to be the negative
        real axis.

        INPUT:

        - ``all`` -- boolean (default: ``False``); if ``True``, return a
          list of all square roots

        EXAMPLES::

            sage: C.<i> = ComplexField(30)
            sage: i.sqrt()
            0.70710678 + 0.70710678*I
            sage: (1+i).sqrt()
            1.0986841 + 0.45508986*I
            sage: (C(-1)).sqrt()
            1.0000000*I
            sage: (1 + 1e-100*i).sqrt()^2
            1.0000000 + 1.0000000e-100*I
            sage: i = ComplexField(200).0
            sage: i.sqrt()
            0.70710678118654752440084436210484903928483593768847403658834 + 0.70710678118654752440084436210484903928483593768847403658834*I"""
    @overload
    def sqrt(self) -> Any:
        """ComplexNumber.sqrt(self, all=False)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 2988)

        The square root function, taking the branch cut to be the negative
        real axis.

        INPUT:

        - ``all`` -- boolean (default: ``False``); if ``True``, return a
          list of all square roots

        EXAMPLES::

            sage: C.<i> = ComplexField(30)
            sage: i.sqrt()
            0.70710678 + 0.70710678*I
            sage: (1+i).sqrt()
            1.0986841 + 0.45508986*I
            sage: (C(-1)).sqrt()
            1.0000000*I
            sage: (1 + 1e-100*i).sqrt()^2
            1.0000000 + 1.0000000e-100*I
            sage: i = ComplexField(200).0
            sage: i.sqrt()
            0.70710678118654752440084436210484903928483593768847403658834 + 0.70710678118654752440084436210484903928483593768847403658834*I"""
    @overload
    def sqrt(self) -> Any:
        """ComplexNumber.sqrt(self, all=False)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 2988)

        The square root function, taking the branch cut to be the negative
        real axis.

        INPUT:

        - ``all`` -- boolean (default: ``False``); if ``True``, return a
          list of all square roots

        EXAMPLES::

            sage: C.<i> = ComplexField(30)
            sage: i.sqrt()
            0.70710678 + 0.70710678*I
            sage: (1+i).sqrt()
            1.0986841 + 0.45508986*I
            sage: (C(-1)).sqrt()
            1.0000000*I
            sage: (1 + 1e-100*i).sqrt()^2
            1.0000000 + 1.0000000e-100*I
            sage: i = ComplexField(200).0
            sage: i.sqrt()
            0.70710678118654752440084436210484903928483593768847403658834 + 0.70710678118654752440084436210484903928483593768847403658834*I"""
    @overload
    def str(self, base=..., istr=..., **kwds) -> Any:
        """ComplexNumber.str(self, base=10, istr='I', **kwds)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 1275)

        Return a string representation of ``self``.

        INPUT:

        - ``base`` -- (default: 10) base for output

        - ``istr`` -- (default: ``I``) string representation of the complex unit

        - ``**kwds`` -- other arguments to pass to the ``str()``
          method of the real numbers in the real and imaginary parts

        EXAMPLES::

            sage: # needs sage.symbolic
            sage: a = CC(pi + I*e); a
            3.14159265358979 + 2.71828182845905*I
            sage: a.str(truncate=True)
            '3.14159265358979 + 2.71828182845905*I'
            sage: a.str()
            '3.1415926535897931 + 2.7182818284590451*I'
            sage: a.str(base=2)
            '11.001001000011111101101010100010001000010110100011000 + 10.101101111110000101010001011000101000101011101101001*I'
            sage: CC(0.5 + 0.625*I).str(base=2)
            '0.10000000000000000000000000000000000000000000000000000 + 0.10100000000000000000000000000000000000000000000000000*I'
            sage: a.str(base=16)
            '3.243f6a8885a30 + 2.b7e151628aed2*I'
            sage: a.str(base=36)
            '3.53i5ab8p5fc + 2.puw5nggjf8f*I'

            sage: CC(0)
            0.000000000000000
            sage: CC.0.str(istr='%i')
            '1.0000000000000000*%i'"""
    @overload
    def str(self) -> Any:
        """ComplexNumber.str(self, base=10, istr='I', **kwds)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 1275)

        Return a string representation of ``self``.

        INPUT:

        - ``base`` -- (default: 10) base for output

        - ``istr`` -- (default: ``I``) string representation of the complex unit

        - ``**kwds`` -- other arguments to pass to the ``str()``
          method of the real numbers in the real and imaginary parts

        EXAMPLES::

            sage: # needs sage.symbolic
            sage: a = CC(pi + I*e); a
            3.14159265358979 + 2.71828182845905*I
            sage: a.str(truncate=True)
            '3.14159265358979 + 2.71828182845905*I'
            sage: a.str()
            '3.1415926535897931 + 2.7182818284590451*I'
            sage: a.str(base=2)
            '11.001001000011111101101010100010001000010110100011000 + 10.101101111110000101010001011000101000101011101101001*I'
            sage: CC(0.5 + 0.625*I).str(base=2)
            '0.10000000000000000000000000000000000000000000000000000 + 0.10100000000000000000000000000000000000000000000000000*I'
            sage: a.str(base=16)
            '3.243f6a8885a30 + 2.b7e151628aed2*I'
            sage: a.str(base=36)
            '3.53i5ab8p5fc + 2.puw5nggjf8f*I'

            sage: CC(0)
            0.000000000000000
            sage: CC.0.str(istr='%i')
            '1.0000000000000000*%i'"""
    @overload
    def str(self, truncate=...) -> Any:
        """ComplexNumber.str(self, base=10, istr='I', **kwds)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 1275)

        Return a string representation of ``self``.

        INPUT:

        - ``base`` -- (default: 10) base for output

        - ``istr`` -- (default: ``I``) string representation of the complex unit

        - ``**kwds`` -- other arguments to pass to the ``str()``
          method of the real numbers in the real and imaginary parts

        EXAMPLES::

            sage: # needs sage.symbolic
            sage: a = CC(pi + I*e); a
            3.14159265358979 + 2.71828182845905*I
            sage: a.str(truncate=True)
            '3.14159265358979 + 2.71828182845905*I'
            sage: a.str()
            '3.1415926535897931 + 2.7182818284590451*I'
            sage: a.str(base=2)
            '11.001001000011111101101010100010001000010110100011000 + 10.101101111110000101010001011000101000101011101101001*I'
            sage: CC(0.5 + 0.625*I).str(base=2)
            '0.10000000000000000000000000000000000000000000000000000 + 0.10100000000000000000000000000000000000000000000000000*I'
            sage: a.str(base=16)
            '3.243f6a8885a30 + 2.b7e151628aed2*I'
            sage: a.str(base=36)
            '3.53i5ab8p5fc + 2.puw5nggjf8f*I'

            sage: CC(0)
            0.000000000000000
            sage: CC.0.str(istr='%i')
            '1.0000000000000000*%i'"""
    @overload
    def str(self) -> Any:
        """ComplexNumber.str(self, base=10, istr='I', **kwds)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 1275)

        Return a string representation of ``self``.

        INPUT:

        - ``base`` -- (default: 10) base for output

        - ``istr`` -- (default: ``I``) string representation of the complex unit

        - ``**kwds`` -- other arguments to pass to the ``str()``
          method of the real numbers in the real and imaginary parts

        EXAMPLES::

            sage: # needs sage.symbolic
            sage: a = CC(pi + I*e); a
            3.14159265358979 + 2.71828182845905*I
            sage: a.str(truncate=True)
            '3.14159265358979 + 2.71828182845905*I'
            sage: a.str()
            '3.1415926535897931 + 2.7182818284590451*I'
            sage: a.str(base=2)
            '11.001001000011111101101010100010001000010110100011000 + 10.101101111110000101010001011000101000101011101101001*I'
            sage: CC(0.5 + 0.625*I).str(base=2)
            '0.10000000000000000000000000000000000000000000000000000 + 0.10100000000000000000000000000000000000000000000000000*I'
            sage: a.str(base=16)
            '3.243f6a8885a30 + 2.b7e151628aed2*I'
            sage: a.str(base=36)
            '3.53i5ab8p5fc + 2.puw5nggjf8f*I'

            sage: CC(0)
            0.000000000000000
            sage: CC.0.str(istr='%i')
            '1.0000000000000000*%i'"""
    @overload
    def str(self, base=...) -> Any:
        """ComplexNumber.str(self, base=10, istr='I', **kwds)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 1275)

        Return a string representation of ``self``.

        INPUT:

        - ``base`` -- (default: 10) base for output

        - ``istr`` -- (default: ``I``) string representation of the complex unit

        - ``**kwds`` -- other arguments to pass to the ``str()``
          method of the real numbers in the real and imaginary parts

        EXAMPLES::

            sage: # needs sage.symbolic
            sage: a = CC(pi + I*e); a
            3.14159265358979 + 2.71828182845905*I
            sage: a.str(truncate=True)
            '3.14159265358979 + 2.71828182845905*I'
            sage: a.str()
            '3.1415926535897931 + 2.7182818284590451*I'
            sage: a.str(base=2)
            '11.001001000011111101101010100010001000010110100011000 + 10.101101111110000101010001011000101000101011101101001*I'
            sage: CC(0.5 + 0.625*I).str(base=2)
            '0.10000000000000000000000000000000000000000000000000000 + 0.10100000000000000000000000000000000000000000000000000*I'
            sage: a.str(base=16)
            '3.243f6a8885a30 + 2.b7e151628aed2*I'
            sage: a.str(base=36)
            '3.53i5ab8p5fc + 2.puw5nggjf8f*I'

            sage: CC(0)
            0.000000000000000
            sage: CC.0.str(istr='%i')
            '1.0000000000000000*%i'"""
    @overload
    def str(self, base=...) -> Any:
        """ComplexNumber.str(self, base=10, istr='I', **kwds)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 1275)

        Return a string representation of ``self``.

        INPUT:

        - ``base`` -- (default: 10) base for output

        - ``istr`` -- (default: ``I``) string representation of the complex unit

        - ``**kwds`` -- other arguments to pass to the ``str()``
          method of the real numbers in the real and imaginary parts

        EXAMPLES::

            sage: # needs sage.symbolic
            sage: a = CC(pi + I*e); a
            3.14159265358979 + 2.71828182845905*I
            sage: a.str(truncate=True)
            '3.14159265358979 + 2.71828182845905*I'
            sage: a.str()
            '3.1415926535897931 + 2.7182818284590451*I'
            sage: a.str(base=2)
            '11.001001000011111101101010100010001000010110100011000 + 10.101101111110000101010001011000101000101011101101001*I'
            sage: CC(0.5 + 0.625*I).str(base=2)
            '0.10000000000000000000000000000000000000000000000000000 + 0.10100000000000000000000000000000000000000000000000000*I'
            sage: a.str(base=16)
            '3.243f6a8885a30 + 2.b7e151628aed2*I'
            sage: a.str(base=36)
            '3.53i5ab8p5fc + 2.puw5nggjf8f*I'

            sage: CC(0)
            0.000000000000000
            sage: CC.0.str(istr='%i')
            '1.0000000000000000*%i'"""
    @overload
    def str(self, base=...) -> Any:
        """ComplexNumber.str(self, base=10, istr='I', **kwds)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 1275)

        Return a string representation of ``self``.

        INPUT:

        - ``base`` -- (default: 10) base for output

        - ``istr`` -- (default: ``I``) string representation of the complex unit

        - ``**kwds`` -- other arguments to pass to the ``str()``
          method of the real numbers in the real and imaginary parts

        EXAMPLES::

            sage: # needs sage.symbolic
            sage: a = CC(pi + I*e); a
            3.14159265358979 + 2.71828182845905*I
            sage: a.str(truncate=True)
            '3.14159265358979 + 2.71828182845905*I'
            sage: a.str()
            '3.1415926535897931 + 2.7182818284590451*I'
            sage: a.str(base=2)
            '11.001001000011111101101010100010001000010110100011000 + 10.101101111110000101010001011000101000101011101101001*I'
            sage: CC(0.5 + 0.625*I).str(base=2)
            '0.10000000000000000000000000000000000000000000000000000 + 0.10100000000000000000000000000000000000000000000000000*I'
            sage: a.str(base=16)
            '3.243f6a8885a30 + 2.b7e151628aed2*I'
            sage: a.str(base=36)
            '3.53i5ab8p5fc + 2.puw5nggjf8f*I'

            sage: CC(0)
            0.000000000000000
            sage: CC.0.str(istr='%i')
            '1.0000000000000000*%i'"""
    @overload
    def str(self, base=...) -> Any:
        """ComplexNumber.str(self, base=10, istr='I', **kwds)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 1275)

        Return a string representation of ``self``.

        INPUT:

        - ``base`` -- (default: 10) base for output

        - ``istr`` -- (default: ``I``) string representation of the complex unit

        - ``**kwds`` -- other arguments to pass to the ``str()``
          method of the real numbers in the real and imaginary parts

        EXAMPLES::

            sage: # needs sage.symbolic
            sage: a = CC(pi + I*e); a
            3.14159265358979 + 2.71828182845905*I
            sage: a.str(truncate=True)
            '3.14159265358979 + 2.71828182845905*I'
            sage: a.str()
            '3.1415926535897931 + 2.7182818284590451*I'
            sage: a.str(base=2)
            '11.001001000011111101101010100010001000010110100011000 + 10.101101111110000101010001011000101000101011101101001*I'
            sage: CC(0.5 + 0.625*I).str(base=2)
            '0.10000000000000000000000000000000000000000000000000000 + 0.10100000000000000000000000000000000000000000000000000*I'
            sage: a.str(base=16)
            '3.243f6a8885a30 + 2.b7e151628aed2*I'
            sage: a.str(base=36)
            '3.53i5ab8p5fc + 2.puw5nggjf8f*I'

            sage: CC(0)
            0.000000000000000
            sage: CC.0.str(istr='%i')
            '1.0000000000000000*%i'"""
    @overload
    def str(self, istr=...) -> Any:
        """ComplexNumber.str(self, base=10, istr='I', **kwds)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 1275)

        Return a string representation of ``self``.

        INPUT:

        - ``base`` -- (default: 10) base for output

        - ``istr`` -- (default: ``I``) string representation of the complex unit

        - ``**kwds`` -- other arguments to pass to the ``str()``
          method of the real numbers in the real and imaginary parts

        EXAMPLES::

            sage: # needs sage.symbolic
            sage: a = CC(pi + I*e); a
            3.14159265358979 + 2.71828182845905*I
            sage: a.str(truncate=True)
            '3.14159265358979 + 2.71828182845905*I'
            sage: a.str()
            '3.1415926535897931 + 2.7182818284590451*I'
            sage: a.str(base=2)
            '11.001001000011111101101010100010001000010110100011000 + 10.101101111110000101010001011000101000101011101101001*I'
            sage: CC(0.5 + 0.625*I).str(base=2)
            '0.10000000000000000000000000000000000000000000000000000 + 0.10100000000000000000000000000000000000000000000000000*I'
            sage: a.str(base=16)
            '3.243f6a8885a30 + 2.b7e151628aed2*I'
            sage: a.str(base=36)
            '3.53i5ab8p5fc + 2.puw5nggjf8f*I'

            sage: CC(0)
            0.000000000000000
            sage: CC.0.str(istr='%i')
            '1.0000000000000000*%i'"""
    @overload
    def tan(self) -> Any:
        """ComplexNumber.tan(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 2462)

        Return the tangent of ``self``.

        EXAMPLES::

            sage: (1+CC(I)).tan()
            0.271752585319512 + 1.08392332733869*I"""
    @overload
    def tan(self) -> Any:
        """ComplexNumber.tan(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 2462)

        Return the tangent of ``self``.

        EXAMPLES::

            sage: (1+CC(I)).tan()
            0.271752585319512 + 1.08392332733869*I"""
    @overload
    def tanh(self) -> Any:
        """ComplexNumber.tanh(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 2501)

        Return the hyperbolic tangent of ``self``.

        EXAMPLES::

            sage: (1+CC(I)).tanh()
            1.08392332733869 + 0.271752585319512*I"""
    @overload
    def tanh(self) -> Any:
        """ComplexNumber.tanh(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 2501)

        Return the hyperbolic tangent of ``self``.

        EXAMPLES::

            sage: (1+CC(I)).tanh()
            1.08392332733869 + 0.271752585319512*I"""
    @overload
    def zeta(self) -> Any:
        """ComplexNumber.zeta(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 3233)

        Return the Riemann zeta function evaluated at this complex number.

        EXAMPLES::

            sage: i = ComplexField(30).gen()
            sage: z = 1 + i
            sage: z.zeta()                                                              # needs sage.libs.pari
            0.58215806 - 0.92684856*I
            sage: zeta(z)                                                               # needs sage.libs.pari
            0.58215806 - 0.92684856*I

            sage: CC(1).zeta()
            Infinity"""
    @overload
    def zeta(self) -> Any:
        """ComplexNumber.zeta(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 3233)

        Return the Riemann zeta function evaluated at this complex number.

        EXAMPLES::

            sage: i = ComplexField(30).gen()
            sage: z = 1 + i
            sage: z.zeta()                                                              # needs sage.libs.pari
            0.58215806 - 0.92684856*I
            sage: zeta(z)                                                               # needs sage.libs.pari
            0.58215806 - 0.92684856*I

            sage: CC(1).zeta()
            Infinity"""
    @overload
    def zeta(self, z) -> Any:
        """ComplexNumber.zeta(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 3233)

        Return the Riemann zeta function evaluated at this complex number.

        EXAMPLES::

            sage: i = ComplexField(30).gen()
            sage: z = 1 + i
            sage: z.zeta()                                                              # needs sage.libs.pari
            0.58215806 - 0.92684856*I
            sage: zeta(z)                                                               # needs sage.libs.pari
            0.58215806 - 0.92684856*I

            sage: CC(1).zeta()
            Infinity"""
    @overload
    def zeta(self) -> Any:
        """ComplexNumber.zeta(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 3233)

        Return the Riemann zeta function evaluated at this complex number.

        EXAMPLES::

            sage: i = ComplexField(30).gen()
            sage: z = 1 + i
            sage: z.zeta()                                                              # needs sage.libs.pari
            0.58215806 - 0.92684856*I
            sage: zeta(z)                                                               # needs sage.libs.pari
            0.58215806 - 0.92684856*I

            sage: CC(1).zeta()
            Infinity"""
    @overload
    def __abs__(self) -> Any:
        """ComplexNumber.__abs__(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 1863)

        Method for computing the absolute value or modulus of ``self``.

        .. MATH::

            `|a + bi| = sqrt(a^2 + b^2)`

        EXAMPLES:

        Note that the absolute value of a complex number with imaginary
        component equal to zero is the absolute value of the real component.

        ::

            sage: a = ComplexNumber(2,1)
            sage: abs(a)
            2.23606797749979
            sage: a.__abs__()
            2.23606797749979
            sage: float(sqrt(2^2 + 1^1))                                                # needs sage.symbolic
            2.23606797749979

        ::

            sage: b = ComplexNumber(42,0)
            sage: abs(b)
            42.0000000000000
            sage: b.__abs__()
            42.0000000000000
            sage: b
            42.0000000000000"""
    @overload
    def __abs__(self) -> Any:
        """ComplexNumber.__abs__(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 1863)

        Method for computing the absolute value or modulus of ``self``.

        .. MATH::

            `|a + bi| = sqrt(a^2 + b^2)`

        EXAMPLES:

        Note that the absolute value of a complex number with imaginary
        component equal to zero is the absolute value of the real component.

        ::

            sage: a = ComplexNumber(2,1)
            sage: abs(a)
            2.23606797749979
            sage: a.__abs__()
            2.23606797749979
            sage: float(sqrt(2^2 + 1^1))                                                # needs sage.symbolic
            2.23606797749979

        ::

            sage: b = ComplexNumber(42,0)
            sage: abs(b)
            42.0000000000000
            sage: b.__abs__()
            42.0000000000000
            sage: b
            42.0000000000000"""
    @overload
    def __abs__(self) -> Any:
        """ComplexNumber.__abs__(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 1863)

        Method for computing the absolute value or modulus of ``self``.

        .. MATH::

            `|a + bi| = sqrt(a^2 + b^2)`

        EXAMPLES:

        Note that the absolute value of a complex number with imaginary
        component equal to zero is the absolute value of the real component.

        ::

            sage: a = ComplexNumber(2,1)
            sage: abs(a)
            2.23606797749979
            sage: a.__abs__()
            2.23606797749979
            sage: float(sqrt(2^2 + 1^1))                                                # needs sage.symbolic
            2.23606797749979

        ::

            sage: b = ComplexNumber(42,0)
            sage: abs(b)
            42.0000000000000
            sage: b.__abs__()
            42.0000000000000
            sage: b
            42.0000000000000"""
    def __bool__(self) -> bool:
        """True if self else False"""
    @overload
    def __complex__(self) -> Any:
        """ComplexNumber.__complex__(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 1981)

        Method for converting ``self`` to type ``complex``.

        Called by the ``complex`` function.

        EXAMPLES::

            sage: a = ComplexNumber(2,1)
            sage: complex(a)
            (2+1j)
            sage: type(complex(a))
            <... 'complex'>
            sage: a.__complex__()
            (2+1j)"""
    @overload
    def __complex__(self) -> Any:
        """ComplexNumber.__complex__(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 1981)

        Method for converting ``self`` to type ``complex``.

        Called by the ``complex`` function.

        EXAMPLES::

            sage: a = ComplexNumber(2,1)
            sage: complex(a)
            (2+1j)
            sage: type(complex(a))
            <... 'complex'>
            sage: a.__complex__()
            (2+1j)"""
    @overload
    def __float__(self) -> Any:
        """ComplexNumber.__float__(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 1952)

        Method for converting ``self`` to type ``float``.

        Called by the ``float`` function.  This conversion will throw an error
        if the number has a nonzero imaginary part.

        EXAMPLES::

            sage: a = ComplexNumber(1, 0)
            sage: float(a)
            1.0
            sage: a = ComplexNumber(2,1)
            sage: float(a)
            Traceback (most recent call last):
            ...
            TypeError: unable to convert 2.00000000000000 + 1.00000000000000*I to float; use abs() or real_part() as desired
            sage: a.__float__()
            Traceback (most recent call last):
            ...
            TypeError: unable to convert 2.00000000000000 + 1.00000000000000*I to float; use abs() or real_part() as desired
            sage: float(abs(ComplexNumber(1,1)))
            1.4142135623730951"""
    @overload
    def __float__(self) -> Any:
        """ComplexNumber.__float__(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 1952)

        Method for converting ``self`` to type ``float``.

        Called by the ``float`` function.  This conversion will throw an error
        if the number has a nonzero imaginary part.

        EXAMPLES::

            sage: a = ComplexNumber(1, 0)
            sage: float(a)
            1.0
            sage: a = ComplexNumber(2,1)
            sage: float(a)
            Traceback (most recent call last):
            ...
            TypeError: unable to convert 2.00000000000000 + 1.00000000000000*I to float; use abs() or real_part() as desired
            sage: a.__float__()
            Traceback (most recent call last):
            ...
            TypeError: unable to convert 2.00000000000000 + 1.00000000000000*I to float; use abs() or real_part() as desired
            sage: float(abs(ComplexNumber(1,1)))
            1.4142135623730951"""
    def __format__(self, format_spec) -> Any:
        """ComplexNumber.__format__(self, format_spec)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 1328)

        Return a formatted string representation of this complex number.

        INPUT:

        - ``format_spec`` -- string; a floating point format specifier as
          defined by :python:`the format specification mini-language
          <library/string.html#formatspec>` in Python

        EXAMPLES::

            sage: format(CC(32/3, 0), ' .4f')
            ' 10.6667 + 0.0000*I'
            sage: format(CC(-2/3, -2/3), '.4e')
            '-6.6667e-1 - 6.6667e-1*I'

        If the representation type character is absent, the output matches the
        string representation of the complex number. This has the effect that
        real and imaginary part are only shown if they are not zero::

            sage: format(CC(0, 2/3), '.4')
            '0.6667*I'
            sage: format(CC(2, 0), '.4')
            '2.000'
            sage: format(ComplexField(240)(0, 1/7), '.60')
            '0.142857142857142857142857142857142857142857142857142857142857*I'
            sage: format(ComplexField(240)(0, 1/7), '.60f')
            '0.000000000000000000000000000000000000000000000000000000000000
            + 0.142857142857142857142857142857142857142857142857142857142857*I'

        Note that the general format does not exactly match the behaviour of
        ``float``. Some Python versions do not implement the full spec
        (see :issue:`30689`)::

            sage: format(CC(3, 0), '.4g')
            '3.000 + 0e-15*I'
            sage: try:
            ....:     assert format(CC(3, 0), '#.4g') == '3.000 + 0.e-15*I'
            ....:     assert format(CC(0, 0), '+#.4') == '+0.E-15'
            ....: except ValueError:
            ....:     pass"""
    def __getitem__(self, i) -> Any:
        """ComplexNumber.__getitem__(self, i)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 1200)

        Return either the real or imaginary component of ``self`` depending on
        the choice of ``i``: real (``i=0``), imaginary (``i=1``).

        INPUT:

        - ``i`` -- 0 or 1
            - ``0`` -- will return the real component of ``self``
            - ``1`` -- will return the imaginary component of ``self``

        EXAMPLES::

            sage: a = ComplexNumber(2,1)
            sage: a.__getitem__(0)
            2.00000000000000
            sage: a.__getitem__(1)
            1.00000000000000

        ::

            sage: b = CC(42,0)
            sage: b
            42.0000000000000
            sage: b.__getitem__(1)
            0.000000000000000"""
    def __hash__(self) -> Any:
        """ComplexNumber.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 1184)

        Return the hash of ``self``, which coincides with the python complex
        and float (and often int) types.

        This has the drawback that two very close high precision numbers
        will have the same hash, but allows them to play nicely with other
        real types.

        EXAMPLES::

            sage: hash(CC(1.2, 33)) == hash(complex(1.2, 33))
            True"""
    @overload
    def __int__(self) -> Any:
        """ComplexNumber.__int__(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 1930)

        Method for converting ``self`` to type ``int``.

        Called by the ``int`` function. Note that calling this method returns
        an error since, in general, complex numbers cannot be coerced into
        integers.

        EXAMPLES::

            sage: a = ComplexNumber(2,1)
            sage: int(a)
            Traceback (most recent call last):
            ...
            TypeError: can...t convert complex to int; use int(abs(z))
            sage: a.__int__()
            Traceback (most recent call last):
            ...
            TypeError: can...t convert complex to int; use int(abs(z))"""
    @overload
    def __int__(self) -> Any:
        """ComplexNumber.__int__(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 1930)

        Method for converting ``self`` to type ``int``.

        Called by the ``int`` function. Note that calling this method returns
        an error since, in general, complex numbers cannot be coerced into
        integers.

        EXAMPLES::

            sage: a = ComplexNumber(2,1)
            sage: int(a)
            Traceback (most recent call last):
            ...
            TypeError: can...t convert complex to int; use int(abs(z))
            sage: a.__int__()
            Traceback (most recent call last):
            ...
            TypeError: can...t convert complex to int; use int(abs(z))"""
    def __invert__(self) -> Any:
        """ComplexNumber.__invert__(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 1898)

        Return the multiplicative inverse.

        EXAMPLES::

            sage: I = CC.0
            sage: a = ~(5+I)
            sage: a * (5+I)
            1.00000000000000"""
    @overload
    def __mpc__(self) -> Any:
        """ComplexNumber.__mpc__(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 1440)

        Convert Sage ``ComplexNumber`` to gmpy2 ``mpc``.

        EXAMPLES::

            sage: c = ComplexNumber(2,1)
            sage: c.__mpc__()
            mpc('2.0+1.0j')
            sage: from gmpy2 import mpc
            sage: mpc(c)
            mpc('2.0+1.0j')
            sage: CF = ComplexField(134)
            sage: mpc(CF.pi()).precision
            (134, 134)
            sage: CF = ComplexField(45)
            sage: mpc(CF.zeta(5)).precision
            (45, 45)
            sage: CF = ComplexField(255)
            sage: x = CF(5, 8)
            sage: y = mpc(x)
            sage: y.precision
            (255, 255)
            sage: CF(y) == x
            True
            sage: x = mpc('1.324+4e50j', precision=(70,70))
            sage: CF = ComplexField(70)
            sage: y = CF(x)
            sage: x == mpc(y)
            True"""
    @overload
    def __mpc__(self) -> Any:
        """ComplexNumber.__mpc__(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 1440)

        Convert Sage ``ComplexNumber`` to gmpy2 ``mpc``.

        EXAMPLES::

            sage: c = ComplexNumber(2,1)
            sage: c.__mpc__()
            mpc('2.0+1.0j')
            sage: from gmpy2 import mpc
            sage: mpc(c)
            mpc('2.0+1.0j')
            sage: CF = ComplexField(134)
            sage: mpc(CF.pi()).precision
            (134, 134)
            sage: CF = ComplexField(45)
            sage: mpc(CF.zeta(5)).precision
            (45, 45)
            sage: CF = ComplexField(255)
            sage: x = CF(5, 8)
            sage: y = mpc(x)
            sage: y.precision
            (255, 255)
            sage: CF(y) == x
            True
            sage: x = mpc('1.324+4e50j', precision=(70,70))
            sage: CF = ComplexField(70)
            sage: y = CF(x)
            sage: x == mpc(y)
            True"""
    @overload
    def __neg__(self) -> Any:
        """ComplexNumber.__neg__(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 1827)

        Method for computing the negative of ``self``.

        .. MATH::

            -(a + bi) = -a - bi

        EXAMPLES::

            sage: a = ComplexNumber(2,1)
            sage: -a
            -2.00000000000000 - 1.00000000000000*I
            sage: a.__neg__()
            -2.00000000000000 - 1.00000000000000*I"""
    @overload
    def __neg__(self) -> Any:
        """ComplexNumber.__neg__(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 1827)

        Method for computing the negative of ``self``.

        .. MATH::

            -(a + bi) = -a - bi

        EXAMPLES::

            sage: a = ComplexNumber(2,1)
            sage: -a
            -2.00000000000000 - 1.00000000000000*I
            sage: a.__neg__()
            -2.00000000000000 - 1.00000000000000*I"""
    @overload
    def __pari__(self) -> Any:
        """ComplexNumber.__pari__(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 1406)

        Coerces ``self`` into a PARI ``t_COMPLEX`` object,
        or a ``t_REAL`` if ``self`` is real.

        EXAMPLES:

        Coerce the object using the ``pari`` function::

            sage: # needs sage.libs.pari
            sage: a = ComplexNumber(2,1)
            sage: pari(a)
            2.00000000000000 + 1.00000000000000*I
            sage: pari(a).type()
            't_COMPLEX'
            sage: type(pari(a))
            <class 'cypari2.gen.Gen'>
            sage: a.__pari__()
            2.00000000000000 + 1.00000000000000*I
            sage: type(a.__pari__())
            <class 'cypari2.gen.Gen'>
            sage: a = CC(pi)                                                            # needs sage.symbolic
            sage: pari(a)                                                               # needs sage.symbolic
            3.14159265358979
            sage: pari(a).type()                                                        # needs sage.symbolic
            't_REAL'
            sage: a = CC(-2).sqrt()
            sage: pari(a)
            1.41421356237310*I"""
    @overload
    def __pari__(self) -> Any:
        """ComplexNumber.__pari__(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 1406)

        Coerces ``self`` into a PARI ``t_COMPLEX`` object,
        or a ``t_REAL`` if ``self`` is real.

        EXAMPLES:

        Coerce the object using the ``pari`` function::

            sage: # needs sage.libs.pari
            sage: a = ComplexNumber(2,1)
            sage: pari(a)
            2.00000000000000 + 1.00000000000000*I
            sage: pari(a).type()
            't_COMPLEX'
            sage: type(pari(a))
            <class 'cypari2.gen.Gen'>
            sage: a.__pari__()
            2.00000000000000 + 1.00000000000000*I
            sage: type(a.__pari__())
            <class 'cypari2.gen.Gen'>
            sage: a = CC(pi)                                                            # needs sage.symbolic
            sage: pari(a)                                                               # needs sage.symbolic
            3.14159265358979
            sage: pari(a).type()                                                        # needs sage.symbolic
            't_REAL'
            sage: a = CC(-2).sqrt()
            sage: pari(a)
            1.41421356237310*I"""
    @overload
    def __pari__(self) -> Any:
        """ComplexNumber.__pari__(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 1406)

        Coerces ``self`` into a PARI ``t_COMPLEX`` object,
        or a ``t_REAL`` if ``self`` is real.

        EXAMPLES:

        Coerce the object using the ``pari`` function::

            sage: # needs sage.libs.pari
            sage: a = ComplexNumber(2,1)
            sage: pari(a)
            2.00000000000000 + 1.00000000000000*I
            sage: pari(a).type()
            't_COMPLEX'
            sage: type(pari(a))
            <class 'cypari2.gen.Gen'>
            sage: a.__pari__()
            2.00000000000000 + 1.00000000000000*I
            sage: type(a.__pari__())
            <class 'cypari2.gen.Gen'>
            sage: a = CC(pi)                                                            # needs sage.symbolic
            sage: pari(a)                                                               # needs sage.symbolic
            3.14159265358979
            sage: pari(a).type()                                                        # needs sage.symbolic
            't_REAL'
            sage: a = CC(-2).sqrt()
            sage: pari(a)
            1.41421356237310*I"""
    @overload
    def __pos__(self) -> Any:
        '''ComplexNumber.__pos__(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 1849)

        Method for computing the "positive" of ``self``.

        EXAMPLES::

            sage: a = ComplexNumber(2,1)
            sage: +a
            2.00000000000000 + 1.00000000000000*I
            sage: a.__pos__()
            2.00000000000000 + 1.00000000000000*I'''
    @overload
    def __pos__(self) -> Any:
        '''ComplexNumber.__pos__(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 1849)

        Method for computing the "positive" of ``self``.

        EXAMPLES::

            sage: a = ComplexNumber(2,1)
            sage: +a
            2.00000000000000 + 1.00000000000000*I
            sage: a.__pos__()
            2.00000000000000 + 1.00000000000000*I'''
    def __pow__(self, right, modulus) -> Any:
        """ComplexNumber.__pow__(self, right, modulus)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 1684)

        Raise ``self`` to the ``right`` exponent.

        This takes `a^b` and computes `\\exp(b \\log(a))`.

        EXAMPLES::

            sage: C.<i> = ComplexField(20)
            sage: a = i^2; a
            -1.0000
            sage: a.parent()
            Complex Field with 20 bits of precision
            sage: a = (1+i)^i; a
            0.42883 + 0.15487*I
            sage: (1+i)^(1+i)
            0.27396 + 0.58370*I
            sage: a.parent()
            Complex Field with 20 bits of precision
            sage: i^i
            0.20788
            sage: (2+i)^(0.5)
            1.4553 + 0.34356*I

        TESTS:

        Check that :issue:`11323` is fixed::

            sage: float(5)^(0.5 + 14.1347251*I)
            -1.62414637645790 - 1.53692828324508*I"""
    def __reduce__(self) -> Any:
        """ComplexNumber.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 1233)

        Pickling support.

        EXAMPLES::

            sage: a = CC(1 + I)
            sage: loads(dumps(a)) == a
            True"""
    def __rpow__(self, other):
        """Return pow(value, self, mod)."""

class RRtoCC(sage.categories.map.Map):
    """RRtoCC(RR, CC)"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, RR, CC) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/complex_mpfr.pyx (starting at line 3369)

                EXAMPLES::

                    sage: from sage.rings.complex_mpfr import RRtoCC
                    sage: RRtoCC(RR, CC)
                    Natural map:
                      From: Real Field with 53 bits of precision
                      To:   Complex Field with 53 bits of precision
        """

class ComplexField_class_with_category(ComplexField_class, JoinCategory.parent_class):
    ...
    # TODO: check mro of CC to decides exactly which classes to inherit from


CC = ComplexField_class_with_category(53)