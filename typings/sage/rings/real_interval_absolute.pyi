import _cython_3_2_1
import sage as sage
import sage.rings.ring
import sage.structure.element
import sage.structure.factory
from sage.categories.category import RR_min_prec as RR_min_prec
from sage.rings.rational_field import QQ as QQ
from sage.rings.real_mpfi import RealIntervalField as RealIntervalField, RealIntervalFieldElement as RealIntervalFieldElement
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from sage.structure.factory import UniqueFactory as UniqueFactory
from typing import Any, ClassVar, overload

RealIntervalAbsoluteField: Factory
shift_ceil: _cython_3_2_1.cython_function_or_method
shift_floor: _cython_3_2_1.cython_function_or_method

class Factory(sage.structure.factory.UniqueFactory):
    def create_key(self, prec) -> Any:
        """Factory.create_key(self, prec)

        File: /build/sagemath/src/sage/src/sage/rings/real_interval_absolute.pyx (starting at line 66)

        The only piece of data is the precision.

        TESTS::

            sage: from sage.rings.real_interval_absolute import RealIntervalAbsoluteField
            sage: RealIntervalAbsoluteField.create_key(1000)
            1000"""
    def create_object(self, version, prec) -> Any:
        """Factory.create_object(self, version, prec)

        File: /build/sagemath/src/sage/src/sage/rings/real_interval_absolute.pyx (starting at line 78)

        Ensures uniqueness.

        TESTS::

            sage: from sage.rings.real_interval_absolute import RealIntervalAbsoluteField
            sage: RealIntervalAbsoluteField(23) is RealIntervalAbsoluteField(23) # indirect doctest
            True"""

