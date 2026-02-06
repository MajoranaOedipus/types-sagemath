r"""
Bessel functions

This module provides symbolic Bessel and Hankel functions, and their
spherical versions. These functions use the `mpmath library`_ for numerical
evaluation and Maxima, GiNaC, Pynac for symbolics.

The main objects which are exported from this module are:

 * :meth:`bessel_J(n, x) <Function_Bessel_J>` -- the Bessel J function
 * :meth:`bessel_Y(n, x) <Function_Bessel_Y>` -- the Bessel Y function
 * :meth:`bessel_I(n, x) <Function_Bessel_I>` -- the Bessel I function
 * :meth:`bessel_K(n, x) <Function_Bessel_K>` -- the Bessel K function
 * :meth:`Bessel(...) <Bessel>` -- a factory function for producing Bessel functions of
   various kinds and orders
 * :meth:`hankel1(nu, z) <Function_Hankel1>` -- the Hankel function of the first kind
 * :meth:`hankel2(nu, z) <Function_Hankel2>` -- the Hankel function of the second kind
 * :meth:`struve_H(nu, z) <Function_Struve_H>` -- the Struve function
 * :meth:`struve_L(nu, z) <Function_Struve_L>` -- the modified Struve function
 * :meth:`spherical_bessel_J(n, z) <SphericalBesselJ>` -- the Spherical Bessel J function
 * :meth:`spherical_bessel_Y(n, z) <SphericalBesselY>` -- the Spherical Bessel J function
 * :meth:`spherical_hankel1(n, z) <SphericalHankel1>` -- the Spherical Hankel function of the first kind
 * :meth:`spherical_hankel2(n, z) <SphericalHankel2>` -- the Spherical Hankel function of the second kind

-  Bessel functions, first defined by the Swiss mathematician
   Daniel Bernoulli and named after Friedrich Bessel, are canonical
   solutions y(x) of Bessel's differential equation:

   .. MATH::

         x^2 \frac{d^2 y}{dx^2} + x \frac{dy}{dx} + \left(x^2 - \nu^2\right)y =
         0,

   for an arbitrary complex number `\nu` (the order).

-  In this module, `J_\nu` denotes the unique solution of Bessel's equation
   which is non-singular at `x = 0`. This function is known as the Bessel
   Function of the First Kind. This function also arises as a special case
   of the hypergeometric function `{}_0F_1`:

   .. MATH::

        J_\nu(x) = \frac{x^n}{2^\nu \Gamma(\nu + 1)} {}_0F_1(\nu +
        1, -\frac{x^2}{4}).

-  The second linearly independent solution to Bessel's equation (which is
   singular at `x=0`) is denoted by `Y_\nu` and is called the Bessel
   Function of the Second Kind:

   .. MATH::

        Y_\nu(x) = \frac{ J_\nu(x) \cos(\pi \nu) -
        J_{-\nu}(x)}{\sin(\pi \nu)}.

-  There are also two commonly used combinations of the Bessel J and Y
   Functions. The Bessel I Function, or the Modified Bessel Function of the
   First Kind, is defined by:

   .. MATH::

       I_\nu(x) = i^{-\nu} J_\nu(ix).

   The Bessel K Function, or the Modified Bessel Function of the Second Kind,
   is defined by:

   .. MATH::

       K_\nu(x) = \frac{\pi}{2} \cdot \frac{I_{-\nu}(x) -
       I_n(x)}{\sin(\pi \nu)}.

   We should note here that the above formulas for Bessel Y and K functions
   should be understood as limits when `\nu` is an integer.

-  It follows from Bessel's differential equation that the derivative of
   `J_n(x)` with respect to `x` is:

   .. MATH::

       \frac{d}{dx} J_n(x) = \frac{1}{x^n} \left(x^n J_{n-1}(x) - n x^{n-1}
       J_n(z) \right)

-  Another important formulation of the two linearly independent
   solutions to Bessel's equation are the Hankel functions
   `H_\nu^{(1)}(x)` and `H_\nu^{(2)}(x)`,
   defined by:

   .. MATH::

         H_\nu^{(1)}(x) = J_\nu(x) + i Y_\nu(x)

   .. MATH::

         H_\nu^{(2)}(x) = J_\nu(x) - i Y_\nu(x)

   where `i` is the imaginary unit (and `J_*` and
   `Y_*` are the usual J- and Y-Bessel functions). These
   linear combinations are also known as Bessel functions of the third
   kind; they are also two linearly independent solutions of Bessel's
   differential equation. They are named for Hermann Hankel.

-  When solving for separable solutions of Laplace's equation in
   spherical coordinates, the radial equation has the form:

   .. MATH::

         x^2 \frac{d^2 y}{dx^2} + 2x \frac{dy}{dx} + [x^2 - n(n+1)]y = 0.

   The spherical Bessel functions `j_n` and `y_n`,
   are two linearly independent solutions to this equation. They are
   related to the ordinary Bessel functions `J_n` and
   `Y_n` by:

   .. MATH::

         j_n(x) = \sqrt{\frac{\pi}{2x}} J_{n+1/2}(x),

   .. MATH::

         y_n(x) = \sqrt{\frac{\pi}{2x}} Y_{n+1/2}(x) = (-1)^{n+1} \sqrt{\frac{\pi}{2x}} J_{-n-1/2}(x).

EXAMPLES:

    Evaluate the Bessel J function symbolically and numerically::

        sage: # needs sage.symbolic
        sage: bessel_J(0, x)
        bessel_J(0, x)
        sage: bessel_J(0, 0)
        1
        sage: bessel_J(0, x).diff(x)
        -1/2*bessel_J(1, x) + 1/2*bessel_J(-1, x)
        sage: N(bessel_J(0, 0), digits=20)
        1.0000000000000000000
        sage: find_root(bessel_J(0,x), 0, 5)                                            # needs scipy
        2.404825557695773

    Plot the Bessel J function::

        sage: f(x) = Bessel(0)(x); f                                                    # needs sage.symbolic
        x |--> bessel_J(0, x)
        sage: plot(f, (x, 1, 10))                                                       # needs sage.plot sage.symbolic
        Graphics object consisting of 1 graphics primitive

    Visualize the Bessel Y function on the complex plane
    (set plot_points to a higher value to get more detail)::

        sage: complex_plot(bessel_Y(0, x), (-5, 5), (-5, 5), plot_points=20)            # needs sage.plot sage.symbolic
        Graphics object consisting of 1 graphics primitive

    Evaluate a combination of Bessel functions::

        sage: # needs sage.symbolic
        sage: f(x) = bessel_J(1, x) - bessel_Y(0, x)
        sage: f(pi)
        bessel_J(1, pi) - bessel_Y(0, pi)
        sage: f(pi).n()
        -0.0437509653365599
        sage: f(pi).n(digits=50)
        -0.043750965336559909054985168023342675387737118378169

    Symbolically solve a second order differential equation with initial
    conditions `y(1) = a` and `y'(1) = b` in terms of Bessel functions::

        sage: # needs sage.symbolic
        sage: y = function('y')(x)
        sage: a, b = var('a, b')
        sage: diffeq = x^2*diff(y,x,x) + x*diff(y,x) + x^2*y == 0
        sage: f = desolve(diffeq, y, [1, a, b]); f
        (a*bessel_Y(1, 1) + b*bessel_Y(0, 1))*bessel_J(0, x)/(bessel_J(0,
        1)*bessel_Y(1, 1) - bessel_J(1, 1)*bessel_Y(0, 1)) -
        (a*bessel_J(1, 1) + b*bessel_J(0, 1))*bessel_Y(0, x)/(bessel_J(0,
        1)*bessel_Y(1, 1) - bessel_J(1, 1)*bessel_Y(0, 1))


    For more examples, see the docstring for :meth:`Bessel`.

AUTHORS:

    - Some of the documentation here has been adapted from David Joyner's
      original documentation of Sage's special functions module (2006).

REFERENCES:

- [AS-Bessel]_

- [AS-Spherical]_

- [AS-Struve]_

- [DLMF-Bessel]_

- [DLMF-Struve]_

.. _`mpmath library`: http://mpmath.org

- [WP-Bessel]_

- [WP-Struve]_
"""

