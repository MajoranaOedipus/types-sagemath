r"""
Airy functions

This module implements Airy functions and their generalized derivatives. It
supports symbolic functionality through Maxima and numeric evaluation through
mpmath and scipy.

Airy functions are solutions to the differential equation
`f''(x) - x f(x) = 0`.

Four global function symbols are immediately available, please see

- :func:`airy_ai`: for the Airy Ai function

- :func:`airy_ai_prime()<FunctionAiryAiPrime>`: for the first differential
  of the Airy Ai function

- :func:`airy_bi`: for the Airy Bi function

- :func:`airy_bi_prime()<FunctionAiryBiPrime>`: for the first differential
   of the Airy Bi function

AUTHORS:

- Oscar Gerardo Lazo Arjona (2010): initial version

- Douglas McNeil (2012): rewrite

EXAMPLES:

Verify that the Airy functions are solutions to the differential equation::

    sage: diff(airy_ai(x), x, 2) - x * airy_ai(x)                                       # needs sage.symbolic
    0
    sage: diff(airy_bi(x), x, 2) - x * airy_bi(x)                                       # needs sage.symbolic
    0
"""

from typing import Literal, overload
from typings_sagemath import FloatingSage, ComplexInexactSage
from sage.symbolic.ring import SymbolicRing
from sage.rings.abc import SymbolicRing as SymbolicRingABC
from sage.rings.polynomial.commutative_polynomial import CommutativePolynomial
from sage.rings.infinity import FiniteNumber, MinusInfinity, PlusInfinity, UnsignedInfinity
from sage.rings.real_mpfr import RealNumber
from sage.rings.real_double import RealDoubleElement
from sage.rings.real_arb import RealBall
from sage.rings.real_mpfi import RealIntervalFieldElement
from sage.rings.complex_mpfr import ComplexNumber
from sage.rings.complex_double import ComplexDoubleElement
from sage.rings.complex_arb import ComplexBall
from sage.rings.complex_interval import ComplexIntervalFieldElement
from sage.rings.integer import Integer
from sage.rings.rational import Rational

type _py_number = int | float | complex
type _MpfrSage = RealNumber | ComplexNumber
type _DoubleSage = RealDoubleElement | ComplexDoubleElement
type _RealMpfrDoubleSage = RealNumber | RealDoubleElement
type _ComplexMpfrDoubleSage = ComplexNumber | ComplexDoubleElement
type _MpfrDoubleSage = _RealMpfrDoubleSage | _ComplexMpfrDoubleSage
type _BallMpfiSage = RealBall | RealIntervalFieldElement | ComplexBall | ComplexIntervalFieldElement
type _inf = PlusInfinity | MinusInfinity | UnsignedInfinity
type _inf_signed = PlusInfinity | MinusInfinity

from sage.calculus.functional import derivative as derivative
from sage.rings.integer_ring import ZZ as ZZ
from sage.structure.element import Expression as Expression
from sage.symbolic.function import BuiltinFunction as BuiltinFunction
from sage.symbolic.ring import SR as SR

