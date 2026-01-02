"""
Other functions

TESTS:

Check that gamma function imports are deprecated (:issue:`24411`)::

    sage: from sage.functions.other import beta
    sage: beta(x, x)                                                                    # needs sage.symbolic
    doctest:warning...: DeprecationWarning:
    Importing beta from here is deprecated; please use "from sage.functions.gamma import beta" instead.
    See https://github.com/sagemath/sage/issues/24411 for details.
    beta(x, x)
"""
from sage.functions.trig import arctan2 as arctan2
from sage.misc.functional import sqrt as sqrt
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.rings.integer import Integer as Integer
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.rational import Rational as Rational
from sage.structure.element import Element as Element, Expression as Expression, coercion_model as coercion_model
from sage.symbolic.function import BuiltinFunction as BuiltinFunction, GinacFunction as GinacFunction
from sage.symbolic.symbols import register_symbol as register_symbol, symbol_table as symbol_table

class Function_abs(GinacFunction):
    def __init__(self) -> None:
        """
        The absolute value function.

        EXAMPLES::

            sage: abs(-2)
            2

            sage: # needs sage.symbolic
            sage: var('x y')
            (x, y)
            sage: abs(x)
            abs(x)
            sage: abs(x^2 + y^2)
            abs(x^2 + y^2)
            sage: sqrt(x^2)
            sqrt(x^2)
            sage: abs(sqrt(x))
            sqrt(abs(x))
            sage: complex(abs(3*I))
            (3+0j)

            sage: f = sage.functions.other.Function_abs()
            sage: latex(f)
            \\mathrm{abs}
            sage: latex(abs(x))                                                         # needs sage.symbolic
            {\\left| x \\right|}
            sage: abs(x)._sympy_()                                                      # needs sympy sage.symbolic
            Abs(x)

        Test pickling::

            sage: loads(dumps(abs(x)))                                                  # needs sage.symbolic
            abs(x)

        TESTS:

        Check that :issue:`12588` is fixed::

            sage: # needs sage.symbolic
            sage: abs(pi*I)
            pi
            sage: abs(pi*I*catalan)
            catalan*pi
            sage: abs(pi*catalan*x)
            catalan*pi*abs(x)
            sage: abs(pi*I*catalan*x)
            catalan*pi*abs(x)
            sage: abs(1.0j*pi)
            1.00000000000000*pi
            sage: abs(I*x)
            abs(x)
            sage: abs(I*pi)
            pi
            sage: abs(I*log(2))
            log(2)
            sage: abs(I*e^5)
            e^5
            sage: abs(log(1/2))
            -log(1/2)
            sage: abs(log(3/2))
            log(3/2)
            sage: abs(log(1/2)*log(1/3))
            log(1/2)*log(1/3)
            sage: abs(log(1/2)*log(1/3)*log(1/4))
            -log(1/2)*log(1/3)*log(1/4)
            sage: abs(log(1/2)*log(1/3)*log(1/4)*i)
            -log(1/2)*log(1/3)*log(1/4)
            sage: abs(log(x))
            abs(log(x))
            sage: abs(zeta(I))
            abs(zeta(I))
            sage: abs(e^2*x)
            abs(x)*e^2
            sage: abs((pi+e)*x)
            (pi + e)*abs(x)

            sage: fricas(abs(x)).sage().derivative()    # optional - fricas             # needs sage.symbolic
            1/2*(x + conjugate(x))/abs(x)
        """

abs: Function_abs

abs_symbolic: Function_abs