from typing import Callable, Literal, overload
from _typeshed import Incomplete
from typings_sagemath import (
    FloatingSage, RealInexactSage, ComplexInexactSage, CoercibleToExpression)
from sage.symbolic.expression import Expression as Expression_
from sage.symbolic.ring import SymbolicRing
from sage.rings.abc import SymbolicRing as SymbolicRingABC
from sage.rings.polynomial.commutative_polynomial import CommutativePolynomial
from sage.rings.infinity import MinusInfinity, PlusInfinity, UnsignedInfinity
from sage.rings.real_mpfr import RealNumber
from sage.rings.real_double import RealDoubleElement
from sage.rings.real_arb import RealBall
from sage.rings.real_mpfi import RealIntervalFieldElement
from sage.rings.complex_mpfr import ComplexNumber
from sage.rings.complex_double import ComplexDoubleElement
from sage.rings.complex_arb import ComplexBall
from sage.rings.complex_interval import ComplexIntervalFieldElement
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

from sage.functions.gamma import gamma as gamma
from sage.functions.hyperbolic import cosh as cosh, sinh as sinh
from sage.functions.log import exp as exp
from sage.functions.trig import cos as cos, sin as sin
from sage.misc.functional import sqrt as sqrt
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.misc.latex import latex as latex
from sage.rings.infinity import infinity as infinity, unsigned_infinity as unsigned_infinity
from sage.rings.integer import Integer as Integer
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.rational_field import QQ as QQ
# from sage.structure.element import Expression as Expression, get_coercion_model as get_coercion_model
from sage.symbolic.function import BuiltinFunction as BuiltinFunction
from sage.symbolic.constants import pi as pi
from sage.symbolic.ring import SR as SR

