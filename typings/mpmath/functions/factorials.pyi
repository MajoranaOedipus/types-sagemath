from __future__ import annotations
from builtins import range as xrange
from mpmath.functions.functions import defun
from mpmath.functions.functions import defun_wrapped
__all__: list[str] = ['barnesg', 'beta', 'binomial', 'defun', 'defun_wrapped', 'fac2', 'ff', 'gammaprod', 'hyperfac', 'rf', 'superfac', 'xrange']
def barnesg(ctx, z):
    ...
def beta(ctx, x, y):
    """
    
    Computes the beta function,
    `B(x,y) = \\Gamma(x) \\Gamma(y) / \\Gamma(x+y)`.
    The beta function is also commonly defined by the integral
    representation
    
    .. math ::
    
        B(x,y) = \\int_0^1 t^{x-1} (1-t)^{y-1} \\, dt
    
    **Examples**
    
    For integer and half-integer arguments where all three gamma
    functions are finite, the beta function becomes either rational
    number or a rational multiple of `\\pi`::
    
        >>> from mpmath import *
        >>> mp.dps = 15; mp.pretty = True
        >>> beta(5, 2)
        0.0333333333333333
        >>> beta(1.5, 2)
        0.266666666666667
        >>> 16*beta(2.5, 1.5)
        3.14159265358979
    
    Where appropriate, :func:`~mpmath.beta` evaluates limits. A pole
    of the beta function is taken to result in ``+inf``::
    
        >>> beta(-0.5, 0.5)
        0.0
        >>> beta(-3, 3)
        -0.333333333333333
        >>> beta(-2, 3)
        +inf
        >>> beta(inf, 1)
        0.0
        >>> beta(inf, 0)
        nan
    
    :func:`~mpmath.beta` supports complex numbers and arbitrary precision
    evaluation::
    
        >>> beta(1, 2+j)
        (0.4 - 0.2j)
        >>> mp.dps = 25
        >>> beta(j,0.5)
        (1.079424249270925780135675 - 1.410032405664160838288752j)
        >>> mp.dps = 50
        >>> beta(pi, e)
        0.037890298781212201348153837138927165984170287886464
    
    Various integrals can be computed by means of the
    beta function::
    
        >>> mp.dps = 15
        >>> quad(lambda t: t**2.5*(1-t)**2, [0, 1])
        0.0230880230880231
        >>> beta(3.5, 3)
        0.0230880230880231
        >>> quad(lambda t: sin(t)**4 * sqrt(cos(t)), [0, pi/2])
        0.319504062596158
        >>> beta(2.5, 0.75)/2
        0.319504062596158
    
    """
def binomial(ctx, n, k):
    """
    
    Computes the binomial coefficient
    
    .. math ::
    
        {n \\choose k} = \\frac{n!}{k!(n-k)!}.
    
    The binomial coefficient gives the number of ways that `k` items
    can be chosen from a set of `n` items. More generally, the binomial
    coefficient is a well-defined function of arbitrary real or
    complex `n` and `k`, via the gamma function.
    
    **Examples**
    
    Generate Pascal's triangle::
    
        >>> from mpmath import *
        >>> mp.dps = 15; mp.pretty = True
        >>> for n in range(5):
        ...     nprint([binomial(n,k) for k in range(n+1)])
        ...
        [1.0]
        [1.0, 1.0]
        [1.0, 2.0, 1.0]
        [1.0, 3.0, 3.0, 1.0]
        [1.0, 4.0, 6.0, 4.0, 1.0]
    
    There is 1 way to select 0 items from the empty set, and 0 ways to
    select 1 item from the empty set::
    
        >>> binomial(0, 0)
        1.0
        >>> binomial(0, 1)
        0.0
    
    :func:`~mpmath.binomial` supports large arguments::
    
        >>> binomial(10**20, 10**20-5)
        8.33333333333333e+97
        >>> binomial(10**20, 10**10)
        2.60784095465201e+104342944813
    
    Nonintegral binomial coefficients find use in series
    expansions::
    
        >>> nprint(taylor(lambda x: (1+x)**0.25, 0, 4))
        [1.0, 0.25, -0.09375, 0.0546875, -0.0375977]
        >>> nprint([binomial(0.25, k) for k in range(5)])
        [1.0, 0.25, -0.09375, 0.0546875, -0.0375977]
    
    An integral representation::
    
        >>> n, k = 5, 3
        >>> f = lambda t: exp(-j*k*t)*(1+exp(j*t))**n
        >>> chop(quad(f, [-pi,pi])/(2*pi))
        10.0
        >>> binomial(n,k)
        10.0
    
    """
def fac2(ctx, x):
    ...