class FunctionAiryAiGeneral(BuiltinFunction):
    def __init__(self) -> None:
        """
        The generalized derivative of the Airy Ai function.

        INPUT:

        - ``alpha`` -- return the `\\alpha`-th order fractional derivative with
          respect to `z`.
          For `\\alpha = n = 1,2,3,\\ldots` this gives the derivative
          `\\operatorname{Ai}^{(n)}(z)`, and for `\\alpha = -n = -1,-2,-3,\\ldots`
          this gives the `n`-fold iterated integral.

        .. MATH::

            f_0(z) = \\operatorname{Ai}(z)

            f_n(z) = \\int_0^z f_{n-1}(t) dt

        - ``x`` -- the argument of the function

        EXAMPLES::

            sage: # needs sage.symbolic
            sage: from sage.functions.airy import airy_ai_general
            sage: x, n = var('x n')
            sage: airy_ai_general(-2, x)
            airy_ai(-2, x)
            sage: derivative(airy_ai_general(-2, x), x)
            airy_ai(-1, x)
            sage: airy_ai_general(n, x)
            airy_ai(n, x)
            sage: derivative(airy_ai_general(n, x), x)
            airy_ai(n + 1, x)
        """
    # int
    @overload
    def __call__(
        self, alpha: int, x: int, /, *, hold: bool = False) -> int: ...
    @overload
    def __call__[T: float | complex | _MpfrDoubleSage](
        self, alpha: int | Integer, x: T, /, *, hold: bool = False
    ) -> T: ...
    @overload
    def __call__(
        self, 
        alpha: int | Integer | Rational | CommutativePolynomial, 
        x: Integer | Rational | CommutativePolynomial | ComplexBall, 
        /, *, hold: Literal[True]
    ) -> Expression[SymbolicRing]: ...
    @overload
    def __call__(
        self, alpha: int, x: Integer | Rational, /
    ) -> Expression[SymbolicRing] | Integer: ...
    @overload
    def __call__(
        self, alpha: int, x: CommutativePolynomial, /
    ) -> Expression[SymbolicRing] | Integer | FloatingSage: ...
    @overload
    def __call__(
        self, alpha: int | Integer | Rational | CommutativePolynomial, 
        x: RealBall | RealIntervalFieldElement | ComplexIntervalFieldElement | _inf, 
        /, *, hold: bool = False
    ) -> Expression[SymbolicRing]: ...
    @overload
    def __call__(
        self, alpha: int | Integer | Rational | CommutativePolynomial, 
        x: ComplexBall, /, 
    ) -> Expression[SymbolicRing] | ComplexBall: ...
    # (_, int)
    @overload
    def __call__(
        self, alpha: float, x: int | Integer | Rational, 
        /, *, hold: bool = False
    ) -> Expression[SymbolicRing] | complex | float: ...
    @overload
    def __call__(
        self, alpha: complex, x: int | Integer | Rational, 
        /, *, hold: bool = False
    ) -> Expression[SymbolicRing] | complex: ...
    @overload
    def __call__(
        self, alpha: Integer | Rational, x: int | Integer | Rational, 
        /, *, hold: bool = False
    ) -> Expression[SymbolicRing]: ...
    @overload
    def __call__(
        self, 
        alpha: CommutativePolynomial, 
        x: int | Integer | Rational | CommutativePolynomial, 
        /, *, hold: Literal[True]
    ) -> Expression[SymbolicRing]: ...
    @overload
    def __call__(
        self, alpha: CommutativePolynomial, 
        x: int | Integer | Rational | CommutativePolynomial, /, 
    ) -> Expression[SymbolicRing] | FloatingSage: ...
    @overload
    def __call__(
        self, alpha: RealNumber, x: int | Integer | Rational, /, *, hold: bool = False
    ) -> Expression[SymbolicRing] | _MpfrSage: ...
    @overload
    def __call__(
        self, alpha: RealDoubleElement, x: int | Integer | Rational, /, *, hold: bool = False
    ) -> Expression[SymbolicRing] | _DoubleSage: ...
    @overload
    def __call__[C: _ComplexMpfrDoubleSage](
        self, alpha: C, x: int | Integer | Rational, /, *, hold: bool = False
    ) -> Expression[SymbolicRing] | C: ...
    @overload
    def __call__(
        self, alpha: _BallMpfiSage, x: int | Integer | Rational, /, *, hold: bool = False
    ) -> Expression[SymbolicRing]: ...
    # float
    @overload
    def __call__(
        self, alpha: float | Rational, x: float, /, *, hold: bool = False
    ) -> complex | float: ...
    @overload
    def __call__(
        self, 
        alpha: float | complex | Integer | Rational | _RealMpfrDoubleSage | RealBall | RealIntervalFieldElement, 
        x: complex, 
        /, *, hold: bool = False
    ) -> complex: ...
    @overload
    def __call__(
        self, alpha: float | complex, x: CommutativePolynomial, 
        /, *, hold: bool = False
    ) -> Expression[SymbolicRing] | CommutativePolynomial: ...
    @overload
    def __call__(
        self, alpha: float | Rational, x: RealNumber, 
        /, *, hold: bool = False
    ) -> _MpfrSage: ...
    @overload
    def __call__(
        self, alpha: float | Rational, x: RealDoubleElement, 
        /, *, hold: bool = False
    ) -> _MpfrSage: ...
    @overload
    def __call__[C: _ComplexMpfrDoubleSage](
        self, alpha: float | complex | Rational | _RealMpfrDoubleSage, x: C, 
        /, *, hold: bool = False
    ) -> C: ...
    @overload
    def __call__(
        self, 
        alpha: float | complex | FloatingSage | _inf, 
        x: _BallMpfiSage | UnsignedInfinity, 
        /, *, hold: bool = False
    ) -> Expression[SymbolicRing]: ...
    @overload
    def __call__(
        self, alpha: float, x: PlusInfinity, 
        /, *, hold: bool = False
    ) -> Expression[SymbolicRing] | PlusInfinity: ...
    @overload
    def __call__(
        self, alpha: float, x: MinusInfinity, 
        /, *, hold: bool = False
    ) -> FiniteNumber | MinusInfinity: ...
    # (_, float)
    @overload
    def __call__(
        self, alpha: complex, x: float | _RealMpfrDoubleSage, /, *, hold: bool = False
    ) -> complex: ...
    @overload
    def __call__(
        self, alpha: CommutativePolynomial, x: float | complex, 
        /, *, hold: bool = False
    ) -> Expression[SymbolicRing] | CommutativePolynomial: ...
    @overload
    def __call__(
        self, alpha: RealNumber, x: float, 
        /, *, hold: bool = False
    ) -> _MpfrSage: ...
    @overload
    def __call__(
        self, alpha: RealDoubleElement, x: float, 
        /, *, hold: bool = False
    ) -> _DoubleSage: ...
    @overload
    def __call__[C: _ComplexMpfrDoubleSage](
        self, alpha: C, x: float | complex, 
        /, *, hold: bool = False
    ) -> C: ...
    @overload
    def __call__(
        self, alpha: _BallMpfiSage, x: float | complex, 
        /, *, hold: Literal[True]
    ) -> Expression[SymbolicRing]: ...
    @overload
    def __call__(
        self, alpha: RealBall | RealIntervalFieldElement, x: float, /, 
    ) -> _MpfrSage: ...
    @overload
    def __call__(
        self, alpha: ComplexIntervalFieldElement, x: float | complex, /, 
    ) -> ComplexNumber: ...
    # complex
    @overload
    def __call__(
        self, 
        alpha: complex | _BallMpfiSage | ComplexInexactSage | _inf, 
        x: _inf, /, *, hold: bool = False
    ) -> Expression[SymbolicRing]: ...
    # Integer / Rational
    @overload
    def __call__(
        self, 
        alpha: Integer | Rational, 
        x: CommutativePolynomial, /, *, hold: bool = False
    ) -> Expression[SymbolicRing] | FloatingSage: ...
    # Polynomial
    @overload
    def __call__(
        self, 
        alpha: CommutativePolynomial, 
        x: _MpfrDoubleSage, /, *, hold: bool = False
    ) -> Expression[SymbolicRing] | CommutativePolynomial: ...
    # RR / RDF
    @overload
    def __call__(
        self, 
        alpha: _MpfrDoubleSage, 
        x: CommutativePolynomial, /, *, hold: bool = False
    ) -> Expression[SymbolicRing] | CommutativePolynomial: ...
    @overload
    def __call__(
        self, 
        alpha: RealNumber, 
        x: _RealMpfrDoubleSage, /, *, hold: bool = False
    ) -> _MpfrSage: ...
    @overload
    def __call__(
        self, 
        alpha: RealDoubleElement, 
        x: _RealMpfrDoubleSage, /, *, hold: bool = False
    ) -> _DoubleSage: ...
    @overload
    def __call__(
        self, 
        alpha: _RealMpfrDoubleSage, 
        x: MinusInfinity, /, *, hold: bool = False
    ) -> FiniteNumber: ...
    @overload
    def __call__(
        self, 
        alpha: _RealMpfrDoubleSage, 
        x: PlusInfinity | UnsignedInfinity, /, *, hold: bool = False
    ) -> Expression[SymbolicRing]: ...
    # CC / CDF
    @overload
    def __call__[C: _ComplexMpfrDoubleSage](
        self, alpha: C, x: _MpfrDoubleSage, /, *, hold: bool = False
    ) -> C: ...
    # Balls / IF
    @overload
    def __call__(
        self, 
        alpha: RealBall | RealIntervalFieldElement | ComplexIntervalFieldElement, 
        x: CommutativePolynomial, /, 
    ) -> Expression[SymbolicRing] | FloatingSage: ...
    @overload
    def __call__(
        self, 
        alpha: RealBall | RealIntervalFieldElement | ComplexIntervalFieldElement, 
        x: CommutativePolynomial, /, hold: Literal[True]
    ) -> Expression[SymbolicRing]: ...
    @overload
    def __call__(
        self, 
        alpha: ComplexBall, 
        x: CommutativePolynomial, /, hold: bool = False
    ) -> Expression[SymbolicRing]: ...
    @overload
    def __call__(
        self, 
        alpha: _BallMpfiSage, 
        x: FloatingSage, /, *, hold: Literal[True]
    ) -> ComplexNumber: ...
    @overload
    def __call__(
        self, 
        alpha: RealBall | RealIntervalFieldElement, 
        x: _RealMpfrDoubleSage, /, 
    ) -> _MpfrSage: ...
    @overload
    def __call__(
        self, 
        alpha: ComplexIntervalFieldElement, 
        x: _MpfrDoubleSage, /, 
    ) -> ComplexNumber: ...
    @overload
    def __call__(
        self, 
        alpha: RealBall | RealIntervalFieldElement, 
        x: _ComplexMpfrDoubleSage, /, 
    ) -> ComplexNumber: ...
    # Inf
    @overload
    def __call__(
        self, 
        alpha: _inf, 
        x: _py_number | Integer | Rational | CommutativePolynomial | FloatingSage | _inf,
        /, *, hold: bool = False
    ) -> Expression[SymbolicRing]: ...
    # Expression
    @overload
    def __call__[P: SymbolicRingABC](
        self, 
        alpha: Expression[P], 
        x: Expression[P] | _py_number | Integer | Rational | CommutativePolynomial | FloatingSage | _inf, 
        /, *, hold: bool = False
    ) -> Expression[P]: ...
    @overload
    def __call__[P: SymbolicRingABC](
        self, 
        alpha: _py_number | Integer | Rational | CommutativePolynomial | FloatingSage | _inf, 
        x: Expression[P], 
        /, *, hold: bool = False
    ) -> Expression[P]: ...
    @overload
    def __call__( # pyright: ignore[reportIncompatibleMethodOverride]
        self, alpha: Expression, x: Expression, /, *, hold: bool = False
    ) -> Expression: ...