class Function_ceil(BuiltinFunction):
    def __init__(self) -> None:
        """
        The ceiling function.

        The ceiling of `x` is computed in the following manner.


        #. The ``x.ceil()`` method is called and returned if it
           is there. If it is not, then Sage checks if `x` is one of
           Python's native numeric data types. If so, then it calls and
           returns ``Integer(math.ceil(x))``.

        #. Sage tries to convert `x` into a
           ``RealIntervalField`` with 53 bits of precision. Next,
           the ceilings of the endpoints are computed. If they are the same,
           then that value is returned. Otherwise, the precision of the
           ``RealIntervalField`` is increased until they do match
           up or it reaches ``bits`` of precision.

        #. If none of the above work, Sage returns a
           ``Expression`` object.

        EXAMPLES::

            sage: # needs sage.symbolic
            sage: a = ceil(2/5 + x); a
            ceil(x + 2/5)
            sage: a(x=4)
            5
            sage: a(x=4.0)
            5
            sage: ZZ(a(x=3))
            4
            sage: a = ceil(x^3 + x + 5/2); a
            ceil(x^3 + x + 5/2)
            sage: a.simplify()
            ceil(x^3 + x + 1/2) + 2
            sage: a(x=2)
            13

        ::

            sage: ceil(sin(8)/sin(2))                                                   # needs sage.symbolic
            2

        ::

            sage: ceil(5.4)
            6
            sage: type(ceil(5.4))
            <class 'sage.rings.integer.Integer'>

        ::

            sage: ceil(factorial(50)/exp(1))                                            # needs sage.symbolic
            11188719610782480504630258070757734324011354208865721592720336801
            sage: ceil(SR(10^50 + 10^(-50)))                                            # needs sage.symbolic
            100000000000000000000000000000000000000000000000001
            sage: ceil(SR(10^50 - 10^(-50)))                                            # needs sage.symbolic
            100000000000000000000000000000000000000000000000000

        Small numbers which are extremely close to an integer are hard to
        deal with::

            sage: ceil((33^100 + 1)^(1/100))                                            # needs sage.symbolic
            Traceback (most recent call last):
            ...
            ValueError: cannot compute ceil(...) using 256 bits of precision

        This can be fixed by giving a sufficiently large ``bits`` argument::

            sage: ceil((33^100 + 1)^(1/100), bits=500)                                  # needs sage.symbolic
            Traceback (most recent call last):
            ...
            ValueError: cannot compute ceil(...) using 512 bits of precision
            sage: ceil((33^100 + 1)^(1/100), bits=1000)                                 # needs sage.symbolic
            34

        ::

            sage: ceil(sec(e))                                                          # needs sage.symbolic
            -1

            sage: latex(ceil(x))                                                        # needs sage.symbolic
            \\left \\lceil x \\right \\rceil
            sage: ceil(x)._sympy_()                                                     # needs sympy sage.symbolic
            ceiling(x)

        ::

            sage: import numpy                                                          # needs numpy
            sage: a = numpy.linspace(0,2,6)                                             # needs numpy
            sage: ceil(a)                                                               # needs numpy
            array([0., 1., 1., 2., 2., 2.])

        Test pickling::

            sage: loads(dumps(ceil))
            ceil
        """
    def __call__(self, x, **kwds):
        """
        Allow an object of this class to behave like a function. If
        ``ceil`` is an instance of this class, we can do ``ceil(n)`` to get
        the ceiling of ``n``.

        TESTS::

            sage: ceil(SR(10^50 + 10^(-50)))                                            # needs sage.symbolic
            100000000000000000000000000000000000000000000000001
            sage: ceil(SR(10^50 - 10^(-50)))                                            # needs sage.symbolic
            100000000000000000000000000000000000000000000000000
            sage: ceil(int(10^50))
            100000000000000000000000000000000000000000000000000
            sage: ceil((1725033*pi - 5419351)/(25510582*pi - 80143857))                 # needs sage.symbolic
            -2
        """

ceil: Function_ceil

