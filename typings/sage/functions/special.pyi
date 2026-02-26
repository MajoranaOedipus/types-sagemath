r"""
Miscellaneous special functions

This module provides easy access to many of Maxima and PARI's
special functions.

Maxima's special functions package (which includes spherical
harmonic functions, spherical Bessel functions (of the 1st and 2nd
kind), and spherical Hankel functions (of the 1st and 2nd kind))
was written by Barton Willis of the University of Nebraska at
Kearney. It is released under the terms of the General Public
License (GPL).

Support for elliptic functions and integrals was written by Raymond
Toy. It is placed under the terms of the General Public License
(GPL) that governs the distribution of Maxima.

Next, we summarize some of the properties of the functions
implemented here.

- **Spherical harmonics**: Laplace's equation in spherical coordinates is:

    .. MATH::

        \frac{1}{r^2} \frac{\partial}{\partial r}
        \left( r^2 \frac{\partial f}{\partial r} \right) +
        \frac{1}{r^2\sin\theta} \frac{\partial}{\partial \theta}
        \left( \sin\theta \frac{\partial f}{\partial \theta} \right) +
        \frac{1}{r^2\sin^2\theta} \frac{\partial^2 f}{\partial \varphi^2} = 0.

  Note that the spherical coordinates `\theta` and `\varphi` are defined here
  as follows: `\theta` is the colatitude or polar angle, ranging from
  `0\leq\theta\leq\pi` and `\varphi` the azimuth or longitude, ranging from
  `0\leq\varphi<2\pi`.

  The general solution which remains finite towards infinity is a linear
  combination of functions of the form

    .. MATH::

        r^{-1-\ell} \cos (m \varphi) P_\ell^m (\cos{\theta} )

   and

    .. MATH::

        r^{-1-\ell} \sin (m \varphi) P_\ell^m (\cos{\theta} )

  where `P_\ell^m` are the associated Legendre polynomials
  (cf. :class:`~sage.functions.orthogonal_polys.Func_assoc_legendre_P`),
  and with integer parameters `\ell \ge 0` and `m` from `0` to `\ell`. Put in
  another way, the solutions with integer parameters `\ell \ge 0` and
  `- \ell\leq m\leq \ell`, can be written as linear combinations of:

    .. MATH::

        U_{\ell,m}(r,\theta , \varphi ) =
        r^{-1-\ell} Y_\ell^m( \theta , \varphi )

  where the functions `Y` are the spherical harmonic functions with
  parameters `\ell`, `m`, which can be written as:

    .. MATH::

        Y_\ell^m( \theta , \varphi ) =
        \sqrt{ \frac{(2\ell+1)}{4\pi} \frac{(\ell-m)!}{(\ell+m)!} }
        \, e^{i m \varphi } \, P_\ell^m ( \cos{\theta} ) .

  The spherical harmonics obey the normalisation condition

    .. MATH::

        \int_{\theta=0}^\pi\int_{\varphi=0}^{2\pi}
        Y_\ell^mY_{\ell'}^{m'*}\,d\Omega =
        \delta_{\ell\ell'}\delta_{mm'}\quad\quad d\Omega =
        \sin\theta\,d\varphi\,d\theta .

- The **incomplete elliptic integrals** (of the first kind, etc.) are:

    .. MATH::

        \begin{array}{c}
        \displaystyle\int_0^\phi \frac{1}{\sqrt{1 - m\sin(x)^2}}\, dx,\\
        \displaystyle\int_0^\phi \sqrt{1 - m\sin(x)^2}\, dx,\\
        \displaystyle\int_0^\phi \frac{\sqrt{1-mt^2}}{\sqrt(1 - t^2)}\, dx,\\
        \displaystyle\int_0^\phi
        \frac{1}{\sqrt{1 - m\sin(x)^2\sqrt{1 - n\sin(x)^2}}}\, dx,
        \end{array}

  and the complete ones are obtained by taking `\phi =\pi/2`.

.. WARNING::

    SciPy's versions are poorly documented and seem less accurate than the
    Maxima and PARI versions. Typically they are limited by hardware floats
    precision.

REFERENCES:

- Abramowitz and Stegun: *Handbook of Mathematical Functions* [AS1964]_

- :wikipedia:`Spherical_harmonics`

- :wikipedia:`Helmholtz_equation`

- `Online Encyclopedia of Special Functions
  <http://algo.inria.fr/esf/index.html>`_

AUTHORS:

- David Joyner (2006-13-06): initial version

- David Joyner (2006-30-10): bug fixes to pari wrappers of Bessel
  functions, hypergeometric_U

- William Stein (2008-02): Impose some sanity checks.

- David Joyner (2008-02-16): optional calls to scipy and replace all ``#random`` by ``...``

- David Joyner (2008-04-23): addition of elliptic integrals

- Eviatar Bach (2013): making elliptic integrals symbolic

- Eric Gourgoulhon (2022): add Condon-Shortley phase to spherical harmonics
"""
from typings_sagemath import FiniteNum, Real
from sage.rings.complex_mpfr import ComplexNumber
from sage.misc.functional import sqrt as sqrt
from sage.libs.mpmath.all import mpf
from sage.rings.integer import Integer as Integer
from sage.rings.integer_ring import ZZ as ZZ
from sage.symbolic.function import BuiltinFunction as BuiltinFunction

