"""
Logarithmic functions

AUTHORS:

- Yoora Yi Tenen (2012-11-16): Add documentation for :meth:`log()` (:issue:`12113`)

- Tomas Kalvoda (2015-04-01): Add :meth:`exp_polar()` (:issue:`18085`)
"""

from typing import Any, Literal, overload
from typings_sagemath import (
    RealInexactSage, ComplexInexactSage, CoercibleToExpression)
from sage.symbolic.function import GinacFunction as GinacFunction
from sage.symbolic.expression import Expression as Expression_
from sage.symbolic.ring import SymbolicRing
from sage.rings.real_mpfr import RealNumber
from sage.rings.complex_mpfr import ComplexNumber
from sage.rings.complex_double import ComplexDoubleElement
from sage.rings.real_double import RealDoubleElement
from sage.rings.real_arb import RealBall
from sage.rings.real_mpfi import RealIntervalFieldElement
from sage.rings.complex_interval import ComplexIntervalFieldElement
from sage.rings.polynomial.commutative_polynomial import CommutativePolynomial
from sage.rings.number_field.number_field_element_quadratic import OrderElement_quadratic
from sage.rings.integer import Integer
from sage.rings.rational import Rational
from numpy import (
    int8 as NumPyInt8,
    int16 as NumPyInt16,
    int32 as NumPyInt32,
    int64 as NumPyInt64,
    uint8 as NumPyUInt8,
    uint16 as NumPyUInt16,
    uint32 as NumPyUInt32,
    uint64 as NumPyUInt64,
    float16 as NumPyFloat16,
    float32 as NumPyFloat32,
    float64 as NumPyFloat64,
    float128 as NumPyFloat128,
    complex64 as NumPyComplex64,
    complex128 as NumPyComplex128,
    complex256 as NumPyComplex256,
    ndarray as NumPyNDArray,
    dtype as NumPyDtype,
)
from mpmath import (
    mpf as MpmathF,
    mpc as MpmathC
)
from gmpy2 import mpfr, mpc

from sage.rings.finite_rings.integer_mod import IntegerMod_int

type _np_byte = NumPyInt8 | NumPyUInt8
type _np_short = NumPyInt16 | NumPyUInt16
type _np_int = NumPyInt32 | NumPyUInt32
type _np_long = NumPyInt64 | NumPyUInt64
type _np_long_int = _np_int | _np_long
type _np_float = NumPyFloat16 | NumPyFloat32 | NumPyFloat64 | NumPyFloat128
type _np_complex = NumPyComplex64 | NumPyComplex128 | NumPyComplex256

from sage.misc.functional import log as log
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.rings.integer import Integer as Integer
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.rational_field import QQ as QQ
from sage.rings.real_double import RDF as RDF
from sage.structure.element import Expression as Expression
from sage.symbolic.function import BuiltinFunction as BuiltinFunction, GinacFunction as GinacFunction
from sage.symbolic.symbols import register_symbol as register_symbol

