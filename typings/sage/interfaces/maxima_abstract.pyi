from .interface import AsciiArtString as AsciiArtString, Interface as Interface, InterfaceElement as InterfaceElement, InterfaceFunction as InterfaceFunction, InterfaceFunctionElement as InterfaceFunctionElement
from _typeshed import Incomplete
from sage.cpython.string import bytes_to_str as bytes_to_str
from sage.env import DOT_SAGE as DOT_SAGE, MAXIMA as MAXIMA
from sage.interfaces.tab_completion import ExtraTabCompletion as ExtraTabCompletion
from sage.misc.instancedoc import instancedoc as instancedoc
from sage.misc.multireplace import multiple_replace as multiple_replace
from sage.structure.richcmp import rich_to_bool as rich_to_bool, richcmp as richcmp

COMMANDS_CACHE: Incomplete

class MaximaAbstract(ExtraTabCompletion, Interface):
    """
    Abstract interface to Maxima.

    INPUT:

    - ``name`` -- string

    OUTPUT: the interface

    EXAMPLES:

    This class should not be instantiated directly,
    but through its subclasses Maxima (Pexpect interface)
    or MaximaLib (library interface)::

        sage: m = Maxima()
        sage: from sage.interfaces.maxima_abstract import MaximaAbstract
        sage: isinstance(m,MaximaAbstract)
        True
    """
    def __init__(self, name: str = 'maxima_abstract') -> None:
        """
        Create an instance of an abstract interface to Maxima.
        See ``MaximaAbstract`` for full documentation.

        EXAMPLES::

            sage: from sage.interfaces.maxima_abstract import MaximaAbstract
            sage: isinstance(maxima,MaximaAbstract)
            True

        TESTS::

            sage: from sage.interfaces.maxima_abstract import MaximaAbstract
            sage: loads(dumps(MaximaAbstract)) == MaximaAbstract
            True
        """
    def chdir(self, dir) -> None:
        """
        Change Maxima's current working directory.

        INPUT:

        - ``dir`` -- string

        OUTPUT: none

        EXAMPLES::

            sage: maxima.chdir('/')
        """
    def help(self, s):
        """
        Return Maxima's help for ``s``.

        INPUT:

        - ``s`` -- string

        OUTPUT: Maxima's help for ``s``

        EXAMPLES::

            sage: maxima.help('gcd')
            -- Function: gcd (<p_1>, <p_2>, <x_1>, ...)
            ...
        """
    def example(self, s):
        """
        Return Maxima's examples for ``s``.

        INPUT:

        - ``s`` -- string

        OUTPUT: Maxima's examples for ``s``

        EXAMPLES::

            sage: maxima.example('arrays')
            a[n]:=n*a[n-1]
                                            a  := n a
                                             n       n - 1
            a[0]:1
            a[5]
                                                  120
            a[n]:=n
            a[6]
                                                   6
            a[4]
                                                  24
                                                 done
        """
    describe = help
    def demo(self, s):
        """
        Run Maxima's demo for ``s``.

        INPUT:

        - ``s`` -- string

        OUTPUT: none

        EXAMPLES::

            sage: maxima.demo('cf') # not tested
            read and interpret file: .../share/maxima/5.34.1/demo/cf.dem

            At the '_' prompt, type ';' and <enter> to get next demonstration.
            frac1:cf([1,2,3,4])
            ...
        """
    def completions(self, s, verbose: bool = True):
        """
        Return all commands that complete the command starting with the
        string ``s``. This is like typing s[tab] in the Maxima interpreter.

        INPUT:

        - ``s`` -- string

        - ``verbose`` -- boolean (default: ``True``)

        OUTPUT: array of strings

        EXAMPLES::

            sage: sorted(maxima.completions('gc', verbose=False))
            ['gcd', 'gcdex', 'gcfactor', 'gctime']
        """
    def console(self) -> None:
        """
        Start the interactive Maxima console. This is a completely separate
        maxima session from this interface. To interact with this session,
        you should instead use ``maxima.interact()``.

        OUTPUT: none

        EXAMPLES::

            sage: maxima.console()             # not tested (since we can't)
            Maxima 5.46.0 https://maxima.sourceforge.io
            using Lisp ECL 21.2.1
            Distributed under the GNU Public License. See the file COPYING.
            Dedicated to the memory of William Schelter.
            This is a development version of Maxima. The function bug_report()
            provides bug reporting information.
            (%i1)

        ::

            sage: maxima.interact()     # not tested
              --> Switching to Maxima <--
            maxima: 2+2
            4
            maxima:
              --> Exiting back to Sage <--
        """
    def cputime(self, t=None):
        """
        Return the amount of CPU time that this Maxima session has used.

        INPUT:

        - ``t`` -- float (default: ``None``); if \\var{t} is not None, then
          it returns the difference between the current CPU time and \\var{t}

        OUTPUT: float

        EXAMPLES::

            sage: t = maxima.cputime()
            sage: _ = maxima.de_solve('diff(y,x,2) + 3*x = y', ['x','y'], [1,1,1])
            sage: maxima.cputime(t) # output random
            0.568913
        """
    def version(self):
        """
        Return the version of Maxima that Sage includes.

        OUTPUT: none

        EXAMPLES::

            sage: maxima.version()  # random
            '5.41.0'
        """
    def function(self, args, defn, rep=None, latex=None):
        """
        Return the Maxima function with given arguments and definition.

        INPUT:

        - ``args`` -- string with variable names separated by
          commas

        - ``defn`` -- string (or Maxima expression) that
          defines a function of the arguments in Maxima

        - ``rep`` -- an optional string; if given, this is how
          the function will print

        OUTPUT: Maxima function

        EXAMPLES::

            sage: f = maxima.function('x', 'sin(x)')
            sage: f(3.2)  # abs tol 2e-16
            -0.058374143427579909
            sage: f = maxima.function('x,y', 'sin(x)+cos(y)')
            sage: f(2, 3.5)  # abs tol 2e-16
            sin(2)-0.9364566872907963
            sage: f
            sin(x)+cos(y)

        ::

            sage: g = f.integrate('z')
            sage: g
            (cos(y)+sin(x))*z
            sage: g(1,2,3)
            3*(cos(2)+sin(1))

        The function definition can be a Maxima object::

            sage: an_expr = maxima('sin(x)*gamma(x)')
            sage: t = maxima.function('x', an_expr)
            sage: t
            gamma(x)*sin(x)
            sage: t(2)
             sin(2)
            sage: float(t(2))
            0.9092974268256817
            sage: loads(t.dumps())
            gamma(x)*sin(x)
        """
    def plot2d(self, *args) -> None:
        '''
        Plot a 2d graph using Maxima / gnuplot.

        maxima.plot2d(f, \'[var, min, max]\', options)

        INPUT:

        - ``f`` -- string representing a function (such as
          f="sin(x)") [var, xmin, xmax]

        - ``options`` -- an optional string representing plot2d
          options in gnuplot format

        EXAMPLES::

            sage: maxima.plot2d(\'sin(x)\',\'[x,-5,5]\')   # not tested
            sage: opts = \'[gnuplot_term, ps], [gnuplot_out_file, "sin-plot.eps"]\'
            sage: maxima.plot2d(\'sin(x)\',\'[x,-5,5]\',opts)    # not tested

        The eps file is saved in the current directory.
        '''
    def plot2d_parametric(self, r, var, trange, nticks: int = 50, options=None) -> None:
        '''
        Plot r = [x(t), y(t)] for t = tmin...tmax using gnuplot with
        options.

        INPUT:

        - ``r`` -- string representing a function (such as
          r="[x(t),y(t)]")

        - ``var`` -- string representing the variable (such
          as var = "t")

        - ``trange`` -- [tmin, tmax] are numbers with tmintmax

        - ``nticks`` -- integer (default: 50)

        - ``options`` -- an optional string representing plot2d
          options in gnuplot format

        EXAMPLES::

            sage: maxima.plot2d_parametric(["sin(t)","cos(t)"], "t",[-3.1,3.1])   # not tested

        ::

            sage: opts = \'[gnuplot_preamble, "set nokey"], [gnuplot_term, ps], [gnuplot_out_file, "circle-plot.eps"]\'
            sage: maxima.plot2d_parametric(["sin(t)","cos(t)"], "t", [-3.1,3.1], options=opts)   # not tested

        The eps file is saved to the current working directory.

        Here is another fun plot::

            sage: maxima.plot2d_parametric(["sin(5*t)","cos(11*t)"], "t", [0,2*pi()], nticks=400)    # not tested
        '''
    def plot3d(self, *args) -> None:
        '''
        Plot a 3d graph using Maxima / gnuplot.

        maxima.plot3d(f, \'[x, xmin, xmax]\', \'[y, ymin, ymax]\', \'[grid, nx,
        ny]\', options)

        INPUT:

        - ``f`` -- string representing a function (such as
          f="sin(x)") [var, min, max]

        - ``args`` should be of the form \'[x, xmin, xmax]\', \'[y, ymin, ymax]\',
          \'[grid, nx, ny]\', options

        EXAMPLES::

            sage: maxima.plot3d(\'1 + x^3 - y^2\', \'[x,-2,2]\', \'[y,-2,2]\', \'[grid,12,12]\')    # not tested
            sage: maxima.plot3d(\'sin(x)*cos(y)\', \'[x,-2,2]\', \'[y,-2,2]\', \'[grid,30,30]\')   # not tested
            sage: opts = \'[gnuplot_term, ps], [gnuplot_out_file, "sin-plot.eps"]\'
            sage: maxima.plot3d(\'sin(x+y)\', \'[x,-5,5]\', \'[y,-1,1]\', opts)    # not tested

        The eps file is saved in the current working directory.
        '''
    def plot3d_parametric(self, r, vars, urange, vrange, options=None) -> None:
        '''
        Plot a 3d parametric graph with r=(x,y,z), x = x(u,v), y = y(u,v),
        z = z(u,v), for u = umin...umax, v = vmin...vmax using gnuplot with
        options.

        INPUT:

        - ``x``, ``y``, ``z`` -- string representing a function (such
          as ``x="u2+v2"``, ...) vars is a list or two strings
          representing variables (such as vars = ["u","v"])

        - ``urange`` -- [umin, umax]

        - ``vrange`` -- [vmin, vmax] are lists of numbers with
          umin umax, vmin vmax

        - ``options`` -- (optional) string representing plot2d
          options in gnuplot format

        OUTPUT: displays a plot on screen or saves to a file

        EXAMPLES::

            sage: maxima.plot3d_parametric(["v*sin(u)","v*cos(u)","v"], ["u","v"],[-3.2,3.2],[0,3])     # not tested
            sage: opts = \'[gnuplot_term, ps], [gnuplot_out_file, "sin-cos-plot.eps"]\'
            sage: maxima.plot3d_parametric(["v*sin(u)","v*cos(u)","v"], ["u","v"],[-3.2,3.2],[0,3],opts)      # not tested

        The eps file is saved in the current working directory.

        Here is a torus::

            sage: _ = maxima.eval("expr_1: cos(y)*(10.0+6*cos(x)); expr_2: sin(y)*(10.0+6*cos(x)); expr_3: -6*sin(x);")
            sage: maxima.plot3d_parametric(["expr_1","expr_2","expr_3"], ["x","y"],[0,6],[0,6])  # not tested

        Here is a Möbius strip::

            sage: x = "cos(u)*(3 + v*cos(u/2))"
            sage: y = "sin(u)*(3 + v*cos(u/2))"
            sage: z = "v*sin(u/2)"
            sage: maxima.plot3d_parametric([x,y,z],["u","v"],[-3.1,3.2],[-1/10,1/10])   # not tested
        '''
    def de_solve(self, de, vars, ics=None):
        """
        Solve a 1st or 2nd order ordinary differential equation (ODE) in
        two variables, possibly with initial conditions.

        INPUT:

        - ``de`` -- string representing the ODE

        - ``vars`` -- list of strings representing the two
          variables

        - ``ics`` -- a triple of numbers [a,b1,b2] representing
          y(a)=b1, y'(a)=b2

        EXAMPLES::

            sage: maxima.de_solve('diff(y,x,2) + 3*x = y', ['x','y'], [1,1,1])
            y = 3*x-2*%e^(x-1)
            sage: maxima.de_solve('diff(y,x,2) + 3*x = y', ['x','y'])
            y = %k1*%e^x+%k2*%e^-x+3*x
            sage: maxima.de_solve('diff(y,x) + 3*x = y', ['x','y'])
            y = (%c-3*(...-x...-1)*%e^-x)*%e^x
            sage: maxima.de_solve('diff(y,x) + 3*x = y', ['x','y'],[1,1])
            y = -...%e^-1*(5*%e^x-3*%e*x-3*%e)...
        """
    def de_solve_laplace(self, de, vars, ics=None):
        '''
        Solve an ordinary differential equation (ODE) using Laplace
        transforms.

        INPUT:

        - ``de`` -- string representing the ODE (e.g., de =
          "diff(f(x),x,2)=diff(f(x),x)+sin(x)")

        - ``vars`` -- list of strings representing the
          variables (e.g., ``vars = ["x","f"]``)

        - ``ics`` -- list of numbers representing initial
          conditions, with symbols allowed which are represented by strings
          (eg, f(0)=1, f\'(0)=2 is ics = [0,1,2])

        EXAMPLES::

            sage: maxima.clear(\'x\'); maxima.clear(\'f\')
            sage: maxima.de_solve_laplace("diff(f(x),x,2) = 2*diff(f(x),x)-f(x)", ["x","f"], [0,1,2])
            f(x) = x*%e^x+%e^x

        ::

            sage: maxima.clear(\'x\'); maxima.clear(\'f\')
            sage: f = maxima.de_solve_laplace("diff(f(x),x,2) = 2*diff(f(x),x)-f(x)", ["x","f"])
            sage: f
            f(x) = x*%e^x*(\'at(\'diff(f(x),x,1),x = 0))-f(0)*x*%e^x+f(0)*%e^x
            sage: print(f)
                                               !
                                   x  d        !                  x          x
                        f(x) = x %e  (-- (f(x))!     ) - f(0) x %e  + f(0) %e
                                      dx       !
                                               !x = 0

        .. NOTE::

           The second equation sets the values of `f(0)` and
           `f\'(0)` in Maxima, so subsequent ODEs involving these
           variables will have these initial conditions automatically
           imposed.
        '''
    def solve_linear(self, eqns, vars):
        '''
        Wraps maxima\'s linsolve.

        INPUT:

        - ``eqns`` -- list of m strings; each representing a linear
          question in m = n variables

        - ``vars`` -- list of n strings; each
          representing a variable

        EXAMPLES::

            sage: eqns = ["x + z = y","2*a*x - y = 2*a^2","y - 2*z = 2"]
            sage: vars = ["x","y","z"]
            sage: maxima.solve_linear(eqns, vars)
            [x = a+1,y = 2*a,z = a-1]
        '''
    def unit_quadratic_integer(self, n):
        """
        Finds a unit of the ring of integers of the quadratic number field
        `\\QQ(\\sqrt{n})`, `n>1`, using the qunit maxima command.

        INPUT:

        - ``n`` -- integer

        EXAMPLES::

            sage: u = maxima.unit_quadratic_integer(101); u
            a + 10
            sage: u.parent()
            Number Field in a with defining polynomial x^2 - 101 with a = 10.04987562112089?
            sage: u = maxima.unit_quadratic_integer(13)
            sage: u
            5*a + 18
            sage: u.parent()
            Number Field in a with defining polynomial x^2 - 13 with a = 3.605551275463990?
        """
    def plot_list(self, ptsx, ptsy, options=None) -> None:
        '''
        Plots a curve determined by a sequence of points.

        INPUT:

        - ``ptsx`` -- [x1,...,xn], where the xi and yi are
          real,

        - ``ptsy`` -- [y1,...,yn]

        - ``options`` -- string representing maxima plot2d
          options

        The points are (x1,y1), (x2,y2), etc.

        This function requires maxima 5.9.2 or newer.

        .. NOTE::

           More that 150 points can sometimes lead to the program
           hanging. Why?

        EXAMPLES::

            sage: zeta_ptsx = [(pari(1/2 + i*I/10).zeta().real()).precision(1)          # needs sage.libs.pari
            ....:              for i in range(70,150)]
            sage: zeta_ptsy = [(pari(1/2 + i*I/10).zeta().imag()).precision(1)          # needs sage.libs.pari
            ....:              for i in range(70,150)]
            sage: maxima.plot_list(zeta_ptsx, zeta_ptsy)        # not tested            # needs sage.libs.pari
            sage: opts=\'[gnuplot_preamble, "set nokey"], [gnuplot_term, ps], [gnuplot_out_file, "zeta.eps"]\'
            sage: maxima.plot_list(zeta_ptsx, zeta_ptsy, opts)  # not tested            # needs sage.libs.pari
        '''
    def plot_multilist(self, pts_list, options=None) -> None:
        '''
        Plots a list of list of points pts_list=[pts1,pts2,...,ptsn],
        where each ptsi is of the form [[x1,y1],...,[xn,yn]] x\'s must be
        integers and y\'s reals options is a string representing maxima
        plot2d options.

        INPUT:

        - ``pts_lst`` -- list of points; each point must be of the form [x,y]
          where ``x`` is an integer and ``y`` is a real

        - ``var`` -- string; representing Maxima\'s plot2d options

        Requires maxima 5.9.2 at least.

        .. NOTE::

           More that 150 points can sometimes lead to the program
           hanging.

        EXAMPLES::

            sage: xx = [i/10.0 for i in range(-10,10)]
            sage: yy = [i/10.0 for i in range(-10,10)]
            sage: x0 = [0 for i in range(-10,10)]
            sage: y0 = [0 for i in range(-10,10)]
            sage: zeta_ptsx1 = [(pari(1/2+i*I/10).zeta().real()).precision(1)           # needs sage.libs.pari
            ....:               for i in range(10)]
            sage: zeta_ptsy1 = [(pari(1/2+i*I/10).zeta().imag()).precision(1)           # needs sage.libs.pari
            ....:               for i in range(10)]
            sage: maxima.plot_multilist([[zeta_ptsx1,zeta_ptsy1], [xx,y0], [x0,yy]])    # not tested
            sage: zeta_ptsx1 = [(pari(1/2+i*I/10).zeta().real()).precision(1)           # needs sage.libs.pari
            ....:               for i in range(10,150)]
            sage: zeta_ptsy1 = [(pari(1/2+i*I/10).zeta().imag()).precision(1)           # needs sage.libs.pari
            ....:               for i in range(10,150)]
            sage: maxima.plot_multilist([[zeta_ptsx1,zeta_ptsy1], [xx,y0], [x0,yy]])    # not tested
            sage: opts=\'[gnuplot_preamble, "set nokey"]\'
            sage: maxima.plot_multilist([[zeta_ptsx1,zeta_ptsy1], [xx,y0], [x0,yy]],    # not tested
            ....:                       opts)
        '''

