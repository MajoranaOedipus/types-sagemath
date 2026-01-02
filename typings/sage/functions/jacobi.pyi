r"""
Jacobi elliptic functions

This module implements the 12 Jacobi elliptic functions, along with their
inverses and the Jacobi amplitude function.

Jacobi elliptic functions can be thought of as generalizations
of both ordinary and hyperbolic trig functions. There are twelve
Jacobian elliptic functions. Each of the twelve corresponds to an
arrow drawn from one corner of a rectangle to another.

::

                n ------------------- d
                |                     |
                |                     |
                |                     |
                s ------------------- c

Each of the corners of the rectangle are labeled, by convention, ``s``,
``c``, ``d``, and ``n``. The rectangle is understood to be lying on the complex
plane, so that ``s`` is at the origin, ``c`` is on the real axis, and ``n`` is
on the imaginary axis. The twelve Jacobian elliptic functions are
then `\operatorname{pq}(x)`, where ``p`` and ``q`` are one of the letters
``s``, ``c``, ``d``, ``n``.

The Jacobian elliptic functions are then the unique
doubly-periodic, meromorphic functions satisfying the following
three properties:

#. There is a simple zero at the corner ``p``, and a simple pole at the
   corner ``q``.
#. The step from ``p`` to ``q`` is equal to half the period of the function
   `\operatorname{pq}(x)`; that is, the function `\operatorname{pq}(x)` is
   periodic in the direction ``pq``, with the period being twice the distance
   from ``p`` to ``q``. `\operatorname{pq}(x)` is periodic in the other two
   directions as well, with a period such that the distance from ``p`` to one
   of the other corners is a quarter period.
#. If the function `\operatorname{pq}(x)` is expanded in terms of `x` at one of
   the corners, the leading term in the expansion has a coefficient of 1.
   In other words, the leading term of the expansion of `\operatorname{pq}(x)`
   at the corner ``p`` is `x`; the leading term of the expansion at the corner
   ``q`` is `1/x`, and the leading term of an expansion at the other two
   corners is 1.

We can write

.. MATH::

    \operatorname{pq}(x) = \frac{\operatorname{pr}(x)}{\operatorname{qr}(x)}

where ``p``, ``q``, and ``r`` are any of the
letters ``s``, ``c``, ``d``, ``n``, with
the understanding that `\mathrm{ss} = \mathrm{cc} = \mathrm{dd}
= \mathrm{nn} = 1`.

Let

.. MATH::

    u = \int_0^{\phi} \frac{d\theta} {\sqrt {1-m \sin^2 \theta}},

then the *Jacobi elliptic function* `\operatorname{sn}(u)` is given by

.. MATH::

    \operatorname{sn}{u} = \sin{\phi}

and `\operatorname{cn}(u)` is given by

.. MATH::

    \operatorname{cn}{u} = \cos{\phi}

and

.. MATH::

    \operatorname{dn}{u} = \sqrt{1 - m\sin^2 \phi}.

To emphasize the dependence on `m`, one can write
`\operatorname{sn}(u|m)` for example (and similarly for `\mathrm{cn}` and
`\mathrm{dn}`). This is the notation used below.

For a given `k` with `0 < k < 1` they therefore are
solutions to the following nonlinear ordinary differential
equations:

- `\operatorname{sn}\,(x;k)` solves the differential equations

  .. MATH::

      \frac{d^2 y}{dx^2} + (1+k^2) y - 2 k^2 y^3 = 0
      \quad \text{ and } \quad
      \left(\frac{dy}{dx}\right)^2 = (1-y^2) (1-k^2 y^2).

- `\operatorname{cn}(x;k)` solves the differential equations

  .. MATH::

      \frac{d^2 y}{dx^2} + (1-2k^2) y + 2 k^2 y^3 = 0
      \quad \text{ and } \quad
      \left(\frac{dy}{dx}\right)^2 = (1-y^2)(1-k^2 + k^2 y^2).

- `\operatorname{dn}(x;k)` solves the differential equations

  .. MATH::

      \frac{d^2 y}{dx^2} - (2 - k^2) y + 2 y^3 = 0
      \quad \text{ and } \quad
      \left(\frac{dy}{dx}\right)^2 = y^2 (1 - k^2 - y^2).

  If `K(m)` denotes the complete elliptic integral of the
  first kind (named ``elliptic_kc`` in Sage), the elliptic functions
  `\operatorname{sn}(x|m)` and `\operatorname{cn}(x|m)` have real periods
  `4K(m)`, whereas `\operatorname{dn}(x|m)` has a period
  `2K(m)`. The limit `m \rightarrow 0` gives
  `K(0) = \pi/2` and trigonometric functions:
  `\operatorname{sn}(x|0) = \sin{x}`, `\operatorname{cn}(x|0) = \cos{x}`,
  `\operatorname{dn}(x|0) = 1`. The limit `m \rightarrow 1` gives
  `K(1) \rightarrow \infty` and hyperbolic functions:
  `\operatorname{sn}(x|1) = \tanh{x}`,
  `\operatorname{cn}(x|1) = \operatorname{sech}{x}`,
  `\operatorname{dn}(x|1) = \operatorname{sech}{x}`.

REFERENCES:

- :wikipedia:`Jacobi%27s_elliptic_functions`

- [KS2002]_

AUTHORS:

- David Joyner (2006): initial version

- Eviatar Bach (2013): complete rewrite, new numerical evaluation, and
  addition of the Jacobi amplitude function
"""