class Function_exp(GinacFunction):
    """
    The exponential function, `\\exp(x) = e^x`.

    EXAMPLES::

        sage: # needs sage.symbolic
        sage: exp(-1)
        e^(-1)
        sage: exp(2)
        e^2
        sage: exp(2).n(100)
        7.3890560989306502272304274606
        sage: exp(x^2 + log(x))
        e^(x^2 + log(x))
        sage: exp(x^2 + log(x)).simplify()
        x*e^(x^2)
        sage: exp(2.5)
        12.1824939607035
        sage: exp(I*pi/12)
        (1/4*I + 1/4)*sqrt(6) - (1/4*I - 1/4)*sqrt(2)

        sage: exp(float(2.5))
        12.182493960703473
        sage: exp(RDF('2.5'))                                                           # needs sage.symbolic
        12.182493960703473

    To prevent automatic evaluation, use the ``hold`` parameter::

        sage: exp(I*pi, hold=True)                                                      # needs sage.symbolic
        e^(I*pi)
        sage: exp(0, hold=True)                                                         # needs sage.symbolic
        e^0

    To then evaluate again, we currently must use Maxima via
    :meth:`sage.symbolic.expression.Expression.simplify`::

        sage: exp(0, hold=True).simplify()                                              # needs sage.symbolic
        1

    ::

        sage: # needs sage.symbolic
        sage: exp(pi*I/2)
        I
        sage: exp(pi*I)
        -1
        sage: exp(8*pi*I)
        1
        sage: exp(7*pi*I/2)
        -I

    For the sake of simplification, the argument is reduced modulo the
    period of the complex exponential function, `2\\pi i`::

        sage: k = var('k', domain='integer')                                            # needs sage.symbolic
        sage: exp(2*k*pi*I)                                                             # needs sage.symbolic
        1
        sage: exp(log(2) + 2*k*pi*I)                                                    # needs sage.symbolic
        2

    The precision for the result is deduced from the precision of
    the input. Convert the input to a higher precision explicitly
    if a result with higher precision is desired::

        sage: t = exp(RealField(100)(2)); t                                             # needs sage.rings.real_mpfr
        7.3890560989306502272304274606
        sage: t.prec()                                                                  # needs sage.rings.real_mpfr
        100
        sage: exp(2).n(100)                                                             # needs sage.symbolic
        7.3890560989306502272304274606

    TESTS::

        sage: # needs sage.symbolic
        sage: latex(exp(x))
        e^{x}
        sage: latex(exp(sqrt(x)))
        e^{\\sqrt{x}}
        sage: latex(exp)
        \\exp
        sage: latex(exp(sqrt(x))^x)
        \\left(e^{\\sqrt{x}}\\right)^{x}
        sage: latex(exp(sqrt(x)^x))
        e^{\\left(\\sqrt{x}^{x}\\right)}
        sage: exp(x)._sympy_()                                                          # needs sympy
        exp(x)

    Test conjugates::

        sage: conjugate(exp(x))                                                         # needs sage.symbolic
        e^conjugate(x)

    Test simplifications when taking powers of exp (:issue:`7264`)::

        sage: # needs sage.symbolic
        sage: var('a,b,c,II')
        (a, b, c, II)
        sage: model_exp = exp(II)**a*(b)
        sage: sol1_l = {b: 5.0, a: 1.1}
        sage: model_exp.subs(sol1_l)
        5.00000000000000*e^(1.10000000000000*II)

    ::

        sage: # needs sage.symbolic
        sage: exp(3)^II*exp(x)
        e^(3*II + x)
        sage: exp(x)*exp(x)
        e^(2*x)
        sage: exp(x)*exp(a)
        e^(a + x)
        sage: exp(x)*exp(a)^2
        e^(2*a + x)

    Another instance of the same problem (:issue:`7394`)::

        sage: 2*sqrt(e)                                                                 # needs sage.symbolic
        2*e^(1/2)

    Check that :issue:`19918` is fixed::

        sage: exp(-x^2).subs(x=oo)                                                      # needs sage.symbolic
        0
        sage: exp(-x).subs(x=-oo)                                                       # needs sage.symbolic
        +Infinity
    """
    def __init__(self) -> None:
        """
        TESTS::

            sage: loads(dumps(exp))
            exp
            sage: maxima(exp(x))._sage_()                                               # needs sage.symbolic
            e^x
        """
    @overload
    def __call__( # pyright: ignore[reportOverlappingOverload]
        self,
        arg: _np_byte,
        /,
    ) -> NumPyFloat16: ...
    @overload
    def __call__(
        self,
        arg: _np_short,
        /
    ) -> NumPyFloat32: ...
    @overload
    def __call__(
        self,
        arg: _np_long_int,
        /
    ) -> NumPyFloat64: ...
    @overload
    def __call__(
        self, 
        arg: Expression_ | int | Integer | Rational 
            | OrderElement_quadratic | CommutativePolynomial
    ) -> Expression_[SymbolicRing]: ...
    @overload
    def __call__[
        F: _np_float | _np_complex | MpmathF | MpmathC | float | complex
            | RealInexactSage | ComplexInexactSage
            | NumPyNDArray[Any, NumPyDtype[_np_float | _np_complex]]
    ](self, arg: F, /) -> F: ...
    @overload
    def __call__(self, arg: mpfr, /) -> float: ...
    @overload
    def __call__(self, arg: mpc, /) -> complex: ...
    @overload
    def __call__( # pyright: ignore[reportIncompatibleMethodOverride]
        self, 
        arg: CoercibleToExpression, 
        /, 
        *, 
        hold: Literal[True] = ...
    ) -> Expression_[SymbolicRing]: ...

