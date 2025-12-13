import _cython_3_2_1
from sage.categories.category import RDF as RDF
from sage.ext.fast_callable import fast_callable as fast_callable
from sage.misc.sageinspect import sage_getargspec as sage_getargspec
from typing import ClassVar

monte_carlo_integral: _cython_3_2_1.cython_function_or_method

def numerical_integral(
    func,
    a,
    b=None,
    algorithm='qag',
    max_points=87,
    params=None,
    eps_abs=1e-06,
    eps_rel=1e-06,
    rule=6
): 
    """numerical_integral(func, a, b=None, algorithm='qag', max_points=87, params=None, eps_abs=1e-6, eps_rel=1e-6, rule=6)

File: /build/sagemath/src/sage/src/sage/calculus/integration.pyx (starting at line 74)

Return the numerical integral of the function on the interval
from a to b and an error bound.

INPUT:

- ``a``, ``b`` -- the interval of integration, specified as two
  numbers or as a tuple/list with the first element the lower bound
  and the second element the upper bound.  Use ``+Infinity`` and
  ``-Infinity`` for plus or minus infinity.
- ``algorithm`` -- valid choices are:

  * 'qag' -- for an adaptive integration
  * 'qags' -- for an adaptive integration with (integrable) singularities
  * 'qng' -- for a non-adaptive Gauss-Kronrod (samples at a maximum of 87pts)

- ``max_points`` -- sets the maximum number of sample points
- ``params`` -- used to pass parameters to your function
- ``eps_abs``, ``eps_rel`` -- sets the absolute and relative error
  tolerances which satisfies the relation ``|RESULT - I|  <= max(eps_abs,
  eps_rel * |I|)``, where ``I = \int_a^b f(x) d x``.
- ``rule`` -- this controls the Gauss-Kronrod rule used in the adaptive integration:

  * rule=1 -- 15 point rule
  * rule=2 -- 21 point rule
  * rule=3 -- 31 point rule
  * rule=4 -- 41 point rule
  * rule=5 -- 51 point rule
  * rule=6 -- 61 point rule

  Higher key values are more accurate for smooth functions but lower
  key values deal better with discontinuities.

OUTPUT:

A tuple whose first component is the answer and whose second
component is an error estimate.

REMARK:

There is also a method ``nintegral`` on symbolic expressions
that implements numerical integration using Maxima.  It is potentially
very useful for symbolic expressions.

EXAMPLES:

To integrate the function `x^2` from 0 to 1, we do ::

    sage: numerical_integral(x^2, 0, 1, max_points=100)
    (0.3333333333333333, 3.700743415417188e-15)

To integrate the function `\sin(x)^3 + \sin(x)` we do ::

    sage: numerical_integral(sin(x)^3 + sin(x),  0, pi)
    (3.333333333333333, 3.700743415417188e-14)

The input can be any callable::

    sage: numerical_integral(lambda x: sin(x)^3 + sin(x),  0, pi)
    (3.333333333333333, 3.700743415417188e-14)

We check this with a symbolic integration::

    sage: (sin(x)^3+sin(x)).integral(x,0,pi)
    10/3

If we want to change the error tolerances and Gauss rule used::

    sage: f = x^2
    sage: numerical_integral(f, 0, 1, max_points=200, eps_abs=1e-7, eps_rel=1e-7, rule=4)
    (0.3333333333333333, 3.700743415417188e-15)

For a Python function with parameters::

    sage: f(x,a) = 1/(a+x^2)
    sage: [numerical_integral(f, 1, 2, max_points=100, params=[n])[0]  # abs tol 1.0e-6
    ....:           for n in range(10)]
    [0.5000000000000000,
     0.3217505543966422,
     0.24030098317248832,
     0.19253082576711372,
     0.1608752771983211,
     0.138275456763492,
     0.1212997593570257,
     0.10806674191683492,
     0.09745444625553161,
     0.08875068305030848]

    sage: y = var('y')
    sage: numerical_integral(x*y, 0, 1)
    Traceback (most recent call last):
    ...
    ValueError: The function to be integrated depends on 2 variables (x, y),
    and so cannot be integrated in one dimension. Please fix additional
    variables with the 'params' argument

Note the parameters are always a tuple even if they have one component.

It is possible to integrate on infinite intervals as well by using
+Infinity or -Infinity in the interval argument. For example::

    sage: f = exp(-x)
    sage: numerical_integral(f, 0, +Infinity)  # random output
    (0.99999999999957279, 1.8429811298996553e-07)

Note the coercion to the real field RR, which prevents underflow::

    sage: f = exp(-x**2)
    sage: numerical_integral(f, -Infinity, +Infinity)  # random output
    (1.7724538509060035, 3.4295192165889879e-08)

One can integrate any real-valued callable function::

    sage: numerical_integral(lambda x: abs(zeta(x)), [1.1,1.5])  # random output
    (1.8488570602160455, 2.052643677492633e-14)

We can also numerically integrate symbolic expressions using either this
function (which uses GSL) or the native integration (which uses Maxima)::

    sage: exp(-1/x).nintegral(x, 1, 2)  # via maxima
    (0.50479221787318..., 5.60431942934407...e-15, 21, 0)
    sage: numerical_integral(exp(-1/x), 1, 2)
    (0.50479221787318..., 5.60431942934407...e-15)

We can also integrate constant expressions::

    sage: numerical_integral(2, 1, 7)
    (12.0, 0.0)

If the interval of integration is a point, then the result is
always zero (this makes sense within the Lebesgue theory of
integration), see :issue:`12047`::

    sage: numerical_integral(log, 0, 0)
    (0.0, 0.0)
    sage: numerical_integral(lambda x: sqrt(x), (-2.0, -2.0) )
    (0.0, 0.0)

In the presence of integrable singularity, the default adaptive method might
fail and it is advised to use ``'qags'``::

    sage: b = 1.81759643554688
    sage: F(x) = sqrt((-x + b)/((x - 1.0)*x))
    sage: numerical_integral(F, 1, b)
    (inf, nan)
    sage: numerical_integral(F, 1, b, algorithm='qags')    # abs tol 1e-10
    (1.1817104238446596, 3.387268288079781e-07)

AUTHORS:

- Josh Kantor
- William Stein
- Robert Bradshaw
- Jeroen Demeyer

ALGORITHM: Uses calls to the GSL (GNU Scientific Library) C library.
Documentation can be found in [GSL]_ chapter "Numerical Integration".

TESTS:

Make sure that constant Expressions, not merely uncallable arguments,
can be integrated (:issue:`10088`), at least if we can coerce them
to float::

    sage: f, g = x, x-1
    sage: numerical_integral(f-g, -2, 2)
    (4.0, 0.0)
    sage: numerical_integral(SR(2.5), 5, 20)
    (37.5, 0.0)
    sage: numerical_integral(SR(1+3j), 2, 3)
    Traceback (most recent call last):
    ...
    TypeError: unable to simplify to float approximation

Check for :issue:`15496`::

    sage: f = x^2/exp(-1/(x^2+1))/(x^2+1)
    sage: D = integrate(f,(x,-infinity,infinity),hold=True)
    sage: D.n()
    Traceback (most recent call last):
    ...
    ValueError: integral does not converge at -infinity

Symbolic functions can be integrated as conveniently as symbolic
expressions, as in :issue:`15219`::

    sage: h(x) = x
    sage: numerical_integral(h,0,1)[0] # abs tol 1e-8
    0.5
"""
    ...
integral_numerical = numerical_integral

class PyFunctionWrapper:
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""

class compiled_integrand:
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