from typing import Literal
from sage.rings.rational import Rational
from sage.functions.hyperbolic import (
    arccosh as arccosh,
    arccoth as arccoth,
    arccsch as arccsch,
    arcsech as arcsech,
    arcsinh as arcsinh,
    arctanh as arctanh,
    cosh as cosh,
    coth as coth,
    csch as csch,
    sech as sech,
    sinh as sinh,
    tanh as tanh,
)
from sage.functions.special import elliptic_e as elliptic_e, elliptic_kc as elliptic_kc
from sage.functions.trig import (
    arccos as arccos,
    arccot as arccot,
    arccsc as arccsc,
    arcsec as arcsec,
    arcsin as arcsin,
    arctan as arctan,
    cos as cos,
    cot as cot,
    csc as csc,
    sec as sec,
    sin as sin,
    tan as tan,
)
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.rings.integer import Integer as Integer
from sage.rings.rational_field import QQ as QQ
from sage.symbolic.function import BuiltinFunction as BuiltinFunction

HALF: Rational

type JacobiKind = Literal[
        "nd", "ns", "nc", "dn", "ds", "dc", "sn", "sd", "sc", "cn", "cd", "cs"
    ]

class Jacobi[K: JacobiKind](BuiltinFunction):
    """
    Base class for the Jacobi elliptic functions.
    """

    kind: K
    def __init__(
        self,
        kind: K,
    ) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: from sage.functions.jacobi import Jacobi
            sage: Jacobi(\'sn\')
            jacobi_sn

        TESTS::

            sage: N(jacobi("sn", I, 1/2))   # abs tol 1e-12                             # needs sage.symbolic
            -8.59454886300046e-73 + 1.34737147138542*I

            sage: # optional - fricas, needs sage.symbolic
            sage: CN = fricas(jacobi(\'cn\',x, 2)); CN
            jacobiCn(x,2)
            sage: fricas.series(CN, x=0)
                1  2   3  4   17  6    79  8    1381  10      11
            1 - - x  + - x  - -- x  + --- x  - ----- x   + O(x  )
                2      8      80      640      19200
            sage: fricas(jacobi(\'sn\',x, 2))
            jacobiSn(x,2)
            sage: fricas(jacobi(\'dn\',x, 2))
            jacobiDn(x,2)
        """

jacobi_nd: Jacobi[Literal["nd"]]
jacobi_ns: Jacobi[Literal["ns"]]
jacobi_nc: Jacobi[Literal["nc"]]
jacobi_dn: Jacobi[Literal["dn"]]
jacobi_ds: Jacobi[Literal["ds"]]
jacobi_dc: Jacobi[Literal["dc"]]
jacobi_sn: Jacobi[Literal["sn"]]
jacobi_sd: Jacobi[Literal["sd"]]
jacobi_sc: Jacobi[Literal["sc"]]
jacobi_cn: Jacobi[Literal["cn"]]
jacobi_cd: Jacobi[Literal["cd"]]
jacobi_cs: Jacobi[Literal["cs"]]

class InverseJacobi[K: JacobiKind](BuiltinFunction):
    """
    Base class for the inverse Jacobi elliptic functions.
    """

    kind: K
    def __init__(self, kind: K) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: from sage.functions.jacobi import InverseJacobi
            sage: InverseJacobi('sn')
            inverse_jacobi_sn
        """

inverse_jacobi_nd: InverseJacobi[Literal["nd"]]
inverse_jacobi_ns: InverseJacobi[Literal["ns"]]
inverse_jacobi_nc: InverseJacobi[Literal["nc"]]
inverse_jacobi_dn: InverseJacobi[Literal["dn"]]
inverse_jacobi_ds: InverseJacobi[Literal["ds"]]
inverse_jacobi_dc: InverseJacobi[Literal["dc"]]
inverse_jacobi_sn: InverseJacobi[Literal["sn"]]
inverse_jacobi_sd: InverseJacobi[Literal["sd"]]
inverse_jacobi_sc: InverseJacobi[Literal["sc"]]
inverse_jacobi_cn: InverseJacobi[Literal["cn"]]
inverse_jacobi_cd: InverseJacobi[Literal["cd"]]
inverse_jacobi_cs: InverseJacobi[Literal["cs"]]


def jacobi(kind: JacobiKind, z, m, **kwargs):
    """
    The 12 Jacobi elliptic functions.

    INPUT:

    - ``kind`` -- string of the form ``'pq'``, where ``p``, ``q`` are in
      ``c``, ``d``, ``n``, ``s``
    - ``z`` -- a complex number
    - ``m`` -- a complex number; note that `m = k^2`, where `k` is
      the elliptic modulus

    EXAMPLES::

        sage: # needs mpmath
        sage: jacobi('sn', 1, 1)
        tanh(1)
        sage: jacobi('cd', 1, 1/2)
        jacobi_cd(1, 1/2)
        sage: RDF(jacobi('cd', 1, 1/2))
        0.7240097216593705
        sage: (RDF(jacobi('cn', 1, 1/2)), RDF(jacobi('dn', 1, 1/2)),
        ....:  RDF(jacobi('cn', 1, 1/2) / jacobi('dn', 1, 1/2)))
        (0.5959765676721407, 0.8231610016315962, 0.7240097216593705)

        sage: jsn = jacobi('sn', x, 1)                                                  # needs sage.symbolic
        sage: P = plot(jsn, 0, 1)                                                       # needs sage.plot sage.symbolic
    """

def inverse_jacobi(kind: JacobiKind, x, m, **kwargs):
    """
    The inverses of the 12 Jacobi elliptic functions. They have the property
    that

    .. MATH::

        \\operatorname{pq}(\\operatorname{arcpq}(x|m)|m) =
        \\operatorname{pq}(\\operatorname{pq}^{-1}(x|m)|m) = x.

    INPUT:

    - ``kind`` -- string of the form ``'pq'``, where ``p``, ``q`` are in
      ``c``, ``d``, ``n``, ``s``
    - ``x`` -- a real number
    - ``m`` -- a real number; note that `m = k^2`, where `k` is the elliptic
      modulus

    EXAMPLES::

        sage: jacobi('dn', inverse_jacobi('dn', 3, 0.4), 0.4)                           # needs mpmath
        3.00000000000000
        sage: inverse_jacobi('dn', 10, 1/10).n(digits=50)                               # needs mpmath
        2.4777736267904273296523691232988240759001423661683*I
        sage: inverse_jacobi_dn(x, 1)                                                   # needs sage.symbolic
        arcsech(x)
        sage: inverse_jacobi_dn(1, 3)                                                   # needs mpmath
        0

        sage: # needs sage.symbolic
        sage: m = var('m')
        sage: z = inverse_jacobi_dn(x, m).series(x, 4).subs(x=0.1, m=0.7)
        sage: jacobi_dn(z, 0.7)
        0.0999892750039819...
        sage: inverse_jacobi_nd(x, 1)
        arccosh(x)

        sage: # needs mpmath
        sage: inverse_jacobi_nd(1, 2)
        0
        sage: inverse_jacobi_ns(10^-5, 3).n()
        5.77350269202456e-6 + 1.17142008414677*I
        sage: jacobi('sn', 1/2, 1/2)
        jacobi_sn(1/2, 1/2)
        sage: jacobi('sn', 1/2, 1/2).n()
        0.470750473655657
        sage: inverse_jacobi('sn', 0.47, 1/2)
        0.499098231322220
        sage: inverse_jacobi('sn', 0.4707504, 0.5)
        0.499999911466555
        sage: P = plot(inverse_jacobi('sn', x, 0.5), 0, 1)                              # needs sage.plot
    """

class JacobiAmplitude(BuiltinFunction):
    """
    The Jacobi amplitude function
    `\\operatorname{am}(x|m) = \\int_0^x \\operatorname{dn}(t|m) dt` for
    `-K(m) \\leq x \\leq K(m)`, `F(\\operatorname{am}(x|m)|m) = x`.
    """

    def __init__(self) -> None:
        """
        TESTS::

            sage: from sage.functions.jacobi import JacobiAmplitude
            sage: JacobiAmplitude()
            jacobi_am
        """

jacobi_am: JacobiAmplitude

def inverse_jacobi_f(kind, x, m):
    """
    Internal function for numerical evaluation of a continuous complex branch
    of each inverse Jacobi function, as described in [Tee1997]_. Only accepts
    real arguments.

    TESTS::

        sage: from mpmath import ellipfun, chop                                         # needs mpmath
        sage: from sage.functions.jacobi import inverse_jacobi_f

        sage: # needs mpmath
        sage: chop(ellipfun('sn', inverse_jacobi_f('sn', 0.6, 0), 0))
        mpf('0.59999999999999998')
        sage: chop(ellipfun('sn', inverse_jacobi_f('sn', 0.6, 1), 1))
        mpf('0.59999999999999998')
        sage: chop(ellipfun('sn', inverse_jacobi_f('sn', 0, -3), -3))
        mpf('0.0')
        sage: chop(ellipfun('sn', inverse_jacobi_f('sn', -1, 4), 4))
        mpf('-1.0')
        sage: chop(ellipfun('sn', inverse_jacobi_f('sn', 0.3, 4), 4))
        mpf('0.29999999999999999')
        sage: chop(ellipfun('sn', inverse_jacobi_f('sn', 0.8, 4), 4))
        mpf('0.80000000000000004')

        sage: # needs mpmath
        sage: chop(ellipfun('ns', inverse_jacobi_f('ns', 0.8, 0), 0))
        mpf('0.80000000000000004')
        sage: chop(ellipfun('ns', inverse_jacobi_f('ns', -0.7, 1), 1))
        mpf('-0.69999999999999996')
        sage: chop(ellipfun('ns', inverse_jacobi_f('ns', 0.01, 2), 2))
        mpf('0.01')
        sage: chop(ellipfun('ns', inverse_jacobi_f('ns', 0, 2), 2))
        mpf('0.0')
        sage: chop(ellipfun('ns', inverse_jacobi_f('ns', -10, 6), 6))
        mpf('-10.0')

        sage: # needs mpmath
        sage: chop(ellipfun('cn', inverse_jacobi_f('cn', -10, 0), 0))
        mpf('-9.9999999999999982')
        sage: chop(ellipfun('cn', inverse_jacobi_f('cn', 50, 1), 1))
        mpf('50.000000000000071')
        sage: chop(ellipfun('cn', inverse_jacobi_f('cn', 1, 5), 5))
        mpf('1.0')
        sage: chop(ellipfun('cn', inverse_jacobi_f('cn', 0.5, -5), -5))
        mpf('0.5')
        sage: chop(ellipfun('cn', inverse_jacobi_f('cn', -0.75, -15), -15))
        mpf('-0.75000000000000022')
        sage: chop(ellipfun('cn', inverse_jacobi_f('cn', 10, 0.8), 0.8))
        mpf('9.9999999999999982')
        sage: chop(ellipfun('cn', inverse_jacobi_f('cn', -2, 0.9), 0.9))
        mpf('-2.0')

        sage: # needs mpmath
        sage: chop(ellipfun('nc', inverse_jacobi_f('nc', -4, 0), 0))
        mpf('-3.9999999999999987')
        sage: chop(ellipfun('nc', inverse_jacobi_f('nc', 7, 1), 1))
        mpf('7.0000000000000009')
        sage: chop(ellipfun('nc', inverse_jacobi_f('nc', 7, 3), 3))
        mpf('7.0')
        sage: chop(ellipfun('nc', inverse_jacobi_f('nc', 0, 2), 2))
        mpf('0.0')
        sage: chop(ellipfun('nc', inverse_jacobi_f('nc', -18, -4), -4))
        mpf('-17.999999999999925')

        sage: # needs mpmath
        sage: chop(ellipfun('dn', inverse_jacobi_f('dn', -0.3, 1), 1))
        mpf('-0.29999999999999999')
        sage: chop(ellipfun('dn', inverse_jacobi_f('dn', 1, -1), -1))
        mpf('1.0')
        sage: chop(ellipfun('dn', inverse_jacobi_f('dn', 0.8, 0.5), 0.5))
        mpf('0.80000000000000004')
        sage: chop(ellipfun('dn', inverse_jacobi_f('dn', 5, -4), -4))
        mpf('5.0')
        sage: chop(ellipfun('dn', inverse_jacobi_f('dn', 0.4, 0.5), 0.5))
        mpf('0.40000000000000002')
        sage: chop(ellipfun('dn', inverse_jacobi_f('dn', -0.4, 0.5), 0.5))
        mpf('-0.40000000000000002')
        sage: chop(ellipfun('dn', inverse_jacobi_f('dn', -0.9, 0.5), 0.5))
        mpf('-0.90000000000000002')
        sage: chop(ellipfun('dn', inverse_jacobi_f('dn', -1.9, 0.2), 0.2))
        mpf('-1.8999999999999999')

        sage: # needs mpmath
        sage: chop(ellipfun('nd', inverse_jacobi_f('nd', -1.9, 1), 1))
        mpf('-1.8999999999999999')
        sage: chop(ellipfun('nd', inverse_jacobi_f('nd', 1, -1), -1))
        mpf('1.0')
        sage: chop(ellipfun('nd', inverse_jacobi_f('nd', 11, -6), -6))
        mpf('11.0')
        sage: chop(ellipfun('nd', inverse_jacobi_f('nd', 0, 8), 8))
        mpf('0.0')
        sage: chop(ellipfun('nd', inverse_jacobi_f('nd', -3, 0.8), 0.8))
        mpf('-2.9999999999999996')

        sage: # needs mpmath
        sage: chop(ellipfun('sc', inverse_jacobi_f('sc', -3, 0), 0))
        mpf('-3.0')
        sage: chop(ellipfun('sc', inverse_jacobi_f('sc', 2, 1), 1))
        mpf('2.0')
        sage: chop(ellipfun('sc', inverse_jacobi_f('sc', 0, 9), 9))
        mpf('0.0')
        sage: chop(ellipfun('sc', inverse_jacobi_f('sc', -7, 3), 3))
        mpf('-7.0')

        sage: # needs mpmath
        sage: chop(ellipfun('cs', inverse_jacobi_f('cs', -7, 0), 0))
        mpf('-6.9999999999999991')
        sage: chop(ellipfun('cs', inverse_jacobi_f('cs', 8, 1), 1))
        mpf('8.0')
        sage: chop(ellipfun('cs', inverse_jacobi_f('cs', 2, 6), 6))
        mpf('2.0')
        sage: chop(ellipfun('cs', inverse_jacobi_f('cs', 0, 4), 4))
        mpf('0.0')
        sage: chop(ellipfun('cs', inverse_jacobi_f('cs', -6, 8), 8))
        mpf('-6.0000000000000018')

        sage: chop(ellipfun('cd', inverse_jacobi_f('cd', -6, 0), 0))                    # needs mpmath
        mpf('-6.0000000000000009')
        sage: chop(ellipfun('cd', inverse_jacobi_f('cd', 1, 3), 3))                     # needs mpmath
        mpf('1.0')
        sage: chop(ellipfun('cd', inverse_jacobi_f('cd', 6, 8), 8))                     # needs mpmath
        mpf('6.0000000000000027')

        sage: chop(ellipfun('dc', inverse_jacobi_f('dc', 5, 0), 0))                     # needs mpmath
        mpf('5.0000000000000018')
        sage: chop(ellipfun('dc', inverse_jacobi_f('dc', -4, 2), 2))                    # needs mpmath
        mpf('-4.0000000000000018')

        sage: # needs mpmath
        sage: chop(ellipfun('sd', inverse_jacobi_f('sd', -4, 0), 0))
        mpf('-3.9999999999999991')
        sage: chop(ellipfun('sd', inverse_jacobi_f('sd', 7, 1), 1))
        mpf('7.0')
        sage: chop(ellipfun('sd', inverse_jacobi_f('sd', 0, 9), 9))
        mpf('0.0')
        sage: chop(ellipfun('sd', inverse_jacobi_f('sd', 8, 0.8), 0.8))
        mpf('7.9999999999999991')

        sage: chop(ellipfun('ds', inverse_jacobi_f('ds', 4, 0.25), 0.25))               # needs mpmath
        mpf('4.0')
    """

def jacobi_am_f(x, m):
    """
    Internal function for numeric evaluation of the Jacobi amplitude function
    for real arguments. Procedure described in [Eh2013]_.

    TESTS::

        sage: # needs mpmath
        sage: from mpmath import ellipf
        sage: from sage.functions.jacobi import jacobi_am_f
        sage: ellipf(jacobi_am_f(0.5, 1), 1)
        mpf('0.5')
        sage: ellipf(jacobi_am(3, 0.3), 0.3)
        mpf('3.0')
        sage: ellipf(jacobi_am_f(2, -0.5), -0.5)
        mpf('2.0')
        sage: jacobi_am_f(2, -0.5)
        mpf('2.2680930777934176')
        sage: jacobi_am_f(-2, -0.5)
        mpf('-2.2680930777934176')
        sage: jacobi_am_f(-3, 2)
        mpf('0.36067407399586108')
    """