exp: Function_exp

class Function_log1(GinacFunction):
    """
    The natural logarithm of ``x``.

    See :meth:`log()` for extensive documentation.

    EXAMPLES::

        sage: ln(e^2)                                                                   # needs sage.symbolic
        2
        sage: ln(2)                                                                     # needs sage.symbolic
        log(2)
        sage: ln(10)                                                                    # needs sage.symbolic
        log(10)

    TESTS::

        sage: # needs sage.symbolic
        sage: latex(x.log())
        \\log\\left(x\\right)
        sage: latex(log(1/4))
        \\log\\left(\\frac{1}{4}\\right)
        sage: log(x)._sympy_()                                                          # needs sympy
        log(x)
        sage: loads(dumps(ln(x)+1))
        log(x) + 1

    ``conjugate(log(x))==log(conjugate(x))`` unless on the branch cut which
    runs along the negative real axis.::

        sage: # needs sage.symbolic
        sage: conjugate(log(x))
        conjugate(log(x))
        sage: var('y', domain='positive')
        y
        sage: conjugate(log(y))
        log(y)
        sage: conjugate(log(y + I))
        conjugate(log(y + I))
        sage: conjugate(log(-1))
        -I*pi
        sage: log(conjugate(-1))
        I*pi

    Check if float arguments are handled properly.::

        sage: from sage.functions.log import function_log as log
        sage: log(float(5))
        1.6094379124341003
        sage: log(float(0))                                                             # needs sage.symbolic
        -inf
        sage: log(float(-1))                                                            # needs sage.symbolic
        3.141592653589793j
        sage: log(x).subs(x=float(-1))                                                  # needs sage.symbolic
        3.141592653589793j

    :issue:`22142`::

        sage: log(QQbar(sqrt(2)))                                                       # needs sage.rings.number_field sage.symbolic
        log(1.414213562373095?)
        sage: log(QQbar(sqrt(2))*1.)                                                    # needs sage.rings.number_field sage.symbolic
        0.346573590279973
        sage: polylog(QQbar(sqrt(2)),3)                                                 # needs sage.rings.number_field sage.symbolic
        polylog(1.414213562373095?, 3)
    """
    
    def __init__(self) -> None:
        """
        TESTS::

            sage: loads(dumps(ln))
            log
            sage: maxima(ln(x))._sage_()                                                # needs sage.symbolic
            log(x)
        """
    @overload
    def __call__(self, arg: IntegerMod_int, /) -> Integer: ...
    @overload
    def __call__(
        self, 
        arg: Expression_ | int | Integer | Rational 
            | OrderElement_quadratic | CommutativePolynomial
    ) -> Expression_[SymbolicRing]: ...
    @overload
    def __call__( # pyright: ignore[reportOverlappingOverload]
        self,
        arg: _np_byte,
        /,
    ) -> NumPyFloat16: ...
    @overload
    def __call__(
        self,
        arg: _np_short,
        /
    ) -> NumPyFloat32: ...
    @overload
    def __call__(
        self,
        arg: _np_long_int,
        /
    ) -> NumPyFloat64: ...
    @overload
    def __call__[
        F: _np_float | RealBall | _np_complex | complex | ComplexInexactSage
            | NumPyNDArray[Any, NumPyDtype[_np_float | _np_complex]]
    ](self, arg: F, /) -> F: ...
    @overload
    def __call__(self, arg: RealNumber, /) -> RealNumber | ComplexNumber: ...
    @overload
    def __call__(self, arg: RealDoubleElement, /) -> RealDoubleElement | ComplexDoubleElement: ...
    @overload
    def __call__(self, arg: RealIntervalFieldElement, /) -> RealIntervalFieldElement | ComplexIntervalFieldElement: ...
    @overload
    def __call__(self, arg: MpmathF, /) -> MpmathF | MpmathC: ...
    @overload
    def __call__(self, arg: MpmathC, /) -> MpmathC: ...
    @overload
    def __call__(self, arg: mpfr, /) -> float: ...
    @overload
    def __call__(self, arg: mpc | float, /) -> complex: ...
    @overload
    def __call__( # pyright: ignore[reportIncompatibleMethodOverride]
        self, 
        arg: CoercibleToExpression, 
        /, 
        *, 
        hold: Literal[True] = ...
    ) -> Expression_[SymbolicRing]: ...
