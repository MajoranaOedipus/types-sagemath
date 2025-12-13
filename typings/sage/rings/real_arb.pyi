import _cython_3_2_1
import sage as sage
import sage.rings.abc
import sage.structure.element
import sage.structure.unique_representation
from sage.categories.category import ZZ as ZZ
from sage.cpython.string import bytes_to_str as bytes_to_str, str_to_bytes as str_to_bytes
from sage.misc.lazy_string import lazy_string as lazy_string
from sage.rings.rational_field import QQ as QQ
from sage.rings.real_mpfi import RealIntervalField as RealIntervalField
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation
from typing import Any, ClassVar, overload

RBF: RealBallField_with_category
__pyx_capi__: dict
create_RealBall: _cython_3_2_1.cython_function_or_method

class RealBall(sage.structure.element.RingElement):
    """RealBall(parent, mid=None, rad=None)

    File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 1190)

    Hold one ``arb_t``.

    EXAMPLES::

        sage: a = RealBallField()(RIF(1))                     # indirect doctest
        sage: b = a.psi()
        sage: b # abs tol 1e-15
        [-0.5772156649015329 +/- 4.84e-17]
        sage: RIF(b)
        -0.577215664901533?"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, parent, mid=..., rad=...) -> Any:
        '''File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 1226)

                Initialize the :class:`RealBall`.

                INPUT:

                - ``parent`` -- a :class:`RealBallField`

                - ``mid`` -- (optional) ball midpoint, see examples below. If omitted,
                  initialize the ball to zero, ignoring the ``rad`` argument.

                - ``rad`` -- (optional) a :class:`RealNumber` or a Python float, ball
                  radius. If the midpoint is not exactly representable in
                  floating-point, the radius is adjusted to account for the roundoff
                  error.

                EXAMPLES::

                    sage: RBF = RealBallField()
                    sage: RBF()
                    0

                One can create exact real balls using elements of various exact parents,
                or using floating-point numbers::

                    sage: RBF(3)
                    3.000000000000000
                    sage: RBF(3r)
                    3.000000000000000
                    sage: RBF(1/3)
                    [0.3333333333333333 +/- ...e-17]
                    sage: RBF(3.14)
                    [3.140000000000000 +/- ...e-16]

                ::

                    sage: RBF(3, 0.125)
                    [3e+0 +/- 0.126]
                    sage: RBF(pi, 0.125r)                                                       # needs sage.symbolic
                    [3e+0 +/- 0.267]
                    sage: RBF(3, 1/8)
                    [3e+0 +/- 0.126]
                    sage: RBF(13, 1)
                    [1e+1 +/- 4.01]

                ::

                    sage: NF.<sqrt2> = QuadraticField(2)                                        # needs sage.rings.number_field
                    sage: RBF(1/5 + sqrt2/2)                                                    # needs sage.rings.number_field
                    [0.907106781186547 +/- ...e-16]

                Note that integers and floating-point numbers are \'\'not\'\' rounded to
                the parent\'s precision::

                    sage: b = RBF(11111111111111111111111111111111111111111111111); b
                    [1.111111111111111e+46 +/- ...e+30]
                    sage: b.mid().exact_rational()
                    11111111111111111111111111111111111111111111111

                Similarly, converting a real ball from one real ball field to another
                (with a different precision) only changes the way it is displayed and
                the precision of operations involving it, not the actual representation
                of its center::

                    sage: RBF100 = RealBallField(100)
                    sage: b100 = RBF100(1/3); b100
                    [0.333333333333333333333333333333 +/- ...e-31]
                    sage: b53 = RBF(b100); b53
                    [0.3333333333333333 +/- ...e-17]
                    sage: RBF100(b53)
                    [0.333333333333333333333333333333 +/- ...e-31]

                Special values are supported::

                    sage: RBF(oo).mid(), RBF(-oo).mid(), RBF(unsigned_infinity).mid()
                    (+infinity, -infinity, 0.000000000000000)
                    sage: RBF(NaN)
                    nan

                Strings can be given as input. Strings must contain decimal
                floating-point literals. A valid string must consist of a midpoint,
                a midpoint and a radius separated by "+/-", or just a
                radius prefixed by "+/-". Optionally, the whole string can be enclosed
                in square brackets. In general, the string representation of a
                real ball as returned by ``str()`` can be parsed back (the result
                will be larger than the original ball if rounding occurs).
                A few examples::

                    sage: RBF("1.1")
                    [1.100000000000000 +/- ...e-16]
                    sage: RBF(str(RBF("1.1")))
                    [1.100000000000000 +/- ...e-16]
                    sage: RBF("3.25")
                    3.250000000000000
                    sage: RBF("-3.1 +/- 1e-10")
                    [-3.100000000 +/- ...e-10]
                    sage: RBF("[+/-1]")
                    [+/- 1.01]
                    sage: RBF("inf +/- inf")
                    [+/- inf]

                .. SEEALSO:: :meth:`RealBallField._element_constructor_`

                TESTS::

                    sage: from sage.rings.real_arb import RealBall
                    sage: RealBall(RBF, sage.symbolic.constants.Pi())
                    [3.141592653589793 +/- ...e-16]
                    sage: RealBall(RBF, sage.symbolic.constants.Log2())
                    [0.6931471805599453 +/- ...e-17]
                    sage: RealBall(RBF, sage.symbolic.constants.Catalan())
                    [0.915965594177219 +/- ...e-16]
                    sage: RealBall(RBF, sage.symbolic.constants.Khinchin())
                    [2.685452001065306 +/- ...e-16]
                    sage: RealBall(RBF, sage.symbolic.constants.Glaisher())
                    [1.282427129100623 +/- ...e-16]
                    sage: RealBall(RBF, sage.symbolic.constants.e)
                    [2.718281828459045 +/- ...e-16]
                    sage: RealBall(RBF, sage.symbolic.constants.EulerGamma()) # abs tol 1e-15
                    [0.5772156649015329 +/- 9.00e-17]
                    sage: RBF("1 +/- 0.001")
                    [1.00 +/- ...e-3]
                    sage: RBF("2.3e10000000000000000000000 +/- 0.00005e10000000000000000000000")
                    [2.3000e+10000000000000000000000 +/- ...e+9999999999999999999995]
                    sage: RBF("0.3 +/- 0.2 +/- 0.1")
                    Traceback (most recent call last):
                    ...
                    ValueError: unsupported string format

                    sage: NF.<a> = QuadraticField(2, embedding=AA(2).sqrt())
                    sage: RBF.coerce(a)
                    [1.414213562373095 +/- ...e-16]
                    sage: NF.<a> = QuadraticField(2, embedding=-AA(2).sqrt())
                    sage: RBF.coerce(a)
                    [-1.414213562373095 +/- ...e-16]
                    sage: NF.<a> = QuadraticField(2, embedding=None)
                    sage: RBF.coerce(a)
                    Traceback (most recent call last):
                    ...
                    TypeError: no canonical coercion ...
                    sage: QQi.<i> = QuadraticField(-1)
                    sage: RBF(QQi(3))
                    3.000000000000000
                    sage: RBF(i)
                    Traceback (most recent call last):
                    ...
                    ValueError: nonzero imaginary part
                    sage: RBF.coerce(QQi(3))
                    Traceback (most recent call last):
                    ...
                    TypeError: no canonical coercion...
        '''
    @overload
    def Chi(self) -> Any:
        """RealBall.Chi(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3626)

        Hyperbolic cosine integral.

        EXAMPLES::

            sage: RBF(1).Chi()  # abs tol 5e-16
            [0.837866940980208 +/- 4.72e-16]

        TESTS::

            sage: RBF(Chi(1))  # abs tol 5e-16                                          # needs sage.symbolic
            [0.837866940980208 +/- 4.72e-16]"""
    @overload
    def Chi(self) -> Any:
        """RealBall.Chi(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3626)

        Hyperbolic cosine integral.

        EXAMPLES::

            sage: RBF(1).Chi()  # abs tol 5e-16
            [0.837866940980208 +/- 4.72e-16]

        TESTS::

            sage: RBF(Chi(1))  # abs tol 5e-16                                          # needs sage.symbolic
            [0.837866940980208 +/- 4.72e-16]"""
    @overload
    def Ci(self) -> Any:
        """RealBall.Ci(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3582)

        Cosine integral.

        EXAMPLES::

            sage: RBF(1).Ci()  # abs tol 5e-16
            [0.337403922900968 +/- 3.25e-16]

        TESTS::

            sage: RBF(Ci(1))  # abs tol 5e-16                                           # needs sage.symbolic
            [0.337403922900968 +/- 3.25e-16]"""
    @overload
    def Ci(self) -> Any:
        """RealBall.Ci(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3582)

        Cosine integral.

        EXAMPLES::

            sage: RBF(1).Ci()  # abs tol 5e-16
            [0.337403922900968 +/- 3.25e-16]

        TESTS::

            sage: RBF(Ci(1))  # abs tol 5e-16                                           # needs sage.symbolic
            [0.337403922900968 +/- 3.25e-16]"""
    @overload
    def Ei(self) -> Any:
        """RealBall.Ei(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3540)

        Exponential integral.

        EXAMPLES::

            sage: RBF(1).Ei()  # abs tol 5e-15
            [1.89511781635594 +/- 4.94e-15]

        TESTS::

            sage: RBF(Ei(1))  # abs tol 5e-15                                           # needs sage.symbolic
            [1.89511781635594 +/- 4.94e-15]"""
    @overload
    def Ei(self) -> Any:
        """RealBall.Ei(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3540)

        Exponential integral.

        EXAMPLES::

            sage: RBF(1).Ei()  # abs tol 5e-15
            [1.89511781635594 +/- 4.94e-15]

        TESTS::

            sage: RBF(Ei(1))  # abs tol 5e-15                                           # needs sage.symbolic
            [1.89511781635594 +/- 4.94e-15]"""
    @overload
    def Li(self) -> Any:
        """RealBall.Li(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3672)

        Offset logarithmic integral.

        EXAMPLES::

            sage: RBF(3).Li()  # abs tol 5e-15
            [1.11842481454970 +/- 7.61e-15]"""
    @overload
    def Li(self) -> Any:
        """RealBall.Li(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3672)

        Offset logarithmic integral.

        EXAMPLES::

            sage: RBF(3).Li()  # abs tol 5e-15
            [1.11842481454970 +/- 7.61e-15]"""
    @overload
    def Shi(self) -> Any:
        """RealBall.Shi(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3604)

        Hyperbolic sine integral.

        EXAMPLES::

            sage: RBF(1).Shi() # abs tol 5e-15
            [1.05725087537573 +/- 2.77e-15]

        TESTS::

            sage: RBF(Shi(1))  # abs tol 5e-15                                          # needs sage.symbolic
            [1.05725087537573 +/- 2.77e-15]"""
    @overload
    def Shi(self) -> Any:
        """RealBall.Shi(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3604)

        Hyperbolic sine integral.

        EXAMPLES::

            sage: RBF(1).Shi() # abs tol 5e-15
            [1.05725087537573 +/- 2.77e-15]

        TESTS::

            sage: RBF(Shi(1))  # abs tol 5e-15                                          # needs sage.symbolic
            [1.05725087537573 +/- 2.77e-15]"""
    @overload
    def Si(self) -> Any:
        """RealBall.Si(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3560)

        Sine integral.

        EXAMPLES::

            sage: RBF(1).Si() # abs tol 1e-15
            [0.946083070367183 +/- 9.22e-16]

        TESTS::

            sage: RBF(Si(1))  # abs tol 1e-15                                           # needs sage.symbolic
            [0.946083070367183 +/- 9.22e-16]"""
    @overload
    def Si(self) -> Any:
        """RealBall.Si(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3560)

        Sine integral.

        EXAMPLES::

            sage: RBF(1).Si() # abs tol 1e-15
            [0.946083070367183 +/- 9.22e-16]

        TESTS::

            sage: RBF(Si(1))  # abs tol 1e-15                                           # needs sage.symbolic
            [0.946083070367183 +/- 9.22e-16]"""
    @overload
    def above_abs(self) -> Any:
        """RealBall.above_abs(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 1897)

        Return an upper bound for the absolute value of this ball.

        OUTPUT: a ball with zero radius

        EXAMPLES::

            sage: b = RealBallField(8)(1/3).above_abs()
            sage: b
            [0.33 +/- ...e-3]
            sage: b.is_exact()
            True
            sage: QQ(b)
            171/512

        .. SEEALSO:: :meth:`below_abs`"""
    @overload
    def above_abs(self) -> Any:
        """RealBall.above_abs(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 1897)

        Return an upper bound for the absolute value of this ball.

        OUTPUT: a ball with zero radius

        EXAMPLES::

            sage: b = RealBallField(8)(1/3).above_abs()
            sage: b
            [0.33 +/- ...e-3]
            sage: b.is_exact()
            True
            sage: QQ(b)
            171/512

        .. SEEALSO:: :meth:`below_abs`"""
    @overload
    def accuracy(self) -> Any:
        """RealBall.accuracy(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 2082)

        Return the effective relative accuracy of this ball measured in bits.

        The accuracy is defined as the difference between the position of the
        top bit in the midpoint and the top bit in the radius, minus one.
        The result is clamped between plus/minus
        :meth:`~RealBallField.maximal_accuracy`.

        EXAMPLES::

            sage: RBF(pi).accuracy()                                                    # needs sage.symbolic
            52
            sage: RBF(1).accuracy() == RBF.maximal_accuracy()
            True
            sage: RBF(NaN).accuracy() == -RBF.maximal_accuracy()                        # needs sage.symbolic
            True

        .. SEEALSO:: :meth:`~RealBallField.maximal_accuracy`"""
    @overload
    def accuracy(self) -> Any:
        """RealBall.accuracy(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 2082)

        Return the effective relative accuracy of this ball measured in bits.

        The accuracy is defined as the difference between the position of the
        top bit in the midpoint and the top bit in the radius, minus one.
        The result is clamped between plus/minus
        :meth:`~RealBallField.maximal_accuracy`.

        EXAMPLES::

            sage: RBF(pi).accuracy()                                                    # needs sage.symbolic
            52
            sage: RBF(1).accuracy() == RBF.maximal_accuracy()
            True
            sage: RBF(NaN).accuracy() == -RBF.maximal_accuracy()                        # needs sage.symbolic
            True

        .. SEEALSO:: :meth:`~RealBallField.maximal_accuracy`"""
    @overload
    def accuracy(self) -> Any:
        """RealBall.accuracy(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 2082)

        Return the effective relative accuracy of this ball measured in bits.

        The accuracy is defined as the difference between the position of the
        top bit in the midpoint and the top bit in the radius, minus one.
        The result is clamped between plus/minus
        :meth:`~RealBallField.maximal_accuracy`.

        EXAMPLES::

            sage: RBF(pi).accuracy()                                                    # needs sage.symbolic
            52
            sage: RBF(1).accuracy() == RBF.maximal_accuracy()
            True
            sage: RBF(NaN).accuracy() == -RBF.maximal_accuracy()                        # needs sage.symbolic
            True

        .. SEEALSO:: :meth:`~RealBallField.maximal_accuracy`"""
    @overload
    def accuracy(self) -> Any:
        """RealBall.accuracy(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 2082)

        Return the effective relative accuracy of this ball measured in bits.

        The accuracy is defined as the difference between the position of the
        top bit in the midpoint and the top bit in the radius, minus one.
        The result is clamped between plus/minus
        :meth:`~RealBallField.maximal_accuracy`.

        EXAMPLES::

            sage: RBF(pi).accuracy()                                                    # needs sage.symbolic
            52
            sage: RBF(1).accuracy() == RBF.maximal_accuracy()
            True
            sage: RBF(NaN).accuracy() == -RBF.maximal_accuracy()                        # needs sage.symbolic
            True

        .. SEEALSO:: :meth:`~RealBallField.maximal_accuracy`"""
    @overload
    def add_error(self, ampl) -> Any:
        """RealBall.add_error(self, ampl)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 2129)

        Increase the radius of this ball by (an upper bound on) ``ampl``.

        If ``ampl`` is negative, the radius is unchanged.

        INPUT:

        - ``ampl`` -- a real ball (or an object that can be coerced to a real
          ball)

        OUTPUT: a new real ball

        EXAMPLES::

            sage: err = RBF(10^-16)
            sage: RBF(1).add_error(err)
            [1.000000000000000 +/- ...e-16]

        TESTS::

            sage: RBF(1).add_error(-1)
            1.000000000000000
            sage: RBF(0).add_error(RBF(1, rad=2.)).endpoints()
            (-3.00000000745059, 3.00000000745059)"""
    @overload
    def add_error(self, err) -> Any:
        """RealBall.add_error(self, ampl)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 2129)

        Increase the radius of this ball by (an upper bound on) ``ampl``.

        If ``ampl`` is negative, the radius is unchanged.

        INPUT:

        - ``ampl`` -- a real ball (or an object that can be coerced to a real
          ball)

        OUTPUT: a new real ball

        EXAMPLES::

            sage: err = RBF(10^-16)
            sage: RBF(1).add_error(err)
            [1.000000000000000 +/- ...e-16]

        TESTS::

            sage: RBF(1).add_error(-1)
            1.000000000000000
            sage: RBF(0).add_error(RBF(1, rad=2.)).endpoints()
            (-3.00000000745059, 3.00000000745059)"""
    def agm(self, other) -> Any:
        """RealBall.agm(self, other)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 4042)

        Return the arithmetic-geometric mean of ``self`` and ``other``.

        EXAMPLES::

            sage: RBF(1).agm(1)
            1.000000000000000
            sage: RBF(sqrt(2)).agm(1)^(-1)                                              # needs sage.symbolic
            [0.8346268416740...]"""
    @overload
    def arccos(self) -> Any:
        """RealBall.arccos(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3329)

        Return the arccosine of this ball.

        EXAMPLES::

            sage: RBF(1).arccos()
            0
            sage: RBF(1, rad=.125r).arccos()
            nan"""
    @overload
    def arccos(self) -> Any:
        """RealBall.arccos(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3329)

        Return the arccosine of this ball.

        EXAMPLES::

            sage: RBF(1).arccos()
            0
            sage: RBF(1, rad=.125r).arccos()
            nan"""
    @overload
    def arccos(self) -> Any:
        """RealBall.arccos(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3329)

        Return the arccosine of this ball.

        EXAMPLES::

            sage: RBF(1).arccos()
            0
            sage: RBF(1, rad=.125r).arccos()
            nan"""
    @overload
    def arccosh(self) -> Any:
        """RealBall.arccosh(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3470)

        Return the inverse hyperbolic cosine of this ball.

        EXAMPLES::

            sage: RBF(2).arccosh()
            [1.316957896924817 +/- ...e-16]
            sage: RBF(1).arccosh()
            0
            sage: RBF(0).arccosh()
            nan"""
    @overload
    def arccosh(self) -> Any:
        """RealBall.arccosh(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3470)

        Return the inverse hyperbolic cosine of this ball.

        EXAMPLES::

            sage: RBF(2).arccosh()
            [1.316957896924817 +/- ...e-16]
            sage: RBF(1).arccosh()
            0
            sage: RBF(0).arccosh()
            nan"""
    @overload
    def arccosh(self) -> Any:
        """RealBall.arccosh(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3470)

        Return the inverse hyperbolic cosine of this ball.

        EXAMPLES::

            sage: RBF(2).arccosh()
            [1.316957896924817 +/- ...e-16]
            sage: RBF(1).arccosh()
            0
            sage: RBF(0).arccosh()
            nan"""
    @overload
    def arccosh(self) -> Any:
        """RealBall.arccosh(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3470)

        Return the inverse hyperbolic cosine of this ball.

        EXAMPLES::

            sage: RBF(2).arccosh()
            [1.316957896924817 +/- ...e-16]
            sage: RBF(1).arccosh()
            0
            sage: RBF(0).arccosh()
            nan"""
    @overload
    def arcsin(self) -> Any:
        """RealBall.arcsin(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3312)

        Return the arcsine of this ball.

        EXAMPLES::

            sage: RBF(1).arcsin()
            [1.570796326794897 +/- ...e-16]
            sage: RBF(1, rad=.125r).arcsin()
            nan"""
    @overload
    def arcsin(self) -> Any:
        """RealBall.arcsin(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3312)

        Return the arcsine of this ball.

        EXAMPLES::

            sage: RBF(1).arcsin()
            [1.570796326794897 +/- ...e-16]
            sage: RBF(1, rad=.125r).arcsin()
            nan"""
    @overload
    def arcsin(self) -> Any:
        """RealBall.arcsin(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3312)

        Return the arcsine of this ball.

        EXAMPLES::

            sage: RBF(1).arcsin()
            [1.570796326794897 +/- ...e-16]
            sage: RBF(1, rad=.125r).arcsin()
            nan"""
    @overload
    def arcsinh(self) -> Any:
        """RealBall.arcsinh(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3453)

        Return the inverse hyperbolic sine of this ball.

        EXAMPLES::

            sage: RBF(1).arcsinh()
            [0.881373587019543 +/- ...e-16]
            sage: RBF(0).arcsinh()
            0"""
    @overload
    def arcsinh(self) -> Any:
        """RealBall.arcsinh(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3453)

        Return the inverse hyperbolic sine of this ball.

        EXAMPLES::

            sage: RBF(1).arcsinh()
            [0.881373587019543 +/- ...e-16]
            sage: RBF(0).arcsinh()
            0"""
    @overload
    def arcsinh(self) -> Any:
        """RealBall.arcsinh(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3453)

        Return the inverse hyperbolic sine of this ball.

        EXAMPLES::

            sage: RBF(1).arcsinh()
            [0.881373587019543 +/- ...e-16]
            sage: RBF(0).arcsinh()
            0"""
    @overload
    def arctan(self) -> Any:
        """RealBall.arctan(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3346)

        Return the arctangent of this ball.

        EXAMPLES::

            sage: RBF(1).arctan()
            [0.7853981633974483 +/- ...e-17]"""
    @overload
    def arctan(self) -> Any:
        """RealBall.arctan(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3346)

        Return the arctangent of this ball.

        EXAMPLES::

            sage: RBF(1).arctan()
            [0.7853981633974483 +/- ...e-17]"""
    @overload
    def arctanh(self) -> Any:
        """RealBall.arctanh(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3489)

        Return the inverse hyperbolic tangent of this ball.

        EXAMPLES::

            sage: RBF(0).arctanh()
            0
            sage: RBF(1/2).arctanh()
            [0.549306144334055 +/- ...e-16]
            sage: RBF(1).arctanh()
            nan"""
    @overload
    def arctanh(self) -> Any:
        """RealBall.arctanh(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3489)

        Return the inverse hyperbolic tangent of this ball.

        EXAMPLES::

            sage: RBF(0).arctanh()
            0
            sage: RBF(1/2).arctanh()
            [0.549306144334055 +/- ...e-16]
            sage: RBF(1).arctanh()
            nan"""
    @overload
    def arctanh(self) -> Any:
        """RealBall.arctanh(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3489)

        Return the inverse hyperbolic tangent of this ball.

        EXAMPLES::

            sage: RBF(0).arctanh()
            0
            sage: RBF(1/2).arctanh()
            [0.549306144334055 +/- ...e-16]
            sage: RBF(1).arctanh()
            nan"""
    @overload
    def arctanh(self) -> Any:
        """RealBall.arctanh(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3489)

        Return the inverse hyperbolic tangent of this ball.

        EXAMPLES::

            sage: RBF(0).arctanh()
            0
            sage: RBF(1/2).arctanh()
            [0.549306144334055 +/- ...e-16]
            sage: RBF(1).arctanh()
            nan"""
    @overload
    def below_abs(self, test_zero=...) -> Any:
        """RealBall.below_abs(self, test_zero=False)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 1857)

        Return a lower bound for the absolute value of this ball.

        INPUT:

        - ``test_zero`` -- boolean (default: ``False``); if ``True``,
          make sure that the returned lower bound is positive, raising
          an error if the ball contains zero.

        OUTPUT: a ball with zero radius

        EXAMPLES::

            sage: RealBallField(8)(1/3).below_abs()
            [0.33 +/- ...e-5]
            sage: b = RealBallField(8)(1/3).below_abs()
            sage: b
            [0.33 +/- ...e-5]
            sage: b.is_exact()
            True
            sage: QQ(b)
            169/512

            sage: RBF(0).below_abs()
            0
            sage: RBF(0).below_abs(test_zero=True)
            Traceback (most recent call last):
            ...
            ValueError: ball contains zero

        .. SEEALSO:: :meth:`above_abs`"""
    @overload
    def below_abs(self) -> Any:
        """RealBall.below_abs(self, test_zero=False)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 1857)

        Return a lower bound for the absolute value of this ball.

        INPUT:

        - ``test_zero`` -- boolean (default: ``False``); if ``True``,
          make sure that the returned lower bound is positive, raising
          an error if the ball contains zero.

        OUTPUT: a ball with zero radius

        EXAMPLES::

            sage: RealBallField(8)(1/3).below_abs()
            [0.33 +/- ...e-5]
            sage: b = RealBallField(8)(1/3).below_abs()
            sage: b
            [0.33 +/- ...e-5]
            sage: b.is_exact()
            True
            sage: QQ(b)
            169/512

            sage: RBF(0).below_abs()
            0
            sage: RBF(0).below_abs(test_zero=True)
            Traceback (most recent call last):
            ...
            ValueError: ball contains zero

        .. SEEALSO:: :meth:`above_abs`"""
    @overload
    def below_abs(self) -> Any:
        """RealBall.below_abs(self, test_zero=False)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 1857)

        Return a lower bound for the absolute value of this ball.

        INPUT:

        - ``test_zero`` -- boolean (default: ``False``); if ``True``,
          make sure that the returned lower bound is positive, raising
          an error if the ball contains zero.

        OUTPUT: a ball with zero radius

        EXAMPLES::

            sage: RealBallField(8)(1/3).below_abs()
            [0.33 +/- ...e-5]
            sage: b = RealBallField(8)(1/3).below_abs()
            sage: b
            [0.33 +/- ...e-5]
            sage: b.is_exact()
            True
            sage: QQ(b)
            169/512

            sage: RBF(0).below_abs()
            0
            sage: RBF(0).below_abs(test_zero=True)
            Traceback (most recent call last):
            ...
            ValueError: ball contains zero

        .. SEEALSO:: :meth:`above_abs`"""
    @overload
    def below_abs(self) -> Any:
        """RealBall.below_abs(self, test_zero=False)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 1857)

        Return a lower bound for the absolute value of this ball.

        INPUT:

        - ``test_zero`` -- boolean (default: ``False``); if ``True``,
          make sure that the returned lower bound is positive, raising
          an error if the ball contains zero.

        OUTPUT: a ball with zero radius

        EXAMPLES::

            sage: RealBallField(8)(1/3).below_abs()
            [0.33 +/- ...e-5]
            sage: b = RealBallField(8)(1/3).below_abs()
            sage: b
            [0.33 +/- ...e-5]
            sage: b.is_exact()
            True
            sage: QQ(b)
            169/512

            sage: RBF(0).below_abs()
            0
            sage: RBF(0).below_abs(test_zero=True)
            Traceback (most recent call last):
            ...
            ValueError: ball contains zero

        .. SEEALSO:: :meth:`above_abs`"""
    @overload
    def below_abs(self, test_zero=...) -> Any:
        """RealBall.below_abs(self, test_zero=False)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 1857)

        Return a lower bound for the absolute value of this ball.

        INPUT:

        - ``test_zero`` -- boolean (default: ``False``); if ``True``,
          make sure that the returned lower bound is positive, raising
          an error if the ball contains zero.

        OUTPUT: a ball with zero radius

        EXAMPLES::

            sage: RealBallField(8)(1/3).below_abs()
            [0.33 +/- ...e-5]
            sage: b = RealBallField(8)(1/3).below_abs()
            sage: b
            [0.33 +/- ...e-5]
            sage: b.is_exact()
            True
            sage: QQ(b)
            169/512

            sage: RBF(0).below_abs()
            0
            sage: RBF(0).below_abs(test_zero=True)
            Traceback (most recent call last):
            ...
            ValueError: ball contains zero

        .. SEEALSO:: :meth:`above_abs`"""
    @overload
    def beta(self, a, z=...) -> Any:
        """RealBall.beta(self, a, z=1)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3689)

        (Incomplete) beta function.

        INPUT:

        - ``a``, ``z`` -- (optional) real balls

        OUTPUT:

        The lower incomplete beta function `B(self, a, z)`.

        With the default value of ``z``, the complete beta function `B(self, a)`.

        EXAMPLES::

            sage: RBF(sin(3)).beta(RBF(2/3).sqrt())  # abs tol 1e-13                    # needs sage.symbolic
            [7.407661629415 +/- 1.07e-13]
            sage: RealBallField(100)(7/2).beta(1)  # abs tol 1e-30
            [0.28571428571428571428571428571 +/- 5.23e-30]
            sage: RealBallField(100)(7/2).beta(1, 1/2)
            [0.025253813613805268728601584361 +/- 2.53e-31]

        .. TODO::

            At the moment RBF(beta(a,b)) does not work, one needs
            RBF(a).beta(b) for this to work. See :issue:`32851`
            and :issue:`24641`."""
    @overload
    def beta(self, a, b) -> Any:
        """RealBall.beta(self, a, z=1)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3689)

        (Incomplete) beta function.

        INPUT:

        - ``a``, ``z`` -- (optional) real balls

        OUTPUT:

        The lower incomplete beta function `B(self, a, z)`.

        With the default value of ``z``, the complete beta function `B(self, a)`.

        EXAMPLES::

            sage: RBF(sin(3)).beta(RBF(2/3).sqrt())  # abs tol 1e-13                    # needs sage.symbolic
            [7.407661629415 +/- 1.07e-13]
            sage: RealBallField(100)(7/2).beta(1)  # abs tol 1e-30
            [0.28571428571428571428571428571 +/- 5.23e-30]
            sage: RealBallField(100)(7/2).beta(1, 1/2)
            [0.025253813613805268728601584361 +/- 2.53e-31]

        .. TODO::

            At the moment RBF(beta(a,b)) does not work, one needs
            RBF(a).beta(b) for this to work. See :issue:`32851`
            and :issue:`24641`."""
    @overload
    def beta(self, b) -> Any:
        """RealBall.beta(self, a, z=1)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3689)

        (Incomplete) beta function.

        INPUT:

        - ``a``, ``z`` -- (optional) real balls

        OUTPUT:

        The lower incomplete beta function `B(self, a, z)`.

        With the default value of ``z``, the complete beta function `B(self, a)`.

        EXAMPLES::

            sage: RBF(sin(3)).beta(RBF(2/3).sqrt())  # abs tol 1e-13                    # needs sage.symbolic
            [7.407661629415 +/- 1.07e-13]
            sage: RealBallField(100)(7/2).beta(1)  # abs tol 1e-30
            [0.28571428571428571428571428571 +/- 5.23e-30]
            sage: RealBallField(100)(7/2).beta(1, 1/2)
            [0.025253813613805268728601584361 +/- 2.53e-31]

        .. TODO::

            At the moment RBF(beta(a,b)) does not work, one needs
            RBF(a).beta(b) for this to work. See :issue:`32851`
            and :issue:`24641`."""
    @overload
    def ceil(self) -> Any:
        """RealBall.ceil(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3011)

        Return the ceil of this ball.

        EXAMPLES::

            sage: RBF(1000+1/3, rad=1.r).ceil()
            [1.00e+3 +/- 2.01]"""
    @overload
    def ceil(self) -> Any:
        """RealBall.ceil(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3011)

        Return the ceil of this ball.

        EXAMPLES::

            sage: RBF(1000+1/3, rad=1.r).ceil()
            [1.00e+3 +/- 2.01]"""
    def center(self, *args, **kwargs):
        """RealBall.mid(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 1718)

        Return the center of this ball.

        EXAMPLES::

            sage: RealBallField(16)(1/3).mid()
            0.3333
            sage: RealBallField(16)(1/3).mid().parent()
            Real Field with 16 bits of precision
            sage: RealBallField(16)(RBF(1/3)).mid().parent()
            Real Field with 53 bits of precision
            sage: RBF('inf').mid()
            +infinity

        ::

            sage: b = RBF(2)^(2^1000)
            sage: b.mid()
            +infinity

        .. SEEALSO:: :meth:`rad`, :meth:`squash`"""
    def chebyshev_T(self, n) -> Any:
        """RealBall.chebyshev_T(self, n)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3976)

        Evaluate the Chebyshev polynomial of the first kind ``T_n`` at this
        ball.

        EXAMPLES::

            sage: # needs sage.symbolic
            sage: RBF(pi).chebyshev_T(0)
            1.000000000000000
            sage: RBF(pi).chebyshev_T(1)
            [3.141592653589793 +/- ...e-16]
            sage: RBF(pi).chebyshev_T(10**20)
            Traceback (most recent call last):
            ...
            ValueError: index too large
            sage: RBF(pi).chebyshev_T(-1)
            Traceback (most recent call last):
            ...
            ValueError: expected a nonnegative index"""
    def chebyshev_U(self, n) -> Any:
        """RealBall.chebyshev_U(self, n)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 4009)

        Evaluate the Chebyshev polynomial of the second kind ``U_n`` at this
        ball.

        EXAMPLES::

            sage: # needs sage.symbolic
            sage: RBF(pi).chebyshev_U(0)
            1.000000000000000
            sage: RBF(pi).chebyshev_U(1)
            [6.283185307179586 +/- ...e-16]
            sage: RBF(pi).chebyshev_U(10**20)
            Traceback (most recent call last):
            ...
            ValueError: index too large
            sage: RBF(pi).chebyshev_U(-1)
            Traceback (most recent call last):
            ...
            ValueError: expected a nonnegative index"""
    @overload
    def conjugate(self) -> Any:
        """RealBall.conjugate(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3110)

        Return the conjugate of this ball.

        EXAMPLES::

            sage: RBF(1).conjugate()
            1.000000000000000"""
    @overload
    def conjugate(self) -> Any:
        """RealBall.conjugate(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3110)

        Return the conjugate of this ball.

        EXAMPLES::

            sage: RBF(1).conjugate()
            1.000000000000000"""
    @overload
    def contains_exact(self, other) -> Any:
        """RealBall.contains_exact(self, other)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 2564)

        Return ``True`` *iff* the given number (or ball) ``other`` is contained
        in the interval represented by ``self``.

        If ``self`` contains NaN, this function always returns ``True`` (as
        it could represent anything, and in particular could represent all the
        points included in ``other``). If ``other`` contains NaN and ``self``
        does not, it always returns ``False``.

        Use ``other in self`` for a test that works for a wider range of inputs
        but may return false negatives.

        EXAMPLES::

            sage: b = RBF(1)
            sage: b.contains_exact(1)
            True
            sage: b.contains_exact(QQ(1))
            True
            sage: b.contains_exact(1.)
            True
            sage: b.contains_exact(b)
            True

        ::

            sage: RBF(1/3).contains_exact(1/3)
            True
            sage: RBF(sqrt(2)).contains_exact(sqrt(2))                                  # needs sage.symbolic
            Traceback (most recent call last):
            ...
            TypeError: unsupported type: <class 'sage.symbolic.expression.Expression'>

        TESTS::

            sage: b.contains_exact(1r)
            True"""
    @overload
    def contains_exact(self, b) -> Any:
        """RealBall.contains_exact(self, other)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 2564)

        Return ``True`` *iff* the given number (or ball) ``other`` is contained
        in the interval represented by ``self``.

        If ``self`` contains NaN, this function always returns ``True`` (as
        it could represent anything, and in particular could represent all the
        points included in ``other``). If ``other`` contains NaN and ``self``
        does not, it always returns ``False``.

        Use ``other in self`` for a test that works for a wider range of inputs
        but may return false negatives.

        EXAMPLES::

            sage: b = RBF(1)
            sage: b.contains_exact(1)
            True
            sage: b.contains_exact(QQ(1))
            True
            sage: b.contains_exact(1.)
            True
            sage: b.contains_exact(b)
            True

        ::

            sage: RBF(1/3).contains_exact(1/3)
            True
            sage: RBF(sqrt(2)).contains_exact(sqrt(2))                                  # needs sage.symbolic
            Traceback (most recent call last):
            ...
            TypeError: unsupported type: <class 'sage.symbolic.expression.Expression'>

        TESTS::

            sage: b.contains_exact(1r)
            True"""
    @overload
    def contains_integer(self) -> Any:
        """RealBall.contains_integer(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 2665)

        Return ``True`` iff this ball contains any integer.

        EXAMPLES::

            sage: RBF(3.1, 0.1).contains_integer()
            True
            sage: RBF(3.1, 0.05).contains_integer()
            False"""
    @overload
    def contains_integer(self) -> Any:
        """RealBall.contains_integer(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 2665)

        Return ``True`` iff this ball contains any integer.

        EXAMPLES::

            sage: RBF(3.1, 0.1).contains_integer()
            True
            sage: RBF(3.1, 0.05).contains_integer()
            False"""
    @overload
    def contains_integer(self) -> Any:
        """RealBall.contains_integer(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 2665)

        Return ``True`` iff this ball contains any integer.

        EXAMPLES::

            sage: RBF(3.1, 0.1).contains_integer()
            True
            sage: RBF(3.1, 0.05).contains_integer()
            False"""
    @overload
    def contains_zero(self) -> Any:
        """RealBall.contains_zero(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 2650)

        Return ``True`` iff this ball contains zero.

        EXAMPLES::

            sage: RBF(0).contains_zero()
            True
            sage: RBF(RIF(-1, 1)).contains_zero()
            True
            sage: RBF(1/3).contains_zero()
            False"""
    @overload
    def contains_zero(self) -> Any:
        """RealBall.contains_zero(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 2650)

        Return ``True`` iff this ball contains zero.

        EXAMPLES::

            sage: RBF(0).contains_zero()
            True
            sage: RBF(RIF(-1, 1)).contains_zero()
            True
            sage: RBF(1/3).contains_zero()
            False"""
    @overload
    def contains_zero(self) -> Any:
        """RealBall.contains_zero(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 2650)

        Return ``True`` iff this ball contains zero.

        EXAMPLES::

            sage: RBF(0).contains_zero()
            True
            sage: RBF(RIF(-1, 1)).contains_zero()
            True
            sage: RBF(1/3).contains_zero()
            False"""
    @overload
    def contains_zero(self) -> Any:
        """RealBall.contains_zero(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 2650)

        Return ``True`` iff this ball contains zero.

        EXAMPLES::

            sage: RBF(0).contains_zero()
            True
            sage: RBF(RIF(-1, 1)).contains_zero()
            True
            sage: RBF(1/3).contains_zero()
            False"""
    @overload
    def cos(self) -> Any:
        """RealBall.cos(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3231)

        Return the cosine of this ball.

        EXAMPLES::

            sage: RBF(pi).cos()                                                         # needs sage.symbolic
            [-1.00000000000000 +/- ...e-16]

        .. SEEALSO:: :meth:`~sage.rings.real_arb.RealBallField.cospi`"""
    @overload
    def cos(self) -> Any:
        """RealBall.cos(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3231)

        Return the cosine of this ball.

        EXAMPLES::

            sage: RBF(pi).cos()                                                         # needs sage.symbolic
            [-1.00000000000000 +/- ...e-16]

        .. SEEALSO:: :meth:`~sage.rings.real_arb.RealBallField.cospi`"""
    def cos_integral(self, *args, **kwargs):
        """RealBall.Ci(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3582)

        Cosine integral.

        EXAMPLES::

            sage: RBF(1).Ci()  # abs tol 5e-16
            [0.337403922900968 +/- 3.25e-16]

        TESTS::

            sage: RBF(Ci(1))  # abs tol 5e-16                                           # needs sage.symbolic
            [0.337403922900968 +/- 3.25e-16]"""
    @overload
    def cosh(self) -> Any:
        """RealBall.cosh(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3376)

        Return the hyperbolic cosine of this ball.

        EXAMPLES::

            sage: RBF(1).cosh()
            [1.543080634815244 +/- ...e-16]"""
    @overload
    def cosh(self) -> Any:
        """RealBall.cosh(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3376)

        Return the hyperbolic cosine of this ball.

        EXAMPLES::

            sage: RBF(1).cosh()
            [1.543080634815244 +/- ...e-16]"""
    def cosh_integral(self, *args, **kwargs):
        """RealBall.Chi(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3626)

        Hyperbolic cosine integral.

        EXAMPLES::

            sage: RBF(1).Chi()  # abs tol 5e-16
            [0.837866940980208 +/- 4.72e-16]

        TESTS::

            sage: RBF(Chi(1))  # abs tol 5e-16                                          # needs sage.symbolic
            [0.837866940980208 +/- 4.72e-16]"""
    @overload
    def cot(self) -> Any:
        """RealBall.cot(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3265)

        Return the cotangent of this ball.

        EXAMPLES::

            sage: RBF(1).cot()
            [0.642092615934331 +/- ...e-16]
            sage: RBF(pi).cot()                                                         # needs sage.symbolic
            nan"""
    @overload
    def cot(self) -> Any:
        """RealBall.cot(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3265)

        Return the cotangent of this ball.

        EXAMPLES::

            sage: RBF(1).cot()
            [0.642092615934331 +/- ...e-16]
            sage: RBF(pi).cot()                                                         # needs sage.symbolic
            nan"""
    @overload
    def cot(self) -> Any:
        """RealBall.cot(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3265)

        Return the cotangent of this ball.

        EXAMPLES::

            sage: RBF(1).cot()
            [0.642092615934331 +/- ...e-16]
            sage: RBF(pi).cot()                                                         # needs sage.symbolic
            nan"""
    @overload
    def coth(self) -> Any:
        """RealBall.coth(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3406)

        Return the hyperbolic cotangent of this ball.

        EXAMPLES::

            sage: RBF(1).coth()
            [1.313035285499331 +/- ...e-16]
            sage: RBF(0).coth()
            nan"""
    @overload
    def coth(self) -> Any:
        """RealBall.coth(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3406)

        Return the hyperbolic cotangent of this ball.

        EXAMPLES::

            sage: RBF(1).coth()
            [1.313035285499331 +/- ...e-16]
            sage: RBF(0).coth()
            nan"""
    @overload
    def coth(self) -> Any:
        """RealBall.coth(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3406)

        Return the hyperbolic cotangent of this ball.

        EXAMPLES::

            sage: RBF(1).coth()
            [1.313035285499331 +/- ...e-16]
            sage: RBF(0).coth()
            nan"""
    @overload
    def csc(self) -> Any:
        """RealBall.csc(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3297)

        Return the cosecant of this ball.

        EXAMPLES::

            sage: RBF(1).csc()
            [1.188395105778121 +/- ...e-16]"""
    @overload
    def csc(self) -> Any:
        """RealBall.csc(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3297)

        Return the cosecant of this ball.

        EXAMPLES::

            sage: RBF(1).csc()
            [1.188395105778121 +/- ...e-16]"""
    @overload
    def csch(self) -> Any:
        """RealBall.csch(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3438)

        Return the hyperbolic cosecant of this ball.

        EXAMPLES::

            sage: RBF(1).csch()
            [0.850918128239321 +/- ...e-16]"""
    @overload
    def csch(self) -> Any:
        """RealBall.csch(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3438)

        Return the hyperbolic cosecant of this ball.

        EXAMPLES::

            sage: RBF(1).csch()
            [0.850918128239321 +/- ...e-16]"""
    @overload
    def diameter(self) -> Any:
        """RealBall.diameter(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 1783)

        Return the diameter of this ball.

        EXAMPLES::

            sage: RBF(1/3).diameter()
            1.1102230e-16
            sage: RBF(1/3).diameter().parent()
            Real Field with 30 bits of precision
            sage: RBF(RIF(1.02, 1.04)).diameter()
            0.020000000

        .. SEEALSO:: :meth:`rad`, :meth:`rad_as_ball`, :meth:`mid`"""
    @overload
    def diameter(self) -> Any:
        """RealBall.diameter(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 1783)

        Return the diameter of this ball.

        EXAMPLES::

            sage: RBF(1/3).diameter()
            1.1102230e-16
            sage: RBF(1/3).diameter().parent()
            Real Field with 30 bits of precision
            sage: RBF(RIF(1.02, 1.04)).diameter()
            0.020000000

        .. SEEALSO:: :meth:`rad`, :meth:`rad_as_ball`, :meth:`mid`"""
    @overload
    def diameter(self) -> Any:
        """RealBall.diameter(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 1783)

        Return the diameter of this ball.

        EXAMPLES::

            sage: RBF(1/3).diameter()
            1.1102230e-16
            sage: RBF(1/3).diameter().parent()
            Real Field with 30 bits of precision
            sage: RBF(RIF(1.02, 1.04)).diameter()
            0.020000000

        .. SEEALSO:: :meth:`rad`, :meth:`rad_as_ball`, :meth:`mid`"""
    @overload
    def diameter(self) -> Any:
        """RealBall.diameter(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 1783)

        Return the diameter of this ball.

        EXAMPLES::

            sage: RBF(1/3).diameter()
            1.1102230e-16
            sage: RBF(1/3).diameter().parent()
            Real Field with 30 bits of precision
            sage: RBF(RIF(1.02, 1.04)).diameter()
            0.020000000

        .. SEEALSO:: :meth:`rad`, :meth:`rad_as_ball`, :meth:`mid`"""
    @overload
    def endpoints(self, rnd=...) -> Any:
        """RealBall.endpoints(self, rnd=None)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 1969)

        Return the endpoints of this ball, rounded outwards.

        INPUT:

        - ``rnd`` -- string; rounding mode for the parent of the resulting
          floating-point numbers (does not affect their values!), see
          :meth:`sage.rings.real_mpfi.RealIntervalFieldElement.upper`

        OUTPUT: a pair of real numbers

        EXAMPLES::

            sage: RBF(-1/3).endpoints()
            (-0.333333333333334, -0.333333333333333)

        .. SEEALSO:: :meth:`lower`, :meth:`upper`"""
    @overload
    def endpoints(self) -> Any:
        """RealBall.endpoints(self, rnd=None)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 1969)

        Return the endpoints of this ball, rounded outwards.

        INPUT:

        - ``rnd`` -- string; rounding mode for the parent of the resulting
          floating-point numbers (does not affect their values!), see
          :meth:`sage.rings.real_mpfi.RealIntervalFieldElement.upper`

        OUTPUT: a pair of real numbers

        EXAMPLES::

            sage: RBF(-1/3).endpoints()
            (-0.333333333333334, -0.333333333333333)

        .. SEEALSO:: :meth:`lower`, :meth:`upper`"""
    @overload
    def erf(self) -> Any:
        """RealBall.erf(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3510)

        Error function.

        EXAMPLES::

            sage: RBF(1/2).erf() # abs tol 1e-16
            [0.520499877813047 +/- 6.10e-16]"""
    @overload
    def erf(self) -> Any:
        """RealBall.erf(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3510)

        Error function.

        EXAMPLES::

            sage: RBF(1/2).erf() # abs tol 1e-16
            [0.520499877813047 +/- 6.10e-16]"""
    @overload
    def erfi(self) -> Any:
        """RealBall.erfi(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3525)

        Imaginary error function.

        EXAMPLES::

            sage: RBF(1/2).erfi()
            [0.614952094696511 +/- 2.22e-16]"""
    @overload
    def erfi(self) -> Any:
        """RealBall.erfi(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3525)

        Imaginary error function.

        EXAMPLES::

            sage: RBF(1/2).erfi()
            [0.614952094696511 +/- 2.22e-16]"""
    @overload
    def exp(self) -> Any:
        """RealBall.exp(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3180)

        Return the exponential of this ball.

        EXAMPLES::

            sage: RBF(1).exp()
            [2.718281828459045 +/- ...e-16]"""
    @overload
    def exp(self) -> Any:
        """RealBall.exp(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3180)

        Return the exponential of this ball.

        EXAMPLES::

            sage: RBF(1).exp()
            [2.718281828459045 +/- ...e-16]"""
    @overload
    def expm1(self) -> Any:
        """RealBall.expm1(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3195)

        Return ``exp(self) - 1``, computed accurately when ``self`` is close to
        zero.

        EXAMPLES::

            sage: eps = RBF(1e-30)
            sage: exp(eps) - 1
            [+/- ...e-30]
            sage: eps.expm1()
            [1.000000000000000e-30 +/- ...e-47]"""
    @overload
    def expm1(self) -> Any:
        """RealBall.expm1(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3195)

        Return ``exp(self) - 1``, computed accurately when ``self`` is close to
        zero.

        EXAMPLES::

            sage: eps = RBF(1e-30)
            sage: exp(eps) - 1
            [+/- ...e-30]
            sage: eps.expm1()
            [1.000000000000000e-30 +/- ...e-47]"""
    @overload
    def floor(self) -> Any:
        """RealBall.floor(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 2996)

        Return the floor of this ball.

        EXAMPLES::

            sage: RBF(1000+1/3, rad=1.r).floor()
            [1.00e+3 +/- 1.01]"""
    @overload
    def floor(self) -> Any:
        """RealBall.floor(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 2996)

        Return the floor of this ball.

        EXAMPLES::

            sage: RBF(1000+1/3, rad=1.r).floor()
            [1.00e+3 +/- 1.01]"""
    def gamma(self, a=...) -> Any:
        """RealBall.gamma(self, a=None)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3728)

        Image of this ball by the (upper incomplete) Euler Gamma function.

        For `a` real, return the upper incomplete Gamma function
        `\\Gamma(self,a)`.

        For integer and rational arguments,
        :meth:`~sage.rings.real_arb.RealBallField.gamma` may be faster.

        EXAMPLES::

            sage: RBF(1/2).gamma()
            [1.772453850905516 +/- ...e-16]
            sage: RBF(gamma(3/2, RBF(2).sqrt()))  # abs tol 2e-17
            [0.37118875695353 +/- 3.00e-15]
            sage: RBF(3/2).gamma_inc(RBF(2).sqrt())  # abs tol 2e-17
            [0.37118875695353 +/- 3.00e-15]

        .. SEEALSO::
            :meth:`~sage.rings.real_arb.RealBallField.gamma`

        TESTS::

            sage: RealBallField(100).gamma(1/2)
            [1.77245385090551602729816748334 +/- 1.90e-30]"""
    def gamma_inc(self, *args, **kwargs):
        """RealBall.gamma(self, a=None)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3728)

        Image of this ball by the (upper incomplete) Euler Gamma function.

        For `a` real, return the upper incomplete Gamma function
        `\\Gamma(self,a)`.

        For integer and rational arguments,
        :meth:`~sage.rings.real_arb.RealBallField.gamma` may be faster.

        EXAMPLES::

            sage: RBF(1/2).gamma()
            [1.772453850905516 +/- ...e-16]
            sage: RBF(gamma(3/2, RBF(2).sqrt()))  # abs tol 2e-17
            [0.37118875695353 +/- 3.00e-15]
            sage: RBF(3/2).gamma_inc(RBF(2).sqrt())  # abs tol 2e-17
            [0.37118875695353 +/- 3.00e-15]

        .. SEEALSO::
            :meth:`~sage.rings.real_arb.RealBallField.gamma`

        TESTS::

            sage: RealBallField(100).gamma(1/2)
            [1.77245385090551602729816748334 +/- 1.90e-30]"""
    def gamma_inc_lower(self, a) -> Any:
        """RealBall.gamma_inc_lower(self, a)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3770)

        Image of this ball by the lower incomplete Euler Gamma function.

        For `a` real, return the lower incomplete Gamma function
        of `\\Gamma(self,a)`.

        EXAMPLES::

            sage: RBF(gamma_inc_lower(1/2, RBF(2).sqrt()))
            [1.608308637729248 +/- 8.14e-16]
            sage: RealBallField(100)(7/2).gamma_inc_lower(5)
            [2.6966551541863035516887949614 +/- 8.91e-29]"""
    def identical(self, RealBallother) -> Any:
        """RealBall.identical(self, RealBall other)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 2524)

        Return ``True`` iff ``self`` and ``other`` are equal as balls, i.e.
        have both the same midpoint and radius.

        Note that this is not the same thing as testing whether both ``self``
        and ``other`` certainly represent the same real number, unless either
        ``self`` or ``other`` is exact (and neither contains NaN). To test
        whether both operands might represent the same mathematical quantity,
        use :meth:`overlaps` or :meth:`contains`, depending on the
        circumstance.

        EXAMPLES::

            sage: RBF(1).identical(RBF(3)-RBF(2))
            True
            sage: RBF(1, rad=0.25r).identical(RBF(1, rad=0.25r))
            True
            sage: RBF(1).identical(RBF(1, rad=0.25r))
            False"""
    @overload
    def imag(self) -> Any:
        """RealBall.imag(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 2018)

        Return the imaginary part of this ball.

        EXAMPLES::

            sage: RBF(1/3).imag()
            0"""
    @overload
    def imag(self) -> Any:
        """RealBall.imag(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 2018)

        Return the imaginary part of this ball.

        EXAMPLES::

            sage: RBF(1/3).imag()
            0"""
    @overload
    def is_NaN(self) -> Any:
        """RealBall.is_NaN(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 2732)

        Return ``True`` if this ball is not-a-number.

        EXAMPLES::

            sage: RBF(NaN).is_NaN()                                                     # needs sage.symbolic
            True
            sage: RBF(-5).gamma().is_NaN()
            True
            sage: RBF(infinity).is_NaN()
            False
            sage: RBF(42, rad=1.r).is_NaN()
            False"""
    @overload
    def is_NaN(self) -> Any:
        """RealBall.is_NaN(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 2732)

        Return ``True`` if this ball is not-a-number.

        EXAMPLES::

            sage: RBF(NaN).is_NaN()                                                     # needs sage.symbolic
            True
            sage: RBF(-5).gamma().is_NaN()
            True
            sage: RBF(infinity).is_NaN()
            False
            sage: RBF(42, rad=1.r).is_NaN()
            False"""
    @overload
    def is_NaN(self) -> Any:
        """RealBall.is_NaN(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 2732)

        Return ``True`` if this ball is not-a-number.

        EXAMPLES::

            sage: RBF(NaN).is_NaN()                                                     # needs sage.symbolic
            True
            sage: RBF(-5).gamma().is_NaN()
            True
            sage: RBF(infinity).is_NaN()
            False
            sage: RBF(42, rad=1.r).is_NaN()
            False"""
    @overload
    def is_NaN(self) -> Any:
        """RealBall.is_NaN(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 2732)

        Return ``True`` if this ball is not-a-number.

        EXAMPLES::

            sage: RBF(NaN).is_NaN()                                                     # needs sage.symbolic
            True
            sage: RBF(-5).gamma().is_NaN()
            True
            sage: RBF(infinity).is_NaN()
            False
            sage: RBF(42, rad=1.r).is_NaN()
            False"""
    @overload
    def is_NaN(self) -> Any:
        """RealBall.is_NaN(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 2732)

        Return ``True`` if this ball is not-a-number.

        EXAMPLES::

            sage: RBF(NaN).is_NaN()                                                     # needs sage.symbolic
            True
            sage: RBF(-5).gamma().is_NaN()
            True
            sage: RBF(infinity).is_NaN()
            False
            sage: RBF(42, rad=1.r).is_NaN()
            False"""
    @overload
    def is_exact(self) -> Any:
        """RealBall.is_exact(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 2232)

        Return ``True`` iff the radius of this ball is zero.

        EXAMPLES::

            sage: RBF = RealBallField()
            sage: RBF(1).is_exact()
            True
            sage: RBF(RIF(0.1, 0.2)).is_exact()
            False"""
    @overload
    def is_exact(self) -> Any:
        """RealBall.is_exact(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 2232)

        Return ``True`` iff the radius of this ball is zero.

        EXAMPLES::

            sage: RBF = RealBallField()
            sage: RBF(1).is_exact()
            True
            sage: RBF(RIF(0.1, 0.2)).is_exact()
            False"""
    @overload
    def is_exact(self) -> Any:
        """RealBall.is_exact(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 2232)

        Return ``True`` iff the radius of this ball is zero.

        EXAMPLES::

            sage: RBF = RealBallField()
            sage: RBF(1).is_exact()
            True
            sage: RBF(RIF(0.1, 0.2)).is_exact()
            False"""
    @overload
    def is_finite(self) -> Any:
        """RealBall.is_finite(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 2510)

        Return ``True`` iff the midpoint and radius of this ball are both
        finite floating-point numbers, i.e. not infinities or NaN.

        EXAMPLES::

            sage: (RBF(2)^(2^1000)).is_finite()
            True
            sage: RBF(oo).is_finite()
            False"""
    @overload
    def is_finite(self) -> Any:
        """RealBall.is_finite(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 2510)

        Return ``True`` iff the midpoint and radius of this ball are both
        finite floating-point numbers, i.e. not infinities or NaN.

        EXAMPLES::

            sage: (RBF(2)^(2^1000)).is_finite()
            True
            sage: RBF(oo).is_finite()
            False"""
    @overload
    def is_finite(self) -> Any:
        """RealBall.is_finite(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 2510)

        Return ``True`` iff the midpoint and radius of this ball are both
        finite floating-point numbers, i.e. not infinities or NaN.

        EXAMPLES::

            sage: (RBF(2)^(2^1000)).is_finite()
            True
            sage: RBF(oo).is_finite()
            False"""
    @overload
    def is_infinity(self) -> Any:
        """RealBall.is_infinity(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 2702)

        Return ``True`` if this ball contains or may represent a point at
        infinity.

        This is the exact negation of :meth:`is_finite`, used in comparisons
        with Sage symbolic infinities.

        .. WARNING::

            Contrary to the usual convention, a return value of ``True`` does
            not imply that all points of the ball satisfy the predicate.
            This is due to the way comparisons with symbolic infinities work in
            sage.

        EXAMPLES::

            sage: RBF(infinity).is_infinity()
            True
            sage: RBF(-infinity).is_infinity()
            True
            sage: RBF(NaN).is_infinity()                                                # needs sage.symbolic
            True
            sage: (~RBF(0)).is_infinity()
            True
            sage: RBF(42, rad=1.r).is_infinity()
            False"""
    @overload
    def is_infinity(self) -> Any:
        """RealBall.is_infinity(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 2702)

        Return ``True`` if this ball contains or may represent a point at
        infinity.

        This is the exact negation of :meth:`is_finite`, used in comparisons
        with Sage symbolic infinities.

        .. WARNING::

            Contrary to the usual convention, a return value of ``True`` does
            not imply that all points of the ball satisfy the predicate.
            This is due to the way comparisons with symbolic infinities work in
            sage.

        EXAMPLES::

            sage: RBF(infinity).is_infinity()
            True
            sage: RBF(-infinity).is_infinity()
            True
            sage: RBF(NaN).is_infinity()                                                # needs sage.symbolic
            True
            sage: (~RBF(0)).is_infinity()
            True
            sage: RBF(42, rad=1.r).is_infinity()
            False"""
    @overload
    def is_infinity(self) -> Any:
        """RealBall.is_infinity(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 2702)

        Return ``True`` if this ball contains or may represent a point at
        infinity.

        This is the exact negation of :meth:`is_finite`, used in comparisons
        with Sage symbolic infinities.

        .. WARNING::

            Contrary to the usual convention, a return value of ``True`` does
            not imply that all points of the ball satisfy the predicate.
            This is due to the way comparisons with symbolic infinities work in
            sage.

        EXAMPLES::

            sage: RBF(infinity).is_infinity()
            True
            sage: RBF(-infinity).is_infinity()
            True
            sage: RBF(NaN).is_infinity()                                                # needs sage.symbolic
            True
            sage: (~RBF(0)).is_infinity()
            True
            sage: RBF(42, rad=1.r).is_infinity()
            False"""
    @overload
    def is_infinity(self) -> Any:
        """RealBall.is_infinity(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 2702)

        Return ``True`` if this ball contains or may represent a point at
        infinity.

        This is the exact negation of :meth:`is_finite`, used in comparisons
        with Sage symbolic infinities.

        .. WARNING::

            Contrary to the usual convention, a return value of ``True`` does
            not imply that all points of the ball satisfy the predicate.
            This is due to the way comparisons with symbolic infinities work in
            sage.

        EXAMPLES::

            sage: RBF(infinity).is_infinity()
            True
            sage: RBF(-infinity).is_infinity()
            True
            sage: RBF(NaN).is_infinity()                                                # needs sage.symbolic
            True
            sage: (~RBF(0)).is_infinity()
            True
            sage: RBF(42, rad=1.r).is_infinity()
            False"""
    @overload
    def is_infinity(self) -> Any:
        """RealBall.is_infinity(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 2702)

        Return ``True`` if this ball contains or may represent a point at
        infinity.

        This is the exact negation of :meth:`is_finite`, used in comparisons
        with Sage symbolic infinities.

        .. WARNING::

            Contrary to the usual convention, a return value of ``True`` does
            not imply that all points of the ball satisfy the predicate.
            This is due to the way comparisons with symbolic infinities work in
            sage.

        EXAMPLES::

            sage: RBF(infinity).is_infinity()
            True
            sage: RBF(-infinity).is_infinity()
            True
            sage: RBF(NaN).is_infinity()                                                # needs sage.symbolic
            True
            sage: (~RBF(0)).is_infinity()
            True
            sage: RBF(42, rad=1.r).is_infinity()
            False"""
    @overload
    def is_infinity(self) -> Any:
        """RealBall.is_infinity(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 2702)

        Return ``True`` if this ball contains or may represent a point at
        infinity.

        This is the exact negation of :meth:`is_finite`, used in comparisons
        with Sage symbolic infinities.

        .. WARNING::

            Contrary to the usual convention, a return value of ``True`` does
            not imply that all points of the ball satisfy the predicate.
            This is due to the way comparisons with symbolic infinities work in
            sage.

        EXAMPLES::

            sage: RBF(infinity).is_infinity()
            True
            sage: RBF(-infinity).is_infinity()
            True
            sage: RBF(NaN).is_infinity()                                                # needs sage.symbolic
            True
            sage: (~RBF(0)).is_infinity()
            True
            sage: RBF(42, rad=1.r).is_infinity()
            False"""
    @overload
    def is_negative_infinity(self) -> Any:
        """RealBall.is_negative_infinity(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 2678)

        Return ``True`` if this ball is the point -∞.

        EXAMPLES::

            sage: RBF(-infinity).is_negative_infinity()
            True"""
    @overload
    def is_negative_infinity(self) -> Any:
        """RealBall.is_negative_infinity(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 2678)

        Return ``True`` if this ball is the point -∞.

        EXAMPLES::

            sage: RBF(-infinity).is_negative_infinity()
            True"""
    @overload
    def is_nonzero(self) -> Any:
        """RealBall.is_nonzero(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 2181)

        Return ``True`` iff zero is not contained in the interval represented
        by this ball.

        .. NOTE::

            This method is not the negation of :meth:`is_zero`: it only
            returns ``True`` if zero is known not to be contained in the ball.

            Use ``bool(b)`` (or, equivalently, ``not b.is_zero()``) to check if
            a ball\xa0``b`` **may** represent a nonzero number (for instance, to
            determine the “degree” of a polynomial with ball coefficients).

        EXAMPLES::

            sage: RBF = RealBallField()
            sage: RBF(pi).is_nonzero()                                                  # needs sage.symbolic
            True
            sage: RBF(RIF(-0.5, 0.5)).is_nonzero()
            False

        .. SEEALSO:: :meth:`is_zero`"""
    @overload
    def is_nonzero(self) -> Any:
        """RealBall.is_nonzero(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 2181)

        Return ``True`` iff zero is not contained in the interval represented
        by this ball.

        .. NOTE::

            This method is not the negation of :meth:`is_zero`: it only
            returns ``True`` if zero is known not to be contained in the ball.

            Use ``bool(b)`` (or, equivalently, ``not b.is_zero()``) to check if
            a ball\xa0``b`` **may** represent a nonzero number (for instance, to
            determine the “degree” of a polynomial with ball coefficients).

        EXAMPLES::

            sage: RBF = RealBallField()
            sage: RBF(pi).is_nonzero()                                                  # needs sage.symbolic
            True
            sage: RBF(RIF(-0.5, 0.5)).is_nonzero()
            False

        .. SEEALSO:: :meth:`is_zero`"""
    @overload
    def is_nonzero(self) -> Any:
        """RealBall.is_nonzero(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 2181)

        Return ``True`` iff zero is not contained in the interval represented
        by this ball.

        .. NOTE::

            This method is not the negation of :meth:`is_zero`: it only
            returns ``True`` if zero is known not to be contained in the ball.

            Use ``bool(b)`` (or, equivalently, ``not b.is_zero()``) to check if
            a ball\xa0``b`` **may** represent a nonzero number (for instance, to
            determine the “degree” of a polynomial with ball coefficients).

        EXAMPLES::

            sage: RBF = RealBallField()
            sage: RBF(pi).is_nonzero()                                                  # needs sage.symbolic
            True
            sage: RBF(RIF(-0.5, 0.5)).is_nonzero()
            False

        .. SEEALSO:: :meth:`is_zero`"""
    @overload
    def is_positive_infinity(self) -> Any:
        """RealBall.is_positive_infinity(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 2690)

        Return ``True`` if this ball is the point +∞.

        EXAMPLES::

            sage: RBF(infinity).is_positive_infinity()
            True"""
    @overload
    def is_positive_infinity(self) -> Any:
        """RealBall.is_positive_infinity(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 2690)

        Return ``True`` if this ball is the point +∞.

        EXAMPLES::

            sage: RBF(infinity).is_positive_infinity()
            True"""
    @overload
    def is_zero(self) -> Any:
        """RealBall.is_zero(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 2165)

        Return ``True`` iff the midpoint and radius of this ball are both zero.

        EXAMPLES::

            sage: RBF = RealBallField()
            sage: RBF(0).is_zero()
            True
            sage: RBF(RIF(-0.5, 0.5)).is_zero()
            False

        .. SEEALSO:: :meth:`is_nonzero`"""
    @overload
    def is_zero(self) -> Any:
        """RealBall.is_zero(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 2165)

        Return ``True`` iff the midpoint and radius of this ball are both zero.

        EXAMPLES::

            sage: RBF = RealBallField()
            sage: RBF(0).is_zero()
            True
            sage: RBF(RIF(-0.5, 0.5)).is_zero()
            False

        .. SEEALSO:: :meth:`is_nonzero`"""
    @overload
    def is_zero(self) -> Any:
        """RealBall.is_zero(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 2165)

        Return ``True`` iff the midpoint and radius of this ball are both zero.

        EXAMPLES::

            sage: RBF = RealBallField()
            sage: RBF(0).is_zero()
            True
            sage: RBF(RIF(-0.5, 0.5)).is_zero()
            False

        .. SEEALSO:: :meth:`is_nonzero`"""
    @overload
    def lambert_w(self) -> Any:
        """RealBall.lambert_w(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3919)

        Return the image of this ball by the Lambert\xa0W function.

        EXAMPLES::

            sage: RBF(1).lambert_w()
            [0.5671432904097...]"""
    @overload
    def lambert_w(self) -> Any:
        """RealBall.lambert_w(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3919)

        Return the image of this ball by the Lambert\xa0W function.

        EXAMPLES::

            sage: RBF(1).lambert_w()
            [0.5671432904097...]"""
    @overload
    def li(self) -> Any:
        """RealBall.li(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3648)

        Logarithmic integral.

        EXAMPLES::

            sage: RBF(3).li()  # abs tol 5e-15
            [2.16358859466719 +/- 4.72e-15]

        TESTS::

            sage: RBF(li(0))                                                            # needs sage.symbolic
            0
            sage: RBF(Li(0))  # abs tol 5e-15                                           # needs sage.symbolic
            [-1.04516378011749 +/- 4.23e-15]"""
    @overload
    def li(self) -> Any:
        """RealBall.li(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3648)

        Logarithmic integral.

        EXAMPLES::

            sage: RBF(3).li()  # abs tol 5e-15
            [2.16358859466719 +/- 4.72e-15]

        TESTS::

            sage: RBF(li(0))                                                            # needs sage.symbolic
            0
            sage: RBF(Li(0))  # abs tol 5e-15                                           # needs sage.symbolic
            [-1.04516378011749 +/- 4.23e-15]"""
    @overload
    def log(self, base=...) -> Any:
        """RealBall.log(self, base=None)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3123)

        Return the logarithm of this ball.

        INPUT:

        - ``base`` -- (optional) positive real ball or number; if ``None``,
          return the natural logarithm ``ln(self)``, otherwise, return the
          general logarithm ``ln(self)/ln(base)``

        EXAMPLES::

            sage: RBF(3).log()
            [1.098612288668110 +/- ...e-16]
            sage: RBF(3).log(2)
            [1.58496250072116 +/- ...e-15]
            sage: log(RBF(5), 2)
            [2.32192809488736 +/- ...e-15]

            sage: RBF(-1/3).log()
            nan
            sage: RBF(3).log(-1)
            nan
            sage: RBF(2).log(0)
            nan"""
    @overload
    def log(self) -> Any:
        """RealBall.log(self, base=None)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3123)

        Return the logarithm of this ball.

        INPUT:

        - ``base`` -- (optional) positive real ball or number; if ``None``,
          return the natural logarithm ``ln(self)``, otherwise, return the
          general logarithm ``ln(self)/ln(base)``

        EXAMPLES::

            sage: RBF(3).log()
            [1.098612288668110 +/- ...e-16]
            sage: RBF(3).log(2)
            [1.58496250072116 +/- ...e-15]
            sage: log(RBF(5), 2)
            [2.32192809488736 +/- ...e-15]

            sage: RBF(-1/3).log()
            nan
            sage: RBF(3).log(-1)
            nan
            sage: RBF(2).log(0)
            nan"""
    @overload
    def log(self) -> Any:
        """RealBall.log(self, base=None)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3123)

        Return the logarithm of this ball.

        INPUT:

        - ``base`` -- (optional) positive real ball or number; if ``None``,
          return the natural logarithm ``ln(self)``, otherwise, return the
          general logarithm ``ln(self)/ln(base)``

        EXAMPLES::

            sage: RBF(3).log()
            [1.098612288668110 +/- ...e-16]
            sage: RBF(3).log(2)
            [1.58496250072116 +/- ...e-15]
            sage: log(RBF(5), 2)
            [2.32192809488736 +/- ...e-15]

            sage: RBF(-1/3).log()
            nan
            sage: RBF(3).log(-1)
            nan
            sage: RBF(2).log(0)
            nan"""
    @overload
    def log1p(self) -> Any:
        """RealBall.log1p(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3161)

        Return ``log(1 + self)``, computed accurately when ``self`` is close to
        zero.

        EXAMPLES::

            sage: eps = RBF(1e-30)
            sage: (1 + eps).log()
            [+/- ...e-16]
            sage: eps.log1p()
            [1.00000000000000e-30 +/- ...e-46]"""
    @overload
    def log1p(self) -> Any:
        """RealBall.log1p(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3161)

        Return ``log(1 + self)``, computed accurately when ``self`` is close to
        zero.

        EXAMPLES::

            sage: eps = RBF(1e-30)
            sage: (1 + eps).log()
            [+/- ...e-16]
            sage: eps.log1p()
            [1.00000000000000e-30 +/- ...e-46]"""
    @overload
    def log_gamma(self) -> Any:
        """RealBall.log_gamma(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3792)

        Return the image of this ball by the logarithmic Gamma function.

        The complex branch structure is assumed, so if ``self <= 0``, the result
        is an indeterminate interval.

        EXAMPLES::

            sage: RBF(1/2).log_gamma()
            [0.572364942924700 +/- ...e-16]"""
    @overload
    def log_gamma(self) -> Any:
        """RealBall.log_gamma(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3792)

        Return the image of this ball by the logarithmic Gamma function.

        The complex branch structure is assumed, so if ``self <= 0``, the result
        is an indeterminate interval.

        EXAMPLES::

            sage: RBF(1/2).log_gamma()
            [0.572364942924700 +/- ...e-16]"""
    def log_integral(self, *args, **kwargs):
        """RealBall.li(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3648)

        Logarithmic integral.

        EXAMPLES::

            sage: RBF(3).li()  # abs tol 5e-15
            [2.16358859466719 +/- 4.72e-15]

        TESTS::

            sage: RBF(li(0))                                                            # needs sage.symbolic
            0
            sage: RBF(Li(0))  # abs tol 5e-15                                           # needs sage.symbolic
            [-1.04516378011749 +/- 4.23e-15]"""
    def log_integral_offset(self, *args, **kwargs):
        """RealBall.Li(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3672)

        Offset logarithmic integral.

        EXAMPLES::

            sage: RBF(3).Li()  # abs tol 5e-15
            [1.11842481454970 +/- 7.61e-15]"""
    @overload
    def lower(self, rnd=...) -> Any:
        """RealBall.lower(self, rnd=None)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 1945)

        Return the right endpoint of this ball, rounded downwards.

        INPUT:

        - ``rnd`` -- string; rounding mode for the parent of the result (does
          not affect its value!), see
          :meth:`sage.rings.real_mpfi.RealIntervalFieldElement.lower`

        OUTPUT: a real number

        EXAMPLES::

            sage: RBF(-1/3).lower()
            -0.333333333333334
            sage: RBF(-1/3).lower().parent()
            Real Field with 53 bits of precision and rounding RNDD

        .. SEEALSO:: :meth:`upper`, :meth:`endpoints`"""
    @overload
    def lower(self) -> Any:
        """RealBall.lower(self, rnd=None)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 1945)

        Return the right endpoint of this ball, rounded downwards.

        INPUT:

        - ``rnd`` -- string; rounding mode for the parent of the result (does
          not affect its value!), see
          :meth:`sage.rings.real_mpfi.RealIntervalFieldElement.lower`

        OUTPUT: a real number

        EXAMPLES::

            sage: RBF(-1/3).lower()
            -0.333333333333334
            sage: RBF(-1/3).lower().parent()
            Real Field with 53 bits of precision and rounding RNDD

        .. SEEALSO:: :meth:`upper`, :meth:`endpoints`"""
    @overload
    def lower(self) -> Any:
        """RealBall.lower(self, rnd=None)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 1945)

        Return the right endpoint of this ball, rounded downwards.

        INPUT:

        - ``rnd`` -- string; rounding mode for the parent of the result (does
          not affect its value!), see
          :meth:`sage.rings.real_mpfi.RealIntervalFieldElement.lower`

        OUTPUT: a real number

        EXAMPLES::

            sage: RBF(-1/3).lower()
            -0.333333333333334
            sage: RBF(-1/3).lower().parent()
            Real Field with 53 bits of precision and rounding RNDD

        .. SEEALSO:: :meth:`upper`, :meth:`endpoints`"""
    @overload
    def max(self, *others) -> Any:
        """RealBall.max(self, *others)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 2475)

        Return a ball containing the maximum of this ball and the
        remaining arguments.

        EXAMPLES::

            sage: RBF(-1, rad=.5).max(0)
            0

            sage: RBF(0, rad=2.).max(RBF(0, rad=1.)).endpoints()
            (-1.00000000465662, 2.00000000651926)

            sage: RBF(-infinity).max(-3, 1/3)
            [0.3333333333333333 +/- ...e-17]

            sage: RBF('nan').max(0)
            nan

        .. SEEALSO:: :meth:`min`

        TESTS::

            sage: RBF(0).max()
            0"""
    @overload
    def max(self) -> Any:
        """RealBall.max(self, *others)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 2475)

        Return a ball containing the maximum of this ball and the
        remaining arguments.

        EXAMPLES::

            sage: RBF(-1, rad=.5).max(0)
            0

            sage: RBF(0, rad=2.).max(RBF(0, rad=1.)).endpoints()
            (-1.00000000465662, 2.00000000651926)

            sage: RBF(-infinity).max(-3, 1/3)
            [0.3333333333333333 +/- ...e-17]

            sage: RBF('nan').max(0)
            nan

        .. SEEALSO:: :meth:`min`

        TESTS::

            sage: RBF(0).max()
            0"""
    @overload
    def mid(self) -> Any:
        """RealBall.mid(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 1718)

        Return the center of this ball.

        EXAMPLES::

            sage: RealBallField(16)(1/3).mid()
            0.3333
            sage: RealBallField(16)(1/3).mid().parent()
            Real Field with 16 bits of precision
            sage: RealBallField(16)(RBF(1/3)).mid().parent()
            Real Field with 53 bits of precision
            sage: RBF('inf').mid()
            +infinity

        ::

            sage: b = RBF(2)^(2^1000)
            sage: b.mid()
            +infinity

        .. SEEALSO:: :meth:`rad`, :meth:`squash`"""
    @overload
    def mid(self) -> Any:
        """RealBall.mid(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 1718)

        Return the center of this ball.

        EXAMPLES::

            sage: RealBallField(16)(1/3).mid()
            0.3333
            sage: RealBallField(16)(1/3).mid().parent()
            Real Field with 16 bits of precision
            sage: RealBallField(16)(RBF(1/3)).mid().parent()
            Real Field with 53 bits of precision
            sage: RBF('inf').mid()
            +infinity

        ::

            sage: b = RBF(2)^(2^1000)
            sage: b.mid()
            +infinity

        .. SEEALSO:: :meth:`rad`, :meth:`squash`"""
    @overload
    def mid(self) -> Any:
        """RealBall.mid(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 1718)

        Return the center of this ball.

        EXAMPLES::

            sage: RealBallField(16)(1/3).mid()
            0.3333
            sage: RealBallField(16)(1/3).mid().parent()
            Real Field with 16 bits of precision
            sage: RealBallField(16)(RBF(1/3)).mid().parent()
            Real Field with 53 bits of precision
            sage: RBF('inf').mid()
            +infinity

        ::

            sage: b = RBF(2)^(2^1000)
            sage: b.mid()
            +infinity

        .. SEEALSO:: :meth:`rad`, :meth:`squash`"""
    @overload
    def mid(self) -> Any:
        """RealBall.mid(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 1718)

        Return the center of this ball.

        EXAMPLES::

            sage: RealBallField(16)(1/3).mid()
            0.3333
            sage: RealBallField(16)(1/3).mid().parent()
            Real Field with 16 bits of precision
            sage: RealBallField(16)(RBF(1/3)).mid().parent()
            Real Field with 53 bits of precision
            sage: RBF('inf').mid()
            +infinity

        ::

            sage: b = RBF(2)^(2^1000)
            sage: b.mid()
            +infinity

        .. SEEALSO:: :meth:`rad`, :meth:`squash`"""
    @overload
    def mid(self) -> Any:
        """RealBall.mid(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 1718)

        Return the center of this ball.

        EXAMPLES::

            sage: RealBallField(16)(1/3).mid()
            0.3333
            sage: RealBallField(16)(1/3).mid().parent()
            Real Field with 16 bits of precision
            sage: RealBallField(16)(RBF(1/3)).mid().parent()
            Real Field with 53 bits of precision
            sage: RBF('inf').mid()
            +infinity

        ::

            sage: b = RBF(2)^(2^1000)
            sage: b.mid()
            +infinity

        .. SEEALSO:: :meth:`rad`, :meth:`squash`"""
    @overload
    def mid(self) -> Any:
        """RealBall.mid(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 1718)

        Return the center of this ball.

        EXAMPLES::

            sage: RealBallField(16)(1/3).mid()
            0.3333
            sage: RealBallField(16)(1/3).mid().parent()
            Real Field with 16 bits of precision
            sage: RealBallField(16)(RBF(1/3)).mid().parent()
            Real Field with 53 bits of precision
            sage: RBF('inf').mid()
            +infinity

        ::

            sage: b = RBF(2)^(2^1000)
            sage: b.mid()
            +infinity

        .. SEEALSO:: :meth:`rad`, :meth:`squash`"""
    @overload
    def min(self, *others) -> Any:
        """RealBall.min(self, *others)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 2438)

        Return a ball containing the minimum of this ball and the
        remaining arguments.

        EXAMPLES::

            sage: RBF(1, rad=.5).min(0)
            0

            sage: RBF(0, rad=2.).min(RBF(0, rad=1.)).endpoints()
            (-2.00000000651926, 1.00000000465662)

            sage: RBF(infinity).min(3, 1/3)
            [0.3333333333333333 +/- ...e-17]

            sage: RBF('nan').min(0)
            nan

        .. SEEALSO:: :meth:`max`

        TESTS::

            sage: RBF(0).min()
            0
            sage: RBF(infinity).min().rad()
            0.00000000"""
    @overload
    def min(self) -> Any:
        """RealBall.min(self, *others)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 2438)

        Return a ball containing the minimum of this ball and the
        remaining arguments.

        EXAMPLES::

            sage: RBF(1, rad=.5).min(0)
            0

            sage: RBF(0, rad=2.).min(RBF(0, rad=1.)).endpoints()
            (-2.00000000651926, 1.00000000465662)

            sage: RBF(infinity).min(3, 1/3)
            [0.3333333333333333 +/- ...e-17]

            sage: RBF('nan').min(0)
            nan

        .. SEEALSO:: :meth:`max`

        TESTS::

            sage: RBF(0).min()
            0
            sage: RBF(infinity).min().rad()
            0.00000000"""
    @overload
    def min(self) -> Any:
        """RealBall.min(self, *others)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 2438)

        Return a ball containing the minimum of this ball and the
        remaining arguments.

        EXAMPLES::

            sage: RBF(1, rad=.5).min(0)
            0

            sage: RBF(0, rad=2.).min(RBF(0, rad=1.)).endpoints()
            (-2.00000000651926, 1.00000000465662)

            sage: RBF(infinity).min(3, 1/3)
            [0.3333333333333333 +/- ...e-17]

            sage: RBF('nan').min(0)
            nan

        .. SEEALSO:: :meth:`max`

        TESTS::

            sage: RBF(0).min()
            0
            sage: RBF(infinity).min().rad()
            0.00000000"""
    @overload
    def nbits(self) -> Any:
        """RealBall.nbits(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 2031)

        Return the minimum precision sufficient to represent this ball exactly.

        In other words, return the number of bits needed to represent the
        absolute value of the mantissa of the midpoint of this ball. The result
        is 0 if the midpoint is a special value.

        EXAMPLES::

            sage: RBF(1/3).nbits()
            53
            sage: RBF(1023, .1).nbits()
            10
            sage: RBF(1024, .1).nbits()
            1
            sage: RBF(0).nbits()
            0
            sage: RBF(infinity).nbits()
            0"""
    @overload
    def nbits(self) -> Any:
        """RealBall.nbits(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 2031)

        Return the minimum precision sufficient to represent this ball exactly.

        In other words, return the number of bits needed to represent the
        absolute value of the mantissa of the midpoint of this ball. The result
        is 0 if the midpoint is a special value.

        EXAMPLES::

            sage: RBF(1/3).nbits()
            53
            sage: RBF(1023, .1).nbits()
            10
            sage: RBF(1024, .1).nbits()
            1
            sage: RBF(0).nbits()
            0
            sage: RBF(infinity).nbits()
            0"""
    @overload
    def nbits(self) -> Any:
        """RealBall.nbits(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 2031)

        Return the minimum precision sufficient to represent this ball exactly.

        In other words, return the number of bits needed to represent the
        absolute value of the mantissa of the midpoint of this ball. The result
        is 0 if the midpoint is a special value.

        EXAMPLES::

            sage: RBF(1/3).nbits()
            53
            sage: RBF(1023, .1).nbits()
            10
            sage: RBF(1024, .1).nbits()
            1
            sage: RBF(0).nbits()
            0
            sage: RBF(infinity).nbits()
            0"""
    @overload
    def nbits(self) -> Any:
        """RealBall.nbits(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 2031)

        Return the minimum precision sufficient to represent this ball exactly.

        In other words, return the number of bits needed to represent the
        absolute value of the mantissa of the midpoint of this ball. The result
        is 0 if the midpoint is a special value.

        EXAMPLES::

            sage: RBF(1/3).nbits()
            53
            sage: RBF(1023, .1).nbits()
            10
            sage: RBF(1024, .1).nbits()
            1
            sage: RBF(0).nbits()
            0
            sage: RBF(infinity).nbits()
            0"""
    @overload
    def nbits(self) -> Any:
        """RealBall.nbits(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 2031)

        Return the minimum precision sufficient to represent this ball exactly.

        In other words, return the number of bits needed to represent the
        absolute value of the mantissa of the midpoint of this ball. The result
        is 0 if the midpoint is a special value.

        EXAMPLES::

            sage: RBF(1/3).nbits()
            53
            sage: RBF(1023, .1).nbits()
            10
            sage: RBF(1024, .1).nbits()
            1
            sage: RBF(0).nbits()
            0
            sage: RBF(infinity).nbits()
            0"""
    @overload
    def nbits(self) -> Any:
        """RealBall.nbits(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 2031)

        Return the minimum precision sufficient to represent this ball exactly.

        In other words, return the number of bits needed to represent the
        absolute value of the mantissa of the midpoint of this ball. The result
        is 0 if the midpoint is a special value.

        EXAMPLES::

            sage: RBF(1/3).nbits()
            53
            sage: RBF(1023, .1).nbits()
            10
            sage: RBF(1024, .1).nbits()
            1
            sage: RBF(0).nbits()
            0
            sage: RBF(infinity).nbits()
            0"""
    def overlaps(self, RealBallother) -> Any:
        """RealBall.overlaps(self, RealBall other)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 2547)

        Return ``True`` iff ``self`` and ``other`` have some point in common.

        If either ``self`` or ``other`` contains NaN, this method always
        returns nonzero (as a NaN could be anything, it could in particular
        contain any number that is included in the other operand).

        EXAMPLES::

            sage: RBF(pi).overlaps(RBF(pi) + 2**(-100))                                 # needs sage.symbolic
            True
            sage: RBF(pi).overlaps(RBF(3))                                              # needs sage.symbolic
            False"""
    def polylog(self, s) -> Any:
        """RealBall.polylog(self, s)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3934)

        Return the polylogarithm `\\operatorname{Li}_s(\\mathrm{self})`.

        EXAMPLES::

            sage: polylog(0, -1)                                                        # needs sage.symbolic
            -1/2
            sage: RBF(-1).polylog(0)
            [-0.50000000000000 +/- ...e-16]
            sage: polylog(1, 1/2)                                                       # needs sage.symbolic
            -log(1/2)
            sage: RBF(1/2).polylog(1)
            [0.69314718055995 +/- ...e-15]
            sage: RBF(1/3).polylog(1/2)
            [0.44210883528067 +/- 6.7...e-15]
            sage: RBF(1/3).polylog(RLF(pi))                                             # needs sage.symbolic
            [0.34728895057225 +/- ...e-15]

        TESTS::

            sage: RBF(1/3).polylog(2r)
            [0.366213229977063 +/- ...e-16]"""
    @overload
    def psi(self) -> RealBall:
        """RealBall.psi(self) -> RealBall

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3850)

        Compute the digamma function with argument ``self``.

        EXAMPLES::

            sage: RBF(1).psi() # abs tol 1e-15
            [-0.5772156649015329 +/- 4.84e-17]"""
    @overload
    def psi(self) -> Any:
        """RealBall.psi(self) -> RealBall

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3850)

        Compute the digamma function with argument ``self``.

        EXAMPLES::

            sage: RBF(1).psi() # abs tol 1e-15
            [-0.5772156649015329 +/- 4.84e-17]"""
    @overload
    def rad(self) -> Any:
        """RealBall.rad(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 1749)

        Return the radius of this ball.

        EXAMPLES::

            sage: RBF(1/3).rad()
            5.5511151e-17
            sage: RBF(1/3).rad().parent()
            Real Field with 30 bits of precision

        .. SEEALSO:: :meth:`mid`, :meth:`rad_as_ball`, :meth:`diameter`

        TESTS::

            sage: (RBF(1, rad=.1) << (2^64)).rad()
            Traceback (most recent call last):
            ...
            RuntimeError: unable to convert the radius to MPFR (exponent out of range?)"""
    @overload
    def rad(self) -> Any:
        """RealBall.rad(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 1749)

        Return the radius of this ball.

        EXAMPLES::

            sage: RBF(1/3).rad()
            5.5511151e-17
            sage: RBF(1/3).rad().parent()
            Real Field with 30 bits of precision

        .. SEEALSO:: :meth:`mid`, :meth:`rad_as_ball`, :meth:`diameter`

        TESTS::

            sage: (RBF(1, rad=.1) << (2^64)).rad()
            Traceback (most recent call last):
            ...
            RuntimeError: unable to convert the radius to MPFR (exponent out of range?)"""
    @overload
    def rad(self) -> Any:
        """RealBall.rad(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 1749)

        Return the radius of this ball.

        EXAMPLES::

            sage: RBF(1/3).rad()
            5.5511151e-17
            sage: RBF(1/3).rad().parent()
            Real Field with 30 bits of precision

        .. SEEALSO:: :meth:`mid`, :meth:`rad_as_ball`, :meth:`diameter`

        TESTS::

            sage: (RBF(1, rad=.1) << (2^64)).rad()
            Traceback (most recent call last):
            ...
            RuntimeError: unable to convert the radius to MPFR (exponent out of range?)"""
    @overload
    def rad(self) -> Any:
        """RealBall.rad(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 1749)

        Return the radius of this ball.

        EXAMPLES::

            sage: RBF(1/3).rad()
            5.5511151e-17
            sage: RBF(1/3).rad().parent()
            Real Field with 30 bits of precision

        .. SEEALSO:: :meth:`mid`, :meth:`rad_as_ball`, :meth:`diameter`

        TESTS::

            sage: (RBF(1, rad=.1) << (2^64)).rad()
            Traceback (most recent call last):
            ...
            RuntimeError: unable to convert the radius to MPFR (exponent out of range?)"""
    @overload
    def rad_as_ball(self) -> Any:
        """RealBall.rad_as_ball(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 1821)

        Return an exact ball with center equal to the radius of this ball.

        EXAMPLES::

            sage: rad = RBF(1/3).rad_as_ball()
            sage: rad
            [5.55111512e-17 +/- ...e-26]
            sage: rad.is_exact()
            True
            sage: rad.parent()
            Real ball field with 30 bits of precision

        .. SEEALSO:: :meth:`squash`, :meth:`rad`"""
    @overload
    def rad_as_ball(self) -> Any:
        """RealBall.rad_as_ball(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 1821)

        Return an exact ball with center equal to the radius of this ball.

        EXAMPLES::

            sage: rad = RBF(1/3).rad_as_ball()
            sage: rad
            [5.55111512e-17 +/- ...e-26]
            sage: rad.is_exact()
            True
            sage: rad.parent()
            Real ball field with 30 bits of precision

        .. SEEALSO:: :meth:`squash`, :meth:`rad`"""
    @overload
    def real(self) -> Any:
        """RealBall.real(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 2007)

        Return the real part of this ball.

        EXAMPLES::

            sage: RBF(1/3).real()
            [0.3333333333333333 +/- 7.04e-17]"""
    @overload
    def real(self) -> Any:
        """RealBall.real(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 2007)

        Return the real part of this ball.

        EXAMPLES::

            sage: RBF(1/3).real()
            [0.3333333333333333 +/- 7.04e-17]"""
    @overload
    def rgamma(self) -> Any:
        """RealBall.rgamma(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3810)

        Return the image of this ball by the function 1/Γ, avoiding division by
        zero at the poles of the gamma function.

        EXAMPLES::

            sage: RBF(-1).rgamma()
            0
            sage: RBF(3).rgamma()
            0.5000000000000000"""
    @overload
    def rgamma(self) -> Any:
        """RealBall.rgamma(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3810)

        Return the image of this ball by the function 1/Γ, avoiding division by
        zero at the poles of the gamma function.

        EXAMPLES::

            sage: RBF(-1).rgamma()
            0
            sage: RBF(3).rgamma()
            0.5000000000000000"""
    @overload
    def rgamma(self) -> Any:
        """RealBall.rgamma(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3810)

        Return the image of this ball by the function 1/Γ, avoiding division by
        zero at the poles of the gamma function.

        EXAMPLES::

            sage: RBF(-1).rgamma()
            0
            sage: RBF(3).rgamma()
            0.5000000000000000"""
    def rising_factorial(self, n) -> Any:
        """RealBall.rising_factorial(self, n)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3828)

        Return the ``n``-th rising factorial of this ball.

        The `n`-th rising factorial of `x` is equal to `x (x+1) \\cdots (x+n-1)`.

        For real `n`, it is a quotient of gamma functions.

        EXAMPLES::

            sage: RBF(1).rising_factorial(5)
            120.0000000000000
            sage: RBF(1/2).rising_factorial(1/3) # abs tol 1e-14
            [0.636849884317974 +/- 8.98e-16]"""
    def round(self) -> Any:
        """RealBall.round(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 2054)

        Return a copy of this ball with center rounded to the precision of the
        parent.

        EXAMPLES:

        It is possible to create balls whose midpoint is more precise than
        their parent's nominal precision (see :mod:`~sage.rings.real_arb` for
        more information)::

            sage: b = RBF(pi.n(100))                                                    # needs sage.symbolic
            sage: b.mid()                                                               # needs sage.symbolic
            3.141592653589793238462643383

        The ``round()`` method rounds such a ball to its parent's precision::

            sage: b.round().mid()                                                       # needs sage.symbolic
            3.14159265358979

        .. SEEALSO:: :meth:`trim`"""
    @overload
    def rsqrt(self) -> Any:
        """RealBall.rsqrt(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 2956)

        Return the reciprocal square root of ``self``.

        At high precision, this is faster than computing a square root.

        EXAMPLES::

            sage: RBF(2).rsqrt()
            [0.707106781186547 +/- ...e-16]
            sage: RBF(0).rsqrt()
            nan"""
    @overload
    def rsqrt(self) -> Any:
        """RealBall.rsqrt(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 2956)

        Return the reciprocal square root of ``self``.

        At high precision, this is faster than computing a square root.

        EXAMPLES::

            sage: RBF(2).rsqrt()
            [0.707106781186547 +/- ...e-16]
            sage: RBF(0).rsqrt()
            nan"""
    @overload
    def rsqrt(self) -> Any:
        """RealBall.rsqrt(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 2956)

        Return the reciprocal square root of ``self``.

        At high precision, this is faster than computing a square root.

        EXAMPLES::

            sage: RBF(2).rsqrt()
            [0.707106781186547 +/- ...e-16]
            sage: RBF(0).rsqrt()
            nan"""
    @overload
    def sec(self) -> Any:
        """RealBall.sec(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3282)

        Return the secant of this ball.

        EXAMPLES::

            sage: RBF(1).sec()
            [1.850815717680925 +/- ...e-16]"""
    @overload
    def sec(self) -> Any:
        """RealBall.sec(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3282)

        Return the secant of this ball.

        EXAMPLES::

            sage: RBF(1).sec()
            [1.850815717680925 +/- ...e-16]"""
    @overload
    def sech(self) -> Any:
        """RealBall.sech(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3423)

        Return the hyperbolic secant of this ball.

        EXAMPLES::

            sage: RBF(1).sech()
            [0.648054273663885 +/- ...e-16]"""
    @overload
    def sech(self) -> Any:
        """RealBall.sech(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3423)

        Return the hyperbolic secant of this ball.

        EXAMPLES::

            sage: RBF(1).sech()
            [0.648054273663885 +/- ...e-16]"""
    @overload
    def sin(self) -> Any:
        """RealBall.sin(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3214)

        Return the sine of this ball.

        EXAMPLES::

            sage: RBF(pi).sin()                                                         # needs sage.symbolic
            [+/- ...e-16]

        .. SEEALSO:: :meth:`~sage.rings.real_arb.RealBallField.sinpi`"""
    @overload
    def sin(self) -> Any:
        """RealBall.sin(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3214)

        Return the sine of this ball.

        EXAMPLES::

            sage: RBF(pi).sin()                                                         # needs sage.symbolic
            [+/- ...e-16]

        .. SEEALSO:: :meth:`~sage.rings.real_arb.RealBallField.sinpi`"""
    def sin_integral(self, *args, **kwargs):
        """RealBall.Si(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3560)

        Sine integral.

        EXAMPLES::

            sage: RBF(1).Si() # abs tol 1e-15
            [0.946083070367183 +/- 9.22e-16]

        TESTS::

            sage: RBF(Si(1))  # abs tol 1e-15                                           # needs sage.symbolic
            [0.946083070367183 +/- 9.22e-16]"""
    @overload
    def sinh(self) -> Any:
        """RealBall.sinh(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3361)

        Return the hyperbolic sine of this ball.

        EXAMPLES::

            sage: RBF(1).sinh()
            [1.175201193643801 +/- ...e-16]"""
    @overload
    def sinh(self) -> Any:
        """RealBall.sinh(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3361)

        Return the hyperbolic sine of this ball.

        EXAMPLES::

            sage: RBF(1).sinh()
            [1.175201193643801 +/- ...e-16]"""
    def sinh_integral(self, *args, **kwargs):
        """RealBall.Shi(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3604)

        Hyperbolic sine integral.

        EXAMPLES::

            sage: RBF(1).Shi() # abs tol 5e-15
            [1.05725087537573 +/- 2.77e-15]

        TESTS::

            sage: RBF(Shi(1))  # abs tol 5e-15                                          # needs sage.symbolic
            [1.05725087537573 +/- 2.77e-15]"""
    @overload
    def sqrt(self) -> Any:
        """RealBall.sqrt(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 2917)

        Return the square root of this ball.

        EXAMPLES::

            sage: RBF(2).sqrt()
            [1.414213562373095 +/- ...e-16]
            sage: RBF(-1/3).sqrt()
            nan"""
    @overload
    def sqrt(self) -> Any:
        """RealBall.sqrt(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 2917)

        Return the square root of this ball.

        EXAMPLES::

            sage: RBF(2).sqrt()
            [1.414213562373095 +/- ...e-16]
            sage: RBF(-1/3).sqrt()
            nan"""
    @overload
    def sqrt(self) -> Any:
        """RealBall.sqrt(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 2917)

        Return the square root of this ball.

        EXAMPLES::

            sage: RBF(2).sqrt()
            [1.414213562373095 +/- ...e-16]
            sage: RBF(-1/3).sqrt()
            nan"""
    def sqrt1pm1(self) -> Any:
        """RealBall.sqrt1pm1(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 2975)

        Return `\\sqrt{1+\\mathrm{self}}-1`, computed accurately when ``self`` is
        close to zero.

        EXAMPLES::

            sage: eps = RBF(10^(-20))
            sage: (1 + eps).sqrt() - 1
            [+/- ...e-16]
            sage: eps.sqrt1pm1()
            [5.00000000000000e-21 +/- ...e-36]"""
    @overload
    def sqrtpos(self) -> Any:
        """RealBall.sqrtpos(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 2934)

        Return the square root of this ball, assuming that it represents a
        nonnegative number.

        Any negative numbers in the input interval are discarded.

        EXAMPLES::

            sage: RBF(2).sqrtpos()
            [1.414213562373095 +/- ...e-16]
            sage: RBF(-1/3).sqrtpos()
            0
            sage: RBF(0, rad=2.r).sqrtpos()
            [+/- 1.42]"""
    @overload
    def sqrtpos(self) -> Any:
        """RealBall.sqrtpos(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 2934)

        Return the square root of this ball, assuming that it represents a
        nonnegative number.

        Any negative numbers in the input interval are discarded.

        EXAMPLES::

            sage: RBF(2).sqrtpos()
            [1.414213562373095 +/- ...e-16]
            sage: RBF(-1/3).sqrtpos()
            0
            sage: RBF(0, rad=2.r).sqrtpos()
            [+/- 1.42]"""
    @overload
    def sqrtpos(self) -> Any:
        """RealBall.sqrtpos(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 2934)

        Return the square root of this ball, assuming that it represents a
        nonnegative number.

        Any negative numbers in the input interval are discarded.

        EXAMPLES::

            sage: RBF(2).sqrtpos()
            [1.414213562373095 +/- ...e-16]
            sage: RBF(-1/3).sqrtpos()
            0
            sage: RBF(0, rad=2.r).sqrtpos()
            [+/- 1.42]"""
    @overload
    def sqrtpos(self) -> Any:
        """RealBall.sqrtpos(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 2934)

        Return the square root of this ball, assuming that it represents a
        nonnegative number.

        Any negative numbers in the input interval are discarded.

        EXAMPLES::

            sage: RBF(2).sqrtpos()
            [1.414213562373095 +/- ...e-16]
            sage: RBF(-1/3).sqrtpos()
            0
            sage: RBF(0, rad=2.r).sqrtpos()
            [+/- 1.42]"""
    @overload
    def squash(self) -> Any:
        """RealBall.squash(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 1800)

        Return an exact ball with the same center as this ball.

        EXAMPLES::

            sage: mid = RealBallField(16)(1/3).squash()
            sage: mid
            [0.3333 +/- ...e-5]
            sage: mid.is_exact()
            True
            sage: mid.parent()
            Real ball field with 16 bits of precision

        .. SEEALSO:: :meth:`mid`, :meth:`rad_as_ball`"""
    @overload
    def squash(self) -> Any:
        """RealBall.squash(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 1800)

        Return an exact ball with the same center as this ball.

        EXAMPLES::

            sage: mid = RealBallField(16)(1/3).squash()
            sage: mid
            [0.3333 +/- ...e-5]
            sage: mid.is_exact()
            True
            sage: mid.parent()
            Real ball field with 16 bits of precision

        .. SEEALSO:: :meth:`mid`, :meth:`rad_as_ball`"""
    @overload
    def tan(self) -> Any:
        """RealBall.tan(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3248)

        Return the tangent of this ball.

        EXAMPLES::

            sage: RBF(1).tan()
            [1.557407724654902 +/- ...e-16]
            sage: RBF(pi/2).tan()                                                       # needs sage.symbolic
            nan"""
    @overload
    def tan(self) -> Any:
        """RealBall.tan(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3248)

        Return the tangent of this ball.

        EXAMPLES::

            sage: RBF(1).tan()
            [1.557407724654902 +/- ...e-16]
            sage: RBF(pi/2).tan()                                                       # needs sage.symbolic
            nan"""
    @overload
    def tan(self) -> Any:
        """RealBall.tan(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3248)

        Return the tangent of this ball.

        EXAMPLES::

            sage: RBF(1).tan()
            [1.557407724654902 +/- ...e-16]
            sage: RBF(pi/2).tan()                                                       # needs sage.symbolic
            nan"""
    @overload
    def tanh(self) -> Any:
        """RealBall.tanh(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3391)

        Return the hyperbolic tangent of this ball.

        EXAMPLES::

            sage: RBF(1).tanh()
            [0.761594155955765 +/- ...e-16]"""
    @overload
    def tanh(self) -> Any:
        """RealBall.tanh(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3391)

        Return the hyperbolic tangent of this ball.

        EXAMPLES::

            sage: RBF(1).tanh()
            [0.761594155955765 +/- ...e-16]"""
    @overload
    def trim(self) -> Any:
        """RealBall.trim(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 2104)

        Return a trimmed copy of this ball.

        Round ``self`` to a number of bits equal to the :meth:`accuracy` of
        ``self`` (as indicated by its radius), plus a few guard bits. The
        resulting ball is guaranteed to contain ``self``, but is more economical
        if ``self`` has less than full accuracy.

        EXAMPLES::

            sage: b = RBF(0.11111111111111, rad=.001)
            sage: b.mid()
            0.111111111111110
            sage: b.trim().mid()
            0.111111104488373

        .. SEEALSO:: :meth:`round`"""
    @overload
    def trim(self) -> Any:
        """RealBall.trim(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 2104)

        Return a trimmed copy of this ball.

        Round ``self`` to a number of bits equal to the :meth:`accuracy` of
        ``self`` (as indicated by its radius), plus a few guard bits. The
        resulting ball is guaranteed to contain ``self``, but is more economical
        if ``self`` has less than full accuracy.

        EXAMPLES::

            sage: b = RBF(0.11111111111111, rad=.001)
            sage: b.mid()
            0.111111111111110
            sage: b.trim().mid()
            0.111111104488373

        .. SEEALSO:: :meth:`round`"""
    def union(self, other) -> Any:
        """RealBall.union(self, other)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 1991)

        Return a ball containing the convex hull of ``self`` and ``other``.

        EXAMPLES::

            sage: RBF(0).union(1).endpoints()
            (-9.31322574615479e-10, 1.00000000093133)"""
    @overload
    def upper(self, rnd=...) -> Any:
        """RealBall.upper(self, rnd=None)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 1919)

        Return the right endpoint of this ball, rounded upwards.

        INPUT:

        - ``rnd`` -- string; rounding mode for the parent of the result (does
          not affect its value!), see
          :meth:`sage.rings.real_mpfi.RealIntervalFieldElement.upper`

        OUTPUT: a real number

        EXAMPLES::

            sage: RBF(-1/3).upper()
            -0.333333333333333
            sage: RBF(-1/3).upper().parent()
            Real Field with 53 bits of precision and rounding RNDU

        .. SEEALSO::

           :meth:`lower`, :meth:`endpoints`"""
    @overload
    def upper(self) -> Any:
        """RealBall.upper(self, rnd=None)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 1919)

        Return the right endpoint of this ball, rounded upwards.

        INPUT:

        - ``rnd`` -- string; rounding mode for the parent of the result (does
          not affect its value!), see
          :meth:`sage.rings.real_mpfi.RealIntervalFieldElement.upper`

        OUTPUT: a real number

        EXAMPLES::

            sage: RBF(-1/3).upper()
            -0.333333333333333
            sage: RBF(-1/3).upper().parent()
            Real Field with 53 bits of precision and rounding RNDU

        .. SEEALSO::

           :meth:`lower`, :meth:`endpoints`"""
    @overload
    def upper(self) -> Any:
        """RealBall.upper(self, rnd=None)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 1919)

        Return the right endpoint of this ball, rounded upwards.

        INPUT:

        - ``rnd`` -- string; rounding mode for the parent of the result (does
          not affect its value!), see
          :meth:`sage.rings.real_mpfi.RealIntervalFieldElement.upper`

        OUTPUT: a real number

        EXAMPLES::

            sage: RBF(-1/3).upper()
            -0.333333333333333
            sage: RBF(-1/3).upper().parent()
            Real Field with 53 bits of precision and rounding RNDU

        .. SEEALSO::

           :meth:`lower`, :meth:`endpoints`"""
    @overload
    def zeta(self, a=...) -> Any:
        """RealBall.zeta(self, a=None)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3866)

        Return the image of this ball by the Hurwitz zeta function.

        For ``a = 1`` (or ``a = None``), this computes the Riemann zeta function.

        Otherwise, it computes the Hurwitz zeta function.

        Use :meth:`RealBallField.zeta` to compute the Riemann zeta function of
        a small integer without first converting it to a real ball.

        EXAMPLES::

            sage: RBF(-1).zeta()
            [-0.0833333333333333 +/- ...e-17]
            sage: RBF(-1).zeta(1)
            [-0.0833333333333333 +/- ...e-17]
            sage: RBF(-1).zeta(2)
            [-1.083333333333333 +/- ...e-16]"""
    @overload
    def zeta(self) -> Any:
        """RealBall.zeta(self, a=None)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3866)

        Return the image of this ball by the Hurwitz zeta function.

        For ``a = 1`` (or ``a = None``), this computes the Riemann zeta function.

        Otherwise, it computes the Hurwitz zeta function.

        Use :meth:`RealBallField.zeta` to compute the Riemann zeta function of
        a small integer without first converting it to a real ball.

        EXAMPLES::

            sage: RBF(-1).zeta()
            [-0.0833333333333333 +/- ...e-17]
            sage: RBF(-1).zeta(1)
            [-0.0833333333333333 +/- ...e-17]
            sage: RBF(-1).zeta(2)
            [-1.083333333333333 +/- ...e-16]"""
    def zetaderiv(self, k) -> Any:
        """RealBall.zetaderiv(self, k)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3899)

        Return the image of this ball by the `k`-th derivative of the Riemann
        zeta function.

        For a more flexible interface, see the low-level method
        ``_zeta_series`` of polynomials with complex ball coefficients.

        EXAMPLES::

            sage: RBF(1/2).zetaderiv(1)
            [-3.92264613920915...]
            sage: RBF(2).zetaderiv(3)
            [-6.0001458028430...]"""
    def __abs__(self) -> Any:
        """RealBall.__abs__(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 1842)

        Return the absolute value of this ball.

        EXAMPLES::

            sage: RBF(-1/3).abs() # indirect doctest
            [0.3333333333333333 +/- ...e-17]
            sage: abs(RBF(-1))
            1.000000000000000"""
    def __bool__(self) -> bool:
        """True if self else False"""
    def __complex__(self) -> Any:
        """RealBall.__complex__(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 1705)

        Convert ``self`` to a ``complex``.

        EXAMPLES::

            sage: complex(RBF(1))
            (1+0j)"""
    def __contains__(self, other) -> Any:
        """RealBall.__contains__(self, other)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 2629)

        Return ``True`` if ``other`` can be verified to be contained in ``self``.

        The test is done using interval arithmetic with a precision determined
        by the parent of ``self`` and may return false negatives.

        EXAMPLES::

            sage: sqrt(2) in RBF(sqrt(2))                                               # needs sage.symbolic
            True

        A false negative::

            sage: sqrt(2) in RBF(RealBallField(100)(sqrt(2)))                           # needs sage.symbolic
            False

        .. SEEALSO:: :meth:`contains_exact`"""
    def __float__(self) -> Any:
        """RealBall.__float__(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 1694)

        Convert ``self`` to a ``float``.

        EXAMPLES::

            sage: float(RBF(1))
            1.0"""
    def __hash__(self) -> Any:
        """RealBall.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 1492)

        TESTS::

            sage: hash(RealBallField(10)(1)) == hash(RealBallField(20)(1))
            True
            sage: hash(RBF(1/3)) == hash(RBF(1/3, rad=.1))
            False
            sage: vals = [0, 1, 3/4, 5/8, 7/8, infinity, 'nan', 2^1000 - 1]
            sage: len({hash(RBF(v)) for v in vals}) == len(vals)
            True"""
    def __invert__(self) -> Any:
        """RealBall.__invert__(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 2764)

        Return the inverse of this ball.

        The result is guaranteed to contain the inverse of any point of the
        input ball.

        EXAMPLES::

            sage: ~RBF(5)
            [0.2000000000000000 +/- ...e-17]
            sage: ~RBF(0)
            nan
            sage: RBF(RIF(-0.1,0.1))
            [+/- 0.101]"""
    def __lshift__(self, val, shift) -> Any:
        '''RealBall.__lshift__(val, shift)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3026)

        If ``val`` is a ``RealBall`` and ``shift`` is an integer, return the
        ball obtained by shifting the center and radius of ``val`` to the left
        by ``shift`` bits.

        INPUT:

        - ``shift`` -- integer; may be negative

        EXAMPLES::

            sage: RBF(1/3) << 2 # indirect doctest
            [1.333333333333333 +/- ...e-16]
            sage: RBF(1) << -1
            0.5000000000000000

        TESTS::

            sage: RBF(1) << (2^100)
            [2.285367694229514e+381600854690147056244358827360 +/- ...e+381600854690147056244358827344]
            sage: RBF(1) << (-2^100)
            [4.375663498372584e-381600854690147056244358827361 +/- ...e-381600854690147056244358827378]

            sage: "a" << RBF(1/3)
            Traceback (most recent call last):
            ...
            TypeError: unsupported operand type(s) for <<: \'str\' and \'RealBall\'
            sage: RBF(1) << RBF(1/3)
            Traceback (most recent call last):
            ...
            TypeError: shift should be an integer'''
    def __neg__(self) -> Any:
        """RealBall.__neg__(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 2751)

        Return the opposite of this ball.

        EXAMPLES::

            sage: -RBF(1/3)
            [-0.3333333333333333 +/- ...e-17]"""
    def __pow__(self, base, expo, _) -> Any:
        """RealBall.__pow__(base, expo, _)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 2863)

        EXAMPLES::

            sage: # needs sage.symbolic
            sage: RBF(e)^17
            [24154952.7535753 +/- ...e-8]
            sage: RBF(e)^(-1)
            [0.367879441171442 +/- ...e-16]
            sage: RBF(e)^(1/2)
            [1.648721270700128 +/- ...e-16]
            sage: RBF(e)^RBF(pi)
            [23.1406926327793 +/- ...e-14]

        ::

            sage: RBF(-1)^(1/3)
            nan
            sage: RBF(0)^(-1)
            nan
            sage: RBF(-e)**RBF(pi)                                                      # needs sage.symbolic
            nan

        TESTS::

            sage: RBF(e)**(2r)                                                          # needs sage.symbolic
            [7.38905609893065 +/- ...e-15]
            sage: RBF(e)**(-1r)                                                         # needs sage.symbolic
            [0.367879441171442 +/- ...e-16]"""
    def __reduce__(self) -> Any:
        """RealBall.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 1539)

        Serialize a RealBall.

        TESTS::

            sage: [loads(dumps(b)).identical(b)
            ....:  for b in [RealBallField(60).pi(), RBF(infinity)]]
            [True, True]
            sage: b = RBF(NaN); loads(dumps(b)).identical(b)                            # needs sage.symbolic
            True"""
    def __rlshift__(self, other):
        """Return value<<self."""
    def __rpow__(self, other):
        """Return pow(value, self, mod)."""
    def __rrshift__(self, other):
        """Return value>>self."""
    def __rshift__(self, val, shift) -> Any:
        '''RealBall.__rshift__(val, shift)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3079)

        If ``val`` is a ``RealBall`` and ``shift`` is an integer, return the
        ball obtained by shifting the center and radius of ``val`` to the right
        by ``shift`` bits.

        INPUT:

        - ``shift`` -- integer; may be negative

        EXAMPLES::

            sage: RBF(4) >> 2
            1.000000000000000
            sage: RBF(1/3) >> -2
            [1.333333333333333 +/- ...e-16]

        TESTS::

            sage: "a" >> RBF(1/3)
            Traceback (most recent call last):
            ...
            TypeError: unsupported operand type(s) for >>: \'str\' and \'RealBall\''''

class RealBallField(sage.structure.unique_representation.UniqueRepresentation, sage.rings.abc.RealBallField):
    """File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 318)

        An approximation of the field of real numbers using mid-rad intervals, also
        known as balls.

        INPUT:

        - ``precision`` -- integer `\\ge 2`

        EXAMPLES::

            sage: RBF = RealBallField() # indirect doctest
            sage: RBF(1)
            1.000000000000000

        ::

            sage: (1/2*RBF(1)) + AA(sqrt(2)) - 1 + polygen(QQ, 'x')                         # needs sage.symbolic
            x + [0.914213562373095 +/- ...e-16]

        TESTS::

            sage: RBF.bracket(RBF(1/2), RBF(1/3))
            [+/- ...e-17]
            sage: RBF.cardinality()
            +Infinity
            sage: RBF.cartesian_product(QQ).an_element()**2
            ([1.440000000000000 +/- ...e-16], 1/4)
            sage: RBF.coerce_embedding() is None
            True
            sage: RBF['x'].gens_dict_recursive()
            {'x': x}
            sage: RBF.is_finite()
            False
            sage: RBF.is_zero()
            False
            sage: RBF.one()
            1.000000000000000
            sage: RBF.zero()
            0

            sage: NF.<sqrt2> = QuadraticField(2, embedding=AA(2).sqrt())                    # needs sage.rings.number_field
            sage: a = (sqrt2 - 1)^1000                                                      # needs sage.rings.number_field
            sage: RBF(a)                                                                    # needs sage.rings.number_field
            [1.676156872756536e-383 +/- ...e-399]

            sage: RealBallField().is_finite()
            False

            sage: loads(dumps(RealBallField(60))) is RealBallField(60)
            True

        .. SEEALSO::

            - :mod:`sage.rings.real_arb`
            - :mod:`sage.rings.real_mpfr`
            - :mod:`sage.rings.real_mpfi` (real intervals represented by their
              endpoints)
            - :mod:`sage.rings.complex_arb`
    """

    class Element(sage.structure.element.RingElement):
        """RealBall(parent, mid=None, rad=None)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 1190)

        Hold one ``arb_t``.

        EXAMPLES::

            sage: a = RealBallField()(RIF(1))                     # indirect doctest
            sage: b = a.psi()
            sage: b # abs tol 1e-15
            [-0.5772156649015329 +/- 4.84e-17]
            sage: RIF(b)
            -0.577215664901533?"""
        __pyx_vtable__: ClassVar[PyCapsule] = ...
        def __init__(self, *args, **kwargs) -> None:
            '''File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 1226)

                    Initialize the :class:`RealBall`.

                    INPUT:

                    - ``parent`` -- a :class:`RealBallField`

                    - ``mid`` -- (optional) ball midpoint, see examples below. If omitted,
                      initialize the ball to zero, ignoring the ``rad`` argument.

                    - ``rad`` -- (optional) a :class:`RealNumber` or a Python float, ball
                      radius. If the midpoint is not exactly representable in
                      floating-point, the radius is adjusted to account for the roundoff
                      error.

                    EXAMPLES::

                        sage: RBF = RealBallField()
                        sage: RBF()
                        0

                    One can create exact real balls using elements of various exact parents,
                    or using floating-point numbers::

                        sage: RBF(3)
                        3.000000000000000
                        sage: RBF(3r)
                        3.000000000000000
                        sage: RBF(1/3)
                        [0.3333333333333333 +/- ...e-17]
                        sage: RBF(3.14)
                        [3.140000000000000 +/- ...e-16]

                    ::

                        sage: RBF(3, 0.125)
                        [3e+0 +/- 0.126]
                        sage: RBF(pi, 0.125r)                                                       # needs sage.symbolic
                        [3e+0 +/- 0.267]
                        sage: RBF(3, 1/8)
                        [3e+0 +/- 0.126]
                        sage: RBF(13, 1)
                        [1e+1 +/- 4.01]

                    ::

                        sage: NF.<sqrt2> = QuadraticField(2)                                        # needs sage.rings.number_field
                        sage: RBF(1/5 + sqrt2/2)                                                    # needs sage.rings.number_field
                        [0.907106781186547 +/- ...e-16]

                    Note that integers and floating-point numbers are \'\'not\'\' rounded to
                    the parent\'s precision::

                        sage: b = RBF(11111111111111111111111111111111111111111111111); b
                        [1.111111111111111e+46 +/- ...e+30]
                        sage: b.mid().exact_rational()
                        11111111111111111111111111111111111111111111111

                    Similarly, converting a real ball from one real ball field to another
                    (with a different precision) only changes the way it is displayed and
                    the precision of operations involving it, not the actual representation
                    of its center::

                        sage: RBF100 = RealBallField(100)
                        sage: b100 = RBF100(1/3); b100
                        [0.333333333333333333333333333333 +/- ...e-31]
                        sage: b53 = RBF(b100); b53
                        [0.3333333333333333 +/- ...e-17]
                        sage: RBF100(b53)
                        [0.333333333333333333333333333333 +/- ...e-31]

                    Special values are supported::

                        sage: RBF(oo).mid(), RBF(-oo).mid(), RBF(unsigned_infinity).mid()
                        (+infinity, -infinity, 0.000000000000000)
                        sage: RBF(NaN)
                        nan

                    Strings can be given as input. Strings must contain decimal
                    floating-point literals. A valid string must consist of a midpoint,
                    a midpoint and a radius separated by "+/-", or just a
                    radius prefixed by "+/-". Optionally, the whole string can be enclosed
                    in square brackets. In general, the string representation of a
                    real ball as returned by ``str()`` can be parsed back (the result
                    will be larger than the original ball if rounding occurs).
                    A few examples::

                        sage: RBF("1.1")
                        [1.100000000000000 +/- ...e-16]
                        sage: RBF(str(RBF("1.1")))
                        [1.100000000000000 +/- ...e-16]
                        sage: RBF("3.25")
                        3.250000000000000
                        sage: RBF("-3.1 +/- 1e-10")
                        [-3.100000000 +/- ...e-10]
                        sage: RBF("[+/-1]")
                        [+/- 1.01]
                        sage: RBF("inf +/- inf")
                        [+/- inf]

                    .. SEEALSO:: :meth:`RealBallField._element_constructor_`

                    TESTS::

                        sage: from sage.rings.real_arb import RealBall
                        sage: RealBall(RBF, sage.symbolic.constants.Pi())
                        [3.141592653589793 +/- ...e-16]
                        sage: RealBall(RBF, sage.symbolic.constants.Log2())
                        [0.6931471805599453 +/- ...e-17]
                        sage: RealBall(RBF, sage.symbolic.constants.Catalan())
                        [0.915965594177219 +/- ...e-16]
                        sage: RealBall(RBF, sage.symbolic.constants.Khinchin())
                        [2.685452001065306 +/- ...e-16]
                        sage: RealBall(RBF, sage.symbolic.constants.Glaisher())
                        [1.282427129100623 +/- ...e-16]
                        sage: RealBall(RBF, sage.symbolic.constants.e)
                        [2.718281828459045 +/- ...e-16]
                        sage: RealBall(RBF, sage.symbolic.constants.EulerGamma()) # abs tol 1e-15
                        [0.5772156649015329 +/- 9.00e-17]
                        sage: RBF("1 +/- 0.001")
                        [1.00 +/- ...e-3]
                        sage: RBF("2.3e10000000000000000000000 +/- 0.00005e10000000000000000000000")
                        [2.3000e+10000000000000000000000 +/- ...e+9999999999999999999995]
                        sage: RBF("0.3 +/- 0.2 +/- 0.1")
                        Traceback (most recent call last):
                        ...
                        ValueError: unsupported string format

                        sage: NF.<a> = QuadraticField(2, embedding=AA(2).sqrt())
                        sage: RBF.coerce(a)
                        [1.414213562373095 +/- ...e-16]
                        sage: NF.<a> = QuadraticField(2, embedding=-AA(2).sqrt())
                        sage: RBF.coerce(a)
                        [-1.414213562373095 +/- ...e-16]
                        sage: NF.<a> = QuadraticField(2, embedding=None)
                        sage: RBF.coerce(a)
                        Traceback (most recent call last):
                        ...
                        TypeError: no canonical coercion ...
                        sage: QQi.<i> = QuadraticField(-1)
                        sage: RBF(QQi(3))
                        3.000000000000000
                        sage: RBF(i)
                        Traceback (most recent call last):
                        ...
                        ValueError: nonzero imaginary part
                        sage: RBF.coerce(QQi(3))
                        Traceback (most recent call last):
                        ...
                        TypeError: no canonical coercion...
        '''
        @overload
        def Chi(self) -> Any:
            """RealBall.Chi(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3626)

            Hyperbolic cosine integral.

            EXAMPLES::

                sage: RBF(1).Chi()  # abs tol 5e-16
                [0.837866940980208 +/- 4.72e-16]

            TESTS::

                sage: RBF(Chi(1))  # abs tol 5e-16                                          # needs sage.symbolic
                [0.837866940980208 +/- 4.72e-16]"""
        @overload
        def Chi(self) -> Any:
            """RealBall.Chi(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3626)

            Hyperbolic cosine integral.

            EXAMPLES::

                sage: RBF(1).Chi()  # abs tol 5e-16
                [0.837866940980208 +/- 4.72e-16]

            TESTS::

                sage: RBF(Chi(1))  # abs tol 5e-16                                          # needs sage.symbolic
                [0.837866940980208 +/- 4.72e-16]"""
        @overload
        def Ci(self) -> Any:
            """RealBall.Ci(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3582)

            Cosine integral.

            EXAMPLES::

                sage: RBF(1).Ci()  # abs tol 5e-16
                [0.337403922900968 +/- 3.25e-16]

            TESTS::

                sage: RBF(Ci(1))  # abs tol 5e-16                                           # needs sage.symbolic
                [0.337403922900968 +/- 3.25e-16]"""
        @overload
        def Ci(self) -> Any:
            """RealBall.Ci(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3582)

            Cosine integral.

            EXAMPLES::

                sage: RBF(1).Ci()  # abs tol 5e-16
                [0.337403922900968 +/- 3.25e-16]

            TESTS::

                sage: RBF(Ci(1))  # abs tol 5e-16                                           # needs sage.symbolic
                [0.337403922900968 +/- 3.25e-16]"""
        @overload
        def Ei(self) -> Any:
            """RealBall.Ei(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3540)

            Exponential integral.

            EXAMPLES::

                sage: RBF(1).Ei()  # abs tol 5e-15
                [1.89511781635594 +/- 4.94e-15]

            TESTS::

                sage: RBF(Ei(1))  # abs tol 5e-15                                           # needs sage.symbolic
                [1.89511781635594 +/- 4.94e-15]"""
        @overload
        def Ei(self) -> Any:
            """RealBall.Ei(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3540)

            Exponential integral.

            EXAMPLES::

                sage: RBF(1).Ei()  # abs tol 5e-15
                [1.89511781635594 +/- 4.94e-15]

            TESTS::

                sage: RBF(Ei(1))  # abs tol 5e-15                                           # needs sage.symbolic
                [1.89511781635594 +/- 4.94e-15]"""
        @overload
        def Li(self) -> Any:
            """RealBall.Li(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3672)

            Offset logarithmic integral.

            EXAMPLES::

                sage: RBF(3).Li()  # abs tol 5e-15
                [1.11842481454970 +/- 7.61e-15]"""
        @overload
        def Li(self) -> Any:
            """RealBall.Li(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3672)

            Offset logarithmic integral.

            EXAMPLES::

                sage: RBF(3).Li()  # abs tol 5e-15
                [1.11842481454970 +/- 7.61e-15]"""
        @overload
        def Shi(self) -> Any:
            """RealBall.Shi(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3604)

            Hyperbolic sine integral.

            EXAMPLES::

                sage: RBF(1).Shi() # abs tol 5e-15
                [1.05725087537573 +/- 2.77e-15]

            TESTS::

                sage: RBF(Shi(1))  # abs tol 5e-15                                          # needs sage.symbolic
                [1.05725087537573 +/- 2.77e-15]"""
        @overload
        def Shi(self) -> Any:
            """RealBall.Shi(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3604)

            Hyperbolic sine integral.

            EXAMPLES::

                sage: RBF(1).Shi() # abs tol 5e-15
                [1.05725087537573 +/- 2.77e-15]

            TESTS::

                sage: RBF(Shi(1))  # abs tol 5e-15                                          # needs sage.symbolic
                [1.05725087537573 +/- 2.77e-15]"""
        @overload
        def Si(self) -> Any:
            """RealBall.Si(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3560)

            Sine integral.

            EXAMPLES::

                sage: RBF(1).Si() # abs tol 1e-15
                [0.946083070367183 +/- 9.22e-16]

            TESTS::

                sage: RBF(Si(1))  # abs tol 1e-15                                           # needs sage.symbolic
                [0.946083070367183 +/- 9.22e-16]"""
        @overload
        def Si(self) -> Any:
            """RealBall.Si(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3560)

            Sine integral.

            EXAMPLES::

                sage: RBF(1).Si() # abs tol 1e-15
                [0.946083070367183 +/- 9.22e-16]

            TESTS::

                sage: RBF(Si(1))  # abs tol 1e-15                                           # needs sage.symbolic
                [0.946083070367183 +/- 9.22e-16]"""
        @overload
        def above_abs(self) -> Any:
            """RealBall.above_abs(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 1897)

            Return an upper bound for the absolute value of this ball.

            OUTPUT: a ball with zero radius

            EXAMPLES::

                sage: b = RealBallField(8)(1/3).above_abs()
                sage: b
                [0.33 +/- ...e-3]
                sage: b.is_exact()
                True
                sage: QQ(b)
                171/512

            .. SEEALSO:: :meth:`below_abs`"""
        @overload
        def above_abs(self) -> Any:
            """RealBall.above_abs(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 1897)

            Return an upper bound for the absolute value of this ball.

            OUTPUT: a ball with zero radius

            EXAMPLES::

                sage: b = RealBallField(8)(1/3).above_abs()
                sage: b
                [0.33 +/- ...e-3]
                sage: b.is_exact()
                True
                sage: QQ(b)
                171/512

            .. SEEALSO:: :meth:`below_abs`"""
        @overload
        def accuracy(self) -> Any:
            """RealBall.accuracy(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 2082)

            Return the effective relative accuracy of this ball measured in bits.

            The accuracy is defined as the difference between the position of the
            top bit in the midpoint and the top bit in the radius, minus one.
            The result is clamped between plus/minus
            :meth:`~RealBallField.maximal_accuracy`.

            EXAMPLES::

                sage: RBF(pi).accuracy()                                                    # needs sage.symbolic
                52
                sage: RBF(1).accuracy() == RBF.maximal_accuracy()
                True
                sage: RBF(NaN).accuracy() == -RBF.maximal_accuracy()                        # needs sage.symbolic
                True

            .. SEEALSO:: :meth:`~RealBallField.maximal_accuracy`"""
        @overload
        def accuracy(self) -> Any:
            """RealBall.accuracy(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 2082)

            Return the effective relative accuracy of this ball measured in bits.

            The accuracy is defined as the difference between the position of the
            top bit in the midpoint and the top bit in the radius, minus one.
            The result is clamped between plus/minus
            :meth:`~RealBallField.maximal_accuracy`.

            EXAMPLES::

                sage: RBF(pi).accuracy()                                                    # needs sage.symbolic
                52
                sage: RBF(1).accuracy() == RBF.maximal_accuracy()
                True
                sage: RBF(NaN).accuracy() == -RBF.maximal_accuracy()                        # needs sage.symbolic
                True

            .. SEEALSO:: :meth:`~RealBallField.maximal_accuracy`"""
        @overload
        def accuracy(self) -> Any:
            """RealBall.accuracy(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 2082)

            Return the effective relative accuracy of this ball measured in bits.

            The accuracy is defined as the difference between the position of the
            top bit in the midpoint and the top bit in the radius, minus one.
            The result is clamped between plus/minus
            :meth:`~RealBallField.maximal_accuracy`.

            EXAMPLES::

                sage: RBF(pi).accuracy()                                                    # needs sage.symbolic
                52
                sage: RBF(1).accuracy() == RBF.maximal_accuracy()
                True
                sage: RBF(NaN).accuracy() == -RBF.maximal_accuracy()                        # needs sage.symbolic
                True

            .. SEEALSO:: :meth:`~RealBallField.maximal_accuracy`"""
        @overload
        def accuracy(self) -> Any:
            """RealBall.accuracy(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 2082)

            Return the effective relative accuracy of this ball measured in bits.

            The accuracy is defined as the difference between the position of the
            top bit in the midpoint and the top bit in the radius, minus one.
            The result is clamped between plus/minus
            :meth:`~RealBallField.maximal_accuracy`.

            EXAMPLES::

                sage: RBF(pi).accuracy()                                                    # needs sage.symbolic
                52
                sage: RBF(1).accuracy() == RBF.maximal_accuracy()
                True
                sage: RBF(NaN).accuracy() == -RBF.maximal_accuracy()                        # needs sage.symbolic
                True

            .. SEEALSO:: :meth:`~RealBallField.maximal_accuracy`"""
        @overload
        def add_error(self, ampl) -> Any:
            """RealBall.add_error(self, ampl)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 2129)

            Increase the radius of this ball by (an upper bound on) ``ampl``.

            If ``ampl`` is negative, the radius is unchanged.

            INPUT:

            - ``ampl`` -- a real ball (or an object that can be coerced to a real
              ball)

            OUTPUT: a new real ball

            EXAMPLES::

                sage: err = RBF(10^-16)
                sage: RBF(1).add_error(err)
                [1.000000000000000 +/- ...e-16]

            TESTS::

                sage: RBF(1).add_error(-1)
                1.000000000000000
                sage: RBF(0).add_error(RBF(1, rad=2.)).endpoints()
                (-3.00000000745059, 3.00000000745059)"""
        @overload
        def add_error(self, err) -> Any:
            """RealBall.add_error(self, ampl)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 2129)

            Increase the radius of this ball by (an upper bound on) ``ampl``.

            If ``ampl`` is negative, the radius is unchanged.

            INPUT:

            - ``ampl`` -- a real ball (or an object that can be coerced to a real
              ball)

            OUTPUT: a new real ball

            EXAMPLES::

                sage: err = RBF(10^-16)
                sage: RBF(1).add_error(err)
                [1.000000000000000 +/- ...e-16]

            TESTS::

                sage: RBF(1).add_error(-1)
                1.000000000000000
                sage: RBF(0).add_error(RBF(1, rad=2.)).endpoints()
                (-3.00000000745059, 3.00000000745059)"""
        def agm(self, other) -> Any:
            """RealBall.agm(self, other)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 4042)

            Return the arithmetic-geometric mean of ``self`` and ``other``.

            EXAMPLES::

                sage: RBF(1).agm(1)
                1.000000000000000
                sage: RBF(sqrt(2)).agm(1)^(-1)                                              # needs sage.symbolic
                [0.8346268416740...]"""
        @overload
        def arccos(self) -> Any:
            """RealBall.arccos(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3329)

            Return the arccosine of this ball.

            EXAMPLES::

                sage: RBF(1).arccos()
                0
                sage: RBF(1, rad=.125r).arccos()
                nan"""
        @overload
        def arccos(self) -> Any:
            """RealBall.arccos(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3329)

            Return the arccosine of this ball.

            EXAMPLES::

                sage: RBF(1).arccos()
                0
                sage: RBF(1, rad=.125r).arccos()
                nan"""
        @overload
        def arccos(self) -> Any:
            """RealBall.arccos(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3329)

            Return the arccosine of this ball.

            EXAMPLES::

                sage: RBF(1).arccos()
                0
                sage: RBF(1, rad=.125r).arccos()
                nan"""
        @overload
        def arccosh(self) -> Any:
            """RealBall.arccosh(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3470)

            Return the inverse hyperbolic cosine of this ball.

            EXAMPLES::

                sage: RBF(2).arccosh()
                [1.316957896924817 +/- ...e-16]
                sage: RBF(1).arccosh()
                0
                sage: RBF(0).arccosh()
                nan"""
        @overload
        def arccosh(self) -> Any:
            """RealBall.arccosh(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3470)

            Return the inverse hyperbolic cosine of this ball.

            EXAMPLES::

                sage: RBF(2).arccosh()
                [1.316957896924817 +/- ...e-16]
                sage: RBF(1).arccosh()
                0
                sage: RBF(0).arccosh()
                nan"""
        @overload
        def arccosh(self) -> Any:
            """RealBall.arccosh(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3470)

            Return the inverse hyperbolic cosine of this ball.

            EXAMPLES::

                sage: RBF(2).arccosh()
                [1.316957896924817 +/- ...e-16]
                sage: RBF(1).arccosh()
                0
                sage: RBF(0).arccosh()
                nan"""
        @overload
        def arccosh(self) -> Any:
            """RealBall.arccosh(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3470)

            Return the inverse hyperbolic cosine of this ball.

            EXAMPLES::

                sage: RBF(2).arccosh()
                [1.316957896924817 +/- ...e-16]
                sage: RBF(1).arccosh()
                0
                sage: RBF(0).arccosh()
                nan"""
        @overload
        def arcsin(self) -> Any:
            """RealBall.arcsin(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3312)

            Return the arcsine of this ball.

            EXAMPLES::

                sage: RBF(1).arcsin()
                [1.570796326794897 +/- ...e-16]
                sage: RBF(1, rad=.125r).arcsin()
                nan"""
        @overload
        def arcsin(self) -> Any:
            """RealBall.arcsin(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3312)

            Return the arcsine of this ball.

            EXAMPLES::

                sage: RBF(1).arcsin()
                [1.570796326794897 +/- ...e-16]
                sage: RBF(1, rad=.125r).arcsin()
                nan"""
        @overload
        def arcsin(self) -> Any:
            """RealBall.arcsin(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3312)

            Return the arcsine of this ball.

            EXAMPLES::

                sage: RBF(1).arcsin()
                [1.570796326794897 +/- ...e-16]
                sage: RBF(1, rad=.125r).arcsin()
                nan"""
        @overload
        def arcsinh(self) -> Any:
            """RealBall.arcsinh(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3453)

            Return the inverse hyperbolic sine of this ball.

            EXAMPLES::

                sage: RBF(1).arcsinh()
                [0.881373587019543 +/- ...e-16]
                sage: RBF(0).arcsinh()
                0"""
        @overload
        def arcsinh(self) -> Any:
            """RealBall.arcsinh(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3453)

            Return the inverse hyperbolic sine of this ball.

            EXAMPLES::

                sage: RBF(1).arcsinh()
                [0.881373587019543 +/- ...e-16]
                sage: RBF(0).arcsinh()
                0"""
        @overload
        def arcsinh(self) -> Any:
            """RealBall.arcsinh(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3453)

            Return the inverse hyperbolic sine of this ball.

            EXAMPLES::

                sage: RBF(1).arcsinh()
                [0.881373587019543 +/- ...e-16]
                sage: RBF(0).arcsinh()
                0"""
        @overload
        def arctan(self) -> Any:
            """RealBall.arctan(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3346)

            Return the arctangent of this ball.

            EXAMPLES::

                sage: RBF(1).arctan()
                [0.7853981633974483 +/- ...e-17]"""
        @overload
        def arctan(self) -> Any:
            """RealBall.arctan(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3346)

            Return the arctangent of this ball.

            EXAMPLES::

                sage: RBF(1).arctan()
                [0.7853981633974483 +/- ...e-17]"""
        @overload
        def arctanh(self) -> Any:
            """RealBall.arctanh(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3489)

            Return the inverse hyperbolic tangent of this ball.

            EXAMPLES::

                sage: RBF(0).arctanh()
                0
                sage: RBF(1/2).arctanh()
                [0.549306144334055 +/- ...e-16]
                sage: RBF(1).arctanh()
                nan"""
        @overload
        def arctanh(self) -> Any:
            """RealBall.arctanh(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3489)

            Return the inverse hyperbolic tangent of this ball.

            EXAMPLES::

                sage: RBF(0).arctanh()
                0
                sage: RBF(1/2).arctanh()
                [0.549306144334055 +/- ...e-16]
                sage: RBF(1).arctanh()
                nan"""
        @overload
        def arctanh(self) -> Any:
            """RealBall.arctanh(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3489)

            Return the inverse hyperbolic tangent of this ball.

            EXAMPLES::

                sage: RBF(0).arctanh()
                0
                sage: RBF(1/2).arctanh()
                [0.549306144334055 +/- ...e-16]
                sage: RBF(1).arctanh()
                nan"""
        @overload
        def arctanh(self) -> Any:
            """RealBall.arctanh(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3489)

            Return the inverse hyperbolic tangent of this ball.

            EXAMPLES::

                sage: RBF(0).arctanh()
                0
                sage: RBF(1/2).arctanh()
                [0.549306144334055 +/- ...e-16]
                sage: RBF(1).arctanh()
                nan"""
        @overload
        def below_abs(self, test_zero=...) -> Any:
            """RealBall.below_abs(self, test_zero=False)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 1857)

            Return a lower bound for the absolute value of this ball.

            INPUT:

            - ``test_zero`` -- boolean (default: ``False``); if ``True``,
              make sure that the returned lower bound is positive, raising
              an error if the ball contains zero.

            OUTPUT: a ball with zero radius

            EXAMPLES::

                sage: RealBallField(8)(1/3).below_abs()
                [0.33 +/- ...e-5]
                sage: b = RealBallField(8)(1/3).below_abs()
                sage: b
                [0.33 +/- ...e-5]
                sage: b.is_exact()
                True
                sage: QQ(b)
                169/512

                sage: RBF(0).below_abs()
                0
                sage: RBF(0).below_abs(test_zero=True)
                Traceback (most recent call last):
                ...
                ValueError: ball contains zero

            .. SEEALSO:: :meth:`above_abs`"""
        @overload
        def below_abs(self) -> Any:
            """RealBall.below_abs(self, test_zero=False)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 1857)

            Return a lower bound for the absolute value of this ball.

            INPUT:

            - ``test_zero`` -- boolean (default: ``False``); if ``True``,
              make sure that the returned lower bound is positive, raising
              an error if the ball contains zero.

            OUTPUT: a ball with zero radius

            EXAMPLES::

                sage: RealBallField(8)(1/3).below_abs()
                [0.33 +/- ...e-5]
                sage: b = RealBallField(8)(1/3).below_abs()
                sage: b
                [0.33 +/- ...e-5]
                sage: b.is_exact()
                True
                sage: QQ(b)
                169/512

                sage: RBF(0).below_abs()
                0
                sage: RBF(0).below_abs(test_zero=True)
                Traceback (most recent call last):
                ...
                ValueError: ball contains zero

            .. SEEALSO:: :meth:`above_abs`"""
        @overload
        def below_abs(self) -> Any:
            """RealBall.below_abs(self, test_zero=False)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 1857)

            Return a lower bound for the absolute value of this ball.

            INPUT:

            - ``test_zero`` -- boolean (default: ``False``); if ``True``,
              make sure that the returned lower bound is positive, raising
              an error if the ball contains zero.

            OUTPUT: a ball with zero radius

            EXAMPLES::

                sage: RealBallField(8)(1/3).below_abs()
                [0.33 +/- ...e-5]
                sage: b = RealBallField(8)(1/3).below_abs()
                sage: b
                [0.33 +/- ...e-5]
                sage: b.is_exact()
                True
                sage: QQ(b)
                169/512

                sage: RBF(0).below_abs()
                0
                sage: RBF(0).below_abs(test_zero=True)
                Traceback (most recent call last):
                ...
                ValueError: ball contains zero

            .. SEEALSO:: :meth:`above_abs`"""
        @overload
        def below_abs(self) -> Any:
            """RealBall.below_abs(self, test_zero=False)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 1857)

            Return a lower bound for the absolute value of this ball.

            INPUT:

            - ``test_zero`` -- boolean (default: ``False``); if ``True``,
              make sure that the returned lower bound is positive, raising
              an error if the ball contains zero.

            OUTPUT: a ball with zero radius

            EXAMPLES::

                sage: RealBallField(8)(1/3).below_abs()
                [0.33 +/- ...e-5]
                sage: b = RealBallField(8)(1/3).below_abs()
                sage: b
                [0.33 +/- ...e-5]
                sage: b.is_exact()
                True
                sage: QQ(b)
                169/512

                sage: RBF(0).below_abs()
                0
                sage: RBF(0).below_abs(test_zero=True)
                Traceback (most recent call last):
                ...
                ValueError: ball contains zero

            .. SEEALSO:: :meth:`above_abs`"""
        @overload
        def below_abs(self, test_zero=...) -> Any:
            """RealBall.below_abs(self, test_zero=False)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 1857)

            Return a lower bound for the absolute value of this ball.

            INPUT:

            - ``test_zero`` -- boolean (default: ``False``); if ``True``,
              make sure that the returned lower bound is positive, raising
              an error if the ball contains zero.

            OUTPUT: a ball with zero radius

            EXAMPLES::

                sage: RealBallField(8)(1/3).below_abs()
                [0.33 +/- ...e-5]
                sage: b = RealBallField(8)(1/3).below_abs()
                sage: b
                [0.33 +/- ...e-5]
                sage: b.is_exact()
                True
                sage: QQ(b)
                169/512

                sage: RBF(0).below_abs()
                0
                sage: RBF(0).below_abs(test_zero=True)
                Traceback (most recent call last):
                ...
                ValueError: ball contains zero

            .. SEEALSO:: :meth:`above_abs`"""
        @overload
        def beta(self, a, z=...) -> Any:
            """RealBall.beta(self, a, z=1)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3689)

            (Incomplete) beta function.

            INPUT:

            - ``a``, ``z`` -- (optional) real balls

            OUTPUT:

            The lower incomplete beta function `B(self, a, z)`.

            With the default value of ``z``, the complete beta function `B(self, a)`.

            EXAMPLES::

                sage: RBF(sin(3)).beta(RBF(2/3).sqrt())  # abs tol 1e-13                    # needs sage.symbolic
                [7.407661629415 +/- 1.07e-13]
                sage: RealBallField(100)(7/2).beta(1)  # abs tol 1e-30
                [0.28571428571428571428571428571 +/- 5.23e-30]
                sage: RealBallField(100)(7/2).beta(1, 1/2)
                [0.025253813613805268728601584361 +/- 2.53e-31]

            .. TODO::

                At the moment RBF(beta(a,b)) does not work, one needs
                RBF(a).beta(b) for this to work. See :issue:`32851`
                and :issue:`24641`."""
        @overload
        def beta(self, a, b) -> Any:
            """RealBall.beta(self, a, z=1)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3689)

            (Incomplete) beta function.

            INPUT:

            - ``a``, ``z`` -- (optional) real balls

            OUTPUT:

            The lower incomplete beta function `B(self, a, z)`.

            With the default value of ``z``, the complete beta function `B(self, a)`.

            EXAMPLES::

                sage: RBF(sin(3)).beta(RBF(2/3).sqrt())  # abs tol 1e-13                    # needs sage.symbolic
                [7.407661629415 +/- 1.07e-13]
                sage: RealBallField(100)(7/2).beta(1)  # abs tol 1e-30
                [0.28571428571428571428571428571 +/- 5.23e-30]
                sage: RealBallField(100)(7/2).beta(1, 1/2)
                [0.025253813613805268728601584361 +/- 2.53e-31]

            .. TODO::

                At the moment RBF(beta(a,b)) does not work, one needs
                RBF(a).beta(b) for this to work. See :issue:`32851`
                and :issue:`24641`."""
        @overload
        def beta(self, b) -> Any:
            """RealBall.beta(self, a, z=1)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3689)

            (Incomplete) beta function.

            INPUT:

            - ``a``, ``z`` -- (optional) real balls

            OUTPUT:

            The lower incomplete beta function `B(self, a, z)`.

            With the default value of ``z``, the complete beta function `B(self, a)`.

            EXAMPLES::

                sage: RBF(sin(3)).beta(RBF(2/3).sqrt())  # abs tol 1e-13                    # needs sage.symbolic
                [7.407661629415 +/- 1.07e-13]
                sage: RealBallField(100)(7/2).beta(1)  # abs tol 1e-30
                [0.28571428571428571428571428571 +/- 5.23e-30]
                sage: RealBallField(100)(7/2).beta(1, 1/2)
                [0.025253813613805268728601584361 +/- 2.53e-31]

            .. TODO::

                At the moment RBF(beta(a,b)) does not work, one needs
                RBF(a).beta(b) for this to work. See :issue:`32851`
                and :issue:`24641`."""
        @overload
        def ceil(self) -> Any:
            """RealBall.ceil(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3011)

            Return the ceil of this ball.

            EXAMPLES::

                sage: RBF(1000+1/3, rad=1.r).ceil()
                [1.00e+3 +/- 2.01]"""
        @overload
        def ceil(self) -> Any:
            """RealBall.ceil(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3011)

            Return the ceil of this ball.

            EXAMPLES::

                sage: RBF(1000+1/3, rad=1.r).ceil()
                [1.00e+3 +/- 2.01]"""
        def center(self, *args, **kwargs):
            """RealBall.mid(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 1718)

            Return the center of this ball.

            EXAMPLES::

                sage: RealBallField(16)(1/3).mid()
                0.3333
                sage: RealBallField(16)(1/3).mid().parent()
                Real Field with 16 bits of precision
                sage: RealBallField(16)(RBF(1/3)).mid().parent()
                Real Field with 53 bits of precision
                sage: RBF('inf').mid()
                +infinity

            ::

                sage: b = RBF(2)^(2^1000)
                sage: b.mid()
                +infinity

            .. SEEALSO:: :meth:`rad`, :meth:`squash`"""
        def chebyshev_T(self, n) -> Any:
            """RealBall.chebyshev_T(self, n)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3976)

            Evaluate the Chebyshev polynomial of the first kind ``T_n`` at this
            ball.

            EXAMPLES::

                sage: # needs sage.symbolic
                sage: RBF(pi).chebyshev_T(0)
                1.000000000000000
                sage: RBF(pi).chebyshev_T(1)
                [3.141592653589793 +/- ...e-16]
                sage: RBF(pi).chebyshev_T(10**20)
                Traceback (most recent call last):
                ...
                ValueError: index too large
                sage: RBF(pi).chebyshev_T(-1)
                Traceback (most recent call last):
                ...
                ValueError: expected a nonnegative index"""
        def chebyshev_U(self, n) -> Any:
            """RealBall.chebyshev_U(self, n)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 4009)

            Evaluate the Chebyshev polynomial of the second kind ``U_n`` at this
            ball.

            EXAMPLES::

                sage: # needs sage.symbolic
                sage: RBF(pi).chebyshev_U(0)
                1.000000000000000
                sage: RBF(pi).chebyshev_U(1)
                [6.283185307179586 +/- ...e-16]
                sage: RBF(pi).chebyshev_U(10**20)
                Traceback (most recent call last):
                ...
                ValueError: index too large
                sage: RBF(pi).chebyshev_U(-1)
                Traceback (most recent call last):
                ...
                ValueError: expected a nonnegative index"""
        @overload
        def conjugate(self) -> Any:
            """RealBall.conjugate(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3110)

            Return the conjugate of this ball.

            EXAMPLES::

                sage: RBF(1).conjugate()
                1.000000000000000"""
        @overload
        def conjugate(self) -> Any:
            """RealBall.conjugate(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3110)

            Return the conjugate of this ball.

            EXAMPLES::

                sage: RBF(1).conjugate()
                1.000000000000000"""
        @overload
        def contains_exact(self, other) -> Any:
            """RealBall.contains_exact(self, other)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 2564)

            Return ``True`` *iff* the given number (or ball) ``other`` is contained
            in the interval represented by ``self``.

            If ``self`` contains NaN, this function always returns ``True`` (as
            it could represent anything, and in particular could represent all the
            points included in ``other``). If ``other`` contains NaN and ``self``
            does not, it always returns ``False``.

            Use ``other in self`` for a test that works for a wider range of inputs
            but may return false negatives.

            EXAMPLES::

                sage: b = RBF(1)
                sage: b.contains_exact(1)
                True
                sage: b.contains_exact(QQ(1))
                True
                sage: b.contains_exact(1.)
                True
                sage: b.contains_exact(b)
                True

            ::

                sage: RBF(1/3).contains_exact(1/3)
                True
                sage: RBF(sqrt(2)).contains_exact(sqrt(2))                                  # needs sage.symbolic
                Traceback (most recent call last):
                ...
                TypeError: unsupported type: <class 'sage.symbolic.expression.Expression'>

            TESTS::

                sage: b.contains_exact(1r)
                True"""
        @overload
        def contains_exact(self, b) -> Any:
            """RealBall.contains_exact(self, other)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 2564)

            Return ``True`` *iff* the given number (or ball) ``other`` is contained
            in the interval represented by ``self``.

            If ``self`` contains NaN, this function always returns ``True`` (as
            it could represent anything, and in particular could represent all the
            points included in ``other``). If ``other`` contains NaN and ``self``
            does not, it always returns ``False``.

            Use ``other in self`` for a test that works for a wider range of inputs
            but may return false negatives.

            EXAMPLES::

                sage: b = RBF(1)
                sage: b.contains_exact(1)
                True
                sage: b.contains_exact(QQ(1))
                True
                sage: b.contains_exact(1.)
                True
                sage: b.contains_exact(b)
                True

            ::

                sage: RBF(1/3).contains_exact(1/3)
                True
                sage: RBF(sqrt(2)).contains_exact(sqrt(2))                                  # needs sage.symbolic
                Traceback (most recent call last):
                ...
                TypeError: unsupported type: <class 'sage.symbolic.expression.Expression'>

            TESTS::

                sage: b.contains_exact(1r)
                True"""
        @overload
        def contains_integer(self) -> Any:
            """RealBall.contains_integer(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 2665)

            Return ``True`` iff this ball contains any integer.

            EXAMPLES::

                sage: RBF(3.1, 0.1).contains_integer()
                True
                sage: RBF(3.1, 0.05).contains_integer()
                False"""
        @overload
        def contains_integer(self) -> Any:
            """RealBall.contains_integer(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 2665)

            Return ``True`` iff this ball contains any integer.

            EXAMPLES::

                sage: RBF(3.1, 0.1).contains_integer()
                True
                sage: RBF(3.1, 0.05).contains_integer()
                False"""
        @overload
        def contains_integer(self) -> Any:
            """RealBall.contains_integer(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 2665)

            Return ``True`` iff this ball contains any integer.

            EXAMPLES::

                sage: RBF(3.1, 0.1).contains_integer()
                True
                sage: RBF(3.1, 0.05).contains_integer()
                False"""
        @overload
        def contains_zero(self) -> Any:
            """RealBall.contains_zero(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 2650)

            Return ``True`` iff this ball contains zero.

            EXAMPLES::

                sage: RBF(0).contains_zero()
                True
                sage: RBF(RIF(-1, 1)).contains_zero()
                True
                sage: RBF(1/3).contains_zero()
                False"""
        @overload
        def contains_zero(self) -> Any:
            """RealBall.contains_zero(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 2650)

            Return ``True`` iff this ball contains zero.

            EXAMPLES::

                sage: RBF(0).contains_zero()
                True
                sage: RBF(RIF(-1, 1)).contains_zero()
                True
                sage: RBF(1/3).contains_zero()
                False"""
        @overload
        def contains_zero(self) -> Any:
            """RealBall.contains_zero(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 2650)

            Return ``True`` iff this ball contains zero.

            EXAMPLES::

                sage: RBF(0).contains_zero()
                True
                sage: RBF(RIF(-1, 1)).contains_zero()
                True
                sage: RBF(1/3).contains_zero()
                False"""
        @overload
        def contains_zero(self) -> Any:
            """RealBall.contains_zero(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 2650)

            Return ``True`` iff this ball contains zero.

            EXAMPLES::

                sage: RBF(0).contains_zero()
                True
                sage: RBF(RIF(-1, 1)).contains_zero()
                True
                sage: RBF(1/3).contains_zero()
                False"""
        @overload
        def cos(self) -> Any:
            """RealBall.cos(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3231)

            Return the cosine of this ball.

            EXAMPLES::

                sage: RBF(pi).cos()                                                         # needs sage.symbolic
                [-1.00000000000000 +/- ...e-16]

            .. SEEALSO:: :meth:`~sage.rings.real_arb.RealBallField.cospi`"""
        @overload
        def cos(self) -> Any:
            """RealBall.cos(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3231)

            Return the cosine of this ball.

            EXAMPLES::

                sage: RBF(pi).cos()                                                         # needs sage.symbolic
                [-1.00000000000000 +/- ...e-16]

            .. SEEALSO:: :meth:`~sage.rings.real_arb.RealBallField.cospi`"""
        def cos_integral(self, *args, **kwargs):
            """RealBall.Ci(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3582)

            Cosine integral.

            EXAMPLES::

                sage: RBF(1).Ci()  # abs tol 5e-16
                [0.337403922900968 +/- 3.25e-16]

            TESTS::

                sage: RBF(Ci(1))  # abs tol 5e-16                                           # needs sage.symbolic
                [0.337403922900968 +/- 3.25e-16]"""
        @overload
        def cosh(self) -> Any:
            """RealBall.cosh(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3376)

            Return the hyperbolic cosine of this ball.

            EXAMPLES::

                sage: RBF(1).cosh()
                [1.543080634815244 +/- ...e-16]"""
        @overload
        def cosh(self) -> Any:
            """RealBall.cosh(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3376)

            Return the hyperbolic cosine of this ball.

            EXAMPLES::

                sage: RBF(1).cosh()
                [1.543080634815244 +/- ...e-16]"""
        def cosh_integral(self, *args, **kwargs):
            """RealBall.Chi(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3626)

            Hyperbolic cosine integral.

            EXAMPLES::

                sage: RBF(1).Chi()  # abs tol 5e-16
                [0.837866940980208 +/- 4.72e-16]

            TESTS::

                sage: RBF(Chi(1))  # abs tol 5e-16                                          # needs sage.symbolic
                [0.837866940980208 +/- 4.72e-16]"""
        @overload
        def cot(self) -> Any:
            """RealBall.cot(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3265)

            Return the cotangent of this ball.

            EXAMPLES::

                sage: RBF(1).cot()
                [0.642092615934331 +/- ...e-16]
                sage: RBF(pi).cot()                                                         # needs sage.symbolic
                nan"""
        @overload
        def cot(self) -> Any:
            """RealBall.cot(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3265)

            Return the cotangent of this ball.

            EXAMPLES::

                sage: RBF(1).cot()
                [0.642092615934331 +/- ...e-16]
                sage: RBF(pi).cot()                                                         # needs sage.symbolic
                nan"""
        @overload
        def cot(self) -> Any:
            """RealBall.cot(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3265)

            Return the cotangent of this ball.

            EXAMPLES::

                sage: RBF(1).cot()
                [0.642092615934331 +/- ...e-16]
                sage: RBF(pi).cot()                                                         # needs sage.symbolic
                nan"""
        @overload
        def coth(self) -> Any:
            """RealBall.coth(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3406)

            Return the hyperbolic cotangent of this ball.

            EXAMPLES::

                sage: RBF(1).coth()
                [1.313035285499331 +/- ...e-16]
                sage: RBF(0).coth()
                nan"""
        @overload
        def coth(self) -> Any:
            """RealBall.coth(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3406)

            Return the hyperbolic cotangent of this ball.

            EXAMPLES::

                sage: RBF(1).coth()
                [1.313035285499331 +/- ...e-16]
                sage: RBF(0).coth()
                nan"""
        @overload
        def coth(self) -> Any:
            """RealBall.coth(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3406)

            Return the hyperbolic cotangent of this ball.

            EXAMPLES::

                sage: RBF(1).coth()
                [1.313035285499331 +/- ...e-16]
                sage: RBF(0).coth()
                nan"""
        @overload
        def csc(self) -> Any:
            """RealBall.csc(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3297)

            Return the cosecant of this ball.

            EXAMPLES::

                sage: RBF(1).csc()
                [1.188395105778121 +/- ...e-16]"""
        @overload
        def csc(self) -> Any:
            """RealBall.csc(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3297)

            Return the cosecant of this ball.

            EXAMPLES::

                sage: RBF(1).csc()
                [1.188395105778121 +/- ...e-16]"""
        @overload
        def csch(self) -> Any:
            """RealBall.csch(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3438)

            Return the hyperbolic cosecant of this ball.

            EXAMPLES::

                sage: RBF(1).csch()
                [0.850918128239321 +/- ...e-16]"""
        @overload
        def csch(self) -> Any:
            """RealBall.csch(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3438)

            Return the hyperbolic cosecant of this ball.

            EXAMPLES::

                sage: RBF(1).csch()
                [0.850918128239321 +/- ...e-16]"""
        @overload
        def diameter(self) -> Any:
            """RealBall.diameter(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 1783)

            Return the diameter of this ball.

            EXAMPLES::

                sage: RBF(1/3).diameter()
                1.1102230e-16
                sage: RBF(1/3).diameter().parent()
                Real Field with 30 bits of precision
                sage: RBF(RIF(1.02, 1.04)).diameter()
                0.020000000

            .. SEEALSO:: :meth:`rad`, :meth:`rad_as_ball`, :meth:`mid`"""
        @overload
        def diameter(self) -> Any:
            """RealBall.diameter(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 1783)

            Return the diameter of this ball.

            EXAMPLES::

                sage: RBF(1/3).diameter()
                1.1102230e-16
                sage: RBF(1/3).diameter().parent()
                Real Field with 30 bits of precision
                sage: RBF(RIF(1.02, 1.04)).diameter()
                0.020000000

            .. SEEALSO:: :meth:`rad`, :meth:`rad_as_ball`, :meth:`mid`"""
        @overload
        def diameter(self) -> Any:
            """RealBall.diameter(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 1783)

            Return the diameter of this ball.

            EXAMPLES::

                sage: RBF(1/3).diameter()
                1.1102230e-16
                sage: RBF(1/3).diameter().parent()
                Real Field with 30 bits of precision
                sage: RBF(RIF(1.02, 1.04)).diameter()
                0.020000000

            .. SEEALSO:: :meth:`rad`, :meth:`rad_as_ball`, :meth:`mid`"""
        @overload
        def diameter(self) -> Any:
            """RealBall.diameter(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 1783)

            Return the diameter of this ball.

            EXAMPLES::

                sage: RBF(1/3).diameter()
                1.1102230e-16
                sage: RBF(1/3).diameter().parent()
                Real Field with 30 bits of precision
                sage: RBF(RIF(1.02, 1.04)).diameter()
                0.020000000

            .. SEEALSO:: :meth:`rad`, :meth:`rad_as_ball`, :meth:`mid`"""
        @overload
        def endpoints(self, rnd=...) -> Any:
            """RealBall.endpoints(self, rnd=None)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 1969)

            Return the endpoints of this ball, rounded outwards.

            INPUT:

            - ``rnd`` -- string; rounding mode for the parent of the resulting
              floating-point numbers (does not affect their values!), see
              :meth:`sage.rings.real_mpfi.RealIntervalFieldElement.upper`

            OUTPUT: a pair of real numbers

            EXAMPLES::

                sage: RBF(-1/3).endpoints()
                (-0.333333333333334, -0.333333333333333)

            .. SEEALSO:: :meth:`lower`, :meth:`upper`"""
        @overload
        def endpoints(self) -> Any:
            """RealBall.endpoints(self, rnd=None)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 1969)

            Return the endpoints of this ball, rounded outwards.

            INPUT:

            - ``rnd`` -- string; rounding mode for the parent of the resulting
              floating-point numbers (does not affect their values!), see
              :meth:`sage.rings.real_mpfi.RealIntervalFieldElement.upper`

            OUTPUT: a pair of real numbers

            EXAMPLES::

                sage: RBF(-1/3).endpoints()
                (-0.333333333333334, -0.333333333333333)

            .. SEEALSO:: :meth:`lower`, :meth:`upper`"""
        @overload
        def erf(self) -> Any:
            """RealBall.erf(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3510)

            Error function.

            EXAMPLES::

                sage: RBF(1/2).erf() # abs tol 1e-16
                [0.520499877813047 +/- 6.10e-16]"""
        @overload
        def erf(self) -> Any:
            """RealBall.erf(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3510)

            Error function.

            EXAMPLES::

                sage: RBF(1/2).erf() # abs tol 1e-16
                [0.520499877813047 +/- 6.10e-16]"""
        @overload
        def erfi(self) -> Any:
            """RealBall.erfi(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3525)

            Imaginary error function.

            EXAMPLES::

                sage: RBF(1/2).erfi()
                [0.614952094696511 +/- 2.22e-16]"""
        @overload
        def erfi(self) -> Any:
            """RealBall.erfi(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3525)

            Imaginary error function.

            EXAMPLES::

                sage: RBF(1/2).erfi()
                [0.614952094696511 +/- 2.22e-16]"""
        @overload
        def exp(self) -> Any:
            """RealBall.exp(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3180)

            Return the exponential of this ball.

            EXAMPLES::

                sage: RBF(1).exp()
                [2.718281828459045 +/- ...e-16]"""
        @overload
        def exp(self) -> Any:
            """RealBall.exp(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3180)

            Return the exponential of this ball.

            EXAMPLES::

                sage: RBF(1).exp()
                [2.718281828459045 +/- ...e-16]"""
        @overload
        def expm1(self) -> Any:
            """RealBall.expm1(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3195)

            Return ``exp(self) - 1``, computed accurately when ``self`` is close to
            zero.

            EXAMPLES::

                sage: eps = RBF(1e-30)
                sage: exp(eps) - 1
                [+/- ...e-30]
                sage: eps.expm1()
                [1.000000000000000e-30 +/- ...e-47]"""
        @overload
        def expm1(self) -> Any:
            """RealBall.expm1(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3195)

            Return ``exp(self) - 1``, computed accurately when ``self`` is close to
            zero.

            EXAMPLES::

                sage: eps = RBF(1e-30)
                sage: exp(eps) - 1
                [+/- ...e-30]
                sage: eps.expm1()
                [1.000000000000000e-30 +/- ...e-47]"""
        @overload
        def floor(self) -> Any:
            """RealBall.floor(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 2996)

            Return the floor of this ball.

            EXAMPLES::

                sage: RBF(1000+1/3, rad=1.r).floor()
                [1.00e+3 +/- 1.01]"""
        @overload
        def floor(self) -> Any:
            """RealBall.floor(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 2996)

            Return the floor of this ball.

            EXAMPLES::

                sage: RBF(1000+1/3, rad=1.r).floor()
                [1.00e+3 +/- 1.01]"""
        def gamma(self, a=...) -> Any:
            """RealBall.gamma(self, a=None)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3728)

            Image of this ball by the (upper incomplete) Euler Gamma function.

            For `a` real, return the upper incomplete Gamma function
            `\\Gamma(self,a)`.

            For integer and rational arguments,
            :meth:`~sage.rings.real_arb.RealBallField.gamma` may be faster.

            EXAMPLES::

                sage: RBF(1/2).gamma()
                [1.772453850905516 +/- ...e-16]
                sage: RBF(gamma(3/2, RBF(2).sqrt()))  # abs tol 2e-17
                [0.37118875695353 +/- 3.00e-15]
                sage: RBF(3/2).gamma_inc(RBF(2).sqrt())  # abs tol 2e-17
                [0.37118875695353 +/- 3.00e-15]

            .. SEEALSO::
                :meth:`~sage.rings.real_arb.RealBallField.gamma`

            TESTS::

                sage: RealBallField(100).gamma(1/2)
                [1.77245385090551602729816748334 +/- 1.90e-30]"""
        def gamma_inc(self, *args, **kwargs):
            """RealBall.gamma(self, a=None)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3728)

            Image of this ball by the (upper incomplete) Euler Gamma function.

            For `a` real, return the upper incomplete Gamma function
            `\\Gamma(self,a)`.

            For integer and rational arguments,
            :meth:`~sage.rings.real_arb.RealBallField.gamma` may be faster.

            EXAMPLES::

                sage: RBF(1/2).gamma()
                [1.772453850905516 +/- ...e-16]
                sage: RBF(gamma(3/2, RBF(2).sqrt()))  # abs tol 2e-17
                [0.37118875695353 +/- 3.00e-15]
                sage: RBF(3/2).gamma_inc(RBF(2).sqrt())  # abs tol 2e-17
                [0.37118875695353 +/- 3.00e-15]

            .. SEEALSO::
                :meth:`~sage.rings.real_arb.RealBallField.gamma`

            TESTS::

                sage: RealBallField(100).gamma(1/2)
                [1.77245385090551602729816748334 +/- 1.90e-30]"""
        def gamma_inc_lower(self, a) -> Any:
            """RealBall.gamma_inc_lower(self, a)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3770)

            Image of this ball by the lower incomplete Euler Gamma function.

            For `a` real, return the lower incomplete Gamma function
            of `\\Gamma(self,a)`.

            EXAMPLES::

                sage: RBF(gamma_inc_lower(1/2, RBF(2).sqrt()))
                [1.608308637729248 +/- 8.14e-16]
                sage: RealBallField(100)(7/2).gamma_inc_lower(5)
                [2.6966551541863035516887949614 +/- 8.91e-29]"""
        def identical(self, RealBallother) -> Any:
            """RealBall.identical(self, RealBall other)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 2524)

            Return ``True`` iff ``self`` and ``other`` are equal as balls, i.e.
            have both the same midpoint and radius.

            Note that this is not the same thing as testing whether both ``self``
            and ``other`` certainly represent the same real number, unless either
            ``self`` or ``other`` is exact (and neither contains NaN). To test
            whether both operands might represent the same mathematical quantity,
            use :meth:`overlaps` or :meth:`contains`, depending on the
            circumstance.

            EXAMPLES::

                sage: RBF(1).identical(RBF(3)-RBF(2))
                True
                sage: RBF(1, rad=0.25r).identical(RBF(1, rad=0.25r))
                True
                sage: RBF(1).identical(RBF(1, rad=0.25r))
                False"""
        @overload
        def imag(self) -> Any:
            """RealBall.imag(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 2018)

            Return the imaginary part of this ball.

            EXAMPLES::

                sage: RBF(1/3).imag()
                0"""
        @overload
        def imag(self) -> Any:
            """RealBall.imag(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 2018)

            Return the imaginary part of this ball.

            EXAMPLES::

                sage: RBF(1/3).imag()
                0"""
        @overload
        def is_NaN(self) -> Any:
            """RealBall.is_NaN(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 2732)

            Return ``True`` if this ball is not-a-number.

            EXAMPLES::

                sage: RBF(NaN).is_NaN()                                                     # needs sage.symbolic
                True
                sage: RBF(-5).gamma().is_NaN()
                True
                sage: RBF(infinity).is_NaN()
                False
                sage: RBF(42, rad=1.r).is_NaN()
                False"""
        @overload
        def is_NaN(self) -> Any:
            """RealBall.is_NaN(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 2732)

            Return ``True`` if this ball is not-a-number.

            EXAMPLES::

                sage: RBF(NaN).is_NaN()                                                     # needs sage.symbolic
                True
                sage: RBF(-5).gamma().is_NaN()
                True
                sage: RBF(infinity).is_NaN()
                False
                sage: RBF(42, rad=1.r).is_NaN()
                False"""
        @overload
        def is_NaN(self) -> Any:
            """RealBall.is_NaN(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 2732)

            Return ``True`` if this ball is not-a-number.

            EXAMPLES::

                sage: RBF(NaN).is_NaN()                                                     # needs sage.symbolic
                True
                sage: RBF(-5).gamma().is_NaN()
                True
                sage: RBF(infinity).is_NaN()
                False
                sage: RBF(42, rad=1.r).is_NaN()
                False"""
        @overload
        def is_NaN(self) -> Any:
            """RealBall.is_NaN(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 2732)

            Return ``True`` if this ball is not-a-number.

            EXAMPLES::

                sage: RBF(NaN).is_NaN()                                                     # needs sage.symbolic
                True
                sage: RBF(-5).gamma().is_NaN()
                True
                sage: RBF(infinity).is_NaN()
                False
                sage: RBF(42, rad=1.r).is_NaN()
                False"""
        @overload
        def is_NaN(self) -> Any:
            """RealBall.is_NaN(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 2732)

            Return ``True`` if this ball is not-a-number.

            EXAMPLES::

                sage: RBF(NaN).is_NaN()                                                     # needs sage.symbolic
                True
                sage: RBF(-5).gamma().is_NaN()
                True
                sage: RBF(infinity).is_NaN()
                False
                sage: RBF(42, rad=1.r).is_NaN()
                False"""
        @overload
        def is_exact(self) -> Any:
            """RealBall.is_exact(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 2232)

            Return ``True`` iff the radius of this ball is zero.

            EXAMPLES::

                sage: RBF = RealBallField()
                sage: RBF(1).is_exact()
                True
                sage: RBF(RIF(0.1, 0.2)).is_exact()
                False"""
        @overload
        def is_exact(self) -> Any:
            """RealBall.is_exact(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 2232)

            Return ``True`` iff the radius of this ball is zero.

            EXAMPLES::

                sage: RBF = RealBallField()
                sage: RBF(1).is_exact()
                True
                sage: RBF(RIF(0.1, 0.2)).is_exact()
                False"""
        @overload
        def is_exact(self) -> Any:
            """RealBall.is_exact(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 2232)

            Return ``True`` iff the radius of this ball is zero.

            EXAMPLES::

                sage: RBF = RealBallField()
                sage: RBF(1).is_exact()
                True
                sage: RBF(RIF(0.1, 0.2)).is_exact()
                False"""
        @overload
        def is_finite(self) -> Any:
            """RealBall.is_finite(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 2510)

            Return ``True`` iff the midpoint and radius of this ball are both
            finite floating-point numbers, i.e. not infinities or NaN.

            EXAMPLES::

                sage: (RBF(2)^(2^1000)).is_finite()
                True
                sage: RBF(oo).is_finite()
                False"""
        @overload
        def is_finite(self) -> Any:
            """RealBall.is_finite(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 2510)

            Return ``True`` iff the midpoint and radius of this ball are both
            finite floating-point numbers, i.e. not infinities or NaN.

            EXAMPLES::

                sage: (RBF(2)^(2^1000)).is_finite()
                True
                sage: RBF(oo).is_finite()
                False"""
        @overload
        def is_finite(self) -> Any:
            """RealBall.is_finite(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 2510)

            Return ``True`` iff the midpoint and radius of this ball are both
            finite floating-point numbers, i.e. not infinities or NaN.

            EXAMPLES::

                sage: (RBF(2)^(2^1000)).is_finite()
                True
                sage: RBF(oo).is_finite()
                False"""
        @overload
        def is_infinity(self) -> Any:
            """RealBall.is_infinity(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 2702)

            Return ``True`` if this ball contains or may represent a point at
            infinity.

            This is the exact negation of :meth:`is_finite`, used in comparisons
            with Sage symbolic infinities.

            .. WARNING::

                Contrary to the usual convention, a return value of ``True`` does
                not imply that all points of the ball satisfy the predicate.
                This is due to the way comparisons with symbolic infinities work in
                sage.

            EXAMPLES::

                sage: RBF(infinity).is_infinity()
                True
                sage: RBF(-infinity).is_infinity()
                True
                sage: RBF(NaN).is_infinity()                                                # needs sage.symbolic
                True
                sage: (~RBF(0)).is_infinity()
                True
                sage: RBF(42, rad=1.r).is_infinity()
                False"""
        @overload
        def is_infinity(self) -> Any:
            """RealBall.is_infinity(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 2702)

            Return ``True`` if this ball contains or may represent a point at
            infinity.

            This is the exact negation of :meth:`is_finite`, used in comparisons
            with Sage symbolic infinities.

            .. WARNING::

                Contrary to the usual convention, a return value of ``True`` does
                not imply that all points of the ball satisfy the predicate.
                This is due to the way comparisons with symbolic infinities work in
                sage.

            EXAMPLES::

                sage: RBF(infinity).is_infinity()
                True
                sage: RBF(-infinity).is_infinity()
                True
                sage: RBF(NaN).is_infinity()                                                # needs sage.symbolic
                True
                sage: (~RBF(0)).is_infinity()
                True
                sage: RBF(42, rad=1.r).is_infinity()
                False"""
        @overload
        def is_infinity(self) -> Any:
            """RealBall.is_infinity(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 2702)

            Return ``True`` if this ball contains or may represent a point at
            infinity.

            This is the exact negation of :meth:`is_finite`, used in comparisons
            with Sage symbolic infinities.

            .. WARNING::

                Contrary to the usual convention, a return value of ``True`` does
                not imply that all points of the ball satisfy the predicate.
                This is due to the way comparisons with symbolic infinities work in
                sage.

            EXAMPLES::

                sage: RBF(infinity).is_infinity()
                True
                sage: RBF(-infinity).is_infinity()
                True
                sage: RBF(NaN).is_infinity()                                                # needs sage.symbolic
                True
                sage: (~RBF(0)).is_infinity()
                True
                sage: RBF(42, rad=1.r).is_infinity()
                False"""
        @overload
        def is_infinity(self) -> Any:
            """RealBall.is_infinity(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 2702)

            Return ``True`` if this ball contains or may represent a point at
            infinity.

            This is the exact negation of :meth:`is_finite`, used in comparisons
            with Sage symbolic infinities.

            .. WARNING::

                Contrary to the usual convention, a return value of ``True`` does
                not imply that all points of the ball satisfy the predicate.
                This is due to the way comparisons with symbolic infinities work in
                sage.

            EXAMPLES::

                sage: RBF(infinity).is_infinity()
                True
                sage: RBF(-infinity).is_infinity()
                True
                sage: RBF(NaN).is_infinity()                                                # needs sage.symbolic
                True
                sage: (~RBF(0)).is_infinity()
                True
                sage: RBF(42, rad=1.r).is_infinity()
                False"""
        @overload
        def is_infinity(self) -> Any:
            """RealBall.is_infinity(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 2702)

            Return ``True`` if this ball contains or may represent a point at
            infinity.

            This is the exact negation of :meth:`is_finite`, used in comparisons
            with Sage symbolic infinities.

            .. WARNING::

                Contrary to the usual convention, a return value of ``True`` does
                not imply that all points of the ball satisfy the predicate.
                This is due to the way comparisons with symbolic infinities work in
                sage.

            EXAMPLES::

                sage: RBF(infinity).is_infinity()
                True
                sage: RBF(-infinity).is_infinity()
                True
                sage: RBF(NaN).is_infinity()                                                # needs sage.symbolic
                True
                sage: (~RBF(0)).is_infinity()
                True
                sage: RBF(42, rad=1.r).is_infinity()
                False"""
        @overload
        def is_infinity(self) -> Any:
            """RealBall.is_infinity(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 2702)

            Return ``True`` if this ball contains or may represent a point at
            infinity.

            This is the exact negation of :meth:`is_finite`, used in comparisons
            with Sage symbolic infinities.

            .. WARNING::

                Contrary to the usual convention, a return value of ``True`` does
                not imply that all points of the ball satisfy the predicate.
                This is due to the way comparisons with symbolic infinities work in
                sage.

            EXAMPLES::

                sage: RBF(infinity).is_infinity()
                True
                sage: RBF(-infinity).is_infinity()
                True
                sage: RBF(NaN).is_infinity()                                                # needs sage.symbolic
                True
                sage: (~RBF(0)).is_infinity()
                True
                sage: RBF(42, rad=1.r).is_infinity()
                False"""
        @overload
        def is_negative_infinity(self) -> Any:
            """RealBall.is_negative_infinity(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 2678)

            Return ``True`` if this ball is the point -∞.

            EXAMPLES::

                sage: RBF(-infinity).is_negative_infinity()
                True"""
        @overload
        def is_negative_infinity(self) -> Any:
            """RealBall.is_negative_infinity(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 2678)

            Return ``True`` if this ball is the point -∞.

            EXAMPLES::

                sage: RBF(-infinity).is_negative_infinity()
                True"""
        @overload
        def is_nonzero(self) -> Any:
            """RealBall.is_nonzero(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 2181)

            Return ``True`` iff zero is not contained in the interval represented
            by this ball.

            .. NOTE::

                This method is not the negation of :meth:`is_zero`: it only
                returns ``True`` if zero is known not to be contained in the ball.

                Use ``bool(b)`` (or, equivalently, ``not b.is_zero()``) to check if
                a ball\xa0``b`` **may** represent a nonzero number (for instance, to
                determine the “degree” of a polynomial with ball coefficients).

            EXAMPLES::

                sage: RBF = RealBallField()
                sage: RBF(pi).is_nonzero()                                                  # needs sage.symbolic
                True
                sage: RBF(RIF(-0.5, 0.5)).is_nonzero()
                False

            .. SEEALSO:: :meth:`is_zero`"""
        @overload
        def is_nonzero(self) -> Any:
            """RealBall.is_nonzero(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 2181)

            Return ``True`` iff zero is not contained in the interval represented
            by this ball.

            .. NOTE::

                This method is not the negation of :meth:`is_zero`: it only
                returns ``True`` if zero is known not to be contained in the ball.

                Use ``bool(b)`` (or, equivalently, ``not b.is_zero()``) to check if
                a ball\xa0``b`` **may** represent a nonzero number (for instance, to
                determine the “degree” of a polynomial with ball coefficients).

            EXAMPLES::

                sage: RBF = RealBallField()
                sage: RBF(pi).is_nonzero()                                                  # needs sage.symbolic
                True
                sage: RBF(RIF(-0.5, 0.5)).is_nonzero()
                False

            .. SEEALSO:: :meth:`is_zero`"""
        @overload
        def is_nonzero(self) -> Any:
            """RealBall.is_nonzero(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 2181)

            Return ``True`` iff zero is not contained in the interval represented
            by this ball.

            .. NOTE::

                This method is not the negation of :meth:`is_zero`: it only
                returns ``True`` if zero is known not to be contained in the ball.

                Use ``bool(b)`` (or, equivalently, ``not b.is_zero()``) to check if
                a ball\xa0``b`` **may** represent a nonzero number (for instance, to
                determine the “degree” of a polynomial with ball coefficients).

            EXAMPLES::

                sage: RBF = RealBallField()
                sage: RBF(pi).is_nonzero()                                                  # needs sage.symbolic
                True
                sage: RBF(RIF(-0.5, 0.5)).is_nonzero()
                False

            .. SEEALSO:: :meth:`is_zero`"""
        @overload
        def is_positive_infinity(self) -> Any:
            """RealBall.is_positive_infinity(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 2690)

            Return ``True`` if this ball is the point +∞.

            EXAMPLES::

                sage: RBF(infinity).is_positive_infinity()
                True"""
        @overload
        def is_positive_infinity(self) -> Any:
            """RealBall.is_positive_infinity(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 2690)

            Return ``True`` if this ball is the point +∞.

            EXAMPLES::

                sage: RBF(infinity).is_positive_infinity()
                True"""
        @overload
        def is_zero(self) -> Any:
            """RealBall.is_zero(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 2165)

            Return ``True`` iff the midpoint and radius of this ball are both zero.

            EXAMPLES::

                sage: RBF = RealBallField()
                sage: RBF(0).is_zero()
                True
                sage: RBF(RIF(-0.5, 0.5)).is_zero()
                False

            .. SEEALSO:: :meth:`is_nonzero`"""
        @overload
        def is_zero(self) -> Any:
            """RealBall.is_zero(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 2165)

            Return ``True`` iff the midpoint and radius of this ball are both zero.

            EXAMPLES::

                sage: RBF = RealBallField()
                sage: RBF(0).is_zero()
                True
                sage: RBF(RIF(-0.5, 0.5)).is_zero()
                False

            .. SEEALSO:: :meth:`is_nonzero`"""
        @overload
        def is_zero(self) -> Any:
            """RealBall.is_zero(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 2165)

            Return ``True`` iff the midpoint and radius of this ball are both zero.

            EXAMPLES::

                sage: RBF = RealBallField()
                sage: RBF(0).is_zero()
                True
                sage: RBF(RIF(-0.5, 0.5)).is_zero()
                False

            .. SEEALSO:: :meth:`is_nonzero`"""
        @overload
        def lambert_w(self) -> Any:
            """RealBall.lambert_w(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3919)

            Return the image of this ball by the Lambert\xa0W function.

            EXAMPLES::

                sage: RBF(1).lambert_w()
                [0.5671432904097...]"""
        @overload
        def lambert_w(self) -> Any:
            """RealBall.lambert_w(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3919)

            Return the image of this ball by the Lambert\xa0W function.

            EXAMPLES::

                sage: RBF(1).lambert_w()
                [0.5671432904097...]"""
        @overload
        def li(self) -> Any:
            """RealBall.li(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3648)

            Logarithmic integral.

            EXAMPLES::

                sage: RBF(3).li()  # abs tol 5e-15
                [2.16358859466719 +/- 4.72e-15]

            TESTS::

                sage: RBF(li(0))                                                            # needs sage.symbolic
                0
                sage: RBF(Li(0))  # abs tol 5e-15                                           # needs sage.symbolic
                [-1.04516378011749 +/- 4.23e-15]"""
        @overload
        def li(self) -> Any:
            """RealBall.li(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3648)

            Logarithmic integral.

            EXAMPLES::

                sage: RBF(3).li()  # abs tol 5e-15
                [2.16358859466719 +/- 4.72e-15]

            TESTS::

                sage: RBF(li(0))                                                            # needs sage.symbolic
                0
                sage: RBF(Li(0))  # abs tol 5e-15                                           # needs sage.symbolic
                [-1.04516378011749 +/- 4.23e-15]"""
        @overload
        def log(self, base=...) -> Any:
            """RealBall.log(self, base=None)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3123)

            Return the logarithm of this ball.

            INPUT:

            - ``base`` -- (optional) positive real ball or number; if ``None``,
              return the natural logarithm ``ln(self)``, otherwise, return the
              general logarithm ``ln(self)/ln(base)``

            EXAMPLES::

                sage: RBF(3).log()
                [1.098612288668110 +/- ...e-16]
                sage: RBF(3).log(2)
                [1.58496250072116 +/- ...e-15]
                sage: log(RBF(5), 2)
                [2.32192809488736 +/- ...e-15]

                sage: RBF(-1/3).log()
                nan
                sage: RBF(3).log(-1)
                nan
                sage: RBF(2).log(0)
                nan"""
        @overload
        def log(self) -> Any:
            """RealBall.log(self, base=None)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3123)

            Return the logarithm of this ball.

            INPUT:

            - ``base`` -- (optional) positive real ball or number; if ``None``,
              return the natural logarithm ``ln(self)``, otherwise, return the
              general logarithm ``ln(self)/ln(base)``

            EXAMPLES::

                sage: RBF(3).log()
                [1.098612288668110 +/- ...e-16]
                sage: RBF(3).log(2)
                [1.58496250072116 +/- ...e-15]
                sage: log(RBF(5), 2)
                [2.32192809488736 +/- ...e-15]

                sage: RBF(-1/3).log()
                nan
                sage: RBF(3).log(-1)
                nan
                sage: RBF(2).log(0)
                nan"""
        @overload
        def log(self) -> Any:
            """RealBall.log(self, base=None)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3123)

            Return the logarithm of this ball.

            INPUT:

            - ``base`` -- (optional) positive real ball or number; if ``None``,
              return the natural logarithm ``ln(self)``, otherwise, return the
              general logarithm ``ln(self)/ln(base)``

            EXAMPLES::

                sage: RBF(3).log()
                [1.098612288668110 +/- ...e-16]
                sage: RBF(3).log(2)
                [1.58496250072116 +/- ...e-15]
                sage: log(RBF(5), 2)
                [2.32192809488736 +/- ...e-15]

                sage: RBF(-1/3).log()
                nan
                sage: RBF(3).log(-1)
                nan
                sage: RBF(2).log(0)
                nan"""
        @overload
        def log1p(self) -> Any:
            """RealBall.log1p(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3161)

            Return ``log(1 + self)``, computed accurately when ``self`` is close to
            zero.

            EXAMPLES::

                sage: eps = RBF(1e-30)
                sage: (1 + eps).log()
                [+/- ...e-16]
                sage: eps.log1p()
                [1.00000000000000e-30 +/- ...e-46]"""
        @overload
        def log1p(self) -> Any:
            """RealBall.log1p(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3161)

            Return ``log(1 + self)``, computed accurately when ``self`` is close to
            zero.

            EXAMPLES::

                sage: eps = RBF(1e-30)
                sage: (1 + eps).log()
                [+/- ...e-16]
                sage: eps.log1p()
                [1.00000000000000e-30 +/- ...e-46]"""
        @overload
        def log_gamma(self) -> Any:
            """RealBall.log_gamma(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3792)

            Return the image of this ball by the logarithmic Gamma function.

            The complex branch structure is assumed, so if ``self <= 0``, the result
            is an indeterminate interval.

            EXAMPLES::

                sage: RBF(1/2).log_gamma()
                [0.572364942924700 +/- ...e-16]"""
        @overload
        def log_gamma(self) -> Any:
            """RealBall.log_gamma(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3792)

            Return the image of this ball by the logarithmic Gamma function.

            The complex branch structure is assumed, so if ``self <= 0``, the result
            is an indeterminate interval.

            EXAMPLES::

                sage: RBF(1/2).log_gamma()
                [0.572364942924700 +/- ...e-16]"""
        def log_integral(self, *args, **kwargs):
            """RealBall.li(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3648)

            Logarithmic integral.

            EXAMPLES::

                sage: RBF(3).li()  # abs tol 5e-15
                [2.16358859466719 +/- 4.72e-15]

            TESTS::

                sage: RBF(li(0))                                                            # needs sage.symbolic
                0
                sage: RBF(Li(0))  # abs tol 5e-15                                           # needs sage.symbolic
                [-1.04516378011749 +/- 4.23e-15]"""
        def log_integral_offset(self, *args, **kwargs):
            """RealBall.Li(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3672)

            Offset logarithmic integral.

            EXAMPLES::

                sage: RBF(3).Li()  # abs tol 5e-15
                [1.11842481454970 +/- 7.61e-15]"""
        @overload
        def lower(self, rnd=...) -> Any:
            """RealBall.lower(self, rnd=None)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 1945)

            Return the right endpoint of this ball, rounded downwards.

            INPUT:

            - ``rnd`` -- string; rounding mode for the parent of the result (does
              not affect its value!), see
              :meth:`sage.rings.real_mpfi.RealIntervalFieldElement.lower`

            OUTPUT: a real number

            EXAMPLES::

                sage: RBF(-1/3).lower()
                -0.333333333333334
                sage: RBF(-1/3).lower().parent()
                Real Field with 53 bits of precision and rounding RNDD

            .. SEEALSO:: :meth:`upper`, :meth:`endpoints`"""
        @overload
        def lower(self) -> Any:
            """RealBall.lower(self, rnd=None)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 1945)

            Return the right endpoint of this ball, rounded downwards.

            INPUT:

            - ``rnd`` -- string; rounding mode for the parent of the result (does
              not affect its value!), see
              :meth:`sage.rings.real_mpfi.RealIntervalFieldElement.lower`

            OUTPUT: a real number

            EXAMPLES::

                sage: RBF(-1/3).lower()
                -0.333333333333334
                sage: RBF(-1/3).lower().parent()
                Real Field with 53 bits of precision and rounding RNDD

            .. SEEALSO:: :meth:`upper`, :meth:`endpoints`"""
        @overload
        def lower(self) -> Any:
            """RealBall.lower(self, rnd=None)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 1945)

            Return the right endpoint of this ball, rounded downwards.

            INPUT:

            - ``rnd`` -- string; rounding mode for the parent of the result (does
              not affect its value!), see
              :meth:`sage.rings.real_mpfi.RealIntervalFieldElement.lower`

            OUTPUT: a real number

            EXAMPLES::

                sage: RBF(-1/3).lower()
                -0.333333333333334
                sage: RBF(-1/3).lower().parent()
                Real Field with 53 bits of precision and rounding RNDD

            .. SEEALSO:: :meth:`upper`, :meth:`endpoints`"""
        @overload
        def max(self, *others) -> Any:
            """RealBall.max(self, *others)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 2475)

            Return a ball containing the maximum of this ball and the
            remaining arguments.

            EXAMPLES::

                sage: RBF(-1, rad=.5).max(0)
                0

                sage: RBF(0, rad=2.).max(RBF(0, rad=1.)).endpoints()
                (-1.00000000465662, 2.00000000651926)

                sage: RBF(-infinity).max(-3, 1/3)
                [0.3333333333333333 +/- ...e-17]

                sage: RBF('nan').max(0)
                nan

            .. SEEALSO:: :meth:`min`

            TESTS::

                sage: RBF(0).max()
                0"""
        @overload
        def max(self) -> Any:
            """RealBall.max(self, *others)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 2475)

            Return a ball containing the maximum of this ball and the
            remaining arguments.

            EXAMPLES::

                sage: RBF(-1, rad=.5).max(0)
                0

                sage: RBF(0, rad=2.).max(RBF(0, rad=1.)).endpoints()
                (-1.00000000465662, 2.00000000651926)

                sage: RBF(-infinity).max(-3, 1/3)
                [0.3333333333333333 +/- ...e-17]

                sage: RBF('nan').max(0)
                nan

            .. SEEALSO:: :meth:`min`

            TESTS::

                sage: RBF(0).max()
                0"""
        @overload
        def mid(self) -> Any:
            """RealBall.mid(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 1718)

            Return the center of this ball.

            EXAMPLES::

                sage: RealBallField(16)(1/3).mid()
                0.3333
                sage: RealBallField(16)(1/3).mid().parent()
                Real Field with 16 bits of precision
                sage: RealBallField(16)(RBF(1/3)).mid().parent()
                Real Field with 53 bits of precision
                sage: RBF('inf').mid()
                +infinity

            ::

                sage: b = RBF(2)^(2^1000)
                sage: b.mid()
                +infinity

            .. SEEALSO:: :meth:`rad`, :meth:`squash`"""
        @overload
        def mid(self) -> Any:
            """RealBall.mid(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 1718)

            Return the center of this ball.

            EXAMPLES::

                sage: RealBallField(16)(1/3).mid()
                0.3333
                sage: RealBallField(16)(1/3).mid().parent()
                Real Field with 16 bits of precision
                sage: RealBallField(16)(RBF(1/3)).mid().parent()
                Real Field with 53 bits of precision
                sage: RBF('inf').mid()
                +infinity

            ::

                sage: b = RBF(2)^(2^1000)
                sage: b.mid()
                +infinity

            .. SEEALSO:: :meth:`rad`, :meth:`squash`"""
        @overload
        def mid(self) -> Any:
            """RealBall.mid(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 1718)

            Return the center of this ball.

            EXAMPLES::

                sage: RealBallField(16)(1/3).mid()
                0.3333
                sage: RealBallField(16)(1/3).mid().parent()
                Real Field with 16 bits of precision
                sage: RealBallField(16)(RBF(1/3)).mid().parent()
                Real Field with 53 bits of precision
                sage: RBF('inf').mid()
                +infinity

            ::

                sage: b = RBF(2)^(2^1000)
                sage: b.mid()
                +infinity

            .. SEEALSO:: :meth:`rad`, :meth:`squash`"""
        @overload
        def mid(self) -> Any:
            """RealBall.mid(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 1718)

            Return the center of this ball.

            EXAMPLES::

                sage: RealBallField(16)(1/3).mid()
                0.3333
                sage: RealBallField(16)(1/3).mid().parent()
                Real Field with 16 bits of precision
                sage: RealBallField(16)(RBF(1/3)).mid().parent()
                Real Field with 53 bits of precision
                sage: RBF('inf').mid()
                +infinity

            ::

                sage: b = RBF(2)^(2^1000)
                sage: b.mid()
                +infinity

            .. SEEALSO:: :meth:`rad`, :meth:`squash`"""
        @overload
        def mid(self) -> Any:
            """RealBall.mid(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 1718)

            Return the center of this ball.

            EXAMPLES::

                sage: RealBallField(16)(1/3).mid()
                0.3333
                sage: RealBallField(16)(1/3).mid().parent()
                Real Field with 16 bits of precision
                sage: RealBallField(16)(RBF(1/3)).mid().parent()
                Real Field with 53 bits of precision
                sage: RBF('inf').mid()
                +infinity

            ::

                sage: b = RBF(2)^(2^1000)
                sage: b.mid()
                +infinity

            .. SEEALSO:: :meth:`rad`, :meth:`squash`"""
        @overload
        def mid(self) -> Any:
            """RealBall.mid(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 1718)

            Return the center of this ball.

            EXAMPLES::

                sage: RealBallField(16)(1/3).mid()
                0.3333
                sage: RealBallField(16)(1/3).mid().parent()
                Real Field with 16 bits of precision
                sage: RealBallField(16)(RBF(1/3)).mid().parent()
                Real Field with 53 bits of precision
                sage: RBF('inf').mid()
                +infinity

            ::

                sage: b = RBF(2)^(2^1000)
                sage: b.mid()
                +infinity

            .. SEEALSO:: :meth:`rad`, :meth:`squash`"""
        @overload
        def min(self, *others) -> Any:
            """RealBall.min(self, *others)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 2438)

            Return a ball containing the minimum of this ball and the
            remaining arguments.

            EXAMPLES::

                sage: RBF(1, rad=.5).min(0)
                0

                sage: RBF(0, rad=2.).min(RBF(0, rad=1.)).endpoints()
                (-2.00000000651926, 1.00000000465662)

                sage: RBF(infinity).min(3, 1/3)
                [0.3333333333333333 +/- ...e-17]

                sage: RBF('nan').min(0)
                nan

            .. SEEALSO:: :meth:`max`

            TESTS::

                sage: RBF(0).min()
                0
                sage: RBF(infinity).min().rad()
                0.00000000"""
        @overload
        def min(self) -> Any:
            """RealBall.min(self, *others)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 2438)

            Return a ball containing the minimum of this ball and the
            remaining arguments.

            EXAMPLES::

                sage: RBF(1, rad=.5).min(0)
                0

                sage: RBF(0, rad=2.).min(RBF(0, rad=1.)).endpoints()
                (-2.00000000651926, 1.00000000465662)

                sage: RBF(infinity).min(3, 1/3)
                [0.3333333333333333 +/- ...e-17]

                sage: RBF('nan').min(0)
                nan

            .. SEEALSO:: :meth:`max`

            TESTS::

                sage: RBF(0).min()
                0
                sage: RBF(infinity).min().rad()
                0.00000000"""
        @overload
        def min(self) -> Any:
            """RealBall.min(self, *others)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 2438)

            Return a ball containing the minimum of this ball and the
            remaining arguments.

            EXAMPLES::

                sage: RBF(1, rad=.5).min(0)
                0

                sage: RBF(0, rad=2.).min(RBF(0, rad=1.)).endpoints()
                (-2.00000000651926, 1.00000000465662)

                sage: RBF(infinity).min(3, 1/3)
                [0.3333333333333333 +/- ...e-17]

                sage: RBF('nan').min(0)
                nan

            .. SEEALSO:: :meth:`max`

            TESTS::

                sage: RBF(0).min()
                0
                sage: RBF(infinity).min().rad()
                0.00000000"""
        @overload
        def nbits(self) -> Any:
            """RealBall.nbits(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 2031)

            Return the minimum precision sufficient to represent this ball exactly.

            In other words, return the number of bits needed to represent the
            absolute value of the mantissa of the midpoint of this ball. The result
            is 0 if the midpoint is a special value.

            EXAMPLES::

                sage: RBF(1/3).nbits()
                53
                sage: RBF(1023, .1).nbits()
                10
                sage: RBF(1024, .1).nbits()
                1
                sage: RBF(0).nbits()
                0
                sage: RBF(infinity).nbits()
                0"""
        @overload
        def nbits(self) -> Any:
            """RealBall.nbits(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 2031)

            Return the minimum precision sufficient to represent this ball exactly.

            In other words, return the number of bits needed to represent the
            absolute value of the mantissa of the midpoint of this ball. The result
            is 0 if the midpoint is a special value.

            EXAMPLES::

                sage: RBF(1/3).nbits()
                53
                sage: RBF(1023, .1).nbits()
                10
                sage: RBF(1024, .1).nbits()
                1
                sage: RBF(0).nbits()
                0
                sage: RBF(infinity).nbits()
                0"""
        @overload
        def nbits(self) -> Any:
            """RealBall.nbits(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 2031)

            Return the minimum precision sufficient to represent this ball exactly.

            In other words, return the number of bits needed to represent the
            absolute value of the mantissa of the midpoint of this ball. The result
            is 0 if the midpoint is a special value.

            EXAMPLES::

                sage: RBF(1/3).nbits()
                53
                sage: RBF(1023, .1).nbits()
                10
                sage: RBF(1024, .1).nbits()
                1
                sage: RBF(0).nbits()
                0
                sage: RBF(infinity).nbits()
                0"""
        @overload
        def nbits(self) -> Any:
            """RealBall.nbits(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 2031)

            Return the minimum precision sufficient to represent this ball exactly.

            In other words, return the number of bits needed to represent the
            absolute value of the mantissa of the midpoint of this ball. The result
            is 0 if the midpoint is a special value.

            EXAMPLES::

                sage: RBF(1/3).nbits()
                53
                sage: RBF(1023, .1).nbits()
                10
                sage: RBF(1024, .1).nbits()
                1
                sage: RBF(0).nbits()
                0
                sage: RBF(infinity).nbits()
                0"""
        @overload
        def nbits(self) -> Any:
            """RealBall.nbits(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 2031)

            Return the minimum precision sufficient to represent this ball exactly.

            In other words, return the number of bits needed to represent the
            absolute value of the mantissa of the midpoint of this ball. The result
            is 0 if the midpoint is a special value.

            EXAMPLES::

                sage: RBF(1/3).nbits()
                53
                sage: RBF(1023, .1).nbits()
                10
                sage: RBF(1024, .1).nbits()
                1
                sage: RBF(0).nbits()
                0
                sage: RBF(infinity).nbits()
                0"""
        @overload
        def nbits(self) -> Any:
            """RealBall.nbits(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 2031)

            Return the minimum precision sufficient to represent this ball exactly.

            In other words, return the number of bits needed to represent the
            absolute value of the mantissa of the midpoint of this ball. The result
            is 0 if the midpoint is a special value.

            EXAMPLES::

                sage: RBF(1/3).nbits()
                53
                sage: RBF(1023, .1).nbits()
                10
                sage: RBF(1024, .1).nbits()
                1
                sage: RBF(0).nbits()
                0
                sage: RBF(infinity).nbits()
                0"""
        def overlaps(self, RealBallother) -> Any:
            """RealBall.overlaps(self, RealBall other)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 2547)

            Return ``True`` iff ``self`` and ``other`` have some point in common.

            If either ``self`` or ``other`` contains NaN, this method always
            returns nonzero (as a NaN could be anything, it could in particular
            contain any number that is included in the other operand).

            EXAMPLES::

                sage: RBF(pi).overlaps(RBF(pi) + 2**(-100))                                 # needs sage.symbolic
                True
                sage: RBF(pi).overlaps(RBF(3))                                              # needs sage.symbolic
                False"""
        def polylog(self, s) -> Any:
            """RealBall.polylog(self, s)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3934)

            Return the polylogarithm `\\operatorname{Li}_s(\\mathrm{self})`.

            EXAMPLES::

                sage: polylog(0, -1)                                                        # needs sage.symbolic
                -1/2
                sage: RBF(-1).polylog(0)
                [-0.50000000000000 +/- ...e-16]
                sage: polylog(1, 1/2)                                                       # needs sage.symbolic
                -log(1/2)
                sage: RBF(1/2).polylog(1)
                [0.69314718055995 +/- ...e-15]
                sage: RBF(1/3).polylog(1/2)
                [0.44210883528067 +/- 6.7...e-15]
                sage: RBF(1/3).polylog(RLF(pi))                                             # needs sage.symbolic
                [0.34728895057225 +/- ...e-15]

            TESTS::

                sage: RBF(1/3).polylog(2r)
                [0.366213229977063 +/- ...e-16]"""
        @overload
        def psi(self) -> RealBall:
            """RealBall.psi(self) -> RealBall

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3850)

            Compute the digamma function with argument ``self``.

            EXAMPLES::

                sage: RBF(1).psi() # abs tol 1e-15
                [-0.5772156649015329 +/- 4.84e-17]"""
        @overload
        def psi(self) -> Any:
            """RealBall.psi(self) -> RealBall

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3850)

            Compute the digamma function with argument ``self``.

            EXAMPLES::

                sage: RBF(1).psi() # abs tol 1e-15
                [-0.5772156649015329 +/- 4.84e-17]"""
        @overload
        def rad(self) -> Any:
            """RealBall.rad(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 1749)

            Return the radius of this ball.

            EXAMPLES::

                sage: RBF(1/3).rad()
                5.5511151e-17
                sage: RBF(1/3).rad().parent()
                Real Field with 30 bits of precision

            .. SEEALSO:: :meth:`mid`, :meth:`rad_as_ball`, :meth:`diameter`

            TESTS::

                sage: (RBF(1, rad=.1) << (2^64)).rad()
                Traceback (most recent call last):
                ...
                RuntimeError: unable to convert the radius to MPFR (exponent out of range?)"""
        @overload
        def rad(self) -> Any:
            """RealBall.rad(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 1749)

            Return the radius of this ball.

            EXAMPLES::

                sage: RBF(1/3).rad()
                5.5511151e-17
                sage: RBF(1/3).rad().parent()
                Real Field with 30 bits of precision

            .. SEEALSO:: :meth:`mid`, :meth:`rad_as_ball`, :meth:`diameter`

            TESTS::

                sage: (RBF(1, rad=.1) << (2^64)).rad()
                Traceback (most recent call last):
                ...
                RuntimeError: unable to convert the radius to MPFR (exponent out of range?)"""
        @overload
        def rad(self) -> Any:
            """RealBall.rad(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 1749)

            Return the radius of this ball.

            EXAMPLES::

                sage: RBF(1/3).rad()
                5.5511151e-17
                sage: RBF(1/3).rad().parent()
                Real Field with 30 bits of precision

            .. SEEALSO:: :meth:`mid`, :meth:`rad_as_ball`, :meth:`diameter`

            TESTS::

                sage: (RBF(1, rad=.1) << (2^64)).rad()
                Traceback (most recent call last):
                ...
                RuntimeError: unable to convert the radius to MPFR (exponent out of range?)"""
        @overload
        def rad(self) -> Any:
            """RealBall.rad(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 1749)

            Return the radius of this ball.

            EXAMPLES::

                sage: RBF(1/3).rad()
                5.5511151e-17
                sage: RBF(1/3).rad().parent()
                Real Field with 30 bits of precision

            .. SEEALSO:: :meth:`mid`, :meth:`rad_as_ball`, :meth:`diameter`

            TESTS::

                sage: (RBF(1, rad=.1) << (2^64)).rad()
                Traceback (most recent call last):
                ...
                RuntimeError: unable to convert the radius to MPFR (exponent out of range?)"""
        @overload
        def rad_as_ball(self) -> Any:
            """RealBall.rad_as_ball(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 1821)

            Return an exact ball with center equal to the radius of this ball.

            EXAMPLES::

                sage: rad = RBF(1/3).rad_as_ball()
                sage: rad
                [5.55111512e-17 +/- ...e-26]
                sage: rad.is_exact()
                True
                sage: rad.parent()
                Real ball field with 30 bits of precision

            .. SEEALSO:: :meth:`squash`, :meth:`rad`"""
        @overload
        def rad_as_ball(self) -> Any:
            """RealBall.rad_as_ball(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 1821)

            Return an exact ball with center equal to the radius of this ball.

            EXAMPLES::

                sage: rad = RBF(1/3).rad_as_ball()
                sage: rad
                [5.55111512e-17 +/- ...e-26]
                sage: rad.is_exact()
                True
                sage: rad.parent()
                Real ball field with 30 bits of precision

            .. SEEALSO:: :meth:`squash`, :meth:`rad`"""
        @overload
        def real(self) -> Any:
            """RealBall.real(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 2007)

            Return the real part of this ball.

            EXAMPLES::

                sage: RBF(1/3).real()
                [0.3333333333333333 +/- 7.04e-17]"""
        @overload
        def real(self) -> Any:
            """RealBall.real(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 2007)

            Return the real part of this ball.

            EXAMPLES::

                sage: RBF(1/3).real()
                [0.3333333333333333 +/- 7.04e-17]"""
        @overload
        def rgamma(self) -> Any:
            """RealBall.rgamma(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3810)

            Return the image of this ball by the function 1/Γ, avoiding division by
            zero at the poles of the gamma function.

            EXAMPLES::

                sage: RBF(-1).rgamma()
                0
                sage: RBF(3).rgamma()
                0.5000000000000000"""
        @overload
        def rgamma(self) -> Any:
            """RealBall.rgamma(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3810)

            Return the image of this ball by the function 1/Γ, avoiding division by
            zero at the poles of the gamma function.

            EXAMPLES::

                sage: RBF(-1).rgamma()
                0
                sage: RBF(3).rgamma()
                0.5000000000000000"""
        @overload
        def rgamma(self) -> Any:
            """RealBall.rgamma(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3810)

            Return the image of this ball by the function 1/Γ, avoiding division by
            zero at the poles of the gamma function.

            EXAMPLES::

                sage: RBF(-1).rgamma()
                0
                sage: RBF(3).rgamma()
                0.5000000000000000"""
        def rising_factorial(self, n) -> Any:
            """RealBall.rising_factorial(self, n)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3828)

            Return the ``n``-th rising factorial of this ball.

            The `n`-th rising factorial of `x` is equal to `x (x+1) \\cdots (x+n-1)`.

            For real `n`, it is a quotient of gamma functions.

            EXAMPLES::

                sage: RBF(1).rising_factorial(5)
                120.0000000000000
                sage: RBF(1/2).rising_factorial(1/3) # abs tol 1e-14
                [0.636849884317974 +/- 8.98e-16]"""
        def round(self) -> Any:
            """RealBall.round(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 2054)

            Return a copy of this ball with center rounded to the precision of the
            parent.

            EXAMPLES:

            It is possible to create balls whose midpoint is more precise than
            their parent's nominal precision (see :mod:`~sage.rings.real_arb` for
            more information)::

                sage: b = RBF(pi.n(100))                                                    # needs sage.symbolic
                sage: b.mid()                                                               # needs sage.symbolic
                3.141592653589793238462643383

            The ``round()`` method rounds such a ball to its parent's precision::

                sage: b.round().mid()                                                       # needs sage.symbolic
                3.14159265358979

            .. SEEALSO:: :meth:`trim`"""
        @overload
        def rsqrt(self) -> Any:
            """RealBall.rsqrt(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 2956)

            Return the reciprocal square root of ``self``.

            At high precision, this is faster than computing a square root.

            EXAMPLES::

                sage: RBF(2).rsqrt()
                [0.707106781186547 +/- ...e-16]
                sage: RBF(0).rsqrt()
                nan"""
        @overload
        def rsqrt(self) -> Any:
            """RealBall.rsqrt(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 2956)

            Return the reciprocal square root of ``self``.

            At high precision, this is faster than computing a square root.

            EXAMPLES::

                sage: RBF(2).rsqrt()
                [0.707106781186547 +/- ...e-16]
                sage: RBF(0).rsqrt()
                nan"""
        @overload
        def rsqrt(self) -> Any:
            """RealBall.rsqrt(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 2956)

            Return the reciprocal square root of ``self``.

            At high precision, this is faster than computing a square root.

            EXAMPLES::

                sage: RBF(2).rsqrt()
                [0.707106781186547 +/- ...e-16]
                sage: RBF(0).rsqrt()
                nan"""
        @overload
        def sec(self) -> Any:
            """RealBall.sec(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3282)

            Return the secant of this ball.

            EXAMPLES::

                sage: RBF(1).sec()
                [1.850815717680925 +/- ...e-16]"""
        @overload
        def sec(self) -> Any:
            """RealBall.sec(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3282)

            Return the secant of this ball.

            EXAMPLES::

                sage: RBF(1).sec()
                [1.850815717680925 +/- ...e-16]"""
        @overload
        def sech(self) -> Any:
            """RealBall.sech(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3423)

            Return the hyperbolic secant of this ball.

            EXAMPLES::

                sage: RBF(1).sech()
                [0.648054273663885 +/- ...e-16]"""
        @overload
        def sech(self) -> Any:
            """RealBall.sech(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3423)

            Return the hyperbolic secant of this ball.

            EXAMPLES::

                sage: RBF(1).sech()
                [0.648054273663885 +/- ...e-16]"""
        @overload
        def sin(self) -> Any:
            """RealBall.sin(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3214)

            Return the sine of this ball.

            EXAMPLES::

                sage: RBF(pi).sin()                                                         # needs sage.symbolic
                [+/- ...e-16]

            .. SEEALSO:: :meth:`~sage.rings.real_arb.RealBallField.sinpi`"""
        @overload
        def sin(self) -> Any:
            """RealBall.sin(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3214)

            Return the sine of this ball.

            EXAMPLES::

                sage: RBF(pi).sin()                                                         # needs sage.symbolic
                [+/- ...e-16]

            .. SEEALSO:: :meth:`~sage.rings.real_arb.RealBallField.sinpi`"""
        def sin_integral(self, *args, **kwargs):
            """RealBall.Si(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3560)

            Sine integral.

            EXAMPLES::

                sage: RBF(1).Si() # abs tol 1e-15
                [0.946083070367183 +/- 9.22e-16]

            TESTS::

                sage: RBF(Si(1))  # abs tol 1e-15                                           # needs sage.symbolic
                [0.946083070367183 +/- 9.22e-16]"""
        @overload
        def sinh(self) -> Any:
            """RealBall.sinh(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3361)

            Return the hyperbolic sine of this ball.

            EXAMPLES::

                sage: RBF(1).sinh()
                [1.175201193643801 +/- ...e-16]"""
        @overload
        def sinh(self) -> Any:
            """RealBall.sinh(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3361)

            Return the hyperbolic sine of this ball.

            EXAMPLES::

                sage: RBF(1).sinh()
                [1.175201193643801 +/- ...e-16]"""
        def sinh_integral(self, *args, **kwargs):
            """RealBall.Shi(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3604)

            Hyperbolic sine integral.

            EXAMPLES::

                sage: RBF(1).Shi() # abs tol 5e-15
                [1.05725087537573 +/- 2.77e-15]

            TESTS::

                sage: RBF(Shi(1))  # abs tol 5e-15                                          # needs sage.symbolic
                [1.05725087537573 +/- 2.77e-15]"""
        @overload
        def sqrt(self) -> Any:
            """RealBall.sqrt(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 2917)

            Return the square root of this ball.

            EXAMPLES::

                sage: RBF(2).sqrt()
                [1.414213562373095 +/- ...e-16]
                sage: RBF(-1/3).sqrt()
                nan"""
        @overload
        def sqrt(self) -> Any:
            """RealBall.sqrt(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 2917)

            Return the square root of this ball.

            EXAMPLES::

                sage: RBF(2).sqrt()
                [1.414213562373095 +/- ...e-16]
                sage: RBF(-1/3).sqrt()
                nan"""
        @overload
        def sqrt(self) -> Any:
            """RealBall.sqrt(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 2917)

            Return the square root of this ball.

            EXAMPLES::

                sage: RBF(2).sqrt()
                [1.414213562373095 +/- ...e-16]
                sage: RBF(-1/3).sqrt()
                nan"""
        def sqrt1pm1(self) -> Any:
            """RealBall.sqrt1pm1(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 2975)

            Return `\\sqrt{1+\\mathrm{self}}-1`, computed accurately when ``self`` is
            close to zero.

            EXAMPLES::

                sage: eps = RBF(10^(-20))
                sage: (1 + eps).sqrt() - 1
                [+/- ...e-16]
                sage: eps.sqrt1pm1()
                [5.00000000000000e-21 +/- ...e-36]"""
        @overload
        def sqrtpos(self) -> Any:
            """RealBall.sqrtpos(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 2934)

            Return the square root of this ball, assuming that it represents a
            nonnegative number.

            Any negative numbers in the input interval are discarded.

            EXAMPLES::

                sage: RBF(2).sqrtpos()
                [1.414213562373095 +/- ...e-16]
                sage: RBF(-1/3).sqrtpos()
                0
                sage: RBF(0, rad=2.r).sqrtpos()
                [+/- 1.42]"""
        @overload
        def sqrtpos(self) -> Any:
            """RealBall.sqrtpos(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 2934)

            Return the square root of this ball, assuming that it represents a
            nonnegative number.

            Any negative numbers in the input interval are discarded.

            EXAMPLES::

                sage: RBF(2).sqrtpos()
                [1.414213562373095 +/- ...e-16]
                sage: RBF(-1/3).sqrtpos()
                0
                sage: RBF(0, rad=2.r).sqrtpos()
                [+/- 1.42]"""
        @overload
        def sqrtpos(self) -> Any:
            """RealBall.sqrtpos(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 2934)

            Return the square root of this ball, assuming that it represents a
            nonnegative number.

            Any negative numbers in the input interval are discarded.

            EXAMPLES::

                sage: RBF(2).sqrtpos()
                [1.414213562373095 +/- ...e-16]
                sage: RBF(-1/3).sqrtpos()
                0
                sage: RBF(0, rad=2.r).sqrtpos()
                [+/- 1.42]"""
        @overload
        def sqrtpos(self) -> Any:
            """RealBall.sqrtpos(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 2934)

            Return the square root of this ball, assuming that it represents a
            nonnegative number.

            Any negative numbers in the input interval are discarded.

            EXAMPLES::

                sage: RBF(2).sqrtpos()
                [1.414213562373095 +/- ...e-16]
                sage: RBF(-1/3).sqrtpos()
                0
                sage: RBF(0, rad=2.r).sqrtpos()
                [+/- 1.42]"""
        @overload
        def squash(self) -> Any:
            """RealBall.squash(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 1800)

            Return an exact ball with the same center as this ball.

            EXAMPLES::

                sage: mid = RealBallField(16)(1/3).squash()
                sage: mid
                [0.3333 +/- ...e-5]
                sage: mid.is_exact()
                True
                sage: mid.parent()
                Real ball field with 16 bits of precision

            .. SEEALSO:: :meth:`mid`, :meth:`rad_as_ball`"""
        @overload
        def squash(self) -> Any:
            """RealBall.squash(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 1800)

            Return an exact ball with the same center as this ball.

            EXAMPLES::

                sage: mid = RealBallField(16)(1/3).squash()
                sage: mid
                [0.3333 +/- ...e-5]
                sage: mid.is_exact()
                True
                sage: mid.parent()
                Real ball field with 16 bits of precision

            .. SEEALSO:: :meth:`mid`, :meth:`rad_as_ball`"""
        @overload
        def tan(self) -> Any:
            """RealBall.tan(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3248)

            Return the tangent of this ball.

            EXAMPLES::

                sage: RBF(1).tan()
                [1.557407724654902 +/- ...e-16]
                sage: RBF(pi/2).tan()                                                       # needs sage.symbolic
                nan"""
        @overload
        def tan(self) -> Any:
            """RealBall.tan(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3248)

            Return the tangent of this ball.

            EXAMPLES::

                sage: RBF(1).tan()
                [1.557407724654902 +/- ...e-16]
                sage: RBF(pi/2).tan()                                                       # needs sage.symbolic
                nan"""
        @overload
        def tan(self) -> Any:
            """RealBall.tan(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3248)

            Return the tangent of this ball.

            EXAMPLES::

                sage: RBF(1).tan()
                [1.557407724654902 +/- ...e-16]
                sage: RBF(pi/2).tan()                                                       # needs sage.symbolic
                nan"""
        @overload
        def tanh(self) -> Any:
            """RealBall.tanh(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3391)

            Return the hyperbolic tangent of this ball.

            EXAMPLES::

                sage: RBF(1).tanh()
                [0.761594155955765 +/- ...e-16]"""
        @overload
        def tanh(self) -> Any:
            """RealBall.tanh(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3391)

            Return the hyperbolic tangent of this ball.

            EXAMPLES::

                sage: RBF(1).tanh()
                [0.761594155955765 +/- ...e-16]"""
        @overload
        def trim(self) -> Any:
            """RealBall.trim(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 2104)

            Return a trimmed copy of this ball.

            Round ``self`` to a number of bits equal to the :meth:`accuracy` of
            ``self`` (as indicated by its radius), plus a few guard bits. The
            resulting ball is guaranteed to contain ``self``, but is more economical
            if ``self`` has less than full accuracy.

            EXAMPLES::

                sage: b = RBF(0.11111111111111, rad=.001)
                sage: b.mid()
                0.111111111111110
                sage: b.trim().mid()
                0.111111104488373

            .. SEEALSO:: :meth:`round`"""
        @overload
        def trim(self) -> Any:
            """RealBall.trim(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 2104)

            Return a trimmed copy of this ball.

            Round ``self`` to a number of bits equal to the :meth:`accuracy` of
            ``self`` (as indicated by its radius), plus a few guard bits. The
            resulting ball is guaranteed to contain ``self``, but is more economical
            if ``self`` has less than full accuracy.

            EXAMPLES::

                sage: b = RBF(0.11111111111111, rad=.001)
                sage: b.mid()
                0.111111111111110
                sage: b.trim().mid()
                0.111111104488373

            .. SEEALSO:: :meth:`round`"""
        def union(self, other) -> Any:
            """RealBall.union(self, other)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 1991)

            Return a ball containing the convex hull of ``self`` and ``other``.

            EXAMPLES::

                sage: RBF(0).union(1).endpoints()
                (-9.31322574615479e-10, 1.00000000093133)"""
        @overload
        def upper(self, rnd=...) -> Any:
            """RealBall.upper(self, rnd=None)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 1919)

            Return the right endpoint of this ball, rounded upwards.

            INPUT:

            - ``rnd`` -- string; rounding mode for the parent of the result (does
              not affect its value!), see
              :meth:`sage.rings.real_mpfi.RealIntervalFieldElement.upper`

            OUTPUT: a real number

            EXAMPLES::

                sage: RBF(-1/3).upper()
                -0.333333333333333
                sage: RBF(-1/3).upper().parent()
                Real Field with 53 bits of precision and rounding RNDU

            .. SEEALSO::

               :meth:`lower`, :meth:`endpoints`"""
        @overload
        def upper(self) -> Any:
            """RealBall.upper(self, rnd=None)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 1919)

            Return the right endpoint of this ball, rounded upwards.

            INPUT:

            - ``rnd`` -- string; rounding mode for the parent of the result (does
              not affect its value!), see
              :meth:`sage.rings.real_mpfi.RealIntervalFieldElement.upper`

            OUTPUT: a real number

            EXAMPLES::

                sage: RBF(-1/3).upper()
                -0.333333333333333
                sage: RBF(-1/3).upper().parent()
                Real Field with 53 bits of precision and rounding RNDU

            .. SEEALSO::

               :meth:`lower`, :meth:`endpoints`"""
        @overload
        def upper(self) -> Any:
            """RealBall.upper(self, rnd=None)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 1919)

            Return the right endpoint of this ball, rounded upwards.

            INPUT:

            - ``rnd`` -- string; rounding mode for the parent of the result (does
              not affect its value!), see
              :meth:`sage.rings.real_mpfi.RealIntervalFieldElement.upper`

            OUTPUT: a real number

            EXAMPLES::

                sage: RBF(-1/3).upper()
                -0.333333333333333
                sage: RBF(-1/3).upper().parent()
                Real Field with 53 bits of precision and rounding RNDU

            .. SEEALSO::

               :meth:`lower`, :meth:`endpoints`"""
        @overload
        def zeta(self, a=...) -> Any:
            """RealBall.zeta(self, a=None)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3866)

            Return the image of this ball by the Hurwitz zeta function.

            For ``a = 1`` (or ``a = None``), this computes the Riemann zeta function.

            Otherwise, it computes the Hurwitz zeta function.

            Use :meth:`RealBallField.zeta` to compute the Riemann zeta function of
            a small integer without first converting it to a real ball.

            EXAMPLES::

                sage: RBF(-1).zeta()
                [-0.0833333333333333 +/- ...e-17]
                sage: RBF(-1).zeta(1)
                [-0.0833333333333333 +/- ...e-17]
                sage: RBF(-1).zeta(2)
                [-1.083333333333333 +/- ...e-16]"""
        @overload
        def zeta(self) -> Any:
            """RealBall.zeta(self, a=None)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3866)

            Return the image of this ball by the Hurwitz zeta function.

            For ``a = 1`` (or ``a = None``), this computes the Riemann zeta function.

            Otherwise, it computes the Hurwitz zeta function.

            Use :meth:`RealBallField.zeta` to compute the Riemann zeta function of
            a small integer without first converting it to a real ball.

            EXAMPLES::

                sage: RBF(-1).zeta()
                [-0.0833333333333333 +/- ...e-17]
                sage: RBF(-1).zeta(1)
                [-0.0833333333333333 +/- ...e-17]
                sage: RBF(-1).zeta(2)
                [-1.083333333333333 +/- ...e-16]"""
        def zetaderiv(self, k) -> Any:
            """RealBall.zetaderiv(self, k)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3899)

            Return the image of this ball by the `k`-th derivative of the Riemann
            zeta function.

            For a more flexible interface, see the low-level method
            ``_zeta_series`` of polynomials with complex ball coefficients.

            EXAMPLES::

                sage: RBF(1/2).zetaderiv(1)
                [-3.92264613920915...]
                sage: RBF(2).zetaderiv(3)
                [-6.0001458028430...]"""
        def __abs__(self) -> Any:
            """RealBall.__abs__(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 1842)

            Return the absolute value of this ball.

            EXAMPLES::

                sage: RBF(-1/3).abs() # indirect doctest
                [0.3333333333333333 +/- ...e-17]
                sage: abs(RBF(-1))
                1.000000000000000"""
        def __bool__(self) -> bool:
            """True if self else False"""
        def __complex__(self) -> Any:
            """RealBall.__complex__(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 1705)

            Convert ``self`` to a ``complex``.

            EXAMPLES::

                sage: complex(RBF(1))
                (1+0j)"""
        def __contains__(self, other) -> Any:
            """RealBall.__contains__(self, other)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 2629)

            Return ``True`` if ``other`` can be verified to be contained in ``self``.

            The test is done using interval arithmetic with a precision determined
            by the parent of ``self`` and may return false negatives.

            EXAMPLES::

                sage: sqrt(2) in RBF(sqrt(2))                                               # needs sage.symbolic
                True

            A false negative::

                sage: sqrt(2) in RBF(RealBallField(100)(sqrt(2)))                           # needs sage.symbolic
                False

            .. SEEALSO:: :meth:`contains_exact`"""
        def __float__(self) -> Any:
            """RealBall.__float__(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 1694)

            Convert ``self`` to a ``float``.

            EXAMPLES::

                sage: float(RBF(1))
                1.0"""
        def __hash__(self) -> Any:
            """RealBall.__hash__(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 1492)

            TESTS::

                sage: hash(RealBallField(10)(1)) == hash(RealBallField(20)(1))
                True
                sage: hash(RBF(1/3)) == hash(RBF(1/3, rad=.1))
                False
                sage: vals = [0, 1, 3/4, 5/8, 7/8, infinity, 'nan', 2^1000 - 1]
                sage: len({hash(RBF(v)) for v in vals}) == len(vals)
                True"""
        def __invert__(self) -> Any:
            """RealBall.__invert__(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 2764)

            Return the inverse of this ball.

            The result is guaranteed to contain the inverse of any point of the
            input ball.

            EXAMPLES::

                sage: ~RBF(5)
                [0.2000000000000000 +/- ...e-17]
                sage: ~RBF(0)
                nan
                sage: RBF(RIF(-0.1,0.1))
                [+/- 0.101]"""
        def __lshift__(self, val, shift) -> Any:
            '''RealBall.__lshift__(val, shift)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3026)

            If ``val`` is a ``RealBall`` and ``shift`` is an integer, return the
            ball obtained by shifting the center and radius of ``val`` to the left
            by ``shift`` bits.

            INPUT:

            - ``shift`` -- integer; may be negative

            EXAMPLES::

                sage: RBF(1/3) << 2 # indirect doctest
                [1.333333333333333 +/- ...e-16]
                sage: RBF(1) << -1
                0.5000000000000000

            TESTS::

                sage: RBF(1) << (2^100)
                [2.285367694229514e+381600854690147056244358827360 +/- ...e+381600854690147056244358827344]
                sage: RBF(1) << (-2^100)
                [4.375663498372584e-381600854690147056244358827361 +/- ...e-381600854690147056244358827378]

                sage: "a" << RBF(1/3)
                Traceback (most recent call last):
                ...
                TypeError: unsupported operand type(s) for <<: \'str\' and \'RealBall\'
                sage: RBF(1) << RBF(1/3)
                Traceback (most recent call last):
                ...
                TypeError: shift should be an integer'''
        def __neg__(self) -> Any:
            """RealBall.__neg__(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 2751)

            Return the opposite of this ball.

            EXAMPLES::

                sage: -RBF(1/3)
                [-0.3333333333333333 +/- ...e-17]"""
        def __pow__(self, base, expo, _) -> Any:
            """RealBall.__pow__(base, expo, _)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 2863)

            EXAMPLES::

                sage: # needs sage.symbolic
                sage: RBF(e)^17
                [24154952.7535753 +/- ...e-8]
                sage: RBF(e)^(-1)
                [0.367879441171442 +/- ...e-16]
                sage: RBF(e)^(1/2)
                [1.648721270700128 +/- ...e-16]
                sage: RBF(e)^RBF(pi)
                [23.1406926327793 +/- ...e-14]

            ::

                sage: RBF(-1)^(1/3)
                nan
                sage: RBF(0)^(-1)
                nan
                sage: RBF(-e)**RBF(pi)                                                      # needs sage.symbolic
                nan

            TESTS::

                sage: RBF(e)**(2r)                                                          # needs sage.symbolic
                [7.38905609893065 +/- ...e-15]
                sage: RBF(e)**(-1r)                                                         # needs sage.symbolic
                [0.367879441171442 +/- ...e-16]"""
        def __reduce__(self) -> Any:
            """RealBall.__reduce__(self)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 1539)

            Serialize a RealBall.

            TESTS::

                sage: [loads(dumps(b)).identical(b)
                ....:  for b in [RealBallField(60).pi(), RBF(infinity)]]
                [True, True]
                sage: b = RBF(NaN); loads(dumps(b)).identical(b)                            # needs sage.symbolic
                True"""
        def __rlshift__(self, other):
            """Return value<<self."""
        def __rpow__(self, other):
            """Return pow(value, self, mod)."""
        def __rrshift__(self, other):
            """Return value>>self."""
        def __rshift__(self, val, shift) -> Any:
            '''RealBall.__rshift__(val, shift)

            File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 3079)

            If ``val`` is a ``RealBall`` and ``shift`` is an integer, return the
            ball obtained by shifting the center and radius of ``val`` to the right
            by ``shift`` bits.

            INPUT:

            - ``shift`` -- integer; may be negative

            EXAMPLES::

                sage: RBF(4) >> 2
                1.000000000000000
                sage: RBF(1/3) >> -2
                [1.333333333333333 +/- ...e-16]

            TESTS::

                sage: "a" >> RBF(1/3)
                Traceback (most recent call last):
                ...
                TypeError: unsupported operand type(s) for >>: \'str\' and \'RealBall\''''
    def __init__(self, longprecision=...) -> Any:
        """RealBallField.__init__(self, long precision=53)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 392)

        Initialize the real ball field.

        INPUT:

        - ``precision`` -- integer `\\ge 2`

        EXAMPLES::

            sage: RBF = RealBallField()
            sage: RBF(1)
            1.000000000000000
            sage: RealBallField(0)
            Traceback (most recent call last):
            ...
            ValueError: precision must be at least 2
            sage: RealBallField(1)
            Traceback (most recent call last):
            ...
            ValueError: precision must be at least 2

        TESTS::

            sage: RBF.base()
            Real ball field with 53 bits of precision
            sage: RBF.base_ring()
            Real ball field with 53 bits of precision"""
    def algebraic_closure(self) -> Any:
        """RealBallField.complex_field(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 611)

        Return the complex ball field with the same precision.

        EXAMPLES::

            sage: from sage.rings.complex_arb import ComplexBallField
            sage: RBF.complex_field()
            Complex ball field with 53 bits of precision
            sage: RealBallField(3).algebraic_closure()
            Complex ball field with 3 bits of precision"""
    @overload
    def bell_number(self, n) -> Any:
        """RealBallField.bell_number(self, n)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 1058)

        Return a ball enclosing the ``n``-th Bell number.

        EXAMPLES::

            sage: [RBF.bell_number(n) for n in range(7)]
            [1.000000000000000,
             1.000000000000000,
             2.000000000000000,
             5.000000000000000,
             15.00000000000000,
             52.00000000000000,
             203.0000000000000]
            sage: RBF.bell_number(-1)
            Traceback (most recent call last):
            ...
            ValueError: expected a nonnegative index
            sage: RBF.bell_number(10**20)
            [5.38270113176282e+1794956117137290721328 +/- ...e+1794956117137290721313]"""
    @overload
    def bell_number(self, n) -> Any:
        """RealBallField.bell_number(self, n)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 1058)

        Return a ball enclosing the ``n``-th Bell number.

        EXAMPLES::

            sage: [RBF.bell_number(n) for n in range(7)]
            [1.000000000000000,
             1.000000000000000,
             2.000000000000000,
             5.000000000000000,
             15.00000000000000,
             52.00000000000000,
             203.0000000000000]
            sage: RBF.bell_number(-1)
            Traceback (most recent call last):
            ...
            ValueError: expected a nonnegative index
            sage: RBF.bell_number(10**20)
            [5.38270113176282e+1794956117137290721328 +/- ...e+1794956117137290721313]"""
    @overload
    def bernoulli(self, n) -> Any:
        """RealBallField.bernoulli(self, n)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 984)

        Return a ball enclosing the ``n``-th Bernoulli number.

        EXAMPLES::

            sage: [RBF.bernoulli(n) for n in range(4)]
            [1.000000000000000, -0.5000000000000000, [0.1666666666666667 +/- ...e-17], 0]
            sage: RBF.bernoulli(2**20)
            [-1.823002872104961e+5020717 +/- ...e+5020701]
            sage: RBF.bernoulli(2**1000)
            Traceback (most recent call last):
            ...
            ValueError: argument too large

        TESTS::

            sage: RBF.bernoulli(2r)
            [0.1666666666666667 +/- ...e-17]
            sage: RBF.bernoulli(2/3)
            Traceback (most recent call last):
            ...
            TypeError: no canonical coercion from Rational Field to Integer Ring
            sage: RBF.bernoulli(-1)
            Traceback (most recent call last):
            ...
            ValueError: expected a nonnegative index"""
    @overload
    def bernoulli(self, n) -> Any:
        """RealBallField.bernoulli(self, n)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 984)

        Return a ball enclosing the ``n``-th Bernoulli number.

        EXAMPLES::

            sage: [RBF.bernoulli(n) for n in range(4)]
            [1.000000000000000, -0.5000000000000000, [0.1666666666666667 +/- ...e-17], 0]
            sage: RBF.bernoulli(2**20)
            [-1.823002872104961e+5020717 +/- ...e+5020701]
            sage: RBF.bernoulli(2**1000)
            Traceback (most recent call last):
            ...
            ValueError: argument too large

        TESTS::

            sage: RBF.bernoulli(2r)
            [0.1666666666666667 +/- ...e-17]
            sage: RBF.bernoulli(2/3)
            Traceback (most recent call last):
            ...
            TypeError: no canonical coercion from Rational Field to Integer Ring
            sage: RBF.bernoulli(-1)
            Traceback (most recent call last):
            ...
            ValueError: expected a nonnegative index"""
    @overload
    def catalan_constant(self) -> Any:
        """RealBallField.catalan_constant(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 783)

        Return a ball enclosing the Catalan constant.

        EXAMPLES::

            sage: RBF.catalan_constant()
            [0.915965594177219 +/- ...e-16]
            sage: RealBallField(128).catalan_constant()
            [0.91596559417721901505460351493238411077 +/- ...e-39]"""
    @overload
    def catalan_constant(self) -> Any:
        """RealBallField.catalan_constant(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 783)

        Return a ball enclosing the Catalan constant.

        EXAMPLES::

            sage: RBF.catalan_constant()
            [0.915965594177219 +/- ...e-16]
            sage: RealBallField(128).catalan_constant()
            [0.91596559417721901505460351493238411077 +/- ...e-39]"""
    @overload
    def catalan_constant(self) -> Any:
        """RealBallField.catalan_constant(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 783)

        Return a ball enclosing the Catalan constant.

        EXAMPLES::

            sage: RBF.catalan_constant()
            [0.915965594177219 +/- ...e-16]
            sage: RealBallField(128).catalan_constant()
            [0.91596559417721901505460351493238411077 +/- ...e-39]"""
    @overload
    def characteristic(self) -> Any:
        """RealBallField.characteristic(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 652)

        Real ball fields have characteristic zero.

        EXAMPLES::

            sage: RealBallField().characteristic()
            0"""
    @overload
    def characteristic(self) -> Any:
        """RealBallField.characteristic(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 652)

        Real ball fields have characteristic zero.

        EXAMPLES::

            sage: RealBallField().characteristic()
            0"""
    @overload
    def complex_field(self) -> Any:
        """RealBallField.complex_field(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 611)

        Return the complex ball field with the same precision.

        EXAMPLES::

            sage: from sage.rings.complex_arb import ComplexBallField
            sage: RBF.complex_field()
            Complex ball field with 53 bits of precision
            sage: RealBallField(3).algebraic_closure()
            Complex ball field with 3 bits of precision"""
    @overload
    def complex_field(self) -> Any:
        """RealBallField.complex_field(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 611)

        Return the complex ball field with the same precision.

        EXAMPLES::

            sage: from sage.rings.complex_arb import ComplexBallField
            sage: RBF.complex_field()
            Complex ball field with 53 bits of precision
            sage: RealBallField(3).algebraic_closure()
            Complex ball field with 3 bits of precision"""
    @overload
    def construction(self) -> Any:
        """RealBallField.construction(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 591)

        Return the construction of a real ball field as a completion of the
        rationals.

        EXAMPLES::

            sage: RBF = RealBallField(42)
            sage: functor, base = RBF.construction()
            sage: functor, base
            (Completion[+Infinity, prec=42], Rational Field)
            sage: functor(base) is RBF
            True"""
    @overload
    def construction(self) -> Any:
        """RealBallField.construction(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 591)

        Return the construction of a real ball field as a completion of the
        rationals.

        EXAMPLES::

            sage: RBF = RealBallField(42)
            sage: functor, base = RBF.construction()
            sage: functor, base
            (Completion[+Infinity, prec=42], Rational Field)
            sage: functor(base) is RBF
            True"""
    def cospi(self, x) -> Any:
        """RealBallField.cospi(self, x)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 849)

        Return a ball enclosing `\\cos(\\pi x)`.

        This works even if ``x`` itself is not a ball, and may be faster or
        more accurate where ``x`` is a rational number.

        EXAMPLES::

            sage: RBF.cospi(1)
            -1.000000000000000
            sage: RBF.cospi(1/3)
            0.5000000000000000

        .. SEEALSO:: :meth:`~sage.rings.real_arb.RealBall.cos`

        TESTS::

            sage: RBF.cospi(RLF(sqrt(2)))                                               # needs sage.symbolic
            [-0.26625534204142 +/- ...e-15]"""
    @overload
    def double_factorial(self, n) -> Any:
        """RealBallField.double_factorial(self, n)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 1094)

        Return a ball enclosing the ``n``-th double factorial.

        EXAMPLES::

            sage: [RBF.double_factorial(n) for n in range(7)]
            [1.000000000000000,
             1.000000000000000,
             2.000000000000000,
             3.000000000000000,
             8.000000000000000,
             15.00000000000000,
             48.00000000000000]
            sage: RBF.double_factorial(2**20)
            [1.448372990...e+2928836 +/- ...]
            sage: RBF.double_factorial(2**1000)
            Traceback (most recent call last):
            ...
            ValueError: argument too large
            sage: RBF.double_factorial(-1)
            Traceback (most recent call last):
            ...
            ValueError: expected a nonnegative index"""
    @overload
    def double_factorial(self, n) -> Any:
        """RealBallField.double_factorial(self, n)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 1094)

        Return a ball enclosing the ``n``-th double factorial.

        EXAMPLES::

            sage: [RBF.double_factorial(n) for n in range(7)]
            [1.000000000000000,
             1.000000000000000,
             2.000000000000000,
             3.000000000000000,
             8.000000000000000,
             15.00000000000000,
             48.00000000000000]
            sage: RBF.double_factorial(2**20)
            [1.448372990...e+2928836 +/- ...]
            sage: RBF.double_factorial(2**1000)
            Traceback (most recent call last):
            ...
            ValueError: argument too large
            sage: RBF.double_factorial(-1)
            Traceback (most recent call last):
            ...
            ValueError: expected a nonnegative index"""
    @overload
    def euler_constant(self) -> Any:
        """RealBallField.euler_constant(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 765)

        Return a ball enclosing the Euler constant.

        EXAMPLES::

            sage: RBF.euler_constant() # abs tol 1e-15
            [0.5772156649015329 +/- 9.00e-17]
            sage: RealBallField(128).euler_constant()
            [0.57721566490153286060651209008240243104 +/- ...e-39]"""
    @overload
    def euler_constant(self) -> Any:
        """RealBallField.euler_constant(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 765)

        Return a ball enclosing the Euler constant.

        EXAMPLES::

            sage: RBF.euler_constant() # abs tol 1e-15
            [0.5772156649015329 +/- 9.00e-17]
            sage: RealBallField(128).euler_constant()
            [0.57721566490153286060651209008240243104 +/- ...e-39]"""
    @overload
    def euler_constant(self) -> Any:
        """RealBallField.euler_constant(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 765)

        Return a ball enclosing the Euler constant.

        EXAMPLES::

            sage: RBF.euler_constant() # abs tol 1e-15
            [0.5772156649015329 +/- 9.00e-17]
            sage: RealBallField(128).euler_constant()
            [0.57721566490153286060651209008240243104 +/- ...e-39]"""
    @overload
    def fibonacci(self, n) -> Any:
        """RealBallField.fibonacci(self, n)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 1026)

        Return a ball enclosing the ``n``-th Fibonacci number.

        EXAMPLES::

            sage: [RBF.fibonacci(n) for n in range(7)]
            [0,
            1.000000000000000,
            1.000000000000000,
            2.000000000000000,
            3.000000000000000,
            5.000000000000000,
            8.000000000000000]
            sage: RBF.fibonacci(-2)
            -1.000000000000000
            sage: RBF.fibonacci(10**20)
            [3.78202087472056e+20898764024997873376 +/- ...e+20898764024997873361]"""
    @overload
    def fibonacci(self, n) -> Any:
        """RealBallField.fibonacci(self, n)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 1026)

        Return a ball enclosing the ``n``-th Fibonacci number.

        EXAMPLES::

            sage: [RBF.fibonacci(n) for n in range(7)]
            [0,
            1.000000000000000,
            1.000000000000000,
            2.000000000000000,
            3.000000000000000,
            5.000000000000000,
            8.000000000000000]
            sage: RBF.fibonacci(-2)
            -1.000000000000000
            sage: RBF.fibonacci(10**20)
            [3.78202087472056e+20898764024997873376 +/- ...e+20898764024997873361]"""
    def gamma(self, x) -> Any:
        """RealBallField.gamma(self, x)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 893)

        Return a ball enclosing the gamma function of ``x``.

        This works even if ``x`` itself is not a ball, and may be more
        efficient in the case where ``x`` is an integer or a rational number.

        EXAMPLES::

            sage: RBF.gamma(5)
            24.00000000000000
            sage: RBF.gamma(10**20)
            [1.932849514310098...+1956570551809674817225 +/- ...]
            sage: RBF.gamma(1/3)
            [2.678938534707747 +/- ...e-16]
            sage: RBF.gamma(-5)
            nan

        .. SEEALSO:: :meth:`~sage.rings.real_arb.RealBall.gamma`

        TESTS::

            sage: RBF.gamma(RLF(pi))  # abs tol 1e-13                                   # needs sage.symbolic
            [2.28803779534003 +/- 4.12e-15]"""
    @overload
    def gens(self) -> tuple:
        """RealBallField.gens(self) -> tuple

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 580)

        EXAMPLES::

            sage: RBF.gens()
            (1.000000000000000,)
            sage: RBF.gens_dict()
            {'1.000000000000000': 1.000000000000000}"""
    @overload
    def gens(self) -> Any:
        """RealBallField.gens(self) -> tuple

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 580)

        EXAMPLES::

            sage: RBF.gens()
            (1.000000000000000,)
            sage: RBF.gens_dict()
            {'1.000000000000000': 1.000000000000000}"""
    @overload
    def is_exact(self) -> Any:
        """RealBallField.is_exact(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 641)

        Real ball fields are not exact.

        EXAMPLES::

            sage: RealBallField().is_exact()
            False"""
    @overload
    def is_exact(self) -> Any:
        """RealBallField.is_exact(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 641)

        Real ball fields are not exact.

        EXAMPLES::

            sage: RealBallField().is_exact()
            False"""
    def log2(self) -> Any:
        """RealBallField.log2(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 747)

        Return a ball enclosing `\\log(2)`.

        EXAMPLES::

            sage: RBF.log2()
            [0.6931471805599453 +/- ...e-17]
            sage: RealBallField(128).log2()
            [0.69314718055994530941723212145817656807 +/- ...e-39]"""
    @overload
    def maximal_accuracy(self) -> Any:
        """RealBallField.maximal_accuracy(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 1133)

        Return the relative accuracy of exact elements measured in bits.

        OUTPUT: integer

        EXAMPLES::

            sage: RBF.maximal_accuracy()
            9223372036854775807 # 64-bit
            2147483647          # 32-bit

        .. SEEALSO:: :meth:`RealBall.accuracy`"""
    @overload
    def maximal_accuracy(self) -> Any:
        """RealBallField.maximal_accuracy(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 1133)

        Return the relative accuracy of exact elements measured in bits.

        OUTPUT: integer

        EXAMPLES::

            sage: RBF.maximal_accuracy()
            9223372036854775807 # 64-bit
            2147483647          # 32-bit

        .. SEEALSO:: :meth:`RealBall.accuracy`"""
    def pi(self) -> Any:
        """RealBallField.pi(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 729)

        Return a ball enclosing `\\pi`.

        EXAMPLES::

            sage: RBF.pi()
            [3.141592653589793 +/- ...e-16]
            sage: RealBallField(128).pi()
            [3.1415926535897932384626433832795028842 +/- ...e-38]"""
    def prec(self, *args, **kwargs):
        """RealBallField.precision(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 628)

        Return the bit precision used for operations on elements of this field.

        EXAMPLES::

            sage: RealBallField().precision()
            53"""
    @overload
    def precision(self) -> Any:
        """RealBallField.precision(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 628)

        Return the bit precision used for operations on elements of this field.

        EXAMPLES::

            sage: RealBallField().precision()
            53"""
    @overload
    def precision(self) -> Any:
        """RealBallField.precision(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 628)

        Return the bit precision used for operations on elements of this field.

        EXAMPLES::

            sage: RealBallField().precision()
            53"""
    def sinpi(self, x) -> Any:
        """RealBallField.sinpi(self, x)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 803)

        Return a ball enclosing `\\sin(\\pi x)`.

        This works even if ``x`` itself is not a ball, and may be faster or
        more accurate where ``x`` is a rational number.

        EXAMPLES::

            sage: RBF.sinpi(1)
            0
            sage: RBF.sinpi(1/3)
            [0.866025403784439 +/- ...e-16]
            sage: RBF.sinpi(1 + 2^(-100))
            [-2.478279624546525e-30 +/- ...e-46]

        .. SEEALSO:: :meth:`~sage.rings.real_arb.RealBall.sin`

        TESTS::

            sage: RBF.sinpi(RLF(sqrt(2)))                                               # needs sage.symbolic
            [-0.963902532849877 +/- ...e-16]"""
    @overload
    def some_elements(self) -> Any:
        """RealBallField.some_elements(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 663)

        Real ball fields contain exact balls, inexact balls, infinities, and
        more.

        EXAMPLES::

            sage: RBF.some_elements()
            [0, 1.000000000000000, [0.3333333333333333 +/- ...e-17],
            [-4.733045976388941e+363922934236666733021124 +/- ...e+363922934236666733021108],
            [+/- inf], [+/- inf], [+/- inf], nan]"""
    @overload
    def some_elements(self) -> Any:
        """RealBallField.some_elements(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 663)

        Real ball fields contain exact balls, inexact balls, infinities, and
        more.

        EXAMPLES::

            sage: RBF.some_elements()
            [0, 1.000000000000000, [0.3333333333333333 +/- ...e-17],
            [-4.733045976388941e+363922934236666733021124 +/- ...e+363922934236666733021108],
            [+/- inf], [+/- inf], [+/- inf], nan]"""
    def zeta(self, s) -> Any:
        """RealBallField.zeta(self, s)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 952)

        Return a ball enclosing the Riemann zeta function of ``s``.

        This works even if ``s`` itself is not a ball, and may be more
        efficient in the case where ``s`` is an integer.

        EXAMPLES::

            sage: RBF.zeta(3)
            [1.202056903159594 +/- ...e-16]
            sage: RBF.zeta(1)
            nan
            sage: RBF.zeta(1/2)
            [-1.460354508809587 +/- ...e-16]

        .. SEEALSO:: :meth:`~sage.rings.real_arb.RealBall.zeta`"""
    @staticmethod
    def __classcall__(cls, longprecision=...) -> Any:
        """RealBallField.__classcall__(cls, long precision=53)

        File: /build/sagemath/src/sage/src/sage/rings/real_arb.pyx (starting at line 380)

        Normalize the arguments for caching.

        TESTS::

            sage: RealBallField(53) is RealBallField() is RBF
            True"""
