r"""
Double precision floating point real numbers

EXAMPLES:

We create the real double vector space of dimension `3`::

    sage: V = RDF^3; V                                                                  # needs sage.modules
    Vector space of dimension 3 over Real Double Field

Notice that this space is unique::

    sage: V is RDF^3                                                                    # needs sage.modules
    True
    sage: V is FreeModule(RDF, 3)                                                       # needs sage.modules
    True
    sage: V is VectorSpace(RDF, 3)                                                      # needs sage.modules
    True

Also, you can instantly create a space of large dimension::

    sage: V = RDF^10000                                                                 # needs sage.modules

TESTS:

Test NumPy conversions::

    sage: RDF(1).__array_interface__
    {'typestr': '=f8'}
    sage: import numpy                                                                  # needs numpy
    sage: numpy.array([RDF.pi()]).dtype                                                 # needs numpy
    dtype('float64')
"""
import _cython_3_2_1
import sage as sage
import sage.categories.morphism
import sage.rings.abc
import sage.structure.element
from sage.categories.category import ZZ as ZZ
from sage.rings.real_double_element_gsl import RealDoubleElement_gsl as RealDoubleElement_gsl
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from sage.structure.richcmp import revop as revop, rich_to_bool as rich_to_bool, rich_to_bool_sgn as rich_to_bool_sgn, richcmp as richcmp, richcmp_not_equal as richcmp_not_equal
from typing import Any, ClassVar, TypeGuard, overload

def RealDoubleField() -> RealDoubleField_class:
    """
    Return the unique instance of the
    :class:`real double field<RealDoubleField_class>`.

    EXAMPLES::

        sage: RealDoubleField() is RealDoubleField()
        True
    """
    ...

def is_RealDoubleElement(x) -> TypeGuard[RealDoubleElement]:
    """
    Check if ``x`` is an element of the real double field.

    EXAMPLES::

        sage: from sage.rings.real_double import is_RealDoubleElement
        sage: is_RealDoubleElement(RDF(3))
        doctest:warning...
        DeprecationWarning: The function is_RealDoubleElement is deprecated;
        use 'isinstance(..., RealDoubleElement)' instead.
        See https://github.com/sagemath/sage/issues/38128 for details.
        True
        sage: is_RealDoubleElement(RIF(3))                                              # needs sage.rings.real_interval_field
        False
    """
    ...

from sage.libs.pari.convert_sage_real_double import new_gen_from_real_double_element as new_gen_from_real_double_element

