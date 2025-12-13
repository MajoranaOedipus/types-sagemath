import _cython_3_2_1
import sage as sage
import sage.categories.morphism
import sage.rings.ring
import sage.structure.element
from sage.rings.integer import Integer as Integer
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from sage.structure.richcmp import revop as revop, rich_to_bool as rich_to_bool, rich_to_bool_sgn as rich_to_bool_sgn, richcmp as richcmp, richcmp_not_equal as richcmp_not_equal
from typing import Any, ClassVar, overload

CLF: ComplexLazyField_class_with_category
ComplexLazyField: _cython_3_2_1.cython_function_or_method
RLF: RealLazyField_class_with_category
RealLazyField: _cython_3_2_1.cython_function_or_method
make_element: _cython_3_2_1.cython_function_or_method

class ComplexLazyField_class(LazyField):
    """File: /build/sagemath/src/sage/src/sage/rings/real_lazy.pyx (starting at line 371)

        This class represents the set of complex numbers to unspecified precision.
        For the most part it simply wraps exact elements and defers evaluation
        until a specified precision is requested.

        For more information, see the documentation of the
        :class:`RLF <sage.rings.real_lazy.RealLazyField_class>`.

        EXAMPLES::

            sage: a = CLF(-1).sqrt()
            sage: a
            1*I
            sage: CDF(a)
            1.0*I
            sage: ComplexField(200)(a)
            1.0000000000000000000000000000000000000000000000000000000000*I

        TESTS::

            sage: TestSuite(CLF).run()
    """
    def __init__(self) -> Any:
        """ComplexLazyField_class.__init__(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_lazy.pyx (starting at line 394)

        This lazy field does not evaluate its elements until they are cast into
        a field of fixed precision.

        EXAMPLES::

            sage: a = RLF(1/3); a
            0.3333333333333334?
            sage: Reals(200)(a)
            0.33333333333333333333333333333333333333333333333333333333333"""
    @overload
    def construction(self) -> Any:
        """ComplexLazyField_class.construction(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_lazy.pyx (starting at line 447)

        Return the functorial construction of ``self``, namely,
        algebraic closure of the real lazy field.

        EXAMPLES::

            sage: c, S = CLF.construction(); S
            Real Lazy Field
            sage: CLF == c(S)
            True"""
    @overload
    def construction(self) -> Any:
        """ComplexLazyField_class.construction(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_lazy.pyx (starting at line 447)

        Return the functorial construction of ``self``, namely,
        algebraic closure of the real lazy field.

        EXAMPLES::

            sage: c, S = CLF.construction(); S
            Real Lazy Field
            sage: CLF == c(S)
            True"""
    @overload
    def gen(self, i=...) -> Any:
        """ComplexLazyField_class.gen(self, i=0)

        File: /build/sagemath/src/sage/src/sage/rings/real_lazy.pyx (starting at line 430)

        Return the `i`-th generator of ``self``.

        EXAMPLES::

            sage: CLF.gen()
            1*I
            sage: ComplexField(100)(CLF.gen())                                          # needs sage.rings.number_field
            1.0000000000000000000000000000*I"""
    @overload
    def gen(self) -> Any:
        """ComplexLazyField_class.gen(self, i=0)

        File: /build/sagemath/src/sage/src/sage/rings/real_lazy.pyx (starting at line 430)

        Return the `i`-th generator of ``self``.

        EXAMPLES::

            sage: CLF.gen()
            1*I
            sage: ComplexField(100)(CLF.gen())                                          # needs sage.rings.number_field
            1.0000000000000000000000000000*I"""
    @overload
    def gen(self) -> Any:
        """ComplexLazyField_class.gen(self, i=0)

        File: /build/sagemath/src/sage/src/sage/rings/real_lazy.pyx (starting at line 430)

        Return the `i`-th generator of ``self``.

        EXAMPLES::

            sage: CLF.gen()
            1*I
            sage: ComplexField(100)(CLF.gen())                                          # needs sage.rings.number_field
            1.0000000000000000000000000000*I"""
    @overload
    def interval_field(self, prec=...) -> Any:
        """ComplexLazyField_class.interval_field(self, prec=None)

        File: /build/sagemath/src/sage/src/sage/rings/real_lazy.pyx (starting at line 409)

        Return the interval field that represents the same mathematical
        field as ``self``.

        EXAMPLES::

            sage: CLF.interval_field()
            Complex Interval Field with 53 bits of precision
            sage: CLF.interval_field(333)                                               # needs sage.rings.complex_interval_field
            Complex Interval Field with 333 bits of precision
            sage: CLF.interval_field() is CIF
            True"""
    @overload
    def interval_field(self) -> Any:
        """ComplexLazyField_class.interval_field(self, prec=None)

        File: /build/sagemath/src/sage/src/sage/rings/real_lazy.pyx (starting at line 409)

        Return the interval field that represents the same mathematical
        field as ``self``.

        EXAMPLES::

            sage: CLF.interval_field()
            Complex Interval Field with 53 bits of precision
            sage: CLF.interval_field(333)                                               # needs sage.rings.complex_interval_field
            Complex Interval Field with 333 bits of precision
            sage: CLF.interval_field() is CIF
            True"""
    @overload
    def interval_field(self) -> Any:
        """ComplexLazyField_class.interval_field(self, prec=None)

        File: /build/sagemath/src/sage/src/sage/rings/real_lazy.pyx (starting at line 409)

        Return the interval field that represents the same mathematical
        field as ``self``.

        EXAMPLES::

            sage: CLF.interval_field()
            Complex Interval Field with 53 bits of precision
            sage: CLF.interval_field(333)                                               # needs sage.rings.complex_interval_field
            Complex Interval Field with 333 bits of precision
            sage: CLF.interval_field() is CIF
            True"""
    def __hash__(self) -> Any:
        """ComplexLazyField_class.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_lazy.pyx (starting at line 484)

        Return the hash of ``self``.

        EXAMPLES::

            sage: from sage.rings.real_lazy import ComplexLazyField_class
            sage: hash(CLF) == hash(ComplexLazyField_class())
            True"""
    def __reduce__(self) -> Any:
        """ComplexLazyField_class.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_lazy.pyx (starting at line 496)

        For pickling.

        TESTS::

            sage: CLF == loads(dumps(CLF))
            True
            sage: CLF is loads(dumps(CLF))
            True"""

