from sage.modules.free_module_element import vector as vector
from sage.rings.real_double import RDF as RDF

def find_root(f, a, b, xtol: float = 1e-12, rtol=..., maxiter: int = 100, full_output: bool = False):
    """
    Numerically find a root of ``f`` on the closed interval `[a,b]`
    (or `[b,a]`) if possible, where ``f`` is a function in the one variable.
    Note: this function only works in fixed (machine) precision, it is not
    possible to get arbitrary precision approximations with it.

    INPUT:

    - ``f`` -- a function of one variable or symbolic equality

    - ``a``, ``b`` -- endpoints of the interval

    - ``xtol``, ``rtol`` -- the routine converges when a root is known
      to lie within ``xtol`` of the value return. Should be `\\geq 0`.
      The routine modifies this to take into account the relative precision
      of doubles. By default, rtol is ``4*numpy.finfo(float).eps``, the
      minimum allowed value for :func:`scipy:scipy.optimize.brentq`, which is
      what this method uses underneath. This value is equal to ``2.0**-50`` for
      IEEE-754 double precision floats as used by Python.

    - ``maxiter`` -- integer; if convergence is not achieved in
      ``maxiter`` iterations, an error is raised. Must be `\\geq 0`.

    - ``full_output`` -- boolean (default: ``False``); if ``True``, also return
      object that contains information about convergence

    EXAMPLES:

    An example involving an algebraic polynomial function::

        sage: R.<x> = QQ[]
        sage: f = (x+17)*(x-3)*(x-1/8)^3
        sage: find_root(f, 0,4)
        2.999999999999995
        sage: find_root(f, 0,1)  # abs tol 1e-6 (note -- precision of answer isn't very good on some machines)
        0.124999
        sage: find_root(f, -20,-10)
        -17.0

    In Pomerance's book on primes he asserts that the famous Riemann
    Hypothesis is equivalent to the statement that the function `f(x)`
    defined below is positive for all `x \\geq 2.01`::

        sage: def f(x):
        ....:     return sqrt(x) * log(x) - abs(Li(x) - prime_pi(x))

    We find where `f` equals, i.e., what value that is slightly smaller
    than `2.01` that could have been used in the formulation of the Riemann
    Hypothesis::

        sage: find_root(f, 2, 4, rtol=0.0001)
        2.0082...

    This agrees with the plot::

        sage: plot(f,2,2.01)
        Graphics object consisting of 1 graphics primitive

    The following example was added due to :issue:`4942` and demonstrates that
    the function need not be defined at the endpoints::

        sage: find_root(x^2*log(x,2)-1,0, 2)  # abs tol 1e-6
        1.41421356237

    The following is an example, again from :issue:`4942` where Brent's method
    fails. Currently no other method is implemented, but at least we
    acknowledge the fact that the algorithm fails::

        sage: find_root(1/(x-1)+1,0, 2)
        0.0
        sage: find_root(1/(x-1)+1,0.00001, 2)
        Traceback (most recent call last):
        ...
        NotImplementedError: Brent's method failed to find a zero for f on the interval

    An example of a function which evaluates to NaN on the entire interval::

        sage: f(x) = 0.0 / max(0, x)
        sage: find_root(f, -1, 0)
        Traceback (most recent call last):
        ...
        RuntimeError: f appears to have no zero on the interval
    """
def find_local_maximum(f, a, b, tol: float = 1.48e-08, maxfun: int = 500):
    """
    Numerically find a local maximum of the expression `f` on the interval
    `[a,b]` (or `[b,a]`) along with the point at which the maximum is attained.

    Note that this function only finds a *local* maximum, and not the
    global maximum on that interval -- see the examples with
    :func:`find_local_maximum`.

    See the documentation for :func:`find_local_maximum` for more
    details and possible workarounds for finding the global minimum on
    an interval.

    EXAMPLES::

        sage: f = lambda x: x*cos(x)
        sage: find_local_maximum(f, 0, 5)
        (0.561096338191..., 0.8603335890...)
        sage: find_local_maximum(f, 0, 5, tol=0.1, maxfun=10)
        (0.561090323458..., 0.857926501456...)
        sage: find_local_maximum(8*e^(-x)*sin(x) - 1, 0, 7)                             # needs sage.symbolic
        (1.579175535558..., 0.7853981...)
    """
