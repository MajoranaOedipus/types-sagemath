import _cython_3_2_1
import sage.structure.element
from sage.rings.infinity import infinity as infinity
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from typing import Any, ClassVar, overload

create_ComplexIntervalFieldElement: _cython_3_2_1.cython_function_or_method
is_ComplexIntervalFieldElement: _cython_3_2_1.cython_function_or_method
make_ComplexIntervalFieldElement0: _cython_3_2_1.cython_function_or_method

class ComplexIntervalFieldElement(sage.structure.element.FieldElement):
    """ComplexIntervalFieldElement(parent, real, imag=None, int base=10)

    File: /build/sagemath/src/sage/src/sage/rings/complex_interval.pyx (starting at line 100)

    A complex interval.

    EXAMPLES::

        sage: I = CIF.gen()
        sage: b = 3/2 + 5/2*I
        sage: TestSuite(b).run()"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, parent, real, imag=..., intbase=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/complex_interval.pyx (starting at line 128)

                Initialize a complex number (interval).

                EXAMPLES::

                    sage: CIF(1.5, 2.5)
                    1.5000000000000000? + 2.5000000000000000?*I
                    sage: CIF((1.5, 2.5))
                    1.5000000000000000? + 2.5000000000000000?*I
                    sage: CIF(1.5 + 2.5*I)
                    1.5000000000000000? + 2.5000000000000000?*I
        """
    @overload
    def arg(self) -> Any:
        """ComplexIntervalFieldElement.arg(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_interval.pyx (starting at line 1715)

        Same as :meth:`argument()`.

        EXAMPLES::

            sage: i = CIF.0
            sage: (i^2).arg()
            3.141592653589794?"""
    @overload
    def arg(self) -> Any:
        """ComplexIntervalFieldElement.arg(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_interval.pyx (starting at line 1715)

        Same as :meth:`argument()`.

        EXAMPLES::

            sage: i = CIF.0
            sage: (i^2).arg()
            3.141592653589794?"""
    @overload
    def argument(self) -> Any:
        """ComplexIntervalFieldElement.argument(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_interval.pyx (starting at line 1611)

        The argument (angle) of the complex number, normalized
        so that `-\\pi < \\theta.lower() \\leq \\pi`.

        We raise a :exc:`ValueError` if the interval strictly contains 0,
        or if the interval contains only 0.

        .. WARNING::

            We do not always use the standard branch cut for
            argument!  If the interval crosses the negative real axis,
            then the argument will be an interval whose lower bound is
            less than `\\pi` and whose upper bound is more than `\\pi`; in
            effect, we move the branch cut away from the interval.

        EXAMPLES::

            sage: i = CIF.0
            sage: (i^2).argument()
            3.141592653589794?
            sage: (1+i).argument()
            0.785398163397449?
            sage: i.argument()
            1.570796326794897?
            sage: (-i).argument()
            -1.570796326794897?
            sage: (-1/1000 - i).argument()
            -1.571796326461564?
            sage: CIF(2).argument()
            0
            sage: CIF(-2).argument()
            3.141592653589794?

        Here we see that if the interval crosses the negative real
        axis, then the argument can exceed `\\pi`, and we
        we violate the standard interval guarantees in the process::

            sage: CIF(-2, RIF(-0.1, 0.1)).argument().str(style='brackets')
            '[3.0916342578678501 .. 3.1915510493117365]'
            sage: CIF(-2, -0.1).argument()
            -3.091634257867851?"""
    @overload
    def argument(self, angle) -> Any:
        """ComplexIntervalFieldElement.argument(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_interval.pyx (starting at line 1611)

        The argument (angle) of the complex number, normalized
        so that `-\\pi < \\theta.lower() \\leq \\pi`.

        We raise a :exc:`ValueError` if the interval strictly contains 0,
        or if the interval contains only 0.

        .. WARNING::

            We do not always use the standard branch cut for
            argument!  If the interval crosses the negative real axis,
            then the argument will be an interval whose lower bound is
            less than `\\pi` and whose upper bound is more than `\\pi`; in
            effect, we move the branch cut away from the interval.

        EXAMPLES::

            sage: i = CIF.0
            sage: (i^2).argument()
            3.141592653589794?
            sage: (1+i).argument()
            0.785398163397449?
            sage: i.argument()
            1.570796326794897?
            sage: (-i).argument()
            -1.570796326794897?
            sage: (-1/1000 - i).argument()
            -1.571796326461564?
            sage: CIF(2).argument()
            0
            sage: CIF(-2).argument()
            3.141592653589794?

        Here we see that if the interval crosses the negative real
        axis, then the argument can exceed `\\pi`, and we
        we violate the standard interval guarantees in the process::

            sage: CIF(-2, RIF(-0.1, 0.1)).argument().str(style='brackets')
            '[3.0916342578678501 .. 3.1915510493117365]'
            sage: CIF(-2, -0.1).argument()
            -3.091634257867851?"""
    @overload
    def bisection(self) -> Any:
        """ComplexIntervalFieldElement.bisection(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_interval.pyx (starting at line 342)

        Return the bisection of ``self`` into four intervals whose union is
        ``self`` and intersection is :meth:`center()`.

        EXAMPLES::

            sage: z = CIF(RIF(2, 3), RIF(-5, -4))
            sage: z.bisection()
            (3.? - 5.?*I, 3.? - 5.?*I, 3.? - 5.?*I, 3.? - 5.?*I)
            sage: for z in z.bisection():
            ....:     print(z.real().endpoints())
            ....:     print(z.imag().endpoints())
            (2.00000000000000, 2.50000000000000)
            (-5.00000000000000, -4.50000000000000)
            (2.50000000000000, 3.00000000000000)
            (-5.00000000000000, -4.50000000000000)
            (2.00000000000000, 2.50000000000000)
            (-4.50000000000000, -4.00000000000000)
            (2.50000000000000, 3.00000000000000)
            (-4.50000000000000, -4.00000000000000)

            sage: # needs sage.symbolic
            sage: z = CIF(RIF(sqrt(2), sqrt(3)), RIF(e, pi))
            sage: a, b, c, d = z.bisection()
            sage: a.intersection(b).intersection(c).intersection(d) == CIF(z.center())
            True
            sage: zz = a.union(b).union(c).union(c)
            sage: zz.real().endpoints() == z.real().endpoints()
            True
            sage: zz.imag().endpoints() == z.imag().endpoints()
            True"""
    @overload
    def bisection(self) -> Any:
        """ComplexIntervalFieldElement.bisection(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_interval.pyx (starting at line 342)

        Return the bisection of ``self`` into four intervals whose union is
        ``self`` and intersection is :meth:`center()`.

        EXAMPLES::

            sage: z = CIF(RIF(2, 3), RIF(-5, -4))
            sage: z.bisection()
            (3.? - 5.?*I, 3.? - 5.?*I, 3.? - 5.?*I, 3.? - 5.?*I)
            sage: for z in z.bisection():
            ....:     print(z.real().endpoints())
            ....:     print(z.imag().endpoints())
            (2.00000000000000, 2.50000000000000)
            (-5.00000000000000, -4.50000000000000)
            (2.50000000000000, 3.00000000000000)
            (-5.00000000000000, -4.50000000000000)
            (2.00000000000000, 2.50000000000000)
            (-4.50000000000000, -4.00000000000000)
            (2.50000000000000, 3.00000000000000)
            (-4.50000000000000, -4.00000000000000)

            sage: # needs sage.symbolic
            sage: z = CIF(RIF(sqrt(2), sqrt(3)), RIF(e, pi))
            sage: a, b, c, d = z.bisection()
            sage: a.intersection(b).intersection(c).intersection(d) == CIF(z.center())
            True
            sage: zz = a.union(b).union(c).union(c)
            sage: zz.real().endpoints() == z.real().endpoints()
            True
            sage: zz.imag().endpoints() == z.imag().endpoints()
            True"""
    @overload
    def bisection(self) -> Any:
        """ComplexIntervalFieldElement.bisection(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_interval.pyx (starting at line 342)

        Return the bisection of ``self`` into four intervals whose union is
        ``self`` and intersection is :meth:`center()`.

        EXAMPLES::

            sage: z = CIF(RIF(2, 3), RIF(-5, -4))
            sage: z.bisection()
            (3.? - 5.?*I, 3.? - 5.?*I, 3.? - 5.?*I, 3.? - 5.?*I)
            sage: for z in z.bisection():
            ....:     print(z.real().endpoints())
            ....:     print(z.imag().endpoints())
            (2.00000000000000, 2.50000000000000)
            (-5.00000000000000, -4.50000000000000)
            (2.50000000000000, 3.00000000000000)
            (-5.00000000000000, -4.50000000000000)
            (2.00000000000000, 2.50000000000000)
            (-4.50000000000000, -4.00000000000000)
            (2.50000000000000, 3.00000000000000)
            (-4.50000000000000, -4.00000000000000)

            sage: # needs sage.symbolic
            sage: z = CIF(RIF(sqrt(2), sqrt(3)), RIF(e, pi))
            sage: a, b, c, d = z.bisection()
            sage: a.intersection(b).intersection(c).intersection(d) == CIF(z.center())
            True
            sage: zz = a.union(b).union(c).union(c)
            sage: zz.real().endpoints() == z.real().endpoints()
            True
            sage: zz.imag().endpoints() == z.imag().endpoints()
            True"""
    @overload
    def bisection(self) -> Any:
        """ComplexIntervalFieldElement.bisection(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_interval.pyx (starting at line 342)

        Return the bisection of ``self`` into four intervals whose union is
        ``self`` and intersection is :meth:`center()`.

        EXAMPLES::

            sage: z = CIF(RIF(2, 3), RIF(-5, -4))
            sage: z.bisection()
            (3.? - 5.?*I, 3.? - 5.?*I, 3.? - 5.?*I, 3.? - 5.?*I)
            sage: for z in z.bisection():
            ....:     print(z.real().endpoints())
            ....:     print(z.imag().endpoints())
            (2.00000000000000, 2.50000000000000)
            (-5.00000000000000, -4.50000000000000)
            (2.50000000000000, 3.00000000000000)
            (-5.00000000000000, -4.50000000000000)
            (2.00000000000000, 2.50000000000000)
            (-4.50000000000000, -4.00000000000000)
            (2.50000000000000, 3.00000000000000)
            (-4.50000000000000, -4.00000000000000)

            sage: # needs sage.symbolic
            sage: z = CIF(RIF(sqrt(2), sqrt(3)), RIF(e, pi))
            sage: a, b, c, d = z.bisection()
            sage: a.intersection(b).intersection(c).intersection(d) == CIF(z.center())
            True
            sage: zz = a.union(b).union(c).union(c)
            sage: zz.real().endpoints() == z.real().endpoints()
            True
            sage: zz.imag().endpoints() == z.imag().endpoints()
            True"""
    @overload
    def center(self) -> Any:
        """ComplexIntervalFieldElement.center(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_interval.pyx (starting at line 650)

        Return the closest floating-point approximation to the center
        of the interval.

        EXAMPLES::

            sage: CIF(RIF(1, 2), RIF(3, 4)).center()
            1.50000000000000 + 3.50000000000000*I"""
    @overload
    def center(self) -> Any:
        """ComplexIntervalFieldElement.center(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_interval.pyx (starting at line 650)

        Return the closest floating-point approximation to the center
        of the interval.

        EXAMPLES::

            sage: CIF(RIF(1, 2), RIF(3, 4)).center()
            1.50000000000000 + 3.50000000000000*I"""
    @overload
    def conjugate(self) -> Any:
        """ComplexIntervalFieldElement.conjugate(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_interval.pyx (starting at line 1752)

        Return the complex conjugate of this complex number.

        EXAMPLES::

            sage: i = CIF.0
            sage: (1+i).conjugate()
            1 - 1*I"""
    @overload
    def conjugate(self) -> Any:
        """ComplexIntervalFieldElement.conjugate(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_interval.pyx (starting at line 1752)

        Return the complex conjugate of this complex number.

        EXAMPLES::

            sage: i = CIF.0
            sage: (1+i).conjugate()
            1 - 1*I"""
    @overload
    def contains_zero(self) -> Any:
        """ComplexIntervalFieldElement.contains_zero(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_interval.pyx (starting at line 679)

        Return ``True`` if ``self`` is an interval containing zero.

        EXAMPLES::

            sage: CIF(0).contains_zero()
            True
            sage: CIF(RIF(-1, 1), 1).contains_zero()
            False"""
    @overload
    def contains_zero(self) -> Any:
        """ComplexIntervalFieldElement.contains_zero(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_interval.pyx (starting at line 679)

        Return ``True`` if ``self`` is an interval containing zero.

        EXAMPLES::

            sage: CIF(0).contains_zero()
            True
            sage: CIF(RIF(-1, 1), 1).contains_zero()
            False"""
    @overload
    def contains_zero(self) -> Any:
        """ComplexIntervalFieldElement.contains_zero(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_interval.pyx (starting at line 679)

        Return ``True`` if ``self`` is an interval containing zero.

        EXAMPLES::

            sage: CIF(0).contains_zero()
            True
            sage: CIF(RIF(-1, 1), 1).contains_zero()
            False"""
    @overload
    def cos(self) -> Any:
        """ComplexIntervalFieldElement.cos(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_interval.pyx (starting at line 1922)

        Compute the cosine of this complex interval.

        EXAMPLES::

            sage: CIF(1,1).cos()
            0.833730025131149? - 0.988897705762865?*I
            sage: CIF(3).cos()
            -0.9899924966004455?
            sage: CIF(0,2).cos()
            3.762195691083632?

        Check that :issue:`17285` is fixed::

            sage: CIF(cos(2/3))                                                         # needs sage.symbolic
            0.7858872607769480?

        ALGORITHM:

        The implementation uses the following trigonometric identity

        .. MATH::

            \\cos(x + iy) = \\cos(x) \\cosh(y) - i \\sin(x) \\sinh(y)"""
    @overload
    def cos(self) -> Any:
        """ComplexIntervalFieldElement.cos(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_interval.pyx (starting at line 1922)

        Compute the cosine of this complex interval.

        EXAMPLES::

            sage: CIF(1,1).cos()
            0.833730025131149? - 0.988897705762865?*I
            sage: CIF(3).cos()
            -0.9899924966004455?
            sage: CIF(0,2).cos()
            3.762195691083632?

        Check that :issue:`17285` is fixed::

            sage: CIF(cos(2/3))                                                         # needs sage.symbolic
            0.7858872607769480?

        ALGORITHM:

        The implementation uses the following trigonometric identity

        .. MATH::

            \\cos(x + iy) = \\cos(x) \\cosh(y) - i \\sin(x) \\sinh(y)"""
    @overload
    def cos(self) -> Any:
        """ComplexIntervalFieldElement.cos(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_interval.pyx (starting at line 1922)

        Compute the cosine of this complex interval.

        EXAMPLES::

            sage: CIF(1,1).cos()
            0.833730025131149? - 0.988897705762865?*I
            sage: CIF(3).cos()
            -0.9899924966004455?
            sage: CIF(0,2).cos()
            3.762195691083632?

        Check that :issue:`17285` is fixed::

            sage: CIF(cos(2/3))                                                         # needs sage.symbolic
            0.7858872607769480?

        ALGORITHM:

        The implementation uses the following trigonometric identity

        .. MATH::

            \\cos(x + iy) = \\cos(x) \\cosh(y) - i \\sin(x) \\sinh(y)"""
    @overload
    def cos(self) -> Any:
        """ComplexIntervalFieldElement.cos(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_interval.pyx (starting at line 1922)

        Compute the cosine of this complex interval.

        EXAMPLES::

            sage: CIF(1,1).cos()
            0.833730025131149? - 0.988897705762865?*I
            sage: CIF(3).cos()
            -0.9899924966004455?
            sage: CIF(0,2).cos()
            3.762195691083632?

        Check that :issue:`17285` is fixed::

            sage: CIF(cos(2/3))                                                         # needs sage.symbolic
            0.7858872607769480?

        ALGORITHM:

        The implementation uses the following trigonometric identity

        .. MATH::

            \\cos(x + iy) = \\cos(x) \\cosh(y) - i \\sin(x) \\sinh(y)"""
    @overload
    def cosh(self) -> Any:
        """ComplexIntervalFieldElement.cosh(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_interval.pyx (starting at line 2020)

        Return the hyperbolic cosine of this complex interval.

        EXAMPLES::

            sage: CIF(1,1).cosh()
            0.833730025131149? + 0.988897705762865?*I
            sage: CIF(2).cosh()
            3.762195691083632?
            sage: CIF(0,2).cosh()
            -0.4161468365471424?

        ALGORITHM:

        The implementation uses the following trigonometric identity

        .. MATH::

            \\cosh(x+iy) = \\cos(y) \\cosh(x) + i \\sin(y) \\sinh(x)"""
    @overload
    def cosh(self) -> Any:
        """ComplexIntervalFieldElement.cosh(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_interval.pyx (starting at line 2020)

        Return the hyperbolic cosine of this complex interval.

        EXAMPLES::

            sage: CIF(1,1).cosh()
            0.833730025131149? + 0.988897705762865?*I
            sage: CIF(2).cosh()
            3.762195691083632?
            sage: CIF(0,2).cosh()
            -0.4161468365471424?

        ALGORITHM:

        The implementation uses the following trigonometric identity

        .. MATH::

            \\cosh(x+iy) = \\cos(y) \\cosh(x) + i \\sin(y) \\sinh(x)"""
    @overload
    def cosh(self) -> Any:
        """ComplexIntervalFieldElement.cosh(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_interval.pyx (starting at line 2020)

        Return the hyperbolic cosine of this complex interval.

        EXAMPLES::

            sage: CIF(1,1).cosh()
            0.833730025131149? + 0.988897705762865?*I
            sage: CIF(2).cosh()
            3.762195691083632?
            sage: CIF(0,2).cosh()
            -0.4161468365471424?

        ALGORITHM:

        The implementation uses the following trigonometric identity

        .. MATH::

            \\cosh(x+iy) = \\cos(y) \\cosh(x) + i \\sin(y) \\sinh(x)"""
    @overload
    def cosh(self) -> Any:
        """ComplexIntervalFieldElement.cosh(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_interval.pyx (starting at line 2020)

        Return the hyperbolic cosine of this complex interval.

        EXAMPLES::

            sage: CIF(1,1).cosh()
            0.833730025131149? + 0.988897705762865?*I
            sage: CIF(2).cosh()
            3.762195691083632?
            sage: CIF(0,2).cosh()
            -0.4161468365471424?

        ALGORITHM:

        The implementation uses the following trigonometric identity

        .. MATH::

            \\cosh(x+iy) = \\cos(y) \\cosh(x) + i \\sin(y) \\sinh(x)"""
    @overload
    def crosses_log_branch_cut(self) -> Any:
        """ComplexIntervalFieldElement.crosses_log_branch_cut(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_interval.pyx (starting at line 1727)

        Return ``True`` if this interval crosses the standard branch cut
        for :meth:`log()` (and hence for exponentiation) and for argument.
        (Recall that this branch cut is infinitesimally below the
        negative portion of the real axis.)

        EXAMPLES::

            sage: z = CIF(1.5, 2.5) - CIF(0, 2.50000000000000001); z
            1.5000000000000000? + -1.?e-15*I
            sage: z.crosses_log_branch_cut()
            False
            sage: CIF(-2, RIF(-0.1, 0.1)).crosses_log_branch_cut()
            True"""
    @overload
    def crosses_log_branch_cut(self) -> Any:
        """ComplexIntervalFieldElement.crosses_log_branch_cut(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_interval.pyx (starting at line 1727)

        Return ``True`` if this interval crosses the standard branch cut
        for :meth:`log()` (and hence for exponentiation) and for argument.
        (Recall that this branch cut is infinitesimally below the
        negative portion of the real axis.)

        EXAMPLES::

            sage: z = CIF(1.5, 2.5) - CIF(0, 2.50000000000000001); z
            1.5000000000000000? + -1.?e-15*I
            sage: z.crosses_log_branch_cut()
            False
            sage: CIF(-2, RIF(-0.1, 0.1)).crosses_log_branch_cut()
            True"""
    @overload
    def crosses_log_branch_cut(self) -> Any:
        """ComplexIntervalFieldElement.crosses_log_branch_cut(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_interval.pyx (starting at line 1727)

        Return ``True`` if this interval crosses the standard branch cut
        for :meth:`log()` (and hence for exponentiation) and for argument.
        (Recall that this branch cut is infinitesimally below the
        negative portion of the real axis.)

        EXAMPLES::

            sage: z = CIF(1.5, 2.5) - CIF(0, 2.50000000000000001); z
            1.5000000000000000? + -1.?e-15*I
            sage: z.crosses_log_branch_cut()
            False
            sage: CIF(-2, RIF(-0.1, 0.1)).crosses_log_branch_cut()
            True"""
    @overload
    def diameter(self) -> Any:
        '''ComplexIntervalFieldElement.diameter(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_interval.pyx (starting at line 505)

        Return a somewhat-arbitrarily defined "diameter" for this interval.

        The diameter of an interval is the maximum of the diameter of the real
        and imaginary components, where diameter on a real interval is defined
        as absolute diameter if the interval contains zero, and relative
        diameter otherwise.

        EXAMPLES::

            sage: CIF(RIF(-1, 1), RIF(13, 17)).diameter()
            2.00000000000000
            sage: CIF(RIF(-0.1, 0.1), RIF(13, 17)).diameter()
            0.266666666666667
            sage: CIF(RIF(-1, 1), 15).diameter()
            2.00000000000000'''
    @overload
    def diameter(self) -> Any:
        '''ComplexIntervalFieldElement.diameter(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_interval.pyx (starting at line 505)

        Return a somewhat-arbitrarily defined "diameter" for this interval.

        The diameter of an interval is the maximum of the diameter of the real
        and imaginary components, where diameter on a real interval is defined
        as absolute diameter if the interval contains zero, and relative
        diameter otherwise.

        EXAMPLES::

            sage: CIF(RIF(-1, 1), RIF(13, 17)).diameter()
            2.00000000000000
            sage: CIF(RIF(-0.1, 0.1), RIF(13, 17)).diameter()
            0.266666666666667
            sage: CIF(RIF(-1, 1), 15).diameter()
            2.00000000000000'''
    @overload
    def diameter(self) -> Any:
        '''ComplexIntervalFieldElement.diameter(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_interval.pyx (starting at line 505)

        Return a somewhat-arbitrarily defined "diameter" for this interval.

        The diameter of an interval is the maximum of the diameter of the real
        and imaginary components, where diameter on a real interval is defined
        as absolute diameter if the interval contains zero, and relative
        diameter otherwise.

        EXAMPLES::

            sage: CIF(RIF(-1, 1), RIF(13, 17)).diameter()
            2.00000000000000
            sage: CIF(RIF(-0.1, 0.1), RIF(13, 17)).diameter()
            0.266666666666667
            sage: CIF(RIF(-1, 1), 15).diameter()
            2.00000000000000'''
    @overload
    def diameter(self) -> Any:
        '''ComplexIntervalFieldElement.diameter(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_interval.pyx (starting at line 505)

        Return a somewhat-arbitrarily defined "diameter" for this interval.

        The diameter of an interval is the maximum of the diameter of the real
        and imaginary components, where diameter on a real interval is defined
        as absolute diameter if the interval contains zero, and relative
        diameter otherwise.

        EXAMPLES::

            sage: CIF(RIF(-1, 1), RIF(13, 17)).diameter()
            2.00000000000000
            sage: CIF(RIF(-0.1, 0.1), RIF(13, 17)).diameter()
            0.266666666666667
            sage: CIF(RIF(-1, 1), 15).diameter()
            2.00000000000000'''
    @overload
    def edges(self) -> Any:
        """ComplexIntervalFieldElement.edges(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_interval.pyx (starting at line 455)

        Return the 4 edges of the rectangle in the complex plane
        defined by this interval as intervals.

        OUTPUT: a 4-tuple of complex intervals
        (left edge, right edge, lower edge, upper edge)

        .. SEEALSO::

            :meth:`endpoints` which returns the 4 corners of the
            rectangle.

        EXAMPLES::

            sage: CIF(RIF(1,2), RIF(3,4)).edges()
            (1 + 4.?*I, 2 + 4.?*I, 2.? + 3*I, 2.? + 4*I)
            sage: ComplexIntervalField(20)(-2).log().edges()
            (0.69314671? + 3.14160?*I,
             0.69314766? + 3.14160?*I,
             0.693147? + 3.1415902?*I,
             0.693147? + 3.1415940?*I)"""
    @overload
    def edges(self) -> Any:
        """ComplexIntervalFieldElement.edges(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_interval.pyx (starting at line 455)

        Return the 4 edges of the rectangle in the complex plane
        defined by this interval as intervals.

        OUTPUT: a 4-tuple of complex intervals
        (left edge, right edge, lower edge, upper edge)

        .. SEEALSO::

            :meth:`endpoints` which returns the 4 corners of the
            rectangle.

        EXAMPLES::

            sage: CIF(RIF(1,2), RIF(3,4)).edges()
            (1 + 4.?*I, 2 + 4.?*I, 2.? + 3*I, 2.? + 4*I)
            sage: ComplexIntervalField(20)(-2).log().edges()
            (0.69314671? + 3.14160?*I,
             0.69314766? + 3.14160?*I,
             0.693147? + 3.1415902?*I,
             0.693147? + 3.1415940?*I)"""
    @overload
    def edges(self) -> Any:
        """ComplexIntervalFieldElement.edges(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_interval.pyx (starting at line 455)

        Return the 4 edges of the rectangle in the complex plane
        defined by this interval as intervals.

        OUTPUT: a 4-tuple of complex intervals
        (left edge, right edge, lower edge, upper edge)

        .. SEEALSO::

            :meth:`endpoints` which returns the 4 corners of the
            rectangle.

        EXAMPLES::

            sage: CIF(RIF(1,2), RIF(3,4)).edges()
            (1 + 4.?*I, 2 + 4.?*I, 2.? + 3*I, 2.? + 4*I)
            sage: ComplexIntervalField(20)(-2).log().edges()
            (0.69314671? + 3.14160?*I,
             0.69314766? + 3.14160?*I,
             0.693147? + 3.1415902?*I,
             0.693147? + 3.1415940?*I)"""
    @overload
    def endpoints(self) -> Any:
        """ComplexIntervalFieldElement.endpoints(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_interval.pyx (starting at line 424)

        Return the 4 corners of the rectangle in the complex plane
        defined by this interval.

        OUTPUT: a 4-tuple of complex numbers
        (lower left, upper right, upper left, lower right)

        .. SEEALSO::

            :meth:`edges` which returns the 4 edges of the rectangle.

        EXAMPLES::

            sage: CIF(RIF(1,2), RIF(3,4)).endpoints()
            (1.00000000000000 + 3.00000000000000*I,
             2.00000000000000 + 4.00000000000000*I,
             1.00000000000000 + 4.00000000000000*I,
             2.00000000000000 + 3.00000000000000*I)
            sage: ComplexIntervalField(20)(-2).log().endpoints()
            (0.69315 + 3.1416*I,
             0.69315 + 3.1416*I,
             0.69315 + 3.1416*I,
             0.69315 + 3.1416*I)"""
    @overload
    def endpoints(self) -> Any:
        """ComplexIntervalFieldElement.endpoints(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_interval.pyx (starting at line 424)

        Return the 4 corners of the rectangle in the complex plane
        defined by this interval.

        OUTPUT: a 4-tuple of complex numbers
        (lower left, upper right, upper left, lower right)

        .. SEEALSO::

            :meth:`edges` which returns the 4 edges of the rectangle.

        EXAMPLES::

            sage: CIF(RIF(1,2), RIF(3,4)).endpoints()
            (1.00000000000000 + 3.00000000000000*I,
             2.00000000000000 + 4.00000000000000*I,
             1.00000000000000 + 4.00000000000000*I,
             2.00000000000000 + 3.00000000000000*I)
            sage: ComplexIntervalField(20)(-2).log().endpoints()
            (0.69315 + 3.1416*I,
             0.69315 + 3.1416*I,
             0.69315 + 3.1416*I,
             0.69315 + 3.1416*I)"""
    @overload
    def endpoints(self) -> Any:
        """ComplexIntervalFieldElement.endpoints(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_interval.pyx (starting at line 424)

        Return the 4 corners of the rectangle in the complex plane
        defined by this interval.

        OUTPUT: a 4-tuple of complex numbers
        (lower left, upper right, upper left, lower right)

        .. SEEALSO::

            :meth:`edges` which returns the 4 edges of the rectangle.

        EXAMPLES::

            sage: CIF(RIF(1,2), RIF(3,4)).endpoints()
            (1.00000000000000 + 3.00000000000000*I,
             2.00000000000000 + 4.00000000000000*I,
             1.00000000000000 + 4.00000000000000*I,
             2.00000000000000 + 3.00000000000000*I)
            sage: ComplexIntervalField(20)(-2).log().endpoints()
            (0.69315 + 3.1416*I,
             0.69315 + 3.1416*I,
             0.69315 + 3.1416*I,
             0.69315 + 3.1416*I)"""
    def exp(self) -> Any:
        """ComplexIntervalFieldElement.exp(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_interval.pyx (starting at line 1768)

        Compute `e^z` or `\\exp(z)` where `z` is the complex number ``self``.

        EXAMPLES::

            sage: i = ComplexIntervalField(300).0
            sage: z = 1 + i
            sage: z.exp()
            1.46869393991588515713896759732660426132695673662900872279767567631093696585951213872272450? + 2.28735528717884239120817190670050180895558625666835568093865811410364716018934540926734485?*I"""
    @overload
    def imag(self) -> Any:
        """ComplexIntervalFieldElement.imag(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_interval.pyx (starting at line 1057)

        Return imaginary part of ``self``.

        EXAMPLES::

            sage: i = ComplexIntervalField(100).0
            sage: z = 2 + 3*i
            sage: x = z.imag(); x
            3
            sage: x.parent()
            Real Interval Field with 100 bits of precision"""
    @overload
    def imag(self) -> Any:
        """ComplexIntervalFieldElement.imag(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_interval.pyx (starting at line 1057)

        Return imaginary part of ``self``.

        EXAMPLES::

            sage: i = ComplexIntervalField(100).0
            sage: z = 2 + 3*i
            sage: x = z.imag(); x
            3
            sage: x.parent()
            Real Interval Field with 100 bits of precision"""
    def intersection(self, other) -> Any:
        """ComplexIntervalFieldElement.intersection(self, other)

        File: /build/sagemath/src/sage/src/sage/rings/complex_interval.pyx (starting at line 550)

        Return the intersection of the two complex intervals ``self`` and
        ``other``.

        EXAMPLES::

            sage: CIF(RIF(1, 3), RIF(1, 3)).intersection(CIF(RIF(2, 4), RIF(2, 4))).str(style='brackets')
            '[2.0000000000000000 .. 3.0000000000000000] + [2.0000000000000000 .. 3.0000000000000000]*I'
            sage: CIF(RIF(1, 2), RIF(1, 3)).intersection(CIF(RIF(3, 4), RIF(2, 4)))
            Traceback (most recent call last):
            ...
            ValueError: intersection of non-overlapping intervals"""
    @overload
    def is_NaN(self) -> Any:
        """ComplexIntervalFieldElement.is_NaN(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_interval.pyx (starting at line 1907)

        Return ``True`` if this is not-a-number.

        EXAMPLES::

            sage: CIF(2, 1).is_NaN()
            False
            sage: CIF(NaN).is_NaN()                                                     # needs sage.symbolic
            True
            sage: (1 / CIF(0, 0)).is_NaN()
            True"""
    @overload
    def is_NaN(self) -> Any:
        """ComplexIntervalFieldElement.is_NaN(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_interval.pyx (starting at line 1907)

        Return ``True`` if this is not-a-number.

        EXAMPLES::

            sage: CIF(2, 1).is_NaN()
            False
            sage: CIF(NaN).is_NaN()                                                     # needs sage.symbolic
            True
            sage: (1 / CIF(0, 0)).is_NaN()
            True"""
    @overload
    def is_NaN(self) -> Any:
        """ComplexIntervalFieldElement.is_NaN(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_interval.pyx (starting at line 1907)

        Return ``True`` if this is not-a-number.

        EXAMPLES::

            sage: CIF(2, 1).is_NaN()
            False
            sage: CIF(NaN).is_NaN()                                                     # needs sage.symbolic
            True
            sage: (1 / CIF(0, 0)).is_NaN()
            True"""
    @overload
    def is_NaN(self) -> Any:
        """ComplexIntervalFieldElement.is_NaN(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_interval.pyx (starting at line 1907)

        Return ``True`` if this is not-a-number.

        EXAMPLES::

            sage: CIF(2, 1).is_NaN()
            False
            sage: CIF(NaN).is_NaN()                                                     # needs sage.symbolic
            True
            sage: (1 / CIF(0, 0)).is_NaN()
            True"""
    @overload
    def is_exact(self) -> Any:
        """ComplexIntervalFieldElement.is_exact(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_interval.pyx (starting at line 397)

        Return whether this complex interval is exact (i.e. contains exactly
        one complex value).

        EXAMPLES::

            sage: CIF(3).is_exact()
            True
            sage: CIF(0, 2).is_exact()
            True
            sage: CIF(-4, 0).sqrt().is_exact()
            True
            sage: CIF(-5, 0).sqrt().is_exact()
            False
            sage: CIF(0, 2*pi).is_exact()                                               # needs sage.symbolic
            False
            sage: CIF(e).is_exact()                                                     # needs sage.symbolic
            False
            sage: CIF(1e100).is_exact()
            True
            sage: (CIF(1e100) + 1).is_exact()
            False"""
    @overload
    def is_exact(self) -> Any:
        """ComplexIntervalFieldElement.is_exact(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_interval.pyx (starting at line 397)

        Return whether this complex interval is exact (i.e. contains exactly
        one complex value).

        EXAMPLES::

            sage: CIF(3).is_exact()
            True
            sage: CIF(0, 2).is_exact()
            True
            sage: CIF(-4, 0).sqrt().is_exact()
            True
            sage: CIF(-5, 0).sqrt().is_exact()
            False
            sage: CIF(0, 2*pi).is_exact()                                               # needs sage.symbolic
            False
            sage: CIF(e).is_exact()                                                     # needs sage.symbolic
            False
            sage: CIF(1e100).is_exact()
            True
            sage: (CIF(1e100) + 1).is_exact()
            False"""
    @overload
    def is_exact(self) -> Any:
        """ComplexIntervalFieldElement.is_exact(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_interval.pyx (starting at line 397)

        Return whether this complex interval is exact (i.e. contains exactly
        one complex value).

        EXAMPLES::

            sage: CIF(3).is_exact()
            True
            sage: CIF(0, 2).is_exact()
            True
            sage: CIF(-4, 0).sqrt().is_exact()
            True
            sage: CIF(-5, 0).sqrt().is_exact()
            False
            sage: CIF(0, 2*pi).is_exact()                                               # needs sage.symbolic
            False
            sage: CIF(e).is_exact()                                                     # needs sage.symbolic
            False
            sage: CIF(1e100).is_exact()
            True
            sage: (CIF(1e100) + 1).is_exact()
            False"""
    @overload
    def is_exact(self) -> Any:
        """ComplexIntervalFieldElement.is_exact(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_interval.pyx (starting at line 397)

        Return whether this complex interval is exact (i.e. contains exactly
        one complex value).

        EXAMPLES::

            sage: CIF(3).is_exact()
            True
            sage: CIF(0, 2).is_exact()
            True
            sage: CIF(-4, 0).sqrt().is_exact()
            True
            sage: CIF(-5, 0).sqrt().is_exact()
            False
            sage: CIF(0, 2*pi).is_exact()                                               # needs sage.symbolic
            False
            sage: CIF(e).is_exact()                                                     # needs sage.symbolic
            False
            sage: CIF(1e100).is_exact()
            True
            sage: (CIF(1e100) + 1).is_exact()
            False"""
    @overload
    def is_exact(self) -> Any:
        """ComplexIntervalFieldElement.is_exact(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_interval.pyx (starting at line 397)

        Return whether this complex interval is exact (i.e. contains exactly
        one complex value).

        EXAMPLES::

            sage: CIF(3).is_exact()
            True
            sage: CIF(0, 2).is_exact()
            True
            sage: CIF(-4, 0).sqrt().is_exact()
            True
            sage: CIF(-5, 0).sqrt().is_exact()
            False
            sage: CIF(0, 2*pi).is_exact()                                               # needs sage.symbolic
            False
            sage: CIF(e).is_exact()                                                     # needs sage.symbolic
            False
            sage: CIF(1e100).is_exact()
            True
            sage: (CIF(1e100) + 1).is_exact()
            False"""
    @overload
    def is_exact(self) -> Any:
        """ComplexIntervalFieldElement.is_exact(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_interval.pyx (starting at line 397)

        Return whether this complex interval is exact (i.e. contains exactly
        one complex value).

        EXAMPLES::

            sage: CIF(3).is_exact()
            True
            sage: CIF(0, 2).is_exact()
            True
            sage: CIF(-4, 0).sqrt().is_exact()
            True
            sage: CIF(-5, 0).sqrt().is_exact()
            False
            sage: CIF(0, 2*pi).is_exact()                                               # needs sage.symbolic
            False
            sage: CIF(e).is_exact()                                                     # needs sage.symbolic
            False
            sage: CIF(1e100).is_exact()
            True
            sage: (CIF(1e100) + 1).is_exact()
            False"""
    @overload
    def is_exact(self) -> Any:
        """ComplexIntervalFieldElement.is_exact(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_interval.pyx (starting at line 397)

        Return whether this complex interval is exact (i.e. contains exactly
        one complex value).

        EXAMPLES::

            sage: CIF(3).is_exact()
            True
            sage: CIF(0, 2).is_exact()
            True
            sage: CIF(-4, 0).sqrt().is_exact()
            True
            sage: CIF(-5, 0).sqrt().is_exact()
            False
            sage: CIF(0, 2*pi).is_exact()                                               # needs sage.symbolic
            False
            sage: CIF(e).is_exact()                                                     # needs sage.symbolic
            False
            sage: CIF(1e100).is_exact()
            True
            sage: (CIF(1e100) + 1).is_exact()
            False"""
    @overload
    def is_exact(self) -> Any:
        """ComplexIntervalFieldElement.is_exact(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_interval.pyx (starting at line 397)

        Return whether this complex interval is exact (i.e. contains exactly
        one complex value).

        EXAMPLES::

            sage: CIF(3).is_exact()
            True
            sage: CIF(0, 2).is_exact()
            True
            sage: CIF(-4, 0).sqrt().is_exact()
            True
            sage: CIF(-5, 0).sqrt().is_exact()
            False
            sage: CIF(0, 2*pi).is_exact()                                               # needs sage.symbolic
            False
            sage: CIF(e).is_exact()                                                     # needs sage.symbolic
            False
            sage: CIF(1e100).is_exact()
            True
            sage: (CIF(1e100) + 1).is_exact()
            False"""
    @overload
    def is_exact(self) -> Any:
        """ComplexIntervalFieldElement.is_exact(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_interval.pyx (starting at line 397)

        Return whether this complex interval is exact (i.e. contains exactly
        one complex value).

        EXAMPLES::

            sage: CIF(3).is_exact()
            True
            sage: CIF(0, 2).is_exact()
            True
            sage: CIF(-4, 0).sqrt().is_exact()
            True
            sage: CIF(-5, 0).sqrt().is_exact()
            False
            sage: CIF(0, 2*pi).is_exact()                                               # needs sage.symbolic
            False
            sage: CIF(e).is_exact()                                                     # needs sage.symbolic
            False
            sage: CIF(1e100).is_exact()
            True
            sage: (CIF(1e100) + 1).is_exact()
            False"""
    def is_square(self) -> Any:
        """ComplexIntervalFieldElement.is_square(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_interval.pyx (starting at line 1896)

        Return ``True`` as `\\CC` is algebraically closed.

        EXAMPLES::

            sage: CIF(2, 1).is_square()
            True"""
    @overload
    def lexico_cmp(self, left, right) -> Any:
        """ComplexIntervalFieldElement.lexico_cmp(left, right)

        File: /build/sagemath/src/sage/src/sage/rings/complex_interval.pyx (starting at line 1498)

        Intervals are compared lexicographically on the 4-tuple:
        ``(x.real().lower(), x.real().upper(),
        x.imag().lower(), x.imag().upper())``

        EXAMPLES::

            sage: a = CIF(RIF(0,1), RIF(0,1))
            sage: b = CIF(RIF(0,1), RIF(0,2))
            sage: c = CIF(RIF(0,2), RIF(0,2))
            sage: a.lexico_cmp(b)
            -1
            sage: b.lexico_cmp(c)
            -1
            sage: a.lexico_cmp(c)
            -1
            sage: a.lexico_cmp(a)
            0
            sage: b.lexico_cmp(a)
            1

        TESTS::

            sage: tests = []
            sage: for rl in (0, 1):
            ....:     for ru in (rl, rl + 1):
            ....:         for il in (0, 1):
            ....:             for iu in (il, il + 1):
            ....:                 tests.append((CIF(RIF(rl, ru), RIF(il, iu)), (rl, ru, il, iu)))
            sage: for (i1, t1) in tests:
            ....:     for (i2, t2) in tests:
            ....:         if t1 == t2:
            ....:             assert(i1.lexico_cmp(i2) == 0)
            ....:         elif t1 < t2:
            ....:             assert(i1.lexico_cmp(i2) == -1)
            ....:         elif t1 > t2:
            ....:             assert(i1.lexico_cmp(i2) == 1)"""
    @overload
    def lexico_cmp(self, b) -> Any:
        """ComplexIntervalFieldElement.lexico_cmp(left, right)

        File: /build/sagemath/src/sage/src/sage/rings/complex_interval.pyx (starting at line 1498)

        Intervals are compared lexicographically on the 4-tuple:
        ``(x.real().lower(), x.real().upper(),
        x.imag().lower(), x.imag().upper())``

        EXAMPLES::

            sage: a = CIF(RIF(0,1), RIF(0,1))
            sage: b = CIF(RIF(0,1), RIF(0,2))
            sage: c = CIF(RIF(0,2), RIF(0,2))
            sage: a.lexico_cmp(b)
            -1
            sage: b.lexico_cmp(c)
            -1
            sage: a.lexico_cmp(c)
            -1
            sage: a.lexico_cmp(a)
            0
            sage: b.lexico_cmp(a)
            1

        TESTS::

            sage: tests = []
            sage: for rl in (0, 1):
            ....:     for ru in (rl, rl + 1):
            ....:         for il in (0, 1):
            ....:             for iu in (il, il + 1):
            ....:                 tests.append((CIF(RIF(rl, ru), RIF(il, iu)), (rl, ru, il, iu)))
            sage: for (i1, t1) in tests:
            ....:     for (i2, t2) in tests:
            ....:         if t1 == t2:
            ....:             assert(i1.lexico_cmp(i2) == 0)
            ....:         elif t1 < t2:
            ....:             assert(i1.lexico_cmp(i2) == -1)
            ....:         elif t1 > t2:
            ....:             assert(i1.lexico_cmp(i2) == 1)"""
    @overload
    def lexico_cmp(self, c) -> Any:
        """ComplexIntervalFieldElement.lexico_cmp(left, right)

        File: /build/sagemath/src/sage/src/sage/rings/complex_interval.pyx (starting at line 1498)

        Intervals are compared lexicographically on the 4-tuple:
        ``(x.real().lower(), x.real().upper(),
        x.imag().lower(), x.imag().upper())``

        EXAMPLES::

            sage: a = CIF(RIF(0,1), RIF(0,1))
            sage: b = CIF(RIF(0,1), RIF(0,2))
            sage: c = CIF(RIF(0,2), RIF(0,2))
            sage: a.lexico_cmp(b)
            -1
            sage: b.lexico_cmp(c)
            -1
            sage: a.lexico_cmp(c)
            -1
            sage: a.lexico_cmp(a)
            0
            sage: b.lexico_cmp(a)
            1

        TESTS::

            sage: tests = []
            sage: for rl in (0, 1):
            ....:     for ru in (rl, rl + 1):
            ....:         for il in (0, 1):
            ....:             for iu in (il, il + 1):
            ....:                 tests.append((CIF(RIF(rl, ru), RIF(il, iu)), (rl, ru, il, iu)))
            sage: for (i1, t1) in tests:
            ....:     for (i2, t2) in tests:
            ....:         if t1 == t2:
            ....:             assert(i1.lexico_cmp(i2) == 0)
            ....:         elif t1 < t2:
            ....:             assert(i1.lexico_cmp(i2) == -1)
            ....:         elif t1 > t2:
            ....:             assert(i1.lexico_cmp(i2) == 1)"""
    @overload
    def lexico_cmp(self, c) -> Any:
        """ComplexIntervalFieldElement.lexico_cmp(left, right)

        File: /build/sagemath/src/sage/src/sage/rings/complex_interval.pyx (starting at line 1498)

        Intervals are compared lexicographically on the 4-tuple:
        ``(x.real().lower(), x.real().upper(),
        x.imag().lower(), x.imag().upper())``

        EXAMPLES::

            sage: a = CIF(RIF(0,1), RIF(0,1))
            sage: b = CIF(RIF(0,1), RIF(0,2))
            sage: c = CIF(RIF(0,2), RIF(0,2))
            sage: a.lexico_cmp(b)
            -1
            sage: b.lexico_cmp(c)
            -1
            sage: a.lexico_cmp(c)
            -1
            sage: a.lexico_cmp(a)
            0
            sage: b.lexico_cmp(a)
            1

        TESTS::

            sage: tests = []
            sage: for rl in (0, 1):
            ....:     for ru in (rl, rl + 1):
            ....:         for il in (0, 1):
            ....:             for iu in (il, il + 1):
            ....:                 tests.append((CIF(RIF(rl, ru), RIF(il, iu)), (rl, ru, il, iu)))
            sage: for (i1, t1) in tests:
            ....:     for (i2, t2) in tests:
            ....:         if t1 == t2:
            ....:             assert(i1.lexico_cmp(i2) == 0)
            ....:         elif t1 < t2:
            ....:             assert(i1.lexico_cmp(i2) == -1)
            ....:         elif t1 > t2:
            ....:             assert(i1.lexico_cmp(i2) == 1)"""
    @overload
    def lexico_cmp(self, a) -> Any:
        """ComplexIntervalFieldElement.lexico_cmp(left, right)

        File: /build/sagemath/src/sage/src/sage/rings/complex_interval.pyx (starting at line 1498)

        Intervals are compared lexicographically on the 4-tuple:
        ``(x.real().lower(), x.real().upper(),
        x.imag().lower(), x.imag().upper())``

        EXAMPLES::

            sage: a = CIF(RIF(0,1), RIF(0,1))
            sage: b = CIF(RIF(0,1), RIF(0,2))
            sage: c = CIF(RIF(0,2), RIF(0,2))
            sage: a.lexico_cmp(b)
            -1
            sage: b.lexico_cmp(c)
            -1
            sage: a.lexico_cmp(c)
            -1
            sage: a.lexico_cmp(a)
            0
            sage: b.lexico_cmp(a)
            1

        TESTS::

            sage: tests = []
            sage: for rl in (0, 1):
            ....:     for ru in (rl, rl + 1):
            ....:         for il in (0, 1):
            ....:             for iu in (il, il + 1):
            ....:                 tests.append((CIF(RIF(rl, ru), RIF(il, iu)), (rl, ru, il, iu)))
            sage: for (i1, t1) in tests:
            ....:     for (i2, t2) in tests:
            ....:         if t1 == t2:
            ....:             assert(i1.lexico_cmp(i2) == 0)
            ....:         elif t1 < t2:
            ....:             assert(i1.lexico_cmp(i2) == -1)
            ....:         elif t1 > t2:
            ....:             assert(i1.lexico_cmp(i2) == 1)"""
    @overload
    def lexico_cmp(self, a) -> Any:
        """ComplexIntervalFieldElement.lexico_cmp(left, right)

        File: /build/sagemath/src/sage/src/sage/rings/complex_interval.pyx (starting at line 1498)

        Intervals are compared lexicographically on the 4-tuple:
        ``(x.real().lower(), x.real().upper(),
        x.imag().lower(), x.imag().upper())``

        EXAMPLES::

            sage: a = CIF(RIF(0,1), RIF(0,1))
            sage: b = CIF(RIF(0,1), RIF(0,2))
            sage: c = CIF(RIF(0,2), RIF(0,2))
            sage: a.lexico_cmp(b)
            -1
            sage: b.lexico_cmp(c)
            -1
            sage: a.lexico_cmp(c)
            -1
            sage: a.lexico_cmp(a)
            0
            sage: b.lexico_cmp(a)
            1

        TESTS::

            sage: tests = []
            sage: for rl in (0, 1):
            ....:     for ru in (rl, rl + 1):
            ....:         for il in (0, 1):
            ....:             for iu in (il, il + 1):
            ....:                 tests.append((CIF(RIF(rl, ru), RIF(il, iu)), (rl, ru, il, iu)))
            sage: for (i1, t1) in tests:
            ....:     for (i2, t2) in tests:
            ....:         if t1 == t2:
            ....:             assert(i1.lexico_cmp(i2) == 0)
            ....:         elif t1 < t2:
            ....:             assert(i1.lexico_cmp(i2) == -1)
            ....:         elif t1 > t2:
            ....:             assert(i1.lexico_cmp(i2) == 1)"""
    @overload
    def lexico_cmp(self, i2) -> Any:
        """ComplexIntervalFieldElement.lexico_cmp(left, right)

        File: /build/sagemath/src/sage/src/sage/rings/complex_interval.pyx (starting at line 1498)

        Intervals are compared lexicographically on the 4-tuple:
        ``(x.real().lower(), x.real().upper(),
        x.imag().lower(), x.imag().upper())``

        EXAMPLES::

            sage: a = CIF(RIF(0,1), RIF(0,1))
            sage: b = CIF(RIF(0,1), RIF(0,2))
            sage: c = CIF(RIF(0,2), RIF(0,2))
            sage: a.lexico_cmp(b)
            -1
            sage: b.lexico_cmp(c)
            -1
            sage: a.lexico_cmp(c)
            -1
            sage: a.lexico_cmp(a)
            0
            sage: b.lexico_cmp(a)
            1

        TESTS::

            sage: tests = []
            sage: for rl in (0, 1):
            ....:     for ru in (rl, rl + 1):
            ....:         for il in (0, 1):
            ....:             for iu in (il, il + 1):
            ....:                 tests.append((CIF(RIF(rl, ru), RIF(il, iu)), (rl, ru, il, iu)))
            sage: for (i1, t1) in tests:
            ....:     for (i2, t2) in tests:
            ....:         if t1 == t2:
            ....:             assert(i1.lexico_cmp(i2) == 0)
            ....:         elif t1 < t2:
            ....:             assert(i1.lexico_cmp(i2) == -1)
            ....:         elif t1 > t2:
            ....:             assert(i1.lexico_cmp(i2) == 1)"""
    @overload
    def lexico_cmp(self, i2) -> Any:
        """ComplexIntervalFieldElement.lexico_cmp(left, right)

        File: /build/sagemath/src/sage/src/sage/rings/complex_interval.pyx (starting at line 1498)

        Intervals are compared lexicographically on the 4-tuple:
        ``(x.real().lower(), x.real().upper(),
        x.imag().lower(), x.imag().upper())``

        EXAMPLES::

            sage: a = CIF(RIF(0,1), RIF(0,1))
            sage: b = CIF(RIF(0,1), RIF(0,2))
            sage: c = CIF(RIF(0,2), RIF(0,2))
            sage: a.lexico_cmp(b)
            -1
            sage: b.lexico_cmp(c)
            -1
            sage: a.lexico_cmp(c)
            -1
            sage: a.lexico_cmp(a)
            0
            sage: b.lexico_cmp(a)
            1

        TESTS::

            sage: tests = []
            sage: for rl in (0, 1):
            ....:     for ru in (rl, rl + 1):
            ....:         for il in (0, 1):
            ....:             for iu in (il, il + 1):
            ....:                 tests.append((CIF(RIF(rl, ru), RIF(il, iu)), (rl, ru, il, iu)))
            sage: for (i1, t1) in tests:
            ....:     for (i2, t2) in tests:
            ....:         if t1 == t2:
            ....:             assert(i1.lexico_cmp(i2) == 0)
            ....:         elif t1 < t2:
            ....:             assert(i1.lexico_cmp(i2) == -1)
            ....:         elif t1 > t2:
            ....:             assert(i1.lexico_cmp(i2) == 1)"""
    @overload
    def lexico_cmp(self, i2) -> Any:
        """ComplexIntervalFieldElement.lexico_cmp(left, right)

        File: /build/sagemath/src/sage/src/sage/rings/complex_interval.pyx (starting at line 1498)

        Intervals are compared lexicographically on the 4-tuple:
        ``(x.real().lower(), x.real().upper(),
        x.imag().lower(), x.imag().upper())``

        EXAMPLES::

            sage: a = CIF(RIF(0,1), RIF(0,1))
            sage: b = CIF(RIF(0,1), RIF(0,2))
            sage: c = CIF(RIF(0,2), RIF(0,2))
            sage: a.lexico_cmp(b)
            -1
            sage: b.lexico_cmp(c)
            -1
            sage: a.lexico_cmp(c)
            -1
            sage: a.lexico_cmp(a)
            0
            sage: b.lexico_cmp(a)
            1

        TESTS::

            sage: tests = []
            sage: for rl in (0, 1):
            ....:     for ru in (rl, rl + 1):
            ....:         for il in (0, 1):
            ....:             for iu in (il, il + 1):
            ....:                 tests.append((CIF(RIF(rl, ru), RIF(il, iu)), (rl, ru, il, iu)))
            sage: for (i1, t1) in tests:
            ....:     for (i2, t2) in tests:
            ....:         if t1 == t2:
            ....:             assert(i1.lexico_cmp(i2) == 0)
            ....:         elif t1 < t2:
            ....:             assert(i1.lexico_cmp(i2) == -1)
            ....:         elif t1 > t2:
            ....:             assert(i1.lexico_cmp(i2) == 1)"""
    @overload
    def log(self, base=...) -> Any:
        """ComplexIntervalFieldElement.log(self, base=None)

        File: /build/sagemath/src/sage/src/sage/rings/complex_interval.pyx (starting at line 1785)

        Complex logarithm of `z`.

        .. WARNING::

            This does always not use the standard branch cut for complex log!
            See the docstring for :meth:`argument()` to see what we do instead.

        EXAMPLES::

            sage: a = CIF(RIF(3, 4), RIF(13, 14))
            sage: a.log().str(style='brackets')
            '[2.5908917751460420 .. 2.6782931373360067] + [1.2722973952087170 .. 1.3597029935721503]*I'
            sage: a.log().exp().str(style='brackets')
            '[2.7954667135098274 .. 4.2819545928390213] + [12.751682453911920 .. 14.237018048974635]*I'
            sage: a in a.log().exp()
            True

        If the interval crosses the negative real axis, then we don't
        use the standard branch cut (and we violate the interval guarantees)::

            sage: CIF(-3, RIF(-1/4, 1/4)).log().str(style='brackets')
            '[1.0986122886681095 .. 1.1020725100903968] + [3.0584514217013518 .. 3.2247338854782349]*I'
            sage: CIF(-3, -1/4).log()
            1.102072510090397? - 3.058451421701352?*I

        Usually if an interval contains zero, we raise an exception::

            sage: CIF(RIF(-1,1),RIF(-1,1)).log()
            Traceback (most recent call last):
            ...
            ValueError: Can...t take the argument of interval strictly containing zero

        But we allow the exact input zero::

            sage: CIF(0).log()
            [-infinity .. -infinity]

        If a base is passed from another function, we can accommodate this::

            sage: CIF(-1,1).log(2)
            0.500000000000000? + 3.39927010637040?*I"""
    @overload
    def log(self) -> Any:
        """ComplexIntervalFieldElement.log(self, base=None)

        File: /build/sagemath/src/sage/src/sage/rings/complex_interval.pyx (starting at line 1785)

        Complex logarithm of `z`.

        .. WARNING::

            This does always not use the standard branch cut for complex log!
            See the docstring for :meth:`argument()` to see what we do instead.

        EXAMPLES::

            sage: a = CIF(RIF(3, 4), RIF(13, 14))
            sage: a.log().str(style='brackets')
            '[2.5908917751460420 .. 2.6782931373360067] + [1.2722973952087170 .. 1.3597029935721503]*I'
            sage: a.log().exp().str(style='brackets')
            '[2.7954667135098274 .. 4.2819545928390213] + [12.751682453911920 .. 14.237018048974635]*I'
            sage: a in a.log().exp()
            True

        If the interval crosses the negative real axis, then we don't
        use the standard branch cut (and we violate the interval guarantees)::

            sage: CIF(-3, RIF(-1/4, 1/4)).log().str(style='brackets')
            '[1.0986122886681095 .. 1.1020725100903968] + [3.0584514217013518 .. 3.2247338854782349]*I'
            sage: CIF(-3, -1/4).log()
            1.102072510090397? - 3.058451421701352?*I

        Usually if an interval contains zero, we raise an exception::

            sage: CIF(RIF(-1,1),RIF(-1,1)).log()
            Traceback (most recent call last):
            ...
            ValueError: Can...t take the argument of interval strictly containing zero

        But we allow the exact input zero::

            sage: CIF(0).log()
            [-infinity .. -infinity]

        If a base is passed from another function, we can accommodate this::

            sage: CIF(-1,1).log(2)
            0.500000000000000? + 3.39927010637040?*I"""
    @overload
    def log(self) -> Any:
        """ComplexIntervalFieldElement.log(self, base=None)

        File: /build/sagemath/src/sage/src/sage/rings/complex_interval.pyx (starting at line 1785)

        Complex logarithm of `z`.

        .. WARNING::

            This does always not use the standard branch cut for complex log!
            See the docstring for :meth:`argument()` to see what we do instead.

        EXAMPLES::

            sage: a = CIF(RIF(3, 4), RIF(13, 14))
            sage: a.log().str(style='brackets')
            '[2.5908917751460420 .. 2.6782931373360067] + [1.2722973952087170 .. 1.3597029935721503]*I'
            sage: a.log().exp().str(style='brackets')
            '[2.7954667135098274 .. 4.2819545928390213] + [12.751682453911920 .. 14.237018048974635]*I'
            sage: a in a.log().exp()
            True

        If the interval crosses the negative real axis, then we don't
        use the standard branch cut (and we violate the interval guarantees)::

            sage: CIF(-3, RIF(-1/4, 1/4)).log().str(style='brackets')
            '[1.0986122886681095 .. 1.1020725100903968] + [3.0584514217013518 .. 3.2247338854782349]*I'
            sage: CIF(-3, -1/4).log()
            1.102072510090397? - 3.058451421701352?*I

        Usually if an interval contains zero, we raise an exception::

            sage: CIF(RIF(-1,1),RIF(-1,1)).log()
            Traceback (most recent call last):
            ...
            ValueError: Can...t take the argument of interval strictly containing zero

        But we allow the exact input zero::

            sage: CIF(0).log()
            [-infinity .. -infinity]

        If a base is passed from another function, we can accommodate this::

            sage: CIF(-1,1).log(2)
            0.500000000000000? + 3.39927010637040?*I"""
    @overload
    def log(self) -> Any:
        """ComplexIntervalFieldElement.log(self, base=None)

        File: /build/sagemath/src/sage/src/sage/rings/complex_interval.pyx (starting at line 1785)

        Complex logarithm of `z`.

        .. WARNING::

            This does always not use the standard branch cut for complex log!
            See the docstring for :meth:`argument()` to see what we do instead.

        EXAMPLES::

            sage: a = CIF(RIF(3, 4), RIF(13, 14))
            sage: a.log().str(style='brackets')
            '[2.5908917751460420 .. 2.6782931373360067] + [1.2722973952087170 .. 1.3597029935721503]*I'
            sage: a.log().exp().str(style='brackets')
            '[2.7954667135098274 .. 4.2819545928390213] + [12.751682453911920 .. 14.237018048974635]*I'
            sage: a in a.log().exp()
            True

        If the interval crosses the negative real axis, then we don't
        use the standard branch cut (and we violate the interval guarantees)::

            sage: CIF(-3, RIF(-1/4, 1/4)).log().str(style='brackets')
            '[1.0986122886681095 .. 1.1020725100903968] + [3.0584514217013518 .. 3.2247338854782349]*I'
            sage: CIF(-3, -1/4).log()
            1.102072510090397? - 3.058451421701352?*I

        Usually if an interval contains zero, we raise an exception::

            sage: CIF(RIF(-1,1),RIF(-1,1)).log()
            Traceback (most recent call last):
            ...
            ValueError: Can...t take the argument of interval strictly containing zero

        But we allow the exact input zero::

            sage: CIF(0).log()
            [-infinity .. -infinity]

        If a base is passed from another function, we can accommodate this::

            sage: CIF(-1,1).log(2)
            0.500000000000000? + 3.39927010637040?*I"""
    @overload
    def magnitude(self) -> Any:
        """ComplexIntervalFieldElement.magnitude(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_interval.pyx (starting at line 602)

        The largest absolute value of the elements of the interval, rounded
        away from zero.

        OUTPUT: a real number with rounding mode ``RNDU``

        EXAMPLES::

            sage: CIF(RIF(-1,1), RIF(-1,1)).magnitude()
            1.41421356237310
            sage: CIF(RIF(1,2), RIF(3,4)).magnitude()
            4.47213595499958
            sage: parent(CIF(1).magnitude())
            Real Field with 53 bits of precision and rounding RNDU"""
    @overload
    def magnitude(self) -> Any:
        """ComplexIntervalFieldElement.magnitude(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_interval.pyx (starting at line 602)

        The largest absolute value of the elements of the interval, rounded
        away from zero.

        OUTPUT: a real number with rounding mode ``RNDU``

        EXAMPLES::

            sage: CIF(RIF(-1,1), RIF(-1,1)).magnitude()
            1.41421356237310
            sage: CIF(RIF(1,2), RIF(3,4)).magnitude()
            4.47213595499958
            sage: parent(CIF(1).magnitude())
            Real Field with 53 bits of precision and rounding RNDU"""
    @overload
    def magnitude(self) -> Any:
        """ComplexIntervalFieldElement.magnitude(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_interval.pyx (starting at line 602)

        The largest absolute value of the elements of the interval, rounded
        away from zero.

        OUTPUT: a real number with rounding mode ``RNDU``

        EXAMPLES::

            sage: CIF(RIF(-1,1), RIF(-1,1)).magnitude()
            1.41421356237310
            sage: CIF(RIF(1,2), RIF(3,4)).magnitude()
            4.47213595499958
            sage: parent(CIF(1).magnitude())
            Real Field with 53 bits of precision and rounding RNDU"""
    @overload
    def magnitude(self) -> Any:
        """ComplexIntervalFieldElement.magnitude(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_interval.pyx (starting at line 602)

        The largest absolute value of the elements of the interval, rounded
        away from zero.

        OUTPUT: a real number with rounding mode ``RNDU``

        EXAMPLES::

            sage: CIF(RIF(-1,1), RIF(-1,1)).magnitude()
            1.41421356237310
            sage: CIF(RIF(1,2), RIF(3,4)).magnitude()
            4.47213595499958
            sage: parent(CIF(1).magnitude())
            Real Field with 53 bits of precision and rounding RNDU"""
    @overload
    def mignitude(self) -> Any:
        """ComplexIntervalFieldElement.mignitude(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_interval.pyx (starting at line 626)

        The smallest absolute value of the elements of the interval, rounded
        towards zero.

        OUTPUT: a real number with rounding mode ``RNDD``

        EXAMPLES::

            sage: CIF(RIF(-1,1), RIF(-1,1)).mignitude()
            0.000000000000000
            sage: CIF(RIF(1,2), RIF(3,4)).mignitude()
            3.16227766016837
            sage: parent(CIF(1).mignitude())
            Real Field with 53 bits of precision and rounding RNDD"""
    @overload
    def mignitude(self) -> Any:
        """ComplexIntervalFieldElement.mignitude(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_interval.pyx (starting at line 626)

        The smallest absolute value of the elements of the interval, rounded
        towards zero.

        OUTPUT: a real number with rounding mode ``RNDD``

        EXAMPLES::

            sage: CIF(RIF(-1,1), RIF(-1,1)).mignitude()
            0.000000000000000
            sage: CIF(RIF(1,2), RIF(3,4)).mignitude()
            3.16227766016837
            sage: parent(CIF(1).mignitude())
            Real Field with 53 bits of precision and rounding RNDD"""
    @overload
    def mignitude(self) -> Any:
        """ComplexIntervalFieldElement.mignitude(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_interval.pyx (starting at line 626)

        The smallest absolute value of the elements of the interval, rounded
        towards zero.

        OUTPUT: a real number with rounding mode ``RNDD``

        EXAMPLES::

            sage: CIF(RIF(-1,1), RIF(-1,1)).mignitude()
            0.000000000000000
            sage: CIF(RIF(1,2), RIF(3,4)).mignitude()
            3.16227766016837
            sage: parent(CIF(1).mignitude())
            Real Field with 53 bits of precision and rounding RNDD"""
    @overload
    def mignitude(self) -> Any:
        """ComplexIntervalFieldElement.mignitude(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_interval.pyx (starting at line 626)

        The smallest absolute value of the elements of the interval, rounded
        towards zero.

        OUTPUT: a real number with rounding mode ``RNDD``

        EXAMPLES::

            sage: CIF(RIF(-1,1), RIF(-1,1)).mignitude()
            0.000000000000000
            sage: CIF(RIF(1,2), RIF(3,4)).mignitude()
            3.16227766016837
            sage: parent(CIF(1).mignitude())
            Real Field with 53 bits of precision and rounding RNDD"""
    @overload
    def multiplicative_order(self) -> Any:
        """ComplexIntervalFieldElement.multiplicative_order(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_interval.pyx (starting at line 1570)

        Return the multiplicative order of this complex number, if known,
        or raise a :exc:`NotImplementedError`.

        EXAMPLES::

            sage: C = CIF
            sage: i = C.0
            sage: i.multiplicative_order()
            4
            sage: C(1).multiplicative_order()
            1
            sage: C(-1).multiplicative_order()
            2
            sage: (i^2).multiplicative_order()
            2
            sage: (-i).multiplicative_order()
            4
            sage: C(2).multiplicative_order()
            +Infinity
            sage: w = (1 + C(-3).sqrt())/2 ; w
            0.50000000000000000? + 0.866025403784439?*I
            sage: w.multiplicative_order()
            Traceback (most recent call last):
            ...
            NotImplementedError: order of element not known"""
    @overload
    def multiplicative_order(self) -> Any:
        """ComplexIntervalFieldElement.multiplicative_order(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_interval.pyx (starting at line 1570)

        Return the multiplicative order of this complex number, if known,
        or raise a :exc:`NotImplementedError`.

        EXAMPLES::

            sage: C = CIF
            sage: i = C.0
            sage: i.multiplicative_order()
            4
            sage: C(1).multiplicative_order()
            1
            sage: C(-1).multiplicative_order()
            2
            sage: (i^2).multiplicative_order()
            2
            sage: (-i).multiplicative_order()
            4
            sage: C(2).multiplicative_order()
            +Infinity
            sage: w = (1 + C(-3).sqrt())/2 ; w
            0.50000000000000000? + 0.866025403784439?*I
            sage: w.multiplicative_order()
            Traceback (most recent call last):
            ...
            NotImplementedError: order of element not known"""
    @overload
    def multiplicative_order(self) -> Any:
        """ComplexIntervalFieldElement.multiplicative_order(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_interval.pyx (starting at line 1570)

        Return the multiplicative order of this complex number, if known,
        or raise a :exc:`NotImplementedError`.

        EXAMPLES::

            sage: C = CIF
            sage: i = C.0
            sage: i.multiplicative_order()
            4
            sage: C(1).multiplicative_order()
            1
            sage: C(-1).multiplicative_order()
            2
            sage: (i^2).multiplicative_order()
            2
            sage: (-i).multiplicative_order()
            4
            sage: C(2).multiplicative_order()
            +Infinity
            sage: w = (1 + C(-3).sqrt())/2 ; w
            0.50000000000000000? + 0.866025403784439?*I
            sage: w.multiplicative_order()
            Traceback (most recent call last):
            ...
            NotImplementedError: order of element not known"""
    @overload
    def multiplicative_order(self) -> Any:
        """ComplexIntervalFieldElement.multiplicative_order(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_interval.pyx (starting at line 1570)

        Return the multiplicative order of this complex number, if known,
        or raise a :exc:`NotImplementedError`.

        EXAMPLES::

            sage: C = CIF
            sage: i = C.0
            sage: i.multiplicative_order()
            4
            sage: C(1).multiplicative_order()
            1
            sage: C(-1).multiplicative_order()
            2
            sage: (i^2).multiplicative_order()
            2
            sage: (-i).multiplicative_order()
            4
            sage: C(2).multiplicative_order()
            +Infinity
            sage: w = (1 + C(-3).sqrt())/2 ; w
            0.50000000000000000? + 0.866025403784439?*I
            sage: w.multiplicative_order()
            Traceback (most recent call last):
            ...
            NotImplementedError: order of element not known"""
    @overload
    def multiplicative_order(self) -> Any:
        """ComplexIntervalFieldElement.multiplicative_order(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_interval.pyx (starting at line 1570)

        Return the multiplicative order of this complex number, if known,
        or raise a :exc:`NotImplementedError`.

        EXAMPLES::

            sage: C = CIF
            sage: i = C.0
            sage: i.multiplicative_order()
            4
            sage: C(1).multiplicative_order()
            1
            sage: C(-1).multiplicative_order()
            2
            sage: (i^2).multiplicative_order()
            2
            sage: (-i).multiplicative_order()
            4
            sage: C(2).multiplicative_order()
            +Infinity
            sage: w = (1 + C(-3).sqrt())/2 ; w
            0.50000000000000000? + 0.866025403784439?*I
            sage: w.multiplicative_order()
            Traceback (most recent call last):
            ...
            NotImplementedError: order of element not known"""
    @overload
    def multiplicative_order(self) -> Any:
        """ComplexIntervalFieldElement.multiplicative_order(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_interval.pyx (starting at line 1570)

        Return the multiplicative order of this complex number, if known,
        or raise a :exc:`NotImplementedError`.

        EXAMPLES::

            sage: C = CIF
            sage: i = C.0
            sage: i.multiplicative_order()
            4
            sage: C(1).multiplicative_order()
            1
            sage: C(-1).multiplicative_order()
            2
            sage: (i^2).multiplicative_order()
            2
            sage: (-i).multiplicative_order()
            4
            sage: C(2).multiplicative_order()
            +Infinity
            sage: w = (1 + C(-3).sqrt())/2 ; w
            0.50000000000000000? + 0.866025403784439?*I
            sage: w.multiplicative_order()
            Traceback (most recent call last):
            ...
            NotImplementedError: order of element not known"""
    @overload
    def multiplicative_order(self) -> Any:
        """ComplexIntervalFieldElement.multiplicative_order(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_interval.pyx (starting at line 1570)

        Return the multiplicative order of this complex number, if known,
        or raise a :exc:`NotImplementedError`.

        EXAMPLES::

            sage: C = CIF
            sage: i = C.0
            sage: i.multiplicative_order()
            4
            sage: C(1).multiplicative_order()
            1
            sage: C(-1).multiplicative_order()
            2
            sage: (i^2).multiplicative_order()
            2
            sage: (-i).multiplicative_order()
            4
            sage: C(2).multiplicative_order()
            +Infinity
            sage: w = (1 + C(-3).sqrt())/2 ; w
            0.50000000000000000? + 0.866025403784439?*I
            sage: w.multiplicative_order()
            Traceback (most recent call last):
            ...
            NotImplementedError: order of element not known"""
    @overload
    def multiplicative_order(self) -> Any:
        """ComplexIntervalFieldElement.multiplicative_order(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_interval.pyx (starting at line 1570)

        Return the multiplicative order of this complex number, if known,
        or raise a :exc:`NotImplementedError`.

        EXAMPLES::

            sage: C = CIF
            sage: i = C.0
            sage: i.multiplicative_order()
            4
            sage: C(1).multiplicative_order()
            1
            sage: C(-1).multiplicative_order()
            2
            sage: (i^2).multiplicative_order()
            2
            sage: (-i).multiplicative_order()
            4
            sage: C(2).multiplicative_order()
            +Infinity
            sage: w = (1 + C(-3).sqrt())/2 ; w
            0.50000000000000000? + 0.866025403784439?*I
            sage: w.multiplicative_order()
            Traceback (most recent call last):
            ...
            NotImplementedError: order of element not known"""
    def norm(self) -> Any:
        """ComplexIntervalFieldElement.norm(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_interval.pyx (starting at line 743)

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

            - :meth:`sage.rings.complex_double.ComplexDoubleElement.norm`

        EXAMPLES::

            sage: CIF(2, 1).norm()
            5
            sage: CIF(1, -2).norm()
            5"""
    def overlaps(self, ComplexIntervalFieldElementother) -> Any:
        """ComplexIntervalFieldElement.overlaps(self, ComplexIntervalFieldElement other)

        File: /build/sagemath/src/sage/src/sage/rings/complex_interval.pyx (starting at line 533)

        Return ``True`` if ``self`` and ``other`` are intervals with at least
        one value in common.

        EXAMPLES::

            sage: CIF(0).overlaps(CIF(RIF(0, 1), RIF(-1, 0)))
            True
            sage: CIF(1).overlaps(CIF(1, 1))
            False"""
    def plot(self, pointsize=..., **kwds) -> Any:
        """ComplexIntervalFieldElement.plot(self, pointsize=10, **kwds)

        File: /build/sagemath/src/sage/src/sage/rings/complex_interval.pyx (starting at line 290)

        Plot a complex interval as a rectangle.

        EXAMPLES::

            sage: sum(plot(CIF(RIF(1/k, 1/k), RIF(-k, k))) for k in [1..10])            # needs sage.plot
            Graphics object consisting of 20 graphics primitives

        Exact and nearly exact points are still visible::

            sage: # needs sage.plot sage.symbolic
            sage: plot(CIF(pi, 1), color='red') + plot(CIF(1, e), color='purple') + plot(CIF(-1, -1))
            Graphics object consisting of 6 graphics primitives

        A demonstration that `z \\mapsto z^2` acts chaotically on `|z|=1`::

            sage: # needs sage.plot sage.symbolic
            sage: z = CIF(0, 2*pi/1000).exp()
            sage: g = Graphics()
            sage: for i in range(40):
            ....:     z = z^2
            ....:     g += z.plot(color=(1./(40-i), 0, 1))
            ...
            sage: g
            Graphics object consisting of 80 graphics primitives"""
    @overload
    def prec(self) -> Any:
        """ComplexIntervalFieldElement.prec(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_interval.pyx (starting at line 1028)

        Return precision of this complex number.

        EXAMPLES::

            sage: i = ComplexIntervalField(2000).0
            sage: i.prec()
            2000"""
    @overload
    def prec(self) -> Any:
        """ComplexIntervalFieldElement.prec(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_interval.pyx (starting at line 1028)

        Return precision of this complex number.

        EXAMPLES::

            sage: i = ComplexIntervalField(2000).0
            sage: i.prec()
            2000"""
    @overload
    def real(self) -> Any:
        """ComplexIntervalFieldElement.real(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_interval.pyx (starting at line 1040)

        Return real part of ``self``.

        EXAMPLES::

            sage: i = ComplexIntervalField(100).0
            sage: z = 2 + 3*i
            sage: x = z.real(); x
            2
            sage: x.parent()
            Real Interval Field with 100 bits of precision"""
    @overload
    def real(self) -> Any:
        """ComplexIntervalFieldElement.real(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_interval.pyx (starting at line 1040)

        Return real part of ``self``.

        EXAMPLES::

            sage: i = ComplexIntervalField(100).0
            sage: z = 2 + 3*i
            sage: x = z.real(); x
            2
            sage: x.parent()
            Real Interval Field with 100 bits of precision"""
    @overload
    def sin(self) -> Any:
        """ComplexIntervalFieldElement.sin(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_interval.pyx (starting at line 1964)

        Compute the sine of this complex interval.

        EXAMPLES::

            sage: CIF(1,1).sin()
            1.298457581415978? + 0.634963914784736?*I
            sage: CIF(2).sin()
            0.909297426825682?
            sage: CIF(0,2).sin()
            3.626860407847019?*I

        Check that :issue:`17825` is fixed::

            sage: CIF(sin(2/3))                                                         # needs sage.symbolic
            0.618369803069737?

        ALGORITHM:

        The implementation uses the following trigonometric identity

        .. MATH::

            \\sin(x + iy) = \\sin(x) \\cosh(y) + i \\cos (x) \\sinh(y)"""
    @overload
    def sin(self) -> Any:
        """ComplexIntervalFieldElement.sin(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_interval.pyx (starting at line 1964)

        Compute the sine of this complex interval.

        EXAMPLES::

            sage: CIF(1,1).sin()
            1.298457581415978? + 0.634963914784736?*I
            sage: CIF(2).sin()
            0.909297426825682?
            sage: CIF(0,2).sin()
            3.626860407847019?*I

        Check that :issue:`17825` is fixed::

            sage: CIF(sin(2/3))                                                         # needs sage.symbolic
            0.618369803069737?

        ALGORITHM:

        The implementation uses the following trigonometric identity

        .. MATH::

            \\sin(x + iy) = \\sin(x) \\cosh(y) + i \\cos (x) \\sinh(y)"""
    @overload
    def sin(self) -> Any:
        """ComplexIntervalFieldElement.sin(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_interval.pyx (starting at line 1964)

        Compute the sine of this complex interval.

        EXAMPLES::

            sage: CIF(1,1).sin()
            1.298457581415978? + 0.634963914784736?*I
            sage: CIF(2).sin()
            0.909297426825682?
            sage: CIF(0,2).sin()
            3.626860407847019?*I

        Check that :issue:`17825` is fixed::

            sage: CIF(sin(2/3))                                                         # needs sage.symbolic
            0.618369803069737?

        ALGORITHM:

        The implementation uses the following trigonometric identity

        .. MATH::

            \\sin(x + iy) = \\sin(x) \\cosh(y) + i \\cos (x) \\sinh(y)"""
    @overload
    def sin(self) -> Any:
        """ComplexIntervalFieldElement.sin(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_interval.pyx (starting at line 1964)

        Compute the sine of this complex interval.

        EXAMPLES::

            sage: CIF(1,1).sin()
            1.298457581415978? + 0.634963914784736?*I
            sage: CIF(2).sin()
            0.909297426825682?
            sage: CIF(0,2).sin()
            3.626860407847019?*I

        Check that :issue:`17825` is fixed::

            sage: CIF(sin(2/3))                                                         # needs sage.symbolic
            0.618369803069737?

        ALGORITHM:

        The implementation uses the following trigonometric identity

        .. MATH::

            \\sin(x + iy) = \\sin(x) \\cosh(y) + i \\cos (x) \\sinh(y)"""
    @overload
    def sinh(self) -> Any:
        """ComplexIntervalFieldElement.sinh(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_interval.pyx (starting at line 2056)

        Return the hyperbolic sine of this complex interval.

        EXAMPLES::

            sage: CIF(1,1).sinh()
            0.634963914784736? + 1.298457581415978?*I
            sage: CIF(2).sinh()
            3.626860407847019?
            sage: CIF(0,2).sinh()
            0.909297426825682?*I

        ALGORITHM:

        The implementation uses the following trigonometric identity

        .. MATH::

            \\sinh(x+iy) = \\cos(y) \\sinh(x) + i \\sin(y) \\cosh(x)"""
    @overload
    def sinh(self) -> Any:
        """ComplexIntervalFieldElement.sinh(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_interval.pyx (starting at line 2056)

        Return the hyperbolic sine of this complex interval.

        EXAMPLES::

            sage: CIF(1,1).sinh()
            0.634963914784736? + 1.298457581415978?*I
            sage: CIF(2).sinh()
            3.626860407847019?
            sage: CIF(0,2).sinh()
            0.909297426825682?*I

        ALGORITHM:

        The implementation uses the following trigonometric identity

        .. MATH::

            \\sinh(x+iy) = \\cos(y) \\sinh(x) + i \\sin(y) \\cosh(x)"""
    @overload
    def sinh(self) -> Any:
        """ComplexIntervalFieldElement.sinh(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_interval.pyx (starting at line 2056)

        Return the hyperbolic sine of this complex interval.

        EXAMPLES::

            sage: CIF(1,1).sinh()
            0.634963914784736? + 1.298457581415978?*I
            sage: CIF(2).sinh()
            3.626860407847019?
            sage: CIF(0,2).sinh()
            0.909297426825682?*I

        ALGORITHM:

        The implementation uses the following trigonometric identity

        .. MATH::

            \\sinh(x+iy) = \\cos(y) \\sinh(x) + i \\sin(y) \\cosh(x)"""
    @overload
    def sinh(self) -> Any:
        """ComplexIntervalFieldElement.sinh(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_interval.pyx (starting at line 2056)

        Return the hyperbolic sine of this complex interval.

        EXAMPLES::

            sage: CIF(1,1).sinh()
            0.634963914784736? + 1.298457581415978?*I
            sage: CIF(2).sinh()
            3.626860407847019?
            sage: CIF(0,2).sinh()
            0.909297426825682?*I

        ALGORITHM:

        The implementation uses the following trigonometric identity

        .. MATH::

            \\sinh(x+iy) = \\cos(y) \\sinh(x) + i \\sin(y) \\cosh(x)"""
    @overload
    def sqrt(self, boolall=..., **kwds) -> Any:
        """ComplexIntervalFieldElement.sqrt(self, bool all=False, **kwds)

        File: /build/sagemath/src/sage/src/sage/rings/complex_interval.pyx (starting at line 1843)

        The square root function.

        .. WARNING::

            We approximate the standard branch cut along the negative real
            axis, with ``sqrt(-r^2) = i*r`` for positive real ``r``; but if
            the interval crosses the negative real axis, we pick the root with
            positive imaginary component for the entire interval.

        INPUT:

        - ``all`` -- boolean (default: ``False``); if ``True``, return a list
          of all square roots

        EXAMPLES::

            sage: CIF(-1).sqrt()^2
            -1
            sage: sqrt(CIF(2))
            1.414213562373095?
            sage: sqrt(CIF(-1))
            1*I
            sage: sqrt(CIF(2-I))^2
            2.00000000000000? - 1.00000000000000?*I
            sage: CC(-2-I).sqrt()^2
            -2.00000000000000 - 1.00000000000000*I

        Here, we select a non-principal root for part of the interval, and
        violate the standard interval guarantees::

            sage: CIF(-5, RIF(-1, 1)).sqrt().str(style='brackets')
            '[-0.22250788030178321 .. 0.22250788030178296] + [2.2251857651053086 .. 2.2581008643532262]*I'
            sage: CIF(-5, -1).sqrt()
            0.222507880301783? - 2.247111425095870?*I"""
    @overload
    def sqrt(self) -> Any:
        """ComplexIntervalFieldElement.sqrt(self, bool all=False, **kwds)

        File: /build/sagemath/src/sage/src/sage/rings/complex_interval.pyx (starting at line 1843)

        The square root function.

        .. WARNING::

            We approximate the standard branch cut along the negative real
            axis, with ``sqrt(-r^2) = i*r`` for positive real ``r``; but if
            the interval crosses the negative real axis, we pick the root with
            positive imaginary component for the entire interval.

        INPUT:

        - ``all`` -- boolean (default: ``False``); if ``True``, return a list
          of all square roots

        EXAMPLES::

            sage: CIF(-1).sqrt()^2
            -1
            sage: sqrt(CIF(2))
            1.414213562373095?
            sage: sqrt(CIF(-1))
            1*I
            sage: sqrt(CIF(2-I))^2
            2.00000000000000? - 1.00000000000000?*I
            sage: CC(-2-I).sqrt()^2
            -2.00000000000000 - 1.00000000000000*I

        Here, we select a non-principal root for part of the interval, and
        violate the standard interval guarantees::

            sage: CIF(-5, RIF(-1, 1)).sqrt().str(style='brackets')
            '[-0.22250788030178321 .. 0.22250788030178296] + [2.2251857651053086 .. 2.2581008643532262]*I'
            sage: CIF(-5, -1).sqrt()
            0.222507880301783? - 2.247111425095870?*I"""
    @overload
    def sqrt(self) -> Any:
        """ComplexIntervalFieldElement.sqrt(self, bool all=False, **kwds)

        File: /build/sagemath/src/sage/src/sage/rings/complex_interval.pyx (starting at line 1843)

        The square root function.

        .. WARNING::

            We approximate the standard branch cut along the negative real
            axis, with ``sqrt(-r^2) = i*r`` for positive real ``r``; but if
            the interval crosses the negative real axis, we pick the root with
            positive imaginary component for the entire interval.

        INPUT:

        - ``all`` -- boolean (default: ``False``); if ``True``, return a list
          of all square roots

        EXAMPLES::

            sage: CIF(-1).sqrt()^2
            -1
            sage: sqrt(CIF(2))
            1.414213562373095?
            sage: sqrt(CIF(-1))
            1*I
            sage: sqrt(CIF(2-I))^2
            2.00000000000000? - 1.00000000000000?*I
            sage: CC(-2-I).sqrt()^2
            -2.00000000000000 - 1.00000000000000*I

        Here, we select a non-principal root for part of the interval, and
        violate the standard interval guarantees::

            sage: CIF(-5, RIF(-1, 1)).sqrt().str(style='brackets')
            '[-0.22250788030178321 .. 0.22250788030178296] + [2.2251857651053086 .. 2.2581008643532262]*I'
            sage: CIF(-5, -1).sqrt()
            0.222507880301783? - 2.247111425095870?*I"""
    @overload
    def sqrt(self) -> Any:
        """ComplexIntervalFieldElement.sqrt(self, bool all=False, **kwds)

        File: /build/sagemath/src/sage/src/sage/rings/complex_interval.pyx (starting at line 1843)

        The square root function.

        .. WARNING::

            We approximate the standard branch cut along the negative real
            axis, with ``sqrt(-r^2) = i*r`` for positive real ``r``; but if
            the interval crosses the negative real axis, we pick the root with
            positive imaginary component for the entire interval.

        INPUT:

        - ``all`` -- boolean (default: ``False``); if ``True``, return a list
          of all square roots

        EXAMPLES::

            sage: CIF(-1).sqrt()^2
            -1
            sage: sqrt(CIF(2))
            1.414213562373095?
            sage: sqrt(CIF(-1))
            1*I
            sage: sqrt(CIF(2-I))^2
            2.00000000000000? - 1.00000000000000?*I
            sage: CC(-2-I).sqrt()^2
            -2.00000000000000 - 1.00000000000000*I

        Here, we select a non-principal root for part of the interval, and
        violate the standard interval guarantees::

            sage: CIF(-5, RIF(-1, 1)).sqrt().str(style='brackets')
            '[-0.22250788030178321 .. 0.22250788030178296] + [2.2251857651053086 .. 2.2581008643532262]*I'
            sage: CIF(-5, -1).sqrt()
            0.222507880301783? - 2.247111425095870?*I"""
    @overload
    def sqrt(self) -> Any:
        """ComplexIntervalFieldElement.sqrt(self, bool all=False, **kwds)

        File: /build/sagemath/src/sage/src/sage/rings/complex_interval.pyx (starting at line 1843)

        The square root function.

        .. WARNING::

            We approximate the standard branch cut along the negative real
            axis, with ``sqrt(-r^2) = i*r`` for positive real ``r``; but if
            the interval crosses the negative real axis, we pick the root with
            positive imaginary component for the entire interval.

        INPUT:

        - ``all`` -- boolean (default: ``False``); if ``True``, return a list
          of all square roots

        EXAMPLES::

            sage: CIF(-1).sqrt()^2
            -1
            sage: sqrt(CIF(2))
            1.414213562373095?
            sage: sqrt(CIF(-1))
            1*I
            sage: sqrt(CIF(2-I))^2
            2.00000000000000? - 1.00000000000000?*I
            sage: CC(-2-I).sqrt()^2
            -2.00000000000000 - 1.00000000000000*I

        Here, we select a non-principal root for part of the interval, and
        violate the standard interval guarantees::

            sage: CIF(-5, RIF(-1, 1)).sqrt().str(style='brackets')
            '[-0.22250788030178321 .. 0.22250788030178296] + [2.2251857651053086 .. 2.2581008643532262]*I'
            sage: CIF(-5, -1).sqrt()
            0.222507880301783? - 2.247111425095870?*I"""
    @overload
    def str(self, base=..., style=...) -> Any:
        """ComplexIntervalFieldElement.str(self, base=10, style=None)

        File: /build/sagemath/src/sage/src/sage/rings/complex_interval.pyx (starting at line 225)

        Return a string representation of ``self``.

        EXAMPLES::

            sage: CIF(1.5).str()
            '1.5000000000000000?'
            sage: CIF(1.5, 2.5).str()
            '1.5000000000000000? + 2.5000000000000000?*I'
            sage: CIF(1.5, -2.5).str()
            '1.5000000000000000? - 2.5000000000000000?*I'
            sage: CIF(0, -2.5).str()
            '-2.5000000000000000?*I'
            sage: CIF(1.5).str(base=3)
            '1.1111111111111111111111111111111112?'
            sage: CIF(1, pi).str(style='brackets')                                      # needs sage.symbolic
            '[1.0000000000000000 .. 1.0000000000000000] + [3.1415926535897931 .. 3.1415926535897936]*I'

        .. SEEALSO::

            - :meth:`RealIntervalFieldElement.str`"""
    @overload
    def str(self) -> Any:
        """ComplexIntervalFieldElement.str(self, base=10, style=None)

        File: /build/sagemath/src/sage/src/sage/rings/complex_interval.pyx (starting at line 225)

        Return a string representation of ``self``.

        EXAMPLES::

            sage: CIF(1.5).str()
            '1.5000000000000000?'
            sage: CIF(1.5, 2.5).str()
            '1.5000000000000000? + 2.5000000000000000?*I'
            sage: CIF(1.5, -2.5).str()
            '1.5000000000000000? - 2.5000000000000000?*I'
            sage: CIF(0, -2.5).str()
            '-2.5000000000000000?*I'
            sage: CIF(1.5).str(base=3)
            '1.1111111111111111111111111111111112?'
            sage: CIF(1, pi).str(style='brackets')                                      # needs sage.symbolic
            '[1.0000000000000000 .. 1.0000000000000000] + [3.1415926535897931 .. 3.1415926535897936]*I'

        .. SEEALSO::

            - :meth:`RealIntervalFieldElement.str`"""
    @overload
    def str(self) -> Any:
        """ComplexIntervalFieldElement.str(self, base=10, style=None)

        File: /build/sagemath/src/sage/src/sage/rings/complex_interval.pyx (starting at line 225)

        Return a string representation of ``self``.

        EXAMPLES::

            sage: CIF(1.5).str()
            '1.5000000000000000?'
            sage: CIF(1.5, 2.5).str()
            '1.5000000000000000? + 2.5000000000000000?*I'
            sage: CIF(1.5, -2.5).str()
            '1.5000000000000000? - 2.5000000000000000?*I'
            sage: CIF(0, -2.5).str()
            '-2.5000000000000000?*I'
            sage: CIF(1.5).str(base=3)
            '1.1111111111111111111111111111111112?'
            sage: CIF(1, pi).str(style='brackets')                                      # needs sage.symbolic
            '[1.0000000000000000 .. 1.0000000000000000] + [3.1415926535897931 .. 3.1415926535897936]*I'

        .. SEEALSO::

            - :meth:`RealIntervalFieldElement.str`"""
    @overload
    def str(self) -> Any:
        """ComplexIntervalFieldElement.str(self, base=10, style=None)

        File: /build/sagemath/src/sage/src/sage/rings/complex_interval.pyx (starting at line 225)

        Return a string representation of ``self``.

        EXAMPLES::

            sage: CIF(1.5).str()
            '1.5000000000000000?'
            sage: CIF(1.5, 2.5).str()
            '1.5000000000000000? + 2.5000000000000000?*I'
            sage: CIF(1.5, -2.5).str()
            '1.5000000000000000? - 2.5000000000000000?*I'
            sage: CIF(0, -2.5).str()
            '-2.5000000000000000?*I'
            sage: CIF(1.5).str(base=3)
            '1.1111111111111111111111111111111112?'
            sage: CIF(1, pi).str(style='brackets')                                      # needs sage.symbolic
            '[1.0000000000000000 .. 1.0000000000000000] + [3.1415926535897931 .. 3.1415926535897936]*I'

        .. SEEALSO::

            - :meth:`RealIntervalFieldElement.str`"""
    @overload
    def str(self) -> Any:
        """ComplexIntervalFieldElement.str(self, base=10, style=None)

        File: /build/sagemath/src/sage/src/sage/rings/complex_interval.pyx (starting at line 225)

        Return a string representation of ``self``.

        EXAMPLES::

            sage: CIF(1.5).str()
            '1.5000000000000000?'
            sage: CIF(1.5, 2.5).str()
            '1.5000000000000000? + 2.5000000000000000?*I'
            sage: CIF(1.5, -2.5).str()
            '1.5000000000000000? - 2.5000000000000000?*I'
            sage: CIF(0, -2.5).str()
            '-2.5000000000000000?*I'
            sage: CIF(1.5).str(base=3)
            '1.1111111111111111111111111111111112?'
            sage: CIF(1, pi).str(style='brackets')                                      # needs sage.symbolic
            '[1.0000000000000000 .. 1.0000000000000000] + [3.1415926535897931 .. 3.1415926535897936]*I'

        .. SEEALSO::

            - :meth:`RealIntervalFieldElement.str`"""
    @overload
    def str(self, base=...) -> Any:
        """ComplexIntervalFieldElement.str(self, base=10, style=None)

        File: /build/sagemath/src/sage/src/sage/rings/complex_interval.pyx (starting at line 225)

        Return a string representation of ``self``.

        EXAMPLES::

            sage: CIF(1.5).str()
            '1.5000000000000000?'
            sage: CIF(1.5, 2.5).str()
            '1.5000000000000000? + 2.5000000000000000?*I'
            sage: CIF(1.5, -2.5).str()
            '1.5000000000000000? - 2.5000000000000000?*I'
            sage: CIF(0, -2.5).str()
            '-2.5000000000000000?*I'
            sage: CIF(1.5).str(base=3)
            '1.1111111111111111111111111111111112?'
            sage: CIF(1, pi).str(style='brackets')                                      # needs sage.symbolic
            '[1.0000000000000000 .. 1.0000000000000000] + [3.1415926535897931 .. 3.1415926535897936]*I'

        .. SEEALSO::

            - :meth:`RealIntervalFieldElement.str`"""
    @overload
    def str(self, style=...) -> Any:
        """ComplexIntervalFieldElement.str(self, base=10, style=None)

        File: /build/sagemath/src/sage/src/sage/rings/complex_interval.pyx (starting at line 225)

        Return a string representation of ``self``.

        EXAMPLES::

            sage: CIF(1.5).str()
            '1.5000000000000000?'
            sage: CIF(1.5, 2.5).str()
            '1.5000000000000000? + 2.5000000000000000?*I'
            sage: CIF(1.5, -2.5).str()
            '1.5000000000000000? - 2.5000000000000000?*I'
            sage: CIF(0, -2.5).str()
            '-2.5000000000000000?*I'
            sage: CIF(1.5).str(base=3)
            '1.1111111111111111111111111111111112?'
            sage: CIF(1, pi).str(style='brackets')                                      # needs sage.symbolic
            '[1.0000000000000000 .. 1.0000000000000000] + [3.1415926535897931 .. 3.1415926535897936]*I'

        .. SEEALSO::

            - :meth:`RealIntervalFieldElement.str`"""
    @overload
    def tan(self) -> Any:
        """ComplexIntervalFieldElement.tan(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_interval.pyx (starting at line 2005)

        Return the tangent of this complex interval.

        EXAMPLES::

            sage: CIF(1,1).tan()
            0.27175258531952? + 1.08392332733870?*I
            sage: CIF(2).tan()
            -2.185039863261519?
            sage: CIF(0,2).tan()
            0.964027580075817?*I"""
    @overload
    def tan(self) -> Any:
        """ComplexIntervalFieldElement.tan(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_interval.pyx (starting at line 2005)

        Return the tangent of this complex interval.

        EXAMPLES::

            sage: CIF(1,1).tan()
            0.27175258531952? + 1.08392332733870?*I
            sage: CIF(2).tan()
            -2.185039863261519?
            sage: CIF(0,2).tan()
            0.964027580075817?*I"""
    @overload
    def tan(self) -> Any:
        """ComplexIntervalFieldElement.tan(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_interval.pyx (starting at line 2005)

        Return the tangent of this complex interval.

        EXAMPLES::

            sage: CIF(1,1).tan()
            0.27175258531952? + 1.08392332733870?*I
            sage: CIF(2).tan()
            -2.185039863261519?
            sage: CIF(0,2).tan()
            0.964027580075817?*I"""
    @overload
    def tan(self) -> Any:
        """ComplexIntervalFieldElement.tan(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_interval.pyx (starting at line 2005)

        Return the tangent of this complex interval.

        EXAMPLES::

            sage: CIF(1,1).tan()
            0.27175258531952? + 1.08392332733870?*I
            sage: CIF(2).tan()
            -2.185039863261519?
            sage: CIF(0,2).tan()
            0.964027580075817?*I"""
    @overload
    def tanh(self) -> Any:
        """ComplexIntervalFieldElement.tanh(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_interval.pyx (starting at line 2092)

        Return the hyperbolic tangent of this complex interval.

        EXAMPLES::

            sage: CIF(1,1).tanh()
            1.08392332733870? + 0.27175258531952?*I
            sage: CIF(2).tanh()
            0.964027580075817?
            sage: CIF(0,2).tanh()
            -2.185039863261519?*I"""
    @overload
    def tanh(self) -> Any:
        """ComplexIntervalFieldElement.tanh(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_interval.pyx (starting at line 2092)

        Return the hyperbolic tangent of this complex interval.

        EXAMPLES::

            sage: CIF(1,1).tanh()
            1.08392332733870? + 0.27175258531952?*I
            sage: CIF(2).tanh()
            0.964027580075817?
            sage: CIF(0,2).tanh()
            -2.185039863261519?*I"""
    @overload
    def tanh(self) -> Any:
        """ComplexIntervalFieldElement.tanh(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_interval.pyx (starting at line 2092)

        Return the hyperbolic tangent of this complex interval.

        EXAMPLES::

            sage: CIF(1,1).tanh()
            1.08392332733870? + 0.27175258531952?*I
            sage: CIF(2).tanh()
            0.964027580075817?
            sage: CIF(0,2).tanh()
            -2.185039863261519?*I"""
    @overload
    def tanh(self) -> Any:
        """ComplexIntervalFieldElement.tanh(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_interval.pyx (starting at line 2092)

        Return the hyperbolic tangent of this complex interval.

        EXAMPLES::

            sage: CIF(1,1).tanh()
            1.08392332733870? + 0.27175258531952?*I
            sage: CIF(2).tanh()
            0.964027580075817?
            sage: CIF(0,2).tanh()
            -2.185039863261519?*I"""
    def union(self, other) -> Any:
        """ComplexIntervalFieldElement.union(self, other)

        File: /build/sagemath/src/sage/src/sage/rings/complex_interval.pyx (starting at line 580)

        Return the smallest complex interval including the
        two complex intervals ``self`` and ``other``.

        EXAMPLES::

            sage: CIF(0).union(CIF(5, 5)).str(style='brackets')
            '[0.0000000000000000 .. 5.0000000000000000] + [0.0000000000000000 .. 5.0000000000000000]*I'"""
    def zeta(self, a=...) -> Any:
        """ComplexIntervalFieldElement.zeta(self, a=None)

        File: /build/sagemath/src/sage/src/sage/rings/complex_interval.pyx (starting at line 2107)

        Return the image of this interval by the Hurwitz zeta function.

        For ``a = 1`` (or ``a = None``), this computes the Riemann zeta function.

        EXAMPLES::

            sage: zeta(CIF(2, 3))
            0.7980219851462757? - 0.1137443080529385?*I
            sage: _.parent()
            Complex Interval Field with 53 bits of precision
            sage: CIF(2, 3).zeta(1/2)
            -1.955171567161496? + 3.123301509220897?*I"""
    @overload
    def __abs__(self) -> Any:
        """ComplexIntervalFieldElement.__abs__(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_interval.pyx (starting at line 1099)

        Return the absolute value of ``self``.

        EXAMPLES::

            sage: abs(CIF(1.5, 2.5))
            2.915475947422650?
            sage: CIF(1.5, 2.5).__abs__()
            2.915475947422650?"""
    @overload
    def __abs__(self) -> Any:
        """ComplexIntervalFieldElement.__abs__(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_interval.pyx (starting at line 1099)

        Return the absolute value of ``self``.

        EXAMPLES::

            sage: abs(CIF(1.5, 2.5))
            2.915475947422650?
            sage: CIF(1.5, 2.5).__abs__()
            2.915475947422650?"""
    def __bool__(self) -> bool:
        """True if self else False"""
    def __complex__(self) -> Any:
        """ComplexIntervalFieldElement.__complex__(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_interval.pyx (starting at line 1397)

        Convert ``self`` to a ``complex``.

        EXAMPLES::

            sage: complex(CIF(1,1))
            (1+1j)"""
    def __contains__(self, other) -> Any:
        """ComplexIntervalFieldElement.__contains__(self, other)

        File: /build/sagemath/src/sage/src/sage/rings/complex_interval.pyx (starting at line 667)

        Test whether ``other`` is totally contained in ``self``.

        EXAMPLES::

            sage: CIF(1, 1) in CIF(RIF(1, 2), RIF(1, 2))
            True"""
    def __float__(self) -> Any:
        """ComplexIntervalFieldElement.__float__(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_interval.pyx (starting at line 1379)

        Convert ``self`` to a ``float``.

        EXAMPLES::

            sage: float(CIF(1))
            1.0
            sage: float(CIF(1,1))
            Traceback (most recent call last):
            ...
            TypeError: can...t convert complex interval to float"""
    def __getitem__(self, i) -> Any:
        """ComplexIntervalFieldElement.__getitem__(self, i)

        File: /build/sagemath/src/sage/src/sage/rings/complex_interval.pyx (starting at line 185)

        Return either the real or imaginary component of ``self`` depending
        on the choice of ``i``: real (``i=0``), imaginary (``i=1``)

        INPUT:

        - ``i`` -- 0 or 1

          - ``0`` -- will return the real component of ``self``
          - ``1`` -- will return the imaginary component of ``self``

        EXAMPLES::

            sage: z = CIF(1.5, 2.5)
            sage: z[0]
            1.5000000000000000?
            sage: z[1]
            2.5000000000000000?"""
    def __hash__(self) -> Any:
        """ComplexIntervalFieldElement.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_interval.pyx (starting at line 171)

        Return the hash value of ``self``.

        EXAMPLES::

            sage: C = ComplexIntervalField()
            sage: hash(CIF(1.5)) == hash(C(1.5))
            True
            sage: hash(CIF(1.5, 2.5)) != hash(CIF(2,3))
            True"""
    def __int__(self) -> Any:
        """ComplexIntervalFieldElement.__int__(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_interval.pyx (starting at line 1342)

        Convert ``self`` to an ``int``.

        EXAMPLES::

            sage: int(CIF(1,1))
            Traceback (most recent call last):
            ...
            TypeError: can...t convert complex interval to int"""
    @overload
    def __invert__(self) -> Any:
        """ComplexIntervalFieldElement.__invert__(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_interval.pyx (starting at line 1124)

        Return the multiplicative inverse of ``self``.

        EXAMPLES::

            sage: I = CIF.0
            sage: a = ~(5+I) # indirect doctest
            sage: a * (5+I)
            1.000000000000000? + 0.?e-16*I
            sage: a = CIF((1, 2), (3, 4))
            sage: c = a.__invert__()
            sage: c.endpoints()
            (0.0588235294117647 - 0.300000000000000*I,
             0.153846153846154 - 0.200000000000000*I,
             0.0588235294117647 - 0.200000000000000*I,
             0.153846153846154 - 0.300000000000000*I)

        TESTS:

        Check that the code is valid in all kind of complex intervals::

            sage: rpts = [0, -194323/42, -110/439423, -411923/122212,             ....:         15423/906, 337/59976, 145151/145112]
            sage: rpts = [RIF(a, b) if a <= b else RIF(b,a)             ....:       for a in rpts for b in rpts]
            sage: cpts = [CIF(a, b) for a in rpts for b in rpts if not CIF(a, b).contains_zero()]
            sage: for x in cpts:
            ....:     assert (x * (~x) - 1).contains_zero()

        Test that the bug reported in :issue:`25414` has been fixed::

            sage: 1 / CIF(RIF(-1 ,1), 0)
            [.. NaN ..] + [.. NaN ..]*I

        Test that the bug reported in :issue:`37927` is fixed::

            sage: (961 * (1 / CIF(0, 31))**2 + 1).contains_zero()
            True

        REFERENCES:

        - [RL1971]_"""
    @overload
    def __invert__(self) -> Any:
        """ComplexIntervalFieldElement.__invert__(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_interval.pyx (starting at line 1124)

        Return the multiplicative inverse of ``self``.

        EXAMPLES::

            sage: I = CIF.0
            sage: a = ~(5+I) # indirect doctest
            sage: a * (5+I)
            1.000000000000000? + 0.?e-16*I
            sage: a = CIF((1, 2), (3, 4))
            sage: c = a.__invert__()
            sage: c.endpoints()
            (0.0588235294117647 - 0.300000000000000*I,
             0.153846153846154 - 0.200000000000000*I,
             0.0588235294117647 - 0.200000000000000*I,
             0.153846153846154 - 0.300000000000000*I)

        TESTS:

        Check that the code is valid in all kind of complex intervals::

            sage: rpts = [0, -194323/42, -110/439423, -411923/122212,             ....:         15423/906, 337/59976, 145151/145112]
            sage: rpts = [RIF(a, b) if a <= b else RIF(b,a)             ....:       for a in rpts for b in rpts]
            sage: cpts = [CIF(a, b) for a in rpts for b in rpts if not CIF(a, b).contains_zero()]
            sage: for x in cpts:
            ....:     assert (x * (~x) - 1).contains_zero()

        Test that the bug reported in :issue:`25414` has been fixed::

            sage: 1 / CIF(RIF(-1 ,1), 0)
            [.. NaN ..] + [.. NaN ..]*I

        Test that the bug reported in :issue:`37927` is fixed::

            sage: (961 * (1 / CIF(0, 31))**2 + 1).contains_zero()
            True

        REFERENCES:

        - [RL1971]_"""
    @overload
    def __neg__(self) -> Any:
        """ComplexIntervalFieldElement.__neg__(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_interval.pyx (starting at line 1074)

        Return the negation of ``self``.

        EXAMPLES::

            sage: CIF(1.5, 2.5).__neg__()
            -1.5000000000000000? - 2.5000000000000000?*I"""
    @overload
    def __neg__(self) -> Any:
        """ComplexIntervalFieldElement.__neg__(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_interval.pyx (starting at line 1074)

        Return the negation of ``self``.

        EXAMPLES::

            sage: CIF(1.5, 2.5).__neg__()
            -1.5000000000000000? - 2.5000000000000000?*I"""
    @overload
    def __pos__(self) -> Any:
        '''ComplexIntervalFieldElement.__pos__(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_interval.pyx (starting at line 1088)

        Return the "positive" of ``self``, which is just ``self``.

        EXAMPLES::

            sage: CIF(1.5, 2.5).__pos__()
            1.5000000000000000? + 2.5000000000000000?*I'''
    @overload
    def __pos__(self) -> Any:
        '''ComplexIntervalFieldElement.__pos__(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_interval.pyx (starting at line 1088)

        Return the "positive" of ``self``, which is just ``self``.

        EXAMPLES::

            sage: CIF(1.5, 2.5).__pos__()
            1.5000000000000000? + 2.5000000000000000?*I'''
    def __pow__(self, right, modulus) -> Any:
        '''ComplexIntervalFieldElement.__pow__(self, right, modulus)

        File: /build/sagemath/src/sage/src/sage/rings/complex_interval.pyx (starting at line 815)

        Compute `x^y`.

        If `y` is an integer, uses multiplication;
        otherwise, uses the standard definition `\\exp(\\log(x) \\cdot y)`.

        .. WARNING::

            If the interval `x` crosses the negative real axis, then we use a
            non-standard definition of `\\log()` (see the docstring for
            :meth:`argument()` for more details). This means that we will not
            select the principal value of the power, for part of the input
            interval (and that we violate the interval guarantees).

        EXAMPLES::

            sage: C.<i> = ComplexIntervalField(20)
            sage: a = i^2; a
            -1
            sage: a.parent()
            Complex Interval Field with 20 bits of precision
            sage: a = (1+i)^7; a
            8 - 8*I
            sage: (1+i)^(1+i)
            0.27396? + 0.58370?*I
            sage: a.parent()
            Complex Interval Field with 20 bits of precision
            sage: (2+i)^(-39)
            1.688?e-14 + 1.628?e-14*I

        If the interval crosses the negative real axis, then we don\'t use the
        standard branch cut (and we violate the interval guarantees)::

            sage: (CIF(-7, RIF(-1, 1)) ^ CIF(0.3)).str(style=\'brackets\')
            \'[0.99109735947126309 .. 1.1179269966896264] + [1.4042388462787560 .. 1.4984624123369835]*I\'
            sage: CIF(-7, -1) ^ CIF(0.3)
            1.117926996689626? - 1.408500714575360?*I

        Note that ``x^2`` is not the same as ``x*x``::

            sage: a = CIF(RIF(-1,1))
            sage: print((a^2).str(style=\'brackets\'))
            [0.0000000000000000 .. 1.0000000000000000]
            sage: print((a*a).str(style=\'brackets\'))
            [-1.0000000000000000 .. 1.0000000000000000]
            sage: a = CIF(0, RIF(-1,1))
            sage: print((a^2).str(style=\'brackets\'))
            [-1.0000000000000000 .. -0.0000000000000000]
            sage: print((a*a).str(style=\'brackets\'))
            [-1.0000000000000000 .. 1.0000000000000000]
            sage: a = CIF(RIF(-1,1), RIF(-1,1))
            sage: print((a^2).str(style=\'brackets\'))
            [-1.0000000000000000 .. 1.0000000000000000] + [-2.0000000000000000 .. 2.0000000000000000]*I
            sage: print((a*a).str(style=\'brackets\'))
            [-2.0000000000000000 .. 2.0000000000000000] + [-2.0000000000000000 .. 2.0000000000000000]*I

        We can take very high powers::

            sage: RIF = RealIntervalField(27)
            sage: CIF = ComplexIntervalField(27)
            sage: s = RealField(27, rnd="RNDZ")(1/2)^(1/3)
            sage: a = CIF(RIF(-s/2,s/2), RIF(-s, s))
            sage: r = a^(10^10000)
            sage: print(r.str(style=\'brackets\'))
            [-2.107553304e1028 .. 2.107553304e1028] + [-2.107553304e1028 .. 2.107553304e1028]*I

        TESTS::

            sage: CIF = ComplexIntervalField(7)
            sage: [CIF(2) ^ RDF(i) for i in range(-5,6)]
            [0.03125?, 0.06250?, 0.1250?, 0.2500?, 0.5000?, 1, 2, 4, 8, 16, 32]
            sage: pow(CIF(1), CIF(1), CIF(1))
            Traceback (most recent call last):
            ...
            TypeError: pow() 3rd argument not allowed unless all arguments are integers'''
    def __reduce__(self) -> Any:
        """ComplexIntervalFieldElement.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/rings/complex_interval.pyx (starting at line 211)

        Pickling support.

        TESTS::

            sage: a = CIF(1 + I)
            sage: loads(dumps(a)) == a
            True"""
    def __rpow__(self, other):
        """Return pow(value, self, mod)."""