class Function_floor(BuiltinFunction):
    def __init__(self) -> None:
        """
        The floor function.

        The floor of `x` is computed in the following manner.


        #. The ``x.floor()`` method is called and returned if
           it is there. If it is not, then Sage checks if `x` is one
           of Python's native numeric data types. If so, then it calls and
           returns ``Integer(math.floor(x))``.

        #. Sage tries to convert `x` into a
           ``RealIntervalField`` with 53 bits of precision. Next,
           the floors of the endpoints are computed. If they are the same,
           then that value is returned. Otherwise, the precision of the
           ``RealIntervalField`` is increased until they do match
           up or it reaches ``bits`` of precision.

        #. If none of the above work, Sage returns a
           symbolic ``Expression`` object.

        EXAMPLES::

            sage: floor(5.4)
            5
            sage: type(floor(5.4))
            <class 'sage.rings.integer.Integer'>

            sage: # needs sage.symbolic
            sage: var('x')
            x
            sage: a = floor(5.25 + x); a
            floor(x + 5.25000000000000)
            sage: a.simplify()
            floor(x + 0.25) + 5
            sage: a(x=2)
            7

        ::

            sage: # needs sage.symbolic
            sage: floor(cos(8) / cos(2))
            0
            sage: floor(log(4) / log(2))
            2
            sage: a = floor(5.4 + x); a
            floor(x + 5.40000000000000)
            sage: a.subs(x==2)
            7
            sage: floor(log(2^(3/2)) / log(2) + 1/2)
            2
            sage: floor(log(2^(-3/2)) / log(2) + 1/2)
            -1

        ::

            sage: floor(factorial(50)/exp(1))                                           # needs sage.symbolic
            11188719610782480504630258070757734324011354208865721592720336800
            sage: floor(SR(10^50 + 10^(-50)))                                           # needs sage.symbolic
            100000000000000000000000000000000000000000000000000
            sage: floor(SR(10^50 - 10^(-50)))                                           # needs sage.symbolic
            99999999999999999999999999999999999999999999999999
            sage: floor(int(10^50))
            100000000000000000000000000000000000000000000000000

        Small numbers which are extremely close to an integer are hard to
        deal with::

            sage: floor((33^100 + 1)^(1/100))                                           # needs sage.symbolic
            Traceback (most recent call last):
            ...
            ValueError: cannot compute floor(...) using 256 bits of precision

        This can be fixed by giving a sufficiently large ``bits`` argument::

            sage: floor((33^100 + 1)^(1/100), bits=500)                                 # needs sage.symbolic
            Traceback (most recent call last):
            ...
            ValueError: cannot compute floor(...) using 512 bits of precision
            sage: floor((33^100 + 1)^(1/100), bits=1000)                                # needs sage.symbolic
            33

        ::

            sage: import numpy                                                          # needs numpy
            sage: a = numpy.linspace(0,2,6)                                             # needs numpy
            sage: floor(a)                                                              # needs numpy
            array([0., 0., 0., 1., 1., 2.])
            sage: floor(x)._sympy_()                                                    # needs sympy sage.symbolic
            floor(x)

        Test pickling::

            sage: loads(dumps(floor))
            floor
        """
    def __call__(self, x, **kwds):
        """
        Allow an object of this class to behave like a function. If
        ``floor`` is an instance of this class, we can do ``floor(n)`` to
        obtain the floor of ``n``.

        TESTS::

            sage: floor(SR(10^50 + 10^(-50)))                                           # needs sage.symbolic
            100000000000000000000000000000000000000000000000000
            sage: floor(SR(10^50 - 10^(-50)))                                           # needs sage.symbolic
            99999999999999999999999999999999999999999999999999
            sage: floor(int(10^50))
            100000000000000000000000000000000000000000000000000
            sage: floor((1725033*pi - 5419351)/(25510582*pi - 80143857))                # needs sage.symbolic
            -3
        """

floor: Function_floor

class Function_Order(GinacFunction):
    def __init__(self) -> None:
        """
        The order function.

        This function gives the order of magnitude of some expression,
        similar to `O`-terms.

        .. SEEALSO::

            :meth:`~sage.symbolic.expression.Expression.Order`,
            :mod:`~sage.rings.big_oh`

        EXAMPLES::

            sage: x = SR('x')                                                           # needs sage.symbolic
            sage: x.Order()                                                             # needs sage.symbolic
            Order(x)
            sage: (x^2 + x).Order()                                                     # needs sage.symbolic
            Order(x^2 + x)

        TESTS:

        Check that :issue:`19425` is resolved::

            sage: x.Order().operator()                                                  # needs sage.symbolic
            Order
        """

Order: Function_Order

class Function_frac(BuiltinFunction):
    def __init__(self) -> None:
        """
        The fractional part function `\\{x\\}`.

        ``frac(x)`` is defined as `\\{x\\} = x - \\lfloor x\\rfloor`.

        EXAMPLES::

            sage: frac(5.4)                                                             # needs sage.rings.real_mpfr
            0.400000000000000
            sage: type(frac(5.4))                                                       # needs sage.rings.real_mpfr
            <class 'sage.rings.real_mpfr.RealNumber'>
            sage: frac(456/123)
            29/41

            sage: # needs sage.symbolic
            sage: var('x')
            x
            sage: a = frac(5.4 + x); a
            frac(x + 5.40000000000000)
            sage: frac(cos(8)/cos(2))
            cos(8)/cos(2)
            sage: latex(frac(x))
            \\operatorname{frac}\\left(x\\right)
            sage: frac(x)._sympy_()                                                     # needs sympy
            frac(x)

        Test pickling::

            sage: loads(dumps(floor))
            floor
        """

frac: Function_frac
Function_sqrt: Function_frac