def find_local_minimum(f, a, b, tol: float = 1.48e-08, maxfun: int = 500):
    """
    Numerically find a local minimum of the expression ``f`` on the
    interval `[a,b]` (or `[b,a]`) and the point at which it attains that
    minimum.  Note that ``f`` must be a function of (at most) one
    variable.

    Note that this function only finds a *local* minimum, and not the
    global minimum on that interval -- see the examples below.

    INPUT:

    - ``f`` -- a function of at most one variable

    - ``a``, ``b`` -- endpoints of interval on which to minimize `f`

    - ``tol`` -- the convergence tolerance

    - ``maxfun`` -- maximum function evaluations

    OUTPUT:

    - ``minval`` -- (float) the minimum value that `f` takes on in the
      interval `[a,b]`

    - ``x`` -- (float) the point at which `f` takes on the minimum value

    EXAMPLES::

        sage: f = lambda x: x*cos(x)
        sage: find_local_minimum(f, 1, 5)
        (-3.28837139559..., 3.4256184695...)
        sage: find_local_minimum(f, 1, 5, tol=1e-3)
        (-3.28837136189098..., 3.42575079030572...)
        sage: find_local_minimum(f, 1, 5, tol=1e-2, maxfun=10)
        (-3.28837084598..., 3.4250840220...)
        sage: show(plot(f, 0, 20))                                                      # needs sage.plot
        sage: find_local_minimum(f, 1, 15)
        (-9.4772942594..., 9.5293344109...)

    Only local minima are found; if you enlarge the interval, the
    returned minimum may be *larger*! See :issue:`2607`.

    ::

        sage: # needs sage.symbolic
        sage: f(x) = -x*sin(x^2)
        sage: find_local_minimum(f, -2.5, -1)
        (-2.182769784677722, -2.1945027498534686)

    Enlarging the interval returns a larger minimum::

        sage: # needs sage.symbolic
        sage: find_local_minimum(f, -2.5, 2)
        (-1.3076194129914434, 1.3552111405712108)

    One work-around is to plot the function and grab the minimum from
    that, although the plotting code does not necessarily do careful
    numerics (observe the small number of decimal places that we
    actually test)::

        sage: # needs sage.plot sage.symbolic
        sage: plot(f, (x, -2.5, -1)).ymin()
        -2.182...
        sage: plot(f, (x, -2.5, 2)).ymin()
        -2.182...

    ALGORITHM:

    Uses :func:`scipy:scipy.optimize.fminbound` which uses Brent's method.


    AUTHOR:

    - William Stein (2007-12-07)
    """
