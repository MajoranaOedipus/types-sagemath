r"""
Exponential integrals

AUTHORS:

- Benjamin Jones (2011-06-12)

This module provides easy access to many exponential integral
special functions. It utilizes Maxima's `special functions package`_ and
the `mpmath library`_.

REFERENCES:

- [AS1964]_ Abramowitz and Stegun: *Handbook of Mathematical Functions*
- :wikipedia:`Exponential_integral`
- Online Encyclopedia of Special Function: http://algo.inria.fr/esf/index.html
- NIST Digital Library of Mathematical Functions: https://dlmf.nist.gov/
- Maxima `special functions package`_
- `mpmath library`_

.. _`special functions package`: http://maxima.sourceforge.net/docs/manual/en/maxima_15.html
.. _`mpmath library`: https://github.com/fredrik-johansson/mpmath/

AUTHORS:

- Benjamin Jones

    Implementations of the classes ``Function_exp_integral_*``.

- David Joyner and William Stein

    Authors of the code which was moved from special.py and trans.py.
    Implementation of :meth:`exp_int` (from sage/functions/special.py).
    Implementation of :meth:`exponential_integral_1` (from
    sage/functions/transcendental.py).
"""
from _typeshed import Incomplete
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.rings.infinity import Infinity as Infinity
from sage.rings.integer_ring import ZZ as ZZ
from sage.structure.element import Expression as Expression, parent as parent
from sage.symbolic.function import BuiltinFunction as BuiltinFunction
from typings_sagemath import Real, Int

class Function_exp_integral_e(BuiltinFunction):
    """
    The generalized complex exponential integral `E_n(z)` defined by

    .. MATH::

        E_n(z) = \\int_1^{\\infty} \\frac{e^{-z t}}{t^n} \\; dt

    for complex numbers `n` and `z`, see [AS1964]_ 5.1.4.

    The special case where `n = 1` is denoted in Sage by
    ``exp_integral_e1``.

    EXAMPLES:

    Numerical evaluation is handled using mpmath::

        sage: N(exp_integral_e(1, 1))                                                   # needs sage.symbolic
        0.219383934395520
        sage: exp_integral_e(1, RealField(100)(1))                                      # needs sage.symbolic
        0.21938393439552027367716377546

    We can compare this to PARI's evaluation of
    :meth:`exponential_integral_1`::

        sage: N(exponential_integral_1(1))                                              # needs sage.symbolic
        0.219383934395520

    We can verify one case of [AS1964]_ 5.1.45, i.e.
    `E_n(z) = z^{n-1}\\Gamma(1-n,z)`::

        sage: N(exp_integral_e(2, 3+I))                                                 # needs sage.symbolic
        0.00354575823814662 - 0.00973200528288687*I
        sage: N((3+I)*gamma(-1, 3+I))                                                   # needs sage.symbolic
        0.00354575823814662 - 0.00973200528288687*I

    Maxima returns the following improper integral as a multiple of
    ``exp_integral_e(1,1)``::

        sage: uu = integral(e^(-x)*log(x+1), x, 0, oo); uu                              # needs sage.symbolic
        e*exp_integral_e(1, 1)
        sage: uu.n(digits=30)                                                           # needs sage.symbolic
        0.596347362323194074341078499369

    Symbolic derivatives and integrals are handled by Sage and Maxima::

        sage: # needs sage.symbolic
        sage: x = var('x')
        sage: f = exp_integral_e(2,x)
        sage: f.diff(x)
        -exp_integral_e(1, x)
        sage: f.integrate(x)
        -exp_integral_e(3, x)
        sage: f = exp_integral_e(-1, x)
        sage: f.integrate(x)
        Ei(-x) - gamma(-1, x)

    Some special values of ``exp_integral_e`` can be simplified.
    [AS1964]_ 5.1.23::

        sage: exp_integral_e(0, x)                                                      # needs sage.symbolic
        e^(-x)/x

    [AS1964]_ 5.1.24::

        sage: # needs sage.symbolic
        sage: exp_integral_e(6, 0)
        1/5
        sage: nn = var('nn')
        sage: assume(nn > 1)
        sage: f = exp_integral_e(nn, 0)
        sage: f.simplify()
        1/(nn - 1)


    ALGORITHM:

    Numerical evaluation is handled using mpmath, but symbolics are handled
    by Sage and Maxima.
    """
    def __init__(self) -> None:
        """
        See the docstring for :meth:`Function_exp_integral_e`.

        EXAMPLES::

            sage: exp_integral_e(1, 0)                                                  # needs sage.symbolic
            exp_integral_e(1, 0)
            sage: exp_integral_e(1, x)._sympy_()                                        # needs sage.symbolic
            expint(1, x)
        """