ln: Function_log1

function_log: Function_log1

class Function_log2(GinacFunction):
    """
    Return the logarithm of x to the given base.

    See :meth:`log() <sage.functions.log.log>` for extensive documentation.

    EXAMPLES::

        sage: from sage.functions.log import logb
        sage: logb(1000, 10)                                                            # needs sage.symbolic
        3

    TESTS::

        sage: logb(7, 2)                                                                # needs sage.symbolic
        log(7)/log(2)
        sage: logb(int(7), 2)                                                           # needs sage.symbolic
        log(7)/log(2)
    """
    def __init__(self) -> None:
        """
        TESTS::

            sage: from sage.functions.log import logb
            sage: loads(dumps(logb))
            log
        """

logb: Function_log2

class Function_polylog(GinacFunction):
    def __init__(self) -> None:
        """
        The polylog function
        `\\text{Li}_s(z) = \\sum_{k=1}^{\\infty} z^k / k^s`.

        The first argument is `s` (usually an integer called the weight)
        and the second argument is `z`: ``polylog(s, z)``.

        This definition is valid for arbitrary complex numbers `s` and `z`
        with `|z| < 1`. It can be extended to `|z| \\ge 1` by the process of
        analytic continuation, with a branch cut along the positive real axis
        from `1` to `+\\infty`. A ``NaN`` value may be returned for floating
        point arguments that are on the branch cut.

        EXAMPLES::

            sage: # needs sage.symbolic
            sage: polylog(2.7, 0)
            0.000000000000000
            sage: polylog(2, 1)
            1/6*pi^2
            sage: polylog(2, -1)
            -1/12*pi^2
            sage: polylog(3, -1)
            -3/4*zeta(3)
            sage: polylog(2, I)
            I*catalan - 1/48*pi^2
            sage: polylog(4, 1/2)
            polylog(4, 1/2)
            sage: polylog(4, 0.5)
            0.517479061673899

            sage: # needs sage.symbolic
            sage: polylog(1, x)
            -log(-x + 1)
            sage: polylog(2, x^2 + 1)
            dilog(x^2 + 1)
            sage: f = polylog(4, 1); f
            1/90*pi^4
            sage: f.n()
            1.08232323371114
            sage: polylog(4, 2).n()
            2.42786280675470 - 0.174371300025453*I
            sage: complex(polylog(4, 2))
            (2.4278628067547032-0.17437130002545306j)
            sage: float(polylog(4, 0.5))
            0.5174790616738993
            sage: z = var('z')
            sage: polylog(2, z).series(z==0, 5)
            1*z + 1/4*z^2 + 1/9*z^3 + 1/16*z^4 + Order(z^5)

            sage: loads(dumps(polylog))
            polylog

            sage: latex(polylog(5, x))                                                  # needs sage.symbolic
            {\\rm Li}_{5}(x)
            sage: polylog(x, x)._sympy_()                                               # needs sympy sage.symbolic
            polylog(x, x)

        TESTS:

        Check if :issue:`8459` is fixed::

            sage: t = maxima(polylog(5,x)).sage(); t                                    # needs sage.symbolic
            polylog(5, x)
            sage: t.operator() == polylog                                               # needs sage.symbolic
            True
            sage: t.subs(x=.5).n()                                                      # needs sage.symbolic
            0.50840057924226...

        Check if :issue:`18386` is fixed::

            sage: polylog(2.0, 1)                                                       # needs sage.symbolic
            1.64493406684823
            sage: polylog(2, 1.0)                                                       # needs sage.symbolic
            1.64493406684823
            sage: polylog(2.0, 1.0)                                                     # needs sage.symbolic
            1.64493406684823

            sage: # needs sage.libs.flint
            sage: polylog(2, RealBallField(100)(1/3))
            [0.36621322997706348761674629766... +/- ...]
            sage: polylog(2, ComplexBallField(100)(4/3))
            [2.27001825336107090380391448586 +/- ...] + [-0.90377988538400159956755721265 +/- ...]*I
            sage: polylog(2, CBF(1/3))
            [0.366213229977063 +/- ...]
            sage: parent(_)
            Complex ball field with 53 bits of precision
            sage: polylog(2, CBF(1))
            [1.644934066848226 +/- ...]
            sage: parent(_)
            Complex ball field with 53 bits of precision

            sage: polylog(1, -1)                # known bug                             # needs sage.symbolic
            -log(2)

        Check for :issue:`21907`::

            sage: bool(x*polylog(x,x)==0)                                               # needs sage.symbolic
            False
        """