class LazyAlgebraic(LazyFieldElement):
    """LazyAlgebraic(parent, poly, approx, int prec=0)"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, parent, poly, approx, intprec=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/real_lazy.pyx (starting at line 1596)

                This represents an algebraic number, specified by a polynomial over
                `\\QQ` and a real or complex approximation.

                EXAMPLES::

                    sage: x = polygen(QQ)
                    sage: from sage.rings.real_lazy import LazyAlgebraic
                    sage: a = LazyAlgebraic(RLF, x^2-2, 1.5)
                    sage: a
                    1.414213562373095?
        """
    def eval(self, R) -> Any:
        """LazyAlgebraic.eval(self, R)

        File: /build/sagemath/src/sage/src/sage/rings/real_lazy.pyx (starting at line 1629)

        Convert ``self`` into an element of ``R``.

        EXAMPLES::

            sage: from sage.rings.real_lazy import LazyAlgebraic
            sage: a = LazyAlgebraic(CLF, QQ['x'].cyclotomic_polynomial(7), 0.6+0.8*CC.0)
            sage: a
            0.6234898018587335? + 0.7818314824680299?*I
            sage: ComplexField(150)(a)  # indirect doctest                              # needs sage.rings.number_field
            0.62348980185873353052500488400423981063227473 + 0.78183148246802980870844452667405775023233452*I

            sage: a = LazyAlgebraic(CLF, QQ['x'].0^2-7, -2.0)
            sage: RR(a)                                                                 # needs sage.rings.number_field
            -2.64575131106459
            sage: RR(a)^2                                                               # needs sage.rings.number_field
            7.00000000000000"""
    def __float__(self) -> Any:
        """LazyAlgebraic.__float__(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_lazy.pyx (starting at line 1688)

        TESTS::

            sage: x = polygen(QQ)
            sage: from sage.rings.real_lazy import LazyAlgebraic
            sage: a = LazyAlgebraic(RLF, x^3-10, 1.5)
            sage: float(a)
            2.154434690031883..."""
    def __reduce__(self) -> Any:
        """LazyAlgebraic.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_lazy.pyx (starting at line 1700)

        TESTS::

            sage: from sage.rings.real_lazy import LazyAlgebraic
            sage: x = polygen(QQ)
            sage: a = LazyAlgebraic(RLF, x^2 - 2, 1.5)
            sage: float(loads(dumps(a))) == float(a)
            True"""

class LazyBinop(LazyFieldElement):
    """LazyBinop(LazyField parent, left, right, op)"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, LazyFieldparent, left, right, op) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/real_lazy.pyx (starting at line 1066)

                A lazy element representing a binary (usually arithmetic) operation
                between two other lazy elements.

                EXAMPLES::

                    sage: from sage.rings.real_lazy import LazyBinop
                    sage: a = LazyBinop(RLF, 2, 1/3, operator.add)
                    sage: a
                    2.333333333333334?
                    sage: Reals(200)(a)
                    2.3333333333333333333333333333333333333333333333333333333333
        """
    @overload
    def depth(self) -> int:
        """LazyBinop.depth(self) -> int

        File: /build/sagemath/src/sage/src/sage/rings/real_lazy.pyx (starting at line 1089)

        Return the depth of ``self`` as an arithmetic expression.

        This is the  maximum number of dependent intermediate expressions when
        evaluating ``self``, and is used to determine the precision needed to
        get the final result to the desired number of bits.

        It is equal to the maximum of the right and left depths, plus one.

        EXAMPLES::

            sage: from sage.rings.real_lazy import LazyBinop
            sage: a = LazyBinop(RLF, 6, 8, operator.mul)
            sage: a.depth()
            1
            sage: b = LazyBinop(RLF, 2, a, operator.sub)
            sage: b.depth()
            2"""
    @overload
    def depth(self) -> Any:
        """LazyBinop.depth(self) -> int

        File: /build/sagemath/src/sage/src/sage/rings/real_lazy.pyx (starting at line 1089)

        Return the depth of ``self`` as an arithmetic expression.

        This is the  maximum number of dependent intermediate expressions when
        evaluating ``self``, and is used to determine the precision needed to
        get the final result to the desired number of bits.

        It is equal to the maximum of the right and left depths, plus one.

        EXAMPLES::

            sage: from sage.rings.real_lazy import LazyBinop
            sage: a = LazyBinop(RLF, 6, 8, operator.mul)
            sage: a.depth()
            1
            sage: b = LazyBinop(RLF, 2, a, operator.sub)
            sage: b.depth()
            2"""
    @overload
    def depth(self) -> Any:
        """LazyBinop.depth(self) -> int

        File: /build/sagemath/src/sage/src/sage/rings/real_lazy.pyx (starting at line 1089)

        Return the depth of ``self`` as an arithmetic expression.

        This is the  maximum number of dependent intermediate expressions when
        evaluating ``self``, and is used to determine the precision needed to
        get the final result to the desired number of bits.

        It is equal to the maximum of the right and left depths, plus one.

        EXAMPLES::

            sage: from sage.rings.real_lazy import LazyBinop
            sage: a = LazyBinop(RLF, 6, 8, operator.mul)
            sage: a.depth()
            1
            sage: b = LazyBinop(RLF, 2, a, operator.sub)
            sage: b.depth()
            2"""
    @overload
    def eval(self, R) -> Any:
        """LazyBinop.eval(self, R)

        File: /build/sagemath/src/sage/src/sage/rings/real_lazy.pyx (starting at line 1113)

        Convert the operands to elements of ``R``, then perform the operation
        on them.

        EXAMPLES::

            sage: from sage.rings.real_lazy import LazyBinop
            sage: a = LazyBinop(RLF, 6, 8, operator.add)
            sage: a.eval(RR)
            14.0000000000000

        A bit absurd::

            sage: a.eval(str)
            '68'"""
    @overload
    def eval(self, RR) -> Any:
        """LazyBinop.eval(self, R)

        File: /build/sagemath/src/sage/src/sage/rings/real_lazy.pyx (starting at line 1113)

        Convert the operands to elements of ``R``, then perform the operation
        on them.

        EXAMPLES::

            sage: from sage.rings.real_lazy import LazyBinop
            sage: a = LazyBinop(RLF, 6, 8, operator.add)
            sage: a.eval(RR)
            14.0000000000000

        A bit absurd::

            sage: a.eval(str)
            '68'"""
    @overload
    def eval(self, str) -> Any:
        """LazyBinop.eval(self, R)

        File: /build/sagemath/src/sage/src/sage/rings/real_lazy.pyx (starting at line 1113)

        Convert the operands to elements of ``R``, then perform the operation
        on them.

        EXAMPLES::

            sage: from sage.rings.real_lazy import LazyBinop
            sage: a = LazyBinop(RLF, 6, 8, operator.add)
            sage: a.eval(RR)
            14.0000000000000

        A bit absurd::

            sage: a.eval(str)
            '68'"""
    def __float__(self) -> Any:
        """LazyBinop.__float__(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_lazy.pyx (starting at line 1146)

        EXAMPLES::

            sage: from sage.rings.real_lazy import LazyBinop
            sage: a = LazyBinop(RLF, 3, 1/2, operator.sub)
            sage: float(a)
            2.5
            sage: type(float(a))
            <... 'float'>"""
    def __hash__(self) -> Any:
        """LazyBinop.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_lazy.pyx (starting at line 1173)

        Return the hash value of ``self``.

        EXAMPLES::

            sage: from sage.rings.real_lazy import LazyBinop
            sage: a = LazyBinop(RLF, 5, 1/2, operator.sub)
            sage: b = LazyBinop(RLF, 4, 1/2, operator.add)
            sage: hash(a) == hash(b)
            False"""
    def __reduce__(self) -> Any:
        """LazyBinop.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_lazy.pyx (starting at line 1187)

        For pickling.

        TESTS::

            sage: from sage.rings.real_lazy import LazyBinop
            sage: a = LazyBinop(CLF, 3, 2, operator.truediv)
            sage: loads(dumps(a)) == a
            True"""