exp_integral_e: Function_exp_integral_e

class Function_exp_integral_e1(BuiltinFunction):
    """
    The generalized complex exponential integral `E_1(z)` defined by

    .. MATH::

        E_1(z) = \\int_z^\\infty \\frac{e^{-t}}{t} \\; dt

    see [AS1964]_ 5.1.4.

    EXAMPLES::

        sage: exp_integral_e1(x)                                                        # needs sage.symbolic
        exp_integral_e1(x)
        sage: exp_integral_e1(1.0)                                                      # needs mpmath
        0.219383934395520

    Numerical evaluation is handled using mpmath::

        sage: N(exp_integral_e1(1))                                                     # needs sage.symbolic
        0.219383934395520
        sage: exp_integral_e1(RealField(100)(1))                                        # needs sage.rings.real_mpfr
        0.21938393439552027367716377546

    We can compare this to PARI's evaluation of
    :meth:`exponential_integral_1`::

        sage: N(exp_integral_e1(2.0))                                                   # needs mpmath
        0.0489005107080611
        sage: N(exponential_integral_1(2.0))                                            # needs sage.rings.real_mpfr
        0.0489005107080611

    Symbolic derivatives and integrals are handled by Sage and Maxima::

        sage: # needs sage.symbolic
        sage: x = var('x')
        sage: f = exp_integral_e1(x)
        sage: f.diff(x)
        -e^(-x)/x
        sage: f.integrate(x)
        -exp_integral_e(2, x)

    ALGORITHM:

    Numerical evaluation is handled using mpmath, but symbolics are handled
    by Sage and Maxima.
    """
    def __init__(self) -> None:
        """
        See the docstring for :class:`Function_exp_integral_e1`.

        EXAMPLES::

            sage: exp_integral_e1(1)                                                    # needs sage.symbolic
            exp_integral_e1(1)
            sage: exp_integral_e1(x)._sympy_()                                          # needs sympy sage.symbolic
            expint(1, x)
        """

exp_integral_e1: Function_exp_integral_e1

class Function_log_integral(BuiltinFunction):
    """
    The logarithmic integral `\\operatorname{li}(z)` defined by

    .. MATH::

        \\operatorname{li}(x) = \\int_0^z \\frac{dt}{\\ln(t)} = \\operatorname{Ei}(\\ln(x))

    for x > 1 and by analytic continuation for complex arguments z (see [AS1964]_ 5.1.3).

    EXAMPLES:

    Numerical evaluation for real and complex arguments is handled using mpmath::

        sage: N(log_integral(3))                                                        # needs sage.symbolic
        2.16358859466719
        sage: N(log_integral(3), digits=30)                                             # needs sage.symbolic
        2.16358859466719197287692236735
        sage: log_integral(ComplexField(100)(3+I))                                      # needs sage.symbolic
        2.2879892769816826157078450911 + 0.87232935488528370139883806779*I
        sage: log_integral(0)                                                           # needs mpmath
        0

    Symbolic derivatives and integrals are handled by Sage and Maxima::

        sage: # needs sage.symbolic
        sage: x = var('x')
        sage: f = log_integral(x)
        sage: f.diff(x)
        1/log(x)
        sage: f.integrate(x)
        x*log_integral(x) - Ei(2*log(x))

    Here is a test from the mpmath documentation. There are
    1,925,320,391,606,803,968,923 many prime numbers less than 1e23. The
    value of ``log_integral(1e23)`` is very close to this::

        sage: log_integral(1e23)                                                        # needs mpmath
        1.92532039161405e21

    ALGORITHM:

    Numerical evaluation is handled using mpmath, but symbolics are handled
    by Sage and Maxima.

    REFERENCES:

    - :wikipedia:`Logarithmic_integral_function`
    - mpmath documentation: `logarithmic-integral`_

    .. _`logarithmic-integral`: http://mpmath.org/doc/current/functions/expintegrals.html#logarithmic-integral
    """
    def __init__(self) -> None:
        """
        See the docstring for ``Function_log_integral``.

        EXAMPLES::

            sage: log_integral(3)                                                       # needs sage.symbolic
            log_integral(3)
            sage: log_integral(x)._sympy_()                                             # needs sympy sage.symbolic
            li(x)
            sage: log_integral(x)._fricas_init_()                                       # needs sage.symbolic
            'li(x)'

        TESTS:

        Verify that :issue:`28917` is fixed::

            sage: latex(log_integral(x))                                                # needs sage.symbolic
            \\operatorname{log\\_integral}\\left(x\\right)
        """