polylog: Function_polylog

class Function_dilog(GinacFunction):
    def __init__(self) -> None:
        """
        The dilogarithm function
        `\\text{Li}_2(z) = \\sum_{k=1}^{\\infty} z^k / k^2`.

        This is simply an alias for ``polylog(2, z)``.

        EXAMPLES::

            sage: # needs sage.symbolic
            sage: dilog(1)
            1/6*pi^2
            sage: dilog(1/2)
            1/12*pi^2 - 1/2*log(2)^2
            sage: dilog(x^2+1)
            dilog(x^2 + 1)
            sage: dilog(-1)
            -1/12*pi^2
            sage: dilog(-1.0)
            -0.822467033424113
            sage: dilog(-1.1)
            -0.890838090262283
            sage: dilog(1/2)
            1/12*pi^2 - 1/2*log(2)^2
            sage: dilog(.5)
            0.582240526465012
            sage: dilog(1/2).n()
            0.582240526465012
            sage: var('z')
            z
            sage: dilog(z).diff(z, 2)
            log(-z + 1)/z^2 - 1/((z - 1)*z)
            sage: dilog(z).series(z==1/2, 3)
            (1/12*pi^2 - 1/2*log(2)^2) + (-2*log(1/2))*(z - 1/2)
             + (2*log(1/2) + 2)*(z - 1/2)^2 + Order(1/8*(2*z - 1)^3)

            sage: latex(dilog(z))                                                       # needs sage.symbolic
            {\\rm Li}_2\\left(z\\right)

        Dilog has a branch point at `1`. Sage's floating point libraries
        may handle this differently from the symbolic package::

            sage: # needs sage.symbolic
            sage: dilog(1)
            1/6*pi^2
            sage: dilog(1.)
            1.64493406684823
            sage: dilog(1).n()
            1.64493406684823
            sage: float(dilog(1))
            1.6449340668482262

        TESTS:

        ``conjugate(dilog(x))==dilog(conjugate(x))`` unless on the branch cuts
        which run along the positive real axis beginning at 1.::

            sage: # needs sage.symbolic
            sage: conjugate(dilog(x))
            conjugate(dilog(x))
            sage: var('y', domain='positive')
            y
            sage: conjugate(dilog(y))
            conjugate(dilog(y))
            sage: conjugate(dilog(1/19))
            dilog(1/19)
            sage: conjugate(dilog(1/2*I))
            dilog(-1/2*I)
            sage: dilog(conjugate(1/2*I))
            dilog(-1/2*I)
            sage: conjugate(dilog(2))
            conjugate(dilog(2))

        Check that return type matches argument type where possible
        (:issue:`18386`)::

            sage: dilog(0.5)                                                            # needs sage.symbolic
            0.582240526465012
            sage: dilog(-1.0)                                                           # needs sage.symbolic
            -0.822467033424113

            sage: # needs sage.rings.real_mpfr sage.symbolic
            sage: y = dilog(RealField(13)(0.5))
            sage: parent(y)
            Real Field with 13 bits of precision
            sage: dilog(RealField(13)(1.1))
            1.96 - 0.300*I
            sage: parent(_)
            Complex Field with 13 bits of precision
        """