class MpfrOp:
    """MpfrOp(value, name)

    File: /build/sagemath/src/sage/src/sage/rings/real_interval_absolute.pyx (starting at line 1015)

    This class is used to endow absolute real interval field elements with
    all the methods of (relative) real interval field elements.

    EXAMPLES::

        sage: from sage.rings.real_interval_absolute import RealIntervalAbsoluteField
        sage: R = RealIntervalAbsoluteField(100)
        sage: R(1).sin()
        0.841470984807896506652502321631?"""
    def __init__(self, value, name) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/real_interval_absolute.pyx (starting at line 1030)

                EXAMPLES::

                    sage: from sage.rings.real_interval_absolute import RealIntervalAbsoluteField, MpfrOp
                    sage: R = RealIntervalAbsoluteField(100)
                    sage: MpfrOp(R(1), 'tan')()
                    1.557407724654902230506974807459?
        """
    def __call__(self, *args) -> Any:
        """MpfrOp.__call__(self, *args)

        File: /build/sagemath/src/sage/src/sage/rings/real_interval_absolute.pyx (starting at line 1042)

        EXAMPLES::

            sage: from sage.rings.real_interval_absolute import RealIntervalAbsoluteField, MpfrOp
            sage: R = RealIntervalAbsoluteField(100)
            sage: curried_log = MpfrOp(R(2), 'log')
            sage: curried_log()
            0.693147180559945309417232121458?
            sage: curried_log(2)
            1"""

class RealIntervalAbsoluteElement(sage.structure.element.FieldElement):
    """RealIntervalAbsoluteElement(RealIntervalAbsoluteField_class parent, value)"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, RealIntervalAbsoluteField_classparent, value) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/real_interval_absolute.pyx (starting at line 248)

                Create a :class:`RealIntervalAbsoluteElement`.

                EXAMPLES::

                    sage: from sage.rings.real_interval_absolute import RealIntervalAbsoluteField
                    sage: R = RealIntervalAbsoluteField(50)
                    sage: R(1)
                    1
                    sage: R(1/3)
                    0.333333333333334?
                    sage: R(1.3)
                    1.300000000000000?
                    sage: R(pi)
                    3.141592653589794?
                    sage: R((11, 12))
                    12.?
                    sage: R((11, 11.00001))
                    11.00001?

                    sage: R100 = RealIntervalAbsoluteField(100)
                    sage: R(R100((5,6)))
                    6.?
                    sage: R100(R((5,6)))
                    6.?
                    sage: RIF(CIF(NaN))
                    [.. NaN ..]
        """
    @overload
    def abs(self) -> Any:
        """RealIntervalAbsoluteElement.abs(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_interval_absolute.pyx (starting at line 618)

        Return the absolute value of ``self``.

        EXAMPLES::

            sage: from sage.rings.real_interval_absolute import RealIntervalAbsoluteField
            sage: R = RealIntervalAbsoluteField(100)
            sage: R(1/3).abs()
            0.333333333333333333333333333334?
            sage: R(-1/3).abs()
            0.333333333333333333333333333334?
            sage: R((-1/3, 1/2)).abs()
            1.?
            sage: R((-1/3, 1/2)).abs().endpoints()
            (0, 1/2)
            sage: R((-3/2, 1/2)).abs().endpoints()
            (0, 3/2)"""
    @overload
    def abs(self) -> Any:
        """RealIntervalAbsoluteElement.abs(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_interval_absolute.pyx (starting at line 618)

        Return the absolute value of ``self``.

        EXAMPLES::

            sage: from sage.rings.real_interval_absolute import RealIntervalAbsoluteField
            sage: R = RealIntervalAbsoluteField(100)
            sage: R(1/3).abs()
            0.333333333333333333333333333334?
            sage: R(-1/3).abs()
            0.333333333333333333333333333334?
            sage: R((-1/3, 1/2)).abs()
            1.?
            sage: R((-1/3, 1/2)).abs().endpoints()
            (0, 1/2)
            sage: R((-3/2, 1/2)).abs().endpoints()
            (0, 3/2)"""
    @overload
    def abs(self) -> Any:
        """RealIntervalAbsoluteElement.abs(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_interval_absolute.pyx (starting at line 618)

        Return the absolute value of ``self``.

        EXAMPLES::

            sage: from sage.rings.real_interval_absolute import RealIntervalAbsoluteField
            sage: R = RealIntervalAbsoluteField(100)
            sage: R(1/3).abs()
            0.333333333333333333333333333334?
            sage: R(-1/3).abs()
            0.333333333333333333333333333334?
            sage: R((-1/3, 1/2)).abs()
            1.?
            sage: R((-1/3, 1/2)).abs().endpoints()
            (0, 1/2)
            sage: R((-3/2, 1/2)).abs().endpoints()
            (0, 3/2)"""
    @overload
    def abs(self) -> Any:
        """RealIntervalAbsoluteElement.abs(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_interval_absolute.pyx (starting at line 618)

        Return the absolute value of ``self``.

        EXAMPLES::

            sage: from sage.rings.real_interval_absolute import RealIntervalAbsoluteField
            sage: R = RealIntervalAbsoluteField(100)
            sage: R(1/3).abs()
            0.333333333333333333333333333334?
            sage: R(-1/3).abs()
            0.333333333333333333333333333334?
            sage: R((-1/3, 1/2)).abs()
            1.?
            sage: R((-1/3, 1/2)).abs().endpoints()
            (0, 1/2)
            sage: R((-3/2, 1/2)).abs().endpoints()
            (0, 3/2)"""
    @overload
    def abs(self) -> Any:
        """RealIntervalAbsoluteElement.abs(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_interval_absolute.pyx (starting at line 618)

        Return the absolute value of ``self``.

        EXAMPLES::

            sage: from sage.rings.real_interval_absolute import RealIntervalAbsoluteField
            sage: R = RealIntervalAbsoluteField(100)
            sage: R(1/3).abs()
            0.333333333333333333333333333334?
            sage: R(-1/3).abs()
            0.333333333333333333333333333334?
            sage: R((-1/3, 1/2)).abs()
            1.?
            sage: R((-1/3, 1/2)).abs().endpoints()
            (0, 1/2)
            sage: R((-3/2, 1/2)).abs().endpoints()
            (0, 3/2)"""
    @overload
    def abs(self) -> Any:
        """RealIntervalAbsoluteElement.abs(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_interval_absolute.pyx (starting at line 618)

        Return the absolute value of ``self``.

        EXAMPLES::

            sage: from sage.rings.real_interval_absolute import RealIntervalAbsoluteField
            sage: R = RealIntervalAbsoluteField(100)
            sage: R(1/3).abs()
            0.333333333333333333333333333334?
            sage: R(-1/3).abs()
            0.333333333333333333333333333334?
            sage: R((-1/3, 1/2)).abs()
            1.?
            sage: R((-1/3, 1/2)).abs().endpoints()
            (0, 1/2)
            sage: R((-3/2, 1/2)).abs().endpoints()
            (0, 3/2)"""
    @overload
    def absolute_diameter(self) -> Any:
        """RealIntervalAbsoluteElement.absolute_diameter(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_interval_absolute.pyx (starting at line 376)

        Return the diameter ``self``.

        EXAMPLES::

            sage: from sage.rings.real_interval_absolute import RealIntervalAbsoluteField
            sage: R = RealIntervalAbsoluteField(10)
            sage: R(1/4).absolute_diameter()
            0
            sage: a = R(pi)
            sage: a.absolute_diameter()
            1/1024
            sage: a.upper() - a.lower()
            1/1024"""
    @overload
    def absolute_diameter(self) -> Any:
        """RealIntervalAbsoluteElement.absolute_diameter(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_interval_absolute.pyx (starting at line 376)

        Return the diameter ``self``.

        EXAMPLES::

            sage: from sage.rings.real_interval_absolute import RealIntervalAbsoluteField
            sage: R = RealIntervalAbsoluteField(10)
            sage: R(1/4).absolute_diameter()
            0
            sage: a = R(pi)
            sage: a.absolute_diameter()
            1/1024
            sage: a.upper() - a.lower()
            1/1024"""
    @overload
    def absolute_diameter(self) -> Any:
        """RealIntervalAbsoluteElement.absolute_diameter(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_interval_absolute.pyx (starting at line 376)

        Return the diameter ``self``.

        EXAMPLES::

            sage: from sage.rings.real_interval_absolute import RealIntervalAbsoluteField
            sage: R = RealIntervalAbsoluteField(10)
            sage: R(1/4).absolute_diameter()
            0
            sage: a = R(pi)
            sage: a.absolute_diameter()
            1/1024
            sage: a.upper() - a.lower()
            1/1024"""
    @overload
    def contains_zero(self) -> bool:
        """RealIntervalAbsoluteElement.contains_zero(self) -> bool

        File: /build/sagemath/src/sage/src/sage/rings/real_interval_absolute.pyx (starting at line 524)

        Return whether ``self`` contains zero.

        EXAMPLES::

            sage: from sage.rings.real_interval_absolute import RealIntervalAbsoluteField
            sage: R = RealIntervalAbsoluteField(10)
            sage: R(10).contains_zero()
            False
            sage: R((10,11)).contains_zero()
            False
            sage: R((0,11)).contains_zero()
            True
            sage: R((-10,11)).contains_zero()
            True
            sage: R((-10,-1)).contains_zero()
            False
            sage: R((-10,0)).contains_zero()
            True
            sage: R(pi).contains_zero()
            False"""
    @overload
    def contains_zero(self) -> Any:
        """RealIntervalAbsoluteElement.contains_zero(self) -> bool

        File: /build/sagemath/src/sage/src/sage/rings/real_interval_absolute.pyx (starting at line 524)

        Return whether ``self`` contains zero.

        EXAMPLES::

            sage: from sage.rings.real_interval_absolute import RealIntervalAbsoluteField
            sage: R = RealIntervalAbsoluteField(10)
            sage: R(10).contains_zero()
            False
            sage: R((10,11)).contains_zero()
            False
            sage: R((0,11)).contains_zero()
            True
            sage: R((-10,11)).contains_zero()
            True
            sage: R((-10,-1)).contains_zero()
            False
            sage: R((-10,0)).contains_zero()
            True
            sage: R(pi).contains_zero()
            False"""
    @overload
    def contains_zero(self) -> Any:
        """RealIntervalAbsoluteElement.contains_zero(self) -> bool

        File: /build/sagemath/src/sage/src/sage/rings/real_interval_absolute.pyx (starting at line 524)

        Return whether ``self`` contains zero.

        EXAMPLES::

            sage: from sage.rings.real_interval_absolute import RealIntervalAbsoluteField
            sage: R = RealIntervalAbsoluteField(10)
            sage: R(10).contains_zero()
            False
            sage: R((10,11)).contains_zero()
            False
            sage: R((0,11)).contains_zero()
            True
            sage: R((-10,11)).contains_zero()
            True
            sage: R((-10,-1)).contains_zero()
            False
            sage: R((-10,0)).contains_zero()
            True
            sage: R(pi).contains_zero()
            False"""
    @overload
    def contains_zero(self) -> Any:
        """RealIntervalAbsoluteElement.contains_zero(self) -> bool

        File: /build/sagemath/src/sage/src/sage/rings/real_interval_absolute.pyx (starting at line 524)

        Return whether ``self`` contains zero.

        EXAMPLES::

            sage: from sage.rings.real_interval_absolute import RealIntervalAbsoluteField
            sage: R = RealIntervalAbsoluteField(10)
            sage: R(10).contains_zero()
            False
            sage: R((10,11)).contains_zero()
            False
            sage: R((0,11)).contains_zero()
            True
            sage: R((-10,11)).contains_zero()
            True
            sage: R((-10,-1)).contains_zero()
            False
            sage: R((-10,0)).contains_zero()
            True
            sage: R(pi).contains_zero()
            False"""
    @overload
    def contains_zero(self) -> Any:
        """RealIntervalAbsoluteElement.contains_zero(self) -> bool

        File: /build/sagemath/src/sage/src/sage/rings/real_interval_absolute.pyx (starting at line 524)

        Return whether ``self`` contains zero.

        EXAMPLES::

            sage: from sage.rings.real_interval_absolute import RealIntervalAbsoluteField
            sage: R = RealIntervalAbsoluteField(10)
            sage: R(10).contains_zero()
            False
            sage: R((10,11)).contains_zero()
            False
            sage: R((0,11)).contains_zero()
            True
            sage: R((-10,11)).contains_zero()
            True
            sage: R((-10,-1)).contains_zero()
            False
            sage: R((-10,0)).contains_zero()
            True
            sage: R(pi).contains_zero()
            False"""
    @overload
    def contains_zero(self) -> Any:
        """RealIntervalAbsoluteElement.contains_zero(self) -> bool

        File: /build/sagemath/src/sage/src/sage/rings/real_interval_absolute.pyx (starting at line 524)

        Return whether ``self`` contains zero.

        EXAMPLES::

            sage: from sage.rings.real_interval_absolute import RealIntervalAbsoluteField
            sage: R = RealIntervalAbsoluteField(10)
            sage: R(10).contains_zero()
            False
            sage: R((10,11)).contains_zero()
            False
            sage: R((0,11)).contains_zero()
            True
            sage: R((-10,11)).contains_zero()
            True
            sage: R((-10,-1)).contains_zero()
            False
            sage: R((-10,0)).contains_zero()
            True
            sage: R(pi).contains_zero()
            False"""
    @overload
    def contains_zero(self) -> Any:
        """RealIntervalAbsoluteElement.contains_zero(self) -> bool

        File: /build/sagemath/src/sage/src/sage/rings/real_interval_absolute.pyx (starting at line 524)

        Return whether ``self`` contains zero.

        EXAMPLES::

            sage: from sage.rings.real_interval_absolute import RealIntervalAbsoluteField
            sage: R = RealIntervalAbsoluteField(10)
            sage: R(10).contains_zero()
            False
            sage: R((10,11)).contains_zero()
            False
            sage: R((0,11)).contains_zero()
            True
            sage: R((-10,11)).contains_zero()
            True
            sage: R((-10,-1)).contains_zero()
            False
            sage: R((-10,0)).contains_zero()
            True
            sage: R(pi).contains_zero()
            False"""
    @overload
    def contains_zero(self) -> Any:
        """RealIntervalAbsoluteElement.contains_zero(self) -> bool

        File: /build/sagemath/src/sage/src/sage/rings/real_interval_absolute.pyx (starting at line 524)

        Return whether ``self`` contains zero.

        EXAMPLES::

            sage: from sage.rings.real_interval_absolute import RealIntervalAbsoluteField
            sage: R = RealIntervalAbsoluteField(10)
            sage: R(10).contains_zero()
            False
            sage: R((10,11)).contains_zero()
            False
            sage: R((0,11)).contains_zero()
            True
            sage: R((-10,11)).contains_zero()
            True
            sage: R((-10,-1)).contains_zero()
            False
            sage: R((-10,0)).contains_zero()
            True
            sage: R(pi).contains_zero()
            False"""
    def diameter(self, *args, **kwargs):
        """RealIntervalAbsoluteElement.absolute_diameter(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_interval_absolute.pyx (starting at line 376)

        Return the diameter ``self``.

        EXAMPLES::

            sage: from sage.rings.real_interval_absolute import RealIntervalAbsoluteField
            sage: R = RealIntervalAbsoluteField(10)
            sage: R(1/4).absolute_diameter()
            0
            sage: a = R(pi)
            sage: a.absolute_diameter()
            1/1024
            sage: a.upper() - a.lower()
            1/1024"""
    @overload
    def endpoints(self) -> Any:
        """RealIntervalAbsoluteElement.endpoints(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_interval_absolute.pyx (starting at line 396)

        Return the left and right endpoints of ``self``, as a tuple.

        EXAMPLES::

            sage: from sage.rings.real_interval_absolute import RealIntervalAbsoluteField
            sage: R = RealIntervalAbsoluteField(10)
            sage: R(1/4).endpoints()
            (1/4, 1/4)
            sage: R((1,2)).endpoints()
            (1, 2)"""
    @overload
    def endpoints(self) -> Any:
        """RealIntervalAbsoluteElement.endpoints(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_interval_absolute.pyx (starting at line 396)

        Return the left and right endpoints of ``self``, as a tuple.

        EXAMPLES::

            sage: from sage.rings.real_interval_absolute import RealIntervalAbsoluteField
            sage: R = RealIntervalAbsoluteField(10)
            sage: R(1/4).endpoints()
            (1/4, 1/4)
            sage: R((1,2)).endpoints()
            (1, 2)"""
    @overload
    def endpoints(self) -> Any:
        """RealIntervalAbsoluteElement.endpoints(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_interval_absolute.pyx (starting at line 396)

        Return the left and right endpoints of ``self``, as a tuple.

        EXAMPLES::

            sage: from sage.rings.real_interval_absolute import RealIntervalAbsoluteField
            sage: R = RealIntervalAbsoluteField(10)
            sage: R(1/4).endpoints()
            (1/4, 1/4)
            sage: R((1,2)).endpoints()
            (1, 2)"""
    @overload
    def is_negative(self) -> bool:
        """RealIntervalAbsoluteElement.is_negative(self) -> bool

        File: /build/sagemath/src/sage/src/sage/rings/real_interval_absolute.pyx (starting at line 550)

        Return whether ``self`` is definitely negative.

        EXAMPLES::

            sage: from sage.rings.real_interval_absolute import RealIntervalAbsoluteField
            sage: R = RealIntervalAbsoluteField(100)
            sage: R(10).is_negative()
            False
            sage: R((10,11)).is_negative()
            False
            sage: R((0,11)).is_negative()
            False
            sage: R((-10,11)).is_negative()
            False
            sage: R((-10,-1)).is_negative()
            True
            sage: R(pi).is_negative()
            False"""
    @overload
    def is_negative(self) -> Any:
        """RealIntervalAbsoluteElement.is_negative(self) -> bool

        File: /build/sagemath/src/sage/src/sage/rings/real_interval_absolute.pyx (starting at line 550)

        Return whether ``self`` is definitely negative.

        EXAMPLES::

            sage: from sage.rings.real_interval_absolute import RealIntervalAbsoluteField
            sage: R = RealIntervalAbsoluteField(100)
            sage: R(10).is_negative()
            False
            sage: R((10,11)).is_negative()
            False
            sage: R((0,11)).is_negative()
            False
            sage: R((-10,11)).is_negative()
            False
            sage: R((-10,-1)).is_negative()
            True
            sage: R(pi).is_negative()
            False"""
    @overload
    def is_negative(self) -> Any:
        """RealIntervalAbsoluteElement.is_negative(self) -> bool

        File: /build/sagemath/src/sage/src/sage/rings/real_interval_absolute.pyx (starting at line 550)

        Return whether ``self`` is definitely negative.

        EXAMPLES::

            sage: from sage.rings.real_interval_absolute import RealIntervalAbsoluteField
            sage: R = RealIntervalAbsoluteField(100)
            sage: R(10).is_negative()
            False
            sage: R((10,11)).is_negative()
            False
            sage: R((0,11)).is_negative()
            False
            sage: R((-10,11)).is_negative()
            False
            sage: R((-10,-1)).is_negative()
            True
            sage: R(pi).is_negative()
            False"""
    @overload
    def is_negative(self) -> Any:
        """RealIntervalAbsoluteElement.is_negative(self) -> bool

        File: /build/sagemath/src/sage/src/sage/rings/real_interval_absolute.pyx (starting at line 550)

        Return whether ``self`` is definitely negative.

        EXAMPLES::

            sage: from sage.rings.real_interval_absolute import RealIntervalAbsoluteField
            sage: R = RealIntervalAbsoluteField(100)
            sage: R(10).is_negative()
            False
            sage: R((10,11)).is_negative()
            False
            sage: R((0,11)).is_negative()
            False
            sage: R((-10,11)).is_negative()
            False
            sage: R((-10,-1)).is_negative()
            True
            sage: R(pi).is_negative()
            False"""
    @overload
    def is_negative(self) -> Any:
        """RealIntervalAbsoluteElement.is_negative(self) -> bool

        File: /build/sagemath/src/sage/src/sage/rings/real_interval_absolute.pyx (starting at line 550)

        Return whether ``self`` is definitely negative.

        EXAMPLES::

            sage: from sage.rings.real_interval_absolute import RealIntervalAbsoluteField
            sage: R = RealIntervalAbsoluteField(100)
            sage: R(10).is_negative()
            False
            sage: R((10,11)).is_negative()
            False
            sage: R((0,11)).is_negative()
            False
            sage: R((-10,11)).is_negative()
            False
            sage: R((-10,-1)).is_negative()
            True
            sage: R(pi).is_negative()
            False"""
    @overload
    def is_negative(self) -> Any:
        """RealIntervalAbsoluteElement.is_negative(self) -> bool

        File: /build/sagemath/src/sage/src/sage/rings/real_interval_absolute.pyx (starting at line 550)

        Return whether ``self`` is definitely negative.

        EXAMPLES::

            sage: from sage.rings.real_interval_absolute import RealIntervalAbsoluteField
            sage: R = RealIntervalAbsoluteField(100)
            sage: R(10).is_negative()
            False
            sage: R((10,11)).is_negative()
            False
            sage: R((0,11)).is_negative()
            False
            sage: R((-10,11)).is_negative()
            False
            sage: R((-10,-1)).is_negative()
            True
            sage: R(pi).is_negative()
            False"""
    @overload
    def is_negative(self) -> Any:
        """RealIntervalAbsoluteElement.is_negative(self) -> bool

        File: /build/sagemath/src/sage/src/sage/rings/real_interval_absolute.pyx (starting at line 550)

        Return whether ``self`` is definitely negative.

        EXAMPLES::

            sage: from sage.rings.real_interval_absolute import RealIntervalAbsoluteField
            sage: R = RealIntervalAbsoluteField(100)
            sage: R(10).is_negative()
            False
            sage: R((10,11)).is_negative()
            False
            sage: R((0,11)).is_negative()
            False
            sage: R((-10,11)).is_negative()
            False
            sage: R((-10,-1)).is_negative()
            True
            sage: R(pi).is_negative()
            False"""
    @overload
    def is_positive(self) -> bool:
        """RealIntervalAbsoluteElement.is_positive(self) -> bool

        File: /build/sagemath/src/sage/src/sage/rings/real_interval_absolute.pyx (starting at line 501)

        Return whether ``self`` is definitely positive.

        EXAMPLES::

            sage: from sage.rings.real_interval_absolute import RealIntervalAbsoluteField
            sage: R = RealIntervalAbsoluteField(10)
            sage: R(10).is_positive()
            True
            sage: R((10,11)).is_positive()
            True
            sage: R((0,11)).is_positive()
            False
            sage: R((-10,11)).is_positive()
            False
            sage: R((-10,-1)).is_positive()
            False
            sage: R(pi).is_positive()
            True"""
    @overload
    def is_positive(self) -> Any:
        """RealIntervalAbsoluteElement.is_positive(self) -> bool

        File: /build/sagemath/src/sage/src/sage/rings/real_interval_absolute.pyx (starting at line 501)

        Return whether ``self`` is definitely positive.

        EXAMPLES::

            sage: from sage.rings.real_interval_absolute import RealIntervalAbsoluteField
            sage: R = RealIntervalAbsoluteField(10)
            sage: R(10).is_positive()
            True
            sage: R((10,11)).is_positive()
            True
            sage: R((0,11)).is_positive()
            False
            sage: R((-10,11)).is_positive()
            False
            sage: R((-10,-1)).is_positive()
            False
            sage: R(pi).is_positive()
            True"""
    @overload
    def is_positive(self) -> Any:
        """RealIntervalAbsoluteElement.is_positive(self) -> bool

        File: /build/sagemath/src/sage/src/sage/rings/real_interval_absolute.pyx (starting at line 501)

        Return whether ``self`` is definitely positive.

        EXAMPLES::

            sage: from sage.rings.real_interval_absolute import RealIntervalAbsoluteField
            sage: R = RealIntervalAbsoluteField(10)
            sage: R(10).is_positive()
            True
            sage: R((10,11)).is_positive()
            True
            sage: R((0,11)).is_positive()
            False
            sage: R((-10,11)).is_positive()
            False
            sage: R((-10,-1)).is_positive()
            False
            sage: R(pi).is_positive()
            True"""
    @overload
    def is_positive(self) -> Any:
        """RealIntervalAbsoluteElement.is_positive(self) -> bool

        File: /build/sagemath/src/sage/src/sage/rings/real_interval_absolute.pyx (starting at line 501)

        Return whether ``self`` is definitely positive.

        EXAMPLES::

            sage: from sage.rings.real_interval_absolute import RealIntervalAbsoluteField
            sage: R = RealIntervalAbsoluteField(10)
            sage: R(10).is_positive()
            True
            sage: R((10,11)).is_positive()
            True
            sage: R((0,11)).is_positive()
            False
            sage: R((-10,11)).is_positive()
            False
            sage: R((-10,-1)).is_positive()
            False
            sage: R(pi).is_positive()
            True"""
    @overload
    def is_positive(self) -> Any:
        """RealIntervalAbsoluteElement.is_positive(self) -> bool

        File: /build/sagemath/src/sage/src/sage/rings/real_interval_absolute.pyx (starting at line 501)

        Return whether ``self`` is definitely positive.

        EXAMPLES::

            sage: from sage.rings.real_interval_absolute import RealIntervalAbsoluteField
            sage: R = RealIntervalAbsoluteField(10)
            sage: R(10).is_positive()
            True
            sage: R((10,11)).is_positive()
            True
            sage: R((0,11)).is_positive()
            False
            sage: R((-10,11)).is_positive()
            False
            sage: R((-10,-1)).is_positive()
            False
            sage: R(pi).is_positive()
            True"""
    @overload
    def is_positive(self) -> Any:
        """RealIntervalAbsoluteElement.is_positive(self) -> bool

        File: /build/sagemath/src/sage/src/sage/rings/real_interval_absolute.pyx (starting at line 501)

        Return whether ``self`` is definitely positive.

        EXAMPLES::

            sage: from sage.rings.real_interval_absolute import RealIntervalAbsoluteField
            sage: R = RealIntervalAbsoluteField(10)
            sage: R(10).is_positive()
            True
            sage: R((10,11)).is_positive()
            True
            sage: R((0,11)).is_positive()
            False
            sage: R((-10,11)).is_positive()
            False
            sage: R((-10,-1)).is_positive()
            False
            sage: R(pi).is_positive()
            True"""
    @overload
    def is_positive(self) -> Any:
        """RealIntervalAbsoluteElement.is_positive(self) -> bool

        File: /build/sagemath/src/sage/src/sage/rings/real_interval_absolute.pyx (starting at line 501)

        Return whether ``self`` is definitely positive.

        EXAMPLES::

            sage: from sage.rings.real_interval_absolute import RealIntervalAbsoluteField
            sage: R = RealIntervalAbsoluteField(10)
            sage: R(10).is_positive()
            True
            sage: R((10,11)).is_positive()
            True
            sage: R((0,11)).is_positive()
            False
            sage: R((-10,11)).is_positive()
            False
            sage: R((-10,-1)).is_positive()
            False
            sage: R(pi).is_positive()
            True"""
    @overload
    def lower(self) -> Any:
        """RealIntervalAbsoluteElement.lower(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_interval_absolute.pyx (starting at line 333)

        Return the lower bound of ``self``.

        EXAMPLES::

            sage: from sage.rings.real_interval_absolute import RealIntervalAbsoluteField
            sage: R = RealIntervalAbsoluteField(50)
            sage: R(1/4).lower()
            1/4"""
    @overload
    def lower(self) -> Any:
        """RealIntervalAbsoluteElement.lower(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_interval_absolute.pyx (starting at line 333)

        Return the lower bound of ``self``.

        EXAMPLES::

            sage: from sage.rings.real_interval_absolute import RealIntervalAbsoluteField
            sage: R = RealIntervalAbsoluteField(50)
            sage: R(1/4).lower()
            1/4"""
    @overload
    def midpoint(self) -> Any:
        """RealIntervalAbsoluteElement.midpoint(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_interval_absolute.pyx (starting at line 346)

        Return the midpoint of ``self``.

        EXAMPLES::

            sage: from sage.rings.real_interval_absolute import RealIntervalAbsoluteField
            sage: R = RealIntervalAbsoluteField(100)
            sage: R(1/4).midpoint()
            1/4
            sage: R(pi).midpoint()
            7964883625991394727376702227905/2535301200456458802993406410752
            sage: R(pi).midpoint().n()
            3.14159265358979"""
    @overload
    def midpoint(self) -> Any:
        """RealIntervalAbsoluteElement.midpoint(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_interval_absolute.pyx (starting at line 346)

        Return the midpoint of ``self``.

        EXAMPLES::

            sage: from sage.rings.real_interval_absolute import RealIntervalAbsoluteField
            sage: R = RealIntervalAbsoluteField(100)
            sage: R(1/4).midpoint()
            1/4
            sage: R(pi).midpoint()
            7964883625991394727376702227905/2535301200456458802993406410752
            sage: R(pi).midpoint().n()
            3.14159265358979"""
    @overload
    def midpoint(self) -> Any:
        """RealIntervalAbsoluteElement.midpoint(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_interval_absolute.pyx (starting at line 346)

        Return the midpoint of ``self``.

        EXAMPLES::

            sage: from sage.rings.real_interval_absolute import RealIntervalAbsoluteField
            sage: R = RealIntervalAbsoluteField(100)
            sage: R(1/4).midpoint()
            1/4
            sage: R(pi).midpoint()
            7964883625991394727376702227905/2535301200456458802993406410752
            sage: R(pi).midpoint().n()
            3.14159265358979"""
    @overload
    def midpoint(self) -> Any:
        """RealIntervalAbsoluteElement.midpoint(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_interval_absolute.pyx (starting at line 346)

        Return the midpoint of ``self``.

        EXAMPLES::

            sage: from sage.rings.real_interval_absolute import RealIntervalAbsoluteField
            sage: R = RealIntervalAbsoluteField(100)
            sage: R(1/4).midpoint()
            1/4
            sage: R(pi).midpoint()
            7964883625991394727376702227905/2535301200456458802993406410752
            sage: R(pi).midpoint().n()
            3.14159265358979"""
    @overload
    def mpfi_prec(self) -> long:
        """RealIntervalAbsoluteElement.mpfi_prec(self) -> long

        File: /build/sagemath/src/sage/src/sage/rings/real_interval_absolute.pyx (starting at line 428)

        Return the precision needed to represent this value as an mpfi interval.

        EXAMPLES::

            sage: from sage.rings.real_interval_absolute import RealIntervalAbsoluteField
            sage: R = RealIntervalAbsoluteField(10)
            sage: R(10).mpfi_prec()
            14
            sage: R(1000).mpfi_prec()
            20"""
    @overload
    def mpfi_prec(self) -> Any:
        """RealIntervalAbsoluteElement.mpfi_prec(self) -> long

        File: /build/sagemath/src/sage/src/sage/rings/real_interval_absolute.pyx (starting at line 428)

        Return the precision needed to represent this value as an mpfi interval.

        EXAMPLES::

            sage: from sage.rings.real_interval_absolute import RealIntervalAbsoluteField
            sage: R = RealIntervalAbsoluteField(10)
            sage: R(10).mpfi_prec()
            14
            sage: R(1000).mpfi_prec()
            20"""
    @overload
    def mpfi_prec(self) -> Any:
        """RealIntervalAbsoluteElement.mpfi_prec(self) -> long

        File: /build/sagemath/src/sage/src/sage/rings/real_interval_absolute.pyx (starting at line 428)

        Return the precision needed to represent this value as an mpfi interval.

        EXAMPLES::

            sage: from sage.rings.real_interval_absolute import RealIntervalAbsoluteField
            sage: R = RealIntervalAbsoluteField(10)
            sage: R(10).mpfi_prec()
            14
            sage: R(1000).mpfi_prec()
            20"""
    @overload
    def sqrt(self) -> Any:
        """RealIntervalAbsoluteElement.sqrt(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_interval_absolute.pyx (starting at line 1000)

        Return the square root of ``self``.

        EXAMPLES::

            sage: from sage.rings.real_interval_absolute import RealIntervalAbsoluteField
            sage: R = RealIntervalAbsoluteField(100)
            sage: R(2).sqrt()
            1.414213562373095048801688724210?
            sage: R((4,9)).sqrt().endpoints()
            (2, 3)"""
    @overload
    def sqrt(self) -> Any:
        """RealIntervalAbsoluteElement.sqrt(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_interval_absolute.pyx (starting at line 1000)

        Return the square root of ``self``.

        EXAMPLES::

            sage: from sage.rings.real_interval_absolute import RealIntervalAbsoluteField
            sage: R = RealIntervalAbsoluteField(100)
            sage: R(2).sqrt()
            1.414213562373095048801688724210?
            sage: R((4,9)).sqrt().endpoints()
            (2, 3)"""
    @overload
    def sqrt(self) -> Any:
        """RealIntervalAbsoluteElement.sqrt(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_interval_absolute.pyx (starting at line 1000)

        Return the square root of ``self``.

        EXAMPLES::

            sage: from sage.rings.real_interval_absolute import RealIntervalAbsoluteField
            sage: R = RealIntervalAbsoluteField(100)
            sage: R(2).sqrt()
            1.414213562373095048801688724210?
            sage: R((4,9)).sqrt().endpoints()
            (2, 3)"""
    @overload
    def upper(self) -> Any:
        """RealIntervalAbsoluteElement.upper(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_interval_absolute.pyx (starting at line 363)

        Return the upper bound of ``self``.

        EXAMPLES::

            sage: from sage.rings.real_interval_absolute import RealIntervalAbsoluteField
            sage: R = RealIntervalAbsoluteField(50)
            sage: R(1/4).upper()
            1/4"""
    @overload
    def upper(self) -> Any:
        """RealIntervalAbsoluteElement.upper(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_interval_absolute.pyx (starting at line 363)

        Return the upper bound of ``self``.

        EXAMPLES::

            sage: from sage.rings.real_interval_absolute import RealIntervalAbsoluteField
            sage: R = RealIntervalAbsoluteField(50)
            sage: R(1/4).upper()
            1/4"""
    def __abs__(self) -> Any:
        """RealIntervalAbsoluteElement.__abs__(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_interval_absolute.pyx (starting at line 607)

        EXAMPLES::

            sage: from sage.rings.real_interval_absolute import RealIntervalAbsoluteField
            sage: R = RealIntervalAbsoluteField(100)
            sage: abs(-R(1/4))
            0.2500000000000000000000000000000?"""
    def __bool__(self) -> bool:
        """True if self else False"""
    def __contains__(self, x) -> Any:
        """RealIntervalAbsoluteElement.__contains__(self, x)

        File: /build/sagemath/src/sage/src/sage/rings/real_interval_absolute.pyx (starting at line 481)

        Return whether the given value lies in this interval.

        EXAMPLES::

            sage: from sage.rings.real_interval_absolute import RealIntervalAbsoluteField
            sage: R = RealIntervalAbsoluteField(50)
            sage: 1 in R((1,2))
            True
            sage: 2 in R((1,2))
            True
            sage: 3 in R((1,2))
            False
            sage: 1.75 in R((1,2))
            True"""
    def __hash__(self) -> Any:
        """RealIntervalAbsoluteElement.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_interval_absolute.pyx (starting at line 461)

        Hash to the midpoint of the interval.

        TESTS::

            sage: from sage.rings.real_interval_absolute import RealIntervalAbsoluteField
            sage: R = RealIntervalAbsoluteField(10)
            sage: hash(R(10))
            10
            sage: hash(R((11,13)))
            12
            sage: hash(R(1/4)) == hash(1/4)
            True
            sage: hash(R(pi))
            891658780           # 32-bit
            532995478001132060  # 64-bit"""
    def __invert__(self) -> Any:
        """RealIntervalAbsoluteElement.__invert__(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_interval_absolute.pyx (starting at line 781)

        EXAMPLES::

            sage: from sage.rings.real_interval_absolute import RealIntervalAbsoluteField
            sage: R = RealIntervalAbsoluteField(10)
            sage: ~R(2)
            0.50000?
            sage: ~~R(2)
            2
            sage: ~R(3)
            0.334?
            sage: ~~R(3)
            3.00?

            sage: R = RealIntervalAbsoluteField(200)
            sage: ~R(1e10)
            1.00000000000000000000000000000000000000000000000000?e-10
            sage: ~~R(1e10)
            1.00000000000000000000000000000000000000000000000000?e10
            sage: (~R((1,2))).endpoints()
            (1/2, 1)
            sage: (~R((1/4,8))).endpoints()
            (1/8, 4)
            sage: R(1/pi) - 1/R(pi)
            0.?e-60"""
    def __lshift__(self, RealIntervalAbsoluteElementself, longn) -> Any:
        """RealIntervalAbsoluteElement.__lshift__(RealIntervalAbsoluteElement self, long n)

        File: /build/sagemath/src/sage/src/sage/rings/real_interval_absolute.pyx (starting at line 896)

        EXAMPLES::

            sage: from sage.rings.real_interval_absolute import RealIntervalAbsoluteField
            sage: R = RealIntervalAbsoluteField(10)
            sage: R(1) << 2
            4
            sage: R(3) << -2
            0.75000?
            sage: (R((1/2, 5)) << 10).endpoints()
            (512, 5120)"""
    def __neg__(self) -> Any:
        """RealIntervalAbsoluteElement.__neg__(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_interval_absolute.pyx (starting at line 594)

        TESTS::

            sage: from sage.rings.real_interval_absolute import RealIntervalAbsoluteField
            sage: R = RealIntervalAbsoluteField(100)
            sage: -R(1/2)
            -0.50000000000000000000000000000000?
            sage: -R((101,102))
            -102.?"""
    def __pow__(self, exponent, dummy) -> Any:
        """RealIntervalAbsoluteElement.__pow__(self, exponent, dummy)

        File: /build/sagemath/src/sage/src/sage/rings/real_interval_absolute.pyx (starting at line 932)

        EXAMPLES::

            sage: from sage.rings.real_interval_absolute import RealIntervalAbsoluteField
            sage: R = RealIntervalAbsoluteField(10)
            sage: R(10)^10
            10000000000
            sage: R(10)^100
            10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
            sage: R(10)^-2
            0.010?
            sage: R(10)^-10
            0.001?
            sage: R(100)^(1/2)
            10.00?
            sage: (R((2,3))^2).endpoints()
            (4, 9)
            sage: (R((-5,3))^3).endpoints()
            (-125, 75)
            sage: (R((-5,3))^4).endpoints()
            (0, 625)"""
    def __reduce__(self) -> Any:
        """RealIntervalAbsoluteElement.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_interval_absolute.pyx (starting at line 307)

        Used for pickling.

        EXAMPLES::

            sage: from sage.rings.real_interval_absolute import RealIntervalAbsoluteField
            sage: R = RealIntervalAbsoluteField(50)
            sage: loads(dumps(R(1/16)))
            0.06250000000000000?
            sage: R = RealIntervalAbsoluteField(100)
            sage: loads(dumps(R(1/3)))
            0.333333333333333333333333333334?
            sage: loads(dumps(R(pi))).endpoints() == R(pi).endpoints()
            True"""
    def __rlshift__(self, other):
        """Return value<<self."""
    def __rpow__(self, other):
        """Return pow(value, self, mod)."""
    def __rrshift__(self, other):
        """Return value>>self."""
    def __rshift__(self, RealIntervalAbsoluteElementself, longn) -> Any:
        """RealIntervalAbsoluteElement.__rshift__(RealIntervalAbsoluteElement self, long n)

        File: /build/sagemath/src/sage/src/sage/rings/real_interval_absolute.pyx (starting at line 911)

        EXAMPLES::

            sage: from sage.rings.real_interval_absolute import RealIntervalAbsoluteField
            sage: R = RealIntervalAbsoluteField(10)
            sage: R(1) >> 2
            0.2500?
            sage: R(3) >> -2
            12
            sage: (R((1/2, 5)) >> 10).endpoints()
            (0, 5/1024)"""

class RealIntervalAbsoluteField_class(sage.rings.ring.Field):
    """RealIntervalAbsoluteField_class(absprec)

    File: /build/sagemath/src/sage/src/sage/rings/real_interval_absolute.pyx (starting at line 95)

    This field is similar to the :class:`RealIntervalField` except instead of
    truncating everything to a fixed relative precision, it maintains a
    fixed absolute precision.

    Note that unlike the standard real interval field, elements in this
    field can have different size and experience coefficient blowup. On
    the other hand, it avoids precision loss on addition and subtraction.
    This is useful for, e.g., series computations for special functions.

    EXAMPLES::

            sage: from sage.rings.real_interval_absolute import RealIntervalAbsoluteField
            sage: R = RealIntervalAbsoluteField(10); R
            Real Interval Field with absolute precision 2^-10
            sage: R(3/10)
            0.300?
            sage: R(1000003/10)
            100000.300?
            sage: R(1e100) + R(1) - R(1e100)
            1"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, absprec) -> Any:
        '''File: /build/sagemath/src/sage/src/sage/rings/real_interval_absolute.pyx (starting at line 121)

                Initialize ``self``.

                EXAMPLES::

                    sage: from sage.rings.real_interval_absolute import RealIntervalAbsoluteField
                    sage: RealIntervalAbsoluteField(100)
                    Real Interval Field with absolute precision 2^-100
                    sage: RealIntervalAbsoluteField(-100)
                    Traceback (most recent call last):
                      File "<ipython console>", line 1, in <module>
                      File "real_interval_absolute.pyx", line 81, in sage.rings.real_interval_absolute.RealIntervalAbsoluteField.__init__ (sage/rings/real_interval_absolute.c:2463)
                    ValueError: Absolute precision must be positive.
        '''
    @overload
    def absprec(self) -> Any:
        """RealIntervalAbsoluteField_class.absprec(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_interval_absolute.pyx (starting at line 213)

        Return the absolute precision of ``self``.

        EXAMPLES::

            sage: from sage.rings.real_interval_absolute import RealIntervalAbsoluteField
            sage: R = RealIntervalAbsoluteField(100)
            sage: R.absprec()
            100
            sage: RealIntervalAbsoluteField(5).absprec()
            5"""
    @overload
    def absprec(self) -> Any:
        """RealIntervalAbsoluteField_class.absprec(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_interval_absolute.pyx (starting at line 213)

        Return the absolute precision of ``self``.

        EXAMPLES::

            sage: from sage.rings.real_interval_absolute import RealIntervalAbsoluteField
            sage: R = RealIntervalAbsoluteField(100)
            sage: R.absprec()
            100
            sage: RealIntervalAbsoluteField(5).absprec()
            5"""
    @overload
    def absprec(self) -> Any:
        """RealIntervalAbsoluteField_class.absprec(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_interval_absolute.pyx (starting at line 213)

        Return the absolute precision of ``self``.

        EXAMPLES::

            sage: from sage.rings.real_interval_absolute import RealIntervalAbsoluteField
            sage: R = RealIntervalAbsoluteField(100)
            sage: R.absprec()
            100
            sage: RealIntervalAbsoluteField(5).absprec()
            5"""
    def __reduce__(self) -> Any:
        """RealIntervalAbsoluteField_class.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/rings/real_interval_absolute.pyx (starting at line 141)

        Used for pickling.

        TESTS::

            sage: from sage.rings.real_interval_absolute import RealIntervalAbsoluteField
            sage: R = RealIntervalAbsoluteField(100)
            sage: loads(dumps(R))
            Real Interval Field with absolute precision 2^-100"""
