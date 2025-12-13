import sage as sage
from sage.misc.sageinspect import sage_getargspec as sage_getargspec
from typing import Any, ClassVar, overload

class PyFunctionWrapper:
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""

class ode_solver:
    '''File: /build/sagemath/src/sage/src/sage/calculus/ode.pyx (starting at line 106)

        :meth:`ode_solver` is a class that wraps the GSL library\'s ode solver routines.

        To use it, instantiate the class::

            sage: T = ode_solver()

        To solve a system of the form `dy_i/dt=f_i(t,y)`, you must
        supply a vector or tuple/list valued function ``f`` representing
        `f_i`.  The functions `f` and the jacobian should have the
        form ``foo(t,y)`` or ``foo(t,y,params)``.  ``params`` which is
        optional allows for your function to depend on one or a tuple of
        parameters.  Note if you use it, ``params`` must be a tuple even
        if it only has one component.  For example if you wanted to solve
        `y\'\'+y=0`, you would need to write it as a first order system::

            y_0\' = y_1
            y_1\' = -y_0

        In code::

            sage: f = lambda t, y: [y[1], -y[0]]
            sage: T.function = f

        For some algorithms, the jacobian must be supplied as well, the
        form of this should be a function returning a list of lists of the
        form ``[ [df_1/dy_1,...,df_1/dy_n], ...,
        [df_n/dy_1,...,df_n,dy_n], [df_1/dt,...,df_n/dt] ]``.

        There are examples below, if your jacobian was the function
        ``my_jacobian`` you would do::

            sage: T.jacobian = my_jacobian     # not tested, since it doesn\'t make sense to test this

        There are a variety of algorithms available for different types of systems. Possible algorithms are

        - ``\'rkf45\'`` -- Runge-Kutta-Fehlberg (4,5)

        - ``\'rk2\'`` -- embedded Runge-Kutta (2,3)

        - ``\'rk4\'`` -- `4`-th order classical Runge-Kutta

        - ``\'rk8pd\'`` -- Runge-Kutta Prince-Dormand (8,9)

        - ``\'rk2imp\'`` -- implicit 2nd order Runge-Kutta at gaussian points

        - ``\'rk4imp\'`` -- implicit `4`-th order Runge-Kutta at gaussian points

        - ``\'bsimp\'`` -- implicit Burlisch-Stoer (requires jacobian)

        - ``\'gear1\'`` -- M=1 implicit gear

        - ``\'gear2\'`` -- M=2 implicit gear

        The default algorithm is ``\'rkf45\'``. If you instead wanted to use
        ``\'bsimp\'`` you would do::

            sage: T.algorithm = "bsimp"

        The user should supply initial conditions in ``y_0``. For example if
        your initial conditions are `y_0=1, y_1=1`, do::

            sage: T.y_0 = [1,1]

        The actual solver is invoked by the method :meth:`ode_solve`.  It
        has arguments ``t_span``, ``y_0``, ``num_points``, ``params``.
        ``y_0`` must be supplied either as an argument or above by
        assignment.  Params which are optional and only necessary if your
        system uses ``params`` can be supplied to ``ode_solve`` or by
        assignment.

        ``t_span`` is the time interval on which to solve the ode.  There
        are two ways to specify ``t_span``:

        * If ``num_points`` is not specified, then the sequence ``t_span``
          is used as the time points for the solution.  Note that the
          first element ``t_span[0]`` is the initial time, where the
          initial condition ``y_0`` is the specified solution, and
          subsequent elements are the ones where the solution is computed.

        * If ``num_points`` is specified and ``t_span`` is a sequence with
          just 2 elements, then these are the starting and ending times,
          and the solution will be computed at ``num_points`` equally
          spaced points between ``t_span[0]`` and ``t_span[1]``.  The
          initial condition is also included in the output so that
          ``num_points + 1`` total points are returned.  E.g. if ``t_span
          = [0.0, 1.0]`` and ``num_points = 10``, then solution is
          returned at the 11 time points ``[0.0, 0.1, 0.2, 0.3, 0.4, 0.5,
          0.6, 0.7, 0.8, 0.9, 1.0]``.

        (Note that if ``num_points`` is specified and ``t_span`` is not
        length 2 then ``t_span`` are used as the time points and
        ``num_points`` is ignored.)

        Error is estimated via the expression ``D_i =
        error_abs*s_i+error_rel*(a|y_i|+a_dydt*h*|y_i\'|)``.  The user can
        specify

        - ``error_abs`` (1e-10 by default),
        - ``error_rel`` (1e-10 by default),
        - ``a`` (1 by default),
        - ``a_dydt`` (0 by default) and
        - ``s_i`` (as ``scaling_abs`` which should be a tuple and is 1 in all
          components by default).

        If you specify one of ``a`` or ``a_dydt``
        you must specify the other.  You may specify ``a`` and ``a_dydt``
        without ``scaling_abs`` (which will be taken =1 be default).
        ``h`` is the initial step size, which is 1e-2 by default.

        ``ode_solve`` solves the solution as a list of tuples of the form,
        ``[ (t_0,[y_1,...,y_n]),(t_1,[y_1,...,y_n]),...,(t_n,[y_1,...,y_n])]``.

        This data is stored in the variable solutions::

            sage: T.solution               # not tested

        EXAMPLES:

        Consider solving the Van der Pol oscillator `x\'\'(t) +
        ux\'(t)(x(t)^2-1)+x(t)=0` between `t=0` and `t= 100`.  As a first
        order system it is `x\'=y`, `y\'=-x+uy(1-x^2)`. Let us take `u=10`
        and use initial conditions `(x,y)=(1,0)` and use the Runge-Kutta
        Prince-Dormand algorithm. ::

            sage: def f_1(t, y, params):
            ....:    return [y[1], -y[0] - params[0]*y[1]*(y[0]**2-1.0)]

            sage: def j_1(t, y, params):
            ....:    return [[0.0, 1.0],
            ....:            [-2.0*params[0]*y[0]*y[1] - 1.0, -params[0]*(y[0]*y[0]-1.0)],
            ....:            [0.0, 0.0]]

            sage: T = ode_solver()
            sage: T.algorithm = "rk8pd"
            sage: T.function = f_1
            sage: T.jacobian = j_1
            sage: T.ode_solve(y_0=[1,0], t_span=[0,100], params=[10.0], num_points=1000)
            sage: import tempfile
            sage: with tempfile.NamedTemporaryFile(suffix=\'.png\') as f:                     # needs sage.plot
            ....:     T.plot_solution(filename=f.name)

        The solver line is equivalent to::

            sage: T.ode_solve(y_0=[1,0], t_span=[x/10.0 for x in range(1000)], params=[10.0])

        Let\'s try a system::

            y_0\'=y_1*y_2
            y_1\'=-y_0*y_2
            y_2\'=-.51*y_0*y_1

        We will not use the jacobian this time and will change the
        error tolerances. ::

            sage: g_1 = lambda t,y: [y[1]*y[2], -y[0]*y[2], -0.51*y[0]*y[1]]
            sage: T.function = g_1
            sage: T.y_0 = [0,1,1]
            sage: T.scale_abs = [1e-4, 1e-4, 1e-5]
            sage: T.error_rel = 1e-4
            sage: T.ode_solve(t_span=[0,12], num_points=100)

        By default ``T.plot_solution()`` plots the `y_0`; to plot general `y_i`, use::

            sage: with tempfile.NamedTemporaryFile(suffix=\'.png\') as f:                     # needs sage.plot
            ....:     T.plot_solution(i=0, filename=f.name)
            ....:     T.plot_solution(i=1, filename=f.name)
            ....:     T.plot_solution(i=2, filename=f.name)

        The method interpolate_solution will return a spline interpolation
        through the points found by the solver. By default, `y_0` is
        interpolated.  You can interpolate `y_i` through the keyword
        argument ``i``. ::

            sage: f = T.interpolate_solution()
            sage: plot(f,0,12).show()                                                       # needs sage.plot
            sage: f = T.interpolate_solution(i=1)
            sage: plot(f,0,12).show()                                                       # needs sage.plot
            sage: f = T.interpolate_solution(i=2)
            sage: plot(f,0,12).show()                                                       # needs sage.plot
            sage: f = T.interpolate_solution()
            sage: from math import pi
            sage: f(pi)
            0.5379...

        The solver attributes may also be set up using arguments to
        ode_solver.  The previous example can be rewritten as::

            sage: T = ode_solver(g_1, y_0=[0,1,1], scale_abs=[1e-4,1e-4,1e-5],
            ....:                error_rel=1e-4, algorithm=\'rk8pd\')
            sage: T.ode_solve(t_span=[0,12], num_points=100)
            sage: f = T.interpolate_solution()
            sage: f(pi)
            0.5379...

        Unfortunately because Python functions are used, this solver
        is slow on systems that require many function evaluations.  It
        is possible to pass a compiled function by deriving from the
        class :class:`ode_system` and overloading ``c_f`` and ``c_j`` with C
        functions that specify the system. The following will work in the
        notebook:

        .. code-block:: cython

              %cython
              cimport sage.calculus.ode
              import sage.calculus.ode
              from sage.libs.gsl.all cimport *

              cdef class van_der_pol(sage.calculus.ode.ode_system):
                  cdef int c_f(self, double t, double *y, double *dydt):
                      dydt[0]=y[1]
                      dydt[1]=-y[0]-1000*y[1]*(y[0]*y[0]-1)
                      return GSL_SUCCESS
                  cdef int c_j(self, double t, double *y, double *dfdy, double *dfdt):
                      dfdy[0]=0
                      dfdy[1]=1.0
                      dfdy[2]=-2.0*1000*y[0]*y[1]-1.0
                      dfdy[3]=-1000*(y[0]*y[0]-1.0)
                      dfdt[0]=0
                      dfdt[1]=0
                      return GSL_SUCCESS

        After executing the above block of code you can do the
        following (WARNING: the following is *not* automatically
        doctested)::

            sage: # not tested
            sage: T = ode_solver()
            sage: T.algorithm = "bsimp"
            sage: vander = van_der_pol()
            sage: T.function = vander
            sage: T.ode_solve(y_0=[1, 0], t_span=[0, 2000],
            ....:             num_points=1000)
            sage: from tempfile import NamedTemporaryFile
            sage: with NamedTemporaryFile(suffix=\'.png\') as f:
            ....:     T.plot_solution(i=0, filename=f.name)
    '''
    def __init__(self, function=..., jacobian=..., h=..., error_abs=..., error_rel=..., a=..., a_dydt=..., scale_abs=..., algorithm=..., y_0=..., t_span=..., params=...) -> Any:
        """ode_solver.__init__(self, function=None, jacobian=None, h=1e-2, error_abs=1e-10, error_rel=1e-10, a=False, a_dydt=False, scale_abs=False, algorithm='rkf45', y_0=None, t_span=None, params=None)

        File: /build/sagemath/src/sage/src/sage/calculus/ode.pyx (starting at line 345)"""
    def interpolate_solution(self, i=...) -> Any:
        """ode_solver.interpolate_solution(self, i=0)

        File: /build/sagemath/src/sage/src/sage/calculus/ode.pyx (starting at line 367)"""
    def ode_solve(self, t_span=..., y_0=..., num_points=..., params=...) -> Any:
        """ode_solver.ode_solve(self, t_span=False, y_0=False, num_points=False, params=None)

        File: /build/sagemath/src/sage/src/sage/calculus/ode.pyx (starting at line 412)"""
    @overload
    def plot_solution(self, i=..., filename=..., interpolate=..., **kwds) -> Any:
        '''ode_solver.plot_solution(self, i=0, filename=None, interpolate=False, **kwds)

        File: /build/sagemath/src/sage/src/sage/calculus/ode.pyx (starting at line 371)

        Plot a one dimensional projection of the solution.

        INPUT:

        - ``i`` -- nonnegative integer; composant of the projection

        - ``filename`` -- string or ``None``; whether to plot the picture or
          save it in a file

        - ``interpolate`` -- whether to interpolate between the points of the
          discretized solution

        - additional keywords are passed to the graphics primitive

        EXAMPLES::

            sage: T = ode_solver()
            sage: T.function = lambda t,y: [cos(y[0]) * sin(t)]
            sage: T.jacobian = lambda t,y: [[-sin(y[0]) * sin(t)]]
            sage: T.ode_solve(y_0=[1],t_span=[0,20],num_points=1000)
            sage: T.plot_solution()                                                     # needs sage.plot

        And with some options::

            sage: T.plot_solution(color=\'red\', axes_labels=["t", "x(t)"])               # needs sage.plot'''
    @overload
    def plot_solution(self) -> Any:
        '''ode_solver.plot_solution(self, i=0, filename=None, interpolate=False, **kwds)

        File: /build/sagemath/src/sage/src/sage/calculus/ode.pyx (starting at line 371)

        Plot a one dimensional projection of the solution.

        INPUT:

        - ``i`` -- nonnegative integer; composant of the projection

        - ``filename`` -- string or ``None``; whether to plot the picture or
          save it in a file

        - ``interpolate`` -- whether to interpolate between the points of the
          discretized solution

        - additional keywords are passed to the graphics primitive

        EXAMPLES::

            sage: T = ode_solver()
            sage: T.function = lambda t,y: [cos(y[0]) * sin(t)]
            sage: T.jacobian = lambda t,y: [[-sin(y[0]) * sin(t)]]
            sage: T.ode_solve(y_0=[1],t_span=[0,20],num_points=1000)
            sage: T.plot_solution()                                                     # needs sage.plot

        And with some options::

            sage: T.plot_solution(color=\'red\', axes_labels=["t", "x(t)"])               # needs sage.plot'''
    @overload
    def plot_solution(self, color=..., axes_labels=...) -> Any:
        '''ode_solver.plot_solution(self, i=0, filename=None, interpolate=False, **kwds)

        File: /build/sagemath/src/sage/src/sage/calculus/ode.pyx (starting at line 371)

        Plot a one dimensional projection of the solution.

        INPUT:

        - ``i`` -- nonnegative integer; composant of the projection

        - ``filename`` -- string or ``None``; whether to plot the picture or
          save it in a file

        - ``interpolate`` -- whether to interpolate between the points of the
          discretized solution

        - additional keywords are passed to the graphics primitive

        EXAMPLES::

            sage: T = ode_solver()
            sage: T.function = lambda t,y: [cos(y[0]) * sin(t)]
            sage: T.jacobian = lambda t,y: [[-sin(y[0]) * sin(t)]]
            sage: T.ode_solve(y_0=[1],t_span=[0,20],num_points=1000)
            sage: T.plot_solution()                                                     # needs sage.plot

        And with some options::

            sage: T.plot_solution(color=\'red\', axes_labels=["t", "x(t)"])               # needs sage.plot'''
    def __setattr__(self, name, value) -> Any:
        """ode_solver.__setattr__(self, name, value)

        File: /build/sagemath/src/sage/src/sage/calculus/ode.pyx (starting at line 362)"""

class ode_system:
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