class Function_real_nth_root(BuiltinFunction):
    """
    Real `n`-th root function `x^\\frac{1}{n}`.

    The function assumes positive integer `n` and real number `x`.

    EXAMPLES::

        sage: real_nth_root(2, 3)                                                       # needs sage.symbolic
        2^(1/3)
        sage: real_nth_root(-2, 3)                                                      # needs sage.symbolic
        -2^(1/3)
        sage: real_nth_root(8, 3)
        2
        sage: real_nth_root(-8, 3)
        -2

        sage: real_nth_root(-2, 4)
        Traceback (most recent call last):
        ...
        ValueError: no real nth root of negative real number with even n

    For numeric input, it gives a numerical approximation. ::

        sage: real_nth_root(2., 3)                                                      # needs sage.rings.real_mpfr
        1.25992104989487
        sage: real_nth_root(-2., 3)                                                     # needs sage.rings.real_mpfr
        -1.25992104989487

    Some symbolic calculus::

        sage: # needs sage.symbolic
        sage: f = real_nth_root(x, 5)^3; f
        real_nth_root(x^3, 5)
        sage: f.diff()
        3/5*x^2*real_nth_root(x^(-12), 5)
        sage: result = f.integrate(x)
        ...
        sage: result
        integrate((abs(x)^3)^(1/5)*sgn(x^3), x)
        sage: _.diff()
        (abs(x)^3)^(1/5)*sgn(x^3)
    """
    def __init__(self) -> None:
        """
        Initialize.

        TESTS::

            sage: cube_root = real_nth_root(x, 3)                                       # needs sage.symbolic
            sage: loads(dumps(cube_root))                                               # needs sage.symbolic
            real_nth_root(x, 3)

        ::

            sage: f = real_nth_root(x, 3)                                               # needs sage.symbolic
            sage: f._sympy_()                                                           # needs sympy sage.symbolic
            Piecewise((Abs(x)**(1/3)*sign(x), Eq(im(x), 0)), (x**(1/3), True))
        """

real_nth_root: Function_real_nth_root

class Function_arg(BuiltinFunction):
    def __init__(self) -> None:
        """
        The argument function for complex numbers.

        EXAMPLES::

            sage: # needs sage.symbolic
            sage: arg(3+i)
            arctan(1/3)
            sage: arg(-1+i)
            3/4*pi
            sage: arg(2+2*i)
            1/4*pi
            sage: arg(2+x)
            arg(x + 2)
            sage: arg(2.0+i+x)
            arg(x + 2.00000000000000 + 1.00000000000000*I)
            sage: arg(-3)
            pi
            sage: arg(3)
            0
            sage: arg(0)
            0

            sage: # needs sage.symbolic
            sage: latex(arg(x))
            {\\rm arg}\\left(x\\right)
            sage: maxima(arg(x))
            atan2(0,_SAGE_VAR_x)
            sage: maxima(arg(2+i))
            atan(1/2)
            sage: maxima(arg(sqrt(2)+i))
            atan(1/sqrt(2))
            sage: arg(x)._sympy_()                                                      # needs sympy
            arg(x)

            sage: arg(2+i)                                                              # needs sage.symbolic
            arctan(1/2)
            sage: arg(sqrt(2)+i)                                                        # needs sage.symbolic
            arg(sqrt(2) + I)
            sage: arg(sqrt(2)+i).simplify()                                             # needs sage.symbolic
            arctan(1/2*sqrt(2))

        TESTS::

            sage: arg(0.0)                                                              # needs sage.rings.complex_double
            0.000000000000000
            sage: arg(3.0)                                                              # needs sage.rings.complex_double
            0.000000000000000
            sage: arg(-2.5)                                                             # needs sage.rings.complex_double
            3.14159265358979
            sage: arg(2.0+3*i)                                                          # needs sage.symbolic
            0.982793723247329
        """

arg: Function_arg

class Function_real_part(GinacFunction):
    def __init__(self) -> None:
        """
        Return the real part of the (possibly complex) input.

        It is possible to prevent automatic evaluation using the
        ``hold`` parameter::

            sage: real_part(I, hold=True)                                               # needs sage.symbolic
            real_part(I)

        To then evaluate again, we currently must use Maxima via
        :meth:`sage.symbolic.expression.Expression.simplify`::

            sage: real_part(I, hold=True).simplify()                                    # needs sage.symbolic
            0

        EXAMPLES::

            sage: z = 1+2*I                                                             # needs sage.symbolic
            sage: real(z)                                                               # needs sage.symbolic
            1
            sage: real(5/3)
            5/3
            sage: a = 2.5
            sage: real(a)                                                               # needs sage.rings.real_mpfr
            2.50000000000000
            sage: type(real(a))                                                         # needs sage.rings.real_mpfr
            <class 'sage.rings.real_mpfr.RealLiteral'>
            sage: real(1.0r)
            1.0
            sage: real(complex(3, 4))
            3.0

        Sage can recognize some expressions as real and accordingly
        return the identical argument::

            sage: # needs sage.symbolic
            sage: SR.var('x', domain='integer').real_part()
            x
            sage: SR.var('x', domain='integer').imag_part()
            0
            sage: real_part(sin(x)+x)
            x + sin(x)
            sage: real_part(x*exp(x))
            x*e^x
            sage: imag_part(sin(x)+x)
            0
            sage: real_part(real_part(x))
            x
            sage: forget()

        TESTS::

            sage: loads(dumps(real_part))
            real_part
            sage: real_part(x)._sympy_()                                                # needs sympy sage.symbolic
            re(x)

        Check if :issue:`6401` is fixed::

            sage: latex(x.real())                                                       # needs sage.symbolic
            \\Re \\left( x \\right)

            sage: f(x) = function('f')(x)                                               # needs sage.symbolic
            sage: latex( f(x).real())                                                   # needs sage.symbolic
            \\Re \\left( f\\left(x\\right) \\right)

        Check that some real part expansions evaluate correctly
        (:issue:`21614`)::

            sage: real(sqrt(sin(x))).subs(x==0)                                         # needs sage.symbolic
            0
        """
    def __call__(self, x, **kwargs):
        """
        TESTS::

            sage: type(real(complex(3, 4)))
            <... 'float'>
        """