class SphericalHarmonic(BuiltinFunction):
    '''
    Return the spherical harmonic function `Y_n^m(\\theta, \\varphi)`.

    For integers `n > -1`, `|m| \\leq n`, simplification is done automatically.
    Numeric evaluation is supported for complex `n` and `m`.

    EXAMPLES::

        sage: # needs sage.symbolic
        sage: x, y = var(\'x, y\')
        sage: spherical_harmonic(3, 2, x, y)
        1/8*sqrt(30)*sqrt(7)*cos(x)*e^(2*I*y)*sin(x)^2/sqrt(pi)
        sage: spherical_harmonic(3, 2, 1, 2)
        1/8*sqrt(30)*sqrt(7)*cos(1)*e^(4*I)*sin(1)^2/sqrt(pi)
        sage: spherical_harmonic(3 + I, 2., 1, 2)
        -0.351154337307488 - 0.415562233975369*I
        sage: latex(spherical_harmonic(3, 2, x, y, hold=True))
        Y_{3}^{2}\\left(x, y\\right)
        sage: spherical_harmonic(1, 2, x, y)
        0

    The degree `n` and the order `m` can be symbolic::

        sage: # needs sage.symbolic
        sage: n, m = var(\'n m\')
        sage: spherical_harmonic(n, m, x, y)
        spherical_harmonic(n, m, x, y)
        sage: latex(spherical_harmonic(n, m, x, y))
        Y_{n}^{m}\\left(x, y\\right)
        sage: diff(spherical_harmonic(n, m, x, y), x)
        m*cot(x)*spherical_harmonic(n, m, x, y)
         + sqrt(-(m + n + 1)*(m - n))*e^(-I*y)*spherical_harmonic(n, m + 1, x, y)
        sage: diff(spherical_harmonic(n, m, x, y), y)
        I*m*spherical_harmonic(n, m, x, y)

    The convention regarding the Condon-Shortley phase `(-1)^m` is the same
    as for SymPy\'s spherical harmonics and :wikipedia:`Spherical_harmonics`::

        sage: # needs sage.symbolic
        sage: spherical_harmonic(1, 1, x, y)
        -1/4*sqrt(3)*sqrt(2)*e^(I*y)*sin(x)/sqrt(pi)
        sage: from sympy import Ynm                                                     # needs sympy
        sage: Ynm(1, 1, x, y).expand(func=True)                                         # needs sympy
        -sqrt(6)*exp(I*y)*sin(x)/(4*sqrt(pi))
        sage: spherical_harmonic(1, 1, x, y) - Ynm(1, 1, x, y)                          # needs sympy
        0

    It also agrees with SciPy\'s spherical harmonics::

        sage: spherical_harmonic(1, 1, pi/2, pi).n()  # abs tol 1e-14                   # needs sage.symbolic
        0.345494149471335
        sage: import numpy as np                                                        # needs scipy
        sage: if int(np.version.short_version[0]) > 1:                                  # needs scipy
        ....:     _ = np.set_printoptions(legacy="1.25")                                # needs scipy
        sage: import scipy.version
        sage: if scipy.version.version < \'1.15.0\':
        ....:     from scipy.special import sph_harm # NB: arguments x and y are swapped   # needs scipy
        ....:     sph_harm(1, 1, pi.n(), (pi/2).n())  # abs tol 1e-14                   # needs scipy sage.symbolic
        ....: else:
        ....:     from scipy.special import sph_harm_y                                  # needs scipy
        ....:     sph_harm_y(1, 1, (pi/2).n(), pi.n()).item()  # abs tol 1e-9           # needs scipy sage.symbolic
        (0.3454941494713355-4.231083042742082e-17j)

    Note that this convention differs from the one in Maxima, as revealed by
    the sign difference for odd values of `m`::

        sage: maxima.spherical_harmonic(1, 1, x, y).sage()                              # needs sage.symbolic
        1/2*sqrt(3/2)*e^(I*y)*sin(x)/sqrt(pi)

    It follows that, contrary to Maxima, SageMath uses the same sign convention
    for spherical harmonics as SymPy, SciPy, Mathematica and
    :wikipedia:`Table_of_spherical_harmonics`.

    REFERENCES:

    - :wikipedia:`Spherical_harmonics`
    '''
    def __init__(self) -> None:
        """
        TESTS::

            sage: n, m, theta, phi = var('n m theta phi')                               # needs sage.symbolic
            sage: spherical_harmonic(n, m, theta, phi)._sympy_()                        # needs sympy sage.symbolic
            Ynm(n, m, theta, phi)
        """

