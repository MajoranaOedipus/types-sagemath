import sage as sage
import sage.rings.abc
import sage.structure.element
import sage.structure.unique_representation
from sage.categories.category import ZZ as ZZ
from sage.misc.lazy_string import lazy_string as lazy_string
from sage.rings.complex_interval_field import ComplexIntervalField as ComplexIntervalField, ComplexIntervalField_class as ComplexIntervalField_class
from sage.rings.number_field.number_field_base import NumberField as NumberField
from sage.rings.rational_field import QQ as QQ
from sage.rings.real_arb import RealBallField as RealBallField
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation
from typing import Any, ClassVar, overload

CBF: ComplexBallField_with_category
__pyx_capi__: dict

class ComplexBall(sage.structure.element.RingElement):
    """ComplexBall(parent, x=None, y=None)

    File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 1370)

    Hold one ``acb_t`` of the `FLINT library <https://flintlib.org>`_.

    EXAMPLES::

        sage: a = ComplexBallField()(1, 1)
        sage: a
        1.000000000000000 + 1.000000000000000*I"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, parent, x=..., y=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 1402)

                Initialize the :class:`ComplexBall`.

                INPUT:

                - ``parent`` -- a :class:`ComplexBallField`

                - ``x``, ``y`` -- (optional) either a complex number, interval or ball,
                  or two real ones

                .. SEEALSO:: :meth:`ComplexBallField._element_constructor_`

                TESTS::

                    sage: from sage.rings.complex_arb import ComplexBall
                    sage: CBF53, CBF100 = ComplexBallField(53), ComplexBallField(100)
                    sage: ComplexBall(CBF100)
                    0
                    sage: ComplexBall(CBF100, ComplexBall(CBF53, ComplexBall(CBF100, 1/3)))
                    [0.333333333333333333333333333333 +/- ...e-31]
                    sage: ComplexBall(CBF100, RBF(pi))                                          # needs sage.symbolic
                    [3.141592653589793 +/- ...e-16]

                    sage: ComplexBall(CBF100, -3r)
                    Traceback (most recent call last):
                    ...
                    TypeError: unsupported initializer
                    sage: CBF100(-3r)
                    -3.000000000000000000000000000000

                    sage: ComplexBall(CBF100, CIF(1, 2))
                    1.000000000000000000000000000000 + 2.000000000000000000000000000000*I
                    sage: ComplexBall(CBF100, RBF(1/3), RBF(1))
                    [0.3333333333333333 +/- ...e-17] + 1.000000000000000000000000000000*I
                    sage: ComplexBall(CBF100, 10^100)
                    [1.000000000000000000000000000000e+100 +/- ...]

                    sage: NF.<a> = QuadraticField(-1, embedding=CC(0, -1))
                    sage: CBF(a)
                    -1.000000000000000*I

                    sage: NF.<a> = QuadraticField(-1, embedding=None)
                    sage: CBF(a)
                    1.000000000000000*I
                    sage: CBF.coerce(a)
                    Traceback (most recent call last):
                    ...
                    TypeError: no canonical coercion ...

                    sage: NF.<a> = QuadraticField(-2)
                    sage: CBF(1/3 + a).real()
                    [0.3333333333333333 +/- ...e-17]

                    sage: ComplexBall(CBF, 1, 1/2)
                    1.000000000000000 + 0.5000000000000000*I
                    sage: ComplexBall(CBF, 1, 1)
                    1.000000000000000 + 1.000000000000000*I
                    sage: ComplexBall(CBF, 1, 1/2)
                    1.000000000000000 + 0.5000000000000000*I
                    sage: ComplexBall(CBF, 1/2, 1)
                    0.5000000000000000 + 1.000000000000000*I
                    sage: ComplexBall(CBF, 1/2, 1/2)
                    0.5000000000000000 + 0.5000000000000000*I
                    sage: ComplexBall(CBF, 1/2, 'a')
                    Traceback (most recent call last):
                    ...
                    TypeError: unsupported initializer
                    sage: ComplexBall(CBF, 'a')
                    Traceback (most recent call last):
                    ...
                    TypeError: unsupported initializer
        """
    @overload
    def Chi(self) -> Any:
        """ComplexBall.Chi(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4353)

        Return the hyperbolic cosine integral with argument ``self``.

        EXAMPLES::

            sage: CBF(1, 1).Chi()  # abs tol 1e-15
            [0.882172180555936 +/- 5.89e-16] + [1.28354719327494 +/- 1.01e-15]*I
            sage: CBF(0).Chi()
            nan + nan*I

        TESTS:

            sage: CBF(Chi(I))  # abs tol 5e-16                                          # needs sage.symbolic
            [0.337403922900968 +/- 3.25e-16] + [1.570796326794897 +/- 5.54e-16]*I"""
    @overload
    def Chi(self) -> Any:
        """ComplexBall.Chi(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4353)

        Return the hyperbolic cosine integral with argument ``self``.

        EXAMPLES::

            sage: CBF(1, 1).Chi()  # abs tol 1e-15
            [0.882172180555936 +/- 5.89e-16] + [1.28354719327494 +/- 1.01e-15]*I
            sage: CBF(0).Chi()
            nan + nan*I

        TESTS:

            sage: CBF(Chi(I))  # abs tol 5e-16                                          # needs sage.symbolic
            [0.337403922900968 +/- 3.25e-16] + [1.570796326794897 +/- 5.54e-16]*I"""
    @overload
    def Chi(self) -> Any:
        """ComplexBall.Chi(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4353)

        Return the hyperbolic cosine integral with argument ``self``.

        EXAMPLES::

            sage: CBF(1, 1).Chi()  # abs tol 1e-15
            [0.882172180555936 +/- 5.89e-16] + [1.28354719327494 +/- 1.01e-15]*I
            sage: CBF(0).Chi()
            nan + nan*I

        TESTS:

            sage: CBF(Chi(I))  # abs tol 5e-16                                          # needs sage.symbolic
            [0.337403922900968 +/- 3.25e-16] + [1.570796326794897 +/- 5.54e-16]*I"""
    @overload
    def Chi(self, I) -> Any:
        """ComplexBall.Chi(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4353)

        Return the hyperbolic cosine integral with argument ``self``.

        EXAMPLES::

            sage: CBF(1, 1).Chi()  # abs tol 1e-15
            [0.882172180555936 +/- 5.89e-16] + [1.28354719327494 +/- 1.01e-15]*I
            sage: CBF(0).Chi()
            nan + nan*I

        TESTS:

            sage: CBF(Chi(I))  # abs tol 5e-16                                          # needs sage.symbolic
            [0.337403922900968 +/- 3.25e-16] + [1.570796326794897 +/- 5.54e-16]*I"""
    @overload
    def Ci(self) -> Any:
        """ComplexBall.Ci(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4305)

        Return the cosine integral with argument ``self``.

        EXAMPLES::

            sage: CBF(1, 1).Ci()  # abs tol 5e-16
            [0.882172180555936 +/- 5.89e-16] + [0.287249133519956 +/- 3.37e-16]*I
            sage: CBF(0).Ci()
            nan + nan*I

        TESTS:

            sage: CBF(Ci(I))  # abs tol 5e-16                                           # needs sage.symbolic
            [0.837866940980208 +/- 4.72e-16] + [1.570796326794897 +/- 5.54e-16]*I"""
    @overload
    def Ci(self) -> Any:
        """ComplexBall.Ci(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4305)

        Return the cosine integral with argument ``self``.

        EXAMPLES::

            sage: CBF(1, 1).Ci()  # abs tol 5e-16
            [0.882172180555936 +/- 5.89e-16] + [0.287249133519956 +/- 3.37e-16]*I
            sage: CBF(0).Ci()
            nan + nan*I

        TESTS:

            sage: CBF(Ci(I))  # abs tol 5e-16                                           # needs sage.symbolic
            [0.837866940980208 +/- 4.72e-16] + [1.570796326794897 +/- 5.54e-16]*I"""
    @overload
    def Ci(self) -> Any:
        """ComplexBall.Ci(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4305)

        Return the cosine integral with argument ``self``.

        EXAMPLES::

            sage: CBF(1, 1).Ci()  # abs tol 5e-16
            [0.882172180555936 +/- 5.89e-16] + [0.287249133519956 +/- 3.37e-16]*I
            sage: CBF(0).Ci()
            nan + nan*I

        TESTS:

            sage: CBF(Ci(I))  # abs tol 5e-16                                           # needs sage.symbolic
            [0.837866940980208 +/- 4.72e-16] + [1.570796326794897 +/- 5.54e-16]*I"""
    @overload
    def Ci(self, I) -> Any:
        """ComplexBall.Ci(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4305)

        Return the cosine integral with argument ``self``.

        EXAMPLES::

            sage: CBF(1, 1).Ci()  # abs tol 5e-16
            [0.882172180555936 +/- 5.89e-16] + [0.287249133519956 +/- 3.37e-16]*I
            sage: CBF(0).Ci()
            nan + nan*I

        TESTS:

            sage: CBF(Ci(I))  # abs tol 5e-16                                           # needs sage.symbolic
            [0.837866940980208 +/- 4.72e-16] + [1.570796326794897 +/- 5.54e-16]*I"""
    @overload
    def Ei(self) -> Any:
        """ComplexBall.Ei(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4259)

        Return the exponential integral with argument ``self``.

        EXAMPLES::

            sage: CBF(1, 1).Ei()  # abs tol 6e-15
            [1.76462598556385 +/- 6.03e-15] + [2.38776985151052 +/- 4.23e-15]*I
            sage: CBF(0).Ei()
            nan...

        TESTS:

            sage: CBF(Ei(I))  # abs tol 2e-15                                           # needs sage.symbolic
            [0.337403922900968 +/- 3.76e-16] + [2.51687939716208 +/- 2.01e-15]*I"""
    @overload
    def Ei(self) -> Any:
        """ComplexBall.Ei(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4259)

        Return the exponential integral with argument ``self``.

        EXAMPLES::

            sage: CBF(1, 1).Ei()  # abs tol 6e-15
            [1.76462598556385 +/- 6.03e-15] + [2.38776985151052 +/- 4.23e-15]*I
            sage: CBF(0).Ei()
            nan...

        TESTS:

            sage: CBF(Ei(I))  # abs tol 2e-15                                           # needs sage.symbolic
            [0.337403922900968 +/- 3.76e-16] + [2.51687939716208 +/- 2.01e-15]*I"""
    @overload
    def Ei(self) -> Any:
        """ComplexBall.Ei(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4259)

        Return the exponential integral with argument ``self``.

        EXAMPLES::

            sage: CBF(1, 1).Ei()  # abs tol 6e-15
            [1.76462598556385 +/- 6.03e-15] + [2.38776985151052 +/- 4.23e-15]*I
            sage: CBF(0).Ei()
            nan...

        TESTS:

            sage: CBF(Ei(I))  # abs tol 2e-15                                           # needs sage.symbolic
            [0.337403922900968 +/- 3.76e-16] + [2.51687939716208 +/- 2.01e-15]*I"""
    @overload
    def Ei(self, I) -> Any:
        """ComplexBall.Ei(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4259)

        Return the exponential integral with argument ``self``.

        EXAMPLES::

            sage: CBF(1, 1).Ei()  # abs tol 6e-15
            [1.76462598556385 +/- 6.03e-15] + [2.38776985151052 +/- 4.23e-15]*I
            sage: CBF(0).Ei()
            nan...

        TESTS:

            sage: CBF(Ei(I))  # abs tol 2e-15                                           # needs sage.symbolic
            [0.337403922900968 +/- 3.76e-16] + [2.51687939716208 +/- 2.01e-15]*I"""
    @overload
    def Li(self) -> Any:
        """ComplexBall.Li(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4411)

        Offset logarithmic integral.

        EXAMPLES::

            sage: CBF(0).Li()
            [-1.045163780117493 +/- ...e-16]
            sage: li(0).n()                                                             # needs sage.symbolic
            0.000000000000000
            sage: Li(0).n()                                                             # needs sage.symbolic
            -1.04516378011749"""
    @overload
    def Li(self) -> Any:
        """ComplexBall.Li(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4411)

        Offset logarithmic integral.

        EXAMPLES::

            sage: CBF(0).Li()
            [-1.045163780117493 +/- ...e-16]
            sage: li(0).n()                                                             # needs sage.symbolic
            0.000000000000000
            sage: Li(0).n()                                                             # needs sage.symbolic
            -1.04516378011749"""
    @overload
    def Shi(self) -> Any:
        """ComplexBall.Shi(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4329)

        Return the hyperbolic sine integral with argument ``self``.

        EXAMPLES::

            sage: CBF(1, 1).Shi()  # abs tol 3e-15
            [0.88245380500792 +/- 3.36e-15] + [1.10422265823558 +/- 2.48e-15]*I
            sage: CBF(0).Shi()
            0

        TESTS:

            sage: CBF(Shi(I))  # abs tol 1e-15                                          # needs sage.symbolic
            [0.946083070367183 +/- 9.22e-16]*I"""
    @overload
    def Shi(self) -> Any:
        """ComplexBall.Shi(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4329)

        Return the hyperbolic sine integral with argument ``self``.

        EXAMPLES::

            sage: CBF(1, 1).Shi()  # abs tol 3e-15
            [0.88245380500792 +/- 3.36e-15] + [1.10422265823558 +/- 2.48e-15]*I
            sage: CBF(0).Shi()
            0

        TESTS:

            sage: CBF(Shi(I))  # abs tol 1e-15                                          # needs sage.symbolic
            [0.946083070367183 +/- 9.22e-16]*I"""
    @overload
    def Shi(self) -> Any:
        """ComplexBall.Shi(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4329)

        Return the hyperbolic sine integral with argument ``self``.

        EXAMPLES::

            sage: CBF(1, 1).Shi()  # abs tol 3e-15
            [0.88245380500792 +/- 3.36e-15] + [1.10422265823558 +/- 2.48e-15]*I
            sage: CBF(0).Shi()
            0

        TESTS:

            sage: CBF(Shi(I))  # abs tol 1e-15                                          # needs sage.symbolic
            [0.946083070367183 +/- 9.22e-16]*I"""
    @overload
    def Shi(self, I) -> Any:
        """ComplexBall.Shi(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4329)

        Return the hyperbolic sine integral with argument ``self``.

        EXAMPLES::

            sage: CBF(1, 1).Shi()  # abs tol 3e-15
            [0.88245380500792 +/- 3.36e-15] + [1.10422265823558 +/- 2.48e-15]*I
            sage: CBF(0).Shi()
            0

        TESTS:

            sage: CBF(Shi(I))  # abs tol 1e-15                                          # needs sage.symbolic
            [0.946083070367183 +/- 9.22e-16]*I"""
    @overload
    def Si(self) -> Any:
        """ComplexBall.Si(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4281)

        Return the sine integral with argument ``self``.

        EXAMPLES::

            sage: CBF(1, 1).Si()  # abs tol 3e-15
            [1.10422265823558 +/- 2.48e-15] + [0.88245380500792 +/- 3.36e-15]*I
            sage: CBF(0).Si()
            0

        TESTS:

            sage: CBF(Si(I))  # abs tol 3e-15                                           # needs sage.symbolic
            [1.05725087537573 +/- 2.77e-15]*I"""
    @overload
    def Si(self) -> Any:
        """ComplexBall.Si(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4281)

        Return the sine integral with argument ``self``.

        EXAMPLES::

            sage: CBF(1, 1).Si()  # abs tol 3e-15
            [1.10422265823558 +/- 2.48e-15] + [0.88245380500792 +/- 3.36e-15]*I
            sage: CBF(0).Si()
            0

        TESTS:

            sage: CBF(Si(I))  # abs tol 3e-15                                           # needs sage.symbolic
            [1.05725087537573 +/- 2.77e-15]*I"""
    @overload
    def Si(self) -> Any:
        """ComplexBall.Si(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4281)

        Return the sine integral with argument ``self``.

        EXAMPLES::

            sage: CBF(1, 1).Si()  # abs tol 3e-15
            [1.10422265823558 +/- 2.48e-15] + [0.88245380500792 +/- 3.36e-15]*I
            sage: CBF(0).Si()
            0

        TESTS:

            sage: CBF(Si(I))  # abs tol 3e-15                                           # needs sage.symbolic
            [1.05725087537573 +/- 2.77e-15]*I"""
    @overload
    def Si(self, I) -> Any:
        """ComplexBall.Si(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4281)

        Return the sine integral with argument ``self``.

        EXAMPLES::

            sage: CBF(1, 1).Si()  # abs tol 3e-15
            [1.10422265823558 +/- 2.48e-15] + [0.88245380500792 +/- 3.36e-15]*I
            sage: CBF(0).Si()
            0

        TESTS:

            sage: CBF(Si(I))  # abs tol 3e-15                                           # needs sage.symbolic
            [1.05725087537573 +/- 2.77e-15]*I"""
    @overload
    def above_abs(self) -> Any:
        """ComplexBall.above_abs(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 1968)

        Return an upper bound for the absolute value of this complex ball.

        OUTPUT: a ball with zero radius

        EXAMPLES::

            sage: b = ComplexBallField(8)(1+i).above_abs()
            sage: b
            [1.4 +/- 0.0219]
            sage: b.is_exact()
            True
            sage: QQ(b)*128
            182

        .. SEEALSO:: :meth:`below_abs`"""
    @overload
    def above_abs(self) -> Any:
        """ComplexBall.above_abs(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 1968)

        Return an upper bound for the absolute value of this complex ball.

        OUTPUT: a ball with zero radius

        EXAMPLES::

            sage: b = ComplexBallField(8)(1+i).above_abs()
            sage: b
            [1.4 +/- 0.0219]
            sage: b.is_exact()
            True
            sage: QQ(b)*128
            182

        .. SEEALSO:: :meth:`below_abs`"""
    @overload
    def accuracy(self) -> Any:
        """ComplexBall.accuracy(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 2201)

        Return the effective relative accuracy of this ball measured in bits.

        This is computed as if calling
        :meth:`~sage.rings.real_arb.RealBall.accuracy()`
        on the real ball whose midpoint is the larger out of the real and
        imaginary midpoints of this complex ball, and whose radius is the
        larger out of the real and imaginary radii of this complex ball.

        EXAMPLES::

            sage: CBF(exp(I*pi/3)).accuracy()                                           # needs sage.symbolic
            51
            sage: CBF(I/2).accuracy() == CBF.base().maximal_accuracy()
            True
            sage: CBF('nan', 'inf').accuracy() == -CBF.base().maximal_accuracy()
            True

        .. SEEALSO::

            :meth:`~sage.rings.real_arb.RealBallField.maximal_accuracy`"""
    @overload
    def accuracy(self) -> Any:
        """ComplexBall.accuracy(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 2201)

        Return the effective relative accuracy of this ball measured in bits.

        This is computed as if calling
        :meth:`~sage.rings.real_arb.RealBall.accuracy()`
        on the real ball whose midpoint is the larger out of the real and
        imaginary midpoints of this complex ball, and whose radius is the
        larger out of the real and imaginary radii of this complex ball.

        EXAMPLES::

            sage: CBF(exp(I*pi/3)).accuracy()                                           # needs sage.symbolic
            51
            sage: CBF(I/2).accuracy() == CBF.base().maximal_accuracy()
            True
            sage: CBF('nan', 'inf').accuracy() == -CBF.base().maximal_accuracy()
            True

        .. SEEALSO::

            :meth:`~sage.rings.real_arb.RealBallField.maximal_accuracy`"""
    @overload
    def accuracy(self) -> Any:
        """ComplexBall.accuracy(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 2201)

        Return the effective relative accuracy of this ball measured in bits.

        This is computed as if calling
        :meth:`~sage.rings.real_arb.RealBall.accuracy()`
        on the real ball whose midpoint is the larger out of the real and
        imaginary midpoints of this complex ball, and whose radius is the
        larger out of the real and imaginary radii of this complex ball.

        EXAMPLES::

            sage: CBF(exp(I*pi/3)).accuracy()                                           # needs sage.symbolic
            51
            sage: CBF(I/2).accuracy() == CBF.base().maximal_accuracy()
            True
            sage: CBF('nan', 'inf').accuracy() == -CBF.base().maximal_accuracy()
            True

        .. SEEALSO::

            :meth:`~sage.rings.real_arb.RealBallField.maximal_accuracy`"""
    @overload
    def accuracy(self) -> Any:
        """ComplexBall.accuracy(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 2201)

        Return the effective relative accuracy of this ball measured in bits.

        This is computed as if calling
        :meth:`~sage.rings.real_arb.RealBall.accuracy()`
        on the real ball whose midpoint is the larger out of the real and
        imaginary midpoints of this complex ball, and whose radius is the
        larger out of the real and imaginary radii of this complex ball.

        EXAMPLES::

            sage: CBF(exp(I*pi/3)).accuracy()                                           # needs sage.symbolic
            51
            sage: CBF(I/2).accuracy() == CBF.base().maximal_accuracy()
            True
            sage: CBF('nan', 'inf').accuracy() == -CBF.base().maximal_accuracy()
            True

        .. SEEALSO::

            :meth:`~sage.rings.real_arb.RealBallField.maximal_accuracy`"""
    @overload
    def accuracy(self) -> Any:
        """ComplexBall.accuracy(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 2201)

        Return the effective relative accuracy of this ball measured in bits.

        This is computed as if calling
        :meth:`~sage.rings.real_arb.RealBall.accuracy()`
        on the real ball whose midpoint is the larger out of the real and
        imaginary midpoints of this complex ball, and whose radius is the
        larger out of the real and imaginary radii of this complex ball.

        EXAMPLES::

            sage: CBF(exp(I*pi/3)).accuracy()                                           # needs sage.symbolic
            51
            sage: CBF(I/2).accuracy() == CBF.base().maximal_accuracy()
            True
            sage: CBF('nan', 'inf').accuracy() == -CBF.base().maximal_accuracy()
            True

        .. SEEALSO::

            :meth:`~sage.rings.real_arb.RealBallField.maximal_accuracy`"""
    def add_error(self, ampl) -> Any:
        """ComplexBall.add_error(self, ampl)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 2249)

        Increase the radii of the real and imaginary parts by (an upper bound
        on) ``ampl``.

        If ``ampl`` is negative, the radii remain unchanged.

        INPUT:

        - ``ampl`` -- a **real** ball (or an object that can be coerced to a
          real ball)

        OUTPUT: a new complex ball

        EXAMPLES::

            sage: CBF(1+i).add_error(10^-16)
            [1.000000000000000 +/- ...e-16] + [1.000000000000000 +/- ...e-16]*I"""
    @overload
    def agm1(self) -> Any:
        '''ComplexBall.agm1(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3836)

        Return the arithmetic-geometric mean of 1 and ``self``.

        The arithmetic-geometric mean is defined such that the function is
        continuous in the complex plane except for a branch cut along the
        negative half axis (where it is continuous from above). This
        corresponds to always choosing an "optimal" branch for the square root
        in the arithmetic-geometric mean iteration.

        EXAMPLES::

            sage: CBF(0, -1).agm1()
            [0.599070117367796 +/- 3.9...e-16] + [-0.599070117367796 +/- 5.5...e-16]*I'''
    @overload
    def agm1(self) -> Any:
        '''ComplexBall.agm1(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3836)

        Return the arithmetic-geometric mean of 1 and ``self``.

        The arithmetic-geometric mean is defined such that the function is
        continuous in the complex plane except for a branch cut along the
        negative half axis (where it is continuous from above). This
        corresponds to always choosing an "optimal" branch for the square root
        in the arithmetic-geometric mean iteration.

        EXAMPLES::

            sage: CBF(0, -1).agm1()
            [0.599070117367796 +/- 3.9...e-16] + [-0.599070117367796 +/- 5.5...e-16]*I'''
    @overload
    def airy(self) -> Any:
        """ComplexBall.airy(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4055)

        Return the Airy functions Ai, Ai', Bi, Bi' with argument ``self``,
        evaluated simultaneously.

        EXAMPLES::

            sage: CBF(10*pi).airy()                                                     # needs sage.symbolic
            ([1.2408955946101e-52 +/- ...e-66],
             [-6.965048886977e-52 +/- ...e-65],
             [2.2882956833435e+50 +/- ...e+36],
             [1.2807602335816e+51 +/- ...e+37])
            sage: ai, aip, bi, bip = CBF(1,2).airy()
            sage: (ai * bip - bi * aip) * CBF(pi)                                       # needs sage.symbolic
            [1.0000000000000 +/- ...e-15] + [+/- ...e-16]*I"""
    @overload
    def airy(self) -> Any:
        """ComplexBall.airy(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4055)

        Return the Airy functions Ai, Ai', Bi, Bi' with argument ``self``,
        evaluated simultaneously.

        EXAMPLES::

            sage: CBF(10*pi).airy()                                                     # needs sage.symbolic
            ([1.2408955946101e-52 +/- ...e-66],
             [-6.965048886977e-52 +/- ...e-65],
             [2.2882956833435e+50 +/- ...e+36],
             [1.2807602335816e+51 +/- ...e+37])
            sage: ai, aip, bi, bip = CBF(1,2).airy()
            sage: (ai * bip - bi * aip) * CBF(pi)                                       # needs sage.symbolic
            [1.0000000000000 +/- ...e-15] + [+/- ...e-16]*I"""
    @overload
    def airy(self) -> Any:
        """ComplexBall.airy(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4055)

        Return the Airy functions Ai, Ai', Bi, Bi' with argument ``self``,
        evaluated simultaneously.

        EXAMPLES::

            sage: CBF(10*pi).airy()                                                     # needs sage.symbolic
            ([1.2408955946101e-52 +/- ...e-66],
             [-6.965048886977e-52 +/- ...e-65],
             [2.2882956833435e+50 +/- ...e+36],
             [1.2807602335816e+51 +/- ...e+37])
            sage: ai, aip, bi, bip = CBF(1,2).airy()
            sage: (ai * bip - bi * aip) * CBF(pi)                                       # needs sage.symbolic
            [1.0000000000000 +/- ...e-15] + [+/- ...e-16]*I"""
    @overload
    def airy_ai(self) -> Any:
        """ComplexBall.airy_ai(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4080)

        Return the Airy function Ai with argument ``self``.

        EXAMPLES::

            sage: CBF(1,2).airy_ai()
            [-0.2193862549814276 +/- ...e-17] + [-0.1753859114081094 +/- ...e-17]*I"""
    @overload
    def airy_ai(self) -> Any:
        """ComplexBall.airy_ai(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4080)

        Return the Airy function Ai with argument ``self``.

        EXAMPLES::

            sage: CBF(1,2).airy_ai()
            [-0.2193862549814276 +/- ...e-17] + [-0.1753859114081094 +/- ...e-17]*I"""
    def airy_ai_prime(self) -> Any:
        """ComplexBall.airy_ai_prime(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4095)

        Return the Airy function derivative Ai' with argument ``self``.

        EXAMPLES::

            sage: CBF(1,2).airy_ai_prime()
            [0.1704449781789148 +/- ...e-17] + [0.387622439413295 +/- ...e-16]*I"""
    @overload
    def airy_bi(self) -> Any:
        """ComplexBall.airy_bi(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4110)

        Return the Airy function Bi with argument ``self``.

        EXAMPLES::

            sage: CBF(1,2).airy_bi()
            [0.0488220324530612 +/- ...e-17] + [0.1332740579917484 +/- ...e-17]*I"""
    @overload
    def airy_bi(self) -> Any:
        """ComplexBall.airy_bi(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4110)

        Return the Airy function Bi with argument ``self``.

        EXAMPLES::

            sage: CBF(1,2).airy_bi()
            [0.0488220324530612 +/- ...e-17] + [0.1332740579917484 +/- ...e-17]*I"""
    def airy_bi_prime(self) -> Any:
        """ComplexBall.airy_bi_prime(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4125)

        Return the Airy function derivative Bi' with argument ``self``.

        EXAMPLES::

            sage: CBF(1,2).airy_bi_prime()
            [-0.857239258605362 +/- ...e-16] + [0.4955063363095674 +/- ...e-17]*I"""
    @overload
    def arccos(self, analytic=...) -> Any:
        """ComplexBall.arccos(self, analytic=False)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3424)

        Return the arccosine of this ball.

        INPUT:

        - ``analytic`` -- boolean (default: ``False``); if ``True``, return an
          indeterminate (not-a-number) value when the input ball touches
          the branch cut

        EXAMPLES::

            sage: CBF(1+i).arccos()
            [0.90455689430238 +/- ...e-15] + [-1.06127506190504 +/- ...e-15]*I
            sage: CBF(-1).arccos()
            [3.141592653589793 +/- ...e-16]
            sage: CBF(-1).arccos(analytic=True)
            nan + nan*I"""
    @overload
    def arccos(self) -> Any:
        """ComplexBall.arccos(self, analytic=False)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3424)

        Return the arccosine of this ball.

        INPUT:

        - ``analytic`` -- boolean (default: ``False``); if ``True``, return an
          indeterminate (not-a-number) value when the input ball touches
          the branch cut

        EXAMPLES::

            sage: CBF(1+i).arccos()
            [0.90455689430238 +/- ...e-15] + [-1.06127506190504 +/- ...e-15]*I
            sage: CBF(-1).arccos()
            [3.141592653589793 +/- ...e-16]
            sage: CBF(-1).arccos(analytic=True)
            nan + nan*I"""
    @overload
    def arccos(self) -> Any:
        """ComplexBall.arccos(self, analytic=False)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3424)

        Return the arccosine of this ball.

        INPUT:

        - ``analytic`` -- boolean (default: ``False``); if ``True``, return an
          indeterminate (not-a-number) value when the input ball touches
          the branch cut

        EXAMPLES::

            sage: CBF(1+i).arccos()
            [0.90455689430238 +/- ...e-15] + [-1.06127506190504 +/- ...e-15]*I
            sage: CBF(-1).arccos()
            [3.141592653589793 +/- ...e-16]
            sage: CBF(-1).arccos(analytic=True)
            nan + nan*I"""
    @overload
    def arccos(self, analytic=...) -> Any:
        """ComplexBall.arccos(self, analytic=False)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3424)

        Return the arccosine of this ball.

        INPUT:

        - ``analytic`` -- boolean (default: ``False``); if ``True``, return an
          indeterminate (not-a-number) value when the input ball touches
          the branch cut

        EXAMPLES::

            sage: CBF(1+i).arccos()
            [0.90455689430238 +/- ...e-15] + [-1.06127506190504 +/- ...e-15]*I
            sage: CBF(-1).arccos()
            [3.141592653589793 +/- ...e-16]
            sage: CBF(-1).arccos(analytic=True)
            nan + nan*I"""
    @overload
    def arccosh(self, analytic=...) -> Any:
        """ComplexBall.arccosh(self, analytic=False)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3513)

        Return the hyperbolic arccosine of this ball.

        INPUT:

        - ``analytic`` -- boolean (default: ``False``); if ``True``, return an
          indeterminate (not-a-number) value when the input ball touches
          the branch cut

        EXAMPLES::

            sage: CBF(1+i).arccosh()
            [1.061275061905035 +/- ...e-16] + [0.904556894302381 +/- ...e-16]*I
            sage: CBF(-2).arccosh()
            [1.316957896924817 +/- ...e-16] + [3.141592653589793 +/- ...e-16]*I
            sage: CBF(-2).arccosh(analytic=True)
            nan + nan*I"""
    @overload
    def arccosh(self) -> Any:
        """ComplexBall.arccosh(self, analytic=False)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3513)

        Return the hyperbolic arccosine of this ball.

        INPUT:

        - ``analytic`` -- boolean (default: ``False``); if ``True``, return an
          indeterminate (not-a-number) value when the input ball touches
          the branch cut

        EXAMPLES::

            sage: CBF(1+i).arccosh()
            [1.061275061905035 +/- ...e-16] + [0.904556894302381 +/- ...e-16]*I
            sage: CBF(-2).arccosh()
            [1.316957896924817 +/- ...e-16] + [3.141592653589793 +/- ...e-16]*I
            sage: CBF(-2).arccosh(analytic=True)
            nan + nan*I"""
    @overload
    def arccosh(self) -> Any:
        """ComplexBall.arccosh(self, analytic=False)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3513)

        Return the hyperbolic arccosine of this ball.

        INPUT:

        - ``analytic`` -- boolean (default: ``False``); if ``True``, return an
          indeterminate (not-a-number) value when the input ball touches
          the branch cut

        EXAMPLES::

            sage: CBF(1+i).arccosh()
            [1.061275061905035 +/- ...e-16] + [0.904556894302381 +/- ...e-16]*I
            sage: CBF(-2).arccosh()
            [1.316957896924817 +/- ...e-16] + [3.141592653589793 +/- ...e-16]*I
            sage: CBF(-2).arccosh(analytic=True)
            nan + nan*I"""
    @overload
    def arccosh(self, analytic=...) -> Any:
        """ComplexBall.arccosh(self, analytic=False)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3513)

        Return the hyperbolic arccosine of this ball.

        INPUT:

        - ``analytic`` -- boolean (default: ``False``); if ``True``, return an
          indeterminate (not-a-number) value when the input ball touches
          the branch cut

        EXAMPLES::

            sage: CBF(1+i).arccosh()
            [1.061275061905035 +/- ...e-16] + [0.904556894302381 +/- ...e-16]*I
            sage: CBF(-2).arccosh()
            [1.316957896924817 +/- ...e-16] + [3.141592653589793 +/- ...e-16]*I
            sage: CBF(-2).arccosh(analytic=True)
            nan + nan*I"""
    @overload
    def arcsin(self, analytic=...) -> Any:
        """ComplexBall.arcsin(self, analytic=False)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3395)

        Return the arcsine of this ball.

        INPUT:

        - ``analytic`` -- boolean (default: ``False``); if ``True``, return an
          indeterminate (not-a-number) value when the input ball touches
          the branch cut

        EXAMPLES::

            sage: CBF(1+i).arcsin()
            [0.66623943249252 +/- ...e-15] + [1.06127506190504 +/- ...e-15]*I
            sage: CBF(1, RIF(0,1/1000)).arcsin()
            [1.6 +/- 0.0619] + [+/- 0.0322]*I
            sage: CBF(1, RIF(0,1/1000)).arcsin(analytic=True)
            nan + nan*I"""
    @overload
    def arcsin(self) -> Any:
        """ComplexBall.arcsin(self, analytic=False)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3395)

        Return the arcsine of this ball.

        INPUT:

        - ``analytic`` -- boolean (default: ``False``); if ``True``, return an
          indeterminate (not-a-number) value when the input ball touches
          the branch cut

        EXAMPLES::

            sage: CBF(1+i).arcsin()
            [0.66623943249252 +/- ...e-15] + [1.06127506190504 +/- ...e-15]*I
            sage: CBF(1, RIF(0,1/1000)).arcsin()
            [1.6 +/- 0.0619] + [+/- 0.0322]*I
            sage: CBF(1, RIF(0,1/1000)).arcsin(analytic=True)
            nan + nan*I"""
    @overload
    def arcsin(self) -> Any:
        """ComplexBall.arcsin(self, analytic=False)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3395)

        Return the arcsine of this ball.

        INPUT:

        - ``analytic`` -- boolean (default: ``False``); if ``True``, return an
          indeterminate (not-a-number) value when the input ball touches
          the branch cut

        EXAMPLES::

            sage: CBF(1+i).arcsin()
            [0.66623943249252 +/- ...e-15] + [1.06127506190504 +/- ...e-15]*I
            sage: CBF(1, RIF(0,1/1000)).arcsin()
            [1.6 +/- 0.0619] + [+/- 0.0322]*I
            sage: CBF(1, RIF(0,1/1000)).arcsin(analytic=True)
            nan + nan*I"""
    @overload
    def arcsin(self, analytic=...) -> Any:
        """ComplexBall.arcsin(self, analytic=False)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3395)

        Return the arcsine of this ball.

        INPUT:

        - ``analytic`` -- boolean (default: ``False``); if ``True``, return an
          indeterminate (not-a-number) value when the input ball touches
          the branch cut

        EXAMPLES::

            sage: CBF(1+i).arcsin()
            [0.66623943249252 +/- ...e-15] + [1.06127506190504 +/- ...e-15]*I
            sage: CBF(1, RIF(0,1/1000)).arcsin()
            [1.6 +/- 0.0619] + [+/- 0.0322]*I
            sage: CBF(1, RIF(0,1/1000)).arcsin(analytic=True)
            nan + nan*I"""
    @overload
    def arcsinh(self, analytic=...) -> Any:
        """ComplexBall.arcsinh(self, analytic=False)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3484)

        Return the hyperbolic arcsine of this ball.

        INPUT:

        - ``analytic`` -- boolean (default: ``False``); if ``True``, return an
          indeterminate (not-a-number) value when the input ball touches
          the branch cut

        EXAMPLES::

            sage: CBF(1+i).arcsinh()
            [1.06127506190504 +/- ...e-15] + [0.66623943249252 +/- ...e-15]*I
            sage: CBF(2*i).arcsinh()
            [1.31695789692482 +/- ...e-15] + [1.570796326794897 +/- ...e-16]*I
            sage: CBF(2*i).arcsinh(analytic=True)
            nan + nan*I"""
    @overload
    def arcsinh(self) -> Any:
        """ComplexBall.arcsinh(self, analytic=False)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3484)

        Return the hyperbolic arcsine of this ball.

        INPUT:

        - ``analytic`` -- boolean (default: ``False``); if ``True``, return an
          indeterminate (not-a-number) value when the input ball touches
          the branch cut

        EXAMPLES::

            sage: CBF(1+i).arcsinh()
            [1.06127506190504 +/- ...e-15] + [0.66623943249252 +/- ...e-15]*I
            sage: CBF(2*i).arcsinh()
            [1.31695789692482 +/- ...e-15] + [1.570796326794897 +/- ...e-16]*I
            sage: CBF(2*i).arcsinh(analytic=True)
            nan + nan*I"""
    @overload
    def arcsinh(self) -> Any:
        """ComplexBall.arcsinh(self, analytic=False)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3484)

        Return the hyperbolic arcsine of this ball.

        INPUT:

        - ``analytic`` -- boolean (default: ``False``); if ``True``, return an
          indeterminate (not-a-number) value when the input ball touches
          the branch cut

        EXAMPLES::

            sage: CBF(1+i).arcsinh()
            [1.06127506190504 +/- ...e-15] + [0.66623943249252 +/- ...e-15]*I
            sage: CBF(2*i).arcsinh()
            [1.31695789692482 +/- ...e-15] + [1.570796326794897 +/- ...e-16]*I
            sage: CBF(2*i).arcsinh(analytic=True)
            nan + nan*I"""
    @overload
    def arcsinh(self, analytic=...) -> Any:
        """ComplexBall.arcsinh(self, analytic=False)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3484)

        Return the hyperbolic arcsine of this ball.

        INPUT:

        - ``analytic`` -- boolean (default: ``False``); if ``True``, return an
          indeterminate (not-a-number) value when the input ball touches
          the branch cut

        EXAMPLES::

            sage: CBF(1+i).arcsinh()
            [1.06127506190504 +/- ...e-15] + [0.66623943249252 +/- ...e-15]*I
            sage: CBF(2*i).arcsinh()
            [1.31695789692482 +/- ...e-15] + [1.570796326794897 +/- ...e-16]*I
            sage: CBF(2*i).arcsinh(analytic=True)
            nan + nan*I"""
    @overload
    def arctan(self, analytic=...) -> Any:
        """ComplexBall.arctan(self, analytic=False)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3453)

        Return the arctangent of this ball.

        INPUT:

        - ``analytic`` -- boolean (default: ``False``); if ``True``, return an
          indeterminate (not-a-number) value when the input ball touches
          the branch cut

        EXAMPLES::

            sage: CBF(1+i).arctan()
            [1.017221967897851 +/- ...e-16] + [0.4023594781085251 +/- ...e-17]*I
            sage: CBF(i).arctan()
            nan + nan*I
            sage: CBF(2*i).arctan()
            [1.570796326794897 +/- ...e-16] + [0.549306144334055 +/- ...e-16]*I
            sage: CBF(2*i).arctan(analytic=True)
            nan + nan*I"""
    @overload
    def arctan(self) -> Any:
        """ComplexBall.arctan(self, analytic=False)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3453)

        Return the arctangent of this ball.

        INPUT:

        - ``analytic`` -- boolean (default: ``False``); if ``True``, return an
          indeterminate (not-a-number) value when the input ball touches
          the branch cut

        EXAMPLES::

            sage: CBF(1+i).arctan()
            [1.017221967897851 +/- ...e-16] + [0.4023594781085251 +/- ...e-17]*I
            sage: CBF(i).arctan()
            nan + nan*I
            sage: CBF(2*i).arctan()
            [1.570796326794897 +/- ...e-16] + [0.549306144334055 +/- ...e-16]*I
            sage: CBF(2*i).arctan(analytic=True)
            nan + nan*I"""
    @overload
    def arctan(self) -> Any:
        """ComplexBall.arctan(self, analytic=False)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3453)

        Return the arctangent of this ball.

        INPUT:

        - ``analytic`` -- boolean (default: ``False``); if ``True``, return an
          indeterminate (not-a-number) value when the input ball touches
          the branch cut

        EXAMPLES::

            sage: CBF(1+i).arctan()
            [1.017221967897851 +/- ...e-16] + [0.4023594781085251 +/- ...e-17]*I
            sage: CBF(i).arctan()
            nan + nan*I
            sage: CBF(2*i).arctan()
            [1.570796326794897 +/- ...e-16] + [0.549306144334055 +/- ...e-16]*I
            sage: CBF(2*i).arctan(analytic=True)
            nan + nan*I"""
    @overload
    def arctan(self) -> Any:
        """ComplexBall.arctan(self, analytic=False)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3453)

        Return the arctangent of this ball.

        INPUT:

        - ``analytic`` -- boolean (default: ``False``); if ``True``, return an
          indeterminate (not-a-number) value when the input ball touches
          the branch cut

        EXAMPLES::

            sage: CBF(1+i).arctan()
            [1.017221967897851 +/- ...e-16] + [0.4023594781085251 +/- ...e-17]*I
            sage: CBF(i).arctan()
            nan + nan*I
            sage: CBF(2*i).arctan()
            [1.570796326794897 +/- ...e-16] + [0.549306144334055 +/- ...e-16]*I
            sage: CBF(2*i).arctan(analytic=True)
            nan + nan*I"""
    @overload
    def arctan(self, analytic=...) -> Any:
        """ComplexBall.arctan(self, analytic=False)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3453)

        Return the arctangent of this ball.

        INPUT:

        - ``analytic`` -- boolean (default: ``False``); if ``True``, return an
          indeterminate (not-a-number) value when the input ball touches
          the branch cut

        EXAMPLES::

            sage: CBF(1+i).arctan()
            [1.017221967897851 +/- ...e-16] + [0.4023594781085251 +/- ...e-17]*I
            sage: CBF(i).arctan()
            nan + nan*I
            sage: CBF(2*i).arctan()
            [1.570796326794897 +/- ...e-16] + [0.549306144334055 +/- ...e-16]*I
            sage: CBF(2*i).arctan(analytic=True)
            nan + nan*I"""
    @overload
    def arctanh(self, analytic=...) -> Any:
        """ComplexBall.arctanh(self, analytic=False)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3542)

        Return the hyperbolic arctangent of this ball.

        INPUT:

        - ``analytic`` -- boolean (default: ``False``); if ``True``, return an
          indeterminate (not-a-number) value when the input ball touches
          the branch cut

        EXAMPLES::

            sage: CBF(1+i).arctanh()
            [0.4023594781085251 +/- ...e-17] + [1.017221967897851 +/- ...e-16]*I
            sage: CBF(-2).arctanh()
            [-0.549306144334055 +/- ...e-16] + [1.570796326794897 +/- ...e-16]*I
            sage: CBF(-2).arctanh(analytic=True)
            nan + nan*I"""
    @overload
    def arctanh(self) -> Any:
        """ComplexBall.arctanh(self, analytic=False)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3542)

        Return the hyperbolic arctangent of this ball.

        INPUT:

        - ``analytic`` -- boolean (default: ``False``); if ``True``, return an
          indeterminate (not-a-number) value when the input ball touches
          the branch cut

        EXAMPLES::

            sage: CBF(1+i).arctanh()
            [0.4023594781085251 +/- ...e-17] + [1.017221967897851 +/- ...e-16]*I
            sage: CBF(-2).arctanh()
            [-0.549306144334055 +/- ...e-16] + [1.570796326794897 +/- ...e-16]*I
            sage: CBF(-2).arctanh(analytic=True)
            nan + nan*I"""
    @overload
    def arctanh(self) -> Any:
        """ComplexBall.arctanh(self, analytic=False)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3542)

        Return the hyperbolic arctangent of this ball.

        INPUT:

        - ``analytic`` -- boolean (default: ``False``); if ``True``, return an
          indeterminate (not-a-number) value when the input ball touches
          the branch cut

        EXAMPLES::

            sage: CBF(1+i).arctanh()
            [0.4023594781085251 +/- ...e-17] + [1.017221967897851 +/- ...e-16]*I
            sage: CBF(-2).arctanh()
            [-0.549306144334055 +/- ...e-16] + [1.570796326794897 +/- ...e-16]*I
            sage: CBF(-2).arctanh(analytic=True)
            nan + nan*I"""
    @overload
    def arctanh(self, analytic=...) -> Any:
        """ComplexBall.arctanh(self, analytic=False)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3542)

        Return the hyperbolic arctangent of this ball.

        INPUT:

        - ``analytic`` -- boolean (default: ``False``); if ``True``, return an
          indeterminate (not-a-number) value when the input ball touches
          the branch cut

        EXAMPLES::

            sage: CBF(1+i).arctanh()
            [0.4023594781085251 +/- ...e-17] + [1.017221967897851 +/- ...e-16]*I
            sage: CBF(-2).arctanh()
            [-0.549306144334055 +/- ...e-16] + [1.570796326794897 +/- ...e-16]*I
            sage: CBF(-2).arctanh(analytic=True)
            nan + nan*I"""
    @overload
    def arg(self) -> Any:
        """ComplexBall.arg(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 1990)

        Return the argument of this complex ball.

        EXAMPLES::

            sage: CBF(1 + i).arg()
            [0.7853981633974483 +/- ...e-17]
            sage: CBF(-1).arg()
            [3.141592653589793 +/- ...e-16]
            sage: CBF(-1).arg().parent()
            Real ball field with 53 bits of precision"""
    @overload
    def arg(self) -> Any:
        """ComplexBall.arg(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 1990)

        Return the argument of this complex ball.

        EXAMPLES::

            sage: CBF(1 + i).arg()
            [0.7853981633974483 +/- ...e-17]
            sage: CBF(-1).arg()
            [3.141592653589793 +/- ...e-16]
            sage: CBF(-1).arg().parent()
            Real ball field with 53 bits of precision"""
    @overload
    def arg(self) -> Any:
        """ComplexBall.arg(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 1990)

        Return the argument of this complex ball.

        EXAMPLES::

            sage: CBF(1 + i).arg()
            [0.7853981633974483 +/- ...e-17]
            sage: CBF(-1).arg()
            [3.141592653589793 +/- ...e-16]
            sage: CBF(-1).arg().parent()
            Real ball field with 53 bits of precision"""
    @overload
    def arg(self) -> Any:
        """ComplexBall.arg(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 1990)

        Return the argument of this complex ball.

        EXAMPLES::

            sage: CBF(1 + i).arg()
            [0.7853981633974483 +/- ...e-17]
            sage: CBF(-1).arg()
            [3.141592653589793 +/- ...e-16]
            sage: CBF(-1).arg().parent()
            Real ball field with 53 bits of precision"""
    @overload
    def barnes_g(self) -> Any:
        """ComplexBall.barnes_g(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3800)

        Return the Barnes G-function of ``self``.

        EXAMPLES::

            sage: CBF(-4).barnes_g()
            0
            sage: CBF(8).barnes_g()
            24883200.00000000
            sage: CBF(500,10).barnes_g()
            [4.54078781e+254873 +/- ...e+254864] + [8.65835455e+254873 +/- ...e+254864]*I"""
    @overload
    def barnes_g(self) -> Any:
        """ComplexBall.barnes_g(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3800)

        Return the Barnes G-function of ``self``.

        EXAMPLES::

            sage: CBF(-4).barnes_g()
            0
            sage: CBF(8).barnes_g()
            24883200.00000000
            sage: CBF(500,10).barnes_g()
            [4.54078781e+254873 +/- ...e+254864] + [8.65835455e+254873 +/- ...e+254864]*I"""
    @overload
    def barnes_g(self) -> Any:
        """ComplexBall.barnes_g(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3800)

        Return the Barnes G-function of ``self``.

        EXAMPLES::

            sage: CBF(-4).barnes_g()
            0
            sage: CBF(8).barnes_g()
            24883200.00000000
            sage: CBF(500,10).barnes_g()
            [4.54078781e+254873 +/- ...e+254864] + [8.65835455e+254873 +/- ...e+254864]*I"""
    @overload
    def barnes_g(self) -> Any:
        """ComplexBall.barnes_g(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3800)

        Return the Barnes G-function of ``self``.

        EXAMPLES::

            sage: CBF(-4).barnes_g()
            0
            sage: CBF(8).barnes_g()
            24883200.00000000
            sage: CBF(500,10).barnes_g()
            [4.54078781e+254873 +/- ...e+254864] + [8.65835455e+254873 +/- ...e+254864]*I"""
    @overload
    def below_abs(self, test_zero=...) -> Any:
        """ComplexBall.below_abs(self, test_zero=False)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 1931)

        Return a lower bound for the absolute value of this complex ball.

        INPUT:

        - ``test_zero`` -- boolean (default: ``False``); if ``True``,
          make sure that the returned lower bound is positive, raising
          an error if the ball contains zero.

        OUTPUT: a ball with zero radius

        EXAMPLES::

            sage: b = ComplexBallField(8)(1+i).below_abs()
            sage: b
            [1.4 +/- 0.0141]
            sage: b.is_exact()
            True
            sage: QQ(b)*128
            181
            sage: (CBF(1/3) - 1/3).below_abs()
            0
            sage: (CBF(1/3) - 1/3).below_abs(test_zero=True)
            Traceback (most recent call last):
            ...
            ValueError: ball contains zero

        .. SEEALSO:: :meth:`above_abs`"""
    @overload
    def below_abs(self) -> Any:
        """ComplexBall.below_abs(self, test_zero=False)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 1931)

        Return a lower bound for the absolute value of this complex ball.

        INPUT:

        - ``test_zero`` -- boolean (default: ``False``); if ``True``,
          make sure that the returned lower bound is positive, raising
          an error if the ball contains zero.

        OUTPUT: a ball with zero radius

        EXAMPLES::

            sage: b = ComplexBallField(8)(1+i).below_abs()
            sage: b
            [1.4 +/- 0.0141]
            sage: b.is_exact()
            True
            sage: QQ(b)*128
            181
            sage: (CBF(1/3) - 1/3).below_abs()
            0
            sage: (CBF(1/3) - 1/3).below_abs(test_zero=True)
            Traceback (most recent call last):
            ...
            ValueError: ball contains zero

        .. SEEALSO:: :meth:`above_abs`"""
    @overload
    def below_abs(self) -> Any:
        """ComplexBall.below_abs(self, test_zero=False)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 1931)

        Return a lower bound for the absolute value of this complex ball.

        INPUT:

        - ``test_zero`` -- boolean (default: ``False``); if ``True``,
          make sure that the returned lower bound is positive, raising
          an error if the ball contains zero.

        OUTPUT: a ball with zero radius

        EXAMPLES::

            sage: b = ComplexBallField(8)(1+i).below_abs()
            sage: b
            [1.4 +/- 0.0141]
            sage: b.is_exact()
            True
            sage: QQ(b)*128
            181
            sage: (CBF(1/3) - 1/3).below_abs()
            0
            sage: (CBF(1/3) - 1/3).below_abs(test_zero=True)
            Traceback (most recent call last):
            ...
            ValueError: ball contains zero

        .. SEEALSO:: :meth:`above_abs`"""
    @overload
    def below_abs(self, test_zero=...) -> Any:
        """ComplexBall.below_abs(self, test_zero=False)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 1931)

        Return a lower bound for the absolute value of this complex ball.

        INPUT:

        - ``test_zero`` -- boolean (default: ``False``); if ``True``,
          make sure that the returned lower bound is positive, raising
          an error if the ball contains zero.

        OUTPUT: a ball with zero radius

        EXAMPLES::

            sage: b = ComplexBallField(8)(1+i).below_abs()
            sage: b
            [1.4 +/- 0.0141]
            sage: b.is_exact()
            True
            sage: QQ(b)*128
            181
            sage: (CBF(1/3) - 1/3).below_abs()
            0
            sage: (CBF(1/3) - 1/3).below_abs(test_zero=True)
            Traceback (most recent call last):
            ...
            ValueError: ball contains zero

        .. SEEALSO:: :meth:`above_abs`"""
    def bessel_I(self, nu) -> Any:
        """ComplexBall.bessel_I(self, nu)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4200)

        Return the modified Bessel function of the first kind with argument ``self``
        and index ``nu``.

        EXAMPLES::

            sage: CBF(1, 1).bessel_I(1)
            [0.365028028827088 +/- ...e-16] + [0.614160334922903 +/- ...e-16]*I
            sage: CBF(100, -100).bessel_I(1/3)
            [5.4362189595644e+41 +/- ...e+27] + [7.1989436985321e+41 +/- ...e+27]*I"""
    def bessel_J(self, nu) -> Any:
        """ComplexBall.bessel_J(self, nu)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4140)

        Return the Bessel function of the first kind with argument ``self``
        and index ``nu``.

        EXAMPLES::

            sage: CBF(1, 1).bessel_J(1)
            [0.614160334922903 +/- ...e-16] + [0.365028028827088 +/- ...e-16]*I
            sage: CBF(100, -100).bessel_J(1/3)
            [1.108431870251e+41 +/- ...e+28] + [-8.952577603125e+41 +/- ...e+28]*I"""
    def bessel_J_Y(self, nu) -> Any:
        """ComplexBall.bessel_J_Y(self, nu)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4159)

        Return the Bessel function of the first and second kind with argument
        ``self`` and index ``nu``, computed simultaneously.

        EXAMPLES::

            sage: J, Y = CBF(1, 1).bessel_J_Y(1)
            sage: J - CBF(1, 1).bessel_J(1)
            [+/- ...e-16] + [+/- ...e-16]*I
            sage: Y - CBF(1, 1).bessel_Y(1)
            [+/- ...e-14] + [+/- ...e-14]*I"""
    def bessel_K(self, nu) -> Any:
        """ComplexBall.bessel_K(self, nu)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4219)

        Return the modified Bessel function of the second kind with argument
        ``self`` and index ``nu``.

        EXAMPLES::

            sage: CBF(1, 1).bessel_K(0)
            [0.08019772694652 +/- ...e-15] + [-0.357277459285330 +/- ...e-16]*I
            sage: CBF(1, 1).bessel_K(1)
            [0.02456830552374 +/- ...e-15] + [-0.45971947380119 +/- ...e-15]*I
            sage: CBF(100, 100).bessel_K(QQbar(i))
            [3.8693896656383e-45 +/- ...e-59] + [5.507100423418e-46 +/- ...e-59]*I"""
    def bessel_Y(self, nu) -> Any:
        """ComplexBall.bessel_Y(self, nu)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4181)

        Return the Bessel function of the second kind with argument ``self``
        and index ``nu``.

        EXAMPLES::

            sage: CBF(1, 1).bessel_Y(1)
            [-0.6576945355913 +/- ...e-14] + [0.6298010039929 +/- ...e-14]*I
            sage: CBF(100, -100).bessel_Y(1/3)
            [-8.952577603125e+41 +/- ...e+28] + [-1.108431870251e+41 +/- ...e+28]*I"""
    def chebyshev_T(self, n) -> Any:
        """ComplexBall.chebyshev_T(self, n)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4966)

        Return the Chebyshev function of the first kind of order ``n``
        evaluated at ``self``.

        EXAMPLES::

            sage: CBF(1/3).chebyshev_T(20)
            [0.8710045668809 +/- ...e-14]
            sage: CBF(1/3).chebyshev_T(CBF(5,1))
            [1.84296854518763 +/- ...e-15] + [0.20053614301799 +/- ...e-15]*I"""
    def chebyshev_U(self, n) -> Any:
        """ComplexBall.chebyshev_U(self, n)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4985)

        Return the Chebyshev function of the second kind of order ``n``
        evaluated at ``self``.

        EXAMPLES::

            sage: CBF(1/3).chebyshev_U(20)
            [0.6973126541184 +/- ...e-14]
            sage: CBF(1/3).chebyshev_U(CBF(5,1))
            [1.75884964893425 +/- ...e-15] + [0.7497317165104 +/- ...e-14]*I"""
    @overload
    def conjugate(self) -> Any:
        """ComplexBall.conjugate(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 2663)

        Return the complex conjugate of this ball.

        EXAMPLES::

            sage: CBF(-2 + I/3).conjugate()
            -2.000000000000000 + [-0.3333333333333333 +/- ...e-17]*I"""
    @overload
    def conjugate(self) -> Any:
        """ComplexBall.conjugate(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 2663)

        Return the complex conjugate of this ball.

        EXAMPLES::

            sage: CBF(-2 + I/3).conjugate()
            -2.000000000000000 + [-0.3333333333333333 +/- ...e-17]*I"""
    def contains_exact(self, other) -> Any:
        """ComplexBall.contains_exact(self, other)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 2544)

        Return ``True`` *iff* ``other`` is contained in ``self``.

        Use ``other in self`` for a test that works for a wider range of inputs
        but may return false negatives.

        INPUT:

        - ``other`` -- :class:`ComplexBall`,
          :class:`~sage.rings.integer.Integer`,
          or :class:`~sage.rings.rational.Rational`

        EXAMPLES::

            sage: CBF(RealBallField(100)(1/3), 0).contains_exact(1/3)
            True
            sage: CBF(1).contains_exact(1)
            True
            sage: CBF(1).contains_exact(CBF(1))
            True

            sage: CBF(sqrt(2)).contains_exact(sqrt(2))                                  # needs sage.symbolic
            Traceback (most recent call last):
            ...
            TypeError: unsupported type: <class 'sage.symbolic.expression.Expression'>"""
    @overload
    def contains_integer(self) -> Any:
        """ComplexBall.contains_integer(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 2635)

        Return ``True`` iff this ball contains any integer.

        EXAMPLES::

            sage: CBF(3, RBF(0.1)).contains_integer()
            False
            sage: CBF(3, RBF(0.1,0.1)).contains_integer()
            True"""
    @overload
    def contains_integer(self) -> Any:
        """ComplexBall.contains_integer(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 2635)

        Return ``True`` iff this ball contains any integer.

        EXAMPLES::

            sage: CBF(3, RBF(0.1)).contains_integer()
            False
            sage: CBF(3, RBF(0.1,0.1)).contains_integer()
            True"""
    @overload
    def contains_integer(self) -> Any:
        """ComplexBall.contains_integer(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 2635)

        Return ``True`` iff this ball contains any integer.

        EXAMPLES::

            sage: CBF(3, RBF(0.1)).contains_integer()
            False
            sage: CBF(3, RBF(0.1,0.1)).contains_integer()
            True"""
    @overload
    def contains_zero(self) -> Any:
        """ComplexBall.contains_zero(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 2620)

        Return ``True`` iff this ball contains zero.

        EXAMPLES::

            sage: CBF(0).contains_zero()
            True
            sage: CBF(RIF(-1,1)).contains_zero()
            True
            sage: CBF(i).contains_zero()
            False"""
    @overload
    def contains_zero(self) -> Any:
        """ComplexBall.contains_zero(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 2620)

        Return ``True`` iff this ball contains zero.

        EXAMPLES::

            sage: CBF(0).contains_zero()
            True
            sage: CBF(RIF(-1,1)).contains_zero()
            True
            sage: CBF(i).contains_zero()
            False"""
    @overload
    def contains_zero(self) -> Any:
        """ComplexBall.contains_zero(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 2620)

        Return ``True`` iff this ball contains zero.

        EXAMPLES::

            sage: CBF(0).contains_zero()
            True
            sage: CBF(RIF(-1,1)).contains_zero()
            True
            sage: CBF(i).contains_zero()
            False"""
    @overload
    def contains_zero(self) -> Any:
        """ComplexBall.contains_zero(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 2620)

        Return ``True`` iff this ball contains zero.

        EXAMPLES::

            sage: CBF(0).contains_zero()
            True
            sage: CBF(RIF(-1,1)).contains_zero()
            True
            sage: CBF(i).contains_zero()
            False"""
    @overload
    def cos(self) -> Any:
        """ComplexBall.cos(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3220)

        Return the cosine of this ball.

        EXAMPLES::

            sage: CBF(i*pi).cos()                                                       # needs sage.symbolic
            [11.59195327552152 +/- ...e-15]"""
    @overload
    def cos(self) -> Any:
        """ComplexBall.cos(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3220)

        Return the cosine of this ball.

        EXAMPLES::

            sage: CBF(i*pi).cos()                                                       # needs sage.symbolic
            [11.59195327552152 +/- ...e-15]"""
    def cos_integral(self, *args, **kwargs):
        """ComplexBall.Ci(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4305)

        Return the cosine integral with argument ``self``.

        EXAMPLES::

            sage: CBF(1, 1).Ci()  # abs tol 5e-16
            [0.882172180555936 +/- 5.89e-16] + [0.287249133519956 +/- 3.37e-16]*I
            sage: CBF(0).Ci()
            nan + nan*I

        TESTS:

            sage: CBF(Ci(I))  # abs tol 5e-16                                           # needs sage.symbolic
            [0.837866940980208 +/- 4.72e-16] + [1.570796326794897 +/- 5.54e-16]*I"""
    @overload
    def cosh(self) -> Any:
        """ComplexBall.cosh(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3314)

        Return the hyperbolic cosine of this ball.

        EXAMPLES::

            sage: CBF(1, 1).cosh()
            [0.833730025131149 +/- ...e-16] + [0.988897705762865 +/- ...e-16]*I"""
    @overload
    def cosh(self) -> Any:
        """ComplexBall.cosh(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3314)

        Return the hyperbolic cosine of this ball.

        EXAMPLES::

            sage: CBF(1, 1).cosh()
            [0.833730025131149 +/- ...e-16] + [0.988897705762865 +/- ...e-16]*I"""
    def cosh_integral(self, *args, **kwargs):
        """ComplexBall.Chi(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4353)

        Return the hyperbolic cosine integral with argument ``self``.

        EXAMPLES::

            sage: CBF(1, 1).Chi()  # abs tol 1e-15
            [0.882172180555936 +/- 5.89e-16] + [1.28354719327494 +/- 1.01e-15]*I
            sage: CBF(0).Chi()
            nan + nan*I

        TESTS:

            sage: CBF(Chi(I))  # abs tol 5e-16                                          # needs sage.symbolic
            [0.337403922900968 +/- 3.25e-16] + [1.570796326794897 +/- 5.54e-16]*I"""
    @overload
    def cot(self) -> Any:
        """ComplexBall.cot(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3252)

        Return the cotangent of this ball.

        EXAMPLES::

            sage: CBF(pi, 1/10).cot()                                                   # needs sage.symbolic
            [+/- ...e-14] + [-10.03331113225399 +/- ...e-15]*I
            sage: CBF(pi).cot()                                                         # needs sage.symbolic
            nan"""
    @overload
    def cot(self) -> Any:
        """ComplexBall.cot(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3252)

        Return the cotangent of this ball.

        EXAMPLES::

            sage: CBF(pi, 1/10).cot()                                                   # needs sage.symbolic
            [+/- ...e-14] + [-10.03331113225399 +/- ...e-15]*I
            sage: CBF(pi).cot()                                                         # needs sage.symbolic
            nan"""
    @overload
    def cot(self) -> Any:
        """ComplexBall.cot(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3252)

        Return the cotangent of this ball.

        EXAMPLES::

            sage: CBF(pi, 1/10).cot()                                                   # needs sage.symbolic
            [+/- ...e-14] + [-10.03331113225399 +/- ...e-15]*I
            sage: CBF(pi).cot()                                                         # needs sage.symbolic
            nan"""
    @overload
    def coth(self) -> Any:
        """ComplexBall.coth(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3346)

        Return the hyperbolic cotangent of this ball.

        EXAMPLES::

            sage: CBF(1, 1).coth()
            [0.868014142895925 +/- ...e-16] + [-0.2176215618544027 +/- ...e-17]*I
            sage: CBF(0, pi).coth()                                                     # needs sage.symbolic
            nan*I"""
    @overload
    def coth(self) -> Any:
        """ComplexBall.coth(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3346)

        Return the hyperbolic cotangent of this ball.

        EXAMPLES::

            sage: CBF(1, 1).coth()
            [0.868014142895925 +/- ...e-16] + [-0.2176215618544027 +/- ...e-17]*I
            sage: CBF(0, pi).coth()                                                     # needs sage.symbolic
            nan*I"""
    @overload
    def coth(self) -> Any:
        """ComplexBall.coth(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3346)

        Return the hyperbolic cotangent of this ball.

        EXAMPLES::

            sage: CBF(1, 1).coth()
            [0.868014142895925 +/- ...e-16] + [-0.2176215618544027 +/- ...e-17]*I
            sage: CBF(0, pi).coth()                                                     # needs sage.symbolic
            nan*I"""
    @overload
    def csc(self) -> Any:
        """ComplexBall.csc(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3284)

        Return the cosecant of this ball.

        EXAMPLES::

            sage: CBF(1, 1).csc()
            [0.621518017170428 +/- ...e-16] + [-0.303931001628426 +/- ...e-16]*I"""
    @overload
    def csc(self) -> Any:
        """ComplexBall.csc(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3284)

        Return the cosecant of this ball.

        EXAMPLES::

            sage: CBF(1, 1).csc()
            [0.621518017170428 +/- ...e-16] + [-0.303931001628426 +/- ...e-16]*I"""
    @overload
    def csch(self) -> Any:
        """ComplexBall.csch(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3378)

        Return the hyperbolic cosecant of this ball.

        EXAMPLES::

            sage: CBF(1, 1).csch()
            [0.303931001628426 +/- ...e-16] + [-0.621518017170428 +/- ...e-16]*I
            sage: CBF(i*pi).csch()                                                      # needs sage.symbolic
            nan*I"""
    @overload
    def csch(self) -> Any:
        """ComplexBall.csch(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3378)

        Return the hyperbolic cosecant of this ball.

        EXAMPLES::

            sage: CBF(1, 1).csch()
            [0.303931001628426 +/- ...e-16] + [-0.621518017170428 +/- ...e-16]*I
            sage: CBF(i*pi).csch()                                                      # needs sage.symbolic
            nan*I"""
    @overload
    def csch(self) -> Any:
        """ComplexBall.csch(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3378)

        Return the hyperbolic cosecant of this ball.

        EXAMPLES::

            sage: CBF(1, 1).csch()
            [0.303931001628426 +/- ...e-16] + [-0.621518017170428 +/- ...e-16]*I
            sage: CBF(i*pi).csch()                                                      # needs sage.symbolic
            nan*I"""
    @overload
    def cube(self) -> Any:
        """ComplexBall.cube(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3030)

        Return the cube of this ball.

        The result is computed efficiently using two real squarings, two real
        multiplications, and scalar operations.

        EXAMPLES::

            sage: CBF(1, 1).cube()
            -2.000000000000000 + 2.000000000000000*I"""
    @overload
    def cube(self) -> Any:
        """ComplexBall.cube(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3030)

        Return the cube of this ball.

        The result is computed efficiently using two real squarings, two real
        multiplications, and scalar operations.

        EXAMPLES::

            sage: CBF(1, 1).cube()
            -2.000000000000000 + 2.000000000000000*I"""
    @overload
    def diameter(self) -> Any:
        """ComplexBall.diameter(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 2117)

        Return the diameter of this ball.

        EXAMPLES::

            sage: CBF(1 + i).diameter()
            0.00000000
            sage: CBF(i/3).diameter()
            2.2204460e-16
            sage: CBF(i/3).diameter().parent()
            Real Field with 30 bits of precision
            sage: CBF(CIF(RIF(1.02, 1.04), RIF(2.1, 2.2))).diameter()
            0.20000000

        .. SEEALSO:: :meth:`rad`, :meth:`mid`"""
    @overload
    def diameter(self) -> Any:
        """ComplexBall.diameter(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 2117)

        Return the diameter of this ball.

        EXAMPLES::

            sage: CBF(1 + i).diameter()
            0.00000000
            sage: CBF(i/3).diameter()
            2.2204460e-16
            sage: CBF(i/3).diameter().parent()
            Real Field with 30 bits of precision
            sage: CBF(CIF(RIF(1.02, 1.04), RIF(2.1, 2.2))).diameter()
            0.20000000

        .. SEEALSO:: :meth:`rad`, :meth:`mid`"""
    @overload
    def diameter(self) -> Any:
        """ComplexBall.diameter(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 2117)

        Return the diameter of this ball.

        EXAMPLES::

            sage: CBF(1 + i).diameter()
            0.00000000
            sage: CBF(i/3).diameter()
            2.2204460e-16
            sage: CBF(i/3).diameter().parent()
            Real Field with 30 bits of precision
            sage: CBF(CIF(RIF(1.02, 1.04), RIF(2.1, 2.2))).diameter()
            0.20000000

        .. SEEALSO:: :meth:`rad`, :meth:`mid`"""
    @overload
    def diameter(self) -> Any:
        """ComplexBall.diameter(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 2117)

        Return the diameter of this ball.

        EXAMPLES::

            sage: CBF(1 + i).diameter()
            0.00000000
            sage: CBF(i/3).diameter()
            2.2204460e-16
            sage: CBF(i/3).diameter().parent()
            Real Field with 30 bits of precision
            sage: CBF(CIF(RIF(1.02, 1.04), RIF(2.1, 2.2))).diameter()
            0.20000000

        .. SEEALSO:: :meth:`rad`, :meth:`mid`"""
    @overload
    def diameter(self) -> Any:
        """ComplexBall.diameter(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 2117)

        Return the diameter of this ball.

        EXAMPLES::

            sage: CBF(1 + i).diameter()
            0.00000000
            sage: CBF(i/3).diameter()
            2.2204460e-16
            sage: CBF(i/3).diameter().parent()
            Real Field with 30 bits of precision
            sage: CBF(CIF(RIF(1.02, 1.04), RIF(2.1, 2.2))).diameter()
            0.20000000

        .. SEEALSO:: :meth:`rad`, :meth:`mid`"""
    def eisenstein(self, longn) -> Any:
        """ComplexBall.eisenstein(self, long n)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4556)

        Return the first ``n`` entries in the sequence of Eisenstein series
        `G_4(\\tau), G_6(\\tau), G_8(\\tau), \\ldots` where *tau* is given
        by ``self``. The output is a list.

        EXAMPLES::

            sage: a, b, c, d = 2, 5, 1, 3
            sage: tau = CBF(1,3)
            sage: tau.eisenstein(4)
            [[2.1646498507193 +/- ...e-14],
             [2.0346794456073 +/- ...e-14],
             [2.0081609898081 +/- ...e-14],
             [2.0019857082706 +/- ...e-14]]
            sage: ((a*tau+b)/(c*tau+d)).eisenstein(3)[2]
            [331011.2004330 +/- ...e-8] + [-711178.1655746 +/- ...e-8]*I
            sage: (c*tau+d)^8 * tau.eisenstein(3)[2]
            [331011.20043304 +/- ...e-9] + [-711178.1655746 +/- ...e-8]*I"""
    @overload
    def elliptic_e(self) -> Any:
        """ComplexBall.elliptic_e(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4703)

        Return the complete elliptic integral of the second kind evaluated
        at *m* given by ``self``.

        EXAMPLES::

            sage: CBF(2,3).elliptic_e()
            [1.472797144959 +/- ...e-13] + [-1.231604783936 +/- ...e-14]*I"""
    @overload
    def elliptic_e(self) -> Any:
        """ComplexBall.elliptic_e(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4703)

        Return the complete elliptic integral of the second kind evaluated
        at *m* given by ``self``.

        EXAMPLES::

            sage: CBF(2,3).elliptic_e()
            [1.472797144959 +/- ...e-13] + [-1.231604783936 +/- ...e-14]*I"""
    def elliptic_e_inc(self, m) -> Any:
        """ComplexBall.elliptic_e_inc(self, m)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4773)

        Return the incomplete elliptic integral of the second kind evaluated
        at *m*.

        See :meth:`elliptic_e` for the corresponding complete integral

        INPUT:

        - ``m`` -- complex ball

        EXAMPLES::

            sage: CBF(1,2).elliptic_e_inc(CBF(0,1))
            [1.906576998914 +/- ...e-13] + [3.6896645289411 +/- ...e-14]*I

        At parameter `\\pi/2` it is a complete integral::

            sage: phi = CBF(1,1)
            sage: (CBF.pi()/2).elliptic_e_inc(phi)
            [1.2838409578982 +/- ...e-14] + [-0.5317843366915 +/- ...e-14]*I
            sage: phi.elliptic_e()
            [1.2838409578982 +/- 5...e-14] + [-0.5317843366915 +/- 3...e-14]*I

            sage: phi = CBF(2, 3/7)
            sage: (CBF.pi()/2).elliptic_e_inc(phi)
            [0.787564350925 +/- ...e-13] + [-0.686896129145 +/- ...e-13]*I
            sage: phi.elliptic_e()
            [0.7875643509254 +/- ...e-14] + [-0.686896129145 +/- ...e-13]*I"""
    def elliptic_f(self, m) -> Any:
        """ComplexBall.elliptic_f(self, m)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4736)

        Return the incomplete elliptic integral of the first kind evaluated
        at *m*.

        See :meth:`elliptic_k` for the corresponding complete integral

        INPUT:

        - ``m`` -- complex ball

        EXAMPLES::

            sage: CBF(1,2).elliptic_f(CBF(0,1))
            [0.6821522911854 +/- ...e-14] + [1.2482780628143 +/- ...e-14]*I

        At parameter `\\pi/2` it is a complete integral::

            sage: phi = CBF(1,1)
            sage: (CBF.pi()/2).elliptic_f(phi)
            [1.5092369540513 +/- ...e-14] + [0.6251464152027 +/- ...e-15]*I
            sage: phi.elliptic_k()
            [1.50923695405127 +/- ...e-15] + [0.62514641520270 +/- ...e-15]*I

            sage: phi = CBF(2, 3/7)
            sage: (CBF.pi()/2).elliptic_f(phi)
            [1.3393589639094 +/- ...e-14] + [1.1104369690719 +/- ...e-14]*I
            sage: phi.elliptic_k()
            [1.33935896390938 +/- ...e-15] + [1.11043696907194 +/- ...e-15]*I"""
    @overload
    def elliptic_invariants(self) -> Any:
        """ComplexBall.elliptic_invariants(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4645)

        Return the lattice invariants ``(g2, g3)``.

        EXAMPLES::

            sage: CBF(0,1).elliptic_invariants()
            ([189.07272012923 +/- ...e-12], [+/- ...e-12])
            sage: CBF(sqrt(2)/2, sqrt(2)/2).elliptic_invariants()                       # needs sage.symbolic
            ([+/- ...e-12] + [-332.5338031465...]*I,
             [1254.46842157...] + [1254.46842157...]*I)"""
    @overload
    def elliptic_invariants(self) -> Any:
        """ComplexBall.elliptic_invariants(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4645)

        Return the lattice invariants ``(g2, g3)``.

        EXAMPLES::

            sage: CBF(0,1).elliptic_invariants()
            ([189.07272012923 +/- ...e-12], [+/- ...e-12])
            sage: CBF(sqrt(2)/2, sqrt(2)/2).elliptic_invariants()                       # needs sage.symbolic
            ([+/- ...e-12] + [-332.5338031465...]*I,
             [1254.46842157...] + [1254.46842157...]*I)"""
    @overload
    def elliptic_invariants(self) -> Any:
        """ComplexBall.elliptic_invariants(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4645)

        Return the lattice invariants ``(g2, g3)``.

        EXAMPLES::

            sage: CBF(0,1).elliptic_invariants()
            ([189.07272012923 +/- ...e-12], [+/- ...e-12])
            sage: CBF(sqrt(2)/2, sqrt(2)/2).elliptic_invariants()                       # needs sage.symbolic
            ([+/- ...e-12] + [-332.5338031465...]*I,
             [1254.46842157...] + [1254.46842157...]*I)"""
    @overload
    def elliptic_k(self) -> Any:
        """ComplexBall.elliptic_k(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4687)

        Return the complete elliptic integral of the first kind evaluated
        at *m* given by ``self``.

        EXAMPLES::

            sage: CBF(2,3).elliptic_k()
            [1.04291329192852 +/- ...e-15] + [0.62968247230864 +/- ...e-15]*I"""
    @overload
    def elliptic_k(self) -> Any:
        """ComplexBall.elliptic_k(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4687)

        Return the complete elliptic integral of the first kind evaluated
        at *m* given by ``self``.

        EXAMPLES::

            sage: CBF(2,3).elliptic_k()
            [1.04291329192852 +/- ...e-15] + [0.62968247230864 +/- ...e-15]*I"""
    @overload
    def elliptic_p(self, tau, n=...) -> Any:
        """ComplexBall.elliptic_p(self, tau, n=None)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4588)

        Return the Weierstrass elliptic function with lattice parameter ``tau``,
        evaluated at ``self``. The function is doubly periodic in ``self``
        with periods 1 and ``tau``, which should lie in the upper half plane.

        If ``n`` is given, return a list containing the first ``n``
        terms in the Taylor expansion at ``self``. In particular, with
        ``n`` = 2, compute the Weierstrass elliptic function together
        with its derivative, which generate the field of elliptic
        functions with periods 1 and ``tau``.

        EXAMPLES::

            sage: tau = CBF(1,4)
            sage: z = CBF(sqrt(2), sqrt(3))                                             # needs sage.symbolic
            sage: z.elliptic_p(tau)                                                     # needs sage.symbolic
            [-3.28920996772709 +/- ...e-15] + [-0.0003673767302933 +/- ...e-17]*I
            sage: (z + tau).elliptic_p(tau)                                             # needs sage.symbolic
            [-3.28920996772709 +/- ...e-15] + [-0.000367376730293 +/- ...e-16]*I
            sage: (z + 1).elliptic_p(tau)                                               # needs sage.symbolic
            [-3.28920996772709 +/- ...e-15] + [-0.0003673767302933 +/- ...e-17]*I

            sage: z.elliptic_p(tau, 3)                                                  # needs sage.symbolic
            [[-3.28920996772709 +/- ...e-15] + [-0.0003673767302933 +/- ...e-17]*I,
             [0.002473055794309 +/- ...e-16] + [0.003859554040267 +/- ...e-16]*I,
             [-0.01299087561709 +/- ...e-15] + [0.00725027521915 +/- ...e-15]*I]
            sage: (z + 3 + 4*tau).elliptic_p(tau, 3)                                    # needs sage.symbolic
            [[-3.28920996772709 +/- ...e-15] + [-0.00036737673029 +/- ...e-15]*I,
             [0.0024730557943 +/- ...e-14] + [0.0038595540403 +/- ...e-14]*I,
             [-0.01299087562 +/- ...e-12] + [0.00725027522 +/- ...e-12]*I]"""
    @overload
    def elliptic_p(self, tau) -> Any:
        """ComplexBall.elliptic_p(self, tau, n=None)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4588)

        Return the Weierstrass elliptic function with lattice parameter ``tau``,
        evaluated at ``self``. The function is doubly periodic in ``self``
        with periods 1 and ``tau``, which should lie in the upper half plane.

        If ``n`` is given, return a list containing the first ``n``
        terms in the Taylor expansion at ``self``. In particular, with
        ``n`` = 2, compute the Weierstrass elliptic function together
        with its derivative, which generate the field of elliptic
        functions with periods 1 and ``tau``.

        EXAMPLES::

            sage: tau = CBF(1,4)
            sage: z = CBF(sqrt(2), sqrt(3))                                             # needs sage.symbolic
            sage: z.elliptic_p(tau)                                                     # needs sage.symbolic
            [-3.28920996772709 +/- ...e-15] + [-0.0003673767302933 +/- ...e-17]*I
            sage: (z + tau).elliptic_p(tau)                                             # needs sage.symbolic
            [-3.28920996772709 +/- ...e-15] + [-0.000367376730293 +/- ...e-16]*I
            sage: (z + 1).elliptic_p(tau)                                               # needs sage.symbolic
            [-3.28920996772709 +/- ...e-15] + [-0.0003673767302933 +/- ...e-17]*I

            sage: z.elliptic_p(tau, 3)                                                  # needs sage.symbolic
            [[-3.28920996772709 +/- ...e-15] + [-0.0003673767302933 +/- ...e-17]*I,
             [0.002473055794309 +/- ...e-16] + [0.003859554040267 +/- ...e-16]*I,
             [-0.01299087561709 +/- ...e-15] + [0.00725027521915 +/- ...e-15]*I]
            sage: (z + 3 + 4*tau).elliptic_p(tau, 3)                                    # needs sage.symbolic
            [[-3.28920996772709 +/- ...e-15] + [-0.00036737673029 +/- ...e-15]*I,
             [0.0024730557943 +/- ...e-14] + [0.0038595540403 +/- ...e-14]*I,
             [-0.01299087562 +/- ...e-12] + [0.00725027522 +/- ...e-12]*I]"""
    @overload
    def elliptic_p(self, tau) -> Any:
        """ComplexBall.elliptic_p(self, tau, n=None)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4588)

        Return the Weierstrass elliptic function with lattice parameter ``tau``,
        evaluated at ``self``. The function is doubly periodic in ``self``
        with periods 1 and ``tau``, which should lie in the upper half plane.

        If ``n`` is given, return a list containing the first ``n``
        terms in the Taylor expansion at ``self``. In particular, with
        ``n`` = 2, compute the Weierstrass elliptic function together
        with its derivative, which generate the field of elliptic
        functions with periods 1 and ``tau``.

        EXAMPLES::

            sage: tau = CBF(1,4)
            sage: z = CBF(sqrt(2), sqrt(3))                                             # needs sage.symbolic
            sage: z.elliptic_p(tau)                                                     # needs sage.symbolic
            [-3.28920996772709 +/- ...e-15] + [-0.0003673767302933 +/- ...e-17]*I
            sage: (z + tau).elliptic_p(tau)                                             # needs sage.symbolic
            [-3.28920996772709 +/- ...e-15] + [-0.000367376730293 +/- ...e-16]*I
            sage: (z + 1).elliptic_p(tau)                                               # needs sage.symbolic
            [-3.28920996772709 +/- ...e-15] + [-0.0003673767302933 +/- ...e-17]*I

            sage: z.elliptic_p(tau, 3)                                                  # needs sage.symbolic
            [[-3.28920996772709 +/- ...e-15] + [-0.0003673767302933 +/- ...e-17]*I,
             [0.002473055794309 +/- ...e-16] + [0.003859554040267 +/- ...e-16]*I,
             [-0.01299087561709 +/- ...e-15] + [0.00725027521915 +/- ...e-15]*I]
            sage: (z + 3 + 4*tau).elliptic_p(tau, 3)                                    # needs sage.symbolic
            [[-3.28920996772709 +/- ...e-15] + [-0.00036737673029 +/- ...e-15]*I,
             [0.0024730557943 +/- ...e-14] + [0.0038595540403 +/- ...e-14]*I,
             [-0.01299087562 +/- ...e-12] + [0.00725027522 +/- ...e-12]*I]"""
    @overload
    def elliptic_p(self, tau) -> Any:
        """ComplexBall.elliptic_p(self, tau, n=None)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4588)

        Return the Weierstrass elliptic function with lattice parameter ``tau``,
        evaluated at ``self``. The function is doubly periodic in ``self``
        with periods 1 and ``tau``, which should lie in the upper half plane.

        If ``n`` is given, return a list containing the first ``n``
        terms in the Taylor expansion at ``self``. In particular, with
        ``n`` = 2, compute the Weierstrass elliptic function together
        with its derivative, which generate the field of elliptic
        functions with periods 1 and ``tau``.

        EXAMPLES::

            sage: tau = CBF(1,4)
            sage: z = CBF(sqrt(2), sqrt(3))                                             # needs sage.symbolic
            sage: z.elliptic_p(tau)                                                     # needs sage.symbolic
            [-3.28920996772709 +/- ...e-15] + [-0.0003673767302933 +/- ...e-17]*I
            sage: (z + tau).elliptic_p(tau)                                             # needs sage.symbolic
            [-3.28920996772709 +/- ...e-15] + [-0.000367376730293 +/- ...e-16]*I
            sage: (z + 1).elliptic_p(tau)                                               # needs sage.symbolic
            [-3.28920996772709 +/- ...e-15] + [-0.0003673767302933 +/- ...e-17]*I

            sage: z.elliptic_p(tau, 3)                                                  # needs sage.symbolic
            [[-3.28920996772709 +/- ...e-15] + [-0.0003673767302933 +/- ...e-17]*I,
             [0.002473055794309 +/- ...e-16] + [0.003859554040267 +/- ...e-16]*I,
             [-0.01299087561709 +/- ...e-15] + [0.00725027521915 +/- ...e-15]*I]
            sage: (z + 3 + 4*tau).elliptic_p(tau, 3)                                    # needs sage.symbolic
            [[-3.28920996772709 +/- ...e-15] + [-0.00036737673029 +/- ...e-15]*I,
             [0.0024730557943 +/- ...e-14] + [0.0038595540403 +/- ...e-14]*I,
             [-0.01299087562 +/- ...e-12] + [0.00725027522 +/- ...e-12]*I]"""
    def elliptic_pi(self, m) -> Any:
        """ComplexBall.elliptic_pi(self, m)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4719)

        Return the complete elliptic integral of the third kind evaluated
        at *m* given by ``self``.

        EXAMPLES::

            sage: CBF(2,3).elliptic_pi(CBF(1,1))
            [0.2702999736198...] + [0.715676058329...]*I"""
    def elliptic_pi_inc(self, phi, m) -> Any:
        """ComplexBall.elliptic_pi_inc(self, phi, m)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4810)

        Return the Legendre incomplete elliptic integral of the third kind.

        See: :meth:`elliptic_pi` for the complete integral.

        INPUT:

        - ``phi`` -- complex ball

        - ``m`` -- complex ball

        EXAMPLES::

            sage: CBF(1,2).elliptic_pi_inc(CBF(0,1), CBF(2,-3))
            [0.05738864021418 +/- ...e-15] + [0.55557494549951 +/- ...e-15]*I

        At parameter `\\pi/2` it is a complete integral::

            sage: n = CBF(1,1)
            sage: m = CBF(-2/3, 3/5)
            sage: n.elliptic_pi_inc(CBF.pi()/2, m) # this is a regression, see :issue:28623
            nan + nan*I
            sage: n.elliptic_pi(m)
            [0.8934793755173...] + [0.957078687107...]*I

            sage: n = CBF(2, 3/7)
            sage: m = CBF(-1/3, 2/9)
            sage: n.elliptic_pi_inc(CBF.pi()/2, m) # this is a regression, see :issue:28623
            nan + nan*I
            sage: n.elliptic_pi(m)
            [0.296958874641...] + [1.318879533273...]*I"""
    def elliptic_rf(self, y, z) -> Any:
        """ComplexBall.elliptic_rf(self, y, z)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4851)

        Return the Carlson symmetric elliptic integral of the first kind evaluated
        at ``(self, y, z)``.

        INPUT:

        - ``y`` -- complex ball

        - ``z`` -- complex ball

        EXAMPLES::

            sage: CBF(0,1).elliptic_rf(CBF(-1/2,1), CBF(-1,-1))
            [1.469800396738515 +/- ...e-16] + [-0.2358791199824196 +/- ...e-17]*I"""
    def elliptic_rg(self, y, z) -> Any:
        """ComplexBall.elliptic_rg(self, y, z)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4875)

        Return the Carlson symmetric elliptic integral of the second kind evaluated
        at ``(self, y, z)``.

        INPUT:

        - ``y`` -- complex ball

        - ``z`` -- complex ball

        EXAMPLES::

            sage: CBF(0,1).elliptic_rg(CBF(-1/2,1), CBF(-1,-1))
            [0.1586786770922370 +/- ...e-17] + [0.2239733128130531 +/- ...e-17]*I"""
    def elliptic_rj(self, y, z, p) -> Any:
        """ComplexBall.elliptic_rj(self, y, z, p)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4899)

        Return the Carlson symmetric elliptic integral of the third kind evaluated
        at ``(self, y, z)``.

        INPUT:

        - ``y`` -- complex ball

        - ``z`` -- complex ball

        - ``p`` -- complex bamm

        EXAMPLES::

            sage: CBF(0,1).elliptic_rj(CBF(-1/2,1), CBF(-1,-1), CBF(2))
            [1.00438675628573...] + [-0.24516268343916...]*I"""
    @overload
    def elliptic_roots(self) -> Any:
        """ComplexBall.elliptic_roots(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4664)

        Return the lattice roots ``(e1, e2, e3)`` of `4 z^3 - g_2 z - g_3`.

        EXAMPLES::

            sage: e1, e2, e3 = CBF(0,1).elliptic_roots()
            sage: e1, e2, e3
            ([6.8751858180204 +/- ...e-14],
             [+/- ...e-14],
             [-6.8751858180204 +/- ...e-14])
            sage: g2, g3 = CBF(0,1).elliptic_invariants()
            sage: 4 * e1^3 - g2 * e1 - g3
            [+/- ...e-11]"""
    @overload
    def elliptic_roots(self) -> Any:
        """ComplexBall.elliptic_roots(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4664)

        Return the lattice roots ``(e1, e2, e3)`` of `4 z^3 - g_2 z - g_3`.

        EXAMPLES::

            sage: e1, e2, e3 = CBF(0,1).elliptic_roots()
            sage: e1, e2, e3
            ([6.8751858180204 +/- ...e-14],
             [+/- ...e-14],
             [-6.8751858180204 +/- ...e-14])
            sage: g2, g3 = CBF(0,1).elliptic_invariants()
            sage: 4 * e1^3 - g2 * e1 - g3
            [+/- ...e-11]"""
    def elliptic_sigma(self, tau) -> Any:
        """ComplexBall.elliptic_sigma(self, tau)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4946)

        Return the value of the Weierstrass sigma function at ``(self, tau)``.

        EXAMPLES::

        - ``tau`` -- a complex ball with positive imaginary part

        EXAMPLES::

            sage: CBF(1,1).elliptic_sigma(CBF(1,3))
            [-0.543073363596 +/- ...e-13] + [3.6357291186244 +/- ...e-14]*I"""
    def elliptic_zeta(self, tau) -> Any:
        """ComplexBall.elliptic_zeta(self, tau)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4926)

        Return the value of the Weierstrass zeta function at ``(self, tau)``.

        EXAMPLES::

        - ``tau`` -- a complex ball with positive imaginary part

        EXAMPLES::

            sage: CBF(1,1).elliptic_zeta(CBF(1,3))
            [3.2898676194970 +/- ...e-14] + [0.1365414361782 +/- ...e-14]*I"""
    @overload
    def erf(self) -> Any:
        """ComplexBall.erf(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4022)

        Return the error function with argument ``self``.

        EXAMPLES::

            sage: CBF(1, 1).erf()
            [1.316151281697947 +/- ...e-16] + [0.1904534692378347 +/- ...e-17]*I"""
    @overload
    def erf(self) -> Any:
        """ComplexBall.erf(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4022)

        Return the error function with argument ``self``.

        EXAMPLES::

            sage: CBF(1, 1).erf()
            [1.316151281697947 +/- ...e-16] + [0.1904534692378347 +/- ...e-17]*I"""
    @overload
    def erfc(self) -> Any:
        """ComplexBall.erfc(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4038)

        Compute the complementary error function with argument ``self``.

        EXAMPLES::

            sage: CBF(20).erfc() # abs tol 1e-190
            [5.39586561160790e-176 +/- 6.73e-191]
            sage: CBF(100, 100).erfc()
            [0.00065234366376858 +/- ...e-18] + [-0.00393572636292141 +/- ...e-18]*I"""
    @overload
    def erfc(self) -> Any:
        """ComplexBall.erfc(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4038)

        Compute the complementary error function with argument ``self``.

        EXAMPLES::

            sage: CBF(20).erfc() # abs tol 1e-190
            [5.39586561160790e-176 +/- 6.73e-191]
            sage: CBF(100, 100).erfc()
            [0.00065234366376858 +/- ...e-18] + [-0.00393572636292141 +/- ...e-18]*I"""
    @overload
    def erfc(self) -> Any:
        """ComplexBall.erfc(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4038)

        Compute the complementary error function with argument ``self``.

        EXAMPLES::

            sage: CBF(20).erfc() # abs tol 1e-190
            [5.39586561160790e-176 +/- 6.73e-191]
            sage: CBF(100, 100).erfc()
            [0.00065234366376858 +/- ...e-18] + [-0.00393572636292141 +/- ...e-18]*I"""
    @overload
    def exp(self) -> Any:
        """ComplexBall.exp(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3171)

        Return the exponential of this ball.

        .. SEEALSO:: :meth:`exppii`

        EXAMPLES::

            sage: CBF(i*pi).exp()                                                       # needs sage.symbolic
            [-1.00000000000000 +/- ...e-16] + [+/- ...e-16]*I"""
    @overload
    def exp(self) -> Any:
        """ComplexBall.exp(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3171)

        Return the exponential of this ball.

        .. SEEALSO:: :meth:`exppii`

        EXAMPLES::

            sage: CBF(i*pi).exp()                                                       # needs sage.symbolic
            [-1.00000000000000 +/- ...e-16] + [+/- ...e-16]*I"""
    def exp_integral_e(self, s) -> Any:
        """ComplexBall.exp_integral_e(self, s)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4240)

        Return the image of this ball by the generalized exponential integral
        with index ``s``.

        EXAMPLES::

            sage: CBF(1+i).exp_integral_e(1)
            [0.00028162445198 +/- ...e-15] + [-0.17932453503936 +/- ...e-15]*I
            sage: CBF(1+i).exp_integral_e(QQbar(i))
            [-0.10396361883964 +/- ...e-15] + [-0.16268401277783 +/- ...e-15]*I"""
    @overload
    def exppii(self) -> Any:
        """ComplexBall.exppii(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3188)

        Return ``exp(pi*i*self)``.

        EXAMPLES::

            sage: CBF(1/2).exppii()
            1.000000000000000*I
            sage: CBF(0, -1/pi).exppii()                                                # needs sage.symbolic
            [2.71828182845904 +/- ...e-15]"""
    @overload
    def exppii(self) -> Any:
        """ComplexBall.exppii(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3188)

        Return ``exp(pi*i*self)``.

        EXAMPLES::

            sage: CBF(1/2).exppii()
            1.000000000000000*I
            sage: CBF(0, -1/pi).exppii()                                                # needs sage.symbolic
            [2.71828182845904 +/- ...e-15]"""
    @overload
    def exppii(self) -> Any:
        """ComplexBall.exppii(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3188)

        Return ``exp(pi*i*self)``.

        EXAMPLES::

            sage: CBF(1/2).exppii()
            1.000000000000000*I
            sage: CBF(0, -1/pi).exppii()                                                # needs sage.symbolic
            [2.71828182845904 +/- ...e-15]"""
    @overload
    def gamma(self, z=...) -> Any:
        """ComplexBall.gamma(self, z=None)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3573)

        Return the image of this ball by the Euler Gamma function (if
        ``z = None``) or the incomplete Gamma function (otherwise).

        EXAMPLES::

            sage: CBF(1, 1).gamma() # abs tol 1e-15
            [0.498015668118356 +/- 1.26e-16] + [-0.1549498283018107 +/- 8.43e-17]*I
            sage: CBF(-1).gamma()
            nan
            sage: CBF(1, 1).gamma(0) # abs tol 1e-15
            [0.498015668118356 +/- 1.26e-16] + [-0.1549498283018107 +/- 8.43e-17]*I
            sage: CBF(1, 1).gamma(100)
            [-3.6143867454139e-45 +/- ...e-59] + [-3.7022961377791e-44 +/- ...e-58]*I
            sage: CBF(1, 1).gamma(CLF(i)) # abs tol 1e-14
            [0.328866841935004 +/- 7.07e-16] + [-0.189749450456210 +/- 9.05e-16]*I"""
    @overload
    def gamma(self) -> Any:
        """ComplexBall.gamma(self, z=None)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3573)

        Return the image of this ball by the Euler Gamma function (if
        ``z = None``) or the incomplete Gamma function (otherwise).

        EXAMPLES::

            sage: CBF(1, 1).gamma() # abs tol 1e-15
            [0.498015668118356 +/- 1.26e-16] + [-0.1549498283018107 +/- 8.43e-17]*I
            sage: CBF(-1).gamma()
            nan
            sage: CBF(1, 1).gamma(0) # abs tol 1e-15
            [0.498015668118356 +/- 1.26e-16] + [-0.1549498283018107 +/- 8.43e-17]*I
            sage: CBF(1, 1).gamma(100)
            [-3.6143867454139e-45 +/- ...e-59] + [-3.7022961377791e-44 +/- ...e-58]*I
            sage: CBF(1, 1).gamma(CLF(i)) # abs tol 1e-14
            [0.328866841935004 +/- 7.07e-16] + [-0.189749450456210 +/- 9.05e-16]*I"""
    @overload
    def gamma(self) -> Any:
        """ComplexBall.gamma(self, z=None)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3573)

        Return the image of this ball by the Euler Gamma function (if
        ``z = None``) or the incomplete Gamma function (otherwise).

        EXAMPLES::

            sage: CBF(1, 1).gamma() # abs tol 1e-15
            [0.498015668118356 +/- 1.26e-16] + [-0.1549498283018107 +/- 8.43e-17]*I
            sage: CBF(-1).gamma()
            nan
            sage: CBF(1, 1).gamma(0) # abs tol 1e-15
            [0.498015668118356 +/- 1.26e-16] + [-0.1549498283018107 +/- 8.43e-17]*I
            sage: CBF(1, 1).gamma(100)
            [-3.6143867454139e-45 +/- ...e-59] + [-3.7022961377791e-44 +/- ...e-58]*I
            sage: CBF(1, 1).gamma(CLF(i)) # abs tol 1e-14
            [0.328866841935004 +/- 7.07e-16] + [-0.189749450456210 +/- 9.05e-16]*I"""
    def gamma_inc(self, *args, **kwargs):
        """ComplexBall.gamma(self, z=None)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3573)

        Return the image of this ball by the Euler Gamma function (if
        ``z = None``) or the incomplete Gamma function (otherwise).

        EXAMPLES::

            sage: CBF(1, 1).gamma() # abs tol 1e-15
            [0.498015668118356 +/- 1.26e-16] + [-0.1549498283018107 +/- 8.43e-17]*I
            sage: CBF(-1).gamma()
            nan
            sage: CBF(1, 1).gamma(0) # abs tol 1e-15
            [0.498015668118356 +/- 1.26e-16] + [-0.1549498283018107 +/- 8.43e-17]*I
            sage: CBF(1, 1).gamma(100)
            [-3.6143867454139e-45 +/- ...e-59] + [-3.7022961377791e-44 +/- ...e-58]*I
            sage: CBF(1, 1).gamma(CLF(i)) # abs tol 1e-14
            [0.328866841935004 +/- 7.07e-16] + [-0.189749450456210 +/- 9.05e-16]*I"""
    def gegenbauer_C(self, n, m) -> Any:
        """ComplexBall.gegenbauer_C(self, n, m)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 5024)

        Return the Gegenbauer polynomial (or function) `C_n^m(z)`
        evaluated at ``self``.

        EXAMPLES::

            sage: CBF(-10).gegenbauer_C(7, 1/2)
            [-263813415.6250000 +/- ...e-8]"""
    def hermite_H(self, n) -> Any:
        """ComplexBall.hermite_H(self, n)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 5066)

        Return the Hermite function (or polynomial) of order ``n``
        evaluated at ``self``.

        EXAMPLES::

            sage: CBF(10).hermite_H(1)
            20.00000000000000
            sage: CBF(10).hermite_H(30)
            [8.0574670961707e+37 +/- ...e+23]"""
    def hypergeometric(self, a, b, boolregularized=...) -> Any:
        """ComplexBall.hypergeometric(self, a, b, bool regularized=False)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3857)

        Return the generalized hypergeometric function of ``self``.

        INPUT:

        - ``a`` -- upper parameters; list of complex numbers that coerce into
          this ball's parent

        - ``b`` -- lower parameters; list of complex numbers that coerce into
          this ball's parent

        - ``regularized`` -- if ``True``, the regularized generalized
          hypergeometric function is computed

        OUTPUT: the generalized hypergeometric function defined by

        .. MATH::

            {}_pF_q(a_1,\\ldots,a_p;b_1,\\ldots,b_q;z)
            = \\sum_{k=0}^\\infty \\frac{(a_1)_k\\dots(a_p)_k}{(b_1)_k\\dots(b_q)_k} \\frac {z^k} {k!}

        extended using analytic continuation or regularization when the sum
        does not converge.

        The regularized generalized hypergeometric function

        .. MATH::

            {}_pF_q(a_1,\\ldots,a_p;b_1,\\ldots,b_q;z)
            = \\sum_{k=0}^\\infty \\frac{(a_1)_k\\dots(a_p)_k}{\\Gamma(b_1+k)\\dots\\Gamma(b_q+k)} \\frac {z^k} {k!}

        is well-defined even when the lower parameters are nonpositive
        integers. Currently, this is only supported for some `p` and `q`.

        EXAMPLES::

            sage: CBF(1, pi/2).hypergeometric([], [])                                   # needs sage.symbolic
            [+/- ...e-16] + [2.71828182845904 +/- ...e-15]*I

            sage: CBF(1, pi).hypergeometric([1/4], [1/4])                               # needs sage.symbolic
            [-2.7182818284590 +/- ...e-14] + [+/- ...e-14]*I

            sage: CBF(1000, 1000).hypergeometric([10], [AA(sqrt(2))])                   # needs sage.symbolic
            [9.79300951360e+454 +/- ...e+442] + [5.522579106816e+455 +/- ...e+442]*I
            sage: CBF(1000, 1000).hypergeometric([100], [AA(sqrt(2))])                  # needs sage.symbolic
            [1.27967355557e+590 +/- ...e+578] + [-9.32333491987e+590 +/- ...e+578]*I

            sage: CBF(0, 1).hypergeometric([], [1/2, 1/3, 1/4])
            [-3.7991962344383 +/- ...e-14] + [23.878097177805 +/- ...e-13]*I

            sage: CBF(0).hypergeometric([1], [])
            1.000000000000000
            sage: CBF(1, 1).hypergeometric([1], [])
            1.000000000000000*I

            sage: CBF(2+3*I).hypergeometric([1/4,1/3],[1/2]) # abs tol 1e-14
            [0.7871684267473 +/- 6.79e-14] + [0.2749254173721 +/- 8.82e-14]*I
            sage: CBF(2+3*I).hypergeometric([1/4,1/3],[1/2],regularized=True)
            [0.4441122268685 +/- 3...e-14] + [0.1551100567338 +/- 5...e-14]*I

            sage: CBF(5).hypergeometric([2,3], [-5])
            nan + nan*I
            sage: CBF(5).hypergeometric([2,3], [-5], regularized=True)
            [5106.925964355 +/- ...e-10]

            sage: CBF(2016).hypergeometric([], [2/3]) # abs tol 1e+26
            [2.0256426923278e+38 +/- 9.59e+24]
            sage: CBF(-2016).hypergeometric([], [2/3], regularized=True)
            [-0.0005428550847 +/- ...e-14]

            sage: CBF(-7).hypergeometric([4], [])
            0.0002441406250000000

            sage: CBF(0, 3).hypergeometric([CBF(1,1)], [-4], regularized=True)
            [239.514000752841 +/- ...e-13] + [105.175157349015 +/- ...e-13]*I

        TESTS::

            sage: CBF(0, 1).hypergeometric([QQbar(sqrt(2)), RLF(pi)], [1r, 1/2])        # needs sage.symbolic
            [-8.7029449215408 +/- ...e-14] + [-0.8499070546106 +/- ...e-14]*I"""
    def hypergeometric_U(self, a, b) -> Any:
        """ComplexBall.hypergeometric_U(self, a, b)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4002)

        Return the Tricomi confluent hypergeometric function U(a, b, self) of
        this ball.

        EXAMPLES::

            sage: CBF(1000, 1000).hypergeometric_U(RLF(pi), -100)                       # needs sage.symbolic
            [-7.261605907166e-11 +/- ...e-24] + [-7.928136216391e-11 +/- ...e-24]*I
            sage: CBF(1000, 1000).hypergeometric_U(0, -100)
            1.000000000000000"""
    def identical(self, ComplexBallother) -> Any:
        """ComplexBall.identical(self, ComplexBall other)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 2496)

        Return whether ``self`` and ``other`` represent the same ball.

        INPUT:

        - ``other`` -- a :class:`ComplexBall`

        OUTPUT:

        Return ``True`` iff ``self`` and ``other`` are equal as sets, i.e. if their
        real and imaginary parts each have the same midpoint and radius.

        Note that this is not the same thing as testing whether both ``self``
        and ``other`` certainly represent the complex real number, unless
        either ``self`` or ``other`` is exact (and neither contains NaN). To
        test whether both operands might represent the same mathematical
        quantity, use :meth:`overlaps` or ``in``, depending on the
        circumstance.

        EXAMPLES::

            sage: CBF(1, 1/3).identical(1 + CBF(0, 1)/3)
            True
            sage: CBF(1, 1).identical(1 + CBF(0, 1/3)*3)
            False"""
    @overload
    def imag(self) -> RealBall:
        """ComplexBall.imag(self) -> RealBall

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 1894)

        Return the imaginary part of this ball.

        OUTPUT: a :class:`~sage.rings.real_arb.RealBall`

        EXAMPLES::

           sage: a = CBF(1/3, 1/5)
           sage: a.imag()
           [0.2000000000000000 +/- ...e-17]
           sage: a.imag().parent()
           Real ball field with 53 bits of precision"""
    @overload
    def imag(self) -> Any:
        """ComplexBall.imag(self) -> RealBall

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 1894)

        Return the imaginary part of this ball.

        OUTPUT: a :class:`~sage.rings.real_arb.RealBall`

        EXAMPLES::

           sage: a = CBF(1/3, 1/5)
           sage: a.imag()
           [0.2000000000000000 +/- ...e-17]
           sage: a.imag().parent()
           Real ball field with 53 bits of precision"""
    @overload
    def imag(self) -> Any:
        """ComplexBall.imag(self) -> RealBall

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 1894)

        Return the imaginary part of this ball.

        OUTPUT: a :class:`~sage.rings.real_arb.RealBall`

        EXAMPLES::

           sage: a = CBF(1/3, 1/5)
           sage: a.imag()
           [0.2000000000000000 +/- ...e-17]
           sage: a.imag().parent()
           Real ball field with 53 bits of precision"""
    @overload
    def is_NaN(self) -> Any:
        """ComplexBall.is_NaN(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 2272)

        Return ``True`` iff either the real or the imaginary part
        is not-a-number.

        EXAMPLES::

            sage: CBF(NaN).is_NaN()                                                     # needs sage.symbolic
            True
            sage: CBF(-5).gamma().is_NaN()
            True
            sage: CBF(oo).is_NaN()
            False
            sage: CBF(42+I).is_NaN()
            False"""
    @overload
    def is_NaN(self) -> Any:
        """ComplexBall.is_NaN(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 2272)

        Return ``True`` iff either the real or the imaginary part
        is not-a-number.

        EXAMPLES::

            sage: CBF(NaN).is_NaN()                                                     # needs sage.symbolic
            True
            sage: CBF(-5).gamma().is_NaN()
            True
            sage: CBF(oo).is_NaN()
            False
            sage: CBF(42+I).is_NaN()
            False"""
    @overload
    def is_NaN(self) -> Any:
        """ComplexBall.is_NaN(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 2272)

        Return ``True`` iff either the real or the imaginary part
        is not-a-number.

        EXAMPLES::

            sage: CBF(NaN).is_NaN()                                                     # needs sage.symbolic
            True
            sage: CBF(-5).gamma().is_NaN()
            True
            sage: CBF(oo).is_NaN()
            False
            sage: CBF(42+I).is_NaN()
            False"""
    @overload
    def is_NaN(self) -> Any:
        """ComplexBall.is_NaN(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 2272)

        Return ``True`` iff either the real or the imaginary part
        is not-a-number.

        EXAMPLES::

            sage: CBF(NaN).is_NaN()                                                     # needs sage.symbolic
            True
            sage: CBF(-5).gamma().is_NaN()
            True
            sage: CBF(oo).is_NaN()
            False
            sage: CBF(42+I).is_NaN()
            False"""
    @overload
    def is_NaN(self) -> Any:
        """ComplexBall.is_NaN(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 2272)

        Return ``True`` iff either the real or the imaginary part
        is not-a-number.

        EXAMPLES::

            sage: CBF(NaN).is_NaN()                                                     # needs sage.symbolic
            True
            sage: CBF(-5).gamma().is_NaN()
            True
            sage: CBF(oo).is_NaN()
            False
            sage: CBF(42+I).is_NaN()
            False"""
    @overload
    def is_exact(self) -> Any:
        """ComplexBall.is_exact(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 2361)

        Return ``True`` iff the radius of this ball is zero.

        EXAMPLES::

            sage: CBF(1).is_exact()
            True
            sage: CBF(1/3, 1/3).is_exact()
            False"""
    @overload
    def is_exact(self) -> Any:
        """ComplexBall.is_exact(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 2361)

        Return ``True`` iff the radius of this ball is zero.

        EXAMPLES::

            sage: CBF(1).is_exact()
            True
            sage: CBF(1/3, 1/3).is_exact()
            False"""
    @overload
    def is_exact(self) -> Any:
        """ComplexBall.is_exact(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 2361)

        Return ``True`` iff the radius of this ball is zero.

        EXAMPLES::

            sage: CBF(1).is_exact()
            True
            sage: CBF(1/3, 1/3).is_exact()
            False"""
    @overload
    def is_nonzero(self) -> Any:
        """ComplexBall.is_nonzero(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 2306)

        Return ``True`` iff zero is not contained in the interval represented
        by this ball.

        .. NOTE::

            This method is not the negation of :meth:`is_zero`: it only
            returns ``True`` if zero is known not to be contained in the ball.

            Use ``bool(b)`` (or, equivalently, ``not b.is_zero()``) to check if
            a ball\xa0``b`` **may** represent a nonzero number (for instance, to
            determine the “degree” of a polynomial with ball coefficients).

        EXAMPLES::

            sage: CBF(pi, 1/3).is_nonzero()                                             # needs sage.symbolic
            True
            sage: CBF(RIF(-0.5, 0.5), 1/3).is_nonzero()
            True
            sage: CBF(1/3, RIF(-0.5, 0.5)).is_nonzero()
            True
            sage: CBF(RIF(-0.5, 0.5), RIF(-0.5, 0.5)).is_nonzero()
            False

        .. SEEALSO:: :meth:`is_zero`"""
    @overload
    def is_nonzero(self) -> Any:
        """ComplexBall.is_nonzero(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 2306)

        Return ``True`` iff zero is not contained in the interval represented
        by this ball.

        .. NOTE::

            This method is not the negation of :meth:`is_zero`: it only
            returns ``True`` if zero is known not to be contained in the ball.

            Use ``bool(b)`` (or, equivalently, ``not b.is_zero()``) to check if
            a ball\xa0``b`` **may** represent a nonzero number (for instance, to
            determine the “degree” of a polynomial with ball coefficients).

        EXAMPLES::

            sage: CBF(pi, 1/3).is_nonzero()                                             # needs sage.symbolic
            True
            sage: CBF(RIF(-0.5, 0.5), 1/3).is_nonzero()
            True
            sage: CBF(1/3, RIF(-0.5, 0.5)).is_nonzero()
            True
            sage: CBF(RIF(-0.5, 0.5), RIF(-0.5, 0.5)).is_nonzero()
            False

        .. SEEALSO:: :meth:`is_zero`"""
    @overload
    def is_nonzero(self) -> Any:
        """ComplexBall.is_nonzero(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 2306)

        Return ``True`` iff zero is not contained in the interval represented
        by this ball.

        .. NOTE::

            This method is not the negation of :meth:`is_zero`: it only
            returns ``True`` if zero is known not to be contained in the ball.

            Use ``bool(b)`` (or, equivalently, ``not b.is_zero()``) to check if
            a ball\xa0``b`` **may** represent a nonzero number (for instance, to
            determine the “degree” of a polynomial with ball coefficients).

        EXAMPLES::

            sage: CBF(pi, 1/3).is_nonzero()                                             # needs sage.symbolic
            True
            sage: CBF(RIF(-0.5, 0.5), 1/3).is_nonzero()
            True
            sage: CBF(1/3, RIF(-0.5, 0.5)).is_nonzero()
            True
            sage: CBF(RIF(-0.5, 0.5), RIF(-0.5, 0.5)).is_nonzero()
            False

        .. SEEALSO:: :meth:`is_zero`"""
    @overload
    def is_nonzero(self) -> Any:
        """ComplexBall.is_nonzero(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 2306)

        Return ``True`` iff zero is not contained in the interval represented
        by this ball.

        .. NOTE::

            This method is not the negation of :meth:`is_zero`: it only
            returns ``True`` if zero is known not to be contained in the ball.

            Use ``bool(b)`` (or, equivalently, ``not b.is_zero()``) to check if
            a ball\xa0``b`` **may** represent a nonzero number (for instance, to
            determine the “degree” of a polynomial with ball coefficients).

        EXAMPLES::

            sage: CBF(pi, 1/3).is_nonzero()                                             # needs sage.symbolic
            True
            sage: CBF(RIF(-0.5, 0.5), 1/3).is_nonzero()
            True
            sage: CBF(1/3, RIF(-0.5, 0.5)).is_nonzero()
            True
            sage: CBF(RIF(-0.5, 0.5), RIF(-0.5, 0.5)).is_nonzero()
            False

        .. SEEALSO:: :meth:`is_zero`"""
    @overload
    def is_nonzero(self) -> Any:
        """ComplexBall.is_nonzero(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 2306)

        Return ``True`` iff zero is not contained in the interval represented
        by this ball.

        .. NOTE::

            This method is not the negation of :meth:`is_zero`: it only
            returns ``True`` if zero is known not to be contained in the ball.

            Use ``bool(b)`` (or, equivalently, ``not b.is_zero()``) to check if
            a ball\xa0``b`` **may** represent a nonzero number (for instance, to
            determine the “degree” of a polynomial with ball coefficients).

        EXAMPLES::

            sage: CBF(pi, 1/3).is_nonzero()                                             # needs sage.symbolic
            True
            sage: CBF(RIF(-0.5, 0.5), 1/3).is_nonzero()
            True
            sage: CBF(1/3, RIF(-0.5, 0.5)).is_nonzero()
            True
            sage: CBF(RIF(-0.5, 0.5), RIF(-0.5, 0.5)).is_nonzero()
            False

        .. SEEALSO:: :meth:`is_zero`"""
    @overload
    def is_real(self) -> Any:
        """ComplexBall.is_real(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 2374)

        Return ``True`` iff the imaginary part of this ball is exactly zero.

        EXAMPLES::

            sage: CBF(1/3, 0).is_real()
            True
            sage: (CBF(i/3) - CBF(1, 1/3)).is_real()
            False
            sage: CBF('inf').is_real()
            True"""
    @overload
    def is_real(self) -> Any:
        """ComplexBall.is_real(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 2374)

        Return ``True`` iff the imaginary part of this ball is exactly zero.

        EXAMPLES::

            sage: CBF(1/3, 0).is_real()
            True
            sage: (CBF(i/3) - CBF(1, 1/3)).is_real()
            False
            sage: CBF('inf').is_real()
            True"""
    @overload
    def is_real(self) -> Any:
        """ComplexBall.is_real(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 2374)

        Return ``True`` iff the imaginary part of this ball is exactly zero.

        EXAMPLES::

            sage: CBF(1/3, 0).is_real()
            True
            sage: (CBF(i/3) - CBF(1, 1/3)).is_real()
            False
            sage: CBF('inf').is_real()
            True"""
    @overload
    def is_real(self) -> Any:
        """ComplexBall.is_real(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 2374)

        Return ``True`` iff the imaginary part of this ball is exactly zero.

        EXAMPLES::

            sage: CBF(1/3, 0).is_real()
            True
            sage: (CBF(i/3) - CBF(1, 1/3)).is_real()
            False
            sage: CBF('inf').is_real()
            True"""
    @overload
    def is_zero(self) -> Any:
        """ComplexBall.is_zero(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 2291)

        Return ``True`` iff the midpoint and radius of this ball are both zero.

        EXAMPLES::

            sage: CBF(0).is_zero()
            True
            sage: CBF(RIF(-0.5, 0.5)).is_zero()
            False

        .. SEEALSO:: :meth:`is_nonzero`"""
    @overload
    def is_zero(self) -> Any:
        """ComplexBall.is_zero(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 2291)

        Return ``True`` iff the midpoint and radius of this ball are both zero.

        EXAMPLES::

            sage: CBF(0).is_zero()
            True
            sage: CBF(RIF(-0.5, 0.5)).is_zero()
            False

        .. SEEALSO:: :meth:`is_nonzero`"""
    @overload
    def is_zero(self) -> Any:
        """ComplexBall.is_zero(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 2291)

        Return ``True`` iff the midpoint and radius of this ball are both zero.

        EXAMPLES::

            sage: CBF(0).is_zero()
            True
            sage: CBF(RIF(-0.5, 0.5)).is_zero()
            False

        .. SEEALSO:: :meth:`is_nonzero`"""
    def jacobi_P(self, n, a, b) -> Any:
        """ComplexBall.jacobi_P(self, n, a, b)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 5004)

        Return the Jacobi polynomial (or function) `P_n^{(a,b)}(z)`
        evaluated at ``self``.

        EXAMPLES::

            sage: CBF(5,-6).jacobi_P(8, CBF(1,2), CBF(2,3))
            [-920983000.45982 +/- ...e-6] + [6069919969.92857 +/- ...e-6]*I"""
    def jacobi_theta(self, tau) -> Any:
        """ComplexBall.jacobi_theta(self, tau)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4432)

        Return the four Jacobi theta functions evaluated at the argument
        ``self`` (representing `z`) and the parameter ``tau`` which should lie
        in the upper half plane.

        The following definitions are used:

        .. MATH::

            \\theta_1(z,\\tau) = 2 q_{1/4} \\sum_{n=0}^{\\infty} (-1)^n q^{n(n+1)} \\sin((2n+1) \\pi z)

            \\theta_2(z,\\tau) = 2 q_{1/4} \\sum_{n=0}^{\\infty} q^{n(n+1)} \\cos((2n+1) \\pi z)

            \\theta_3(z,\\tau) = 1 + 2 \\sum_{n=1}^{\\infty} q^{n^2} \\cos(2n \\pi z)

            \\theta_4(z,\\tau) = 1 + 2 \\sum_{n=1}^{\\infty} (-1)^n q^{n^2} \\cos(2n \\pi z)

        where `q = \\exp(\\pi i \\tau)` and `q_{1/4} = \\exp(\\pi i \\tau / 4)`.
        Note that `z` is multiplied by `\\pi`; some authors omit this factor.

        EXAMPLES::

            sage: CBF(3,-1/2).jacobi_theta(CBF(1/4,2))
            ([-0.186580562274757 +/- ...e-16] + [0.93841744788594 +/- ...e-15]*I,
             [-1.02315311037951 +/- ...e-15] + [-0.203600094532010 +/- ...e-16]*I,
             [1.030613911309632 +/- ...e-16] + [0.030613917822067 +/- ...e-16]*I,
             [0.969386075665498 +/- ...e-16] + [-0.030613917822067 +/- ...e-16]*I)

            sage: CBF(3,-1/2).jacobi_theta(CBF(1/4,-2))
            (nan + nan*I, nan + nan*I, nan + nan*I, nan + nan*I)

            sage: CBF(0).jacobi_theta(CBF(0,1))
            (0,
             [0.913579138156117 +/- ...e-16],
             [1.086434811213308 +/- ...e-16],
             [0.913579138156117 +/- ...e-16])"""
    def laguerre_L(self, n, m=...) -> Any:
        """ComplexBall.laguerre_L(self, n, m=0)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 5043)

        Return the Laguerre polynomial (or function) `L_n^m(z)`
        evaluated at ``self``.

        EXAMPLES::

            sage: CBF(10).laguerre_L(3)
            [-45.6666666666666 +/- ...e-14]
            sage: CBF(10).laguerre_L(3, 2)
            [-6.666666666667 +/- ...e-13]
            sage: CBF(5,7).laguerre_L(CBF(2,3), CBF(1,-2)) # abs tol 1e-9
            [5515.3150302713 +/- 5.02e-11] + [-12386.9428452714 +/- 6.21e-11]*I"""
    @overload
    def lambert_w(self, branch=...) -> Any:
        """ComplexBall.lambert_w(self, branch=0)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3742)

        Return the image of this ball by the specified branch of the Lambert\xa0W
        function.

        EXAMPLES::

            sage: CBF(1 + I).lambert_w()
            [0.6569660692304...] + [0.3254503394134...]*I
            sage: CBF(1 + I).lambert_w(2)
            [-2.1208839379437...] + [11.600137110774...]*I
            sage: CBF(1 + I).lambert_w(2^100)
            [-70.806021532123...] + [7.9648836259913...]*I"""
    @overload
    def lambert_w(self) -> Any:
        """ComplexBall.lambert_w(self, branch=0)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3742)

        Return the image of this ball by the specified branch of the Lambert\xa0W
        function.

        EXAMPLES::

            sage: CBF(1 + I).lambert_w()
            [0.6569660692304...] + [0.3254503394134...]*I
            sage: CBF(1 + I).lambert_w(2)
            [-2.1208839379437...] + [11.600137110774...]*I
            sage: CBF(1 + I).lambert_w(2^100)
            [-70.806021532123...] + [7.9648836259913...]*I"""
    def legendre_P(self, n, m=..., type=...) -> Any:
        '''ComplexBall.legendre_P(self, n, m=0, type=2)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 5085)

        Return the Legendre function of the first kind `P_n^m(z)`
        evaluated at ``self``.

        The ``type`` parameter can be either 2 or 3. This selects between
        different branch cut conventions. The definitions of the "type 2"
        and "type 3" functions are the same as those used by *Mathematica*
        and *mpmath*.

        EXAMPLES::

            sage: CBF(1/2).legendre_P(5)
            [0.0898437500000000 +/- 7...e-17]
            sage: CBF(1,2).legendre_P(CBF(2,3), CBF(0,1))
            [0.10996180744364 +/- ...e-15] + [0.14312767804055 +/- ...e-15]*I
            sage: CBF(-10).legendre_P(5, 325/100)
            [-22104403.487377 +/- ...e-7] + [53364750.687392 +/- ...e-7]*I
            sage: CBF(-10).legendre_P(5, 325/100, type=3)
            [-57761589.914581 +/- ...e-7] + [+/- ...e-7]*I'''
    def legendre_Q(self, n, m=..., type=...) -> Any:
        '''ComplexBall.legendre_Q(self, n, m=0, type=2)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 5118)

        Return the Legendre function of the second kind `Q_n^m(z)`
        evaluated at ``self``.

        The ``type`` parameter can be either 2 or 3. This selects between
        different branch cut conventions. The definitions of the "type 2"
        and "type 3" functions are the same as those used by *Mathematica*
        and *mpmath*.

        EXAMPLES::

            sage: CBF(1/2).legendre_Q(5)
            [0.55508089057168 +/- ...e-15]
            sage: CBF(1,2).legendre_Q(CBF(2,3), CBF(0,1))
            [0.167678710 +/- ...e-10] + [-0.161558598 +/- ...e-10]*I
            sage: CBF(-10).legendre_Q(5, 325/100)
            [-83825154.36008 +/- ...e-6] + [-34721515.80396 +/- ...e-6]*I
            sage: CBF(-10).legendre_Q(5, 325/100, type=3)
            [-4.797306921692e-6 +/- ...e-19] + [-4.797306921692e-6 +/- ...e-19]*I'''
    @overload
    def li(self, booloffset=...) -> Any:
        """ComplexBall.li(self, bool offset=False)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4377)

        Return the logarithmic integral with argument ``self``.

        If ``offset`` is True, return the offset logarithmic integral.

        EXAMPLES::

            sage: CBF(1, 1).li()  # abs tol 6e-15
            [0.61391166922120 +/- 6.23e-15] + [2.05958421419258 +/- 5.59e-15]*I
            sage: CBF(0).li()
            0
            sage: CBF(0).li(offset=True)
            [-1.045163780117493 +/- ...e-16]
            sage: li(0).n()                                                             # needs sage.symbolic
            0.000000000000000
            sage: Li(0).n()                                                             # needs sage.symbolic
            -1.04516378011749

        TESTS::

            sage: CBF(li(0))                                                            # needs sage.symbolic
            0
            sage: CBF(Li(0))                                                            # needs sage.symbolic
            [-1.04516378011749...]"""
    @overload
    def li(self) -> Any:
        """ComplexBall.li(self, bool offset=False)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4377)

        Return the logarithmic integral with argument ``self``.

        If ``offset`` is True, return the offset logarithmic integral.

        EXAMPLES::

            sage: CBF(1, 1).li()  # abs tol 6e-15
            [0.61391166922120 +/- 6.23e-15] + [2.05958421419258 +/- 5.59e-15]*I
            sage: CBF(0).li()
            0
            sage: CBF(0).li(offset=True)
            [-1.045163780117493 +/- ...e-16]
            sage: li(0).n()                                                             # needs sage.symbolic
            0.000000000000000
            sage: Li(0).n()                                                             # needs sage.symbolic
            -1.04516378011749

        TESTS::

            sage: CBF(li(0))                                                            # needs sage.symbolic
            0
            sage: CBF(Li(0))                                                            # needs sage.symbolic
            [-1.04516378011749...]"""
    @overload
    def li(self) -> Any:
        """ComplexBall.li(self, bool offset=False)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4377)

        Return the logarithmic integral with argument ``self``.

        If ``offset`` is True, return the offset logarithmic integral.

        EXAMPLES::

            sage: CBF(1, 1).li()  # abs tol 6e-15
            [0.61391166922120 +/- 6.23e-15] + [2.05958421419258 +/- 5.59e-15]*I
            sage: CBF(0).li()
            0
            sage: CBF(0).li(offset=True)
            [-1.045163780117493 +/- ...e-16]
            sage: li(0).n()                                                             # needs sage.symbolic
            0.000000000000000
            sage: Li(0).n()                                                             # needs sage.symbolic
            -1.04516378011749

        TESTS::

            sage: CBF(li(0))                                                            # needs sage.symbolic
            0
            sage: CBF(Li(0))                                                            # needs sage.symbolic
            [-1.04516378011749...]"""
    @overload
    def li(self, offset=...) -> Any:
        """ComplexBall.li(self, bool offset=False)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4377)

        Return the logarithmic integral with argument ``self``.

        If ``offset`` is True, return the offset logarithmic integral.

        EXAMPLES::

            sage: CBF(1, 1).li()  # abs tol 6e-15
            [0.61391166922120 +/- 6.23e-15] + [2.05958421419258 +/- 5.59e-15]*I
            sage: CBF(0).li()
            0
            sage: CBF(0).li(offset=True)
            [-1.045163780117493 +/- ...e-16]
            sage: li(0).n()                                                             # needs sage.symbolic
            0.000000000000000
            sage: Li(0).n()                                                             # needs sage.symbolic
            -1.04516378011749

        TESTS::

            sage: CBF(li(0))                                                            # needs sage.symbolic
            0
            sage: CBF(Li(0))                                                            # needs sage.symbolic
            [-1.04516378011749...]"""
    @overload
    def log(self, base=..., analytic=...) -> Any:
        """ComplexBall.log(self, base=None, analytic=False)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3081)

        General logarithm (principal branch).

        INPUT:

        - ``base`` -- (optional) complex ball or number; if ``None``, return
          the principal branch of the natural logarithm ``ln(self)``,
          otherwise, return the general logarithm ``ln(self)/ln(base)``

        - ``analytic`` -- boolean (default: ``False``); if ``True``, return an
          indeterminate (not-a-number) value when the input ball touches
          the branch cut (with respect to ``self``)

        EXAMPLES::

            sage: CBF(2*i).log()
            [0.693147180559945 +/- ...e-16] + [1.570796326794897 +/- ...e-16]*I
            sage: CBF(-1).log()
            [3.141592653589793 +/- ...e-16]*I

            sage: CBF(2*i).log(2)
            [1.000000000000000 +/- ...e-16] + [2.26618007091360 +/- ...e-15]*I
            sage: CBF(2*i).log(CBF(i))
            [1.000000000000000 +/- ...e-16] + [-0.441271200305303 +/- ...e-16]*I

            sage: CBF('inf').log()
            [+/- inf]
            sage: CBF(2).log(0)
            nan + nan*I

            sage: CBF(-1).log(2)
            [4.53236014182719 +/- ...e-15]*I
            sage: CBF(-1).log(2, analytic=True)
            nan + nan*I
            sage: CBF(-1, RBF(0, rad=.1r)).log(analytic=False)
            [+/- ...e-3] + [+/- 3.15]*I"""
    @overload
    def log(self) -> Any:
        """ComplexBall.log(self, base=None, analytic=False)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3081)

        General logarithm (principal branch).

        INPUT:

        - ``base`` -- (optional) complex ball or number; if ``None``, return
          the principal branch of the natural logarithm ``ln(self)``,
          otherwise, return the general logarithm ``ln(self)/ln(base)``

        - ``analytic`` -- boolean (default: ``False``); if ``True``, return an
          indeterminate (not-a-number) value when the input ball touches
          the branch cut (with respect to ``self``)

        EXAMPLES::

            sage: CBF(2*i).log()
            [0.693147180559945 +/- ...e-16] + [1.570796326794897 +/- ...e-16]*I
            sage: CBF(-1).log()
            [3.141592653589793 +/- ...e-16]*I

            sage: CBF(2*i).log(2)
            [1.000000000000000 +/- ...e-16] + [2.26618007091360 +/- ...e-15]*I
            sage: CBF(2*i).log(CBF(i))
            [1.000000000000000 +/- ...e-16] + [-0.441271200305303 +/- ...e-16]*I

            sage: CBF('inf').log()
            [+/- inf]
            sage: CBF(2).log(0)
            nan + nan*I

            sage: CBF(-1).log(2)
            [4.53236014182719 +/- ...e-15]*I
            sage: CBF(-1).log(2, analytic=True)
            nan + nan*I
            sage: CBF(-1, RBF(0, rad=.1r)).log(analytic=False)
            [+/- ...e-3] + [+/- 3.15]*I"""
    @overload
    def log(self) -> Any:
        """ComplexBall.log(self, base=None, analytic=False)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3081)

        General logarithm (principal branch).

        INPUT:

        - ``base`` -- (optional) complex ball or number; if ``None``, return
          the principal branch of the natural logarithm ``ln(self)``,
          otherwise, return the general logarithm ``ln(self)/ln(base)``

        - ``analytic`` -- boolean (default: ``False``); if ``True``, return an
          indeterminate (not-a-number) value when the input ball touches
          the branch cut (with respect to ``self``)

        EXAMPLES::

            sage: CBF(2*i).log()
            [0.693147180559945 +/- ...e-16] + [1.570796326794897 +/- ...e-16]*I
            sage: CBF(-1).log()
            [3.141592653589793 +/- ...e-16]*I

            sage: CBF(2*i).log(2)
            [1.000000000000000 +/- ...e-16] + [2.26618007091360 +/- ...e-15]*I
            sage: CBF(2*i).log(CBF(i))
            [1.000000000000000 +/- ...e-16] + [-0.441271200305303 +/- ...e-16]*I

            sage: CBF('inf').log()
            [+/- inf]
            sage: CBF(2).log(0)
            nan + nan*I

            sage: CBF(-1).log(2)
            [4.53236014182719 +/- ...e-15]*I
            sage: CBF(-1).log(2, analytic=True)
            nan + nan*I
            sage: CBF(-1, RBF(0, rad=.1r)).log(analytic=False)
            [+/- ...e-3] + [+/- 3.15]*I"""
    @overload
    def log(self) -> Any:
        """ComplexBall.log(self, base=None, analytic=False)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3081)

        General logarithm (principal branch).

        INPUT:

        - ``base`` -- (optional) complex ball or number; if ``None``, return
          the principal branch of the natural logarithm ``ln(self)``,
          otherwise, return the general logarithm ``ln(self)/ln(base)``

        - ``analytic`` -- boolean (default: ``False``); if ``True``, return an
          indeterminate (not-a-number) value when the input ball touches
          the branch cut (with respect to ``self``)

        EXAMPLES::

            sage: CBF(2*i).log()
            [0.693147180559945 +/- ...e-16] + [1.570796326794897 +/- ...e-16]*I
            sage: CBF(-1).log()
            [3.141592653589793 +/- ...e-16]*I

            sage: CBF(2*i).log(2)
            [1.000000000000000 +/- ...e-16] + [2.26618007091360 +/- ...e-15]*I
            sage: CBF(2*i).log(CBF(i))
            [1.000000000000000 +/- ...e-16] + [-0.441271200305303 +/- ...e-16]*I

            sage: CBF('inf').log()
            [+/- inf]
            sage: CBF(2).log(0)
            nan + nan*I

            sage: CBF(-1).log(2)
            [4.53236014182719 +/- ...e-15]*I
            sage: CBF(-1).log(2, analytic=True)
            nan + nan*I
            sage: CBF(-1, RBF(0, rad=.1r)).log(analytic=False)
            [+/- ...e-3] + [+/- 3.15]*I"""
    @overload
    def log(self, analytic=...) -> Any:
        """ComplexBall.log(self, base=None, analytic=False)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3081)

        General logarithm (principal branch).

        INPUT:

        - ``base`` -- (optional) complex ball or number; if ``None``, return
          the principal branch of the natural logarithm ``ln(self)``,
          otherwise, return the general logarithm ``ln(self)/ln(base)``

        - ``analytic`` -- boolean (default: ``False``); if ``True``, return an
          indeterminate (not-a-number) value when the input ball touches
          the branch cut (with respect to ``self``)

        EXAMPLES::

            sage: CBF(2*i).log()
            [0.693147180559945 +/- ...e-16] + [1.570796326794897 +/- ...e-16]*I
            sage: CBF(-1).log()
            [3.141592653589793 +/- ...e-16]*I

            sage: CBF(2*i).log(2)
            [1.000000000000000 +/- ...e-16] + [2.26618007091360 +/- ...e-15]*I
            sage: CBF(2*i).log(CBF(i))
            [1.000000000000000 +/- ...e-16] + [-0.441271200305303 +/- ...e-16]*I

            sage: CBF('inf').log()
            [+/- inf]
            sage: CBF(2).log(0)
            nan + nan*I

            sage: CBF(-1).log(2)
            [4.53236014182719 +/- ...e-15]*I
            sage: CBF(-1).log(2, analytic=True)
            nan + nan*I
            sage: CBF(-1, RBF(0, rad=.1r)).log(analytic=False)
            [+/- ...e-3] + [+/- 3.15]*I"""
    @overload
    def log1p(self, analytic=...) -> Any:
        """ComplexBall.log1p(self, analytic=False)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3135)

        Return ``log(1 + self)``, computed accurately when ``self`` is close to
        zero.

        INPUT:

        - ``analytic`` -- boolean (default: ``False``); if ``True``, return an
          indeterminate (not-a-number) value when the input ball touches
          the branch cut

        EXAMPLES::

            sage: eps = RBF(1e-50)
            sage: CBF(1+eps, eps).log()
            [+/- ...e-16] + [1.000000000000000e-50 +/- ...e-66]*I
            sage: CBF(eps, eps).log1p()
            [1.000000000000000e-50 +/- ...e-68] + [1.00000000000000e-50 +/- ...e-66]*I
            sage: CBF(-3/2).log1p(analytic=True)
            nan + nan*I

        TESTS::

            sage: CBF(-1/2).log1p(analytic=True)
            [-0.693147180559945 +/- ...e-16]"""
    @overload
    def log1p(self) -> Any:
        """ComplexBall.log1p(self, analytic=False)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3135)

        Return ``log(1 + self)``, computed accurately when ``self`` is close to
        zero.

        INPUT:

        - ``analytic`` -- boolean (default: ``False``); if ``True``, return an
          indeterminate (not-a-number) value when the input ball touches
          the branch cut

        EXAMPLES::

            sage: eps = RBF(1e-50)
            sage: CBF(1+eps, eps).log()
            [+/- ...e-16] + [1.000000000000000e-50 +/- ...e-66]*I
            sage: CBF(eps, eps).log1p()
            [1.000000000000000e-50 +/- ...e-68] + [1.00000000000000e-50 +/- ...e-66]*I
            sage: CBF(-3/2).log1p(analytic=True)
            nan + nan*I

        TESTS::

            sage: CBF(-1/2).log1p(analytic=True)
            [-0.693147180559945 +/- ...e-16]"""
    @overload
    def log1p(self, analytic=...) -> Any:
        """ComplexBall.log1p(self, analytic=False)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3135)

        Return ``log(1 + self)``, computed accurately when ``self`` is close to
        zero.

        INPUT:

        - ``analytic`` -- boolean (default: ``False``); if ``True``, return an
          indeterminate (not-a-number) value when the input ball touches
          the branch cut

        EXAMPLES::

            sage: eps = RBF(1e-50)
            sage: CBF(1+eps, eps).log()
            [+/- ...e-16] + [1.000000000000000e-50 +/- ...e-66]*I
            sage: CBF(eps, eps).log1p()
            [1.000000000000000e-50 +/- ...e-68] + [1.00000000000000e-50 +/- ...e-66]*I
            sage: CBF(-3/2).log1p(analytic=True)
            nan + nan*I

        TESTS::

            sage: CBF(-1/2).log1p(analytic=True)
            [-0.693147180559945 +/- ...e-16]"""
    @overload
    def log1p(self, analytic=...) -> Any:
        """ComplexBall.log1p(self, analytic=False)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3135)

        Return ``log(1 + self)``, computed accurately when ``self`` is close to
        zero.

        INPUT:

        - ``analytic`` -- boolean (default: ``False``); if ``True``, return an
          indeterminate (not-a-number) value when the input ball touches
          the branch cut

        EXAMPLES::

            sage: eps = RBF(1e-50)
            sage: CBF(1+eps, eps).log()
            [+/- ...e-16] + [1.000000000000000e-50 +/- ...e-66]*I
            sage: CBF(eps, eps).log1p()
            [1.000000000000000e-50 +/- ...e-68] + [1.00000000000000e-50 +/- ...e-66]*I
            sage: CBF(-3/2).log1p(analytic=True)
            nan + nan*I

        TESTS::

            sage: CBF(-1/2).log1p(analytic=True)
            [-0.693147180559945 +/- ...e-16]"""
    @overload
    def log_barnes_g(self) -> Any:
        """ComplexBall.log_barnes_g(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3819)

        Return the logarithmic Barnes G-function of ``self``.

        EXAMPLES::

            sage: CBF(10^100).log_barnes_g()
            [1.14379254649702e+202 +/- ...e+187]
            sage: CBF(0,1000).log_barnes_g()
            [-2702305.04929258 +/- ...e-9] + [-790386.325561423 +/- ...e-10]*I"""
    @overload
    def log_barnes_g(self) -> Any:
        """ComplexBall.log_barnes_g(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3819)

        Return the logarithmic Barnes G-function of ``self``.

        EXAMPLES::

            sage: CBF(10^100).log_barnes_g()
            [1.14379254649702e+202 +/- ...e+187]
            sage: CBF(0,1000).log_barnes_g()
            [-2702305.04929258 +/- ...e-9] + [-790386.325561423 +/- ...e-10]*I"""
    @overload
    def log_barnes_g(self) -> Any:
        """ComplexBall.log_barnes_g(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3819)

        Return the logarithmic Barnes G-function of ``self``.

        EXAMPLES::

            sage: CBF(10^100).log_barnes_g()
            [1.14379254649702e+202 +/- ...e+187]
            sage: CBF(0,1000).log_barnes_g()
            [-2702305.04929258 +/- ...e-9] + [-790386.325561423 +/- ...e-10]*I"""
    @overload
    def log_gamma(self, analytic=...) -> Any:
        """ComplexBall.log_gamma(self, analytic=False)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3606)

        Return the image of this ball by the logarithmic Gamma function.

        The branch cut of the logarithmic gamma function is placed on the
        negative half-axis, which means that
        ``log_gamma(z) + log z = log_gamma(z+1)`` holds for all `z`,
        whereas ``log_gamma(z) != log(gamma(z))`` in general.

        INPUT:

        - ``analytic`` -- boolean (default: ``False``); if ``True``, return an
          indeterminate (not-a-number) value when the input ball touches
          the branch cut

        EXAMPLES::

            sage: CBF(1000, 1000).log_gamma()
            [5466.22252162990 +/- ...e-12] + [7039.33429191119 +/- ...e-12]*I
            sage: CBF(-1/2).log_gamma()
            [1.265512123484645 +/- ...e-16] + [-3.141592653589793 +/- ...e-16]*I
            sage: CBF(-1).log_gamma()
            nan + ...*I
            sage: CBF(-3/2).log_gamma() # abs tol 1e-14
            [0.860047015376481 +/- 3.82e-16] + [-6.283185307179586 +/- 6.77e-16]*I
            sage: CBF(-3/2).log_gamma(analytic=True)
            nan + nan*I"""
    @overload
    def log_gamma(self, z) -> Any:
        """ComplexBall.log_gamma(self, analytic=False)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3606)

        Return the image of this ball by the logarithmic Gamma function.

        The branch cut of the logarithmic gamma function is placed on the
        negative half-axis, which means that
        ``log_gamma(z) + log z = log_gamma(z+1)`` holds for all `z`,
        whereas ``log_gamma(z) != log(gamma(z))`` in general.

        INPUT:

        - ``analytic`` -- boolean (default: ``False``); if ``True``, return an
          indeterminate (not-a-number) value when the input ball touches
          the branch cut

        EXAMPLES::

            sage: CBF(1000, 1000).log_gamma()
            [5466.22252162990 +/- ...e-12] + [7039.33429191119 +/- ...e-12]*I
            sage: CBF(-1/2).log_gamma()
            [1.265512123484645 +/- ...e-16] + [-3.141592653589793 +/- ...e-16]*I
            sage: CBF(-1).log_gamma()
            nan + ...*I
            sage: CBF(-3/2).log_gamma() # abs tol 1e-14
            [0.860047015376481 +/- 3.82e-16] + [-6.283185307179586 +/- 6.77e-16]*I
            sage: CBF(-3/2).log_gamma(analytic=True)
            nan + nan*I"""
    @overload
    def log_gamma(self) -> Any:
        """ComplexBall.log_gamma(self, analytic=False)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3606)

        Return the image of this ball by the logarithmic Gamma function.

        The branch cut of the logarithmic gamma function is placed on the
        negative half-axis, which means that
        ``log_gamma(z) + log z = log_gamma(z+1)`` holds for all `z`,
        whereas ``log_gamma(z) != log(gamma(z))`` in general.

        INPUT:

        - ``analytic`` -- boolean (default: ``False``); if ``True``, return an
          indeterminate (not-a-number) value when the input ball touches
          the branch cut

        EXAMPLES::

            sage: CBF(1000, 1000).log_gamma()
            [5466.22252162990 +/- ...e-12] + [7039.33429191119 +/- ...e-12]*I
            sage: CBF(-1/2).log_gamma()
            [1.265512123484645 +/- ...e-16] + [-3.141592653589793 +/- ...e-16]*I
            sage: CBF(-1).log_gamma()
            nan + ...*I
            sage: CBF(-3/2).log_gamma() # abs tol 1e-14
            [0.860047015376481 +/- 3.82e-16] + [-6.283185307179586 +/- 6.77e-16]*I
            sage: CBF(-3/2).log_gamma(analytic=True)
            nan + nan*I"""
    @overload
    def log_gamma(self) -> Any:
        """ComplexBall.log_gamma(self, analytic=False)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3606)

        Return the image of this ball by the logarithmic Gamma function.

        The branch cut of the logarithmic gamma function is placed on the
        negative half-axis, which means that
        ``log_gamma(z) + log z = log_gamma(z+1)`` holds for all `z`,
        whereas ``log_gamma(z) != log(gamma(z))`` in general.

        INPUT:

        - ``analytic`` -- boolean (default: ``False``); if ``True``, return an
          indeterminate (not-a-number) value when the input ball touches
          the branch cut

        EXAMPLES::

            sage: CBF(1000, 1000).log_gamma()
            [5466.22252162990 +/- ...e-12] + [7039.33429191119 +/- ...e-12]*I
            sage: CBF(-1/2).log_gamma()
            [1.265512123484645 +/- ...e-16] + [-3.141592653589793 +/- ...e-16]*I
            sage: CBF(-1).log_gamma()
            nan + ...*I
            sage: CBF(-3/2).log_gamma() # abs tol 1e-14
            [0.860047015376481 +/- 3.82e-16] + [-6.283185307179586 +/- 6.77e-16]*I
            sage: CBF(-3/2).log_gamma(analytic=True)
            nan + nan*I"""
    @overload
    def log_gamma(self) -> Any:
        """ComplexBall.log_gamma(self, analytic=False)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3606)

        Return the image of this ball by the logarithmic Gamma function.

        The branch cut of the logarithmic gamma function is placed on the
        negative half-axis, which means that
        ``log_gamma(z) + log z = log_gamma(z+1)`` holds for all `z`,
        whereas ``log_gamma(z) != log(gamma(z))`` in general.

        INPUT:

        - ``analytic`` -- boolean (default: ``False``); if ``True``, return an
          indeterminate (not-a-number) value when the input ball touches
          the branch cut

        EXAMPLES::

            sage: CBF(1000, 1000).log_gamma()
            [5466.22252162990 +/- ...e-12] + [7039.33429191119 +/- ...e-12]*I
            sage: CBF(-1/2).log_gamma()
            [1.265512123484645 +/- ...e-16] + [-3.141592653589793 +/- ...e-16]*I
            sage: CBF(-1).log_gamma()
            nan + ...*I
            sage: CBF(-3/2).log_gamma() # abs tol 1e-14
            [0.860047015376481 +/- 3.82e-16] + [-6.283185307179586 +/- 6.77e-16]*I
            sage: CBF(-3/2).log_gamma(analytic=True)
            nan + nan*I"""
    @overload
    def log_gamma(self) -> Any:
        """ComplexBall.log_gamma(self, analytic=False)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3606)

        Return the image of this ball by the logarithmic Gamma function.

        The branch cut of the logarithmic gamma function is placed on the
        negative half-axis, which means that
        ``log_gamma(z) + log z = log_gamma(z+1)`` holds for all `z`,
        whereas ``log_gamma(z) != log(gamma(z))`` in general.

        INPUT:

        - ``analytic`` -- boolean (default: ``False``); if ``True``, return an
          indeterminate (not-a-number) value when the input ball touches
          the branch cut

        EXAMPLES::

            sage: CBF(1000, 1000).log_gamma()
            [5466.22252162990 +/- ...e-12] + [7039.33429191119 +/- ...e-12]*I
            sage: CBF(-1/2).log_gamma()
            [1.265512123484645 +/- ...e-16] + [-3.141592653589793 +/- ...e-16]*I
            sage: CBF(-1).log_gamma()
            nan + ...*I
            sage: CBF(-3/2).log_gamma() # abs tol 1e-14
            [0.860047015376481 +/- 3.82e-16] + [-6.283185307179586 +/- 6.77e-16]*I
            sage: CBF(-3/2).log_gamma(analytic=True)
            nan + nan*I"""
    @overload
    def log_gamma(self, analytic=...) -> Any:
        """ComplexBall.log_gamma(self, analytic=False)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3606)

        Return the image of this ball by the logarithmic Gamma function.

        The branch cut of the logarithmic gamma function is placed on the
        negative half-axis, which means that
        ``log_gamma(z) + log z = log_gamma(z+1)`` holds for all `z`,
        whereas ``log_gamma(z) != log(gamma(z))`` in general.

        INPUT:

        - ``analytic`` -- boolean (default: ``False``); if ``True``, return an
          indeterminate (not-a-number) value when the input ball touches
          the branch cut

        EXAMPLES::

            sage: CBF(1000, 1000).log_gamma()
            [5466.22252162990 +/- ...e-12] + [7039.33429191119 +/- ...e-12]*I
            sage: CBF(-1/2).log_gamma()
            [1.265512123484645 +/- ...e-16] + [-3.141592653589793 +/- ...e-16]*I
            sage: CBF(-1).log_gamma()
            nan + ...*I
            sage: CBF(-3/2).log_gamma() # abs tol 1e-14
            [0.860047015376481 +/- 3.82e-16] + [-6.283185307179586 +/- 6.77e-16]*I
            sage: CBF(-3/2).log_gamma(analytic=True)
            nan + nan*I"""
    def log_integral(self, *args, **kwargs):
        """ComplexBall.li(self, bool offset=False)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4377)

        Return the logarithmic integral with argument ``self``.

        If ``offset`` is True, return the offset logarithmic integral.

        EXAMPLES::

            sage: CBF(1, 1).li()  # abs tol 6e-15
            [0.61391166922120 +/- 6.23e-15] + [2.05958421419258 +/- 5.59e-15]*I
            sage: CBF(0).li()
            0
            sage: CBF(0).li(offset=True)
            [-1.045163780117493 +/- ...e-16]
            sage: li(0).n()                                                             # needs sage.symbolic
            0.000000000000000
            sage: Li(0).n()                                                             # needs sage.symbolic
            -1.04516378011749

        TESTS::

            sage: CBF(li(0))                                                            # needs sage.symbolic
            0
            sage: CBF(Li(0))                                                            # needs sage.symbolic
            [-1.04516378011749...]"""
    def log_integral_offset(self, *args, **kwargs):
        """ComplexBall.Li(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4411)

        Offset logarithmic integral.

        EXAMPLES::

            sage: CBF(0).Li()
            [-1.045163780117493 +/- ...e-16]
            sage: li(0).n()                                                             # needs sage.symbolic
            0.000000000000000
            sage: Li(0).n()                                                             # needs sage.symbolic
            -1.04516378011749"""
    @overload
    def mid(self) -> Any:
        """ComplexBall.mid(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 2007)

        Return the midpoint of this ball.

        OUTPUT:

        :class:`~sage.rings.complex_mpfr.ComplexNumber`, floating-point
        complex number formed by the centers of the real and imaginary parts of
        this ball.

        EXAMPLES::

            sage: CBF(1/3, 1).mid()
            0.333333333333333 + 1.00000000000000*I
            sage: CBF(1/3, 1).mid().parent()
            Complex Field with 53 bits of precision
            sage: CBF('inf', 'nan').mid()
            +infinity + NaN*I
            sage: CBF('nan', 'inf').mid()
            NaN + +infinity*I
            sage: CBF('nan').mid()
            NaN
            sage: CBF('inf').mid()
            +infinity
            sage: CBF(0, 'inf').mid()
            +infinity*I

        .. SEEALSO:: :meth:`squash`"""
    @overload
    def mid(self) -> Any:
        """ComplexBall.mid(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 2007)

        Return the midpoint of this ball.

        OUTPUT:

        :class:`~sage.rings.complex_mpfr.ComplexNumber`, floating-point
        complex number formed by the centers of the real and imaginary parts of
        this ball.

        EXAMPLES::

            sage: CBF(1/3, 1).mid()
            0.333333333333333 + 1.00000000000000*I
            sage: CBF(1/3, 1).mid().parent()
            Complex Field with 53 bits of precision
            sage: CBF('inf', 'nan').mid()
            +infinity + NaN*I
            sage: CBF('nan', 'inf').mid()
            NaN + +infinity*I
            sage: CBF('nan').mid()
            NaN
            sage: CBF('inf').mid()
            +infinity
            sage: CBF(0, 'inf').mid()
            +infinity*I

        .. SEEALSO:: :meth:`squash`"""
    @overload
    def mid(self) -> Any:
        """ComplexBall.mid(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 2007)

        Return the midpoint of this ball.

        OUTPUT:

        :class:`~sage.rings.complex_mpfr.ComplexNumber`, floating-point
        complex number formed by the centers of the real and imaginary parts of
        this ball.

        EXAMPLES::

            sage: CBF(1/3, 1).mid()
            0.333333333333333 + 1.00000000000000*I
            sage: CBF(1/3, 1).mid().parent()
            Complex Field with 53 bits of precision
            sage: CBF('inf', 'nan').mid()
            +infinity + NaN*I
            sage: CBF('nan', 'inf').mid()
            NaN + +infinity*I
            sage: CBF('nan').mid()
            NaN
            sage: CBF('inf').mid()
            +infinity
            sage: CBF(0, 'inf').mid()
            +infinity*I

        .. SEEALSO:: :meth:`squash`"""
    @overload
    def mid(self) -> Any:
        """ComplexBall.mid(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 2007)

        Return the midpoint of this ball.

        OUTPUT:

        :class:`~sage.rings.complex_mpfr.ComplexNumber`, floating-point
        complex number formed by the centers of the real and imaginary parts of
        this ball.

        EXAMPLES::

            sage: CBF(1/3, 1).mid()
            0.333333333333333 + 1.00000000000000*I
            sage: CBF(1/3, 1).mid().parent()
            Complex Field with 53 bits of precision
            sage: CBF('inf', 'nan').mid()
            +infinity + NaN*I
            sage: CBF('nan', 'inf').mid()
            NaN + +infinity*I
            sage: CBF('nan').mid()
            NaN
            sage: CBF('inf').mid()
            +infinity
            sage: CBF(0, 'inf').mid()
            +infinity*I

        .. SEEALSO:: :meth:`squash`"""
    @overload
    def mid(self) -> Any:
        """ComplexBall.mid(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 2007)

        Return the midpoint of this ball.

        OUTPUT:

        :class:`~sage.rings.complex_mpfr.ComplexNumber`, floating-point
        complex number formed by the centers of the real and imaginary parts of
        this ball.

        EXAMPLES::

            sage: CBF(1/3, 1).mid()
            0.333333333333333 + 1.00000000000000*I
            sage: CBF(1/3, 1).mid().parent()
            Complex Field with 53 bits of precision
            sage: CBF('inf', 'nan').mid()
            +infinity + NaN*I
            sage: CBF('nan', 'inf').mid()
            NaN + +infinity*I
            sage: CBF('nan').mid()
            NaN
            sage: CBF('inf').mid()
            +infinity
            sage: CBF(0, 'inf').mid()
            +infinity*I

        .. SEEALSO:: :meth:`squash`"""
    @overload
    def mid(self) -> Any:
        """ComplexBall.mid(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 2007)

        Return the midpoint of this ball.

        OUTPUT:

        :class:`~sage.rings.complex_mpfr.ComplexNumber`, floating-point
        complex number formed by the centers of the real and imaginary parts of
        this ball.

        EXAMPLES::

            sage: CBF(1/3, 1).mid()
            0.333333333333333 + 1.00000000000000*I
            sage: CBF(1/3, 1).mid().parent()
            Complex Field with 53 bits of precision
            sage: CBF('inf', 'nan').mid()
            +infinity + NaN*I
            sage: CBF('nan', 'inf').mid()
            NaN + +infinity*I
            sage: CBF('nan').mid()
            NaN
            sage: CBF('inf').mid()
            +infinity
            sage: CBF(0, 'inf').mid()
            +infinity*I

        .. SEEALSO:: :meth:`squash`"""
    @overload
    def mid(self) -> Any:
        """ComplexBall.mid(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 2007)

        Return the midpoint of this ball.

        OUTPUT:

        :class:`~sage.rings.complex_mpfr.ComplexNumber`, floating-point
        complex number formed by the centers of the real and imaginary parts of
        this ball.

        EXAMPLES::

            sage: CBF(1/3, 1).mid()
            0.333333333333333 + 1.00000000000000*I
            sage: CBF(1/3, 1).mid().parent()
            Complex Field with 53 bits of precision
            sage: CBF('inf', 'nan').mid()
            +infinity + NaN*I
            sage: CBF('nan', 'inf').mid()
            NaN + +infinity*I
            sage: CBF('nan').mid()
            NaN
            sage: CBF('inf').mid()
            +infinity
            sage: CBF(0, 'inf').mid()
            +infinity*I

        .. SEEALSO:: :meth:`squash`"""
    @overload
    def mid(self) -> Any:
        """ComplexBall.mid(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 2007)

        Return the midpoint of this ball.

        OUTPUT:

        :class:`~sage.rings.complex_mpfr.ComplexNumber`, floating-point
        complex number formed by the centers of the real and imaginary parts of
        this ball.

        EXAMPLES::

            sage: CBF(1/3, 1).mid()
            0.333333333333333 + 1.00000000000000*I
            sage: CBF(1/3, 1).mid().parent()
            Complex Field with 53 bits of precision
            sage: CBF('inf', 'nan').mid()
            +infinity + NaN*I
            sage: CBF('nan', 'inf').mid()
            NaN + +infinity*I
            sage: CBF('nan').mid()
            NaN
            sage: CBF('inf').mid()
            +infinity
            sage: CBF(0, 'inf').mid()
            +infinity*I

        .. SEEALSO:: :meth:`squash`"""
    @overload
    def modular_delta(self) -> Any:
        """ComplexBall.modular_delta(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4535)

        Return the modular discriminant with *tau* given by ``self``.

        EXAMPLES::

            sage: CBF(0,1).modular_delta()
            [0.0017853698506421 +/- ...e-17]
            sage: a, b, c, d = 2, 5, 1, 3
            sage: tau = CBF(1,3)
            sage: ((a*tau+b)/(c*tau+d)).modular_delta()
            [0.20921376655 +/- ...e-12] + [1.57611925523 +/- ...e-12]*I
            sage: (c*tau+d)^12 * tau.modular_delta()
            [0.20921376654986 +/- ...e-15] + [1.5761192552253 +/- ...e-14]*I"""
    @overload
    def modular_delta(self) -> Any:
        """ComplexBall.modular_delta(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4535)

        Return the modular discriminant with *tau* given by ``self``.

        EXAMPLES::

            sage: CBF(0,1).modular_delta()
            [0.0017853698506421 +/- ...e-17]
            sage: a, b, c, d = 2, 5, 1, 3
            sage: tau = CBF(1,3)
            sage: ((a*tau+b)/(c*tau+d)).modular_delta()
            [0.20921376655 +/- ...e-12] + [1.57611925523 +/- ...e-12]*I
            sage: (c*tau+d)^12 * tau.modular_delta()
            [0.20921376654986 +/- ...e-15] + [1.5761192552253 +/- ...e-14]*I"""
    @overload
    def modular_delta(self) -> Any:
        """ComplexBall.modular_delta(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4535)

        Return the modular discriminant with *tau* given by ``self``.

        EXAMPLES::

            sage: CBF(0,1).modular_delta()
            [0.0017853698506421 +/- ...e-17]
            sage: a, b, c, d = 2, 5, 1, 3
            sage: tau = CBF(1,3)
            sage: ((a*tau+b)/(c*tau+d)).modular_delta()
            [0.20921376655 +/- ...e-12] + [1.57611925523 +/- ...e-12]*I
            sage: (c*tau+d)^12 * tau.modular_delta()
            [0.20921376654986 +/- ...e-15] + [1.5761192552253 +/- ...e-14]*I"""
    @overload
    def modular_delta(self) -> Any:
        """ComplexBall.modular_delta(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4535)

        Return the modular discriminant with *tau* given by ``self``.

        EXAMPLES::

            sage: CBF(0,1).modular_delta()
            [0.0017853698506421 +/- ...e-17]
            sage: a, b, c, d = 2, 5, 1, 3
            sage: tau = CBF(1,3)
            sage: ((a*tau+b)/(c*tau+d)).modular_delta()
            [0.20921376655 +/- ...e-12] + [1.57611925523 +/- ...e-12]*I
            sage: (c*tau+d)^12 * tau.modular_delta()
            [0.20921376654986 +/- ...e-15] + [1.5761192552253 +/- ...e-14]*I"""
    @overload
    def modular_eta(self) -> Any:
        """ComplexBall.modular_eta(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4497)

        Return the Dedekind eta function with *tau* given by ``self``.

        EXAMPLES::

            sage: CBF(0,1).modular_eta()
            [0.768225422326057 +/- ...e-16]
            sage: CBF(12,1).modular_eta()
            [-0.768225422326057 +/- ...e-16]"""
    @overload
    def modular_eta(self) -> Any:
        """ComplexBall.modular_eta(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4497)

        Return the Dedekind eta function with *tau* given by ``self``.

        EXAMPLES::

            sage: CBF(0,1).modular_eta()
            [0.768225422326057 +/- ...e-16]
            sage: CBF(12,1).modular_eta()
            [-0.768225422326057 +/- ...e-16]"""
    @overload
    def modular_eta(self) -> Any:
        """ComplexBall.modular_eta(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4497)

        Return the Dedekind eta function with *tau* given by ``self``.

        EXAMPLES::

            sage: CBF(0,1).modular_eta()
            [0.768225422326057 +/- ...e-16]
            sage: CBF(12,1).modular_eta()
            [-0.768225422326057 +/- ...e-16]"""
    @overload
    def modular_j(self) -> Any:
        """ComplexBall.modular_j(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4482)

        Return the modular j-invariant with *tau* given by ``self``.

        EXAMPLES::

            sage: CBF(0,1).modular_j()
            [1728.0000000000 +/- ...e-11]"""
    @overload
    def modular_j(self) -> Any:
        """ComplexBall.modular_j(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4482)

        Return the modular j-invariant with *tau* given by ``self``.

        EXAMPLES::

            sage: CBF(0,1).modular_j()
            [1728.0000000000 +/- ...e-11]"""
    @overload
    def modular_lambda(self) -> Any:
        """ComplexBall.modular_lambda(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4514)

        Return the modular lambda function with *tau* given by ``self``.

        EXAMPLES::

            sage: # needs sage.symbolic
            sage: tau = CBF(sqrt(2),pi)
            sage: tau.modular_lambda()
            [-0.00022005123884157 +/- ...e-18] + [-0.00079787346459944 +/- ...e-18]*I
            sage: (tau + 2).modular_lambda()
            [-0.00022005123884157 +/- ...e-18] + [-0.00079787346459944 +/- ...e-18]*I
            sage: (tau / (1 - 2*tau)).modular_lambda()
            [-0.00022005123884 +/- ...e-15] + [-0.00079787346460 +/- ...e-15]*I"""
    @overload
    def modular_lambda(self) -> Any:
        """ComplexBall.modular_lambda(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4514)

        Return the modular lambda function with *tau* given by ``self``.

        EXAMPLES::

            sage: # needs sage.symbolic
            sage: tau = CBF(sqrt(2),pi)
            sage: tau.modular_lambda()
            [-0.00022005123884157 +/- ...e-18] + [-0.00079787346459944 +/- ...e-18]*I
            sage: (tau + 2).modular_lambda()
            [-0.00022005123884157 +/- ...e-18] + [-0.00079787346459944 +/- ...e-18]*I
            sage: (tau / (1 - 2*tau)).modular_lambda()
            [-0.00022005123884 +/- ...e-15] + [-0.00079787346460 +/- ...e-15]*I"""
    @overload
    def modular_lambda(self) -> Any:
        """ComplexBall.modular_lambda(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4514)

        Return the modular lambda function with *tau* given by ``self``.

        EXAMPLES::

            sage: # needs sage.symbolic
            sage: tau = CBF(sqrt(2),pi)
            sage: tau.modular_lambda()
            [-0.00022005123884157 +/- ...e-18] + [-0.00079787346459944 +/- ...e-18]*I
            sage: (tau + 2).modular_lambda()
            [-0.00022005123884157 +/- ...e-18] + [-0.00079787346459944 +/- ...e-18]*I
            sage: (tau / (1 - 2*tau)).modular_lambda()
            [-0.00022005123884 +/- ...e-15] + [-0.00079787346460 +/- ...e-15]*I"""
    @overload
    def modular_lambda(self) -> Any:
        """ComplexBall.modular_lambda(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4514)

        Return the modular lambda function with *tau* given by ``self``.

        EXAMPLES::

            sage: # needs sage.symbolic
            sage: tau = CBF(sqrt(2),pi)
            sage: tau.modular_lambda()
            [-0.00022005123884157 +/- ...e-18] + [-0.00079787346459944 +/- ...e-18]*I
            sage: (tau + 2).modular_lambda()
            [-0.00022005123884157 +/- ...e-18] + [-0.00079787346459944 +/- ...e-18]*I
            sage: (tau / (1 - 2*tau)).modular_lambda()
            [-0.00022005123884 +/- ...e-15] + [-0.00079787346460 +/- ...e-15]*I"""
    @overload
    def nbits(self) -> Any:
        """ComplexBall.nbits(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 2155)

        Return the minimum precision sufficient to represent this ball exactly.

        More precisely, the output is the number of bits needed to represent
        the absolute value of the mantissa of both the real and the imaginary
        part of the midpoint.

        EXAMPLES::

            sage: CBF(17, 1023).nbits()
            10
            sage: CBF(1/3, NaN).nbits()                                                 # needs sage.symbolic
            53
            sage: CBF(NaN).nbits()                                                      # needs sage.symbolic
            0"""
    @overload
    def nbits(self) -> Any:
        """ComplexBall.nbits(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 2155)

        Return the minimum precision sufficient to represent this ball exactly.

        More precisely, the output is the number of bits needed to represent
        the absolute value of the mantissa of both the real and the imaginary
        part of the midpoint.

        EXAMPLES::

            sage: CBF(17, 1023).nbits()
            10
            sage: CBF(1/3, NaN).nbits()                                                 # needs sage.symbolic
            53
            sage: CBF(NaN).nbits()                                                      # needs sage.symbolic
            0"""
    @overload
    def nbits(self) -> Any:
        """ComplexBall.nbits(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 2155)

        Return the minimum precision sufficient to represent this ball exactly.

        More precisely, the output is the number of bits needed to represent
        the absolute value of the mantissa of both the real and the imaginary
        part of the midpoint.

        EXAMPLES::

            sage: CBF(17, 1023).nbits()
            10
            sage: CBF(1/3, NaN).nbits()                                                 # needs sage.symbolic
            53
            sage: CBF(NaN).nbits()                                                      # needs sage.symbolic
            0"""
    @overload
    def nbits(self) -> Any:
        """ComplexBall.nbits(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 2155)

        Return the minimum precision sufficient to represent this ball exactly.

        More precisely, the output is the number of bits needed to represent
        the absolute value of the mantissa of both the real and the imaginary
        part of the midpoint.

        EXAMPLES::

            sage: CBF(17, 1023).nbits()
            10
            sage: CBF(1/3, NaN).nbits()                                                 # needs sage.symbolic
            53
            sage: CBF(NaN).nbits()                                                      # needs sage.symbolic
            0"""
    def overlaps(self, ComplexBallother) -> Any:
        """ComplexBall.overlaps(self, ComplexBall other)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 2525)

        Return ``True`` iff ``self`` and ``other`` have some point in common.

        INPUT:

        - ``other`` -- a :class:`ComplexBall`

        EXAMPLES::

            sage: CBF(1, 1).overlaps(1 + CBF(0, 1/3)*3)
            True
            sage: CBF(1, 1).overlaps(CBF(1, 'nan'))
            True
            sage: CBF(1, 1).overlaps(CBF(0, 'nan'))
            False"""
    def polylog(self, s) -> Any:
        """ComplexBall.polylog(self, s)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3766)

        Return the polylogarithm `\\operatorname{Li}_s(\\mathrm{self})`.

        EXAMPLES::

            sage: CBF(2).polylog(1)
            [+/- ...e-15] + [-3.14159265358979 +/- ...e-15]*I
            sage: CBF(1, 1).polylog(CBF(1, 1))
            [0.3708160030469 +/- ...e-14] + [2.7238016577979 +/- ...e-14]*I

        TESTS::

            sage: CBF(2).polylog(1r)
            [+/- ...e-15] + [-3.14159265358979 +/- ...e-15]*I"""
    def pow(self, expo, analytic=...) -> Any:
        """ComplexBall.pow(self, expo, analytic=False)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 2902)

        Raise this ball to the power of ``expo``.

        INPUT:

        - ``analytic`` -- boolean (default: ``False``); if ``True``, return an
          indeterminate (not-a-number) value when the exponent is not an
          integer and the base ball touches the branch cut of the logarithm

        EXAMPLES::

            sage: CBF(-1).pow(CBF(i))
            [0.0432139182637723 +/- ...e-17]
            sage: CBF(-1).pow(CBF(i), analytic=True)
            nan + nan*I
            sage: CBF(-10).pow(-2)
            [0.0100000000000000 +/- ...e-18]
            sage: CBF(-10).pow(-2, analytic=True)
            [0.0100000000000000 +/- ...e-18]

        TESTS::

            sage: CBF(2).pow(SR.var('x'))                                               # needs sage.symbolic
            Traceback (most recent call last):
            ...
            TypeError: no canonical coercion from Symbolic Ring to Complex ball
            field with 53 bits of precision"""
    @overload
    def psi(self, n=...) -> Any:
        """ComplexBall.psi(self, n=None)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3661)

        Compute the digamma function with argument ``self``.

        If ``n`` is provided, compute the polygamma function of order ``n``
        and argument ``self``.

        EXAMPLES::

            sage: CBF(1, 1).psi()
            [0.0946503206224770 +/- ...e-17] + [1.076674047468581 +/- ...e-16]*I
            sage: CBF(-1).psi()
            nan
            sage: CBF(1,1).psi(10)
            [56514.8269344249 +/- ...e-11] + [56215.1218005823 +/- ...e-11]*I"""
    @overload
    def psi(self) -> Any:
        """ComplexBall.psi(self, n=None)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3661)

        Compute the digamma function with argument ``self``.

        If ``n`` is provided, compute the polygamma function of order ``n``
        and argument ``self``.

        EXAMPLES::

            sage: CBF(1, 1).psi()
            [0.0946503206224770 +/- ...e-17] + [1.076674047468581 +/- ...e-16]*I
            sage: CBF(-1).psi()
            nan
            sage: CBF(1,1).psi(10)
            [56514.8269344249 +/- ...e-11] + [56215.1218005823 +/- ...e-11]*I"""
    @overload
    def psi(self) -> Any:
        """ComplexBall.psi(self, n=None)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3661)

        Compute the digamma function with argument ``self``.

        If ``n`` is provided, compute the polygamma function of order ``n``
        and argument ``self``.

        EXAMPLES::

            sage: CBF(1, 1).psi()
            [0.0946503206224770 +/- ...e-17] + [1.076674047468581 +/- ...e-16]*I
            sage: CBF(-1).psi()
            nan
            sage: CBF(1,1).psi(10)
            [56514.8269344249 +/- ...e-11] + [56215.1218005823 +/- ...e-11]*I"""
    @overload
    def rad(self) -> Any:
        """ComplexBall.rad(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 2066)

        Return an upper bound for the error radius of this ball.

        OUTPUT:

        A :class:`~sage.rings.real_mpfr.RealNumber` of the same precision as
        the radii of real balls.

        .. WARNING::

            Unlike a :class:`~sage.rings.real_arb.RealBall`,
            a :class:`ComplexBall` is *not* defined
            by its midpoint and radius. (Instances of :class:`ComplexBall` are
            actually rectangles, not balls.)

        EXAMPLES::

            sage: CBF(1 + i).rad()
            0.00000000
            sage: CBF(i/3).rad()
            1.1102230e-16
            sage: CBF(i/3).rad().parent()
            Real Field with 30 bits of precision

        .. SEEALSO:: :meth:`diameter`, :meth:`mid`

        TESTS::

            sage: (CBF(0, 1/3) << (2^64)).rad()
            Traceback (most recent call last):
            ...
            RuntimeError: unable to convert the radius to MPFR (exponent out of range?)"""
    @overload
    def rad(self) -> Any:
        """ComplexBall.rad(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 2066)

        Return an upper bound for the error radius of this ball.

        OUTPUT:

        A :class:`~sage.rings.real_mpfr.RealNumber` of the same precision as
        the radii of real balls.

        .. WARNING::

            Unlike a :class:`~sage.rings.real_arb.RealBall`,
            a :class:`ComplexBall` is *not* defined
            by its midpoint and radius. (Instances of :class:`ComplexBall` are
            actually rectangles, not balls.)

        EXAMPLES::

            sage: CBF(1 + i).rad()
            0.00000000
            sage: CBF(i/3).rad()
            1.1102230e-16
            sage: CBF(i/3).rad().parent()
            Real Field with 30 bits of precision

        .. SEEALSO:: :meth:`diameter`, :meth:`mid`

        TESTS::

            sage: (CBF(0, 1/3) << (2^64)).rad()
            Traceback (most recent call last):
            ...
            RuntimeError: unable to convert the radius to MPFR (exponent out of range?)"""
    @overload
    def rad(self) -> Any:
        """ComplexBall.rad(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 2066)

        Return an upper bound for the error radius of this ball.

        OUTPUT:

        A :class:`~sage.rings.real_mpfr.RealNumber` of the same precision as
        the radii of real balls.

        .. WARNING::

            Unlike a :class:`~sage.rings.real_arb.RealBall`,
            a :class:`ComplexBall` is *not* defined
            by its midpoint and radius. (Instances of :class:`ComplexBall` are
            actually rectangles, not balls.)

        EXAMPLES::

            sage: CBF(1 + i).rad()
            0.00000000
            sage: CBF(i/3).rad()
            1.1102230e-16
            sage: CBF(i/3).rad().parent()
            Real Field with 30 bits of precision

        .. SEEALSO:: :meth:`diameter`, :meth:`mid`

        TESTS::

            sage: (CBF(0, 1/3) << (2^64)).rad()
            Traceback (most recent call last):
            ...
            RuntimeError: unable to convert the radius to MPFR (exponent out of range?)"""
    @overload
    def rad(self) -> Any:
        """ComplexBall.rad(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 2066)

        Return an upper bound for the error radius of this ball.

        OUTPUT:

        A :class:`~sage.rings.real_mpfr.RealNumber` of the same precision as
        the radii of real balls.

        .. WARNING::

            Unlike a :class:`~sage.rings.real_arb.RealBall`,
            a :class:`ComplexBall` is *not* defined
            by its midpoint and radius. (Instances of :class:`ComplexBall` are
            actually rectangles, not balls.)

        EXAMPLES::

            sage: CBF(1 + i).rad()
            0.00000000
            sage: CBF(i/3).rad()
            1.1102230e-16
            sage: CBF(i/3).rad().parent()
            Real Field with 30 bits of precision

        .. SEEALSO:: :meth:`diameter`, :meth:`mid`

        TESTS::

            sage: (CBF(0, 1/3) << (2^64)).rad()
            Traceback (most recent call last):
            ...
            RuntimeError: unable to convert the radius to MPFR (exponent out of range?)"""
    @overload
    def rad(self) -> Any:
        """ComplexBall.rad(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 2066)

        Return an upper bound for the error radius of this ball.

        OUTPUT:

        A :class:`~sage.rings.real_mpfr.RealNumber` of the same precision as
        the radii of real balls.

        .. WARNING::

            Unlike a :class:`~sage.rings.real_arb.RealBall`,
            a :class:`ComplexBall` is *not* defined
            by its midpoint and radius. (Instances of :class:`ComplexBall` are
            actually rectangles, not balls.)

        EXAMPLES::

            sage: CBF(1 + i).rad()
            0.00000000
            sage: CBF(i/3).rad()
            1.1102230e-16
            sage: CBF(i/3).rad().parent()
            Real Field with 30 bits of precision

        .. SEEALSO:: :meth:`diameter`, :meth:`mid`

        TESTS::

            sage: (CBF(0, 1/3) << (2^64)).rad()
            Traceback (most recent call last):
            ...
            RuntimeError: unable to convert the radius to MPFR (exponent out of range?)"""
    @overload
    def real(self) -> RealBall:
        """ComplexBall.real(self) -> RealBall

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 1875)

        Return the real part of this ball.

        OUTPUT: a :class:`~sage.rings.real_arb.RealBall`

        EXAMPLES::

           sage: a = CBF(1/3, 1/5)
           sage: a.real()
           [0.3333333333333333 +/- ...e-17]
           sage: a.real().parent()
           Real ball field with 53 bits of precision"""
    @overload
    def real(self) -> Any:
        """ComplexBall.real(self) -> RealBall

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 1875)

        Return the real part of this ball.

        OUTPUT: a :class:`~sage.rings.real_arb.RealBall`

        EXAMPLES::

           sage: a = CBF(1/3, 1/5)
           sage: a.real()
           [0.3333333333333333 +/- ...e-17]
           sage: a.real().parent()
           Real ball field with 53 bits of precision"""
    @overload
    def real(self) -> Any:
        """ComplexBall.real(self) -> RealBall

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 1875)

        Return the real part of this ball.

        OUTPUT: a :class:`~sage.rings.real_arb.RealBall`

        EXAMPLES::

           sage: a = CBF(1/3, 1/5)
           sage: a.real()
           [0.3333333333333333 +/- ...e-17]
           sage: a.real().parent()
           Real ball field with 53 bits of precision"""
    @overload
    def rgamma(self) -> Any:
        """ComplexBall.rgamma(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3644)

        Compute the reciprocal gamma function with argument ``self``.

        EXAMPLES::

            sage: CBF(6).rgamma()
            [0.00833333333333333 +/- ...e-18]
            sage: CBF(-1).rgamma()
            0"""
    @overload
    def rgamma(self) -> Any:
        """ComplexBall.rgamma(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3644)

        Compute the reciprocal gamma function with argument ``self``.

        EXAMPLES::

            sage: CBF(6).rgamma()
            [0.00833333333333333 +/- ...e-18]
            sage: CBF(-1).rgamma()
            0"""
    @overload
    def rgamma(self) -> Any:
        """ComplexBall.rgamma(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3644)

        Compute the reciprocal gamma function with argument ``self``.

        EXAMPLES::

            sage: CBF(6).rgamma()
            [0.00833333333333333 +/- ...e-18]
            sage: CBF(-1).rgamma()
            0"""
    def rising_factorial(self, n) -> Any:
        """ComplexBall.rising_factorial(self, n)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3048)

        Return the ``n``-th rising factorial of this ball.

        The `n`-th rising factorial of `x` is equal to `x (x+1) \\cdots (x+n-1)`.

        For complex `n`, it is a quotient of gamma functions.

        EXAMPLES::

            sage: CBF(1).rising_factorial(5)
            120.0000000000000
            sage: CBF(1/3, 1/2).rising_factorial(300)
            [-3.87949484514e+612 +/- 5...e+600] + [-3.52042209763e+612 +/- 5...e+600]*I

            sage: CBF(1).rising_factorial(-1)
            nan
            sage: CBF(1).rising_factorial(2**64)
            [+/- ...e+347382171326740403407]
            sage: ComplexBallField(128)(1).rising_factorial(2**64)
            [2.34369112679686134...e+347382171305201285713 +/- ...]
            sage: CBF(1/2).rising_factorial(CBF(2,3)) # abs tol 1e-15
            [-0.123060451458124 +/- 3.06e-16] + [0.0406412631676552 +/- 7.57e-17]*I"""
    def round(self) -> Any:
        """ComplexBall.round(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 2174)

        Return a copy of this ball rounded to the precision of the parent.

        EXAMPLES:

        It is possible to create balls whose midpoint is more precise that
        their parent's nominal precision (see :mod:`~sage.rings.real_arb` for
        more information)::

            sage: b = CBF(exp(I*pi/3).n(100))                                           # needs sage.symbolic
            sage: b.mid()                                                               # needs sage.symbolic
            0.50000000000000000000000000000 + 0.86602540378443864676372317075*I

        The ``round()`` method rounds such a ball to its parent's precision::

            sage: b.round().mid()                                                       # needs sage.symbolic
            0.500000000000000 + 0.866025403784439*I

        .. SEEALSO:: :meth:`trim`"""
    @overload
    def rsqrt(self, analytic=...) -> Any:
        """ComplexBall.rsqrt(self, analytic=False)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 2996)

        Return the reciprocal square root of ``self``.

        If either the real or imaginary part is exactly zero, only a single
        real reciprocal square root is needed.

        INPUT:

        - ``analytic`` -- boolean (default: ``False``); if ``True``, return an
          indeterminate (not-a-number) value when the input ball touches
          the branch cut

        EXAMPLES::

            sage: CBF(-2).rsqrt()
            [-0.707106781186547 +/- ...e-16]*I
            sage: CBF(-2).rsqrt(analytic=True)
            nan + nan*I
            sage: CBF(0, 1/2).rsqrt()
            1.000000000000000 - 1.000000000000000*I
            sage: CBF(0).rsqrt()
            nan + nan*I"""
    @overload
    def rsqrt(self) -> Any:
        """ComplexBall.rsqrt(self, analytic=False)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 2996)

        Return the reciprocal square root of ``self``.

        If either the real or imaginary part is exactly zero, only a single
        real reciprocal square root is needed.

        INPUT:

        - ``analytic`` -- boolean (default: ``False``); if ``True``, return an
          indeterminate (not-a-number) value when the input ball touches
          the branch cut

        EXAMPLES::

            sage: CBF(-2).rsqrt()
            [-0.707106781186547 +/- ...e-16]*I
            sage: CBF(-2).rsqrt(analytic=True)
            nan + nan*I
            sage: CBF(0, 1/2).rsqrt()
            1.000000000000000 - 1.000000000000000*I
            sage: CBF(0).rsqrt()
            nan + nan*I"""
    @overload
    def rsqrt(self, analytic=...) -> Any:
        """ComplexBall.rsqrt(self, analytic=False)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 2996)

        Return the reciprocal square root of ``self``.

        If either the real or imaginary part is exactly zero, only a single
        real reciprocal square root is needed.

        INPUT:

        - ``analytic`` -- boolean (default: ``False``); if ``True``, return an
          indeterminate (not-a-number) value when the input ball touches
          the branch cut

        EXAMPLES::

            sage: CBF(-2).rsqrt()
            [-0.707106781186547 +/- ...e-16]*I
            sage: CBF(-2).rsqrt(analytic=True)
            nan + nan*I
            sage: CBF(0, 1/2).rsqrt()
            1.000000000000000 - 1.000000000000000*I
            sage: CBF(0).rsqrt()
            nan + nan*I"""
    @overload
    def rsqrt(self) -> Any:
        """ComplexBall.rsqrt(self, analytic=False)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 2996)

        Return the reciprocal square root of ``self``.

        If either the real or imaginary part is exactly zero, only a single
        real reciprocal square root is needed.

        INPUT:

        - ``analytic`` -- boolean (default: ``False``); if ``True``, return an
          indeterminate (not-a-number) value when the input ball touches
          the branch cut

        EXAMPLES::

            sage: CBF(-2).rsqrt()
            [-0.707106781186547 +/- ...e-16]*I
            sage: CBF(-2).rsqrt(analytic=True)
            nan + nan*I
            sage: CBF(0, 1/2).rsqrt()
            1.000000000000000 - 1.000000000000000*I
            sage: CBF(0).rsqrt()
            nan + nan*I"""
    @overload
    def rsqrt(self) -> Any:
        """ComplexBall.rsqrt(self, analytic=False)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 2996)

        Return the reciprocal square root of ``self``.

        If either the real or imaginary part is exactly zero, only a single
        real reciprocal square root is needed.

        INPUT:

        - ``analytic`` -- boolean (default: ``False``); if ``True``, return an
          indeterminate (not-a-number) value when the input ball touches
          the branch cut

        EXAMPLES::

            sage: CBF(-2).rsqrt()
            [-0.707106781186547 +/- ...e-16]*I
            sage: CBF(-2).rsqrt(analytic=True)
            nan + nan*I
            sage: CBF(0, 1/2).rsqrt()
            1.000000000000000 - 1.000000000000000*I
            sage: CBF(0).rsqrt()
            nan + nan*I"""
    @overload
    def sec(self) -> Any:
        """ComplexBall.sec(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3269)

        Return the secant of this ball.

        EXAMPLES::

            sage: CBF(1, 1).sec()
            [0.498337030555187 +/- ...e-16] + [0.591083841721045 +/- ...e-16]*I"""
    @overload
    def sec(self) -> Any:
        """ComplexBall.sec(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3269)

        Return the secant of this ball.

        EXAMPLES::

            sage: CBF(1, 1).sec()
            [0.498337030555187 +/- ...e-16] + [0.591083841721045 +/- ...e-16]*I"""
    @overload
    def sech(self) -> Any:
        """ComplexBall.sech(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3363)

        Return the hyperbolic secant of this ball.

        EXAMPLES::

            sage: CBF(pi/2, 1/10).sech()                                                # needs sage.symbolic
            [0.397174529918189 +/- ...e-16] + [-0.0365488656274242 +/- ...e-17]*I"""
    @overload
    def sech(self) -> Any:
        """ComplexBall.sech(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3363)

        Return the hyperbolic secant of this ball.

        EXAMPLES::

            sage: CBF(pi/2, 1/10).sech()                                                # needs sage.symbolic
            [0.397174529918189 +/- ...e-16] + [-0.0365488656274242 +/- ...e-17]*I"""
    @overload
    def sin(self) -> Any:
        """ComplexBall.sin(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3205)

        Return the sine of this ball.

        EXAMPLES::

            sage: CBF(i*pi).sin()                                                       # needs sage.symbolic
            [11.54873935725775 +/- ...e-15]*I"""
    @overload
    def sin(self) -> Any:
        """ComplexBall.sin(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3205)

        Return the sine of this ball.

        EXAMPLES::

            sage: CBF(i*pi).sin()                                                       # needs sage.symbolic
            [11.54873935725775 +/- ...e-15]*I"""
    def sin_integral(self, *args, **kwargs):
        """ComplexBall.Si(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4281)

        Return the sine integral with argument ``self``.

        EXAMPLES::

            sage: CBF(1, 1).Si()  # abs tol 3e-15
            [1.10422265823558 +/- 2.48e-15] + [0.88245380500792 +/- 3.36e-15]*I
            sage: CBF(0).Si()
            0

        TESTS:

            sage: CBF(Si(I))  # abs tol 3e-15                                           # needs sage.symbolic
            [1.05725087537573 +/- 2.77e-15]*I"""
    @overload
    def sinh(self) -> Any:
        """ComplexBall.sinh(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3299)

        Return the hyperbolic sine of this ball.

        EXAMPLES::

            sage: CBF(1, 1).sinh()
            [0.634963914784736 +/- ...e-16] + [1.298457581415977 +/- ...e-16]*I"""
    @overload
    def sinh(self) -> Any:
        """ComplexBall.sinh(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3299)

        Return the hyperbolic sine of this ball.

        EXAMPLES::

            sage: CBF(1, 1).sinh()
            [0.634963914784736 +/- ...e-16] + [1.298457581415977 +/- ...e-16]*I"""
    def sinh_integral(self, *args, **kwargs):
        """ComplexBall.Shi(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4329)

        Return the hyperbolic sine integral with argument ``self``.

        EXAMPLES::

            sage: CBF(1, 1).Shi()  # abs tol 3e-15
            [0.88245380500792 +/- 3.36e-15] + [1.10422265823558 +/- 2.48e-15]*I
            sage: CBF(0).Shi()
            0

        TESTS:

            sage: CBF(Shi(I))  # abs tol 1e-15                                          # needs sage.symbolic
            [0.946083070367183 +/- 9.22e-16]*I"""
    def spherical_harmonic(self, phi, n, m) -> Any:
        """ComplexBall.spherical_harmonic(self, phi, n, m)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 5151)

        Return the spherical harmonic `Y_n^m(\\theta,\\phi)`
        evaluated at `\\theta` given by ``self``.
        In the current implementation, ``n`` and ``m`` must be small integers.

        EXAMPLES::

            sage: CBF(1+I).spherical_harmonic(1/2, -3, -2)
            [0.80370071745224 +/- ...e-15] + [-0.07282031864711 +/- ...e-15]*I"""
    @overload
    def sqrt(self, analytic=...) -> Any:
        """ComplexBall.sqrt(self, analytic=False)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 2966)

        Return the square root of this ball.

        If either the real or imaginary part is exactly zero, only a single
        real square root is needed.

        INPUT:

        - ``analytic`` -- boolean (default: ``False``); if ``True``, return an
          indeterminate (not-a-number) value when the input ball touches
          the branch cut

        EXAMPLES::

            sage: CBF(-2).sqrt()
            [1.414213562373095 +/- ...e-16]*I
            sage: CBF(-2).sqrt(analytic=True)
            nan + nan*I"""
    @overload
    def sqrt(self) -> Any:
        """ComplexBall.sqrt(self, analytic=False)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 2966)

        Return the square root of this ball.

        If either the real or imaginary part is exactly zero, only a single
        real square root is needed.

        INPUT:

        - ``analytic`` -- boolean (default: ``False``); if ``True``, return an
          indeterminate (not-a-number) value when the input ball touches
          the branch cut

        EXAMPLES::

            sage: CBF(-2).sqrt()
            [1.414213562373095 +/- ...e-16]*I
            sage: CBF(-2).sqrt(analytic=True)
            nan + nan*I"""
    @overload
    def sqrt(self, analytic=...) -> Any:
        """ComplexBall.sqrt(self, analytic=False)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 2966)

        Return the square root of this ball.

        If either the real or imaginary part is exactly zero, only a single
        real square root is needed.

        INPUT:

        - ``analytic`` -- boolean (default: ``False``); if ``True``, return an
          indeterminate (not-a-number) value when the input ball touches
          the branch cut

        EXAMPLES::

            sage: CBF(-2).sqrt()
            [1.414213562373095 +/- ...e-16]*I
            sage: CBF(-2).sqrt(analytic=True)
            nan + nan*I"""
    @overload
    def squash(self) -> Any:
        """ComplexBall.squash(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 2041)

        Return an exact ball with the same midpoint as this ball.

        OUTPUT: a :class:`ComplexBall`

        EXAMPLES::

            sage: mid = CBF(1/3, 1/10).squash()
            sage: mid
            [0.3333333333333333 +/- ...e-17] + [0.09999999999999999 +/- ...e-18]*I
            sage: mid.parent()
            Complex ball field with 53 bits of precision
            sage: mid.is_exact()
            True

        .. SEEALSO:: :meth:`mid`"""
    @overload
    def squash(self) -> Any:
        """ComplexBall.squash(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 2041)

        Return an exact ball with the same midpoint as this ball.

        OUTPUT: a :class:`ComplexBall`

        EXAMPLES::

            sage: mid = CBF(1/3, 1/10).squash()
            sage: mid
            [0.3333333333333333 +/- ...e-17] + [0.09999999999999999 +/- ...e-18]*I
            sage: mid.parent()
            Complex ball field with 53 bits of precision
            sage: mid.is_exact()
            True

        .. SEEALSO:: :meth:`mid`"""
    @overload
    def tan(self) -> Any:
        """ComplexBall.tan(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3235)

        Return the tangent of this ball.

        EXAMPLES::

            sage: CBF(pi/2, 1/10).tan()                                                 # needs sage.symbolic
            [+/- ...e-14] + [10.03331113225399 +/- ...e-15]*I
            sage: CBF(pi/2).tan()                                                       # needs sage.symbolic
            nan"""
    @overload
    def tan(self) -> Any:
        """ComplexBall.tan(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3235)

        Return the tangent of this ball.

        EXAMPLES::

            sage: CBF(pi/2, 1/10).tan()                                                 # needs sage.symbolic
            [+/- ...e-14] + [10.03331113225399 +/- ...e-15]*I
            sage: CBF(pi/2).tan()                                                       # needs sage.symbolic
            nan"""
    @overload
    def tan(self) -> Any:
        """ComplexBall.tan(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3235)

        Return the tangent of this ball.

        EXAMPLES::

            sage: CBF(pi/2, 1/10).tan()                                                 # needs sage.symbolic
            [+/- ...e-14] + [10.03331113225399 +/- ...e-15]*I
            sage: CBF(pi/2).tan()                                                       # needs sage.symbolic
            nan"""
    @overload
    def tanh(self) -> Any:
        """ComplexBall.tanh(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3329)

        Return the hyperbolic tangent of this ball.

        EXAMPLES::

            sage: CBF(1, 1).tanh()
            [1.083923327338694 +/- ...e-16] + [0.2717525853195117 +/- ...e-17]*I
            sage: CBF(0, pi/2).tanh()                                                   # needs sage.symbolic
            nan*I"""
    @overload
    def tanh(self) -> Any:
        """ComplexBall.tanh(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3329)

        Return the hyperbolic tangent of this ball.

        EXAMPLES::

            sage: CBF(1, 1).tanh()
            [1.083923327338694 +/- ...e-16] + [0.2717525853195117 +/- ...e-17]*I
            sage: CBF(0, pi/2).tanh()                                                   # needs sage.symbolic
            nan*I"""
    @overload
    def tanh(self) -> Any:
        """ComplexBall.tanh(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3329)

        Return the hyperbolic tangent of this ball.

        EXAMPLES::

            sage: CBF(1, 1).tanh()
            [1.083923327338694 +/- ...e-16] + [0.2717525853195117 +/- ...e-17]*I
            sage: CBF(0, pi/2).tanh()                                                   # needs sage.symbolic
            nan*I"""
    @overload
    def trim(self) -> Any:
        """ComplexBall.trim(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 2226)

        Return a trimmed copy of this ball.

        Return a copy of this ball with both the real and imaginary parts
        trimmed (see :meth:`~sage.rings.real_arb.RealBall.trim()`).

        EXAMPLES::

            sage: b = CBF(1/3, RBF(1/3, rad=.01))
            sage: b.mid()
            0.333333333333333 + 0.333333333333333*I
            sage: b.trim().mid()
            0.333333333333333 + 0.333333015441895*I

        .. SEEALSO:: :meth:`round`"""
    @overload
    def trim(self) -> Any:
        """ComplexBall.trim(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 2226)

        Return a trimmed copy of this ball.

        Return a copy of this ball with both the real and imaginary parts
        trimmed (see :meth:`~sage.rings.real_arb.RealBall.trim()`).

        EXAMPLES::

            sage: b = CBF(1/3, RBF(1/3, rad=.01))
            sage: b.mid()
            0.333333333333333 + 0.333333333333333*I
            sage: b.trim().mid()
            0.333333333333333 + 0.333333015441895*I

        .. SEEALSO:: :meth:`round`"""
    @overload
    def trim(self) -> Any:
        """ComplexBall.trim(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 2226)

        Return a trimmed copy of this ball.

        Return a copy of this ball with both the real and imaginary parts
        trimmed (see :meth:`~sage.rings.real_arb.RealBall.trim()`).

        EXAMPLES::

            sage: b = CBF(1/3, RBF(1/3, rad=.01))
            sage: b.mid()
            0.333333333333333 + 0.333333333333333*I
            sage: b.trim().mid()
            0.333333333333333 + 0.333333015441895*I

        .. SEEALSO:: :meth:`round`"""
    def union(self, other) -> Any:
        """ComplexBall.union(self, other)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 2136)

        Return a ball containing the convex hull of ``self`` and ``other``.

        EXAMPLES::

            sage: b = CBF(1 + i).union(0)
            sage: b.real().endpoints()
            (-9.31322574615479e-10, 1.00000000093133)"""
    @overload
    def zeta(self, a=...) -> Any:
        """ComplexBall.zeta(self, a=None)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3690)

        Return the image of this ball by the Hurwitz zeta function.

        For ``a = None``, this computes the Riemann zeta function.

        EXAMPLES::

            sage: CBF(1, 1).zeta()
            [0.5821580597520036 +/- ...e-17] + [-0.9268485643308071 +/- ...e-17]*I
            sage: CBF(1, 1).zeta(1)
            [0.5821580597520036 +/- ...e-17] + [-0.9268485643308071 +/- ...e-17]*I
            sage: CBF(1, 1).zeta(1/2)
            [1.497919876084167 +/- ...e-16] + [0.2448655353684164 +/- ...e-17]*I
            sage: CBF(1, 1).zeta(CBF(1, 1))
            [-0.3593983122202835 +/- ...e-17] + [-2.875283329756940 +/- ...e-16]*I
            sage: CBF(1, 1).zeta(-1)
            nan + nan*I"""
    @overload
    def zeta(self) -> Any:
        """ComplexBall.zeta(self, a=None)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3690)

        Return the image of this ball by the Hurwitz zeta function.

        For ``a = None``, this computes the Riemann zeta function.

        EXAMPLES::

            sage: CBF(1, 1).zeta()
            [0.5821580597520036 +/- ...e-17] + [-0.9268485643308071 +/- ...e-17]*I
            sage: CBF(1, 1).zeta(1)
            [0.5821580597520036 +/- ...e-17] + [-0.9268485643308071 +/- ...e-17]*I
            sage: CBF(1, 1).zeta(1/2)
            [1.497919876084167 +/- ...e-16] + [0.2448655353684164 +/- ...e-17]*I
            sage: CBF(1, 1).zeta(CBF(1, 1))
            [-0.3593983122202835 +/- ...e-17] + [-2.875283329756940 +/- ...e-16]*I
            sage: CBF(1, 1).zeta(-1)
            nan + nan*I"""
    def zetaderiv(self, k) -> Any:
        """ComplexBall.zetaderiv(self, k)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3722)

        Return the image of this ball by the `k`-th derivative of the Riemann
        zeta function.

        For a more flexible interface, see the low-level method
        ``_zeta_series`` of polynomials with complex ball coefficients.

        EXAMPLES::

            sage: CBF(1/2, 3).zetaderiv(1)
            [0.191759884092721...] + [-0.073135728865928...]*I
            sage: CBF(2).zetaderiv(3)
            [-6.0001458028430...]"""
    def __abs__(self) -> Any:
        """ComplexBall.__abs__(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 1913)

        Return the absolute value of this complex ball.

        EXAMPLES::

            sage: CBF(1 + i).abs() # indirect doctest
            [1.414213562373095 +/- ...e-16]
            sage: abs(CBF(i))
            1.000000000000000

            sage: CBF(1 + i).abs().parent()
            Real ball field with 53 bits of precision"""
    def __bool__(self) -> bool:
        """True if self else False"""
    def __complex__(self) -> Any:
        """ComplexBall.__complex__(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 1770)

        Convert ``self`` to a ``complex``.

        EXAMPLES::

            sage: complex(CBF(1))
            (1+0j)
            sage: complex(CBF(1,1))
            (1+1j)

        Check nan and inf::

            sage: complex(CBF(0, 'nan'))
            nanj
            sage: complex(CBF('+inf', '-inf'))
            (inf-infj)"""
    def __contains__(self, other) -> Any:
        """ComplexBall.__contains__(self, other)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 2593)

        Return ``True`` if ``other`` can be verified to be contained in ``self``.

        Depending on the type of ``other``, the test may use interval
        arithmetic with a precision determined by the parent of ``self`` and
        may return false negatives.

        EXAMPLES::

            sage: 1/3*i in CBF(0, 1/3)
            True

        A false negative::

            sage: RLF(1/3) in CBF(RealBallField(100)(1/3), 0)
            False

        .. SEEALSO:: :meth:`contains_exact`"""
    def __float__(self) -> Any:
        """ComplexBall.__float__(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 1751)

        Convert ``self`` to a ``float``.

        EXAMPLES::

            sage: float(CBF(1))
            1.0
            sage: float(CBF(1/3))
            0.3333333333333333
            sage: float(CBF(1,1))
            Traceback (most recent call last):
            ...
            TypeError: can...t convert complex ball to float"""
    def __hash__(self) -> Any:
        """ComplexBall.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 1532)

        TESTS::

            sage: hash(CBF(1/3)) == hash(RBF(1/3))
            True
            sage: hash(CBF(1/3 + 2*i)) != hash(CBF(1/3 + i))
            True"""
    def __invert__(self) -> Any:
        """ComplexBall.__invert__(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 2713)

        Return the inverse of this ball.

        The result is guaranteed to contain the inverse of any point of the
        input ball.

        EXAMPLES::

            sage: ~CBF(i/3)
            [-3.00000000000000 +/- ...e-16]*I
            sage: ~CBF(0)
            nan
            sage: ~CBF(RIF(10,11))
            [0.1 +/- ...e-3]"""
    def __lshift__(self, val, shift) -> Any:
        """ComplexBall.__lshift__(val, shift)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 2754)

        If ``val`` is a ``ComplexBall`` and ``shift`` is an integer, return the
        ball obtained by shifting the center and radius of ``val`` to the left
        by ``shift`` bits.

        INPUT:

        - ``shift`` -- integer; may be negative

        EXAMPLES::

            sage: CBF(i/3) << 2
            [1.333333333333333 +/- ...e-16]*I
            sage: CBF(i) << -2
            0.2500000000000000*I

        TESTS::

            sage: CBF(i) << (2^65)
            [3.636549880934858e+11106046577046714264 +/- ...e+11106046577046714248]*I
            sage: 'a' << CBF(1/3)
            Traceback (most recent call last):
            ...
            TypeError: unsupported operand type(s) for <<: 'str' and
            'ComplexBall'
            sage: CBF(1) << 1/2
            Traceback (most recent call last):
            ...
            TypeError: shift should be an integer"""
    def __neg__(self) -> Any:
        """ComplexBall.__neg__(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 2650)

        Return the opposite of this ball.

        EXAMPLES::

            sage: -CBF(1/3 + I)
            [-0.3333333333333333 +/- ...e-17] - 1.000000000000000*I"""
    def __pow__(self, base, expo, _) -> Any:
        """ComplexBall.__pow__(base, expo, _)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 2860)

        EXAMPLES::

            sage: CBF(-1)**(1/2)
            1.000000000000000*I
            sage: CBF(e)**CBF(i*pi)                                                     # needs sage.symbolic
            [-1.00000000000000 +/- ...e-16] + [+/- ...e-15]*I
            sage: CBF(0, 1)**AA(2)**(1/2)
            [-0.60569986707881 +/- ...e-15] + [0.79569320156748 +/- ...e-15]*I

            sage: CBF(i)**RBF(2**1000)
            [+/- 1.01] + [+/- 1.01]*I
            sage: CBF(i)**(2**1000)
            1.000000000000000

            sage: CBF(0)^(1/3)
            0
            sage: CBF(0)^(-1)
            nan
            sage: CBF(0)^(-2)
            nan + nan*I

        TESTS::

            sage: (CBF(e)**CBF(i))**RBF(pi)                                             # needs sage.symbolic
            [-1.0000000000000 +/- ...e-15] + [+/- ...e-15]*I
            sage: CBF(2*i)**10r
            -1024.000000000000
            sage: CBF(1,1) ^ -1r
            0.5000000000000000 - 0.5000000000000000*I
            sage: CBF(2)**SR.var('x')                                                   # needs sage.symbolic
            2.000000000000000^x"""
    def __reduce__(self) -> Any:
        """ComplexBall.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 1579)

        Serialize a ComplexBall.

        TESTS::

            sage: [loads(dumps(b)).identical(b) for b in                                # needs sage.symbolic
            ....:     [ComplexBallField(60)(1/3 + i*pi), CBF(NaN)]]
            [True, True]"""
    def __rlshift__(self, other):
        """Return value<<self."""
    def __rpow__(self, other):
        """Return pow(value, self, mod)."""
    def __rrshift__(self, other):
        """Return value>>self."""
    def __rshift__(self, val, shift) -> Any:
        """ComplexBall.__rshift__(val, shift)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 2805)

        If ``val`` is a ``ComplexBall`` and ``shift`` is an integer, return the
        ball obtained by shifting the center and radius of ``val`` to the right
        by ``shift`` bits.

        INPUT:

        - ``shift`` -- integer; may be negative

        EXAMPLES::

            sage: CBF(1+I) >> 2
            0.2500000000000000 + 0.2500000000000000*I

        TESTS::

            sage: 'a' >> CBF(1/3)
            Traceback (most recent call last):
            ...
            TypeError: unsupported operand type(s) for >>: 'str' and
            'ComplexBall'"""

class ComplexBallField(sage.structure.unique_representation.UniqueRepresentation, sage.rings.abc.ComplexBallField):
    """File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 311)

        An approximation of the field of complex numbers using pairs of mid-rad
        intervals.

        INPUT:

        - ``precision`` -- integer `\\ge 2`

        EXAMPLES::

            sage: CBF(1)
            1.000000000000000

        TESTS::

            sage: ComplexBallField(0)
            Traceback (most recent call last):
            ...
            ValueError: precision must be at least 2
            sage: ComplexBallField(1)
            Traceback (most recent call last):
            ...
            ValueError: precision must be at least 2

            sage: ComplexBallField().is_finite()
            False

            sage: loads(dumps(ComplexBallField(60))) is ComplexBallField(60)
            True

        .. SEEALSO::

            - :mod:`sage.rings.complex_arb`
            - :mod:`sage.rings.complex_mpfr`
            - :mod:`sage.rings.complex_mpfi`
            - :mod:`sage.rings.real_arb`
    """

    class Element(sage.structure.element.RingElement):
        """ComplexBall(parent, x=None, y=None)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 1370)

        Hold one ``acb_t`` of the `FLINT library <https://flintlib.org>`_.

        EXAMPLES::

            sage: a = ComplexBallField()(1, 1)
            sage: a
            1.000000000000000 + 1.000000000000000*I"""
        __pyx_vtable__: ClassVar[PyCapsule] = ...
        def __init__(self, *args, **kwargs) -> None:
            """File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 1402)

                    Initialize the :class:`ComplexBall`.

                    INPUT:

                    - ``parent`` -- a :class:`ComplexBallField`

                    - ``x``, ``y`` -- (optional) either a complex number, interval or ball,
                      or two real ones

                    .. SEEALSO:: :meth:`ComplexBallField._element_constructor_`

                    TESTS::

                        sage: from sage.rings.complex_arb import ComplexBall
                        sage: CBF53, CBF100 = ComplexBallField(53), ComplexBallField(100)
                        sage: ComplexBall(CBF100)
                        0
                        sage: ComplexBall(CBF100, ComplexBall(CBF53, ComplexBall(CBF100, 1/3)))
                        [0.333333333333333333333333333333 +/- ...e-31]
                        sage: ComplexBall(CBF100, RBF(pi))                                          # needs sage.symbolic
                        [3.141592653589793 +/- ...e-16]

                        sage: ComplexBall(CBF100, -3r)
                        Traceback (most recent call last):
                        ...
                        TypeError: unsupported initializer
                        sage: CBF100(-3r)
                        -3.000000000000000000000000000000

                        sage: ComplexBall(CBF100, CIF(1, 2))
                        1.000000000000000000000000000000 + 2.000000000000000000000000000000*I
                        sage: ComplexBall(CBF100, RBF(1/3), RBF(1))
                        [0.3333333333333333 +/- ...e-17] + 1.000000000000000000000000000000*I
                        sage: ComplexBall(CBF100, 10^100)
                        [1.000000000000000000000000000000e+100 +/- ...]

                        sage: NF.<a> = QuadraticField(-1, embedding=CC(0, -1))
                        sage: CBF(a)
                        -1.000000000000000*I

                        sage: NF.<a> = QuadraticField(-1, embedding=None)
                        sage: CBF(a)
                        1.000000000000000*I
                        sage: CBF.coerce(a)
                        Traceback (most recent call last):
                        ...
                        TypeError: no canonical coercion ...

                        sage: NF.<a> = QuadraticField(-2)
                        sage: CBF(1/3 + a).real()
                        [0.3333333333333333 +/- ...e-17]

                        sage: ComplexBall(CBF, 1, 1/2)
                        1.000000000000000 + 0.5000000000000000*I
                        sage: ComplexBall(CBF, 1, 1)
                        1.000000000000000 + 1.000000000000000*I
                        sage: ComplexBall(CBF, 1, 1/2)
                        1.000000000000000 + 0.5000000000000000*I
                        sage: ComplexBall(CBF, 1/2, 1)
                        0.5000000000000000 + 1.000000000000000*I
                        sage: ComplexBall(CBF, 1/2, 1/2)
                        0.5000000000000000 + 0.5000000000000000*I
                        sage: ComplexBall(CBF, 1/2, 'a')
                        Traceback (most recent call last):
                        ...
                        TypeError: unsupported initializer
                        sage: ComplexBall(CBF, 'a')
                        Traceback (most recent call last):
                        ...
                        TypeError: unsupported initializer
        """
        @overload
        def Chi(self) -> Any:
            """ComplexBall.Chi(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4353)

            Return the hyperbolic cosine integral with argument ``self``.

            EXAMPLES::

                sage: CBF(1, 1).Chi()  # abs tol 1e-15
                [0.882172180555936 +/- 5.89e-16] + [1.28354719327494 +/- 1.01e-15]*I
                sage: CBF(0).Chi()
                nan + nan*I

            TESTS:

                sage: CBF(Chi(I))  # abs tol 5e-16                                          # needs sage.symbolic
                [0.337403922900968 +/- 3.25e-16] + [1.570796326794897 +/- 5.54e-16]*I"""
        @overload
        def Chi(self) -> Any:
            """ComplexBall.Chi(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4353)

            Return the hyperbolic cosine integral with argument ``self``.

            EXAMPLES::

                sage: CBF(1, 1).Chi()  # abs tol 1e-15
                [0.882172180555936 +/- 5.89e-16] + [1.28354719327494 +/- 1.01e-15]*I
                sage: CBF(0).Chi()
                nan + nan*I

            TESTS:

                sage: CBF(Chi(I))  # abs tol 5e-16                                          # needs sage.symbolic
                [0.337403922900968 +/- 3.25e-16] + [1.570796326794897 +/- 5.54e-16]*I"""
        @overload
        def Chi(self) -> Any:
            """ComplexBall.Chi(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4353)

            Return the hyperbolic cosine integral with argument ``self``.

            EXAMPLES::

                sage: CBF(1, 1).Chi()  # abs tol 1e-15
                [0.882172180555936 +/- 5.89e-16] + [1.28354719327494 +/- 1.01e-15]*I
                sage: CBF(0).Chi()
                nan + nan*I

            TESTS:

                sage: CBF(Chi(I))  # abs tol 5e-16                                          # needs sage.symbolic
                [0.337403922900968 +/- 3.25e-16] + [1.570796326794897 +/- 5.54e-16]*I"""
        @overload
        def Chi(self, I) -> Any:
            """ComplexBall.Chi(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4353)

            Return the hyperbolic cosine integral with argument ``self``.

            EXAMPLES::

                sage: CBF(1, 1).Chi()  # abs tol 1e-15
                [0.882172180555936 +/- 5.89e-16] + [1.28354719327494 +/- 1.01e-15]*I
                sage: CBF(0).Chi()
                nan + nan*I

            TESTS:

                sage: CBF(Chi(I))  # abs tol 5e-16                                          # needs sage.symbolic
                [0.337403922900968 +/- 3.25e-16] + [1.570796326794897 +/- 5.54e-16]*I"""
        @overload
        def Ci(self) -> Any:
            """ComplexBall.Ci(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4305)

            Return the cosine integral with argument ``self``.

            EXAMPLES::

                sage: CBF(1, 1).Ci()  # abs tol 5e-16
                [0.882172180555936 +/- 5.89e-16] + [0.287249133519956 +/- 3.37e-16]*I
                sage: CBF(0).Ci()
                nan + nan*I

            TESTS:

                sage: CBF(Ci(I))  # abs tol 5e-16                                           # needs sage.symbolic
                [0.837866940980208 +/- 4.72e-16] + [1.570796326794897 +/- 5.54e-16]*I"""
        @overload
        def Ci(self) -> Any:
            """ComplexBall.Ci(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4305)

            Return the cosine integral with argument ``self``.

            EXAMPLES::

                sage: CBF(1, 1).Ci()  # abs tol 5e-16
                [0.882172180555936 +/- 5.89e-16] + [0.287249133519956 +/- 3.37e-16]*I
                sage: CBF(0).Ci()
                nan + nan*I

            TESTS:

                sage: CBF(Ci(I))  # abs tol 5e-16                                           # needs sage.symbolic
                [0.837866940980208 +/- 4.72e-16] + [1.570796326794897 +/- 5.54e-16]*I"""
        @overload
        def Ci(self) -> Any:
            """ComplexBall.Ci(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4305)

            Return the cosine integral with argument ``self``.

            EXAMPLES::

                sage: CBF(1, 1).Ci()  # abs tol 5e-16
                [0.882172180555936 +/- 5.89e-16] + [0.287249133519956 +/- 3.37e-16]*I
                sage: CBF(0).Ci()
                nan + nan*I

            TESTS:

                sage: CBF(Ci(I))  # abs tol 5e-16                                           # needs sage.symbolic
                [0.837866940980208 +/- 4.72e-16] + [1.570796326794897 +/- 5.54e-16]*I"""
        @overload
        def Ci(self, I) -> Any:
            """ComplexBall.Ci(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4305)

            Return the cosine integral with argument ``self``.

            EXAMPLES::

                sage: CBF(1, 1).Ci()  # abs tol 5e-16
                [0.882172180555936 +/- 5.89e-16] + [0.287249133519956 +/- 3.37e-16]*I
                sage: CBF(0).Ci()
                nan + nan*I

            TESTS:

                sage: CBF(Ci(I))  # abs tol 5e-16                                           # needs sage.symbolic
                [0.837866940980208 +/- 4.72e-16] + [1.570796326794897 +/- 5.54e-16]*I"""
        @overload
        def Ei(self) -> Any:
            """ComplexBall.Ei(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4259)

            Return the exponential integral with argument ``self``.

            EXAMPLES::

                sage: CBF(1, 1).Ei()  # abs tol 6e-15
                [1.76462598556385 +/- 6.03e-15] + [2.38776985151052 +/- 4.23e-15]*I
                sage: CBF(0).Ei()
                nan...

            TESTS:

                sage: CBF(Ei(I))  # abs tol 2e-15                                           # needs sage.symbolic
                [0.337403922900968 +/- 3.76e-16] + [2.51687939716208 +/- 2.01e-15]*I"""
        @overload
        def Ei(self) -> Any:
            """ComplexBall.Ei(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4259)

            Return the exponential integral with argument ``self``.

            EXAMPLES::

                sage: CBF(1, 1).Ei()  # abs tol 6e-15
                [1.76462598556385 +/- 6.03e-15] + [2.38776985151052 +/- 4.23e-15]*I
                sage: CBF(0).Ei()
                nan...

            TESTS:

                sage: CBF(Ei(I))  # abs tol 2e-15                                           # needs sage.symbolic
                [0.337403922900968 +/- 3.76e-16] + [2.51687939716208 +/- 2.01e-15]*I"""
        @overload
        def Ei(self) -> Any:
            """ComplexBall.Ei(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4259)

            Return the exponential integral with argument ``self``.

            EXAMPLES::

                sage: CBF(1, 1).Ei()  # abs tol 6e-15
                [1.76462598556385 +/- 6.03e-15] + [2.38776985151052 +/- 4.23e-15]*I
                sage: CBF(0).Ei()
                nan...

            TESTS:

                sage: CBF(Ei(I))  # abs tol 2e-15                                           # needs sage.symbolic
                [0.337403922900968 +/- 3.76e-16] + [2.51687939716208 +/- 2.01e-15]*I"""
        @overload
        def Ei(self, I) -> Any:
            """ComplexBall.Ei(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4259)

            Return the exponential integral with argument ``self``.

            EXAMPLES::

                sage: CBF(1, 1).Ei()  # abs tol 6e-15
                [1.76462598556385 +/- 6.03e-15] + [2.38776985151052 +/- 4.23e-15]*I
                sage: CBF(0).Ei()
                nan...

            TESTS:

                sage: CBF(Ei(I))  # abs tol 2e-15                                           # needs sage.symbolic
                [0.337403922900968 +/- 3.76e-16] + [2.51687939716208 +/- 2.01e-15]*I"""
        @overload
        def Li(self) -> Any:
            """ComplexBall.Li(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4411)

            Offset logarithmic integral.

            EXAMPLES::

                sage: CBF(0).Li()
                [-1.045163780117493 +/- ...e-16]
                sage: li(0).n()                                                             # needs sage.symbolic
                0.000000000000000
                sage: Li(0).n()                                                             # needs sage.symbolic
                -1.04516378011749"""
        @overload
        def Li(self) -> Any:
            """ComplexBall.Li(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4411)

            Offset logarithmic integral.

            EXAMPLES::

                sage: CBF(0).Li()
                [-1.045163780117493 +/- ...e-16]
                sage: li(0).n()                                                             # needs sage.symbolic
                0.000000000000000
                sage: Li(0).n()                                                             # needs sage.symbolic
                -1.04516378011749"""
        @overload
        def Shi(self) -> Any:
            """ComplexBall.Shi(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4329)

            Return the hyperbolic sine integral with argument ``self``.

            EXAMPLES::

                sage: CBF(1, 1).Shi()  # abs tol 3e-15
                [0.88245380500792 +/- 3.36e-15] + [1.10422265823558 +/- 2.48e-15]*I
                sage: CBF(0).Shi()
                0

            TESTS:

                sage: CBF(Shi(I))  # abs tol 1e-15                                          # needs sage.symbolic
                [0.946083070367183 +/- 9.22e-16]*I"""
        @overload
        def Shi(self) -> Any:
            """ComplexBall.Shi(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4329)

            Return the hyperbolic sine integral with argument ``self``.

            EXAMPLES::

                sage: CBF(1, 1).Shi()  # abs tol 3e-15
                [0.88245380500792 +/- 3.36e-15] + [1.10422265823558 +/- 2.48e-15]*I
                sage: CBF(0).Shi()
                0

            TESTS:

                sage: CBF(Shi(I))  # abs tol 1e-15                                          # needs sage.symbolic
                [0.946083070367183 +/- 9.22e-16]*I"""
        @overload
        def Shi(self) -> Any:
            """ComplexBall.Shi(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4329)

            Return the hyperbolic sine integral with argument ``self``.

            EXAMPLES::

                sage: CBF(1, 1).Shi()  # abs tol 3e-15
                [0.88245380500792 +/- 3.36e-15] + [1.10422265823558 +/- 2.48e-15]*I
                sage: CBF(0).Shi()
                0

            TESTS:

                sage: CBF(Shi(I))  # abs tol 1e-15                                          # needs sage.symbolic
                [0.946083070367183 +/- 9.22e-16]*I"""
        @overload
        def Shi(self, I) -> Any:
            """ComplexBall.Shi(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4329)

            Return the hyperbolic sine integral with argument ``self``.

            EXAMPLES::

                sage: CBF(1, 1).Shi()  # abs tol 3e-15
                [0.88245380500792 +/- 3.36e-15] + [1.10422265823558 +/- 2.48e-15]*I
                sage: CBF(0).Shi()
                0

            TESTS:

                sage: CBF(Shi(I))  # abs tol 1e-15                                          # needs sage.symbolic
                [0.946083070367183 +/- 9.22e-16]*I"""
        @overload
        def Si(self) -> Any:
            """ComplexBall.Si(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4281)

            Return the sine integral with argument ``self``.

            EXAMPLES::

                sage: CBF(1, 1).Si()  # abs tol 3e-15
                [1.10422265823558 +/- 2.48e-15] + [0.88245380500792 +/- 3.36e-15]*I
                sage: CBF(0).Si()
                0

            TESTS:

                sage: CBF(Si(I))  # abs tol 3e-15                                           # needs sage.symbolic
                [1.05725087537573 +/- 2.77e-15]*I"""
        @overload
        def Si(self) -> Any:
            """ComplexBall.Si(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4281)

            Return the sine integral with argument ``self``.

            EXAMPLES::

                sage: CBF(1, 1).Si()  # abs tol 3e-15
                [1.10422265823558 +/- 2.48e-15] + [0.88245380500792 +/- 3.36e-15]*I
                sage: CBF(0).Si()
                0

            TESTS:

                sage: CBF(Si(I))  # abs tol 3e-15                                           # needs sage.symbolic
                [1.05725087537573 +/- 2.77e-15]*I"""
        @overload
        def Si(self) -> Any:
            """ComplexBall.Si(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4281)

            Return the sine integral with argument ``self``.

            EXAMPLES::

                sage: CBF(1, 1).Si()  # abs tol 3e-15
                [1.10422265823558 +/- 2.48e-15] + [0.88245380500792 +/- 3.36e-15]*I
                sage: CBF(0).Si()
                0

            TESTS:

                sage: CBF(Si(I))  # abs tol 3e-15                                           # needs sage.symbolic
                [1.05725087537573 +/- 2.77e-15]*I"""
        @overload
        def Si(self, I) -> Any:
            """ComplexBall.Si(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4281)

            Return the sine integral with argument ``self``.

            EXAMPLES::

                sage: CBF(1, 1).Si()  # abs tol 3e-15
                [1.10422265823558 +/- 2.48e-15] + [0.88245380500792 +/- 3.36e-15]*I
                sage: CBF(0).Si()
                0

            TESTS:

                sage: CBF(Si(I))  # abs tol 3e-15                                           # needs sage.symbolic
                [1.05725087537573 +/- 2.77e-15]*I"""
        @overload
        def above_abs(self) -> Any:
            """ComplexBall.above_abs(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 1968)

            Return an upper bound for the absolute value of this complex ball.

            OUTPUT: a ball with zero radius

            EXAMPLES::

                sage: b = ComplexBallField(8)(1+i).above_abs()
                sage: b
                [1.4 +/- 0.0219]
                sage: b.is_exact()
                True
                sage: QQ(b)*128
                182

            .. SEEALSO:: :meth:`below_abs`"""
        @overload
        def above_abs(self) -> Any:
            """ComplexBall.above_abs(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 1968)

            Return an upper bound for the absolute value of this complex ball.

            OUTPUT: a ball with zero radius

            EXAMPLES::

                sage: b = ComplexBallField(8)(1+i).above_abs()
                sage: b
                [1.4 +/- 0.0219]
                sage: b.is_exact()
                True
                sage: QQ(b)*128
                182

            .. SEEALSO:: :meth:`below_abs`"""
        @overload
        def accuracy(self) -> Any:
            """ComplexBall.accuracy(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 2201)

            Return the effective relative accuracy of this ball measured in bits.

            This is computed as if calling
            :meth:`~sage.rings.real_arb.RealBall.accuracy()`
            on the real ball whose midpoint is the larger out of the real and
            imaginary midpoints of this complex ball, and whose radius is the
            larger out of the real and imaginary radii of this complex ball.

            EXAMPLES::

                sage: CBF(exp(I*pi/3)).accuracy()                                           # needs sage.symbolic
                51
                sage: CBF(I/2).accuracy() == CBF.base().maximal_accuracy()
                True
                sage: CBF('nan', 'inf').accuracy() == -CBF.base().maximal_accuracy()
                True

            .. SEEALSO::

                :meth:`~sage.rings.real_arb.RealBallField.maximal_accuracy`"""
        @overload
        def accuracy(self) -> Any:
            """ComplexBall.accuracy(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 2201)

            Return the effective relative accuracy of this ball measured in bits.

            This is computed as if calling
            :meth:`~sage.rings.real_arb.RealBall.accuracy()`
            on the real ball whose midpoint is the larger out of the real and
            imaginary midpoints of this complex ball, and whose radius is the
            larger out of the real and imaginary radii of this complex ball.

            EXAMPLES::

                sage: CBF(exp(I*pi/3)).accuracy()                                           # needs sage.symbolic
                51
                sage: CBF(I/2).accuracy() == CBF.base().maximal_accuracy()
                True
                sage: CBF('nan', 'inf').accuracy() == -CBF.base().maximal_accuracy()
                True

            .. SEEALSO::

                :meth:`~sage.rings.real_arb.RealBallField.maximal_accuracy`"""
        @overload
        def accuracy(self) -> Any:
            """ComplexBall.accuracy(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 2201)

            Return the effective relative accuracy of this ball measured in bits.

            This is computed as if calling
            :meth:`~sage.rings.real_arb.RealBall.accuracy()`
            on the real ball whose midpoint is the larger out of the real and
            imaginary midpoints of this complex ball, and whose radius is the
            larger out of the real and imaginary radii of this complex ball.

            EXAMPLES::

                sage: CBF(exp(I*pi/3)).accuracy()                                           # needs sage.symbolic
                51
                sage: CBF(I/2).accuracy() == CBF.base().maximal_accuracy()
                True
                sage: CBF('nan', 'inf').accuracy() == -CBF.base().maximal_accuracy()
                True

            .. SEEALSO::

                :meth:`~sage.rings.real_arb.RealBallField.maximal_accuracy`"""
        @overload
        def accuracy(self) -> Any:
            """ComplexBall.accuracy(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 2201)

            Return the effective relative accuracy of this ball measured in bits.

            This is computed as if calling
            :meth:`~sage.rings.real_arb.RealBall.accuracy()`
            on the real ball whose midpoint is the larger out of the real and
            imaginary midpoints of this complex ball, and whose radius is the
            larger out of the real and imaginary radii of this complex ball.

            EXAMPLES::

                sage: CBF(exp(I*pi/3)).accuracy()                                           # needs sage.symbolic
                51
                sage: CBF(I/2).accuracy() == CBF.base().maximal_accuracy()
                True
                sage: CBF('nan', 'inf').accuracy() == -CBF.base().maximal_accuracy()
                True

            .. SEEALSO::

                :meth:`~sage.rings.real_arb.RealBallField.maximal_accuracy`"""
        @overload
        def accuracy(self) -> Any:
            """ComplexBall.accuracy(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 2201)

            Return the effective relative accuracy of this ball measured in bits.

            This is computed as if calling
            :meth:`~sage.rings.real_arb.RealBall.accuracy()`
            on the real ball whose midpoint is the larger out of the real and
            imaginary midpoints of this complex ball, and whose radius is the
            larger out of the real and imaginary radii of this complex ball.

            EXAMPLES::

                sage: CBF(exp(I*pi/3)).accuracy()                                           # needs sage.symbolic
                51
                sage: CBF(I/2).accuracy() == CBF.base().maximal_accuracy()
                True
                sage: CBF('nan', 'inf').accuracy() == -CBF.base().maximal_accuracy()
                True

            .. SEEALSO::

                :meth:`~sage.rings.real_arb.RealBallField.maximal_accuracy`"""
        def add_error(self, ampl) -> Any:
            """ComplexBall.add_error(self, ampl)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 2249)

            Increase the radii of the real and imaginary parts by (an upper bound
            on) ``ampl``.

            If ``ampl`` is negative, the radii remain unchanged.

            INPUT:

            - ``ampl`` -- a **real** ball (or an object that can be coerced to a
              real ball)

            OUTPUT: a new complex ball

            EXAMPLES::

                sage: CBF(1+i).add_error(10^-16)
                [1.000000000000000 +/- ...e-16] + [1.000000000000000 +/- ...e-16]*I"""
        @overload
        def agm1(self) -> Any:
            '''ComplexBall.agm1(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3836)

            Return the arithmetic-geometric mean of 1 and ``self``.

            The arithmetic-geometric mean is defined such that the function is
            continuous in the complex plane except for a branch cut along the
            negative half axis (where it is continuous from above). This
            corresponds to always choosing an "optimal" branch for the square root
            in the arithmetic-geometric mean iteration.

            EXAMPLES::

                sage: CBF(0, -1).agm1()
                [0.599070117367796 +/- 3.9...e-16] + [-0.599070117367796 +/- 5.5...e-16]*I'''
        @overload
        def agm1(self) -> Any:
            '''ComplexBall.agm1(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3836)

            Return the arithmetic-geometric mean of 1 and ``self``.

            The arithmetic-geometric mean is defined such that the function is
            continuous in the complex plane except for a branch cut along the
            negative half axis (where it is continuous from above). This
            corresponds to always choosing an "optimal" branch for the square root
            in the arithmetic-geometric mean iteration.

            EXAMPLES::

                sage: CBF(0, -1).agm1()
                [0.599070117367796 +/- 3.9...e-16] + [-0.599070117367796 +/- 5.5...e-16]*I'''
        @overload
        def airy(self) -> Any:
            """ComplexBall.airy(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4055)

            Return the Airy functions Ai, Ai', Bi, Bi' with argument ``self``,
            evaluated simultaneously.

            EXAMPLES::

                sage: CBF(10*pi).airy()                                                     # needs sage.symbolic
                ([1.2408955946101e-52 +/- ...e-66],
                 [-6.965048886977e-52 +/- ...e-65],
                 [2.2882956833435e+50 +/- ...e+36],
                 [1.2807602335816e+51 +/- ...e+37])
                sage: ai, aip, bi, bip = CBF(1,2).airy()
                sage: (ai * bip - bi * aip) * CBF(pi)                                       # needs sage.symbolic
                [1.0000000000000 +/- ...e-15] + [+/- ...e-16]*I"""
        @overload
        def airy(self) -> Any:
            """ComplexBall.airy(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4055)

            Return the Airy functions Ai, Ai', Bi, Bi' with argument ``self``,
            evaluated simultaneously.

            EXAMPLES::

                sage: CBF(10*pi).airy()                                                     # needs sage.symbolic
                ([1.2408955946101e-52 +/- ...e-66],
                 [-6.965048886977e-52 +/- ...e-65],
                 [2.2882956833435e+50 +/- ...e+36],
                 [1.2807602335816e+51 +/- ...e+37])
                sage: ai, aip, bi, bip = CBF(1,2).airy()
                sage: (ai * bip - bi * aip) * CBF(pi)                                       # needs sage.symbolic
                [1.0000000000000 +/- ...e-15] + [+/- ...e-16]*I"""
        @overload
        def airy(self) -> Any:
            """ComplexBall.airy(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4055)

            Return the Airy functions Ai, Ai', Bi, Bi' with argument ``self``,
            evaluated simultaneously.

            EXAMPLES::

                sage: CBF(10*pi).airy()                                                     # needs sage.symbolic
                ([1.2408955946101e-52 +/- ...e-66],
                 [-6.965048886977e-52 +/- ...e-65],
                 [2.2882956833435e+50 +/- ...e+36],
                 [1.2807602335816e+51 +/- ...e+37])
                sage: ai, aip, bi, bip = CBF(1,2).airy()
                sage: (ai * bip - bi * aip) * CBF(pi)                                       # needs sage.symbolic
                [1.0000000000000 +/- ...e-15] + [+/- ...e-16]*I"""
        @overload
        def airy_ai(self) -> Any:
            """ComplexBall.airy_ai(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4080)

            Return the Airy function Ai with argument ``self``.

            EXAMPLES::

                sage: CBF(1,2).airy_ai()
                [-0.2193862549814276 +/- ...e-17] + [-0.1753859114081094 +/- ...e-17]*I"""
        @overload
        def airy_ai(self) -> Any:
            """ComplexBall.airy_ai(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4080)

            Return the Airy function Ai with argument ``self``.

            EXAMPLES::

                sage: CBF(1,2).airy_ai()
                [-0.2193862549814276 +/- ...e-17] + [-0.1753859114081094 +/- ...e-17]*I"""
        def airy_ai_prime(self) -> Any:
            """ComplexBall.airy_ai_prime(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4095)

            Return the Airy function derivative Ai' with argument ``self``.

            EXAMPLES::

                sage: CBF(1,2).airy_ai_prime()
                [0.1704449781789148 +/- ...e-17] + [0.387622439413295 +/- ...e-16]*I"""
        @overload
        def airy_bi(self) -> Any:
            """ComplexBall.airy_bi(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4110)

            Return the Airy function Bi with argument ``self``.

            EXAMPLES::

                sage: CBF(1,2).airy_bi()
                [0.0488220324530612 +/- ...e-17] + [0.1332740579917484 +/- ...e-17]*I"""
        @overload
        def airy_bi(self) -> Any:
            """ComplexBall.airy_bi(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4110)

            Return the Airy function Bi with argument ``self``.

            EXAMPLES::

                sage: CBF(1,2).airy_bi()
                [0.0488220324530612 +/- ...e-17] + [0.1332740579917484 +/- ...e-17]*I"""
        def airy_bi_prime(self) -> Any:
            """ComplexBall.airy_bi_prime(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4125)

            Return the Airy function derivative Bi' with argument ``self``.

            EXAMPLES::

                sage: CBF(1,2).airy_bi_prime()
                [-0.857239258605362 +/- ...e-16] + [0.4955063363095674 +/- ...e-17]*I"""
        @overload
        def arccos(self, analytic=...) -> Any:
            """ComplexBall.arccos(self, analytic=False)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3424)

            Return the arccosine of this ball.

            INPUT:

            - ``analytic`` -- boolean (default: ``False``); if ``True``, return an
              indeterminate (not-a-number) value when the input ball touches
              the branch cut

            EXAMPLES::

                sage: CBF(1+i).arccos()
                [0.90455689430238 +/- ...e-15] + [-1.06127506190504 +/- ...e-15]*I
                sage: CBF(-1).arccos()
                [3.141592653589793 +/- ...e-16]
                sage: CBF(-1).arccos(analytic=True)
                nan + nan*I"""
        @overload
        def arccos(self) -> Any:
            """ComplexBall.arccos(self, analytic=False)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3424)

            Return the arccosine of this ball.

            INPUT:

            - ``analytic`` -- boolean (default: ``False``); if ``True``, return an
              indeterminate (not-a-number) value when the input ball touches
              the branch cut

            EXAMPLES::

                sage: CBF(1+i).arccos()
                [0.90455689430238 +/- ...e-15] + [-1.06127506190504 +/- ...e-15]*I
                sage: CBF(-1).arccos()
                [3.141592653589793 +/- ...e-16]
                sage: CBF(-1).arccos(analytic=True)
                nan + nan*I"""
        @overload
        def arccos(self) -> Any:
            """ComplexBall.arccos(self, analytic=False)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3424)

            Return the arccosine of this ball.

            INPUT:

            - ``analytic`` -- boolean (default: ``False``); if ``True``, return an
              indeterminate (not-a-number) value when the input ball touches
              the branch cut

            EXAMPLES::

                sage: CBF(1+i).arccos()
                [0.90455689430238 +/- ...e-15] + [-1.06127506190504 +/- ...e-15]*I
                sage: CBF(-1).arccos()
                [3.141592653589793 +/- ...e-16]
                sage: CBF(-1).arccos(analytic=True)
                nan + nan*I"""
        @overload
        def arccos(self, analytic=...) -> Any:
            """ComplexBall.arccos(self, analytic=False)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3424)

            Return the arccosine of this ball.

            INPUT:

            - ``analytic`` -- boolean (default: ``False``); if ``True``, return an
              indeterminate (not-a-number) value when the input ball touches
              the branch cut

            EXAMPLES::

                sage: CBF(1+i).arccos()
                [0.90455689430238 +/- ...e-15] + [-1.06127506190504 +/- ...e-15]*I
                sage: CBF(-1).arccos()
                [3.141592653589793 +/- ...e-16]
                sage: CBF(-1).arccos(analytic=True)
                nan + nan*I"""
        @overload
        def arccosh(self, analytic=...) -> Any:
            """ComplexBall.arccosh(self, analytic=False)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3513)

            Return the hyperbolic arccosine of this ball.

            INPUT:

            - ``analytic`` -- boolean (default: ``False``); if ``True``, return an
              indeterminate (not-a-number) value when the input ball touches
              the branch cut

            EXAMPLES::

                sage: CBF(1+i).arccosh()
                [1.061275061905035 +/- ...e-16] + [0.904556894302381 +/- ...e-16]*I
                sage: CBF(-2).arccosh()
                [1.316957896924817 +/- ...e-16] + [3.141592653589793 +/- ...e-16]*I
                sage: CBF(-2).arccosh(analytic=True)
                nan + nan*I"""
        @overload
        def arccosh(self) -> Any:
            """ComplexBall.arccosh(self, analytic=False)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3513)

            Return the hyperbolic arccosine of this ball.

            INPUT:

            - ``analytic`` -- boolean (default: ``False``); if ``True``, return an
              indeterminate (not-a-number) value when the input ball touches
              the branch cut

            EXAMPLES::

                sage: CBF(1+i).arccosh()
                [1.061275061905035 +/- ...e-16] + [0.904556894302381 +/- ...e-16]*I
                sage: CBF(-2).arccosh()
                [1.316957896924817 +/- ...e-16] + [3.141592653589793 +/- ...e-16]*I
                sage: CBF(-2).arccosh(analytic=True)
                nan + nan*I"""
        @overload
        def arccosh(self) -> Any:
            """ComplexBall.arccosh(self, analytic=False)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3513)

            Return the hyperbolic arccosine of this ball.

            INPUT:

            - ``analytic`` -- boolean (default: ``False``); if ``True``, return an
              indeterminate (not-a-number) value when the input ball touches
              the branch cut

            EXAMPLES::

                sage: CBF(1+i).arccosh()
                [1.061275061905035 +/- ...e-16] + [0.904556894302381 +/- ...e-16]*I
                sage: CBF(-2).arccosh()
                [1.316957896924817 +/- ...e-16] + [3.141592653589793 +/- ...e-16]*I
                sage: CBF(-2).arccosh(analytic=True)
                nan + nan*I"""
        @overload
        def arccosh(self, analytic=...) -> Any:
            """ComplexBall.arccosh(self, analytic=False)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3513)

            Return the hyperbolic arccosine of this ball.

            INPUT:

            - ``analytic`` -- boolean (default: ``False``); if ``True``, return an
              indeterminate (not-a-number) value when the input ball touches
              the branch cut

            EXAMPLES::

                sage: CBF(1+i).arccosh()
                [1.061275061905035 +/- ...e-16] + [0.904556894302381 +/- ...e-16]*I
                sage: CBF(-2).arccosh()
                [1.316957896924817 +/- ...e-16] + [3.141592653589793 +/- ...e-16]*I
                sage: CBF(-2).arccosh(analytic=True)
                nan + nan*I"""
        @overload
        def arcsin(self, analytic=...) -> Any:
            """ComplexBall.arcsin(self, analytic=False)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3395)

            Return the arcsine of this ball.

            INPUT:

            - ``analytic`` -- boolean (default: ``False``); if ``True``, return an
              indeterminate (not-a-number) value when the input ball touches
              the branch cut

            EXAMPLES::

                sage: CBF(1+i).arcsin()
                [0.66623943249252 +/- ...e-15] + [1.06127506190504 +/- ...e-15]*I
                sage: CBF(1, RIF(0,1/1000)).arcsin()
                [1.6 +/- 0.0619] + [+/- 0.0322]*I
                sage: CBF(1, RIF(0,1/1000)).arcsin(analytic=True)
                nan + nan*I"""
        @overload
        def arcsin(self) -> Any:
            """ComplexBall.arcsin(self, analytic=False)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3395)

            Return the arcsine of this ball.

            INPUT:

            - ``analytic`` -- boolean (default: ``False``); if ``True``, return an
              indeterminate (not-a-number) value when the input ball touches
              the branch cut

            EXAMPLES::

                sage: CBF(1+i).arcsin()
                [0.66623943249252 +/- ...e-15] + [1.06127506190504 +/- ...e-15]*I
                sage: CBF(1, RIF(0,1/1000)).arcsin()
                [1.6 +/- 0.0619] + [+/- 0.0322]*I
                sage: CBF(1, RIF(0,1/1000)).arcsin(analytic=True)
                nan + nan*I"""
        @overload
        def arcsin(self) -> Any:
            """ComplexBall.arcsin(self, analytic=False)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3395)

            Return the arcsine of this ball.

            INPUT:

            - ``analytic`` -- boolean (default: ``False``); if ``True``, return an
              indeterminate (not-a-number) value when the input ball touches
              the branch cut

            EXAMPLES::

                sage: CBF(1+i).arcsin()
                [0.66623943249252 +/- ...e-15] + [1.06127506190504 +/- ...e-15]*I
                sage: CBF(1, RIF(0,1/1000)).arcsin()
                [1.6 +/- 0.0619] + [+/- 0.0322]*I
                sage: CBF(1, RIF(0,1/1000)).arcsin(analytic=True)
                nan + nan*I"""
        @overload
        def arcsin(self, analytic=...) -> Any:
            """ComplexBall.arcsin(self, analytic=False)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3395)

            Return the arcsine of this ball.

            INPUT:

            - ``analytic`` -- boolean (default: ``False``); if ``True``, return an
              indeterminate (not-a-number) value when the input ball touches
              the branch cut

            EXAMPLES::

                sage: CBF(1+i).arcsin()
                [0.66623943249252 +/- ...e-15] + [1.06127506190504 +/- ...e-15]*I
                sage: CBF(1, RIF(0,1/1000)).arcsin()
                [1.6 +/- 0.0619] + [+/- 0.0322]*I
                sage: CBF(1, RIF(0,1/1000)).arcsin(analytic=True)
                nan + nan*I"""
        @overload
        def arcsinh(self, analytic=...) -> Any:
            """ComplexBall.arcsinh(self, analytic=False)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3484)

            Return the hyperbolic arcsine of this ball.

            INPUT:

            - ``analytic`` -- boolean (default: ``False``); if ``True``, return an
              indeterminate (not-a-number) value when the input ball touches
              the branch cut

            EXAMPLES::

                sage: CBF(1+i).arcsinh()
                [1.06127506190504 +/- ...e-15] + [0.66623943249252 +/- ...e-15]*I
                sage: CBF(2*i).arcsinh()
                [1.31695789692482 +/- ...e-15] + [1.570796326794897 +/- ...e-16]*I
                sage: CBF(2*i).arcsinh(analytic=True)
                nan + nan*I"""
        @overload
        def arcsinh(self) -> Any:
            """ComplexBall.arcsinh(self, analytic=False)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3484)

            Return the hyperbolic arcsine of this ball.

            INPUT:

            - ``analytic`` -- boolean (default: ``False``); if ``True``, return an
              indeterminate (not-a-number) value when the input ball touches
              the branch cut

            EXAMPLES::

                sage: CBF(1+i).arcsinh()
                [1.06127506190504 +/- ...e-15] + [0.66623943249252 +/- ...e-15]*I
                sage: CBF(2*i).arcsinh()
                [1.31695789692482 +/- ...e-15] + [1.570796326794897 +/- ...e-16]*I
                sage: CBF(2*i).arcsinh(analytic=True)
                nan + nan*I"""
        @overload
        def arcsinh(self) -> Any:
            """ComplexBall.arcsinh(self, analytic=False)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3484)

            Return the hyperbolic arcsine of this ball.

            INPUT:

            - ``analytic`` -- boolean (default: ``False``); if ``True``, return an
              indeterminate (not-a-number) value when the input ball touches
              the branch cut

            EXAMPLES::

                sage: CBF(1+i).arcsinh()
                [1.06127506190504 +/- ...e-15] + [0.66623943249252 +/- ...e-15]*I
                sage: CBF(2*i).arcsinh()
                [1.31695789692482 +/- ...e-15] + [1.570796326794897 +/- ...e-16]*I
                sage: CBF(2*i).arcsinh(analytic=True)
                nan + nan*I"""
        @overload
        def arcsinh(self, analytic=...) -> Any:
            """ComplexBall.arcsinh(self, analytic=False)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3484)

            Return the hyperbolic arcsine of this ball.

            INPUT:

            - ``analytic`` -- boolean (default: ``False``); if ``True``, return an
              indeterminate (not-a-number) value when the input ball touches
              the branch cut

            EXAMPLES::

                sage: CBF(1+i).arcsinh()
                [1.06127506190504 +/- ...e-15] + [0.66623943249252 +/- ...e-15]*I
                sage: CBF(2*i).arcsinh()
                [1.31695789692482 +/- ...e-15] + [1.570796326794897 +/- ...e-16]*I
                sage: CBF(2*i).arcsinh(analytic=True)
                nan + nan*I"""
        @overload
        def arctan(self, analytic=...) -> Any:
            """ComplexBall.arctan(self, analytic=False)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3453)

            Return the arctangent of this ball.

            INPUT:

            - ``analytic`` -- boolean (default: ``False``); if ``True``, return an
              indeterminate (not-a-number) value when the input ball touches
              the branch cut

            EXAMPLES::

                sage: CBF(1+i).arctan()
                [1.017221967897851 +/- ...e-16] + [0.4023594781085251 +/- ...e-17]*I
                sage: CBF(i).arctan()
                nan + nan*I
                sage: CBF(2*i).arctan()
                [1.570796326794897 +/- ...e-16] + [0.549306144334055 +/- ...e-16]*I
                sage: CBF(2*i).arctan(analytic=True)
                nan + nan*I"""
        @overload
        def arctan(self) -> Any:
            """ComplexBall.arctan(self, analytic=False)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3453)

            Return the arctangent of this ball.

            INPUT:

            - ``analytic`` -- boolean (default: ``False``); if ``True``, return an
              indeterminate (not-a-number) value when the input ball touches
              the branch cut

            EXAMPLES::

                sage: CBF(1+i).arctan()
                [1.017221967897851 +/- ...e-16] + [0.4023594781085251 +/- ...e-17]*I
                sage: CBF(i).arctan()
                nan + nan*I
                sage: CBF(2*i).arctan()
                [1.570796326794897 +/- ...e-16] + [0.549306144334055 +/- ...e-16]*I
                sage: CBF(2*i).arctan(analytic=True)
                nan + nan*I"""
        @overload
        def arctan(self) -> Any:
            """ComplexBall.arctan(self, analytic=False)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3453)

            Return the arctangent of this ball.

            INPUT:

            - ``analytic`` -- boolean (default: ``False``); if ``True``, return an
              indeterminate (not-a-number) value when the input ball touches
              the branch cut

            EXAMPLES::

                sage: CBF(1+i).arctan()
                [1.017221967897851 +/- ...e-16] + [0.4023594781085251 +/- ...e-17]*I
                sage: CBF(i).arctan()
                nan + nan*I
                sage: CBF(2*i).arctan()
                [1.570796326794897 +/- ...e-16] + [0.549306144334055 +/- ...e-16]*I
                sage: CBF(2*i).arctan(analytic=True)
                nan + nan*I"""
        @overload
        def arctan(self) -> Any:
            """ComplexBall.arctan(self, analytic=False)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3453)

            Return the arctangent of this ball.

            INPUT:

            - ``analytic`` -- boolean (default: ``False``); if ``True``, return an
              indeterminate (not-a-number) value when the input ball touches
              the branch cut

            EXAMPLES::

                sage: CBF(1+i).arctan()
                [1.017221967897851 +/- ...e-16] + [0.4023594781085251 +/- ...e-17]*I
                sage: CBF(i).arctan()
                nan + nan*I
                sage: CBF(2*i).arctan()
                [1.570796326794897 +/- ...e-16] + [0.549306144334055 +/- ...e-16]*I
                sage: CBF(2*i).arctan(analytic=True)
                nan + nan*I"""
        @overload
        def arctan(self, analytic=...) -> Any:
            """ComplexBall.arctan(self, analytic=False)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3453)

            Return the arctangent of this ball.

            INPUT:

            - ``analytic`` -- boolean (default: ``False``); if ``True``, return an
              indeterminate (not-a-number) value when the input ball touches
              the branch cut

            EXAMPLES::

                sage: CBF(1+i).arctan()
                [1.017221967897851 +/- ...e-16] + [0.4023594781085251 +/- ...e-17]*I
                sage: CBF(i).arctan()
                nan + nan*I
                sage: CBF(2*i).arctan()
                [1.570796326794897 +/- ...e-16] + [0.549306144334055 +/- ...e-16]*I
                sage: CBF(2*i).arctan(analytic=True)
                nan + nan*I"""
        @overload
        def arctanh(self, analytic=...) -> Any:
            """ComplexBall.arctanh(self, analytic=False)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3542)

            Return the hyperbolic arctangent of this ball.

            INPUT:

            - ``analytic`` -- boolean (default: ``False``); if ``True``, return an
              indeterminate (not-a-number) value when the input ball touches
              the branch cut

            EXAMPLES::

                sage: CBF(1+i).arctanh()
                [0.4023594781085251 +/- ...e-17] + [1.017221967897851 +/- ...e-16]*I
                sage: CBF(-2).arctanh()
                [-0.549306144334055 +/- ...e-16] + [1.570796326794897 +/- ...e-16]*I
                sage: CBF(-2).arctanh(analytic=True)
                nan + nan*I"""
        @overload
        def arctanh(self) -> Any:
            """ComplexBall.arctanh(self, analytic=False)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3542)

            Return the hyperbolic arctangent of this ball.

            INPUT:

            - ``analytic`` -- boolean (default: ``False``); if ``True``, return an
              indeterminate (not-a-number) value when the input ball touches
              the branch cut

            EXAMPLES::

                sage: CBF(1+i).arctanh()
                [0.4023594781085251 +/- ...e-17] + [1.017221967897851 +/- ...e-16]*I
                sage: CBF(-2).arctanh()
                [-0.549306144334055 +/- ...e-16] + [1.570796326794897 +/- ...e-16]*I
                sage: CBF(-2).arctanh(analytic=True)
                nan + nan*I"""
        @overload
        def arctanh(self) -> Any:
            """ComplexBall.arctanh(self, analytic=False)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3542)

            Return the hyperbolic arctangent of this ball.

            INPUT:

            - ``analytic`` -- boolean (default: ``False``); if ``True``, return an
              indeterminate (not-a-number) value when the input ball touches
              the branch cut

            EXAMPLES::

                sage: CBF(1+i).arctanh()
                [0.4023594781085251 +/- ...e-17] + [1.017221967897851 +/- ...e-16]*I
                sage: CBF(-2).arctanh()
                [-0.549306144334055 +/- ...e-16] + [1.570796326794897 +/- ...e-16]*I
                sage: CBF(-2).arctanh(analytic=True)
                nan + nan*I"""
        @overload
        def arctanh(self, analytic=...) -> Any:
            """ComplexBall.arctanh(self, analytic=False)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3542)

            Return the hyperbolic arctangent of this ball.

            INPUT:

            - ``analytic`` -- boolean (default: ``False``); if ``True``, return an
              indeterminate (not-a-number) value when the input ball touches
              the branch cut

            EXAMPLES::

                sage: CBF(1+i).arctanh()
                [0.4023594781085251 +/- ...e-17] + [1.017221967897851 +/- ...e-16]*I
                sage: CBF(-2).arctanh()
                [-0.549306144334055 +/- ...e-16] + [1.570796326794897 +/- ...e-16]*I
                sage: CBF(-2).arctanh(analytic=True)
                nan + nan*I"""
        @overload
        def arg(self) -> Any:
            """ComplexBall.arg(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 1990)

            Return the argument of this complex ball.

            EXAMPLES::

                sage: CBF(1 + i).arg()
                [0.7853981633974483 +/- ...e-17]
                sage: CBF(-1).arg()
                [3.141592653589793 +/- ...e-16]
                sage: CBF(-1).arg().parent()
                Real ball field with 53 bits of precision"""
        @overload
        def arg(self) -> Any:
            """ComplexBall.arg(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 1990)

            Return the argument of this complex ball.

            EXAMPLES::

                sage: CBF(1 + i).arg()
                [0.7853981633974483 +/- ...e-17]
                sage: CBF(-1).arg()
                [3.141592653589793 +/- ...e-16]
                sage: CBF(-1).arg().parent()
                Real ball field with 53 bits of precision"""
        @overload
        def arg(self) -> Any:
            """ComplexBall.arg(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 1990)

            Return the argument of this complex ball.

            EXAMPLES::

                sage: CBF(1 + i).arg()
                [0.7853981633974483 +/- ...e-17]
                sage: CBF(-1).arg()
                [3.141592653589793 +/- ...e-16]
                sage: CBF(-1).arg().parent()
                Real ball field with 53 bits of precision"""
        @overload
        def arg(self) -> Any:
            """ComplexBall.arg(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 1990)

            Return the argument of this complex ball.

            EXAMPLES::

                sage: CBF(1 + i).arg()
                [0.7853981633974483 +/- ...e-17]
                sage: CBF(-1).arg()
                [3.141592653589793 +/- ...e-16]
                sage: CBF(-1).arg().parent()
                Real ball field with 53 bits of precision"""
        @overload
        def barnes_g(self) -> Any:
            """ComplexBall.barnes_g(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3800)

            Return the Barnes G-function of ``self``.

            EXAMPLES::

                sage: CBF(-4).barnes_g()
                0
                sage: CBF(8).barnes_g()
                24883200.00000000
                sage: CBF(500,10).barnes_g()
                [4.54078781e+254873 +/- ...e+254864] + [8.65835455e+254873 +/- ...e+254864]*I"""
        @overload
        def barnes_g(self) -> Any:
            """ComplexBall.barnes_g(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3800)

            Return the Barnes G-function of ``self``.

            EXAMPLES::

                sage: CBF(-4).barnes_g()
                0
                sage: CBF(8).barnes_g()
                24883200.00000000
                sage: CBF(500,10).barnes_g()
                [4.54078781e+254873 +/- ...e+254864] + [8.65835455e+254873 +/- ...e+254864]*I"""
        @overload
        def barnes_g(self) -> Any:
            """ComplexBall.barnes_g(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3800)

            Return the Barnes G-function of ``self``.

            EXAMPLES::

                sage: CBF(-4).barnes_g()
                0
                sage: CBF(8).barnes_g()
                24883200.00000000
                sage: CBF(500,10).barnes_g()
                [4.54078781e+254873 +/- ...e+254864] + [8.65835455e+254873 +/- ...e+254864]*I"""
        @overload
        def barnes_g(self) -> Any:
            """ComplexBall.barnes_g(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3800)

            Return the Barnes G-function of ``self``.

            EXAMPLES::

                sage: CBF(-4).barnes_g()
                0
                sage: CBF(8).barnes_g()
                24883200.00000000
                sage: CBF(500,10).barnes_g()
                [4.54078781e+254873 +/- ...e+254864] + [8.65835455e+254873 +/- ...e+254864]*I"""
        @overload
        def below_abs(self, test_zero=...) -> Any:
            """ComplexBall.below_abs(self, test_zero=False)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 1931)

            Return a lower bound for the absolute value of this complex ball.

            INPUT:

            - ``test_zero`` -- boolean (default: ``False``); if ``True``,
              make sure that the returned lower bound is positive, raising
              an error if the ball contains zero.

            OUTPUT: a ball with zero radius

            EXAMPLES::

                sage: b = ComplexBallField(8)(1+i).below_abs()
                sage: b
                [1.4 +/- 0.0141]
                sage: b.is_exact()
                True
                sage: QQ(b)*128
                181
                sage: (CBF(1/3) - 1/3).below_abs()
                0
                sage: (CBF(1/3) - 1/3).below_abs(test_zero=True)
                Traceback (most recent call last):
                ...
                ValueError: ball contains zero

            .. SEEALSO:: :meth:`above_abs`"""
        @overload
        def below_abs(self) -> Any:
            """ComplexBall.below_abs(self, test_zero=False)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 1931)

            Return a lower bound for the absolute value of this complex ball.

            INPUT:

            - ``test_zero`` -- boolean (default: ``False``); if ``True``,
              make sure that the returned lower bound is positive, raising
              an error if the ball contains zero.

            OUTPUT: a ball with zero radius

            EXAMPLES::

                sage: b = ComplexBallField(8)(1+i).below_abs()
                sage: b
                [1.4 +/- 0.0141]
                sage: b.is_exact()
                True
                sage: QQ(b)*128
                181
                sage: (CBF(1/3) - 1/3).below_abs()
                0
                sage: (CBF(1/3) - 1/3).below_abs(test_zero=True)
                Traceback (most recent call last):
                ...
                ValueError: ball contains zero

            .. SEEALSO:: :meth:`above_abs`"""
        @overload
        def below_abs(self) -> Any:
            """ComplexBall.below_abs(self, test_zero=False)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 1931)

            Return a lower bound for the absolute value of this complex ball.

            INPUT:

            - ``test_zero`` -- boolean (default: ``False``); if ``True``,
              make sure that the returned lower bound is positive, raising
              an error if the ball contains zero.

            OUTPUT: a ball with zero radius

            EXAMPLES::

                sage: b = ComplexBallField(8)(1+i).below_abs()
                sage: b
                [1.4 +/- 0.0141]
                sage: b.is_exact()
                True
                sage: QQ(b)*128
                181
                sage: (CBF(1/3) - 1/3).below_abs()
                0
                sage: (CBF(1/3) - 1/3).below_abs(test_zero=True)
                Traceback (most recent call last):
                ...
                ValueError: ball contains zero

            .. SEEALSO:: :meth:`above_abs`"""
        @overload
        def below_abs(self, test_zero=...) -> Any:
            """ComplexBall.below_abs(self, test_zero=False)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 1931)

            Return a lower bound for the absolute value of this complex ball.

            INPUT:

            - ``test_zero`` -- boolean (default: ``False``); if ``True``,
              make sure that the returned lower bound is positive, raising
              an error if the ball contains zero.

            OUTPUT: a ball with zero radius

            EXAMPLES::

                sage: b = ComplexBallField(8)(1+i).below_abs()
                sage: b
                [1.4 +/- 0.0141]
                sage: b.is_exact()
                True
                sage: QQ(b)*128
                181
                sage: (CBF(1/3) - 1/3).below_abs()
                0
                sage: (CBF(1/3) - 1/3).below_abs(test_zero=True)
                Traceback (most recent call last):
                ...
                ValueError: ball contains zero

            .. SEEALSO:: :meth:`above_abs`"""
        def bessel_I(self, nu) -> Any:
            """ComplexBall.bessel_I(self, nu)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4200)

            Return the modified Bessel function of the first kind with argument ``self``
            and index ``nu``.

            EXAMPLES::

                sage: CBF(1, 1).bessel_I(1)
                [0.365028028827088 +/- ...e-16] + [0.614160334922903 +/- ...e-16]*I
                sage: CBF(100, -100).bessel_I(1/3)
                [5.4362189595644e+41 +/- ...e+27] + [7.1989436985321e+41 +/- ...e+27]*I"""
        def bessel_J(self, nu) -> Any:
            """ComplexBall.bessel_J(self, nu)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4140)

            Return the Bessel function of the first kind with argument ``self``
            and index ``nu``.

            EXAMPLES::

                sage: CBF(1, 1).bessel_J(1)
                [0.614160334922903 +/- ...e-16] + [0.365028028827088 +/- ...e-16]*I
                sage: CBF(100, -100).bessel_J(1/3)
                [1.108431870251e+41 +/- ...e+28] + [-8.952577603125e+41 +/- ...e+28]*I"""
        def bessel_J_Y(self, nu) -> Any:
            """ComplexBall.bessel_J_Y(self, nu)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4159)

            Return the Bessel function of the first and second kind with argument
            ``self`` and index ``nu``, computed simultaneously.

            EXAMPLES::

                sage: J, Y = CBF(1, 1).bessel_J_Y(1)
                sage: J - CBF(1, 1).bessel_J(1)
                [+/- ...e-16] + [+/- ...e-16]*I
                sage: Y - CBF(1, 1).bessel_Y(1)
                [+/- ...e-14] + [+/- ...e-14]*I"""
        def bessel_K(self, nu) -> Any:
            """ComplexBall.bessel_K(self, nu)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4219)

            Return the modified Bessel function of the second kind with argument
            ``self`` and index ``nu``.

            EXAMPLES::

                sage: CBF(1, 1).bessel_K(0)
                [0.08019772694652 +/- ...e-15] + [-0.357277459285330 +/- ...e-16]*I
                sage: CBF(1, 1).bessel_K(1)
                [0.02456830552374 +/- ...e-15] + [-0.45971947380119 +/- ...e-15]*I
                sage: CBF(100, 100).bessel_K(QQbar(i))
                [3.8693896656383e-45 +/- ...e-59] + [5.507100423418e-46 +/- ...e-59]*I"""
        def bessel_Y(self, nu) -> Any:
            """ComplexBall.bessel_Y(self, nu)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4181)

            Return the Bessel function of the second kind with argument ``self``
            and index ``nu``.

            EXAMPLES::

                sage: CBF(1, 1).bessel_Y(1)
                [-0.6576945355913 +/- ...e-14] + [0.6298010039929 +/- ...e-14]*I
                sage: CBF(100, -100).bessel_Y(1/3)
                [-8.952577603125e+41 +/- ...e+28] + [-1.108431870251e+41 +/- ...e+28]*I"""
        def chebyshev_T(self, n) -> Any:
            """ComplexBall.chebyshev_T(self, n)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4966)

            Return the Chebyshev function of the first kind of order ``n``
            evaluated at ``self``.

            EXAMPLES::

                sage: CBF(1/3).chebyshev_T(20)
                [0.8710045668809 +/- ...e-14]
                sage: CBF(1/3).chebyshev_T(CBF(5,1))
                [1.84296854518763 +/- ...e-15] + [0.20053614301799 +/- ...e-15]*I"""
        def chebyshev_U(self, n) -> Any:
            """ComplexBall.chebyshev_U(self, n)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4985)

            Return the Chebyshev function of the second kind of order ``n``
            evaluated at ``self``.

            EXAMPLES::

                sage: CBF(1/3).chebyshev_U(20)
                [0.6973126541184 +/- ...e-14]
                sage: CBF(1/3).chebyshev_U(CBF(5,1))
                [1.75884964893425 +/- ...e-15] + [0.7497317165104 +/- ...e-14]*I"""
        @overload
        def conjugate(self) -> Any:
            """ComplexBall.conjugate(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 2663)

            Return the complex conjugate of this ball.

            EXAMPLES::

                sage: CBF(-2 + I/3).conjugate()
                -2.000000000000000 + [-0.3333333333333333 +/- ...e-17]*I"""
        @overload
        def conjugate(self) -> Any:
            """ComplexBall.conjugate(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 2663)

            Return the complex conjugate of this ball.

            EXAMPLES::

                sage: CBF(-2 + I/3).conjugate()
                -2.000000000000000 + [-0.3333333333333333 +/- ...e-17]*I"""
        def contains_exact(self, other) -> Any:
            """ComplexBall.contains_exact(self, other)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 2544)

            Return ``True`` *iff* ``other`` is contained in ``self``.

            Use ``other in self`` for a test that works for a wider range of inputs
            but may return false negatives.

            INPUT:

            - ``other`` -- :class:`ComplexBall`,
              :class:`~sage.rings.integer.Integer`,
              or :class:`~sage.rings.rational.Rational`

            EXAMPLES::

                sage: CBF(RealBallField(100)(1/3), 0).contains_exact(1/3)
                True
                sage: CBF(1).contains_exact(1)
                True
                sage: CBF(1).contains_exact(CBF(1))
                True

                sage: CBF(sqrt(2)).contains_exact(sqrt(2))                                  # needs sage.symbolic
                Traceback (most recent call last):
                ...
                TypeError: unsupported type: <class 'sage.symbolic.expression.Expression'>"""
        @overload
        def contains_integer(self) -> Any:
            """ComplexBall.contains_integer(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 2635)

            Return ``True`` iff this ball contains any integer.

            EXAMPLES::

                sage: CBF(3, RBF(0.1)).contains_integer()
                False
                sage: CBF(3, RBF(0.1,0.1)).contains_integer()
                True"""
        @overload
        def contains_integer(self) -> Any:
            """ComplexBall.contains_integer(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 2635)

            Return ``True`` iff this ball contains any integer.

            EXAMPLES::

                sage: CBF(3, RBF(0.1)).contains_integer()
                False
                sage: CBF(3, RBF(0.1,0.1)).contains_integer()
                True"""
        @overload
        def contains_integer(self) -> Any:
            """ComplexBall.contains_integer(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 2635)

            Return ``True`` iff this ball contains any integer.

            EXAMPLES::

                sage: CBF(3, RBF(0.1)).contains_integer()
                False
                sage: CBF(3, RBF(0.1,0.1)).contains_integer()
                True"""
        @overload
        def contains_zero(self) -> Any:
            """ComplexBall.contains_zero(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 2620)

            Return ``True`` iff this ball contains zero.

            EXAMPLES::

                sage: CBF(0).contains_zero()
                True
                sage: CBF(RIF(-1,1)).contains_zero()
                True
                sage: CBF(i).contains_zero()
                False"""
        @overload
        def contains_zero(self) -> Any:
            """ComplexBall.contains_zero(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 2620)

            Return ``True`` iff this ball contains zero.

            EXAMPLES::

                sage: CBF(0).contains_zero()
                True
                sage: CBF(RIF(-1,1)).contains_zero()
                True
                sage: CBF(i).contains_zero()
                False"""
        @overload
        def contains_zero(self) -> Any:
            """ComplexBall.contains_zero(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 2620)

            Return ``True`` iff this ball contains zero.

            EXAMPLES::

                sage: CBF(0).contains_zero()
                True
                sage: CBF(RIF(-1,1)).contains_zero()
                True
                sage: CBF(i).contains_zero()
                False"""
        @overload
        def contains_zero(self) -> Any:
            """ComplexBall.contains_zero(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 2620)

            Return ``True`` iff this ball contains zero.

            EXAMPLES::

                sage: CBF(0).contains_zero()
                True
                sage: CBF(RIF(-1,1)).contains_zero()
                True
                sage: CBF(i).contains_zero()
                False"""
        @overload
        def cos(self) -> Any:
            """ComplexBall.cos(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3220)

            Return the cosine of this ball.

            EXAMPLES::

                sage: CBF(i*pi).cos()                                                       # needs sage.symbolic
                [11.59195327552152 +/- ...e-15]"""
        @overload
        def cos(self) -> Any:
            """ComplexBall.cos(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3220)

            Return the cosine of this ball.

            EXAMPLES::

                sage: CBF(i*pi).cos()                                                       # needs sage.symbolic
                [11.59195327552152 +/- ...e-15]"""
        def cos_integral(self, *args, **kwargs):
            """ComplexBall.Ci(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4305)

            Return the cosine integral with argument ``self``.

            EXAMPLES::

                sage: CBF(1, 1).Ci()  # abs tol 5e-16
                [0.882172180555936 +/- 5.89e-16] + [0.287249133519956 +/- 3.37e-16]*I
                sage: CBF(0).Ci()
                nan + nan*I

            TESTS:

                sage: CBF(Ci(I))  # abs tol 5e-16                                           # needs sage.symbolic
                [0.837866940980208 +/- 4.72e-16] + [1.570796326794897 +/- 5.54e-16]*I"""
        @overload
        def cosh(self) -> Any:
            """ComplexBall.cosh(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3314)

            Return the hyperbolic cosine of this ball.

            EXAMPLES::

                sage: CBF(1, 1).cosh()
                [0.833730025131149 +/- ...e-16] + [0.988897705762865 +/- ...e-16]*I"""
        @overload
        def cosh(self) -> Any:
            """ComplexBall.cosh(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3314)

            Return the hyperbolic cosine of this ball.

            EXAMPLES::

                sage: CBF(1, 1).cosh()
                [0.833730025131149 +/- ...e-16] + [0.988897705762865 +/- ...e-16]*I"""
        def cosh_integral(self, *args, **kwargs):
            """ComplexBall.Chi(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4353)

            Return the hyperbolic cosine integral with argument ``self``.

            EXAMPLES::

                sage: CBF(1, 1).Chi()  # abs tol 1e-15
                [0.882172180555936 +/- 5.89e-16] + [1.28354719327494 +/- 1.01e-15]*I
                sage: CBF(0).Chi()
                nan + nan*I

            TESTS:

                sage: CBF(Chi(I))  # abs tol 5e-16                                          # needs sage.symbolic
                [0.337403922900968 +/- 3.25e-16] + [1.570796326794897 +/- 5.54e-16]*I"""
        @overload
        def cot(self) -> Any:
            """ComplexBall.cot(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3252)

            Return the cotangent of this ball.

            EXAMPLES::

                sage: CBF(pi, 1/10).cot()                                                   # needs sage.symbolic
                [+/- ...e-14] + [-10.03331113225399 +/- ...e-15]*I
                sage: CBF(pi).cot()                                                         # needs sage.symbolic
                nan"""
        @overload
        def cot(self) -> Any:
            """ComplexBall.cot(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3252)

            Return the cotangent of this ball.

            EXAMPLES::

                sage: CBF(pi, 1/10).cot()                                                   # needs sage.symbolic
                [+/- ...e-14] + [-10.03331113225399 +/- ...e-15]*I
                sage: CBF(pi).cot()                                                         # needs sage.symbolic
                nan"""
        @overload
        def cot(self) -> Any:
            """ComplexBall.cot(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3252)

            Return the cotangent of this ball.

            EXAMPLES::

                sage: CBF(pi, 1/10).cot()                                                   # needs sage.symbolic
                [+/- ...e-14] + [-10.03331113225399 +/- ...e-15]*I
                sage: CBF(pi).cot()                                                         # needs sage.symbolic
                nan"""
        @overload
        def coth(self) -> Any:
            """ComplexBall.coth(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3346)

            Return the hyperbolic cotangent of this ball.

            EXAMPLES::

                sage: CBF(1, 1).coth()
                [0.868014142895925 +/- ...e-16] + [-0.2176215618544027 +/- ...e-17]*I
                sage: CBF(0, pi).coth()                                                     # needs sage.symbolic
                nan*I"""
        @overload
        def coth(self) -> Any:
            """ComplexBall.coth(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3346)

            Return the hyperbolic cotangent of this ball.

            EXAMPLES::

                sage: CBF(1, 1).coth()
                [0.868014142895925 +/- ...e-16] + [-0.2176215618544027 +/- ...e-17]*I
                sage: CBF(0, pi).coth()                                                     # needs sage.symbolic
                nan*I"""
        @overload
        def coth(self) -> Any:
            """ComplexBall.coth(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3346)

            Return the hyperbolic cotangent of this ball.

            EXAMPLES::

                sage: CBF(1, 1).coth()
                [0.868014142895925 +/- ...e-16] + [-0.2176215618544027 +/- ...e-17]*I
                sage: CBF(0, pi).coth()                                                     # needs sage.symbolic
                nan*I"""
        @overload
        def csc(self) -> Any:
            """ComplexBall.csc(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3284)

            Return the cosecant of this ball.

            EXAMPLES::

                sage: CBF(1, 1).csc()
                [0.621518017170428 +/- ...e-16] + [-0.303931001628426 +/- ...e-16]*I"""
        @overload
        def csc(self) -> Any:
            """ComplexBall.csc(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3284)

            Return the cosecant of this ball.

            EXAMPLES::

                sage: CBF(1, 1).csc()
                [0.621518017170428 +/- ...e-16] + [-0.303931001628426 +/- ...e-16]*I"""
        @overload
        def csch(self) -> Any:
            """ComplexBall.csch(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3378)

            Return the hyperbolic cosecant of this ball.

            EXAMPLES::

                sage: CBF(1, 1).csch()
                [0.303931001628426 +/- ...e-16] + [-0.621518017170428 +/- ...e-16]*I
                sage: CBF(i*pi).csch()                                                      # needs sage.symbolic
                nan*I"""
        @overload
        def csch(self) -> Any:
            """ComplexBall.csch(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3378)

            Return the hyperbolic cosecant of this ball.

            EXAMPLES::

                sage: CBF(1, 1).csch()
                [0.303931001628426 +/- ...e-16] + [-0.621518017170428 +/- ...e-16]*I
                sage: CBF(i*pi).csch()                                                      # needs sage.symbolic
                nan*I"""
        @overload
        def csch(self) -> Any:
            """ComplexBall.csch(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3378)

            Return the hyperbolic cosecant of this ball.

            EXAMPLES::

                sage: CBF(1, 1).csch()
                [0.303931001628426 +/- ...e-16] + [-0.621518017170428 +/- ...e-16]*I
                sage: CBF(i*pi).csch()                                                      # needs sage.symbolic
                nan*I"""
        @overload
        def cube(self) -> Any:
            """ComplexBall.cube(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3030)

            Return the cube of this ball.

            The result is computed efficiently using two real squarings, two real
            multiplications, and scalar operations.

            EXAMPLES::

                sage: CBF(1, 1).cube()
                -2.000000000000000 + 2.000000000000000*I"""
        @overload
        def cube(self) -> Any:
            """ComplexBall.cube(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3030)

            Return the cube of this ball.

            The result is computed efficiently using two real squarings, two real
            multiplications, and scalar operations.

            EXAMPLES::

                sage: CBF(1, 1).cube()
                -2.000000000000000 + 2.000000000000000*I"""
        @overload
        def diameter(self) -> Any:
            """ComplexBall.diameter(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 2117)

            Return the diameter of this ball.

            EXAMPLES::

                sage: CBF(1 + i).diameter()
                0.00000000
                sage: CBF(i/3).diameter()
                2.2204460e-16
                sage: CBF(i/3).diameter().parent()
                Real Field with 30 bits of precision
                sage: CBF(CIF(RIF(1.02, 1.04), RIF(2.1, 2.2))).diameter()
                0.20000000

            .. SEEALSO:: :meth:`rad`, :meth:`mid`"""
        @overload
        def diameter(self) -> Any:
            """ComplexBall.diameter(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 2117)

            Return the diameter of this ball.

            EXAMPLES::

                sage: CBF(1 + i).diameter()
                0.00000000
                sage: CBF(i/3).diameter()
                2.2204460e-16
                sage: CBF(i/3).diameter().parent()
                Real Field with 30 bits of precision
                sage: CBF(CIF(RIF(1.02, 1.04), RIF(2.1, 2.2))).diameter()
                0.20000000

            .. SEEALSO:: :meth:`rad`, :meth:`mid`"""
        @overload
        def diameter(self) -> Any:
            """ComplexBall.diameter(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 2117)

            Return the diameter of this ball.

            EXAMPLES::

                sage: CBF(1 + i).diameter()
                0.00000000
                sage: CBF(i/3).diameter()
                2.2204460e-16
                sage: CBF(i/3).diameter().parent()
                Real Field with 30 bits of precision
                sage: CBF(CIF(RIF(1.02, 1.04), RIF(2.1, 2.2))).diameter()
                0.20000000

            .. SEEALSO:: :meth:`rad`, :meth:`mid`"""
        @overload
        def diameter(self) -> Any:
            """ComplexBall.diameter(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 2117)

            Return the diameter of this ball.

            EXAMPLES::

                sage: CBF(1 + i).diameter()
                0.00000000
                sage: CBF(i/3).diameter()
                2.2204460e-16
                sage: CBF(i/3).diameter().parent()
                Real Field with 30 bits of precision
                sage: CBF(CIF(RIF(1.02, 1.04), RIF(2.1, 2.2))).diameter()
                0.20000000

            .. SEEALSO:: :meth:`rad`, :meth:`mid`"""
        @overload
        def diameter(self) -> Any:
            """ComplexBall.diameter(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 2117)

            Return the diameter of this ball.

            EXAMPLES::

                sage: CBF(1 + i).diameter()
                0.00000000
                sage: CBF(i/3).diameter()
                2.2204460e-16
                sage: CBF(i/3).diameter().parent()
                Real Field with 30 bits of precision
                sage: CBF(CIF(RIF(1.02, 1.04), RIF(2.1, 2.2))).diameter()
                0.20000000

            .. SEEALSO:: :meth:`rad`, :meth:`mid`"""
        def eisenstein(self, longn) -> Any:
            """ComplexBall.eisenstein(self, long n)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4556)

            Return the first ``n`` entries in the sequence of Eisenstein series
            `G_4(\\tau), G_6(\\tau), G_8(\\tau), \\ldots` where *tau* is given
            by ``self``. The output is a list.

            EXAMPLES::

                sage: a, b, c, d = 2, 5, 1, 3
                sage: tau = CBF(1,3)
                sage: tau.eisenstein(4)
                [[2.1646498507193 +/- ...e-14],
                 [2.0346794456073 +/- ...e-14],
                 [2.0081609898081 +/- ...e-14],
                 [2.0019857082706 +/- ...e-14]]
                sage: ((a*tau+b)/(c*tau+d)).eisenstein(3)[2]
                [331011.2004330 +/- ...e-8] + [-711178.1655746 +/- ...e-8]*I
                sage: (c*tau+d)^8 * tau.eisenstein(3)[2]
                [331011.20043304 +/- ...e-9] + [-711178.1655746 +/- ...e-8]*I"""
        @overload
        def elliptic_e(self) -> Any:
            """ComplexBall.elliptic_e(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4703)

            Return the complete elliptic integral of the second kind evaluated
            at *m* given by ``self``.

            EXAMPLES::

                sage: CBF(2,3).elliptic_e()
                [1.472797144959 +/- ...e-13] + [-1.231604783936 +/- ...e-14]*I"""
        @overload
        def elliptic_e(self) -> Any:
            """ComplexBall.elliptic_e(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4703)

            Return the complete elliptic integral of the second kind evaluated
            at *m* given by ``self``.

            EXAMPLES::

                sage: CBF(2,3).elliptic_e()
                [1.472797144959 +/- ...e-13] + [-1.231604783936 +/- ...e-14]*I"""
        def elliptic_e_inc(self, m) -> Any:
            """ComplexBall.elliptic_e_inc(self, m)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4773)

            Return the incomplete elliptic integral of the second kind evaluated
            at *m*.

            See :meth:`elliptic_e` for the corresponding complete integral

            INPUT:

            - ``m`` -- complex ball

            EXAMPLES::

                sage: CBF(1,2).elliptic_e_inc(CBF(0,1))
                [1.906576998914 +/- ...e-13] + [3.6896645289411 +/- ...e-14]*I

            At parameter `\\pi/2` it is a complete integral::

                sage: phi = CBF(1,1)
                sage: (CBF.pi()/2).elliptic_e_inc(phi)
                [1.2838409578982 +/- ...e-14] + [-0.5317843366915 +/- ...e-14]*I
                sage: phi.elliptic_e()
                [1.2838409578982 +/- 5...e-14] + [-0.5317843366915 +/- 3...e-14]*I

                sage: phi = CBF(2, 3/7)
                sage: (CBF.pi()/2).elliptic_e_inc(phi)
                [0.787564350925 +/- ...e-13] + [-0.686896129145 +/- ...e-13]*I
                sage: phi.elliptic_e()
                [0.7875643509254 +/- ...e-14] + [-0.686896129145 +/- ...e-13]*I"""
        def elliptic_f(self, m) -> Any:
            """ComplexBall.elliptic_f(self, m)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4736)

            Return the incomplete elliptic integral of the first kind evaluated
            at *m*.

            See :meth:`elliptic_k` for the corresponding complete integral

            INPUT:

            - ``m`` -- complex ball

            EXAMPLES::

                sage: CBF(1,2).elliptic_f(CBF(0,1))
                [0.6821522911854 +/- ...e-14] + [1.2482780628143 +/- ...e-14]*I

            At parameter `\\pi/2` it is a complete integral::

                sage: phi = CBF(1,1)
                sage: (CBF.pi()/2).elliptic_f(phi)
                [1.5092369540513 +/- ...e-14] + [0.6251464152027 +/- ...e-15]*I
                sage: phi.elliptic_k()
                [1.50923695405127 +/- ...e-15] + [0.62514641520270 +/- ...e-15]*I

                sage: phi = CBF(2, 3/7)
                sage: (CBF.pi()/2).elliptic_f(phi)
                [1.3393589639094 +/- ...e-14] + [1.1104369690719 +/- ...e-14]*I
                sage: phi.elliptic_k()
                [1.33935896390938 +/- ...e-15] + [1.11043696907194 +/- ...e-15]*I"""
        @overload
        def elliptic_invariants(self) -> Any:
            """ComplexBall.elliptic_invariants(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4645)

            Return the lattice invariants ``(g2, g3)``.

            EXAMPLES::

                sage: CBF(0,1).elliptic_invariants()
                ([189.07272012923 +/- ...e-12], [+/- ...e-12])
                sage: CBF(sqrt(2)/2, sqrt(2)/2).elliptic_invariants()                       # needs sage.symbolic
                ([+/- ...e-12] + [-332.5338031465...]*I,
                 [1254.46842157...] + [1254.46842157...]*I)"""
        @overload
        def elliptic_invariants(self) -> Any:
            """ComplexBall.elliptic_invariants(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4645)

            Return the lattice invariants ``(g2, g3)``.

            EXAMPLES::

                sage: CBF(0,1).elliptic_invariants()
                ([189.07272012923 +/- ...e-12], [+/- ...e-12])
                sage: CBF(sqrt(2)/2, sqrt(2)/2).elliptic_invariants()                       # needs sage.symbolic
                ([+/- ...e-12] + [-332.5338031465...]*I,
                 [1254.46842157...] + [1254.46842157...]*I)"""
        @overload
        def elliptic_invariants(self) -> Any:
            """ComplexBall.elliptic_invariants(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4645)

            Return the lattice invariants ``(g2, g3)``.

            EXAMPLES::

                sage: CBF(0,1).elliptic_invariants()
                ([189.07272012923 +/- ...e-12], [+/- ...e-12])
                sage: CBF(sqrt(2)/2, sqrt(2)/2).elliptic_invariants()                       # needs sage.symbolic
                ([+/- ...e-12] + [-332.5338031465...]*I,
                 [1254.46842157...] + [1254.46842157...]*I)"""
        @overload
        def elliptic_k(self) -> Any:
            """ComplexBall.elliptic_k(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4687)

            Return the complete elliptic integral of the first kind evaluated
            at *m* given by ``self``.

            EXAMPLES::

                sage: CBF(2,3).elliptic_k()
                [1.04291329192852 +/- ...e-15] + [0.62968247230864 +/- ...e-15]*I"""
        @overload
        def elliptic_k(self) -> Any:
            """ComplexBall.elliptic_k(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4687)

            Return the complete elliptic integral of the first kind evaluated
            at *m* given by ``self``.

            EXAMPLES::

                sage: CBF(2,3).elliptic_k()
                [1.04291329192852 +/- ...e-15] + [0.62968247230864 +/- ...e-15]*I"""
        @overload
        def elliptic_p(self, tau, n=...) -> Any:
            """ComplexBall.elliptic_p(self, tau, n=None)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4588)

            Return the Weierstrass elliptic function with lattice parameter ``tau``,
            evaluated at ``self``. The function is doubly periodic in ``self``
            with periods 1 and ``tau``, which should lie in the upper half plane.

            If ``n`` is given, return a list containing the first ``n``
            terms in the Taylor expansion at ``self``. In particular, with
            ``n`` = 2, compute the Weierstrass elliptic function together
            with its derivative, which generate the field of elliptic
            functions with periods 1 and ``tau``.

            EXAMPLES::

                sage: tau = CBF(1,4)
                sage: z = CBF(sqrt(2), sqrt(3))                                             # needs sage.symbolic
                sage: z.elliptic_p(tau)                                                     # needs sage.symbolic
                [-3.28920996772709 +/- ...e-15] + [-0.0003673767302933 +/- ...e-17]*I
                sage: (z + tau).elliptic_p(tau)                                             # needs sage.symbolic
                [-3.28920996772709 +/- ...e-15] + [-0.000367376730293 +/- ...e-16]*I
                sage: (z + 1).elliptic_p(tau)                                               # needs sage.symbolic
                [-3.28920996772709 +/- ...e-15] + [-0.0003673767302933 +/- ...e-17]*I

                sage: z.elliptic_p(tau, 3)                                                  # needs sage.symbolic
                [[-3.28920996772709 +/- ...e-15] + [-0.0003673767302933 +/- ...e-17]*I,
                 [0.002473055794309 +/- ...e-16] + [0.003859554040267 +/- ...e-16]*I,
                 [-0.01299087561709 +/- ...e-15] + [0.00725027521915 +/- ...e-15]*I]
                sage: (z + 3 + 4*tau).elliptic_p(tau, 3)                                    # needs sage.symbolic
                [[-3.28920996772709 +/- ...e-15] + [-0.00036737673029 +/- ...e-15]*I,
                 [0.0024730557943 +/- ...e-14] + [0.0038595540403 +/- ...e-14]*I,
                 [-0.01299087562 +/- ...e-12] + [0.00725027522 +/- ...e-12]*I]"""
        @overload
        def elliptic_p(self, tau) -> Any:
            """ComplexBall.elliptic_p(self, tau, n=None)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4588)

            Return the Weierstrass elliptic function with lattice parameter ``tau``,
            evaluated at ``self``. The function is doubly periodic in ``self``
            with periods 1 and ``tau``, which should lie in the upper half plane.

            If ``n`` is given, return a list containing the first ``n``
            terms in the Taylor expansion at ``self``. In particular, with
            ``n`` = 2, compute the Weierstrass elliptic function together
            with its derivative, which generate the field of elliptic
            functions with periods 1 and ``tau``.

            EXAMPLES::

                sage: tau = CBF(1,4)
                sage: z = CBF(sqrt(2), sqrt(3))                                             # needs sage.symbolic
                sage: z.elliptic_p(tau)                                                     # needs sage.symbolic
                [-3.28920996772709 +/- ...e-15] + [-0.0003673767302933 +/- ...e-17]*I
                sage: (z + tau).elliptic_p(tau)                                             # needs sage.symbolic
                [-3.28920996772709 +/- ...e-15] + [-0.000367376730293 +/- ...e-16]*I
                sage: (z + 1).elliptic_p(tau)                                               # needs sage.symbolic
                [-3.28920996772709 +/- ...e-15] + [-0.0003673767302933 +/- ...e-17]*I

                sage: z.elliptic_p(tau, 3)                                                  # needs sage.symbolic
                [[-3.28920996772709 +/- ...e-15] + [-0.0003673767302933 +/- ...e-17]*I,
                 [0.002473055794309 +/- ...e-16] + [0.003859554040267 +/- ...e-16]*I,
                 [-0.01299087561709 +/- ...e-15] + [0.00725027521915 +/- ...e-15]*I]
                sage: (z + 3 + 4*tau).elliptic_p(tau, 3)                                    # needs sage.symbolic
                [[-3.28920996772709 +/- ...e-15] + [-0.00036737673029 +/- ...e-15]*I,
                 [0.0024730557943 +/- ...e-14] + [0.0038595540403 +/- ...e-14]*I,
                 [-0.01299087562 +/- ...e-12] + [0.00725027522 +/- ...e-12]*I]"""
        @overload
        def elliptic_p(self, tau) -> Any:
            """ComplexBall.elliptic_p(self, tau, n=None)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4588)

            Return the Weierstrass elliptic function with lattice parameter ``tau``,
            evaluated at ``self``. The function is doubly periodic in ``self``
            with periods 1 and ``tau``, which should lie in the upper half plane.

            If ``n`` is given, return a list containing the first ``n``
            terms in the Taylor expansion at ``self``. In particular, with
            ``n`` = 2, compute the Weierstrass elliptic function together
            with its derivative, which generate the field of elliptic
            functions with periods 1 and ``tau``.

            EXAMPLES::

                sage: tau = CBF(1,4)
                sage: z = CBF(sqrt(2), sqrt(3))                                             # needs sage.symbolic
                sage: z.elliptic_p(tau)                                                     # needs sage.symbolic
                [-3.28920996772709 +/- ...e-15] + [-0.0003673767302933 +/- ...e-17]*I
                sage: (z + tau).elliptic_p(tau)                                             # needs sage.symbolic
                [-3.28920996772709 +/- ...e-15] + [-0.000367376730293 +/- ...e-16]*I
                sage: (z + 1).elliptic_p(tau)                                               # needs sage.symbolic
                [-3.28920996772709 +/- ...e-15] + [-0.0003673767302933 +/- ...e-17]*I

                sage: z.elliptic_p(tau, 3)                                                  # needs sage.symbolic
                [[-3.28920996772709 +/- ...e-15] + [-0.0003673767302933 +/- ...e-17]*I,
                 [0.002473055794309 +/- ...e-16] + [0.003859554040267 +/- ...e-16]*I,
                 [-0.01299087561709 +/- ...e-15] + [0.00725027521915 +/- ...e-15]*I]
                sage: (z + 3 + 4*tau).elliptic_p(tau, 3)                                    # needs sage.symbolic
                [[-3.28920996772709 +/- ...e-15] + [-0.00036737673029 +/- ...e-15]*I,
                 [0.0024730557943 +/- ...e-14] + [0.0038595540403 +/- ...e-14]*I,
                 [-0.01299087562 +/- ...e-12] + [0.00725027522 +/- ...e-12]*I]"""
        @overload
        def elliptic_p(self, tau) -> Any:
            """ComplexBall.elliptic_p(self, tau, n=None)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4588)

            Return the Weierstrass elliptic function with lattice parameter ``tau``,
            evaluated at ``self``. The function is doubly periodic in ``self``
            with periods 1 and ``tau``, which should lie in the upper half plane.

            If ``n`` is given, return a list containing the first ``n``
            terms in the Taylor expansion at ``self``. In particular, with
            ``n`` = 2, compute the Weierstrass elliptic function together
            with its derivative, which generate the field of elliptic
            functions with periods 1 and ``tau``.

            EXAMPLES::

                sage: tau = CBF(1,4)
                sage: z = CBF(sqrt(2), sqrt(3))                                             # needs sage.symbolic
                sage: z.elliptic_p(tau)                                                     # needs sage.symbolic
                [-3.28920996772709 +/- ...e-15] + [-0.0003673767302933 +/- ...e-17]*I
                sage: (z + tau).elliptic_p(tau)                                             # needs sage.symbolic
                [-3.28920996772709 +/- ...e-15] + [-0.000367376730293 +/- ...e-16]*I
                sage: (z + 1).elliptic_p(tau)                                               # needs sage.symbolic
                [-3.28920996772709 +/- ...e-15] + [-0.0003673767302933 +/- ...e-17]*I

                sage: z.elliptic_p(tau, 3)                                                  # needs sage.symbolic
                [[-3.28920996772709 +/- ...e-15] + [-0.0003673767302933 +/- ...e-17]*I,
                 [0.002473055794309 +/- ...e-16] + [0.003859554040267 +/- ...e-16]*I,
                 [-0.01299087561709 +/- ...e-15] + [0.00725027521915 +/- ...e-15]*I]
                sage: (z + 3 + 4*tau).elliptic_p(tau, 3)                                    # needs sage.symbolic
                [[-3.28920996772709 +/- ...e-15] + [-0.00036737673029 +/- ...e-15]*I,
                 [0.0024730557943 +/- ...e-14] + [0.0038595540403 +/- ...e-14]*I,
                 [-0.01299087562 +/- ...e-12] + [0.00725027522 +/- ...e-12]*I]"""
        def elliptic_pi(self, m) -> Any:
            """ComplexBall.elliptic_pi(self, m)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4719)

            Return the complete elliptic integral of the third kind evaluated
            at *m* given by ``self``.

            EXAMPLES::

                sage: CBF(2,3).elliptic_pi(CBF(1,1))
                [0.2702999736198...] + [0.715676058329...]*I"""
        def elliptic_pi_inc(self, phi, m) -> Any:
            """ComplexBall.elliptic_pi_inc(self, phi, m)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4810)

            Return the Legendre incomplete elliptic integral of the third kind.

            See: :meth:`elliptic_pi` for the complete integral.

            INPUT:

            - ``phi`` -- complex ball

            - ``m`` -- complex ball

            EXAMPLES::

                sage: CBF(1,2).elliptic_pi_inc(CBF(0,1), CBF(2,-3))
                [0.05738864021418 +/- ...e-15] + [0.55557494549951 +/- ...e-15]*I

            At parameter `\\pi/2` it is a complete integral::

                sage: n = CBF(1,1)
                sage: m = CBF(-2/3, 3/5)
                sage: n.elliptic_pi_inc(CBF.pi()/2, m) # this is a regression, see :issue:28623
                nan + nan*I
                sage: n.elliptic_pi(m)
                [0.8934793755173...] + [0.957078687107...]*I

                sage: n = CBF(2, 3/7)
                sage: m = CBF(-1/3, 2/9)
                sage: n.elliptic_pi_inc(CBF.pi()/2, m) # this is a regression, see :issue:28623
                nan + nan*I
                sage: n.elliptic_pi(m)
                [0.296958874641...] + [1.318879533273...]*I"""
        def elliptic_rf(self, y, z) -> Any:
            """ComplexBall.elliptic_rf(self, y, z)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4851)

            Return the Carlson symmetric elliptic integral of the first kind evaluated
            at ``(self, y, z)``.

            INPUT:

            - ``y`` -- complex ball

            - ``z`` -- complex ball

            EXAMPLES::

                sage: CBF(0,1).elliptic_rf(CBF(-1/2,1), CBF(-1,-1))
                [1.469800396738515 +/- ...e-16] + [-0.2358791199824196 +/- ...e-17]*I"""
        def elliptic_rg(self, y, z) -> Any:
            """ComplexBall.elliptic_rg(self, y, z)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4875)

            Return the Carlson symmetric elliptic integral of the second kind evaluated
            at ``(self, y, z)``.

            INPUT:

            - ``y`` -- complex ball

            - ``z`` -- complex ball

            EXAMPLES::

                sage: CBF(0,1).elliptic_rg(CBF(-1/2,1), CBF(-1,-1))
                [0.1586786770922370 +/- ...e-17] + [0.2239733128130531 +/- ...e-17]*I"""
        def elliptic_rj(self, y, z, p) -> Any:
            """ComplexBall.elliptic_rj(self, y, z, p)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4899)

            Return the Carlson symmetric elliptic integral of the third kind evaluated
            at ``(self, y, z)``.

            INPUT:

            - ``y`` -- complex ball

            - ``z`` -- complex ball

            - ``p`` -- complex bamm

            EXAMPLES::

                sage: CBF(0,1).elliptic_rj(CBF(-1/2,1), CBF(-1,-1), CBF(2))
                [1.00438675628573...] + [-0.24516268343916...]*I"""
        @overload
        def elliptic_roots(self) -> Any:
            """ComplexBall.elliptic_roots(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4664)

            Return the lattice roots ``(e1, e2, e3)`` of `4 z^3 - g_2 z - g_3`.

            EXAMPLES::

                sage: e1, e2, e3 = CBF(0,1).elliptic_roots()
                sage: e1, e2, e3
                ([6.8751858180204 +/- ...e-14],
                 [+/- ...e-14],
                 [-6.8751858180204 +/- ...e-14])
                sage: g2, g3 = CBF(0,1).elliptic_invariants()
                sage: 4 * e1^3 - g2 * e1 - g3
                [+/- ...e-11]"""
        @overload
        def elliptic_roots(self) -> Any:
            """ComplexBall.elliptic_roots(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4664)

            Return the lattice roots ``(e1, e2, e3)`` of `4 z^3 - g_2 z - g_3`.

            EXAMPLES::

                sage: e1, e2, e3 = CBF(0,1).elliptic_roots()
                sage: e1, e2, e3
                ([6.8751858180204 +/- ...e-14],
                 [+/- ...e-14],
                 [-6.8751858180204 +/- ...e-14])
                sage: g2, g3 = CBF(0,1).elliptic_invariants()
                sage: 4 * e1^3 - g2 * e1 - g3
                [+/- ...e-11]"""
        def elliptic_sigma(self, tau) -> Any:
            """ComplexBall.elliptic_sigma(self, tau)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4946)

            Return the value of the Weierstrass sigma function at ``(self, tau)``.

            EXAMPLES::

            - ``tau`` -- a complex ball with positive imaginary part

            EXAMPLES::

                sage: CBF(1,1).elliptic_sigma(CBF(1,3))
                [-0.543073363596 +/- ...e-13] + [3.6357291186244 +/- ...e-14]*I"""
        def elliptic_zeta(self, tau) -> Any:
            """ComplexBall.elliptic_zeta(self, tau)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4926)

            Return the value of the Weierstrass zeta function at ``(self, tau)``.

            EXAMPLES::

            - ``tau`` -- a complex ball with positive imaginary part

            EXAMPLES::

                sage: CBF(1,1).elliptic_zeta(CBF(1,3))
                [3.2898676194970 +/- ...e-14] + [0.1365414361782 +/- ...e-14]*I"""
        @overload
        def erf(self) -> Any:
            """ComplexBall.erf(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4022)

            Return the error function with argument ``self``.

            EXAMPLES::

                sage: CBF(1, 1).erf()
                [1.316151281697947 +/- ...e-16] + [0.1904534692378347 +/- ...e-17]*I"""
        @overload
        def erf(self) -> Any:
            """ComplexBall.erf(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4022)

            Return the error function with argument ``self``.

            EXAMPLES::

                sage: CBF(1, 1).erf()
                [1.316151281697947 +/- ...e-16] + [0.1904534692378347 +/- ...e-17]*I"""
        @overload
        def erfc(self) -> Any:
            """ComplexBall.erfc(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4038)

            Compute the complementary error function with argument ``self``.

            EXAMPLES::

                sage: CBF(20).erfc() # abs tol 1e-190
                [5.39586561160790e-176 +/- 6.73e-191]
                sage: CBF(100, 100).erfc()
                [0.00065234366376858 +/- ...e-18] + [-0.00393572636292141 +/- ...e-18]*I"""
        @overload
        def erfc(self) -> Any:
            """ComplexBall.erfc(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4038)

            Compute the complementary error function with argument ``self``.

            EXAMPLES::

                sage: CBF(20).erfc() # abs tol 1e-190
                [5.39586561160790e-176 +/- 6.73e-191]
                sage: CBF(100, 100).erfc()
                [0.00065234366376858 +/- ...e-18] + [-0.00393572636292141 +/- ...e-18]*I"""
        @overload
        def erfc(self) -> Any:
            """ComplexBall.erfc(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4038)

            Compute the complementary error function with argument ``self``.

            EXAMPLES::

                sage: CBF(20).erfc() # abs tol 1e-190
                [5.39586561160790e-176 +/- 6.73e-191]
                sage: CBF(100, 100).erfc()
                [0.00065234366376858 +/- ...e-18] + [-0.00393572636292141 +/- ...e-18]*I"""
        @overload
        def exp(self) -> Any:
            """ComplexBall.exp(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3171)

            Return the exponential of this ball.

            .. SEEALSO:: :meth:`exppii`

            EXAMPLES::

                sage: CBF(i*pi).exp()                                                       # needs sage.symbolic
                [-1.00000000000000 +/- ...e-16] + [+/- ...e-16]*I"""
        @overload
        def exp(self) -> Any:
            """ComplexBall.exp(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3171)

            Return the exponential of this ball.

            .. SEEALSO:: :meth:`exppii`

            EXAMPLES::

                sage: CBF(i*pi).exp()                                                       # needs sage.symbolic
                [-1.00000000000000 +/- ...e-16] + [+/- ...e-16]*I"""
        def exp_integral_e(self, s) -> Any:
            """ComplexBall.exp_integral_e(self, s)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4240)

            Return the image of this ball by the generalized exponential integral
            with index ``s``.

            EXAMPLES::

                sage: CBF(1+i).exp_integral_e(1)
                [0.00028162445198 +/- ...e-15] + [-0.17932453503936 +/- ...e-15]*I
                sage: CBF(1+i).exp_integral_e(QQbar(i))
                [-0.10396361883964 +/- ...e-15] + [-0.16268401277783 +/- ...e-15]*I"""
        @overload
        def exppii(self) -> Any:
            """ComplexBall.exppii(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3188)

            Return ``exp(pi*i*self)``.

            EXAMPLES::

                sage: CBF(1/2).exppii()
                1.000000000000000*I
                sage: CBF(0, -1/pi).exppii()                                                # needs sage.symbolic
                [2.71828182845904 +/- ...e-15]"""
        @overload
        def exppii(self) -> Any:
            """ComplexBall.exppii(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3188)

            Return ``exp(pi*i*self)``.

            EXAMPLES::

                sage: CBF(1/2).exppii()
                1.000000000000000*I
                sage: CBF(0, -1/pi).exppii()                                                # needs sage.symbolic
                [2.71828182845904 +/- ...e-15]"""
        @overload
        def exppii(self) -> Any:
            """ComplexBall.exppii(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3188)

            Return ``exp(pi*i*self)``.

            EXAMPLES::

                sage: CBF(1/2).exppii()
                1.000000000000000*I
                sage: CBF(0, -1/pi).exppii()                                                # needs sage.symbolic
                [2.71828182845904 +/- ...e-15]"""
        @overload
        def gamma(self, z=...) -> Any:
            """ComplexBall.gamma(self, z=None)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3573)

            Return the image of this ball by the Euler Gamma function (if
            ``z = None``) or the incomplete Gamma function (otherwise).

            EXAMPLES::

                sage: CBF(1, 1).gamma() # abs tol 1e-15
                [0.498015668118356 +/- 1.26e-16] + [-0.1549498283018107 +/- 8.43e-17]*I
                sage: CBF(-1).gamma()
                nan
                sage: CBF(1, 1).gamma(0) # abs tol 1e-15
                [0.498015668118356 +/- 1.26e-16] + [-0.1549498283018107 +/- 8.43e-17]*I
                sage: CBF(1, 1).gamma(100)
                [-3.6143867454139e-45 +/- ...e-59] + [-3.7022961377791e-44 +/- ...e-58]*I
                sage: CBF(1, 1).gamma(CLF(i)) # abs tol 1e-14
                [0.328866841935004 +/- 7.07e-16] + [-0.189749450456210 +/- 9.05e-16]*I"""
        @overload
        def gamma(self) -> Any:
            """ComplexBall.gamma(self, z=None)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3573)

            Return the image of this ball by the Euler Gamma function (if
            ``z = None``) or the incomplete Gamma function (otherwise).

            EXAMPLES::

                sage: CBF(1, 1).gamma() # abs tol 1e-15
                [0.498015668118356 +/- 1.26e-16] + [-0.1549498283018107 +/- 8.43e-17]*I
                sage: CBF(-1).gamma()
                nan
                sage: CBF(1, 1).gamma(0) # abs tol 1e-15
                [0.498015668118356 +/- 1.26e-16] + [-0.1549498283018107 +/- 8.43e-17]*I
                sage: CBF(1, 1).gamma(100)
                [-3.6143867454139e-45 +/- ...e-59] + [-3.7022961377791e-44 +/- ...e-58]*I
                sage: CBF(1, 1).gamma(CLF(i)) # abs tol 1e-14
                [0.328866841935004 +/- 7.07e-16] + [-0.189749450456210 +/- 9.05e-16]*I"""
        @overload
        def gamma(self) -> Any:
            """ComplexBall.gamma(self, z=None)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3573)

            Return the image of this ball by the Euler Gamma function (if
            ``z = None``) or the incomplete Gamma function (otherwise).

            EXAMPLES::

                sage: CBF(1, 1).gamma() # abs tol 1e-15
                [0.498015668118356 +/- 1.26e-16] + [-0.1549498283018107 +/- 8.43e-17]*I
                sage: CBF(-1).gamma()
                nan
                sage: CBF(1, 1).gamma(0) # abs tol 1e-15
                [0.498015668118356 +/- 1.26e-16] + [-0.1549498283018107 +/- 8.43e-17]*I
                sage: CBF(1, 1).gamma(100)
                [-3.6143867454139e-45 +/- ...e-59] + [-3.7022961377791e-44 +/- ...e-58]*I
                sage: CBF(1, 1).gamma(CLF(i)) # abs tol 1e-14
                [0.328866841935004 +/- 7.07e-16] + [-0.189749450456210 +/- 9.05e-16]*I"""
        def gamma_inc(self, *args, **kwargs):
            """ComplexBall.gamma(self, z=None)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3573)

            Return the image of this ball by the Euler Gamma function (if
            ``z = None``) or the incomplete Gamma function (otherwise).

            EXAMPLES::

                sage: CBF(1, 1).gamma() # abs tol 1e-15
                [0.498015668118356 +/- 1.26e-16] + [-0.1549498283018107 +/- 8.43e-17]*I
                sage: CBF(-1).gamma()
                nan
                sage: CBF(1, 1).gamma(0) # abs tol 1e-15
                [0.498015668118356 +/- 1.26e-16] + [-0.1549498283018107 +/- 8.43e-17]*I
                sage: CBF(1, 1).gamma(100)
                [-3.6143867454139e-45 +/- ...e-59] + [-3.7022961377791e-44 +/- ...e-58]*I
                sage: CBF(1, 1).gamma(CLF(i)) # abs tol 1e-14
                [0.328866841935004 +/- 7.07e-16] + [-0.189749450456210 +/- 9.05e-16]*I"""
        def gegenbauer_C(self, n, m) -> Any:
            """ComplexBall.gegenbauer_C(self, n, m)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 5024)

            Return the Gegenbauer polynomial (or function) `C_n^m(z)`
            evaluated at ``self``.

            EXAMPLES::

                sage: CBF(-10).gegenbauer_C(7, 1/2)
                [-263813415.6250000 +/- ...e-8]"""
        def hermite_H(self, n) -> Any:
            """ComplexBall.hermite_H(self, n)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 5066)

            Return the Hermite function (or polynomial) of order ``n``
            evaluated at ``self``.

            EXAMPLES::

                sage: CBF(10).hermite_H(1)
                20.00000000000000
                sage: CBF(10).hermite_H(30)
                [8.0574670961707e+37 +/- ...e+23]"""
        def hypergeometric(self, a, b, boolregularized=...) -> Any:
            """ComplexBall.hypergeometric(self, a, b, bool regularized=False)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3857)

            Return the generalized hypergeometric function of ``self``.

            INPUT:

            - ``a`` -- upper parameters; list of complex numbers that coerce into
              this ball's parent

            - ``b`` -- lower parameters; list of complex numbers that coerce into
              this ball's parent

            - ``regularized`` -- if ``True``, the regularized generalized
              hypergeometric function is computed

            OUTPUT: the generalized hypergeometric function defined by

            .. MATH::

                {}_pF_q(a_1,\\ldots,a_p;b_1,\\ldots,b_q;z)
                = \\sum_{k=0}^\\infty \\frac{(a_1)_k\\dots(a_p)_k}{(b_1)_k\\dots(b_q)_k} \\frac {z^k} {k!}

            extended using analytic continuation or regularization when the sum
            does not converge.

            The regularized generalized hypergeometric function

            .. MATH::

                {}_pF_q(a_1,\\ldots,a_p;b_1,\\ldots,b_q;z)
                = \\sum_{k=0}^\\infty \\frac{(a_1)_k\\dots(a_p)_k}{\\Gamma(b_1+k)\\dots\\Gamma(b_q+k)} \\frac {z^k} {k!}

            is well-defined even when the lower parameters are nonpositive
            integers. Currently, this is only supported for some `p` and `q`.

            EXAMPLES::

                sage: CBF(1, pi/2).hypergeometric([], [])                                   # needs sage.symbolic
                [+/- ...e-16] + [2.71828182845904 +/- ...e-15]*I

                sage: CBF(1, pi).hypergeometric([1/4], [1/4])                               # needs sage.symbolic
                [-2.7182818284590 +/- ...e-14] + [+/- ...e-14]*I

                sage: CBF(1000, 1000).hypergeometric([10], [AA(sqrt(2))])                   # needs sage.symbolic
                [9.79300951360e+454 +/- ...e+442] + [5.522579106816e+455 +/- ...e+442]*I
                sage: CBF(1000, 1000).hypergeometric([100], [AA(sqrt(2))])                  # needs sage.symbolic
                [1.27967355557e+590 +/- ...e+578] + [-9.32333491987e+590 +/- ...e+578]*I

                sage: CBF(0, 1).hypergeometric([], [1/2, 1/3, 1/4])
                [-3.7991962344383 +/- ...e-14] + [23.878097177805 +/- ...e-13]*I

                sage: CBF(0).hypergeometric([1], [])
                1.000000000000000
                sage: CBF(1, 1).hypergeometric([1], [])
                1.000000000000000*I

                sage: CBF(2+3*I).hypergeometric([1/4,1/3],[1/2]) # abs tol 1e-14
                [0.7871684267473 +/- 6.79e-14] + [0.2749254173721 +/- 8.82e-14]*I
                sage: CBF(2+3*I).hypergeometric([1/4,1/3],[1/2],regularized=True)
                [0.4441122268685 +/- 3...e-14] + [0.1551100567338 +/- 5...e-14]*I

                sage: CBF(5).hypergeometric([2,3], [-5])
                nan + nan*I
                sage: CBF(5).hypergeometric([2,3], [-5], regularized=True)
                [5106.925964355 +/- ...e-10]

                sage: CBF(2016).hypergeometric([], [2/3]) # abs tol 1e+26
                [2.0256426923278e+38 +/- 9.59e+24]
                sage: CBF(-2016).hypergeometric([], [2/3], regularized=True)
                [-0.0005428550847 +/- ...e-14]

                sage: CBF(-7).hypergeometric([4], [])
                0.0002441406250000000

                sage: CBF(0, 3).hypergeometric([CBF(1,1)], [-4], regularized=True)
                [239.514000752841 +/- ...e-13] + [105.175157349015 +/- ...e-13]*I

            TESTS::

                sage: CBF(0, 1).hypergeometric([QQbar(sqrt(2)), RLF(pi)], [1r, 1/2])        # needs sage.symbolic
                [-8.7029449215408 +/- ...e-14] + [-0.8499070546106 +/- ...e-14]*I"""
        def hypergeometric_U(self, a, b) -> Any:
            """ComplexBall.hypergeometric_U(self, a, b)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4002)

            Return the Tricomi confluent hypergeometric function U(a, b, self) of
            this ball.

            EXAMPLES::

                sage: CBF(1000, 1000).hypergeometric_U(RLF(pi), -100)                       # needs sage.symbolic
                [-7.261605907166e-11 +/- ...e-24] + [-7.928136216391e-11 +/- ...e-24]*I
                sage: CBF(1000, 1000).hypergeometric_U(0, -100)
                1.000000000000000"""
        def identical(self, ComplexBallother) -> Any:
            """ComplexBall.identical(self, ComplexBall other)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 2496)

            Return whether ``self`` and ``other`` represent the same ball.

            INPUT:

            - ``other`` -- a :class:`ComplexBall`

            OUTPUT:

            Return ``True`` iff ``self`` and ``other`` are equal as sets, i.e. if their
            real and imaginary parts each have the same midpoint and radius.

            Note that this is not the same thing as testing whether both ``self``
            and ``other`` certainly represent the complex real number, unless
            either ``self`` or ``other`` is exact (and neither contains NaN). To
            test whether both operands might represent the same mathematical
            quantity, use :meth:`overlaps` or ``in``, depending on the
            circumstance.

            EXAMPLES::

                sage: CBF(1, 1/3).identical(1 + CBF(0, 1)/3)
                True
                sage: CBF(1, 1).identical(1 + CBF(0, 1/3)*3)
                False"""
        @overload
        def imag(self) -> RealBall:
            """ComplexBall.imag(self) -> RealBall

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 1894)

            Return the imaginary part of this ball.

            OUTPUT: a :class:`~sage.rings.real_arb.RealBall`

            EXAMPLES::

               sage: a = CBF(1/3, 1/5)
               sage: a.imag()
               [0.2000000000000000 +/- ...e-17]
               sage: a.imag().parent()
               Real ball field with 53 bits of precision"""
        @overload
        def imag(self) -> Any:
            """ComplexBall.imag(self) -> RealBall

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 1894)

            Return the imaginary part of this ball.

            OUTPUT: a :class:`~sage.rings.real_arb.RealBall`

            EXAMPLES::

               sage: a = CBF(1/3, 1/5)
               sage: a.imag()
               [0.2000000000000000 +/- ...e-17]
               sage: a.imag().parent()
               Real ball field with 53 bits of precision"""
        @overload
        def imag(self) -> Any:
            """ComplexBall.imag(self) -> RealBall

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 1894)

            Return the imaginary part of this ball.

            OUTPUT: a :class:`~sage.rings.real_arb.RealBall`

            EXAMPLES::

               sage: a = CBF(1/3, 1/5)
               sage: a.imag()
               [0.2000000000000000 +/- ...e-17]
               sage: a.imag().parent()
               Real ball field with 53 bits of precision"""
        @overload
        def is_NaN(self) -> Any:
            """ComplexBall.is_NaN(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 2272)

            Return ``True`` iff either the real or the imaginary part
            is not-a-number.

            EXAMPLES::

                sage: CBF(NaN).is_NaN()                                                     # needs sage.symbolic
                True
                sage: CBF(-5).gamma().is_NaN()
                True
                sage: CBF(oo).is_NaN()
                False
                sage: CBF(42+I).is_NaN()
                False"""
        @overload
        def is_NaN(self) -> Any:
            """ComplexBall.is_NaN(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 2272)

            Return ``True`` iff either the real or the imaginary part
            is not-a-number.

            EXAMPLES::

                sage: CBF(NaN).is_NaN()                                                     # needs sage.symbolic
                True
                sage: CBF(-5).gamma().is_NaN()
                True
                sage: CBF(oo).is_NaN()
                False
                sage: CBF(42+I).is_NaN()
                False"""
        @overload
        def is_NaN(self) -> Any:
            """ComplexBall.is_NaN(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 2272)

            Return ``True`` iff either the real or the imaginary part
            is not-a-number.

            EXAMPLES::

                sage: CBF(NaN).is_NaN()                                                     # needs sage.symbolic
                True
                sage: CBF(-5).gamma().is_NaN()
                True
                sage: CBF(oo).is_NaN()
                False
                sage: CBF(42+I).is_NaN()
                False"""
        @overload
        def is_NaN(self) -> Any:
            """ComplexBall.is_NaN(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 2272)

            Return ``True`` iff either the real or the imaginary part
            is not-a-number.

            EXAMPLES::

                sage: CBF(NaN).is_NaN()                                                     # needs sage.symbolic
                True
                sage: CBF(-5).gamma().is_NaN()
                True
                sage: CBF(oo).is_NaN()
                False
                sage: CBF(42+I).is_NaN()
                False"""
        @overload
        def is_NaN(self) -> Any:
            """ComplexBall.is_NaN(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 2272)

            Return ``True`` iff either the real or the imaginary part
            is not-a-number.

            EXAMPLES::

                sage: CBF(NaN).is_NaN()                                                     # needs sage.symbolic
                True
                sage: CBF(-5).gamma().is_NaN()
                True
                sage: CBF(oo).is_NaN()
                False
                sage: CBF(42+I).is_NaN()
                False"""
        @overload
        def is_exact(self) -> Any:
            """ComplexBall.is_exact(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 2361)

            Return ``True`` iff the radius of this ball is zero.

            EXAMPLES::

                sage: CBF(1).is_exact()
                True
                sage: CBF(1/3, 1/3).is_exact()
                False"""
        @overload
        def is_exact(self) -> Any:
            """ComplexBall.is_exact(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 2361)

            Return ``True`` iff the radius of this ball is zero.

            EXAMPLES::

                sage: CBF(1).is_exact()
                True
                sage: CBF(1/3, 1/3).is_exact()
                False"""
        @overload
        def is_exact(self) -> Any:
            """ComplexBall.is_exact(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 2361)

            Return ``True`` iff the radius of this ball is zero.

            EXAMPLES::

                sage: CBF(1).is_exact()
                True
                sage: CBF(1/3, 1/3).is_exact()
                False"""
        @overload
        def is_nonzero(self) -> Any:
            """ComplexBall.is_nonzero(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 2306)

            Return ``True`` iff zero is not contained in the interval represented
            by this ball.

            .. NOTE::

                This method is not the negation of :meth:`is_zero`: it only
                returns ``True`` if zero is known not to be contained in the ball.

                Use ``bool(b)`` (or, equivalently, ``not b.is_zero()``) to check if
                a ball\xa0``b`` **may** represent a nonzero number (for instance, to
                determine the “degree” of a polynomial with ball coefficients).

            EXAMPLES::

                sage: CBF(pi, 1/3).is_nonzero()                                             # needs sage.symbolic
                True
                sage: CBF(RIF(-0.5, 0.5), 1/3).is_nonzero()
                True
                sage: CBF(1/3, RIF(-0.5, 0.5)).is_nonzero()
                True
                sage: CBF(RIF(-0.5, 0.5), RIF(-0.5, 0.5)).is_nonzero()
                False

            .. SEEALSO:: :meth:`is_zero`"""
        @overload
        def is_nonzero(self) -> Any:
            """ComplexBall.is_nonzero(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 2306)

            Return ``True`` iff zero is not contained in the interval represented
            by this ball.

            .. NOTE::

                This method is not the negation of :meth:`is_zero`: it only
                returns ``True`` if zero is known not to be contained in the ball.

                Use ``bool(b)`` (or, equivalently, ``not b.is_zero()``) to check if
                a ball\xa0``b`` **may** represent a nonzero number (for instance, to
                determine the “degree” of a polynomial with ball coefficients).

            EXAMPLES::

                sage: CBF(pi, 1/3).is_nonzero()                                             # needs sage.symbolic
                True
                sage: CBF(RIF(-0.5, 0.5), 1/3).is_nonzero()
                True
                sage: CBF(1/3, RIF(-0.5, 0.5)).is_nonzero()
                True
                sage: CBF(RIF(-0.5, 0.5), RIF(-0.5, 0.5)).is_nonzero()
                False

            .. SEEALSO:: :meth:`is_zero`"""
        @overload
        def is_nonzero(self) -> Any:
            """ComplexBall.is_nonzero(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 2306)

            Return ``True`` iff zero is not contained in the interval represented
            by this ball.

            .. NOTE::

                This method is not the negation of :meth:`is_zero`: it only
                returns ``True`` if zero is known not to be contained in the ball.

                Use ``bool(b)`` (or, equivalently, ``not b.is_zero()``) to check if
                a ball\xa0``b`` **may** represent a nonzero number (for instance, to
                determine the “degree” of a polynomial with ball coefficients).

            EXAMPLES::

                sage: CBF(pi, 1/3).is_nonzero()                                             # needs sage.symbolic
                True
                sage: CBF(RIF(-0.5, 0.5), 1/3).is_nonzero()
                True
                sage: CBF(1/3, RIF(-0.5, 0.5)).is_nonzero()
                True
                sage: CBF(RIF(-0.5, 0.5), RIF(-0.5, 0.5)).is_nonzero()
                False

            .. SEEALSO:: :meth:`is_zero`"""
        @overload
        def is_nonzero(self) -> Any:
            """ComplexBall.is_nonzero(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 2306)

            Return ``True`` iff zero is not contained in the interval represented
            by this ball.

            .. NOTE::

                This method is not the negation of :meth:`is_zero`: it only
                returns ``True`` if zero is known not to be contained in the ball.

                Use ``bool(b)`` (or, equivalently, ``not b.is_zero()``) to check if
                a ball\xa0``b`` **may** represent a nonzero number (for instance, to
                determine the “degree” of a polynomial with ball coefficients).

            EXAMPLES::

                sage: CBF(pi, 1/3).is_nonzero()                                             # needs sage.symbolic
                True
                sage: CBF(RIF(-0.5, 0.5), 1/3).is_nonzero()
                True
                sage: CBF(1/3, RIF(-0.5, 0.5)).is_nonzero()
                True
                sage: CBF(RIF(-0.5, 0.5), RIF(-0.5, 0.5)).is_nonzero()
                False

            .. SEEALSO:: :meth:`is_zero`"""
        @overload
        def is_nonzero(self) -> Any:
            """ComplexBall.is_nonzero(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 2306)

            Return ``True`` iff zero is not contained in the interval represented
            by this ball.

            .. NOTE::

                This method is not the negation of :meth:`is_zero`: it only
                returns ``True`` if zero is known not to be contained in the ball.

                Use ``bool(b)`` (or, equivalently, ``not b.is_zero()``) to check if
                a ball\xa0``b`` **may** represent a nonzero number (for instance, to
                determine the “degree” of a polynomial with ball coefficients).

            EXAMPLES::

                sage: CBF(pi, 1/3).is_nonzero()                                             # needs sage.symbolic
                True
                sage: CBF(RIF(-0.5, 0.5), 1/3).is_nonzero()
                True
                sage: CBF(1/3, RIF(-0.5, 0.5)).is_nonzero()
                True
                sage: CBF(RIF(-0.5, 0.5), RIF(-0.5, 0.5)).is_nonzero()
                False

            .. SEEALSO:: :meth:`is_zero`"""
        @overload
        def is_real(self) -> Any:
            """ComplexBall.is_real(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 2374)

            Return ``True`` iff the imaginary part of this ball is exactly zero.

            EXAMPLES::

                sage: CBF(1/3, 0).is_real()
                True
                sage: (CBF(i/3) - CBF(1, 1/3)).is_real()
                False
                sage: CBF('inf').is_real()
                True"""
        @overload
        def is_real(self) -> Any:
            """ComplexBall.is_real(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 2374)

            Return ``True`` iff the imaginary part of this ball is exactly zero.

            EXAMPLES::

                sage: CBF(1/3, 0).is_real()
                True
                sage: (CBF(i/3) - CBF(1, 1/3)).is_real()
                False
                sage: CBF('inf').is_real()
                True"""
        @overload
        def is_real(self) -> Any:
            """ComplexBall.is_real(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 2374)

            Return ``True`` iff the imaginary part of this ball is exactly zero.

            EXAMPLES::

                sage: CBF(1/3, 0).is_real()
                True
                sage: (CBF(i/3) - CBF(1, 1/3)).is_real()
                False
                sage: CBF('inf').is_real()
                True"""
        @overload
        def is_real(self) -> Any:
            """ComplexBall.is_real(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 2374)

            Return ``True`` iff the imaginary part of this ball is exactly zero.

            EXAMPLES::

                sage: CBF(1/3, 0).is_real()
                True
                sage: (CBF(i/3) - CBF(1, 1/3)).is_real()
                False
                sage: CBF('inf').is_real()
                True"""
        @overload
        def is_zero(self) -> Any:
            """ComplexBall.is_zero(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 2291)

            Return ``True`` iff the midpoint and radius of this ball are both zero.

            EXAMPLES::

                sage: CBF(0).is_zero()
                True
                sage: CBF(RIF(-0.5, 0.5)).is_zero()
                False

            .. SEEALSO:: :meth:`is_nonzero`"""
        @overload
        def is_zero(self) -> Any:
            """ComplexBall.is_zero(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 2291)

            Return ``True`` iff the midpoint and radius of this ball are both zero.

            EXAMPLES::

                sage: CBF(0).is_zero()
                True
                sage: CBF(RIF(-0.5, 0.5)).is_zero()
                False

            .. SEEALSO:: :meth:`is_nonzero`"""
        @overload
        def is_zero(self) -> Any:
            """ComplexBall.is_zero(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 2291)

            Return ``True`` iff the midpoint and radius of this ball are both zero.

            EXAMPLES::

                sage: CBF(0).is_zero()
                True
                sage: CBF(RIF(-0.5, 0.5)).is_zero()
                False

            .. SEEALSO:: :meth:`is_nonzero`"""
        def jacobi_P(self, n, a, b) -> Any:
            """ComplexBall.jacobi_P(self, n, a, b)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 5004)

            Return the Jacobi polynomial (or function) `P_n^{(a,b)}(z)`
            evaluated at ``self``.

            EXAMPLES::

                sage: CBF(5,-6).jacobi_P(8, CBF(1,2), CBF(2,3))
                [-920983000.45982 +/- ...e-6] + [6069919969.92857 +/- ...e-6]*I"""
        def jacobi_theta(self, tau) -> Any:
            """ComplexBall.jacobi_theta(self, tau)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4432)

            Return the four Jacobi theta functions evaluated at the argument
            ``self`` (representing `z`) and the parameter ``tau`` which should lie
            in the upper half plane.

            The following definitions are used:

            .. MATH::

                \\theta_1(z,\\tau) = 2 q_{1/4} \\sum_{n=0}^{\\infty} (-1)^n q^{n(n+1)} \\sin((2n+1) \\pi z)

                \\theta_2(z,\\tau) = 2 q_{1/4} \\sum_{n=0}^{\\infty} q^{n(n+1)} \\cos((2n+1) \\pi z)

                \\theta_3(z,\\tau) = 1 + 2 \\sum_{n=1}^{\\infty} q^{n^2} \\cos(2n \\pi z)

                \\theta_4(z,\\tau) = 1 + 2 \\sum_{n=1}^{\\infty} (-1)^n q^{n^2} \\cos(2n \\pi z)

            where `q = \\exp(\\pi i \\tau)` and `q_{1/4} = \\exp(\\pi i \\tau / 4)`.
            Note that `z` is multiplied by `\\pi`; some authors omit this factor.

            EXAMPLES::

                sage: CBF(3,-1/2).jacobi_theta(CBF(1/4,2))
                ([-0.186580562274757 +/- ...e-16] + [0.93841744788594 +/- ...e-15]*I,
                 [-1.02315311037951 +/- ...e-15] + [-0.203600094532010 +/- ...e-16]*I,
                 [1.030613911309632 +/- ...e-16] + [0.030613917822067 +/- ...e-16]*I,
                 [0.969386075665498 +/- ...e-16] + [-0.030613917822067 +/- ...e-16]*I)

                sage: CBF(3,-1/2).jacobi_theta(CBF(1/4,-2))
                (nan + nan*I, nan + nan*I, nan + nan*I, nan + nan*I)

                sage: CBF(0).jacobi_theta(CBF(0,1))
                (0,
                 [0.913579138156117 +/- ...e-16],
                 [1.086434811213308 +/- ...e-16],
                 [0.913579138156117 +/- ...e-16])"""
        def laguerre_L(self, n, m=...) -> Any:
            """ComplexBall.laguerre_L(self, n, m=0)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 5043)

            Return the Laguerre polynomial (or function) `L_n^m(z)`
            evaluated at ``self``.

            EXAMPLES::

                sage: CBF(10).laguerre_L(3)
                [-45.6666666666666 +/- ...e-14]
                sage: CBF(10).laguerre_L(3, 2)
                [-6.666666666667 +/- ...e-13]
                sage: CBF(5,7).laguerre_L(CBF(2,3), CBF(1,-2)) # abs tol 1e-9
                [5515.3150302713 +/- 5.02e-11] + [-12386.9428452714 +/- 6.21e-11]*I"""
        @overload
        def lambert_w(self, branch=...) -> Any:
            """ComplexBall.lambert_w(self, branch=0)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3742)

            Return the image of this ball by the specified branch of the Lambert\xa0W
            function.

            EXAMPLES::

                sage: CBF(1 + I).lambert_w()
                [0.6569660692304...] + [0.3254503394134...]*I
                sage: CBF(1 + I).lambert_w(2)
                [-2.1208839379437...] + [11.600137110774...]*I
                sage: CBF(1 + I).lambert_w(2^100)
                [-70.806021532123...] + [7.9648836259913...]*I"""
        @overload
        def lambert_w(self) -> Any:
            """ComplexBall.lambert_w(self, branch=0)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3742)

            Return the image of this ball by the specified branch of the Lambert\xa0W
            function.

            EXAMPLES::

                sage: CBF(1 + I).lambert_w()
                [0.6569660692304...] + [0.3254503394134...]*I
                sage: CBF(1 + I).lambert_w(2)
                [-2.1208839379437...] + [11.600137110774...]*I
                sage: CBF(1 + I).lambert_w(2^100)
                [-70.806021532123...] + [7.9648836259913...]*I"""
        def legendre_P(self, n, m=..., type=...) -> Any:
            '''ComplexBall.legendre_P(self, n, m=0, type=2)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 5085)

            Return the Legendre function of the first kind `P_n^m(z)`
            evaluated at ``self``.

            The ``type`` parameter can be either 2 or 3. This selects between
            different branch cut conventions. The definitions of the "type 2"
            and "type 3" functions are the same as those used by *Mathematica*
            and *mpmath*.

            EXAMPLES::

                sage: CBF(1/2).legendre_P(5)
                [0.0898437500000000 +/- 7...e-17]
                sage: CBF(1,2).legendre_P(CBF(2,3), CBF(0,1))
                [0.10996180744364 +/- ...e-15] + [0.14312767804055 +/- ...e-15]*I
                sage: CBF(-10).legendre_P(5, 325/100)
                [-22104403.487377 +/- ...e-7] + [53364750.687392 +/- ...e-7]*I
                sage: CBF(-10).legendre_P(5, 325/100, type=3)
                [-57761589.914581 +/- ...e-7] + [+/- ...e-7]*I'''
        def legendre_Q(self, n, m=..., type=...) -> Any:
            '''ComplexBall.legendre_Q(self, n, m=0, type=2)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 5118)

            Return the Legendre function of the second kind `Q_n^m(z)`
            evaluated at ``self``.

            The ``type`` parameter can be either 2 or 3. This selects between
            different branch cut conventions. The definitions of the "type 2"
            and "type 3" functions are the same as those used by *Mathematica*
            and *mpmath*.

            EXAMPLES::

                sage: CBF(1/2).legendre_Q(5)
                [0.55508089057168 +/- ...e-15]
                sage: CBF(1,2).legendre_Q(CBF(2,3), CBF(0,1))
                [0.167678710 +/- ...e-10] + [-0.161558598 +/- ...e-10]*I
                sage: CBF(-10).legendre_Q(5, 325/100)
                [-83825154.36008 +/- ...e-6] + [-34721515.80396 +/- ...e-6]*I
                sage: CBF(-10).legendre_Q(5, 325/100, type=3)
                [-4.797306921692e-6 +/- ...e-19] + [-4.797306921692e-6 +/- ...e-19]*I'''
        @overload
        def li(self, booloffset=...) -> Any:
            """ComplexBall.li(self, bool offset=False)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4377)

            Return the logarithmic integral with argument ``self``.

            If ``offset`` is True, return the offset logarithmic integral.

            EXAMPLES::

                sage: CBF(1, 1).li()  # abs tol 6e-15
                [0.61391166922120 +/- 6.23e-15] + [2.05958421419258 +/- 5.59e-15]*I
                sage: CBF(0).li()
                0
                sage: CBF(0).li(offset=True)
                [-1.045163780117493 +/- ...e-16]
                sage: li(0).n()                                                             # needs sage.symbolic
                0.000000000000000
                sage: Li(0).n()                                                             # needs sage.symbolic
                -1.04516378011749

            TESTS::

                sage: CBF(li(0))                                                            # needs sage.symbolic
                0
                sage: CBF(Li(0))                                                            # needs sage.symbolic
                [-1.04516378011749...]"""
        @overload
        def li(self) -> Any:
            """ComplexBall.li(self, bool offset=False)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4377)

            Return the logarithmic integral with argument ``self``.

            If ``offset`` is True, return the offset logarithmic integral.

            EXAMPLES::

                sage: CBF(1, 1).li()  # abs tol 6e-15
                [0.61391166922120 +/- 6.23e-15] + [2.05958421419258 +/- 5.59e-15]*I
                sage: CBF(0).li()
                0
                sage: CBF(0).li(offset=True)
                [-1.045163780117493 +/- ...e-16]
                sage: li(0).n()                                                             # needs sage.symbolic
                0.000000000000000
                sage: Li(0).n()                                                             # needs sage.symbolic
                -1.04516378011749

            TESTS::

                sage: CBF(li(0))                                                            # needs sage.symbolic
                0
                sage: CBF(Li(0))                                                            # needs sage.symbolic
                [-1.04516378011749...]"""
        @overload
        def li(self) -> Any:
            """ComplexBall.li(self, bool offset=False)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4377)

            Return the logarithmic integral with argument ``self``.

            If ``offset`` is True, return the offset logarithmic integral.

            EXAMPLES::

                sage: CBF(1, 1).li()  # abs tol 6e-15
                [0.61391166922120 +/- 6.23e-15] + [2.05958421419258 +/- 5.59e-15]*I
                sage: CBF(0).li()
                0
                sage: CBF(0).li(offset=True)
                [-1.045163780117493 +/- ...e-16]
                sage: li(0).n()                                                             # needs sage.symbolic
                0.000000000000000
                sage: Li(0).n()                                                             # needs sage.symbolic
                -1.04516378011749

            TESTS::

                sage: CBF(li(0))                                                            # needs sage.symbolic
                0
                sage: CBF(Li(0))                                                            # needs sage.symbolic
                [-1.04516378011749...]"""
        @overload
        def li(self, offset=...) -> Any:
            """ComplexBall.li(self, bool offset=False)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4377)

            Return the logarithmic integral with argument ``self``.

            If ``offset`` is True, return the offset logarithmic integral.

            EXAMPLES::

                sage: CBF(1, 1).li()  # abs tol 6e-15
                [0.61391166922120 +/- 6.23e-15] + [2.05958421419258 +/- 5.59e-15]*I
                sage: CBF(0).li()
                0
                sage: CBF(0).li(offset=True)
                [-1.045163780117493 +/- ...e-16]
                sage: li(0).n()                                                             # needs sage.symbolic
                0.000000000000000
                sage: Li(0).n()                                                             # needs sage.symbolic
                -1.04516378011749

            TESTS::

                sage: CBF(li(0))                                                            # needs sage.symbolic
                0
                sage: CBF(Li(0))                                                            # needs sage.symbolic
                [-1.04516378011749...]"""
        @overload
        def log(self, base=..., analytic=...) -> Any:
            """ComplexBall.log(self, base=None, analytic=False)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3081)

            General logarithm (principal branch).

            INPUT:

            - ``base`` -- (optional) complex ball or number; if ``None``, return
              the principal branch of the natural logarithm ``ln(self)``,
              otherwise, return the general logarithm ``ln(self)/ln(base)``

            - ``analytic`` -- boolean (default: ``False``); if ``True``, return an
              indeterminate (not-a-number) value when the input ball touches
              the branch cut (with respect to ``self``)

            EXAMPLES::

                sage: CBF(2*i).log()
                [0.693147180559945 +/- ...e-16] + [1.570796326794897 +/- ...e-16]*I
                sage: CBF(-1).log()
                [3.141592653589793 +/- ...e-16]*I

                sage: CBF(2*i).log(2)
                [1.000000000000000 +/- ...e-16] + [2.26618007091360 +/- ...e-15]*I
                sage: CBF(2*i).log(CBF(i))
                [1.000000000000000 +/- ...e-16] + [-0.441271200305303 +/- ...e-16]*I

                sage: CBF('inf').log()
                [+/- inf]
                sage: CBF(2).log(0)
                nan + nan*I

                sage: CBF(-1).log(2)
                [4.53236014182719 +/- ...e-15]*I
                sage: CBF(-1).log(2, analytic=True)
                nan + nan*I
                sage: CBF(-1, RBF(0, rad=.1r)).log(analytic=False)
                [+/- ...e-3] + [+/- 3.15]*I"""
        @overload
        def log(self) -> Any:
            """ComplexBall.log(self, base=None, analytic=False)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3081)

            General logarithm (principal branch).

            INPUT:

            - ``base`` -- (optional) complex ball or number; if ``None``, return
              the principal branch of the natural logarithm ``ln(self)``,
              otherwise, return the general logarithm ``ln(self)/ln(base)``

            - ``analytic`` -- boolean (default: ``False``); if ``True``, return an
              indeterminate (not-a-number) value when the input ball touches
              the branch cut (with respect to ``self``)

            EXAMPLES::

                sage: CBF(2*i).log()
                [0.693147180559945 +/- ...e-16] + [1.570796326794897 +/- ...e-16]*I
                sage: CBF(-1).log()
                [3.141592653589793 +/- ...e-16]*I

                sage: CBF(2*i).log(2)
                [1.000000000000000 +/- ...e-16] + [2.26618007091360 +/- ...e-15]*I
                sage: CBF(2*i).log(CBF(i))
                [1.000000000000000 +/- ...e-16] + [-0.441271200305303 +/- ...e-16]*I

                sage: CBF('inf').log()
                [+/- inf]
                sage: CBF(2).log(0)
                nan + nan*I

                sage: CBF(-1).log(2)
                [4.53236014182719 +/- ...e-15]*I
                sage: CBF(-1).log(2, analytic=True)
                nan + nan*I
                sage: CBF(-1, RBF(0, rad=.1r)).log(analytic=False)
                [+/- ...e-3] + [+/- 3.15]*I"""
        @overload
        def log(self) -> Any:
            """ComplexBall.log(self, base=None, analytic=False)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3081)

            General logarithm (principal branch).

            INPUT:

            - ``base`` -- (optional) complex ball or number; if ``None``, return
              the principal branch of the natural logarithm ``ln(self)``,
              otherwise, return the general logarithm ``ln(self)/ln(base)``

            - ``analytic`` -- boolean (default: ``False``); if ``True``, return an
              indeterminate (not-a-number) value when the input ball touches
              the branch cut (with respect to ``self``)

            EXAMPLES::

                sage: CBF(2*i).log()
                [0.693147180559945 +/- ...e-16] + [1.570796326794897 +/- ...e-16]*I
                sage: CBF(-1).log()
                [3.141592653589793 +/- ...e-16]*I

                sage: CBF(2*i).log(2)
                [1.000000000000000 +/- ...e-16] + [2.26618007091360 +/- ...e-15]*I
                sage: CBF(2*i).log(CBF(i))
                [1.000000000000000 +/- ...e-16] + [-0.441271200305303 +/- ...e-16]*I

                sage: CBF('inf').log()
                [+/- inf]
                sage: CBF(2).log(0)
                nan + nan*I

                sage: CBF(-1).log(2)
                [4.53236014182719 +/- ...e-15]*I
                sage: CBF(-1).log(2, analytic=True)
                nan + nan*I
                sage: CBF(-1, RBF(0, rad=.1r)).log(analytic=False)
                [+/- ...e-3] + [+/- 3.15]*I"""
        @overload
        def log(self) -> Any:
            """ComplexBall.log(self, base=None, analytic=False)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3081)

            General logarithm (principal branch).

            INPUT:

            - ``base`` -- (optional) complex ball or number; if ``None``, return
              the principal branch of the natural logarithm ``ln(self)``,
              otherwise, return the general logarithm ``ln(self)/ln(base)``

            - ``analytic`` -- boolean (default: ``False``); if ``True``, return an
              indeterminate (not-a-number) value when the input ball touches
              the branch cut (with respect to ``self``)

            EXAMPLES::

                sage: CBF(2*i).log()
                [0.693147180559945 +/- ...e-16] + [1.570796326794897 +/- ...e-16]*I
                sage: CBF(-1).log()
                [3.141592653589793 +/- ...e-16]*I

                sage: CBF(2*i).log(2)
                [1.000000000000000 +/- ...e-16] + [2.26618007091360 +/- ...e-15]*I
                sage: CBF(2*i).log(CBF(i))
                [1.000000000000000 +/- ...e-16] + [-0.441271200305303 +/- ...e-16]*I

                sage: CBF('inf').log()
                [+/- inf]
                sage: CBF(2).log(0)
                nan + nan*I

                sage: CBF(-1).log(2)
                [4.53236014182719 +/- ...e-15]*I
                sage: CBF(-1).log(2, analytic=True)
                nan + nan*I
                sage: CBF(-1, RBF(0, rad=.1r)).log(analytic=False)
                [+/- ...e-3] + [+/- 3.15]*I"""
        @overload
        def log(self, analytic=...) -> Any:
            """ComplexBall.log(self, base=None, analytic=False)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3081)

            General logarithm (principal branch).

            INPUT:

            - ``base`` -- (optional) complex ball or number; if ``None``, return
              the principal branch of the natural logarithm ``ln(self)``,
              otherwise, return the general logarithm ``ln(self)/ln(base)``

            - ``analytic`` -- boolean (default: ``False``); if ``True``, return an
              indeterminate (not-a-number) value when the input ball touches
              the branch cut (with respect to ``self``)

            EXAMPLES::

                sage: CBF(2*i).log()
                [0.693147180559945 +/- ...e-16] + [1.570796326794897 +/- ...e-16]*I
                sage: CBF(-1).log()
                [3.141592653589793 +/- ...e-16]*I

                sage: CBF(2*i).log(2)
                [1.000000000000000 +/- ...e-16] + [2.26618007091360 +/- ...e-15]*I
                sage: CBF(2*i).log(CBF(i))
                [1.000000000000000 +/- ...e-16] + [-0.441271200305303 +/- ...e-16]*I

                sage: CBF('inf').log()
                [+/- inf]
                sage: CBF(2).log(0)
                nan + nan*I

                sage: CBF(-1).log(2)
                [4.53236014182719 +/- ...e-15]*I
                sage: CBF(-1).log(2, analytic=True)
                nan + nan*I
                sage: CBF(-1, RBF(0, rad=.1r)).log(analytic=False)
                [+/- ...e-3] + [+/- 3.15]*I"""
        @overload
        def log1p(self, analytic=...) -> Any:
            """ComplexBall.log1p(self, analytic=False)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3135)

            Return ``log(1 + self)``, computed accurately when ``self`` is close to
            zero.

            INPUT:

            - ``analytic`` -- boolean (default: ``False``); if ``True``, return an
              indeterminate (not-a-number) value when the input ball touches
              the branch cut

            EXAMPLES::

                sage: eps = RBF(1e-50)
                sage: CBF(1+eps, eps).log()
                [+/- ...e-16] + [1.000000000000000e-50 +/- ...e-66]*I
                sage: CBF(eps, eps).log1p()
                [1.000000000000000e-50 +/- ...e-68] + [1.00000000000000e-50 +/- ...e-66]*I
                sage: CBF(-3/2).log1p(analytic=True)
                nan + nan*I

            TESTS::

                sage: CBF(-1/2).log1p(analytic=True)
                [-0.693147180559945 +/- ...e-16]"""
        @overload
        def log1p(self) -> Any:
            """ComplexBall.log1p(self, analytic=False)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3135)

            Return ``log(1 + self)``, computed accurately when ``self`` is close to
            zero.

            INPUT:

            - ``analytic`` -- boolean (default: ``False``); if ``True``, return an
              indeterminate (not-a-number) value when the input ball touches
              the branch cut

            EXAMPLES::

                sage: eps = RBF(1e-50)
                sage: CBF(1+eps, eps).log()
                [+/- ...e-16] + [1.000000000000000e-50 +/- ...e-66]*I
                sage: CBF(eps, eps).log1p()
                [1.000000000000000e-50 +/- ...e-68] + [1.00000000000000e-50 +/- ...e-66]*I
                sage: CBF(-3/2).log1p(analytic=True)
                nan + nan*I

            TESTS::

                sage: CBF(-1/2).log1p(analytic=True)
                [-0.693147180559945 +/- ...e-16]"""
        @overload
        def log1p(self, analytic=...) -> Any:
            """ComplexBall.log1p(self, analytic=False)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3135)

            Return ``log(1 + self)``, computed accurately when ``self`` is close to
            zero.

            INPUT:

            - ``analytic`` -- boolean (default: ``False``); if ``True``, return an
              indeterminate (not-a-number) value when the input ball touches
              the branch cut

            EXAMPLES::

                sage: eps = RBF(1e-50)
                sage: CBF(1+eps, eps).log()
                [+/- ...e-16] + [1.000000000000000e-50 +/- ...e-66]*I
                sage: CBF(eps, eps).log1p()
                [1.000000000000000e-50 +/- ...e-68] + [1.00000000000000e-50 +/- ...e-66]*I
                sage: CBF(-3/2).log1p(analytic=True)
                nan + nan*I

            TESTS::

                sage: CBF(-1/2).log1p(analytic=True)
                [-0.693147180559945 +/- ...e-16]"""
        @overload
        def log1p(self, analytic=...) -> Any:
            """ComplexBall.log1p(self, analytic=False)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3135)

            Return ``log(1 + self)``, computed accurately when ``self`` is close to
            zero.

            INPUT:

            - ``analytic`` -- boolean (default: ``False``); if ``True``, return an
              indeterminate (not-a-number) value when the input ball touches
              the branch cut

            EXAMPLES::

                sage: eps = RBF(1e-50)
                sage: CBF(1+eps, eps).log()
                [+/- ...e-16] + [1.000000000000000e-50 +/- ...e-66]*I
                sage: CBF(eps, eps).log1p()
                [1.000000000000000e-50 +/- ...e-68] + [1.00000000000000e-50 +/- ...e-66]*I
                sage: CBF(-3/2).log1p(analytic=True)
                nan + nan*I

            TESTS::

                sage: CBF(-1/2).log1p(analytic=True)
                [-0.693147180559945 +/- ...e-16]"""
        @overload
        def log_barnes_g(self) -> Any:
            """ComplexBall.log_barnes_g(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3819)

            Return the logarithmic Barnes G-function of ``self``.

            EXAMPLES::

                sage: CBF(10^100).log_barnes_g()
                [1.14379254649702e+202 +/- ...e+187]
                sage: CBF(0,1000).log_barnes_g()
                [-2702305.04929258 +/- ...e-9] + [-790386.325561423 +/- ...e-10]*I"""
        @overload
        def log_barnes_g(self) -> Any:
            """ComplexBall.log_barnes_g(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3819)

            Return the logarithmic Barnes G-function of ``self``.

            EXAMPLES::

                sage: CBF(10^100).log_barnes_g()
                [1.14379254649702e+202 +/- ...e+187]
                sage: CBF(0,1000).log_barnes_g()
                [-2702305.04929258 +/- ...e-9] + [-790386.325561423 +/- ...e-10]*I"""
        @overload
        def log_barnes_g(self) -> Any:
            """ComplexBall.log_barnes_g(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3819)

            Return the logarithmic Barnes G-function of ``self``.

            EXAMPLES::

                sage: CBF(10^100).log_barnes_g()
                [1.14379254649702e+202 +/- ...e+187]
                sage: CBF(0,1000).log_barnes_g()
                [-2702305.04929258 +/- ...e-9] + [-790386.325561423 +/- ...e-10]*I"""
        @overload
        def log_gamma(self, analytic=...) -> Any:
            """ComplexBall.log_gamma(self, analytic=False)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3606)

            Return the image of this ball by the logarithmic Gamma function.

            The branch cut of the logarithmic gamma function is placed on the
            negative half-axis, which means that
            ``log_gamma(z) + log z = log_gamma(z+1)`` holds for all `z`,
            whereas ``log_gamma(z) != log(gamma(z))`` in general.

            INPUT:

            - ``analytic`` -- boolean (default: ``False``); if ``True``, return an
              indeterminate (not-a-number) value when the input ball touches
              the branch cut

            EXAMPLES::

                sage: CBF(1000, 1000).log_gamma()
                [5466.22252162990 +/- ...e-12] + [7039.33429191119 +/- ...e-12]*I
                sage: CBF(-1/2).log_gamma()
                [1.265512123484645 +/- ...e-16] + [-3.141592653589793 +/- ...e-16]*I
                sage: CBF(-1).log_gamma()
                nan + ...*I
                sage: CBF(-3/2).log_gamma() # abs tol 1e-14
                [0.860047015376481 +/- 3.82e-16] + [-6.283185307179586 +/- 6.77e-16]*I
                sage: CBF(-3/2).log_gamma(analytic=True)
                nan + nan*I"""
        @overload
        def log_gamma(self, z) -> Any:
            """ComplexBall.log_gamma(self, analytic=False)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3606)

            Return the image of this ball by the logarithmic Gamma function.

            The branch cut of the logarithmic gamma function is placed on the
            negative half-axis, which means that
            ``log_gamma(z) + log z = log_gamma(z+1)`` holds for all `z`,
            whereas ``log_gamma(z) != log(gamma(z))`` in general.

            INPUT:

            - ``analytic`` -- boolean (default: ``False``); if ``True``, return an
              indeterminate (not-a-number) value when the input ball touches
              the branch cut

            EXAMPLES::

                sage: CBF(1000, 1000).log_gamma()
                [5466.22252162990 +/- ...e-12] + [7039.33429191119 +/- ...e-12]*I
                sage: CBF(-1/2).log_gamma()
                [1.265512123484645 +/- ...e-16] + [-3.141592653589793 +/- ...e-16]*I
                sage: CBF(-1).log_gamma()
                nan + ...*I
                sage: CBF(-3/2).log_gamma() # abs tol 1e-14
                [0.860047015376481 +/- 3.82e-16] + [-6.283185307179586 +/- 6.77e-16]*I
                sage: CBF(-3/2).log_gamma(analytic=True)
                nan + nan*I"""
        @overload
        def log_gamma(self) -> Any:
            """ComplexBall.log_gamma(self, analytic=False)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3606)

            Return the image of this ball by the logarithmic Gamma function.

            The branch cut of the logarithmic gamma function is placed on the
            negative half-axis, which means that
            ``log_gamma(z) + log z = log_gamma(z+1)`` holds for all `z`,
            whereas ``log_gamma(z) != log(gamma(z))`` in general.

            INPUT:

            - ``analytic`` -- boolean (default: ``False``); if ``True``, return an
              indeterminate (not-a-number) value when the input ball touches
              the branch cut

            EXAMPLES::

                sage: CBF(1000, 1000).log_gamma()
                [5466.22252162990 +/- ...e-12] + [7039.33429191119 +/- ...e-12]*I
                sage: CBF(-1/2).log_gamma()
                [1.265512123484645 +/- ...e-16] + [-3.141592653589793 +/- ...e-16]*I
                sage: CBF(-1).log_gamma()
                nan + ...*I
                sage: CBF(-3/2).log_gamma() # abs tol 1e-14
                [0.860047015376481 +/- 3.82e-16] + [-6.283185307179586 +/- 6.77e-16]*I
                sage: CBF(-3/2).log_gamma(analytic=True)
                nan + nan*I"""
        @overload
        def log_gamma(self) -> Any:
            """ComplexBall.log_gamma(self, analytic=False)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3606)

            Return the image of this ball by the logarithmic Gamma function.

            The branch cut of the logarithmic gamma function is placed on the
            negative half-axis, which means that
            ``log_gamma(z) + log z = log_gamma(z+1)`` holds for all `z`,
            whereas ``log_gamma(z) != log(gamma(z))`` in general.

            INPUT:

            - ``analytic`` -- boolean (default: ``False``); if ``True``, return an
              indeterminate (not-a-number) value when the input ball touches
              the branch cut

            EXAMPLES::

                sage: CBF(1000, 1000).log_gamma()
                [5466.22252162990 +/- ...e-12] + [7039.33429191119 +/- ...e-12]*I
                sage: CBF(-1/2).log_gamma()
                [1.265512123484645 +/- ...e-16] + [-3.141592653589793 +/- ...e-16]*I
                sage: CBF(-1).log_gamma()
                nan + ...*I
                sage: CBF(-3/2).log_gamma() # abs tol 1e-14
                [0.860047015376481 +/- 3.82e-16] + [-6.283185307179586 +/- 6.77e-16]*I
                sage: CBF(-3/2).log_gamma(analytic=True)
                nan + nan*I"""
        @overload
        def log_gamma(self) -> Any:
            """ComplexBall.log_gamma(self, analytic=False)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3606)

            Return the image of this ball by the logarithmic Gamma function.

            The branch cut of the logarithmic gamma function is placed on the
            negative half-axis, which means that
            ``log_gamma(z) + log z = log_gamma(z+1)`` holds for all `z`,
            whereas ``log_gamma(z) != log(gamma(z))`` in general.

            INPUT:

            - ``analytic`` -- boolean (default: ``False``); if ``True``, return an
              indeterminate (not-a-number) value when the input ball touches
              the branch cut

            EXAMPLES::

                sage: CBF(1000, 1000).log_gamma()
                [5466.22252162990 +/- ...e-12] + [7039.33429191119 +/- ...e-12]*I
                sage: CBF(-1/2).log_gamma()
                [1.265512123484645 +/- ...e-16] + [-3.141592653589793 +/- ...e-16]*I
                sage: CBF(-1).log_gamma()
                nan + ...*I
                sage: CBF(-3/2).log_gamma() # abs tol 1e-14
                [0.860047015376481 +/- 3.82e-16] + [-6.283185307179586 +/- 6.77e-16]*I
                sage: CBF(-3/2).log_gamma(analytic=True)
                nan + nan*I"""
        @overload
        def log_gamma(self) -> Any:
            """ComplexBall.log_gamma(self, analytic=False)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3606)

            Return the image of this ball by the logarithmic Gamma function.

            The branch cut of the logarithmic gamma function is placed on the
            negative half-axis, which means that
            ``log_gamma(z) + log z = log_gamma(z+1)`` holds for all `z`,
            whereas ``log_gamma(z) != log(gamma(z))`` in general.

            INPUT:

            - ``analytic`` -- boolean (default: ``False``); if ``True``, return an
              indeterminate (not-a-number) value when the input ball touches
              the branch cut

            EXAMPLES::

                sage: CBF(1000, 1000).log_gamma()
                [5466.22252162990 +/- ...e-12] + [7039.33429191119 +/- ...e-12]*I
                sage: CBF(-1/2).log_gamma()
                [1.265512123484645 +/- ...e-16] + [-3.141592653589793 +/- ...e-16]*I
                sage: CBF(-1).log_gamma()
                nan + ...*I
                sage: CBF(-3/2).log_gamma() # abs tol 1e-14
                [0.860047015376481 +/- 3.82e-16] + [-6.283185307179586 +/- 6.77e-16]*I
                sage: CBF(-3/2).log_gamma(analytic=True)
                nan + nan*I"""
        @overload
        def log_gamma(self, analytic=...) -> Any:
            """ComplexBall.log_gamma(self, analytic=False)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3606)

            Return the image of this ball by the logarithmic Gamma function.

            The branch cut of the logarithmic gamma function is placed on the
            negative half-axis, which means that
            ``log_gamma(z) + log z = log_gamma(z+1)`` holds for all `z`,
            whereas ``log_gamma(z) != log(gamma(z))`` in general.

            INPUT:

            - ``analytic`` -- boolean (default: ``False``); if ``True``, return an
              indeterminate (not-a-number) value when the input ball touches
              the branch cut

            EXAMPLES::

                sage: CBF(1000, 1000).log_gamma()
                [5466.22252162990 +/- ...e-12] + [7039.33429191119 +/- ...e-12]*I
                sage: CBF(-1/2).log_gamma()
                [1.265512123484645 +/- ...e-16] + [-3.141592653589793 +/- ...e-16]*I
                sage: CBF(-1).log_gamma()
                nan + ...*I
                sage: CBF(-3/2).log_gamma() # abs tol 1e-14
                [0.860047015376481 +/- 3.82e-16] + [-6.283185307179586 +/- 6.77e-16]*I
                sage: CBF(-3/2).log_gamma(analytic=True)
                nan + nan*I"""
        def log_integral(self, *args, **kwargs):
            """ComplexBall.li(self, bool offset=False)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4377)

            Return the logarithmic integral with argument ``self``.

            If ``offset`` is True, return the offset logarithmic integral.

            EXAMPLES::

                sage: CBF(1, 1).li()  # abs tol 6e-15
                [0.61391166922120 +/- 6.23e-15] + [2.05958421419258 +/- 5.59e-15]*I
                sage: CBF(0).li()
                0
                sage: CBF(0).li(offset=True)
                [-1.045163780117493 +/- ...e-16]
                sage: li(0).n()                                                             # needs sage.symbolic
                0.000000000000000
                sage: Li(0).n()                                                             # needs sage.symbolic
                -1.04516378011749

            TESTS::

                sage: CBF(li(0))                                                            # needs sage.symbolic
                0
                sage: CBF(Li(0))                                                            # needs sage.symbolic
                [-1.04516378011749...]"""
        def log_integral_offset(self, *args, **kwargs):
            """ComplexBall.Li(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4411)

            Offset logarithmic integral.

            EXAMPLES::

                sage: CBF(0).Li()
                [-1.045163780117493 +/- ...e-16]
                sage: li(0).n()                                                             # needs sage.symbolic
                0.000000000000000
                sage: Li(0).n()                                                             # needs sage.symbolic
                -1.04516378011749"""
        @overload
        def mid(self) -> Any:
            """ComplexBall.mid(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 2007)

            Return the midpoint of this ball.

            OUTPUT:

            :class:`~sage.rings.complex_mpfr.ComplexNumber`, floating-point
            complex number formed by the centers of the real and imaginary parts of
            this ball.

            EXAMPLES::

                sage: CBF(1/3, 1).mid()
                0.333333333333333 + 1.00000000000000*I
                sage: CBF(1/3, 1).mid().parent()
                Complex Field with 53 bits of precision
                sage: CBF('inf', 'nan').mid()
                +infinity + NaN*I
                sage: CBF('nan', 'inf').mid()
                NaN + +infinity*I
                sage: CBF('nan').mid()
                NaN
                sage: CBF('inf').mid()
                +infinity
                sage: CBF(0, 'inf').mid()
                +infinity*I

            .. SEEALSO:: :meth:`squash`"""
        @overload
        def mid(self) -> Any:
            """ComplexBall.mid(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 2007)

            Return the midpoint of this ball.

            OUTPUT:

            :class:`~sage.rings.complex_mpfr.ComplexNumber`, floating-point
            complex number formed by the centers of the real and imaginary parts of
            this ball.

            EXAMPLES::

                sage: CBF(1/3, 1).mid()
                0.333333333333333 + 1.00000000000000*I
                sage: CBF(1/3, 1).mid().parent()
                Complex Field with 53 bits of precision
                sage: CBF('inf', 'nan').mid()
                +infinity + NaN*I
                sage: CBF('nan', 'inf').mid()
                NaN + +infinity*I
                sage: CBF('nan').mid()
                NaN
                sage: CBF('inf').mid()
                +infinity
                sage: CBF(0, 'inf').mid()
                +infinity*I

            .. SEEALSO:: :meth:`squash`"""
        @overload
        def mid(self) -> Any:
            """ComplexBall.mid(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 2007)

            Return the midpoint of this ball.

            OUTPUT:

            :class:`~sage.rings.complex_mpfr.ComplexNumber`, floating-point
            complex number formed by the centers of the real and imaginary parts of
            this ball.

            EXAMPLES::

                sage: CBF(1/3, 1).mid()
                0.333333333333333 + 1.00000000000000*I
                sage: CBF(1/3, 1).mid().parent()
                Complex Field with 53 bits of precision
                sage: CBF('inf', 'nan').mid()
                +infinity + NaN*I
                sage: CBF('nan', 'inf').mid()
                NaN + +infinity*I
                sage: CBF('nan').mid()
                NaN
                sage: CBF('inf').mid()
                +infinity
                sage: CBF(0, 'inf').mid()
                +infinity*I

            .. SEEALSO:: :meth:`squash`"""
        @overload
        def mid(self) -> Any:
            """ComplexBall.mid(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 2007)

            Return the midpoint of this ball.

            OUTPUT:

            :class:`~sage.rings.complex_mpfr.ComplexNumber`, floating-point
            complex number formed by the centers of the real and imaginary parts of
            this ball.

            EXAMPLES::

                sage: CBF(1/3, 1).mid()
                0.333333333333333 + 1.00000000000000*I
                sage: CBF(1/3, 1).mid().parent()
                Complex Field with 53 bits of precision
                sage: CBF('inf', 'nan').mid()
                +infinity + NaN*I
                sage: CBF('nan', 'inf').mid()
                NaN + +infinity*I
                sage: CBF('nan').mid()
                NaN
                sage: CBF('inf').mid()
                +infinity
                sage: CBF(0, 'inf').mid()
                +infinity*I

            .. SEEALSO:: :meth:`squash`"""
        @overload
        def mid(self) -> Any:
            """ComplexBall.mid(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 2007)

            Return the midpoint of this ball.

            OUTPUT:

            :class:`~sage.rings.complex_mpfr.ComplexNumber`, floating-point
            complex number formed by the centers of the real and imaginary parts of
            this ball.

            EXAMPLES::

                sage: CBF(1/3, 1).mid()
                0.333333333333333 + 1.00000000000000*I
                sage: CBF(1/3, 1).mid().parent()
                Complex Field with 53 bits of precision
                sage: CBF('inf', 'nan').mid()
                +infinity + NaN*I
                sage: CBF('nan', 'inf').mid()
                NaN + +infinity*I
                sage: CBF('nan').mid()
                NaN
                sage: CBF('inf').mid()
                +infinity
                sage: CBF(0, 'inf').mid()
                +infinity*I

            .. SEEALSO:: :meth:`squash`"""
        @overload
        def mid(self) -> Any:
            """ComplexBall.mid(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 2007)

            Return the midpoint of this ball.

            OUTPUT:

            :class:`~sage.rings.complex_mpfr.ComplexNumber`, floating-point
            complex number formed by the centers of the real and imaginary parts of
            this ball.

            EXAMPLES::

                sage: CBF(1/3, 1).mid()
                0.333333333333333 + 1.00000000000000*I
                sage: CBF(1/3, 1).mid().parent()
                Complex Field with 53 bits of precision
                sage: CBF('inf', 'nan').mid()
                +infinity + NaN*I
                sage: CBF('nan', 'inf').mid()
                NaN + +infinity*I
                sage: CBF('nan').mid()
                NaN
                sage: CBF('inf').mid()
                +infinity
                sage: CBF(0, 'inf').mid()
                +infinity*I

            .. SEEALSO:: :meth:`squash`"""
        @overload
        def mid(self) -> Any:
            """ComplexBall.mid(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 2007)

            Return the midpoint of this ball.

            OUTPUT:

            :class:`~sage.rings.complex_mpfr.ComplexNumber`, floating-point
            complex number formed by the centers of the real and imaginary parts of
            this ball.

            EXAMPLES::

                sage: CBF(1/3, 1).mid()
                0.333333333333333 + 1.00000000000000*I
                sage: CBF(1/3, 1).mid().parent()
                Complex Field with 53 bits of precision
                sage: CBF('inf', 'nan').mid()
                +infinity + NaN*I
                sage: CBF('nan', 'inf').mid()
                NaN + +infinity*I
                sage: CBF('nan').mid()
                NaN
                sage: CBF('inf').mid()
                +infinity
                sage: CBF(0, 'inf').mid()
                +infinity*I

            .. SEEALSO:: :meth:`squash`"""
        @overload
        def mid(self) -> Any:
            """ComplexBall.mid(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 2007)

            Return the midpoint of this ball.

            OUTPUT:

            :class:`~sage.rings.complex_mpfr.ComplexNumber`, floating-point
            complex number formed by the centers of the real and imaginary parts of
            this ball.

            EXAMPLES::

                sage: CBF(1/3, 1).mid()
                0.333333333333333 + 1.00000000000000*I
                sage: CBF(1/3, 1).mid().parent()
                Complex Field with 53 bits of precision
                sage: CBF('inf', 'nan').mid()
                +infinity + NaN*I
                sage: CBF('nan', 'inf').mid()
                NaN + +infinity*I
                sage: CBF('nan').mid()
                NaN
                sage: CBF('inf').mid()
                +infinity
                sage: CBF(0, 'inf').mid()
                +infinity*I

            .. SEEALSO:: :meth:`squash`"""
        @overload
        def modular_delta(self) -> Any:
            """ComplexBall.modular_delta(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4535)

            Return the modular discriminant with *tau* given by ``self``.

            EXAMPLES::

                sage: CBF(0,1).modular_delta()
                [0.0017853698506421 +/- ...e-17]
                sage: a, b, c, d = 2, 5, 1, 3
                sage: tau = CBF(1,3)
                sage: ((a*tau+b)/(c*tau+d)).modular_delta()
                [0.20921376655 +/- ...e-12] + [1.57611925523 +/- ...e-12]*I
                sage: (c*tau+d)^12 * tau.modular_delta()
                [0.20921376654986 +/- ...e-15] + [1.5761192552253 +/- ...e-14]*I"""
        @overload
        def modular_delta(self) -> Any:
            """ComplexBall.modular_delta(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4535)

            Return the modular discriminant with *tau* given by ``self``.

            EXAMPLES::

                sage: CBF(0,1).modular_delta()
                [0.0017853698506421 +/- ...e-17]
                sage: a, b, c, d = 2, 5, 1, 3
                sage: tau = CBF(1,3)
                sage: ((a*tau+b)/(c*tau+d)).modular_delta()
                [0.20921376655 +/- ...e-12] + [1.57611925523 +/- ...e-12]*I
                sage: (c*tau+d)^12 * tau.modular_delta()
                [0.20921376654986 +/- ...e-15] + [1.5761192552253 +/- ...e-14]*I"""
        @overload
        def modular_delta(self) -> Any:
            """ComplexBall.modular_delta(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4535)

            Return the modular discriminant with *tau* given by ``self``.

            EXAMPLES::

                sage: CBF(0,1).modular_delta()
                [0.0017853698506421 +/- ...e-17]
                sage: a, b, c, d = 2, 5, 1, 3
                sage: tau = CBF(1,3)
                sage: ((a*tau+b)/(c*tau+d)).modular_delta()
                [0.20921376655 +/- ...e-12] + [1.57611925523 +/- ...e-12]*I
                sage: (c*tau+d)^12 * tau.modular_delta()
                [0.20921376654986 +/- ...e-15] + [1.5761192552253 +/- ...e-14]*I"""
        @overload
        def modular_delta(self) -> Any:
            """ComplexBall.modular_delta(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4535)

            Return the modular discriminant with *tau* given by ``self``.

            EXAMPLES::

                sage: CBF(0,1).modular_delta()
                [0.0017853698506421 +/- ...e-17]
                sage: a, b, c, d = 2, 5, 1, 3
                sage: tau = CBF(1,3)
                sage: ((a*tau+b)/(c*tau+d)).modular_delta()
                [0.20921376655 +/- ...e-12] + [1.57611925523 +/- ...e-12]*I
                sage: (c*tau+d)^12 * tau.modular_delta()
                [0.20921376654986 +/- ...e-15] + [1.5761192552253 +/- ...e-14]*I"""
        @overload
        def modular_eta(self) -> Any:
            """ComplexBall.modular_eta(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4497)

            Return the Dedekind eta function with *tau* given by ``self``.

            EXAMPLES::

                sage: CBF(0,1).modular_eta()
                [0.768225422326057 +/- ...e-16]
                sage: CBF(12,1).modular_eta()
                [-0.768225422326057 +/- ...e-16]"""
        @overload
        def modular_eta(self) -> Any:
            """ComplexBall.modular_eta(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4497)

            Return the Dedekind eta function with *tau* given by ``self``.

            EXAMPLES::

                sage: CBF(0,1).modular_eta()
                [0.768225422326057 +/- ...e-16]
                sage: CBF(12,1).modular_eta()
                [-0.768225422326057 +/- ...e-16]"""
        @overload
        def modular_eta(self) -> Any:
            """ComplexBall.modular_eta(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4497)

            Return the Dedekind eta function with *tau* given by ``self``.

            EXAMPLES::

                sage: CBF(0,1).modular_eta()
                [0.768225422326057 +/- ...e-16]
                sage: CBF(12,1).modular_eta()
                [-0.768225422326057 +/- ...e-16]"""
        @overload
        def modular_j(self) -> Any:
            """ComplexBall.modular_j(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4482)

            Return the modular j-invariant with *tau* given by ``self``.

            EXAMPLES::

                sage: CBF(0,1).modular_j()
                [1728.0000000000 +/- ...e-11]"""
        @overload
        def modular_j(self) -> Any:
            """ComplexBall.modular_j(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4482)

            Return the modular j-invariant with *tau* given by ``self``.

            EXAMPLES::

                sage: CBF(0,1).modular_j()
                [1728.0000000000 +/- ...e-11]"""
        @overload
        def modular_lambda(self) -> Any:
            """ComplexBall.modular_lambda(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4514)

            Return the modular lambda function with *tau* given by ``self``.

            EXAMPLES::

                sage: # needs sage.symbolic
                sage: tau = CBF(sqrt(2),pi)
                sage: tau.modular_lambda()
                [-0.00022005123884157 +/- ...e-18] + [-0.00079787346459944 +/- ...e-18]*I
                sage: (tau + 2).modular_lambda()
                [-0.00022005123884157 +/- ...e-18] + [-0.00079787346459944 +/- ...e-18]*I
                sage: (tau / (1 - 2*tau)).modular_lambda()
                [-0.00022005123884 +/- ...e-15] + [-0.00079787346460 +/- ...e-15]*I"""
        @overload
        def modular_lambda(self) -> Any:
            """ComplexBall.modular_lambda(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4514)

            Return the modular lambda function with *tau* given by ``self``.

            EXAMPLES::

                sage: # needs sage.symbolic
                sage: tau = CBF(sqrt(2),pi)
                sage: tau.modular_lambda()
                [-0.00022005123884157 +/- ...e-18] + [-0.00079787346459944 +/- ...e-18]*I
                sage: (tau + 2).modular_lambda()
                [-0.00022005123884157 +/- ...e-18] + [-0.00079787346459944 +/- ...e-18]*I
                sage: (tau / (1 - 2*tau)).modular_lambda()
                [-0.00022005123884 +/- ...e-15] + [-0.00079787346460 +/- ...e-15]*I"""
        @overload
        def modular_lambda(self) -> Any:
            """ComplexBall.modular_lambda(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4514)

            Return the modular lambda function with *tau* given by ``self``.

            EXAMPLES::

                sage: # needs sage.symbolic
                sage: tau = CBF(sqrt(2),pi)
                sage: tau.modular_lambda()
                [-0.00022005123884157 +/- ...e-18] + [-0.00079787346459944 +/- ...e-18]*I
                sage: (tau + 2).modular_lambda()
                [-0.00022005123884157 +/- ...e-18] + [-0.00079787346459944 +/- ...e-18]*I
                sage: (tau / (1 - 2*tau)).modular_lambda()
                [-0.00022005123884 +/- ...e-15] + [-0.00079787346460 +/- ...e-15]*I"""
        @overload
        def modular_lambda(self) -> Any:
            """ComplexBall.modular_lambda(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4514)

            Return the modular lambda function with *tau* given by ``self``.

            EXAMPLES::

                sage: # needs sage.symbolic
                sage: tau = CBF(sqrt(2),pi)
                sage: tau.modular_lambda()
                [-0.00022005123884157 +/- ...e-18] + [-0.00079787346459944 +/- ...e-18]*I
                sage: (tau + 2).modular_lambda()
                [-0.00022005123884157 +/- ...e-18] + [-0.00079787346459944 +/- ...e-18]*I
                sage: (tau / (1 - 2*tau)).modular_lambda()
                [-0.00022005123884 +/- ...e-15] + [-0.00079787346460 +/- ...e-15]*I"""
        @overload
        def nbits(self) -> Any:
            """ComplexBall.nbits(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 2155)

            Return the minimum precision sufficient to represent this ball exactly.

            More precisely, the output is the number of bits needed to represent
            the absolute value of the mantissa of both the real and the imaginary
            part of the midpoint.

            EXAMPLES::

                sage: CBF(17, 1023).nbits()
                10
                sage: CBF(1/3, NaN).nbits()                                                 # needs sage.symbolic
                53
                sage: CBF(NaN).nbits()                                                      # needs sage.symbolic
                0"""
        @overload
        def nbits(self) -> Any:
            """ComplexBall.nbits(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 2155)

            Return the minimum precision sufficient to represent this ball exactly.

            More precisely, the output is the number of bits needed to represent
            the absolute value of the mantissa of both the real and the imaginary
            part of the midpoint.

            EXAMPLES::

                sage: CBF(17, 1023).nbits()
                10
                sage: CBF(1/3, NaN).nbits()                                                 # needs sage.symbolic
                53
                sage: CBF(NaN).nbits()                                                      # needs sage.symbolic
                0"""
        @overload
        def nbits(self) -> Any:
            """ComplexBall.nbits(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 2155)

            Return the minimum precision sufficient to represent this ball exactly.

            More precisely, the output is the number of bits needed to represent
            the absolute value of the mantissa of both the real and the imaginary
            part of the midpoint.

            EXAMPLES::

                sage: CBF(17, 1023).nbits()
                10
                sage: CBF(1/3, NaN).nbits()                                                 # needs sage.symbolic
                53
                sage: CBF(NaN).nbits()                                                      # needs sage.symbolic
                0"""
        @overload
        def nbits(self) -> Any:
            """ComplexBall.nbits(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 2155)

            Return the minimum precision sufficient to represent this ball exactly.

            More precisely, the output is the number of bits needed to represent
            the absolute value of the mantissa of both the real and the imaginary
            part of the midpoint.

            EXAMPLES::

                sage: CBF(17, 1023).nbits()
                10
                sage: CBF(1/3, NaN).nbits()                                                 # needs sage.symbolic
                53
                sage: CBF(NaN).nbits()                                                      # needs sage.symbolic
                0"""
        def overlaps(self, ComplexBallother) -> Any:
            """ComplexBall.overlaps(self, ComplexBall other)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 2525)

            Return ``True`` iff ``self`` and ``other`` have some point in common.

            INPUT:

            - ``other`` -- a :class:`ComplexBall`

            EXAMPLES::

                sage: CBF(1, 1).overlaps(1 + CBF(0, 1/3)*3)
                True
                sage: CBF(1, 1).overlaps(CBF(1, 'nan'))
                True
                sage: CBF(1, 1).overlaps(CBF(0, 'nan'))
                False"""
        def polylog(self, s) -> Any:
            """ComplexBall.polylog(self, s)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3766)

            Return the polylogarithm `\\operatorname{Li}_s(\\mathrm{self})`.

            EXAMPLES::

                sage: CBF(2).polylog(1)
                [+/- ...e-15] + [-3.14159265358979 +/- ...e-15]*I
                sage: CBF(1, 1).polylog(CBF(1, 1))
                [0.3708160030469 +/- ...e-14] + [2.7238016577979 +/- ...e-14]*I

            TESTS::

                sage: CBF(2).polylog(1r)
                [+/- ...e-15] + [-3.14159265358979 +/- ...e-15]*I"""
        def pow(self, expo, analytic=...) -> Any:
            """ComplexBall.pow(self, expo, analytic=False)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 2902)

            Raise this ball to the power of ``expo``.

            INPUT:

            - ``analytic`` -- boolean (default: ``False``); if ``True``, return an
              indeterminate (not-a-number) value when the exponent is not an
              integer and the base ball touches the branch cut of the logarithm

            EXAMPLES::

                sage: CBF(-1).pow(CBF(i))
                [0.0432139182637723 +/- ...e-17]
                sage: CBF(-1).pow(CBF(i), analytic=True)
                nan + nan*I
                sage: CBF(-10).pow(-2)
                [0.0100000000000000 +/- ...e-18]
                sage: CBF(-10).pow(-2, analytic=True)
                [0.0100000000000000 +/- ...e-18]

            TESTS::

                sage: CBF(2).pow(SR.var('x'))                                               # needs sage.symbolic
                Traceback (most recent call last):
                ...
                TypeError: no canonical coercion from Symbolic Ring to Complex ball
                field with 53 bits of precision"""
        @overload
        def psi(self, n=...) -> Any:
            """ComplexBall.psi(self, n=None)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3661)

            Compute the digamma function with argument ``self``.

            If ``n`` is provided, compute the polygamma function of order ``n``
            and argument ``self``.

            EXAMPLES::

                sage: CBF(1, 1).psi()
                [0.0946503206224770 +/- ...e-17] + [1.076674047468581 +/- ...e-16]*I
                sage: CBF(-1).psi()
                nan
                sage: CBF(1,1).psi(10)
                [56514.8269344249 +/- ...e-11] + [56215.1218005823 +/- ...e-11]*I"""
        @overload
        def psi(self) -> Any:
            """ComplexBall.psi(self, n=None)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3661)

            Compute the digamma function with argument ``self``.

            If ``n`` is provided, compute the polygamma function of order ``n``
            and argument ``self``.

            EXAMPLES::

                sage: CBF(1, 1).psi()
                [0.0946503206224770 +/- ...e-17] + [1.076674047468581 +/- ...e-16]*I
                sage: CBF(-1).psi()
                nan
                sage: CBF(1,1).psi(10)
                [56514.8269344249 +/- ...e-11] + [56215.1218005823 +/- ...e-11]*I"""
        @overload
        def psi(self) -> Any:
            """ComplexBall.psi(self, n=None)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3661)

            Compute the digamma function with argument ``self``.

            If ``n`` is provided, compute the polygamma function of order ``n``
            and argument ``self``.

            EXAMPLES::

                sage: CBF(1, 1).psi()
                [0.0946503206224770 +/- ...e-17] + [1.076674047468581 +/- ...e-16]*I
                sage: CBF(-1).psi()
                nan
                sage: CBF(1,1).psi(10)
                [56514.8269344249 +/- ...e-11] + [56215.1218005823 +/- ...e-11]*I"""
        @overload
        def rad(self) -> Any:
            """ComplexBall.rad(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 2066)

            Return an upper bound for the error radius of this ball.

            OUTPUT:

            A :class:`~sage.rings.real_mpfr.RealNumber` of the same precision as
            the radii of real balls.

            .. WARNING::

                Unlike a :class:`~sage.rings.real_arb.RealBall`,
                a :class:`ComplexBall` is *not* defined
                by its midpoint and radius. (Instances of :class:`ComplexBall` are
                actually rectangles, not balls.)

            EXAMPLES::

                sage: CBF(1 + i).rad()
                0.00000000
                sage: CBF(i/3).rad()
                1.1102230e-16
                sage: CBF(i/3).rad().parent()
                Real Field with 30 bits of precision

            .. SEEALSO:: :meth:`diameter`, :meth:`mid`

            TESTS::

                sage: (CBF(0, 1/3) << (2^64)).rad()
                Traceback (most recent call last):
                ...
                RuntimeError: unable to convert the radius to MPFR (exponent out of range?)"""
        @overload
        def rad(self) -> Any:
            """ComplexBall.rad(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 2066)

            Return an upper bound for the error radius of this ball.

            OUTPUT:

            A :class:`~sage.rings.real_mpfr.RealNumber` of the same precision as
            the radii of real balls.

            .. WARNING::

                Unlike a :class:`~sage.rings.real_arb.RealBall`,
                a :class:`ComplexBall` is *not* defined
                by its midpoint and radius. (Instances of :class:`ComplexBall` are
                actually rectangles, not balls.)

            EXAMPLES::

                sage: CBF(1 + i).rad()
                0.00000000
                sage: CBF(i/3).rad()
                1.1102230e-16
                sage: CBF(i/3).rad().parent()
                Real Field with 30 bits of precision

            .. SEEALSO:: :meth:`diameter`, :meth:`mid`

            TESTS::

                sage: (CBF(0, 1/3) << (2^64)).rad()
                Traceback (most recent call last):
                ...
                RuntimeError: unable to convert the radius to MPFR (exponent out of range?)"""
        @overload
        def rad(self) -> Any:
            """ComplexBall.rad(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 2066)

            Return an upper bound for the error radius of this ball.

            OUTPUT:

            A :class:`~sage.rings.real_mpfr.RealNumber` of the same precision as
            the radii of real balls.

            .. WARNING::

                Unlike a :class:`~sage.rings.real_arb.RealBall`,
                a :class:`ComplexBall` is *not* defined
                by its midpoint and radius. (Instances of :class:`ComplexBall` are
                actually rectangles, not balls.)

            EXAMPLES::

                sage: CBF(1 + i).rad()
                0.00000000
                sage: CBF(i/3).rad()
                1.1102230e-16
                sage: CBF(i/3).rad().parent()
                Real Field with 30 bits of precision

            .. SEEALSO:: :meth:`diameter`, :meth:`mid`

            TESTS::

                sage: (CBF(0, 1/3) << (2^64)).rad()
                Traceback (most recent call last):
                ...
                RuntimeError: unable to convert the radius to MPFR (exponent out of range?)"""
        @overload
        def rad(self) -> Any:
            """ComplexBall.rad(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 2066)

            Return an upper bound for the error radius of this ball.

            OUTPUT:

            A :class:`~sage.rings.real_mpfr.RealNumber` of the same precision as
            the radii of real balls.

            .. WARNING::

                Unlike a :class:`~sage.rings.real_arb.RealBall`,
                a :class:`ComplexBall` is *not* defined
                by its midpoint and radius. (Instances of :class:`ComplexBall` are
                actually rectangles, not balls.)

            EXAMPLES::

                sage: CBF(1 + i).rad()
                0.00000000
                sage: CBF(i/3).rad()
                1.1102230e-16
                sage: CBF(i/3).rad().parent()
                Real Field with 30 bits of precision

            .. SEEALSO:: :meth:`diameter`, :meth:`mid`

            TESTS::

                sage: (CBF(0, 1/3) << (2^64)).rad()
                Traceback (most recent call last):
                ...
                RuntimeError: unable to convert the radius to MPFR (exponent out of range?)"""
        @overload
        def rad(self) -> Any:
            """ComplexBall.rad(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 2066)

            Return an upper bound for the error radius of this ball.

            OUTPUT:

            A :class:`~sage.rings.real_mpfr.RealNumber` of the same precision as
            the radii of real balls.

            .. WARNING::

                Unlike a :class:`~sage.rings.real_arb.RealBall`,
                a :class:`ComplexBall` is *not* defined
                by its midpoint and radius. (Instances of :class:`ComplexBall` are
                actually rectangles, not balls.)

            EXAMPLES::

                sage: CBF(1 + i).rad()
                0.00000000
                sage: CBF(i/3).rad()
                1.1102230e-16
                sage: CBF(i/3).rad().parent()
                Real Field with 30 bits of precision

            .. SEEALSO:: :meth:`diameter`, :meth:`mid`

            TESTS::

                sage: (CBF(0, 1/3) << (2^64)).rad()
                Traceback (most recent call last):
                ...
                RuntimeError: unable to convert the radius to MPFR (exponent out of range?)"""
        @overload
        def real(self) -> RealBall:
            """ComplexBall.real(self) -> RealBall

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 1875)

            Return the real part of this ball.

            OUTPUT: a :class:`~sage.rings.real_arb.RealBall`

            EXAMPLES::

               sage: a = CBF(1/3, 1/5)
               sage: a.real()
               [0.3333333333333333 +/- ...e-17]
               sage: a.real().parent()
               Real ball field with 53 bits of precision"""
        @overload
        def real(self) -> Any:
            """ComplexBall.real(self) -> RealBall

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 1875)

            Return the real part of this ball.

            OUTPUT: a :class:`~sage.rings.real_arb.RealBall`

            EXAMPLES::

               sage: a = CBF(1/3, 1/5)
               sage: a.real()
               [0.3333333333333333 +/- ...e-17]
               sage: a.real().parent()
               Real ball field with 53 bits of precision"""
        @overload
        def real(self) -> Any:
            """ComplexBall.real(self) -> RealBall

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 1875)

            Return the real part of this ball.

            OUTPUT: a :class:`~sage.rings.real_arb.RealBall`

            EXAMPLES::

               sage: a = CBF(1/3, 1/5)
               sage: a.real()
               [0.3333333333333333 +/- ...e-17]
               sage: a.real().parent()
               Real ball field with 53 bits of precision"""
        @overload
        def rgamma(self) -> Any:
            """ComplexBall.rgamma(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3644)

            Compute the reciprocal gamma function with argument ``self``.

            EXAMPLES::

                sage: CBF(6).rgamma()
                [0.00833333333333333 +/- ...e-18]
                sage: CBF(-1).rgamma()
                0"""
        @overload
        def rgamma(self) -> Any:
            """ComplexBall.rgamma(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3644)

            Compute the reciprocal gamma function with argument ``self``.

            EXAMPLES::

                sage: CBF(6).rgamma()
                [0.00833333333333333 +/- ...e-18]
                sage: CBF(-1).rgamma()
                0"""
        @overload
        def rgamma(self) -> Any:
            """ComplexBall.rgamma(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3644)

            Compute the reciprocal gamma function with argument ``self``.

            EXAMPLES::

                sage: CBF(6).rgamma()
                [0.00833333333333333 +/- ...e-18]
                sage: CBF(-1).rgamma()
                0"""
        def rising_factorial(self, n) -> Any:
            """ComplexBall.rising_factorial(self, n)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3048)

            Return the ``n``-th rising factorial of this ball.

            The `n`-th rising factorial of `x` is equal to `x (x+1) \\cdots (x+n-1)`.

            For complex `n`, it is a quotient of gamma functions.

            EXAMPLES::

                sage: CBF(1).rising_factorial(5)
                120.0000000000000
                sage: CBF(1/3, 1/2).rising_factorial(300)
                [-3.87949484514e+612 +/- 5...e+600] + [-3.52042209763e+612 +/- 5...e+600]*I

                sage: CBF(1).rising_factorial(-1)
                nan
                sage: CBF(1).rising_factorial(2**64)
                [+/- ...e+347382171326740403407]
                sage: ComplexBallField(128)(1).rising_factorial(2**64)
                [2.34369112679686134...e+347382171305201285713 +/- ...]
                sage: CBF(1/2).rising_factorial(CBF(2,3)) # abs tol 1e-15
                [-0.123060451458124 +/- 3.06e-16] + [0.0406412631676552 +/- 7.57e-17]*I"""
        def round(self) -> Any:
            """ComplexBall.round(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 2174)

            Return a copy of this ball rounded to the precision of the parent.

            EXAMPLES:

            It is possible to create balls whose midpoint is more precise that
            their parent's nominal precision (see :mod:`~sage.rings.real_arb` for
            more information)::

                sage: b = CBF(exp(I*pi/3).n(100))                                           # needs sage.symbolic
                sage: b.mid()                                                               # needs sage.symbolic
                0.50000000000000000000000000000 + 0.86602540378443864676372317075*I

            The ``round()`` method rounds such a ball to its parent's precision::

                sage: b.round().mid()                                                       # needs sage.symbolic
                0.500000000000000 + 0.866025403784439*I

            .. SEEALSO:: :meth:`trim`"""
        @overload
        def rsqrt(self, analytic=...) -> Any:
            """ComplexBall.rsqrt(self, analytic=False)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 2996)

            Return the reciprocal square root of ``self``.

            If either the real or imaginary part is exactly zero, only a single
            real reciprocal square root is needed.

            INPUT:

            - ``analytic`` -- boolean (default: ``False``); if ``True``, return an
              indeterminate (not-a-number) value when the input ball touches
              the branch cut

            EXAMPLES::

                sage: CBF(-2).rsqrt()
                [-0.707106781186547 +/- ...e-16]*I
                sage: CBF(-2).rsqrt(analytic=True)
                nan + nan*I
                sage: CBF(0, 1/2).rsqrt()
                1.000000000000000 - 1.000000000000000*I
                sage: CBF(0).rsqrt()
                nan + nan*I"""
        @overload
        def rsqrt(self) -> Any:
            """ComplexBall.rsqrt(self, analytic=False)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 2996)

            Return the reciprocal square root of ``self``.

            If either the real or imaginary part is exactly zero, only a single
            real reciprocal square root is needed.

            INPUT:

            - ``analytic`` -- boolean (default: ``False``); if ``True``, return an
              indeterminate (not-a-number) value when the input ball touches
              the branch cut

            EXAMPLES::

                sage: CBF(-2).rsqrt()
                [-0.707106781186547 +/- ...e-16]*I
                sage: CBF(-2).rsqrt(analytic=True)
                nan + nan*I
                sage: CBF(0, 1/2).rsqrt()
                1.000000000000000 - 1.000000000000000*I
                sage: CBF(0).rsqrt()
                nan + nan*I"""
        @overload
        def rsqrt(self, analytic=...) -> Any:
            """ComplexBall.rsqrt(self, analytic=False)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 2996)

            Return the reciprocal square root of ``self``.

            If either the real or imaginary part is exactly zero, only a single
            real reciprocal square root is needed.

            INPUT:

            - ``analytic`` -- boolean (default: ``False``); if ``True``, return an
              indeterminate (not-a-number) value when the input ball touches
              the branch cut

            EXAMPLES::

                sage: CBF(-2).rsqrt()
                [-0.707106781186547 +/- ...e-16]*I
                sage: CBF(-2).rsqrt(analytic=True)
                nan + nan*I
                sage: CBF(0, 1/2).rsqrt()
                1.000000000000000 - 1.000000000000000*I
                sage: CBF(0).rsqrt()
                nan + nan*I"""
        @overload
        def rsqrt(self) -> Any:
            """ComplexBall.rsqrt(self, analytic=False)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 2996)

            Return the reciprocal square root of ``self``.

            If either the real or imaginary part is exactly zero, only a single
            real reciprocal square root is needed.

            INPUT:

            - ``analytic`` -- boolean (default: ``False``); if ``True``, return an
              indeterminate (not-a-number) value when the input ball touches
              the branch cut

            EXAMPLES::

                sage: CBF(-2).rsqrt()
                [-0.707106781186547 +/- ...e-16]*I
                sage: CBF(-2).rsqrt(analytic=True)
                nan + nan*I
                sage: CBF(0, 1/2).rsqrt()
                1.000000000000000 - 1.000000000000000*I
                sage: CBF(0).rsqrt()
                nan + nan*I"""
        @overload
        def rsqrt(self) -> Any:
            """ComplexBall.rsqrt(self, analytic=False)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 2996)

            Return the reciprocal square root of ``self``.

            If either the real or imaginary part is exactly zero, only a single
            real reciprocal square root is needed.

            INPUT:

            - ``analytic`` -- boolean (default: ``False``); if ``True``, return an
              indeterminate (not-a-number) value when the input ball touches
              the branch cut

            EXAMPLES::

                sage: CBF(-2).rsqrt()
                [-0.707106781186547 +/- ...e-16]*I
                sage: CBF(-2).rsqrt(analytic=True)
                nan + nan*I
                sage: CBF(0, 1/2).rsqrt()
                1.000000000000000 - 1.000000000000000*I
                sage: CBF(0).rsqrt()
                nan + nan*I"""
        @overload
        def sec(self) -> Any:
            """ComplexBall.sec(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3269)

            Return the secant of this ball.

            EXAMPLES::

                sage: CBF(1, 1).sec()
                [0.498337030555187 +/- ...e-16] + [0.591083841721045 +/- ...e-16]*I"""
        @overload
        def sec(self) -> Any:
            """ComplexBall.sec(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3269)

            Return the secant of this ball.

            EXAMPLES::

                sage: CBF(1, 1).sec()
                [0.498337030555187 +/- ...e-16] + [0.591083841721045 +/- ...e-16]*I"""
        @overload
        def sech(self) -> Any:
            """ComplexBall.sech(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3363)

            Return the hyperbolic secant of this ball.

            EXAMPLES::

                sage: CBF(pi/2, 1/10).sech()                                                # needs sage.symbolic
                [0.397174529918189 +/- ...e-16] + [-0.0365488656274242 +/- ...e-17]*I"""
        @overload
        def sech(self) -> Any:
            """ComplexBall.sech(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3363)

            Return the hyperbolic secant of this ball.

            EXAMPLES::

                sage: CBF(pi/2, 1/10).sech()                                                # needs sage.symbolic
                [0.397174529918189 +/- ...e-16] + [-0.0365488656274242 +/- ...e-17]*I"""
        @overload
        def sin(self) -> Any:
            """ComplexBall.sin(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3205)

            Return the sine of this ball.

            EXAMPLES::

                sage: CBF(i*pi).sin()                                                       # needs sage.symbolic
                [11.54873935725775 +/- ...e-15]*I"""
        @overload
        def sin(self) -> Any:
            """ComplexBall.sin(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3205)

            Return the sine of this ball.

            EXAMPLES::

                sage: CBF(i*pi).sin()                                                       # needs sage.symbolic
                [11.54873935725775 +/- ...e-15]*I"""
        def sin_integral(self, *args, **kwargs):
            """ComplexBall.Si(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4281)

            Return the sine integral with argument ``self``.

            EXAMPLES::

                sage: CBF(1, 1).Si()  # abs tol 3e-15
                [1.10422265823558 +/- 2.48e-15] + [0.88245380500792 +/- 3.36e-15]*I
                sage: CBF(0).Si()
                0

            TESTS:

                sage: CBF(Si(I))  # abs tol 3e-15                                           # needs sage.symbolic
                [1.05725087537573 +/- 2.77e-15]*I"""
        @overload
        def sinh(self) -> Any:
            """ComplexBall.sinh(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3299)

            Return the hyperbolic sine of this ball.

            EXAMPLES::

                sage: CBF(1, 1).sinh()
                [0.634963914784736 +/- ...e-16] + [1.298457581415977 +/- ...e-16]*I"""
        @overload
        def sinh(self) -> Any:
            """ComplexBall.sinh(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3299)

            Return the hyperbolic sine of this ball.

            EXAMPLES::

                sage: CBF(1, 1).sinh()
                [0.634963914784736 +/- ...e-16] + [1.298457581415977 +/- ...e-16]*I"""
        def sinh_integral(self, *args, **kwargs):
            """ComplexBall.Shi(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 4329)

            Return the hyperbolic sine integral with argument ``self``.

            EXAMPLES::

                sage: CBF(1, 1).Shi()  # abs tol 3e-15
                [0.88245380500792 +/- 3.36e-15] + [1.10422265823558 +/- 2.48e-15]*I
                sage: CBF(0).Shi()
                0

            TESTS:

                sage: CBF(Shi(I))  # abs tol 1e-15                                          # needs sage.symbolic
                [0.946083070367183 +/- 9.22e-16]*I"""
        def spherical_harmonic(self, phi, n, m) -> Any:
            """ComplexBall.spherical_harmonic(self, phi, n, m)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 5151)

            Return the spherical harmonic `Y_n^m(\\theta,\\phi)`
            evaluated at `\\theta` given by ``self``.
            In the current implementation, ``n`` and ``m`` must be small integers.

            EXAMPLES::

                sage: CBF(1+I).spherical_harmonic(1/2, -3, -2)
                [0.80370071745224 +/- ...e-15] + [-0.07282031864711 +/- ...e-15]*I"""
        @overload
        def sqrt(self, analytic=...) -> Any:
            """ComplexBall.sqrt(self, analytic=False)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 2966)

            Return the square root of this ball.

            If either the real or imaginary part is exactly zero, only a single
            real square root is needed.

            INPUT:

            - ``analytic`` -- boolean (default: ``False``); if ``True``, return an
              indeterminate (not-a-number) value when the input ball touches
              the branch cut

            EXAMPLES::

                sage: CBF(-2).sqrt()
                [1.414213562373095 +/- ...e-16]*I
                sage: CBF(-2).sqrt(analytic=True)
                nan + nan*I"""
        @overload
        def sqrt(self) -> Any:
            """ComplexBall.sqrt(self, analytic=False)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 2966)

            Return the square root of this ball.

            If either the real or imaginary part is exactly zero, only a single
            real square root is needed.

            INPUT:

            - ``analytic`` -- boolean (default: ``False``); if ``True``, return an
              indeterminate (not-a-number) value when the input ball touches
              the branch cut

            EXAMPLES::

                sage: CBF(-2).sqrt()
                [1.414213562373095 +/- ...e-16]*I
                sage: CBF(-2).sqrt(analytic=True)
                nan + nan*I"""
        @overload
        def sqrt(self, analytic=...) -> Any:
            """ComplexBall.sqrt(self, analytic=False)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 2966)

            Return the square root of this ball.

            If either the real or imaginary part is exactly zero, only a single
            real square root is needed.

            INPUT:

            - ``analytic`` -- boolean (default: ``False``); if ``True``, return an
              indeterminate (not-a-number) value when the input ball touches
              the branch cut

            EXAMPLES::

                sage: CBF(-2).sqrt()
                [1.414213562373095 +/- ...e-16]*I
                sage: CBF(-2).sqrt(analytic=True)
                nan + nan*I"""
        @overload
        def squash(self) -> Any:
            """ComplexBall.squash(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 2041)

            Return an exact ball with the same midpoint as this ball.

            OUTPUT: a :class:`ComplexBall`

            EXAMPLES::

                sage: mid = CBF(1/3, 1/10).squash()
                sage: mid
                [0.3333333333333333 +/- ...e-17] + [0.09999999999999999 +/- ...e-18]*I
                sage: mid.parent()
                Complex ball field with 53 bits of precision
                sage: mid.is_exact()
                True

            .. SEEALSO:: :meth:`mid`"""
        @overload
        def squash(self) -> Any:
            """ComplexBall.squash(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 2041)

            Return an exact ball with the same midpoint as this ball.

            OUTPUT: a :class:`ComplexBall`

            EXAMPLES::

                sage: mid = CBF(1/3, 1/10).squash()
                sage: mid
                [0.3333333333333333 +/- ...e-17] + [0.09999999999999999 +/- ...e-18]*I
                sage: mid.parent()
                Complex ball field with 53 bits of precision
                sage: mid.is_exact()
                True

            .. SEEALSO:: :meth:`mid`"""
        @overload
        def tan(self) -> Any:
            """ComplexBall.tan(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3235)

            Return the tangent of this ball.

            EXAMPLES::

                sage: CBF(pi/2, 1/10).tan()                                                 # needs sage.symbolic
                [+/- ...e-14] + [10.03331113225399 +/- ...e-15]*I
                sage: CBF(pi/2).tan()                                                       # needs sage.symbolic
                nan"""
        @overload
        def tan(self) -> Any:
            """ComplexBall.tan(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3235)

            Return the tangent of this ball.

            EXAMPLES::

                sage: CBF(pi/2, 1/10).tan()                                                 # needs sage.symbolic
                [+/- ...e-14] + [10.03331113225399 +/- ...e-15]*I
                sage: CBF(pi/2).tan()                                                       # needs sage.symbolic
                nan"""
        @overload
        def tan(self) -> Any:
            """ComplexBall.tan(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3235)

            Return the tangent of this ball.

            EXAMPLES::

                sage: CBF(pi/2, 1/10).tan()                                                 # needs sage.symbolic
                [+/- ...e-14] + [10.03331113225399 +/- ...e-15]*I
                sage: CBF(pi/2).tan()                                                       # needs sage.symbolic
                nan"""
        @overload
        def tanh(self) -> Any:
            """ComplexBall.tanh(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3329)

            Return the hyperbolic tangent of this ball.

            EXAMPLES::

                sage: CBF(1, 1).tanh()
                [1.083923327338694 +/- ...e-16] + [0.2717525853195117 +/- ...e-17]*I
                sage: CBF(0, pi/2).tanh()                                                   # needs sage.symbolic
                nan*I"""
        @overload
        def tanh(self) -> Any:
            """ComplexBall.tanh(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3329)

            Return the hyperbolic tangent of this ball.

            EXAMPLES::

                sage: CBF(1, 1).tanh()
                [1.083923327338694 +/- ...e-16] + [0.2717525853195117 +/- ...e-17]*I
                sage: CBF(0, pi/2).tanh()                                                   # needs sage.symbolic
                nan*I"""
        @overload
        def tanh(self) -> Any:
            """ComplexBall.tanh(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3329)

            Return the hyperbolic tangent of this ball.

            EXAMPLES::

                sage: CBF(1, 1).tanh()
                [1.083923327338694 +/- ...e-16] + [0.2717525853195117 +/- ...e-17]*I
                sage: CBF(0, pi/2).tanh()                                                   # needs sage.symbolic
                nan*I"""
        @overload
        def trim(self) -> Any:
            """ComplexBall.trim(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 2226)

            Return a trimmed copy of this ball.

            Return a copy of this ball with both the real and imaginary parts
            trimmed (see :meth:`~sage.rings.real_arb.RealBall.trim()`).

            EXAMPLES::

                sage: b = CBF(1/3, RBF(1/3, rad=.01))
                sage: b.mid()
                0.333333333333333 + 0.333333333333333*I
                sage: b.trim().mid()
                0.333333333333333 + 0.333333015441895*I

            .. SEEALSO:: :meth:`round`"""
        @overload
        def trim(self) -> Any:
            """ComplexBall.trim(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 2226)

            Return a trimmed copy of this ball.

            Return a copy of this ball with both the real and imaginary parts
            trimmed (see :meth:`~sage.rings.real_arb.RealBall.trim()`).

            EXAMPLES::

                sage: b = CBF(1/3, RBF(1/3, rad=.01))
                sage: b.mid()
                0.333333333333333 + 0.333333333333333*I
                sage: b.trim().mid()
                0.333333333333333 + 0.333333015441895*I

            .. SEEALSO:: :meth:`round`"""
        @overload
        def trim(self) -> Any:
            """ComplexBall.trim(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 2226)

            Return a trimmed copy of this ball.

            Return a copy of this ball with both the real and imaginary parts
            trimmed (see :meth:`~sage.rings.real_arb.RealBall.trim()`).

            EXAMPLES::

                sage: b = CBF(1/3, RBF(1/3, rad=.01))
                sage: b.mid()
                0.333333333333333 + 0.333333333333333*I
                sage: b.trim().mid()
                0.333333333333333 + 0.333333015441895*I

            .. SEEALSO:: :meth:`round`"""
        def union(self, other) -> Any:
            """ComplexBall.union(self, other)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 2136)

            Return a ball containing the convex hull of ``self`` and ``other``.

            EXAMPLES::

                sage: b = CBF(1 + i).union(0)
                sage: b.real().endpoints()
                (-9.31322574615479e-10, 1.00000000093133)"""
        @overload
        def zeta(self, a=...) -> Any:
            """ComplexBall.zeta(self, a=None)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3690)

            Return the image of this ball by the Hurwitz zeta function.

            For ``a = None``, this computes the Riemann zeta function.

            EXAMPLES::

                sage: CBF(1, 1).zeta()
                [0.5821580597520036 +/- ...e-17] + [-0.9268485643308071 +/- ...e-17]*I
                sage: CBF(1, 1).zeta(1)
                [0.5821580597520036 +/- ...e-17] + [-0.9268485643308071 +/- ...e-17]*I
                sage: CBF(1, 1).zeta(1/2)
                [1.497919876084167 +/- ...e-16] + [0.2448655353684164 +/- ...e-17]*I
                sage: CBF(1, 1).zeta(CBF(1, 1))
                [-0.3593983122202835 +/- ...e-17] + [-2.875283329756940 +/- ...e-16]*I
                sage: CBF(1, 1).zeta(-1)
                nan + nan*I"""
        @overload
        def zeta(self) -> Any:
            """ComplexBall.zeta(self, a=None)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3690)

            Return the image of this ball by the Hurwitz zeta function.

            For ``a = None``, this computes the Riemann zeta function.

            EXAMPLES::

                sage: CBF(1, 1).zeta()
                [0.5821580597520036 +/- ...e-17] + [-0.9268485643308071 +/- ...e-17]*I
                sage: CBF(1, 1).zeta(1)
                [0.5821580597520036 +/- ...e-17] + [-0.9268485643308071 +/- ...e-17]*I
                sage: CBF(1, 1).zeta(1/2)
                [1.497919876084167 +/- ...e-16] + [0.2448655353684164 +/- ...e-17]*I
                sage: CBF(1, 1).zeta(CBF(1, 1))
                [-0.3593983122202835 +/- ...e-17] + [-2.875283329756940 +/- ...e-16]*I
                sage: CBF(1, 1).zeta(-1)
                nan + nan*I"""
        def zetaderiv(self, k) -> Any:
            """ComplexBall.zetaderiv(self, k)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 3722)

            Return the image of this ball by the `k`-th derivative of the Riemann
            zeta function.

            For a more flexible interface, see the low-level method
            ``_zeta_series`` of polynomials with complex ball coefficients.

            EXAMPLES::

                sage: CBF(1/2, 3).zetaderiv(1)
                [0.191759884092721...] + [-0.073135728865928...]*I
                sage: CBF(2).zetaderiv(3)
                [-6.0001458028430...]"""
        def __abs__(self) -> Any:
            """ComplexBall.__abs__(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 1913)

            Return the absolute value of this complex ball.

            EXAMPLES::

                sage: CBF(1 + i).abs() # indirect doctest
                [1.414213562373095 +/- ...e-16]
                sage: abs(CBF(i))
                1.000000000000000

                sage: CBF(1 + i).abs().parent()
                Real ball field with 53 bits of precision"""
        def __bool__(self) -> bool:
            """True if self else False"""
        def __complex__(self) -> Any:
            """ComplexBall.__complex__(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 1770)

            Convert ``self`` to a ``complex``.

            EXAMPLES::

                sage: complex(CBF(1))
                (1+0j)
                sage: complex(CBF(1,1))
                (1+1j)

            Check nan and inf::

                sage: complex(CBF(0, 'nan'))
                nanj
                sage: complex(CBF('+inf', '-inf'))
                (inf-infj)"""
        def __contains__(self, other) -> Any:
            """ComplexBall.__contains__(self, other)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 2593)

            Return ``True`` if ``other`` can be verified to be contained in ``self``.

            Depending on the type of ``other``, the test may use interval
            arithmetic with a precision determined by the parent of ``self`` and
            may return false negatives.

            EXAMPLES::

                sage: 1/3*i in CBF(0, 1/3)
                True

            A false negative::

                sage: RLF(1/3) in CBF(RealBallField(100)(1/3), 0)
                False

            .. SEEALSO:: :meth:`contains_exact`"""
        def __float__(self) -> Any:
            """ComplexBall.__float__(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 1751)

            Convert ``self`` to a ``float``.

            EXAMPLES::

                sage: float(CBF(1))
                1.0
                sage: float(CBF(1/3))
                0.3333333333333333
                sage: float(CBF(1,1))
                Traceback (most recent call last):
                ...
                TypeError: can...t convert complex ball to float"""
        def __hash__(self) -> Any:
            """ComplexBall.__hash__(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 1532)

            TESTS::

                sage: hash(CBF(1/3)) == hash(RBF(1/3))
                True
                sage: hash(CBF(1/3 + 2*i)) != hash(CBF(1/3 + i))
                True"""
        def __invert__(self) -> Any:
            """ComplexBall.__invert__(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 2713)

            Return the inverse of this ball.

            The result is guaranteed to contain the inverse of any point of the
            input ball.

            EXAMPLES::

                sage: ~CBF(i/3)
                [-3.00000000000000 +/- ...e-16]*I
                sage: ~CBF(0)
                nan
                sage: ~CBF(RIF(10,11))
                [0.1 +/- ...e-3]"""
        def __lshift__(self, val, shift) -> Any:
            """ComplexBall.__lshift__(val, shift)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 2754)

            If ``val`` is a ``ComplexBall`` and ``shift`` is an integer, return the
            ball obtained by shifting the center and radius of ``val`` to the left
            by ``shift`` bits.

            INPUT:

            - ``shift`` -- integer; may be negative

            EXAMPLES::

                sage: CBF(i/3) << 2
                [1.333333333333333 +/- ...e-16]*I
                sage: CBF(i) << -2
                0.2500000000000000*I

            TESTS::

                sage: CBF(i) << (2^65)
                [3.636549880934858e+11106046577046714264 +/- ...e+11106046577046714248]*I
                sage: 'a' << CBF(1/3)
                Traceback (most recent call last):
                ...
                TypeError: unsupported operand type(s) for <<: 'str' and
                'ComplexBall'
                sage: CBF(1) << 1/2
                Traceback (most recent call last):
                ...
                TypeError: shift should be an integer"""
        def __neg__(self) -> Any:
            """ComplexBall.__neg__(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 2650)

            Return the opposite of this ball.

            EXAMPLES::

                sage: -CBF(1/3 + I)
                [-0.3333333333333333 +/- ...e-17] - 1.000000000000000*I"""
        def __pow__(self, base, expo, _) -> Any:
            """ComplexBall.__pow__(base, expo, _)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 2860)

            EXAMPLES::

                sage: CBF(-1)**(1/2)
                1.000000000000000*I
                sage: CBF(e)**CBF(i*pi)                                                     # needs sage.symbolic
                [-1.00000000000000 +/- ...e-16] + [+/- ...e-15]*I
                sage: CBF(0, 1)**AA(2)**(1/2)
                [-0.60569986707881 +/- ...e-15] + [0.79569320156748 +/- ...e-15]*I

                sage: CBF(i)**RBF(2**1000)
                [+/- 1.01] + [+/- 1.01]*I
                sage: CBF(i)**(2**1000)
                1.000000000000000

                sage: CBF(0)^(1/3)
                0
                sage: CBF(0)^(-1)
                nan
                sage: CBF(0)^(-2)
                nan + nan*I

            TESTS::

                sage: (CBF(e)**CBF(i))**RBF(pi)                                             # needs sage.symbolic
                [-1.0000000000000 +/- ...e-15] + [+/- ...e-15]*I
                sage: CBF(2*i)**10r
                -1024.000000000000
                sage: CBF(1,1) ^ -1r
                0.5000000000000000 - 0.5000000000000000*I
                sage: CBF(2)**SR.var('x')                                                   # needs sage.symbolic
                2.000000000000000^x"""
        def __reduce__(self) -> Any:
            """ComplexBall.__reduce__(self)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 1579)

            Serialize a ComplexBall.

            TESTS::

                sage: [loads(dumps(b)).identical(b) for b in                                # needs sage.symbolic
                ....:     [ComplexBallField(60)(1/3 + i*pi), CBF(NaN)]]
                [True, True]"""
        def __rlshift__(self, other):
            """Return value<<self."""
        def __rpow__(self, other):
            """Return pow(value, self, mod)."""
        def __rrshift__(self, other):
            """Return value>>self."""
        def __rshift__(self, val, shift) -> Any:
            """ComplexBall.__rshift__(val, shift)

            File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 2805)

            If ``val`` is a ``ComplexBall`` and ``shift`` is an integer, return the
            ball obtained by shifting the center and radius of ``val`` to the right
            by ``shift`` bits.

            INPUT:

            - ``shift`` -- integer; may be negative

            EXAMPLES::

                sage: CBF(1+I) >> 2
                0.2500000000000000 + 0.2500000000000000*I

            TESTS::

                sage: 'a' >> CBF(1/3)
                Traceback (most recent call last):
                ...
                TypeError: unsupported operand type(s) for >>: 'str' and
                'ComplexBall'"""
    def __init__(self, longprecision=...) -> Any:
        """ComplexBallField.__init__(self, long precision=53)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 363)

        Initialize the complex ball field.

        INPUT:

        - ``precision`` -- integer `\\ge 2`

        EXAMPLES::

            sage: CBF(1)
            1.000000000000000

        TESTS::

            sage: CBF.base()
            Real ball field with 53 bits of precision
            sage: CBF.base_ring()
            Real ball field with 53 bits of precision

        There are direct coercions from ZZ and QQ (for which FLINT provides
        construction functions)::

            sage: CBF.coerce_map_from(ZZ)
            Coercion map:
              From: Integer Ring
              To:   Complex ball field with 53 bits of precision
            sage: CBF.coerce_map_from(QQ)
            Coercion map:
              From: Rational Field
              To:   Complex ball field with 53 bits of precision

        Various other coercions are available through real ball fields or CLF::

            sage: CBF.has_coerce_map_from(RLF)
            True
            sage: CBF.has_coerce_map_from(AA)
            True
            sage: CBF.has_coerce_map_from(QuadraticField(-1))
            True
            sage: CBF.has_coerce_map_from(QQbar)
            True
            sage: CBF.has_coerce_map_from(CLF)
            True"""
    @overload
    def characteristic(self) -> Any:
        """ComplexBallField.characteristic(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 732)

        Complex ball fields have characteristic zero.

        EXAMPLES::

            sage: ComplexBallField().characteristic()
            0"""
    @overload
    def characteristic(self) -> Any:
        """ComplexBallField.characteristic(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 732)

        Complex ball fields have characteristic zero.

        EXAMPLES::

            sage: ComplexBallField().characteristic()
            0"""
    @overload
    def complex_field(self) -> Any:
        """ComplexBallField.complex_field(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 456)

        Return the complex ball field with the same precision, i.e. ``self``.

        EXAMPLES::

            sage: CBF.complex_field() is CBF
            True"""
    @overload
    def complex_field(self) -> Any:
        """ComplexBallField.complex_field(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 456)

        Return the complex ball field with the same precision, i.e. ``self``.

        EXAMPLES::

            sage: CBF.complex_field() is CBF
            True"""
    @overload
    def construction(self) -> Any:
        """ComplexBallField.construction(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 440)

        Return the construction of a complex ball field as the algebraic
        closure of the real ball field with the same precision.

        EXAMPLES::

            sage: functor, base = CBF.construction()
            sage: functor, base
            (AlgebraicClosureFunctor, Real ball field with 53 bits of precision)
            sage: functor(base) is CBF
            True"""
    @overload
    def construction(self) -> Any:
        """ComplexBallField.construction(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 440)

        Return the construction of a complex ball field as the algebraic
        closure of the real ball field with the same precision.

        EXAMPLES::

            sage: functor, base = CBF.construction()
            sage: functor, base
            (AlgebraicClosureFunctor, Real ball field with 53 bits of precision)
            sage: functor(base) is CBF
            True"""
    def gen(self, i) -> Any:
        """ComplexBallField.gen(self, i)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 478)

        For i = 0, return the imaginary unit in this complex ball field.

        EXAMPLES::

            sage: CBF.0
            1.000000000000000*I
            sage: CBF.gen(1)
            Traceback (most recent call last):
            ...
            ValueError: only one generator"""
    @overload
    def gens(self) -> tuple:
        """ComplexBallField.gens(self) -> tuple

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 496)

        Return the tuple of generators of this complex ball field, i.e.
        ``(i,)``.

        EXAMPLES::

            sage: CBF.gens()
            (1.000000000000000*I,)
            sage: CBF.gens_dict()
            {'1.000000000000000*I': 1.000000000000000*I}"""
    @overload
    def gens(self) -> Any:
        """ComplexBallField.gens(self) -> tuple

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 496)

        Return the tuple of generators of this complex ball field, i.e.
        ``(i,)``.

        EXAMPLES::

            sage: CBF.gens()
            (1.000000000000000*I,)
            sage: CBF.gens_dict()
            {'1.000000000000000*I': 1.000000000000000*I}"""
    def integral(self, func, a, b, params=..., rel_tol=..., abs_tol=..., deg_limit=..., eval_limit=..., depth_limit=..., use_heap=..., verbose=...) -> Any:
        """ComplexBallField.integral(self, func, a, b, params=None, rel_tol=None, abs_tol=None, deg_limit=None, eval_limit=None, depth_limit=None, use_heap=None, verbose=None)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 1002)

        Compute a rigorous enclosure of the integral of ``func`` on the
        interval [``a``, ``b``].

        INPUT:

        - ``func`` -- a callable object accepting two parameters, a complex
          ball\xa0``x`` and a boolean flag ``analytic``, and returning an element
          of this ball field (or some value that coerces into this ball field),
          such that:

          - ``func(x, False)`` evaluates the integrand `f` on the ball ``x``.
            There are no restrictions on the behavior of `f` on ``x``; in
            particular, it can be discontinuous.

          - ``func(x, True)`` evaluates `f(x)` if  `f` is analytic on the
            whole\xa0``x``, and returns some non-finite ball (e.g., ``self(NaN)``)
            otherwise.

          (The ``analytic`` flag only needs to be checked for integrands that
          are non-analytic but bounded in some regions, typically complex
          functions with branch cuts, like `\\sqrt{z}`. In particular, it can be
          ignored for meromorphic functions.)

        - ``a``, ``b`` -- integration bounds. The bounds can be real or complex
          balls, or elements of any parent that coerces into this ball field,
          e.g. rational or algebraic numbers.

        - ``rel_tol`` -- relative accuracy goal (default: `2^{-p}` where `p` is
          the precision of the ball field)

        - ``abs_tol`` -- absolute accuracy goal (default: `2^{-p}` where `p` is
          the precision of the ball field)

        Additionally, the following optional parameters can be used to control
        the integration algorithm. See the `FLINT documentation <https://flintlib.org/doc/acb_calc.html>`_
        for more information.

        - ``deg_limit`` -- maximum quadrature degree for each
          subinterval

        - ``eval_limit`` -- maximum number of function
          evaluations

        - ``depth_limit`` -- maximum search depth for
          adaptive subdivision

        - ``use_heap`` -- boolean (default: ``False``); if ``True``, use a
          priority queue instead of a stack to manage subintervals. This
          sometimes gives better results for integrals with slow convergence but
          may require more memory and increasing ``depth_limit``.

        - ``verbose`` -- integer (default: 0); if set to 1, some information
          about the overall integration process is printed to standard
          output. If set to 2, information about each subinterval is printed.

        EXAMPLES:

        Some analytic integrands::

            sage: CBF.integral(lambda x, _: x, 0, 1)
            [0.500000000000000 +/- ...e-16]

            sage: CBF.integral(lambda x, _: x.gamma(), 1 - CBF(i), 1 + CBF(i)) # abs tol 1e-13
            [+/- 1.39e-15] + [1.57239266949806 +/- 8.33e-15]*I

            sage: C = ComplexBallField(100)
            sage: C.integral(lambda x, _: x.cos() * x.sin(), 0, 1)
            [0.35403670913678559674939205737 +/- ...e-30]

            sage: CBF.integral(lambda x, _: (x + x.exp()).sin(), 0, 8)
            [0.34740017266 +/- ...e-12]

            sage: C = ComplexBallField(2000)
            sage: C.integral(lambda x, _: (x + x.exp()).sin(), 0, 8) # long time
            [0.34740017...55347713 +/- ...e-598]

        Here the integration path crosses the branch cut of the square root::

            sage: def my_sqrt(z, analytic):
            ....:     if (analytic and not z.real() > 0
            ....:                  and z.imag().contains_zero()):
            ....:         return CBF(NaN)
            ....:     else:
            ....:         return z.sqrt()
            sage: CBF.integral(my_sqrt, -1 + CBF(i), -1 - CBF(i))                       # needs sage.symbolic
            [+/- ...e-14] + [-0.4752076627926 +/- 5...e-14]*I

        Note, though, that proper handling of the ``analytic`` flag is required
        even when the path does not touch the branch cut::

            sage: correct = CBF.integral(my_sqrt, 1, 2); correct
            [1.21895141649746 +/- ...e-15]
            sage: RBF(integral(sqrt(x), x, 1, 2))       # long time                     # needs sage.symbolic
            [1.21895141649746 +/- ...e-15]
            sage: wrong = CBF.integral(lambda z, _: z.sqrt(), 1, 2) # WRONG!
            sage: correct - wrong
            [-5.640636259e-5 +/- ...e-15]

        We can integrate the real absolute value function by defining a
        piecewise holomorphic extension::

            sage: def real_abs(z, analytic):
            ....:     if z.real().contains_zero():
            ....:         if analytic:
            ....:             return z.parent()(NaN)
            ....:         else:
            ....:             return z.union(-z)
            ....:     elif z.real() > 0:
            ....:         return z
            ....:     else:
            ....:         return -z
            sage: CBF.integral(real_abs, -1, 1)
            [1.00000000000...]
            sage: CBF.integral(lambda z, analytic: real_abs(z.sin(), analytic), 0, 2*CBF.pi())
            [4.00000000000...]

        Some methods of complex balls natively support the ``analytic`` flag::

            sage: CBF.integral(lambda z, analytic: z.log(analytic=analytic),
            ....:              -1-CBF(i), -1+CBF(i))
            [+/- ...e-14] + [0.26394350735484 +/- ...e-15]*I
            sage: from sage.rings.complex_arb import ComplexBall
            sage: CBF.integral(ComplexBall.sqrt, -1+CBF(i), -1-CBF(i))
            [+/- ...e-14] + [-0.4752076627926 +/- 5...e-14]*I

        Here the integrand has a pole on or very close to the integration path,
        but there is no need to explicitly handle the ``analytic`` flag since
        the integrand is unbounded::

            sage: CBF.integral(lambda x, _: 1/x, -1, 1)
            nan + nan*I
            sage: CBF.integral(lambda x, _: 1/x, 10^-1000, 1)
            nan + nan*I
            sage: CBF.integral(lambda x, _: 1/x, 10^-1000, 1, abs_tol=1e-10)
            [2302.5850930 +/- ...e-8]

        Tolerances::

            sage: CBF.integral(lambda x, _: x.exp(), -1020, -1010)
            [+/- ...e-438]
            sage: CBF.integral(lambda x, _: x.exp(), -1020, -1010, abs_tol=1e-450)
            [2.304377150950e-439 +/- ...e-452]
            sage: CBF.integral(lambda x, _: x.exp(), -1020, -1010, abs_tol=0)
            [2.304377150950e-439 +/- 7...e-452]
            sage: CBF.integral(lambda x, _: x.exp(), -1020, -1010, rel_tol=1e-2, abs_tol=0)
            [2.3044e-439 +/- ...e-444]

            sage: epsi = CBF(1e-10)
            sage: CBF.integral(lambda x, _: x*(1/x).sin(), epsi, 1)
            [0.38 +/- ...e-3]
            sage: CBF.integral(lambda x, _: x*(1/x).sin(), epsi, 1, use_heap=True)
            [0.37853002 +/- ...e-9]

        ALGORITHM:

        Uses the `acb_calc <https://flintlib.org/doc/acb_calc.html>`_ module of
        the FLINT library.

        TESTS::

            sage: CBF.integral(lambda x, _: x, 0, 10, rel_tol=1e-10,
            ....:     abs_tol=1e-10, deg_limit=1, eval_limit=20, depth_limit=4,
            ....:     use_heap=False)
            [50.00000000 +/- ...e-9]

            sage: i = QuadraticField(-1).gen()
            sage: CBF.integral(lambda x, _: (1 + i*x).gamma(), -1, 1) # abs tol 1e-13
            [1.57239266949806 +/- 8.33e-15] + [+/- 1.39e-15]*I

            sage: ComplexBallField(10000).integral(lambda x, _: x.sin(), 0, 1, rel_tol=1e-300)
            [0.459... +/- ...e-3...]
            sage: CBF.integral(lambda x, _: x.sin(), 0, 100, rel_tol=10)
            [0.1377 +/- ...e-5]

            sage: ComplexBallField(10000).integral(lambda x, _: x.sin(), 0, 1, abs_tol=1e-400)
            [0.459697... +/- ...e-4...]
            sage: CBF.integral(lambda x, _: x.sin(), 0, 1, abs_tol=10)
            [+/- 0.842]

            sage: ComplexBallField(100).integral(lambda x, _: sin(x), RBF(0), RBF(1))
            [0.4596976941318602825990633926 +/- ...e-29]

            sage: from sage.doctest.util import ensure_interruptible_after
            sage: with ensure_interruptible_after(0.1):
            ....:     C = ComplexBallField(1000000)
            ....:     C.integral(lambda x, _: x.cos() * x.sin(), 0, 1)"""
    @overload
    def is_exact(self) -> Any:
        """ComplexBallField.is_exact(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 721)

        Complex ball fields are not exact.

        EXAMPLES::

            sage: ComplexBallField().is_exact()
            False"""
    @overload
    def is_exact(self) -> Any:
        """ComplexBallField.is_exact(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 721)

        Complex ball fields are not exact.

        EXAMPLES::

            sage: ComplexBallField().is_exact()
            False"""
    @overload
    def ngens(self) -> Any:
        """ComplexBallField.ngens(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 467)

        Return 1 as the only generator is the imaginary unit.

        EXAMPLES::

            sage: CBF.ngens()
            1"""
    @overload
    def ngens(self) -> Any:
        """ComplexBallField.ngens(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 467)

        Return 1 as the only generator is the imaginary unit.

        EXAMPLES::

            sage: CBF.ngens()
            1"""
    def pi(self) -> Any:
        """ComplexBallField.pi(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 980)

        Return a ball enclosing `\\pi`.

        EXAMPLES::

            sage: CBF.pi()
            [3.141592653589793 +/- ...e-16]
            sage: ComplexBallField(128).pi()
            [3.1415926535897932384626433832795028842 +/- ...e-38]

            sage: CBF.pi().parent()
            Complex ball field with 53 bits of precision"""
    def prec(self, *args, **kwargs):
        """ComplexBallField.precision(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 708)

        Return the bit precision used for operations on elements of this field.

        EXAMPLES::

            sage: ComplexBallField().precision()
            53"""
    @overload
    def precision(self) -> Any:
        """ComplexBallField.precision(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 708)

        Return the bit precision used for operations on elements of this field.

        EXAMPLES::

            sage: ComplexBallField().precision()
            53"""
    @overload
    def precision(self) -> Any:
        """ComplexBallField.precision(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 708)

        Return the bit precision used for operations on elements of this field.

        EXAMPLES::

            sage: ComplexBallField().precision()
            53"""
    @overload
    def some_elements(self) -> Any:
        """ComplexBallField.some_elements(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 743)

        Complex ball fields contain elements with exact, inexact, infinite, or
        undefined real and imaginary parts.

        EXAMPLES::

            sage: CBF.some_elements()
            [1.000000000000000,
             -0.5000000000000000*I,
             1.000000000000000 + [0.3333333333333333 +/- ...e-17]*I,
             [-0.3333333333333333 +/- ...e-17] + 0.2500000000000000*I,
             [-2.175556475109056e+181961467118333366510562 +/- ...e+181961467118333366510545],
             [+/- inf],
             [0.3333333333333333 +/- ...e-17] + [+/- inf]*I,
             [+/- inf] + [+/- inf]*I,
             nan,
             nan + nan*I,
             [+/- inf] + nan*I]"""
    @overload
    def some_elements(self) -> Any:
        """ComplexBallField.some_elements(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 743)

        Complex ball fields contain elements with exact, inexact, infinite, or
        undefined real and imaginary parts.

        EXAMPLES::

            sage: CBF.some_elements()
            [1.000000000000000,
             -0.5000000000000000*I,
             1.000000000000000 + [0.3333333333333333 +/- ...e-17]*I,
             [-0.3333333333333333 +/- ...e-17] + 0.2500000000000000*I,
             [-2.175556475109056e+181961467118333366510562 +/- ...e+181961467118333366510545],
             [+/- inf],
             [0.3333333333333333 +/- ...e-17] + [+/- inf]*I,
             [+/- inf] + [+/- inf]*I,
             nan,
             nan + nan*I,
             [+/- inf] + nan*I]"""
    def zeta_zeros(self, count, start=...) -> Any:
        """ComplexBallField.zeta_zeros(self, count, start=1)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 1263)

        Compute consecutive zeros of the Riemann zeta function.

        INPUT:

        - ``count`` -- positive integer; number of zeros to be computed, must fit in a machine integer

        - ``start`` -- positive integer (default: 1); index of the first zero to be computed

        OUTPUT:

        A list of ``count`` consecutive zeros of the Riemann zeta function, starting from the ``start``-th zero.
        Indexing starts at one, following usual mathematical notations.

        EXAMPLES::

            sage: CBF.zeta_zeros(10)
            [0.5000000000000000 + [14.134725141734...]*I,
            0.5000000000000000 + [21.0220396387715...]*I,
            0.5000000000000000 + [25.010857580145...]*I,
            0.5000000000000000 + [30.4248761258595...]*I,
            0.5000000000000000 + [32.935061587739...]*I,
            0.5000000000000000 + [37.586178158825...]*I,
            0.5000000000000000 + [40.918719012147...]*I,
            0.5000000000000000 + [43.32707328091...]*I,
            0.5000000000000000 + [48.005150881167...]*I,
            0.5000000000000000 + [49.773832477672...]*I]

            sage: CBF.zeta_zeros(6, start=5)
            [0.5000000000000000 + [32.935061587739...]*I,
            0.5000000000000000 + [37.586178158825...]*I,
            0.5000000000000000 + [40.918719012147...]*I,
            0.5000000000000000 + [43.32707328091...]*I,
            0.5000000000000000 + [48.005150881167...]*I,
            0.5000000000000000 + [49.773832477672...]*I]"""
    @staticmethod
    def __classcall__(cls, longprecision=...) -> Any:
        """ComplexBallField.__classcall__(cls, long precision=53)

        File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 351)

        Normalize the arguments for caching.

        TESTS::

            sage: ComplexBallField(53) is ComplexBallField()
            True"""

class IntegrationContext:
    """File: /build/sagemath/src/sage/src/sage/rings/complex_arb.pyx (starting at line 243)

        Used to wrap the integrand and hold some context information during
        numerical integration.
    """
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