class LazyConstant(LazyFieldElement):
    """LazyConstant(LazyField parent, name, extra_args=None)"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, LazyFieldparent, name, extra_args=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/real_lazy.pyx (starting at line 1450)

                This class represents a real or complex constant (such as ``pi``
                or ``I``).

                TESTS::

                    sage: a = RLF.pi(); a
                    3.141592653589794?
                    sage: RealField(300)(a)
                    3.14159265358979323846264338327950288419716939937510582097494459230781640628620899862803482

                    sage: from sage.rings.real_lazy import LazyConstant
                    sage: a = LazyConstant(RLF, 'euler_constant')
                    sage: RealField(200)(a)
                    0.57721566490153286060651209008240243104215933593992359880577
        """
    @overload
    def eval(self, R) -> Any:
        """LazyConstant.eval(self, R)

        File: /build/sagemath/src/sage/src/sage/rings/real_lazy.pyx (starting at line 1471)

        Convert ``self`` into an element of ``R``.

        EXAMPLES::

            sage: from sage.rings.real_lazy import LazyConstant
            sage: a = LazyConstant(RLF, 'e')
            sage: RDF(a) # indirect doctest
            2.718281828459045
            sage: a = LazyConstant(CLF, 'I')
            sage: CC(a)
            1.00000000000000*I

        TESTS:

        Check that :issue:`26839` is fixed::

            sage: RLF.pi().eval(float)
            3.141592653589793
            sage: type(RLF.pi().eval(float)) is float
            True

            sage: RLF.pi().eval(complex)
            (3.141592653589793+0j)
            sage: type(RLF.pi().eval(complex)) is complex
            True

            sage: RLF.pi().eval(RealBallField(128))
            [3.1415926535897932384626433832795028842 +/- 1.06e-38]

            sage: float(sin(RLF.pi()))
            1.2246467991473532e-16"""
    @overload
    def eval(self, float) -> Any:
        """LazyConstant.eval(self, R)

        File: /build/sagemath/src/sage/src/sage/rings/real_lazy.pyx (starting at line 1471)

        Convert ``self`` into an element of ``R``.

        EXAMPLES::

            sage: from sage.rings.real_lazy import LazyConstant
            sage: a = LazyConstant(RLF, 'e')
            sage: RDF(a) # indirect doctest
            2.718281828459045
            sage: a = LazyConstant(CLF, 'I')
            sage: CC(a)
            1.00000000000000*I

        TESTS:

        Check that :issue:`26839` is fixed::

            sage: RLF.pi().eval(float)
            3.141592653589793
            sage: type(RLF.pi().eval(float)) is float
            True

            sage: RLF.pi().eval(complex)
            (3.141592653589793+0j)
            sage: type(RLF.pi().eval(complex)) is complex
            True

            sage: RLF.pi().eval(RealBallField(128))
            [3.1415926535897932384626433832795028842 +/- 1.06e-38]

            sage: float(sin(RLF.pi()))
            1.2246467991473532e-16"""
    @overload
    def eval(self, float) -> Any:
        """LazyConstant.eval(self, R)

        File: /build/sagemath/src/sage/src/sage/rings/real_lazy.pyx (starting at line 1471)

        Convert ``self`` into an element of ``R``.

        EXAMPLES::

            sage: from sage.rings.real_lazy import LazyConstant
            sage: a = LazyConstant(RLF, 'e')
            sage: RDF(a) # indirect doctest
            2.718281828459045
            sage: a = LazyConstant(CLF, 'I')
            sage: CC(a)
            1.00000000000000*I

        TESTS:

        Check that :issue:`26839` is fixed::

            sage: RLF.pi().eval(float)
            3.141592653589793
            sage: type(RLF.pi().eval(float)) is float
            True

            sage: RLF.pi().eval(complex)
            (3.141592653589793+0j)
            sage: type(RLF.pi().eval(complex)) is complex
            True

            sage: RLF.pi().eval(RealBallField(128))
            [3.1415926535897932384626433832795028842 +/- 1.06e-38]

            sage: float(sin(RLF.pi()))
            1.2246467991473532e-16"""
    @overload
    def eval(self, complex) -> Any:
        """LazyConstant.eval(self, R)

        File: /build/sagemath/src/sage/src/sage/rings/real_lazy.pyx (starting at line 1471)

        Convert ``self`` into an element of ``R``.

        EXAMPLES::

            sage: from sage.rings.real_lazy import LazyConstant
            sage: a = LazyConstant(RLF, 'e')
            sage: RDF(a) # indirect doctest
            2.718281828459045
            sage: a = LazyConstant(CLF, 'I')
            sage: CC(a)
            1.00000000000000*I

        TESTS:

        Check that :issue:`26839` is fixed::

            sage: RLF.pi().eval(float)
            3.141592653589793
            sage: type(RLF.pi().eval(float)) is float
            True

            sage: RLF.pi().eval(complex)
            (3.141592653589793+0j)
            sage: type(RLF.pi().eval(complex)) is complex
            True

            sage: RLF.pi().eval(RealBallField(128))
            [3.1415926535897932384626433832795028842 +/- 1.06e-38]

            sage: float(sin(RLF.pi()))
            1.2246467991473532e-16"""
    @overload
    def eval(self, complex) -> Any:
        """LazyConstant.eval(self, R)

        File: /build/sagemath/src/sage/src/sage/rings/real_lazy.pyx (starting at line 1471)

        Convert ``self`` into an element of ``R``.

        EXAMPLES::

            sage: from sage.rings.real_lazy import LazyConstant
            sage: a = LazyConstant(RLF, 'e')
            sage: RDF(a) # indirect doctest
            2.718281828459045
            sage: a = LazyConstant(CLF, 'I')
            sage: CC(a)
            1.00000000000000*I

        TESTS:

        Check that :issue:`26839` is fixed::

            sage: RLF.pi().eval(float)
            3.141592653589793
            sage: type(RLF.pi().eval(float)) is float
            True

            sage: RLF.pi().eval(complex)
            (3.141592653589793+0j)
            sage: type(RLF.pi().eval(complex)) is complex
            True

            sage: RLF.pi().eval(RealBallField(128))
            [3.1415926535897932384626433832795028842 +/- 1.06e-38]

            sage: float(sin(RLF.pi()))
            1.2246467991473532e-16"""
    def __call__(self, *args) -> Any:
        """LazyConstant.__call__(self, *args)

        File: /build/sagemath/src/sage/src/sage/rings/real_lazy.pyx (starting at line 1539)

        TESTS::

            sage: CLF.I()
            1*I
            sage: CDF(CLF.I())
            1.0*I"""
    def __float__(self) -> Any:
        """LazyConstant.__float__(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_lazy.pyx (starting at line 1564)

        TESTS::

            sage: from sage.rings.real_lazy import LazyConstant
            sage: a = LazyConstant(RLF, 'pi')
            sage: float(a)
            3.141592653589793"""
    def __hash__(self) -> Any:
        """LazyConstant.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_lazy.pyx (starting at line 1551)

        Return the hash value of ``self``.

        TESTS::

            sage: from sage.rings.real_lazy import LazyConstant
            sage: a = LazyConstant(RLF, 'e')
            sage: hash(a) == hash(1)
            False"""
    def __reduce__(self) -> Any:
        """LazyConstant.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_lazy.pyx (starting at line 1576)

        TESTS::

            sage: from sage.rings.real_lazy import LazyConstant
            sage: a = LazyConstant(RLF, 'pi')
            sage: float(loads(dumps(a))) == float(a)
            True"""