class Function_Bessel_J(BuiltinFunction):
    """
    The Bessel J Function, denoted by bessel_J(`\\nu`, x) or `J_\\nu(x)`.
    As a Taylor series about `x=0` it is equal to:

    .. MATH::

        J_\\nu(x) = \\sum_{k=0}^\\infty \\frac{(-1)^k}{k! \\Gamma(k+\\nu+1)}
        \\left(\\frac{x}{2}\\right)^{2k+\\nu}

    The parameter `\\nu` is called the order and may be any real or
    complex number; however, integer and half-integer values are most
    common. It is defined for all complex numbers `x` when `\\nu`
    is an integer or greater than zero and it diverges as `x \\to 0`
    for negative non-integer values of `\\nu`.

    For integer orders `\\nu = n` there is an integral representation:

    .. MATH::

        J_n(x) = \\frac{1}{\\pi} \\int_0^\\pi \\cos(n t - x \\sin(t)) \\; dt

    This function also arises as a special case of the hypergeometric
    function `{}_0F_1`:

    .. MATH::

        J_\\nu(x) = \\frac{x^n}{2^\\nu \\Gamma(\\nu + 1)} {}_0F_1\\left(\\nu +
        1, -\\frac{x^2}{4}\\right).

    EXAMPLES::

        sage: bessel_J(1.0, 1.0)                                                        # needs mpmath
        0.440050585744933

        sage: # needs sage.symbolic
        sage: bessel_J(2, I).n(digits=30)
        -0.135747669767038281182852569995
        sage: bessel_J(1, x)
        bessel_J(1, x)
        sage: n = var('n')
        sage: bessel_J(n, x)
        bessel_J(n, x)

    Examples of symbolic manipulation::

        sage: # needs sage.symbolic
        sage: a = bessel_J(pi, bessel_J(1, I)); a
        bessel_J(pi, bessel_J(1, I))
        sage: N(a, digits=20)
        0.00059023706363796717363 - 0.0026098820470081958110*I
        sage: f = bessel_J(2, x)
        sage: f.diff(x)
        -1/2*bessel_J(3, x) + 1/2*bessel_J(1, x)

    Comparison to a well-known integral representation of `J_1(1)`::

        sage: A = numerical_integral(1/pi*cos(x - sin(x)), 0, pi)                       # needs sage.symbolic
        sage: A[0]  # abs tol 1e-14                                                     # needs sage.symbolic
        0.44005058574493355
        sage: bessel_J(1.0, 1.0) - A[0] < 1e-15                                         # needs sage.symbolic
        True

    Integration is supported directly and through Maxima::

        sage: f = bessel_J(2, x)                                                        # needs sage.symbolic
        sage: f.integrate(x)                                                            # needs sage.symbolic
        1/24*x^3*hypergeometric((3/2,), (5/2, 3), -1/4*x^2)

    Visualization (set plot_points to a higher value to get more detail)::

        sage: plot(bessel_J(1,x), (x,0,5), color='blue')                                # needs sage.plot sage.symbolic
        Graphics object consisting of 1 graphics primitive
        sage: complex_plot(bessel_J(1, x), (-5, 5), (-5, 5), plot_points=20)            # needs sage.plot sage.symbolic
        Graphics object consisting of 1 graphics primitive

    ALGORITHM:

        Numerical evaluation is handled by the mpmath library. Symbolics are
        handled by a combination of Maxima and Sage (Ginac/Pynac).

    Check whether the return value is real whenever the argument is real (:issue:`10251`)::

        sage: bessel_J(5, 1.5) in RR                                                    # needs mpmath
        True

    REFERENCES:

    - [AS-Bessel]_

    - [DLMF-Bessel]_

    - [AS-Bessel]_
    """
    def __init__(self) -> None:
        """
        See the docstring for :meth:`Function_Bessel_J`.

        EXAMPLES::

            sage: sage.functions.bessel.Function_Bessel_J()
            bessel_J
            sage: bessel_J(x, x)._sympy_()                                              # needs sympy sage.symbolic
            besselj(x, x)
        """
    # int
    @overload
    def __call__(
        self, 
        nu: _py_number | Integer | Rational | CommutativePolynomial | FloatingSage | _inf, 
        x:  _BallMpfiSage | _inf, 
        /, *, 
        hold: bool = False
    ) -> Expression_[SymbolicRing]: ...
    @overload
    def __call__(
        self, 
        nu: int | Integer | Rational | CommutativePolynomial, 
        x: int | Integer | Rational | CommutativePolynomial, 
        /, *, 
        hold: Literal[True]
    ) -> Expression_[SymbolicRing]: ...
    @overload
    def __call__(
        self, nu: int, x: int, /, 
    ) -> Expression_[SymbolicRing] | int: ...
    @overload
    def __call__(
        self, nu: int | Integer | Rational, x: Integer | Rational, /, 
    ) -> Expression_[SymbolicRing] | Integer: ...
    @overload
    def __call__(
        self, nu: int | Integer | Rational, x: CommutativePolynomial, /, 
    ) -> Expression_[SymbolicRing] | Integer | FloatingSage: ...
    @overload
    def __call__(
        self, 
        nu: Integer | Rational, 
        x: int, /, 
    ) -> Expression_[SymbolicRing] | Integer: ...
    @overload
    def __call__[T: float | complex | _MpfrDoubleSage](
        self, 
        nu: int | Integer, 
        x: T, 
        /, *, hold: bool = False
    ) -> T: ...
    #float
    @overload
    def __call__(
        self, nu: float, x: int | float | Integer | Rational, /, *,
        hold: bool = False
    ) -> float | complex: ...
    @overload
    def __call__(
        self, nu: float | Rational | _RealMpfrDoubleSage, x: complex, /, *,
        hold: bool = False
    ) -> complex: ...
    @overload
    def __call__(
        self, 
        nu: float | complex | _MpfrDoubleSage, 
        x: CommutativePolynomial, /, *,
        hold: bool = False
    ) -> CommutativePolynomial | Expression_[SymbolicRing]: ...
    @overload
    def __call__(
        self, 
        nu: float | Rational | RealNumber, 
        x: RealNumber, /, *,
        hold: bool = False
    ) -> RealNumber | ComplexNumber: ...
    @overload
    def __call__(
        self, 
        nu: float | Rational | RealDoubleElement, 
        x: RealDoubleElement, /, *,
        hold: bool = False
    ) -> RealDoubleElement | ComplexDoubleElement: ...
    @overload
    def __call__[T: ComplexNumber | ComplexDoubleElement](
        self, 
        nu: float | complex | Integer | Rational | _RealMpfrDoubleSage | ComplexNumber, 
        x: T, /, *,
        hold: bool = False
    ) -> T: ...
    # complex
    @overload
    def __call__(
        self, 
        nu: complex, 
        x: _py_number | Integer | Rational | _RealMpfrDoubleSage, /, *,
        hold: bool = False
    ) -> complex: ...
    # Rational
    @overload
    def __call__(
        self, nu: Rational, x: float, /, *, hold: bool = False
    ) -> complex | float: ...
    # Polynomials
    @overload
    def __call__(
        self, 
        nu: CommutativePolynomial, 
        x: float | complex | _MpfrDoubleSage, /, *, hold: bool = False
    ) -> CommutativePolynomial | Expression_[SymbolicRing]: ...
    @overload
    def __call__(
        self, 
        nu: CommutativePolynomial, 
        x: int | Integer | Rational | CommutativePolynomial, /, 
    ) -> Integer | FloatingSage | Expression_[SymbolicRing]: ...
    @overload
    def __call__(
        self, 
        nu: CommutativePolynomial, 
        x: int | Integer | Rational | CommutativePolynomial, /, 
        *, hold: Literal[True]
    ) -> Expression_[SymbolicRing]: ...
    # Sage Real Floating
    @overload
    def __call__(
        self, 
        nu: RealNumber, 
        x: int | float | Integer | Rational | RealDoubleElement, /, 
        *, hold: bool = False
    ) -> RealNumber | ComplexNumber: ...
    @overload
    def __call__(
        self, 
        nu: RealDoubleElement, 
        x: int | float | Integer | Rational | RealNumber, /, 
        *, hold: bool = False
    ) -> RealDoubleElement | ComplexDoubleElement: ...
    @overload
    def __call__(
        self, 
        nu: _BallMpfiSage, 
        x: float | complex | _MpfrDoubleSage, /, 
        *, hold: bool = False
    ) -> Expression_[SymbolicRing]: ...
    @overload
    def __call__(
        self, 
        nu: RealBall | RealIntervalFieldElement | ComplexBall, 
        x: int | Integer | Rational | CommutativePolynomial, /, 
    ) -> Expression_[SymbolicRing] | Integer: ...
    @overload
    def __call__(
        self, 
        nu: _BallMpfiSage, 
        x: int | Integer | Rational | CommutativePolynomial, 
        /, *, hold: Literal[True]
    ) -> Expression_[SymbolicRing]: ...
    # Sage Complex Floating
    @overload
    def __call__[T: ComplexNumber | ComplexDoubleElement](
        self, nu: T, x: _py_number | Integer | Rational | _MpfrDoubleSage, /
    ) -> T: ...
    @overload
    def __call__(
        self, 
        nu: ComplexIntervalFieldElement, 
        x: int | Integer | Rational | CommutativePolynomial, 
        /, *, hold: bool = False
    ) -> Expression_[SymbolicRing]: ...
    # inf
    @overload
    def __call__(
        self, 
        nu: MinusInfinity | UnsignedInfinity, 
        x: _py_number | Integer | Rational | CommutativePolynomial | FloatingSage, /, *, hold: bool = False
    ) -> Expression_[SymbolicRing]: ...
    @overload
    def __call__(
        self, 
        nu: PlusInfinity, 
        x: float | complex | FloatingSage, /, *, hold: bool = False
    ) -> Expression_[SymbolicRing]: ...
    @overload
    def __call__(
        self, 
        nu: PlusInfinity, 
        x: int | Integer | Rational | CommutativePolynomial, 
        /, 
    ) -> Expression_[SymbolicRing] | Integer: ...
    @overload
    def __call__(
        self, 
        nu: PlusInfinity, 
        x: int | Integer | Rational | CommutativePolynomial, 
        /, *, hold: Literal[True]
    ) -> Expression_[SymbolicRing]: ...
    @overload
    def __call__[P: SymbolicRingABC](
        self, 
        nu: Expression_[P], 
        x: _py_number | Integer | Rational | CommutativePolynomial | FloatingSage | Expression_[P], /, *, hold: bool = False
    ) -> Expression_[P]: ...
    @overload
    def __call__[P: SymbolicRingABC](
        self, 
        nu: _py_number | Integer | Rational | CommutativePolynomial | FloatingSage,
        x: Expression_[P], /, *, hold: bool = False
    ) -> Expression_[P]: ...
    @overload
    def __call__(
        self, 
        nu: Expression_,
        x: Expression_, /, *, hold: bool = False
    ) -> Expression_: ...

bessel_J: Function_Bessel_J

