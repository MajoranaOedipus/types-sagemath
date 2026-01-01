r"""
Interface to Mathematica

The Mathematica interface will only work if Mathematica is installed on your
computer with a command line interface that runs when you give the ``math``
command. The interface lets you send certain Sage objects to Mathematica,
run Mathematica functions, import certain Mathematica expressions to Sage,
or any combination of the above.
The Sage command::

    sage: print(mathematica._install_hints())
    ...

prints more information on Mathematica installation.

To send a Sage object ``sobj`` to Mathematica, call ``mathematica(sobj)``.
This exports the Sage object to Mathematica and returns a new Sage object
wrapping the Mathematica expression/variable, so that you can use the
Mathematica variable from within Sage. You can then call Mathematica
functions on the new object; for example::

    sage: mobj = mathematica(x^2-1)             # optional - mathematica
    sage: mobj.Factor()                         # optional - mathematica
    (-1 + x)*(1 + x)

In the above example the factorization is done using Mathematica's
``Factor[]`` function.

To see Mathematica's output you can simply print the Mathematica wrapper
object. However if you want to import Mathematica's output back to Sage,
call the Mathematica wrapper object's ``sage()`` method. This method returns
a native Sage object::

    sage: # optional - mathematica
    sage: mobj = mathematica(x^2-1)
    sage: mobj2 = mobj.Factor(); mobj2
    (-1 + x)*(1 + x)
    sage: mobj2.parent()
    Mathematica
    sage: sobj = mobj2.sage(); sobj
    (x + 1)*(x - 1)
    sage: sobj.parent()
    Symbolic Ring


If you want to run a Mathematica function and don't already have the input
in the form of a Sage object, then it might be simpler to input a string to
``mathematica(expr)``. This string will be evaluated as if you had typed it
into Mathematica::

    sage: mathematica('Factor[x^2-1]')          # optional - mathematica
    (-1 + x)*(1 + x)
    sage: mathematica('Range[3]')               # optional - mathematica
    {1, 2, 3}

If you don't want Sage to go to the trouble of creating a wrapper for the
Mathematica expression, then you can call ``mathematica.eval(expr)``, which
returns the result as a Mathematica AsciiArtString formatted string. If you
want the result to be a string formatted like Mathematica's InputForm, call
``repr(mobj)`` on the wrapper object ``mobj``. If you want a string
formatted in Sage style, call ``mobj._sage_repr()``::

    sage: mathematica.eval('x^2 - 1')           # optional - mathematica
                   2
             -1 + x
    sage: repr(mathematica('Range[3]'))         # optional - mathematica
    '{1, 2, 3}'
    sage: mathematica('Range[3]')._sage_repr()  # optional - mathematica
    '[1, 2, 3]'

Finally, if you just want to use a Mathematica command line from within
Sage, the function ``mathematica_console()`` dumps you into an interactive
command-line Mathematica session. This is an enhanced version of the usual
Mathematica command-line, in that it provides readline editing and history
(the usual one doesn't!)

Tutorial
--------

We follow some of the tutorial from
http://library.wolfram.com/conferences/devconf99/withoff/Basic1.html/.

For any of this to work you must buy and install the Mathematica
program, and it must be available as the command
``math`` in your PATH.

Syntax
~~~~~~

Now make 1 and add it to itself. The result is a Mathematica
object.

::

    sage: m = mathematica
    sage: a = m(1) + m(1); a                # optional - mathematica
    2
    sage: a.parent()                        # optional - mathematica
    Mathematica
    sage: m('1+1')                          # optional - mathematica
    2
    sage: m(3)**m(50)                       # optional - mathematica
    717897987691852588770249

The following is equivalent to ``Plus[2, 3]`` in
Mathematica::

    sage: m = mathematica
    sage: m(2).Plus(m(3))                   # optional - mathematica
    5

We can also compute `7(2+3)`.

::

    sage: m(7).Times(m(2).Plus(m(3)))       # optional - mathematica
    35
    sage: m('7(2+3)')                       # optional - mathematica
    35

Some typical input
~~~~~~~~~~~~~~~~~~

We solve an equation and a system of two equations::

    sage: # optional - mathematica
    sage: eqn = mathematica('3x + 5 == 14')
    sage: eqn
    5 + 3*x == 14
    sage: eqn.Solve('x')
    {{x -> 3}}
    sage: sys = mathematica('{x^2 - 3y == 3, 2x - y == 1}')
    sage: print(sys)
               2
             {x  - 3 y == 3, 2 x - y == 1}
    sage: sys.Solve('{x, y}')
    {{x -> 0, y -> -1}, {x -> 6, y -> 11}}

Assignments and definitions
~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you assign the mathematica `5` to a variable `c`
in Sage, this does not affect the `c` in Mathematica.

::

    sage: c = m(5)                          # optional - mathematica
    sage: print(m('b + c x'))               # optional - mathematica
                 b + c x
    sage: print(m('b') + c*m('x'))          # optional - mathematica
             b + 5 x

The Sage interfaces changes Sage lists into Mathematica lists::

    sage: m = mathematica
    sage: eq1 = m('x^2 - 3y == 3')          # optional - mathematica
    sage: eq2 = m('2x - y == 1')            # optional - mathematica
    sage: v = m([eq1, eq2]); v              # optional - mathematica
    {x^2 - 3*y == 3, 2*x - y == 1}
    sage: v.Solve(['x', 'y'])               # optional - mathematica
    {{x -> 0, y -> -1}, {x -> 6, y -> 11}}

Function definitions
~~~~~~~~~~~~~~~~~~~~

Define mathematica functions by simply sending the definition to
the interpreter.

::

    sage: m = mathematica
    sage: _ = mathematica('f[p_] = p^2');   # optional - mathematica
    sage: m('f[9]')                         # optional - mathematica
    81

Numerical Calculations
~~~~~~~~~~~~~~~~~~~~~~

We find the `x` such that `e^x - 3x = 0`.

::

    sage: eqn = mathematica('Exp[x] - 3x == 0') # optional - mathematica
    sage: eqn.FindRoot(['x', 2])                # optional - mathematica
    {x -> 1.512134551657842}

Note that this agrees with what the PARI interpreter gp produces::

    sage: gp('solve(x=1,2,exp(x)-3*x)')
    1.5121345516578424738967396780720387046

Next we find the minimum of a polynomial using the two different
ways of accessing Mathematica::

    sage: mathematica('FindMinimum[x^3 - 6x^2 + 11x - 5, {x,3}]')  # optional - mathematica
    {0.6150998205402516, {x -> 2.5773502699629733}}
    sage: f = mathematica('x^3 - 6x^2 + 11x - 5')  # optional - mathematica
    sage: f.FindMinimum(['x', 3])                  # optional - mathematica
    {0.6150998205402516, {x -> 2.5773502699629733}}

Polynomial and Integer Factorization
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We factor a polynomial of degree 200 over the integers.

::

    sage: R.<x> = PolynomialRing(ZZ)
    sage: f = (x**100+17*x+5)*(x**100-5*x+20)
    sage: f
    x^200 + 12*x^101 + 25*x^100 - 85*x^2 + 315*x + 100
    sage: g = mathematica(str(f))            # optional - mathematica
    sage: print(g)                           # optional - mathematica
                               2       100       101    200
             100 + 315 x - 85 x  + 25 x    + 12 x    + x
    sage: g                                  # optional - mathematica
    100 + 315*x - 85*x^2 + 25*x^100 + 12*x^101 + x^200
    sage: print(g.Factor())                  # optional - mathematica
                          100               100
             (20 - 5 x + x   ) (5 + 17 x + x   )

We can also factor a multivariate polynomial::

    sage: f = mathematica('x^6 + (-y - 2)*x^5 + (y^3 + 2*y)*x^4 - y^4*x^3')  # optional - mathematica
    sage: print(f.Factor())                  # optional - mathematica
              3                  2    3
             x  (x - y) (-2 x + x  + y )

We factor an integer::

    sage: # optional - mathematica
    sage: n = mathematica(2434500)
    sage: n.FactorInteger()
    {{2, 2}, {3, 2}, {5, 3}, {541, 1}}
    sage: n = mathematica(2434500)
    sage: F = n.FactorInteger(); F
    {{2, 2}, {3, 2}, {5, 3}, {541, 1}}
    sage: F[1]
    {2, 2}
    sage: F[4]
    {541, 1}

Mathematica's ECM package is no longer available.

Long Input
----------

The Mathematica interface reads in even very long input (using
files) in a robust manner.

::

    sage: t = '"%s"'%10^10000   # ten thousand character string.
    sage: a = mathematica(t)        # optional - mathematica
    sage: a = mathematica.eval(t)   # optional - mathematica

Loading and saving
------------------

Mathematica has an excellent ``InputForm`` function,
which makes saving and loading Mathematica objects possible. The
first examples test saving and loading to strings.

::

    sage: # optional - mathematica
    sage: x = mathematica(pi/2)
    sage: print(x)
             Pi
             --
             2
    sage: loads(dumps(x)) == x
    True
    sage: n = x.N(50)
    sage: print(n)
                  1.5707963267948966192313216916397514420985846996876
    sage: loads(dumps(n)) == n
    True

Complicated translations
------------------------

The ``mobj.sage()`` method tries to convert a Mathematica object to a Sage
object. In many cases, it will just work. In particular, it should be able to
convert expressions entirely consisting of:

- numbers, i.e. integers, floats, complex numbers;
- functions and named constants also present in Sage, where:

    - Sage knows how to translate the function or constant's name from
      Mathematica's, or
    - the Sage name for the function or constant is trivially related to
      Mathematica's;

- symbolic variables whose names don't pathologically overlap with
  objects already defined in Sage.

This method will not work when Mathematica's output includes:

- strings;
- functions unknown to Sage;
- Mathematica functions with different parameters/parameter order to
  the Sage equivalent.

If you want to convert more complicated Mathematica expressions, you can
instead call ``mobj._sage_()`` and supply a translation dictionary::

    sage: m = mathematica('NewFn[x]')       # optional - mathematica
    sage: m._sage_(locals={('NewFn', 1): sin})   # optional - mathematica
    sin(x)

For more details, see the documentation for ``._sage_()``.


OTHER Examples::

    sage: def math_bessel_K(nu, x):
    ....:     return mathematica(nu).BesselK(x).N(20)
    sage: math_bessel_K(2,I)                      # optional - mathematica
    -2.59288617549119697817 + 0.18048997206696202663*I

::

    sage: slist = [[1, 2], 3., 4 + I]
    sage: mlist = mathematica(slist); mlist     # optional - mathematica
    {{1, 2}, 3., 4 + I}
    sage: slist2 = list(mlist); slist2          # optional - mathematica
    [{1, 2}, 3., 4 + I]
    sage: slist2[0]                             # optional - mathematica
    {1, 2}
    sage: slist2[0].parent()                    # optional - mathematica
    Mathematica
    sage: slist3 = mlist.sage(); slist3         # optional - mathematica
    [[1, 2], 3.00000000000000, I + 4]

::

    sage: mathematica('10.^80')     # optional - mathematica
    1.*^80
    sage: mathematica('10.^80').sage()  # optional - mathematica
    1.00000000000000e80

AUTHORS:

- William Stein (2005): first version

- Doug Cutrell (2006-03-01): Instructions for use under Cygwin/Windows.

- Felix Lawrence (2009-08-21): Added support for importing Mathematica lists
  and floats with exponents.

TESTS:

Check that numerical approximations via Mathematica's `N[]` function work
correctly (:issue:`18888`, :issue:`28907`)::

    sage: # optional - mathematica
    sage: mathematica('Pi/2').N(10)
    1.5707963268
    sage: mathematica('Pi').N(10)
    3.1415926536
    sage: mathematica('Pi').N(50)
    3.14159265358979323846264338327950288419716939937511
    sage: str(mathematica('Pi*x^2-1/2').N())
                    2
    -0.5 + 3.14159 x

Check that Mathematica's `E` exponential symbol is correctly backtranslated
as Sage's `e` (:issue:`29833`)::

    sage: x = var('x')
    sage: (e^x)._mathematica_().sage()  # optional -- mathematica
    e^x
    sage: exp(x)._mathematica_().sage() # optional -- mathematica
    e^x

Check that all trig/hyperbolic functions and their reciprocals are correctly
translated to Mathematica (:issue:`34087`)::

    sage: # optional - mathematica
    sage: x=var('x')
    sage: FL=[sin, cos, tan, csc, sec, cot,
    ....:     sinh, cosh, tanh, csch, sech, coth]
    sage: IFL=[arcsin, arccos, arctan, arccsc,
    ....:      arcsec, arccot, arcsinh, arccosh,
    ....:      arctanh, arccsch, arcsech, arccoth]
    sage: [mathematica.TrigToExp(u(x)).sage()
    ....:  for u in FL]
    [-1/2*I*e^(I*x) + 1/2*I*e^(-I*x),
     1/2*e^(I*x) + 1/2*e^(-I*x),
     (-I*e^(I*x) + I*e^(-I*x))/(e^(I*x) + e^(-I*x)),
     2*I/(e^(I*x) - e^(-I*x)),
     2/(e^(I*x) + e^(-I*x)),
     -(-I*e^(I*x) - I*e^(-I*x))/(e^(I*x) - e^(-I*x)),
     -1/2*e^(-x) + 1/2*e^x,
     1/2*e^(-x) + 1/2*e^x,
     -e^(-x)/(e^(-x) + e^x) + e^x/(e^(-x) + e^x),
     -2/(e^(-x) - e^x),
     2/(e^(-x) + e^x),
     -(e^(-x) + e^x)/(e^(-x) - e^x)]
    sage: [mathematica.TrigToExp(u(x)).sage()
    ....:  for u in IFL]
    [-I*log(I*x + sqrt(-x^2 + 1)),
     1/2*pi + I*log(I*x + sqrt(-x^2 + 1)),
     -1/2*I*log(I*x + 1) + 1/2*I*log(-I*x + 1),
     -I*log(sqrt(-1/x^2 + 1) + I/x),
     1/2*pi + I*log(sqrt(-1/x^2 + 1) + I/x),
     -1/2*I*log(I/x + 1) + 1/2*I*log(-I/x + 1),
     log(x + sqrt(x^2 + 1)),
     log(sqrt(x + 1)*sqrt(x - 1) + x),
     1/2*log(x + 1) - 1/2*log(-x + 1),
     log(sqrt(1/x^2 + 1) + 1/x),
     log(sqrt(1/x + 1)*sqrt(1/x - 1) + 1/x),
     1/2*log(1/x + 1) - 1/2*log(-1/x + 1)]
"""