li: Function_log_integral

log_integral: Function_log_integral

class Function_log_integral_offset(BuiltinFunction):
    '''
    The offset logarithmic integral, or Eulerian logarithmic integral,
    `\\operatorname{Li}(x)` is defined by

    .. MATH::

        \\operatorname{Li}(x) = \\int_2^x \\frac{dt}{\\ln(t)} =
        \\operatorname{li}(x)-\\operatorname{li}(2)

    for `x \\ge 2`.

    The offset logarithmic integral should also not be confused with the
    polylogarithm (also denoted by `\\operatorname{Li}(x)` ), which is
    implemented as :class:`sage.functions.log.Function_polylog`.

    `\\operatorname{Li}(x)` is identical to `\\operatorname{li}(x)` except that
    the lower limit of integration is `2` rather than `0` to avoid the
    singularity at `x = 1` of

    .. MATH::

        \\frac{1}{\\ln(t)}

    See :class:`Function_log_integral` for details of `\\operatorname{li}(x)`.
    Thus `\\operatorname{Li}(x)` can also be represented by

    .. MATH::

        \\operatorname{Li}(x) = \\operatorname{li}(x)-\\operatorname{li}(2)

    So we have::

        sage: li(4.5) - li(2.0) - Li(4.5)                                               # needs mpmath
        0.000000000000000

    `\\operatorname{Li}(x)` is extended to complex arguments `z`
    by analytic continuation (see [AS1964]_ 5.1.3)::

        sage: Li(6.6 + 5.4*I)                                                           # needs sage.symbolic
        3.97032201503632 + 2.62311237593572*I

    The function `\\operatorname{Li}` is an approximation for the number of
    primes up to `x`. In fact, the famous Riemann Hypothesis is

    .. MATH::

        |\\pi(x) - \\operatorname{Li}(x)| \\leq \\sqrt{x} \\log(x).

    For "small" `x`, `\\operatorname{Li}(x)` is always slightly bigger
    than `\\pi(x)`. However it is a theorem that there are very
    large values of `x` (e.g., around `10^{316}`), such that
    `\\exists x: \\pi(x) > \\operatorname{Li}(x)`.  See "A new bound for the
    smallest x with `\\pi(x) > \\operatorname{li}(x)`",
    Bays and Hudson, Mathematics of Computation, 69 (2000) 1285-1296.

    .. NOTE::

        Definite integration returns a part symbolic and part
        numerical result.  This is because when Li(x) is evaluated it is
        passed as li(x)-li(2).

    EXAMPLES:

    Numerical evaluation for real and complex arguments is handled using mpmath::

        sage: # needs sage.symbolic
        sage: N(log_integral_offset(3))
        1.11842481454970
        sage: N(log_integral_offset(3), digits=30)
        1.11842481454969918803233347815
        sage: log_integral_offset(ComplexField(100)(3+I))
        1.2428254968641898308632562019 + 0.87232935488528370139883806779*I
        sage: log_integral_offset(2)
        0
        sage: for n in range(1,7):                                                      # needs primecountpy
        ....:  print(\'%-10s%-10s%-20s\'%(10^n, prime_pi(10^n), N(Li(10^n))))
        10        4         5.12043572466980
        100       25        29.0809778039621
        1000      168       176.564494210035
        10000     1229      1245.09205211927
        100000    9592      9628.76383727068
        1000000   78498     78626.5039956821

    Here is a test from the mpmath documentation.
    There are 1,925,320,391,606,803,968,923 prime numbers less than 1e23.
    The value of ``log_integral_offset(1e23)`` is very close to this::

        sage: log_integral_offset(1e23)                                                 # needs mpmath
        1.92532039161405e21

    Symbolic derivatives are handled by Sage and integration by Maxima::

        sage: # needs sage.symbolic
        sage: x = var(\'x\')
        sage: f = log_integral_offset(x)
        sage: f.diff(x)
        1/log(x)
        sage: f.integrate(x)
        -x*log_integral(2) + x*log_integral(x) - Ei(2*log(x))
        sage: Li(x).integrate(x, 2.0, 4.5).n(digits=10)
        3.186411697
        sage: N(f.integrate(x, 2.0, 3.0))   # abs tol 1e-15
        0.601621785860587

    ALGORITHM:

    Numerical evaluation is handled using mpmath, but symbolics are handled
    by Sage and Maxima.

    REFERENCES:

    - :wikipedia:`Logarithmic_integral_function`
    - mpmath documentation: `logarithmic-integral`_

    .. _`logarithmic-integral`: http://mpmath.org/doc/current/functions/expintegrals.html#logarithmic-integral
    '''
    def __init__(self) -> None:
        """
        See the docstring for ``Function_log_integral_offset``.

        EXAMPLES::

            sage: log_integral_offset(3)                                                # needs sage.symbolic
            log_integral(3) - log_integral(2)
            sage: log_integral_offset(x, hold=True)._sympy_()                           # needs sympy sage.symbolic
            Li(x)

        TESTS:

        Verify that the problem described in :issue:`28917` no longer appears here::

            sage: latex(log_integral_offset)
            \\operatorname{log\\_integral\\_offset}
        """