class Function_Bessel_Y(BuiltinFunction):
    """
    The Bessel Y functions, also known as the Bessel functions of the second
    kind, Weber functions, or Neumann functions.

    `Y_\\nu(z)` is a holomorphic function of `z` on the complex plane,
    cut along the negative real axis. It is singular at `z = 0`. When `z`
    is fixed, `Y_\\nu(z)` is an entire function of the order `\\nu`.

    DEFINITION:

    .. MATH::

        Y_n(z) = \\frac{J_\\nu(z) \\cos(\\nu z) -
        J_{-\\nu}(z)}{\\sin(\\nu z)}

    Its derivative with respect to `z` is:

    .. MATH::

        \\frac{d}{dz} Y_n(z) = \\frac{1}{z^n} \\left(z^n Y_{n-1}(z) - n z^{n-1}
        Y_n(z) \\right)

    EXAMPLES::

        sage: bessel_Y(1, x)                                                            # needs sage.symbolic
        bessel_Y(1, x)
        sage: bessel_Y(1.0, 1.0)                                                        # needs mpmath
        -0.781212821300289

        sage: # needs sage.symbolic
        sage: n = var('n')
        sage: bessel_Y(n, x)
        bessel_Y(n, x)
        sage: bessel_Y(2, I).n()
        1.03440456978312 - 0.135747669767038*I
        sage: bessel_Y(0, 0).n()
        -infinity
        sage: bessel_Y(0, 1).n(128)
        0.088256964215676957982926766023515162828

    Examples of symbolic manipulation::

        sage: # needs sage.symbolic
        sage: a = bessel_Y(pi, bessel_Y(1, I)); a
        bessel_Y(pi, bessel_Y(1, I))
        sage: N(a, digits=20)
        4.2059146571791095708 + 21.307914215321993526*I
        sage: f = bessel_Y(2, x)
        sage: f.diff(x)
        -1/2*bessel_Y(3, x) + 1/2*bessel_Y(1, x)

    High precision and complex valued inputs (see :issue:`4230`)::

        sage: bessel_Y(0, 1).n(128)                                                     # needs sage.symbolic
        0.088256964215676957982926766023515162828
        sage: bessel_Y(0, RealField(200)(1))                                            # needs sage.rings.real_mpfr
        0.088256964215676957982926766023515162827817523090675546711044
        sage: bessel_Y(0, ComplexField(200)(0.5+I))                                     # needs sage.symbolic
        0.077763160184438051408593468823822434235010300228009867784073
         + 1.0142336049916069152644677682828326441579314239591288411739*I

    Visualization (set plot_points to a higher value to get more detail)::

        sage: plot(bessel_Y(1, x), (x, 0, 5), color='blue')                             # needs sage.plot sage.symbolic
        Graphics object consisting of 1 graphics primitive
        sage: complex_plot(bessel_Y(1, x), (-5, 5), (-5, 5), plot_points=20)            # needs sage.plot sage.symbolic
        Graphics object consisting of 1 graphics primitive

    ALGORITHM:

        Numerical evaluation is handled by the mpmath library. Symbolics are
        handled by a combination of Maxima and Sage (Ginac/Pynac).

    TESTS:

    Check whether the return value is real whenever the argument is real (:issue:`10251`)::

        sage: bessel_Y(5, 1.5) in RR                                                    # needs mpmath
        True

    Coercion works correctly (see :issue:`17130`)::

        sage: # needs sage.rings.real_mpfr
        sage: r = bessel_Y(RealField(200)(1), 1.0); r
        -0.781212821300289
        sage: parent(r)
        Real Field with 53 bits of precision
        sage: r = bessel_Y(RealField(200)(1), 1); r
        -0.78121282130028871654715000004796482054990639071644460784383
        sage: parent(r)
        Real Field with 200 bits of precision

    REFERENCES:

    - [AS-Bessel]_

    - [DLMF-Bessel]_

    - [WP-Bessel]_
    """
    def __init__(self) -> None:
        """
        See the docstring for :meth:`Function_Bessel_Y`.

        EXAMPLES::

            sage: sage.functions.bessel.Function_Bessel_Y()(0, x)                       # needs sage.symbolic
            bessel_Y(0, x)
            sage: bessel_Y(x, x)._sympy_()                                              # needs sympy sage.symbolic
            bessely(x, x)
        """

bessel_Y: Function_Bessel_Y

