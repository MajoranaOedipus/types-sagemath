r"""
Interface to Mathics

Mathics is an open source interpreter for the Wolfram Language.
From the introduction of its reference manual:

.. NOTE::

    Mathics — to be pronounced like “Mathematics” without the
    “emat” — is a general-purpose computer algebra system (CAS).
    It is meant to be a free, light-weight alternative to
    Mathematica®. It is free both as in “free beer” and as in
    “freedom”. There are various online mirrors running
    Mathics but it is also possible to run Mathics locally.
    A list of mirrors can be found at the Mathics homepage,
    http://mathics.github.io.

    The programming language of Mathics is meant to resemble
    Wolfram’s famous Mathematica® as much as possible. However,
    Mathics is in no way affiliated or supported by Wolfram.
    Mathics will probably never have the power to compete with
    Mathematica® in industrial applications; yet, it might be
    an interesting alternative for educational purposes.

The Mathics interface will only work if the optional Sage package Mathics
is installed. The interface lets you send certain Sage objects to Mathics,
run Mathics functions, import certain Mathics expressions to Sage,
or any combination of the above.

To send a Sage object ``sobj`` to Mathics, call ``mathics(sobj)``.
This exports the Sage object to Mathics and returns a new Sage object
wrapping the Mathics expression/variable, so that you can use the
Mathics variable from within Sage. You can then call Mathics
functions on the new object; for example::

    sage: from sage.interfaces.mathics import mathics
    sage: mobj = mathics(x^2-1); mobj       # optional - mathics
    -1 + x ^ 2
    sage: mobj.Factor()                     # optional - mathics
    (-1 + x) (1 + x)

In the above example the factorization is done using Mathics's
``Factor[]`` function.

To see Mathics's output you can simply print the Mathics wrapper
object. However if you want to import Mathics's output back to Sage,
call the Mathics wrapper object's ``sage()`` method. This method returns
a native Sage object::

    sage: # optional - mathics
    sage: mobj = mathics(x^2-1)
    sage: mobj2 = mobj.Factor(); mobj2
    (-1 + x) (1 + x)
    sage: mobj2.parent()
    Mathics
    sage: sobj = mobj2.sage(); sobj
    (x + 1)*(x - 1)
    sage: sobj.parent()
    Symbolic Ring


If you want to run a Mathics function and don't already have the input
in the form of a Sage object, then it might be simpler to input a string to
``mathics(expr)``. This string will be evaluated as if you had typed it
into Mathics::

    sage: mathics('Factor[x^2-1]')          # optional - mathics
    (-1 + x) (1 + x)
    sage: mathics('Range[3]')               # optional - mathics
    {1, 2, 3}

If you want work with the internal Mathics expression, then you can call
``mathics.eval(expr)``, which returns an instance of
:class:`mathics.core.expression.Expression`. If you want the result to
be a string formatted like Mathics's InputForm, call ``repr(mobj)`` on
the wrapper object ``mobj``. If you want a string formatted in Sage style,
call ``mobj._sage_repr()``::

    sage: mathics.eval('x^2 - 1')           # optional - mathics
    '-1 + x ^ 2'
    sage: repr(mathics('Range[3]'))         # optional - mathics
    '{1, 2, 3}'
    sage: mathics('Range[3]')._sage_repr()  # optional - mathics
    '[1, 2, 3]'

Finally, if you just want to use a Mathics command line from within
Sage, the function ``mathics_console()`` dumps you into an interactive
command-line Mathics session.

Tutorial
--------

We follow some of the tutorial from
http://library.wolfram.com/conferences/devconf99/withoff/Basic1.html/.


Syntax
~~~~~~

Now make 1 and add it to itself. The result is a Mathics
object.

::

    sage: m = mathics
    sage: a = m(1) + m(1); a                # optional - mathics
    2
    sage: a.parent()                        # optional - mathics
    Mathics
    sage: m('1+1')                          # optional - mathics
    2
    sage: m(3)**m(50)                       # optional - mathics
    717897987691852588770249

The following is equivalent to ``Plus[2, 3]`` in
Mathics::

    sage: m = mathics
    sage: m(2).Plus(m(3))                   # optional - mathics
    5

We can also compute `7(2+3)`.

::

    sage: m(7).Times(m(2).Plus(m(3)))       # optional - mathics
    35
    sage: m('7(2+3)')                       # optional - mathics
    35

Some typical input
~~~~~~~~~~~~~~~~~~

We solve an equation and a system of two equations::

    sage: # optional - mathics
    sage: eqn = mathics('3x + 5 == 14')
    sage: eqn
    5 + 3 x == 14
    sage: eqn.Solve('x')
    {{x -> 3}}
    sage: sys = mathics('{x^2 - 3y == 3, 2x - y == 1}')
    sage: print(sys)
    {x ^ 2 - 3 y == 3, 2 x - y == 1}
    sage: sys.Solve('{x, y}')
    {{x -> 0, y -> -1}, {x -> 6, y -> 11}}

Assignments and definitions
~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you assign the mathics `5` to a variable `c`
in Sage, this does not affect the `c` in Mathics.

::

    sage: c = m(5)                          # optional - mathics
    sage: print(m('b + c x'))               # optional - mathics
                 b + c x
    sage: print(m('b') + c*m('x'))          # optional - mathics
             b + 5 x

The Sage interfaces changes Sage lists into Mathics lists::

    sage: m = mathics
    sage: eq1 = m('x^2 - 3y == 3')          # optional - mathics
    sage: eq2 = m('2x - y == 1')            # optional - mathics
    sage: v = m([eq1, eq2]); v              # optional - mathics
    {x ^ 2 - 3 y == 3, 2 x - y == 1}
    sage: v.Solve(['x', 'y'])               # optional - mathics
    {{x -> 0, y -> -1}, {x -> 6, y -> 11}}

Function definitions
~~~~~~~~~~~~~~~~~~~~

Define mathics functions by simply sending the definition to
the interpreter.

::

    sage: m = mathics
    sage: _ = mathics('f[p_] = p^2');       # optional - mathics
    sage: m('f[9]')                         # optional - mathics
    81

Numerical Calculations
~~~~~~~~~~~~~~~~~~~~~~

We find the `x` such that `e^x - 3x = 0`.

::

    sage: eqn = mathics('Exp[x] - 3x == 0') # optional - mathics
    sage: eqn.FindRoot(['x', 2])            # optional - mathics
    {x -> 1.51213}

Note that this agrees with what the PARI interpreter gp produces::

    sage: gp('solve(x=1,2,exp(x)-3*x)')
    1.5121345516578424738967396780720387046

Next we find the minimum of a polynomial using the two different
ways of accessing Mathics::

    sage: mathics('FindMinimum[x^3 - 6x^2 + 11x - 5, {x,3}]')  # not tested (since not supported, so far)
    {0.6150998205402516, {x -> 2.5773502699629733}}
    sage: f = mathics('x^3 - 6x^2 + 11x - 5')                  # optional - mathics
    sage: f.FindMinimum(['x', 3])                              # not tested (since not supported, so far)
    {0.6150998205402516, {x -> 2.5773502699629733}}

Polynomial and Integer Factorization
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We factor a polynomial of degree 200 over the integers.

::

    sage: R.<x> = PolynomialRing(ZZ)
    sage: f = (x**100+17*x+5)*(x**100-5*x+20)
    sage: f
    x^200 + 12*x^101 + 25*x^100 - 85*x^2 + 315*x + 100
    sage: g = mathics(str(f))                # optional - mathics
    sage: print(g)                           # optional - mathics
    100 + 315 x - 85 x ^ 2 + 25 x ^ 100 + 12 x ^ 101 + x ^ 200
    sage: g                                  # optional - mathics
    100 + 315 x - 85 x ^ 2 + 25 x ^ 100 + 12 x ^ 101 + x ^ 200
    sage: print(g.Factor())                  # optional - mathics
    (5 + 17 x + x ^ 100) (20 - 5 x + x ^ 100)

We can also factor a multivariate polynomial::

    sage: f = mathics('x^6 + (-y - 2)*x^5 + (y^3 + 2*y)*x^4 - y^4*x^3')  # optional - mathics
    sage: print(f.Factor())                  # optional - mathics
    x ^ 3 (x - y) (-2 x + x ^ 2 + y ^ 3)

We factor an integer::

    sage: # optional - mathics
    sage: n = mathics(2434500)
    sage: n.FactorInteger()
    {{2, 2}, {3, 2}, {5, 3}, {541, 1}}
    sage: n = mathics(2434500)
    sage: F = n.FactorInteger(); F
    {{2, 2}, {3, 2}, {5, 3}, {541, 1}}
    sage: F[1]
    {2, 2}
    sage: F[4]
    {541, 1}


Long Input
----------

The Mathics interface reads in even very long input (using
files) in a robust manner.

::

    sage: t = '"%s"'%10^10000   # ten thousand character string.
    sage: a = mathics(t)        # optional - mathics
    sage: a = mathics.eval(t)   # optional - mathics

Loading and saving
------------------

Mathics has an excellent ``InputForm`` function,
which makes saving and loading Mathics objects possible. The
first examples test saving and loading to strings.

::

    sage: # optional - mathics
    sage: x = mathics(pi/2)
    sage: print(x)
    Pi / 2
    sage: loads(dumps(x)) == x
    True
    sage: n = x.N(50)
    sage: print(n)
                  1.5707963267948966192313216916397514420985846996876
    sage: loads(dumps(n)) == n
    True

Complicated translations
------------------------

The ``mobj.sage()`` method tries to convert a Mathics object to a Sage
object. In many cases, it will just work. In particular, it should be able to
convert expressions entirely consisting of:

- numbers, i.e. integers, floats, complex numbers;
- functions and named constants also present in Sage, where:

    - Sage knows how to translate the function or constant's name from
      Mathics's, or
    - the Sage name for the function or constant is trivially related to
      Mathics's;

- symbolic variables whose names don't pathologically overlap with
  objects already defined in Sage.

This method will not work when Mathics's output includes:

- strings;
- functions unknown to Sage;
- Mathics functions with different parameters/parameter order to
  the Sage equivalent.

If you want to convert more complicated Mathics expressions, you can
instead call ``mobj._sage_()`` and supply a translation dictionary::

    sage: x = var('x')
    sage: m = mathics('NewFn[x]')                 # optional - mathics
    sage: m._sage_(locals={'NewFn': sin, 'x':x})  # optional - mathics
    sin(x)

For more details, see the documentation for ``._sage_()``.


OTHER Examples::

    sage: def math_bessel_K(nu, x):
    ....:     return mathics(nu).BesselK(x).N(20)
    sage: math_bessel_K(2,I)                      # optional - mathics
    -2.5928861754911969782 + 0.18048997206696202663 I

::

    sage: slist = [[1, 2], 3., 4 + I]
    sage: mlist = mathics(slist); mlist         # optional - mathics
    {{1, 2}, 3., 4 + I}
    sage: slist2 = list(mlist); slist2          # optional - mathics
    [{1, 2}, 3., 4 + I]
    sage: slist2[0]                             # optional - mathics
    {1, 2}
    sage: slist2[0].parent()                    # optional - mathics
    Mathics
    sage: slist3 = mlist.sage(); slist3         # optional - mathics
    [[1, 2], 3.00000000000000, 4.00000000000000 + 1.00000000000000*I]

::

    sage: mathics('10.^80')         # optional - mathics
    1.×10^80
    sage: mathics('10.^80').sage()  # optional - mathics
    1.00000000000000e80

AUTHORS:

- Sebastian Oehms (2021): first version from a copy of the Mathematica interface (see :issue:`31778`).


Thanks to Rocky Bernstein and Juan Mauricio Matera for their support. For further acknowledgments see `this list <https://github.com/mathics/Mathics/blob/master/AUTHORS.txt>`__.

TESTS:

Check that numerical approximations via Mathics's `N[]` function work
correctly (:issue:`18888`, :issue:`28907`)::

    sage: # optional - mathics
    sage: mathics('Pi/2').N(10)
    1.570796327
    sage: mathics('Pi').N(10)
    3.141592654
    sage: mathics('Pi').N(50)
    3.1415926535897932384626433832795028841971693993751
    sage: str(mathics('Pi*x^2-1/2').N())
    '-0.5 + 3.14159 x ^ 2.'

Check that Mathics's `E` exponential symbol is correctly backtranslated
as Sage's `e` (:issue:`29833`)::

    sage: (e^x)._mathics_().sage()  # optional -- mathics
    e^x
    sage: exp(x)._mathics_().sage() # optional -- mathics
    e^x
"""