dilog: Function_dilog

class Function_lambert_w(BuiltinFunction):
    """
    The integral branches of the Lambert W function `W_n(z)`.

    This function satisfies the equation

    .. MATH::

        z = W_n(z) e^{W_n(z)}

    INPUT:

    - ``n`` -- integer; `n=0` corresponds to the principal branch

    - ``z`` -- a complex number

    If called with a single argument, that argument is ``z`` and the branch ``n`` is
    assumed to be 0 (the principal branch).

    ALGORITHM:

    Numerical evaluation is handled using the mpmath and SciPy libraries.

    REFERENCES:

    - :wikipedia:`Lambert_W_function`

    EXAMPLES:

    Evaluation of the principal branch::

        sage: lambert_w(1.0)                                                            # needs scipy
        0.567143290409784
        sage: lambert_w(-1).n()                                                         # needs mpmath
        -0.318131505204764 + 1.33723570143069*I
        sage: lambert_w(-1.5 + 5*I)                                                     # needs mpmath sage.symbolic
        1.17418016254171 + 1.10651494102011*I

    Evaluation of other branches::

        sage: lambert_w(2, 1.0)                                                         # needs scipy
        -2.40158510486800 + 10.7762995161151*I

    Solutions to certain exponential equations are returned in terms of lambert_w::

        sage: S = solve(e^(5*x)+x==0, x, to_poly_solve=True)                            # needs sage.symbolic
        sage: z = S[0].rhs(); z                                                         # needs sage.symbolic
        -1/5*lambert_w(5)
        sage: N(z)                                                                      # needs sage.symbolic
        -0.265344933048440

    Check the defining equation numerically at `z=5`::

        sage: N(lambert_w(5)*exp(lambert_w(5)) - 5)                                     # needs mpmath
        0.000000000000000

    There are several special values of the principal branch which
    are automatically simplified::

        sage: lambert_w(0)                                                              # needs mpmath
        0
        sage: lambert_w(e)                                                              # needs sage.symbolic
        1
        sage: lambert_w(-1/e)                                                           # needs sage.symbolic
        -1

    Integration (of the principal branch) is evaluated using Maxima::

        sage: integrate(lambert_w(x), x)                                                # needs sage.symbolic
        (lambert_w(x)^2 - lambert_w(x) + 1)*x/lambert_w(x)
        sage: integrate(lambert_w(x), x, 0, 1)                                          # needs sage.symbolic
        (lambert_w(1)^2 - lambert_w(1) + 1)/lambert_w(1) - 1
        sage: integrate(lambert_w(x), x, 0, 1.0)                                        # needs sage.symbolic
        0.3303661247616807

    Warning: The integral of a non-principal branch is not implemented,
    neither is numerical integration using GSL. The :meth:`numerical_integral`
    function does work if you pass a lambda function::

        sage: numerical_integral(lambda x: lambert_w(x), 0, 1)                          # needs sage.modules
        (0.33036612476168054, 3.667800782666048e-15)
    """
    def __init__(self) -> None:
        '''
        See the docstring for :meth:`Function_lambert_w`.

        EXAMPLES::

            sage: lambert_w(0, 1.0)                                                     # needs scipy
            0.567143290409784
            sage: lambert_w(x, x)._sympy_()                                             # needs sympy sage.symbolic
            LambertW(x, x)

        TESTS:

        Check that :issue:`25987` is fixed::

            sage: lambert_w(x)._fricas_()                                       # optional - fricas, needs sage.symbolic
            lambertW(x)

            sage: fricas(lambert_w(x)).eval(x=-1/e)                             # optional - fricas, needs sage.symbolic
            - 1

        The two-argument form of Lambert\'s function is not supported
        by FriCAS, so we return a generic operator::

            sage: var("n")                                                              # needs sage.symbolic
            n
            sage: lambert_w(n, x)._fricas_()                                    # optional - fricas, needs sage.symbolic
            generalizedLambertW(n,x)
        '''
    def __call__(self, *args, **kwds):
        """
        Custom call method allows the user to pass one argument or two. If
        one argument is passed, we assume it is ``z`` and that ``n=0``.

        EXAMPLES::

            sage: lambert_w(1)                                                          # needs sage.symbolic
            lambert_w(1)
            sage: lambert_w(1, 2)                                                       # needs sage.symbolic
            lambert_w(1, 2)
        """