real: Function_real_part

real_part: Function_real_part

class Function_imag_part(GinacFunction):
    def __init__(self) -> None:
        """
        Return the imaginary part of the (possibly complex) input.

        It is possible to prevent automatic evaluation using the
        ``hold`` parameter::

            sage: imag_part(I, hold=True)                                               # needs sage.symbolic
            imag_part(I)

        To then evaluate again, we currently must use Maxima via
        :meth:`sage.symbolic.expression.Expression.simplify`::

            sage: imag_part(I, hold=True).simplify()                                    # needs sage.symbolic
            1

        TESTS::

            sage: z = 1+2*I                                                             # needs sage.symbolic
            sage: imaginary(z)                                                          # needs sage.symbolic
            2
            sage: imag(z)                                                               # needs sage.symbolic
            2
            sage: imag(complex(3, 4))
            4.0
            sage: loads(dumps(imag_part))
            imag_part
            sage: imag_part(x)._sympy_()                                                # needs sympy sage.symbolic
            im(x)

        Check if :issue:`6401` is fixed::

            sage: latex(x.imag())                                                       # needs sage.symbolic
            \\Im \\left( x \\right)

            sage: f(x) = function('f')(x)                                               # needs sage.symbolic
            sage: latex(f(x).imag())                                                    # needs sage.symbolic
            \\Im \\left( f\\left(x\\right) \\right)
        """
    def __call__(self, x, **kwargs):
        """
        TESTS::

            sage: type(imag(complex(3, 4)))
            <... 'float'>
        """

imag: Function_imag_part

imag_part: Function_imag_part

imaginary: Function_imag_part

class Function_conjugate(GinacFunction):
    def __init__(self) -> None:
        """
        Return the complex conjugate of the input.

        It is possible to prevent automatic evaluation using the
        ``hold`` parameter::

            sage: conjugate(I, hold=True)                                               # needs sage.symbolic
            conjugate(I)

        To then evaluate again, we currently must use Maxima via
        :meth:`sage.symbolic.expression.Expression.simplify`::

            sage: conjugate(I, hold=True).simplify()                                    # needs sage.symbolic
            -I

        TESTS::

            sage: # needs sage.symbolic
            sage: x,y = var('x,y')
            sage: x.conjugate()
            conjugate(x)
            sage: _._sympy_()                                                           # needs sympy
            conjugate(x)
            sage: latex(conjugate(x))
            \\overline{x}
            sage: f = function('f')
            sage: latex(f(x).conjugate())
            \\overline{f\\left(x\\right)}
            sage: f = function('psi')(x,y)
            sage: latex(f.conjugate())
            \\overline{\\psi\\left(x, y\\right)}
            sage: x.conjugate().conjugate()
            x
            sage: x.conjugate().operator()
            conjugate
            sage: x.conjugate().operator() == conjugate
            True

        Check if :issue:`8755` is fixed::

            sage: # needs sage.symbolic
            sage: conjugate(sqrt(-3))
            conjugate(sqrt(-3))
            sage: conjugate(sqrt(3))
            sqrt(3)
            sage: conjugate(sqrt(x))
            conjugate(sqrt(x))
            sage: conjugate(x^2)
            conjugate(x)^2
            sage: var('y', domain='positive')
            y
            sage: conjugate(sqrt(y))
            sqrt(y)

        Check if :issue:`10964` is fixed::

            sage: # needs sage.symbolic
            sage: z = I*sqrt(-3); z
            I*sqrt(-3)
            sage: conjugate(z)
            -I*conjugate(sqrt(-3))
            sage: var('a')
            a
            sage: conjugate(a*sqrt(-2)*sqrt(-3))
            conjugate(sqrt(-2))*conjugate(sqrt(-3))*conjugate(a)

        Check that sums are handled correctly::

            sage: y = var('y', domain='real')                                           # needs sage.symbolic
            sage: conjugate(y + I)                                                      # needs sage.symbolic
            y - I

        Test pickling::

            sage: loads(dumps(conjugate))
            conjugate
        """