from sage.interfaces.expect import Expect as Expect, ExpectElement as ExpectElement, ExpectFunction as ExpectFunction, FunctionElement as FunctionElement
from sage.interfaces.interface import AsciiArtString as AsciiArtString
from sage.interfaces.tab_completion import ExtraTabCompletion as ExtraTabCompletion
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.instancedoc import instancedoc as instancedoc
from sage.structure.richcmp import rich_to_bool as rich_to_bool

def clean_output(s: str) -> str: ...

class Mathematica(ExtraTabCompletion, Expect):
    """
    Interface to the Mathematica interpreter.
    """
    def __init__(self, maxread=None, script_subdirectory=None, logfile=None, server=None, server_tmpdir=None, command=None, verbose_start: bool = False) -> None:
        '''
        TESTS:

        Test that :issue:`28075` is fixed::

            sage: repr(mathematica.eval("Print[1]; Print[2]; Print[3]"))  # optional - mathematica
            \'1\\n2\\n3\'
        '''
    def eval(self, code, strip: bool = True, **kwds): ...
    def set(self, var, value) -> None:
        """
        Set the variable var to the given value.
        """
    def get(self, var, ascii_art: bool = False):
        """
        Get the value of the variable var.

        AUTHORS:

        - William Stein

        - Kiran Kedlaya (2006-02-04): suggested using InputForm
        """
    def chdir(self, dir) -> None:
        '''
        Change Mathematica\'s current working directory.

        EXAMPLES::

            sage: mathematica.chdir(\'/\')          # optional - mathematica
            sage: mathematica(\'Directory[]\')      # optional - mathematica
            "/"
        '''
    def console(self, readline: bool = True) -> None: ...
    def help(self, cmd): ...
    def __getattr__(self, attrname): ...