lambert_w: Function_lambert_w

class Function_exp_polar(BuiltinFunction):
    def __init__(self) -> None:
        """
        Representation of a complex number in a polar form.

        INPUT:

        - ``z`` -- a complex number `z = a + ib`

        OUTPUT:

        A complex number with modulus `\\exp(a)` and argument `b`.

        If `-\\pi < b \\leq \\pi` then `\\operatorname{exp\\_polar}(z)=\\exp(z)`.
        For other values of `b` the function is left unevaluated.

        EXAMPLES:

        The following expressions are evaluated using the exponential
        function::

            sage: exp_polar(pi*I/2)                                                     # needs sage.symbolic
            I
            sage: x = var('x', domain='real')                                           # needs sage.symbolic
            sage: exp_polar(-1/2*I*pi + x)                                              # needs sage.symbolic
            e^(-1/2*I*pi + x)

        The function is left unevaluated when the imaginary part of the
        input `z` does not satisfy `-\\pi < \\Im(z) \\leq \\pi`::

            sage: exp_polar(2*pi*I)                                                     # needs sage.symbolic
            exp_polar(2*I*pi)
            sage: exp_polar(-4*pi*I)                                                    # needs sage.symbolic
            exp_polar(-4*I*pi)

        This fixes :issue:`18085`::

            sage: integrate(1/sqrt(1+x^3), x, algorithm='sympy')                        # needs sage.symbolic
            1/3*x*gamma(1/3)*hypergeometric((1/3, 1/2), (4/3,), -x^3)/gamma(4/3)


        .. SEEALSO::

            `Examples in Sympy documentation <http://docs.sympy.org/latest/modules/functions/special.html?highlight=exp_polar>`_,
            `Sympy source code of exp_polar <http://docs.sympy.org/0.7.4/_modules/sympy/functions/elementary/exponential.html>`_

        REFERENCES:

            :wikipedia:`Complex_number#Polar_form`
        """

exp_polar: Function_exp_polar