conjugate: Function_conjugate

class Function_factorial(GinacFunction):
    def __init__(self) -> None:
        """
        Return the factorial of `n`.

        INPUT:

        - ``n`` -- a nonnegative integer, a complex number (except negative
          integers) or any symbolic expression

        OUTPUT: integer or symbolic expression

        EXAMPLES::

            sage: factorial(0)
            1
            sage: factorial(4)
            24
            sage: factorial(10)
            3628800
            sage: factorial(6) == 6*5*4*3*2
            True

            sage: # needs sage.symbolic
            sage: x = SR.var('x')
            sage: f = factorial(x + factorial(x)); f
            factorial(x + factorial(x))
            sage: f(x=3)
            362880
            sage: factorial(x)^2
            factorial(x)^2

        To prevent automatic evaluation use the ``hold`` argument::

            sage: factorial(5, hold=True)                                               # needs sage.symbolic
            factorial(5)

        To then evaluate again, we currently must use Maxima via
        :meth:`sage.symbolic.expression.Expression.simplify`::

            sage: factorial(5, hold=True).simplify()                                    # needs sage.symbolic
            120

        We can also give input other than nonnegative integers.  For
        other nonnegative numbers, the :func:`sage.functions.gamma.gamma`
        function is used::

            sage: factorial(1/2)                                                        # needs sage.symbolic
            1/2*sqrt(pi)
            sage: factorial(3/4)                                                        # needs sage.symbolic
            gamma(7/4)
            sage: factorial(2.3)                                                        # needs sage.symbolic
            2.68343738195577

        But negative input always fails::

            sage: factorial(-32)
            Traceback (most recent call last):
            ...
            ValueError: factorial only defined for nonnegative integers

        And very large integers remain unevaluated::

            sage: factorial(2**64)                                                      # needs sage.symbolic
            factorial(18446744073709551616)
            sage: SR(2**64).factorial()                                                 # needs sage.symbolic
            factorial(18446744073709551616)

        TESTS:

        We verify that we can convert this function to Maxima and
        bring it back into Sage.::

            sage: # needs sage.symbolic
            sage: z = var('z')
            sage: factorial._maxima_init_()
            'factorial'
            sage: maxima(factorial(z))
            factorial(_SAGE_VAR_z)
            sage: _.sage()
            factorial(z)
            sage: _._sympy_()                                                           # needs sympy
            factorial(z)
            sage: k = var('k')
            sage: factorial(k)
            factorial(k)

            sage: factorial(3.14)                                                       # needs sage.symbolic
            7.173269190187...

        Test latex typesetting::

            sage: # needs sage.symbolic
            sage: latex(factorial(x))
            x!
            sage: latex(factorial(2*x))
            \\left(2 \\, x\\right)!
            sage: latex(factorial(sin(x)))
            \\sin\\left(x\\right)!
            sage: latex(factorial(sqrt(x+1)))
            \\left(\\sqrt{x + 1}\\right)!
            sage: latex(factorial(sqrt(x)))
            \\sqrt{x}!
            sage: latex(factorial(x^(2/3)))
            \\left(x^{\\frac{2}{3}}\\right)!

            sage: latex(factorial)
            {\\rm factorial}

        Check that :issue:`11539` is fixed::

            sage: # needs sage.symbolic
            sage: (factorial(x) == 0).simplify()
            factorial(x) == 0
            sage: maxima(factorial(x) == 0).sage()
            factorial(x) == 0
            sage: y = var('y')
            sage: (factorial(x) == y).solve(x)
            [factorial(x) == y]

        Check that :issue:`16166` is fixed::

            sage: RBF = RealBallField(53)                                               # needs sage.libs.flint
            sage: factorial(RBF(4.2))  # abs tol 1e-13                                  # needs sage.libs.flint
            [32.5780960503314 +/- 6.06e-14]

        Test pickling::

            sage: loads(dumps(factorial))
            factorial
        """

factorial: Function_factorial