spherical_harmonic: SphericalHarmonic

def elliptic_j(z: FiniteNum, prec: int = 53) -> ComplexNumber:
    """
    Return the elliptic modular `j`-function evaluated at `z`.

    INPUT:

    - ``z`` -- complex; a complex number with positive imaginary part

    - ``prec`` -- (default: 53) precision in bits for the complex field

    OUTPUT: (complex) the value of `j(z)`

    ALGORITHM:

    Calls the ``pari`` function ``ellj()``.

    AUTHOR:

    John Cremona

    EXAMPLES::

        sage: elliptic_j(CC(i))                                                         # needs sage.rings.real_mpfr
        1728.00000000000
        sage: elliptic_j(sqrt(-2.0))                                                    # needs sage.rings.complex_double
        8000.00000000000
        sage: z = ComplexField(100)(1, sqrt(11))/2                                      # needs sage.rings.real_mpfr sage.symbolic
        sage: elliptic_j(z)                                                             # needs sage.rings.real_mpfr sage.symbolic
        -32768.000...
        sage: elliptic_j(z).real().round()                                              # needs sage.rings.real_mpfr sage.symbolic
        -32768

    ::

        sage: tau = (1 + sqrt(-163))/2                                                  # needs sage.symbolic
        sage: (-elliptic_j(tau.n(100)).real().round())^(1/3)                            # needs sage.symbolic
        640320

    This example shows the need for higher precision than the default one of
    the `ComplexField`, see :issue:`28355`::

        sage: # needs sage.symbolic
        sage: -elliptic_j(tau)  # rel tol 1e-2
        2.62537412640767e17 - 732.558854258998*I
        sage: -elliptic_j(tau, 75)  # rel tol 1e-2
        2.625374126407680000000e17 - 0.0001309913593909879441262*I
        sage: -elliptic_j(tau, 100)  # rel tol 1e-2
        2.6253741264076799999999999999e17 - 1.3012822400356887122945119790e-12*I
        sage: (-elliptic_j(tau, 100).real().round())^(1/3)
        640320
    """