class LazyField(sage.rings.ring.Field):
    """LazyField(base=None, names=None, normalize=True, category=None)

    File: /build/sagemath/src/sage/src/sage/rings/real_lazy.pyx (starting at line 82)

    The base class for lazy real fields.

    .. WARNING::

        LazyField uses :meth:`__getattr__`, to implement::

            sage: CLF.pi
            3.141592653589794?

        I (NT, 20/04/2012) did not manage to have ``__getattr__`` call
        :meth:`Parent.__getattr__` in case of failure; hence we can't
        use this ``__getattr__`` trick for extension types to recover
        the methods from categories. Therefore, at this point, no
        concrete subclass of this class should be an extension type
        (which is probably just fine)::

            sage: RLF.__class__
            <class 'sage.rings.real_lazy.RealLazyField_class_with_category'>
            sage: CLF.__class__
            <class 'sage.rings.real_lazy.ComplexLazyField_class_with_category'>"""

    class Element(LazyFieldElement):
        """LazyWrapper(LazyField parent, value, check=True)"""
        __pyx_vtable__: ClassVar[PyCapsule] = ...
        def __init__(self, *args, **kwargs) -> None:
            """File: /build/sagemath/src/sage/src/sage/rings/real_lazy.pyx (starting at line 933)

                    A lazy element that simply wraps an element of another ring.

                    EXAMPLES::

                        sage: from sage.rings.real_lazy import LazyWrapper
                        sage: a = LazyWrapper(RLF, 3)
                        sage: a._value
                        3
        """
        @overload
        def continued_fraction(self) -> Any:
            """LazyWrapper.continued_fraction(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_lazy.pyx (starting at line 1048)

            Return the continued fraction of ``self``.

            EXAMPLES::

                sage: a = RLF(sqrt(2))                                                      # needs sage.symbolic
                sage: a.continued_fraction()                                                # needs sage.symbolic
                [1; 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, ...]"""
        @overload
        def continued_fraction(self) -> Any:
            """LazyWrapper.continued_fraction(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_lazy.pyx (starting at line 1048)

            Return the continued fraction of ``self``.

            EXAMPLES::

                sage: a = RLF(sqrt(2))                                                      # needs sage.symbolic
                sage: a.continued_fraction()                                                # needs sage.symbolic
                [1; 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, ...]"""
        @overload
        def depth(self) -> int:
            """LazyWrapper.depth(self) -> int

            File: /build/sagemath/src/sage/src/sage/rings/real_lazy.pyx (starting at line 922)

            Return the depth of ``self`` as an expression, which is always 0.

            EXAMPLES::

                sage: RLF(4).depth()
                0"""
        @overload
        def depth(self) -> Any:
            """LazyWrapper.depth(self) -> int

            File: /build/sagemath/src/sage/src/sage/rings/real_lazy.pyx (starting at line 922)

            Return the depth of ``self`` as an expression, which is always 0.

            EXAMPLES::

                sage: RLF(4).depth()
                0"""
        @overload
        def eval(self, R) -> Any:
            """LazyWrapper.eval(self, R)

            File: /build/sagemath/src/sage/src/sage/rings/real_lazy.pyx (starting at line 1015)

            Convert ``self`` into an element of ``R``.

            EXAMPLES::

                sage: a = RLF(12)
                sage: a.eval(ZZ)
                12
                sage: a.eval(ZZ).parent()
                Integer Ring"""
        @overload
        def eval(self, ZZ) -> Any:
            """LazyWrapper.eval(self, R)

            File: /build/sagemath/src/sage/src/sage/rings/real_lazy.pyx (starting at line 1015)

            Convert ``self`` into an element of ``R``.

            EXAMPLES::

                sage: a = RLF(12)
                sage: a.eval(ZZ)
                12
                sage: a.eval(ZZ).parent()
                Integer Ring"""
        @overload
        def eval(self, ZZ) -> Any:
            """LazyWrapper.eval(self, R)

            File: /build/sagemath/src/sage/src/sage/rings/real_lazy.pyx (starting at line 1015)

            Convert ``self`` into an element of ``R``.

            EXAMPLES::

                sage: a = RLF(12)
                sage: a.eval(ZZ)
                12
                sage: a.eval(ZZ).parent()
                Integer Ring"""
        def __bool__(self) -> bool:
            """True if self else False"""
        def __float__(self) -> Any:
            """LazyWrapper.__float__(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_lazy.pyx (starting at line 977)

            EXAMPLES::

                sage: from sage.rings.real_lazy import LazyWrapper
                sage: a = LazyWrapper(CLF, 19)
                sage: float(a)
                19.0"""
        def __hash__(self) -> Any:
            """LazyWrapper.__hash__(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_lazy.pyx (starting at line 1002)

            Return the hash value of ``self``.

            EXAMPLES::

                sage: hash(CLF(-1))
                -2
                sage: hash(RLF(9/4)) == hash(9/4)
                True"""
        def __invert__(self) -> Any:
            """LazyWrapper.__invert__(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_lazy.pyx (starting at line 962)

            Return the reciprocal of ``self``.

            EXAMPLES::

                sage: from sage.rings.real_lazy import LazyWrapper
                sage: a = LazyWrapper(RLF, 23)
                sage: ~a
                0.04347826086956522?
                sage: (~a)._value
                1/23"""
        def __neg__(self) -> Any:
            """LazyWrapper.__neg__(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_lazy.pyx (starting at line 949)

            Return the negation of ``self``.

            EXAMPLES::

                sage: from sage.rings.real_lazy import LazyWrapper
                sage: a = LazyWrapper(RLF, 3)
                sage: (-a)._value
                -3"""
        def __reduce__(self) -> Any:
            """LazyWrapper.__reduce__(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_lazy.pyx (starting at line 1036)

            For pickling.

            TESTS::

                sage: a = RLF(2)
                sage: loads(dumps(a)) == a
                True"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, base=..., names=..., normalize=..., category=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/real_lazy.pyx (starting at line 105)

                Initialize ``self``.

                EXAMPLES::

                    sage: RLF # indirect doctest
                    Real Lazy Field
        """
    @overload
    def algebraic_closure(self) -> Any:
        """LazyField.algebraic_closure(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_lazy.pyx (starting at line 193)

        Return the algebraic closure of ``self``, i.e., the complex lazy
        field.

        EXAMPLES::

            sage: RLF.algebraic_closure()
            Complex Lazy Field

            sage: CLF.algebraic_closure()
            Complex Lazy Field"""
    @overload
    def algebraic_closure(self) -> Any:
        """LazyField.algebraic_closure(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_lazy.pyx (starting at line 193)

        Return the algebraic closure of ``self``, i.e., the complex lazy
        field.

        EXAMPLES::

            sage: RLF.algebraic_closure()
            Complex Lazy Field

            sage: CLF.algebraic_closure()
            Complex Lazy Field"""
    @overload
    def algebraic_closure(self) -> Any:
        """LazyField.algebraic_closure(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_lazy.pyx (starting at line 193)

        Return the algebraic closure of ``self``, i.e., the complex lazy
        field.

        EXAMPLES::

            sage: RLF.algebraic_closure()
            Complex Lazy Field

            sage: CLF.algebraic_closure()
            Complex Lazy Field"""
    @overload
    def interval_field(self, prec=...) -> Any:
        """LazyField.interval_field(self, prec=None)

        File: /build/sagemath/src/sage/src/sage/rings/real_lazy.pyx (starting at line 208)

        Abstract method to create the corresponding interval field.

        TESTS::

            sage: RLF.interval_field() # indirect doctest
            Real Interval Field with 53 bits of precision"""
    @overload
    def interval_field(self) -> Any:
        """LazyField.interval_field(self, prec=None)

        File: /build/sagemath/src/sage/src/sage/rings/real_lazy.pyx (starting at line 208)

        Abstract method to create the corresponding interval field.

        TESTS::

            sage: RLF.interval_field() # indirect doctest
            Real Interval Field with 53 bits of precision"""