class MaximaAbstractElement(ExtraTabCompletion, InterfaceElement):
    """
    Element of Maxima through an abstract interface.

    EXAMPLES:

    Elements of this class should not be created directly.
    The targeted parent of a concrete inherited class should be used instead::

        sage: from sage.interfaces.maxima_lib import maxima_lib
        sage: xp = maxima(x)
        sage: type(xp)
        <class 'sage.interfaces.maxima.MaximaElement'>
        sage: xl = maxima_lib(x)
        sage: type(xl)
        <class 'sage.interfaces.maxima_lib.MaximaLibElement'>
    """
    def __bool__(self) -> bool:
        """
        Convert ``self`` into a boolean.

        OUTPUT: boolean

        EXAMPLES::

            sage: bool(maxima(0))
            False
            sage: bool(maxima(1))
            True
            sage: bool(maxima('false'))
            False
            sage: bool(maxima('true'))
            True
        """
    def __complex__(self) -> complex:
        """
        Return a complex number equivalent to this Maxima object.

        OUTPUT: complex

        EXAMPLES::

            sage: complex(maxima('sqrt(-2)+1'))
            (1+1.4142135623730951j)
        """
    def real(self):
        """
        Return the real part of this Maxima element.

        OUTPUT: Maxima real

        EXAMPLES::

            sage: maxima('2 + (2/3)*%i').real()
            2
        """
    def imag(self):
        """
        Return the imaginary part of this Maxima element.

        OUTPUT: Maxima real

        EXAMPLES::

            sage: maxima('2 + (2/3)*%i').imag()
            2/3
        """
    def numer(self):
        """
        Return numerical approximation to ``self`` as a Maxima object.

        OUTPUT: Maxima object

        EXAMPLES::

            sage: a = maxima('sqrt(2)').numer(); a
            1.41421356237309...
            sage: type(a)
            <class 'sage.interfaces.maxima.MaximaElement'>
        """
    def str(self):
        """
        Return string representation of this Maxima object.

        OUTPUT: string

        EXAMPLES::

            sage: maxima('sqrt(2) + 1/3').str()
            'sqrt(2)+1/3'
        """
    def diff(self, var: str = 'x', n: int = 1):
        """
        Return the `n`-th derivative of ``self``.

        INPUT:

        - ``var`` -- variable (default: ``'x'``)

        - ``n`` -- integer (default: 1)

        OUTPUT: `n`-th derivative of ``self`` with respect to the variable var

        EXAMPLES::

            sage: f = maxima('x^2')
            sage: f.diff()
            2*x
            sage: f.diff('x')
            2*x
            sage: f.diff('x', 2)
            2
            sage: maxima('sin(x^2)').diff('x',4)
            16*x^4*sin(x^2)-12*sin(x^2)-48*x^2*cos(x^2)

        ::

            sage: f = maxima('x^2 + 17*y^2')
            sage: f.diff('x')
            34*y*'diff(y,x,1)+2*x
            sage: f.diff('y')
            34*y
        """
    derivative = diff
    def nintegral(self, var: str = 'x', a: int = 0, b: int = 1, desired_relative_error: str = '1e-8', maximum_num_subintervals: int = 200):
        """
        Return a numerical approximation to the integral of ``self`` from `a`
        to `b`.

        INPUT:

        - ``var`` -- variable to integrate with respect to

        - ``a`` -- lower endpoint of integration

        - ``b`` -- upper endpoint of integration

        - ``desired_relative_error`` -- (default: ``'1e-8'``) the
          desired relative error

        - ``maximum_num_subintervals`` -- (default: 200)
          maxima number of subintervals

        OUTPUT: approximation to the integral

        - estimated absolute error of the
          approximation

        - the number of integrand evaluations

        - an error code:

            - ``0`` -- no problems were encountered

            - ``1`` -- too many subintervals were done

            - ``2`` -- excessive roundoff error

            - ``3`` -- extremely bad integrand behavior

            - ``4`` -- failed to converge

            - ``5`` -- integral is probably divergent or slowly convergent

            - ``6`` -- the input is invalid

        EXAMPLES::

            sage: maxima('exp(-sqrt(x))').nintegral('x',0,1)
            (0.5284822353142306, 4.163...e-11, 231, 0)

        Note that GP also does numerical integration, and can do so to very
        high precision very quickly::

            sage: gp('intnum(x=0,1,exp(-sqrt(x)))')
            0.52848223531423071361790491935415653022
            sage: _ = gp.set_precision(80)
            sage: gp('intnum(x=0,1,exp(-sqrt(x)))')
            0.52848223531423071361790491935415653021675547587292866196865279321015401702040079
        """
    def integral(self, var: str = 'x', min=None, max=None):
        """
        Return the integral of ``self`` with respect to the variable `x`.

        INPUT:

        - ``var`` -- variable

        - ``min`` -- (default: ``None``)

        - ``max`` -- (default: ``None``)

        OUTPUT: the definite integral if xmin is not ``None``

        - an indefinite integral otherwise

        EXAMPLES::

            sage: maxima('x^2+1').integral()
            x^3/3+x
            sage: maxima('x^2+ 1 + y^2').integral('y')
            y^3/3+x^2*y+y
            sage: maxima('x / (x^2+1)').integral()
            log(x^2+1)/2
            sage: maxima('1/(x^2+1)').integral()
            atan(x)
            sage: maxima('1/(x^2+1)').integral('x', 0, infinity)
            %pi/2
            sage: maxima('x/(x^2+1)').integral('x', -1, 1)
            0

        ::

            sage: f = maxima('exp(x^2)').integral('x',0,1)
            sage: f.sage()
            -1/2*I*sqrt(pi)*erf(I)
            sage: f.numer()
            1.46265174590718...
        """
    integrate = integral
    def __float__(self) -> float:
        '''
        Return floating point version of this Maxima element.

        OUTPUT: real

        EXAMPLES::

            sage: float(maxima("3.14"))
            3.14
            sage: float(maxima("1.7e+17"))
            1.7e+17
            sage: float(maxima("1.7e-17"))
            1.7e-17
        '''
    def __len__(self) -> int:
        """
        Return the length of a list.

        OUTPUT: integer

        EXAMPLES::

            sage: v = maxima('create_list(x^i,i,0,5)')
            sage: len(v)
            6
        """
    def dot(self, other):
        """
        Implement the notation ``self . other``.

        INPUT:

        - ``other`` -- matrix; argument to dot

        OUTPUT: Maxima matrix

        EXAMPLES::

            sage: A = maxima('matrix ([a1],[a2])')
            sage: B = maxima('matrix ([b1, b2])')
            sage: A.dot(B)
            matrix([a1*b1,a1*b2],[a2*b1,a2*b2])
        """
    def __getitem__(self, n):
        """
        Return the `n`-th element of this list.

        INPUT:

        - ``n`` -- integer

        OUTPUT: Maxima object

        .. NOTE::

           Lists are 0-based when accessed via the Sage interface, not
           1-based as they are in the Maxima interpreter.

        EXAMPLES::

            sage: v = maxima('create_list(i*x^i,i,0,5)'); v
            [0,x,2*x^2,3*x^3,4*x^4,5*x^5]
            sage: v[3]
            3*x^3
            sage: v[0]
            0
            sage: v[10]
            Traceback (most recent call last):
            ...
            IndexError: n = (10) must be between 0 and 5
        """
    def __iter__(self):
        """
        Return an iterator for ``self``.

        OUTPUT: iterator

        EXAMPLES::

            sage: v = maxima('create_list(i*x^i,i,0,5)')
            sage: L = list(v)
            sage: [e._sage_() for e in L]
            [0, x, 2*x^2, 3*x^3, 4*x^4, 5*x^5]
        """
    def subst(self, val):
        """
        Substitute a value or several values into this Maxima object.

        INPUT:

        - ``val`` -- string representing substitution(s) to perform

        OUTPUT: Maxima object

        EXAMPLES::

            sage: maxima('a^2 + 3*a + b').subst('b=2')
            a^2+3*a+2
            sage: maxima('a^2 + 3*a + b').subst('a=17')
            b+340
            sage: maxima('a^2 + 3*a + b').subst('a=17, b=2')
            342
        """
    def comma(self, args):
        """
        Form the expression that would be written 'self, args' in Maxima.

        INPUT:

        - ``args`` -- string

        OUTPUT: Maxima object

        EXAMPLES::

            sage: maxima('sqrt(2) + I').comma('numer')
            I+1.41421356237309...
            sage: maxima('sqrt(2) + I*a').comma('a=5')
            5*I+sqrt(2)
        """
    def partial_fraction_decomposition(self, var: str = 'x'):
        """
        Return the partial fraction decomposition of ``self`` with respect to
        the variable var.

        INPUT:

        - ``var`` -- string

        OUTPUT: Maxima object

        EXAMPLES::

            sage: f = maxima('1/((1+x)*(x-1))')
            sage: f.partial_fraction_decomposition('x')
            1/(2*(x-1))-1/(2*(x+1))
            sage: print(f.partial_fraction_decomposition('x'))
                                 1           1
                             --------- - ---------
                             2 (x - 1)   2 (x + 1)
        """