class EllipticE(BuiltinFunction):
    '''
    Return the incomplete elliptic integral of the
    second kind:

    .. MATH::

        E(\\varphi\\,|\\,m)=\\int_0^\\varphi \\sqrt{1 - m\\sin(x)^2}\\, dx.

    EXAMPLES::

        sage: z = var("z")                                                              # needs sage.symbolic
        sage: elliptic_e(z, 1)                                                          # needs sage.symbolic
        elliptic_e(z, 1)
        sage: elliptic_e(z, 1).simplify()       # not tested                            # needs sage.symbolic
        2*round(z/pi) - sin(pi*round(z/pi) - z)
        sage: elliptic_e(z, 0)                                                          # needs sage.symbolic
        z
        sage: elliptic_e(0.5, 0.1)  # abs tol 2e-15                                     # needs mpmath
        0.498011394498832
        sage: elliptic_e(1/2, 1/10).n(200)                                              # needs sage.symbolic
        0.4980113944988315331154610406...

    .. SEEALSO::

        - Taking `\\varphi = \\pi/2` gives
          :func:`elliptic_ec()<sage.functions.special.EllipticEC>`.

        - Taking `\\varphi = \\operatorname{arc\\,sin}(\\operatorname{sn}(u,m))`
          gives :func:`elliptic_eu()<sage.functions.special.EllipticEU>`.

    REFERENCES:

    - :wikipedia:`Elliptic_integral#Incomplete_elliptic_integral_of_the_second_kind`

    - :wikipedia:`Jacobi_elliptic_functions`
    '''
    def __init__(self) -> None:
        '''
        TESTS::

            sage: loads(dumps(elliptic_e))
            elliptic_e
            sage: elliptic_e(x, x)._sympy_()                                            # needs sympy sage.symbolic
            elliptic_e(x, x)

        Check that :issue:`34085` is fixed::

            sage: _ = var("x y")                                                        # needs sage.symbolic
            sage: fricas(elliptic_e(x, y))                                          # optional - fricas, needs sage.symbolic
            ellipticE(sin(x),y)

        However, the conversion is only correct in the interval
        `[-\\pi/2, \\pi/2]`::

            sage: fricas(elliptic_e(x, y)).D(x).sage()/elliptic_e(x, y).diff(x)     # optional - fricas, needs sage.symbolic
            cos(x)/sqrt(-sin(x)^2 + 1)

        Numerically::

            sage: f = lambda x, y: elliptic_e(arcsin(x), y).subs(x=x, y=y)
            sage: g = lambda x, y: fricas.ellipticE(x, y).sage()
            sage: d = lambda x, y: f(x, y) - g(x, y)
            sage: [d(N(-pi/2 + x), y)                           # abs tol 1e-8      # optional - fricas, needs sage.symbolic
            ....:  for x in range(1, 3) for y in range(-2, 2)]
            [0.000000000000000,
             0.000000000000000,
             0.000000000000000,
             0.000000000000000,
             5.55111512312578e-17,
             0.000000000000000,
             0.000000000000000,
             0.000000000000000]
        '''

elliptic_e: EllipticE

class EllipticEC(BuiltinFunction):
    """
    Return the complete elliptic integral of the second kind:

    .. MATH::

        E(m)=\\int_0^{\\pi/2} \\sqrt{1 - m\\sin(x)^2}\\, dx.

    EXAMPLES::

        sage: elliptic_ec(0.1)                                                          # needs mpmath
        1.53075763689776
        sage: elliptic_ec(x).diff()                                                     # needs sage.symbolic
        1/2*(elliptic_ec(x) - elliptic_kc(x))/x

    .. SEEALSO::

        - :func:`elliptic_e()<sage.functions.special.EllipticE>`.

    REFERENCES:

    - :wikipedia:`Elliptic_integral#Complete_elliptic_integral_of_the_second_kind`
    """
    def __init__(self) -> None:
        """
        EXAMPLES::

            sage: loads(dumps(elliptic_ec))
            elliptic_ec
            sage: elliptic_ec(x)._sympy_()                                              # needs sage.symbolic
            elliptic_e(x)

        TESTS::

            sage: fricas(elliptic_ec(x))                                        # optional - fricas, needs sage.symbolic
            ellipticE(x)

            sage: elliptic_ec(0.5)  # abs tol 1e-8                                      # needs sage.symbolic
            1.35064388104768
            sage: fricas.ellipticE(0.5).sage()  # abs tol 1e-8                  # optional - fricas, needs sage.symbolic
            1.3506438810476755025201749
        """