Li: Function_log_integral_offset

log_integral_offset: Function_log_integral_offset

class Function_sin_integral(BuiltinFunction):
    """
    The trigonometric integral `\\operatorname{Si}(z)` defined by

    .. MATH::

        \\operatorname{Si}(z) = \\int_0^z \\frac{\\sin(t)}{t} \\; dt,

    see [AS1964]_ 5.2.1.

    EXAMPLES:

    Numerical evaluation for real and complex arguments is handled using mpmath::

        sage: sin_integral(0)                                                           # needs mpmath
        0
        sage: sin_integral(0.0)                                                         # needs mpmath
        0.000000000000000
        sage: sin_integral(3.0)                                                         # needs mpmath
        1.84865252799947
        sage: N(sin_integral(3), digits=30)                                             # needs sage.symbolic
        1.84865252799946825639773025111
        sage: sin_integral(ComplexField(100)(3+I))                                      # needs sage.symbolic
        2.0277151656451253616038525998 + 0.015210926166954211913653130271*I

    The alias ``Si`` can be used instead of ``sin_integral``::

        sage: Si(3.0)                                                                   # needs mpmath
        1.84865252799947

    The limit of `\\operatorname{Si}(z)` as `z \\to \\infty` is `\\pi/2`::

        sage: N(sin_integral(1e23))                                                     # needs mpmath
        1.57079632679490
        sage: N(pi/2)                                                                   # needs sage.symbolic
        1.57079632679490

    At 200 bits of precision `\\operatorname{Si}(10^{23})` agrees with `\\pi/2` up to
    `10^{-24}`::

        sage: sin_integral(RealField(200)(1e23))                                        # needs sage.rings.real_mpfr
        1.5707963267948966192313288218697837425815368604836679189519
        sage: N(pi/2, prec=200)                                                         # needs sage.symbolic
        1.5707963267948966192313216916397514420985846996875529104875

    The exponential sine integral is analytic everywhere::

        sage: sin_integral(-1.0)                                                        # needs mpmath
        -0.946083070367183
        sage: sin_integral(-2.0)                                                        # needs mpmath
        -1.60541297680269
        sage: sin_integral(-1e23)                                                       # needs mpmath
        -1.57079632679490

    Symbolic derivatives and integrals are handled by Sage and Maxima::

        sage: # needs sage.symbolic
        sage: x = var('x')
        sage: f = sin_integral(x)
        sage: f.diff(x)
        sin(x)/x
        sage: f.integrate(x)
        x*sin_integral(x) + cos(x)
        sage: integrate(sin(x)/x, x)
        -1/2*I*Ei(I*x) + 1/2*I*Ei(-I*x)


    Compare values of the functions `\\operatorname{Si}(x)` and
    `f(x) = (1/2)i \\cdot \\operatorname{Ei}(-ix) - (1/2)i \\cdot
    \\operatorname{Ei}(ix) - \\pi/2`, which are both anti-derivatives of
    `\\sin(x)/x`, at some random positive real numbers::

        sage: f(x) = 1/2*I*Ei(-I*x) - 1/2*I*Ei(I*x) - pi/2                              # needs sage.symbolic
        sage: g(x) = sin_integral(x)                                                    # needs sage.symbolic
        sage: R = [abs(RDF.random_element()) for i in range(100)]
        sage: all(abs(f(x) - g(x)) < 1e-10 for x in R)                                  # needs sage.symbolic
        True

    The Nielsen spiral is the parametric plot of (Si(t), Ci(t))::

        sage: # needs sage.symbolic
        sage: x = var('x')
        sage: f(x) = sin_integral(x)
        sage: g(x) = cos_integral(x)
        sage: P = parametric_plot([f, g], (x, 0.5 ,20))                                 # needs sage.plot
        sage: show(P, frame=True, axes=False)                                           # needs sage.plot

    ALGORITHM:

    Numerical evaluation is handled using mpmath, but symbolics are handled
    by Sage and Maxima.

    REFERENCES:

    - :wikipedia:`Trigonometric_integral`
    - mpmath documentation: `si`_

    .. _`si`: http://mpmath.org/doc/current/functions/expintegrals.html#si
    """
    def __init__(self) -> None:
        """
        See the docstring for ``Function_sin_integral``.

        EXAMPLES::

            sage: # needs sage.symbolic
            sage: sin_integral(1)
            sin_integral(1)
            sage: sin_integral(x)._sympy_()                                             # needs sympy
            Si(x)
            sage: sin_integral(x)._fricas_init_()
            'Si(x)'
            sage: sin_integral(x)._giac_()                                              # needs giac
            Si(sageVARx)
        """