def minimize(func, x0, gradient=None, hessian=None, algorithm: str = 'default', verbose: bool = False, **args):
    '''
    This function is an interface to a variety of algorithms for computing
    the minimum of a function of several variables.

    INPUT:

    - ``func`` -- either a symbolic function or a Python function whose
      argument is a tuple with `n` components

    - ``x0`` -- initial point for finding minimum

    - ``gradient`` -- (optional) gradient function. This will be computed
      automatically for symbolic functions.  For Python functions, it allows
      the use of algorithms requiring derivatives.  It should accept a
      tuple of arguments and return a NumPy array containing the partial
      derivatives at that point.

    - ``hessian`` -- (optional) hessian function. This will be computed
      automatically for symbolic functions. For Python functions, it allows
      the use of algorithms requiring derivatives. It should accept a tuple
      of arguments and return a NumPy array containing the second partial
      derivatives of the function.

    - ``algorithm`` -- string specifying algorithm to use. Options are
      ``\'default\'`` (for Python functions, the simplex method is the default)
      (for symbolic functions bfgs is the default):

      - ``\'simplex\'`` -- using the downhill simplex algorithm

      - ``\'powell\'`` -- use the modified Powell algorithm

      - ``\'bfgs\'`` -- (Broyden-Fletcher-Goldfarb-Shanno) requires gradient

      - ``\'cg\'`` -- (conjugate-gradient) requires gradient

      - ``\'ncg\'`` -- (newton-conjugate gradient) requires gradient and hessian

    - ``verbose`` -- boolean (default: ``False``); print convergence message

    .. NOTE::

        For additional information on the algorithms implemented in this function,
        consult SciPy\'s :mod:`documentation on optimization and root
        finding <scipy:scipy.optimize>`.

    EXAMPLES:

    Minimize a fourth order polynomial in three variables (see the
    :wikipedia:`Rosenbrock_function`)::

        sage: vars = var(\'x y z\')                                                       # needs sage.symbolic
        sage: f = 100*(y-x^2)^2 + (1-x)^2 + 100*(z-y^2)^2 + (1-y)^2                     # needs sage.symbolic
        sage: minimize(f, [.1,.3,.4])  # abs tol 1e-6                                   # needs sage.symbolic
        (1.0, 1.0, 1.0)

    Try the newton-conjugate gradient method; the gradient and hessian are
    computed automatically::

        sage: minimize(f, [.1, .3, .4], algorithm=\'ncg\')  # abs tol 1e-6                # needs sage.symbolic
        (1.0, 1.0, 1.0)

    We get additional convergence information with the `verbose` option::

        sage: minimize(f, [.1, .3, .4], algorithm=\'ncg\', verbose=True)                  # needs sage.symbolic
        Optimization terminated successfully.
        ...
        (0.9999999..., 0.999999..., 0.999999...)

    Same example with just Python functions::

        sage: def rosen(x):  # The Rosenbrock function
        ....:    return sum(100.0r*(x[1r:]-x[:-1r]**2.0r)**2.0r + (1r-x[:-1r])**2.0r)
        sage: minimize(rosen, [.1,.3,.4]) # abs tol 3e-5
        (1.0, 1.0, 1.0)

    Same example with a pure Python function and a Python function to
    compute the gradient::

        sage: # needs numpy
        sage: def rosen(x):  # The Rosenbrock function
        ....:    return sum(100.0r*(x[1r:]-x[:-1r]**2.0r)**2.0r + (1r-x[:-1r])**2.0r)
        sage: import numpy
        sage: if int(numpy.version.short_version[0]) > 1:
        ....:     _ = numpy.set_printoptions(legacy="1.25")
        sage: from numpy import zeros
        sage: def rosen_der(x):
        ....:    xm = x[1r:-1r]
        ....:    xm_m1 = x[:-2r]
        ....:    xm_p1 = x[2r:]
        ....:    der = zeros(x.shape, dtype=float)
        ....:    der[1r:-1r] = 200r*(xm-xm_m1**2r) - 400r*(xm_p1 - xm**2r)*xm - 2r*(1r-xm)
        ....:    der[0] = -400r*x[0r]*(x[1r]-x[0r]**2r) - 2r*(1r-x[0])
        ....:    der[-1] = 200r*(x[-1r]-x[-2r]**2r)
        ....:    return der
        sage: minimize(rosen, [.1,.3,.4], gradient=rosen_der,  # abs tol 1e-6
        ....:          algorithm=\'bfgs\')
        (1.0, 1.0, 1.0)
    '''
def minimize_constrained(func, cons, x0, gradient=None, algorithm: str = 'default', **args):
    """
    Minimize a function with constraints.

    INPUT:

    - ``func`` -- either a symbolic function, or a Python function whose
      argument is a tuple with `n` components

    - ``cons`` -- constraints. This should be either a function or list of
      functions that must be positive. Alternatively, the constraints can
      be specified as a list of intervals that define the region we are
      minimizing in. If the constraints are specified as functions, the
      functions should be functions of a tuple with `n` components
      (assuming `n` variables). If the constraints are specified as a list
      of intervals and there are no constraints for a given variable, that
      component can be (``None``, ``None``).

    - ``x0`` -- initial point for finding minimum

    - ``algorithm`` -- (optional) specify the algorithm to use:

      - ``'default'`` -- default choices

      - ``'l-bfgs-b'`` -- only effective if you specify bound constraints;
        see [ZBN1997]_

    - ``gradient`` -- (optional) gradient function. This will be computed
      automatically for symbolic functions. This is only used when the
      constraints are specified as a list of intervals.

    EXAMPLES:

    Let us maximize `x + y - 50` subject to the following constraints:
    `50x + 24y \\leq 2400`, `30x + 33y \\leq 2100`, `x \\geq 45`,
    and `y \\geq 5`::

        sage: f = lambda p: -p[0]-p[1]+50
        sage: c_1 = lambda p: p[0]-45
        sage: c_2 = lambda p: p[1]-5
        sage: c_3 = lambda p: -50*p[0]-24*p[1]+2400
        sage: c_4 = lambda p: -30*p[0]-33*p[1]+2100
        sage: a = minimize_constrained(f,[c_1,c_2,c_3,c_4],[2,3])
        sage: a
        (45.0, 6.25...)

    Let's find a minimum of `\\sin(xy)`::

        sage: x,y = var('x y')                                                          # needs sage.symbolic
        sage: f(x,y) = sin(x*y)                                                         # needs sage.symbolic
        sage: minimize_constrained(f, [(None,None),(4,10)],[5,5])                       # needs sage.symbolic
        (4.8..., 4.8...)

    Check if L-BFGS-B finds the same minimum::

        sage: minimize_constrained(f, [(None,None),(4,10)],[5,5],                       # needs sage.symbolic
        ....:                      algorithm='l-bfgs-b')
        (4.7..., 4.9...)

    Rosenbrock function (see the :wikipedia:`Rosenbrock_function`)::

        sage: from scipy.optimize import rosen, rosen_der
        sage: minimize_constrained(rosen, [(-50,-10),(5,10)],[1,1],
        ....:                      gradient=rosen_der, algorithm='l-bfgs-b')
        (-10.0, 10.0)
        sage: minimize_constrained(rosen, [(-50,-10),(5,10)],[1,1],
        ....:                      algorithm='l-bfgs-b')
        (-10.0, 10.0)

    TESTS:

    Check if :issue:`6592` is fixed::

        sage: # needs sage.symbolic
        sage: x, y = var('x y')
        sage: f(x,y) = (100 - x) + (1000 - y)
        sage: c(x,y) = x + y - 479  # > 0
        sage: minimize_constrained(f, [c], [100, 300]) # random
        (805.985..., 1005.985...)
        sage: minimize_constrained(f, c, [100, 300])   # random
        (805.985..., 1005.985...)

    If ``func`` is symbolic, its minimizer should be in the same order
    as its arguments (:issue:`32511`)::

        sage: # needs sage.symbolic
        sage: x,y = SR.var('x,y')
        sage: f(y,x) = x - y
        sage: c1(y,x) = x
        sage: c2(y,x) = 1-y
        sage: minimize_constrained(f, [c1, c2], (0,0)) # abs tol 1e-04
        (1.0, 0.0)
    """