def ff(ctx, x, n):
    """
    
    Computes the falling factorial,
    
    .. math ::
    
        (x)_n = x (x-1) \\cdots (x-n+1) = \\frac{\\Gamma(x+1)}{\\Gamma(x-n+1)}
    
    where the rightmost expression is valid for nonintegral `n`.
    
    **Examples**
    
    For integral `n`, the falling factorial is a polynomial::
    
        >>> from mpmath import *
        >>> mp.dps = 15; mp.pretty = True
        >>> for n in range(5):
        ...     nprint(taylor(lambda x: ff(x,n), 0, n))
        ...
        [1.0]
        [0.0, 1.0]
        [0.0, -1.0, 1.0]
        [0.0, 2.0, -3.0, 1.0]
        [0.0, -6.0, 11.0, -6.0, 1.0]
    
    Evaluation is supported for arbitrary arguments::
    
        >>> ff(2+3j, 5.5)
        (-720.41085888203 + 316.101124983878j)
    """
def gammaprod(ctx, a, b, _infsign = False):
    """
    
    Given iterables `a` and `b`, ``gammaprod(a, b)`` computes the
    product / quotient of gamma functions:
    
    .. math ::
    
        \\frac{\\Gamma(a_0) \\Gamma(a_1) \\cdots \\Gamma(a_p)}
             {\\Gamma(b_0) \\Gamma(b_1) \\cdots \\Gamma(b_q)}
    
    Unlike direct calls to :func:`~mpmath.gamma`, :func:`~mpmath.gammaprod` considers
    the entire product as a limit and evaluates this limit properly if
    any of the numerator or denominator arguments are nonpositive
    integers such that poles of the gamma function are encountered.
    That is, :func:`~mpmath.gammaprod` evaluates
    
    .. math ::
    
        \\lim_{\\epsilon \\to 0}
        \\frac{\\Gamma(a_0+\\epsilon) \\Gamma(a_1+\\epsilon) \\cdots
            \\Gamma(a_p+\\epsilon)}
             {\\Gamma(b_0+\\epsilon) \\Gamma(b_1+\\epsilon) \\cdots
            \\Gamma(b_q+\\epsilon)}
    
    In particular:
    
    * If there are equally many poles in the numerator and the
      denominator, the limit is a rational number times the remaining,
      regular part of the product.
    
    * If there are more poles in the numerator, :func:`~mpmath.gammaprod`
      returns ``+inf``.
    
    * If there are more poles in the denominator, :func:`~mpmath.gammaprod`
      returns 0.
    
    **Examples**
    
    The reciprocal gamma function `1/\\Gamma(x)` evaluated at `x = 0`::
    
        >>> from mpmath import *
        >>> mp.dps = 15
        >>> gammaprod([], [0])
        0.0
    
    A limit::
    
        >>> gammaprod([-4], [-3])
        -0.25
        >>> limit(lambda x: gamma(x-1)/gamma(x), -3, direction=1)
        -0.25
        >>> limit(lambda x: gamma(x-1)/gamma(x), -3, direction=-1)
        -0.25
    
    """
def hyperfac(ctx, z):
    ...
def rf(ctx, x, n):
    """
    
    Computes the rising factorial or Pochhammer symbol,
    
    .. math ::
    
        x^{(n)} = x (x+1) \\cdots (x+n-1) = \\frac{\\Gamma(x+n)}{\\Gamma(x)}
    
    where the rightmost expression is valid for nonintegral `n`.
    
    **Examples**
    
    For integral `n`, the rising factorial is a polynomial::
    
        >>> from mpmath import *
        >>> mp.dps = 15; mp.pretty = True
        >>> for n in range(5):
        ...     nprint(taylor(lambda x: rf(x,n), 0, n))
        ...
        [1.0]
        [0.0, 1.0]
        [0.0, 1.0, 1.0]
        [0.0, 2.0, 3.0, 1.0]
        [0.0, 6.0, 11.0, 6.0, 1.0]
    
    Evaluation is supported for arbitrary arguments::
    
        >>> rf(2+3j, 5.5)
        (-7202.03920483347 - 3777.58810701527j)
    """
def superfac(ctx, z):
    """
    
    Computes the superfactorial, defined as the product of
    consecutive factorials
    
    .. math ::
    
        \\mathrm{sf}(n) = \\prod_{k=1}^n k!
    
    For general complex `z`, `\\mathrm{sf}(z)` is defined
    in terms of the Barnes G-function (see :func:`~mpmath.barnesg`).
    
    **Examples**
    
    The first few superfactorials are (OEIS A000178)::
    
        >>> from mpmath import *
        >>> mp.dps = 15; mp.pretty = True
        >>> for n in range(10):
        ...     print("%s %s" % (n, superfac(n)))
        ...
        0 1.0
        1 1.0
        2 2.0
        3 12.0
        4 288.0
        5 34560.0
        6 24883200.0
        7 125411328000.0
        8 5.05658474496e+15
        9 1.83493347225108e+21
    
    Superfactorials grow very rapidly::
    
        >>> superfac(1000)
        3.24570818422368e+1177245
        >>> superfac(10**10)
        2.61398543581249e+467427913956904067453
    
    Evaluation is supported for arbitrary arguments::
    
        >>> mp.dps = 25
        >>> superfac(pi)
        17.20051550121297985285333
        >>> superfac(2+3j)
        (-0.005915485633199789627466468 + 0.008156449464604044948738263j)
        >>> diff(superfac, 1)
        0.2645072034016070205673056
    
    **References**
    
    1. http://oeis.org/A000178
    
    """