class LazyFieldElement(sage.structure.element.FieldElement):
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    @overload
    def approx(self) -> Any:
        """LazyFieldElement.approx(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_lazy.pyx (starting at line 745)

        Return ``self`` as an element of an interval field.

        EXAMPLES::

            sage: CLF(1/6).approx()
            0.1666666666666667?
            sage: CLF(1/6).approx().parent()
            Complex Interval Field with 53 bits of precision

        When the absolute value is involved, the result might be real::

            sage: # needs sage.symbolic
            sage: z = exp(CLF(1 + I/2)); z
            2.38551673095914? + 1.303213729686996?*I
            sage: r = z.abs(); r
            2.71828182845905?
            sage: parent(z.approx())
            Complex Interval Field with 53 bits of precision
            sage: parent(r.approx())
            Real Interval Field with 53 bits of precision"""
    @overload
    def approx(self) -> Any:
        """LazyFieldElement.approx(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_lazy.pyx (starting at line 745)

        Return ``self`` as an element of an interval field.

        EXAMPLES::

            sage: CLF(1/6).approx()
            0.1666666666666667?
            sage: CLF(1/6).approx().parent()
            Complex Interval Field with 53 bits of precision

        When the absolute value is involved, the result might be real::

            sage: # needs sage.symbolic
            sage: z = exp(CLF(1 + I/2)); z
            2.38551673095914? + 1.303213729686996?*I
            sage: r = z.abs(); r
            2.71828182845905?
            sage: parent(z.approx())
            Complex Interval Field with 53 bits of precision
            sage: parent(r.approx())
            Real Interval Field with 53 bits of precision"""
    @overload
    def approx(self) -> Any:
        """LazyFieldElement.approx(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_lazy.pyx (starting at line 745)

        Return ``self`` as an element of an interval field.

        EXAMPLES::

            sage: CLF(1/6).approx()
            0.1666666666666667?
            sage: CLF(1/6).approx().parent()
            Complex Interval Field with 53 bits of precision

        When the absolute value is involved, the result might be real::

            sage: # needs sage.symbolic
            sage: z = exp(CLF(1 + I/2)); z
            2.38551673095914? + 1.303213729686996?*I
            sage: r = z.abs(); r
            2.71828182845905?
            sage: parent(z.approx())
            Complex Interval Field with 53 bits of precision
            sage: parent(r.approx())
            Real Interval Field with 53 bits of precision"""
    @overload
    def approx(self) -> Any:
        """LazyFieldElement.approx(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_lazy.pyx (starting at line 745)

        Return ``self`` as an element of an interval field.

        EXAMPLES::

            sage: CLF(1/6).approx()
            0.1666666666666667?
            sage: CLF(1/6).approx().parent()
            Complex Interval Field with 53 bits of precision

        When the absolute value is involved, the result might be real::

            sage: # needs sage.symbolic
            sage: z = exp(CLF(1 + I/2)); z
            2.38551673095914? + 1.303213729686996?*I
            sage: r = z.abs(); r
            2.71828182845905?
            sage: parent(z.approx())
            Complex Interval Field with 53 bits of precision
            sage: parent(r.approx())
            Real Interval Field with 53 bits of precision"""
    @overload
    def approx(self) -> Any:
        """LazyFieldElement.approx(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_lazy.pyx (starting at line 745)

        Return ``self`` as an element of an interval field.

        EXAMPLES::

            sage: CLF(1/6).approx()
            0.1666666666666667?
            sage: CLF(1/6).approx().parent()
            Complex Interval Field with 53 bits of precision

        When the absolute value is involved, the result might be real::

            sage: # needs sage.symbolic
            sage: z = exp(CLF(1 + I/2)); z
            2.38551673095914? + 1.303213729686996?*I
            sage: r = z.abs(); r
            2.71828182845905?
            sage: parent(z.approx())
            Complex Interval Field with 53 bits of precision
            sage: parent(r.approx())
            Real Interval Field with 53 bits of precision"""
    @overload
    def continued_fraction(self) -> Any:
        """LazyFieldElement.continued_fraction(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_lazy.pyx (starting at line 889)

        Return the continued fraction of ``self``.

        EXAMPLES::

            sage: # needs sage.symbolic
            sage: a = RLF(sqrt(2)) + RLF(sqrt(3))
            sage: cf = a.continued_fraction()
            sage: cf
            [3; 6, 1, 5, 7, 1, 1, 4, 1, 38, 43, 1, 3, 2, 1, 1, 1, 1, 2, 4, ...]
            sage: cf.convergent(100)
            444927297812646558239761867973501208151173610180916865469/141414466649174973335183571854340329919207428365474086063"""
    @overload
    def continued_fraction(self) -> Any:
        """LazyFieldElement.continued_fraction(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_lazy.pyx (starting at line 889)

        Return the continued fraction of ``self``.

        EXAMPLES::

            sage: # needs sage.symbolic
            sage: a = RLF(sqrt(2)) + RLF(sqrt(3))
            sage: cf = a.continued_fraction()
            sage: cf
            [3; 6, 1, 5, 7, 1, 1, 4, 1, 38, 43, 1, 3, 2, 1, 1, 1, 1, 2, 4, ...]
            sage: cf.convergent(100)
            444927297812646558239761867973501208151173610180916865469/141414466649174973335183571854340329919207428365474086063"""
    @overload
    def depth(self) -> int:
        """LazyFieldElement.depth(self) -> int

        File: /build/sagemath/src/sage/src/sage/rings/real_lazy.pyx (starting at line 839)

        Abstract method for returning the depth of ``self`` as an arithmetic
        expression.

        This is the  maximum number of dependent intermediate expressions when
        evaluating ``self``, and is used to determine the precision needed to
        get the final result to the desired number of bits.

        It is equal to the maximum of the right and left depths, plus one.

        EXAMPLES::

            sage: from sage.rings.real_lazy import LazyBinop
            sage: a = LazyBinop(RLF, 6, 8, operator.mul)
            sage: a.depth()
            1"""
    @overload
    def depth(self) -> Any:
        """LazyFieldElement.depth(self) -> int

        File: /build/sagemath/src/sage/src/sage/rings/real_lazy.pyx (starting at line 839)

        Abstract method for returning the depth of ``self`` as an arithmetic
        expression.

        This is the  maximum number of dependent intermediate expressions when
        evaluating ``self``, and is used to determine the precision needed to
        get the final result to the desired number of bits.

        It is equal to the maximum of the right and left depths, plus one.

        EXAMPLES::

            sage: from sage.rings.real_lazy import LazyBinop
            sage: a = LazyBinop(RLF, 6, 8, operator.mul)
            sage: a.depth()
            1"""
    @overload
    def eval(self, R) -> Any:
        """LazyFieldElement.eval(self, R)

        File: /build/sagemath/src/sage/src/sage/rings/real_lazy.pyx (starting at line 827)

        Abstract method for converting ``self`` into an element of ``R``.

        EXAMPLES::

            sage: a = RLF(12)
            sage: a.eval(ZZ)
            12"""
    @overload
    def eval(self, ZZ) -> Any:
        """LazyFieldElement.eval(self, R)

        File: /build/sagemath/src/sage/src/sage/rings/real_lazy.pyx (starting at line 827)

        Abstract method for converting ``self`` into an element of ``R``.

        EXAMPLES::

            sage: a = RLF(12)
            sage: a.eval(ZZ)
            12"""
    def __complex__(self) -> Any:
        """LazyFieldElement.__complex__(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_lazy.pyx (starting at line 813)

        Return ``self`` as a complex.

        EXAMPLES::

            sage: complex(CLF(-1)^(1/4))
            (0.707106781186547...+0.707106781186547...j)"""
    @overload
    def __dir__(self) -> Any:
        '''LazyFieldElement.__dir__(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_lazy.pyx (starting at line 859)

        Add the named_unops to ``__dir__`` so that tab completion works.

        TESTS::

            sage: "log" in RLF(sqrt(8)).__dir__()                                       # needs sage.symbolic
            True'''
    @overload
    def __dir__(self) -> Any:
        '''LazyFieldElement.__dir__(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_lazy.pyx (starting at line 859)

        Add the named_unops to ``__dir__`` so that tab completion works.

        TESTS::

            sage: "log" in RLF(sqrt(8)).__dir__()                                       # needs sage.symbolic
            True'''
    def __hash__(self) -> Any:
        """LazyFieldElement.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_lazy.pyx (starting at line 698)

        Return the hash value of ``self``.

        EXAMPLES::

            sage: a = RLF(3)
            sage: hash(a)
            3"""
    def __invert__(self) -> Any:
        """LazyFieldElement.__invert__(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_lazy.pyx (starting at line 643)

        Take the reciprocal of ``self``.

        EXAMPLES::

          sage: a = ~RLF(6); a
          0.1666666666666667?
          sage: Reals(90)(a)
          0.16666666666666666666666667"""
    def __neg__(self) -> Any:
        """LazyFieldElement.__neg__(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_lazy.pyx (starting at line 632)

        Return the negation of ``self``.

        EXAMPLES::

            sage: -RLF(7)
            -7"""
    def __pow__(self, left, right, dummy) -> Any:
        """LazyFieldElement.__pow__(left, right, dummy)

        File: /build/sagemath/src/sage/src/sage/rings/real_lazy.pyx (starting at line 610)

        Raise ``left`` to the ``right`` power.

        EXAMPLES::

            sage: a = RLF(2) ^ (1/2); a
            1.414213562373095?
            sage: Reals(300)(a)
            1.41421356237309504880168872420969807856967187537694807317667973799073247846210703885038753"""
    def __rpow__(self, other):
        """Return pow(value, self, mod)."""