class _Airy:
    @overload
    def __call__(
        self, x: int | Integer | Rational | RealBall | RealIntervalFieldElement
         | ComplexIntervalFieldElement | _inf, 
        /, *, hold: bool = False
    ) -> Expression[SymbolicRing]: ...
    @overload
    def __call__(
        self, x: CommutativePolynomial, /, 
    ) -> Expression[SymbolicRing] | FloatingSage: ...
    @overload
    def __call__(
        self, x: CommutativePolynomial | ComplexBall, /, *, hold: Literal[True]
    ) -> Expression[SymbolicRing]: ...
    @overload
    def __call__(self, x: ComplexBall, /, ) -> ComplexBall: ...
    @overload
    def __call__[T: _MpfrDoubleSage](self, x: T, /, ) -> T: ...
    @overload
    def __call__[T: SymbolicRingABC](self, x: Expression[T], /, ) -> Expression[T]: ...

class FunctionAiryAiSimple(_Airy, BuiltinFunction):
    def __init__(self) -> None:
        """
        The class for the Airy Ai function.

        EXAMPLES::

            sage: from sage.functions.airy import airy_ai_simple
            sage: f = airy_ai_simple(x); f                                              # needs sage.symbolic
            airy_ai(x)
            sage: airy_ai_simple(x)._sympy_()                                           # needs sage.symbolic
            airyai(x)
        """

