from __future__ import annotations
from _operator import gt
from _operator import lt
from builtins import range as xrange
import mpmath.calculus.calculus
from mpmath.calculus.calculus import CalculusMethods
import mpmath.calculus.inverselaplace
from mpmath.calculus.inverselaplace import LaplaceTransformInversionMethods
import mpmath.calculus.odes
from mpmath.calculus.odes import ODEMethods
import mpmath.calculus.optimization
from mpmath.calculus.optimization import OptimizationMethods
import mpmath.calculus.quadrature
from mpmath.calculus.quadrature import QuadratureMethods
import mpmath.functions.functions
from mpmath.functions.functions import SpecialFunctions
import mpmath.functions.rszeta
from mpmath.functions.rszeta import RSCache
import mpmath.identification
from mpmath.identification import IdentificationMethods
from mpmath import libmp
import mpmath.matrices.calculus
from mpmath.matrices.calculus import MatrixCalculusMethods
import mpmath.matrices.eigen
from mpmath.matrices.eigen import Eigen
import mpmath.matrices.linalg
from mpmath.matrices.linalg import LinearAlgebraMethods
import mpmath.matrices.matrices
from mpmath.matrices.matrices import MatrixMethods
import mpmath.visualization
from mpmath.visualization import VisualizationMethods
import typing
__all__: list[str] = ['CalculusMethods', 'Context', 'Eigen', 'IdentificationMethods', 'LaplaceTransformInversionMethods', 'LinearAlgebraMethods', 'MatrixCalculusMethods', 'MatrixMethods', 'ODEMethods', 'OptimizationMethods', 'QuadratureMethods', 'RSCache', 'SpecialFunctions', 'StandardBaseContext', 'VisualizationMethods', 'gt', 'libmp', 'lt', 'xrange']
class Context:
    pass