class Function_Bessel_I(BuiltinFunction):
    """
    The Bessel I function, or the Modified Bessel Function of the First Kind.

    DEFINITION:

    .. MATH::

        I_\\nu(x) = i^{-\\nu} J_\\nu(ix)

    EXAMPLES::

        sage: bessel_I(1.0, 1.0)                                                        # needs mpmath
        0.565159103992485

        sage: # needs sage.symbolic
        sage: bessel_I(1, x)
        bessel_I(1, x)
        sage: n = var('n')
        sage: bessel_I(n, x)
        bessel_I(n, x)
        sage: bessel_I(2, I).n()
        -0.114903484931900

    Examples of symbolic manipulation::

        sage: # needs sage.symbolic
        sage: a = bessel_I(pi, bessel_I(1, I))
        sage: N(a, digits=20)
        0.00026073272117205890524 - 0.0011528954889080572268*I
        sage: f = bessel_I(2, x)
        sage: f.diff(x)
        1/2*bessel_I(3, x) + 1/2*bessel_I(1, x)

    Special identities that bessel_I satisfies::

        sage: # needs sage.symbolic
        sage: bessel_I(1/2, x)
        sqrt(2)*sqrt(1/(pi*x))*sinh(x)
        sage: eq = bessel_I(1/2, x) == bessel_I(0.5, x)
        sage: eq.test_relation()
        True
        sage: bessel_I(-1/2, x)
        sqrt(2)*sqrt(1/(pi*x))*cosh(x)
        sage: eq = bessel_I(-1/2, x) == bessel_I(-0.5, x)
        sage: eq.test_relation()
        True

    Examples of asymptotic behavior::

        sage: limit(bessel_I(0, x), x=oo)                                               # needs sage.symbolic
        +Infinity
        sage: limit(bessel_I(0, x), x=0)                                                # needs sage.symbolic
        1

    High precision and complex valued inputs::

        sage: bessel_I(0, 1).n(128)                                                     # needs sage.symbolic
        1.2660658777520083355982446252147175376
        sage: bessel_I(0, RealField(200)(1))                                            # needs sage.rings.real_mpfr
        1.2660658777520083355982446252147175376076703113549622068081
        sage: bessel_I(0, ComplexField(200)(0.5+I))                                     # needs sage.symbolic
        0.80644357583493619472428518415019222845373366024179916785502
         + 0.22686958987911161141397453401487525043310874687430711021434*I

    Visualization (set plot_points to a higher value to get more detail)::

        sage: plot(bessel_I(1, x), (x, 0, 5), color='blue')                             # needs sage.plot sage.symbolic
        Graphics object consisting of 1 graphics primitive
        sage: complex_plot(bessel_I(1, x), (-5, 5), (-5, 5), plot_points=20)            # needs sage.plot sage.symbolic
        Graphics object consisting of 1 graphics primitive

    ALGORITHM:

        Numerical evaluation is handled by the mpmath library. Symbolics are
        handled by a combination of Maxima and Sage (Ginac/Pynac).

    TESTS::

        sage: N(bessel_I(1,1),500)                                                      # needs sage.symbolic
        0.565159103992485027207696027609863307328899621621092009480294489479255640964371134092664997766814410064677886055526302676857637684917179812041131208121

    Check whether the return value is real whenever the argument is real (:issue:`10251`)::

        sage: bessel_I(5, 1.5) in RR                                                    # needs mpmath
        True

    REFERENCES:

    - [AS-Bessel]_

    - [DLMF-Bessel]_

    - [WP-Bessel]_
    """
    def __init__(self) -> None:
        """
        See the docstring for :meth:`Function_Bessel_I`.

        EXAMPLES::

            sage: bessel_I(1, x)                                                        # needs sage.symbolic
            bessel_I(1, x)
            sage: bessel_I(x, x)._sympy_()                                              # needs sympy sage.symbolic
            besseli(x, x)
        """
    # int
    @overload
    def __call__(
        self, 
        nu: _py_number | Integer | Rational | CommutativePolynomial | FloatingSage | _inf, 
        x:  _BallMpfiSage | _inf, 
        /, *, 
        hold: bool = False
    ) -> Expression_[SymbolicRing]: ...
    @overload
    def __call__(
        self, 
        nu: int | Integer | Rational | CommutativePolynomial, 
        x: int | Integer | Rational | CommutativePolynomial, 
        /, *, 
        hold: Literal[True]
    ) -> Expression_[SymbolicRing]: ...
    @overload
    def __call__(
        self, nu: int, x: int, /, 
    ) -> Expression_[SymbolicRing] | int: ...
    @overload
    def __call__(
        self, nu: int | Integer | Rational, x: Integer | Rational, /, 
    ) -> Expression_[SymbolicRing] | Integer: ...
    @overload
    def __call__(
        self, nu: int | Integer | Rational, x: CommutativePolynomial, /, 
    ) -> Expression_[SymbolicRing] | Integer | FloatingSage: ...
    @overload
    def __call__(
        self, 
        nu: int | Integer | Rational, 
        x: float, 
        /, *, hold: bool = False
    ) -> float | complex: ...
    @overload
    def __call__(
        self, 
        nu: int | Integer, 
        x: complex, 
        /, *, hold: bool = False
    ) -> complex: ...
    #float
    @overload
    def __call__(
        self, nu: float, x: int | float | Integer | Rational, /, *,
        hold: bool = False
    ) -> float | complex: ...
    @overload
    def __call__(
        self, nu: float | Rational | _RealMpfrDoubleSage, x: complex, /, *,
        hold: bool = False
    ) -> complex: ...
    @overload
    def __call__(
        self, 
        nu: float | complex | _MpfrDoubleSage, 
        x: CommutativePolynomial, /, *,
        hold: bool = False
    ) -> CommutativePolynomial | Expression_[SymbolicRing]: ...
    @overload
    def __call__(
        self, 
        nu: int | float | Integer | Rational | RealNumber, 
        x: RealNumber, /, *,
        hold: bool = False
    ) -> RealNumber | ComplexNumber: ...
    @overload
    def __call__(
        self, 
        nu: int | float | Integer | Rational | RealDoubleElement, 
        x: RealDoubleElement, /, *,
        hold: bool = False
    ) -> RealDoubleElement | ComplexDoubleElement: ...
    @overload
    def __call__[T: ComplexNumber | ComplexDoubleElement](
        self, 
        nu: float | complex | Integer | Rational | _RealMpfrDoubleSage | ComplexNumber, 
        x: T, /, *,
        hold: bool = False
    ) -> T: ...
    # complex
    @overload
    def __call__(
        self, 
        nu: complex, 
        x: _py_number | Integer | Rational | _RealMpfrDoubleSage, /, *,
        hold: bool = False
    ) -> complex: ...
    # Integer
    @overload
    def __call__(
        self, 
        nu: Integer | Rational, 
        x: int, /, 
    ) -> Expression_[SymbolicRing] | Integer: ...
    # Rational
    @overload
    def __call__(
        self, nu: Rational, x: float, /, *, hold: bool = False
    ) -> complex | float: ...
    # Polynomials
    @overload
    def __call__(
        self, 
        nu: CommutativePolynomial, 
        x: float | complex | _MpfrDoubleSage, /, *, hold: bool = False
    ) -> CommutativePolynomial | Expression_[SymbolicRing]: ...
    @overload
    def __call__(
        self, 
        nu: CommutativePolynomial, 
        x: int | Integer | Rational | CommutativePolynomial, /, 
    ) -> Integer | FloatingSage | Expression_[SymbolicRing]: ...
    @overload
    def __call__(
        self, 
        nu: CommutativePolynomial, 
        x: int | Integer | Rational | CommutativePolynomial, /, 
        *, hold: Literal[True]
    ) -> Expression_[SymbolicRing]: ...
    # Sage Real Floating
    @overload
    def __call__(
        self, 
        nu: RealNumber, 
        x: int | float | Integer | Rational | RealDoubleElement, /, 
        *, hold: bool = False
    ) -> RealNumber | ComplexNumber: ...
    @overload
    def __call__(
        self, 
        nu: RealDoubleElement, 
        x: int | float | Integer | Rational | RealNumber, /, 
        *, hold: bool = False
    ) -> RealDoubleElement | ComplexDoubleElement: ...
    @overload
    def __call__(
        self, 
        nu: _BallMpfiSage, 
        x: float | complex | _MpfrDoubleSage, /, 
        *, hold: bool = False
    ) -> Expression_[SymbolicRing]: ...
    @overload
    def __call__(
        self, 
        nu: RealBall | RealIntervalFieldElement | ComplexBall, 
        x: int | Integer | Rational | CommutativePolynomial, /, 
    ) -> Expression_[SymbolicRing] | Integer: ...
    @overload
    def __call__(
        self, 
        nu: _BallMpfiSage, 
        x: int | Integer | Rational | CommutativePolynomial, 
        /, *, hold: Literal[True]
    ) -> Expression_[SymbolicRing]: ...
    # Sage Complex Floating
    @overload
    def __call__[T: ComplexNumber | ComplexDoubleElement](
        self, nu: T, x: _py_number | Integer | Rational | _MpfrDoubleSage, /
    ) -> T: ...
    @overload
    def __call__(
        self, 
        nu: ComplexIntervalFieldElement, 
        x: int | Integer | Rational | CommutativePolynomial, 
        /, *, hold: bool = False
    ) -> Expression_[SymbolicRing]: ...
    # inf
    @overload
    def __call__(
        self, 
        nu: MinusInfinity | UnsignedInfinity, 
        x: _py_number | Integer | Rational | CommutativePolynomial | FloatingSage, /, *, hold: bool = False
    ) -> Expression_[SymbolicRing]: ...
    @overload
    def __call__(
        self, 
        nu: PlusInfinity, 
        x: float | complex | FloatingSage, /, *, hold: bool = False
    ) -> Expression_[SymbolicRing]: ...
    @overload
    def __call__(
        self, 
        nu: PlusInfinity, 
        x: int | Integer | Rational | CommutativePolynomial, 
        /, 
    ) -> Expression_[SymbolicRing] | Integer: ...
    @overload
    def __call__(
        self, 
        nu: PlusInfinity, 
        x: int | Integer | Rational | CommutativePolynomial, 
        /, *, hold: Literal[True]
    ) -> Expression_[SymbolicRing]: ...
    @overload
    def __call__[P: SymbolicRingABC](
        self, 
        nu: Expression_[P], 
        x: _py_number | Integer | Rational | CommutativePolynomial | FloatingSage | Expression_[P], /, *, hold: bool = False
    ) -> Expression_[P]: ...
    @overload
    def __call__[P: SymbolicRingABC](
        self, 
        nu: _py_number | Integer | Rational | CommutativePolynomial | FloatingSage,
        x: Expression_[P], /, *, hold: bool = False
    ) -> Expression_[P]: ...
    @overload
    def __call__(
        self, 
        nu: Expression_,
        x: Expression_, /, *, hold: bool = False
    ) -> Expression_: ...

bessel_I: Function_Bessel_I