class RealDoubleElement(sage.structure.element.FieldElement):
    """RealDoubleElement(x)

    File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 675)

    An approximation to a real number using double precision floating
    point numbers. Answers derived from calculations with such
    approximations may differ from what they would be if those
    calculations were performed with true real numbers. This is due to
    the rounding errors inherent to finite precision calculations."""
    __array_interface__: ClassVar[dict] = ...
    def __init__(self, x):
        """File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 697)

                Create a new ``RealDoubleElement`` with value ``x``.

                EXAMPLES::

                    sage: RDF(10^100)
                    1e+100

                TESTS::

                    sage: from gmpy2 import *
                    sage: RDF(mpz(42))
                    42.0
                    sage: RDF(mpq(3/4))
                    0.75
                    sage: RDF(mpq('4.1'))
                    4.1
        """
    @overload
    def NaN(self) -> Any:
        """RealDoubleElement.NaN(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1786)

        Return Not-a-Number ``NaN``.

        EXAMPLES::

            sage: RDF.NaN()
            NaN"""
    @overload
    def NaN(self) -> Any:
        """RealDoubleElement.NaN(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1786)

        Return Not-a-Number ``NaN``.

        EXAMPLES::

            sage: RDF.NaN()
            NaN"""
    @overload
    def abs(self) -> RealDoubleElement:
        """RealDoubleElement.abs(self) -> RealDoubleElement

        File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1411)

        Return the absolute value of ``self``.

        EXAMPLES::

            sage: RDF(1e10).abs()
            10000000000.0
            sage: RDF(-1e10).abs()
            10000000000.0"""
    @overload
    def abs(self) -> Any:
        """RealDoubleElement.abs(self) -> RealDoubleElement

        File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1411)

        Return the absolute value of ``self``.

        EXAMPLES::

            sage: RDF(1e10).abs()
            10000000000.0
            sage: RDF(-1e10).abs()
            10000000000.0"""
    @overload
    def abs(self) -> Any:
        """RealDoubleElement.abs(self) -> RealDoubleElement

        File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1411)

        Return the absolute value of ``self``.

        EXAMPLES::

            sage: RDF(1e10).abs()
            10000000000.0
            sage: RDF(-1e10).abs()
            10000000000.0"""
    @overload
    def agm(self, other) -> Any:
        """RealDoubleElement.agm(self, other)

        File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1901)

        Return the arithmetic-geometric mean of ``self`` and ``other``. The
        arithmetic-geometric mean is the common limit of the sequences
        `u_n` and `v_n`, where `u_0` is ``self``,
        `v_0` is other, `u_{n+1}` is the arithmetic mean
        of `u_n` and `v_n`, and `v_{n+1}` is the
        geometric mean of `u_n` and `v_n`. If any operand is negative, the
        return value is ``NaN``.

        EXAMPLES::

            sage: a = RDF(1.5)
            sage: b = RDF(2.3)
            sage: a.agm(b)
            1.8786484558146697

        The arithmetic-geometric mean always lies between the geometric and
        arithmetic mean::

            sage: sqrt(a*b) < a.agm(b) < (a+b)/2
            True"""
    @overload
    def agm(self, b) -> Any:
        """RealDoubleElement.agm(self, other)

        File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1901)

        Return the arithmetic-geometric mean of ``self`` and ``other``. The
        arithmetic-geometric mean is the common limit of the sequences
        `u_n` and `v_n`, where `u_0` is ``self``,
        `v_0` is other, `u_{n+1}` is the arithmetic mean
        of `u_n` and `v_n`, and `v_{n+1}` is the
        geometric mean of `u_n` and `v_n`. If any operand is negative, the
        return value is ``NaN``.

        EXAMPLES::

            sage: a = RDF(1.5)
            sage: b = RDF(2.3)
            sage: a.agm(b)
            1.8786484558146697

        The arithmetic-geometric mean always lies between the geometric and
        arithmetic mean::

            sage: sqrt(a*b) < a.agm(b) < (a+b)/2
            True"""
    @overload
    def agm(self, b) -> Any:
        """RealDoubleElement.agm(self, other)

        File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1901)

        Return the arithmetic-geometric mean of ``self`` and ``other``. The
        arithmetic-geometric mean is the common limit of the sequences
        `u_n` and `v_n`, where `u_0` is ``self``,
        `v_0` is other, `u_{n+1}` is the arithmetic mean
        of `u_n` and `v_n`, and `v_{n+1}` is the
        geometric mean of `u_n` and `v_n`. If any operand is negative, the
        return value is ``NaN``.

        EXAMPLES::

            sage: a = RDF(1.5)
            sage: b = RDF(2.3)
            sage: a.agm(b)
            1.8786484558146697

        The arithmetic-geometric mean always lies between the geometric and
        arithmetic mean::

            sage: sqrt(a*b) < a.agm(b) < (a+b)/2
            True"""
    def algdep(self, *args, **kwargs):
        """RealDoubleElement.algebraic_dependency(self, n)

        File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1936)

        Return a polynomial of degree at most `n` which is
        approximately satisfied by this number.

        .. NOTE::

            The resulting polynomial need not be irreducible, and indeed
            usually won't be if this number is a good approximation to an
            algebraic number of degree less than `n`.

        ALGORITHM:

        Uses the PARI C-library :pari:`algdep` command.

        EXAMPLES::

            sage: r = sqrt(RDF(2)); r
            1.4142135623730951
            sage: r.algebraic_dependency(5)                                             # needs sage.libs.pari
            x^2 - 2"""
    def algebraic_dependency(self, n) -> Any:
        """RealDoubleElement.algebraic_dependency(self, n)

        File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1936)

        Return a polynomial of degree at most `n` which is
        approximately satisfied by this number.

        .. NOTE::

            The resulting polynomial need not be irreducible, and indeed
            usually won't be if this number is a good approximation to an
            algebraic number of degree less than `n`.

        ALGORITHM:

        Uses the PARI C-library :pari:`algdep` command.

        EXAMPLES::

            sage: r = sqrt(RDF(2)); r
            1.4142135623730951
            sage: r.algebraic_dependency(5)                                             # needs sage.libs.pari
            x^2 - 2"""
    @overload
    def as_integer_ratio(self) -> Any:
        """RealDoubleElement.as_integer_ratio(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1273)

        Return a coprime pair of integers ``(a, b)`` such that ``self``
        equals ``a / b`` exactly.

        EXAMPLES::

            sage: RDF(0).as_integer_ratio()
            (0, 1)
            sage: RDF(1/3).as_integer_ratio()
            (6004799503160661, 18014398509481984)
            sage: RDF(37/16).as_integer_ratio()
            (37, 16)
            sage: RDF(3^60).as_integer_ratio()
            (42391158275216203520420085760, 1)"""
    @overload
    def as_integer_ratio(self) -> Any:
        """RealDoubleElement.as_integer_ratio(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1273)

        Return a coprime pair of integers ``(a, b)`` such that ``self``
        equals ``a / b`` exactly.

        EXAMPLES::

            sage: RDF(0).as_integer_ratio()
            (0, 1)
            sage: RDF(1/3).as_integer_ratio()
            (6004799503160661, 18014398509481984)
            sage: RDF(37/16).as_integer_ratio()
            (37, 16)
            sage: RDF(3^60).as_integer_ratio()
            (42391158275216203520420085760, 1)"""
    @overload
    def as_integer_ratio(self) -> Any:
        """RealDoubleElement.as_integer_ratio(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1273)

        Return a coprime pair of integers ``(a, b)`` such that ``self``
        equals ``a / b`` exactly.

        EXAMPLES::

            sage: RDF(0).as_integer_ratio()
            (0, 1)
            sage: RDF(1/3).as_integer_ratio()
            (6004799503160661, 18014398509481984)
            sage: RDF(37/16).as_integer_ratio()
            (37, 16)
            sage: RDF(3^60).as_integer_ratio()
            (42391158275216203520420085760, 1)"""
    @overload
    def as_integer_ratio(self) -> Any:
        """RealDoubleElement.as_integer_ratio(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1273)

        Return a coprime pair of integers ``(a, b)`` such that ``self``
        equals ``a / b`` exactly.

        EXAMPLES::

            sage: RDF(0).as_integer_ratio()
            (0, 1)
            sage: RDF(1/3).as_integer_ratio()
            (6004799503160661, 18014398509481984)
            sage: RDF(37/16).as_integer_ratio()
            (37, 16)
            sage: RDF(3^60).as_integer_ratio()
            (42391158275216203520420085760, 1)"""
    @overload
    def as_integer_ratio(self) -> Any:
        """RealDoubleElement.as_integer_ratio(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1273)

        Return a coprime pair of integers ``(a, b)`` such that ``self``
        equals ``a / b`` exactly.

        EXAMPLES::

            sage: RDF(0).as_integer_ratio()
            (0, 1)
            sage: RDF(1/3).as_integer_ratio()
            (6004799503160661, 18014398509481984)
            sage: RDF(37/16).as_integer_ratio()
            (37, 16)
            sage: RDF(3^60).as_integer_ratio()
            (42391158275216203520420085760, 1)"""
    @overload
    def ceil(self) -> Any:
        """RealDoubleElement.ceil(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1536)

        Return the ceiling of ``self``.

        EXAMPLES::

            sage: RDF(2.99).ceil()
            3
            sage: RDF(2.00).ceil()
            2
            sage: RDF(-5/2).ceil()
            -2"""
    @overload
    def ceil(self) -> Any:
        """RealDoubleElement.ceil(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1536)

        Return the ceiling of ``self``.

        EXAMPLES::

            sage: RDF(2.99).ceil()
            3
            sage: RDF(2.00).ceil()
            2
            sage: RDF(-5/2).ceil()
            -2"""
    @overload
    def ceil(self) -> Any:
        """RealDoubleElement.ceil(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1536)

        Return the ceiling of ``self``.

        EXAMPLES::

            sage: RDF(2.99).ceil()
            3
            sage: RDF(2.00).ceil()
            2
            sage: RDF(-5/2).ceil()
            -2"""
    @overload
    def ceil(self) -> Any:
        """RealDoubleElement.ceil(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1536)

        Return the ceiling of ``self``.

        EXAMPLES::

            sage: RDF(2.99).ceil()
            3
            sage: RDF(2.00).ceil()
            2
            sage: RDF(-5/2).ceil()
            -2"""
    def ceiling(self, *args, **kwargs):
        """RealDoubleElement.ceil(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1536)

        Return the ceiling of ``self``.

        EXAMPLES::

            sage: RDF(2.99).ceil()
            3
            sage: RDF(2.00).ceil()
            2
            sage: RDF(-5/2).ceil()
            -2"""
    @overload
    def conjugate(self) -> Any:
        """RealDoubleElement.conjugate(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1378)

        Return the complex conjugate of this real number, which is
        the real number itself.

        EXAMPLES::

            sage: RDF(4).conjugate()
            4.0"""
    @overload
    def conjugate(self) -> Any:
        """RealDoubleElement.conjugate(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1378)

        Return the complex conjugate of this real number, which is
        the real number itself.

        EXAMPLES::

            sage: RDF(4).conjugate()
            4.0"""
    @overload
    def cube_root(self) -> Any:
        """RealDoubleElement.cube_root(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1887)

        Return the cubic root (defined over the real numbers) of ``self``.

        EXAMPLES::

            sage: r = RDF(125.0); r.cube_root()
            5.000000000000001
            sage: r = RDF(-119.0)
            sage: r.cube_root()^3 - r  # rel tol 1
            -1.4210854715202004e-14"""
    @overload
    def cube_root(self) -> Any:
        """RealDoubleElement.cube_root(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1887)

        Return the cubic root (defined over the real numbers) of ``self``.

        EXAMPLES::

            sage: r = RDF(125.0); r.cube_root()
            5.000000000000001
            sage: r = RDF(-119.0)
            sage: r.cube_root()^3 - r  # rel tol 1
            -1.4210854715202004e-14"""
    @overload
    def cube_root(self) -> Any:
        """RealDoubleElement.cube_root(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1887)

        Return the cubic root (defined over the real numbers) of ``self``.

        EXAMPLES::

            sage: r = RDF(125.0); r.cube_root()
            5.000000000000001
            sage: r = RDF(-119.0)
            sage: r.cube_root()^3 - r  # rel tol 1
            -1.4210854715202004e-14"""
    @overload
    def floor(self) -> Any:
        """RealDoubleElement.floor(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1521)

        Return the floor of ``self``.

        EXAMPLES::

            sage: RDF(2.99).floor()
            2
            sage: RDF(2.00).floor()
            2
            sage: RDF(-5/2).floor()
            -3"""
    @overload
    def floor(self) -> Any:
        """RealDoubleElement.floor(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1521)

        Return the floor of ``self``.

        EXAMPLES::

            sage: RDF(2.99).floor()
            2
            sage: RDF(2.00).floor()
            2
            sage: RDF(-5/2).floor()
            -3"""
    @overload
    def floor(self) -> Any:
        """RealDoubleElement.floor(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1521)

        Return the floor of ``self``.

        EXAMPLES::

            sage: RDF(2.99).floor()
            2
            sage: RDF(2.00).floor()
            2
            sage: RDF(-5/2).floor()
            -3"""
    @overload
    def floor(self) -> Any:
        """RealDoubleElement.floor(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1521)

        Return the floor of ``self``.

        EXAMPLES::

            sage: RDF(2.99).floor()
            2
            sage: RDF(2.00).floor()
            2
            sage: RDF(-5/2).floor()
            -3"""
    @overload
    def frac(self) -> Any:
        """RealDoubleElement.frac(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1568)

        Return a real number in `(-1, 1)`. It satisfies the relation:
        ``x = x.trunc() + x.frac()``

        EXAMPLES::

            sage: RDF(2.99).frac()
            0.9900000000000002
            sage: RDF(2.50).frac()
            0.5
            sage: RDF(-2.79).frac()
            -0.79"""
    @overload
    def frac(self) -> Any:
        """RealDoubleElement.frac(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1568)

        Return a real number in `(-1, 1)`. It satisfies the relation:
        ``x = x.trunc() + x.frac()``

        EXAMPLES::

            sage: RDF(2.99).frac()
            0.9900000000000002
            sage: RDF(2.50).frac()
            0.5
            sage: RDF(-2.79).frac()
            -0.79"""
    @overload
    def frac(self) -> Any:
        """RealDoubleElement.frac(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1568)

        Return a real number in `(-1, 1)`. It satisfies the relation:
        ``x = x.trunc() + x.frac()``

        EXAMPLES::

            sage: RDF(2.99).frac()
            0.9900000000000002
            sage: RDF(2.50).frac()
            0.5
            sage: RDF(-2.79).frac()
            -0.79"""
    @overload
    def frac(self) -> Any:
        """RealDoubleElement.frac(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1568)

        Return a real number in `(-1, 1)`. It satisfies the relation:
        ``x = x.trunc() + x.frac()``

        EXAMPLES::

            sage: RDF(2.99).frac()
            0.9900000000000002
            sage: RDF(2.50).frac()
            0.5
            sage: RDF(-2.79).frac()
            -0.79"""
    @overload
    def frac(self) -> Any:
        """RealDoubleElement.frac(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1568)

        Return a real number in `(-1, 1)`. It satisfies the relation:
        ``x = x.trunc() + x.frac()``

        EXAMPLES::

            sage: RDF(2.99).frac()
            0.9900000000000002
            sage: RDF(2.50).frac()
            0.5
            sage: RDF(-2.79).frac()
            -0.79"""
    @overload
    def imag(self) -> Any:
        """RealDoubleElement.imag(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 878)

        Return the imaginary part of this number, which is zero.

        EXAMPLES::

            sage: a = RDF(3)
            sage: a.imag()
            0.0"""
    @overload
    def imag(self) -> Any:
        """RealDoubleElement.imag(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 878)

        Return the imaginary part of this number, which is zero.

        EXAMPLES::

            sage: a = RDF(3)
            sage: a.imag()
            0.0"""
    @overload
    def integer_part(self) -> Any:
        """RealDoubleElement.integer_part(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1208)

        If in decimal this number is written ``n.defg``, returns ``n``.

        EXAMPLES::

            sage: r = RDF('-1.6')
            sage: a = r.integer_part(); a
            -1
            sage: type(a)
            <class 'sage.rings.integer.Integer'>
            sage: r = RDF(0.0/0.0)
            sage: a = r.integer_part()
            Traceback (most recent call last):
            ...
            TypeError: Attempt to get integer part of NaN"""
    @overload
    def integer_part(self) -> Any:
        """RealDoubleElement.integer_part(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1208)

        If in decimal this number is written ``n.defg``, returns ``n``.

        EXAMPLES::

            sage: r = RDF('-1.6')
            sage: a = r.integer_part(); a
            -1
            sage: type(a)
            <class 'sage.rings.integer.Integer'>
            sage: r = RDF(0.0/0.0)
            sage: a = r.integer_part()
            Traceback (most recent call last):
            ...
            TypeError: Attempt to get integer part of NaN"""
    @overload
    def integer_part(self) -> Any:
        """RealDoubleElement.integer_part(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1208)

        If in decimal this number is written ``n.defg``, returns ``n``.

        EXAMPLES::

            sage: r = RDF('-1.6')
            sage: a = r.integer_part(); a
            -1
            sage: type(a)
            <class 'sage.rings.integer.Integer'>
            sage: r = RDF(0.0/0.0)
            sage: a = r.integer_part()
            Traceback (most recent call last):
            ...
            TypeError: Attempt to get integer part of NaN"""
    @overload
    def is_NaN(self) -> Any:
        """RealDoubleElement.is_NaN(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1680)

        Check if ``self`` is ``NaN``.

        EXAMPLES::

            sage: RDF(1).is_NaN()
            False
            sage: a = RDF(0)/RDF(0)
            sage: a.is_NaN()
            True"""
    @overload
    def is_NaN(self) -> Any:
        """RealDoubleElement.is_NaN(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1680)

        Check if ``self`` is ``NaN``.

        EXAMPLES::

            sage: RDF(1).is_NaN()
            False
            sage: a = RDF(0)/RDF(0)
            sage: a.is_NaN()
            True"""
    @overload
    def is_NaN(self) -> Any:
        """RealDoubleElement.is_NaN(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1680)

        Check if ``self`` is ``NaN``.

        EXAMPLES::

            sage: RDF(1).is_NaN()
            False
            sage: a = RDF(0)/RDF(0)
            sage: a.is_NaN()
            True"""
    def is_infinity(self) -> Any:
        """RealDoubleElement.is_infinity(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1728)

        Check if ``self`` is `\\infty`.

        EXAMPLES::

            sage: a = RDF(2); b = RDF(0)
            sage: (a/b).is_infinity()
            True
            sage: (b/a).is_infinity()
            False"""
    @overload
    def is_integer(self) -> Any:
        """RealDoubleElement.is_integer(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1874)

        Return ``True`` if this number is a integer.

        EXAMPLES::

            sage: RDF(3.5).is_integer()
            False
            sage: RDF(3).is_integer()
            True"""
    @overload
    def is_integer(self) -> Any:
        """RealDoubleElement.is_integer(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1874)

        Return ``True`` if this number is a integer.

        EXAMPLES::

            sage: RDF(3.5).is_integer()
            False
            sage: RDF(3).is_integer()
            True"""
    @overload
    def is_integer(self) -> Any:
        """RealDoubleElement.is_integer(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1874)

        Return ``True`` if this number is a integer.

        EXAMPLES::

            sage: RDF(3.5).is_integer()
            False
            sage: RDF(3).is_integer()
            True"""
    def is_negative_infinity(self) -> Any:
        """RealDoubleElement.is_negative_infinity(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1711)

        Check if ``self`` is `-\\infty`.

        EXAMPLES::

            sage: a = RDF(2)/RDF(0)
            sage: a.is_negative_infinity()
            False
            sage: a = RDF(-3)/RDF(0)
            sage: a.is_negative_infinity()
            True"""
    def is_positive_infinity(self) -> Any:
        """RealDoubleElement.is_positive_infinity(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1694)

        Check if ``self`` is `+\\infty`.

        EXAMPLES::

            sage: a = RDF(1)/RDF(0)
            sage: a.is_positive_infinity()
            True
            sage: a = RDF(-1)/RDF(0)
            sage: a.is_positive_infinity()
            False"""
    @overload
    def is_square(self) -> Any:
        """RealDoubleElement.is_square(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1857)

        Return whether or not this number is a square in this field. For
        the real numbers, this is ``True`` if and only if ``self`` is
        nonnegative.

        EXAMPLES::

            sage: RDF(3.5).is_square()
            True
            sage: RDF(0).is_square()
            True
            sage: RDF(-4).is_square()
            False"""
    @overload
    def is_square(self) -> Any:
        """RealDoubleElement.is_square(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1857)

        Return whether or not this number is a square in this field. For
        the real numbers, this is ``True`` if and only if ``self`` is
        nonnegative.

        EXAMPLES::

            sage: RDF(3.5).is_square()
            True
            sage: RDF(0).is_square()
            True
            sage: RDF(-4).is_square()
            False"""
    @overload
    def is_square(self) -> Any:
        """RealDoubleElement.is_square(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1857)

        Return whether or not this number is a square in this field. For
        the real numbers, this is ``True`` if and only if ``self`` is
        nonnegative.

        EXAMPLES::

            sage: RDF(3.5).is_square()
            True
            sage: RDF(0).is_square()
            True
            sage: RDF(-4).is_square()
            False"""
    @overload
    def is_square(self) -> Any:
        """RealDoubleElement.is_square(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1857)

        Return whether or not this number is a square in this field. For
        the real numbers, this is ``True`` if and only if ``self`` is
        nonnegative.

        EXAMPLES::

            sage: RDF(3.5).is_square()
            True
            sage: RDF(0).is_square()
            True
            sage: RDF(-4).is_square()
            False"""
    def multiplicative_order(self) -> Any:
        """RealDoubleElement.multiplicative_order(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1455)

        Return `n` such that ``self^n == 1``.

        Only `\\pm 1` have finite multiplicative order.

        EXAMPLES::

            sage: RDF(1).multiplicative_order()
            1
            sage: RDF(-1).multiplicative_order()
            2
            sage: RDF(3).multiplicative_order()
            +Infinity"""
    def nan(self, *args, **kwargs):
        """RealDoubleElement.NaN(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1786)

        Return Not-a-Number ``NaN``.

        EXAMPLES::

            sage: RDF.NaN()
            NaN"""
    @overload
    def prec(self) -> Any:
        """RealDoubleElement.prec(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 749)

        Return the precision of this number in bits.

        Always returns 53.

        EXAMPLES::

            sage: RDF(0).prec()
            53"""
    @overload
    def prec(self) -> Any:
        """RealDoubleElement.prec(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 749)

        Return the precision of this number in bits.

        Always returns 53.

        EXAMPLES::

            sage: RDF(0).prec()
            53"""
    @overload
    def real(self) -> Any:
        """RealDoubleElement.real(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 866)

        Return ``self`` - we are already real.

        EXAMPLES::

            sage: a = RDF(3)
            sage: a.real()
            3.0"""
    @overload
    def real(self) -> Any:
        """RealDoubleElement.real(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 866)

        Return ``self`` - we are already real.

        EXAMPLES::

            sage: a = RDF(3)
            sage: a.real()
            3.0"""
    @overload
    def round(self) -> Any:
        """RealDoubleElement.round(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1500)

        Round ``self`` to the nearest integer.

        This uses the convention of rounding half to even
        (i.e., if the fractional part of ``self`` is `0.5`, then it
        is rounded to the nearest even integer).

        EXAMPLES::

            sage: RDF(0.49).round()
            0
            sage: a=RDF(0.51).round(); a
            1
            sage: RDF(0.5).round()
            0
            sage: RDF(1.5).round()
            2"""
    @overload
    def round(self) -> Any:
        """RealDoubleElement.round(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1500)

        Round ``self`` to the nearest integer.

        This uses the convention of rounding half to even
        (i.e., if the fractional part of ``self`` is `0.5`, then it
        is rounded to the nearest even integer).

        EXAMPLES::

            sage: RDF(0.49).round()
            0
            sage: a=RDF(0.51).round(); a
            1
            sage: RDF(0.5).round()
            0
            sage: RDF(1.5).round()
            2"""
    @overload
    def round(self) -> Any:
        """RealDoubleElement.round(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1500)

        Round ``self`` to the nearest integer.

        This uses the convention of rounding half to even
        (i.e., if the fractional part of ``self`` is `0.5`, then it
        is rounded to the nearest even integer).

        EXAMPLES::

            sage: RDF(0.49).round()
            0
            sage: a=RDF(0.51).round(); a
            1
            sage: RDF(0.5).round()
            0
            sage: RDF(1.5).round()
            2"""
    @overload
    def round(self) -> Any:
        """RealDoubleElement.round(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1500)

        Round ``self`` to the nearest integer.

        This uses the convention of rounding half to even
        (i.e., if the fractional part of ``self`` is `0.5`, then it
        is rounded to the nearest even integer).

        EXAMPLES::

            sage: RDF(0.49).round()
            0
            sage: a=RDF(0.51).round(); a
            1
            sage: RDF(0.5).round()
            0
            sage: RDF(1.5).round()
            2"""
    @overload
    def round(self) -> Any:
        """RealDoubleElement.round(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1500)

        Round ``self`` to the nearest integer.

        This uses the convention of rounding half to even
        (i.e., if the fractional part of ``self`` is `0.5`, then it
        is rounded to the nearest even integer).

        EXAMPLES::

            sage: RDF(0.49).round()
            0
            sage: a=RDF(0.51).round(); a
            1
            sage: RDF(0.5).round()
            0
            sage: RDF(1.5).round()
            2"""
    @overload
    def sign(self) -> Any:
        """RealDoubleElement.sign(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1476)

        Return -1, 0, or 1 if ``self`` is negative, zero, or positive;
        respectively.

        EXAMPLES::

            sage: RDF(-1.5).sign()
            -1
            sage: RDF(0).sign()
            0
            sage: RDF(2.5).sign()
            1"""
    @overload
    def sign(self) -> Any:
        """RealDoubleElement.sign(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1476)

        Return -1, 0, or 1 if ``self`` is negative, zero, or positive;
        respectively.

        EXAMPLES::

            sage: RDF(-1.5).sign()
            -1
            sage: RDF(0).sign()
            0
            sage: RDF(2.5).sign()
            1"""
    @overload
    def sign(self) -> Any:
        """RealDoubleElement.sign(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1476)

        Return -1, 0, or 1 if ``self`` is negative, zero, or positive;
        respectively.

        EXAMPLES::

            sage: RDF(-1.5).sign()
            -1
            sage: RDF(0).sign()
            0
            sage: RDF(2.5).sign()
            1"""
    @overload
    def sign(self) -> Any:
        """RealDoubleElement.sign(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1476)

        Return -1, 0, or 1 if ``self`` is negative, zero, or positive;
        respectively.

        EXAMPLES::

            sage: RDF(-1.5).sign()
            -1
            sage: RDF(0).sign()
            0
            sage: RDF(2.5).sign()
            1"""
    def sign_mantissa_exponent(self) -> Any:
        """RealDoubleElement.sign_mantissa_exponent(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1230)

        Return the sign, mantissa, and exponent of ``self``.

        In Sage (as in MPFR), floating-point numbers of precision `p`
        are of the form `s m 2^{e-p}`, where `s \\in \\{-1, 1\\}`,
        `2^{p-1} \\leq m < 2^p`, and `-2^{30} + 1 \\leq e \\leq 2^{30} -
        1`; plus the special values ``+0``, ``-0``, ``+infinity``,
        ``-infinity``, and ``NaN`` (which stands for Not-a-Number).

        This function returns `s`, `m`, and `e-p`.  For the special values:

        - ``+0`` returns ``(1, 0, 0)``
        - ``-0`` returns ``(-1, 0, 0)``
        - the return values for ``+infinity``, ``-infinity``, and ``NaN`` are
          not specified.

        EXAMPLES::

            sage: # needs sage.symbolic
            sage: a = RDF(exp(1.0)); a
            2.718281828459045
            sage: sign, mantissa, exponent = RDF(exp(1.0)).sign_mantissa_exponent()
            sage: sign, mantissa, exponent
            (1, 6121026514868073, -51)
            sage: sign*mantissa*(2**exponent) == a
            True

        The mantissa is always a nonnegative number::

            sage: RDF(-1).sign_mantissa_exponent()                                      # needs sage.rings.real_mpfr
            (-1, 4503599627370496, -52)

        TESTS::

            sage: RDF('+0').sign_mantissa_exponent()                                    # needs sage.rings.real_mpfr
            (1, 0, 0)
            sage: RDF('-0').sign_mantissa_exponent()                                    # needs sage.rings.real_mpfr
            (-1, 0, 0)"""
    @overload
    def sqrt(self, extend=..., all=...) -> Any:
        """RealDoubleElement.sqrt(self, extend=True, all=False)

        File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1799)

        The square root function.

        INPUT:

        - ``extend`` -- boolean (default: ``True``); if ``True``, return a
          square root in a complex field if necessary if ``self`` is negative.
          Otherwise raise a :exc:`ValueError`.

        - ``all`` -- boolean (default: ``False``); if ``True``, return a
          list of all square roots

        EXAMPLES::

            sage: r = RDF(4.0)
            sage: r.sqrt()
            2.0
            sage: r.sqrt()^2 == r
            True

        ::

            sage: r = RDF(4344)
            sage: r.sqrt()
            65.90902821313632
            sage: r.sqrt()^2 - r
            0.0

        ::

            sage: r = RDF(-2.0)
            sage: r.sqrt()                                                              # needs sage.rings.complex_double
            1.4142135623730951*I

        ::

            sage: RDF(2).sqrt(all=True)
            [1.4142135623730951, -1.4142135623730951]
            sage: RDF(0).sqrt(all=True)
            [0.0]
            sage: RDF(-2).sqrt(all=True)                                                # needs sage.rings.complex_double
            [1.4142135623730951*I, -1.4142135623730951*I]"""
    @overload
    def sqrt(self) -> Any:
        """RealDoubleElement.sqrt(self, extend=True, all=False)

        File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1799)

        The square root function.

        INPUT:

        - ``extend`` -- boolean (default: ``True``); if ``True``, return a
          square root in a complex field if necessary if ``self`` is negative.
          Otherwise raise a :exc:`ValueError`.

        - ``all`` -- boolean (default: ``False``); if ``True``, return a
          list of all square roots

        EXAMPLES::

            sage: r = RDF(4.0)
            sage: r.sqrt()
            2.0
            sage: r.sqrt()^2 == r
            True

        ::

            sage: r = RDF(4344)
            sage: r.sqrt()
            65.90902821313632
            sage: r.sqrt()^2 - r
            0.0

        ::

            sage: r = RDF(-2.0)
            sage: r.sqrt()                                                              # needs sage.rings.complex_double
            1.4142135623730951*I

        ::

            sage: RDF(2).sqrt(all=True)
            [1.4142135623730951, -1.4142135623730951]
            sage: RDF(0).sqrt(all=True)
            [0.0]
            sage: RDF(-2).sqrt(all=True)                                                # needs sage.rings.complex_double
            [1.4142135623730951*I, -1.4142135623730951*I]"""
    @overload
    def sqrt(self) -> Any:
        """RealDoubleElement.sqrt(self, extend=True, all=False)

        File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1799)

        The square root function.

        INPUT:

        - ``extend`` -- boolean (default: ``True``); if ``True``, return a
          square root in a complex field if necessary if ``self`` is negative.
          Otherwise raise a :exc:`ValueError`.

        - ``all`` -- boolean (default: ``False``); if ``True``, return a
          list of all square roots

        EXAMPLES::

            sage: r = RDF(4.0)
            sage: r.sqrt()
            2.0
            sage: r.sqrt()^2 == r
            True

        ::

            sage: r = RDF(4344)
            sage: r.sqrt()
            65.90902821313632
            sage: r.sqrt()^2 - r
            0.0

        ::

            sage: r = RDF(-2.0)
            sage: r.sqrt()                                                              # needs sage.rings.complex_double
            1.4142135623730951*I

        ::

            sage: RDF(2).sqrt(all=True)
            [1.4142135623730951, -1.4142135623730951]
            sage: RDF(0).sqrt(all=True)
            [0.0]
            sage: RDF(-2).sqrt(all=True)                                                # needs sage.rings.complex_double
            [1.4142135623730951*I, -1.4142135623730951*I]"""
    @overload
    def sqrt(self) -> Any:
        """RealDoubleElement.sqrt(self, extend=True, all=False)

        File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1799)

        The square root function.

        INPUT:

        - ``extend`` -- boolean (default: ``True``); if ``True``, return a
          square root in a complex field if necessary if ``self`` is negative.
          Otherwise raise a :exc:`ValueError`.

        - ``all`` -- boolean (default: ``False``); if ``True``, return a
          list of all square roots

        EXAMPLES::

            sage: r = RDF(4.0)
            sage: r.sqrt()
            2.0
            sage: r.sqrt()^2 == r
            True

        ::

            sage: r = RDF(4344)
            sage: r.sqrt()
            65.90902821313632
            sage: r.sqrt()^2 - r
            0.0

        ::

            sage: r = RDF(-2.0)
            sage: r.sqrt()                                                              # needs sage.rings.complex_double
            1.4142135623730951*I

        ::

            sage: RDF(2).sqrt(all=True)
            [1.4142135623730951, -1.4142135623730951]
            sage: RDF(0).sqrt(all=True)
            [0.0]
            sage: RDF(-2).sqrt(all=True)                                                # needs sage.rings.complex_double
            [1.4142135623730951*I, -1.4142135623730951*I]"""
    @overload
    def sqrt(self) -> Any:
        """RealDoubleElement.sqrt(self, extend=True, all=False)

        File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1799)

        The square root function.

        INPUT:

        - ``extend`` -- boolean (default: ``True``); if ``True``, return a
          square root in a complex field if necessary if ``self`` is negative.
          Otherwise raise a :exc:`ValueError`.

        - ``all`` -- boolean (default: ``False``); if ``True``, return a
          list of all square roots

        EXAMPLES::

            sage: r = RDF(4.0)
            sage: r.sqrt()
            2.0
            sage: r.sqrt()^2 == r
            True

        ::

            sage: r = RDF(4344)
            sage: r.sqrt()
            65.90902821313632
            sage: r.sqrt()^2 - r
            0.0

        ::

            sage: r = RDF(-2.0)
            sage: r.sqrt()                                                              # needs sage.rings.complex_double
            1.4142135623730951*I

        ::

            sage: RDF(2).sqrt(all=True)
            [1.4142135623730951, -1.4142135623730951]
            sage: RDF(0).sqrt(all=True)
            [0.0]
            sage: RDF(-2).sqrt(all=True)                                                # needs sage.rings.complex_double
            [1.4142135623730951*I, -1.4142135623730951*I]"""
    @overload
    def sqrt(self) -> Any:
        """RealDoubleElement.sqrt(self, extend=True, all=False)

        File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1799)

        The square root function.

        INPUT:

        - ``extend`` -- boolean (default: ``True``); if ``True``, return a
          square root in a complex field if necessary if ``self`` is negative.
          Otherwise raise a :exc:`ValueError`.

        - ``all`` -- boolean (default: ``False``); if ``True``, return a
          list of all square roots

        EXAMPLES::

            sage: r = RDF(4.0)
            sage: r.sqrt()
            2.0
            sage: r.sqrt()^2 == r
            True

        ::

            sage: r = RDF(4344)
            sage: r.sqrt()
            65.90902821313632
            sage: r.sqrt()^2 - r
            0.0

        ::

            sage: r = RDF(-2.0)
            sage: r.sqrt()                                                              # needs sage.rings.complex_double
            1.4142135623730951*I

        ::

            sage: RDF(2).sqrt(all=True)
            [1.4142135623730951, -1.4142135623730951]
            sage: RDF(0).sqrt(all=True)
            [0.0]
            sage: RDF(-2).sqrt(all=True)                                                # needs sage.rings.complex_double
            [1.4142135623730951*I, -1.4142135623730951*I]"""
    @overload
    def sqrt(self, all=...) -> Any:
        """RealDoubleElement.sqrt(self, extend=True, all=False)

        File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1799)

        The square root function.

        INPUT:

        - ``extend`` -- boolean (default: ``True``); if ``True``, return a
          square root in a complex field if necessary if ``self`` is negative.
          Otherwise raise a :exc:`ValueError`.

        - ``all`` -- boolean (default: ``False``); if ``True``, return a
          list of all square roots

        EXAMPLES::

            sage: r = RDF(4.0)
            sage: r.sqrt()
            2.0
            sage: r.sqrt()^2 == r
            True

        ::

            sage: r = RDF(4344)
            sage: r.sqrt()
            65.90902821313632
            sage: r.sqrt()^2 - r
            0.0

        ::

            sage: r = RDF(-2.0)
            sage: r.sqrt()                                                              # needs sage.rings.complex_double
            1.4142135623730951*I

        ::

            sage: RDF(2).sqrt(all=True)
            [1.4142135623730951, -1.4142135623730951]
            sage: RDF(0).sqrt(all=True)
            [0.0]
            sage: RDF(-2).sqrt(all=True)                                                # needs sage.rings.complex_double
            [1.4142135623730951*I, -1.4142135623730951*I]"""
    @overload
    def sqrt(self, all=...) -> Any:
        """RealDoubleElement.sqrt(self, extend=True, all=False)

        File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1799)

        The square root function.

        INPUT:

        - ``extend`` -- boolean (default: ``True``); if ``True``, return a
          square root in a complex field if necessary if ``self`` is negative.
          Otherwise raise a :exc:`ValueError`.

        - ``all`` -- boolean (default: ``False``); if ``True``, return a
          list of all square roots

        EXAMPLES::

            sage: r = RDF(4.0)
            sage: r.sqrt()
            2.0
            sage: r.sqrt()^2 == r
            True

        ::

            sage: r = RDF(4344)
            sage: r.sqrt()
            65.90902821313632
            sage: r.sqrt()^2 - r
            0.0

        ::

            sage: r = RDF(-2.0)
            sage: r.sqrt()                                                              # needs sage.rings.complex_double
            1.4142135623730951*I

        ::

            sage: RDF(2).sqrt(all=True)
            [1.4142135623730951, -1.4142135623730951]
            sage: RDF(0).sqrt(all=True)
            [0.0]
            sage: RDF(-2).sqrt(all=True)                                                # needs sage.rings.complex_double
            [1.4142135623730951*I, -1.4142135623730951*I]"""
    @overload
    def sqrt(self, all=...) -> Any:
        """RealDoubleElement.sqrt(self, extend=True, all=False)

        File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1799)

        The square root function.

        INPUT:

        - ``extend`` -- boolean (default: ``True``); if ``True``, return a
          square root in a complex field if necessary if ``self`` is negative.
          Otherwise raise a :exc:`ValueError`.

        - ``all`` -- boolean (default: ``False``); if ``True``, return a
          list of all square roots

        EXAMPLES::

            sage: r = RDF(4.0)
            sage: r.sqrt()
            2.0
            sage: r.sqrt()^2 == r
            True

        ::

            sage: r = RDF(4344)
            sage: r.sqrt()
            65.90902821313632
            sage: r.sqrt()^2 - r
            0.0

        ::

            sage: r = RDF(-2.0)
            sage: r.sqrt()                                                              # needs sage.rings.complex_double
            1.4142135623730951*I

        ::

            sage: RDF(2).sqrt(all=True)
            [1.4142135623730951, -1.4142135623730951]
            sage: RDF(0).sqrt(all=True)
            [0.0]
            sage: RDF(-2).sqrt(all=True)                                                # needs sage.rings.complex_double
            [1.4142135623730951*I, -1.4142135623730951*I]"""
    @overload
    def str(self) -> Any:
        """RealDoubleElement.str(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1157)

        Return the informal string representation of ``self``.

        EXAMPLES::

            sage: a = RDF('4.5'); a.str()
            '4.5'
            sage: a = RDF('49203480923840.2923904823048'); a.str()
            '49203480923840.29'
            sage: a = RDF(1)/RDF(0); a.str()
            '+infinity'
            sage: a = -RDF(1)/RDF(0); a.str()
            '-infinity'
            sage: a = RDF(0)/RDF(0); a.str()
            'NaN'

        We verify consistency with ``RR`` (mpfr reals)::

            sage: str(RR(RDF(1)/RDF(0))) == str(RDF(1)/RDF(0))
            True
            sage: str(RR(-RDF(1)/RDF(0))) == str(-RDF(1)/RDF(0))
            True
            sage: str(RR(RDF(0)/RDF(0))) == str(RDF(0)/RDF(0))
            True"""
    @overload
    def str(self) -> Any:
        """RealDoubleElement.str(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1157)

        Return the informal string representation of ``self``.

        EXAMPLES::

            sage: a = RDF('4.5'); a.str()
            '4.5'
            sage: a = RDF('49203480923840.2923904823048'); a.str()
            '49203480923840.29'
            sage: a = RDF(1)/RDF(0); a.str()
            '+infinity'
            sage: a = -RDF(1)/RDF(0); a.str()
            '-infinity'
            sage: a = RDF(0)/RDF(0); a.str()
            'NaN'

        We verify consistency with ``RR`` (mpfr reals)::

            sage: str(RR(RDF(1)/RDF(0))) == str(RDF(1)/RDF(0))
            True
            sage: str(RR(-RDF(1)/RDF(0))) == str(-RDF(1)/RDF(0))
            True
            sage: str(RR(RDF(0)/RDF(0))) == str(RDF(0)/RDF(0))
            True"""
    @overload
    def str(self) -> Any:
        """RealDoubleElement.str(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1157)

        Return the informal string representation of ``self``.

        EXAMPLES::

            sage: a = RDF('4.5'); a.str()
            '4.5'
            sage: a = RDF('49203480923840.2923904823048'); a.str()
            '49203480923840.29'
            sage: a = RDF(1)/RDF(0); a.str()
            '+infinity'
            sage: a = -RDF(1)/RDF(0); a.str()
            '-infinity'
            sage: a = RDF(0)/RDF(0); a.str()
            'NaN'

        We verify consistency with ``RR`` (mpfr reals)::

            sage: str(RR(RDF(1)/RDF(0))) == str(RDF(1)/RDF(0))
            True
            sage: str(RR(-RDF(1)/RDF(0))) == str(-RDF(1)/RDF(0))
            True
            sage: str(RR(RDF(0)/RDF(0))) == str(RDF(0)/RDF(0))
            True"""
    @overload
    def str(self) -> Any:
        """RealDoubleElement.str(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1157)

        Return the informal string representation of ``self``.

        EXAMPLES::

            sage: a = RDF('4.5'); a.str()
            '4.5'
            sage: a = RDF('49203480923840.2923904823048'); a.str()
            '49203480923840.29'
            sage: a = RDF(1)/RDF(0); a.str()
            '+infinity'
            sage: a = -RDF(1)/RDF(0); a.str()
            '-infinity'
            sage: a = RDF(0)/RDF(0); a.str()
            'NaN'

        We verify consistency with ``RR`` (mpfr reals)::

            sage: str(RR(RDF(1)/RDF(0))) == str(RDF(1)/RDF(0))
            True
            sage: str(RR(-RDF(1)/RDF(0))) == str(-RDF(1)/RDF(0))
            True
            sage: str(RR(RDF(0)/RDF(0))) == str(RDF(0)/RDF(0))
            True"""
    @overload
    def str(self) -> Any:
        """RealDoubleElement.str(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1157)

        Return the informal string representation of ``self``.

        EXAMPLES::

            sage: a = RDF('4.5'); a.str()
            '4.5'
            sage: a = RDF('49203480923840.2923904823048'); a.str()
            '49203480923840.29'
            sage: a = RDF(1)/RDF(0); a.str()
            '+infinity'
            sage: a = -RDF(1)/RDF(0); a.str()
            '-infinity'
            sage: a = RDF(0)/RDF(0); a.str()
            'NaN'

        We verify consistency with ``RR`` (mpfr reals)::

            sage: str(RR(RDF(1)/RDF(0))) == str(RDF(1)/RDF(0))
            True
            sage: str(RR(-RDF(1)/RDF(0))) == str(-RDF(1)/RDF(0))
            True
            sage: str(RR(RDF(0)/RDF(0))) == str(RDF(0)/RDF(0))
            True"""
    @overload
    def str(self) -> Any:
        """RealDoubleElement.str(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1157)

        Return the informal string representation of ``self``.

        EXAMPLES::

            sage: a = RDF('4.5'); a.str()
            '4.5'
            sage: a = RDF('49203480923840.2923904823048'); a.str()
            '49203480923840.29'
            sage: a = RDF(1)/RDF(0); a.str()
            '+infinity'
            sage: a = -RDF(1)/RDF(0); a.str()
            '-infinity'
            sage: a = RDF(0)/RDF(0); a.str()
            'NaN'

        We verify consistency with ``RR`` (mpfr reals)::

            sage: str(RR(RDF(1)/RDF(0))) == str(RDF(1)/RDF(0))
            True
            sage: str(RR(-RDF(1)/RDF(0))) == str(-RDF(1)/RDF(0))
            True
            sage: str(RR(RDF(0)/RDF(0))) == str(RDF(0)/RDF(0))
            True"""
    @overload
    def trunc(self) -> Any:
        """RealDoubleElement.trunc(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1553)

        Truncates this number (returns integer part).

        EXAMPLES::

            sage: RDF(2.99).trunc()
            2
            sage: RDF(-2.00).trunc()
            -2
            sage: RDF(0.00).trunc()
            0"""
    @overload
    def trunc(self) -> Any:
        """RealDoubleElement.trunc(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1553)

        Truncates this number (returns integer part).

        EXAMPLES::

            sage: RDF(2.99).trunc()
            2
            sage: RDF(-2.00).trunc()
            -2
            sage: RDF(0.00).trunc()
            0"""
    @overload
    def trunc(self) -> Any:
        """RealDoubleElement.trunc(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1553)

        Truncates this number (returns integer part).

        EXAMPLES::

            sage: RDF(2.99).trunc()
            2
            sage: RDF(-2.00).trunc()
            -2
            sage: RDF(0.00).trunc()
            0"""
    @overload
    def trunc(self) -> Any:
        """RealDoubleElement.trunc(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1553)

        Truncates this number (returns integer part).

        EXAMPLES::

            sage: RDF(2.99).trunc()
            2
            sage: RDF(-2.00).trunc()
            -2
            sage: RDF(0.00).trunc()
            0"""
    @overload
    def ulp(self) -> Any:
        """RealDoubleElement.ulp(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 762)

        Return the unit of least precision of ``self``, which is the
        weight of the least significant bit of ``self``. This is always
        a strictly positive number. It is also the gap between this
        number and the closest number with larger absolute value that
        can be represented.

        EXAMPLES::

            sage: a = RDF(pi)                                                           # needs sage.symbolic
            sage: a.ulp()                                                               # needs sage.symbolic
            4.440892098500626e-16
            sage: b = a + a.ulp()                                                       # needs sage.symbolic

        Adding or subtracting an ulp always gives a different number::

            sage: # needs sage.symbolic
            sage: a + a.ulp() == a
            False
            sage: a - a.ulp() == a
            False
            sage: b + b.ulp() == b
            False
            sage: b - b.ulp() == b
            False

        Since the default rounding mode is round-to-nearest, adding or
        subtracting something less than half an ulp always gives the
        same number, unless the result has a smaller ulp. The latter
        can only happen if the input number is (up to sign) exactly a
        power of 2::

            sage: # needs sage.symbolic
            sage: a - a.ulp()/3 == a
            True
            sage: a + a.ulp()/3 == a
            True
            sage: b - b.ulp()/3 == b
            True
            sage: b + b.ulp()/3 == b
            True

            sage: c = RDF(1)
            sage: c - c.ulp()/3 == c
            False
            sage: c.ulp()
            2.220446049250313e-16
            sage: (c - c.ulp()).ulp()
            1.1102230246251565e-16

        The ulp is always positive::

            sage: RDF(-1).ulp()
            2.220446049250313e-16

        The ulp of zero is the smallest positive number in RDF::

            sage: RDF(0).ulp()
            5e-324
            sage: RDF(0).ulp()/2
            0.0

        Some special values::

            sage: a = RDF(1)/RDF(0); a
            +infinity
            sage: a.ulp()
            +infinity
            sage: (-a).ulp()
            +infinity
            sage: a = RDF('nan')
            sage: a.ulp() is a
            True

        The ulp method works correctly with small numbers::

            sage: u = RDF(0).ulp()
            sage: u.ulp() == u
            True
            sage: x = u * (2^52-1)  # largest denormal number
            sage: x.ulp() == u
            True
            sage: x = u * 2^52  # smallest normal number
            sage: x.ulp() == u
            True"""
    @overload
    def ulp(self) -> Any:
        """RealDoubleElement.ulp(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 762)

        Return the unit of least precision of ``self``, which is the
        weight of the least significant bit of ``self``. This is always
        a strictly positive number. It is also the gap between this
        number and the closest number with larger absolute value that
        can be represented.

        EXAMPLES::

            sage: a = RDF(pi)                                                           # needs sage.symbolic
            sage: a.ulp()                                                               # needs sage.symbolic
            4.440892098500626e-16
            sage: b = a + a.ulp()                                                       # needs sage.symbolic

        Adding or subtracting an ulp always gives a different number::

            sage: # needs sage.symbolic
            sage: a + a.ulp() == a
            False
            sage: a - a.ulp() == a
            False
            sage: b + b.ulp() == b
            False
            sage: b - b.ulp() == b
            False

        Since the default rounding mode is round-to-nearest, adding or
        subtracting something less than half an ulp always gives the
        same number, unless the result has a smaller ulp. The latter
        can only happen if the input number is (up to sign) exactly a
        power of 2::

            sage: # needs sage.symbolic
            sage: a - a.ulp()/3 == a
            True
            sage: a + a.ulp()/3 == a
            True
            sage: b - b.ulp()/3 == b
            True
            sage: b + b.ulp()/3 == b
            True

            sage: c = RDF(1)
            sage: c - c.ulp()/3 == c
            False
            sage: c.ulp()
            2.220446049250313e-16
            sage: (c - c.ulp()).ulp()
            1.1102230246251565e-16

        The ulp is always positive::

            sage: RDF(-1).ulp()
            2.220446049250313e-16

        The ulp of zero is the smallest positive number in RDF::

            sage: RDF(0).ulp()
            5e-324
            sage: RDF(0).ulp()/2
            0.0

        Some special values::

            sage: a = RDF(1)/RDF(0); a
            +infinity
            sage: a.ulp()
            +infinity
            sage: (-a).ulp()
            +infinity
            sage: a = RDF('nan')
            sage: a.ulp() is a
            True

        The ulp method works correctly with small numbers::

            sage: u = RDF(0).ulp()
            sage: u.ulp() == u
            True
            sage: x = u * (2^52-1)  # largest denormal number
            sage: x.ulp() == u
            True
            sage: x = u * 2^52  # smallest normal number
            sage: x.ulp() == u
            True"""
    @overload
    def ulp(self) -> Any:
        """RealDoubleElement.ulp(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 762)

        Return the unit of least precision of ``self``, which is the
        weight of the least significant bit of ``self``. This is always
        a strictly positive number. It is also the gap between this
        number and the closest number with larger absolute value that
        can be represented.

        EXAMPLES::

            sage: a = RDF(pi)                                                           # needs sage.symbolic
            sage: a.ulp()                                                               # needs sage.symbolic
            4.440892098500626e-16
            sage: b = a + a.ulp()                                                       # needs sage.symbolic

        Adding or subtracting an ulp always gives a different number::

            sage: # needs sage.symbolic
            sage: a + a.ulp() == a
            False
            sage: a - a.ulp() == a
            False
            sage: b + b.ulp() == b
            False
            sage: b - b.ulp() == b
            False

        Since the default rounding mode is round-to-nearest, adding or
        subtracting something less than half an ulp always gives the
        same number, unless the result has a smaller ulp. The latter
        can only happen if the input number is (up to sign) exactly a
        power of 2::

            sage: # needs sage.symbolic
            sage: a - a.ulp()/3 == a
            True
            sage: a + a.ulp()/3 == a
            True
            sage: b - b.ulp()/3 == b
            True
            sage: b + b.ulp()/3 == b
            True

            sage: c = RDF(1)
            sage: c - c.ulp()/3 == c
            False
            sage: c.ulp()
            2.220446049250313e-16
            sage: (c - c.ulp()).ulp()
            1.1102230246251565e-16

        The ulp is always positive::

            sage: RDF(-1).ulp()
            2.220446049250313e-16

        The ulp of zero is the smallest positive number in RDF::

            sage: RDF(0).ulp()
            5e-324
            sage: RDF(0).ulp()/2
            0.0

        Some special values::

            sage: a = RDF(1)/RDF(0); a
            +infinity
            sage: a.ulp()
            +infinity
            sage: (-a).ulp()
            +infinity
            sage: a = RDF('nan')
            sage: a.ulp() is a
            True

        The ulp method works correctly with small numbers::

            sage: u = RDF(0).ulp()
            sage: u.ulp() == u
            True
            sage: x = u * (2^52-1)  # largest denormal number
            sage: x.ulp() == u
            True
            sage: x = u * 2^52  # smallest normal number
            sage: x.ulp() == u
            True"""
    @overload
    def ulp(self) -> Any:
        """RealDoubleElement.ulp(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 762)

        Return the unit of least precision of ``self``, which is the
        weight of the least significant bit of ``self``. This is always
        a strictly positive number. It is also the gap between this
        number and the closest number with larger absolute value that
        can be represented.

        EXAMPLES::

            sage: a = RDF(pi)                                                           # needs sage.symbolic
            sage: a.ulp()                                                               # needs sage.symbolic
            4.440892098500626e-16
            sage: b = a + a.ulp()                                                       # needs sage.symbolic

        Adding or subtracting an ulp always gives a different number::

            sage: # needs sage.symbolic
            sage: a + a.ulp() == a
            False
            sage: a - a.ulp() == a
            False
            sage: b + b.ulp() == b
            False
            sage: b - b.ulp() == b
            False

        Since the default rounding mode is round-to-nearest, adding or
        subtracting something less than half an ulp always gives the
        same number, unless the result has a smaller ulp. The latter
        can only happen if the input number is (up to sign) exactly a
        power of 2::

            sage: # needs sage.symbolic
            sage: a - a.ulp()/3 == a
            True
            sage: a + a.ulp()/3 == a
            True
            sage: b - b.ulp()/3 == b
            True
            sage: b + b.ulp()/3 == b
            True

            sage: c = RDF(1)
            sage: c - c.ulp()/3 == c
            False
            sage: c.ulp()
            2.220446049250313e-16
            sage: (c - c.ulp()).ulp()
            1.1102230246251565e-16

        The ulp is always positive::

            sage: RDF(-1).ulp()
            2.220446049250313e-16

        The ulp of zero is the smallest positive number in RDF::

            sage: RDF(0).ulp()
            5e-324
            sage: RDF(0).ulp()/2
            0.0

        Some special values::

            sage: a = RDF(1)/RDF(0); a
            +infinity
            sage: a.ulp()
            +infinity
            sage: (-a).ulp()
            +infinity
            sage: a = RDF('nan')
            sage: a.ulp() is a
            True

        The ulp method works correctly with small numbers::

            sage: u = RDF(0).ulp()
            sage: u.ulp() == u
            True
            sage: x = u * (2^52-1)  # largest denormal number
            sage: x.ulp() == u
            True
            sage: x = u * 2^52  # smallest normal number
            sage: x.ulp() == u
            True"""
    @overload
    def ulp(self) -> Any:
        """RealDoubleElement.ulp(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 762)

        Return the unit of least precision of ``self``, which is the
        weight of the least significant bit of ``self``. This is always
        a strictly positive number. It is also the gap between this
        number and the closest number with larger absolute value that
        can be represented.

        EXAMPLES::

            sage: a = RDF(pi)                                                           # needs sage.symbolic
            sage: a.ulp()                                                               # needs sage.symbolic
            4.440892098500626e-16
            sage: b = a + a.ulp()                                                       # needs sage.symbolic

        Adding or subtracting an ulp always gives a different number::

            sage: # needs sage.symbolic
            sage: a + a.ulp() == a
            False
            sage: a - a.ulp() == a
            False
            sage: b + b.ulp() == b
            False
            sage: b - b.ulp() == b
            False

        Since the default rounding mode is round-to-nearest, adding or
        subtracting something less than half an ulp always gives the
        same number, unless the result has a smaller ulp. The latter
        can only happen if the input number is (up to sign) exactly a
        power of 2::

            sage: # needs sage.symbolic
            sage: a - a.ulp()/3 == a
            True
            sage: a + a.ulp()/3 == a
            True
            sage: b - b.ulp()/3 == b
            True
            sage: b + b.ulp()/3 == b
            True

            sage: c = RDF(1)
            sage: c - c.ulp()/3 == c
            False
            sage: c.ulp()
            2.220446049250313e-16
            sage: (c - c.ulp()).ulp()
            1.1102230246251565e-16

        The ulp is always positive::

            sage: RDF(-1).ulp()
            2.220446049250313e-16

        The ulp of zero is the smallest positive number in RDF::

            sage: RDF(0).ulp()
            5e-324
            sage: RDF(0).ulp()/2
            0.0

        Some special values::

            sage: a = RDF(1)/RDF(0); a
            +infinity
            sage: a.ulp()
            +infinity
            sage: (-a).ulp()
            +infinity
            sage: a = RDF('nan')
            sage: a.ulp() is a
            True

        The ulp method works correctly with small numbers::

            sage: u = RDF(0).ulp()
            sage: u.ulp() == u
            True
            sage: x = u * (2^52-1)  # largest denormal number
            sage: x.ulp() == u
            True
            sage: x = u * 2^52  # smallest normal number
            sage: x.ulp() == u
            True"""
    @overload
    def ulp(self) -> Any:
        """RealDoubleElement.ulp(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 762)

        Return the unit of least precision of ``self``, which is the
        weight of the least significant bit of ``self``. This is always
        a strictly positive number. It is also the gap between this
        number and the closest number with larger absolute value that
        can be represented.

        EXAMPLES::

            sage: a = RDF(pi)                                                           # needs sage.symbolic
            sage: a.ulp()                                                               # needs sage.symbolic
            4.440892098500626e-16
            sage: b = a + a.ulp()                                                       # needs sage.symbolic

        Adding or subtracting an ulp always gives a different number::

            sage: # needs sage.symbolic
            sage: a + a.ulp() == a
            False
            sage: a - a.ulp() == a
            False
            sage: b + b.ulp() == b
            False
            sage: b - b.ulp() == b
            False

        Since the default rounding mode is round-to-nearest, adding or
        subtracting something less than half an ulp always gives the
        same number, unless the result has a smaller ulp. The latter
        can only happen if the input number is (up to sign) exactly a
        power of 2::

            sage: # needs sage.symbolic
            sage: a - a.ulp()/3 == a
            True
            sage: a + a.ulp()/3 == a
            True
            sage: b - b.ulp()/3 == b
            True
            sage: b + b.ulp()/3 == b
            True

            sage: c = RDF(1)
            sage: c - c.ulp()/3 == c
            False
            sage: c.ulp()
            2.220446049250313e-16
            sage: (c - c.ulp()).ulp()
            1.1102230246251565e-16

        The ulp is always positive::

            sage: RDF(-1).ulp()
            2.220446049250313e-16

        The ulp of zero is the smallest positive number in RDF::

            sage: RDF(0).ulp()
            5e-324
            sage: RDF(0).ulp()/2
            0.0

        Some special values::

            sage: a = RDF(1)/RDF(0); a
            +infinity
            sage: a.ulp()
            +infinity
            sage: (-a).ulp()
            +infinity
            sage: a = RDF('nan')
            sage: a.ulp() is a
            True

        The ulp method works correctly with small numbers::

            sage: u = RDF(0).ulp()
            sage: u.ulp() == u
            True
            sage: x = u * (2^52-1)  # largest denormal number
            sage: x.ulp() == u
            True
            sage: x = u * 2^52  # smallest normal number
            sage: x.ulp() == u
            True"""
    @overload
    def ulp(self) -> Any:
        """RealDoubleElement.ulp(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 762)

        Return the unit of least precision of ``self``, which is the
        weight of the least significant bit of ``self``. This is always
        a strictly positive number. It is also the gap between this
        number and the closest number with larger absolute value that
        can be represented.

        EXAMPLES::

            sage: a = RDF(pi)                                                           # needs sage.symbolic
            sage: a.ulp()                                                               # needs sage.symbolic
            4.440892098500626e-16
            sage: b = a + a.ulp()                                                       # needs sage.symbolic

        Adding or subtracting an ulp always gives a different number::

            sage: # needs sage.symbolic
            sage: a + a.ulp() == a
            False
            sage: a - a.ulp() == a
            False
            sage: b + b.ulp() == b
            False
            sage: b - b.ulp() == b
            False

        Since the default rounding mode is round-to-nearest, adding or
        subtracting something less than half an ulp always gives the
        same number, unless the result has a smaller ulp. The latter
        can only happen if the input number is (up to sign) exactly a
        power of 2::

            sage: # needs sage.symbolic
            sage: a - a.ulp()/3 == a
            True
            sage: a + a.ulp()/3 == a
            True
            sage: b - b.ulp()/3 == b
            True
            sage: b + b.ulp()/3 == b
            True

            sage: c = RDF(1)
            sage: c - c.ulp()/3 == c
            False
            sage: c.ulp()
            2.220446049250313e-16
            sage: (c - c.ulp()).ulp()
            1.1102230246251565e-16

        The ulp is always positive::

            sage: RDF(-1).ulp()
            2.220446049250313e-16

        The ulp of zero is the smallest positive number in RDF::

            sage: RDF(0).ulp()
            5e-324
            sage: RDF(0).ulp()/2
            0.0

        Some special values::

            sage: a = RDF(1)/RDF(0); a
            +infinity
            sage: a.ulp()
            +infinity
            sage: (-a).ulp()
            +infinity
            sage: a = RDF('nan')
            sage: a.ulp() is a
            True

        The ulp method works correctly with small numbers::

            sage: u = RDF(0).ulp()
            sage: u.ulp() == u
            True
            sage: x = u * (2^52-1)  # largest denormal number
            sage: x.ulp() == u
            True
            sage: x = u * 2^52  # smallest normal number
            sage: x.ulp() == u
            True"""
    @overload
    def ulp(self) -> Any:
        """RealDoubleElement.ulp(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 762)

        Return the unit of least precision of ``self``, which is the
        weight of the least significant bit of ``self``. This is always
        a strictly positive number. It is also the gap between this
        number and the closest number with larger absolute value that
        can be represented.

        EXAMPLES::

            sage: a = RDF(pi)                                                           # needs sage.symbolic
            sage: a.ulp()                                                               # needs sage.symbolic
            4.440892098500626e-16
            sage: b = a + a.ulp()                                                       # needs sage.symbolic

        Adding or subtracting an ulp always gives a different number::

            sage: # needs sage.symbolic
            sage: a + a.ulp() == a
            False
            sage: a - a.ulp() == a
            False
            sage: b + b.ulp() == b
            False
            sage: b - b.ulp() == b
            False

        Since the default rounding mode is round-to-nearest, adding or
        subtracting something less than half an ulp always gives the
        same number, unless the result has a smaller ulp. The latter
        can only happen if the input number is (up to sign) exactly a
        power of 2::

            sage: # needs sage.symbolic
            sage: a - a.ulp()/3 == a
            True
            sage: a + a.ulp()/3 == a
            True
            sage: b - b.ulp()/3 == b
            True
            sage: b + b.ulp()/3 == b
            True

            sage: c = RDF(1)
            sage: c - c.ulp()/3 == c
            False
            sage: c.ulp()
            2.220446049250313e-16
            sage: (c - c.ulp()).ulp()
            1.1102230246251565e-16

        The ulp is always positive::

            sage: RDF(-1).ulp()
            2.220446049250313e-16

        The ulp of zero is the smallest positive number in RDF::

            sage: RDF(0).ulp()
            5e-324
            sage: RDF(0).ulp()/2
            0.0

        Some special values::

            sage: a = RDF(1)/RDF(0); a
            +infinity
            sage: a.ulp()
            +infinity
            sage: (-a).ulp()
            +infinity
            sage: a = RDF('nan')
            sage: a.ulp() is a
            True

        The ulp method works correctly with small numbers::

            sage: u = RDF(0).ulp()
            sage: u.ulp() == u
            True
            sage: x = u * (2^52-1)  # largest denormal number
            sage: x.ulp() == u
            True
            sage: x = u * 2^52  # smallest normal number
            sage: x.ulp() == u
            True"""
    @overload
    def ulp(self) -> Any:
        """RealDoubleElement.ulp(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 762)

        Return the unit of least precision of ``self``, which is the
        weight of the least significant bit of ``self``. This is always
        a strictly positive number. It is also the gap between this
        number and the closest number with larger absolute value that
        can be represented.

        EXAMPLES::

            sage: a = RDF(pi)                                                           # needs sage.symbolic
            sage: a.ulp()                                                               # needs sage.symbolic
            4.440892098500626e-16
            sage: b = a + a.ulp()                                                       # needs sage.symbolic

        Adding or subtracting an ulp always gives a different number::

            sage: # needs sage.symbolic
            sage: a + a.ulp() == a
            False
            sage: a - a.ulp() == a
            False
            sage: b + b.ulp() == b
            False
            sage: b - b.ulp() == b
            False

        Since the default rounding mode is round-to-nearest, adding or
        subtracting something less than half an ulp always gives the
        same number, unless the result has a smaller ulp. The latter
        can only happen if the input number is (up to sign) exactly a
        power of 2::

            sage: # needs sage.symbolic
            sage: a - a.ulp()/3 == a
            True
            sage: a + a.ulp()/3 == a
            True
            sage: b - b.ulp()/3 == b
            True
            sage: b + b.ulp()/3 == b
            True

            sage: c = RDF(1)
            sage: c - c.ulp()/3 == c
            False
            sage: c.ulp()
            2.220446049250313e-16
            sage: (c - c.ulp()).ulp()
            1.1102230246251565e-16

        The ulp is always positive::

            sage: RDF(-1).ulp()
            2.220446049250313e-16

        The ulp of zero is the smallest positive number in RDF::

            sage: RDF(0).ulp()
            5e-324
            sage: RDF(0).ulp()/2
            0.0

        Some special values::

            sage: a = RDF(1)/RDF(0); a
            +infinity
            sage: a.ulp()
            +infinity
            sage: (-a).ulp()
            +infinity
            sage: a = RDF('nan')
            sage: a.ulp() is a
            True

        The ulp method works correctly with small numbers::

            sage: u = RDF(0).ulp()
            sage: u.ulp() == u
            True
            sage: x = u * (2^52-1)  # largest denormal number
            sage: x.ulp() == u
            True
            sage: x = u * 2^52  # smallest normal number
            sage: x.ulp() == u
            True"""
    @overload
    def ulp(self) -> Any:
        """RealDoubleElement.ulp(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 762)

        Return the unit of least precision of ``self``, which is the
        weight of the least significant bit of ``self``. This is always
        a strictly positive number. It is also the gap between this
        number and the closest number with larger absolute value that
        can be represented.

        EXAMPLES::

            sage: a = RDF(pi)                                                           # needs sage.symbolic
            sage: a.ulp()                                                               # needs sage.symbolic
            4.440892098500626e-16
            sage: b = a + a.ulp()                                                       # needs sage.symbolic

        Adding or subtracting an ulp always gives a different number::

            sage: # needs sage.symbolic
            sage: a + a.ulp() == a
            False
            sage: a - a.ulp() == a
            False
            sage: b + b.ulp() == b
            False
            sage: b - b.ulp() == b
            False

        Since the default rounding mode is round-to-nearest, adding or
        subtracting something less than half an ulp always gives the
        same number, unless the result has a smaller ulp. The latter
        can only happen if the input number is (up to sign) exactly a
        power of 2::

            sage: # needs sage.symbolic
            sage: a - a.ulp()/3 == a
            True
            sage: a + a.ulp()/3 == a
            True
            sage: b - b.ulp()/3 == b
            True
            sage: b + b.ulp()/3 == b
            True

            sage: c = RDF(1)
            sage: c - c.ulp()/3 == c
            False
            sage: c.ulp()
            2.220446049250313e-16
            sage: (c - c.ulp()).ulp()
            1.1102230246251565e-16

        The ulp is always positive::

            sage: RDF(-1).ulp()
            2.220446049250313e-16

        The ulp of zero is the smallest positive number in RDF::

            sage: RDF(0).ulp()
            5e-324
            sage: RDF(0).ulp()/2
            0.0

        Some special values::

            sage: a = RDF(1)/RDF(0); a
            +infinity
            sage: a.ulp()
            +infinity
            sage: (-a).ulp()
            +infinity
            sage: a = RDF('nan')
            sage: a.ulp() is a
            True

        The ulp method works correctly with small numbers::

            sage: u = RDF(0).ulp()
            sage: u.ulp() == u
            True
            sage: x = u * (2^52-1)  # largest denormal number
            sage: x.ulp() == u
            True
            sage: x = u * 2^52  # smallest normal number
            sage: x.ulp() == u
            True"""
    @overload
    def ulp(self) -> Any:
        """RealDoubleElement.ulp(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 762)

        Return the unit of least precision of ``self``, which is the
        weight of the least significant bit of ``self``. This is always
        a strictly positive number. It is also the gap between this
        number and the closest number with larger absolute value that
        can be represented.

        EXAMPLES::

            sage: a = RDF(pi)                                                           # needs sage.symbolic
            sage: a.ulp()                                                               # needs sage.symbolic
            4.440892098500626e-16
            sage: b = a + a.ulp()                                                       # needs sage.symbolic

        Adding or subtracting an ulp always gives a different number::

            sage: # needs sage.symbolic
            sage: a + a.ulp() == a
            False
            sage: a - a.ulp() == a
            False
            sage: b + b.ulp() == b
            False
            sage: b - b.ulp() == b
            False

        Since the default rounding mode is round-to-nearest, adding or
        subtracting something less than half an ulp always gives the
        same number, unless the result has a smaller ulp. The latter
        can only happen if the input number is (up to sign) exactly a
        power of 2::

            sage: # needs sage.symbolic
            sage: a - a.ulp()/3 == a
            True
            sage: a + a.ulp()/3 == a
            True
            sage: b - b.ulp()/3 == b
            True
            sage: b + b.ulp()/3 == b
            True

            sage: c = RDF(1)
            sage: c - c.ulp()/3 == c
            False
            sage: c.ulp()
            2.220446049250313e-16
            sage: (c - c.ulp()).ulp()
            1.1102230246251565e-16

        The ulp is always positive::

            sage: RDF(-1).ulp()
            2.220446049250313e-16

        The ulp of zero is the smallest positive number in RDF::

            sage: RDF(0).ulp()
            5e-324
            sage: RDF(0).ulp()/2
            0.0

        Some special values::

            sage: a = RDF(1)/RDF(0); a
            +infinity
            sage: a.ulp()
            +infinity
            sage: (-a).ulp()
            +infinity
            sage: a = RDF('nan')
            sage: a.ulp() is a
            True

        The ulp method works correctly with small numbers::

            sage: u = RDF(0).ulp()
            sage: u.ulp() == u
            True
            sage: x = u * (2^52-1)  # largest denormal number
            sage: x.ulp() == u
            True
            sage: x = u * 2^52  # smallest normal number
            sage: x.ulp() == u
            True"""
    @overload
    def ulp(self) -> Any:
        """RealDoubleElement.ulp(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 762)

        Return the unit of least precision of ``self``, which is the
        weight of the least significant bit of ``self``. This is always
        a strictly positive number. It is also the gap between this
        number and the closest number with larger absolute value that
        can be represented.

        EXAMPLES::

            sage: a = RDF(pi)                                                           # needs sage.symbolic
            sage: a.ulp()                                                               # needs sage.symbolic
            4.440892098500626e-16
            sage: b = a + a.ulp()                                                       # needs sage.symbolic

        Adding or subtracting an ulp always gives a different number::

            sage: # needs sage.symbolic
            sage: a + a.ulp() == a
            False
            sage: a - a.ulp() == a
            False
            sage: b + b.ulp() == b
            False
            sage: b - b.ulp() == b
            False

        Since the default rounding mode is round-to-nearest, adding or
        subtracting something less than half an ulp always gives the
        same number, unless the result has a smaller ulp. The latter
        can only happen if the input number is (up to sign) exactly a
        power of 2::

            sage: # needs sage.symbolic
            sage: a - a.ulp()/3 == a
            True
            sage: a + a.ulp()/3 == a
            True
            sage: b - b.ulp()/3 == b
            True
            sage: b + b.ulp()/3 == b
            True

            sage: c = RDF(1)
            sage: c - c.ulp()/3 == c
            False
            sage: c.ulp()
            2.220446049250313e-16
            sage: (c - c.ulp()).ulp()
            1.1102230246251565e-16

        The ulp is always positive::

            sage: RDF(-1).ulp()
            2.220446049250313e-16

        The ulp of zero is the smallest positive number in RDF::

            sage: RDF(0).ulp()
            5e-324
            sage: RDF(0).ulp()/2
            0.0

        Some special values::

            sage: a = RDF(1)/RDF(0); a
            +infinity
            sage: a.ulp()
            +infinity
            sage: (-a).ulp()
            +infinity
            sage: a = RDF('nan')
            sage: a.ulp() is a
            True

        The ulp method works correctly with small numbers::

            sage: u = RDF(0).ulp()
            sage: u.ulp() == u
            True
            sage: x = u * (2^52-1)  # largest denormal number
            sage: x.ulp() == u
            True
            sage: x = u * 2^52  # smallest normal number
            sage: x.ulp() == u
            True"""
    @overload
    def ulp(self) -> Any:
        """RealDoubleElement.ulp(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 762)

        Return the unit of least precision of ``self``, which is the
        weight of the least significant bit of ``self``. This is always
        a strictly positive number. It is also the gap between this
        number and the closest number with larger absolute value that
        can be represented.

        EXAMPLES::

            sage: a = RDF(pi)                                                           # needs sage.symbolic
            sage: a.ulp()                                                               # needs sage.symbolic
            4.440892098500626e-16
            sage: b = a + a.ulp()                                                       # needs sage.symbolic

        Adding or subtracting an ulp always gives a different number::

            sage: # needs sage.symbolic
            sage: a + a.ulp() == a
            False
            sage: a - a.ulp() == a
            False
            sage: b + b.ulp() == b
            False
            sage: b - b.ulp() == b
            False

        Since the default rounding mode is round-to-nearest, adding or
        subtracting something less than half an ulp always gives the
        same number, unless the result has a smaller ulp. The latter
        can only happen if the input number is (up to sign) exactly a
        power of 2::

            sage: # needs sage.symbolic
            sage: a - a.ulp()/3 == a
            True
            sage: a + a.ulp()/3 == a
            True
            sage: b - b.ulp()/3 == b
            True
            sage: b + b.ulp()/3 == b
            True

            sage: c = RDF(1)
            sage: c - c.ulp()/3 == c
            False
            sage: c.ulp()
            2.220446049250313e-16
            sage: (c - c.ulp()).ulp()
            1.1102230246251565e-16

        The ulp is always positive::

            sage: RDF(-1).ulp()
            2.220446049250313e-16

        The ulp of zero is the smallest positive number in RDF::

            sage: RDF(0).ulp()
            5e-324
            sage: RDF(0).ulp()/2
            0.0

        Some special values::

            sage: a = RDF(1)/RDF(0); a
            +infinity
            sage: a.ulp()
            +infinity
            sage: (-a).ulp()
            +infinity
            sage: a = RDF('nan')
            sage: a.ulp() is a
            True

        The ulp method works correctly with small numbers::

            sage: u = RDF(0).ulp()
            sage: u.ulp() == u
            True
            sage: x = u * (2^52-1)  # largest denormal number
            sage: x.ulp() == u
            True
            sage: x = u * 2^52  # smallest normal number
            sage: x.ulp() == u
            True"""
    @overload
    def ulp(self) -> Any:
        """RealDoubleElement.ulp(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 762)

        Return the unit of least precision of ``self``, which is the
        weight of the least significant bit of ``self``. This is always
        a strictly positive number. It is also the gap between this
        number and the closest number with larger absolute value that
        can be represented.

        EXAMPLES::

            sage: a = RDF(pi)                                                           # needs sage.symbolic
            sage: a.ulp()                                                               # needs sage.symbolic
            4.440892098500626e-16
            sage: b = a + a.ulp()                                                       # needs sage.symbolic

        Adding or subtracting an ulp always gives a different number::

            sage: # needs sage.symbolic
            sage: a + a.ulp() == a
            False
            sage: a - a.ulp() == a
            False
            sage: b + b.ulp() == b
            False
            sage: b - b.ulp() == b
            False

        Since the default rounding mode is round-to-nearest, adding or
        subtracting something less than half an ulp always gives the
        same number, unless the result has a smaller ulp. The latter
        can only happen if the input number is (up to sign) exactly a
        power of 2::

            sage: # needs sage.symbolic
            sage: a - a.ulp()/3 == a
            True
            sage: a + a.ulp()/3 == a
            True
            sage: b - b.ulp()/3 == b
            True
            sage: b + b.ulp()/3 == b
            True

            sage: c = RDF(1)
            sage: c - c.ulp()/3 == c
            False
            sage: c.ulp()
            2.220446049250313e-16
            sage: (c - c.ulp()).ulp()
            1.1102230246251565e-16

        The ulp is always positive::

            sage: RDF(-1).ulp()
            2.220446049250313e-16

        The ulp of zero is the smallest positive number in RDF::

            sage: RDF(0).ulp()
            5e-324
            sage: RDF(0).ulp()/2
            0.0

        Some special values::

            sage: a = RDF(1)/RDF(0); a
            +infinity
            sage: a.ulp()
            +infinity
            sage: (-a).ulp()
            +infinity
            sage: a = RDF('nan')
            sage: a.ulp() is a
            True

        The ulp method works correctly with small numbers::

            sage: u = RDF(0).ulp()
            sage: u.ulp() == u
            True
            sage: x = u * (2^52-1)  # largest denormal number
            sage: x.ulp() == u
            True
            sage: x = u * 2^52  # smallest normal number
            sage: x.ulp() == u
            True"""
    @overload
    def ulp(self) -> Any:
        """RealDoubleElement.ulp(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 762)

        Return the unit of least precision of ``self``, which is the
        weight of the least significant bit of ``self``. This is always
        a strictly positive number. It is also the gap between this
        number and the closest number with larger absolute value that
        can be represented.

        EXAMPLES::

            sage: a = RDF(pi)                                                           # needs sage.symbolic
            sage: a.ulp()                                                               # needs sage.symbolic
            4.440892098500626e-16
            sage: b = a + a.ulp()                                                       # needs sage.symbolic

        Adding or subtracting an ulp always gives a different number::

            sage: # needs sage.symbolic
            sage: a + a.ulp() == a
            False
            sage: a - a.ulp() == a
            False
            sage: b + b.ulp() == b
            False
            sage: b - b.ulp() == b
            False

        Since the default rounding mode is round-to-nearest, adding or
        subtracting something less than half an ulp always gives the
        same number, unless the result has a smaller ulp. The latter
        can only happen if the input number is (up to sign) exactly a
        power of 2::

            sage: # needs sage.symbolic
            sage: a - a.ulp()/3 == a
            True
            sage: a + a.ulp()/3 == a
            True
            sage: b - b.ulp()/3 == b
            True
            sage: b + b.ulp()/3 == b
            True

            sage: c = RDF(1)
            sage: c - c.ulp()/3 == c
            False
            sage: c.ulp()
            2.220446049250313e-16
            sage: (c - c.ulp()).ulp()
            1.1102230246251565e-16

        The ulp is always positive::

            sage: RDF(-1).ulp()
            2.220446049250313e-16

        The ulp of zero is the smallest positive number in RDF::

            sage: RDF(0).ulp()
            5e-324
            sage: RDF(0).ulp()/2
            0.0

        Some special values::

            sage: a = RDF(1)/RDF(0); a
            +infinity
            sage: a.ulp()
            +infinity
            sage: (-a).ulp()
            +infinity
            sage: a = RDF('nan')
            sage: a.ulp() is a
            True

        The ulp method works correctly with small numbers::

            sage: u = RDF(0).ulp()
            sage: u.ulp() == u
            True
            sage: x = u * (2^52-1)  # largest denormal number
            sage: x.ulp() == u
            True
            sage: x = u * 2^52  # smallest normal number
            sage: x.ulp() == u
            True"""
    @overload
    def ulp(self) -> Any:
        """RealDoubleElement.ulp(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 762)

        Return the unit of least precision of ``self``, which is the
        weight of the least significant bit of ``self``. This is always
        a strictly positive number. It is also the gap between this
        number and the closest number with larger absolute value that
        can be represented.

        EXAMPLES::

            sage: a = RDF(pi)                                                           # needs sage.symbolic
            sage: a.ulp()                                                               # needs sage.symbolic
            4.440892098500626e-16
            sage: b = a + a.ulp()                                                       # needs sage.symbolic

        Adding or subtracting an ulp always gives a different number::

            sage: # needs sage.symbolic
            sage: a + a.ulp() == a
            False
            sage: a - a.ulp() == a
            False
            sage: b + b.ulp() == b
            False
            sage: b - b.ulp() == b
            False

        Since the default rounding mode is round-to-nearest, adding or
        subtracting something less than half an ulp always gives the
        same number, unless the result has a smaller ulp. The latter
        can only happen if the input number is (up to sign) exactly a
        power of 2::

            sage: # needs sage.symbolic
            sage: a - a.ulp()/3 == a
            True
            sage: a + a.ulp()/3 == a
            True
            sage: b - b.ulp()/3 == b
            True
            sage: b + b.ulp()/3 == b
            True

            sage: c = RDF(1)
            sage: c - c.ulp()/3 == c
            False
            sage: c.ulp()
            2.220446049250313e-16
            sage: (c - c.ulp()).ulp()
            1.1102230246251565e-16

        The ulp is always positive::

            sage: RDF(-1).ulp()
            2.220446049250313e-16

        The ulp of zero is the smallest positive number in RDF::

            sage: RDF(0).ulp()
            5e-324
            sage: RDF(0).ulp()/2
            0.0

        Some special values::

            sage: a = RDF(1)/RDF(0); a
            +infinity
            sage: a.ulp()
            +infinity
            sage: (-a).ulp()
            +infinity
            sage: a = RDF('nan')
            sage: a.ulp() is a
            True

        The ulp method works correctly with small numbers::

            sage: u = RDF(0).ulp()
            sage: u.ulp() == u
            True
            sage: x = u * (2^52-1)  # largest denormal number
            sage: x.ulp() == u
            True
            sage: x = u * 2^52  # smallest normal number
            sage: x.ulp() == u
            True"""
    @overload
    def ulp(self) -> Any:
        """RealDoubleElement.ulp(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 762)

        Return the unit of least precision of ``self``, which is the
        weight of the least significant bit of ``self``. This is always
        a strictly positive number. It is also the gap between this
        number and the closest number with larger absolute value that
        can be represented.

        EXAMPLES::

            sage: a = RDF(pi)                                                           # needs sage.symbolic
            sage: a.ulp()                                                               # needs sage.symbolic
            4.440892098500626e-16
            sage: b = a + a.ulp()                                                       # needs sage.symbolic

        Adding or subtracting an ulp always gives a different number::

            sage: # needs sage.symbolic
            sage: a + a.ulp() == a
            False
            sage: a - a.ulp() == a
            False
            sage: b + b.ulp() == b
            False
            sage: b - b.ulp() == b
            False

        Since the default rounding mode is round-to-nearest, adding or
        subtracting something less than half an ulp always gives the
        same number, unless the result has a smaller ulp. The latter
        can only happen if the input number is (up to sign) exactly a
        power of 2::

            sage: # needs sage.symbolic
            sage: a - a.ulp()/3 == a
            True
            sage: a + a.ulp()/3 == a
            True
            sage: b - b.ulp()/3 == b
            True
            sage: b + b.ulp()/3 == b
            True

            sage: c = RDF(1)
            sage: c - c.ulp()/3 == c
            False
            sage: c.ulp()
            2.220446049250313e-16
            sage: (c - c.ulp()).ulp()
            1.1102230246251565e-16

        The ulp is always positive::

            sage: RDF(-1).ulp()
            2.220446049250313e-16

        The ulp of zero is the smallest positive number in RDF::

            sage: RDF(0).ulp()
            5e-324
            sage: RDF(0).ulp()/2
            0.0

        Some special values::

            sage: a = RDF(1)/RDF(0); a
            +infinity
            sage: a.ulp()
            +infinity
            sage: (-a).ulp()
            +infinity
            sage: a = RDF('nan')
            sage: a.ulp() is a
            True

        The ulp method works correctly with small numbers::

            sage: u = RDF(0).ulp()
            sage: u.ulp() == u
            True
            sage: x = u * (2^52-1)  # largest denormal number
            sage: x.ulp() == u
            True
            sage: x = u * 2^52  # smallest normal number
            sage: x.ulp() == u
            True"""
    @overload
    def ulp(self) -> Any:
        """RealDoubleElement.ulp(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 762)

        Return the unit of least precision of ``self``, which is the
        weight of the least significant bit of ``self``. This is always
        a strictly positive number. It is also the gap between this
        number and the closest number with larger absolute value that
        can be represented.

        EXAMPLES::

            sage: a = RDF(pi)                                                           # needs sage.symbolic
            sage: a.ulp()                                                               # needs sage.symbolic
            4.440892098500626e-16
            sage: b = a + a.ulp()                                                       # needs sage.symbolic

        Adding or subtracting an ulp always gives a different number::

            sage: # needs sage.symbolic
            sage: a + a.ulp() == a
            False
            sage: a - a.ulp() == a
            False
            sage: b + b.ulp() == b
            False
            sage: b - b.ulp() == b
            False

        Since the default rounding mode is round-to-nearest, adding or
        subtracting something less than half an ulp always gives the
        same number, unless the result has a smaller ulp. The latter
        can only happen if the input number is (up to sign) exactly a
        power of 2::

            sage: # needs sage.symbolic
            sage: a - a.ulp()/3 == a
            True
            sage: a + a.ulp()/3 == a
            True
            sage: b - b.ulp()/3 == b
            True
            sage: b + b.ulp()/3 == b
            True

            sage: c = RDF(1)
            sage: c - c.ulp()/3 == c
            False
            sage: c.ulp()
            2.220446049250313e-16
            sage: (c - c.ulp()).ulp()
            1.1102230246251565e-16

        The ulp is always positive::

            sage: RDF(-1).ulp()
            2.220446049250313e-16

        The ulp of zero is the smallest positive number in RDF::

            sage: RDF(0).ulp()
            5e-324
            sage: RDF(0).ulp()/2
            0.0

        Some special values::

            sage: a = RDF(1)/RDF(0); a
            +infinity
            sage: a.ulp()
            +infinity
            sage: (-a).ulp()
            +infinity
            sage: a = RDF('nan')
            sage: a.ulp() is a
            True

        The ulp method works correctly with small numbers::

            sage: u = RDF(0).ulp()
            sage: u.ulp() == u
            True
            sage: x = u * (2^52-1)  # largest denormal number
            sage: x.ulp() == u
            True
            sage: x = u * 2^52  # smallest normal number
            sage: x.ulp() == u
            True"""
    @overload
    def ulp(self) -> Any:
        """RealDoubleElement.ulp(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 762)

        Return the unit of least precision of ``self``, which is the
        weight of the least significant bit of ``self``. This is always
        a strictly positive number. It is also the gap between this
        number and the closest number with larger absolute value that
        can be represented.

        EXAMPLES::

            sage: a = RDF(pi)                                                           # needs sage.symbolic
            sage: a.ulp()                                                               # needs sage.symbolic
            4.440892098500626e-16
            sage: b = a + a.ulp()                                                       # needs sage.symbolic

        Adding or subtracting an ulp always gives a different number::

            sage: # needs sage.symbolic
            sage: a + a.ulp() == a
            False
            sage: a - a.ulp() == a
            False
            sage: b + b.ulp() == b
            False
            sage: b - b.ulp() == b
            False

        Since the default rounding mode is round-to-nearest, adding or
        subtracting something less than half an ulp always gives the
        same number, unless the result has a smaller ulp. The latter
        can only happen if the input number is (up to sign) exactly a
        power of 2::

            sage: # needs sage.symbolic
            sage: a - a.ulp()/3 == a
            True
            sage: a + a.ulp()/3 == a
            True
            sage: b - b.ulp()/3 == b
            True
            sage: b + b.ulp()/3 == b
            True

            sage: c = RDF(1)
            sage: c - c.ulp()/3 == c
            False
            sage: c.ulp()
            2.220446049250313e-16
            sage: (c - c.ulp()).ulp()
            1.1102230246251565e-16

        The ulp is always positive::

            sage: RDF(-1).ulp()
            2.220446049250313e-16

        The ulp of zero is the smallest positive number in RDF::

            sage: RDF(0).ulp()
            5e-324
            sage: RDF(0).ulp()/2
            0.0

        Some special values::

            sage: a = RDF(1)/RDF(0); a
            +infinity
            sage: a.ulp()
            +infinity
            sage: (-a).ulp()
            +infinity
            sage: a = RDF('nan')
            sage: a.ulp() is a
            True

        The ulp method works correctly with small numbers::

            sage: u = RDF(0).ulp()
            sage: u.ulp() == u
            True
            sage: x = u * (2^52-1)  # largest denormal number
            sage: x.ulp() == u
            True
            sage: x = u * 2^52  # smallest normal number
            sage: x.ulp() == u
            True"""
    @overload
    def ulp(self) -> Any:
        """RealDoubleElement.ulp(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 762)

        Return the unit of least precision of ``self``, which is the
        weight of the least significant bit of ``self``. This is always
        a strictly positive number. It is also the gap between this
        number and the closest number with larger absolute value that
        can be represented.

        EXAMPLES::

            sage: a = RDF(pi)                                                           # needs sage.symbolic
            sage: a.ulp()                                                               # needs sage.symbolic
            4.440892098500626e-16
            sage: b = a + a.ulp()                                                       # needs sage.symbolic

        Adding or subtracting an ulp always gives a different number::

            sage: # needs sage.symbolic
            sage: a + a.ulp() == a
            False
            sage: a - a.ulp() == a
            False
            sage: b + b.ulp() == b
            False
            sage: b - b.ulp() == b
            False

        Since the default rounding mode is round-to-nearest, adding or
        subtracting something less than half an ulp always gives the
        same number, unless the result has a smaller ulp. The latter
        can only happen if the input number is (up to sign) exactly a
        power of 2::

            sage: # needs sage.symbolic
            sage: a - a.ulp()/3 == a
            True
            sage: a + a.ulp()/3 == a
            True
            sage: b - b.ulp()/3 == b
            True
            sage: b + b.ulp()/3 == b
            True

            sage: c = RDF(1)
            sage: c - c.ulp()/3 == c
            False
            sage: c.ulp()
            2.220446049250313e-16
            sage: (c - c.ulp()).ulp()
            1.1102230246251565e-16

        The ulp is always positive::

            sage: RDF(-1).ulp()
            2.220446049250313e-16

        The ulp of zero is the smallest positive number in RDF::

            sage: RDF(0).ulp()
            5e-324
            sage: RDF(0).ulp()/2
            0.0

        Some special values::

            sage: a = RDF(1)/RDF(0); a
            +infinity
            sage: a.ulp()
            +infinity
            sage: (-a).ulp()
            +infinity
            sage: a = RDF('nan')
            sage: a.ulp() is a
            True

        The ulp method works correctly with small numbers::

            sage: u = RDF(0).ulp()
            sage: u.ulp() == u
            True
            sage: x = u * (2^52-1)  # largest denormal number
            sage: x.ulp() == u
            True
            sage: x = u * 2^52  # smallest normal number
            sage: x.ulp() == u
            True"""
    @overload
    def ulp(self) -> Any:
        """RealDoubleElement.ulp(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 762)

        Return the unit of least precision of ``self``, which is the
        weight of the least significant bit of ``self``. This is always
        a strictly positive number. It is also the gap between this
        number and the closest number with larger absolute value that
        can be represented.

        EXAMPLES::

            sage: a = RDF(pi)                                                           # needs sage.symbolic
            sage: a.ulp()                                                               # needs sage.symbolic
            4.440892098500626e-16
            sage: b = a + a.ulp()                                                       # needs sage.symbolic

        Adding or subtracting an ulp always gives a different number::

            sage: # needs sage.symbolic
            sage: a + a.ulp() == a
            False
            sage: a - a.ulp() == a
            False
            sage: b + b.ulp() == b
            False
            sage: b - b.ulp() == b
            False

        Since the default rounding mode is round-to-nearest, adding or
        subtracting something less than half an ulp always gives the
        same number, unless the result has a smaller ulp. The latter
        can only happen if the input number is (up to sign) exactly a
        power of 2::

            sage: # needs sage.symbolic
            sage: a - a.ulp()/3 == a
            True
            sage: a + a.ulp()/3 == a
            True
            sage: b - b.ulp()/3 == b
            True
            sage: b + b.ulp()/3 == b
            True

            sage: c = RDF(1)
            sage: c - c.ulp()/3 == c
            False
            sage: c.ulp()
            2.220446049250313e-16
            sage: (c - c.ulp()).ulp()
            1.1102230246251565e-16

        The ulp is always positive::

            sage: RDF(-1).ulp()
            2.220446049250313e-16

        The ulp of zero is the smallest positive number in RDF::

            sage: RDF(0).ulp()
            5e-324
            sage: RDF(0).ulp()/2
            0.0

        Some special values::

            sage: a = RDF(1)/RDF(0); a
            +infinity
            sage: a.ulp()
            +infinity
            sage: (-a).ulp()
            +infinity
            sage: a = RDF('nan')
            sage: a.ulp() is a
            True

        The ulp method works correctly with small numbers::

            sage: u = RDF(0).ulp()
            sage: u.ulp() == u
            True
            sage: x = u * (2^52-1)  # largest denormal number
            sage: x.ulp() == u
            True
            sage: x = u * 2^52  # smallest normal number
            sage: x.ulp() == u
            True"""
    @overload
    def ulp(self) -> Any:
        """RealDoubleElement.ulp(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 762)

        Return the unit of least precision of ``self``, which is the
        weight of the least significant bit of ``self``. This is always
        a strictly positive number. It is also the gap between this
        number and the closest number with larger absolute value that
        can be represented.

        EXAMPLES::

            sage: a = RDF(pi)                                                           # needs sage.symbolic
            sage: a.ulp()                                                               # needs sage.symbolic
            4.440892098500626e-16
            sage: b = a + a.ulp()                                                       # needs sage.symbolic

        Adding or subtracting an ulp always gives a different number::

            sage: # needs sage.symbolic
            sage: a + a.ulp() == a
            False
            sage: a - a.ulp() == a
            False
            sage: b + b.ulp() == b
            False
            sage: b - b.ulp() == b
            False

        Since the default rounding mode is round-to-nearest, adding or
        subtracting something less than half an ulp always gives the
        same number, unless the result has a smaller ulp. The latter
        can only happen if the input number is (up to sign) exactly a
        power of 2::

            sage: # needs sage.symbolic
            sage: a - a.ulp()/3 == a
            True
            sage: a + a.ulp()/3 == a
            True
            sage: b - b.ulp()/3 == b
            True
            sage: b + b.ulp()/3 == b
            True

            sage: c = RDF(1)
            sage: c - c.ulp()/3 == c
            False
            sage: c.ulp()
            2.220446049250313e-16
            sage: (c - c.ulp()).ulp()
            1.1102230246251565e-16

        The ulp is always positive::

            sage: RDF(-1).ulp()
            2.220446049250313e-16

        The ulp of zero is the smallest positive number in RDF::

            sage: RDF(0).ulp()
            5e-324
            sage: RDF(0).ulp()/2
            0.0

        Some special values::

            sage: a = RDF(1)/RDF(0); a
            +infinity
            sage: a.ulp()
            +infinity
            sage: (-a).ulp()
            +infinity
            sage: a = RDF('nan')
            sage: a.ulp() is a
            True

        The ulp method works correctly with small numbers::

            sage: u = RDF(0).ulp()
            sage: u.ulp() == u
            True
            sage: x = u * (2^52-1)  # largest denormal number
            sage: x.ulp() == u
            True
            sage: x = u * 2^52  # smallest normal number
            sage: x.ulp() == u
            True"""
    @overload
    def ulp(self) -> Any:
        """RealDoubleElement.ulp(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 762)

        Return the unit of least precision of ``self``, which is the
        weight of the least significant bit of ``self``. This is always
        a strictly positive number. It is also the gap between this
        number and the closest number with larger absolute value that
        can be represented.

        EXAMPLES::

            sage: a = RDF(pi)                                                           # needs sage.symbolic
            sage: a.ulp()                                                               # needs sage.symbolic
            4.440892098500626e-16
            sage: b = a + a.ulp()                                                       # needs sage.symbolic

        Adding or subtracting an ulp always gives a different number::

            sage: # needs sage.symbolic
            sage: a + a.ulp() == a
            False
            sage: a - a.ulp() == a
            False
            sage: b + b.ulp() == b
            False
            sage: b - b.ulp() == b
            False

        Since the default rounding mode is round-to-nearest, adding or
        subtracting something less than half an ulp always gives the
        same number, unless the result has a smaller ulp. The latter
        can only happen if the input number is (up to sign) exactly a
        power of 2::

            sage: # needs sage.symbolic
            sage: a - a.ulp()/3 == a
            True
            sage: a + a.ulp()/3 == a
            True
            sage: b - b.ulp()/3 == b
            True
            sage: b + b.ulp()/3 == b
            True

            sage: c = RDF(1)
            sage: c - c.ulp()/3 == c
            False
            sage: c.ulp()
            2.220446049250313e-16
            sage: (c - c.ulp()).ulp()
            1.1102230246251565e-16

        The ulp is always positive::

            sage: RDF(-1).ulp()
            2.220446049250313e-16

        The ulp of zero is the smallest positive number in RDF::

            sage: RDF(0).ulp()
            5e-324
            sage: RDF(0).ulp()/2
            0.0

        Some special values::

            sage: a = RDF(1)/RDF(0); a
            +infinity
            sage: a.ulp()
            +infinity
            sage: (-a).ulp()
            +infinity
            sage: a = RDF('nan')
            sage: a.ulp() is a
            True

        The ulp method works correctly with small numbers::

            sage: u = RDF(0).ulp()
            sage: u.ulp() == u
            True
            sage: x = u * (2^52-1)  # largest denormal number
            sage: x.ulp() == u
            True
            sage: x = u * 2^52  # smallest normal number
            sage: x.ulp() == u
            True"""
    @overload
    def ulp(self) -> Any:
        """RealDoubleElement.ulp(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 762)

        Return the unit of least precision of ``self``, which is the
        weight of the least significant bit of ``self``. This is always
        a strictly positive number. It is also the gap between this
        number and the closest number with larger absolute value that
        can be represented.

        EXAMPLES::

            sage: a = RDF(pi)                                                           # needs sage.symbolic
            sage: a.ulp()                                                               # needs sage.symbolic
            4.440892098500626e-16
            sage: b = a + a.ulp()                                                       # needs sage.symbolic

        Adding or subtracting an ulp always gives a different number::

            sage: # needs sage.symbolic
            sage: a + a.ulp() == a
            False
            sage: a - a.ulp() == a
            False
            sage: b + b.ulp() == b
            False
            sage: b - b.ulp() == b
            False

        Since the default rounding mode is round-to-nearest, adding or
        subtracting something less than half an ulp always gives the
        same number, unless the result has a smaller ulp. The latter
        can only happen if the input number is (up to sign) exactly a
        power of 2::

            sage: # needs sage.symbolic
            sage: a - a.ulp()/3 == a
            True
            sage: a + a.ulp()/3 == a
            True
            sage: b - b.ulp()/3 == b
            True
            sage: b + b.ulp()/3 == b
            True

            sage: c = RDF(1)
            sage: c - c.ulp()/3 == c
            False
            sage: c.ulp()
            2.220446049250313e-16
            sage: (c - c.ulp()).ulp()
            1.1102230246251565e-16

        The ulp is always positive::

            sage: RDF(-1).ulp()
            2.220446049250313e-16

        The ulp of zero is the smallest positive number in RDF::

            sage: RDF(0).ulp()
            5e-324
            sage: RDF(0).ulp()/2
            0.0

        Some special values::

            sage: a = RDF(1)/RDF(0); a
            +infinity
            sage: a.ulp()
            +infinity
            sage: (-a).ulp()
            +infinity
            sage: a = RDF('nan')
            sage: a.ulp() is a
            True

        The ulp method works correctly with small numbers::

            sage: u = RDF(0).ulp()
            sage: u.ulp() == u
            True
            sage: x = u * (2^52-1)  # largest denormal number
            sage: x.ulp() == u
            True
            sage: x = u * 2^52  # smallest normal number
            sage: x.ulp() == u
            True"""
    def __abs__(self) -> Any:
        """RealDoubleElement.__abs__(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1390)

        Return the absolute value of ``self``.

        EXAMPLES::

            sage: abs(RDF(1.5))
            1.5
            sage: abs(RDF(-1.5))
            1.5
            sage: abs(RDF(0.0))
            0.0
            sage: abs(RDF(-0.0))
            0.0"""
    def __complex__(self) -> Any:
        """RealDoubleElement.__complex__(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 890)

        Return ``self`` as a python complex number.

        EXAMPLES::

            sage: a = 2303
            sage: RDF(a)
            2303.0
            sage: complex(RDF(a))
            (2303+0j)"""
    @overload
    def __copy__(self) -> Any:
        """RealDoubleElement.__copy__(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1185)

        Return copy of ``self``, which since ``self`` is immutable, is just
        ``self``.

        EXAMPLES::

            sage: r = RDF('-1.6')
            sage: r.__copy__() is r
            True"""
    @overload
    def __copy__(self) -> Any:
        """RealDoubleElement.__copy__(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1185)

        Return copy of ``self``, which since ``self`` is immutable, is just
        ``self``.

        EXAMPLES::

            sage: r = RDF('-1.6')
            sage: r.__copy__() is r
            True"""
    def __deepcopy__(self, memo) -> Any:
        """RealDoubleElement.__deepcopy__(self, memo)

        File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1198)

        EXAMPLES::

            sage: r = RDF('-1.6')
            sage: deepcopy(r) is r
            True"""
    def __float__(self) -> Any:
        """RealDoubleElement.__float__(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1588)

        Return ``self`` as a python float.

        EXAMPLES::

            sage: float(RDF(1.5))
            1.5
            sage: type(float(RDF(1.5)))
            <... 'float'>"""
    def __format__(self, format_spec) -> Any:
        """RealDoubleElement.__format__(self, format_spec)

        File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1095)

        Return a formatted string representation of this real number.

        EXAMPLES::

            sage: format(RDF(32/3), '.4f')
            '10.6667'
            sage: '{:.4e}'.format(RDF(2/3))
            '6.6667e-01'"""
    def __hash__(self) -> Any:
        """RealDoubleElement.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1128)

        Return the hash of ``self``, which coincides with the python float
        (and often int) type.

        EXAMPLES::

            sage: hash(RDF(1.2)) == hash(1.2r)
            True"""
    def __int__(self) -> Any:
        """RealDoubleElement.__int__(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1616)

        Return integer truncation of this real number.

        EXAMPLES::

            sage: int(RDF(2.99))
            2
            sage: int(RDF(-2.99))
            -2"""
    @overload
    def __invert__(self) -> Any:
        """RealDoubleElement.__invert__(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1295)

        Compute the multiplicative inverse of ``self``.

        EXAMPLES::

            sage: a = RDF(-1.5)*RDF(2.5)
            sage: a.__invert__()
            -0.26666666666666666
            sage: ~a
            -0.26666666666666666"""
    @overload
    def __invert__(self) -> Any:
        """RealDoubleElement.__invert__(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1295)

        Compute the multiplicative inverse of ``self``.

        EXAMPLES::

            sage: a = RDF(-1.5)*RDF(2.5)
            sage: a.__invert__()
            -0.26666666666666666
            sage: ~a
            -0.26666666666666666"""
    def __lshift__(self, x, y) -> Any:
        """RealDoubleElement.__lshift__(x, y)

        File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1427)

        LShifting a double is not supported; nor is lshifting a
        :class:`RealDoubleElement`.

        TESTS::

            sage: RDF(2) << 3
            Traceback (most recent call last):
            ...
            TypeError: unsupported operand type(s) for <<"""
    @overload
    def __mpfr__(self) -> Any:
        '''RealDoubleElement.__mpfr__(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 932)

        Convert Sage ``RealDoubleElement`` to gmpy2 ``mpfr``.

        EXAMPLES::

            sage: RDF(42.2).__mpfr__()
            mpfr(\'42.200000000000003\')
            sage: from gmpy2 import mpfr
            sage: mpfr(RDF(5.1))
            mpfr(\'5.0999999999999996\')

        TESTS::

            sage: RDF().__mpfr__(); raise NotImplementedError("gmpy2 is not installed")
            Traceback (most recent call last):
            ...
            NotImplementedError: gmpy2 is not installed'''
    @overload
    def __mpfr__(self) -> Any:
        '''RealDoubleElement.__mpfr__(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 932)

        Convert Sage ``RealDoubleElement`` to gmpy2 ``mpfr``.

        EXAMPLES::

            sage: RDF(42.2).__mpfr__()
            mpfr(\'42.200000000000003\')
            sage: from gmpy2 import mpfr
            sage: mpfr(RDF(5.1))
            mpfr(\'5.0999999999999996\')

        TESTS::

            sage: RDF().__mpfr__(); raise NotImplementedError("gmpy2 is not installed")
            Traceback (most recent call last):
            ...
            NotImplementedError: gmpy2 is not installed'''
    @overload
    def __mpfr__(self) -> Any:
        '''RealDoubleElement.__mpfr__(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 932)

        Convert Sage ``RealDoubleElement`` to gmpy2 ``mpfr``.

        EXAMPLES::

            sage: RDF(42.2).__mpfr__()
            mpfr(\'42.200000000000003\')
            sage: from gmpy2 import mpfr
            sage: mpfr(RDF(5.1))
            mpfr(\'5.0999999999999996\')

        TESTS::

            sage: RDF().__mpfr__(); raise NotImplementedError("gmpy2 is not installed")
            Traceback (most recent call last):
            ...
            NotImplementedError: gmpy2 is not installed'''
    def __neg__(self) -> Any:
        """RealDoubleElement.__neg__(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1365)

        Negate ``self``.

        EXAMPLES::

            sage: -RDF('-1.5')
            1.5"""
    @overload
    def __pari__(self) -> Any:
        """RealDoubleElement.__pari__(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1662)

        Return a PARI representation of ``self``.

        EXAMPLES::

            sage: RDF(1.5).__pari__()                                                   # needs sage.libs.pari
            1.50000000000000"""
    @overload
    def __pari__(self) -> Any:
        """RealDoubleElement.__pari__(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1662)

        Return a PARI representation of ``self``.

        EXAMPLES::

            sage: RDF(1.5).__pari__()                                                   # needs sage.libs.pari
            1.50000000000000"""
    def __reduce__(self) -> Any:
        """RealDoubleElement.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 731)

        For pickling.

        EXAMPLES::

            sage: a = RDF(-2.7)
            sage: loads(dumps(a)) == a
            True"""
    def __rlshift__(self, other):
        """Return value<<self."""
    def __rrshift__(self, other):
        """Return value>>self."""
    def __rshift__(self, x, y) -> Any:
        """RealDoubleElement.__rshift__(x, y)

        File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1441)

        RShifting a double is not supported; nor is rshifting a
        :class:`RealDoubleElement`.

        TESTS::

            sage: RDF(2) >> 3
            Traceback (most recent call last):
            ...
            TypeError: unsupported operand type(s) for >>"""