class FunctionAiryAiPrime(_Airy, BuiltinFunction):
    def __init__(self) -> None:
        """
        The derivative of the Airy Ai function; see :func:`airy_ai`
        for the full documentation.

        EXAMPLES::

            sage: # needs sage.symbolic
            sage: x, n = var('x n')
            sage: airy_ai_prime(x)
            airy_ai_prime(x)
            sage: airy_ai_prime(0)
            -1/3*3^(2/3)/gamma(1/3)
            sage: airy_ai_prime(x)._sympy_()                                            # needs sympy
            airyaiprime(x)
        """

airy_ai_general: FunctionAiryAiGeneral
airy_ai_simple: FunctionAiryAiSimple
airy_ai_prime: FunctionAiryAiPrime

def airy_ai(alpha, x=None, hold_derivative: bool = True, **kwds):
    '''
    The Airy Ai function.

    The Airy Ai function `\\operatorname{Ai}(x)` is (along with
    `\\operatorname{Bi}(x)`) one of the two linearly independent standard
    solutions to the Airy differential equation `f\'\'(x) - x f(x) = 0`. It is
    defined by the initial conditions:

    .. MATH::

        \\operatorname{Ai}(0)=\\frac{1}{2^{2/3} \\Gamma\\left(\\frac{2}{3}\\right)},

        \\operatorname{Ai}\'(0)=-\\frac{1}{2^{1/3}\\Gamma\\left(\\frac{1}{3}\\right)}.

    Another way to define the Airy Ai function is:

    .. MATH::

        \\operatorname{Ai}(x)=\\frac{1}{\\pi}\\int_0^\\infty
        \\cos\\left(\\frac{1}{3}t^3+xt\\right) dt.

    INPUT:

    - ``alpha`` -- return the `\\alpha`-th order fractional derivative with
      respect to `z`.
      For `\\alpha = n = 1,2,3,\\ldots` this gives the derivative
      `\\operatorname{Ai}^{(n)}(z)`, and for `\\alpha = -n = -1,-2,-3,\\ldots`
      this gives the `n`-fold iterated integral.

    .. MATH::

        f_0(z) = \\operatorname{Ai}(z)

        f_n(z) = \\int_0^z f_{n-1}(t) dt

    - ``x`` -- the argument of the function

    - ``hold_derivative`` -- whether or not to stop from returning higher
      derivatives in terms of `\\operatorname{Ai}(x)` and
      `\\operatorname{Ai}\'(x)`

    .. SEEALSO:: :func:`airy_bi`

    EXAMPLES::

        sage: n, x = var(\'n x\')                                                         # needs sage.symbolic
        sage: airy_ai(x)                                                                # needs sage.symbolic
        airy_ai(x)

    It can return derivatives or integrals::

        sage: # needs sage.symbolic
        sage: airy_ai(2, x)
        airy_ai(2, x)
        sage: airy_ai(1, x, hold_derivative=False)
        airy_ai_prime(x)
        sage: airy_ai(2, x, hold_derivative=False)
        x*airy_ai(x)
        sage: airy_ai(-2, x, hold_derivative=False)
        airy_ai(-2, x)
        sage: airy_ai(n, x)
        airy_ai(n, x)

    It can be evaluated symbolically or numerically for real or complex
    values::

        sage: airy_ai(0)                                                                # needs sage.symbolic
        1/3*3^(1/3)/gamma(2/3)
        sage: airy_ai(0.0)                                                              # needs mpmath
        0.355028053887817
        sage: airy_ai(I)                                                                # needs sage.symbolic
        airy_ai(I)
        sage: airy_ai(1.0*I)                                                            # needs sage.symbolic
        0.331493305432141 - 0.317449858968444*I

    The functions can be evaluated numerically either using mpmath. which
    can compute the values to arbitrary precision, and scipy::

        sage: airy_ai(2).n(prec=100)                                                    # needs sage.symbolic
        0.034924130423274379135322080792
        sage: airy_ai(2).n(algorithm=\'mpmath\', prec=100)                                # needs sage.symbolic
        0.034924130423274379135322080792
        sage: airy_ai(2).n(algorithm=\'scipy\')  # rel tol 1e-10                          # needs scipy sage.symbolic
        0.03492413042327323

    And the derivatives can be evaluated::

        sage: airy_ai(1, 0)                                                             # needs sage.symbolic
        -1/3*3^(2/3)/gamma(1/3)
        sage: airy_ai(1, 0.0)                                                           # needs mpmath
        -0.258819403792807

    Plots::

        sage: plot(airy_ai(x), (x, -10, 5)) + plot(airy_ai_prime(x),                    # needs sage.plot sage.symbolic
        ....:  (x, -10, 5), color=\'red\')
        Graphics object consisting of 2 graphics primitives

    REFERENCES:

    - Abramowitz, Milton; Stegun, Irene A., eds. (1965), "Chapter 10"

    - :wikipedia:`Airy_function`
    '''