class Function_Bessel_K(BuiltinFunction):
    """
    The Bessel K function, or the modified Bessel function of the second kind.

    DEFINITION:

    .. MATH::

        K_\\nu(x) = \\frac{\\pi}{2} \\frac{I_{-\\nu}(x)-I_\\nu(x)}{\\sin(\\nu \\pi)}

    EXAMPLES::

        sage: bessel_K(1.0, 1.0)                                                        # needs mpmath
        0.601907230197235

        sage: # needs sage.symbolic
        sage: bessel_K(1, x)
        bessel_K(1, x)
        sage: n = var('n')
        sage: bessel_K(n, x)
        bessel_K(n, x)
        sage: bessel_K(2, I).n()
        -2.59288617549120 + 0.180489972066962*I

    Examples of symbolic manipulation::

        sage: # needs sage.symbolic
        sage: a = bessel_K(pi, bessel_K(1, I)); a
        bessel_K(pi, bessel_K(1, I))
        sage: N(a, digits=20)
        3.8507583115005220156 + 0.068528298579883425456*I
        sage: f = bessel_K(2, x)
        sage: f.diff(x)
        -1/2*bessel_K(3, x) - 1/2*bessel_K(1, x)
        sage: bessel_K(1/2, x)
        sqrt(1/2)*sqrt(pi)*e^(-x)/sqrt(x)
        sage: bessel_K(1/2, -1)
        -I*sqrt(1/2)*sqrt(pi)*e
        sage: bessel_K(1/2, 1)
        sqrt(1/2)*sqrt(pi)*e^(-1)

    Examples of asymptotic behavior::

        sage: bessel_K(0, 0.0)                                                          # needs mpmath
        +infinity
        sage: limit(bessel_K(0, x), x=0)                                                # needs sage.symbolic
        +Infinity
        sage: limit(bessel_K(0, x), x=oo)                                               # needs sage.symbolic
        0

    High precision and complex valued inputs::

        sage: bessel_K(0, 1).n(128)                                                     # needs sage.symbolic
        0.42102443824070833333562737921260903614
        sage: bessel_K(0, RealField(200)(1))                                            # needs sage.rings.real_mpfr
        0.42102443824070833333562737921260903613621974822666047229897
        sage: bessel_K(0, ComplexField(200)(0.5+I))                                     # needs sage.rings.real_mpfr sage.symbolic
        0.058365979093103864080375311643360048144715516692187818271179
         - 0.67645499731334483535184142196073004335768129348518210260256*I

    Visualization (set plot_points to a higher value to get more detail)::

        sage: plot(bessel_K(1,x), (x,0,5), color='blue')                                # needs sage.plot sage.symbolic
        Graphics object consisting of 1 graphics primitive
        sage: complex_plot(bessel_K(1, x), (-5, 5), (-5, 5), plot_points=20)            # needs sage.plot sage.symbolic
        Graphics object consisting of 1 graphics primitive

    ALGORITHM:

        Numerical evaluation is handled by the mpmath library. Symbolics are
        handled by a combination of Maxima and Sage (Ginac/Pynac).

    TESTS:

    Verify that :issue:`3426` is fixed:

    The Bessel K function can be evaluated numerically at complex orders::

        sage: bessel_K(10 * I, 10).n()                                                  # needs sage.symbolic
        9.82415743819925e-8

    For a fixed imaginary order and increasing, real, second component the
    value of Bessel K is exponentially decaying::

        sage: for x in [10, 20, 50, 100, 200]: print(bessel_K(5*I, x).n())              # needs sage.symbolic
        5.27812176514912e-6
        3.11005908421801e-10
        2.66182488515423e-23 - 8.59622057747552e-58*I
        4.11189776828337e-45 - 1.01494840019482e-80*I
        1.15159692553603e-88 - 6.75787862113718e-125*I

    Check whether the return value is real whenever the argument is real (:issue:`10251`)::

        sage: bessel_K(5, 1.5) in RR                                                    # needs mpmath
        True

    REFERENCES:

    - [AS-Bessel]_

    - [DLMF-Bessel]_

    - [WP-Bessel]_
    """
    def __init__(self) -> None:
        """
        See the docstring for :meth:`Function_Bessel_K`.

        EXAMPLES::

            sage: sage.functions.bessel.Function_Bessel_K()
            bessel_K
            sage: bessel_K(x, x)._sympy_()                                              # needs sympy sage.symbolic
            besselk(x, x)
        """

bessel_K: Function_Bessel_K
bessel_type_dict: dict[str, BuiltinFunction] = {'I': bessel_I, 'J': bessel_J, 'K': bessel_K, 'Y': bessel_Y}

@overload
def Bessel(order, type) -> Callable[[Incomplete], Incomplete]:
    ...
@overload
def Bessel(order, *, typ: Literal["J", "I", "K", "Y"] = "J") -> Callable[[Incomplete], Incomplete]:
    ...
@overload
def Bessel(*, typ: Literal["J", "I", "K", "Y"]="J") -> Callable[[Incomplete, Incomplete], Incomplete]:
    ...
    """
    A function factory that produces symbolic I, J, K, and Y Bessel functions.
    There are several ways to call this function:

    - ``Bessel(order, type)``
    - ``Bessel(order)`` -- type defaults to ``'J'``
    - ``Bessel(order, typ=T)``
    - ``Bessel(typ=T)`` -- order is unspecified, this is a 2-parameter
      function
    - ``Bessel()`` -- order is unspecified, type is ``'J'``

    where ``order`` can be any integer and ``T`` must be one of the strings ``'I'``,
    ``'J'``, ``'K'``, or ``'Y'``.

    See the EXAMPLES below.

    EXAMPLES:

    Construction of Bessel functions with various orders and types::

        sage: Bessel()
        bessel_J
        sage: Bessel(typ='K')
        bessel_K

        sage: # needs sage.symbolic
        sage: Bessel(1)(x)
        bessel_J(1, x)
        sage: Bessel(1, 'Y')(x)
        bessel_Y(1, x)
        sage: Bessel(-2, 'Y')(x)
        bessel_Y(-2, x)
        sage: Bessel(0, typ='I')(x)
        bessel_I(0, x)

    Evaluation::

        sage: f = Bessel(1)
        sage: f(3.0)                                                                    # needs mpmath
        0.339058958525936

        sage: # needs sage.symbolic
        sage: f(3)
        bessel_J(1, 3)
        sage: f(3).n(digits=50)
        0.33905895852593645892551459720647889697308041819801
        sage: g = Bessel(typ='J')
        sage: g(1,3)
        bessel_J(1, 3)
        sage: g(2, 3+I).n()
        0.634160370148554 + 0.0253384000032695*I
        sage: abs(numerical_integral(1/pi*cos(3*sin(x)), 0.0, pi)[0]
        ....:      - Bessel(0, 'J')(3.0)) < 1e-15
        True

    Symbolic calculus::

        sage: f(x) = Bessel(0, 'J')(x)                                                  # needs sage.symbolic
        sage: derivative(f, x)                                                          # needs sage.symbolic
        x |--> -1/2*bessel_J(1, x) + 1/2*bessel_J(-1, x)
        sage: derivative(f, x, x)                                                       # needs sage.symbolic
        x |--> 1/4*bessel_J(2, x) - 1/2*bessel_J(0, x) + 1/4*bessel_J(-2, x)

    Verify that `J_0` satisfies Bessel's differential equation numerically
    using the ``test_relation()`` method::

        sage: y = bessel_J(0, x)                                                        # needs sage.symbolic
        sage: diffeq = x^2*derivative(y,x,x) + x*derivative(y,x) + x^2*y == 0           # needs sage.symbolic
        sage: diffeq.test_relation(proof=False)                                         # needs sage.symbolic
        True

    Conversion to other systems::

        sage: # needs sage.symbolic
        sage: x,y = var('x,y')
        sage: f = Bessel(typ='K')(x,y)
        sage: expected = f.derivative(y)
        sage: actual = maxima(f).derivative('_SAGE_VAR_y').sage()
        sage: bool(actual == expected)
        True

    Compute the particular solution to Bessel's Differential Equation that
    satisfies `y(1) = 1` and `y'(1) = 1`, then verify the initial conditions
    and plot it::

        sage: # needs sage.symbolic
        sage: y = function('y')(x)
        sage: diffeq = x^2*diff(y,x,x) + x*diff(y,x) + x^2*y == 0
        sage: f = desolve(diffeq, y, [1, 1, 1]); f
        (bessel_Y(1, 1) + bessel_Y(0, 1))*bessel_J(0, x)/(bessel_J(0,
        1)*bessel_Y(1, 1) - bessel_J(1, 1)*bessel_Y(0, 1)) - (bessel_J(1,
        1) + bessel_J(0, 1))*bessel_Y(0, x)/(bessel_J(0, 1)*bessel_Y(1, 1)
        - bessel_J(1, 1)*bessel_Y(0, 1))
        sage: f.subs(x=1).n()  # numerical verification
        1.00000000000000
        sage: fp = f.diff(x)
        sage: fp.subs(x=1).n()
        1.00000000000000

        sage: f.subs(x=1).simplify_full()  # symbolic verification                      # needs sage.symbolic
        1
        sage: fp = f.diff(x)                                                            # needs sage.symbolic
        sage: fp.subs(x=1).simplify_full()                                              # needs sage.symbolic
        1

        sage: plot(f, (x,0,5))                                                          # needs sage.plot sage.symbolic
        Graphics object consisting of 1 graphics primitive

    Plotting::

        sage: f(x) = Bessel(0)(x); f                                                    # needs sage.symbolic
        x |--> bessel_J(0, x)
        sage: plot(f, (x, 1, 10))                                                       # needs sage.plot sage.symbolic
        Graphics object consisting of 1 graphics primitive

        sage: plot([Bessel(i, 'J') for i in range(5)], 2, 10)                           # needs sage.plot
        Graphics object consisting of 5 graphics primitives

        sage: G = Graphics()                                                            # needs sage.plot
        sage: G += sum(plot(Bessel(i), 0, 4*pi, rgbcolor=hue(sin(pi*i/10)))             # needs sage.plot sage.symbolic
        ....:          for i in range(5))
        sage: show(G)                                                                   # needs sage.plot

    A recreation of Abramowitz and Stegun Figure 9.1::

        sage: # needs sage.plot sage.symbolic
        sage: G  = plot(Bessel(0, 'J'), 0, 15, color='black')
        sage: G += plot(Bessel(0, 'Y'), 0, 15, color='black')
        sage: G += plot(Bessel(1, 'J'), 0, 15, color='black', linestyle='dotted')
        sage: G += plot(Bessel(1, 'Y'), 0, 15, color='black', linestyle='dotted')
        sage: show(G, ymin=-1, ymax=1)
    """