class Function_harmonic_number_generalized(BuiltinFunction):
    """
    Harmonic and generalized harmonic number functions,
    defined by:

    .. MATH::

        H_{n}=H_{n,1}=\\sum_{k=1}^n\\frac{1}{k}

        H_{n,m}=\\sum_{k=1}^n\\frac{1}{k^m}

    They are also well-defined for complex argument, through:

    .. MATH::

        H_{s}=\\int_0^1\\frac{1-x^s}{1-x}

        H_{s,m}=\\zeta(m)-\\zeta(m,s-1)

    If called with a single argument, that argument is ``s`` and ``m`` is
    assumed to be 1 (the normal harmonic numbers `H_s`).

    ALGORITHM:

    Numerical evaluation is handled using the mpmath and FLINT libraries.

    REFERENCES:

    - :wikipedia:`Harmonic_number`

    EXAMPLES:

    Evaluation of integer, rational, or complex argument::

        sage: harmonic_number(5)                                                        # needs mpmath
        137/60

        sage: # needs sage.symbolic
        sage: harmonic_number(3, 3)
        251/216
        sage: harmonic_number(5/2)
        -2*log(2) + 46/15
        sage: harmonic_number(3., 3)
        zeta(3) - 0.0400198661225573
        sage: harmonic_number(3., 3.)
        1.16203703703704
        sage: harmonic_number(3, 3).n(200)
        1.16203703703703703703703...
        sage: harmonic_number(1 + I, 5)
        harmonic_number(I + 1, 5)
        sage: harmonic_number(5, 1. + I)
        1.57436810798989 - 1.06194728851357*I

    Solutions to certain sums are returned in terms of harmonic numbers::

        sage: k = var('k')                                                              # needs sage.symbolic
        sage: sum(1/k^7,k,1,x)                                                          # needs sage.symbolic
        harmonic_number(x, 7)

    Check the defining integral at a random integer::

        sage: n = randint(10,100)
        sage: bool(SR(integrate((1-x^n)/(1-x),x,0,1)) == harmonic_number(n))            # needs sage.symbolic
        True

    There are several special values which are automatically simplified::

        sage: harmonic_number(0)                                                        # needs mpmath
        0
        sage: harmonic_number(1)                                                        # needs mpmath
        1
        sage: harmonic_number(x, 1)                                                     # needs sage.symbolic
        harmonic_number(x)
    """
    def __init__(self) -> None:
        """
        EXAMPLES::

            sage: loads(dumps(harmonic_number(x, 5)))                                   # needs sage.symbolic
            harmonic_number(x, 5)
            sage: harmonic_number(x, x)._sympy_()                                       # needs sympy sage.symbolic
            harmonic(x, x)
        """
    def __call__(self, z, m: int = 1, **kwds):
        """
        Custom call method allows the user to pass one argument or two. If
        one argument is passed, we assume it is ``z`` and that `m=1`.

        EXAMPLES::

            sage: harmonic_number(x)                                                    # needs sage.symbolic
            harmonic_number(x)
            sage: harmonic_number(x, 1)                                                 # needs sage.symbolic
            harmonic_number(x)
            sage: harmonic_number(x, 2)                                                 # needs sage.symbolic
            harmonic_number(x, 2)
        """

harmonic_number: Function_harmonic_number_generalized

class _Function_swap_harmonic(BuiltinFunction):
    """
    Harmonic number function with swapped arguments. For internal use only.

    EXAMPLES::

        sage: # needs sage.symbolic
        sage: maxima(harmonic_number(x, 2))  # maxima expect interface
        gen_harmonic_number(2,_SAGE_VAR_x)
        sage: from sage.calculus.calculus import symbolic_expression_from_maxima_string as sefms
        sage: sefms('gen_harmonic_number(3,x)')
        harmonic_number(x, 3)
        sage: from sage.interfaces.maxima_lib import maxima_lib, max_to_sr
        sage: c = maxima_lib(harmonic_number(x,2)); c
        gen_harmonic_number(2,_SAGE_VAR_x)
        sage: max_to_sr(c.ecl())
        harmonic_number(x, 2)
    """
    def __init__(self) -> None: ...

class Function_harmonic_number(BuiltinFunction):
    """
    Harmonic number function, defined by:

    .. MATH::

        H_{n}=H_{n,1}=\\sum_{k=1}^n\\frac1k

        H_{s}=\\int_0^1\\frac{1-x^s}{1-x}

    See the docstring for :meth:`Function_harmonic_number_generalized`.

    This class exists as callback for ``harmonic_number`` returned by Maxima.
    """
    def __init__(self) -> None:
        """
        EXAMPLES::

            sage: k = var('k')                                                          # needs sage.symbolic
            sage: loads(dumps(sum(1/k, k, 1, x)))                                       # needs sage.symbolic
            harmonic_number(x)
            sage: harmonic_number(x)._sympy_()                                          # needs sympy sage.symbolic
            harmonic(x)
        """

harmonic_m1: Function_harmonic_number