class LazyNamedUnop(LazyUnop):
    """LazyNamedUnop(LazyField parent, arg, op, extra_args=None)"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, LazyFieldparent, arg, op, extra_args=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/real_lazy.pyx (starting at line 1307)

                This class is used to represent the many named methods attached to real
                numbers, and is instantiated by the ``__getattr__`` method of
                :class:`LazyElements`.

                EXAMPLES::

                    sage: from sage.rings.real_lazy import LazyNamedUnop
                    sage: a = LazyNamedUnop(RLF, 1, 'arcsin')
                    sage: RR(a)
                    1.57079632679490
                    sage: a = LazyNamedUnop(RLF, 9, 'log', extra_args=(3,))
                    sage: RR(a)
                    2.00000000000000
        """
    def approx(self) -> Any:
        """LazyNamedUnop.approx(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_lazy.pyx (starting at line 1368)

        Do something reasonable with functions that are not defined on the
        interval fields.

        TESTS::

            sage: from sage.rings.real_lazy import LazyNamedUnop
            sage: LazyNamedUnop(RLF, 8, 'sqrt') # indirect doctest
            2.828427124746190?"""
    def eval(self, R) -> Any:
        """LazyNamedUnop.eval(self, R)

        File: /build/sagemath/src/sage/src/sage/rings/real_lazy.pyx (starting at line 1328)

        Convert ``self`` into an element of ``R``.

        TESTS::

            sage: from sage.rings.real_lazy import LazyNamedUnop
            sage: a = LazyNamedUnop(RLF, 4, 'sqrt')
            sage: RR(a) # indirect doctest
            2.00000000000000
            sage: a.sqrt()
            1.414213562373095?
            sage: RealField(212)(a)
            2.00000000000000000000000000000000000000000000000000000000000000
            sage: float(a)
            2.0

        Now for some extra arguments::

            sage: a = RLF(100)
            sage: a.log(10)
            2
            sage: float(a.log(10))
            2.0"""
    def __call__(self, *args) -> Any:
        """LazyNamedUnop.__call__(self, *args)

        File: /build/sagemath/src/sage/src/sage/rings/real_lazy.pyx (starting at line 1412)

        TESTS::

            sage: a = RLF(32)
            sage: a.log(2)
            5
            sage: float(a.log(2))
            5.0

        What is going on here in the background is::

            sage: from sage.rings.real_lazy import LazyNamedUnop
            sage: b = LazyNamedUnop(RLF, a, 'log')
            sage: b(2)
            5
            sage: b(2)._extra_args
            (2,)"""
    def __float__(self) -> Any:
        """LazyNamedUnop.__float__(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_lazy.pyx (starting at line 1401)

        TESTS::

            sage: from sage.rings.real_lazy import LazyNamedUnop
            sage: a = LazyNamedUnop(RLF, 1, 'sin')
            sage: float(a)
            0.8414709848078965"""
    def __hash__(self) -> Any:
        """LazyNamedUnop.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_lazy.pyx (starting at line 1387)

        Return the hash value of ``self``.

        EXAMPLES::

            sage: from sage.rings.real_lazy import LazyNamedUnop
            sage: a = LazyNamedUnop(RLF, 1, 'sin')
            sage: b = LazyNamedUnop(RLF, 1, 'cos')
            sage: hash(a) == hash(b)
            False"""
    def __reduce__(self) -> Any:
        """LazyNamedUnop.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_lazy.pyx (starting at line 1434)

        TESTS::

            sage: from sage.rings.real_lazy import LazyNamedUnop
            sage: a = LazyNamedUnop(RLF, 1, 'sin')
            sage: float(loads(dumps(a))) == float(a)
            True"""