class MathematicaElement(ExpectElement):
    def __getitem__(self, n): ...
    def __getattr__(self, attrname): ...
    def __float__(self, precision: int = 16) -> float: ...
    def __reduce__(self): ...
    def __len__(self) -> int:
        """
        Return the object's length, evaluated by mathematica.

        EXAMPLES::

            sage: len(mathematica([1,1.,2]))    # optional - mathematica
            3

        AUTHORS:
        - Felix Lawrence (2009-08-21)
        """
    def save_image(self, filename, ImageSize: int = 600) -> None:
        """
        Save a mathematica graphics.

        INPUT:

        - ``filename`` -- string; the filename to save as. The
          extension determines the image file format

        - ``ImageSize`` -- integer; the size of the resulting image

        EXAMPLES::

            sage: P = mathematica('Plot[Sin[x],{x,-2Pi,4Pi}]')   # optional - mathematica
            sage: filename = tmp_filename()                      # optional - mathematica
            sage: P.save_image(filename, ImageSize=800)                # optional - mathematica
        """
    def show(self, ImageSize: int = 600) -> None:
        """
        Show a mathematica expression immediately.

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

            sage: Q = mathematica('Sin[x Cos[y]]/Sqrt[1-x^2]')   # optional - mathematica
            sage: show(Q)                                        # optional - mathematica
            Sin[x*Cos[y]]/Sqrt[1 - x^2]

        The following example starts a Mathematica frontend to do the rendering
        (:issue:`28819`)::

            sage: P = mathematica('Plot[Sin[x],{x,-2Pi,4Pi}]')   # optional - mathematica
            sage: show(P)                                        # optional - mathematica mathematicafrontend
            sage: P.show(ImageSize=800)                          # optional - mathematica mathematicafrontend
        """
    def str(self): ...
    def __bool__(self) -> bool:
        """
        Return whether this Mathematica element is not identical to ``False``.

        EXAMPLES::

            sage: bool(mathematica(True))  # optional - mathematica
            True
            sage: bool(mathematica(False))  # optional - mathematica
            False

        In Mathematica, `0` cannot be used to express falsity::

            sage: bool(mathematica(0))  # optional - mathematica
            True
        """
    def n(self, *args, **kwargs):
        """
        Numerical approximation by converting to Sage object first.

        Convert the object into a Sage object and return its numerical
        approximation. See documentation of the function
        :func:`sage.misc.functional.n` for details.

        EXAMPLES::

            sage: mathematica('Pi').n(10)    # optional -- mathematica
            3.1
            sage: mathematica('Pi').n()      # optional -- mathematica
            3.14159265358979
            sage: mathematica('Pi').n(digits=10)   # optional -- mathematica
            3.141592654
        """