from sage.interfaces.interface import Interface as Interface, InterfaceElement as InterfaceElement, InterfaceFunction as InterfaceFunction, InterfaceFunctionElement as InterfaceFunctionElement
from sage.interfaces.tab_completion import ExtraTabCompletion as ExtraTabCompletion
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.instancedoc import instancedoc as instancedoc
from sage.structure.richcmp import rich_to_bool as rich_to_bool

class Mathics(Interface):
    """
    Interface to the Mathics interpreter.

    Implemented according to the Mathematica interface but avoiding Pexpect
    functionality.

    EXAMPLES::

        sage: # optional - mathics
        sage: t = mathics('Tan[I + 0.5]')
        sage: t.parent()
        Mathics
        sage: ts = t.sage()
        sage: ts.parent()
        Complex Field with 53 bits of precision
        sage: t == mathics(ts)
        True
        sage: mtan = mathics.Tan
        sage: mt = mtan(I+1/2)
        sage: mt == t
        True
        sage: u = mathics(I+1/2)
        sage: u.Tan() == mt
        True


    More examples can be found in the module header.
    """
    def __init__(self, maxread=None, logfile=None, init_list_length: int = 1024, seed=None) -> None:
        """
        Python constructor.

        EXAMPLES::

            sage: mathics._mathics_init_ == mathics._mathematica_init_
            True
        """
    def eval(self, code, *args, **kwds):
        """
        Evaluates a command inside the Mathics interpreter and returns the output
        in printable form.

        EXAMPLES::

            sage: mathics.eval('1+1')  # optional - mathics
            '2'
        """
    def set(self, var, value) -> None:
        """
        Set the variable var to the given value.

        EXAMPLES::

            sage: mathics.set('u', '2*x +E')         # optional - mathics
            sage: bool(mathics('u').sage() == 2*x+e) # optional - mathics
            True
        """
    def get(self, var):
        """
        Get the value of the variable var.

        EXAMPLES::

            sage: mathics.set('u', '2*x +E')        # optional - mathics
            sage: mathics.get('u')                  # optional - mathics
            '2 x + E'
        """
    def chdir(self, dir) -> None:
        """
        Change Mathics's current working directory.

        EXAMPLES::

            sage: mathics.chdir('/')          # optional - mathics
            sage: mathics('Directory[]')      # optional - mathics
            /
        """
    def console(self) -> None:
        """
        Spawn a new Mathics command-line session.

        EXAMPLES::

            sage: mathics.console()  # not tested

            Mathics 2.1.1.dev0
            on CPython 3.9.2 (default, Mar 19 2021, 22:23:28)
            using SymPy 1.7, mpmath 1.2.1, numpy 1.19.5, cython 0.29.21

            Copyright (C) 2011-2021 The Mathics Team.
            This program comes with ABSOLUTELY NO WARRANTY.
            This is free software, and you are welcome to redistribute it
            under certain conditions.
            See the documentation for the full license.

            Quit by evaluating Quit[] or by pressing CONTROL-D.

            In[1]:= Sin[0.5]
            Out[1]= 0.479426

            Goodbye!

            sage:
        """
    def help(self, cmd, long: bool = False):
        """
        Return the Mathics documentation of the given command.

        EXAMPLES::

            sage: mathics.help('Sin')                   # optional - mathics
            'sine function\\n'

            sage: print(_)                              # optional - mathics
            sine function
            <BLANKLINE>

            sage: print(mathics.help('Sin', long=True)) # optional - mathics
            sine function
            <BLANKLINE>
            Attributes[Sin] = {Listable, NumericFunction, Protected}
            <BLANKLINE>

            sage: print(mathics.Factorial.__doc__)  # optional - mathics
            factorial
            <BLANKLINE>

            sage: u = mathics('Pi')                 # optional - mathics
            sage: print(u.Cos.__doc__)              # optional - mathics
            cosine function
            <BLANKLINE>
        """
    def __getattr__(self, attrname):
        """
        EXAMPLES::

            sage: msin = mathics.Sin           # optional - mathics
            sage: msin(0.2)                    # optional - mathics
            0.19866933079506123
            sage: _ == sin(0.2)                # optional - mathics
            True
        """