Si: Function_sin_integral

sin_integral: Function_sin_integral

class Function_cos_integral(BuiltinFunction):
    """
    The trigonometric integral `\\operatorname{Ci}(z)` defined by

    .. MATH::

        \\operatorname{Ci}(z) = \\gamma + \\log(z) + \\int_0^z \\frac{\\cos(t)-1}{t} \\; dt,

    where `\\gamma` is the Euler gamma constant (``euler_gamma`` in Sage),
    see [AS1964]_ 5.2.1.

    EXAMPLES::

        sage: z = var('z')                                                              # needs sage.symbolic
        sage: cos_integral(z)                                                           # needs sage.symbolic
        cos_integral(z)
        sage: cos_integral(3.0)                                                         # needs mpmath
        0.119629786008000
        sage: cos_integral(0)                                                           # needs sage.symbolic
        cos_integral(0)
        sage: N(cos_integral(0))                                                        # needs mpmath
        -infinity

    Numerical evaluation for real and complex arguments is handled using mpmath::

        sage: cos_integral(3.0)                                                         # needs mpmath
        0.119629786008000

    The alias ``Ci`` can be used instead of ``cos_integral``::

        sage: Ci(3.0)                                                                   # needs mpmath
        0.119629786008000

    Compare ``cos_integral(3.0)`` to the definition of the value using
    numerical integration::

        sage: a = numerical_integral((cos(x)-1)/x, 0, 3)[0]                             # needs sage.symbolic
        sage: abs(N(euler_gamma + log(3)) + a - N(cos_integral(3.0))) < 1e-14           # needs sage.symbolic
        True

    Arbitrary precision and complex arguments are handled::

        sage: N(cos_integral(3), digits=30)                                             # needs sage.symbolic
        0.119629786008000327626472281177
        sage: cos_integral(ComplexField(100)(3+I))                                      # needs sage.symbolic
        0.078134230477495714401983633057 - 0.37814733904787920181190368789*I

    The limit `\\operatorname{Ci}(z)` as `z \\to \\infty` is zero::

        sage: N(cos_integral(1e23))                                                     # needs mpmath
        -3.24053937643003e-24

    Symbolic derivatives and integrals are handled by Sage and Maxima::

        sage: # needs sage.symbolic
        sage: x = var('x')
        sage: f = cos_integral(x)
        sage: f.diff(x)
        cos(x)/x
        sage: f.integrate(x)
        x*cos_integral(x) - sin(x)

    The Nielsen spiral is the parametric plot of (Si(t), Ci(t))::

        sage: # needs sage.symbolic
        sage: t = var('t')
        sage: f(t) = sin_integral(t)
        sage: g(t) = cos_integral(t)
        sage: P = parametric_plot([f, g], (t, 0.5 ,20))                                 # needs sage.plot
        sage: show(P, frame=True, axes=False)                                           # needs sage.plot

    ALGORITHM:

    Numerical evaluation is handled using mpmath, but symbolics are handled
    by Sage and Maxima.

    REFERENCES:

    - :wikipedia:`Trigonometric_integral`
    - mpmath documentation: `ci`_

    .. _`ci`: http://mpmath.org/doc/current/functions/expintegrals.html#ci
    """
    def __init__(self) -> None:
        """
        See the docstring for :class:`Function_cos_integral`.

        EXAMPLES::

            sage: # needs sage.symbolic
            sage: cos_integral(1)
            cos_integral(1)
            sage: cos_integral(x)._sympy_()                                             # needs sympy
            Ci(x)
            sage: cos_integral(x)._fricas_init_()
            'Ci(x)'
            sage: cos_integral(x)._giac_()                                              # needs giac
            Ci(sageVARx)
        """