elliptic_ec: EllipticEC

class EllipticEU(BuiltinFunction):
    """
    Return Jacobi's form of the incomplete elliptic integral of the second kind:

    .. MATH::

        E(u,m)=
        \\int_0^u \\mathrm{dn}(x,m)^2\\, dx = \\int_0^\\tau
        \\frac{\\sqrt{1-m x^2}}{\\sqrt{1-x^2}}\\, dx.

    where `\\tau = \\mathrm{sn}(u, m)`.

    Also, ``elliptic_eu(u, m) = elliptic_e(asin(sn(u,m)),m)``.

    EXAMPLES::

        sage: elliptic_eu(0.5, 0.1)                                                     # needs mpmath
        0.496054551286597

    .. SEEALSO::

        - :func:`elliptic_e()<sage.functions.special.EllipticE>`.

    REFERENCES:

    - :wikipedia:`Elliptic_integral#Incomplete_elliptic_integral_of_the_second_kind`

    - :wikipedia:`Jacobi_elliptic_functions`
    """
    def __init__(self) -> None:
        """
        EXAMPLES::

            sage: loads(dumps(elliptic_eu))
            elliptic_eu
        """

def elliptic_eu_f(u: Real, m: Real) -> mpf:
    """
    Internal function for numeric evaluation of ``elliptic_eu``, defined as
    `E\\left(\\operatorname{am}(u, m)|m\\right)`, where `E` is the incomplete
    elliptic integral of the second kind and `\\operatorname{am}` is the Jacobi
    amplitude function.

    EXAMPLES::

        sage: from sage.functions.special import elliptic_eu_f
        sage: elliptic_eu_f(0.5, 0.1)                                                   # needs mpmath
        mpf('0.49605455128659691')
    """

elliptic_eu: EllipticEU

class EllipticF(BuiltinFunction):
    '''
    Return the incomplete elliptic integral of the first kind.

    .. MATH::

        F(\\varphi\\,|\\,m)=\\int_0^\\varphi \\frac{dx}{\\sqrt{1 - m\\sin(x)^2}},

    Taking `\\varphi = \\pi/2` gives
    :func:`elliptic_kc()<sage.functions.special.EllipticKC>`.

    EXAMPLES::

        sage: z = var("z")                                                              # needs sage.symbolic
        sage: elliptic_f(z, 0)                                                          # needs sage.symbolic
        z
        sage: elliptic_f(z, 1).simplify()                                               # needs sage.symbolic
        log(tan(1/4*pi + 1/2*z))
        sage: elliptic_f(0.2, 0.1)                                                      # needs mpmath
        0.200132506747543

    .. SEEALSO::

        - :func:`elliptic_e()<sage.functions.special.EllipticE>`.

    REFERENCES:

    - :wikipedia:`Elliptic_integral#Incomplete_elliptic_integral_of_the_first_kind`
    '''
    def __init__(self) -> None:
        '''
        EXAMPLES::

            sage: loads(dumps(elliptic_f))
            elliptic_f
            sage: elliptic_f(x, 2)._sympy_()                                            # needs sympy sage.symbolic
            elliptic_f(x, 2)

        Check that :issue:`34186` is fixed::

            sage: _ = var("x y")                                                        # needs sage.symbolic
            sage: fricas(elliptic_f(x, y))                                          # optional - fricas, needs sage.symbolic
            ellipticF(sin(x),y)

        However, the conversion is only correct in the interval
        `[-\\pi/2, \\pi/2]`::

            sage: fricas(elliptic_f(x, y)).D(x).sage()/elliptic_f(x, y).diff(x)     # optional - fricas, needs sage.symbolic
            cos(x)/sqrt(-sin(x)^2 + 1)

        Numerically::

            sage: f = lambda x, y: elliptic_f(arcsin(x), y).subs(x=x, y=y)
            sage: g = lambda x, y: fricas.ellipticF(x, y).sage()
            sage: d = lambda x, y: f(x, y) - g(x, y)
            sage: [d(N(-pi/2 + x), y)                          # abs tol 1e-8       # optional - fricas, needs sage.symbolic
            ....:  for x in range(1, 3) for y in range(-2,2)]
            [0.000000000000000,
             0.000000000000000,
             0.000000000000000,
             0.000000000000000,
             5.55111512312578e-17,
             0.000000000000000,
             0.000000000000000,
             0.000000000000000]
        '''