class LazyUnop(LazyFieldElement):
    """LazyUnop(LazyField parent, arg, op)"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, LazyFieldparent, arg, op) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/real_lazy.pyx (starting at line 1203)

                Represent a unevaluated single function of one variable.

                EXAMPLES::

                    sage: from sage.rings.real_lazy import LazyUnop
                    sage: a = LazyUnop(RLF, 3, sqrt); a
                    1.732050807568878?
                    sage: a._arg
                    3
                    sage: a._op
                    <function sqrt at ...>
                    sage: Reals(100)(a)
                    1.7320508075688772935274463415
                    sage: Reals(100)(a)^2
                    3.0000000000000000000000000000
        """
    @overload
    def depth(self) -> int:
        """LazyUnop.depth(self) -> int

        File: /build/sagemath/src/sage/src/sage/rings/real_lazy.pyx (starting at line 1227)

        Return the depth of ``self`` as an arithmetic expression.

        This is the  maximum number of dependent intermediate expressions when
        evaluating ``self``, and is used to determine the precision needed to
        get the final result to the desired number of bits.

        It is equal to one more than the depth of its operand.

        EXAMPLES::

            sage: from sage.rings.real_lazy import LazyUnop
            sage: a = LazyUnop(RLF, 3, sqrt)
            sage: a.depth()
            1
            sage: b = LazyUnop(RLF, a, sin)
            sage: b.depth()
            2"""
    @overload
    def depth(self) -> Any:
        """LazyUnop.depth(self) -> int

        File: /build/sagemath/src/sage/src/sage/rings/real_lazy.pyx (starting at line 1227)

        Return the depth of ``self`` as an arithmetic expression.

        This is the  maximum number of dependent intermediate expressions when
        evaluating ``self``, and is used to determine the precision needed to
        get the final result to the desired number of bits.

        It is equal to one more than the depth of its operand.

        EXAMPLES::

            sage: from sage.rings.real_lazy import LazyUnop
            sage: a = LazyUnop(RLF, 3, sqrt)
            sage: a.depth()
            1
            sage: b = LazyUnop(RLF, a, sin)
            sage: b.depth()
            2"""
    @overload
    def depth(self) -> Any:
        """LazyUnop.depth(self) -> int

        File: /build/sagemath/src/sage/src/sage/rings/real_lazy.pyx (starting at line 1227)

        Return the depth of ``self`` as an arithmetic expression.

        This is the  maximum number of dependent intermediate expressions when
        evaluating ``self``, and is used to determine the precision needed to
        get the final result to the desired number of bits.

        It is equal to one more than the depth of its operand.

        EXAMPLES::

            sage: from sage.rings.real_lazy import LazyUnop
            sage: a = LazyUnop(RLF, 3, sqrt)
            sage: a.depth()
            1
            sage: b = LazyUnop(RLF, a, sin)
            sage: b.depth()
            2"""
    @overload
    def eval(self, R) -> Any:
        """LazyUnop.eval(self, R)

        File: /build/sagemath/src/sage/src/sage/rings/real_lazy.pyx (starting at line 1249)

        Convert ``self`` into an element of ``R``.

        EXAMPLES::

            sage: from sage.rings.real_lazy import LazyUnop
            sage: a = LazyUnop(RLF, 3, sqrt)
            sage: a.eval(ZZ)                                                            # needs sage.symbolic
            sqrt(3)"""
    @overload
    def eval(self, ZZ) -> Any:
        """LazyUnop.eval(self, R)

        File: /build/sagemath/src/sage/src/sage/rings/real_lazy.pyx (starting at line 1249)

        Convert ``self`` into an element of ``R``.

        EXAMPLES::

            sage: from sage.rings.real_lazy import LazyUnop
            sage: a = LazyUnop(RLF, 3, sqrt)
            sage: a.eval(ZZ)                                                            # needs sage.symbolic
            sqrt(3)"""
    def __float__(self) -> Any:
        """LazyUnop.__float__(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_lazy.pyx (starting at line 1278)

        Convert ``self`` into a floating point.

        EXAMPLES::

            sage: from sage.rings.real_lazy import LazyUnop
            sage: a = LazyUnop(RLF, 3, sqrt)
            sage: float(a)
            1.7320508075688772"""
    def __hash__(self) -> Any:
        """LazyUnop.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_lazy.pyx (starting at line 1267)

        Return the hash value of ``self``.

        EXAMPLES::

            sage: hash(RLF(sin(1))) == hash(RLF(sin(1)))                                # needs sage.symbolic
            True"""
    def __reduce__(self) -> Any:
        """LazyUnop.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_lazy.pyx (starting at line 1291)

        For pickling.

        TESTS::

            sage: from sage.rings.real_lazy import LazyUnop
            sage: a = LazyUnop(RLF, 7, sqrt)
            sage: float(loads(dumps(a))) == float(a)
            True"""