class StandardBaseContext(Context, mpmath.functions.functions.SpecialFunctions, mpmath.functions.rszeta.RSCache, mpmath.calculus.quadrature.QuadratureMethods, mpmath.calculus.inverselaplace.LaplaceTransformInversionMethods, mpmath.calculus.calculus.CalculusMethods, mpmath.matrices.matrices.MatrixMethods, mpmath.matrices.calculus.MatrixCalculusMethods, mpmath.matrices.linalg.LinearAlgebraMethods, mpmath.matrices.eigen.Eigen, mpmath.identification.IdentificationMethods, mpmath.calculus.optimization.OptimizationMethods, mpmath.calculus.odes.ODEMethods, mpmath.visualization.VisualizationMethods):
    class ComplexResult(ValueError):
        pass
    class NoConvergence(Exception):
        pass
    _fixed_precision: typing.ClassVar[bool] = False
    verbose: typing.ClassVar[bool] = False
    @staticmethod
    def __init__(ctx):
        ...
    @staticmethod
    def _as_points(ctx, x):
        ...
    @staticmethod
    def _default_hyper_maxprec(ctx, p):
        ...
    @staticmethod
    def _eulernum(m, _cache = ...):
        """
        
        Computes the Euler numbers `E(n)`, which can be defined as
        coefficients of the Taylor expansion of `1/cosh x`:
        
        .. math ::
        
            \\frac{1}{\\cosh x} = \\sum_{n=0}^\\infty \\frac{E_n}{n!} x^n
        
        Example::
        
            >>> [int(eulernum(n)) for n in range(11)]
            [1, 0, -1, 0, 5, 0, -61, 0, 1385, 0, -50521]
            >>> [int(eulernum(n)) for n in range(11)]   # test cache
            [1, 0, -1, 0, 5, 0, -61, 0, 1385, 0, -50521]
        
        """
    @staticmethod
    def _gcd(*args):
        ...
    @staticmethod
    def _ifac(object):
        """
        fac(n, /) -> mpz
        
        Return the exact factorial of n.
        
        See factorial(n) to get the floating-point approximation.
        """
    @staticmethod
    def _im(ctx, x):
        ...
    @staticmethod
    def _init_aliases(ctx):
        ...
    @staticmethod
    def _re(ctx, x):
        ...
    @staticmethod
    def _stirling1(n, k):
        """
        
        Stirling number of the first kind.
        """
    @staticmethod
    def _stirling2(n, k):
        """
        
        Stirling number of the second kind.
        """
    @staticmethod
    def _zeta_int(ctx, n):
        ...
    @staticmethod
    def almosteq(ctx, s, t, rel_eps = None, abs_eps = None):
        """
        
        Determine whether the difference between `s` and `t` is smaller
        than a given epsilon, either relatively or absolutely.
        
        Both a maximum relative difference and a maximum difference
        ('epsilons') may be specified. The absolute difference is
        defined as `|s-t|` and the relative difference is defined
        as `|s-t|/\\max(|s|, |t|)`.
        
        If only one epsilon is given, both are set to the same value.
        If none is given, both epsilons are set to `2^{-p+m}` where
        `p` is the current working precision and `m` is a small
        integer. The default setting typically allows :func:`~mpmath.almosteq`
        to be used to check for mathematical equality
        in the presence of small rounding errors.
        
        **Examples**
        
            >>> from mpmath import *
            >>> mp.dps = 15
            >>> almosteq(3.141592653589793, 3.141592653589790)
            True
            >>> almosteq(3.141592653589793, 3.141592653589700)
            False
            >>> almosteq(3.141592653589793, 3.141592653589700, 1e-10)
            True
            >>> almosteq(1e-20, 2e-20)
            True
            >>> almosteq(1e-20, 2e-20, rel_eps=0, abs_eps=0)
            False
        
        """
    @staticmethod
    def arange(ctx, *args):
        """
        
        This is a generalized version of Python's :func:`~mpmath.range` function
        that accepts fractional endpoints and step sizes and
        returns a list of ``mpf`` instances. Like :func:`~mpmath.range`,
        :func:`~mpmath.arange` can be called with 1, 2 or 3 arguments:
        
        ``arange(b)``
            `[0, 1, 2, \\ldots, x]`
        ``arange(a, b)``
            `[a, a+1, a+2, \\ldots, x]`
        ``arange(a, b, h)``
            `[a, a+h, a+h, \\ldots, x]`
        
        where `b-1 \\le x < b` (in the third case, `b-h \\le x < b`).
        
        Like Python's :func:`~mpmath.range`, the endpoint is not included. To
        produce ranges where the endpoint is included, :func:`~mpmath.linspace`
        is more convenient.
        
        **Examples**
        
            >>> from mpmath import *
            >>> mp.dps = 15; mp.pretty = False
            >>> arange(4)
            [mpf('0.0'), mpf('1.0'), mpf('2.0'), mpf('3.0')]
            >>> arange(1, 2, 0.25)
            [mpf('1.0'), mpf('1.25'), mpf('1.5'), mpf('1.75')]
            >>> arange(1, -1, -0.75)
            [mpf('1.0'), mpf('0.25'), mpf('-0.5')]
        
        """
    @staticmethod
    def bad_domain(ctx, msg):
        ...
    @staticmethod
    def bernfrac(n):
        """
        
        Returns a tuple of integers `(p, q)` such that `p/q = B_n` exactly,
        where `B_n` denotes the `n`-th Bernoulli number. The fraction is
        always reduced to lowest terms. Note that for `n > 1` and `n` odd,
        `B_n = 0`, and `(0, 1)` is returned.
        
        **Examples**
        
        The first few Bernoulli numbers are exactly::
        
            >>> from mpmath import *
            >>> for n in range(15):
            ...     p, q = bernfrac(n)
            ...     print("%s %s/%s" % (n, p, q))
            ...
            0 1/1
            1 -1/2
            2 1/6
            3 0/1
            4 -1/30
            5 0/1
            6 1/42
            7 0/1
            8 -1/30
            9 0/1
            10 5/66
            11 0/1
            12 -691/2730
            13 0/1
            14 7/6
        
        This function works for arbitrarily large `n`::
        
            >>> p, q = bernfrac(10**4)
            >>> print(q)
            2338224387510
            >>> print(len(str(p)))
            27692
            >>> mp.dps = 15
            >>> print(mpf(p) / q)
            -9.04942396360948e+27677
            >>> print(bernoulli(10**4))
            -9.04942396360948e+27677
        
        .. note ::
        
            :func:`~mpmath.bernoulli` computes a floating-point approximation
            directly, without computing the exact fraction first.
            This is much faster for large `n`.
        
        **Algorithm**
        
        :func:`~mpmath.bernfrac` works by computing the value of `B_n` numerically
        and then using the von Staudt-Clausen theorem [1] to reconstruct
        the exact fraction. For large `n`, this is significantly faster than
        computing `B_1, B_2, \\ldots, B_2` recursively with exact arithmetic.
        The implementation has been tested for `n = 10^m` up to `m = 6`.
        
        In practice, :func:`~mpmath.bernfrac` appears to be about three times
        slower than the specialized program calcbn.exe [2]
        
        **References**
        
        1. MathWorld, von Staudt-Clausen Theorem:
           http://mathworld.wolfram.com/vonStaudt-ClausenTheorem.html
        
        2. The Bernoulli Number Page:
           http://www.bernoulli.org/
        
        """
    @staticmethod
    def chop(ctx, x, tol = None):
        """
        
        Chops off small real or imaginary parts, or converts
        numbers close to zero to exact zeros. The input can be a
        single number or an iterable::
        
            >>> from mpmath import *
            >>> mp.dps = 15; mp.pretty = False
            >>> chop(5+1e-10j, tol=1e-9)
            mpf('5.0')
            >>> nprint(chop([1.0, 1e-20, 3+1e-18j, -4, 2]))
            [1.0, 0.0, 3.0, -4.0, 2.0]
        
        The tolerance defaults to ``100*eps``.
        """
    @staticmethod
    def cos_sin(ctx, z, **kwargs):
        ...
    @staticmethod
    def cospi_sinpi(ctx, z, **kwargs):
        ...
    @staticmethod
    def fadd(ctx, x, y, **kwargs):
        ...
    @staticmethod
    def fdiv(ctx, x, y, **kwargs):
        ...
    @staticmethod
    def fdot(ctx, xs, ys = None, conjugate = False):
        ...
    @staticmethod
    def fmul(ctx, x, y, **kwargs):
        ...
    @staticmethod
    def fneg(ctx, x, **kwargs):
        ...
    @staticmethod
    def fprod(ctx, args):
        ...
    @staticmethod
    def fsub(ctx, x, y, **kwargs):
        ...
    @staticmethod
    def fsum(ctx, args, absolute = False, squared = False):
        ...
    @staticmethod
    def isprime(n):
        """
        
        Determines whether n is a prime number. A probabilistic test is
        performed if n is very large. No special trick is used for detecting
        perfect powers.
        
            >>> sum(list_primes(100000))
            454396537
            >>> sum(n*isprime(n) for n in range(100000))
            454396537
        
        """
    @staticmethod
    def linspace(ctx, *args, **kwargs):
        """
        
        ``linspace(a, b, n)`` returns a list of `n` evenly spaced
        samples from `a` to `b`. The syntax ``linspace(mpi(a,b), n)``
        is also valid.
        
        This function is often more convenient than :func:`~mpmath.arange`
        for partitioning an interval into subintervals, since
        the endpoint is included::
        
            >>> from mpmath import *
            >>> mp.dps = 15; mp.pretty = False
            >>> linspace(1, 4, 4)
            [mpf('1.0'), mpf('2.0'), mpf('3.0'), mpf('4.0')]
        
        You may also provide the keyword argument ``endpoint=False``::
        
            >>> linspace(1, 4, 4, endpoint=False)
            [mpf('1.0'), mpf('1.75'), mpf('2.5'), mpf('3.25')]
        
        """
    @staticmethod
    def list_primes(n):
        ...
    @staticmethod
    def maxcalls(ctx, f, N):
        """
        
        Return a wrapped copy of *f* that raises ``NoConvergence`` when *f*
        has been called more than *N* times::
        
            >>> from mpmath import *
            >>> mp.dps = 15
            >>> f = maxcalls(sin, 10)
            >>> print(sum(f(n) for n in range(10)))
            1.95520948210738
            >>> f(10) # doctest: +IGNORE_EXCEPTION_DETAIL
            Traceback (most recent call last):
              ...
            NoConvergence: maxcalls: function evaluated 10 times
        
        """
    @staticmethod
    def memoize(ctx, f):
        """
        
        Return a wrapped copy of *f* that caches computed values, i.e.
        a memoized copy of *f*. Values are only reused if the cached precision
        is equal to or higher than the working precision::
        
            >>> from mpmath import *
            >>> mp.dps = 15; mp.pretty = True
            >>> f = memoize(maxcalls(sin, 1))
            >>> f(2)
            0.909297426825682
            >>> f(2)
            0.909297426825682
            >>> mp.dps = 25
            >>> f(2) # doctest: +IGNORE_EXCEPTION_DETAIL
            Traceback (most recent call last):
              ...
            NoConvergence: maxcalls: function evaluated 1 times
        
        """
    @staticmethod
    def moebius(n):
        """
        
        Evaluates the Moebius function which is `mu(n) = (-1)^k` if `n`
        is a product of `k` distinct primes and `mu(n) = 0` otherwise.
        
        TODO: speed up using factorization
        """
    @staticmethod
    def mul_accurately(ctx, factors, check_step = 1):
        ...
    @staticmethod
    def nprint(ctx, x, n = 6, **kwargs):
        """
        
        Equivalent to ``print(nstr(x, n))``.
        """
    @staticmethod
    def power(ctx, x, y):
        """
        Converts `x` and `y` to mpmath numbers and evaluates
        `x^y = \\exp(y \\log(x))`::
        
            >>> from mpmath import *
            >>> mp.dps = 30; mp.pretty = True
            >>> power(2, 0.5)
            1.41421356237309504880168872421
        
        This shows the leading few digits of a large Mersenne prime
        (performing the exact calculation ``2**43112609-1`` and
        displaying the result in Python would be very slow)::
        
            >>> power(2, 43112609)-1
            3.16470269330255923143453723949e+12978188
        """
    @staticmethod
    def sum_accurately(ctx, terms, check_step = 1):
        ...
    @staticmethod
    def warn(ctx, msg):
        ...