elliptic_f: EllipticF

class EllipticKC(BuiltinFunction):
    """
    Return the complete elliptic integral of the first kind:

    .. MATH::

        K(m)=\\int_0^{\\pi/2} \\frac{dx}{\\sqrt{1 - m\\sin(x)^2}}.

    EXAMPLES::

        sage: elliptic_kc(0.5)                                                          # needs mpmath
        1.85407467730137

    .. SEEALSO::

        - :func:`elliptic_f()<sage.functions.special.EllipticF>`.

        - :func:`elliptic_ec()<sage.functions.special.EllipticEC>`.

    REFERENCES:

    - :wikipedia:`Elliptic_integral#Complete_elliptic_integral_of_the_first_kind`

    - :wikipedia:`Elliptic_integral#Incomplete_elliptic_integral_of_the_first_kind`
    """
    def __init__(self) -> None:
        """
        EXAMPLES::

            sage: loads(dumps(elliptic_kc))
            elliptic_kc
            sage: elliptic_kc(x)._sympy_()                                              # needs sage.symbolic
            elliptic_k(x)

        TESTS::

            sage: fricas(elliptic_kc(x))                                        # optional - fricas, needs sage.symbolic
            ellipticK(x)

            sage: elliptic_kc(0.3)  # abs tol 1e-8                                      # needs mpmath
            1.71388944817879
            sage: fricas.ellipticK(0.3).sage()  # abs tol 1e-3                  # optional - fricas, needs sage.symbolic
            1.7138894481787910555457043
        """

elliptic_kc: EllipticKC

class EllipticPi(BuiltinFunction):
    '''
    Return the incomplete elliptic integral of the third kind:

    .. MATH::

        \\Pi(n, t, m) = \\int_0^t \\frac{dx}{(1 - n \\sin(x)^2)\\sqrt{1 - m \\sin(x)^2}}.

    INPUT:

    - ``n`` -- a real number, called the "characteristic"

    - ``t`` -- a real number, called the "amplitude"

    - ``m`` -- a real number, called the "parameter"

    EXAMPLES::

        sage: N(elliptic_pi(1, pi/4, 1))                                                # needs sage.symbolic
        1.14779357469632

    Compare the value computed by Maxima to the definition as a definite integral
    (using GSL)::

        sage: elliptic_pi(0.1, 0.2, 0.3)                                                # needs mpmath
        0.200665068220979
        sage: numerical_integral(1/(1-0.1*sin(x)^2)/sqrt(1-0.3*sin(x)^2), 0.0, 0.2)     # needs sage.symbolic
        (0.2006650682209791, 2.227829789769088e-15)

    REFERENCES:

    - :wikipedia:`Elliptic_integral#Incomplete_elliptic_integral_of_the_third_kind`
    '''
    def __init__(self) -> None:
        """
        EXAMPLES::

            sage: loads(dumps(elliptic_pi))
            elliptic_pi
            sage: elliptic_pi(x, pi/4, 1)._sympy_()                                     # needs sympy sage.symbolic
            elliptic_pi(x, pi/4, 1)
        """

elliptic_pi: EllipticPi