class FunctionAiryBiGeneral(BuiltinFunction):
    def __init__(self) -> None:
        """
        The generalized derivative of the Airy Bi function.

        INPUT:

        - ``alpha`` -- return the `\\alpha`-th order fractional derivative with
          respect to `z`.
          For `\\alpha = n = 1,2,3,\\ldots` this gives the derivative
          `\\operatorname{Bi}^{(n)}(z)`, and for `\\alpha = -n = -1,-2,-3,\\ldots`
          this gives the `n`-fold iterated integral.

        .. MATH::

            f_0(z) = \\operatorname{Bi}(z)

            f_n(z) = \\int_0^z f_{n-1}(t) dt

        - ``x`` -- the argument of the function

        EXAMPLES::

            sage: # needs sage.symbolic
            sage: from sage.functions.airy import airy_bi_general
            sage: x, n = var('x n')
            sage: airy_bi_general(-2, x)
            airy_bi(-2, x)
            sage: derivative(airy_bi_general(-2, x), x)
            airy_bi(-1, x)
            sage: airy_bi_general(n, x)
            airy_bi(n, x)
            sage: derivative(airy_bi_general(n, x), x)
            airy_bi(n + 1, x)
        """
        # int
    @overload
    def __call__(
        self, alpha: int, x: int, /, *, hold: bool = False) -> int: ...
    @overload
    def __call__[T: float | complex | _MpfrDoubleSage](
        self, alpha: int | Integer, x: T, /, *, hold: bool = False
    ) -> T: ...
    @overload
    def __call__(
        self, 
        alpha: int | Integer | Rational | CommutativePolynomial, 
        x: Integer | Rational | CommutativePolynomial | ComplexBall, 
        /, *, hold: Literal[True]
    ) -> Expression[SymbolicRing]: ...
    @overload
    def __call__(
        self, alpha: int, x: Integer | Rational, /
    ) -> Expression[SymbolicRing] | Integer: ...
    @overload
    def __call__(
        self, alpha: int, x: CommutativePolynomial, /
    ) -> Expression[SymbolicRing] | Integer | FloatingSage: ...
    @overload
    def __call__(
        self, alpha: int | Integer | Rational | CommutativePolynomial, 
        x: RealBall | RealIntervalFieldElement | ComplexIntervalFieldElement | _inf, 
        /, *, hold: bool = False
    ) -> Expression[SymbolicRing]: ...
    @overload
    def __call__(
        self, alpha: int | Integer | Rational | CommutativePolynomial, 
        x: ComplexBall, /, 
    ) -> Expression[SymbolicRing] | ComplexBall: ...
    # (_, int)
    @overload
    def __call__(
        self, alpha: float, x: int | Integer | Rational, 
        /, *, hold: bool = False
    ) -> Expression[SymbolicRing] | complex | float: ...
    @overload
    def __call__(
        self, alpha: complex, x: int | Integer | Rational, 
        /, *, hold: bool = False
    ) -> Expression[SymbolicRing] | complex: ...
    @overload
    def __call__(
        self, alpha: Integer | Rational, x: int | Integer | Rational, 
        /, *, hold: bool = False
    ) -> Expression[SymbolicRing]: ...
    @overload
    def __call__(
        self, 
        alpha: CommutativePolynomial, 
        x: int | Integer | Rational | CommutativePolynomial, 
        /, *, hold: Literal[True]
    ) -> Expression[SymbolicRing]: ...
    @overload
    def __call__(
        self, alpha: CommutativePolynomial, 
        x: int | Integer | Rational | CommutativePolynomial, /, 
    ) -> Expression[SymbolicRing] | FloatingSage: ...
    @overload
    def __call__(
        self, alpha: RealNumber, x: int | Integer | Rational, /, *, hold: bool = False
    ) -> Expression[SymbolicRing] | _MpfrSage: ...
    @overload
    def __call__(
        self, alpha: RealDoubleElement, x: int | Integer | Rational, /, *, hold: bool = False
    ) -> Expression[SymbolicRing] | _DoubleSage: ...
    @overload
    def __call__[C: _ComplexMpfrDoubleSage](
        self, alpha: C, x: int | Integer | Rational, /, *, hold: bool = False
    ) -> Expression[SymbolicRing] | C: ...
    # float
    @overload
    def __call__(
        self, alpha: float | Rational, x: float, /, *, hold: bool = False
    ) -> complex | float: ...
    @overload
    def __call__(
        self, 
        alpha: float | complex | Integer | Rational | _RealMpfrDoubleSage, 
        x: complex, 
        /, *, hold: bool = False
    ) -> complex: ...
    @overload
    def __call__(
        self, alpha: float | complex, x: CommutativePolynomial, 
        /, *, hold: bool = False
    ) -> Expression[SymbolicRing] | CommutativePolynomial: ...
    @overload
    def __call__(
        self, alpha: float | Rational, x: RealNumber, 
        /, *, hold: bool = False
    ) -> _MpfrSage: ...
    @overload
    def __call__(
        self, alpha: float | Rational, x: RealDoubleElement, 
        /, *, hold: bool = False
    ) -> _MpfrSage: ...
    @overload
    def __call__[C: _ComplexMpfrDoubleSage](
        self, alpha: float | complex | Rational | _RealMpfrDoubleSage, x: C, 
        /, *, hold: bool = False
    ) -> C: ...
    @overload
    def __call__(
        self, 
        alpha: float | complex | FloatingSage | _inf, 
        x: _BallMpfiSage | UnsignedInfinity, 
        /, *, hold: bool = False
    ) -> Expression[SymbolicRing]: ...
    @overload
    def __call__[SignedInf: _inf_signed](
        self, alpha: float, x: SignedInf, 
        /, *, hold: bool = False
    ) -> Expression[SymbolicRing] | SignedInf: ...
    # (_, float)
    @overload
    def __call__(
        self, alpha: complex, x: float | _RealMpfrDoubleSage, /, *, hold: bool = False
    ) -> complex: ...
    @overload
    def __call__(
        self, alpha: CommutativePolynomial, x: float | complex, 
        /, *, hold: bool = False
    ) -> Expression[SymbolicRing] | CommutativePolynomial: ...
    @overload
    def __call__(
        self, alpha: RealNumber, x: float, 
        /, *, hold: bool = False
    ) -> _MpfrSage: ...
    @overload
    def __call__(
        self, alpha: RealDoubleElement, x: float, 
        /, *, hold: bool = False
    ) -> _DoubleSage: ...
    @overload
    def __call__[C: _ComplexMpfrDoubleSage](
        self, alpha: C, x: float | complex, 
        /, *, hold: bool = False
    ) -> C: ...
    @overload
    def __call__(
        self, alpha: ComplexIntervalFieldElement, x: float | complex, /, 
    ) -> ComplexNumber: ...
    # complex
    @overload
    def __call__(
        self, 
        alpha: complex | FloatingSage | _inf, 
        x: _inf, /, *, hold: bool = False
    ) -> Expression[SymbolicRing]: ...
    # Integer / Rational
    @overload
    def __call__(
        self, 
        alpha: Integer | Rational, 
        x: CommutativePolynomial, /, *, hold: bool = False
    ) -> Expression[SymbolicRing] | FloatingSage: ...
    # Polynomial
    @overload
    def __call__(
        self, 
        alpha: CommutativePolynomial, 
        x: _MpfrDoubleSage, /, *, hold: bool = False
    ) -> Expression[SymbolicRing] | CommutativePolynomial: ...
    # RR / RDF
    @overload
    def __call__(
        self, 
        alpha: _MpfrDoubleSage, 
        x: CommutativePolynomial, /, *, hold: bool = False
    ) -> Expression[SymbolicRing] | CommutativePolynomial: ...
    @overload
    def __call__(
        self, 
        alpha: RealNumber, 
        x: _RealMpfrDoubleSage, /, *, hold: bool = False
    ) -> _MpfrSage: ...
    @overload
    def __call__(
        self, 
        alpha: RealDoubleElement, 
        x: _RealMpfrDoubleSage, /, *, hold: bool = False
    ) -> _DoubleSage: ...
    # CC / CDF
    @overload
    def __call__[C: _ComplexMpfrDoubleSage](
        self, alpha: C, x: _MpfrDoubleSage, /, *, hold: bool = False
    ) -> C: ...
    # Balls / IF
    @overload
    def __call__(
        self, 
        alpha: _BallMpfiSage, 
        x: _py_number | Integer | Rational | CommutativePolynomial | FloatingSage, /, hold: bool = False
    ) -> Expression[SymbolicRing]: ...
    # Inf
    @overload
    def __call__(
        self, 
        alpha: _inf, 
        x: _py_number | Integer | Rational | CommutativePolynomial | FloatingSage | _inf,
        /, *, hold: bool = False
    ) -> Expression[SymbolicRing]: ...
    # Expression
    @overload
    def __call__[P: SymbolicRingABC](
        self, 
        alpha: Expression[P], 
        x: Expression[P] | _py_number | Integer | Rational | CommutativePolynomial | FloatingSage | _inf, 
        /, *, hold: bool = False
    ) -> Expression[P]: ...
    @overload
    def __call__[P: SymbolicRingABC](
        self, 
        alpha: _py_number | Integer | Rational | CommutativePolynomial | FloatingSage | _inf, 
        x: Expression[P], 
        /, *, hold: bool = False
    ) -> Expression[P]: ...
    @overload
    def __call__( # pyright: ignore[reportIncompatibleMethodOverride]
        self, alpha: Expression, x: Expression, /, *, hold: bool = False
    ) -> Expression: ...