class Function_binomial(GinacFunction):
    def __init__(self) -> None:
        """
        Return the binomial coefficient.

        .. MATH::

            \\binom{x}{m} = x (x-1) \\cdots (x-m+1) / m!


        which is defined for `m \\in \\ZZ` and any
        `x`. We extend this definition to include cases when
        `x-m` is an integer but `m` is not by

        .. MATH::

            \\binom{x}{m}= \\binom{x}{x-m}

        If `m < 0`, return `0`.

        INPUT:

        - ``x``, ``m`` -- numbers or symbolic expressions; either ``m``
          or ``x-m`` must be an integer, else the output is symbolic

        OUTPUT: number or symbolic expression (if input is symbolic)

        EXAMPLES::

            sage: # needs sage.symbolic
            sage: binomial(5, 2)
            10
            sage: binomial(2, 0)
            1
            sage: binomial(1/2, 0)                                                      # needs sage.libs.pari
            1
            sage: binomial(3, -1)
            0
            sage: binomial(20, 10)
            184756
            sage: binomial(-2, 5)
            -6
            sage: n = var('n'); binomial(n, 2)
            1/2*(n - 1)*n
            sage: n = var('n'); binomial(n, n)
            1
            sage: n = var('n'); binomial(n, n - 1)
            n
            sage: binomial(2^100, 2^100)
            1

            sage: binomial(RealField()('2.5'), 2)                                       # needs sage.rings.real_mpfr
            1.87500000000000

        ::

            sage: k, i = var('k,i')                                                     # needs sage.symbolic
            sage: binomial(k,i)                                                         # needs sage.symbolic
            binomial(k, i)

        We can use a ``hold`` parameter to prevent automatic evaluation::

            sage: SR(5).binomial(3, hold=True)                                          # needs sage.symbolic
            binomial(5, 3)
            sage: SR(5).binomial(3, hold=True).simplify()                               # needs sage.symbolic
            10

        TESTS:

        We verify that we can convert this function to Maxima and
        bring it back into Sage.

        ::

            sage: # needs sage.symbolic
            sage: n, k = var('n,k')
            sage: maxima(binomial(n,k))
            binomial(_SAGE_VAR_n,_SAGE_VAR_k)
            sage: _.sage()
            binomial(n, k)
            sage: _._sympy_()                                                           # needs sympy
            binomial(n, k)
            sage: binomial._maxima_init_()
            'binomial'

        For polynomials::

            sage: y = polygen(QQ, 'y')
            sage: binomial(y, 2).parent()                                               # needs sage.symbolic
            Univariate Polynomial Ring in y over Rational Field

        :issue:`16726`::

            sage: binomial(CIF(1), 2)                                                   # needs sage.symbolic
            0
            sage: binomial(CIF(3), 2)                                                   # needs sage.symbolic
            3

        Test pickling::

            sage: loads(dumps(binomial(n, k)))                                          # needs sage.symbolic
            binomial(n, k)
        """

binomial: Function_binomial

class Function_sum(BuiltinFunction):
    """
    Placeholder symbolic sum function that is only accessible internally.

    EXAMPLES::

        sage: from sage.functions.other import symbolic_sum as ssum
        sage: r = ssum(x, x, 1, 10); r                                                  # needs sage.symbolic
        sum(x, x, 1, 10)
        sage: r.unhold()                                                                # needs sage.symbolic
        55
    """
    def __init__(self) -> None:
        """
        EXAMPLES::

            sage: from sage.functions.other import symbolic_sum as ssum
            sage: maxima(ssum(x, x, 1, 10))                                             # needs sage.symbolic
            55
        """

symbolic_sum: Function_sum

class Function_prod(BuiltinFunction):
    """
    Placeholder symbolic product function that is only accessible internally.

    EXAMPLES::

        sage: from sage.functions.other import symbolic_product as sprod
        sage: r = sprod(x, x, 1, 10); r                                                 # needs sage.symbolic
        product(x, x, 1, 10)
        sage: r.unhold()                                                                # needs sage.symbolic
        3628800
    """
    def __init__(self) -> None:
        """
        EXAMPLES::

            sage: # needs sage.symbolic
            sage: from sage.functions.other import symbolic_product as sprod
            sage: _ = var('m n', domain='integer')
            sage: r = maxima(sprod(sin(m), m, 1, n)).sage(); r
            product(sin(m), m, 1, n)
            sage: isinstance(r.operator(), sage.functions.other.Function_prod)
            True
            sage: r = sympy(sprod(sin(m), m, 1, n)).sage(); r   # known bug             # needs sympy
            product(sin(m), m, 1, n)
            sage: isinstance(r.operator(),      # known bug                             # needs sympy
            ....:     sage.functions.other.Function_prod)
            True
            sage: giac(sprod(m, m, 1, n)).sage()  # needs giac
            factorial(n)
        """

symbolic_product: Function_prod