Ci: Function_cos_integral

cos_integral: Function_cos_integral

class Function_sinh_integral(BuiltinFunction):
    """
    The trigonometric integral `\\operatorname{Shi}(z)` defined by

    .. MATH::

        \\operatorname{Shi}(z) = \\int_0^z \\frac{\\sinh(t)}{t} \\; dt,

    see [AS1964]_ 5.2.3.

    EXAMPLES:

    Numerical evaluation for real and complex arguments is handled using mpmath::

        sage: sinh_integral(3.0)                                                        # needs mpmath
        4.97344047585981
        sage: sinh_integral(1.0)                                                        # needs mpmath
        1.05725087537573
        sage: sinh_integral(-1.0)                                                       # needs mpmath
        -1.05725087537573

    The alias ``Shi`` can be used instead of ``sinh_integral``::

        sage: Shi(3.0)                                                                  # needs mpmath
        4.97344047585981

    Compare ``sinh_integral(3.0)`` to the definition of the value using
    numerical integration::

        sage: a = numerical_integral(sinh(x)/x, 0, 3)[0]                                # needs sage.symbolic
        sage: abs(a - N(sinh_integral(3))) < 1e-14                                      # needs sage.symbolic
        True

    Arbitrary precision and complex arguments are handled::

        sage: N(sinh_integral(3), digits=30)                                            # needs sage.symbolic
        4.97344047585980679771041838252
        sage: sinh_integral(ComplexField(100)(3+I))                                     # needs sage.symbolic
        3.9134623660329374406788354078 + 3.0427678212908839256360163759*I

    The limit `\\operatorname{Shi}(z)` as `z \\to \\infty` is `\\infty`::

        sage: N(sinh_integral(Infinity))                                                # needs mpmath
        +infinity

    Symbolic derivatives and integrals are handled by Sage and Maxima::

        sage: x = var('x')                                                              # needs sage.symbolic
        sage: f = sinh_integral(x)                                                      # needs sage.symbolic
        sage: f.diff(x)                                                                 # needs sage.symbolic
        sinh(x)/x

        sage: f.integrate(x)                                                            # needs sage.symbolic
        x*sinh_integral(x) - cosh(x)

    Note that due to some problems with the way Maxima handles these
    expressions, definite integrals can sometimes give unexpected
    results (typically when using inexact endpoints) due to
    inconsistent branching::

        sage: integrate(sinh_integral(x), x, 0, 1/2)                                    # needs sage.symbolic
        -cosh(1/2) + 1/2*sinh_integral(1/2) + 1
        sage: integrate(sinh_integral(x), x, 0, 1/2).n()  # correct                     # needs sage.symbolic
        0.125872409703453
        sage: integrate(sinh_integral(x), x, 0, 0.5).n()  # fixed in maxima 5.29.1      # needs sage.symbolic
        0.125872409703453

    ALGORITHM:

    Numerical evaluation is handled using mpmath, but symbolics are handled
    by Sage and Maxima.

    REFERENCES:

    - :wikipedia:`Trigonometric_integral`
    - mpmath documentation: `shi`_

    .. _`shi`: http://mpmath.org/doc/current/functions/expintegrals.html#shi
    """
    def __init__(self) -> None:
        """
        See the docstring for ``Function_sinh_integral``.

        EXAMPLES::

            sage: sinh_integral(1)                                                      # needs sage.symbolic
            sinh_integral(1)
            sage: sinh_integral(x)._sympy_()                                            # needs sympy sage.symbolic
            Shi(x)
        """

Shi: Function_sinh_integral

sinh_integral: Function_sinh_integral