class Function_Struve_H(BuiltinFunction):
    """
    The Struve functions, solutions to the non-homogeneous Bessel differential equation:

    .. MATH::

        x^2\\frac{d^2y}{dx^2}+x\\frac{dy}{dx}+(x^2-\\alpha^2)y=\\frac{4\\bigl(\\frac{x}{2}\\bigr)^{\\alpha+1}}{\\sqrt\\pi\\Gamma(\\alpha+\\tfrac12)},

    .. MATH::

        \\mathrm{H}_\\alpha(x) = y(x)

    EXAMPLES::

        sage: struve_H(-1/2, x)                                                         # needs sage.symbolic
        sqrt(2)*sqrt(1/(pi*x))*sin(x)
        sage: struve_H(2, x)                                                            # needs sage.symbolic
        struve_H(2, x)
        sage: struve_H(1/2, pi).n()                                                     # needs sage.symbolic
        0.900316316157106

    REFERENCES:

    - [AS-Struve]_

    - [DLMF-Struve]_

    - [WP-Struve]_
    """
    def __init__(self) -> None:
        '''
        EXAMPLES::

            sage: # needs sage.symbolic
            sage: n = var(\'n\')
            sage: maxima("struve_h(n,x);").sage()
            struve_H(n, x)
            sage: struve_H(7/5, 1)._maxima_()
            struve_h(7/5,1)
            sage: loads(dumps(struve_H(n,x)))
            struve_H(n, x)
        '''

struve_H: Function_Struve_H

class Function_Struve_L(BuiltinFunction):
    """
    The modified Struve functions.

    .. MATH::

        \\mathrm{L}_\\alpha(x) = -i\\cdot e^{-\\frac{i\\alpha\\pi}{2}}\\cdot\\mathrm{H}_\\alpha(ix)

    EXAMPLES::

        sage: struve_L(2, x)                                                            # needs sage.symbolic
        struve_L(2, x)
        sage: struve_L(1/2, pi).n()                                                     # needs sage.symbolic
        4.76805417696286
        sage: diff(struve_L(1,x), x)                                                    # needs sage.symbolic
        1/3*x/pi - 1/2*struve_L(2, x) + 1/2*struve_L(0, x)

    REFERENCES:

    - [AS-Struve]_

    - [DLMF-Struve]_

    - [WP-Struve]_
    """
    def __init__(self) -> None:
        '''
        EXAMPLES::

            sage: # needs sage.symbolic
            sage: n = var(\'n\')
            sage: maxima("struve_l(n,x);").sage()
            struve_L(n, x)
            sage: struve_L(7/5, 1)._maxima_()
            struve_l(7/5,1)
            sage: loads(dumps(struve_L(n, x)))
            struve_L(n, x)
        '''

struve_L: Function_Struve_L

class Function_Hankel1(BuiltinFunction):
    """
    The Hankel function of the first kind.

    DEFINITION:

    .. MATH::

        H_\\nu^{(1)}(z) = J_{\\nu}(z) + iY_{\\nu}(z)

    EXAMPLES::

        sage: hankel1(3, x)                                                             # needs sage.symbolic
        hankel1(3, x)
        sage: hankel1(3, 4.)                                                            # needs mpmath
        0.430171473875622 - 0.182022115953485*I
        sage: latex(hankel1(3, x))                                                      # needs sage.symbolic
        H_{3}^{(1)}\\left(x\\right)
        sage: hankel1(3., x).series(x == 2, 10).subs(x=3).n()  # abs tol 1e-12          # needs sage.symbolic
        0.309062682819597 - 0.512591541605233*I
        sage: hankel1(3, 3.)                                                            # needs mpmath
        0.309062722255252 - 0.538541616105032*I

    REFERENCES:

    - [AS-Bessel]_ see 9.1.6
    """
    def __init__(self) -> None:
        """
        TESTS::

            sage: hankel1(3, x)._sympy_()                                               # needs sympy sage.symbolic
            hankel1(3, x)
        """

hankel1: Function_Hankel1

class Function_Hankel2(BuiltinFunction):
    """
    The Hankel function of the second kind.

    DEFINITION:

    .. MATH::

        H_\\nu^{(2)}(z) = J_{\\nu}(z) - iY_{\\nu}(z)

    EXAMPLES::

        sage: hankel2(3, x)                                                             # needs sage.symbolic
        hankel2(3, x)
        sage: hankel2(3, 4.)                                                            # needs mpmath
        0.430171473875622 + 0.182022115953485*I
        sage: latex(hankel2(3, x))                                                      # needs sage.symbolic
        H_{3}^{(2)}\\left(x\\right)
        sage: hankel2(3., x).series(x == 2, 10).subs(x=3).n()  # abs tol 1e-12          # needs sage.symbolic
        0.309062682819597 + 0.512591541605234*I
        sage: hankel2(3, 3.)                                                            # needs mpmath
        0.309062722255252 + 0.538541616105032*I

    REFERENCES:

    - [AS-Bessel]_ see 9.1.6
    """
    def __init__(self) -> None:
        """
        TESTS::

            sage: hankel2(3, x)._sympy_()                                               # needs sympy sage.symbolic
            hankel2(3, x)
        """

hankel2: Function_Hankel2