class Function_limit(BuiltinFunction):
    """
    Placeholder symbolic limit function that is only accessible internally.

    This function is called to create formal wrappers of limits that
    Maxima can't compute::

        sage: a = lim(exp(x^2)*(1-erf(x)), x=infinity); a                               # needs sage.symbolic
        -limit((erf(x) - 1)*e^(x^2), x, +Infinity)

    EXAMPLES::

        sage: # needs sage.symbolic
        sage: from sage.functions.other import symbolic_limit as slimit
        sage: slimit(1/x, x, +oo)
        limit(1/x, x, +Infinity)
        sage: var('minus,plus')
        (minus, plus)
        sage: slimit(1/x, x, +oo)
        limit(1/x, x, +Infinity)
        sage: slimit(1/x, x, 0, plus)
        limit(1/x, x, 0, plus)
        sage: slimit(1/x, x, 0, minus)
        limit(1/x, x, 0, minus)
    """
    def __init__(self) -> None:
        """
        EXAMPLES::

            sage: from sage.functions.other import symbolic_limit as slimit
            sage: maxima(slimit(1/x, x, +oo))                                           # needs sage.symbolic
            0
        """

symbolic_limit: Function_limit

class Function_cases(GinacFunction):
    """
    Formal function holding ``(condition, expression)`` pairs.

    Numbers are considered conditions with zero being ``False``.
    A true condition marks a default value. The function is not
    evaluated as long as it contains a relation that cannot be
    decided by Pynac.

    EXAMPLES::

        sage: # needs sage.symbolic
        sage: ex = cases([(x==0, pi), (True, 0)]); ex
        cases(((x == 0, pi), (1, 0)))
        sage: ex.subs(x==0)
        pi
        sage: ex.subs(x==2)
        0
        sage: ex + 1
        cases(((x == 0, pi), (1, 0))) + 1
        sage: _.subs(x==0)
        pi + 1

    The first encountered default is used, as well as the first relation
    that can be trivially decided::

        sage: cases(((True, pi), (True, 0)))                                            # needs sage.symbolic
        pi

        sage: # needs sage.symbolic
        sage: _ = var('y')
        sage: ex = cases(((x==0, pi), (y==1, 0))); ex
        cases(((x == 0, pi), (y == 1, 0)))
        sage: ex.subs(x==0)
        pi
        sage: ex.subs(x==0, y==1)
        pi
    """
    def __init__(self) -> None:
        """
        EXAMPLES::

            sage: loads(dumps(cases))
            cases
        """
    def __call__(self, l, **kwargs):
        """
        EXAMPLES::

            sage: ex = cases([(x==0, pi), (True, 0)]); ex                               # needs sage.symbolic
            cases(((x == 0, pi), (1, 0)))

        TESTS::

            sage: cases()
            Traceback (most recent call last):
            ...
            TypeError: ...__call__() missing 1 required positional argument: 'l'

            sage: cases(x)                                                              # needs sage.symbolic
            Traceback (most recent call last):
            ...
            RuntimeError: cases argument not a sequence
        """

cases: Function_cases

class Function_crootof(BuiltinFunction):
    """
    Formal function holding ``(polynomial, index)`` pairs.

    The expression evaluates to a floating point value that is an
    approximation to a specific complex root of the polynomial. The
    ordering is fixed so you always get the same root.

    The functionality is imported from SymPy, see
    http://docs.sympy.org/latest/_modules/sympy/polys/rootoftools.html

    EXAMPLES::

        sage: # needs sage.symbolic
        sage: c = complex_root_of(x^6 + x + 1, 1); c
        complex_root_of(x^6 + x + 1, 1)
        sage: c.n()
        -0.790667188814418 + 0.300506920309552*I
        sage: c.n(100)
        -0.79066718881441764449859281847 + 0.30050692030955162512001002521*I
        sage: (c^6 + c + 1).n(100) < 1e-25
        True
    """
    def __init__(self) -> None:
        """
        EXAMPLES::

            sage: loads(dumps(complex_root_of))
            complex_root_of
        """

complex_root_of: Function_crootof

class Function_elementof(BuiltinFunction):
    """
    Formal set membership function that is only accessible internally.

    This function is called to express a set membership statement,
    usually as part of a solution set returned by :func:`solve`.
    See :class:`sage.sets.set.Set` and :class:`sage.sets.real_set.RealSet`
    for possible set arguments.

    EXAMPLES::

        sage: # needs sage.symbolic
        sage: from sage.functions.other import element_of
        sage: element_of(x, SR(ZZ))
        element_of(x, Integer Ring)
        sage: element_of(sin(x), SR(QQ))
        element_of(sin(x), Rational Field)
        sage: element_of(x, SR(RealSet.open_closed(0,1)))
        element_of(x, (0, 1])
        sage: element_of(x, SR(Set([4,6,8])))
        element_of(x, {8, 4, 6})
    """
    def __init__(self) -> None:
        """
        EXAMPLES::

            sage: from sage.functions.other import element_of
            sage: loads(dumps(element_of))
            element_of
        """

element_of: Function_elementof