def find_fit(data, model, initial_guess=None, parameters=None, variables=None, solution_dict: bool = False):
    '''
    Finds numerical estimates for the parameters of the function model to
    give a best fit to data.


    INPUT:

    - ``data`` -- a two dimensional table of floating point numbers of the
      form `[[x_{1,1}, x_{1,2}, \\ldots, x_{1,k}, f_1],
      [x_{2,1}, x_{2,2}, \\ldots, x_{2,k}, f_2],
      \\ldots,
      [x_{n,1}, x_{n,2}, \\ldots, x_{n,k}, f_n]]` given as either a list of
      lists, matrix, or numpy array.

    - ``model`` -- either a symbolic expression, symbolic function, or a
      Python function. ``model`` has to be a function of the variables
      `(x_1, x_2, \\ldots, x_k)` and free parameters
      `(a_1, a_2, \\ldots, a_l)`.

    - ``initial_guess`` -- (default: ``None``) initial estimate for the
      parameters `(a_1, a_2, \\ldots, a_l)`, given as either a list, tuple,
      vector or numpy array. If ``None``, the default estimate for each
      parameter is `1`.

    - ``parameters`` -- (default: ``None``) a list of the parameters
      `(a_1, a_2, \\ldots, a_l)`. If model is a symbolic function it is
      ignored, and the free parameters of the symbolic function are used.

    - ``variables`` -- (default: ``None``) a list of the variables
      `(x_1, x_2, \\ldots, x_k)`. If model is a symbolic function it is
      ignored, and the variables of the symbolic function are used.

    - ``solution_dict`` -- boolean (default: ``False``); if ``True``, return the
      solution as a dictionary rather than an equation

    EXAMPLES:

    First we create some data points of a sine function with some "random"
    perturbations::

        sage: set_random_seed(0)
        sage: data = [(i, 1.2 * sin(0.5*i-0.2) + 0.1 * normalvariate(0, 1))             # needs sage.symbolic
        ....:         for i in xsrange(0, 4*pi, 0.2)]
        sage: var(\'a, b, c, x\')                                                         # needs sage.symbolic
        (a, b, c, x)

    We define a function with free parameters `a`, `b` and `c`::

        sage: model(x) = a * sin(b * x - c)                                             # needs sage.symbolic

    We search for the parameters that give the best fit to the data::

        sage: find_fit(data, model)                                                     # needs sage.symbolic
        [a == 1.21..., b == 0.49..., c == 0.19...]

    We can also use a Python function for the model::

        sage: def f(x, a, b, c): return a * sin(b * x - c)
        sage: fit = find_fit(data, f, parameters=[a, b, c], variables=[x],              # needs sage.symbolic
        ....:                solution_dict = True)
        sage: fit[a], fit[b], fit[c]                                                    # needs sage.symbolic
        (1.21..., 0.49..., 0.19...)

    We search for a formula for the `n`-th prime number::

        sage: # needs sage.libs.pari
        sage: dataprime = [(i, nth_prime(i)) for i in range(1, 5000, 100)]
        sage: find_fit(dataprime, a * x * log(b * x),                                   # needs sage.symbolic
        ....:          parameters=[a, b], variables=[x])
        [a == 1.11..., b == 1.24...]


    ALGORITHM:

    Uses :func:`scipy:scipy.optimize.leastsq` which in turn uses MINPACK\'s
    ``lmdif`` and ``lmder`` algorithms.
    '''