class FunctionAiryBiSimple(_Airy, BuiltinFunction):
    def __init__(self) -> None:
        """
        The class for the Airy Bi function.

        EXAMPLES::

            sage: from sage.functions.airy import airy_bi_simple
            sage: f = airy_bi_simple(x); f                                              # needs sage.symbolic
            airy_bi(x)
            sage: f._sympy_()                                                           # needs sympy sage.symbolic
            airybi(x)
        """

class FunctionAiryBiPrime(_Airy, BuiltinFunction):
    def __init__(self) -> None:
        """
        The derivative of the Airy Bi function; see :func:`airy_bi`
        for the full documentation.

        EXAMPLES::

            sage: # needs sage.symbolic
            sage: x, n = var('x n')
            sage: airy_bi_prime(x)
            airy_bi_prime(x)
            sage: airy_bi_prime(0)
            3^(1/6)/gamma(1/3)
            sage: airy_bi_prime(x)._sympy_()                                            # needs sympy
            airybiprime(x)
        """

airy_bi_general: FunctionAiryBiGeneral
airy_bi_simple: FunctionAiryBiSimple
airy_bi_prime: FunctionAiryBiPrime

def airy_bi(alpha, x=None, hold_derivative: bool = True, **kwds):
    '''
    The Airy Bi function.

    The Airy Bi function `\\operatorname{Bi}(x)` is (along with
    `\\operatorname{Ai}(x)`) one of the two linearly independent standard
    solutions to the Airy differential equation `f\'\'(x) - x f(x) = 0`. It is
    defined by the initial conditions:

    .. MATH::

        \\operatorname{Bi}(0)=\\frac{1}{3^{1/6} \\Gamma\\left(\\frac{2}{3}\\right)},

        \\operatorname{Bi}\'(0)=\\frac{3^{1/6}}{ \\Gamma\\left(\\frac{1}{3}\\right)}.

    Another way to define the Airy Bi function is:

    .. MATH::

        \\operatorname{Bi}(x)=\\frac{1}{\\pi}\\int_0^\\infty
        \\left[ \\exp\\left( xt -\\frac{t^3}{3} \\right)
        +\\sin\\left(xt + \\frac{1}{3}t^3\\right) \\right ] dt.

    INPUT:

    - ``alpha`` -- return the `\\alpha`-th order fractional derivative with
      respect to `z`.
      For `\\alpha = n = 1,2,3,\\ldots` this gives the derivative
      `\\operatorname{Bi}^{(n)}(z)`, and for `\\alpha = -n = -1,-2,-3,\\ldots`
      this gives the `n`-fold iterated integral.

    .. MATH::

        f_0(z) = \\operatorname{Bi}(z)

        f_n(z) = \\int_0^z f_{n-1}(t) dt

    - ``x`` -- the argument of the function

    - ``hold_derivative`` -- boolean (default: ``True``); whether or not to
      stop from returning higher derivatives in terms of `\\operatorname{Bi}(x)`
      and `\\operatorname{Bi}\'(x)`

    .. SEEALSO:: :func:`airy_ai`

    EXAMPLES::

        sage: n, x = var(\'n x\')                                                         # needs sage.symbolic
        sage: airy_bi(x)                                                                # needs sage.symbolic
        airy_bi(x)

    It can return derivatives or integrals::

        sage: # needs sage.symbolic
        sage: airy_bi(2, x)
        airy_bi(2, x)
        sage: airy_bi(1, x, hold_derivative=False)
        airy_bi_prime(x)
        sage: airy_bi(2, x, hold_derivative=False)
        x*airy_bi(x)
        sage: airy_bi(-2, x, hold_derivative=False)
        airy_bi(-2, x)
        sage: airy_bi(n, x)
        airy_bi(n, x)

    It can be evaluated symbolically or numerically for real or complex
    values::

        sage: airy_bi(0)                                                                # needs sage.symbolic
        1/3*3^(5/6)/gamma(2/3)
        sage: airy_bi(0.0)                                                              # needs mpmath
        0.614926627446001
        sage: airy_bi(I)                                                                # needs sage.symbolic
        airy_bi(I)
        sage: airy_bi(1.0*I)                                                            # needs sage.symbolic
        0.648858208330395 + 0.344958634768048*I

    The functions can be evaluated numerically using mpmath,
    which can compute the values to arbitrary precision, and scipy::

        sage: airy_bi(2).n(prec=100)                                                    # needs sage.symbolic
        3.2980949999782147102806044252
        sage: airy_bi(2).n(algorithm=\'mpmath\', prec=100)                                # needs sage.symbolic
        3.2980949999782147102806044252
        sage: airy_bi(2).n(algorithm=\'scipy\')  # rel tol 1e-10                          # needs scipy sage.symbolic
        3.2980949999782134

    And the derivatives can be evaluated::

        sage: airy_bi(1, 0)                                                             # needs sage.symbolic
        3^(1/6)/gamma(1/3)
        sage: airy_bi(1, 0.0)                                                           # needs mpmath
        0.448288357353826

    Plots::

        sage: plot(airy_bi(x), (x, -10, 5)) + plot(airy_bi_prime(x),                    # needs sage.plot sage.symbolic
        ....:  (x, -10, 5), color=\'red\')
        Graphics object consisting of 2 graphics primitives

    REFERENCES:

    - Abramowitz, Milton; Stegun, Irene A., eds. (1965), "Chapter 10"

    - :wikipedia:`Airy_function`
    '''