class RealDoubleField_class(sage.rings.abc.RealDoubleField):
    """RealDoubleField_class()

    File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 72)

    An approximation to the field of real numbers using double
    precision floating point numbers. Answers derived from calculations
    in this approximation may differ from what they would be if those
    calculations were performed in the true field of real numbers. This
    is due to the rounding errors inherent to finite precision
    calculations.

    EXAMPLES::

        sage: RR == RDF                                                                 # needs sage.rings.real_mpfr
        False
        sage: RDF == RealDoubleField()    # RDF is the shorthand
        True

    ::

        sage: RDF(1)
        1.0
        sage: RDF(2/3)
        0.6666666666666666

    A :exc:`TypeError` is raised if the coercion doesn't make sense::

        sage: RDF(QQ['x'].0)
        Traceback (most recent call last):
        ...
        TypeError: cannot convert nonconstant polynomial
        sage: RDF(QQ['x'](3))
        3.0

    One can convert back and forth between double precision real
    numbers and higher-precision ones, though of course there may be
    loss of precision::

        sage: # needs sage.rings.real_mpfr
        sage: a = RealField(200)(2).sqrt(); a
        1.4142135623730950488016887242096980785696718753769480731767
        sage: b = RDF(a); b
        1.4142135623730951
        sage: a.parent()(b)
        1.4142135623730951454746218587388284504413604736328125000000
        sage: a.parent()(b) == b
        True
        sage: b == RR(a)
        True

    TESTS::

        sage: RDF.is_finite()
        False"""

    class _element_constructor_(sage.structure.element.FieldElement):
        """RealDoubleElement(x)

        File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 675)

        An approximation to a real number using double precision floating
        point numbers. Answers derived from calculations with such
        approximations may differ from what they would be if those
        calculations were performed with true real numbers. This is due to
        the rounding errors inherent to finite precision calculations."""
        __array_interface__: ClassVar[dict] = ...
        __pyx_vtable__: ClassVar[PyCapsule] = ...
        def __init__(self, *args, **kwargs) -> None:
            """File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 697)

                    Create a new ``RealDoubleElement`` with value ``x``.

                    EXAMPLES::

                        sage: RDF(10^100)
                        1e+100

                    TESTS::

                        sage: from gmpy2 import *
                        sage: RDF(mpz(42))
                        42.0
                        sage: RDF(mpq(3/4))
                        0.75
                        sage: RDF(mpq('4.1'))
                        4.1
        """
        @overload
        def NaN(self) -> Any:
            """RealDoubleElement.NaN(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1786)

            Return Not-a-Number ``NaN``.

            EXAMPLES::

                sage: RDF.NaN()
                NaN"""
        @overload
        def NaN(self) -> Any:
            """RealDoubleElement.NaN(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1786)

            Return Not-a-Number ``NaN``.

            EXAMPLES::

                sage: RDF.NaN()
                NaN"""
        @overload
        def abs(self) -> RealDoubleElement:
            """RealDoubleElement.abs(self) -> RealDoubleElement

            File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1411)

            Return the absolute value of ``self``.

            EXAMPLES::

                sage: RDF(1e10).abs()
                10000000000.0
                sage: RDF(-1e10).abs()
                10000000000.0"""
        @overload
        def abs(self) -> Any:
            """RealDoubleElement.abs(self) -> RealDoubleElement

            File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1411)

            Return the absolute value of ``self``.

            EXAMPLES::

                sage: RDF(1e10).abs()
                10000000000.0
                sage: RDF(-1e10).abs()
                10000000000.0"""
        @overload
        def abs(self) -> Any:
            """RealDoubleElement.abs(self) -> RealDoubleElement

            File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1411)

            Return the absolute value of ``self``.

            EXAMPLES::

                sage: RDF(1e10).abs()
                10000000000.0
                sage: RDF(-1e10).abs()
                10000000000.0"""
        @overload
        def agm(self, other) -> Any:
            """RealDoubleElement.agm(self, other)

            File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1901)

            Return the arithmetic-geometric mean of ``self`` and ``other``. The
            arithmetic-geometric mean is the common limit of the sequences
            `u_n` and `v_n`, where `u_0` is ``self``,
            `v_0` is other, `u_{n+1}` is the arithmetic mean
            of `u_n` and `v_n`, and `v_{n+1}` is the
            geometric mean of `u_n` and `v_n`. If any operand is negative, the
            return value is ``NaN``.

            EXAMPLES::

                sage: a = RDF(1.5)
                sage: b = RDF(2.3)
                sage: a.agm(b)
                1.8786484558146697

            The arithmetic-geometric mean always lies between the geometric and
            arithmetic mean::

                sage: sqrt(a*b) < a.agm(b) < (a+b)/2
                True"""
        @overload
        def agm(self, b) -> Any:
            """RealDoubleElement.agm(self, other)

            File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1901)

            Return the arithmetic-geometric mean of ``self`` and ``other``. The
            arithmetic-geometric mean is the common limit of the sequences
            `u_n` and `v_n`, where `u_0` is ``self``,
            `v_0` is other, `u_{n+1}` is the arithmetic mean
            of `u_n` and `v_n`, and `v_{n+1}` is the
            geometric mean of `u_n` and `v_n`. If any operand is negative, the
            return value is ``NaN``.

            EXAMPLES::

                sage: a = RDF(1.5)
                sage: b = RDF(2.3)
                sage: a.agm(b)
                1.8786484558146697

            The arithmetic-geometric mean always lies between the geometric and
            arithmetic mean::

                sage: sqrt(a*b) < a.agm(b) < (a+b)/2
                True"""
        @overload
        def agm(self, b) -> Any:
            """RealDoubleElement.agm(self, other)

            File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1901)

            Return the arithmetic-geometric mean of ``self`` and ``other``. The
            arithmetic-geometric mean is the common limit of the sequences
            `u_n` and `v_n`, where `u_0` is ``self``,
            `v_0` is other, `u_{n+1}` is the arithmetic mean
            of `u_n` and `v_n`, and `v_{n+1}` is the
            geometric mean of `u_n` and `v_n`. If any operand is negative, the
            return value is ``NaN``.

            EXAMPLES::

                sage: a = RDF(1.5)
                sage: b = RDF(2.3)
                sage: a.agm(b)
                1.8786484558146697

            The arithmetic-geometric mean always lies between the geometric and
            arithmetic mean::

                sage: sqrt(a*b) < a.agm(b) < (a+b)/2
                True"""
        def algdep(self, *args, **kwargs):
            """RealDoubleElement.algebraic_dependency(self, n)

            File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1936)

            Return a polynomial of degree at most `n` which is
            approximately satisfied by this number.

            .. NOTE::

                The resulting polynomial need not be irreducible, and indeed
                usually won't be if this number is a good approximation to an
                algebraic number of degree less than `n`.

            ALGORITHM:

            Uses the PARI C-library :pari:`algdep` command.

            EXAMPLES::

                sage: r = sqrt(RDF(2)); r
                1.4142135623730951
                sage: r.algebraic_dependency(5)                                             # needs sage.libs.pari
                x^2 - 2"""
        def algebraic_dependency(self, n) -> Any:
            """RealDoubleElement.algebraic_dependency(self, n)

            File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1936)

            Return a polynomial of degree at most `n` which is
            approximately satisfied by this number.

            .. NOTE::

                The resulting polynomial need not be irreducible, and indeed
                usually won't be if this number is a good approximation to an
                algebraic number of degree less than `n`.

            ALGORITHM:

            Uses the PARI C-library :pari:`algdep` command.

            EXAMPLES::

                sage: r = sqrt(RDF(2)); r
                1.4142135623730951
                sage: r.algebraic_dependency(5)                                             # needs sage.libs.pari
                x^2 - 2"""
        @overload
        def as_integer_ratio(self) -> Any:
            """RealDoubleElement.as_integer_ratio(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1273)

            Return a coprime pair of integers ``(a, b)`` such that ``self``
            equals ``a / b`` exactly.

            EXAMPLES::

                sage: RDF(0).as_integer_ratio()
                (0, 1)
                sage: RDF(1/3).as_integer_ratio()
                (6004799503160661, 18014398509481984)
                sage: RDF(37/16).as_integer_ratio()
                (37, 16)
                sage: RDF(3^60).as_integer_ratio()
                (42391158275216203520420085760, 1)"""
        @overload
        def as_integer_ratio(self) -> Any:
            """RealDoubleElement.as_integer_ratio(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1273)

            Return a coprime pair of integers ``(a, b)`` such that ``self``
            equals ``a / b`` exactly.

            EXAMPLES::

                sage: RDF(0).as_integer_ratio()
                (0, 1)
                sage: RDF(1/3).as_integer_ratio()
                (6004799503160661, 18014398509481984)
                sage: RDF(37/16).as_integer_ratio()
                (37, 16)
                sage: RDF(3^60).as_integer_ratio()
                (42391158275216203520420085760, 1)"""
        @overload
        def as_integer_ratio(self) -> Any:
            """RealDoubleElement.as_integer_ratio(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1273)

            Return a coprime pair of integers ``(a, b)`` such that ``self``
            equals ``a / b`` exactly.

            EXAMPLES::

                sage: RDF(0).as_integer_ratio()
                (0, 1)
                sage: RDF(1/3).as_integer_ratio()
                (6004799503160661, 18014398509481984)
                sage: RDF(37/16).as_integer_ratio()
                (37, 16)
                sage: RDF(3^60).as_integer_ratio()
                (42391158275216203520420085760, 1)"""
        @overload
        def as_integer_ratio(self) -> Any:
            """RealDoubleElement.as_integer_ratio(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1273)

            Return a coprime pair of integers ``(a, b)`` such that ``self``
            equals ``a / b`` exactly.

            EXAMPLES::

                sage: RDF(0).as_integer_ratio()
                (0, 1)
                sage: RDF(1/3).as_integer_ratio()
                (6004799503160661, 18014398509481984)
                sage: RDF(37/16).as_integer_ratio()
                (37, 16)
                sage: RDF(3^60).as_integer_ratio()
                (42391158275216203520420085760, 1)"""
        @overload
        def as_integer_ratio(self) -> Any:
            """RealDoubleElement.as_integer_ratio(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1273)

            Return a coprime pair of integers ``(a, b)`` such that ``self``
            equals ``a / b`` exactly.

            EXAMPLES::

                sage: RDF(0).as_integer_ratio()
                (0, 1)
                sage: RDF(1/3).as_integer_ratio()
                (6004799503160661, 18014398509481984)
                sage: RDF(37/16).as_integer_ratio()
                (37, 16)
                sage: RDF(3^60).as_integer_ratio()
                (42391158275216203520420085760, 1)"""
        @overload
        def ceil(self) -> Any:
            """RealDoubleElement.ceil(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1536)

            Return the ceiling of ``self``.

            EXAMPLES::

                sage: RDF(2.99).ceil()
                3
                sage: RDF(2.00).ceil()
                2
                sage: RDF(-5/2).ceil()
                -2"""
        @overload
        def ceil(self) -> Any:
            """RealDoubleElement.ceil(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1536)

            Return the ceiling of ``self``.

            EXAMPLES::

                sage: RDF(2.99).ceil()
                3
                sage: RDF(2.00).ceil()
                2
                sage: RDF(-5/2).ceil()
                -2"""
        @overload
        def ceil(self) -> Any:
            """RealDoubleElement.ceil(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1536)

            Return the ceiling of ``self``.

            EXAMPLES::

                sage: RDF(2.99).ceil()
                3
                sage: RDF(2.00).ceil()
                2
                sage: RDF(-5/2).ceil()
                -2"""
        @overload
        def ceil(self) -> Any:
            """RealDoubleElement.ceil(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1536)

            Return the ceiling of ``self``.

            EXAMPLES::

                sage: RDF(2.99).ceil()
                3
                sage: RDF(2.00).ceil()
                2
                sage: RDF(-5/2).ceil()
                -2"""
        def ceiling(self, *args, **kwargs):
            """RealDoubleElement.ceil(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1536)

            Return the ceiling of ``self``.

            EXAMPLES::

                sage: RDF(2.99).ceil()
                3
                sage: RDF(2.00).ceil()
                2
                sage: RDF(-5/2).ceil()
                -2"""
        @overload
        def conjugate(self) -> Any:
            """RealDoubleElement.conjugate(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1378)

            Return the complex conjugate of this real number, which is
            the real number itself.

            EXAMPLES::

                sage: RDF(4).conjugate()
                4.0"""
        @overload
        def conjugate(self) -> Any:
            """RealDoubleElement.conjugate(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1378)

            Return the complex conjugate of this real number, which is
            the real number itself.

            EXAMPLES::

                sage: RDF(4).conjugate()
                4.0"""
        @overload
        def cube_root(self) -> Any:
            """RealDoubleElement.cube_root(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1887)

            Return the cubic root (defined over the real numbers) of ``self``.

            EXAMPLES::

                sage: r = RDF(125.0); r.cube_root()
                5.000000000000001
                sage: r = RDF(-119.0)
                sage: r.cube_root()^3 - r  # rel tol 1
                -1.4210854715202004e-14"""
        @overload
        def cube_root(self) -> Any:
            """RealDoubleElement.cube_root(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1887)

            Return the cubic root (defined over the real numbers) of ``self``.

            EXAMPLES::

                sage: r = RDF(125.0); r.cube_root()
                5.000000000000001
                sage: r = RDF(-119.0)
                sage: r.cube_root()^3 - r  # rel tol 1
                -1.4210854715202004e-14"""
        @overload
        def cube_root(self) -> Any:
            """RealDoubleElement.cube_root(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1887)

            Return the cubic root (defined over the real numbers) of ``self``.

            EXAMPLES::

                sage: r = RDF(125.0); r.cube_root()
                5.000000000000001
                sage: r = RDF(-119.0)
                sage: r.cube_root()^3 - r  # rel tol 1
                -1.4210854715202004e-14"""
        @overload
        def floor(self) -> Any:
            """RealDoubleElement.floor(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1521)

            Return the floor of ``self``.

            EXAMPLES::

                sage: RDF(2.99).floor()
                2
                sage: RDF(2.00).floor()
                2
                sage: RDF(-5/2).floor()
                -3"""
        @overload
        def floor(self) -> Any:
            """RealDoubleElement.floor(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1521)

            Return the floor of ``self``.

            EXAMPLES::

                sage: RDF(2.99).floor()
                2
                sage: RDF(2.00).floor()
                2
                sage: RDF(-5/2).floor()
                -3"""
        @overload
        def floor(self) -> Any:
            """RealDoubleElement.floor(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1521)

            Return the floor of ``self``.

            EXAMPLES::

                sage: RDF(2.99).floor()
                2
                sage: RDF(2.00).floor()
                2
                sage: RDF(-5/2).floor()
                -3"""
        @overload
        def floor(self) -> Any:
            """RealDoubleElement.floor(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1521)

            Return the floor of ``self``.

            EXAMPLES::

                sage: RDF(2.99).floor()
                2
                sage: RDF(2.00).floor()
                2
                sage: RDF(-5/2).floor()
                -3"""
        @overload
        def frac(self) -> Any:
            """RealDoubleElement.frac(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1568)

            Return a real number in `(-1, 1)`. It satisfies the relation:
            ``x = x.trunc() + x.frac()``

            EXAMPLES::

                sage: RDF(2.99).frac()
                0.9900000000000002
                sage: RDF(2.50).frac()
                0.5
                sage: RDF(-2.79).frac()
                -0.79"""
        @overload
        def frac(self) -> Any:
            """RealDoubleElement.frac(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1568)

            Return a real number in `(-1, 1)`. It satisfies the relation:
            ``x = x.trunc() + x.frac()``

            EXAMPLES::

                sage: RDF(2.99).frac()
                0.9900000000000002
                sage: RDF(2.50).frac()
                0.5
                sage: RDF(-2.79).frac()
                -0.79"""
        @overload
        def frac(self) -> Any:
            """RealDoubleElement.frac(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1568)

            Return a real number in `(-1, 1)`. It satisfies the relation:
            ``x = x.trunc() + x.frac()``

            EXAMPLES::

                sage: RDF(2.99).frac()
                0.9900000000000002
                sage: RDF(2.50).frac()
                0.5
                sage: RDF(-2.79).frac()
                -0.79"""
        @overload
        def frac(self) -> Any:
            """RealDoubleElement.frac(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1568)

            Return a real number in `(-1, 1)`. It satisfies the relation:
            ``x = x.trunc() + x.frac()``

            EXAMPLES::

                sage: RDF(2.99).frac()
                0.9900000000000002
                sage: RDF(2.50).frac()
                0.5
                sage: RDF(-2.79).frac()
                -0.79"""
        @overload
        def frac(self) -> Any:
            """RealDoubleElement.frac(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1568)

            Return a real number in `(-1, 1)`. It satisfies the relation:
            ``x = x.trunc() + x.frac()``

            EXAMPLES::

                sage: RDF(2.99).frac()
                0.9900000000000002
                sage: RDF(2.50).frac()
                0.5
                sage: RDF(-2.79).frac()
                -0.79"""
        @overload
        def imag(self) -> Any:
            """RealDoubleElement.imag(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 878)

            Return the imaginary part of this number, which is zero.

            EXAMPLES::

                sage: a = RDF(3)
                sage: a.imag()
                0.0"""
        @overload
        def imag(self) -> Any:
            """RealDoubleElement.imag(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 878)

            Return the imaginary part of this number, which is zero.

            EXAMPLES::

                sage: a = RDF(3)
                sage: a.imag()
                0.0"""
        @overload
        def integer_part(self) -> Any:
            """RealDoubleElement.integer_part(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1208)

            If in decimal this number is written ``n.defg``, returns ``n``.

            EXAMPLES::

                sage: r = RDF('-1.6')
                sage: a = r.integer_part(); a
                -1
                sage: type(a)
                <class 'sage.rings.integer.Integer'>
                sage: r = RDF(0.0/0.0)
                sage: a = r.integer_part()
                Traceback (most recent call last):
                ...
                TypeError: Attempt to get integer part of NaN"""
        @overload
        def integer_part(self) -> Any:
            """RealDoubleElement.integer_part(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1208)

            If in decimal this number is written ``n.defg``, returns ``n``.

            EXAMPLES::

                sage: r = RDF('-1.6')
                sage: a = r.integer_part(); a
                -1
                sage: type(a)
                <class 'sage.rings.integer.Integer'>
                sage: r = RDF(0.0/0.0)
                sage: a = r.integer_part()
                Traceback (most recent call last):
                ...
                TypeError: Attempt to get integer part of NaN"""
        @overload
        def integer_part(self) -> Any:
            """RealDoubleElement.integer_part(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1208)

            If in decimal this number is written ``n.defg``, returns ``n``.

            EXAMPLES::

                sage: r = RDF('-1.6')
                sage: a = r.integer_part(); a
                -1
                sage: type(a)
                <class 'sage.rings.integer.Integer'>
                sage: r = RDF(0.0/0.0)
                sage: a = r.integer_part()
                Traceback (most recent call last):
                ...
                TypeError: Attempt to get integer part of NaN"""
        @overload
        def is_NaN(self) -> Any:
            """RealDoubleElement.is_NaN(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1680)

            Check if ``self`` is ``NaN``.

            EXAMPLES::

                sage: RDF(1).is_NaN()
                False
                sage: a = RDF(0)/RDF(0)
                sage: a.is_NaN()
                True"""
        @overload
        def is_NaN(self) -> Any:
            """RealDoubleElement.is_NaN(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1680)

            Check if ``self`` is ``NaN``.

            EXAMPLES::

                sage: RDF(1).is_NaN()
                False
                sage: a = RDF(0)/RDF(0)
                sage: a.is_NaN()
                True"""
        @overload
        def is_NaN(self) -> Any:
            """RealDoubleElement.is_NaN(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1680)

            Check if ``self`` is ``NaN``.

            EXAMPLES::

                sage: RDF(1).is_NaN()
                False
                sage: a = RDF(0)/RDF(0)
                sage: a.is_NaN()
                True"""
        def is_infinity(self) -> Any:
            """RealDoubleElement.is_infinity(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1728)

            Check if ``self`` is `\\infty`.

            EXAMPLES::

                sage: a = RDF(2); b = RDF(0)
                sage: (a/b).is_infinity()
                True
                sage: (b/a).is_infinity()
                False"""
        @overload
        def is_integer(self) -> Any:
            """RealDoubleElement.is_integer(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1874)

            Return ``True`` if this number is a integer.

            EXAMPLES::

                sage: RDF(3.5).is_integer()
                False
                sage: RDF(3).is_integer()
                True"""
        @overload
        def is_integer(self) -> Any:
            """RealDoubleElement.is_integer(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1874)

            Return ``True`` if this number is a integer.

            EXAMPLES::

                sage: RDF(3.5).is_integer()
                False
                sage: RDF(3).is_integer()
                True"""
        @overload
        def is_integer(self) -> Any:
            """RealDoubleElement.is_integer(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1874)

            Return ``True`` if this number is a integer.

            EXAMPLES::

                sage: RDF(3.5).is_integer()
                False
                sage: RDF(3).is_integer()
                True"""
        def is_negative_infinity(self) -> Any:
            """RealDoubleElement.is_negative_infinity(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1711)

            Check if ``self`` is `-\\infty`.

            EXAMPLES::

                sage: a = RDF(2)/RDF(0)
                sage: a.is_negative_infinity()
                False
                sage: a = RDF(-3)/RDF(0)
                sage: a.is_negative_infinity()
                True"""
        def is_positive_infinity(self) -> Any:
            """RealDoubleElement.is_positive_infinity(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1694)

            Check if ``self`` is `+\\infty`.

            EXAMPLES::

                sage: a = RDF(1)/RDF(0)
                sage: a.is_positive_infinity()
                True
                sage: a = RDF(-1)/RDF(0)
                sage: a.is_positive_infinity()
                False"""
        @overload
        def is_square(self) -> Any:
            """RealDoubleElement.is_square(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1857)

            Return whether or not this number is a square in this field. For
            the real numbers, this is ``True`` if and only if ``self`` is
            nonnegative.

            EXAMPLES::

                sage: RDF(3.5).is_square()
                True
                sage: RDF(0).is_square()
                True
                sage: RDF(-4).is_square()
                False"""
        @overload
        def is_square(self) -> Any:
            """RealDoubleElement.is_square(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1857)

            Return whether or not this number is a square in this field. For
            the real numbers, this is ``True`` if and only if ``self`` is
            nonnegative.

            EXAMPLES::

                sage: RDF(3.5).is_square()
                True
                sage: RDF(0).is_square()
                True
                sage: RDF(-4).is_square()
                False"""
        @overload
        def is_square(self) -> Any:
            """RealDoubleElement.is_square(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1857)

            Return whether or not this number is a square in this field. For
            the real numbers, this is ``True`` if and only if ``self`` is
            nonnegative.

            EXAMPLES::

                sage: RDF(3.5).is_square()
                True
                sage: RDF(0).is_square()
                True
                sage: RDF(-4).is_square()
                False"""
        @overload
        def is_square(self) -> Any:
            """RealDoubleElement.is_square(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1857)

            Return whether or not this number is a square in this field. For
            the real numbers, this is ``True`` if and only if ``self`` is
            nonnegative.

            EXAMPLES::

                sage: RDF(3.5).is_square()
                True
                sage: RDF(0).is_square()
                True
                sage: RDF(-4).is_square()
                False"""
        def multiplicative_order(self) -> Any:
            """RealDoubleElement.multiplicative_order(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1455)

            Return `n` such that ``self^n == 1``.

            Only `\\pm 1` have finite multiplicative order.

            EXAMPLES::

                sage: RDF(1).multiplicative_order()
                1
                sage: RDF(-1).multiplicative_order()
                2
                sage: RDF(3).multiplicative_order()
                +Infinity"""
        def nan(self, *args, **kwargs):
            """RealDoubleElement.NaN(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1786)

            Return Not-a-Number ``NaN``.

            EXAMPLES::

                sage: RDF.NaN()
                NaN"""
        @overload
        def prec(self) -> Any:
            """RealDoubleElement.prec(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 749)

            Return the precision of this number in bits.

            Always returns 53.

            EXAMPLES::

                sage: RDF(0).prec()
                53"""
        @overload
        def prec(self) -> Any:
            """RealDoubleElement.prec(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 749)

            Return the precision of this number in bits.

            Always returns 53.

            EXAMPLES::

                sage: RDF(0).prec()
                53"""
        @overload
        def real(self) -> Any:
            """RealDoubleElement.real(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 866)

            Return ``self`` - we are already real.

            EXAMPLES::

                sage: a = RDF(3)
                sage: a.real()
                3.0"""
        @overload
        def real(self) -> Any:
            """RealDoubleElement.real(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 866)

            Return ``self`` - we are already real.

            EXAMPLES::

                sage: a = RDF(3)
                sage: a.real()
                3.0"""
        @overload
        def round(self) -> Any:
            """RealDoubleElement.round(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1500)

            Round ``self`` to the nearest integer.

            This uses the convention of rounding half to even
            (i.e., if the fractional part of ``self`` is `0.5`, then it
            is rounded to the nearest even integer).

            EXAMPLES::

                sage: RDF(0.49).round()
                0
                sage: a=RDF(0.51).round(); a
                1
                sage: RDF(0.5).round()
                0
                sage: RDF(1.5).round()
                2"""
        @overload
        def round(self) -> Any:
            """RealDoubleElement.round(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1500)

            Round ``self`` to the nearest integer.

            This uses the convention of rounding half to even
            (i.e., if the fractional part of ``self`` is `0.5`, then it
            is rounded to the nearest even integer).

            EXAMPLES::

                sage: RDF(0.49).round()
                0
                sage: a=RDF(0.51).round(); a
                1
                sage: RDF(0.5).round()
                0
                sage: RDF(1.5).round()
                2"""
        @overload
        def round(self) -> Any:
            """RealDoubleElement.round(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1500)

            Round ``self`` to the nearest integer.

            This uses the convention of rounding half to even
            (i.e., if the fractional part of ``self`` is `0.5`, then it
            is rounded to the nearest even integer).

            EXAMPLES::

                sage: RDF(0.49).round()
                0
                sage: a=RDF(0.51).round(); a
                1
                sage: RDF(0.5).round()
                0
                sage: RDF(1.5).round()
                2"""
        @overload
        def round(self) -> Any:
            """RealDoubleElement.round(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1500)

            Round ``self`` to the nearest integer.

            This uses the convention of rounding half to even
            (i.e., if the fractional part of ``self`` is `0.5`, then it
            is rounded to the nearest even integer).

            EXAMPLES::

                sage: RDF(0.49).round()
                0
                sage: a=RDF(0.51).round(); a
                1
                sage: RDF(0.5).round()
                0
                sage: RDF(1.5).round()
                2"""
        @overload
        def round(self) -> Any:
            """RealDoubleElement.round(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1500)

            Round ``self`` to the nearest integer.

            This uses the convention of rounding half to even
            (i.e., if the fractional part of ``self`` is `0.5`, then it
            is rounded to the nearest even integer).

            EXAMPLES::

                sage: RDF(0.49).round()
                0
                sage: a=RDF(0.51).round(); a
                1
                sage: RDF(0.5).round()
                0
                sage: RDF(1.5).round()
                2"""
        @overload
        def sign(self) -> Any:
            """RealDoubleElement.sign(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1476)

            Return -1, 0, or 1 if ``self`` is negative, zero, or positive;
            respectively.

            EXAMPLES::

                sage: RDF(-1.5).sign()
                -1
                sage: RDF(0).sign()
                0
                sage: RDF(2.5).sign()
                1"""
        @overload
        def sign(self) -> Any:
            """RealDoubleElement.sign(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1476)

            Return -1, 0, or 1 if ``self`` is negative, zero, or positive;
            respectively.

            EXAMPLES::

                sage: RDF(-1.5).sign()
                -1
                sage: RDF(0).sign()
                0
                sage: RDF(2.5).sign()
                1"""
        @overload
        def sign(self) -> Any:
            """RealDoubleElement.sign(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1476)

            Return -1, 0, or 1 if ``self`` is negative, zero, or positive;
            respectively.

            EXAMPLES::

                sage: RDF(-1.5).sign()
                -1
                sage: RDF(0).sign()
                0
                sage: RDF(2.5).sign()
                1"""
        @overload
        def sign(self) -> Any:
            """RealDoubleElement.sign(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1476)

            Return -1, 0, or 1 if ``self`` is negative, zero, or positive;
            respectively.

            EXAMPLES::

                sage: RDF(-1.5).sign()
                -1
                sage: RDF(0).sign()
                0
                sage: RDF(2.5).sign()
                1"""
        def sign_mantissa_exponent(self) -> Any:
            """RealDoubleElement.sign_mantissa_exponent(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1230)

            Return the sign, mantissa, and exponent of ``self``.

            In Sage (as in MPFR), floating-point numbers of precision `p`
            are of the form `s m 2^{e-p}`, where `s \\in \\{-1, 1\\}`,
            `2^{p-1} \\leq m < 2^p`, and `-2^{30} + 1 \\leq e \\leq 2^{30} -
            1`; plus the special values ``+0``, ``-0``, ``+infinity``,
            ``-infinity``, and ``NaN`` (which stands for Not-a-Number).

            This function returns `s`, `m`, and `e-p`.  For the special values:

            - ``+0`` returns ``(1, 0, 0)``
            - ``-0`` returns ``(-1, 0, 0)``
            - the return values for ``+infinity``, ``-infinity``, and ``NaN`` are
              not specified.

            EXAMPLES::

                sage: # needs sage.symbolic
                sage: a = RDF(exp(1.0)); a
                2.718281828459045
                sage: sign, mantissa, exponent = RDF(exp(1.0)).sign_mantissa_exponent()
                sage: sign, mantissa, exponent
                (1, 6121026514868073, -51)
                sage: sign*mantissa*(2**exponent) == a
                True

            The mantissa is always a nonnegative number::

                sage: RDF(-1).sign_mantissa_exponent()                                      # needs sage.rings.real_mpfr
                (-1, 4503599627370496, -52)

            TESTS::

                sage: RDF('+0').sign_mantissa_exponent()                                    # needs sage.rings.real_mpfr
                (1, 0, 0)
                sage: RDF('-0').sign_mantissa_exponent()                                    # needs sage.rings.real_mpfr
                (-1, 0, 0)"""
        @overload
        def sqrt(self, extend=..., all=...) -> Any:
            """RealDoubleElement.sqrt(self, extend=True, all=False)

            File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1799)

            The square root function.

            INPUT:

            - ``extend`` -- boolean (default: ``True``); if ``True``, return a
              square root in a complex field if necessary if ``self`` is negative.
              Otherwise raise a :exc:`ValueError`.

            - ``all`` -- boolean (default: ``False``); if ``True``, return a
              list of all square roots

            EXAMPLES::

                sage: r = RDF(4.0)
                sage: r.sqrt()
                2.0
                sage: r.sqrt()^2 == r
                True

            ::

                sage: r = RDF(4344)
                sage: r.sqrt()
                65.90902821313632
                sage: r.sqrt()^2 - r
                0.0

            ::

                sage: r = RDF(-2.0)
                sage: r.sqrt()                                                              # needs sage.rings.complex_double
                1.4142135623730951*I

            ::

                sage: RDF(2).sqrt(all=True)
                [1.4142135623730951, -1.4142135623730951]
                sage: RDF(0).sqrt(all=True)
                [0.0]
                sage: RDF(-2).sqrt(all=True)                                                # needs sage.rings.complex_double
                [1.4142135623730951*I, -1.4142135623730951*I]"""
        @overload
        def sqrt(self) -> Any:
            """RealDoubleElement.sqrt(self, extend=True, all=False)

            File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1799)

            The square root function.

            INPUT:

            - ``extend`` -- boolean (default: ``True``); if ``True``, return a
              square root in a complex field if necessary if ``self`` is negative.
              Otherwise raise a :exc:`ValueError`.

            - ``all`` -- boolean (default: ``False``); if ``True``, return a
              list of all square roots

            EXAMPLES::

                sage: r = RDF(4.0)
                sage: r.sqrt()
                2.0
                sage: r.sqrt()^2 == r
                True

            ::

                sage: r = RDF(4344)
                sage: r.sqrt()
                65.90902821313632
                sage: r.sqrt()^2 - r
                0.0

            ::

                sage: r = RDF(-2.0)
                sage: r.sqrt()                                                              # needs sage.rings.complex_double
                1.4142135623730951*I

            ::

                sage: RDF(2).sqrt(all=True)
                [1.4142135623730951, -1.4142135623730951]
                sage: RDF(0).sqrt(all=True)
                [0.0]
                sage: RDF(-2).sqrt(all=True)                                                # needs sage.rings.complex_double
                [1.4142135623730951*I, -1.4142135623730951*I]"""
        @overload
        def sqrt(self) -> Any:
            """RealDoubleElement.sqrt(self, extend=True, all=False)

            File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1799)

            The square root function.

            INPUT:

            - ``extend`` -- boolean (default: ``True``); if ``True``, return a
              square root in a complex field if necessary if ``self`` is negative.
              Otherwise raise a :exc:`ValueError`.

            - ``all`` -- boolean (default: ``False``); if ``True``, return a
              list of all square roots

            EXAMPLES::

                sage: r = RDF(4.0)
                sage: r.sqrt()
                2.0
                sage: r.sqrt()^2 == r
                True

            ::

                sage: r = RDF(4344)
                sage: r.sqrt()
                65.90902821313632
                sage: r.sqrt()^2 - r
                0.0

            ::

                sage: r = RDF(-2.0)
                sage: r.sqrt()                                                              # needs sage.rings.complex_double
                1.4142135623730951*I

            ::

                sage: RDF(2).sqrt(all=True)
                [1.4142135623730951, -1.4142135623730951]
                sage: RDF(0).sqrt(all=True)
                [0.0]
                sage: RDF(-2).sqrt(all=True)                                                # needs sage.rings.complex_double
                [1.4142135623730951*I, -1.4142135623730951*I]"""
        @overload
        def sqrt(self) -> Any:
            """RealDoubleElement.sqrt(self, extend=True, all=False)

            File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1799)

            The square root function.

            INPUT:

            - ``extend`` -- boolean (default: ``True``); if ``True``, return a
              square root in a complex field if necessary if ``self`` is negative.
              Otherwise raise a :exc:`ValueError`.

            - ``all`` -- boolean (default: ``False``); if ``True``, return a
              list of all square roots

            EXAMPLES::

                sage: r = RDF(4.0)
                sage: r.sqrt()
                2.0
                sage: r.sqrt()^2 == r
                True

            ::

                sage: r = RDF(4344)
                sage: r.sqrt()
                65.90902821313632
                sage: r.sqrt()^2 - r
                0.0

            ::

                sage: r = RDF(-2.0)
                sage: r.sqrt()                                                              # needs sage.rings.complex_double
                1.4142135623730951*I

            ::

                sage: RDF(2).sqrt(all=True)
                [1.4142135623730951, -1.4142135623730951]
                sage: RDF(0).sqrt(all=True)
                [0.0]
                sage: RDF(-2).sqrt(all=True)                                                # needs sage.rings.complex_double
                [1.4142135623730951*I, -1.4142135623730951*I]"""
        @overload
        def sqrt(self) -> Any:
            """RealDoubleElement.sqrt(self, extend=True, all=False)

            File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1799)

            The square root function.

            INPUT:

            - ``extend`` -- boolean (default: ``True``); if ``True``, return a
              square root in a complex field if necessary if ``self`` is negative.
              Otherwise raise a :exc:`ValueError`.

            - ``all`` -- boolean (default: ``False``); if ``True``, return a
              list of all square roots

            EXAMPLES::

                sage: r = RDF(4.0)
                sage: r.sqrt()
                2.0
                sage: r.sqrt()^2 == r
                True

            ::

                sage: r = RDF(4344)
                sage: r.sqrt()
                65.90902821313632
                sage: r.sqrt()^2 - r
                0.0

            ::

                sage: r = RDF(-2.0)
                sage: r.sqrt()                                                              # needs sage.rings.complex_double
                1.4142135623730951*I

            ::

                sage: RDF(2).sqrt(all=True)
                [1.4142135623730951, -1.4142135623730951]
                sage: RDF(0).sqrt(all=True)
                [0.0]
                sage: RDF(-2).sqrt(all=True)                                                # needs sage.rings.complex_double
                [1.4142135623730951*I, -1.4142135623730951*I]"""
        @overload
        def sqrt(self) -> Any:
            """RealDoubleElement.sqrt(self, extend=True, all=False)

            File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1799)

            The square root function.

            INPUT:

            - ``extend`` -- boolean (default: ``True``); if ``True``, return a
              square root in a complex field if necessary if ``self`` is negative.
              Otherwise raise a :exc:`ValueError`.

            - ``all`` -- boolean (default: ``False``); if ``True``, return a
              list of all square roots

            EXAMPLES::

                sage: r = RDF(4.0)
                sage: r.sqrt()
                2.0
                sage: r.sqrt()^2 == r
                True

            ::

                sage: r = RDF(4344)
                sage: r.sqrt()
                65.90902821313632
                sage: r.sqrt()^2 - r
                0.0

            ::

                sage: r = RDF(-2.0)
                sage: r.sqrt()                                                              # needs sage.rings.complex_double
                1.4142135623730951*I

            ::

                sage: RDF(2).sqrt(all=True)
                [1.4142135623730951, -1.4142135623730951]
                sage: RDF(0).sqrt(all=True)
                [0.0]
                sage: RDF(-2).sqrt(all=True)                                                # needs sage.rings.complex_double
                [1.4142135623730951*I, -1.4142135623730951*I]"""
        @overload
        def sqrt(self, all=...) -> Any:
            """RealDoubleElement.sqrt(self, extend=True, all=False)

            File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1799)

            The square root function.

            INPUT:

            - ``extend`` -- boolean (default: ``True``); if ``True``, return a
              square root in a complex field if necessary if ``self`` is negative.
              Otherwise raise a :exc:`ValueError`.

            - ``all`` -- boolean (default: ``False``); if ``True``, return a
              list of all square roots

            EXAMPLES::

                sage: r = RDF(4.0)
                sage: r.sqrt()
                2.0
                sage: r.sqrt()^2 == r
                True

            ::

                sage: r = RDF(4344)
                sage: r.sqrt()
                65.90902821313632
                sage: r.sqrt()^2 - r
                0.0

            ::

                sage: r = RDF(-2.0)
                sage: r.sqrt()                                                              # needs sage.rings.complex_double
                1.4142135623730951*I

            ::

                sage: RDF(2).sqrt(all=True)
                [1.4142135623730951, -1.4142135623730951]
                sage: RDF(0).sqrt(all=True)
                [0.0]
                sage: RDF(-2).sqrt(all=True)                                                # needs sage.rings.complex_double
                [1.4142135623730951*I, -1.4142135623730951*I]"""
        @overload
        def sqrt(self, all=...) -> Any:
            """RealDoubleElement.sqrt(self, extend=True, all=False)

            File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1799)

            The square root function.

            INPUT:

            - ``extend`` -- boolean (default: ``True``); if ``True``, return a
              square root in a complex field if necessary if ``self`` is negative.
              Otherwise raise a :exc:`ValueError`.

            - ``all`` -- boolean (default: ``False``); if ``True``, return a
              list of all square roots

            EXAMPLES::

                sage: r = RDF(4.0)
                sage: r.sqrt()
                2.0
                sage: r.sqrt()^2 == r
                True

            ::

                sage: r = RDF(4344)
                sage: r.sqrt()
                65.90902821313632
                sage: r.sqrt()^2 - r
                0.0

            ::

                sage: r = RDF(-2.0)
                sage: r.sqrt()                                                              # needs sage.rings.complex_double
                1.4142135623730951*I

            ::

                sage: RDF(2).sqrt(all=True)
                [1.4142135623730951, -1.4142135623730951]
                sage: RDF(0).sqrt(all=True)
                [0.0]
                sage: RDF(-2).sqrt(all=True)                                                # needs sage.rings.complex_double
                [1.4142135623730951*I, -1.4142135623730951*I]"""
        @overload
        def sqrt(self, all=...) -> Any:
            """RealDoubleElement.sqrt(self, extend=True, all=False)

            File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1799)

            The square root function.

            INPUT:

            - ``extend`` -- boolean (default: ``True``); if ``True``, return a
              square root in a complex field if necessary if ``self`` is negative.
              Otherwise raise a :exc:`ValueError`.

            - ``all`` -- boolean (default: ``False``); if ``True``, return a
              list of all square roots

            EXAMPLES::

                sage: r = RDF(4.0)
                sage: r.sqrt()
                2.0
                sage: r.sqrt()^2 == r
                True

            ::

                sage: r = RDF(4344)
                sage: r.sqrt()
                65.90902821313632
                sage: r.sqrt()^2 - r
                0.0

            ::

                sage: r = RDF(-2.0)
                sage: r.sqrt()                                                              # needs sage.rings.complex_double
                1.4142135623730951*I

            ::

                sage: RDF(2).sqrt(all=True)
                [1.4142135623730951, -1.4142135623730951]
                sage: RDF(0).sqrt(all=True)
                [0.0]
                sage: RDF(-2).sqrt(all=True)                                                # needs sage.rings.complex_double
                [1.4142135623730951*I, -1.4142135623730951*I]"""
        @overload
        def str(self) -> Any:
            """RealDoubleElement.str(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1157)

            Return the informal string representation of ``self``.

            EXAMPLES::

                sage: a = RDF('4.5'); a.str()
                '4.5'
                sage: a = RDF('49203480923840.2923904823048'); a.str()
                '49203480923840.29'
                sage: a = RDF(1)/RDF(0); a.str()
                '+infinity'
                sage: a = -RDF(1)/RDF(0); a.str()
                '-infinity'
                sage: a = RDF(0)/RDF(0); a.str()
                'NaN'

            We verify consistency with ``RR`` (mpfr reals)::

                sage: str(RR(RDF(1)/RDF(0))) == str(RDF(1)/RDF(0))
                True
                sage: str(RR(-RDF(1)/RDF(0))) == str(-RDF(1)/RDF(0))
                True
                sage: str(RR(RDF(0)/RDF(0))) == str(RDF(0)/RDF(0))
                True"""
        @overload
        def str(self) -> Any:
            """RealDoubleElement.str(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1157)

            Return the informal string representation of ``self``.

            EXAMPLES::

                sage: a = RDF('4.5'); a.str()
                '4.5'
                sage: a = RDF('49203480923840.2923904823048'); a.str()
                '49203480923840.29'
                sage: a = RDF(1)/RDF(0); a.str()
                '+infinity'
                sage: a = -RDF(1)/RDF(0); a.str()
                '-infinity'
                sage: a = RDF(0)/RDF(0); a.str()
                'NaN'

            We verify consistency with ``RR`` (mpfr reals)::

                sage: str(RR(RDF(1)/RDF(0))) == str(RDF(1)/RDF(0))
                True
                sage: str(RR(-RDF(1)/RDF(0))) == str(-RDF(1)/RDF(0))
                True
                sage: str(RR(RDF(0)/RDF(0))) == str(RDF(0)/RDF(0))
                True"""
        @overload
        def str(self) -> Any:
            """RealDoubleElement.str(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1157)

            Return the informal string representation of ``self``.

            EXAMPLES::

                sage: a = RDF('4.5'); a.str()
                '4.5'
                sage: a = RDF('49203480923840.2923904823048'); a.str()
                '49203480923840.29'
                sage: a = RDF(1)/RDF(0); a.str()
                '+infinity'
                sage: a = -RDF(1)/RDF(0); a.str()
                '-infinity'
                sage: a = RDF(0)/RDF(0); a.str()
                'NaN'

            We verify consistency with ``RR`` (mpfr reals)::

                sage: str(RR(RDF(1)/RDF(0))) == str(RDF(1)/RDF(0))
                True
                sage: str(RR(-RDF(1)/RDF(0))) == str(-RDF(1)/RDF(0))
                True
                sage: str(RR(RDF(0)/RDF(0))) == str(RDF(0)/RDF(0))
                True"""
        @overload
        def str(self) -> Any:
            """RealDoubleElement.str(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1157)

            Return the informal string representation of ``self``.

            EXAMPLES::

                sage: a = RDF('4.5'); a.str()
                '4.5'
                sage: a = RDF('49203480923840.2923904823048'); a.str()
                '49203480923840.29'
                sage: a = RDF(1)/RDF(0); a.str()
                '+infinity'
                sage: a = -RDF(1)/RDF(0); a.str()
                '-infinity'
                sage: a = RDF(0)/RDF(0); a.str()
                'NaN'

            We verify consistency with ``RR`` (mpfr reals)::

                sage: str(RR(RDF(1)/RDF(0))) == str(RDF(1)/RDF(0))
                True
                sage: str(RR(-RDF(1)/RDF(0))) == str(-RDF(1)/RDF(0))
                True
                sage: str(RR(RDF(0)/RDF(0))) == str(RDF(0)/RDF(0))
                True"""
        @overload
        def str(self) -> Any:
            """RealDoubleElement.str(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1157)

            Return the informal string representation of ``self``.

            EXAMPLES::

                sage: a = RDF('4.5'); a.str()
                '4.5'
                sage: a = RDF('49203480923840.2923904823048'); a.str()
                '49203480923840.29'
                sage: a = RDF(1)/RDF(0); a.str()
                '+infinity'
                sage: a = -RDF(1)/RDF(0); a.str()
                '-infinity'
                sage: a = RDF(0)/RDF(0); a.str()
                'NaN'

            We verify consistency with ``RR`` (mpfr reals)::

                sage: str(RR(RDF(1)/RDF(0))) == str(RDF(1)/RDF(0))
                True
                sage: str(RR(-RDF(1)/RDF(0))) == str(-RDF(1)/RDF(0))
                True
                sage: str(RR(RDF(0)/RDF(0))) == str(RDF(0)/RDF(0))
                True"""
        @overload
        def str(self) -> Any:
            """RealDoubleElement.str(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1157)

            Return the informal string representation of ``self``.

            EXAMPLES::

                sage: a = RDF('4.5'); a.str()
                '4.5'
                sage: a = RDF('49203480923840.2923904823048'); a.str()
                '49203480923840.29'
                sage: a = RDF(1)/RDF(0); a.str()
                '+infinity'
                sage: a = -RDF(1)/RDF(0); a.str()
                '-infinity'
                sage: a = RDF(0)/RDF(0); a.str()
                'NaN'

            We verify consistency with ``RR`` (mpfr reals)::

                sage: str(RR(RDF(1)/RDF(0))) == str(RDF(1)/RDF(0))
                True
                sage: str(RR(-RDF(1)/RDF(0))) == str(-RDF(1)/RDF(0))
                True
                sage: str(RR(RDF(0)/RDF(0))) == str(RDF(0)/RDF(0))
                True"""
        @overload
        def trunc(self) -> Any:
            """RealDoubleElement.trunc(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1553)

            Truncates this number (returns integer part).

            EXAMPLES::

                sage: RDF(2.99).trunc()
                2
                sage: RDF(-2.00).trunc()
                -2
                sage: RDF(0.00).trunc()
                0"""
        @overload
        def trunc(self) -> Any:
            """RealDoubleElement.trunc(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1553)

            Truncates this number (returns integer part).

            EXAMPLES::

                sage: RDF(2.99).trunc()
                2
                sage: RDF(-2.00).trunc()
                -2
                sage: RDF(0.00).trunc()
                0"""
        @overload
        def trunc(self) -> Any:
            """RealDoubleElement.trunc(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1553)

            Truncates this number (returns integer part).

            EXAMPLES::

                sage: RDF(2.99).trunc()
                2
                sage: RDF(-2.00).trunc()
                -2
                sage: RDF(0.00).trunc()
                0"""
        @overload
        def trunc(self) -> Any:
            """RealDoubleElement.trunc(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1553)

            Truncates this number (returns integer part).

            EXAMPLES::

                sage: RDF(2.99).trunc()
                2
                sage: RDF(-2.00).trunc()
                -2
                sage: RDF(0.00).trunc()
                0"""
        @overload
        def ulp(self) -> Any:
            """RealDoubleElement.ulp(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 762)

            Return the unit of least precision of ``self``, which is the
            weight of the least significant bit of ``self``. This is always
            a strictly positive number. It is also the gap between this
            number and the closest number with larger absolute value that
            can be represented.

            EXAMPLES::

                sage: a = RDF(pi)                                                           # needs sage.symbolic
                sage: a.ulp()                                                               # needs sage.symbolic
                4.440892098500626e-16
                sage: b = a + a.ulp()                                                       # needs sage.symbolic

            Adding or subtracting an ulp always gives a different number::

                sage: # needs sage.symbolic
                sage: a + a.ulp() == a
                False
                sage: a - a.ulp() == a
                False
                sage: b + b.ulp() == b
                False
                sage: b - b.ulp() == b
                False

            Since the default rounding mode is round-to-nearest, adding or
            subtracting something less than half an ulp always gives the
            same number, unless the result has a smaller ulp. The latter
            can only happen if the input number is (up to sign) exactly a
            power of 2::

                sage: # needs sage.symbolic
                sage: a - a.ulp()/3 == a
                True
                sage: a + a.ulp()/3 == a
                True
                sage: b - b.ulp()/3 == b
                True
                sage: b + b.ulp()/3 == b
                True

                sage: c = RDF(1)
                sage: c - c.ulp()/3 == c
                False
                sage: c.ulp()
                2.220446049250313e-16
                sage: (c - c.ulp()).ulp()
                1.1102230246251565e-16

            The ulp is always positive::

                sage: RDF(-1).ulp()
                2.220446049250313e-16

            The ulp of zero is the smallest positive number in RDF::

                sage: RDF(0).ulp()
                5e-324
                sage: RDF(0).ulp()/2
                0.0

            Some special values::

                sage: a = RDF(1)/RDF(0); a
                +infinity
                sage: a.ulp()
                +infinity
                sage: (-a).ulp()
                +infinity
                sage: a = RDF('nan')
                sage: a.ulp() is a
                True

            The ulp method works correctly with small numbers::

                sage: u = RDF(0).ulp()
                sage: u.ulp() == u
                True
                sage: x = u * (2^52-1)  # largest denormal number
                sage: x.ulp() == u
                True
                sage: x = u * 2^52  # smallest normal number
                sage: x.ulp() == u
                True"""
        @overload
        def ulp(self) -> Any:
            """RealDoubleElement.ulp(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 762)

            Return the unit of least precision of ``self``, which is the
            weight of the least significant bit of ``self``. This is always
            a strictly positive number. It is also the gap between this
            number and the closest number with larger absolute value that
            can be represented.

            EXAMPLES::

                sage: a = RDF(pi)                                                           # needs sage.symbolic
                sage: a.ulp()                                                               # needs sage.symbolic
                4.440892098500626e-16
                sage: b = a + a.ulp()                                                       # needs sage.symbolic

            Adding or subtracting an ulp always gives a different number::

                sage: # needs sage.symbolic
                sage: a + a.ulp() == a
                False
                sage: a - a.ulp() == a
                False
                sage: b + b.ulp() == b
                False
                sage: b - b.ulp() == b
                False

            Since the default rounding mode is round-to-nearest, adding or
            subtracting something less than half an ulp always gives the
            same number, unless the result has a smaller ulp. The latter
            can only happen if the input number is (up to sign) exactly a
            power of 2::

                sage: # needs sage.symbolic
                sage: a - a.ulp()/3 == a
                True
                sage: a + a.ulp()/3 == a
                True
                sage: b - b.ulp()/3 == b
                True
                sage: b + b.ulp()/3 == b
                True

                sage: c = RDF(1)
                sage: c - c.ulp()/3 == c
                False
                sage: c.ulp()
                2.220446049250313e-16
                sage: (c - c.ulp()).ulp()
                1.1102230246251565e-16

            The ulp is always positive::

                sage: RDF(-1).ulp()
                2.220446049250313e-16

            The ulp of zero is the smallest positive number in RDF::

                sage: RDF(0).ulp()
                5e-324
                sage: RDF(0).ulp()/2
                0.0

            Some special values::

                sage: a = RDF(1)/RDF(0); a
                +infinity
                sage: a.ulp()
                +infinity
                sage: (-a).ulp()
                +infinity
                sage: a = RDF('nan')
                sage: a.ulp() is a
                True

            The ulp method works correctly with small numbers::

                sage: u = RDF(0).ulp()
                sage: u.ulp() == u
                True
                sage: x = u * (2^52-1)  # largest denormal number
                sage: x.ulp() == u
                True
                sage: x = u * 2^52  # smallest normal number
                sage: x.ulp() == u
                True"""
        @overload
        def ulp(self) -> Any:
            """RealDoubleElement.ulp(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 762)

            Return the unit of least precision of ``self``, which is the
            weight of the least significant bit of ``self``. This is always
            a strictly positive number. It is also the gap between this
            number and the closest number with larger absolute value that
            can be represented.

            EXAMPLES::

                sage: a = RDF(pi)                                                           # needs sage.symbolic
                sage: a.ulp()                                                               # needs sage.symbolic
                4.440892098500626e-16
                sage: b = a + a.ulp()                                                       # needs sage.symbolic

            Adding or subtracting an ulp always gives a different number::

                sage: # needs sage.symbolic
                sage: a + a.ulp() == a
                False
                sage: a - a.ulp() == a
                False
                sage: b + b.ulp() == b
                False
                sage: b - b.ulp() == b
                False

            Since the default rounding mode is round-to-nearest, adding or
            subtracting something less than half an ulp always gives the
            same number, unless the result has a smaller ulp. The latter
            can only happen if the input number is (up to sign) exactly a
            power of 2::

                sage: # needs sage.symbolic
                sage: a - a.ulp()/3 == a
                True
                sage: a + a.ulp()/3 == a
                True
                sage: b - b.ulp()/3 == b
                True
                sage: b + b.ulp()/3 == b
                True

                sage: c = RDF(1)
                sage: c - c.ulp()/3 == c
                False
                sage: c.ulp()
                2.220446049250313e-16
                sage: (c - c.ulp()).ulp()
                1.1102230246251565e-16

            The ulp is always positive::

                sage: RDF(-1).ulp()
                2.220446049250313e-16

            The ulp of zero is the smallest positive number in RDF::

                sage: RDF(0).ulp()
                5e-324
                sage: RDF(0).ulp()/2
                0.0

            Some special values::

                sage: a = RDF(1)/RDF(0); a
                +infinity
                sage: a.ulp()
                +infinity
                sage: (-a).ulp()
                +infinity
                sage: a = RDF('nan')
                sage: a.ulp() is a
                True

            The ulp method works correctly with small numbers::

                sage: u = RDF(0).ulp()
                sage: u.ulp() == u
                True
                sage: x = u * (2^52-1)  # largest denormal number
                sage: x.ulp() == u
                True
                sage: x = u * 2^52  # smallest normal number
                sage: x.ulp() == u
                True"""
        @overload
        def ulp(self) -> Any:
            """RealDoubleElement.ulp(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 762)

            Return the unit of least precision of ``self``, which is the
            weight of the least significant bit of ``self``. This is always
            a strictly positive number. It is also the gap between this
            number and the closest number with larger absolute value that
            can be represented.

            EXAMPLES::

                sage: a = RDF(pi)                                                           # needs sage.symbolic
                sage: a.ulp()                                                               # needs sage.symbolic
                4.440892098500626e-16
                sage: b = a + a.ulp()                                                       # needs sage.symbolic

            Adding or subtracting an ulp always gives a different number::

                sage: # needs sage.symbolic
                sage: a + a.ulp() == a
                False
                sage: a - a.ulp() == a
                False
                sage: b + b.ulp() == b
                False
                sage: b - b.ulp() == b
                False

            Since the default rounding mode is round-to-nearest, adding or
            subtracting something less than half an ulp always gives the
            same number, unless the result has a smaller ulp. The latter
            can only happen if the input number is (up to sign) exactly a
            power of 2::

                sage: # needs sage.symbolic
                sage: a - a.ulp()/3 == a
                True
                sage: a + a.ulp()/3 == a
                True
                sage: b - b.ulp()/3 == b
                True
                sage: b + b.ulp()/3 == b
                True

                sage: c = RDF(1)
                sage: c - c.ulp()/3 == c
                False
                sage: c.ulp()
                2.220446049250313e-16
                sage: (c - c.ulp()).ulp()
                1.1102230246251565e-16

            The ulp is always positive::

                sage: RDF(-1).ulp()
                2.220446049250313e-16

            The ulp of zero is the smallest positive number in RDF::

                sage: RDF(0).ulp()
                5e-324
                sage: RDF(0).ulp()/2
                0.0

            Some special values::

                sage: a = RDF(1)/RDF(0); a
                +infinity
                sage: a.ulp()
                +infinity
                sage: (-a).ulp()
                +infinity
                sage: a = RDF('nan')
                sage: a.ulp() is a
                True

            The ulp method works correctly with small numbers::

                sage: u = RDF(0).ulp()
                sage: u.ulp() == u
                True
                sage: x = u * (2^52-1)  # largest denormal number
                sage: x.ulp() == u
                True
                sage: x = u * 2^52  # smallest normal number
                sage: x.ulp() == u
                True"""
        @overload
        def ulp(self) -> Any:
            """RealDoubleElement.ulp(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 762)

            Return the unit of least precision of ``self``, which is the
            weight of the least significant bit of ``self``. This is always
            a strictly positive number. It is also the gap between this
            number and the closest number with larger absolute value that
            can be represented.

            EXAMPLES::

                sage: a = RDF(pi)                                                           # needs sage.symbolic
                sage: a.ulp()                                                               # needs sage.symbolic
                4.440892098500626e-16
                sage: b = a + a.ulp()                                                       # needs sage.symbolic

            Adding or subtracting an ulp always gives a different number::

                sage: # needs sage.symbolic
                sage: a + a.ulp() == a
                False
                sage: a - a.ulp() == a
                False
                sage: b + b.ulp() == b
                False
                sage: b - b.ulp() == b
                False

            Since the default rounding mode is round-to-nearest, adding or
            subtracting something less than half an ulp always gives the
            same number, unless the result has a smaller ulp. The latter
            can only happen if the input number is (up to sign) exactly a
            power of 2::

                sage: # needs sage.symbolic
                sage: a - a.ulp()/3 == a
                True
                sage: a + a.ulp()/3 == a
                True
                sage: b - b.ulp()/3 == b
                True
                sage: b + b.ulp()/3 == b
                True

                sage: c = RDF(1)
                sage: c - c.ulp()/3 == c
                False
                sage: c.ulp()
                2.220446049250313e-16
                sage: (c - c.ulp()).ulp()
                1.1102230246251565e-16

            The ulp is always positive::

                sage: RDF(-1).ulp()
                2.220446049250313e-16

            The ulp of zero is the smallest positive number in RDF::

                sage: RDF(0).ulp()
                5e-324
                sage: RDF(0).ulp()/2
                0.0

            Some special values::

                sage: a = RDF(1)/RDF(0); a
                +infinity
                sage: a.ulp()
                +infinity
                sage: (-a).ulp()
                +infinity
                sage: a = RDF('nan')
                sage: a.ulp() is a
                True

            The ulp method works correctly with small numbers::

                sage: u = RDF(0).ulp()
                sage: u.ulp() == u
                True
                sage: x = u * (2^52-1)  # largest denormal number
                sage: x.ulp() == u
                True
                sage: x = u * 2^52  # smallest normal number
                sage: x.ulp() == u
                True"""
        @overload
        def ulp(self) -> Any:
            """RealDoubleElement.ulp(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 762)

            Return the unit of least precision of ``self``, which is the
            weight of the least significant bit of ``self``. This is always
            a strictly positive number. It is also the gap between this
            number and the closest number with larger absolute value that
            can be represented.

            EXAMPLES::

                sage: a = RDF(pi)                                                           # needs sage.symbolic
                sage: a.ulp()                                                               # needs sage.symbolic
                4.440892098500626e-16
                sage: b = a + a.ulp()                                                       # needs sage.symbolic

            Adding or subtracting an ulp always gives a different number::

                sage: # needs sage.symbolic
                sage: a + a.ulp() == a
                False
                sage: a - a.ulp() == a
                False
                sage: b + b.ulp() == b
                False
                sage: b - b.ulp() == b
                False

            Since the default rounding mode is round-to-nearest, adding or
            subtracting something less than half an ulp always gives the
            same number, unless the result has a smaller ulp. The latter
            can only happen if the input number is (up to sign) exactly a
            power of 2::

                sage: # needs sage.symbolic
                sage: a - a.ulp()/3 == a
                True
                sage: a + a.ulp()/3 == a
                True
                sage: b - b.ulp()/3 == b
                True
                sage: b + b.ulp()/3 == b
                True

                sage: c = RDF(1)
                sage: c - c.ulp()/3 == c
                False
                sage: c.ulp()
                2.220446049250313e-16
                sage: (c - c.ulp()).ulp()
                1.1102230246251565e-16

            The ulp is always positive::

                sage: RDF(-1).ulp()
                2.220446049250313e-16

            The ulp of zero is the smallest positive number in RDF::

                sage: RDF(0).ulp()
                5e-324
                sage: RDF(0).ulp()/2
                0.0

            Some special values::

                sage: a = RDF(1)/RDF(0); a
                +infinity
                sage: a.ulp()
                +infinity
                sage: (-a).ulp()
                +infinity
                sage: a = RDF('nan')
                sage: a.ulp() is a
                True

            The ulp method works correctly with small numbers::

                sage: u = RDF(0).ulp()
                sage: u.ulp() == u
                True
                sage: x = u * (2^52-1)  # largest denormal number
                sage: x.ulp() == u
                True
                sage: x = u * 2^52  # smallest normal number
                sage: x.ulp() == u
                True"""
        @overload
        def ulp(self) -> Any:
            """RealDoubleElement.ulp(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 762)

            Return the unit of least precision of ``self``, which is the
            weight of the least significant bit of ``self``. This is always
            a strictly positive number. It is also the gap between this
            number and the closest number with larger absolute value that
            can be represented.

            EXAMPLES::

                sage: a = RDF(pi)                                                           # needs sage.symbolic
                sage: a.ulp()                                                               # needs sage.symbolic
                4.440892098500626e-16
                sage: b = a + a.ulp()                                                       # needs sage.symbolic

            Adding or subtracting an ulp always gives a different number::

                sage: # needs sage.symbolic
                sage: a + a.ulp() == a
                False
                sage: a - a.ulp() == a
                False
                sage: b + b.ulp() == b
                False
                sage: b - b.ulp() == b
                False

            Since the default rounding mode is round-to-nearest, adding or
            subtracting something less than half an ulp always gives the
            same number, unless the result has a smaller ulp. The latter
            can only happen if the input number is (up to sign) exactly a
            power of 2::

                sage: # needs sage.symbolic
                sage: a - a.ulp()/3 == a
                True
                sage: a + a.ulp()/3 == a
                True
                sage: b - b.ulp()/3 == b
                True
                sage: b + b.ulp()/3 == b
                True

                sage: c = RDF(1)
                sage: c - c.ulp()/3 == c
                False
                sage: c.ulp()
                2.220446049250313e-16
                sage: (c - c.ulp()).ulp()
                1.1102230246251565e-16

            The ulp is always positive::

                sage: RDF(-1).ulp()
                2.220446049250313e-16

            The ulp of zero is the smallest positive number in RDF::

                sage: RDF(0).ulp()
                5e-324
                sage: RDF(0).ulp()/2
                0.0

            Some special values::

                sage: a = RDF(1)/RDF(0); a
                +infinity
                sage: a.ulp()
                +infinity
                sage: (-a).ulp()
                +infinity
                sage: a = RDF('nan')
                sage: a.ulp() is a
                True

            The ulp method works correctly with small numbers::

                sage: u = RDF(0).ulp()
                sage: u.ulp() == u
                True
                sage: x = u * (2^52-1)  # largest denormal number
                sage: x.ulp() == u
                True
                sage: x = u * 2^52  # smallest normal number
                sage: x.ulp() == u
                True"""
        @overload
        def ulp(self) -> Any:
            """RealDoubleElement.ulp(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 762)

            Return the unit of least precision of ``self``, which is the
            weight of the least significant bit of ``self``. This is always
            a strictly positive number. It is also the gap between this
            number and the closest number with larger absolute value that
            can be represented.

            EXAMPLES::

                sage: a = RDF(pi)                                                           # needs sage.symbolic
                sage: a.ulp()                                                               # needs sage.symbolic
                4.440892098500626e-16
                sage: b = a + a.ulp()                                                       # needs sage.symbolic

            Adding or subtracting an ulp always gives a different number::

                sage: # needs sage.symbolic
                sage: a + a.ulp() == a
                False
                sage: a - a.ulp() == a
                False
                sage: b + b.ulp() == b
                False
                sage: b - b.ulp() == b
                False

            Since the default rounding mode is round-to-nearest, adding or
            subtracting something less than half an ulp always gives the
            same number, unless the result has a smaller ulp. The latter
            can only happen if the input number is (up to sign) exactly a
            power of 2::

                sage: # needs sage.symbolic
                sage: a - a.ulp()/3 == a
                True
                sage: a + a.ulp()/3 == a
                True
                sage: b - b.ulp()/3 == b
                True
                sage: b + b.ulp()/3 == b
                True

                sage: c = RDF(1)
                sage: c - c.ulp()/3 == c
                False
                sage: c.ulp()
                2.220446049250313e-16
                sage: (c - c.ulp()).ulp()
                1.1102230246251565e-16

            The ulp is always positive::

                sage: RDF(-1).ulp()
                2.220446049250313e-16

            The ulp of zero is the smallest positive number in RDF::

                sage: RDF(0).ulp()
                5e-324
                sage: RDF(0).ulp()/2
                0.0

            Some special values::

                sage: a = RDF(1)/RDF(0); a
                +infinity
                sage: a.ulp()
                +infinity
                sage: (-a).ulp()
                +infinity
                sage: a = RDF('nan')
                sage: a.ulp() is a
                True

            The ulp method works correctly with small numbers::

                sage: u = RDF(0).ulp()
                sage: u.ulp() == u
                True
                sage: x = u * (2^52-1)  # largest denormal number
                sage: x.ulp() == u
                True
                sage: x = u * 2^52  # smallest normal number
                sage: x.ulp() == u
                True"""
        @overload
        def ulp(self) -> Any:
            """RealDoubleElement.ulp(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 762)

            Return the unit of least precision of ``self``, which is the
            weight of the least significant bit of ``self``. This is always
            a strictly positive number. It is also the gap between this
            number and the closest number with larger absolute value that
            can be represented.

            EXAMPLES::

                sage: a = RDF(pi)                                                           # needs sage.symbolic
                sage: a.ulp()                                                               # needs sage.symbolic
                4.440892098500626e-16
                sage: b = a + a.ulp()                                                       # needs sage.symbolic

            Adding or subtracting an ulp always gives a different number::

                sage: # needs sage.symbolic
                sage: a + a.ulp() == a
                False
                sage: a - a.ulp() == a
                False
                sage: b + b.ulp() == b
                False
                sage: b - b.ulp() == b
                False

            Since the default rounding mode is round-to-nearest, adding or
            subtracting something less than half an ulp always gives the
            same number, unless the result has a smaller ulp. The latter
            can only happen if the input number is (up to sign) exactly a
            power of 2::

                sage: # needs sage.symbolic
                sage: a - a.ulp()/3 == a
                True
                sage: a + a.ulp()/3 == a
                True
                sage: b - b.ulp()/3 == b
                True
                sage: b + b.ulp()/3 == b
                True

                sage: c = RDF(1)
                sage: c - c.ulp()/3 == c
                False
                sage: c.ulp()
                2.220446049250313e-16
                sage: (c - c.ulp()).ulp()
                1.1102230246251565e-16

            The ulp is always positive::

                sage: RDF(-1).ulp()
                2.220446049250313e-16

            The ulp of zero is the smallest positive number in RDF::

                sage: RDF(0).ulp()
                5e-324
                sage: RDF(0).ulp()/2
                0.0

            Some special values::

                sage: a = RDF(1)/RDF(0); a
                +infinity
                sage: a.ulp()
                +infinity
                sage: (-a).ulp()
                +infinity
                sage: a = RDF('nan')
                sage: a.ulp() is a
                True

            The ulp method works correctly with small numbers::

                sage: u = RDF(0).ulp()
                sage: u.ulp() == u
                True
                sage: x = u * (2^52-1)  # largest denormal number
                sage: x.ulp() == u
                True
                sage: x = u * 2^52  # smallest normal number
                sage: x.ulp() == u
                True"""
        @overload
        def ulp(self) -> Any:
            """RealDoubleElement.ulp(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 762)

            Return the unit of least precision of ``self``, which is the
            weight of the least significant bit of ``self``. This is always
            a strictly positive number. It is also the gap between this
            number and the closest number with larger absolute value that
            can be represented.

            EXAMPLES::

                sage: a = RDF(pi)                                                           # needs sage.symbolic
                sage: a.ulp()                                                               # needs sage.symbolic
                4.440892098500626e-16
                sage: b = a + a.ulp()                                                       # needs sage.symbolic

            Adding or subtracting an ulp always gives a different number::

                sage: # needs sage.symbolic
                sage: a + a.ulp() == a
                False
                sage: a - a.ulp() == a
                False
                sage: b + b.ulp() == b
                False
                sage: b - b.ulp() == b
                False

            Since the default rounding mode is round-to-nearest, adding or
            subtracting something less than half an ulp always gives the
            same number, unless the result has a smaller ulp. The latter
            can only happen if the input number is (up to sign) exactly a
            power of 2::

                sage: # needs sage.symbolic
                sage: a - a.ulp()/3 == a
                True
                sage: a + a.ulp()/3 == a
                True
                sage: b - b.ulp()/3 == b
                True
                sage: b + b.ulp()/3 == b
                True

                sage: c = RDF(1)
                sage: c - c.ulp()/3 == c
                False
                sage: c.ulp()
                2.220446049250313e-16
                sage: (c - c.ulp()).ulp()
                1.1102230246251565e-16

            The ulp is always positive::

                sage: RDF(-1).ulp()
                2.220446049250313e-16

            The ulp of zero is the smallest positive number in RDF::

                sage: RDF(0).ulp()
                5e-324
                sage: RDF(0).ulp()/2
                0.0

            Some special values::

                sage: a = RDF(1)/RDF(0); a
                +infinity
                sage: a.ulp()
                +infinity
                sage: (-a).ulp()
                +infinity
                sage: a = RDF('nan')
                sage: a.ulp() is a
                True

            The ulp method works correctly with small numbers::

                sage: u = RDF(0).ulp()
                sage: u.ulp() == u
                True
                sage: x = u * (2^52-1)  # largest denormal number
                sage: x.ulp() == u
                True
                sage: x = u * 2^52  # smallest normal number
                sage: x.ulp() == u
                True"""
        @overload
        def ulp(self) -> Any:
            """RealDoubleElement.ulp(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 762)

            Return the unit of least precision of ``self``, which is the
            weight of the least significant bit of ``self``. This is always
            a strictly positive number. It is also the gap between this
            number and the closest number with larger absolute value that
            can be represented.

            EXAMPLES::

                sage: a = RDF(pi)                                                           # needs sage.symbolic
                sage: a.ulp()                                                               # needs sage.symbolic
                4.440892098500626e-16
                sage: b = a + a.ulp()                                                       # needs sage.symbolic

            Adding or subtracting an ulp always gives a different number::

                sage: # needs sage.symbolic
                sage: a + a.ulp() == a
                False
                sage: a - a.ulp() == a
                False
                sage: b + b.ulp() == b
                False
                sage: b - b.ulp() == b
                False

            Since the default rounding mode is round-to-nearest, adding or
            subtracting something less than half an ulp always gives the
            same number, unless the result has a smaller ulp. The latter
            can only happen if the input number is (up to sign) exactly a
            power of 2::

                sage: # needs sage.symbolic
                sage: a - a.ulp()/3 == a
                True
                sage: a + a.ulp()/3 == a
                True
                sage: b - b.ulp()/3 == b
                True
                sage: b + b.ulp()/3 == b
                True

                sage: c = RDF(1)
                sage: c - c.ulp()/3 == c
                False
                sage: c.ulp()
                2.220446049250313e-16
                sage: (c - c.ulp()).ulp()
                1.1102230246251565e-16

            The ulp is always positive::

                sage: RDF(-1).ulp()
                2.220446049250313e-16

            The ulp of zero is the smallest positive number in RDF::

                sage: RDF(0).ulp()
                5e-324
                sage: RDF(0).ulp()/2
                0.0

            Some special values::

                sage: a = RDF(1)/RDF(0); a
                +infinity
                sage: a.ulp()
                +infinity
                sage: (-a).ulp()
                +infinity
                sage: a = RDF('nan')
                sage: a.ulp() is a
                True

            The ulp method works correctly with small numbers::

                sage: u = RDF(0).ulp()
                sage: u.ulp() == u
                True
                sage: x = u * (2^52-1)  # largest denormal number
                sage: x.ulp() == u
                True
                sage: x = u * 2^52  # smallest normal number
                sage: x.ulp() == u
                True"""
        @overload
        def ulp(self) -> Any:
            """RealDoubleElement.ulp(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 762)

            Return the unit of least precision of ``self``, which is the
            weight of the least significant bit of ``self``. This is always
            a strictly positive number. It is also the gap between this
            number and the closest number with larger absolute value that
            can be represented.

            EXAMPLES::

                sage: a = RDF(pi)                                                           # needs sage.symbolic
                sage: a.ulp()                                                               # needs sage.symbolic
                4.440892098500626e-16
                sage: b = a + a.ulp()                                                       # needs sage.symbolic

            Adding or subtracting an ulp always gives a different number::

                sage: # needs sage.symbolic
                sage: a + a.ulp() == a
                False
                sage: a - a.ulp() == a
                False
                sage: b + b.ulp() == b
                False
                sage: b - b.ulp() == b
                False

            Since the default rounding mode is round-to-nearest, adding or
            subtracting something less than half an ulp always gives the
            same number, unless the result has a smaller ulp. The latter
            can only happen if the input number is (up to sign) exactly a
            power of 2::

                sage: # needs sage.symbolic
                sage: a - a.ulp()/3 == a
                True
                sage: a + a.ulp()/3 == a
                True
                sage: b - b.ulp()/3 == b
                True
                sage: b + b.ulp()/3 == b
                True

                sage: c = RDF(1)
                sage: c - c.ulp()/3 == c
                False
                sage: c.ulp()
                2.220446049250313e-16
                sage: (c - c.ulp()).ulp()
                1.1102230246251565e-16

            The ulp is always positive::

                sage: RDF(-1).ulp()
                2.220446049250313e-16

            The ulp of zero is the smallest positive number in RDF::

                sage: RDF(0).ulp()
                5e-324
                sage: RDF(0).ulp()/2
                0.0

            Some special values::

                sage: a = RDF(1)/RDF(0); a
                +infinity
                sage: a.ulp()
                +infinity
                sage: (-a).ulp()
                +infinity
                sage: a = RDF('nan')
                sage: a.ulp() is a
                True

            The ulp method works correctly with small numbers::

                sage: u = RDF(0).ulp()
                sage: u.ulp() == u
                True
                sage: x = u * (2^52-1)  # largest denormal number
                sage: x.ulp() == u
                True
                sage: x = u * 2^52  # smallest normal number
                sage: x.ulp() == u
                True"""
        @overload
        def ulp(self) -> Any:
            """RealDoubleElement.ulp(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 762)

            Return the unit of least precision of ``self``, which is the
            weight of the least significant bit of ``self``. This is always
            a strictly positive number. It is also the gap between this
            number and the closest number with larger absolute value that
            can be represented.

            EXAMPLES::

                sage: a = RDF(pi)                                                           # needs sage.symbolic
                sage: a.ulp()                                                               # needs sage.symbolic
                4.440892098500626e-16
                sage: b = a + a.ulp()                                                       # needs sage.symbolic

            Adding or subtracting an ulp always gives a different number::

                sage: # needs sage.symbolic
                sage: a + a.ulp() == a
                False
                sage: a - a.ulp() == a
                False
                sage: b + b.ulp() == b
                False
                sage: b - b.ulp() == b
                False

            Since the default rounding mode is round-to-nearest, adding or
            subtracting something less than half an ulp always gives the
            same number, unless the result has a smaller ulp. The latter
            can only happen if the input number is (up to sign) exactly a
            power of 2::

                sage: # needs sage.symbolic
                sage: a - a.ulp()/3 == a
                True
                sage: a + a.ulp()/3 == a
                True
                sage: b - b.ulp()/3 == b
                True
                sage: b + b.ulp()/3 == b
                True

                sage: c = RDF(1)
                sage: c - c.ulp()/3 == c
                False
                sage: c.ulp()
                2.220446049250313e-16
                sage: (c - c.ulp()).ulp()
                1.1102230246251565e-16

            The ulp is always positive::

                sage: RDF(-1).ulp()
                2.220446049250313e-16

            The ulp of zero is the smallest positive number in RDF::

                sage: RDF(0).ulp()
                5e-324
                sage: RDF(0).ulp()/2
                0.0

            Some special values::

                sage: a = RDF(1)/RDF(0); a
                +infinity
                sage: a.ulp()
                +infinity
                sage: (-a).ulp()
                +infinity
                sage: a = RDF('nan')
                sage: a.ulp() is a
                True

            The ulp method works correctly with small numbers::

                sage: u = RDF(0).ulp()
                sage: u.ulp() == u
                True
                sage: x = u * (2^52-1)  # largest denormal number
                sage: x.ulp() == u
                True
                sage: x = u * 2^52  # smallest normal number
                sage: x.ulp() == u
                True"""
        @overload
        def ulp(self) -> Any:
            """RealDoubleElement.ulp(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 762)

            Return the unit of least precision of ``self``, which is the
            weight of the least significant bit of ``self``. This is always
            a strictly positive number. It is also the gap between this
            number and the closest number with larger absolute value that
            can be represented.

            EXAMPLES::

                sage: a = RDF(pi)                                                           # needs sage.symbolic
                sage: a.ulp()                                                               # needs sage.symbolic
                4.440892098500626e-16
                sage: b = a + a.ulp()                                                       # needs sage.symbolic

            Adding or subtracting an ulp always gives a different number::

                sage: # needs sage.symbolic
                sage: a + a.ulp() == a
                False
                sage: a - a.ulp() == a
                False
                sage: b + b.ulp() == b
                False
                sage: b - b.ulp() == b
                False

            Since the default rounding mode is round-to-nearest, adding or
            subtracting something less than half an ulp always gives the
            same number, unless the result has a smaller ulp. The latter
            can only happen if the input number is (up to sign) exactly a
            power of 2::

                sage: # needs sage.symbolic
                sage: a - a.ulp()/3 == a
                True
                sage: a + a.ulp()/3 == a
                True
                sage: b - b.ulp()/3 == b
                True
                sage: b + b.ulp()/3 == b
                True

                sage: c = RDF(1)
                sage: c - c.ulp()/3 == c
                False
                sage: c.ulp()
                2.220446049250313e-16
                sage: (c - c.ulp()).ulp()
                1.1102230246251565e-16

            The ulp is always positive::

                sage: RDF(-1).ulp()
                2.220446049250313e-16

            The ulp of zero is the smallest positive number in RDF::

                sage: RDF(0).ulp()
                5e-324
                sage: RDF(0).ulp()/2
                0.0

            Some special values::

                sage: a = RDF(1)/RDF(0); a
                +infinity
                sage: a.ulp()
                +infinity
                sage: (-a).ulp()
                +infinity
                sage: a = RDF('nan')
                sage: a.ulp() is a
                True

            The ulp method works correctly with small numbers::

                sage: u = RDF(0).ulp()
                sage: u.ulp() == u
                True
                sage: x = u * (2^52-1)  # largest denormal number
                sage: x.ulp() == u
                True
                sage: x = u * 2^52  # smallest normal number
                sage: x.ulp() == u
                True"""
        @overload
        def ulp(self) -> Any:
            """RealDoubleElement.ulp(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 762)

            Return the unit of least precision of ``self``, which is the
            weight of the least significant bit of ``self``. This is always
            a strictly positive number. It is also the gap between this
            number and the closest number with larger absolute value that
            can be represented.

            EXAMPLES::

                sage: a = RDF(pi)                                                           # needs sage.symbolic
                sage: a.ulp()                                                               # needs sage.symbolic
                4.440892098500626e-16
                sage: b = a + a.ulp()                                                       # needs sage.symbolic

            Adding or subtracting an ulp always gives a different number::

                sage: # needs sage.symbolic
                sage: a + a.ulp() == a
                False
                sage: a - a.ulp() == a
                False
                sage: b + b.ulp() == b
                False
                sage: b - b.ulp() == b
                False

            Since the default rounding mode is round-to-nearest, adding or
            subtracting something less than half an ulp always gives the
            same number, unless the result has a smaller ulp. The latter
            can only happen if the input number is (up to sign) exactly a
            power of 2::

                sage: # needs sage.symbolic
                sage: a - a.ulp()/3 == a
                True
                sage: a + a.ulp()/3 == a
                True
                sage: b - b.ulp()/3 == b
                True
                sage: b + b.ulp()/3 == b
                True

                sage: c = RDF(1)
                sage: c - c.ulp()/3 == c
                False
                sage: c.ulp()
                2.220446049250313e-16
                sage: (c - c.ulp()).ulp()
                1.1102230246251565e-16

            The ulp is always positive::

                sage: RDF(-1).ulp()
                2.220446049250313e-16

            The ulp of zero is the smallest positive number in RDF::

                sage: RDF(0).ulp()
                5e-324
                sage: RDF(0).ulp()/2
                0.0

            Some special values::

                sage: a = RDF(1)/RDF(0); a
                +infinity
                sage: a.ulp()
                +infinity
                sage: (-a).ulp()
                +infinity
                sage: a = RDF('nan')
                sage: a.ulp() is a
                True

            The ulp method works correctly with small numbers::

                sage: u = RDF(0).ulp()
                sage: u.ulp() == u
                True
                sage: x = u * (2^52-1)  # largest denormal number
                sage: x.ulp() == u
                True
                sage: x = u * 2^52  # smallest normal number
                sage: x.ulp() == u
                True"""
        @overload
        def ulp(self) -> Any:
            """RealDoubleElement.ulp(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 762)

            Return the unit of least precision of ``self``, which is the
            weight of the least significant bit of ``self``. This is always
            a strictly positive number. It is also the gap between this
            number and the closest number with larger absolute value that
            can be represented.

            EXAMPLES::

                sage: a = RDF(pi)                                                           # needs sage.symbolic
                sage: a.ulp()                                                               # needs sage.symbolic
                4.440892098500626e-16
                sage: b = a + a.ulp()                                                       # needs sage.symbolic

            Adding or subtracting an ulp always gives a different number::

                sage: # needs sage.symbolic
                sage: a + a.ulp() == a
                False
                sage: a - a.ulp() == a
                False
                sage: b + b.ulp() == b
                False
                sage: b - b.ulp() == b
                False

            Since the default rounding mode is round-to-nearest, adding or
            subtracting something less than half an ulp always gives the
            same number, unless the result has a smaller ulp. The latter
            can only happen if the input number is (up to sign) exactly a
            power of 2::

                sage: # needs sage.symbolic
                sage: a - a.ulp()/3 == a
                True
                sage: a + a.ulp()/3 == a
                True
                sage: b - b.ulp()/3 == b
                True
                sage: b + b.ulp()/3 == b
                True

                sage: c = RDF(1)
                sage: c - c.ulp()/3 == c
                False
                sage: c.ulp()
                2.220446049250313e-16
                sage: (c - c.ulp()).ulp()
                1.1102230246251565e-16

            The ulp is always positive::

                sage: RDF(-1).ulp()
                2.220446049250313e-16

            The ulp of zero is the smallest positive number in RDF::

                sage: RDF(0).ulp()
                5e-324
                sage: RDF(0).ulp()/2
                0.0

            Some special values::

                sage: a = RDF(1)/RDF(0); a
                +infinity
                sage: a.ulp()
                +infinity
                sage: (-a).ulp()
                +infinity
                sage: a = RDF('nan')
                sage: a.ulp() is a
                True

            The ulp method works correctly with small numbers::

                sage: u = RDF(0).ulp()
                sage: u.ulp() == u
                True
                sage: x = u * (2^52-1)  # largest denormal number
                sage: x.ulp() == u
                True
                sage: x = u * 2^52  # smallest normal number
                sage: x.ulp() == u
                True"""
        @overload
        def ulp(self) -> Any:
            """RealDoubleElement.ulp(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 762)

            Return the unit of least precision of ``self``, which is the
            weight of the least significant bit of ``self``. This is always
            a strictly positive number. It is also the gap between this
            number and the closest number with larger absolute value that
            can be represented.

            EXAMPLES::

                sage: a = RDF(pi)                                                           # needs sage.symbolic
                sage: a.ulp()                                                               # needs sage.symbolic
                4.440892098500626e-16
                sage: b = a + a.ulp()                                                       # needs sage.symbolic

            Adding or subtracting an ulp always gives a different number::

                sage: # needs sage.symbolic
                sage: a + a.ulp() == a
                False
                sage: a - a.ulp() == a
                False
                sage: b + b.ulp() == b
                False
                sage: b - b.ulp() == b
                False

            Since the default rounding mode is round-to-nearest, adding or
            subtracting something less than half an ulp always gives the
            same number, unless the result has a smaller ulp. The latter
            can only happen if the input number is (up to sign) exactly a
            power of 2::

                sage: # needs sage.symbolic
                sage: a - a.ulp()/3 == a
                True
                sage: a + a.ulp()/3 == a
                True
                sage: b - b.ulp()/3 == b
                True
                sage: b + b.ulp()/3 == b
                True

                sage: c = RDF(1)
                sage: c - c.ulp()/3 == c
                False
                sage: c.ulp()
                2.220446049250313e-16
                sage: (c - c.ulp()).ulp()
                1.1102230246251565e-16

            The ulp is always positive::

                sage: RDF(-1).ulp()
                2.220446049250313e-16

            The ulp of zero is the smallest positive number in RDF::

                sage: RDF(0).ulp()
                5e-324
                sage: RDF(0).ulp()/2
                0.0

            Some special values::

                sage: a = RDF(1)/RDF(0); a
                +infinity
                sage: a.ulp()
                +infinity
                sage: (-a).ulp()
                +infinity
                sage: a = RDF('nan')
                sage: a.ulp() is a
                True

            The ulp method works correctly with small numbers::

                sage: u = RDF(0).ulp()
                sage: u.ulp() == u
                True
                sage: x = u * (2^52-1)  # largest denormal number
                sage: x.ulp() == u
                True
                sage: x = u * 2^52  # smallest normal number
                sage: x.ulp() == u
                True"""
        @overload
        def ulp(self) -> Any:
            """RealDoubleElement.ulp(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 762)

            Return the unit of least precision of ``self``, which is the
            weight of the least significant bit of ``self``. This is always
            a strictly positive number. It is also the gap between this
            number and the closest number with larger absolute value that
            can be represented.

            EXAMPLES::

                sage: a = RDF(pi)                                                           # needs sage.symbolic
                sage: a.ulp()                                                               # needs sage.symbolic
                4.440892098500626e-16
                sage: b = a + a.ulp()                                                       # needs sage.symbolic

            Adding or subtracting an ulp always gives a different number::

                sage: # needs sage.symbolic
                sage: a + a.ulp() == a
                False
                sage: a - a.ulp() == a
                False
                sage: b + b.ulp() == b
                False
                sage: b - b.ulp() == b
                False

            Since the default rounding mode is round-to-nearest, adding or
            subtracting something less than half an ulp always gives the
            same number, unless the result has a smaller ulp. The latter
            can only happen if the input number is (up to sign) exactly a
            power of 2::

                sage: # needs sage.symbolic
                sage: a - a.ulp()/3 == a
                True
                sage: a + a.ulp()/3 == a
                True
                sage: b - b.ulp()/3 == b
                True
                sage: b + b.ulp()/3 == b
                True

                sage: c = RDF(1)
                sage: c - c.ulp()/3 == c
                False
                sage: c.ulp()
                2.220446049250313e-16
                sage: (c - c.ulp()).ulp()
                1.1102230246251565e-16

            The ulp is always positive::

                sage: RDF(-1).ulp()
                2.220446049250313e-16

            The ulp of zero is the smallest positive number in RDF::

                sage: RDF(0).ulp()
                5e-324
                sage: RDF(0).ulp()/2
                0.0

            Some special values::

                sage: a = RDF(1)/RDF(0); a
                +infinity
                sage: a.ulp()
                +infinity
                sage: (-a).ulp()
                +infinity
                sage: a = RDF('nan')
                sage: a.ulp() is a
                True

            The ulp method works correctly with small numbers::

                sage: u = RDF(0).ulp()
                sage: u.ulp() == u
                True
                sage: x = u * (2^52-1)  # largest denormal number
                sage: x.ulp() == u
                True
                sage: x = u * 2^52  # smallest normal number
                sage: x.ulp() == u
                True"""
        @overload
        def ulp(self) -> Any:
            """RealDoubleElement.ulp(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 762)

            Return the unit of least precision of ``self``, which is the
            weight of the least significant bit of ``self``. This is always
            a strictly positive number. It is also the gap between this
            number and the closest number with larger absolute value that
            can be represented.

            EXAMPLES::

                sage: a = RDF(pi)                                                           # needs sage.symbolic
                sage: a.ulp()                                                               # needs sage.symbolic
                4.440892098500626e-16
                sage: b = a + a.ulp()                                                       # needs sage.symbolic

            Adding or subtracting an ulp always gives a different number::

                sage: # needs sage.symbolic
                sage: a + a.ulp() == a
                False
                sage: a - a.ulp() == a
                False
                sage: b + b.ulp() == b
                False
                sage: b - b.ulp() == b
                False

            Since the default rounding mode is round-to-nearest, adding or
            subtracting something less than half an ulp always gives the
            same number, unless the result has a smaller ulp. The latter
            can only happen if the input number is (up to sign) exactly a
            power of 2::

                sage: # needs sage.symbolic
                sage: a - a.ulp()/3 == a
                True
                sage: a + a.ulp()/3 == a
                True
                sage: b - b.ulp()/3 == b
                True
                sage: b + b.ulp()/3 == b
                True

                sage: c = RDF(1)
                sage: c - c.ulp()/3 == c
                False
                sage: c.ulp()
                2.220446049250313e-16
                sage: (c - c.ulp()).ulp()
                1.1102230246251565e-16

            The ulp is always positive::

                sage: RDF(-1).ulp()
                2.220446049250313e-16

            The ulp of zero is the smallest positive number in RDF::

                sage: RDF(0).ulp()
                5e-324
                sage: RDF(0).ulp()/2
                0.0

            Some special values::

                sage: a = RDF(1)/RDF(0); a
                +infinity
                sage: a.ulp()
                +infinity
                sage: (-a).ulp()
                +infinity
                sage: a = RDF('nan')
                sage: a.ulp() is a
                True

            The ulp method works correctly with small numbers::

                sage: u = RDF(0).ulp()
                sage: u.ulp() == u
                True
                sage: x = u * (2^52-1)  # largest denormal number
                sage: x.ulp() == u
                True
                sage: x = u * 2^52  # smallest normal number
                sage: x.ulp() == u
                True"""
        @overload
        def ulp(self) -> Any:
            """RealDoubleElement.ulp(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 762)

            Return the unit of least precision of ``self``, which is the
            weight of the least significant bit of ``self``. This is always
            a strictly positive number. It is also the gap between this
            number and the closest number with larger absolute value that
            can be represented.

            EXAMPLES::

                sage: a = RDF(pi)                                                           # needs sage.symbolic
                sage: a.ulp()                                                               # needs sage.symbolic
                4.440892098500626e-16
                sage: b = a + a.ulp()                                                       # needs sage.symbolic

            Adding or subtracting an ulp always gives a different number::

                sage: # needs sage.symbolic
                sage: a + a.ulp() == a
                False
                sage: a - a.ulp() == a
                False
                sage: b + b.ulp() == b
                False
                sage: b - b.ulp() == b
                False

            Since the default rounding mode is round-to-nearest, adding or
            subtracting something less than half an ulp always gives the
            same number, unless the result has a smaller ulp. The latter
            can only happen if the input number is (up to sign) exactly a
            power of 2::

                sage: # needs sage.symbolic
                sage: a - a.ulp()/3 == a
                True
                sage: a + a.ulp()/3 == a
                True
                sage: b - b.ulp()/3 == b
                True
                sage: b + b.ulp()/3 == b
                True

                sage: c = RDF(1)
                sage: c - c.ulp()/3 == c
                False
                sage: c.ulp()
                2.220446049250313e-16
                sage: (c - c.ulp()).ulp()
                1.1102230246251565e-16

            The ulp is always positive::

                sage: RDF(-1).ulp()
                2.220446049250313e-16

            The ulp of zero is the smallest positive number in RDF::

                sage: RDF(0).ulp()
                5e-324
                sage: RDF(0).ulp()/2
                0.0

            Some special values::

                sage: a = RDF(1)/RDF(0); a
                +infinity
                sage: a.ulp()
                +infinity
                sage: (-a).ulp()
                +infinity
                sage: a = RDF('nan')
                sage: a.ulp() is a
                True

            The ulp method works correctly with small numbers::

                sage: u = RDF(0).ulp()
                sage: u.ulp() == u
                True
                sage: x = u * (2^52-1)  # largest denormal number
                sage: x.ulp() == u
                True
                sage: x = u * 2^52  # smallest normal number
                sage: x.ulp() == u
                True"""
        @overload
        def ulp(self) -> Any:
            """RealDoubleElement.ulp(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 762)

            Return the unit of least precision of ``self``, which is the
            weight of the least significant bit of ``self``. This is always
            a strictly positive number. It is also the gap between this
            number and the closest number with larger absolute value that
            can be represented.

            EXAMPLES::

                sage: a = RDF(pi)                                                           # needs sage.symbolic
                sage: a.ulp()                                                               # needs sage.symbolic
                4.440892098500626e-16
                sage: b = a + a.ulp()                                                       # needs sage.symbolic

            Adding or subtracting an ulp always gives a different number::

                sage: # needs sage.symbolic
                sage: a + a.ulp() == a
                False
                sage: a - a.ulp() == a
                False
                sage: b + b.ulp() == b
                False
                sage: b - b.ulp() == b
                False

            Since the default rounding mode is round-to-nearest, adding or
            subtracting something less than half an ulp always gives the
            same number, unless the result has a smaller ulp. The latter
            can only happen if the input number is (up to sign) exactly a
            power of 2::

                sage: # needs sage.symbolic
                sage: a - a.ulp()/3 == a
                True
                sage: a + a.ulp()/3 == a
                True
                sage: b - b.ulp()/3 == b
                True
                sage: b + b.ulp()/3 == b
                True

                sage: c = RDF(1)
                sage: c - c.ulp()/3 == c
                False
                sage: c.ulp()
                2.220446049250313e-16
                sage: (c - c.ulp()).ulp()
                1.1102230246251565e-16

            The ulp is always positive::

                sage: RDF(-1).ulp()
                2.220446049250313e-16

            The ulp of zero is the smallest positive number in RDF::

                sage: RDF(0).ulp()
                5e-324
                sage: RDF(0).ulp()/2
                0.0

            Some special values::

                sage: a = RDF(1)/RDF(0); a
                +infinity
                sage: a.ulp()
                +infinity
                sage: (-a).ulp()
                +infinity
                sage: a = RDF('nan')
                sage: a.ulp() is a
                True

            The ulp method works correctly with small numbers::

                sage: u = RDF(0).ulp()
                sage: u.ulp() == u
                True
                sage: x = u * (2^52-1)  # largest denormal number
                sage: x.ulp() == u
                True
                sage: x = u * 2^52  # smallest normal number
                sage: x.ulp() == u
                True"""
        @overload
        def ulp(self) -> Any:
            """RealDoubleElement.ulp(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 762)

            Return the unit of least precision of ``self``, which is the
            weight of the least significant bit of ``self``. This is always
            a strictly positive number. It is also the gap between this
            number and the closest number with larger absolute value that
            can be represented.

            EXAMPLES::

                sage: a = RDF(pi)                                                           # needs sage.symbolic
                sage: a.ulp()                                                               # needs sage.symbolic
                4.440892098500626e-16
                sage: b = a + a.ulp()                                                       # needs sage.symbolic

            Adding or subtracting an ulp always gives a different number::

                sage: # needs sage.symbolic
                sage: a + a.ulp() == a
                False
                sage: a - a.ulp() == a
                False
                sage: b + b.ulp() == b
                False
                sage: b - b.ulp() == b
                False

            Since the default rounding mode is round-to-nearest, adding or
            subtracting something less than half an ulp always gives the
            same number, unless the result has a smaller ulp. The latter
            can only happen if the input number is (up to sign) exactly a
            power of 2::

                sage: # needs sage.symbolic
                sage: a - a.ulp()/3 == a
                True
                sage: a + a.ulp()/3 == a
                True
                sage: b - b.ulp()/3 == b
                True
                sage: b + b.ulp()/3 == b
                True

                sage: c = RDF(1)
                sage: c - c.ulp()/3 == c
                False
                sage: c.ulp()
                2.220446049250313e-16
                sage: (c - c.ulp()).ulp()
                1.1102230246251565e-16

            The ulp is always positive::

                sage: RDF(-1).ulp()
                2.220446049250313e-16

            The ulp of zero is the smallest positive number in RDF::

                sage: RDF(0).ulp()
                5e-324
                sage: RDF(0).ulp()/2
                0.0

            Some special values::

                sage: a = RDF(1)/RDF(0); a
                +infinity
                sage: a.ulp()
                +infinity
                sage: (-a).ulp()
                +infinity
                sage: a = RDF('nan')
                sage: a.ulp() is a
                True

            The ulp method works correctly with small numbers::

                sage: u = RDF(0).ulp()
                sage: u.ulp() == u
                True
                sage: x = u * (2^52-1)  # largest denormal number
                sage: x.ulp() == u
                True
                sage: x = u * 2^52  # smallest normal number
                sage: x.ulp() == u
                True"""
        @overload
        def ulp(self) -> Any:
            """RealDoubleElement.ulp(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 762)

            Return the unit of least precision of ``self``, which is the
            weight of the least significant bit of ``self``. This is always
            a strictly positive number. It is also the gap between this
            number and the closest number with larger absolute value that
            can be represented.

            EXAMPLES::

                sage: a = RDF(pi)                                                           # needs sage.symbolic
                sage: a.ulp()                                                               # needs sage.symbolic
                4.440892098500626e-16
                sage: b = a + a.ulp()                                                       # needs sage.symbolic

            Adding or subtracting an ulp always gives a different number::

                sage: # needs sage.symbolic
                sage: a + a.ulp() == a
                False
                sage: a - a.ulp() == a
                False
                sage: b + b.ulp() == b
                False
                sage: b - b.ulp() == b
                False

            Since the default rounding mode is round-to-nearest, adding or
            subtracting something less than half an ulp always gives the
            same number, unless the result has a smaller ulp. The latter
            can only happen if the input number is (up to sign) exactly a
            power of 2::

                sage: # needs sage.symbolic
                sage: a - a.ulp()/3 == a
                True
                sage: a + a.ulp()/3 == a
                True
                sage: b - b.ulp()/3 == b
                True
                sage: b + b.ulp()/3 == b
                True

                sage: c = RDF(1)
                sage: c - c.ulp()/3 == c
                False
                sage: c.ulp()
                2.220446049250313e-16
                sage: (c - c.ulp()).ulp()
                1.1102230246251565e-16

            The ulp is always positive::

                sage: RDF(-1).ulp()
                2.220446049250313e-16

            The ulp of zero is the smallest positive number in RDF::

                sage: RDF(0).ulp()
                5e-324
                sage: RDF(0).ulp()/2
                0.0

            Some special values::

                sage: a = RDF(1)/RDF(0); a
                +infinity
                sage: a.ulp()
                +infinity
                sage: (-a).ulp()
                +infinity
                sage: a = RDF('nan')
                sage: a.ulp() is a
                True

            The ulp method works correctly with small numbers::

                sage: u = RDF(0).ulp()
                sage: u.ulp() == u
                True
                sage: x = u * (2^52-1)  # largest denormal number
                sage: x.ulp() == u
                True
                sage: x = u * 2^52  # smallest normal number
                sage: x.ulp() == u
                True"""
        @overload
        def ulp(self) -> Any:
            """RealDoubleElement.ulp(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 762)

            Return the unit of least precision of ``self``, which is the
            weight of the least significant bit of ``self``. This is always
            a strictly positive number. It is also the gap between this
            number and the closest number with larger absolute value that
            can be represented.

            EXAMPLES::

                sage: a = RDF(pi)                                                           # needs sage.symbolic
                sage: a.ulp()                                                               # needs sage.symbolic
                4.440892098500626e-16
                sage: b = a + a.ulp()                                                       # needs sage.symbolic

            Adding or subtracting an ulp always gives a different number::

                sage: # needs sage.symbolic
                sage: a + a.ulp() == a
                False
                sage: a - a.ulp() == a
                False
                sage: b + b.ulp() == b
                False
                sage: b - b.ulp() == b
                False

            Since the default rounding mode is round-to-nearest, adding or
            subtracting something less than half an ulp always gives the
            same number, unless the result has a smaller ulp. The latter
            can only happen if the input number is (up to sign) exactly a
            power of 2::

                sage: # needs sage.symbolic
                sage: a - a.ulp()/3 == a
                True
                sage: a + a.ulp()/3 == a
                True
                sage: b - b.ulp()/3 == b
                True
                sage: b + b.ulp()/3 == b
                True

                sage: c = RDF(1)
                sage: c - c.ulp()/3 == c
                False
                sage: c.ulp()
                2.220446049250313e-16
                sage: (c - c.ulp()).ulp()
                1.1102230246251565e-16

            The ulp is always positive::

                sage: RDF(-1).ulp()
                2.220446049250313e-16

            The ulp of zero is the smallest positive number in RDF::

                sage: RDF(0).ulp()
                5e-324
                sage: RDF(0).ulp()/2
                0.0

            Some special values::

                sage: a = RDF(1)/RDF(0); a
                +infinity
                sage: a.ulp()
                +infinity
                sage: (-a).ulp()
                +infinity
                sage: a = RDF('nan')
                sage: a.ulp() is a
                True

            The ulp method works correctly with small numbers::

                sage: u = RDF(0).ulp()
                sage: u.ulp() == u
                True
                sage: x = u * (2^52-1)  # largest denormal number
                sage: x.ulp() == u
                True
                sage: x = u * 2^52  # smallest normal number
                sage: x.ulp() == u
                True"""
        def __abs__(self) -> Any:
            """RealDoubleElement.__abs__(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1390)

            Return the absolute value of ``self``.

            EXAMPLES::

                sage: abs(RDF(1.5))
                1.5
                sage: abs(RDF(-1.5))
                1.5
                sage: abs(RDF(0.0))
                0.0
                sage: abs(RDF(-0.0))
                0.0"""
        def __complex__(self) -> Any:
            """RealDoubleElement.__complex__(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 890)

            Return ``self`` as a python complex number.

            EXAMPLES::

                sage: a = 2303
                sage: RDF(a)
                2303.0
                sage: complex(RDF(a))
                (2303+0j)"""
        @overload
        def __copy__(self) -> Any:
            """RealDoubleElement.__copy__(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1185)

            Return copy of ``self``, which since ``self`` is immutable, is just
            ``self``.

            EXAMPLES::

                sage: r = RDF('-1.6')
                sage: r.__copy__() is r
                True"""
        @overload
        def __copy__(self) -> Any:
            """RealDoubleElement.__copy__(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1185)

            Return copy of ``self``, which since ``self`` is immutable, is just
            ``self``.

            EXAMPLES::

                sage: r = RDF('-1.6')
                sage: r.__copy__() is r
                True"""
        def __deepcopy__(self, memo) -> Any:
            """RealDoubleElement.__deepcopy__(self, memo)

            File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1198)

            EXAMPLES::

                sage: r = RDF('-1.6')
                sage: deepcopy(r) is r
                True"""
        def __float__(self) -> Any:
            """RealDoubleElement.__float__(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1588)

            Return ``self`` as a python float.

            EXAMPLES::

                sage: float(RDF(1.5))
                1.5
                sage: type(float(RDF(1.5)))
                <... 'float'>"""
        def __format__(self, format_spec) -> Any:
            """RealDoubleElement.__format__(self, format_spec)

            File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1095)

            Return a formatted string representation of this real number.

            EXAMPLES::

                sage: format(RDF(32/3), '.4f')
                '10.6667'
                sage: '{:.4e}'.format(RDF(2/3))
                '6.6667e-01'"""
        def __hash__(self) -> Any:
            """RealDoubleElement.__hash__(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1128)

            Return the hash of ``self``, which coincides with the python float
            (and often int) type.

            EXAMPLES::

                sage: hash(RDF(1.2)) == hash(1.2r)
                True"""
        def __int__(self) -> Any:
            """RealDoubleElement.__int__(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1616)

            Return integer truncation of this real number.

            EXAMPLES::

                sage: int(RDF(2.99))
                2
                sage: int(RDF(-2.99))
                -2"""
        @overload
        def __invert__(self) -> Any:
            """RealDoubleElement.__invert__(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1295)

            Compute the multiplicative inverse of ``self``.

            EXAMPLES::

                sage: a = RDF(-1.5)*RDF(2.5)
                sage: a.__invert__()
                -0.26666666666666666
                sage: ~a
                -0.26666666666666666"""
        @overload
        def __invert__(self) -> Any:
            """RealDoubleElement.__invert__(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1295)

            Compute the multiplicative inverse of ``self``.

            EXAMPLES::

                sage: a = RDF(-1.5)*RDF(2.5)
                sage: a.__invert__()
                -0.26666666666666666
                sage: ~a
                -0.26666666666666666"""
        def __lshift__(self, x, y) -> Any:
            """RealDoubleElement.__lshift__(x, y)

            File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1427)

            LShifting a double is not supported; nor is lshifting a
            :class:`RealDoubleElement`.

            TESTS::

                sage: RDF(2) << 3
                Traceback (most recent call last):
                ...
                TypeError: unsupported operand type(s) for <<"""
        @overload
        def __mpfr__(self) -> Any:
            '''RealDoubleElement.__mpfr__(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 932)

            Convert Sage ``RealDoubleElement`` to gmpy2 ``mpfr``.

            EXAMPLES::

                sage: RDF(42.2).__mpfr__()
                mpfr(\'42.200000000000003\')
                sage: from gmpy2 import mpfr
                sage: mpfr(RDF(5.1))
                mpfr(\'5.0999999999999996\')

            TESTS::

                sage: RDF().__mpfr__(); raise NotImplementedError("gmpy2 is not installed")
                Traceback (most recent call last):
                ...
                NotImplementedError: gmpy2 is not installed'''
        @overload
        def __mpfr__(self) -> Any:
            '''RealDoubleElement.__mpfr__(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 932)

            Convert Sage ``RealDoubleElement`` to gmpy2 ``mpfr``.

            EXAMPLES::

                sage: RDF(42.2).__mpfr__()
                mpfr(\'42.200000000000003\')
                sage: from gmpy2 import mpfr
                sage: mpfr(RDF(5.1))
                mpfr(\'5.0999999999999996\')

            TESTS::

                sage: RDF().__mpfr__(); raise NotImplementedError("gmpy2 is not installed")
                Traceback (most recent call last):
                ...
                NotImplementedError: gmpy2 is not installed'''
        @overload
        def __mpfr__(self) -> Any:
            '''RealDoubleElement.__mpfr__(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 932)

            Convert Sage ``RealDoubleElement`` to gmpy2 ``mpfr``.

            EXAMPLES::

                sage: RDF(42.2).__mpfr__()
                mpfr(\'42.200000000000003\')
                sage: from gmpy2 import mpfr
                sage: mpfr(RDF(5.1))
                mpfr(\'5.0999999999999996\')

            TESTS::

                sage: RDF().__mpfr__(); raise NotImplementedError("gmpy2 is not installed")
                Traceback (most recent call last):
                ...
                NotImplementedError: gmpy2 is not installed'''
        def __neg__(self) -> Any:
            """RealDoubleElement.__neg__(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1365)

            Negate ``self``.

            EXAMPLES::

                sage: -RDF('-1.5')
                1.5"""
        @overload
        def __pari__(self) -> Any:
            """RealDoubleElement.__pari__(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1662)

            Return a PARI representation of ``self``.

            EXAMPLES::

                sage: RDF(1.5).__pari__()                                                   # needs sage.libs.pari
                1.50000000000000"""
        @overload
        def __pari__(self) -> Any:
            """RealDoubleElement.__pari__(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1662)

            Return a PARI representation of ``self``.

            EXAMPLES::

                sage: RDF(1.5).__pari__()                                                   # needs sage.libs.pari
                1.50000000000000"""
        def __reduce__(self) -> Any:
            """RealDoubleElement.__reduce__(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 731)

            For pickling.

            EXAMPLES::

                sage: a = RDF(-2.7)
                sage: loads(dumps(a)) == a
                True"""
        def __rlshift__(self, other):
            """Return value<<self."""
        def __rrshift__(self, other):
            """Return value>>self."""
        def __rshift__(self, x, y) -> Any:
            """RealDoubleElement.__rshift__(x, y)

            File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1441)

            RShifting a double is not supported; nor is rshifting a
            :class:`RealDoubleElement`.

            TESTS::

                sage: RDF(2) >> 3
                Traceback (most recent call last):
                ...
                TypeError: unsupported operand type(s) for >>"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 125)

                Initialize ``self``.

                TESTS::

                    sage: R = RealDoubleField()
                    sage: TestSuite(R).run()
        """
    @overload
    def NaN(self) -> Any:
        """RealDoubleField_class.NaN(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 595)

        Return Not-a-Number ``NaN``.

        EXAMPLES::

            sage: RDF.NaN()
            NaN"""
    @overload
    def NaN(self) -> Any:
        """RealDoubleField_class.NaN(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 595)

        Return Not-a-Number ``NaN``.

        EXAMPLES::

            sage: RDF.NaN()
            NaN"""
    @overload
    def algebraic_closure(self) -> Any:
        """RealDoubleField_class.algebraic_closure(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 269)

        Return the algebraic closure of ``self``, i.e., the complex double
        field.

        EXAMPLES::

            sage: RDF.algebraic_closure()                                               # needs sage.rings.complex_double
            Complex Double Field"""
    @overload
    def algebraic_closure(self) -> Any:
        """RealDoubleField_class.algebraic_closure(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 269)

        Return the algebraic closure of ``self``, i.e., the complex double
        field.

        EXAMPLES::

            sage: RDF.algebraic_closure()                                               # needs sage.rings.complex_double
            Complex Double Field"""
    @overload
    def characteristic(self) -> Any:
        """RealDoubleField_class.characteristic(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 464)

        Return 0, since the field of real numbers has characteristic 0.

        EXAMPLES::

            sage: RDF.characteristic()
            0"""
    @overload
    def characteristic(self) -> Any:
        """RealDoubleField_class.characteristic(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 464)

        Return 0, since the field of real numbers has characteristic 0.

        EXAMPLES::

            sage: RDF.characteristic()
            0"""
    @overload
    def complex_field(self) -> Any:
        """RealDoubleField_class.complex_field(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 256)

        Return the complex field with the same precision as ``self``, i.e.,
        the complex double field.

        EXAMPLES::

            sage: RDF.complex_field()                                                   # needs sage.rings.complex_double
            Complex Double Field"""
    @overload
    def complex_field(self) -> Any:
        """RealDoubleField_class.complex_field(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 256)

        Return the complex field with the same precision as ``self``, i.e.,
        the complex double field.

        EXAMPLES::

            sage: RDF.complex_field()                                                   # needs sage.rings.complex_double
            Complex Double Field"""
    def construction(self) -> Any:
        """RealDoubleField_class.construction(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 235)

        Return the functorial construction of ``self``, namely, completion of
        the rational numbers with respect to the prime at `\\infty`.

        Also preserves other information that makes this field unique (i.e.
        the Real Double Field).

        EXAMPLES::

            sage: c, S = RDF.construction(); S
            Rational Field
            sage: RDF == c(S)
            True"""
    def euler_constant(self) -> Any:
        """RealDoubleField_class.euler_constant(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 538)

        Return Euler's gamma constant to double precision.

        EXAMPLES::

            sage: RDF.euler_constant()
            0.5772156649015329"""
    def factorial(self, intn) -> Any:
        """RealDoubleField_class.factorial(self, int n)

        File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 562)

        Return the factorial of the integer `n` as a real number.

        EXAMPLES::

            sage: RDF.factorial(100)
            9.332621544394415e+157"""
    def gen(self, n=...) -> Any:
        """RealDoubleField_class.gen(self, n=0)

        File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 438)

        Return the generator of the real double field.

        EXAMPLES::

            sage: RDF.0
            1.0
            sage: RDF.gens()
            (1.0,)"""
    @overload
    def is_exact(self) -> bool:
        """RealDoubleField_class.is_exact(self) -> bool

        File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 153)

        Return ``False``, because doubles are not exact.

        EXAMPLES::

            sage: RDF.is_exact()
            False"""
    @overload
    def is_exact(self) -> Any:
        """RealDoubleField_class.is_exact(self) -> bool

        File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 153)

        Return ``False``, because doubles are not exact.

        EXAMPLES::

            sage: RDF.is_exact()
            False"""
    def log2(self) -> Any:
        """RealDoubleField_class.log2(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 549)

        Return `\\log(2)` to the precision of this field.

        EXAMPLES::

            sage: RDF.log2()
            0.6931471805599453
            sage: RDF(2).log()
            0.6931471805599453"""
    @overload
    def name(self) -> Any:
        """RealDoubleField_class.name(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 499)

        The name of ``self``.

        EXAMPLES::

            sage: RDF.name()
            'RealDoubleField'"""
    @overload
    def name(self) -> Any:
        """RealDoubleField_class.name(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 499)

        The name of ``self``.

        EXAMPLES::

            sage: RDF.name()
            'RealDoubleField'"""
    def nan(self, *args, **kwargs):
        """RealDoubleField_class.NaN(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 595)

        Return Not-a-Number ``NaN``.

        EXAMPLES::

            sage: RDF.NaN()
            NaN"""
    @overload
    def ngens(self) -> Any:
        """RealDoubleField_class.ngens(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 453)

        Return the number of generators which is always 1.

        EXAMPLES::

            sage: RDF.ngens()
            1"""
    @overload
    def ngens(self) -> Any:
        """RealDoubleField_class.ngens(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 453)

        Return the number of generators which is always 1.

        EXAMPLES::

            sage: RDF.ngens()
            1"""
    def pi(self) -> Any:
        """RealDoubleField_class.pi(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 525)

        Return `\\pi` to double-precision.

        EXAMPLES::

            sage: RDF.pi()
            3.141592653589793
            sage: RDF.pi().sqrt()/2
            0.8862269254527579"""
    def prec(self, *args, **kwargs):
        """RealDoubleField_class.precision(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 405)

        Return the precision of this real double field in bits.

        Always returns 53.

        EXAMPLES::

            sage: RDF.precision()
            53"""
    @overload
    def precision(self) -> Any:
        """RealDoubleField_class.precision(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 405)

        Return the precision of this real double field in bits.

        Always returns 53.

        EXAMPLES::

            sage: RDF.precision()
            53"""
    @overload
    def precision(self) -> Any:
        """RealDoubleField_class.precision(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 405)

        Return the precision of this real double field in bits.

        Always returns 53.

        EXAMPLES::

            sage: RDF.precision()
            53"""
    @overload
    def random_element(self, doublemin=..., doublemax=...) -> Any:
        """RealDoubleField_class.random_element(self, double min=-1, double max=1)

        File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 481)

        Return a random element of this real double field in the interval
        ``[min, max]``.

        EXAMPLES::

            sage: RDF.random_element().parent() is RDF
            True
            sage: -1 <= RDF.random_element() <= 1
            True
            sage: 100 <= RDF.random_element(min=100, max=110) <= 110
            True"""
    @overload
    def random_element(self) -> Any:
        """RealDoubleField_class.random_element(self, double min=-1, double max=1)

        File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 481)

        Return a random element of this real double field in the interval
        ``[min, max]``.

        EXAMPLES::

            sage: RDF.random_element().parent() is RDF
            True
            sage: -1 <= RDF.random_element() <= 1
            True
            sage: 100 <= RDF.random_element(min=100, max=110) <= 110
            True"""
    @overload
    def random_element(self) -> Any:
        """RealDoubleField_class.random_element(self, double min=-1, double max=1)

        File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 481)

        Return a random element of this real double field in the interval
        ``[min, max]``.

        EXAMPLES::

            sage: RDF.random_element().parent() is RDF
            True
            sage: -1 <= RDF.random_element() <= 1
            True
            sage: 100 <= RDF.random_element(min=100, max=110) <= 110
            True"""
    @overload
    def random_element(self, min=..., max=...) -> Any:
        """RealDoubleField_class.random_element(self, double min=-1, double max=1)

        File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 481)

        Return a random element of this real double field in the interval
        ``[min, max]``.

        EXAMPLES::

            sage: RDF.random_element().parent() is RDF
            True
            sage: -1 <= RDF.random_element() <= 1
            True
            sage: 100 <= RDF.random_element(min=100, max=110) <= 110
            True"""
    def to_prec(self, prec) -> Any:
        """RealDoubleField_class.to_prec(self, prec)

        File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 420)

        Return the real field to the specified precision. As doubles have
        fixed precision, this will only return a real double field if ``prec``
        is exactly 53.

        EXAMPLES::

            sage: RDF.to_prec(52)                                                       # needs sage.rings.real_mpfr
            Real Field with 52 bits of precision
            sage: RDF.to_prec(53)
            Real Double Field"""
    @overload
    def zeta(self, n=...) -> Any:
        """RealDoubleField_class.zeta(self, n=2)

        File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 573)

        Return an `n`-th root of unity in the real field, if one
        exists, or raise a :exc:`ValueError` otherwise.

        EXAMPLES::

            sage: RDF.zeta()
            -1.0
            sage: RDF.zeta(1)
            1.0
            sage: RDF.zeta(5)
            Traceback (most recent call last):
            ...
            ValueError: No 5th root of unity in self"""
    @overload
    def zeta(self) -> Any:
        """RealDoubleField_class.zeta(self, n=2)

        File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 573)

        Return an `n`-th root of unity in the real field, if one
        exists, or raise a :exc:`ValueError` otherwise.

        EXAMPLES::

            sage: RDF.zeta()
            -1.0
            sage: RDF.zeta(1)
            1.0
            sage: RDF.zeta(5)
            Traceback (most recent call last):
            ...
            ValueError: No 5th root of unity in self"""
    def __eq__(self, other: object) -> bool:
        """Return self==value."""
    def __ge__(self, other: object) -> bool:
        """Return self>=value."""
    def __gt__(self, other: object) -> bool:
        """Return self>value."""
    def __hash__(self) -> Any:
        """RealDoubleField_class.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 510)

        Return the hash value of ``self``.

        This class is intended for use as a singleton so any instance
        of it should be equivalent from a hashing perspective.

        TESTS::

            sage: from sage.rings.real_double import RealDoubleField_class
            sage: hash(RDF) == hash(RealDoubleField_class())
            True"""
    def __le__(self, other: object) -> bool:
        """Return self<=value."""
    def __lt__(self, other: object) -> bool:
        """Return self<value."""
    def __ne__(self, other: object) -> bool:
        """Return self!=value."""
    def __reduce__(self) -> Any:
        """RealDoubleField_class.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 142)

        For pickling.

        EXAMPLES::

            sage: loads(dumps(RDF)) is RDF
            True"""

class ToRDF(sage.categories.morphism.Morphism):
    """ToRDF(R)"""
    def __init__(self, R):
        """File: /build/sagemath/src/sage/src/sage/rings/real_double.pyx (starting at line 1963)

                Fast morphism from anything with a ``__float__`` method to an ``RDF``
                element.

                EXAMPLES::

                    sage: f = RDF.coerce_map_from(ZZ); f
                    Native morphism:
                      From: Integer Ring
                      To:   Real Double Field
                    sage: f(4)
                    4.0
                    sage: f = RDF.coerce_map_from(QQ); f
                    Native morphism:
                      From: Rational Field
                      To:   Real Double Field
                    sage: f(1/2)
                    0.5
                    sage: f = RDF.coerce_map_from(int); f
                    Native morphism:
                      From: Set of Python objects of class 'int'
                      To:   Real Double Field
                    sage: f(3r)
                    3.0
                    sage: f = RDF.coerce_map_from(float); f
                    Native morphism:
                      From: Set of Python objects of class 'float'
                      To:   Real Double Field
                    sage: f(3.5)
                    3.5
        """

RDF: RealDoubleField_class