class LazyWrapper(LazyFieldElement):
    """LazyWrapper(LazyField parent, value, check=True)"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, LazyFieldparent, value, check=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/real_lazy.pyx (starting at line 933)

                A lazy element that simply wraps an element of another ring.

                EXAMPLES::

                    sage: from sage.rings.real_lazy import LazyWrapper
                    sage: a = LazyWrapper(RLF, 3)
                    sage: a._value
                    3
        """
    @overload
    def continued_fraction(self) -> Any:
        """LazyWrapper.continued_fraction(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_lazy.pyx (starting at line 1048)

        Return the continued fraction of ``self``.

        EXAMPLES::

            sage: a = RLF(sqrt(2))                                                      # needs sage.symbolic
            sage: a.continued_fraction()                                                # needs sage.symbolic
            [1; 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, ...]"""
    @overload
    def continued_fraction(self) -> Any:
        """LazyWrapper.continued_fraction(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_lazy.pyx (starting at line 1048)

        Return the continued fraction of ``self``.

        EXAMPLES::

            sage: a = RLF(sqrt(2))                                                      # needs sage.symbolic
            sage: a.continued_fraction()                                                # needs sage.symbolic
            [1; 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, ...]"""
    @overload
    def depth(self) -> int:
        """LazyWrapper.depth(self) -> int

        File: /build/sagemath/src/sage/src/sage/rings/real_lazy.pyx (starting at line 922)

        Return the depth of ``self`` as an expression, which is always 0.

        EXAMPLES::

            sage: RLF(4).depth()
            0"""
    @overload
    def depth(self) -> Any:
        """LazyWrapper.depth(self) -> int

        File: /build/sagemath/src/sage/src/sage/rings/real_lazy.pyx (starting at line 922)

        Return the depth of ``self`` as an expression, which is always 0.

        EXAMPLES::

            sage: RLF(4).depth()
            0"""
    @overload
    def eval(self, R) -> Any:
        """LazyWrapper.eval(self, R)

        File: /build/sagemath/src/sage/src/sage/rings/real_lazy.pyx (starting at line 1015)

        Convert ``self`` into an element of ``R``.

        EXAMPLES::

            sage: a = RLF(12)
            sage: a.eval(ZZ)
            12
            sage: a.eval(ZZ).parent()
            Integer Ring"""
    @overload
    def eval(self, ZZ) -> Any:
        """LazyWrapper.eval(self, R)

        File: /build/sagemath/src/sage/src/sage/rings/real_lazy.pyx (starting at line 1015)

        Convert ``self`` into an element of ``R``.

        EXAMPLES::

            sage: a = RLF(12)
            sage: a.eval(ZZ)
            12
            sage: a.eval(ZZ).parent()
            Integer Ring"""
    @overload
    def eval(self, ZZ) -> Any:
        """LazyWrapper.eval(self, R)

        File: /build/sagemath/src/sage/src/sage/rings/real_lazy.pyx (starting at line 1015)

        Convert ``self`` into an element of ``R``.

        EXAMPLES::

            sage: a = RLF(12)
            sage: a.eval(ZZ)
            12
            sage: a.eval(ZZ).parent()
            Integer Ring"""
    def __bool__(self) -> bool:
        """True if self else False"""
    def __float__(self) -> Any:
        """LazyWrapper.__float__(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_lazy.pyx (starting at line 977)

        EXAMPLES::

            sage: from sage.rings.real_lazy import LazyWrapper
            sage: a = LazyWrapper(CLF, 19)
            sage: float(a)
            19.0"""
    def __hash__(self) -> Any:
        """LazyWrapper.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_lazy.pyx (starting at line 1002)

        Return the hash value of ``self``.

        EXAMPLES::

            sage: hash(CLF(-1))
            -2
            sage: hash(RLF(9/4)) == hash(9/4)
            True"""
    def __invert__(self) -> Any:
        """LazyWrapper.__invert__(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_lazy.pyx (starting at line 962)

        Return the reciprocal of ``self``.

        EXAMPLES::

            sage: from sage.rings.real_lazy import LazyWrapper
            sage: a = LazyWrapper(RLF, 23)
            sage: ~a
            0.04347826086956522?
            sage: (~a)._value
            1/23"""
    def __neg__(self) -> Any:
        """LazyWrapper.__neg__(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_lazy.pyx (starting at line 949)

        Return the negation of ``self``.

        EXAMPLES::

            sage: from sage.rings.real_lazy import LazyWrapper
            sage: a = LazyWrapper(RLF, 3)
            sage: (-a)._value
            -3"""
    def __reduce__(self) -> Any:
        """LazyWrapper.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_lazy.pyx (starting at line 1036)

        For pickling.

        TESTS::

            sage: a = RLF(2)
            sage: loads(dumps(a)) == a
            True"""

class LazyWrapperMorphism(sage.categories.morphism.Morphism):
    """LazyWrapperMorphism(domain, LazyField codomain)"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, domain, LazyFieldcodomain) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/real_lazy.pyx (starting at line 1715)

                This morphism coerces elements from anywhere into lazy rings
                by creating a wrapper element (as fast as possible).

                EXAMPLES::

                    sage: from sage.rings.real_lazy import LazyWrapperMorphism
                    sage: f = LazyWrapperMorphism(QQ, RLF)
                    sage: a = f(3); a
                    3
                    sage: type(a)
                    <class 'sage.rings.real_lazy.LazyWrapper'>
                    sage: a._value
                    3
                    sage: a._value.parent()
                    Rational Field
        """

class RealLazyField_class(LazyField):
    """File: /build/sagemath/src/sage/src/sage/rings/real_lazy.pyx (starting at line 220)

        This class represents the set of real numbers to unspecified precision.
        For the most part it simply wraps exact elements and defers evaluation
        until a specified precision is requested.

        Its primary use is to connect the exact rings (such as number fields) to
        fixed precision real numbers. For example, to specify an embedding of a
        number field `K` into `\\RR` one can map into this field and the
        coercion will then be able to carry the mapping to real fields of any
        precision.

        EXAMPLES::

            sage: a = RLF(1/3)
            sage: a
            0.3333333333333334?
            sage: a + 1/5
            0.5333333333333334?
            sage: a = RLF(1/3)
            sage: a
            0.3333333333333334?
            sage: a + 5
            5.333333333333334?
            sage: RealField(100)(a+5)
            5.3333333333333333333333333333

        ::

            sage: CC.0 + RLF(1/3)
            0.333333333333333 + 1.00000000000000*I
            sage: ComplexField(200).0 + RLF(1/3)
            0.33333333333333333333333333333333333333333333333333333333333 + 1.0000000000000000000000000000000000000000000000000000000000*I

        TESTS::

            sage: TestSuite(RLF).run()
    """
    @overload
    def construction(self) -> Any:
        """RealLazyField_class.construction(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_lazy.pyx (starting at line 276)

        Return the functorial construction of ``self``, namely, the
        completion of the rationals at infinity to infinite precision.

        EXAMPLES::

            sage: c, S = RLF.construction(); S
            Rational Field
            sage: RLF == c(S)
            True"""
    @overload
    def construction(self) -> Any:
        """RealLazyField_class.construction(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_lazy.pyx (starting at line 276)

        Return the functorial construction of ``self``, namely, the
        completion of the rationals at infinity to infinite precision.

        EXAMPLES::

            sage: c, S = RLF.construction(); S
            Rational Field
            sage: RLF == c(S)
            True"""
    @overload
    def gen(self, i=...) -> Any:
        """RealLazyField_class.gen(self, i=0)

        File: /build/sagemath/src/sage/src/sage/rings/real_lazy.pyx (starting at line 304)

        Return the `i`-th generator of ``self``.

        EXAMPLES::

            sage: RLF.gen()
            1"""
    @overload
    def gen(self) -> Any:
        """RealLazyField_class.gen(self, i=0)

        File: /build/sagemath/src/sage/src/sage/rings/real_lazy.pyx (starting at line 304)

        Return the `i`-th generator of ``self``.

        EXAMPLES::

            sage: RLF.gen()
            1"""
    @overload
    def interval_field(self, prec=...) -> Any:
        """RealLazyField_class.interval_field(self, prec=None)

        File: /build/sagemath/src/sage/src/sage/rings/real_lazy.pyx (starting at line 258)

        Return the interval field that represents the same mathematical
        field as ``self``.

        EXAMPLES::

            sage: RLF.interval_field()
            Real Interval Field with 53 bits of precision
            sage: RLF.interval_field(200)
            Real Interval Field with 200 bits of precision"""
    @overload
    def interval_field(self) -> Any:
        """RealLazyField_class.interval_field(self, prec=None)

        File: /build/sagemath/src/sage/src/sage/rings/real_lazy.pyx (starting at line 258)

        Return the interval field that represents the same mathematical
        field as ``self``.

        EXAMPLES::

            sage: RLF.interval_field()
            Real Interval Field with 53 bits of precision
            sage: RLF.interval_field(200)
            Real Interval Field with 200 bits of precision"""
    def __hash__(self) -> Any:
        """RealLazyField_class.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_lazy.pyx (starting at line 329)

        Return the hash of ``self``.

        EXAMPLES::

            sage: hash(RLF) == hash(RealLazyField())
            True"""
    def __reduce__(self) -> Any:
        """RealLazyField_class.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_lazy.pyx (starting at line 340)

        For pickling.

        TESTS::

            sage: RLF == loads(dumps(RLF))
            True
            sage: RLF is loads(dumps(RLF))
            True"""