class MathicsElement(ExtraTabCompletion, InterfaceElement):
    """
    Element class of the Mathics interface.

    Its instances are usually constructed via the instance call of its parent.
    It wrapes the Mathics library for this object. In a session Mathics methods
    can be obtained using tab completion.

    EXAMPLES::

        sage: # optional - mathics
        sage: me=mathics(e); me
        E
        sage: type(me)
        <class 'sage.interfaces.mathics.MathicsElement'>
        sage: P = me.parent(); P
        Mathics
        sage: type(P)
        <class 'sage.interfaces.mathics.Mathics'>

    Access to the Mathics expression objects::

        sage: # optional - mathics
        sage: res = me._mathics_result
        sage: type(res)
        <class 'mathics.core.evaluation.Result'>
        sage: expr = res.last_eval; expr
        <Symbol: System`E>
        sage: type(expr)
        <class 'mathics.core.symbols.Symbol'>

    Applying Mathics methods::

        sage: # optional - mathics
        sage: me.to_sympy()
        E
        sage: me.get_name()
        'System`E'
        sage: me.is_inexact()
        False

    Conversion to Sage::

        sage: bool(me.sage() == e)             # optional - mathics
        True
    """
    def __getitem__(self, n):
        """
        EXAMPLES::

            sage: l = mathics('{1, x, .15}')  # optional - mathics
            sage: l[0]                        # optional - mathics
            List
            sage: for i in l: print(i)        # optional - mathics
            1
            x
            0.15
        """
    def __getattr__(self, attrname):
        """
        EXAMPLES::

            sage: # optional - mathics
            sage: a = mathics(5*x)
            sage: res = a._mathics_result
            sage: str(a) == res.result
            True
            sage: t = mathics._eval('5*x')
            sage: t.last_eval  == res.last_eval
            True
        """
    def __float__(self, precision: int = 16) -> float:
        """
        EXAMPLES::

            sage: float(mathics('Pi')) == float(pi)  # optional - mathics
            True
        """
    def __reduce__(self):
        """
        EXAMPLES::

            sage: mpol = mathics('x + y*z')     # optional - mathics
            sage: loads(dumps(mpol)) == mpol    # optional - mathics
            True
        """
    def __len__(self) -> int:
        """
        Return the object's length, evaluated by mathics.

        EXAMPLES::

            sage: len(mathics([1,1.,2]))    # optional - mathics
            3
        """
    def save_image(self, filename, ImageSize: int = 600) -> None:
        """
        Save a mathics graphics.

        INPUT:

        - ``filename`` -- string; the filename to save as. The
          extension determines the image file format

        - ``ImageSize`` -- integer; the size of the resulting image

        EXAMPLES::

            sage: P = mathics('Plot[Sin[x],{x,-2Pi,4Pi}]')   # optional - mathics
            sage: filename = tmp_filename()                  # optional - mathics
            sage: P.save_image(filename, ImageSize=800)      # optional - mathics
        """
    def show(self, ImageSize: int = 600) -> None:
        """
        Show a mathics expression immediately.

        This method attempts to display the graphics immediately,
        without waiting for the currently running code (if any) to
        return to the command line. Be careful, calling it from within
        a loop will potentially launch a large number of external
        viewer programs.

        INPUT:

        - ``ImageSize`` -- integer; the size of the resulting image

        OUTPUT:

        This method does not return anything. Use :meth:`save` if you
        want to save the figure as an image.

        EXAMPLES::

            sage: Q = mathics('Sin[x Cos[y]]/Sqrt[1-x^2]')   # optional - mathics
            sage: show(Q)                                    # optional - mathics
            Sin[x Cos[y]] / Sqrt[1 - x ^ 2]

            sage: P = mathics('Plot[Sin[x],{x,-2Pi,4Pi}]')   # optional - mathics
            sage: show(P)                                    # optional - mathics
            sage: P.show(ImageSize=800)                      # optional - mathics
        """
    def __bool__(self) -> bool:
        """
        Return whether this Mathics element is not identical to ``False``.

        EXAMPLES::

            sage: bool(mathics(True))   # optional - mathics
            True
            sage: bool(mathics(False))  # optional - mathics
            False

        In Mathics, `0` cannot be used to express falsity::

            sage: bool(mathics(0))     # optional - mathics
            True
        """
    def n(self, *args, **kwargs):
        """
        Numerical approximation by converting to Sage object first.

        Convert the object into a Sage object and return its numerical
        approximation. See documentation of the function
        :func:`sage.misc.functional.n` for details.

        EXAMPLES::

            sage: mathics('Pi').n(10)    # optional -- mathics
            3.1
            sage: mathics('Pi').n()      # optional -- mathics
            3.14159265358979
            sage: mathics('Pi').n(digits=10)   # optional -- mathics
            3.141592654
        """

mathics: Mathics

def reduce_load(X):
    """
    Used in unpickling a Mathics element.

    This function is just the ``__call__`` method of the interface instance.

    EXAMPLES::

        sage: sage.interfaces.mathics.reduce_load('Denominator[a / b]')  # optional -- mathics
        b
    """
def mathics_console() -> None:
    """
    Spawn a new Mathics command-line session.

    EXAMPLES::

        sage: mathics_console()  # not tested

        Mathics 2.1.1.dev0
        on CPython 3.9.2 (default, Mar 19 2021, 22:23:28)
        using SymPy 1.7, mpmath 1.2.1, numpy 1.19.5, cython 0.29.21

        Copyright (C) 2011-2021 The Mathics Team.
        This program comes with ABSOLUTELY NO WARRANTY.
        This is free software, and you are welcome to redistribute it
        under certain conditions.
        See the documentation for the full license.

        Quit by evaluating Quit[] or by pressing CONTROL-D.

        In[1]:= Sin[0.5]
        Out[1]= 0.479426

        Goodbye!
    """