MaximaAbstractFunctionElement = InterfaceFunctionElement
MaximaAbstractFunction = InterfaceFunction

class MaximaAbstractElementFunction(MaximaAbstractElement):
    """
    Create a Maxima function with the parent ``parent``,
    name ``name``, definition ``defn``, arguments ``args``
    and latex representation ``latex``.

    INPUT:

    - ``parent`` -- an instance of a concrete Maxima interface

    - ``name`` -- string

    - ``defn`` -- string

    - ``args`` -- string; comma separated names of arguments

    - ``latex`` -- string

    OUTPUT: Maxima function

    EXAMPLES::

        sage: maxima.function('x,y','e^cos(x)')
        e^cos(x)
    """
    def __init__(self, parent, name, defn, args, latex) -> None:
        """
        Create a Maxima function.
        See ``MaximaAbstractElementFunction`` for full documentation.

        TESTS::

            sage: from sage.interfaces.maxima_abstract import MaximaAbstractElementFunction
            sage: MaximaAbstractElementFunction == loads(dumps(MaximaAbstractElementFunction))
            True
            sage: f = maxima.function('x,y','sin(x+y)')
            sage: f == loads(dumps(f))
            True
        """
    def __reduce__(self):
        """
        Implement __reduce__ for ``MaximaAbstractElementFunction``.

        OUTPUT: a couple consisting of:

        - the function to call for unpickling

        - a tuple of arguments for the function

        EXAMPLES::

            sage: f = maxima.function('x,y','sin(x+y)')
            sage: f.__reduce__()
            (<function reduce_load_MaximaAbstract_function at 0x...>,
             (Maxima, 'sin(x+y)', 'x,y', None))
        """
    def __call__(self, *args):
        """
        Return the result of calling this Maxima function
        with the given arguments.

        INPUT:

        - ``args`` -- a variable number of arguments

        OUTPUT: Maxima object

        EXAMPLES::

            sage: f = maxima.function('x,y','sin(x+y)')
            sage: f(1,2)
            sin(3)
            sage: f(x,x)
            sin(2*x)
        """
    def arguments(self, split: bool = True):
        """
        Return the arguments of this Maxima function.

        INPUT:

        - ``split`` -- boolean; if ``True`` return a tuple of strings,
          otherwise return a string of comma-separated arguments

        OUTPUT: string if ``split`` is False

        - a list of strings if ``split`` is True

        EXAMPLES::

            sage: f = maxima.function('x,y','sin(x+y)')
            sage: f.arguments()
            ['x', 'y']
            sage: f.arguments(split=False)
            'x,y'
            sage: f = maxima.function('', 'sin(x)')
            sage: f.arguments()
            []
        """
    def definition(self):
        """
        Return the definition of this Maxima function as a string.

        EXAMPLES::

            sage: f = maxima.function('x,y','sin(x+y)')
            sage: f.definition()
            'sin(x+y)'
        """
    def integral(self, var):
        """
        Return the integral of ``self`` with respect to the variable var.

        INPUT:

        - ``var`` -- a variable

        OUTPUT: Maxima function

        Note that integrate is an alias of integral.

        EXAMPLES::

            sage: x,y = var('x,y')
            sage: f = maxima.function('x','sin(x)')
            sage: f.integral(x)
            -cos(x)
            sage: f.integral(y)
            sin(x)*y
        """
    integrate = integral

def reduce_load_MaximaAbstract_function(parent, defn, args, latex):
    """
    Unpickle a Maxima function.

    EXAMPLES::

        sage: from sage.interfaces.maxima_abstract import reduce_load_MaximaAbstract_function
        sage: f = maxima.function('x,y','sin(x+y)')
        sage: _,args = f.__reduce__()
        sage: g = reduce_load_MaximaAbstract_function(*args)
        sage: g == f
        True
    """
def maxima_version():
    """
    Return Maxima version.

    Currently this calls a new copy of Maxima.

    EXAMPLES::

        sage: from sage.interfaces.maxima_abstract import maxima_version
        sage: maxima_version()  # random
        '5.41.0'
    """
def maxima_console() -> None:
    """
    Spawn a new Maxima command-line session.

    EXAMPLES::

        sage: from sage.interfaces.maxima_abstract import maxima_console
        sage: maxima_console()                    # not tested
        Maxima 5.46.0 https://maxima.sourceforge.io
        ...
    """