class MathematicaFunction(ExpectFunction): ...
class MathematicaFunctionElement(FunctionElement): ...

mathematica: Mathematica

def reduce_load(X): ...
def mathematica_console(readline: bool = True) -> None: ...
def request_wolfram_alpha(input, verbose: bool = False):
    """
    Request Wolfram Alpha website.

    INPUT:

    - ``input`` -- string
    - ``verbose`` -- boolean (default: ``False``)

    OUTPUT: json

    EXAMPLES::

        sage: from sage.interfaces.mathematica import request_wolfram_alpha
        sage: page_data = request_wolfram_alpha('integrate Sin[x]')      # optional internet
        sage: [str(a) for a in sorted(page_data.keys())]                 # optional internet
        ['queryresult']
        sage: [str(a) for a in sorted(page_data['queryresult'].keys())]  # optional internet
        ['datatypes',
         'encryptedEvaluatedExpression',
         'encryptedParsedExpression',
         'error',
         'host',
         'id',
         'inputstring',
         'numpods',
         'parsetimedout',
         'parsetiming',
         'pods',
         'recalculate',
         'related',
         'server',
         'sponsorCategories',
         'success',
         'timedout',
         'timedoutpods',
         'timing',
         'version']
    """
def parse_moutput_from_json(page_data, verbose: bool = False):
    """
    Return the list of outputs found in the json (with key ``'moutput'``).

    INPUT:

    - ``page_data`` -- json obtained from Wolfram Alpha
    - ``verbose`` -- boolean (default: ``False``)

    OUTPUT: list of unicode strings

    EXAMPLES::

        sage: from sage.interfaces.mathematica import request_wolfram_alpha
        sage: from sage.interfaces.mathematica import parse_moutput_from_json
        sage: page_data = request_wolfram_alpha('integrate Sin[x]') # optional internet
        sage: parse_moutput_from_json(page_data)                    # optional internet
        ['-Cos[x]']

    ::

        sage: page_data = request_wolfram_alpha('Sin[x]')           # optional internet
        sage: L = parse_moutput_from_json(page_data)                # optional internet
        sage: sorted(L)                                             # optional internet
        ['-Cos[x]', '{x == 0}', '{x == Pi C[1], Element[C[1], Integers]}']

    TESTS::

        sage: page_data = request_wolfram_alpha('Integrate(Sin[z], y)')  # optional internet
        sage: parse_moutput_from_json(page_data)                         # optional internet
        Traceback (most recent call last):
        ...
        ValueError: asking wolframalpha.com was not successful
    """
def symbolic_expression_from_mathematica_string(mexpr):
    """
    Translate a mathematica string into a symbolic expression.

    INPUT:

    - ``mexpr`` -- string

    OUTPUT: symbolic expression

    EXAMPLES::

        sage: from sage.interfaces.mathematica import symbolic_expression_from_mathematica_string
        sage: symbolic_expression_from_mathematica_string('-Cos[x]')
        -cos(x)
    """