class Function_cosh_integral(BuiltinFunction):
    """
    The trigonometric integral `\\operatorname{Chi}(z)` defined by

    .. MATH::

        \\operatorname{Chi}(z) = \\gamma + \\log(z) + \\int_0^z \\frac{\\cosh(t)-1}{t} \\; dt,

    see [AS1964]_ 5.2.4.

    EXAMPLES::

        sage: z = var('z')                                                              # needs sage.symbolic
        sage: cosh_integral(z)                                                          # needs sage.symbolic
        cosh_integral(z)
        sage: cosh_integral(3.0)                                                        # needs mpmath
        4.96039209476561

    Numerical evaluation for real and complex arguments is handled using mpmath::

        sage: cosh_integral(1.0)                                                        # needs mpmath
        0.837866940980208

    The alias ``Chi`` can be used instead of ``cosh_integral``::

        sage: Chi(1.0)                                                                  # needs mpmath
        0.837866940980208

    Here is an example from the mpmath documentation::

        sage: f(x) = cosh_integral(x)                                                   # needs sage.symbolic
        sage: find_root(f, 0.1, 1.0)                                                    # needs scipy sage.symbolic
        0.523822571389...

    Compare ``cosh_integral(3.0)`` to the definition of the value using
    numerical integration::

        sage: a = numerical_integral((cosh(x)-1)/x, 0, 3)[0]                            # needs sage.symbolic
        sage: abs(N(euler_gamma + log(3)) + a - N(cosh_integral(3.0))) < 1e-14          # needs sage.symbolic
        True

    Arbitrary precision and complex arguments are handled::

        sage: N(cosh_integral(3), digits=30)                                            # needs sage.symbolic
        4.96039209476560976029791763669
        sage: cosh_integral(ComplexField(100)(3+I))                                     # needs sage.symbolic
        3.9096723099686417127843516794 + 3.0547519627014217273323873274*I

    The limit of `\\operatorname{Chi}(z)` as `z \\to \\infty` is `\\infty`::

        sage: N(cosh_integral(Infinity))                                                # needs mpmath
        +infinity

    Symbolic derivatives and integrals are handled by Sage and Maxima::

        sage: # needs sage.symbolic
        sage: x = var('x')
        sage: f = cosh_integral(x)
        sage: f.diff(x)
        cosh(x)/x
        sage: f.integrate(x)
        x*cosh_integral(x) - sinh(x)

    ALGORITHM:

    Numerical evaluation is handled using mpmath, but symbolics are handled
    by Sage and Maxima.

    REFERENCES:

    - :wikipedia:`Trigonometric_integral`
    - mpmath documentation: `chi`_

    .. _`chi`: http://mpmath.org/doc/current/functions/expintegrals.html#chi
    """
    def __init__(self) -> None:
        """
        See the docstring for ``Function_cosh_integral``.

        EXAMPLES::

            sage: cosh_integral(1)                                                      # needs sage.symbolic
            cosh_integral(1)
            sage: cosh_integral(x)._sympy_()                                            # needs sage.symbolic
            Chi(x)
        """

Chi: Function_cosh_integral

cosh_integral: Function_cosh_integral

class Function_exp_integral(BuiltinFunction):
    """
    The generalized complex exponential integral Ei(z) defined by

    .. MATH::

        \\operatorname{Ei}(x) = \\int_{-\\infty}^x \\frac{e^t}{t} \\; dt

    for x > 0 and for complex arguments by analytic continuation,
    see [AS1964]_ 5.1.2.

    EXAMPLES::

        sage: # needs sage.symbolic
        sage: Ei(10)
        Ei(10)
        sage: Ei(I)
        Ei(I)
        sage: Ei(3+I)
        Ei(I + 3)
        sage: Ei(10r)
        Ei(10)

        sage: Ei(1.3)                                                                   # needs mpmath
        2.72139888023202
        sage: Ei(1.3r)                                                                  # needs mpmath
        2.7213988802320235

    The branch cut for this function is along the negative real axis::

        sage: Ei(-3 + 0.1*I)                                                            # needs sage.symbolic
        -0.0129379427181693 + 3.13993830250942*I
        sage: Ei(-3 - 0.1*I)                                                            # needs sage.symbolic
        -0.0129379427181693 - 3.13993830250942*I

    The precision for the result is deduced from the precision of the
    input. Convert the input to a higher precision explicitly if a
    result with higher precision is desired::

        sage: Ei(RealField(300)(1.1))                                                   # needs sage.rings.real_mpfr
        2.16737827956340282358378734233807621497112737591639704719499002090327541763352339357795426

    ALGORITHM: Uses mpmath.

    TESTS:

    Show that the evaluation and limit issue in :issue:`13271` is fixed::

        sage: # needs sage.symbolic
        sage: var('Z')
        Z
        sage: (Ei(-Z)).limit(Z=oo)
        0
        sage: (Ei(-Z)).limit(Z=1000)
        Ei(-1000)
        sage: (Ei(-Z)).limit(Z=1000).n()
        -5.07089306023517e-438
    """
    def __init__(self) -> None:
        """
        TESTS::

            sage: Ei(10)                                                                # needs sage.symbolic
            Ei(10)
            sage: Ei(x)._sympy_()                                                       # needs sympy sage.symbolic
            Ei(x)
        """