class SphericalBesselJ(BuiltinFunction):
    """
    The spherical Bessel function of the first kind.

    DEFINITION:

    .. MATH::

        j_n(z) = \\sqrt{\\frac{\\pi}{2z}} \\,J_{n + \\frac{1}{2}}(z)

    EXAMPLES::

        sage: spherical_bessel_J(3, 3.)                                                 # needs mpmath
        0.152051662030533
        sage: spherical_bessel_J(2.,3.)      # rel tol 1e-10                            # needs mpmath
        0.2986374970757335

        sage: # needs sage.symbolic
        sage: spherical_bessel_J(3, x)
        spherical_bessel_J(3, x)
        sage: spherical_bessel_J(3 + 0.2 * I, 3)
        0.150770999183897 - 0.0260662466510632*I
        sage: spherical_bessel_J(3, x).series(x == 2, 10).subs(x=3).n()
        0.152051648665037
        sage: spherical_bessel_J(4, x).simplify()
        -((45/x^2 - 105/x^4 - 1)*sin(x) + 5*(21/x^2 - 2)*cos(x)/x)/x
        sage: integrate(spherical_bessel_J(1,x)^2,(x,0,oo))
        1/6*pi
        sage: latex(spherical_bessel_J(4, x))
        j_{4}\\left(x\\right)

    REFERENCES:

    - [AS-Spherical]_

    - [DLMF-Bessel]_

    - [WP-Bessel]_
    """
    def __init__(self) -> None:
        """
        TESTS::

            sage: spherical_bessel_J(3, x)._sympy_()                                    # needs sympy sage.symbolic
            jn(3, x)
        """

spherical_bessel_J: SphericalBesselJ

class SphericalBesselY(BuiltinFunction):
    """
    The spherical Bessel function of the second kind.

    DEFINITION:

    .. MATH::

        y_n(z) = \\sqrt{\\frac{\\pi}{2z}} \\,Y_{n + \\frac{1}{2}}(z)

    EXAMPLES::

        sage: # needs sage.symbolic
        sage: spherical_bessel_Y(3, x)
        spherical_bessel_Y(3, x)
        sage: spherical_bessel_Y(3 + 0.2 * I, 3)
        -0.505215297588210 - 0.0508835883281404*I
        sage: spherical_bessel_Y(-3, x).simplify()
        ((3/x^2 - 1)*sin(x) - 3*cos(x)/x)/x
        sage: spherical_bessel_Y(3 + 2 * I, 5 - 0.2 * I)
        -0.270205813266440 - 0.615994702714957*I
        sage: integrate(spherical_bessel_Y(0, x), x)
        -1/2*Ei(I*x) - 1/2*Ei(-I*x)
        sage: integrate(spherical_bessel_Y(1,x)^2,(x,0,oo))
        -1/6*pi
        sage: latex(spherical_bessel_Y(0, x))
        y_{0}\\left(x\\right)

    REFERENCES:

    - [AS-Spherical]_

    - [DLMF-Bessel]_

    - [WP-Bessel]_
    """
    def __init__(self) -> None:
        """
        TESTS::

            sage: spherical_bessel_Y(3, x)._sympy_()                                    # needs sympy sage.symbolic
            yn(3, x)
        """

spherical_bessel_Y: SphericalBesselY

class SphericalHankel1(BuiltinFunction):
    """
    The spherical Hankel function of the first kind.

    DEFINITION:

    .. MATH::

        h_n^{(1)}(z) = \\sqrt{\\frac{\\pi}{2z}} \\,H_{n + \\frac{1}{2}}^{(1)}(z)

    EXAMPLES::

        sage: # needs sage.symbolic
        sage: spherical_hankel1(3, x)
        spherical_hankel1(3, x)
        sage: spherical_hankel1(3 + 0.2 * I, 3)
        0.201654587512037 - 0.531281544239273*I
        sage: spherical_hankel1(1, x).simplify()
        -(x + I)*e^(I*x)/x^2
        sage: spherical_hankel1(3 + 2 * I, 5 - 0.2 * I)
        1.25375216869913 - 0.518011435921789*I
        sage: integrate(spherical_hankel1(3, x), x)
        Ei(I*x) - 6*gamma(-1, -I*x) - 15*gamma(-2, -I*x) - 15*gamma(-3, -I*x)
        sage: latex(spherical_hankel1(3, x))
        h_{3}^{(1)}\\left(x\\right)

    REFERENCES:

    - [AS-Spherical]_

    - [DLMF-Bessel]_

    - [WP-Bessel]_
    """
    def __init__(self) -> None:
        """
        TESTS::

            sage: spherical_hankel1
            spherical_hankel1
        """

spherical_hankel1: SphericalHankel1

class SphericalHankel2(BuiltinFunction):
    """
    The spherical Hankel function of the second kind.

    DEFINITION:

    .. MATH::

        h_n^{(2)}(z) = \\sqrt{\\frac{\\pi}{2z}} \\,H_{n + \\frac{1}{2}}^{(2)}(z)

    EXAMPLES::

        sage: # needs sage.symbolic
        sage: spherical_hankel2(3, x)
        spherical_hankel2(3, x)
        sage: spherical_hankel2(3 + 0.2 * I, 3)
        0.0998874108557565 + 0.479149050937147*I
        sage: spherical_hankel2(1, x).simplify()
        -(x - I)*e^(-I*x)/x^2
        sage: spherical_hankel2(2,i).simplify()
        -e
        sage: spherical_hankel2(2,x).simplify()
        (-I*x^2 - 3*x + 3*I)*e^(-I*x)/x^3
        sage: spherical_hankel2(3 + 2*I, 5 - 0.2*I)
        0.0217627632692163 + 0.0224001906110906*I
        sage: integrate(spherical_hankel2(3, x), x)
        Ei(-I*x) - 6*gamma(-1, I*x) - 15*gamma(-2, I*x) - 15*gamma(-3, I*x)
        sage: latex(spherical_hankel2(3, x))
        h_{3}^{(2)}\\left(x\\right)

    REFERENCES:

    - [AS-Spherical]_

    - [DLMF-Bessel]_

    - [WP-Bessel]_
    """
    def __init__(self) -> None:
        """
        TESTS::

            sage: spherical_hankel2
            spherical_hankel2
        """

spherical_hankel2: SphericalHankel2

def spherical_bessel_f(F, n, z):
    """
    Numerically evaluate the spherical version, `f`, of the Bessel function `F`
    by computing `f_n(z) = \\sqrt{\\frac{1}{2}\\pi/z} F_{n + \\frac{1}{2}}(z)`.
    According to Abramowitz & Stegun, this identity holds for the Bessel
    functions `J`, `Y`, `K`, `I`, `H^{(1)}`, and `H^{(2)}`.

    EXAMPLES::

        sage: from sage.functions.bessel import spherical_bessel_f
        sage: spherical_bessel_f('besselj', 3, 4)                                       # needs mpmath
        mpf('0.22924385795503024')
        sage: spherical_bessel_f('hankel1', 3, 4)                                       # needs mpmath
        mpc(real='0.22924385795503024', imag='-0.21864196590306359')

    TESTS:

    Check that :issue:`28474` is fixed::

        sage: from sage.functions.bessel import spherical_bessel_f
        sage: spherical_bessel_f('besselj', 3, -4)                                      # needs mpmath
        mpc(real='-0.22924385795503024', imag='0.0')
        sage: spherical_bessel_f('bessely', 3, -4)                                      # needs mpmath
        mpc(real='-0.21864196590306359', imag='0.0')
    """