def binpacking(items, maximum: int = 1, k=None, solver=None, verbose: int = 0, *, integrality_tolerance: float = 0.001):
    """
    Solve the bin packing problem.

    The Bin Packing problem is the following :

    Given a list of items of weights `p_i` and a real value `k`, what is the
    least number of bins such that all the items can be packed in the bins,
    while ensuring that the sum of the weights of the items packed in each bin
    is at most `k` ?

    For more informations, see :wikipedia:`Bin_packing_problem`.

    Two versions of this problem are solved by this algorithm :

    - Is it possible to put the given items in `k` bins ?
    - What is the assignment of items using the least number of bins with
      the given list of items ?

    INPUT:

    - ``items`` -- list or dict; either a list of real values (the items'
      weight), or a dictionary associating to each item its weight

    - ``maximum`` -- (default: 1) the maximal size of a bin

    - ``k`` -- integer (default: ``None``); number of bins:

      - When set to an integer value, the function returns a partition of the
        items into `k` bins if possible, and raises an exception otherwise.

      - When set to ``None``, the function returns a partition of the items
        using the least possible number of bins.

    - ``solver`` -- (default: ``None``) specify a Mixed Integer Linear Programming
      (MILP) solver to be used. If set to ``None``, the default one is used. For
      more information on MILP solvers and which default solver is used, see
      the method
      :meth:`solve <sage.numerical.mip.MixedIntegerLinearProgram.solve>`
      of the class
      :class:`MixedIntegerLinearProgram <sage.numerical.mip.MixedIntegerLinearProgram>`.

    - ``verbose`` -- integer (default: 0); sets the level of verbosity. Set
      to 0 by default, which means quiet.

    - ``integrality_tolerance`` -- parameter for use with MILP solvers over an
      inexact base ring; see :meth:`MixedIntegerLinearProgram.get_values`

    OUTPUT:

    A list of lists, each member corresponding to a bin and containing either
    the list of the weights inside it when ``items`` is a list of items' weight,
    or the list of items inside it when ``items`` is a dictionary. If there is
    no solution, an exception is raised (this can only happen when ``k`` is
    specified or if ``maximum`` is less than the weight of one item).

    EXAMPLES:

    Trying to find the minimum amount of boxes for 5 items of weights
    `1/5, 1/4, 2/3, 3/4, 5/7`::

        sage: from sage.numerical.optimize import binpacking
        sage: values = [1/5, 1/3, 2/3, 3/4, 5/7]
        sage: bins = binpacking(values)                                                 # needs sage.numerical.mip
        sage: len(bins)                                                                 # needs sage.numerical.mip
        3

    Checking the bins are of correct size ::

        sage: all(sum(b) <= 1 for b in bins)                                            # needs sage.numerical.mip
        True

    Checking every item is in a bin ::

        sage: b1, b2, b3 = bins                                                         # needs sage.numerical.mip
        sage: all((v in b1 or v in b2 or v in b3) for v in values)                      # needs sage.numerical.mip
        True

    And only in one bin ::

        sage: sum(len(b) for b in bins) == len(values)                                  # needs sage.numerical.mip
        True

    One way to use only three boxes (which is best possible) is to put
    `1/5 + 3/4` together in a box, `1/3+2/3` in another, and `5/7`
    by itself in the third one.

    Of course, we can also check that there is no solution using only two boxes ::

        sage: from sage.numerical.optimize import binpacking
        sage: binpacking([0.2,0.3,0.8,0.9], k=2)                                        # needs sage.numerical.mip
        Traceback (most recent call last):
        ...
        ValueError: this problem has no solution

    We can also provide a dictionary keyed by items and associating to each item
    its weight. Then, the bins contain the name of the items inside it ::

        sage: values = {'a':1/5, 'b':1/3, 'c':2/3, 'd':3/4, 'e':5/7}
        sage: bins = binpacking(values)                                                 # needs sage.numerical.mip
        sage: set(flatten(bins)) == set(values.keys())                                  # needs sage.numerical.mip
        True

    TESTS:

    Wrong type for parameter items::

        sage: binpacking(set())
        Traceback (most recent call last):
        ...
        TypeError: parameter items must be a list or a dictionary.
    """