Ei: Function_exp_integral

exp_integral_ei: Function_exp_integral


def exponential_integral_1(x: Real | Expression, n: Int = 0) -> Real :
    '''
    Return the exponential integral `E_1(x)`. If the optional
    argument `n` is given, computes list of the first
    `n` values of the exponential integral
    `E_1(x m)`.

    The exponential integral `E_1(x)` is

    .. MATH::

                      E_1(x) = \\int_{x}^{\\infty} \\frac{e^{-t}}{t} \\; dt

    INPUT:

    - ``x`` -- a positive real number

    - ``n`` -- (default: 0) a nonnegative integer; if
      nonzero, then return a list of values ``E_1(x*m)`` for m =
      1,2,3,...,n. This is useful, e.g., when computing derivatives of
      `L`-functions.

    OUTPUT:

    A real number if n is 0 (the default) or a list of reals if n > 0.
    The precision is the same as the input, with a default of 53 bits
    in case the input is exact.

    EXAMPLES::

        sage: # needs sage.libs.pari sage.rings.real_mpfr
        sage: exponential_integral_1(2)
        0.0489005107080611
        sage: exponential_integral_1(2, 4)  # abs tol 1e-18
        [0.0489005107080611, 0.00377935240984891, 0.000360082452162659, 0.0000376656228439245]
        sage: exponential_integral_1(40, 5)
        [0.000000000000000, 2.22854325868847e-37, 6.33732515501151e-55,
         2.02336191509997e-72, 6.88522610630764e-90]
        sage: r = exponential_integral_1(RealField(150)(1)); r
        0.21938393439552027367716377546012164903104729
        sage: parent(r)
        Real Field with 150 bits of precision
        sage: exponential_integral_1(RealField(150)(100))
        3.6835977616820321802351926205081189876552201e-46

        sage: exponential_integral_1(0)
        +Infinity

    TESTS:

    The relative error for a single value should be less than 1 ulp::

        sage: for prec in [20..1000]:           # long time (22s on sage.math, 2013), needs sage.libs.pari
        ....:     R = RealField(prec)
        ....:     S = RealField(prec+64)
        ....:     for t in range(8):  # Try 8 values for each precision
        ....:         a = R.random_element(-15,10).exp()
        ....:         x = exponential_integral_1(a)
        ....:         y = exponential_integral_1(S(a))
        ....:         e = float(abs(S(x) - y)/x.ulp())
        ....:         if e >= 1.0:
        ....:             print("exponential_integral_1(%s) with precision %s has error of %s ulp"%(a, prec, e))

    The absolute error for a vector should be less than `2^{-p} c`, where
    `p` is the precision in bits of `x` and `c = 2` ``max(1, exponential_integral_1(x))``::

        sage: for prec in [20..128]:            # long time (15s on sage.math, 2013), needs sage.libs.pari
        ....:     R = RealField(prec)
        ....:     S = RealField(prec+64)
        ....:     a = R.random_element(-15,10).exp()
        ....:     n = 2^ZZ.random_element(14)
        ....:     x = exponential_integral_1(a, n)
        ....:     y = exponential_integral_1(S(a), n)
        ....:     c = RDF(4 * max(1.0, y[0]))
        ....:     for i in range(n):
        ....:         e = float(abs(S(x[i]) - y[i]) << prec)
        ....:         if e >= c:
        ....:             print("exponential_integral_1(%s, %s)[%s] with precision %s has error of %s >= %s"%(a, n, i, prec, e, c))

    ALGORITHM: use the PARI C-library function :pari:`eint1`.

    REFERENCE:

    - See Proposition 5.6.12 of Cohen\'s book "A Course in
      Computational Algebraic Number Theory".
    '''
